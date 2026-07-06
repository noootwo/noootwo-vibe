---
name: noootwo-review
description: Use for code quality, maintainability, refactoring discipline, architecture hygiene, implementation review, test strategy review, project-health review, lean review, over-engineering, bloat, YAGNI, redundant code, unnecessary dependencies, token-cost control, AI-generated code risk, review findings, code-health triage, and preventing software from becoming unstable, under-verified, over-abstracted, hard to change, or expensive to reason about.
---

# Noootwo Review

Use this skill when the project needs code to stay easy to understand, change, test, and review. It is a code-health and implementation-review skill, not a style-only critique.

It can report project-level defects when they affect engineering health, such as missing validation entrypoints, unclear CI, unreproducible release flow, unstable module boundaries, or duplicated sources of truth. It classifies those defects and hands ownership to `$noootwo-workflow` or `$noootwo-docs` when appropriate.

It can also run a lean review for over-engineering, code bloat, unnecessary abstraction, avoidable dependencies, and AI-generated code expansion. Lean review reduces only unnecessary code; it never removes safety, validation, accessibility, or required behavior.

## Review Stance

Prioritize concrete risk over aesthetic preference:

- behavioral regressions
- unclear ownership or module boundaries
- changes that are too large to review safely
- duplication that causes repeated edits or drift
- abstractions with no current pressure
- over-engineered code, redundant layers, avoidable dependencies, and token-cost bloat
- missing tests around shared behavior
- files that force agents to load too much context
- docs, comments, or names that hide the real model

Do not expand scope just because code can be improved. Review the current change and the smallest structural move that reduces real risk.

## First Pass

1. Read the changed files, nearest tests, callers, public interfaces, and docs that describe the behavior.
2. Identify the behavior that must remain true and the evidence that proves it.
3. Classify risk: `correctness`, `changeability`, `reviewability`, `testability`, `operability`, or `context cost`.
4. Identify the smallest structure that supports the current requirement.
5. Separate defects from future improvements.
6. Prefer local fixes unless the same friction appears in multiple places.

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

Use severity labels only when useful:

- `P0`: data loss, security, broken release, or user-blocking regression
- `P1`: likely behavioral bug, brittle migration, or broken contract
- `P2`: maintainability issue likely to cause near-term mistakes
- `P3`: optional cleanup or clarity improvement

When reviewing the whole project rather than a narrow diff, add `Project Defects` after code findings. Examples: no validation entrypoint, no status document, release flow cannot be reproduced, skill routing is unclear, or duplicated truth sources create context cost.

When the user asks for lean review, bloat review, YAGNI review, dependency trimming, token-cost reduction, or over-engineering cleanup, use `Lean Findings` from `references/lean-code-review.md` before broader review commentary.

## Closure Gate

Before approving or finishing work, verify:

- tests or checks cover the changed behavior
- module boundaries match current responsibility
- no speculative framework or dependency was added
- public docs or release notes were routed to `$noootwo-docs` when needed
- broader workflow or skill routing was routed to `$noootwo-workflow` when needed

For deeper guidance, read:

- `references/code-quality-playbook.md` when planning a refactor, reviewing architecture, deciding whether to split files, or evaluating repeated AI implementation friction.
- `references/lean-code-review.md` when reviewing over-engineering, redundant code, YAGNI violations, dependency bloat, or token-cost expansion.
- `references/project-health-review.md` when reviewing project foundation, validation paths, release risk, CI, module boundaries, context cost, or repeated AI friction.
