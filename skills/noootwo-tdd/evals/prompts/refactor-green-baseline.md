# Eval: Refactor keeps a green baseline

Prompt: "Refactor the duplicated validation helper without changing behavior."

Expected:

- The agent confirms the relevant test command is green first.
- It makes small behavior-preserving moves and keeps tests green after each step.
- It runs the full relevant suite at the end.
- It does not bundle semantic changes with cleanup.

Fails when: it refactors without a baseline, changes behavior during cleanup, or submits without re-running tests.
