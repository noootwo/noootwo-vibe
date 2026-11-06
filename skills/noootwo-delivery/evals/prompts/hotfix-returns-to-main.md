# Eval: Hotfix returns to main

Prompt: "Production is broken. Make a hotfix branch, deploy it, and merge it back later."

Expected:

- Branches from `main`, fixes, checks, and opens a PR back to `main`.
- Deploys only after the fix is on `main`, or rolls back the previous artifact first.
- Tags/releases the resulting `main` commit.

Fails when: it deploys the hotfix branch directly, tags it outside `main`, or leaves the merge for later.
