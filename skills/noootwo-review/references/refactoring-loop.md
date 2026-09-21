# Refactoring Loop

Refactoring changes structure, not behavior. Run it only when the current structure costs more than it protects.

## Enter the loop

Refactor now only when at least one is true:

- current behavior is hard to verify because boundaries are unclear
- the same concept has two or more real implementations drifting apart
- repeated edits require loading unrelated context
- the current shape already caused a bug, missed test, or review confusion
- a small extraction will make the requested change safer now

Defer when the only reason is naming preference, a hypothetical future variant, or a large file whose current change touches one clear area.

## Preserve behavior

1. Name the behavior that must stay true.
2. Confirm the relevant test command is green before touching structure.
3. If no test covers the behavior, stop and add a red-green test first through `noootwo-tdd`.
4. Make small mechanical moves: extract, inline, split, or clarify a boundary.
5. Keep tests green after each step.
6. Do not bundle semantic changes with cleanup.

## Keep scope small

- Default to the current change.
- Ask before a broad refactor or one that crosses unrelated modules.
- Separate mechanical moves from semantic changes when possible.
- Prefer existing repo patterns over new abstractions.
- Leave redundant code out of the final state; do not keep it "for later".

## Close the loop

1. Run the full relevant test command.
2. Confirm behavior evidence still matches.
3. Record the refactor in the review output: behavior preserved, tests run, scope, and what was moved.
4. Return to `references/review-gate.md` for re-test and user acceptance.

Do not submit or release from inside this loop.
