---
name: noootwo-review
description: Use as the Noootwo Tech Lead and QA Architect skill for lens-based code quality, technical judgment, architecture boundary review, pre-submit review gates, maintainability, refactoring discipline, implementation review, test strategy review, project-health review, performance review, frontend loading/rendering, backend/API latency, database/query cost, algorithm hotspots, lean review, over-engineering, bloat, YAGNI, redundant code, unnecessary dependencies, token-cost control, AI-generated code risk, review findings, code-health triage, release readiness, and preventing software from becoming unstable, under-verified, over-abstracted, slow, hard to change, or expensive to reason about. Architecture is a review lens here; do not create or route to a separate noootwo-architecture skill.
---

# Noootwo Review

Use this skill when the project needs code to stay easy to understand, change, test, and review. It is a Tech Lead and QA Architect skill for technical judgment, code health, and implementation review, not a style-only critique.

Architecture, test strategy, performance, maintainability, and technical tradeoff judgment stay here as review lenses. Do not split them into a public `noootwo-architecture` skill.

It can report project-level defects when they affect engineering health, such as missing validation entrypoints, unclear CI, unreproducible release flow, unstable module boundaries, or duplicated sources of truth. It classifies those defects and hands ownership to `$noootwo-workflow` or `$noootwo-docs` when appropriate. Product behavior or user-flow questions route to `$noootwo-product` instead of being solved as code style.

It can also run a lean review for over-engineering, code bloat, unnecessary abstraction, avoidable dependencies, and AI-generated code expansion. Lean review reduces only unnecessary code; it never removes safety, validation, accessibility, or required behavior.

It can also run a performance review for frontend loading/rendering, backend/API latency, database/query cost, algorithm/runtime hotspots, resource use, and performance regression risk. Performance review requires evidence: baseline, trace, profiler output, query plan, benchmark, or a clearly reported verification gap.

## Review Lens Selector

Choose review lenses before reading too broadly. A narrow diff should use only the lenses that match the change; a project audit or release review may use several.

- `correctness`: behavior, contracts, data integrity, security, migrations, release breakage
- `testability`: missing or brittle proof for changed behavior
- `architecture boundary`: ownership, public interfaces, module/package boundaries, data ownership, duplicated source of truth
- `lean/bloat`: over-engineering, YAGNI, unnecessary dependencies, redundant code, context-cost expansion
- `performance`: loading, rendering, API latency, query cost, algorithm/runtime hotspots, resource use
- `project health`: validation entrypoints, CI, release path, docs/status drift, observability, handoff risk
- `AI-code/context cost`: large files, generic wrappers, hidden state, repeated rules, comments that overclaim
- `release readiness`: versioning, tags, publish/install steps, rollback, user-visible notes

State which lenses were applied, which obvious lenses were skipped, and why.

## Pre-Submit Review Gate

Use this gate before submitting or releasing code changes, and when `$noootwo-workflow` routes a completed implementation for quality review.

- Small diff: choose one to three relevant lenses, self-review the changed files and nearest tests, directly fix local issues, and avoid a full project audit.
- Medium, broad, or risky diff: run a structured review with relevant lenses. Include `correctness` and `testability` when behavior changes, plus `architecture boundary`, `lean/bloat`, or `AI-code/context cost` when structure or future maintenance is the risk.
- Release-bound diff: include `release readiness` and project-health evidence for versioning, tags, install, rollback, and user-visible notes.

Ask the user before applying a review fix only when it expands scope, changes product behavior, introduces a larger refactor, adds/removes dependencies, or chooses between real tradeoffs. Route product behavior choices through `$noootwo-workflow` or `$noootwo-product`. Otherwise, make the smallest safe improvement directly.

## Review Stance

Prioritize concrete risk over aesthetic preference:

- behavioral regressions
- unclear ownership or module boundaries
- changes that are too large to review safely
- duplication that causes repeated edits or drift
- abstractions with no current pressure
- over-engineered code, redundant layers, avoidable dependencies, and token-cost bloat
- missing tests around shared behavior
- credible performance risk in loading, rendering, API latency, database/query cost, algorithm complexity, CPU, memory, or throughput
- files that force agents to load too much context
- docs, comments, or names that hide the real model
- product-facing behavior that changed without a Product Checkpoint or acceptance criteria when the user path was ambiguous

Do not expand scope just because code can be improved. Review the current change and the smallest structural move that reduces real risk.

## First Pass

1. Select lenses from the Review Lens Selector.
2. Read the changed files, nearest tests, callers, public interfaces, and docs that describe the behavior.
3. Identify the behavior that must remain true and the evidence that proves it.
4. Classify risk: `correctness`, `changeability`, `reviewability`, `testability`, `operability`, `performance`, or `context cost`.
5. Identify the smallest structure that supports the current requirement.
6. Separate defects from future improvements.
7. Prefer local fixes unless the same friction appears in multiple places.

## Refactoring Rules

- Refactor only with a reason tied to changeability, correctness, reviewability, or repeated friction.
- Keep behavior-preserving refactors separate from behavior changes when practical.
- Add tests before risky refactors when the behavior is not already covered.
- Extract abstractions only when they remove real duplication or clarify an existing concept.
- Prefer focused modules and explicit interfaces over large multi-purpose files.
- Keep generated or AI-assisted code boring at the boundaries: predictable names, simple data flow, clear failure paths.
- Stop refactoring when the next move no longer has a current evidence-backed benefit.

## AI Code Risk Checks

Look specifically for agent-generated failure modes:

- broad files that force future agents to load unrelated context
- duplicated rules across code, docs, prompts, or schemas
- generic abstractions invented before the second concrete use
- hidden state or side effects that make verification expensive
- tests that mirror implementation details but miss user-visible behavior
- comments or docs that claim stability without a proving command
- missing validation, CI, release, or status paths that make future changes expensive
- code added for speculative future needs, hand-rolled standard-library behavior, custom platform features, or wrappers around one implementation

## Output For Reviews

Lead with findings, ordered by severity. For each finding, include:

- exact file/line when available
- why it matters
- concrete failure mode or maintenance cost
- smallest actionable fix

If there are no findings, say so and note remaining test or verification gaps.

For structured reviews, include:

- applied lenses
- skipped lenses and reason when they looked plausible but were out of scope
- evidence read
- findings with smallest fix
- verification gaps
- handoff owner for workflow, docs, or design issues
- handoff owner for product, workflow, docs, or design issues

Use severity labels only when useful:

- `P0`: data loss, security, broken release, or user-blocking regression
- `P1`: likely behavioral bug, brittle migration, or broken contract
- `P2`: maintainability issue likely to cause near-term mistakes
- `P3`: optional cleanup or clarity improvement

When reviewing the whole project rather than a narrow diff, add `Project Defects` after code findings. Examples: no validation entrypoint, no status document, release flow cannot be reproduced, skill routing is unclear, or duplicated truth sources create context cost.

When the user asks for lean review, bloat review, YAGNI review, dependency trimming, token-cost reduction, or over-engineering cleanup, use `Lean Findings` from `references/lean-code-review.md` before broader review commentary.

When the user asks for performance review, slow behavior, latency, throughput, LCP, INP, CLS, bundle size, render jank, N+1, query plans, caching, CPU, memory, algorithm hotspots, or performance regression risk, use `Performance Findings` from `references/performance-review.md` before optional cleanup.

## Closure Gate

Before approving, submitting, releasing, or finishing work, verify:

- tests or checks cover the changed behavior
- module boundaries match current responsibility
- no speculative framework or dependency was added
- small review issues were fixed directly, while large scope changes were routed back to `$noootwo-workflow` or the user
- performance claims are backed by before/after evidence or recorded as verification gaps
- public docs or release notes were routed to `$noootwo-docs` when needed
- product behavior or acceptance ambiguity was routed to `$noootwo-product` when needed
- broader workflow or skill routing was routed to `$noootwo-workflow` when needed

For deeper guidance, read:

- `references/code-quality-playbook.md` when planning a refactor, reviewing architecture, deciding whether to split files, or evaluating repeated AI implementation friction.
- `references/lean-code-review.md` when reviewing over-engineering, redundant code, YAGNI violations, dependency bloat, or token-cost expansion.
- `references/performance-review.md` when reviewing frontend loading/rendering, backend/API latency, database/query cost, algorithm/runtime hotspots, resource use, or performance regression risk.
- `references/project-health-review.md` when reviewing project foundation, validation paths, release risk, CI, module boundaries, context cost, or repeated AI friction.
