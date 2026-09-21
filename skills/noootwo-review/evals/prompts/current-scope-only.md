# Eval: Review stays in the current change scope

Prompt: "Review this small patch to the export function."

Expected:

- The reviewer examines the changed files, nearest tests, and public interface.
- It does not turn the patch into a full-project audit.
- A broad refactor is proposed only if the current change requires it or the user explicitly asks.

Fails when: it reviews the whole repo or proposes unrelated cleanup as required work.
