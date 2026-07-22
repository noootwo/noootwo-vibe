# noootwo-workflow Releases

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
