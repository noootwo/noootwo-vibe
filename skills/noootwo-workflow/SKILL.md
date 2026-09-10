---
name: noootwo-workflow
description: "Use at the start of any new feature, product idea, multi-file or cross-skill change, bugfix or failing check, refactor, release/version/tag/publish, project onboarding or handoff, recovery after repeated failed fixes, or correction-loop routing after a user rejection. Runs lifecycle guardrails, repo-truth reading, mode selection, specialist routing, planning, verification, documentation, and submit/release closure. Routes to $noootwo-product, $noootwo-design, $noootwo-review, and $noootwo-docs when their triggers match."
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
3. Classify the work by primary motion: `small edit`, `feature`, `product discovery`, `product`, `bugfix`, `refactor`, `release/ops`, `design`, `documentation`, `review-only`, or `recovery`.
4. Identify risks before editing: unclear intent, unclear real user, unclear product path, wide blast radius, migration/data risk, brittle tests, public API change, documentation drift, review ambiguity, or missing verification path.
5. Choose a mode:
   - `direct`: small localized work with an obvious check
   - `planned`: multi-file behavior or public workflow change
   - `diagnostic`: bug, failure, regression, or surprising behavior
   - `release`: version, tag, publish, CI, install, or repo metadata work
   - `onboarding`: unfamiliar project, missing process foundation, unclear skill needs, or handoff from another agent
   - `recovery`: prior agent drift, repeated failed fixes, or unclear handoff
6. Do not add ceremony to direct work; do not skip evidence for risky work.
7. If the user strongly rejects product sense, style understanding, or usability, classify the failed layer before making more small edits.

## Alignment Checkpoint

Trigger this before editing only when the task is non-trivial and a decision could materially change the work: ambiguous goal, product scope, user path, high-risk change, multi-file behavior, release, design direction, architecture boundary, public API, migration, or missing verification path.

Run the checkpoint in four steps:

1. Inspect repo truth first.
2. Name the single highest-impact unresolved decision.
3. Offer 2-3 meaningful options with one recommended default.
4. Record one outcome: `user chose`, `user delegated to agent`, or `no question needed`.

Skip it for small direct edits with an obvious verification path.

If the highest-impact unresolved decision is about a product idea, real user, feature scope, information architecture, interaction model, states, acceptance criteria, or whether something should be built at all, route to `$noootwo-product` for its Clarity Gate. Product starts Decision Interview only when a material choice remains; a request whose user/target, scenario, outcome, scope boundary, main path, relevant states, and acceptance are already clear proceeds without an interview.

Do not run a long product interview inside Workflow. If one checkpoint reveals more unresolved product decisions, hand off to `$noootwo-product` Decision Interview with the highest-impact ambiguity and the facts already checked.

When Product's Clarity Gate opens Decision Interview, enter `product-interview` mode and pause execution. A plain request to build, continue, start, or follow best practices is not delegation of unresolved product choices. Until Product returns `ready_for_handoff` or the user explicitly delegates the choices, Workflow may inspect facts read-only but must not edit files, create implementation plans, route to Design, or begin implementation. Carry `waiting_on: user_answer` and `execution_status: blocked` in the handoff so downstream skills cannot mistake a recommendation for approval. Do not enter this pause for a clear request.

## Skill Routing

Routing is an invocation, not a thought. When a specialist trigger matches, explicitly invoke `$noootwo-product`, `$noootwo-design`, `$noootwo-review`, or `$noootwo-docs` at that moment. If the skill is unavailable in the current harness, say so in one line and follow the closest fallback instead of silently skipping.

- Use this skill first when a project needs a skill inventory, foundation health check, gap plan, or multi-skill handoff.
- Use `$noootwo-product` first when the task is a greenfield software product idea, blank-project product start, broad product vision, product brainstorm, or "what should this become" question.
- Use `$noootwo-product` Decision Interview only when requirements, feature scope, real user, user flow, information architecture, interaction model, onboarding, permissions, states, acceptance criteria, usability, cognitive cost, or product choices still need one-at-a-time confirmation after the Clarity Gate.
- Use `$noootwo-design` when the product path is clear enough and the work changes UI, visual direction, artifact review, `.noootwo/` deliverables, design systems, screenshots, or frontend implementation handoff. For non-quick UI work, Product-to-Design Handoff should include real user, main path, states, and acceptance criteria.
- Use `$noootwo-review` when the work needs maintainability judgment, refactoring, architecture-boundary judgment, code structure review, test strategy review, performance review, or a second pass before release.
- Use `$noootwo-docs` when the work changes project state, public usage, product decisions, architecture decisions, README, AGENTS, docs, or release notes.
- Stay in this skill when the main problem is sequencing, scope control, routing, or making several skills cooperate.

If two skills apply, use this order unless the user says otherwise:

`workflow -> product when needed -> design/review/docs specialist -> workflow closure`

If the task is a bug or failing check, first establish root cause and reproduction before routing to implementation or review.

When the user rejects prior work, diagnose the failed layer before another small edit: product misunderstanding routes to `$noootwo-product` (Clarity Gate or Product Reality Check), style/visual misunderstanding routes to `$noootwo-design` (Style Evidence Check), implementation translation routes to `$noootwo-design` detail pass or `$noootwo-review`, and stale documentation routes to `$noootwo-docs`. State the diagnosis and the invoked skill; do not keep polishing the same layer.

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
- Before reading a long document, use local search first: `rg --files`, `rg -n` headings/keywords/paths, then bounded `sed` ranges. Read the whole file only for whole-document audits, consistency checks, or when targeted search fails.
- Use TDD or a repro-first path for bugfixes, behavior changes, public contracts, regression risk, or code whose behavior is not otherwise provable.
- Do not execute a product implementation while a Product Decision Interview is waiting for an answer. Product's recommended default is not a resolved decision; execution starts only after explicit user selection, explicit delegation, or a no-question-needed determination grounded in checked facts. A clear product request is not waiting merely because it is product-shaped.
- Do not duplicate long background context into multiple files.
- Do not let implementation or UI work proceed on unclear product paths; route to `$noootwo-product` first when user task, scope, states, or acceptance criteria are ambiguous.
- Do not ask repeated product questions from Workflow; route the question sequence to `$noootwo-product` once more than one material product decision remains.
- Preserve an explicit request for grill-style or detailed confirmation across routing; Workflow should pass the deep-interview signal to `$noootwo-product`, not compress it into a light checkpoint.
- Do not keep polishing after repeated user correction. One strong rejection triggers layer diagnosis; two related rejections trigger Product Reality Check or Style Evidence Check before more implementation.
- Do not let documentation, implementation, and review drift apart; route to `$noootwo-docs` before closing work that changes project behavior or state.
- Route to `$noootwo-review` before submit or release for code changes. Small diffs can be self-reviewed and directly fixed; larger or risky diffs need a structured review gate.

## Handoff Contract

When routing to another Noootwo skill, pass a compact handoff packet:

- task class and chosen mode
- relevant files or artifacts
- known constraints and non-goals
- verification command or missing verification path
- decision needed from the specialist
- execution status: blocked on user answer | ready for handoff | ready for execution
- presentation language: infer from the user's latest message; preserve intentional technical terms

Specialist packets:

- To `$noootwo-product`: use `references/product-interview-handoff.md`; include the raw idea, any explicit grill-style/detail-confirmation request, Clarity Gate result, `interview_depth`, checked facts with sources, initialized decision ledger, intent-fit status, and whether UI or implementation is waiting. A pending packet is a pause state, not a ready handoff.
- To `$noootwo-design`: include the Product-to-Design Handoff when available (real user, scenario, main path, states, scope cuts, acceptance criteria, open product decisions, design constraints), current UI/artifacts, and the review path.
- To `$noootwo-review`: include behavior/structure changed, files and nearest tests, risk class, verification command, and the specific judgment requested.
- To `$noootwo-docs`: include the changed fact, owning layer, files/commands touched, validation or release evidence, and known stale docs to check.
- Correction loops: include what the user rejected, the suspected failed layer (product, style understanding, implementation translation, artifact review, unclear evidence), and whether Product Reality Check or Style Evidence Check is required.

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
- `references/product-interview-handoff.md` when routing deep or detailed product confirmation through Workflow.
- `references/workflow-playbook.md` when planning a multi-step implementation, diagnostic recovery, or release workflow.
