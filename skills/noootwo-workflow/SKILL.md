---
name: noootwo-workflow
description: Use as the Noootwo commander skill for AI software development workflow control, task triage, multi-skill routing, planning, implementation sequencing, debugging/recovery flow, review checkpoints, documentation handoff, release closure, and preventing agentic project work from becoming chaotic, under-verified, or expensive.
---

# Noootwo Workflow

Use this skill before or during non-trivial AI-assisted software development when the work needs coordination across implementation, design, docs, review, debugging, release, or multiple Noootwo skills.

## Operating Goal

Keep work moving through a controlled loop:

`intake -> repo truth -> route -> plan -> execute -> verify -> document -> review -> release/handoff`

Default to the lightest flow that can still prove the result. Load deeper references only when the task needs them.

## First Pass

1. Read the nearest operating truth first: `AGENTS.md`, README, active `docs/status.md`, release notes, package/build metadata, and changed-file context.
2. Classify the work by primary motion: `small edit`, `feature`, `bugfix`, `refactor`, `release/ops`, `design`, `documentation`, `review-only`, or `recovery`.
3. Identify risks before editing: unclear intent, wide blast radius, migration/data risk, brittle tests, public API change, documentation drift, review ambiguity, or missing verification path.
4. Choose a mode:
   - `direct`: small localized work with an obvious check
   - `planned`: multi-file behavior or public workflow change
   - `diagnostic`: bug, failure, regression, or surprising behavior
   - `release`: version, tag, publish, CI, install, or repo metadata work
   - `recovery`: prior agent drift, repeated failed fixes, or unclear handoff
5. Do not add ceremony to direct work; do not skip evidence for risky work.

## Skill Routing

- Use `$noootwo-design` when the work changes UI, visual direction, artifact review, `.noootwo/` deliverables, design systems, screenshots, or frontend implementation handoff.
- Use `$noootwo-docs` when the work changes project state, public usage, architecture decisions, README, AGENTS, docs, or release notes.
- Use `$noootwo-review` when the work needs maintainability judgment, refactoring, code structure review, test strategy review, or a second pass before release.
- Stay in this skill when the main problem is sequencing, scope control, routing, or making several skills cooperate.

If two skills apply, use this order unless the user says otherwise:

`workflow -> design/docs/review specialist -> workflow closure`

If the task is a bug or failing check, first establish root cause and reproduction before routing to implementation or review.

## Planning Rules

- For direct work, state the direct path and implement.
- For planned work, produce a short plan before editing.
- For diagnostic work, record the observed symptom, reproduction, evidence path, and root-cause hypothesis before fixes.
- For release work, list version files, manifests, tags, install targets, and verification commands before publishing.
- For broad work, split into independently verifiable slices with natural review checkpoints.
- Keep decisions explicit: scope, non-scope, assumptions, proof of done, and rollback/compatibility notes when relevant.

## Execution Control

- Prefer existing repo patterns over new frameworks or abstractions.
- Keep files focused enough that future agents can reason about them cheaply.
- Load only the files needed for the current slice; use references as navigation, not as default context dumps.
- Do not duplicate long background context into multiple files.
- Do not let documentation, implementation, and review drift apart; route to `$noootwo-docs` before closing work that changes project behavior or state.
- Route to `$noootwo-review` before release when the change touches architecture, shared code, dependency shape, or repeated AI friction.

## Handoff Contract

When routing to another Noootwo skill, pass a compact handoff packet:

- task class and chosen mode
- relevant files or artifacts
- known constraints and non-goals
- verification command or missing verification path
- decision needed from the specialist

When control returns, close the loop by checking whether docs, review, release, or user confirmation is still missing.

## Completion Gate

Before calling work done, record:

- changed behavior or structure
- validation run and result
- documentation updated or intentionally unchanged
- remaining risk or follow-up
- release/tag/push state when relevant

For deeper guidance, read `references/workflow-playbook.md` only when planning a multi-step implementation, diagnostic recovery, or release workflow.
