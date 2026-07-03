---
name: noootwo-docs
description: Use when maintaining project documentation after code, workflow, release, architecture, repository, product, API, installation, validation, project onboarding, documentation audit, or agent-instruction changes. Owns README, AGENTS, docs/status, ADRs, guides, reference docs, release notes, documentation-state hygiene, anti-duplication, and stale-doc cleanup.
---

# Noootwo Docs

Use this skill when documentation must reflect actual project state. The goal is not more documents; it is the right fact in the right layer, with stale facts removed.

Keep the default path lightweight: inspect the change, update the owning layer, and avoid turning docs into a second implementation.

When `$noootwo-workflow` finds missing project foundation, this skill owns placing the facts in the correct documentation layer. When `$noootwo-review` reports project defects about documentation or duplicated truth, this skill owns the documentation fix.

## Document Layers

- `README.md`: stable public overview, install, usage, skill list, and release model.
- `AGENTS.md`: short always-on instructions for agents; route to skills instead of duplicating their full bodies.
- `docs/status.md`: current repository state, active risks, validation status, and next actions.
- `docs/adr/`: durable decisions with context, decision, consequences, and status.
- `docs/guides/`: how-to workflows that users or agents repeat.
- `docs/reference/`: stable command, schema, manifest, or API references.
- `docs/releases/`: per-skill release notes, migration notes, and tag history.

If a repository uses different names, map by responsibility rather than forcing this exact layout.

## Update Rules

1. Inspect the actual change before writing docs.
2. Classify each changed fact as `usage`, `agent rule`, `current state`, `decision`, `procedure`, `reference`, or `release`.
3. Pick one owning layer for each fact.
4. Update that source of truth; link rather than copy when another layer needs awareness.
5. Remove or revise stale claims in nearby docs during the same pass.
6. Record volatile state in `docs/status.md`, not README or AGENTS.
7. Record lasting architecture or workflow decisions as ADRs.
8. Keep AGENTS short enough to stay useful in every session.
9. Do not claim validation, release, or readiness unless fresh evidence exists.
10. When adopting a project, create the smallest useful docs foundation before adding detailed guides.

## After Any Completed Change

Check whether the change affects:

- install or usage instructions
- repository or package layout
- public commands or scripts
- skill names, descriptions, or routing
- validation, CI, release, tags, or local install flow
- architecture decisions or project status
- project foundation, skill audit, or project-health defects

If yes, update the owning document before final handoff.

If no, state that docs were checked and intentionally unchanged.

## Freshness Rules

- Prefer exact commands, paths, versions, and dates over vague status language.
- Put temporary progress, active risks, and next actions in status docs.
- Put durable decisions in ADRs after they are accepted, not as a chat recap.
- Put repeated procedures in guides only after they are likely to be reused.
- Put schemas, command references, and manifests in reference docs.
- Put release/user migration notes in release docs before tagging.

## Anti-Drift Rules

- Do not write an operational diary in README.
- Do not bury durable decisions in chat summaries.
- Do not spread the same command list across README, AGENTS, and docs/reference.
- Do not leave docs saying `noootwo-design` when the live repo/package is `noootwo-vibe`.
- Do not preserve stale examples for backward compatibility unless the migration note says so explicitly.
- Do not update README first just because it is visible; update the owning layer first.
- Do not describe intent as fact. If something is planned, label it planned.

For deeper guidance, read:

- `references/docs-layering.md` when changing multiple documentation levels, deciding whether to add an ADR, adopting a project, or cleaning up stale docs.
- `references/docs-audit.md` when auditing documentation defects, stale claims, duplicated facts, wrong-layer content, or unverified claims.
