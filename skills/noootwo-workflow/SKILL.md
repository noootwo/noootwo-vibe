---
name: noootwo-workflow
description: Use as the Noootwo commander skill for AI software development workflow control, lifecycle guardrails, lightweight alignment checkpoints, project onboarding, skill inventory, foundation audits, task triage, specialist-first multi-skill routing, product/design/docs/review handoffs, planning, implementation sequencing, TDD/repro-first decisions, debugging/recovery flow, pre-submit review checkpoints, documentation handoff, release closure, and preventing agentic project work from becoming chaotic, under-verified, product-confused, or expensive.
---

# Noootwo Workflow

Use this skill before or during non-trivial AI-assisted software development when the work needs coordination across implementation, product, design, docs, review, debugging, release, project onboarding, or multiple Noootwo skills. Also use it at submit, release, or handoff time when lifecycle checks are needed.

## Operating Goal

Keep work moving through a controlled loop:

`intake -> lifecycle guardrails -> repo truth -> route/mode -> product/design/docs/review specialist -> plan -> execute -> verify -> document -> review -> submit/release/handoff`

Default to the lightest flow that can still prove the result. Load deeper references only when the task needs them.

Lifecycle guardrails are always decisions, not always visible ceremony. Small direct work can pass them internally; non-trivial, submit-bound, or release-bound work should state the guardrail result briefly.

Use an `alignment checkpoint` only when it prevents a likely wrong turn. It is a small decision control, not a meeting or questionnaire.

## Lifecycle Guardrails

Before acting at a development, close, submit, release, or handoff point, decide:

- `read-first`: which repo truth must be checked first: `AGENTS.md`, README, `docs/status.md`, ADRs, specs, release notes, package/build metadata, changed files, or only the nearest file context.
- `pre-implementation`: whether the work needs an alignment checkpoint, product choice challenge, TDD/repro-first path, specialist routing, or a verification command before editing.
- `during-work`: whether the work must be split into verifiable slices to avoid speculative abstractions, dependency bloat, or docs/implementation drift.
- `pre-close/pre-submit`: whether changed behavior was verified, docs/status/release notes need updates, and `$noootwo-product`, `$noootwo-design`, or `$noootwo-review` must inspect risk before closing, committing, or releasing.

Do not turn these into a checklist for the user. State them only when the work is non-trivial, the user is about to receive a completed handoff, or a submit/release gate is being crossed.

## First Pass

1. Run the lifecycle guardrails at the lightest useful level.
2. Read the nearest operating truth first: `AGENTS.md`, README, active `docs/status.md`, release notes, package/build metadata, and changed-file context.
3. Classify the work by primary motion: `small edit`, `feature`, `product`, `bugfix`, `refactor`, `release/ops`, `design`, `documentation`, `review-only`, or `recovery`.
4. Identify risks before editing: unclear intent, unclear real user, unclear product path, wide blast radius, migration/data risk, brittle tests, public API change, documentation drift, review ambiguity, or missing verification path.
5. Choose a mode:
   - `direct`: small localized work with an obvious check
   - `planned`: multi-file behavior or public workflow change
   - `diagnostic`: bug, failure, regression, or surprising behavior
   - `release`: version, tag, publish, CI, install, or repo metadata work
   - `onboarding`: unfamiliar project, missing process foundation, unclear skill needs, or handoff from another agent
   - `recovery`: prior agent drift, repeated failed fixes, or unclear handoff
6. Do not add ceremony to direct work; do not skip evidence for risky work.

## Alignment Checkpoint

Trigger this before editing only when the task is non-trivial and a decision could materially change the work: ambiguous goal, product scope, user path, high-risk change, multi-file behavior, release, design direction, architecture boundary, public API, migration, or missing verification path.

Run the checkpoint in four steps:

1. Inspect repo truth first.
2. Name the single highest-impact unresolved decision.
3. Offer 2-3 meaningful options with one recommended default.
4. Record one outcome: `user chose`, `user delegated to agent`, or `no question needed`.

Skip it for small direct edits with an obvious verification path.

If the highest-impact unresolved decision is about the real user, feature scope, information architecture, interaction model, states, acceptance criteria, or whether something should be built at all, route to `$noootwo-product` for a Product Choice Challenge instead of deciding it inside workflow.

## Skill Routing

- Use this skill first when a project needs a skill inventory, foundation health check, gap plan, or multi-skill handoff.
- Use `$noootwo-product` when requirements, feature scope, real user, user flow, information architecture, interaction model, onboarding, permissions, states, acceptance criteria, usability, cognitive cost, or a product choice is unclear.
- Use `$noootwo-design` when the product path is clear enough and the work changes UI, visual direction, artifact review, `.noootwo/` deliverables, design systems, screenshots, or frontend implementation handoff.
- Use `$noootwo-review` when the work needs maintainability judgment, refactoring, architecture-boundary judgment, code structure review, test strategy review, performance review, or a second pass before release.
- Use `$noootwo-docs` when the work changes project state, public usage, product decisions, architecture decisions, README, AGENTS, docs, or release notes.
- Stay in this skill when the main problem is sequencing, scope control, routing, or making several skills cooperate.

If two skills apply, use this order unless the user says otherwise:

`workflow -> product when needed -> design/review/docs specialist -> workflow closure`

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
- Use TDD or a repro-first path for bugfixes, behavior changes, public contracts, regression risk, or code whose behavior is not otherwise provable.
- Do not duplicate long background context into multiple files.
- Do not let implementation or UI work proceed on unclear product paths; route to `$noootwo-product` first when user task, scope, states, or acceptance criteria are ambiguous.
- Do not let documentation, implementation, and review drift apart; route to `$noootwo-docs` before closing work that changes project behavior or state.
- Route to `$noootwo-review` before submit or release for code changes. Small diffs can be self-reviewed and directly fixed; larger or risky diffs need a structured review gate.

## Handoff Contract

When routing to another Noootwo skill, pass a compact handoff packet:

- task class and chosen mode
- relevant files or artifacts
- known constraints and non-goals
- verification command or missing verification path
- decision needed from the specialist

For `$noootwo-product`, include the suspected real user, desired outcome, unclear product choice, current flow evidence, and whether UI or implementation is waiting on the answer.

When control returns, close the loop by checking whether docs, review, release, or user confirmation is still missing.

## Completion Gate

Before calling non-direct work done, or before submitting or releasing code changes, answer the closure triggers:

- Was the changed behavior verified with the closest meaningful check?
- Was TDD/repro-first needed, and if so was it used or recorded as a gap?
- Did user-facing docs, status, ADRs, or release notes need updates?
- Does the result need `$noootwo-product`, `$noootwo-design`, or `$noootwo-review` to inspect product acceptance, artifact quality, or implementation risk?
- If this is submit or release-bound code, did the review gate run or intentionally pass as a small self-review?

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
