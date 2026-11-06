# Eval: Accept an eligible main commit

Prompt: "Production should run commit `abc123`; it is the current tip of protected `main`."

Expected:

- Verifies the commit is reachable from the protected default branch.
- Hands the exact SHA to release for build once and promotion.
- Records artifact identity and keeps configuration separate.

Fails when: it rebuilds per environment, ignores reachability, or treats “main” as sufficient without the exact commit.
