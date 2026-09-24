# Eval: Choose the right refactoring workflow

Prompt: "Add a small option to this settings parser." The parser is a messy 900-line file, tests are green, and the change only needs one branch in the parsing logic.

Expected:

- Names the touched area and the real pressure, not the file size alone.
- Uses a preparatory, TDD, litter-pickup, or comprehension workflow based on the trigger.
- Makes one small behavior-preserving catalog move in the touched area if it makes this change safer, then runs the relevant tests.
- Records a larger split as `planned` or `long-term` instead of attempting a big rewrite now.

Fails when: it ignores the structure, or it turns a small option change into a full-file rewrite.
