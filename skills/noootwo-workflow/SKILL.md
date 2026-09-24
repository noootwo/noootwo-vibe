---
name: noootwo-workflow
description: "Use for multi-step tasks, refactors, releases, handoffs, rework, or when the right skill is unclear; reads current project state and matches the correct installed skill."
---

# Noootwo Workflow

Run one task through one re-entrant loop:

`read current state -> match one owner -> specialist runs -> collect result -> update state -> next step or stop`

Workflow schedules. It owns order, scope, stop conditions, and handoffs; the specialist or matching installed skill owns the work itself.

## 1. Read current state

Read only what the current step needs. For project state, invoke the `noootwo-state` skill: read its `SKILL.md` and follow it, and use its query helper instead of loading a full state file.

- `direct` — current file, changed-file context, nearest instructions.
- `project` — `AGENTS.md`, README, `docs/status.md`, package/build metadata, nearest tests.
- `decision` — ADRs, specs, release notes, public contracts, migrations, artifacts, `.noootwo/*` state.

Always prefer current repo truth and project state over assumed stage.

**Done when:** you can name the files and state that constrain this step.

## 2. Match one owner

Use `references/route-by-signal.md`. Match by intent, artifact shape, current blockers, and available skill descriptions. Do not route from keywords alone.

- Unambiguous owner → invoke it by reading its `SKILL.md` and following it.
- Tie or no owner → stop, state one or two candidates and why, and wait for the user.
- External installed skills are valid execution resources; they are not added to the Noootwo public set.

**Done when:** one owner is invoked, or the user resolves a tie/absence.

## 3. Schedule, not implement

Use `references/orchestration.md`. Decide one next step at a time. Specialist skills own their method; workflow only returns to the loop after each result.

Precedence is limited to blockers and stage continuity:

`debug/research/product blocker -> design -> review/preparatory when structure blocks -> tdd/implementation -> review/post-green -> retest -> acceptance -> state/release`

Review is not only a release gate. After every non-direct behavior change, the loop returns to `noootwo-code-health` before the work can be reported done. Before release, a triggered Structure Sweep belongs to the same review owner.

Do not precompute a full DAG or pile on condition tables.

## 4. Keep state

For non-direct, cross-skill, or external-skill work, invoke the `noootwo-state` skill after each result to record the next step: read its `SKILL.md` and follow it. Direct single-file edits stay direct and do not create state.

**Done when:** the state names current goal, last owner, last result, next trigger, and open blockers.

## 5. Close

Answer before calling the work done:

- Did the closest meaningful verification run, or is the gap explicit?
- Did a specialist or matching installed skill need to run, and was it invoked?
- For a non-direct code change, did `noootwo-code-health` run and dispose of every structural finding as fixed, opportunity, planned, long-term, or accepted?
- Did behavior, state, or release facts change, and did `noootwo-state` place them?
- Is user acceptance still required before commit, push, tag, or publish?

Then report what changed, what was verified, what was documented, and what remains open.

## Rework

When the user rejects a previous attempt, diagnose the failed layer before changing anything:

| Failure looks like | Layer | Invoke |
| --- | --- | --- |
| They wanted something different, or scope is wrong | product | `noootwo-product` |
| Direction or visual language is wrong | design | `noootwo-design` |
| Intent was right and execution is not | implementation | `noootwo-tdd` detail pass, or `noootwo-code-health` |
| Documents or project state no longer match reality | state | `noootwo-state` |
| A regression or failure has no proven cause | evidence | `noootwo-debug` |

State the layer in one line, then invoke. Do not polish the same layer again.

## References

- `references/route-by-signal.md` — accurate owner matching from current evidence.
- `references/workflow-state.md` — project-local state and re-entrant timing.
- `references/orchestration.md` — one-next-step scheduling and stop conditions.
- `references/workflow-playbook.md` — handoff packets and lightweight guardrail checklist.

Missing skill fallback: first try `npx -y skills add noootwo/noootwo-vibe --global --agent codex --skill <name> --yes`; if install fails, take the smallest direct fallback and mark the record `skill-missing: <name>` (for persistence, write the owning file directly).
