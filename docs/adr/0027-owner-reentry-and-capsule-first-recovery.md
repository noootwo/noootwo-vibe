# 0027 — Owner re-entry and capsule-first recovery

## Status

Accepted on 2026-11-03 as the candidate for the next release batch.

## Context

ADR 0024 bounded individual reads and defined the capsule. ADR 0026 added the
long-turn checkpoint. A read-only audit of the modocc project history now shows
the remaining failure: the checkpoint rule could not fire because the skill that
carries it was not re-entered after compaction.

The audit snapshot taken on 2026-11-03 covers five session files, two threads,
19 turns, 2,371 unique responses, 28 compactions, 3,458 tool calls, and 137.8 MB
of tool output, at 425.3M nominal tokens, 13.2M uncached input, and 2.32M output.
The history was still appending during the audit, so the numbers describe this
snapshot, not a final total.

- 44 commands re-read at least one Noootwo `SKILL.md`: product 22, design 22,
  research 21, workflow 6, state 3, release 3, TDD 1, code-health 1, debug 1,
  ask 0. Fourteen of the 44 were one command reloading the product, design, and
  research trio together.
- 21 of the 28 compactions were followed within 60 seconds by a skill-body
  read, with a median gap of 7.1 seconds and a range of 4.4 to 32.6 seconds.
- Engineering owners enter only late: TDD at 03:19 local, code-health at 03:42,
  and release at 03:43 and 04:02, after the bulk of the session had been spent
  reloading the same three design-stage bodies.
- The project never had `.noootwo/state/`, so `noootwo-state`'s
  "continue from repository evidence without building a state layer" rule
  correctly produced no capsule, and recovery had nothing bounded to read.
- The first phase (no skill named) already found and read product, design, and
  research; `@`-mentioning them later changed nothing about ownership. The third
  phase (no skill mentioned) kept the same owners while implementation, server,
  and deployment work had no engineering owner.

The trigger lived in the wrong place. Workflow's checkpoint text sits in its
body, but the body is only present until the next compaction; the description
index and the recovery rules are what survive. Reloading a skill body is not
recovery, and an earlier read is not an ownership claim.

## Decision

1. `noootwo-workflow`'s description names re-entry after compaction or a phase
   change, so the routing owner is selected again when the context that carried
   the previous decision is gone.
2. Every new request, phase shift, and specialist return re-enters owner
   matching from the current artifact and evidence. A body read earlier never
   stays the owner by itself.
3. A plan pasted by the user or produced by an external skill is approved but
   unowned. Before the first edit, workflow names the current owner, its
   verification depth, and the release boundary when release facts can change.
   A plan with no assertion or verification command is not execution-ready; its
   owner closes that gap instead of the agent inventing validation.
4. Recovery is capsule-first. When state is absent and the work is cross-owner,
   cross-session, or already compacted, one recovery capsule is written through
   `noootwo-state` before further reads. Direct and single-owner read-only work
   keeps repository evidence and builds no state layer, so the cheap path stays
   cheap.
5. Product, design, and research carry one exit sentence: after a handoff or
   compaction they resume from the capsule and current artifacts, and their body
   is reloaded only when that skill owns the next step.
6. No new skill, no schema change, and no fixed reload budget. The public set
   stays at eleven.

## Research basis

The mechanism is measured from local Codex session logs through
`audit_codex_context.py` and a command-text scan that never printed arguments
or output. It extends the accepted context lifecycle of ADR 0024 and the
checkpoint of ADR 0026 and adds no new external claim. The phase discipline
follows ADR 0025: the approved plan owns ordinary implementation details while
user-owned decisions, irreversible effects, and release facts still stop for
their owner.

## Rejected alternatives

- **Loading workflow on every turn or keeping it resident.** It adds permanent
  discovery cost to direct work, and the failure is re-entry, not a missing
  resident owner. The description trigger covers compaction and phase changes.
- **A capsule for every task.** Direct, single-owner, and read-only work would
  pay state ceremony with nothing to recover. The absent-capsule branch stays
  conditional.
- **Reloading the previously used specialists as context restoration.** This is
  the measured failure: 44 body reads and no engineering owner for most of the
  history. A body is a method, not a recovery record.
- **Treating `@` mentions as an ownership signal.** They are user emphasis, not
  a routing decision; phase 2 and phase 3 behaved identically.
- **Adding a twelfth routing skill or a platform hook.** Workflow already owns
  scheduling, and the platform offers no portable hook for this trigger.
- **Adding the recovery line to the product, design, and research
  descriptions.** It would enlarge every always-loaded index entry for a case
  their bodies now cover. It remains the P2 lever if fresh-session measurement
  still shows cross-owner reloads.

## Consequences

- A compacted session has one bounded recovery read instead of a three-body
  reload, and the owner after recovery is chosen from the current artifact.
- The approved-plan rule makes the missing engineering owner visible before the
  first edit rather than after a deployment exists.
- The behaviour change is not yet measured in fresh model sessions; no token,
  time, or rework saving is claimed for it. Only the problem is measured.
- Under-reading is the residual risk: recovery must not suppress a required
  verification. The capsule carries the reopen condition, and the hard gates
  for evidence, tests, and release readiness are unchanged.

## Verification

- Four eval contracts: `phase-shift-reroute`, `approved-plan-names-owners`,
  `compaction-no-capsule`, and `capsule-first-recovery`.
- Workspace validation enforces the description budget, the `SKILL.md` line
  budget, and reference pointers after the new text.
- The refreshed audit is recorded in
  [`docs/experiments/2026-11-03-modocc-route-audit.md`](../experiments/2026-11-03-modocc-route-audit.md);
  a rerun of `audit_codex_context.py --cwd <project> --json --top-turns N`
  reproduces the shape, and fresh-session behaviour remains an open gap.
