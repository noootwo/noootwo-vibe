# Refactor Safety

Refactoring changes structure, not behavior. The proof of that difference is a green test command before and after.

## Before touching structure

- Name the behavior that must stay true.
- Confirm the relevant test command is green.
- If no test covers the behavior, stop and add a red-green test first.

## During the change

- Make small mechanical moves: extract a function, inline a weak abstraction, split a file, or clarify a boundary.
- One concept per step. Do not bundle a semantic fix with cleanup.
- Keep tests green after each step. If a step breaks them, stop and find the mechanical mistake.
- Prefer existing repo patterns over a new abstraction.
- Do not introduce an abstraction for a hypothetical future variant.

## After the change

- Run the full relevant test command.
- Diff behavior evidence: same public inputs and outputs, same side effects, no new contracts.
- Return to `noootwo-review` or `noootwo-workflow` for the review gate. Do not self-certify submit or release.

## Defer when

- The only reason is naming preference.
- The change would touch unrelated code without a test boundary.
- The file is large but the current task touches one clear area.
- The rewrite bundles cleanup with behavior changes.
