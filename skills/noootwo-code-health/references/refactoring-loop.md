# Refactoring Loop

Refactoring changes structure, not behavior. It is a series of small behavior-preserving transformations, each kept on a green baseline. The workflow selection and philosophy live in [refactoring-workflows.md](refactoring-workflows.md).

## Enter the loop

Choose the workflow first:

- **Preparatory** — the desired change is hard because the current structure is wrong; make the change easy first.
- **TDD** — the behavior change is green; improve the structure the change exposed.
- **Litter-pickup** — you are already in messy code; make one small improvement and leave it better.
- **Comprehension** — you had to work to understand the code; move that understanding into names, functions, and boundaries.
- **Planned** — a larger area needs a bounded dedicated pass.
- **Long-term** — the end-state spans iterations; move toward it through ordinary work.

Refactor now only when at least one is true:

- the current structure makes the requested change harder, riskier, or more expensive;
- you had to load unrelated context or reconstruct understanding to make the change;
- the same concept has two or more implementations drifting apart;
- the current shape already caused a bug, missed test, or review confusion;
- a small extraction makes this change safer now;
- a planned or long-term restructuring is already moving through this area.

Do not refactor only for naming taste, a hypothetical future variant, or to make a stable and rarely touched area look prettier. Record an accepted risk instead when the payback is not credible.

## Two hats

Wear only one hat at a time.

1. **Adding-function hat** — change behavior or contracts, add tests, expect red.
2. **Refactoring hat** — preserve observable behavior, keep tests green, make a small structural move.

Switch deliberately. Do not hide a behavior change inside a cleanup, and do not clean up while the behavior is still red.

## Preserve behavior

1. Name the behavior that must stay true.
2. Confirm the relevant test command is green before touching structure.
3. If no credible test covers the behavior, stop and add a red-green test first through `noootwo-tdd`.
4. Make one small mechanical move: extract, inline, rename, move, split, encapsulate, or simplify.
5. Run the tests after each step.
6. If a step fails, assume the refactoring step is wrong and revert it before continuing.
7. Do not bundle semantic changes with cleanup.

Use the catalog as vocabulary, not as ceremony. The default first moves are Extract Function, Extract Variable, Change Function Declaration, Move Function, Replace Nested Conditional with Guard Clauses, Introduce Parameter Object, Split Phase, Remove Dead Code, and Replace Loop with Pipeline. Choose the smallest move that removes the actual pressure.

## Keep scope honest

- Default to the touched path and its nearest boundary.
- Refactoring the touched path is part of the change; refactoring unrelated areas needs a trigger or user request.
- Prefer existing repo patterns over a new abstraction.
- Do not introduce an abstraction for a hypothetical future variant.
- Stop before the yak shave: leave the next improvement as an `opportunity` with a revisit trigger.

## Close the loop

1. Run the full relevant test command.
2. Confirm behavior evidence still matches.
3. Record the workflow used, the catalog move, behavior preserved, tests run, and scope.
4. Record every remaining structural finding with a disposition: `opportunity`, `planned`, `long-term`, or `accepted`.
5. Return to [review-gate.md](review-gate.md) for re-test and user acceptance.

Do not submit or release from inside this loop.
