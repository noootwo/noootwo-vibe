# ADR 0005: Add Product Skill And Keep Architecture As Review Lens

- Status: accepted
- Date: 2026-07-17

## Context

Noootwo Vibe's four-skill model covered workflow, docs, review, and design. That left a gap between project routing and UI execution: user goals, feature scope, information architecture, interaction paths, state models, cognitive cost, and acceptance criteria could be decided implicitly by the implementation or visual design agent.

The repeated failure mode is a product that looks implemented but feels like it was designed for developers, backend fields, internal system structure, or the requester-as-operator instead of the real end user.

At the same time, adding a sixth architecture skill would split technical judgment away from the existing code review surface and increase routing ambiguity. Architecture, test strategy, performance, maintainability, and technical tradeoff judgment already fit the `noootwo-review` lens model.

## Decision

Add `noootwo-product` as the fifth public skill. It acts as a product manager and real-user advocate. Its default output is a lightweight `Product Checkpoint`, not a large PRD.

`noootwo-product` owns:

- real user, use context, and user outcome
- feature scope and should/should-not-build decisions
- user flow, information architecture, interaction model, and state model
- cognitive-cost and usability risk
- user-behavior acceptance criteria
- `Product Choice Challenge` when one product decision materially changes the work

Keep public skills in this order: `noootwo-workflow`, `noootwo-product`, `noootwo-design`, `noootwo-review`, `noootwo-docs`.

Do not add `noootwo-architecture`. Architecture remains a `noootwo-review` lens routed by `noootwo-workflow`.

## Consequences

- Workflow can route `Workflow -> Product -> Design` when a feature, flow, IA, interaction, state, or acceptance path is unclear.
- Design focuses on UI, visual systems, frontend execution, artifacts, and handoff after product path clarity.
- Review remains the owner for architecture boundaries, technical judgment, test strategy, performance, maintainability, code quality, and submit/release gates.
- Docs persists stable Product, Design, Review, Workflow, release, and repository facts in the correct layer.
- Product must stay low-friction: small copy/style fixes do not become PRDs, and challenges expose only the highest-impact product choice.
