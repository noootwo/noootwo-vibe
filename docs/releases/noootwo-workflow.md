# noootwo-workflow Releases

## v0.21.0

- Approved execution now treats the accepted spec and plan as authority for reversible implementation details.
- A plan ambiguity is resolved from the spec, plan, and evidence, then recorded with the decision, basis, error cost, and reopen trigger before work continues.
- Routine naming, local structure, equivalent API, and test-organization choices no longer return for re-approval.
- User-owned decisions, irreversible migration or data loss, security or privacy impact, external side effects or spend, and whole-plan invalidation remain stop boundaries.
- Added two opt-in eval contracts covering continued rulings and real stop boundaries. Fresh model sessions remain unrun.

## v0.20.0

- Replaced broad state loading with `direct | resume | decision/evidence` read depth. Direct work reads no project state; resume reads the capsule, git state, and at most three frontier entry points.
- After compaction, the restored capsule is checked against the current state hash, commit, worktree, and latest evidence.
- State records only actual goal, stage, decision, blocker, evidence, or next-trigger changes; pure reads and unchanged checks emit no event.
- A completed goal followed by an unrelated goal gets a capsule and a new-session recommendation unless the user explicitly continues.
- Added the package-wide context lifecycle, >200-line reference routing, 80-line excerpt, 16 KiB cold-evidence, read-only isolation, and single-writer rules.
- Skill descriptions are now the routing index: a named current spec, ADR, issue, or evidence record is an authority, not a cue to load its authoring skill.
- Before evidence, workflow loads at most one specialist body. Plan-only work does not preload later owners and receives one bounded identifier search plus at most three batched evidence slices.

## v0.19.0

- Routed confirmation requests, suspected-problem lists, and evidence-first recommendations to `noootwo-debug`'s Diagnosis Map.
- Added a close-gate check that every requested claim reaches a terminal verdict before a fix or systemic expansion.
- Added stop conditions for source mutation, deployment, persistent data changes, new systems, and merging independent claims without shared-cause evidence.
- Added `route-confirmation-to-debug` and `multi-question-frontier` evals.

## v0.18.2

- External installed skills remain execution resources, but their default artifact directories no longer become project conventions.
- Durable specs, plans, and other project facts are persisted through `noootwo-state` in the Noootwo-owned layer.
- The close gate now checks whether an external skill produced a durable artifact and whether it was stored in the correct project layer.
- Added an eval for an external brainstorming/writing-plans request that attempts to use `docs/superpowers/`.

## v0.18.1

- The close gate now asks whether a completed change created a release-bound check or known gap, and whether `noootwo-release` added it to the open Release Verification Ledger.
- Requirement-level detail stays in its completed Change Check; the ledger receives only cross-cutting checks, evidence that must be re-established at the release candidate, or a known blocking gap.

## v0.18.0

- Added the Change Check / Release Check split to scheduling and the close gate.
- After one requirement, the loop returns to `noootwo-code-health` for a scoped Change Check; the full suite and Structure Sweep wait for the Release Check.
- The Release Check runs once before release or a ship-readiness submit gate and can use CI evidence for the exact commit.
- Added release-check-once and updated review-after-every-change evals so workflow cannot turn every requirement into a full audit.

## v0.17.0

- Added the pre-implementation `noootwo-code-health` Integration Read to the precedence and route-by-signal guidance when a change's seam is non-obvious.
- Routed the resulting Change Shape into direct TDD, preparatory refactoring, or the owning product, design, research, or stopped-change handoff.
- Added the Change Shape and test seam to the TDD handoff packet, and the new mode to the code-health packet.
- The close gate now checks that a non-direct code change was shaped before implementation when the seam was not obvious.

## v0.16.0

- Added `noootwo-release` to the release stage after code-health readiness, with release sequencing, scope, and close-gate checks.
- Added the release handoff packet for readiness, version source, artifact, environment, changelog, deployment trace, and rollback facts.

## v0.15.0

- Updated review scheduling and close-gate handoffs from `noootwo-review` to `noootwo-code-health`.
- The workflow now points at the renamed `noootwo-code-health` skill for post-green and Structure Sweep work.

## v0.14.0

- Review is now part of done: non-direct behavior changes return to `noootwo-review` after green, before the workflow reports completion.
- The precedence now includes preparatory refactoring before a hard change and a Structure Sweep before release.
- The Close gate checks that every structural finding has a disposition, and the review handoff packet carries the selected refactoring workflow and structural disposition.

## v0.13.0

- Replaced the fixed Noootwo routing table with evidence-driven orchestration.
- Added `references/route-by-signal.md` to match one owner by intent, artifact shape, current blockers, and available skill descriptions.
- Added `references/orchestration.md` for one-next-step scheduling and explicit stop conditions.
- Allowed workflow to discover and invoke other installed skills for slides, documents, or media work without adding them to the Noootwo public set.
- When no owner is clear or two owners tie, workflow stops with one or two candidates instead of guessing.
- Routed behavior-changing code through the new `noootwo-tdd` skill before `noootwo-review`.
- Workflow state and scheduling now read and write through `noootwo-state` instead of a local `.noootwo/workflow-state.md`; reads use the state helper (`state --field`, `events --last`, `summary`).

## v0.11.1

- Tightened the description around multi-step work while making explicit that direct one-file edits stay direct.

## v0.11.0

- Finished the scheduler normalization: `noootwo-workflow` owns order, scope, stop conditions, and handoffs, and no longer carries method a specialist owns.
- Onboarding moved out. `project-skill-audit.md` and `minimal-foundation-templates.md` became `noootwo-onboard`; `project-foundation-check.md` was deleted because `noootwo-review`'s project-health lens already covered the same surface.
- Added routing and hand-off packets for `noootwo-research` and `noootwo-onboard`.
- Added a return rule naming the layer and the owning skill when work belongs to a specialist.
- Added optimization to the review route and updated the playbook's project-entry, mode, and default-loop steps to delegate.


## v0.10.0

- Normalized the skill as a scheduler: it owns order, scope, stop conditions, and handoffs; specialist skills own the work.
- Diagnostic mode is now a delegation — a bug, failure, or regression invokes the `noootwo-debug` skill, and the loop stops while the cause is unproven.
- The playbook's routing matrix, mode details, default loop, stop conditions, and handoff packets point at `$noootwo-debug` instead of carrying a diagnosis method.
- Removed the duplicated build method from the slice step: each slice runs the check its owning skill names.
- Added a `noootwo-debug` handoff packet.
- Rewrote the description around scheduling: `schedule` replaces `run`, and a bare bug is no longer one of its triggers because `noootwo-debug` owns it.


## v0.9.0

- Restructured the body into five steps with a completion criterion each: read repo truth, route, choose the mode, build in slices, close.
- Replaced keyword-stuffed triggers with one trigger per branch, cutting the description from 541 to 180 characters.
- Cross-skill routing now states the mechanism: read the named skill's `SKILL.md` and follow it. Bare `$noootwo-x` references are gone from the body and rejected by the validator.
- Added the rework table, which maps an observed failure to the layer that owns it.
- Kept the pause rule: while a product decision is unsettled, the loop stops.
- Merged `product-interview-handoff.md` into `references/workflow-playbook.md`; five reference files become four.


## v0.8.0

- Replaced vague "non-trivial" triggers with concrete task-start triggers: new feature, product idea, multi-file/cross-skill change, bugfix, refactor, release, onboarding/handoff, recovery, and correction-loop routing.
- Added routing-as-invocation: specialist triggers must explicitly invoke `$noootwo-product` / `$noootwo-design` / `$noootwo-review` / `$noootwo-state`; unavailable skills are declared with a fallback instead of silent substitution.
- Added rework diagnosis after user rejection: diagnose the failed layer and route to the matching skill instead of polishing the same layer.
- Compacted the handoff contract into per-specialist packets.
- Added workflow evals for wake-on-feature, specialist invocation, interview pause, and rework diagnosis.


## v0.7.7

- Added a paused `product-interview` execution mode for unresolved product choices.
- Prevented Workflow from treating a recommended default, "continue", or a build request as user approval.
- Added `execution_status` to the Product Interview Handoff and blocked Design/implementation routing until Product convergence or explicit delegation.
- Routed product work through Product Clarity Gate first so clear requests do not enter a waiting state.
- Preserved the user's presentation language through Product handoff and kept canonical English keys internal.

## v0.7.6

- Preserved explicit grill-style/detail-confirmation requests as `interview_depth: deep` when routing to `noootwo-product`.
- Added `references/product-interview-handoff.md` with initialized fields for checked facts, source paths, decision-ledger state, intent-fit status, and risk evidence.
- Kept Workflow from conducting the product interview itself while preventing deep requests from being compressed into a light checkpoint.

## v0.7.5

- Routed multi-question product ambiguity to `noootwo-product` Decision Interview instead of letting Workflow become a long product interview.
- Updated handoff packets to include whether Decision Interview is needed and what facts were already checked.
- Kept Alignment Checkpoint as a single decision control for non-trivial work.

## v0.7.4

- Added correction-loop routing: strong rejection first diagnoses the failed layer, repeated related rejection routes to Product Reality Check or Style Evidence Check before more implementation.
- Updated design handoff packets to carry selected-direction or style-evidence risk when non-quick UI work is direction-sensitive.
- Kept the control risk-triggered so small direct edits and quick polish do not gain extra ceremony.
- Narrowed trigger metadata and agent prompts around non-trivial, cross-skill, release-bound, recovery, and correction-loop work.

## v0.7.3

- Added Product-to-Design Handoff routing language so non-quick UI work reaches `noootwo-design` with real user, scenario, main path, states, scope cuts, acceptance criteria, open product decisions, and design constraints.
- Updated workflow handoff playbook and OpenAI prompt to keep product decisions in `noootwo-product` and design execution in `noootwo-design`.

## v0.7.2

- Added retrieval-first context control: use local file and heading searches before reading long documents.
- Clarified that whole-document reads are for audits, consistency checks, or failed targeted search, not the default path.

## v0.7.1

- Routed greenfield software product ideas, blank-project product starts, broad product visions, and product brainstorming to `noootwo-product` Product Discovery before design or implementation.
- Updated workflow handoff packets, routing references, and agent prompt text so Product receives the raw idea, assumptions, first-user ambiguity, and first-loop decision.
- Clarified that product-shaped ambiguity should use Product Discovery or a Product Choice Challenge instead of generic brainstorming-style process.

## v0.7.0

- Added specialist-first routing for `noootwo-product` when requirements, feature scope, user paths, IA, interaction models, states, acceptance criteria, usability, or cognitive cost are unclear.
- Updated lifecycle guardrails, routing matrices, and handoff packets so Product can run before Design or implementation.
- Clarified that architecture choices continue through `noootwo-review` rather than a separate public skill.
- Updated local sync behavior to prefer `~/.agents/skills` and remove duplicate Noootwo copies from `~/.codex/skills` when an agent-root copy exists.

## v0.6.1

- Added lifecycle guardrails for read-first, pre-implementation, during-work, and pre-close/pre-submit decisions.
- Clarified that TDD or repro-first is risk-triggered for bugfixes, behavior changes, public contracts, regression risk, data/migration risk, and hard-to-prove shared code.
- Made submit/release-bound code route through a review judgment while keeping small direct work low-ceremony.

## v0.6.0

- Added a lightweight `alignment checkpoint` for non-trivial work where one unresolved decision can materially change implementation.
- Added closure triggers for verification, docs impact, and review/design follow-up before finishing non-direct work.
- Kept small direct edits ceremony-free so workflow control does not become the default cost of every task.

## v0.5.0

- Aligned `noootwo-workflow` version with the unified Noootwo Vibe `0.5.0` skill set.
- No workflow behavior changed in this release.

## v0.4.0

- Aligned `noootwo-workflow` version with the unified Noootwo Vibe `0.4.0` skill set.
- No workflow behavior changed in this release.

## v0.3.0

- Added project onboarding mode for skill inventory, foundation health checks, and controlled takeover of unfamiliar repositories.
- Added `project-skill-audit`, `project-foundation-check`, and `minimal-foundation-templates` references.
- Updated workflow routing so project gaps can be handed to docs/review/design without bloating the default skill body.

## v0.2.0

- Added explicit direct, planned, diagnostic, release, and recovery modes.
- Added compact handoff packet rules for routing to docs, review, and design specialists.
- Expanded the workflow playbook with mode details, release checklists, cost controls, and stop conditions.

## v0.1.0

- Initial public skill for AI development workflow control, routing, planning, verification, and closure.
