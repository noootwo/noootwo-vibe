---
name: noootwo-state
description: "Use to read, record, or place project state and context; choose queryable state for structure and Markdown for narrative artifacts."
---

# Noootwo State

Own how project state and context are persisted, read, and changed. Other skills own the content; this skill owns the format, location, schema, and access.

## Context budget

Context lifecycle `write -> select -> compress -> isolate -> verify`: load this skill and triggered reference sections; route references over 200 lines through headings or query hits; cap live excerpts at 80 lines; put output over 16 KiB in cold evidence with path and hash; isolate only independent read-only work; keep one writer; verify summaries against source.

## 1. Read the request

Take an abstract StateWriteRequest. Do not interpret the content's domain meaning; use only its properties.

| Field | Values |
| --- | --- |
| `fact_type` | `state`, `event`, `decision`, `spec`, `plan`, `narrative`, `release`, `evidence`, `procedure` |
| `query_profile` | `field`, `tail`, `search`, `human` |
| `mutability` | `current`, `append-only`, `immutable` |
| `lifespan` | `hot`, `durable`, `cold` |

## 2. Choose the form

Use `references/format-selection.md`. The decision comes only from the request properties above, never from what the content is about.

## 3. Persist

- Structured current state or append-only events → `scripts/noootwo_state.py request` or `log`.
- Narrative, decision, spec, plan, or release facts → the owning Markdown layer named in `references/state-layering.md`.
- A spec or plan without an explicit destination defaults to `docs/specs/<request_id>.md` or `docs/plans/<request_id>.md`.
- Do not create a second authority for the same fact; replace or link the stale one.
- Another skill's default artifact path is not project policy. Put the durable record in the owning Noootwo layer; keep external paths only as read-only legacy.
- An unchanged structured-state write creates no event.

## 4. Read cheaply

- One field or a tail of events → `scripts/noootwo-state.sh state --field` or `events`.
- Session re-entry → `scripts/noootwo-state.sh capsule`; Markdown and JSON default to 80 lines and 6,000 characters and include the source state hash plus recent evidence handles.
- An unknown long document → `scripts/noootwo-state.sh inspect PATH --query TEXT`; start with headings or a query and load its bounded excerpt, not the whole file for one fact.
- A verbose command above 16 KiB → `scripts/noootwo-state.sh capture --name ID -- <command>`; keep the returned exit status and last lines, and use the log/hash as the evidence handle. Capture needs no current-state file and does not change state.
- A token or compaction question about local Codex history → `python3 scripts/audit_codex_context.py --cwd PATH --since ISO --json`; it reports aggregates only and never emits message or tool content.
- `summary` remains an alias for the same bounded capsule semantics.
- A read-only decision does not create state. When `.noootwo/state/current.json` is absent, continue from repository evidence without building or enumerating a state layer.

## 5. Verify

Run `scripts/noootwo_state.py check`. Confirm the schema is valid, `schema_version` is understood, hashes and idempotency keys hold, and no neighbouring record still contradicts the new one.

A record written during a degraded fallback carries a `skill-missing: <name>` marker. When the named skill becomes available, absorb the marked record through a normal request and remove the marker.

## 6. Migrate legacy records

To take over old files, submit a migration manifest and run `scripts/noootwo_state.py migrate --manifest <file>`.

The manifest is abstract: `protocol` is `noootwo.migrate/0.1` and `entries` names each old `path` plus the abstract properties the new record needs: `request_id`, `fact_type`, `query_profile`, `mutability`, `lifespan`, and optional `owner_skill`, `domain`, and `destination`.

The command reads each old file as content, persists it through the normal form selection, records the old path as `replaces`, and by default archives the source to `.noootwo/state/legacy/<path>`. Pass `--keep` to leave the source in place. The caller supplies the classification; this skill does not interpret the content.

**Done when:** the fact is in exactly one owning location, is readable through the intended query path, is validated, and stale duplicates are removed or linked.

## Context lifecycle

- Append-only events and cold evidence are history; the capsule is a bounded read view, never a second source of truth.
- Record a checkpoint only when the goal, decision, blocker, evidence, or next frontier changes.
- After compaction, read the capsule, the current commit/status, and only the evidence handles needed for the next step.
- When the current goal is complete and an unrelated goal appears, write the capsule and recommend a new session unless the user explicitly continues.

## References

- `references/state-layering.md` — abstract storage layers and ownership.
- `references/format-selection.md` — property-only form selection.
- `references/context-budget.md` — the context lifecycle, bounded reads, capsules, and cold evidence handles.
