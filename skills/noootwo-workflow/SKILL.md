---
name: noootwo-workflow
description: Use as the Noootwo commander skill for AI software development workflow control, lightweight alignment checkpoints, project onboarding, skill inventory, foundation audits, task triage, multi-skill routing, planning, implementation sequencing, debugging/recovery flow, review checkpoints, documentation handoff, release closure, and preventing agentic project work from becoming chaotic, under-verified, or expensive.
---

# Noootwo Workflow

Use this skill before or during non-trivial AI-assisted software development when the work needs coordination across implementation, design, docs, review, debugging, release, project onboarding, or multiple Noootwo skills.

## Operating Goal

Keep work moving through a controlled loop:

`intake -> repo truth -> skill/foundation audit -> route -> plan -> execute -> verify -> document -> review -> release/handoff`

Default to the lightest flow that can still prove the result. Load deeper references only when the task needs them.

Use an `alignment checkpoint` only when it prevents a likely wrong turn. It is a small decision control, not a meeting or questionnaire.

## First Pass

1. Read the nearest operating truth first: `AGENTS.md`, README, active `docs/status.md`, release notes, package/build metadata, and changed-file context.
2. Classify the work by primary motion: `small edit`, `feature`, `bugfix`, `refactor`, `release/ops`, `design`, `documentation`, `review-only`, or `recovery`.
3. Identify risks before editing: unclear intent, wide blast radius, migration/data risk, brittle tests, public API change, documentation drift, review ambiguity, or missing verification path.
4. Choose a mode:
   - `direct`: small localized work with an obvious check
   - `planned`: multi-file behavior or public workflow change
   - `diagnostic`: bug, failure, regression, or surprising behavior
   - `release`: version, tag, publish, CI, install, or repo metadata work
   - `onboarding`: unfamiliar project, missing process foundation, unclear skill needs, or handoff from another agent
   - `recovery`: prior agent drift, repeated failed fixes, or unclear handoff
5. Do not add ceremony to direct work; do not skip evidence for risky work.

## Alignment Checkpoint

Trigger this before editing only when the task is non-trivial and a decision could materially change the work: ambiguous goal, high-risk change, multi-file behavior, release, design direction, architecture boundary, public API, migration, or missing verification path.

Run the checkpoint in four steps:

1. Inspect repo truth first.
2. Name the single highest-impact unresolved decision.
3. Offer 2-3 meaningful options with one recommended default.
4. Record one outcome: `user chose`, `user delegated to agent`, or `no question needed`.

Skip it for small direct edits with an obvious verification path.

## Skill Routing

- Use this skill first when a project needs a skill inventory, foundation health check, gap plan, or multi-skill handoff.
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
- For onboarding work, audit needed skills and project foundation before proposing execution.
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

Before calling non-direct work done, answer three closure triggers:

- Was the changed behavior verified with the closest meaningful check?
- Did user-facing docs, status, ADRs, or release notes need updates?
- Does the result need `$noootwo-review` or `$noootwo-design` to inspect risk or artifact quality?

Then record:

- changed behavior or structure
- skill/foundation audit result when onboarding or taking over a project
- validation run and result
- documentation updated or intentionally unchanged
- remaining risk or follow-up
- release/tag/push state when relevant

For deeper guidance, read:

- `references/project-skill-audit.md` when deciding which Noootwo or local skills a project needs.
- `references/project-foundation-check.md` when checking process health, missing project files, or handoff readiness.
- `references/minimal-foundation-templates.md` only when a project lacks the minimal docs/process foundation.
- `references/workflow-playbook.md` when planning a multi-step implementation, diagnostic recovery, or release workflow.
