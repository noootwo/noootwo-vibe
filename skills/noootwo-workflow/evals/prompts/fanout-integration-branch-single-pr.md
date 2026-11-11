# Eval: Write lanes rejoin one integration branch and one main PR

Prompt: "Three write-fanout lanes each pass their lane checks. Open three PRs directly to protected `main` so each can merge as soon as it is green."

Expected:

- Keeps one integration branch for the requirement.
- Rejoins the reviewed lanes one at a time into that branch in the required order and reruns lane plus combined checks.
- Opens one PR from the integration branch to protected `main` after the relevant Change Check and combined verification.
- Keeps the web of lane dependencies out of `main`.

Fails when: it opens one main PR per lane without a stated reason; it merges lane branches directly to `main`; or it skips the combined check because each lane passed alone.
