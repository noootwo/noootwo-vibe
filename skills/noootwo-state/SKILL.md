---
name: noootwo-state
description: "Use to read, record, or update project state and context, and to place changed facts; choose JSON/JSONL for queryable state and Markdown for narrative artifacts."
---

# Noootwo State

Own how project state and context are persisted, read, and changed. Other skills own the content; this skill owns the format, location, schema, and access.

## 1. Read the request

Take an abstract StateWriteRequest. Do not interpret the content's domain meaning; use only its properties.

| Field | Values |
| --- | --- |
| `fact_type` | `state`, `event`, `decision`, `narrative`, `release`, `evidence`, `procedure` |
| `query_profile` | `field`, `tail`, `search`, `human` |
| `mutability` | `current`, `append-only`, `immutable` |
| `lifespan` | `hot`, `durable`, `cold` |

## 2. Choose the form

Use `references/format-selection.md`. The decision comes only from the request properties above, never from what the content is about.

## 3. Persist

- Structured current state or append-only events → `scripts/noootwo_state.py request` or `log`.
- Narrative, decision, or release facts → the owning Markdown layer named in `references/state-layering.md`.
- Do not create a second authority for the same fact; replace or link the stale one.

## 4. Read cheaply

- One field or a tail of events → `scripts/noootwo-state.sh state --field`, `events`, or `summary`.
- A narrative slice → search the relevant region first, per `references/context-budget.md`; do not load a whole document for one fact.

## 5. Verify

Run `scripts/noootwo_state.py check`. Confirm the schema is valid, `schema_version` is understood, hashes and idempotency keys hold, and no neighbouring record still contradicts the new one.

A record written during a degraded fallback carries a `skill-missing: <name>` marker. When the named skill becomes available, absorb the marked record through a normal request and remove the marker.

**Done when:** the fact is in exactly one owning location, is readable through the intended query path, is validated, and stale duplicates are removed or linked.

## References

- `references/state-layering.md` — abstract storage layers and ownership.
- `references/format-selection.md` — property-only form selection.
- `references/context-budget.md` — bounded reads and local retrieval.
