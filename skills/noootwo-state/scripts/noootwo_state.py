#!/usr/bin/env python3

from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import uuid
from collections import deque
from datetime import datetime, timezone
from pathlib import Path


PROTOCOL_STATE = "noootwo.state/0.1"
PROTOCOL_EVENT = "noootwo.state-event/0.1"
PROTOCOL_CAPSULE = "noootwo.context-capsule/0.1"
STATE_SCHEMA_VERSION = 1
DEFAULT_CAPSULE_MAX_CHARS = 6000
DEFAULT_CAPSULE_LINES = 80
DEFAULT_INSPECT_LINES = 80
DEFAULT_CAPTURE_LINES = 40
STATE_ENUM = {
    "stage": {
        "routing",
        "blocked",
        "building",
        "evaluating",
        "accepting",
        "done",
        "abandoned",
    },
    "waiting_on": {"none", "user", "caller", "external"},
}
EVENT_TYPES = {
    "state.created",
    "state.updated",
    "state.read",
    "event.appended",
    "format.selected",
    "decision.recorded",
    "spec.recorded",
    "plan.recorded",
    "narrative.recorded",
    "release.recorded",
    "evidence.recorded",
    "procedure.recorded",
    "blocker.opened",
    "blocker.resolved",
    "waiting",
    "acceptance.requested",
    "acceptance.received",
    "completed",
    "abandoned",
}
REQUEST_REQUIRED = {"request_id", "fact_type", "query_profile", "mutability", "lifespan", "content"}
FACT_TYPES = {"state", "event", "decision", "spec", "plan", "narrative", "release", "evidence", "procedure"}
QUERY_PROFILES = {"field", "tail", "search", "human"}
MUTABILITIES = {"current", "append-only", "immutable"}
LIFESPANS = {"hot", "durable", "cold"}
HASH_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
ISO_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")
SAFE_REQUEST_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def state_dir(root: Path) -> Path:
    return root / ".noootwo" / "state"


def state_file(root: Path) -> Path:
    return state_dir(root) / "current.json"


def events_file(root: Path) -> Path:
    return state_dir(root) / "events.jsonl"


def atomic_write(path: Path, text: str) -> None:
    atomic_write_bytes(path, text.encode("utf-8"))


def atomic_write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=path.name + ".", dir=str(path.parent))
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def canonical(data: object) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_text(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_bytes(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def state_hash(data: dict) -> str:
    payload = {key: value for key, value in data.items() if key != "state_hash"}
    return sha256_text(canonical(payload))


def read_json(path: Path) -> dict:
    if not path.is_file():
        raise SystemExit(f"missing {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise SystemExit(f"invalid JSON in {path}: {exc}") from exc


def read_events(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    events: list[dict] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            events.append(json.loads(line))
        except Exception as exc:
            raise SystemExit(f"invalid event line {number} in {path}: {exc}") from exc
    return events


def read_recent_events(path: Path, limit: int) -> list[dict]:
    if limit <= 0 or not path.is_file():
        return []
    recent: deque[str] = deque(maxlen=limit)
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                recent.append(line)
    events: list[dict] = []
    for number, line in enumerate(recent, 1):
        try:
            events.append(json.loads(line))
        except Exception as exc:
            raise SystemExit(f"invalid recent event line {number} in {path}: {exc}") from exc
    return events


def display_path(root: Path, path: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(path)


def clip_text(value: object, limit: int = 600) -> str:
    if isinstance(value, str):
        text = value
    else:
        text = canonical(value)
    if len(text) <= limit:
        return text
    return text[: max(0, limit - 3)] + "..."


def default_state(work_id: str, session_id: str, attempt_id: str, goal: str) -> dict:
    data: dict = {
        "protocol": PROTOCOL_STATE,
        "schema_version": STATE_SCHEMA_VERSION,
        "work_id": work_id,
        "session_id": session_id,
        "attempt_id": attempt_id,
        "updated_at": utc_now(),
        "stage": "routing",
        "waiting_on": "none",
        "goal": goal,
        "settled": [],
        "unsettled": [],
        "open_blockers": [],
        "last_owner": "",
        "last_result": "",
        "next_trigger": "",
        "last_event_id": "",
        "state_hash": "",
        "artifact_hashes": [],
        "entries": {},
    }
    data["state_hash"] = state_hash(data)
    return data


def validate_state(data: dict, path: Path) -> None:
    if data.get("protocol") != PROTOCOL_STATE:
        raise SystemExit(f"{path}: unknown or missing protocol")
    version = data.get("schema_version")
    if not isinstance(version, int) or version != STATE_SCHEMA_VERSION:
        raise SystemExit(f"{path}: unsupported schema_version {version!r}")
    required = {
        "work_id",
        "session_id",
        "attempt_id",
        "updated_at",
        "stage",
        "waiting_on",
        "goal",
        "settled",
        "unsettled",
        "open_blockers",
        "last_owner",
        "last_result",
        "next_trigger",
        "last_event_id",
        "state_hash",
        "artifact_hashes",
        "entries",
    }
    missing = sorted(required - set(data))
    if missing:
        raise SystemExit(f"{path}: missing fields: {', '.join(missing)}")
    if data["stage"] not in STATE_ENUM["stage"]:
        raise SystemExit(f"{path}: invalid stage {data['stage']!r}")
    if data["waiting_on"] not in STATE_ENUM["waiting_on"]:
        raise SystemExit(f"{path}: invalid waiting_on {data['waiting_on']!r}")
    if not HASH_RE.match(data["state_hash"]):
        raise SystemExit(f"{path}: invalid state_hash")
    if data["state_hash"] != state_hash(data):
        raise SystemExit(f"{path}: state_hash mismatch")
    if not isinstance(data["open_blockers"], list):
        raise SystemExit(f"{path}: open_blockers must be an array")
    for blocker in data["open_blockers"]:
        if not {"id", "message", "status", "opened_at"} <= set(blocker):
            raise SystemExit(f"{path}: blocker missing required fields")
        if blocker["status"] not in {"open", "resolved"}:
            raise SystemExit(f"{path}: invalid blocker status")
    if not isinstance(data["entries"], dict):
        raise SystemExit(f"{path}: entries must be an object")


def validate_event(event: dict, index: int) -> None:
    if event.get("protocol") != PROTOCOL_EVENT:
        raise SystemExit(f"event {index}: unknown or missing protocol")
    if event.get("event_type") not in EVENT_TYPES:
        raise SystemExit(f"event {index}: invalid event_type {event.get('event_type')!r}")
    required = {
        "event_id",
        "event_type",
        "occurred_at",
        "domain",
        "work_id",
        "session_id",
        "attempt_id",
        "actor",
        "basis",
        "payload",
        "idempotency_key",
    }
    missing = sorted(required - set(event))
    if missing:
        raise SystemExit(f"event {index}: missing fields: {', '.join(missing)}")
    if not ISO_RE.match(event["occurred_at"]):
        raise SystemExit(f"event {index}: invalid occurred_at")
    actor = event["actor"]
    if actor.get("kind") not in {"user", "caller", "harness"} or not actor.get("name"):
        raise SystemExit(f"event {index}: invalid actor")
    if not event.get("idempotency_key"):
        raise SystemExit(f"event {index}: missing idempotency_key")


def new_event(state: dict, event_type: str, domain: str, payload: dict, actor_kind: str, actor_name: str) -> dict:
    key = f"{state['work_id']}:{event_type}:{domain}:{utc_now()}:{uuid.uuid4().hex}"
    return {
        "protocol": PROTOCOL_EVENT,
        "event_id": "evt_" + uuid.uuid4().hex,
        "event_type": event_type,
        "occurred_at": utc_now(),
        "domain": domain,
        "work_id": state["work_id"],
        "session_id": state["session_id"],
        "attempt_id": state["attempt_id"],
        "actor": {"kind": actor_kind, "name": actor_name},
        "basis": {"state_hash": state["state_hash"]},
        "payload": payload,
        "idempotency_key": key,
    }


def append_event(root: Path, state: dict, event: dict) -> None:
    path = events_file(root)
    existing = read_events(path)
    keys = {item.get("idempotency_key") for item in existing}
    if event["idempotency_key"] in keys:
        raise SystemExit("duplicate idempotency_key")
    atomic_write(path, "\n".join(canonical(item) for item in existing + [event]) + "\n")
    state["last_event_id"] = event["event_id"]


def save_state(root: Path, state: dict) -> None:
    state["updated_at"] = utc_now()
    state["state_hash"] = state_hash(state)
    atomic_write(state_file(root), json.dumps(state, indent=2, ensure_ascii=False) + "\n")


def init_command(root: Path, args: argparse.Namespace) -> None:
    path = state_file(root)
    if path.is_file() and not args.force:
        raise SystemExit(f"{path} already exists; pass --force to replace")
    state = default_state(args.work_id, args.session_id, args.attempt_id, args.goal)
    save_state(root, state)
    event = new_event(state, "state.created", "state", {"goal": args.goal}, "harness", "noootwo-state")
    append_event(root, state, event)
    save_state(root, state)
    print(path)


def set_command(root: Path, args: argparse.Namespace) -> None:
    state = read_json(state_file(root))
    changed: dict[str, object] = {}
    settled_added: list[str] = []
    unsettled_added: list[str] = []

    def set_changed(key: str, value: object) -> None:
        if state[key] == value:
            return
        state[key] = value
        changed[key] = clip_text(value, 600)

    if args.stage is not None:
        set_changed("stage", args.stage)
    if args.goal is not None:
        set_changed("goal", args.goal)
    if args.waiting is not None:
        set_changed("waiting_on", args.waiting)
    if args.last_owner is not None:
        set_changed("last_owner", args.last_owner)
    if args.last_result is not None:
        set_changed("last_result", args.last_result)
    if args.next_trigger is not None:
        set_changed("next_trigger", args.next_trigger)
    for value in args.settled or []:
        if value not in state["settled"]:
            state["settled"].append(value)
            settled_added.append(value)
    for value in args.unsettled or []:
        if value not in state["unsettled"]:
            state["unsettled"].append(value)
            unsettled_added.append(value)
    if not changed and not settled_added and not unsettled_added:
        return
    payload: dict[str, object] = {"changed": changed}
    if settled_added:
        payload["settled_added"] = [clip_text(value) for value in settled_added]
    if unsettled_added:
        payload["unsettled_added"] = [clip_text(value) for value in unsettled_added]
    event = new_event(state, "state.updated", "state", payload, "harness", "noootwo-state")
    append_event(root, state, event)
    save_state(root, state)


def sync_blocker(state: dict, event: dict) -> None:
    payload = event.get("payload")
    if not isinstance(payload, dict):
        return
    blocker = payload.get("blocker")
    if event["event_type"] == "blocker.opened":
        if not isinstance(blocker, dict) or not blocker.get("id") or not blocker.get("message"):
            raise SystemExit("blocker.opened requires payload.blocker with id and message")
        record = {
            "id": str(blocker["id"]),
            "message": str(blocker["message"]),
            "status": "open",
            "opened_at": str(blocker.get("opened_at") or event["occurred_at"]),
        }
        state["open_blockers"] = [
            item for item in state["open_blockers"] if item.get("id") != record["id"]
        ] + [record]
    elif event["event_type"] == "blocker.resolved":
        if not isinstance(blocker, dict) or not blocker.get("id"):
            raise SystemExit("blocker.resolved requires payload.blocker.id")
        blocker_id = str(blocker["id"])
        found = False
        for item in state["open_blockers"]:
            if item.get("id") == blocker_id:
                item["status"] = "resolved"
                found = True
        if not found:
            raise SystemExit(f"unknown blocker: {blocker_id}")


def log_command(root: Path, args: argparse.Namespace) -> None:
    state = read_json(state_file(root))
    payload = json.loads(args.payload) if args.payload else {}
    if args.request_id:
        payload["request_id"] = args.request_id
    event = new_event(state, args.type, args.domain, payload, args.actor_kind, args.actor_name)
    sync_blocker(state, event)
    append_event(root, state, event)
    save_state(root, state)


def check_command(root: Path, args: argparse.Namespace) -> None:
    state = read_json(state_file(root))
    validate_state(state, state_file(root))
    events = read_events(events_file(root))
    for index, event in enumerate(events, 1):
        validate_event(event, index)
    keys = [event.get("idempotency_key") for event in events]
    if len(keys) != len(set(keys)):
        raise SystemExit("duplicate idempotency_key in event log")
    if state["last_event_id"] and events and state["last_event_id"] != events[-1]["event_id"]:
        raise SystemExit("last_event_id does not match final event")
    print(f"ok: {len(events)} events")


def render_command(root: Path, args: argparse.Namespace) -> None:
    state = read_json(state_file(root))
    lines = [
        "# State Summary",
        "",
        f"- Stage: {state['stage']}",
        f"- Waiting on: {state['waiting_on']}",
        f"- Goal: {state['goal']}",
        f"- Last owner: {state['last_owner'] or '-'}",
        f"- Next trigger: {state['next_trigger'] or '-'}",
    ]
    events = read_events(events_file(root))[-20:]
    lines.extend(["", "## Recent events", ""])
    for event in events:
        lines.append(f"- {event['event_type']} ({event['occurred_at']})")
    atomic_write(state_dir(root) / "summary.md", "\n".join(lines) + "\n")
    print(state_dir(root) / "summary.md")


def evidence_handles(events: list[dict], limit: int = 5) -> list[dict]:
    handles: list[dict] = []
    for event in reversed(events):
        if event.get("event_type") != "evidence.recorded":
            continue
        payload = event.get("payload")
        if not isinstance(payload, dict):
            payload = {}
        handle = {
            "event_id": event.get("event_id"),
            "occurred_at": event.get("occurred_at"),
            "request_id": clip_text(payload.get("request_id", ""), 160),
            "destination": clip_text(payload.get("destination", ""), 300),
            "source": clip_text(payload.get("source", ""), 300),
            "command": clip_text(payload.get("command", ""), 300),
            "exit_code": payload.get("exit_code"),
            "bytes": payload.get("bytes"),
            "commit": clip_text(payload.get("commit", ""), 80),
            "sha256": clip_text(payload.get("sha256", ""), 100),
            "summary": clip_text(payload.get("summary", ""), 300),
        }
        handles.append({key: value for key, value in handle.items() if value not in ("", None)})
        if len(handles) >= limit:
            break
    return handles


def build_capsule(root: Path, recent: int = 5) -> dict:
    state = read_json(state_file(root))
    validate_state(state, state_file(root))
    events = read_recent_events(events_file(root), max(50, recent * 8))
    recent_events = []
    for event in events[-recent:]:
        payload = event.get("payload") if isinstance(event.get("payload"), dict) else {}
        changed = payload.get("changed") if isinstance(payload.get("changed"), dict) else {}
        recent_events.append({
            "event_id": event.get("event_id"),
            "event_type": event.get("event_type"),
            "occurred_at": event.get("occurred_at"),
            "changed_keys": sorted(changed),
        })
    current = {
        "goal": clip_text(state["goal"], 600),
        "stage": state["stage"],
        "waiting_on": state["waiting_on"],
        "last_owner": clip_text(state["last_owner"], 200),
        "last_result": clip_text(state["last_result"], 600),
        "next_trigger": clip_text(state["next_trigger"], 600),
    }
    blockers = []
    for blocker in state["open_blockers"]:
        blockers.append({
            "id": clip_text(blocker.get("id", ""), 80),
            "message": clip_text(blocker.get("message", ""), 300),
            "status": blocker.get("status", "open"),
            "opened_at": blocker.get("opened_at", ""),
        })
    return {
        "protocol": PROTOCOL_CAPSULE,
        "generated_at": utc_now(),
        "source": {
            "current": display_path(root, state_file(root)),
            "events": display_path(root, events_file(root)),
            "state_hash": state["state_hash"],
            "last_event_id": state["last_event_id"],
        },
        "current": current,
        "settled": [clip_text(value, 400) for value in state["settled"]],
        "unsettled": [clip_text(value, 400) for value in state["unsettled"]],
        "open_blockers": blockers,
        "evidence_handles": evidence_handles(events, recent),
        "recent_events": recent_events,
        "truncated": False,
    }


def fit_capsule_json(
    capsule: dict,
    max_chars: int,
    max_lines: int = DEFAULT_CAPSULE_LINES,
) -> str:
    working = json.loads(json.dumps(capsule, ensure_ascii=False))

    def fit_current_shape() -> str | None:
        pretty = json.dumps(working, indent=2, ensure_ascii=False) + "\n"
        if len(pretty) <= max_chars and len(pretty.splitlines()) <= max_lines:
            return pretty
        compact = json.dumps(working, separators=(",", ":"), ensure_ascii=False) + "\n"
        if len(compact) <= max_chars:
            return compact
        return None

    fitted = fit_current_shape()
    if fitted:
        return fitted

    working["truncated"] = True
    for key in ("settled", "unsettled"):
        working[key] = [clip_text(value, 240) for value in working[key][-10:]]
    working["open_blockers"] = working["open_blockers"][-6:]
    working["evidence_handles"] = working["evidence_handles"][:4]
    working["recent_events"] = working["recent_events"][-4:]
    fitted = fit_current_shape()
    if fitted:
        return fitted

    working["current"] = {
        key: clip_text(value, 160) for key, value in working["current"].items()
    }
    working["source"]["current"] = clip_text(working["source"]["current"], 240)
    working["source"]["events"] = clip_text(working["source"]["events"], 240)
    working["settled"] = [clip_text(value, 120) for value in working["settled"][-5:]]
    working["unsettled"] = [clip_text(value, 120) for value in working["unsettled"][-5:]]
    working["evidence_handles"] = [
        {key: clip_text(value, 120) for key, value in item.items()}
        for item in working["evidence_handles"][:2]
    ]
    working["recent_events"] = working["recent_events"][-2:]
    fitted = fit_current_shape()
    if fitted:
        return fitted

    working["settled"] = working["settled"][-2:]
    working["unsettled"] = working["unsettled"][-2:]
    working["open_blockers"] = working["open_blockers"][-2:]
    working["evidence_handles"] = working["evidence_handles"][:1]
    working["recent_events"] = working["recent_events"][-1:]
    working["current"] = {
        key: clip_text(value, 60) for key, value in working["current"].items()
    }
    for key in ("settled", "unsettled"):
        working[key] = [clip_text(value, 60) for value in working[key]]
    for value in working["open_blockers"]:
        value["message"] = clip_text(value.get("message", ""), 80)
    for value in working["evidence_handles"]:
        for key, item in list(value.items()):
            value[key] = clip_text(item, 80)
    fitted = fit_current_shape()
    if fitted:
        return fitted
    raise SystemExit(f"capsule cannot fit in {max_chars} characters and {max_lines} lines")


def render_capsule(capsule: dict) -> str:
    current = capsule["current"]
    lines = [
        "# Context Capsule",
        "",
        f"- Protocol: {capsule['protocol']}",
        f"- Source: {capsule['source']['current']}",
        f"- State hash: {capsule['source']['state_hash']}",
        f"- Last event: {capsule['source']['last_event_id'] or '-'}",
        "",
        "## Current",
        f"- Goal: {current['goal'] or '-'}",
        f"- Stage: {current['stage']}",
        f"- Waiting on: {current['waiting_on']}",
        f"- Last owner: {current['last_owner'] or '-'}",
        f"- Last result: {current['last_result'] or '-'}",
        f"- Next trigger: {current['next_trigger'] or '-'}",
    ]

    def add_list(title: str, values: list[object], formatter) -> None:
        lines.extend(["", f"## {title}"])
        if not values:
            lines.append("- none")
            return
        lines.extend(f"- {formatter(value)}" for value in values)

    add_list("Settled", capsule["settled"], lambda value: str(value))
    add_list("Unsettled", capsule["unsettled"], lambda value: str(value))
    add_list(
        "Open blockers",
        capsule["open_blockers"],
        lambda value: f"{value.get('id', '-')} [{value.get('status', 'open')}] {value.get('message', '')}",
    )
    add_list(
        "Evidence handles",
        capsule["evidence_handles"],
        lambda value: " | ".join(
            f"{key}={item}"
            for key, item in value.items()
            if key not in {"event_id", "occurred_at"} and item
        ) or value.get("event_id", "-"),
    )
    add_list(
        "Recent events",
        capsule["recent_events"],
        lambda value: (
            f"{value.get('event_type')} {value.get('occurred_at')} "
            f"changed={','.join(value.get('changed_keys', [])) or '-'}"
        ),
    )
    return "\n".join(lines) + "\n"


def cap_rendered_text(text: str, max_chars: int, max_lines: int) -> str:
    lines = text.splitlines()
    truncated = len(lines) > max_lines
    if truncated:
        lines = lines[: max_lines - 1] + ["... [truncated]"]
    text = "\n".join(lines) + "\n"
    if len(text) > max_chars:
        notice = "\n... [truncated]\n"
        text = text[: max(0, max_chars - len(notice))].rstrip() + notice
    return text


def capsule_command(root: Path, args: argparse.Namespace) -> None:
    if args.max_chars < 2000:
        raise SystemExit("--max-chars must be at least 2000")
    capsule = build_capsule(root, recent=max(1, args.last))
    if args.json_output:
        sys.stdout.write(fit_capsule_json(capsule, args.max_chars))
    else:
        sys.stdout.write(cap_rendered_text(render_capsule(capsule), args.max_chars, DEFAULT_CAPSULE_LINES))


def inspect_data(root: Path, relative: str, query: str | None, max_lines: int) -> dict:
    path = Path(relative)
    if not path.is_absolute():
        path = root / path
    path = path.resolve()
    if not path.is_file():
        raise SystemExit(f"not a file: {path}")
    raw = path.read_bytes()
    if b"\x00" in raw:
        text = ""
        text_lines = []
        binary = True
    else:
        try:
            text = raw.decode("utf-8")
            text_lines = text.splitlines()
            binary = False
        except UnicodeDecodeError:
            text = ""
            text_lines = []
            binary = True
    headings = [
        {"line": index, "text": clip_text(line, 200)}
        for index, line in enumerate(text_lines, 1)
        if re.match(r"^#{1,6}\s+", line)
    ][:40]
    title = None
    if headings:
        title = re.sub(r"^#{1,6}\s+", "", headings[0]["text"])
    elif text_lines:
        title = next((clip_text(line, 200) for line in text_lines if line.strip()), None)
    excerpt: list[dict] = []
    if not binary:
        if query:
            needle = query.casefold()
            matching = [
                index
                for index, line in enumerate(text_lines, 1)
                if needle in line.casefold()
            ]
            for index in matching[:max_lines]:
                excerpt.append({"line": index, "text": clip_text(text_lines[index - 1], 400)})
            truncated = len(matching) > max_lines
        elif len(text_lines) <= max_lines:
            excerpt = [
                {"line": index, "text": clip_text(line, 400)}
                for index, line in enumerate(text_lines, 1)
            ]
            truncated = False
        else:
            excerpt = [
                {"line": index, "text": clip_text(line, 400)}
                for index, line in enumerate(text_lines[: min(20, max_lines)], 1)
            ]
            truncated = True
    else:
        truncated = True
    return {
        "protocol": "noootwo.file-inspect/0.1",
        "path": display_path(root, path),
        "bytes": len(raw),
        "lines": len(text_lines),
        "sha256": sha256_bytes(raw),
        "binary": binary,
        "title": title,
        "query": query,
        "headings": headings,
        "excerpt": excerpt,
        "truncated": truncated,
    }


def inspect_command(root: Path, args: argparse.Namespace) -> None:
    if not 1 <= args.max_lines <= DEFAULT_INSPECT_LINES:
        raise SystemExit(
            f"--max-lines must be between 1 and {DEFAULT_INSPECT_LINES}"
        )
    data = inspect_data(root, args.path, args.query, args.max_lines)
    if args.json_output:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return
    print(f"path: {data['path']}")
    print(f"bytes: {data['bytes']}")
    print(f"lines: {data['lines']}")
    print(f"sha256: {data['sha256']}")
    print(f"binary: {'yes' if data['binary'] else 'no'}")
    print(f"title: {data['title'] or '-'}")
    if data["headings"]:
        print("headings:")
        for heading in data["headings"]:
            print(f"  {heading['line']}: {heading['text']}")
    if data["excerpt"]:
        print("excerpt:")
        for line in data["excerpt"]:
            print(f"  {line['line']}: {line['text']}")
    elif not data["binary"]:
        print("excerpt: no matches" if args.query else "excerpt: none")
    if data["truncated"]:
        print("truncated: yes")


def bounded_tail(text: str, max_lines: int, max_chars: int = 6000) -> str:
    lines = text.splitlines()
    if len(lines) > max_lines:
        if max_lines > 1:
            lines = ["... earlier output omitted ..."] + lines[-(max_lines - 1) :]
        else:
            lines = lines[-1:]
    result = "\n".join(lines)
    if len(result) > max_chars:
        notice = "... earlier output omitted ...\n" if max_lines > 1 else ""
        result = notice + result[-max(0, max_chars - len(notice)) :]
    return result


def read_tail_text(path: Path, max_bytes: int = 64 * 1024) -> str:
    size = path.stat().st_size
    if size == 0:
        return ""
    with path.open("rb") as handle:
        offset = max(0, size - max_bytes)
        handle.seek(offset)
        data = handle.read()
    if offset:
        newline = data.find(b"\n")
        if newline >= 0:
            data = data[newline + 1 :]
    return data.decode("utf-8", errors="replace")


def capture_command(root: Path, args: argparse.Namespace) -> None:
    command_parts = getattr(args, "capture_argv", [])
    if not SAFE_REQUEST_ID_RE.match(args.name):
        raise SystemExit("--name must be a safe file name")
    if not command_parts:
        raise SystemExit("capture requires a command after --")
    evidence_dir = state_dir(root) / "evidence"
    log_path = evidence_dir / f"{args.name}.log"
    meta_path = evidence_dir / f"{args.name}.json"
    if log_path.exists() or meta_path.exists():
        raise SystemExit(f"capture already exists: {display_path(root, log_path)}")
    evidence_dir.mkdir(parents=True, exist_ok=True)
    started_at = utc_now()
    temp_fd, temp_name = tempfile.mkstemp(
        prefix=f".{args.name}.",
        suffix=".tmp",
        dir=str(evidence_dir),
    )
    temp_path = Path(temp_name)
    try:
        with os.fdopen(temp_fd, "wb") as output_handle:
            completed = subprocess.run(
                command_parts,
                cwd=root,
                stdin=subprocess.DEVNULL,
                stdout=output_handle,
                stderr=subprocess.STDOUT,
                check=False,
            )
    except OSError as exc:
        if temp_path.exists():
            temp_path.unlink()
        raise SystemExit(f"capture failed to start: {exc}") from exc
    finished_at = utc_now()
    try:
        output_bytes_count = temp_path.stat().st_size
        digest = sha256_file(temp_path)
        os.replace(temp_path, log_path)
    except OSError as exc:
        if temp_path.exists():
            temp_path.unlink()
        raise SystemExit(f"capture failed to store output: {exc}") from exc
    metadata = {
        "protocol": "noootwo.capture/0.1",
        "name": args.name,
        "command": command_parts,
        "cwd": str(root),
        "started_at": started_at,
        "finished_at": finished_at,
        "exit_code": completed.returncode,
        "bytes": output_bytes_count,
        "sha256": digest,
        "log": display_path(root, log_path),
    }
    atomic_write(meta_path, json.dumps(metadata, indent=2, ensure_ascii=False) + "\n")
    print(f"capture: {display_path(root, log_path)}")
    print(f"metadata: {display_path(root, meta_path)}")
    print(f"exit_code: {completed.returncode}")
    print(f"bytes: {output_bytes_count}")
    print(f"sha256: {metadata['sha256']}")
    if output_bytes_count:
        print("last_lines:")
        print(bounded_tail(read_tail_text(log_path), args.max_lines))
    else:
        print("last_lines: (no output)")


def choose_form(request: dict) -> str:
    fact_type = request.get("fact_type")
    query_profile = request.get("query_profile")
    mutability = request.get("mutability")
    lifespan = request.get("lifespan")
    if mutability == "append-only" or fact_type == "event":
        return "event"
    if fact_type == "evidence" or (lifespan == "cold" and query_profile == "search"):
        return "cold"
    if fact_type in {"decision", "spec", "plan", "narrative", "release", "procedure"} or query_profile == "human":
        return "markdown"
    return "state"


def validate_request(request: dict) -> None:
    missing = sorted(REQUEST_REQUIRED - set(request))
    if missing:
        raise SystemExit(f"request missing fields: {', '.join(missing)}")
    if request["fact_type"] not in FACT_TYPES:
        raise SystemExit("invalid fact_type")
    if request["query_profile"] not in QUERY_PROFILES:
        raise SystemExit("invalid query_profile")
    if request["mutability"] not in MUTABILITIES:
        raise SystemExit("invalid mutability")
    if request["lifespan"] not in LIFESPANS:
        raise SystemExit("invalid lifespan")


def resolve_destination(root: Path, destination: Path | None) -> Path | None:
    if destination is None:
        return None
    return destination if destination.is_absolute() else root / destination


def default_markdown_destination(root: Path, request: dict) -> Path:
    fact_type = request["fact_type"]
    if fact_type in {"spec", "plan"}:
        request_id = request["request_id"]
        if not SAFE_REQUEST_ID_RE.match(request_id):
            raise SystemExit("spec and plan request_id must be a safe file name when --destination is omitted")
        directory = "specs" if fact_type == "spec" else "plans"
        return root / "docs" / directory / f"{request_id}.md"
    return state_dir(root) / "records" / f"{request['request_id']}.md"


def apply_request(root: Path, request: dict, destination: Path | None = None, source: str | None = None) -> str:
    replaces = request.get("replaces") or []
    if isinstance(replaces, str):
        replaces = [replaces]
    if not isinstance(replaces, list):
        raise SystemExit("replaces must be a pointer, list of pointers, or omitted")

    state = read_json(state_file(root))
    form = choose_form(request)
    payload: dict[str, object] = {
        "request_id": request["request_id"],
        "replaces": replaces,
    }
    if form == "event":
        event_type = "event.appended"
        content_hash = sha256_text(canonical(request["content"]))
        payload.update({
            "content": request["content"],
            "changed": {"event_content_sha256": content_hash},
        })
    elif form == "state":
        request_id = request["request_id"]
        removed = [old for old in replaces if old in state["entries"]]
        unchanged = state["entries"].get(request_id) == request["content"]
        if unchanged and not removed:
            return ""
        for old in replaces:
            state["entries"].pop(old, None)
        state["entries"][request_id] = request["content"]
        event_type = "state.updated"
        changed: dict[str, object] = {
            "entries": {
                "set": [request_id],
                "sha256": sha256_text(canonical(request["content"])),
            }
        }
        if removed:
            changed["entries_removed"] = removed
        payload["changed"] = changed
    elif form == "cold":
        if isinstance(request["content"], str):
            destination = resolve_destination(root, destination) or state_dir(root) / "evidence" / f"{request['request_id']}.md"
            content = request["content"]
        else:
            destination = resolve_destination(root, destination) or state_dir(root) / "evidence" / f"{request['request_id']}.json"
            content = json.dumps(request["content"], indent=2, ensure_ascii=False)
        data = (content if content.endswith("\n") else content + "\n").encode("utf-8")
        atomic_write_bytes(destination, data)
        event_type = "evidence.recorded"
        payload.update({
            "destination": display_path(root, destination),
            "bytes": len(data),
            "sha256": sha256_bytes(data),
            "changed": {"evidence": display_path(root, destination)},
        })
    else:
        destination = resolve_destination(root, destination) or default_markdown_destination(root, request)
        content = request["content"]
        if not isinstance(content, str):
            content = json.dumps(content, indent=2, ensure_ascii=False)
        data = (content if content.endswith("\n") else content + "\n").encode("utf-8")
        atomic_write_bytes(destination, data)
        event_type = f"{request['fact_type']}.recorded"
        payload.update({
            "destination": display_path(root, destination),
            "bytes": len(data),
            "sha256": sha256_bytes(data),
            "changed": {"record": display_path(root, destination)},
        })

    if source:
        payload["source"] = source
    elif isinstance(request.get("source"), str) and request["source"]:
        payload["source"] = request["source"]
    if request.get("summary"):
        payload["summary"] = clip_text(request["summary"])
    for field in ("command", "exit_code", "url", "commit", "input_ref", "source_role"):
        if field in request and request[field] not in (None, "", [], {}):
            payload[field] = request[field]

    event = new_event(state, event_type, request.get("domain", "state"), payload, "caller", request.get("owner_skill", "caller"))
    append_event(root, state, event)
    save_state(root, state)
    return event["event_id"]


def request_command(root: Path, args: argparse.Namespace) -> None:
    if args.json_request:
        request = json.loads(args.json_request)
    elif args.request_file:
        request = json.loads(Path(args.request_file).read_text(encoding="utf-8"))
    else:
        raise SystemExit("request requires --json-request or --request-file")
    validate_request(request)
    event_id = apply_request(root, request, destination=Path(args.destination) if args.destination else None)
    if event_id:
        print(event_id)


def migrate_command(root: Path, args: argparse.Namespace) -> None:
    manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    if manifest.get("protocol") != "noootwo.migrate/0.1":
        raise SystemExit("unsupported migration protocol")
    entries = manifest.get("entries")
    if not isinstance(entries, list) or not entries:
        raise SystemExit("migration manifest must contain a non-empty entries array")
    for entry in entries:
        missing = sorted({"path", "request_id", "fact_type", "query_profile", "mutability", "lifespan"} - set(entry))
        if missing:
            raise SystemExit(f"migration entry missing fields: {', '.join(missing)}")
        source = Path(entry["path"])
        if source.is_absolute():
            raise SystemExit(f"migration path must be relative: {source}")
        full = root / source
        if not full.is_file():
            raise SystemExit(f"migration source not found: {source}")
        request = {
            "request_id": entry["request_id"],
            "fact_type": entry["fact_type"],
            "query_profile": entry["query_profile"],
            "mutability": entry["mutability"],
            "lifespan": entry["lifespan"],
            "content": full.read_text(encoding="utf-8"),
            "owner_skill": entry.get("owner_skill", "migrate"),
            "domain": entry.get("domain", "state"),
            "replaces": [str(source)],
        }
        validate_request(request)
        destination = Path(entry["destination"]) if entry.get("destination") else None
        apply_request(root, request, destination=destination, source=str(source))
        if getattr(args, "keep", False):
            print(f"migrated {source}")
        else:
            legacy = state_dir(root) / "legacy" / source
            legacy.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(full), str(legacy))
            print(f"migrated {source} -> {legacy}")


def self_test() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        init_command(root, argparse.Namespace(force=False, work_id="w_self", session_id="s_self", attempt_id="a_self", goal="self test"))
        set_command(root, argparse.Namespace(stage="building", goal=None, waiting=None, last_owner="caller", last_result="ok", next_trigger="verify", settled=["one"], unsettled=[]))
        events = read_events(events_file(root))
        if events[-1]["payload"].get("changed", {}).get("stage") != "building":
            raise SystemExit("state.updated did not preserve changed fields")
        event_count = len(events)
        set_command(root, argparse.Namespace(stage="building", goal=None, waiting=None, last_owner=None, last_result=None, next_trigger=None, settled=[], unsettled=[]))
        if len(read_events(events_file(root))) != event_count:
            raise SystemExit("no-op state update created an event")
        state_request = {
            "request_id": "entry_1",
            "fact_type": "state",
            "query_profile": "field",
            "mutability": "current",
            "lifespan": "hot",
            "content": {"value": 1},
            "owner_skill": "caller",
        }
        request_command(
            root,
            argparse.Namespace(
                json_request=json.dumps(state_request),
                request_file=None,
                destination=None,
            ),
        )
        state_event = read_events(events_file(root))[-1]
        if state_event["payload"].get("changed", {}).get("entries", {}).get("set") != ["entry_1"]:
            raise SystemExit("state request did not record its actual changed entry")
        event_count = len(read_events(events_file(root)))
        request_command(
            root,
            argparse.Namespace(
                json_request=json.dumps(state_request),
                request_file=None,
                destination=None,
            ),
        )
        if len(read_events(events_file(root))) != event_count:
            raise SystemExit("unchanged state request created an event")
        check_command(root, argparse.Namespace())
        log_command(root, argparse.Namespace(
            type="blocker.opened",
            domain="state",
            request_id="blk_1",
            payload=json.dumps({"blocker": {"id": "B1", "message": "waiting for proof"}}),
            actor_kind="caller",
            actor_name="self-test",
        ))
        state = read_json(state_file(root))
        if state["open_blockers"][0]["status"] != "open":
            raise SystemExit("blocker.opened did not update current state")
        request = {
            "request_id": "rec_1",
            "fact_type": "narrative",
            "query_profile": "human",
            "mutability": "immutable",
            "lifespan": "durable",
            "content": "self-test narrative",
            "owner_skill": "caller",
        }
        request_command(root, argparse.Namespace(json_request=json.dumps(request), request_file=None, destination=None))
        spec = {
            "request_id": "spec_1",
            "fact_type": "spec",
            "query_profile": "human",
            "mutability": "immutable",
            "lifespan": "durable",
            "content": "# Self-test spec\n",
            "owner_skill": "caller",
        }
        request_command(root, argparse.Namespace(json_request=json.dumps(spec), request_file=None, destination=None))
        if not (root / "docs" / "specs" / "spec_1.md").is_file():
            raise SystemExit("spec was not written to the default spec destination")
        plan = {
            "request_id": "plan_1",
            "fact_type": "plan",
            "query_profile": "human",
            "mutability": "immutable",
            "lifespan": "durable",
            "content": "# Self-test plan\n",
            "owner_skill": "caller",
        }
        request_command(root, argparse.Namespace(json_request=json.dumps(plan), request_file=None, destination=Path("docs") / "plans" / "custom-plan.md"))
        if not (root / "docs" / "plans" / "custom-plan.md").is_file():
            raise SystemExit("plan was not written relative to the project root")
        evidence = {
            "request_id": "ev_1",
            "fact_type": "evidence",
            "query_profile": "search",
            "mutability": "immutable",
            "lifespan": "cold",
            "content": {"path": "notes/raw.txt"},
            "owner_skill": "caller",
        }
        request_command(root, argparse.Namespace(json_request=json.dumps(evidence), request_file=None, destination=None))
        if not (state_dir(root) / "evidence" / "ev_1.json").is_file():
            raise SystemExit("cold evidence was not written")
        evidence_event = read_events(events_file(root))[-1]
        evidence_payload = evidence_event["payload"]
        if (
            evidence_payload.get("destination") != ".noootwo/state/evidence/ev_1.json"
            or not HASH_RE.match(str(evidence_payload.get("sha256", "")))
            or evidence_payload.get("bytes", 0) <= 0
        ):
            raise SystemExit("cold evidence handle missing path, size, or hash")
        log_command(root, argparse.Namespace(
            type="evidence.recorded",
            domain="state",
            request_id="ev_2",
            payload=json.dumps({
                "destination": ".noootwo/state/evidence/ev_2.log",
                "sha256": sha256_text("captured"),
                "summary": "captured evidence",
                "command": ["verify", "--fast"],
                "exit_code": 0,
            }),
            actor_kind="caller",
            actor_name="self-test",
        ))
        capsule = build_capsule(root)
        if capsule["protocol"] != PROTOCOL_CAPSULE or not capsule["evidence_handles"]:
            raise SystemExit("capsule missing protocol or evidence handles")
        if not capsule["open_blockers"] or capsule["open_blockers"][0]["id"] != "B1":
            raise SystemExit("capsule missing open blocker")
        if (
            capsule["evidence_handles"][0].get("command") != '["verify","--fast"]'
            or capsule["evidence_handles"][0].get("exit_code") != 0
        ):
            raise SystemExit("capsule evidence handle lost command or exit status")
        for index in range(6):
            log_command(root, argparse.Namespace(
                type="state.updated",
                domain="state",
                request_id=f"noise_{index}",
                payload=json.dumps({"changed_fields": ["stage"]}),
                actor_kind="caller",
                actor_name="self-test",
            ))
        capsule = build_capsule(root, recent=2)
        if not capsule["evidence_handles"]:
            raise SystemExit("capsule did not scan recent history for evidence handles")
        bounded_json = fit_capsule_json(capsule, 2000)
        if len(bounded_json) > 2000 or len(bounded_json.splitlines()) > DEFAULT_CAPSULE_LINES:
            raise SystemExit("JSON capsule exceeded its character or line budget")
        rendered = cap_rendered_text(render_capsule(capsule), 1200, DEFAULT_CAPSULE_LINES)
        if len(rendered) > 1200 or len(rendered.splitlines()) > DEFAULT_CAPSULE_LINES:
            raise SystemExit("markdown capsule exceeded its budget")
        json_buffer = io.StringIO()
        with contextlib.redirect_stdout(json_buffer):
            capsule_command(root, argparse.Namespace(json_output=True, max_chars=6000, last=5))
        json_capsule = json.loads(json_buffer.getvalue())
        if json_capsule["protocol"] != PROTOCOL_CAPSULE:
            raise SystemExit("JSON capsule command used the wrong protocol")
        markdown_buffer = io.StringIO()
        with contextlib.redirect_stdout(markdown_buffer):
            capsule_command(root, argparse.Namespace(json_output=False, max_chars=6000, last=5))
        markdown_capsule = markdown_buffer.getvalue()
        if len(markdown_capsule) > DEFAULT_CAPSULE_MAX_CHARS or len(markdown_capsule.splitlines()) > DEFAULT_CAPSULE_LINES:
            raise SystemExit("default markdown capsule exceeded its budget")
        long_doc = root / "long.md"
        long_lines = [f"line {index}" for index in range(300)]
        long_lines[19] = "needle unique local hit"
        long_doc.write_text("# Title\n" + "\n".join(long_lines), encoding="utf-8")
        inspected = inspect_data(root, "long.md", "needle unique", 10)
        if inspected["lines"] != 301 or len(inspected["excerpt"]) > 10 or inspected["title"] != "Title":
            raise SystemExit("inspect did not bound a long document")
        if [item["line"] for item in inspected["excerpt"]] != [21]:
            raise SystemExit("inspect did not return the requested local matches")
        binary = root / "binary.dat"
        binary.write_bytes(b"\x00\x01\x02")
        if not inspect_data(root, "binary.dat", None, 10)["binary"]:
            raise SystemExit("inspect did not classify binary data")
        try:
            inspect_command(root, argparse.Namespace(
                path="long.md",
                query="needle",
                max_lines=DEFAULT_INSPECT_LINES + 1,
                json_output=True,
            ))
        except SystemExit:
            pass
        else:
            raise SystemExit("inspect accepted a live excerpt above the context budget")
        empty_root = root / "empty"
        empty_root.mkdir()
        try:
            build_capsule(empty_root)
        except SystemExit:
            pass
        else:
            raise SystemExit("capsule accepted missing state")
        corrupt_root = root / "corrupt"
        state_dir(corrupt_root).mkdir(parents=True)
        state_file(corrupt_root).write_text("{broken", encoding="utf-8")
        try:
            build_capsule(corrupt_root)
        except SystemExit:
            pass
        else:
            raise SystemExit("capsule accepted corrupt state")
        capture_event_bytes = events_file(root).read_bytes()
        capture_stdout = io.StringIO()
        with contextlib.redirect_stdout(io.StringIO()):
            capture_command(root, argparse.Namespace(
                name="capture_self",
                max_lines=5,
                capture_argv=[sys.executable, "-c", "import sys; print('captured'); sys.exit(7)"],
            ))
        capture_meta = read_json(state_dir(root) / "evidence" / "capture_self.json")
        if capture_meta["exit_code"] != 7 or capture_meta["bytes"] == 0:
            raise SystemExit("capture did not preserve exit status and output")
        with contextlib.redirect_stdout(capture_stdout):
            capture_command(root, argparse.Namespace(
                name="capture_long",
                max_lines=3,
                capture_argv=[sys.executable, "-c", "import sys; sys.stdout.write('x' * 20000)"],
            ))
        long_log = state_dir(root) / "evidence" / "capture_long.log"
        long_meta = read_json(state_dir(root) / "evidence" / "capture_long.json")
        if len(long_log.read_bytes()) != 20000 or long_meta["bytes"] != 20000:
            raise SystemExit("capture did not preserve long output")
        if long_meta["sha256"] != sha256_bytes(long_log.read_bytes()):
            raise SystemExit("capture hash does not cover the stored log")
        if len(capture_stdout.getvalue()) > 6500:
            raise SystemExit("capture returned too much of a long output")
        if events_file(root).read_bytes() != capture_event_bytes:
            raise SystemExit("capture changed project state")
        old = root / "old.md"
        old.write_text("old markdown\n", encoding="utf-8")
        manifest_path = root / "migrate.json"
        manifest_path.write_text(json.dumps({
            "protocol": "noootwo.migrate/0.1",
            "entries": [
                {
                    "path": "old.md",
                    "request_id": "mig_1",
                    "fact_type": "narrative",
                    "query_profile": "human",
                    "mutability": "immutable",
                    "lifespan": "durable",
                    "owner_skill": "caller",
                }
            ],
        }), encoding="utf-8")
        migrate_command(root, argparse.Namespace(manifest=str(manifest_path), keep=False))
        if old.exists():
            raise SystemExit("migration did not archive source")
        if not (state_dir(root) / "legacy" / "old.md").is_file():
            raise SystemExit("migration did not write legacy archive")
        if not (state_dir(root) / "records" / "mig_1.md").is_file():
            raise SystemExit("migration did not write converted record")
        check_command(root, argparse.Namespace())
        render_command(root, argparse.Namespace())
        if not (state_dir(root) / "summary.md").is_file():
            raise SystemExit("render did not produce summary.md")
        shell = Path(__file__).with_name("noootwo-state.sh")
        if shell.is_file():
            completed = subprocess.run(["sh", "-n", str(shell)], check=False)
            if completed.returncode:
                raise SystemExit("state shell helper has invalid syntax")
    print("self-test ok")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Read and write Noootwo project state.")
    parser.add_argument("--root", type=Path, default=Path("."), help="Project root.")
    parser.add_argument("--self-test", action="store_true", help="Run the built-in smoke test and exit.")
    sub = parser.add_subparsers(dest="command")

    p_init = sub.add_parser("init")
    p_init.add_argument("--work-id", default=f"w_{uuid.uuid4().hex[:12]}")
    p_init.add_argument("--session-id", default=f"s_{uuid.uuid4().hex[:12]}")
    p_init.add_argument("--attempt-id", default=f"a_{uuid.uuid4().hex[:12]}")
    p_init.add_argument("--goal", default="")
    p_init.add_argument("--force", action="store_true")

    p_set = sub.add_parser("set")
    p_set.add_argument("--stage")
    p_set.add_argument("--goal")
    p_set.add_argument("--waiting", choices=sorted(STATE_ENUM["waiting_on"]))
    p_set.add_argument("--last-owner")
    p_set.add_argument("--last-result")
    p_set.add_argument("--next-trigger")
    p_set.add_argument("--settled", action="append", default=[])
    p_set.add_argument("--unsettled", action="append", default=[])

    p_log = sub.add_parser("log")
    p_log.add_argument("--type", required=True)
    p_log.add_argument("--domain", default="state")
    p_log.add_argument("--request-id")
    p_log.add_argument("--payload")
    p_log.add_argument("--actor-kind", default="harness")
    p_log.add_argument("--actor-name", default="noootwo-state")

    p_request = sub.add_parser("request")
    p_request.add_argument("--json-request")
    p_request.add_argument("--request-file")
    p_request.add_argument("--destination")

    p_migrate = sub.add_parser("migrate")
    p_migrate.add_argument("--manifest", required=True)
    p_migrate.add_argument("--keep", action="store_true")

    sub.add_parser("check")
    sub.add_parser("render")

    p_capsule = sub.add_parser("capsule")
    p_capsule.add_argument("--json", dest="json_output", action="store_true")
    p_capsule.add_argument("--max-chars", type=int, default=DEFAULT_CAPSULE_MAX_CHARS)
    p_capsule.add_argument("--last", type=int, default=5, help="Recent event and evidence handle count.")

    p_inspect = sub.add_parser("inspect")
    p_inspect.add_argument("path")
    p_inspect.add_argument("--query")
    p_inspect.add_argument("--max-lines", type=int, default=DEFAULT_INSPECT_LINES)
    p_inspect.add_argument("--json", dest="json_output", action="store_true")

    p_capture = sub.add_parser("capture")
    p_capture.add_argument("--name", required=True)
    p_capture.add_argument("--max-lines", type=int, default=DEFAULT_CAPTURE_LINES)
    return parser


def main() -> int:
    parser = build_parser()
    args, leftovers = parser.parse_known_args()
    if args.self_test:
        self_test()
        return 0
    if not args.command:
        parser.print_help()
        return 2
    if args.command == "capture":
        args.capture_argv = leftovers[1:] if leftovers[:1] == ["--"] else leftovers
    elif leftovers:
        parser.error(f"unrecognized arguments: {' '.join(leftovers)}")
    root = args.root.resolve()
    if args.command == "init":
        init_command(root, args)
    elif args.command == "set":
        set_command(root, args)
    elif args.command == "log":
        log_command(root, args)
    elif args.command == "check":
        check_command(root, args)
    elif args.command == "render":
        render_command(root, args)
    elif args.command == "capsule":
        capsule_command(root, args)
    elif args.command == "inspect":
        inspect_command(root, args)
    elif args.command == "capture":
        if not 1 <= args.max_lines <= 80:
            raise SystemExit("--max-lines must be between 1 and 80")
        capture_command(root, args)
    elif args.command == "request":
        request_command(root, args)
    elif args.command == "migrate":
        migrate_command(root, args)
    else:
        parser.print_help()
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
