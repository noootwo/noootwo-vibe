---
name: noootwo-docs
description: Use when maintaining project documentation after code, workflow, release, architecture, repository, or product changes. Owns README, AGENTS, docs/status, ADRs, guides, reference docs, release notes, and documentation-state hygiene without duplicating facts across layers.
---

# Noootwo Docs

Use this skill when documentation must reflect actual project state. The goal is not more documents; it is the right fact in the right layer.

## Document Layers

- `README.md`: stable public overview, install, usage, skill list, and release model.
- `AGENTS.md`: short always-on instructions for agents; route to skills instead of duplicating their full bodies.
- `docs/status.md`: current repository state, active risks, validation status, and next actions.
- `docs/adr/`: durable decisions with context, decision, consequences, and status.
- `docs/guides/`: how-to workflows that users or agents repeat.
- `docs/reference/`: stable command, schema, manifest, or API references.
- `docs/releases/`: per-skill release notes, migration notes, and tag history.

## Update Rules

1. Inspect the actual change before writing docs.
2. Pick the lowest document layer that owns the fact.
3. Update one source of truth; link rather than copy when another layer needs awareness.
4. Record volatile state in `docs/status.md`, not README or AGENTS.
5. Record lasting architectural or workflow decisions as ADRs.
6. Keep AGENTS short enough to stay useful in every session.
7. Do not claim validation, release, or readiness unless evidence exists.

## After Any Completed Change

Check whether the change affects:

- install or usage instructions
- repository or package layout
- public commands or scripts
- skill names, descriptions, or routing
- validation, CI, release, tags, or local install flow
- architecture decisions or project status

If yes, update the owning document before final handoff.

## Anti-Drift Rules

- Do not write an operational diary in README.
- Do not bury durable decisions in chat summaries.
- Do not spread the same command list across README, AGENTS, and docs/reference.
- Do not leave docs saying `noootwo-design` when the live repo/package is `noootwo-vibe`.
- Do not preserve stale examples for backward compatibility unless the migration note says so explicitly.

For deeper layer guidance, read `references/docs-layering.md` when changing multiple documentation levels in one task.
