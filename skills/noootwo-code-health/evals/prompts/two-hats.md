# Eval: Two hats stay separate

Prompt: "Fix the validation bug and rename the surrounding functions while you are in there."

Expected:

- Separates the behavior change from the cleanup.
- Uses the adding-function hat to reproduce and fix the bug with tests.
- Returns to green, then switches to the refactoring hat for the rename or extraction, running tests after each small move.
- Records any remaining structural work with a disposition instead of smuggling it into the bug fix.

Fails when: it bundles behavior change and refactoring, or it refactors while the suite is red.
