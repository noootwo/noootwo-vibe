#!/bin/sh

set -eu

root="."
command=""
field=""
json=0
event_type=""
last=20
since=""

usage() {
  cat <<'EOF'
Usage: noootwo-state.sh [--root DIR] <state|events|summary> [options]

  state   --field KEY       print one current field
          --json            print the current snapshot
  events  --type TYPE       filter event_type
          --last N          show the last N events (default 20)
          --since ISO       show events at or after ISO timestamp
          --json            print raw matching JSON lines
  summary                   print the smallest re-entry summary
EOF
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --root) root="${2:-.}"; shift 2 ;;
    --field) field="${2:-}"; shift 2 ;;
    --type) event_type="${2:-}"; shift 2 ;;
    --last) last="${2:-20}"; shift 2 ;;
    --since) since="${2:-}"; shift 2 ;;
    --json) json=1; shift ;;
    state|events|summary) command="$1"; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "unknown argument: $1" >&2; usage >&2; exit 2 ;;
  esac
done

if [ -z "$command" ]; then
  usage >&2
  exit 2
fi

state_dir="$root/.noootwo/state"
state_file="$state_dir/current.json"
events_file="$state_dir/events.jsonl"

read_field() {
  sed -n "s/^[[:space:]]*\"$1\"[[:space:]]*:[[:space:]]*//p" "$state_file" | sed 's/,\{0,1\}$//' | head -n 1
}

if [ "$command" = "state" ]; then
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
  exit 0
fi

if [ "$command" = "events" ]; then
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
  exit 0
fi

if [ "$command" = "summary" ]; then
  [ -f "$state_file" ] || { echo "missing $state_file" >&2; exit 1; }
  for key in stage goal last_owner last_result next_trigger waiting_on; do
    printf '%s=' "$key"
    read_field "$key"
  done
  if [ -f "$events_file" ]; then
    echo "recent events:"
    tail -n "$last" "$events_file" | sed -n 's/.*"event_type":"\([^"]*\)".*/  \1/p'
  fi
  exit 0
fi
