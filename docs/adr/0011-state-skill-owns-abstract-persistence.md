# 0011 — Rename `noootwo-docs` to `noootwo-state` and own abstract persistence

## Status

Accepted.

## Context

`noootwo-docs` treated documentation as the primary output, and `noootwo-workflow` still wrote a project-local Markdown state file directly. Persistence was split between several skills, so the same fact could be written in different forms and locations.

The durable project context needed one owner that decides *how* a fact is stored without knowing *what* the fact means. Structured state should be queryable by field and tail; narrative decisions should remain human-readable Markdown.

## Decision

- Rename `noootwo-docs` to `noootwo-state`.
- Make `noootwo-state` the sole owner of reading and writing project state/context and choosing the storage form.
- Other skills keep their domain methods and content; they invoke `noootwo-state` to persist durable facts instead of writing `.noootwo/` or docs themselves.
- State is stored as a JSON current snapshot plus an append-only JSONL event log, with a generated Markdown projection.
- Query reads use a POSIX shell helper; validation and writes use a Python standard-library script.
- `noootwo-state` must not contain domain-specific vocabulary for design, test, product, review, debug, research, or onboarding; it classifies requests only by abstract properties.

## Consequences

- `noootwo-workflow` no longer owns state file format or writes state directly.
- The public skill set still contains ten skills, with `noootwo-state` replacing `noootwo-docs`.
- Several sibling skills update their handoff language to invoke `noootwo-state`.
- Historical ADRs and experiments may continue to use the old `noootwo-docs` name as a historical record.
