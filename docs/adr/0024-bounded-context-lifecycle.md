# 0024 — Bounded context lifecycle across the skill package

- Status: accepted for candidate `0.23.0`
- Date: 2026-10-25
- Owners: all eleven public skills; operational ownership in `noootwo-workflow`, `noootwo-state`, and `noootwo-onboard`

## Context

The existing skills preserve decisions well and prevent repeated defects, but
using the package on unrelated projects can still spend too many tokens. The
cost comes from broad file reads, repeated project-state inspection, large raw
tool output, and keeping dependent work in shared context without a bounded
re-entry view.

The package must optimize the whole skill set, not one pilot repository.
Historical events, cold evidence, quality gates, and provenance are more
important than any target saving. A new context skill would add another
always-loaded description and another routing path, so the capability must
stay inside existing owners.

## Decision

1. Apply one lifecycle to every model-invoked skill:
   `write -> select -> compress -> isolate -> verify`.
2. Keep the public set at eleven skills. `noootwo-workflow` owns reading depth
   and scheduling; `noootwo-state` owns bounded reads and evidence handles.
3. Select one read depth:
   `direct` reads no project state; `resume` reads a capsule, current git
   state, and at most three frontier entry points; `decision/evidence` reads
   only the records or local evidence that can settle the current step.
4. Default live excerpts to 80 lines. Raw output above 16 KiB goes to cold
   evidence first; the hot context carries its path, source, exit status,
   hash, and bounded tail. References above about 200 lines are entered
   through headings or query hits before the matching section.
5. Keep one writer for dependent work. Isolate only independent read-only
   research or review to a subagent.
6. Add `noootwo-state` commands for a bounded capsule, metadata and local-hit
   file inspection, and cold command capture. Keep `summary` as an alias for
   capsule semantics and keep existing field/event reads.
7. Record state only when the goal, stage, decision, blocker, evidence, or next
   trigger changes. Store actual changed fields; a pure read or unchanged
   check emits no event.
8. After compaction, restore the capsule and verify it against the current
   commit, worktree, and latest evidence. A completed goal followed by an
   unrelated goal gets a capsule and a new-session recommendation unless the
   user explicitly continues.
9. Extend onboarding with a context-health audit for whole-read entrypoints,
   long references without a section route, stale skill names, status
   timelines, and missing short-term state. Persist only the smallest adapter
   through `noootwo-state`; preserve existing history.
10. Add a read-only Codex context audit with aggregate token, compaction, tool
    output, and repeated-command counts. It emits no prompt, tool output,
    arguments, environment, or credentials.
11. Keep the state and event schemas unchanged. Existing history remains
    readable and authoritative.

## Research basis

The decision uses Context Rot, Anthropic's context-engineering guidance, ACE,
Agentic Context Management, The Complexity Trap, Compression Method Matters,
Compaction Laundering, and Cognition's single-thread boundary. The detailed
evidence levels, counterexamples, and limits are in
[`docs/reference/context-cost.md`](../reference/context-cost.md).

The sources agree on bounded, high-signal context and provenance retention.
They disagree on subagent breadth: Anthropic reports gains for isolated
research, while Cognition documents failures when dependent decisions are
fragmented. This ADR resolves that conflict with a single-writer default and a
narrow read-only isolation exception.

## Rejected alternatives

- **A twelfth context skill:** adds permanent discovery load and routing
  ambiguity; the capability already belongs to workflow and state.
- **A user-enabled Lean mode:** makes the default expensive and makes
  comparisons ambiguous.
- **Aggressive whole-history summarization:** risks detail loss, output
  expansion, and provenance laundering; cold evidence and an append-only log
  remain available.
- **Deleting, migrating, or rewriting old history:** not required for a read
  optimization and too risky for historical accuracy.
- **Default multi-agent fan-out:** dependent subtasks can develop incompatible
  implicit decisions.
- **Hard caps on evidence:** limits apply to the live view, not the stored
  source, so a decisive long record can still be reopened.

## Consequences

- Eleven discovery descriptions now total less than 1,800 characters.
- All model-invoked skills carry the same compact context rule, while only
  workflow, state, and onboarding gain new procedures.
- The capsule is a derived read view; events and cold evidence remain the
  facts of record.
- Existing projects can adopt the new helpers without changing their state or
  event files.
- The named real-project A/B gate passed for the six final pairs; universal
  token savings for other tasks or models are still not claimed.

## Verification

- Workspace validation enforces description totals, skill/reference budgets,
  and context-rule markers on model-invoked skills.
- State and audit self-tests cover capsules, character bounds, missing and
  corrupt state, file inspection, binary files, successful and failing
  capture, over-16-KiB output, usage dedupe, top-level compaction counting, and
  privacy-safe output.
- Ten behavior probes compared `0.22.0` and candidate `0.23.0`; the candidate
  passed all ten with no baseline behavior regression.
- Six final pairs across the three fixed commits cleared the predeclared 10%
  median token threshold. The median paired total-token delta was `-44.3%`,
  the median task-level delta was `-32.3%`, and no pair worsened acceptance,
  uncached input, history integrity, duplicate detection, verification, or
  rework. Evidence is in
  [`docs/experiments/2026-10-25-context-budget.md`](../experiments/2026-10-25-context-budget.md).
- Publication remains blocked pending user acceptance; the data and event
  schemas did not change.
