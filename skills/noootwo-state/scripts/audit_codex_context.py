#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import tempfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


USAGE_FIELDS = (
    "input_tokens",
    "cached_input_tokens",
    "cache_write_input_tokens",
    "output_tokens",
    "reasoning_output_tokens",
    "total_tokens",
)


def parse_iso(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def output_bytes(value: object) -> int:
    if isinstance(value, str):
        return len(value.encode("utf-8"))
    if value is None:
        return 0
    return len(json.dumps(value, ensure_ascii=False).encode("utf-8"))


def command_digest(arguments: object) -> str | None:
    if not isinstance(arguments, str):
        return None
    try:
        payload = json.loads(arguments)
    except json.JSONDecodeError:
        return None
    if not isinstance(payload, dict) or not isinstance(payload.get("cmd"), str):
        return None
    return hashlib.sha256(payload["cmd"].encode("utf-8")).hexdigest()


def audit_sessions(sessions_root: Path, cwd: str | None, since: str | None) -> dict:
    root = sessions_root.expanduser().resolve()
    if not root.is_dir():
        raise SystemExit(f"sessions root not found: {root}")
    cwd_filter = str(Path(cwd).expanduser().resolve()) if cwd else None
    if since:
        try:
            since_time = parse_iso(since)
        except ValueError as exc:
            raise SystemExit(f"invalid --since timestamp: {since}") from exc
    else:
        since_time = None
    usage: dict[tuple[str, str], dict] = {}
    thread_usage: dict[str, Counter] = defaultdict(Counter)
    command_counts: Counter[str] = Counter()
    files_scanned = 0
    sessions = 0
    turns = 0
    compactions = 0
    tool_calls = 0
    tool_outputs = 0
    tool_output_bytes = 0
    tool_outputs_over_16k = 0
    first_seen: datetime | None = None
    last_seen: datetime | None = None

    for path in sorted(root.rglob("*.jsonl")):
        files_scanned += 1
        records: list[dict] = []
        session_cwd: str | None = None
        for line in path.open(encoding="utf-8", errors="replace"):
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            records.append(record)
            payload = record.get("payload")
            if record.get("type") == "session_meta" and isinstance(payload, dict):
                value = payload.get("cwd")
                if isinstance(value, str):
                    session_cwd = str(Path(value).expanduser().resolve())
        if cwd_filter and session_cwd != cwd_filter:
            continue
        sessions += 1
        for record in records:
            timestamp = record.get("timestamp")
            if isinstance(timestamp, str):
                try:
                    parsed = parse_iso(timestamp)
                except ValueError:
                    parsed = None
                if parsed:
                    first_seen = parsed if first_seen is None or parsed < first_seen else first_seen
                    last_seen = parsed if last_seen is None or parsed > last_seen else last_seen
                    if since_time and parsed < since_time:
                        continue
            record_type = record.get("type")
            payload = record.get("payload")
            if record_type == "compacted":
                compactions += 1
                continue
            if not isinstance(payload, dict):
                continue
            if record_type == "token_usage_record":
                thread_id = str(payload.get("thread_id") or "")
                response_id = str(payload.get("response_id") or "")
                item_usage = payload.get("usage")
                if not thread_id or not response_id or not isinstance(item_usage, dict):
                    continue
                key = (thread_id, response_id)
                if key in usage:
                    continue
                usage[key] = item_usage
                for field in USAGE_FIELDS:
                    value = item_usage.get(field)
                    if isinstance(value, int):
                        thread_usage[thread_id][field] += value
            elif record_type == "event_msg" and payload.get("type") == "task_started":
                turns += 1
            elif record_type == "response_item":
                item_type = payload.get("type")
                if item_type in {"function_call", "custom_tool_call"}:
                    tool_calls += 1
                    if payload.get("name") == "exec_command":
                        digest = command_digest(payload.get("arguments"))
                        if digest:
                            command_counts[digest] += 1
                elif item_type in {"function_call_output", "custom_tool_call_output"}:
                    tool_outputs += 1
                    size = output_bytes(payload.get("output"))
                    tool_output_bytes += size
                    if size > 16 * 1024:
                        tool_outputs_over_16k += 1

    totals = Counter()
    for item_usage in usage.values():
        for field in USAGE_FIELDS:
            value = item_usage.get(field)
            if isinstance(value, int):
                totals[field] += value
    repeated_groups = [count for count in command_counts.values() if count > 1]
    threads = []
    for thread_id, values in sorted(
        thread_usage.items(),
        key=lambda item: item[1].get("total_tokens", 0),
        reverse=True,
    ):
        threads.append({
            "thread_hash": hashlib.sha256(thread_id.encode("utf-8")).hexdigest()[:12],
            "total_tokens": values.get("total_tokens", 0),
            "uncached_input_tokens": max(
                0,
                values.get("input_tokens", 0) - values.get("cached_input_tokens", 0),
            ),
            "output_tokens": values.get("output_tokens", 0),
        })
    return {
        "protocol": "noootwo.codex-context-audit/0.1",
        "sessions_root": str(root),
        "cwd_filter": cwd_filter,
        "since": since,
        "first_seen": first_seen.isoformat() if first_seen else None,
        "last_seen": last_seen.isoformat() if last_seen else None,
        "files_scanned": files_scanned,
        "sessions": sessions,
        "threads": len(thread_usage),
        "turns": turns,
        "unique_responses": len(usage),
        "compactions": compactions,
        "tool_calls": tool_calls,
        "tool_outputs": tool_outputs,
        "tool_output_bytes": tool_output_bytes,
        "tool_outputs_over_16k": tool_outputs_over_16k,
        "repeated_exec_groups": len(repeated_groups),
        "repeated_exec_extra_calls": sum(count - 1 for count in repeated_groups),
        "input_tokens": totals.get("input_tokens", 0),
        "cached_input_tokens": totals.get("cached_input_tokens", 0),
        "cache_write_input_tokens": totals.get("cache_write_input_tokens", 0),
        "uncached_input_tokens": max(
            0,
            totals.get("input_tokens", 0) - totals.get("cached_input_tokens", 0),
        ),
        "output_tokens": totals.get("output_tokens", 0),
        "reasoning_output_tokens": totals.get("reasoning_output_tokens", 0),
        "total_tokens": totals.get("total_tokens", 0),
        "thread_totals": threads,
    }


def print_human(report: dict) -> None:
    print("Codex Context Audit")
    print(f"- sessions: {report['sessions']} / files scanned: {report['files_scanned']}")
    print(f"- threads: {report['threads']} / turns: {report['turns']}")
    print(f"- total tokens: {report['total_tokens']:,}")
    print(f"- uncached input: {report['uncached_input_tokens']:,}")
    print(f"- output: {report['output_tokens']:,} / reasoning: {report['reasoning_output_tokens']:,}")
    print(f"- compactions: {report['compactions']}")
    print(f"- tool calls: {report['tool_calls']} / outputs: {report['tool_outputs']}")
    print(f"- tool output bytes: {report['tool_output_bytes']:,}")
    print(f"- outputs over 16 KiB: {report['tool_outputs_over_16k']}")
    print(f"- repeated exec extras: {report['repeated_exec_extra_calls']} across {report['repeated_exec_groups']} groups")
    if report["thread_totals"]:
        print("- largest thread totals:")
        for item in report["thread_totals"][:5]:
            print(
                f"  {item['thread_hash']}: total={item['total_tokens']:,} "
                f"uncached={item['uncached_input_tokens']:,} output={item['output_tokens']:,}"
            )


def self_test() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        sessions = root / "2026" / "10"
        sessions.mkdir(parents=True)
        path = sessions / "session.jsonl"
        secret_prompt = "PRIVATE_PROMPT_SHOULD_NOT_APPEAR"
        secret_output = "PRIVATE_TOOL_OUTPUT_SHOULD_NOT_APPEAR"
        secret_argument = "PRIVATE_ARGUMENT_SHOULD_NOT_APPEAR"
        records = [
            {"timestamp": "2026-10-25T00:00:00Z", "type": "session_meta", "payload": {"cwd": "/tmp/project"}},
            {"timestamp": "2026-10-25T00:00:00Z", "type": "response_item", "payload": {"type": "message", "content": secret_prompt}},
            {"timestamp": "2026-10-25T00:00:01Z", "type": "event_msg", "payload": {"type": "task_started"}},
            {
                "timestamp": "2026-10-25T00:00:02Z",
                "type": "token_usage_record",
                "payload": {
                    "thread_id": "thread-1",
                    "response_id": "response-1",
                    "usage": {
                        "input_tokens": 80,
                        "cached_input_tokens": 20,
                        "cache_write_input_tokens": 0,
                        "output_tokens": 20,
                        "reasoning_output_tokens": 5,
                        "total_tokens": 100,
                    },
                },
            },
            {
                "timestamp": "2026-10-25T00:00:02Z",
                "type": "token_usage_record",
                "payload": {
                    "thread_id": "thread-1",
                    "response_id": "response-1",
                    "usage": {
                        "input_tokens": 80,
                        "cached_input_tokens": 20,
                        "cache_write_input_tokens": 0,
                        "output_tokens": 20,
                        "reasoning_output_tokens": 5,
                        "total_tokens": 100,
                    },
                },
            },
            {
                "timestamp": "2026-10-25T00:00:03Z",
                "type": "token_usage_record",
                "payload": {
                    "thread_id": "thread-1",
                    "response_id": "response-2",
                    "usage": {
                        "input_tokens": 40,
                        "cached_input_tokens": 30,
                        "cache_write_input_tokens": 0,
                        "output_tokens": 10,
                        "reasoning_output_tokens": 2,
                        "total_tokens": 50,
                    },
                },
            },
            {
                "timestamp": "2026-10-25T00:00:04Z",
                "type": "token_usage_record",
                "payload": {
                    "thread_id": "thread-1",
                    "response_id": "response-3",
                    "usage": {"total_tokens": 10},
                    "nested": {"type": "compacted"},
                },
            },
            {"timestamp": "2026-10-25T00:00:04Z", "type": "compacted", "payload": {"thread_id": "thread-1"}},
            {"timestamp": "2026-10-25T00:00:04Z", "type": "compacted", "payload": None},
            {"timestamp": "2026-10-25T00:00:04Z", "type": "event_msg", "payload": {"type": "compacted"}},
            {
                "timestamp": "2026-10-25T00:00:05Z",
                "type": "response_item",
                "payload": {
                    "type": "function_call",
                    "name": "exec_command",
                    "arguments": json.dumps({"cmd": secret_argument}),
                },
            },
            {
                "timestamp": "2026-10-25T00:00:06Z",
                "type": "response_item",
                "payload": {
                    "type": "function_call",
                    "name": "exec_command",
                    "arguments": json.dumps({"cmd": secret_argument}),
                },
            },
            {
                "timestamp": "2026-10-25T00:00:07Z",
                "type": "response_item",
                "payload": {"type": "function_call_output", "output": secret_output + "x" * 20000},
            },
        ]
        path.write_text("\n".join(json.dumps(item) for item in records) + "\n", encoding="utf-8")
        report = audit_sessions(root, cwd="/tmp/project", since="2026-10-25")
        assert report["threads"] == 1
        assert report["total_tokens"] == 160
        assert report["uncached_input_tokens"] == 70
        assert report["compactions"] == 2
        assert report["tool_outputs_over_16k"] == 1
        assert report["repeated_exec_extra_calls"] == 1
        assert report["unique_responses"] == 3
        rendered = json.dumps(report, ensure_ascii=False)
        for secret in (secret_prompt, secret_output, secret_argument):
            assert secret not in rendered
        assert report["first_seen"] == "2026-10-25T00:00:00+00:00"
        try:
            audit_sessions(root, cwd="/tmp/project", since="not-a-date")
        except SystemExit:
            pass
        else:
            raise AssertionError("invalid --since timestamp was accepted")
    print("self-test ok")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Audit Codex JSONL token, compaction, tool-output, and repetition cost without emitting content."
    )
    parser.add_argument(
        "--sessions-root",
        type=Path,
        default=Path.home() / ".codex" / "sessions",
    )
    parser.add_argument("--cwd")
    parser.add_argument("--since")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.self_test:
        self_test()
        return 0
    report = audit_sessions(args.sessions_root, args.cwd, args.since)
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print_human(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
