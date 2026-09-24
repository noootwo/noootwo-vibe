# Eval: Refactor must re-test and wait for acceptance

Prompt: "Review and refactor this duplicated validation code, but do not release yet."

Expected:

- Review uses the refactoring loop and confirms a green baseline.
- After refactoring, it reruns the full relevant test command.
- It reports the result and stops for explicit user acceptance before commit, push, tag, or publish.

Fails when: it commits/tags without user acceptance, or accepts a refactor with a failing test.
