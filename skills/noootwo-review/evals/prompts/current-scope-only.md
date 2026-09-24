# Eval: Review stays in the current change scope

Prompt: "Review this small patch to the export function."

Expected:

- The reviewer examines the changed files, nearest tests, and public interface.
- It does not turn the patch into a full-project audit or an unrelated rewrite.
- A structural finding outside the safe local fix is recorded with a disposition: opportunity, planned, long-term, or accepted.
- A broad refactor starts only if the current change requires preparatory work or the user explicitly asks.

Fails when: it reviews the whole repo, proposes unrelated cleanup as required work, or silently drops a structural finding instead of recording it.
