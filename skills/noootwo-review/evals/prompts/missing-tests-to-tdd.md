# Eval: Missing tests route to TDD

Prompt: "Review this changed behavior; there are no tests."

Expected:

- Review stops structural judgment and invokes `noootwo-tdd` by reading its `SKILL.md`.
- It does not evaluate architecture as a substitute for missing behavior proof.

Fails when: it reviews the change as if tests exist, or writes its own quick test without invoking TDD.
