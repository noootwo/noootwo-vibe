---
name: noootwo-workflow
description: "Use for multi-step tasks, refactors, releases, handoffs, rework, or when the right skill is unclear; reads current project state and matches the correct installed skill."
---

# Noootwo Workflow

Run one task through one re-entrant loop:

`read current state -> match one owner -> specialist runs -> collect result -> update state -> next step or stop`

Workflow schedules. It owns order, verification depth, scope, stop conditions, and handoffs; the specialist or matching installed skill owns the work itself.

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
- External installed skills are valid execution resources; they are not added to the Noootwo public set. Their default artifact directories are not project policy; durable output goes through `noootwo-state` into the owning Noootwo layer.

**Done when:** one owner is invoked, or the user resolves a tie/absence.

## 3. Schedule, not implement

Use `references/orchestration.md`. Decide one next step at a time. Specialist skills own their method; workflow only returns to the loop after each result.

Precedence is limited to blockers and stage continuity:

`debug/research/product blocker -> design -> code-health/shape when the seam is non-obvious -> preparatory-refactor when structure blocks -> tdd/implementation -> code-health/change-check -> next change or code-health/release-check -> release when publishing -> state/release -> acceptance`

Code-health is not only a release gate. When a non-direct code change has a non-obvious seam, it shapes the change before TDD: `noootwo-code-health` produces a Change Shape, and its result may be direct TDD, a preparatory refactor, or a handoff to product, design, research, or a stopped change. A local change with an obvious seam and no contract, data, or migration impact skips that pass. After every non-direct behavior change, the loop returns to `noootwo-code-health` for a Change Check before the work can be reported done. That check stays on the diff, changed behavior, nearest callers, affected tests, and one to three lenses; it escalates only when blast radius requires it. Before release or a ship-readiness submit gate, code-health runs a Release Check once for the exact commit: full suite or CI evidence, full Structure Sweep, release evidence, and named gaps. Once readiness is established, versioning, tags, artifacts, deployment traces, provenance, rollback, and release health belong to `noootwo-release`.

Do not precompute a full DAG or pile on condition tables.

## 4. Keep state

For non-direct, cross-skill, or external-skill work, invoke the `noootwo-state` skill after each result to record the next step: read its `SKILL.md` and follow it. Direct single-file edits stay direct and do not create state.

**Done when:** the state names current goal, last owner, last result, next trigger, and open blockers.

## 5. Close

Answer before calling the work done:

- Did the required verification depth run — Change Check, escalation when the blast radius required it, and Release Check at the release boundary — or is the gap explicit?
- Did a specialist or matching installed skill need to run, and was it invoked?
- For a non-direct code change, did `noootwo-code-health` shape the implementation when the seam was non-obvious, run a scoped Change Check after green, and run a Release Check only when the task reached release?
- If a completed change created a release-bound check or known gap, did `noootwo-release` add it to the open Release Verification Ledger?
- For release work, did `noootwo-release` produce the Release Plan and did `noootwo-state` receive the release record and deployment evidence?
- Did behavior, state, or release facts change, and did `noootwo-state` place them?
- Did an external skill propose a spec, plan, or other durable artifact? If so, was it stored in the Noootwo-owned layer instead of the external skill's default directory?
- Is user acceptance still required before commit, push, tag, or publish?

Then report what changed, what was verified, what was documented, and what remains open.

## Rework

When the user rejects a previous attempt, diagnose the failed layer before changing anything:

| Failure looks like | Layer | Invoke |
| --- | --- | --- |
| They wanted something different, or scope is wrong | product | `noootwo-product` |
| Direction or visual language is wrong | design | `noootwo-design` |
| Intent was right and execution is not | implementation | `noootwo-tdd` detail pass, or `noootwo-code-health` |
| Version, tag, artifact, deployment trace, rollback, or release health is wrong | release | `noootwo-release` |
| Documents or project state no longer match reality | state | `noootwo-state` |
| A regression or failure has no proven cause | evidence | `noootwo-debug` |

State the layer in one line, then invoke. Do not polish the same layer again.

## References

- `references/route-by-signal.md` — accurate owner matching from current evidence.
- `references/workflow-state.md` — project-local state and re-entrant timing.
- `references/orchestration.md` — one-next-step scheduling and stop conditions.
- `references/workflow-playbook.md` — handoff packets and lightweight guardrail checklist.

Missing skill fallback: first try `npx -y skills add noootwo/noootwo-vibe --global --agent codex --skill <name> --yes`; if install fails, take the smallest direct fallback and mark the record `skill-missing: <name>` (for persistence, write the owning file directly).
