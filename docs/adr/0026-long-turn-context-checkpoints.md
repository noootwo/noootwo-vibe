# 0026 — Long-turn context checkpoints and capsule-first recovery

## Status

Accepted on 2026-11-02 as the candidate for the next release batch.

## Context

ADR 0024 bounded individual reads, capsules, and cold evidence. A read-only
audit of the real Codex history for `kungfu-community` (`kungfu-trader-community`
carries most of it), and `kungfu-harness` showed that the remaining cost sits
inside single long turns, not in one oversized read:

- 37 sessions, 314 turns, 40,145 unique model responses, 79,907 tool calls, and
  1,097 compactions.
- Nominal `total_tokens` 6.39B at a 92.8% cache-hit rate; uncached input 455M
  and output 43.3M. The cached share is cheap per token, but it is re-sent once
  per response, so a turn with thousands of responses multiplies it.
- Tool output reached 930 MB, 14,812 outputs exceeded 16 KiB, and 6,571
  `exec_command` calls were repeats of a command already run inside the same
  turn.
- The largest harness turn ran 10.4 hours across 3,574 responses, 7,121 tool
  calls, 127 compactions, and 557M tokens; two more turns passed 400M.
- Commands naming `project-status.md` produced 42.3 MB of output, commands
  naming a `SKILL.md` about 20 MB, and commands naming `.noootwo` only 286 KB.
  The capsule existed but was not the re-entry point.

The workflow rules said "do not repeat a file" and "restore the capsule after
compaction", but nothing fired at the moment the drift starts: mid-turn, after
a compaction, or when a read or verification repeats. The capsule stayed
stale and the turn kept buying context it already had.

## Decision

1. Add one behaviour-triggered checkpoint to `noootwo-workflow` and its
   references. It fires when a compaction lands, when the same file or
   verification command is about to run a second time, when two verification
   loops fail without new evidence, or when every current claim is terminal
   while reading continues. Direct work skips it.
2. The checkpoint refreshes the capsule through `noootwo-state` and carries
   the current claim, proven facts, open frontier, last evidence handle, one
   next owner, and the condition that reopens a source. Then the turn
   continues, changes owner, or stops; an unmoved frontier with no new
   evidence ends the attempt.
3. The checkpoint is one capsule write, not a plan rewrite and not a status
   meeting. An unchanged structured write still creates no event.
4. `noootwo-state` gains the recovery order and anti-drift rules: capsule,
   commit, and worktree first; only the evidence handles the frontier names; a
   second read of a source is evidence only when its hash, commit, or claimed
   role changed; a long document behind an entrypoint is read through the
   slice the step needs.
5. `audit_codex_context.py` reports per-turn aggregates (`--top-turns N`) so
   the same audit can be rerun as a regression measure. It still emits no
   message, tool-output, argument, environment, or credential text.
6. No new skill, no fixed token or step budget, and no schema change. The
   public set stays at eleven.

## Research basis

The mechanism rests on the evidence base already accepted in ADR 0024 —
Context Rot, Anthropic's context-engineering guidance, ACE, Agentic Context
Management, The Complexity Trap, and Compaction Laundering — and on the local
measurement above. This ADR adds no new external claim, so no new outside
source was needed; the earlier sources already establish that long, stale,
distractor-heavy context degrades performance and that compaction loses
provenance unless a structured note is kept.

## Rejected alternatives

- **A fixed token, response, or tool-call budget.** The model cannot observe
  a hidden budget reliably, and a hard stop can cut the one decisive probe.
  The triggers are behaviours the turn can actually observe.
- **Global truncation of tool output or conversation.** It destroys provenance;
  the existing 16 KiB cold-evidence boundary already keeps the raw record.
- **A twelfth context skill.** It adds permanent discovery load for a
  capability workflow and state already own.
- **A summarizing subagent per turn.** It splits dependent decisions from
  their context and reintroduces the merge problem ADR 0024 documented.
- **Doing nothing because caching makes tokens cheap.** Cache misses, output,
  wall-clock, and compaction loss are still real, and a 10.4-hour turn has a
  reviewability cost separate from its price.

## Consequences

- Long turns have a named moment to stop paying for context already bought,
  and the capsule becomes the recovery entrypoint it was designed to be.
- The workspace gains three eval prompts and a per-turn measurement; the
  behaviour change itself is not yet measured in fresh model sessions.
- Under-reading is the residual risk: the checkpoint must not suppress a
  required verification. The reopen condition is part of the checkpoint, and
  the existing hard gates for evidence and verification are unchanged.

## Verification

- `audit_codex_context.py --self-test` covers per-turn token, tool, output,
  compaction, repetition, and duration attribution, top-turn limiting, and
  privacy output.
- Workspace validation enforces the `SKILL.md` line budget and reference
  pointers after the new text.
- Per-turn totals reproduce the recorded audit numbers for the three fixed
  projects; the probe record is
  [`docs/experiments/2026-11-02-long-turn-cost-audit.md`](../experiments/2026-11-02-long-turn-cost-audit.md).
