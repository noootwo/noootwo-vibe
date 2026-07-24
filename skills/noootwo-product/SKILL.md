---
name: noootwo-product
description: "Use for product discovery and product decisions before design or implementation: Decision Interview, real user, scenario, first loop, scope, IA/main path, interaction/state model, acceptance criteria, Product Reality Check, Product Choice Challenge, and Product-to-Design Handoff. Trigger for greenfield ideas, unclear or rejected product direction, feature-list-only requests, backend-shaped flows, or UI work missing product path."
---

# Noootwo Product

Use this skill to make product decisions clear before design or implementation. It is a product decision navigator and real-user advocate, not a large-PRD generator.

Default to the lightest artifact that can unblock the next step:

- `Decision Interview` when one or more product decisions must be confirmed before scope, design, or implementation.
- `Product Discovery` for greenfield ideas, blank-project starts, broad product visions, or feature brainstorms.
- `Product Checkpoint` for known product paths that need scope, flow, state, or acceptance clarity.
- `Product Reality Check` when the output may be user-confusing, assumption-heavy, naive-AI, or repeatedly rejected.
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
4. If a missing answer would change product direction, run Decision Interview before choosing the final output.
5. Choose one output: Discovery, Checkpoint, Handoff, or Choice Challenge.
6. Use Product Reality Check before handoff when the request is greenfield, confusing, strongly criticized, or likely to produce a fake-PM answer.
7. Route clarified visual execution to `$noootwo-design`, technical judgment to `$noootwo-review`, durable facts to `$noootwo-docs`, and sequencing back to `$noootwo-workflow`.

If the answer would change the product direction, ask one decisive question with 2-3 options and one recommended default. If the user delegates, state the assumption and proceed.

## Decision Interview

Use this when product ambiguity is high enough that acting now would likely waste work: greenfield ideas, vague requirements, feature-list-only requests, backend-shaped flows, rejected product direction, or UI/implementation work missing `real user`, `main path`, `states`, or `acceptance criteria`.

Rules:

- Inspect repo truth, current UI, docs, screenshots, analytics, or support notes first.
- Do not ask the user for facts that can be discovered from the environment.
- Ask only product tradeoffs that materially change scope, IA, flow, states, or acceptance.
- Ask one highest-impact question at a time; include 2-3 meaningful options and one recommended default.
- Wait for the user's answer unless they explicitly delegate; when delegated, record the assumption and continue.
- Stop as soon as `real user`, `scenario`, `main path`, `scope cuts`, `states`, and `acceptance criteria` are enough for Product-to-Design Handoff or implementation planning.

Do not turn Decision Interview into a fixed questionnaire. If the next question would not change the plan, proceed with a stated assumption.

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

Use Decision Interview inside Product Discovery only when one unresolved decision blocks convergence.

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

## Product Reality Check

Use this only when risk is high enough to justify the extra check: blank-product discovery, vague "stand in the user's shoes" requests, user confusion, repeated correction, or AI-looking product decisions.

```markdown
Product Reality Check
- Real user:
- Moment of use:
- Current alternative:
- First loop:
- User comprehension check:
- Naive-AI failure:
- Decision: keep | revise | ask | stop
- Return action:
```

If the user would not understand the next action, why it matters, or whether progress happened, return to Product Discovery, Checkpoint, or Choice Challenge before design or implementation.

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

Decision Interview may run several Product Choice Challenge turns, but each turn must resolve only one decision.

## Product Rules

- Start from user need, context, and mental model before implementation shape.
- Use the user's vocabulary instead of internal status, ID, flag, or schema terms.
- Treat `should not exist` as a first-class decision.
- Prefer progressive disclosure over exposing all power at once.
- Keep discovery concrete: first user, first loop, first proof signal.
- Make empty, error, permission, and success states explain the next action.
- Treat strong user criticism as evidence to diagnose, not as an automatic instruction to add more features.
- Name the most likely naive-AI failure before handoff when the task is broad, greenfield, or repeatedly corrected.
- Do not let visual polish hide unclear product structure.
- Do not create a full PRD, roadmap, or strategy doc unless requested.

## Acceptance Review

Before product work is handed off, verify:

- the main path can be explained without internal terms
- the first screen or entry makes the next action obvious
- important states do not dead-end the user
- scope cuts did not remove required behavior
- acceptance criteria describe user-visible outcomes
- Product Reality Check ran or was intentionally skipped for low-risk work
- Decision Interview stopped because the path is ready, the user delegated the decision, or no material question remains
- unresolved product choices are routed to the user or `$noootwo-workflow`

## Reference Map

- Read `references/product-decision-layers.md` when a task needs product-layer diagnosis, Product-to-Design Handoff details, IA/main-path checks, or backend-shaped-flow correction.
- Read `references/product-playbook.md` when a task needs deeper discovery, option framing, state checklist, acceptance examples, or product anti-pattern review.
- Read `references/product-reality-check.md` when a product answer feels PM-shaped but may still be hard for the real user to understand or trust.
