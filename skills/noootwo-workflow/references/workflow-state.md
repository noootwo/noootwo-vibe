# Workflow State

For non-direct, cross-skill, or external-skill work, do not write state here. Invoke the `noootwo-state` skill: read its `SKILL.md` and follow it.

## Read

Direct work does not read project state. For resume, read the bounded capsule plus at most three entry points named by the frontier; go deeper only when the capsule conflicts with current evidence.

- `scripts/noootwo-state.sh capsule`
- `scripts/noootwo-state.sh state --field stage`
- `scripts/noootwo-state.sh events --last 5`
- `scripts/noootwo-state.sh inspect PATH --query TEXT`

## Record

When a specialist changes the next frontier, hand it to `noootwo-state`:

- current stage, last owner, last result, next trigger
- settled and unsettled facts
- open blockers and waiting condition

`noootwo-state` owns the form and location. Workflow only supplies the content and abstract properties. A pure read or no-change check creates no event.

## Checkpoint

A long turn drifts: the capsule goes stale, sources get re-read, and failed loops repeat. Refresh the capsule before further reading or acting when:

- a compaction landed in this session
- the same file or verification command is about to run a second time
- two verification loops failed without producing new evidence
- every current claim is terminal and reading continues

The checkpoint carries the current claim, proven facts, the open frontier, the last evidence handle, the one next owner, and the condition that reopens a source. It is one `noootwo-state` capsule write; an unchanged structured write creates no event.

After the checkpoint, resume from the capsule instead of re-reading an entrypoint or a skill body already followed. Then continue, change owner, or stop; an unmoved frontier with no new evidence ends the attempt, and the boundary is reported instead of broadening the read.

## Re-entry

After compaction or on a new invocation, restore the capsule, verify the current commit, worktree status, and newest evidence handle, then prefer the recorded next trigger when it still matches reality. Replace it when new evidence changes the frontier.

When the recorded goal is complete and the new request is unrelated, write the capsule and recommend a new session unless the user explicitly continues here.

Direct single-file edits stay direct and do not create state.
