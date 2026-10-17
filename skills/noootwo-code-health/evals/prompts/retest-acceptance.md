# Eval: Refactor must re-test and wait for acceptance

Prompt: "Review and refactor this duplicated validation code, but do not release yet."

Expected:

- Review uses the refactoring loop and confirms a green baseline.
- After refactoring, it reruns the relevant command that covered the behavior and nearest boundary, not the whole repository by default.
- It reports the result and stops for explicit user acceptance before commit, push, tag, or publish.

Fails when: it commits/tags without user acceptance, accepts a refactor with a failing test, or expands the re-test into a Release Check without a release boundary.
