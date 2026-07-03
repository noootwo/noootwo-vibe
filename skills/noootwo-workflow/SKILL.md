---
name: noootwo-workflow
description: Use as the Noootwo commander skill for AI software development workflow control, multi-skill routing, planning, implementation sequencing, review checkpoints, documentation handoff, and preventing agentic project work from becoming chaotic or expensive.
---

# Noootwo Workflow

Use this skill before or during non-trivial AI-assisted software development when the work needs coordination across design, docs, review, implementation, release, or multiple Noootwo skills.

## Operating Goal

Keep the project moving through a controlled loop:

`intake -> repo truth -> route -> plan -> implement -> verify -> document -> review -> release/handoff`

The default path must stay lightweight. Load deeper references only when the task needs them.

## First Pass

1. Read local project instructions first: `AGENTS.md`, repository README, active docs/status files, and relevant package or build metadata.
2. Classify the work:
   - `small edit`: localized change with low blast radius
   - `feature`: new behavior or user-visible capability
   - `bugfix`: observed failure with expected behavior
   - `refactor`: internal change intended to preserve behavior
   - `release/ops`: publish, deploy, repo rename, CI, version, or tag work
   - `design`: UI, visual system, artifact, or screenshot-sensitive work
   - `documentation`: docs, README, AGENTS, ADR, status, or release notes
3. Identify risks before editing: unclear intent, wide blast radius, migration/data risk, brittle tests, public API change, documentation drift, or missing verification path.
4. Choose the smallest useful workflow. Do not add ceremony to small edits.

## Skill Routing

- Use `$noootwo-design` when the work changes UI, visual direction, artifact review, `.noootwo/` deliverables, design systems, screenshots, or frontend implementation handoff.
- Use `$noootwo-docs` when the work changes project state, public usage, architecture decisions, README, AGENTS, docs, or release notes.
- Use `$noootwo-review` when the work needs maintainability judgment, refactoring, code structure review, test strategy review, or a second pass before release.
- Stay in this skill when the main problem is sequencing, scope control, routing, or making several skills cooperate.

If two skills apply, use this order unless the user says otherwise:

`workflow -> design/docs/review specialist -> workflow closure`

## Planning Rules

- For small edits, state the direct path and implement.
- For non-trivial work, produce a short implementation plan before editing.
- For risky or broad changes, split into independently verifiable tasks.
- For public API, schema, release, repo structure, or migration changes, include rollback/compatibility notes.
- Keep all decisions explicit: what is in scope, what is out of scope, what is assumed, and what will prove the work is done.

## Execution Control

- Prefer existing repo patterns over new frameworks or abstractions.
- Keep files focused enough that future agents can reason about them cheaply.
- Do not duplicate long background context into multiple files.
- Do not let documentation, implementation, and review drift apart; route to `$noootwo-docs` before closing work that changes project behavior or state.
- Route to `$noootwo-review` before release when the change touches architecture, shared code, dependency shape, or repeated AI friction.

## Completion Gate

Before calling work done, record:

- changed behavior or structure
- validation run and result
- documentation updated or intentionally unchanged
- remaining risk or follow-up
- release/tag/push state when relevant

For deeper guidance, read `references/workflow-playbook.md` only when planning a multi-step implementation or release workflow.
