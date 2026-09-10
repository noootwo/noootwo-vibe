# noootwo-review Releases

## v0.9.0

- Restructured around a lens table, sizing rules, a five-step method, and a hand-off map.
- Added the explicit hand-off phrasing used across the suite: invoke the owning skill by loading its `SKILL.md`.
- Cut the description from 513 to 174 characters.


## v0.8.0

- Added hard pre-submit/release triggers: any code change reaching submit or release needs a review decision; risky, public-contract, migration, or wide-blast-radius diffs always review.
- Added a `rework diagnosis` lens for repeated rejection of the same implementation, routing to Product, Design, or verification.


## v0.7.1

- Expanded lean/context-cost review to flag broad skill triggers, fixed question lists, oversized skill flows, and default gates heavier than task risk.
- Clarified that Decision Interview should stay one material question at a time, not become a fixed questionnaire.

## v0.7.0

- Reframed `noootwo-review` as Tech Lead + QA Architect for code quality, architecture-boundary review, technical judgment, test strategy, performance, maintainability, and release readiness.
- Clarified that architecture remains a review lens; no public `noootwo-architecture` skill is introduced.
- Added Product handoff language for product behavior, user-flow, state, or acceptance ambiguity discovered during review.

## v0.6.1

- Added a pre-submit review gate for code changes before commit, release, or implementation handoff.
- Clarified diff-size behavior: small diffs get narrow self-review and direct fixes; medium, broad, risky, or release-bound diffs get structured lens-based review.
- Added the user-escalation boundary for review fixes that expand scope, change product behavior, alter dependencies, or require larger refactoring.

## v0.6.0

- Added an explicit Review Lens Selector covering correctness, testability, architecture boundaries, lean/bloat, performance, project health, AI-code/context cost, and release readiness.
- Updated review output expectations to record applied lenses, skipped lenses, evidence read, smallest fixes, verification gaps, and handoff owners.
- Clarified that narrow diffs should use only relevant lenses instead of becoming full project audits.

## v0.5.0

- Added performance review for frontend loading/rendering, backend/API latency, database/query cost, algorithm/runtime hotspots, resource use, and performance regression risk.
- Added `references/performance-review.md` with the evidence ladder, `Performance Findings` output, project-level performance defects, and before/after honesty boundary.
- Kept performance review evidence-first: missing baselines, traces, query plans, benchmarks, or production metrics are verification gaps, not grounds for speculative rewrites.

## v0.4.0

- Added lean review for over-engineering, redundant code, YAGNI violations, dependency bloat, and token-cost expansion.
- Added `references/lean-code-review.md` with the seven-rung reduction check, `Lean Findings` output, safety floor, and gain honesty boundary.
- Added selected Ponytail source and MIT license notes under `references/external/ponytail/` without vendoring the full external repository.

## v0.3.0

- Added project-health review for validation entrypoints, CI, module boundaries, release risk, context cost, and duplicated truth sources.
- Added `Project Defects` output for engineering-health gaps outside a narrow code diff.
- Clarified review handoff boundaries with workflow and docs.

## v0.2.0

- Added code-health risk classes, AI-generated code risk checks, and severity guidance.
- Expanded the review playbook with refactor decision gates, review output shape, and AI code smells.
- Clarified that review should reduce concrete risk without expanding scope into speculative rewrites.

## v0.1.0

- Initial public skill for code quality review, maintainability, refactoring discipline, architecture hygiene, and test strategy review.
