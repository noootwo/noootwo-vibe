#!/bin/sh

set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
root="."

usage() {
  cat <<'EOF'
Usage: noootwo-state.sh [--root DIR] <command> [options]

  state   --field KEY       print one current field
          --json            print the current snapshot
  events  --type TYPE       filter event_type
          --last N          show the last N events (default 20)
          --since ISO       show events at or after ISO timestamp
          --json            print raw matching JSON lines
  capsule --json            print the bounded context capsule as JSON
          --max-chars N     character budget (default 6000; minimum 2000)
          --last N          recent event evidence handles (default 5)
  summary                   alias for capsule; compatible bounded re-entry
  inspect PATH              show metadata, headings, and bounded matches
          --query TEXT      find matching lines
          --max-lines N     excerpt budget (default 80)
          --json            print JSON
  capture --name ID -- CMD  capture complete output and return a cold handle
          --max-lines N     returned tail budget (default 40)
EOF
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --root) root="${2:-.}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) break ;;
  esac
done

if [ "$#" -eq 0 ]; then
  usage >&2
  exit 2
fi

command="$1"
shift
state_dir="$root/.noootwo/state"
state_file="$state_dir/current.json"
events_file="$state_dir/events.jsonl"

read_field() {
  sed -n "s/^[[:space:]]*\"$1\"[[:space:]]*:[[:space:]]*//p" "$state_file" | sed 's/,\{0,1\}$//' | head -n 1
}

case "$command" in
  capsule|summary|inspect|capture)
    passthrough_command="$command"
    if [ "$command" = "summary" ]; then
      passthrough_command="capsule"
    fi
    exec python3 "$script_dir/noootwo_state.py" --root "$root" "$passthrough_command" "$@"
    ;;
  state)
    field=""
    json=0
    while [ "$#" -gt 0 ]; do
      case "$1" in
        --field) field="${2:-}"; shift 2 ;;
        --json) json=1; shift ;;
        *) echo "unknown state argument: $1" >&2; usage >&2; exit 2 ;;
      esac
    done
    [ -f "$state_file" ] || { echo "missing $state_file" >&2; exit 1; }
    if [ "$json" -eq 1 ]; then
      cat "$state_file"
      exit 0
    fi
    if [ -n "$field" ]; then
      read_field "$field"
      exit 0
    fi
    for key in stage goal last_owner next_trigger waiting_on; do
      printf '%s=' "$key"
      read_field "$key"
    done
    ;;
  events)
    event_type=""
    last=20
    since=""
    json=0
    while [ "$#" -gt 0 ]; do
      case "$1" in
        --type) event_type="${2:-}"; shift 2 ;;
        --last) last="${2:-20}"; shift 2 ;;
        --since) since="${2:-}"; shift 2 ;;
        --json) json=1; shift ;;
        *) echo "unknown events argument: $1" >&2; usage >&2; exit 2 ;;
      esac
    done
    [ -f "$events_file" ] || { echo "missing $events_file" >&2; exit 1; }
    {
      if [ -n "$event_type" ]; then
        grep "\"event_type\":\"$event_type\"" "$events_file"
      else
        cat "$events_file"
      fi
    } | {
      if [ -n "$since" ]; then
        awk -v s="$since" 'substr($0, index($0,"\"occurred_at\":\"")+14, length(s)) >= s'
      else
        cat
      fi
    } | {
      if [ "$json" -eq 1 ]; then
        tail -n "$last"
      else
        tail -n "$last" | sed -n 's/.*"event_type":"\([^"]*\)".*"occurred_at":"\([^"]*\)".*/"\1" \2/p'
      fi
    }
    ;;
  *)
    echo "unknown command: $command" >&2
    usage >&2
    exit 2
    ;;
esac
