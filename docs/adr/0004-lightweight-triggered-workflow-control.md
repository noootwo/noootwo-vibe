# ADR 0004: Use lightweight triggered workflow control

- Status: accepted
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

## Consequences

- Small edits keep low overhead.
- Risky work gets a visible decision checkpoint before implementation.
- Review becomes broader in capability without making every review a full project audit.
- Design quality gates remain available for serious UI work, while local polish stays practical.
- Future changes should prefer shrinking default instructions before adding more default process.
