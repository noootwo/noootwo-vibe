# Eval: A compacted session with no capsule writes one first

Prompt: a long cross-owner session has no `.noootwo/state/` directory when a compaction lands. The user's next message is "carry on", and the last work was mid-implementation with a pending release boundary.

Expected:

- Checks for the capsule before re-reading entrypoints or skill bodies.
- Writes one recovery capsule through `noootwo-state` carrying the claim, proven facts, open frontier, last evidence handle, next owner, and reopen condition.
- Resumes from that capsule plus the current commit and worktree, then re-matches one owner for the next step.
- Creates no broader state layer and does not enumerate `.noootwo/`.

Fails when: it rebuilds context by re-reading `AGENTS.md` or the product, design, and research bodies; it continues with no recovery note at all; or it creates a full structured state layer.
