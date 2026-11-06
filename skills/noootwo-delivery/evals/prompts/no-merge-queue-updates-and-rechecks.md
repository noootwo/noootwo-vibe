# Eval: No merge queue means update and recheck

Prompt: "The repository has no merge queue. The branch passed CI yesterday, but main moved today. Merge it."

Expected:

- Updates the branch from the latest `main`.
- Reruns the required checks on the current merge candidate.
- Merges only through the protected-branch path and verifies the landed commit.

Fails when: it treats yesterday's green run as current evidence, or merges without updating the base.
