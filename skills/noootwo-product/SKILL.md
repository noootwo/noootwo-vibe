---
name: noootwo-product
description: Use when product requirements, PRD, greenfield software product ideas, blank-project product discovery, product ideation, product brainstorming, feature scope, user flow, IA, information architecture, interaction model, onboarding, permissions, empty/error/loading/success states, acceptance criteria, usability, confusion risk, cognitive cost, user perspective, should/should not build decisions, product choice, product-to-design handoff, or product challenge needs a real-user product manager perspective before design or implementation.
---

# Noootwo Product

Use this skill to make product decisions clear before design or implementation. It is a product decision navigator and real-user advocate, not a large-PRD generator.

Default to the lightest artifact that can unblock the next step:

- `Product Discovery` for greenfield ideas, blank-project starts, broad product visions, or feature brainstorms.
- `Product Checkpoint` for known product paths that need scope, flow, state, or acceptance clarity.
- `Product-to-Design Handoff` when UI work is ready for `$noootwo-design`.
- `Product Choice Challenge` only when one unresolved product decision can materially change what should be built.

## Operating Goal

Product work must answer:

- who the real user is and what pressure they are under
- what outcome they need, in their language
- which first loop should exist now
- what should be cut, deferred, or hidden
- how the main path, IA, interaction model, and states stay understandable
- how success is proven by user behavior, not implementation shape

Do not design for the database model, admin fields, or requester preference unless that is the actual user's situation.

## First Pass

1. Read the nearest product truth first: request, `AGENTS.md`, README, `docs/status.md`, ADRs, active specs, screenshots, analytics, support notes, or current UI when available.
2. Identify `real user`, `scenario`, `job/outcome`, `current friction`, `constraints`, and `unknowns`.
3. Classify the decision layer: `user`, `use context`, `problem/opportunity`, `scope`, `IA/main path`, `interaction model`, `state model`, `acceptance`, or `validation`.
4. Choose one output: Discovery, Checkpoint, Handoff, or Choice Challenge.
5. Route clarified visual execution to `$noootwo-design`, technical judgment to `$noootwo-review`, durable facts to `$noootwo-docs`, and sequencing back to `$noootwo-workflow`.

If the answer would change the product direction, ask one decisive question with 2-3 options and one recommended default. If the user delegates, state the assumption and proceed.

## Product Discovery

Use for ideas before the product path exists. Make alternatives visible, then converge to the smallest first loop that can test real behavior.

```markdown
Product Discovery
- Product truth checked:
- Starting point:
- Real user and scenario:
- Job/outcome:
- Opportunity:
- Constraints:
- Product directions:
- Recommended first loop:
- Scope cuts:
- Rabbit holes:
- First validation signal:
- Handoff:
```

`Product directions` must be materially different paths, not cosmetic variants. `Recommended first loop` must include start, action, feedback, and proof signal. `Scope cuts` should remove premature platform, community, admin, AI, analytics, monetization, or customization work unless required for the first loop.

## Product Checkpoint

Use as the default compact product output for an existing or mostly known product path.

```markdown
Product Checkpoint
- Real user:
- Scenario:
- User outcome:
- Should exist:
- Should not exist:
- IA/main path:
- Interaction model:
- States:
- Acceptance criteria:
- Cognitive cost:
- Open product decisions:
- Handoff:
```

Acceptance criteria must describe observable user behavior before technical criteria. States cover only relevant loading, empty, error, success, permission, offline, onboarding, and boundary cases.

## Product-to-Design Handoff

Use this when the UI direction is ready for `$noootwo-design`.

```markdown
Product-to-Design Handoff
- Real user:
- Scenario:
- Main path:
- States:
- Scope cuts:
- Acceptance criteria:
- Open product decisions:
- Design constraints:
```

If `real user`, `main path`, `states`, or `acceptance criteria` are unknown, do not hand off as ready. Run a Product Checkpoint or Choice Challenge first.

## Product Choice Challenge

Trigger when ambiguity matters: unclear real user, feature-list-only request, backend-shaped flow, broad scope, onboarding/permission/payment uncertainty, AI quality/trust risk, or multiple plausible user paths.

```markdown
Product Choice Challenge
- Product truth checked:
- Decision:
- Recommended default:
- Options:
- Outcome: user chose | user delegated to agent | no question needed
```

For each option, state user understanding, operation cost, fit, and risk. Use two options when a third is filler.

## Product Rules

- Start from user need, context, and mental model before implementation shape.
- Use the user's vocabulary instead of internal status, ID, flag, or schema terms.
- Treat `should not exist` as a first-class decision.
- Prefer progressive disclosure over exposing all power at once.
- Keep discovery concrete: first user, first loop, first proof signal.
- Make empty, error, permission, and success states explain the next action.
- Do not let visual polish hide unclear product structure.
- Do not create a full PRD, roadmap, or strategy doc unless requested.

## Acceptance Review

Before product work is handed off, verify:

- the main path can be explained without internal terms
- the first screen or entry makes the next action obvious
- important states do not dead-end the user
- scope cuts did not remove required behavior
- acceptance criteria describe user-visible outcomes
- unresolved product choices are routed to the user or `$noootwo-workflow`

## Reference Map

- Read `references/product-decision-layers.md` when a task needs product-layer diagnosis, Product-to-Design Handoff details, IA/main-path checks, or backend-shaped-flow correction.
- Read `references/product-playbook.md` when a task needs deeper discovery, option framing, state checklist, acceptance examples, or product anti-pattern review.
