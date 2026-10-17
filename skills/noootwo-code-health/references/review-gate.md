# Review Gate

Use before implementation when the integration shape is non-obvious, after every non-direct behavior change, and before release or a ship-readiness submit gate. This is the decision boundary for verification depth, scope, refactoring, and user acceptance.

## When the gate is mandatory

- A behavior-changing code change is about to be reported done.
- A non-obvious change needs a seam, contract, or data-flow decision before implementation.
- A change is about to be released or pass a ship-readiness submit gate, or handed off with unresolved risk.
- The same area is being revised repeatedly, context cost is growing, or the same implementation was rejected twice.
- A Structure Sweep trigger fired.

A code change reaching release without a review decision is not closed. Direct single-file edits with an obvious check may close normally, but they still follow the same two-hat and verification rules internally. A local change with an obvious seam and no contract, data, or migration impact also skips the Integration Read.

## Verification depth

Match verification to blast radius, not diff size or task length.

| Depth | Use | Evidence |
| --- | --- | --- |
| `change` | one completed requirement | current diff, changed behavior, nearest callers, affected tests, one to three lenses, the closest meaningful command; nearest integration check only when a seam is crossed |
| `escalated` | public contract, shared data/schema/migration, auth or security boundary, shared module with broad callers, build/release config, or unclear/flaky impact | the `change` evidence plus affected suites and only the lenses that risk requires |
| `release` | before release or a ship-readiness submit gate | full suite or CI for the exact commit, full Structure Sweep, release evidence, and named gaps |

Do not run a Release Check after every requirement. A long task or a large diff does not by itself trigger one; blast radius does. Existing CI for the exact commit can satisfy the full-suite part without a local rerun.

Prefer the project's affected-test or test-impact entry point when it exists; otherwise use the package or module suite, then the nearest integration test when a seam is crossed.

## Integration Read gate

Before implementing a non-obvious behavior change:

- read `integration-read.md` and produce a Change Shape;
- name the seam, owning boundary, contract, reuse decision, reversibility, test seam, smallest first slice, and rejected alternatives or why none existed;
- do not write production behavior until the shape is settled or explicitly deferred; a material or hard-to-reverse tradeoff waits for the user's choice;
- a preparatory refactor is the next step only when the Change Shape shows it makes the behavior change safe.

## Scope

- Change Check scope is the current diff, its nearest callers, tests, and boundary.
- Release Check scope is the full project and release surface.
- Refactoring inside the touched path is part of reviewing the change, not scope expansion.
- A Structure Sweep or broad refactor runs when triggered or when the user explicitly asks.
- Before expanding into unrelated areas, stop and ask. A local cleanup with one safe answer does not need a question.

## Two hats and the TDD precondition

- Behavior-changing code must have credible test evidence before structural review.
- If tests are missing, brittle, or assert implementation rather than behavior, stop and invoke `noootwo-tdd`: read its `SKILL.md` and follow it.
- Never mix the adding-function hat with the refactoring hat. After green, switch deliberately to refactoring; after the refactor, return to green.
- Review consumes green test evidence; it does not teach the TDD loop.

## Review decision

Select lenses before reading widely. A Change Check uses one to three lenses; an escalated or Release Check includes correctness and testability.

Use code smells as surface indications, not automatic defects. Report findings ordered by severity. Do not inflate severity to force cleanup, and do not hide real structural pressure behind a future-improvement label.

## Refactoring disposition

Every structural finding gets exactly one disposition:

- `fixed now` — the smallest safe catalog move was applied in this pass and the baseline is green.
- `opportunity` — noted for the next time this area is changed; no planned ceremony.
- `planned` — a larger area needs a bounded planned-refactoring pass.
- `long-term` — the end-state spans iterations; record the rough direction and Branch by Abstraction or another safe interim shape.
- `accepted` — stable, rarely touched, and not worth the investment now; record why and what would reopen it.

Persist opportunity, planned, long-term, and accepted items through `noootwo-state`. A finding with no disposition is not reviewed.

## Refactor and optimization

- Refactor = behavior-preserving structural change. Use `refactoring-workflows.md` and `refactoring-loop.md`.
- Optimization = measured metric change. Use `optimization-loop.md`.
- Both are changes, not findings; after either, rerun the command that covered the refactored behavior and nearest boundary.

## Re-test gate

A refactor or optimization is not accepted until:

- the behavior-preserving baseline stayed green,
- the relevant command for the touched behavior and nearest boundary is green,
- verification gaps are named explicitly when no practical test exists.

## User acceptance gate

For non-direct code changes, and for every refactor or optimization:

- stop and report the result,
- wait for explicit user acceptance,
- do not commit, push, tag, or publish before that acceptance.

Direct single-file edits with an obvious check and no structural change may close normally after verification.

## Output

For an Integration Read include the Change Shape, one-way doors, smallest first slice, and what would change the shape. For a structured review include `Verification: change | escalated | release`, applied and skipped lenses, evidence read, findings, verification gaps, re-test evidence, refactoring disposition, acceptance state, and owning skill for each handoff.
