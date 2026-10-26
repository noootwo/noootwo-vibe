---
name: noootwo-workflow
description: "Use for multi-step tasks, evidence confirmation, refactors, releases, handoffs, or unclear routing; load one owner at a time and read state only when the task needs it."
---

# Noootwo Workflow

Run one task through one re-entrant loop:

`read current state -> match one owner -> specialist runs -> collect result -> update state -> next step or stop`

Routing gate: skill descriptions are the index. Do not read another `SKILL.md` to orient; choose from descriptions and load exactly one owner body for the current step.

Workflow schedules. It owns order, verification depth, scope, stop conditions, and handoffs; the specialist or matching installed skill owns the work itself. Context lifecycle `write -> select -> compress -> isolate -> verify`: load this skill and triggered reference sections; route references over 200 lines through headings or query hits; cap live excerpts at 80 lines; put output over 16 KiB in cold evidence with path and hash; isolate only independent read-only work; keep one writer; verify summaries against source. Load at most one specialist body before evidence; for a plan-only request, that is the only specialist body and later owners are named, not loaded.

## 1. Read current state

Choose one depth before reading project files; escalate only when a fact is missing. An explicit issue ID, symbol, path, or error routes to its owner from the skill descriptions, and that owner reads the evidence; project orientation is not an ownership check. A current spec, ADR, issue, or evidence record named by the request is an authority, not a cue to load the skill that authored it; select the owner of the requested outcome. Structured project state exists at `.noootwo/state/current.json`; resume reads it through the `noootwo-state` skill: read its `SKILL.md` and follow it, and use its query helper instead of loading a full state file.

- `direct` — current file, changed-file context, nearest instructions; do not read project state.
- `resume` — state capsule, current commit and worktree status, plus at most three entry points named by the frontier.
- `decision/evidence` — start with one bounded search for the request's own identifier. Read only matching entries and the evidence they name; use README, status, system docs, architecture, or state only when the search points there or no identifier exists. Without an identifier, inspect at most three targeted evidence slices.

Start with one bounded query (`-m 20` or an 80-line slice), batch independent reads, and do not repeat a file or history range. After an environment or permission failure, record it once and change evidence source instead of probing command variants. Stop at the first evidence that makes every current claim terminal; when a named change, artifact, or authority is absent, report that absence before planning around it. After compaction or session re-entry, restore the capsule and verify its source hash, current commit, worktree, and latest evidence before trusting the summary. Always prefer current repo truth and project state over assumed stage.

**Done when:** you can name the files and state that constrain this step.

## 2. Match one owner

Use `references/route-by-signal.md`. Match by intent, artifact shape, current blockers, and available skill descriptions. Do not route from keywords alone.

- Unambiguous owner → invoke it by reading its `SKILL.md` and following it.
- Tie or no owner → stop, state one or two candidates and why, and wait for the user.
- Plan or recommendation only → load only the current owner; do not read a later owner's `SKILL.md` until its step starts.
- Never load a second specialist before the first evidence read. Batch independent reads, and stop once one viable slice and its verification seam are supported; leave alternatives unproven instead of auditing them.
- Plan/recommendation gate: one bounded identifier search, then at most three targeted evidence slices with independent reads batched. Stop when a viable slice is supported; otherwise name the missing authority and stop.
- External installed skills are valid execution resources; they are not added to the Noootwo public set. Their default artifact directories are not project policy; durable output goes through `noootwo-state` into the owning Noootwo layer.

**Done when:** one owner is invoked, or the user resolves a tie/absence.

## 3. Schedule, not implement

Use `references/orchestration.md`. Decide one next step at a time. Specialist skills own their method; workflow only returns to the loop after each result.

When the request is to confirm one or more suspected problems, gather evidence, or give options before a fix exists, schedule `noootwo-debug`'s Diagnosis Map. Keep each claim independent until a shared cause is proven; do not start a cross-system audit or implementation.

Precedence is limited to blockers and stage continuity:

`debug/research/product blocker -> design -> code-health/shape when the seam is non-obvious -> preparatory-refactor when structure blocks -> tdd/implementation -> code-health/change-check -> next change or code-health/release-check -> release when publishing -> state/release -> acceptance`

Code-health is not only a release gate. When a non-direct code change has a non-obvious seam, it shapes the change before TDD: `noootwo-code-health` produces a Change Shape, and its result may be direct TDD, a preparatory refactor, or a handoff to product, design, research, or a stopped change. A local change with an obvious seam and no contract, data, or migration impact skips that pass. After every non-direct behavior change, the loop returns to `noootwo-code-health` for a Change Check before the work can be reported done. That check stays on the diff, changed behavior, nearest callers, affected tests, and one to three lenses; it escalates only when blast radius requires it. Before release or a ship-readiness submit gate, code-health runs a Release Check once for the exact commit: full suite or CI evidence, full Structure Sweep, release evidence, and named gaps. Once readiness is established, versioning, tags, artifacts, deployment traces, provenance, rollback, and release health belong to `noootwo-release`.

After a plan is approved, resolve a reversible ambiguity from the spec, plan, and evidence, record the ruling with its basis, error cost, and reopen trigger, then continue. Stop only for a user-owned decision, irreversible migration or data loss, security or privacy impact, external side effects or spend, or evidence that the plan is no longer viable. Ordinary implementation details do not return for routine re-approval.

Do not precompute a full DAG or pile on condition tables.

## 4. Keep state

For non-direct, cross-skill, or external-skill work, invoke the `noootwo-state` skill when the goal, stage, decision, blocker, evidence, or next trigger actually changes: read its `SKILL.md` and follow it. Pure reads and no-change checks create no event. Direct single-file edits stay direct and do not create state.

When the current goal is complete and an unrelated goal appears, write the capsule and recommend a new session unless the user explicitly asks to continue in this one.

**Done when:** the state names current goal, last owner, last result, next trigger, and open blockers.

## 5. Close

Answer before calling the work done:

- Did the required verification depth run — Change Check, escalation when the blast radius required it, and Release Check at the release boundary — or is the gap explicit?
- For a confirmation request, did every claim end as confirmed, refuted, insufficient, or decision-needed before any fix or expansion?
- Did a specialist or matching installed skill need to run, and was it invoked?
- For a non-direct code change, did `noootwo-code-health` shape the implementation when the seam was non-obvious, run a scoped Change Check after green, and run a Release Check only when the task reached release?
- If a completed change created a release-bound check or known gap, did `noootwo-release` add it to the open Release Verification Ledger?
- For release work, did `noootwo-release` produce the Release Plan and did `noootwo-state` receive the release record and deployment evidence?
- Did behavior, state, or release facts change, and did `noootwo-state` place them?
- During approved execution, are reversible plan conflicts recorded as rulings rather than silently decided or escalated as routine re-approval?
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
