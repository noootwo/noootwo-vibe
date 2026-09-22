#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path


PROTOCOL_STATE = "noootwo.state/0.1"
PROTOCOL_EVENT = "noootwo.state-event/0.1"
STATE_SCHEMA_VERSION = 1
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
FACT_TYPES = {"state", "event", "decision", "narrative", "release", "evidence", "procedure"}
QUERY_PROFILES = {"field", "tail", "search", "human"}
MUTABILITIES = {"current", "append-only", "immutable"}
LIFESPANS = {"hot", "durable", "cold"}
HASH_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
ISO_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def state_dir(root: Path) -> Path:
    return root / ".noootwo" / "state"


def state_file(root: Path) -> Path:
    return state_dir(root) / "current.json"


def events_file(root: Path) -> Path:
    return state_dir(root) / "events.jsonl"


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=path.name + ".", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(text)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def canonical(data: object) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_text(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


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
    if args.stage is not None:
        state["stage"] = args.stage
    if args.goal is not None:
        state["goal"] = args.goal
    if args.waiting is not None:
        state["waiting_on"] = args.waiting
    if args.last_owner is not None:
        state["last_owner"] = args.last_owner
    if args.last_result is not None:
        state["last_result"] = args.last_result
    if args.next_trigger is not None:
        state["next_trigger"] = args.next_trigger
    for value in args.settled or []:
        if value not in state["settled"]:
            state["settled"].append(value)
    for value in args.unsettled or []:
        if value not in state["unsettled"]:
            state["unsettled"].append(value)
    event = new_event(state, "state.updated", "state", {"changed": True}, "harness", "noootwo-state")
    append_event(root, state, event)
    save_state(root, state)


def log_command(root: Path, args: argparse.Namespace) -> None:
    state = read_json(state_file(root))
    payload = json.loads(args.payload) if args.payload else {}
    if args.request_id:
        payload["request_id"] = args.request_id
    event = new_event(state, args.type, args.domain, payload, args.actor_kind, args.actor_name)
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


def choose_form(request: dict) -> str:
    fact_type = request.get("fact_type")
    query_profile = request.get("query_profile")
    mutability = request.get("mutability")
    lifespan = request.get("lifespan")
    if mutability == "append-only" or fact_type == "event":
        return "event"
    if fact_type == "evidence" or (lifespan == "cold" and query_profile == "search"):
        return "cold"
    if fact_type in {"decision", "narrative", "release", "procedure"} or query_profile == "human":
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


def apply_request(root: Path, request: dict, destination: Path | None = None, source: str | None = None) -> str:
    replaces = request.get("replaces") or []
    if isinstance(replaces, str):
        replaces = [replaces]
    if not isinstance(replaces, list):
        raise SystemExit("replaces must be a pointer, list of pointers, or omitted")

    state = read_json(state_file(root))
    form = choose_form(request)
    if form == "event":
        event_type = "event.appended"
        payload = {"request_id": request["request_id"], "content": request["content"], "replaces": replaces}
    elif form == "state":
        for old in replaces:
            state["entries"].pop(old, None)
        state["entries"][request["request_id"]] = request["content"]
        event_type = "state.updated"
        payload = {"request_id": request["request_id"], "replaces": replaces}
    elif form == "cold":
        if isinstance(request["content"], str):
            destination = Path(destination) if destination else state_dir(root) / "evidence" / f"{request['request_id']}.md"
            content = request["content"]
        else:
            destination = Path(destination) if destination else state_dir(root) / "evidence" / f"{request['request_id']}.json"
            content = json.dumps(request["content"], indent=2, ensure_ascii=False)
        atomic_write(destination, content if content.endswith("\n") else content + "\n")
        event_type = "evidence.recorded"
        payload = {"request_id": request["request_id"], "destination": str(destination), "replaces": replaces}
    else:
        destination = Path(destination) if destination else state_dir(root) / "records" / f"{request['request_id']}.md"
        content = request["content"]
        if not isinstance(content, str):
            content = json.dumps(content, indent=2, ensure_ascii=False)
        atomic_write(destination, content if content.endswith("\n") else content + "\n")
        event_type = f"{request['fact_type']}.recorded"
        payload = {"request_id": request["request_id"], "destination": str(destination), "replaces": replaces}

    if source:
        payload["source"] = source

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
        check_command(root, argparse.Namespace())
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
            os.system(f"sh -n {shell}")
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
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if not args.command:
        parser.print_help()
        return 2
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
