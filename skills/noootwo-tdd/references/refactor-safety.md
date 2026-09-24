# Refactor Safety

Refactoring changes structure, not behavior. The proof of that difference is a green test command before and after. The structural workflow and philosophy live in `noootwo-code-health` `references/refactoring-workflows.md`; this file owns the safety inside the TDD loop.

## Two hats

Red and green are the adding-function hat. The refactor step is the refactoring hat. Never wear both at once: finish the behavior change, return to green, then improve structure without adding behavior.

## Before touching structure

- Name the behavior that must stay true.
- Confirm the relevant test command is green.
- If no test covers the behavior, stop and add a red-green test first.

## During the change

- Make small mechanical moves: extract a function, inline a weak abstraction, rename to expose intent, or clarify a boundary.
- One concept per step. Do not bundle a semantic fix with cleanup.
- Keep tests green after each step. If a step breaks them, stop and find the mechanical mistake.
- Prefer existing repo patterns over a new abstraction.
- Do not introduce an abstraction for a hypothetical future variant.
- If the touched code is hard to understand, that is a comprehension signal: move the understanding into names or functions rather than leaving a comment that explains the confusion.
- If the area is messy, one small litter-pickup improvement is better than no improvement; stop before the yak shave.

## After the change

- Run the full relevant test command.
- Diff behavior evidence: same public inputs and outputs, same side effects, no new contracts.
- Return to `noootwo-code-health` or `noootwo-workflow` for the review gate. Record any remaining structural finding with a disposition instead of leaving it as an untracked future improvement. Do not self-certify submit or release.

## Defer when

- The only reason is naming preference.
- The change would touch unrelated code without a test boundary.
- The rewrite bundles cleanup with behavior changes.
- The area is stable and rarely touched, and the refactoring payback is not credible; record it as accepted risk instead of forcing work now.
