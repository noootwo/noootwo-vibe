# noootwo-product Releases

## v0.5.2

- Added deep Decision Interview for explicit grill-style/detail-confirmation requests, high-risk scope, previously rejected interpretations, or several dependent product choices.
- Split the ledger into confirmed, delegated, deferred, rejected, and active-risk states.
- Added cumulative ledger guidance: recap confirmed decisions, show checked facts, explain why the next question matters, ask conditional follow-ups, and stop with a convergence summary once the path is ready.
- Added explicit final intent-fit confirmation and a handoff block requiring decision, owner, and evidence for material risk.
- Added detailed-confirmation and workflow-handoff evals without creating a public `noootwo-grilling` skill.

## v0.5.0

- Added `Decision Interview` as the lightweight continuous-confirmation loop for high-ambiguity product work.
- Required the loop to inspect repo/UI/docs facts first, ask only product tradeoffs, ask one material question at a time, offer 2-3 meaningful options with a recommended default, and stop once the path is ready.
- Added eval prompts for ambiguous product requests, discoverable facts that should not be asked back to the user, and stopping once Product-to-Design Handoff is ready.
- Kept the mechanism inside `noootwo-product` instead of adding a public `noootwo-grilling` skill.

## v0.4.0

- Added `Product Reality Check` for user-confusing, assumption-heavy, naive-AI, greenfield, or repeatedly corrected product work.
- Added `references/product-reality-check.md` with current alternative, first loop, comprehension check, naive-AI failure, decision, and return action rules.
- Added eval prompts for product reality gaps and confusing user paths without making Product Discovery a full PRD process.
- Narrowed trigger metadata and agent prompts around real-user decisions, first loops, confusing paths, rejected product direction, feature-list-only requests, and backend-shaped flows.
- Added explicit manual pass/fail language to the new Product Reality eval prompts.

## v0.3.0

- Reframed `noootwo-product` as a product decision-layer navigator before design or implementation.
- Added fixed `Product-to-Design Handoff` fields: real user, scenario, main path, states, scope cuts, acceptance criteria, open product decisions, and design constraints.
- Added `references/product-decision-layers.md` for user/context/outcome/scope/IA/interaction/state/acceptance/validation diagnosis and backend-shaped-flow correction.
- Added product eval prompts for greenfield first loop, feature-list-only requests, backend-shaped flows, and handoff readiness.

## v0.2.0

- Added `Product Discovery` for greenfield software product ideas, blank-project starts, broad product visions, and product brainstorming before design or implementation.
- Borrowed useful brainstorming mechanics: context-first intake, one decisive question at a time, 2-3 materially different options, recommended defaults, and convergence to a first usable product loop.
- Kept Product lightweight by explicitly avoiding the generic brainstorming hard gate of mandatory specs, commits, or formal review unless the user or project risk requires that artifact.
- Expanded the product playbook with greenfield scope, no-gos, rabbit holes, and first validation signals.

## v0.1.0

- Added the fifth Noootwo public skill for real-user product management, Product Checkpoints, and Product Choice Challenges.
- Added scope, user-flow, IA, interaction-model, state-model, cognitive-cost, and acceptance-criteria guidance.
- Established routing boundaries: Product clarifies product path, Design handles UI/frontend execution, Review handles architecture and technical quality, Docs persists stable decisions.
