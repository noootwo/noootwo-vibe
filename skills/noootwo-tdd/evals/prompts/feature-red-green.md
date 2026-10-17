# Eval: Feature uses red-green-refactor

Prompt: "Add a `normalizeEmail` helper."

Expected:

- The agent writes a failing test first.
- It runs the test and confirms it fails because the behavior is missing.
- It writes the smallest implementation, runs the test green, and runs the relevant suite for the touched behavior and nearest boundary.
- It refactors only after green.

Fails when: production code is written first, tests are added after implementation, the initial failure is never observed, or the full repository suite is treated as the TDD exit.
