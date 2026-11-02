# Eval: Capsule-first recovery decides its own cost

Prompt: "The session compacted in the middle of a task. Continue it." The project has no `.noootwo/state/current.json`; the pending work is an approved multi-owner implementation with a deployment step, and the previous turn had re-read three skill bodies.

Expected:

- Classifies the work as cross-owner and already compacted, so one recovery capsule is warranted.
- Writes the capsule through `noootwo-state` before further reads, carrying the current claim, stage, open frontier, evidence handles, and next trigger.
- Reads the current commit and worktree, then only the evidence handles the frontier names.
- States plainly that a direct or single-owner read-only task would have continued without a state layer.
- Keeps the capsule as a read view: no second source of truth, and no skill body reloaded unless its skill owns the next step.

Fails when: it builds or enumerates a full state layer for a small direct task; it re-reads entrypoints or skill bodies to rebuild context; it writes no recovery note for a compacted cross-owner task; or it trusts the capsule without checking the current commit.
