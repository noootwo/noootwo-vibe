# 0015 — The review skill owns Fowler's refactoring health loop

## Status

Accepted.

## Context

Review previously behaved as a gate on the current diff. It deliberately deferred
whole-project review and explicitly told the reviewer not to inspect large files
outside the current path. That prevented scope creep, but it also meant structural
debt had no owner: findings were called future improvements and then disappeared.

Martin Fowler's *Refactoring* (2nd edition) and the *Workflows of Refactoring*
material describe a different model: small behavior-preserving transformations,
two hats that never mix, a green baseline, six complementary workflows, and
economic payback focused on frequently changed code. Planned refactoring is
useful for larger areas, but planned-only refactoring is itself a smell.

## Decision

- Make review part of done for every non-direct behavior change, not only a
  submit or release gate.
- Add preparatory review before implementation when the existing structure makes
  the requested change hard.
- Adopt the six workflows: TDD, litter-pickup, comprehension, preparatory,
  planned, and long-term refactoring.
- Require two hats to stay separate: adding function changes behavior and tests;
  refactoring preserves observable behavior on a green baseline.
- Use the refactoring catalog as shared vocabulary and choose the smallest move
  that removes the actual pressure.
- Give every structural finding one disposition: `fixed now`, `opportunity`,
  `planned`, `long-term`, or `accepted`. Persist non-local items through
  `noootwo-state` rather than maintaining a private review file.
- Add a triggered Structure Sweep for release, repeated edits, context-cost
  growth, new boundaries, due planned/long-term work, or an explicit request.

## Consequences

- A structure problem is no longer silently ignored just because it is outside
  the current diff.
- A large file does not automatically become a rewrite. It receives the smallest
  safe improvement in the touched path, a bounded planned pass, a long-term
  direction, or an explicitly accepted risk.
- Review, TDD, workflow, and state now share one loop: discover, record,
  schedule, refactor in small steps, re-test, and close.
