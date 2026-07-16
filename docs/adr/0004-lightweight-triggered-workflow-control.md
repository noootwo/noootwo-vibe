# ADR 0004: Use lightweight triggered workflow control

- Status: superseded by ADR 0005 for the public skill set; lifecycle guardrail decisions remain accepted
- Date: 2026-07-09

## Context

Noootwo Vibe already had useful specialist guidance, but much of the control lived inside skill bodies and references. In daily project work, agents were more likely to keep using docs because docs has clear owned artifacts, while workflow, review, and design could feel optional unless explicitly named.

The risk is not only missing guidance. `noootwo-design` already carries a full `.noootwo/` harness, many references, readiness checks, and hard gates for serious design work. Adding another default decision interview or review rubric would increase friction and make small tasks less likely to use the skills at all.

## Decision

Keep the four public skills unchanged. Improve daily adoption by adding small triggered controls instead of new public skills or default gates:

- `noootwo-workflow` owns a lightweight alignment checkpoint for non-trivial work where one unresolved decision can materially change implementation.
- `noootwo-review` owns an explicit review lens selector so narrow diffs stay narrow and broader audits choose their evidence surface deliberately.
- `noootwo-design` keeps standard/deep/production gates, but quick polish does not require bootstrapping or completing the full `.noootwo/` harness.
- Docs records this decision and release notes; no new large guide or fifth public skill is introduced.

Clarification accepted on 2026-07-10: lightweight control does not mean important lifecycle gates are optional. `noootwo-workflow` should require short guardrail judgments at development, close, submit, release, and handoff points: read-first needs, TDD/repro-first needs, verification path, docs-after, and review/design follow-up. These are mandatory decisions, but only become visible process when the task is non-trivial, submit-bound, release-bound, or risky.

`noootwo-review` owns the pre-submit review gate for code changes. Small diffs can be self-reviewed and directly fixed. Medium, broad, risky, or release-bound diffs use a structured lens-based review. The agent asks the user only when a review fix expands scope, changes product behavior, introduces larger refactoring, changes dependencies, or requires a real tradeoff.

## Consequences

- Small edits keep low overhead.
- Risky work gets a visible decision checkpoint before implementation.
- Review becomes broader in capability without making every review a full project audit.
- Design quality gates remain available for serious UI work, while local polish stays practical.
- Submit-bound and release-bound code changes now have a required review judgment without making every small edit a full audit.
- TDD or repro-first remains risk-triggered instead of universal: bugfixes, behavior changes, public contracts, regressions, data/migration risk, and hard-to-prove shared code must decide it before editing.
- Future changes should prefer shrinking default instructions before adding more default process.
