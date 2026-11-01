# Eval: Compaction restores the capsule before more reads

Prompt: a long multi-step task is mid-implementation when the session compacts. The recorded capsule is two days old, the repository has moved on, and the user's next message is "carry on".

Expected:

- Refreshes the capsule through `noootwo-state` before reading further: current claim, proven facts, open frontier, last evidence handle, one next owner, and what reopens a source.
- Verifies the capsule against the current commit, worktree, and latest evidence, and marks what it could not verify.
- Resumes from the refreshed capsule and recent git evidence instead of re-reading `AGENTS.md`, a skill body it already followed, or a long status document from the top.
- Continues, changes owner, or stops, and says which one and why.

Fails when: it trusts the stale capsule unverified; it re-reads entrypoints and long documents to rebuild context it could have recovered from the capsule; it treats the compaction as a reason to restart the task or re-plan.
