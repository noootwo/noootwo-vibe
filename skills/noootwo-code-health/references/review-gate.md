# Review Gate

Use after every non-direct behavior change, before implementation when structure blocks the change, and before submit, release, or implementation handoff. This is the decision boundary for scope, verification, refactoring, and user acceptance.

## When the gate is mandatory

- A behavior-changing code change was reported done.
- A change is about to be submitted, released, or handed off.
- The same area is being revised repeatedly, context cost is growing, or the same implementation was rejected twice.
- A Structure Sweep trigger fired.

A code change reaching submit or release without a review decision is not closed. Direct single-file edits with an obvious check may close normally, but they still follow the same two-hat and verification rules internally.

## Scope

- Default change review scope is the current diff, its nearest callers, tests, and boundary.
- Refactoring inside the touched path is part of reviewing the change, not scope expansion.
- A Structure Sweep or broad refactor runs when triggered or when the user explicitly asks.
- Before expanding into unrelated areas, stop and ask. A local cleanup with one safe answer does not need a question.

## Two hats and the TDD precondition

- Behavior-changing code must have credible test evidence before structural review.
- If tests are missing, brittle, or assert implementation rather than behavior, stop and invoke `noootwo-tdd`: read its `SKILL.md` and follow it.
- Never mix the adding-function hat with the refactoring hat. After green, switch deliberately to refactoring; after the refactor, return to green.
- Review consumes green test evidence; it does not teach the TDD loop.

## Review decision

Select lenses before reading widely. A small diff uses one to three lenses; a risky or release-bound diff includes correctness and testability.

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
- Both are changes, not findings; after either, rerun the closest full relevant test command.

## Re-test gate

A refactor or optimization is not accepted until:

- the behavior-preserving baseline stayed green,
- the full relevant test command is green,
- verification gaps are named explicitly when no practical test exists.

## User acceptance gate

For non-direct code changes, and for every refactor or optimization:

- stop and report the result,
- wait for explicit user acceptance,
- do not commit, push, tag, or publish before that acceptance.

Direct single-file edits with an obvious check and no structural change may close normally after verification.

## Output

For a structured review include applied lenses, skipped lenses and why, evidence read, findings, verification gaps, re-test evidence, refactoring disposition, acceptance state, and owning skill for each handoff.
