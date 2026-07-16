---
name: noootwo-product
description: Use when product requirements, PRD, feature scope, user flow, IA, information architecture, interaction model, onboarding, permissions, empty/error/loading/success states, acceptance criteria, usability, confusion risk, cognitive cost, user perspective, should/should not build decisions, product choice, or product challenge needs a real-user product manager perspective before design or implementation.
---

# Noootwo Product

Use this skill to protect the real user's task path before design or implementation. It is a product manager and user advocate skill, not a large-PRD generator.

Default to a compact `Product Checkpoint`. Use `Product Choice Challenge` only when one unresolved product decision can materially change what should be built.

## Operating Goal

Make product work answer:

- who the real user is
- what they are trying to accomplish
- what should exist now and what should not
- how the main path stays obvious, efficient, and low-friction
- which states and edge cases affect comprehension
- how success is proven by user behavior, not implementation details

Do not design for the developer, internal data model, admin field names, or the current requester alone unless they are the real end user.

## First Pass

1. Read the nearest product truth first: request text, `AGENTS.md`, README, `docs/status.md`, ADRs, active specs, screenshots, analytics, support notes, or current UI when available.
2. Identify the real user, use context, desired outcome, and current friction.
3. Classify the work: `new feature`, `scope decision`, `user flow`, `information architecture`, `interaction model`, `state model`, `onboarding/permission`, `acceptance criteria`, or `usability review`.
4. Decide whether a direct `Product Checkpoint` is enough or whether a `Product Choice Challenge` is needed.
5. Route clarified UI/visual execution to `$noootwo-design`, technical judgment to `$noootwo-review`, durable facts to `$noootwo-docs`, and sequencing back to `$noootwo-workflow`.

## Product Checkpoint

Use this as the default output. Keep it short unless the user explicitly asks for a PRD.

```markdown
Product Checkpoint
- Real user:
- User outcome:
- Should exist:
- Should not exist:
- Main path:
- Cognitive cost:
- States:
- Acceptance criteria:
- Challenge:
- Handoff:
```

Field rules:

- `Real user`: name the actual role and context; avoid generic "user" when a concrete persona is knowable.
- `User outcome`: state the observable result the user wants, not the feature name.
- `Should exist`: include only what helps the current user outcome.
- `Should not exist`: cut or defer confusing, premature, programmer-facing, or low-value surface area.
- `Main path`: describe entry, key steps, and success feedback.
- `Cognitive cost`: name likely confusion, hesitation, hidden concepts, excess choices, or mismatched language.
- `States`: cover only relevant loading, empty, error, success, permission, offline, onboarding, or boundary states.
- `Acceptance criteria`: write user-behavior checks; do not use component names, DOM shape, API fields, or implementation tasks as acceptance.
- `Challenge`: record `needed`, `not needed`, or `already resolved`.
- `Handoff`: name the next owner skill and the decision or artifact it needs.

## Product Choice Challenge

Trigger this when product ambiguity matters:

- the goal is unclear or the request is only a feature list
- multiple user paths are plausible and the choice changes comprehension
- the proposed flow mirrors backend fields, internal systems, or developer mental models
- scope is too broad, too fragmented, too early, or too complex
- onboarding, permissions, payment, login, empty/error states, first use, or the core loop is unclear
- the user says the result is abstract, hard to understand, hard to use, too complex, or made for developers

Run the challenge as a small decision control:

1. Inspect repo and product truth first.
2. Name the single highest-impact product decision.
3. Offer two or three mutually exclusive options with one recommended default.
4. For each option, state user understanding, operation cost, fit, and risk.
5. Record one outcome: `user chose`, `user delegated to agent`, or `no question needed`.

Skip it for small copy, small style, or obvious local fixes with an existing product path.

## Product Rules

- Prefer the simplest path that lets the real user complete the job.
- Use the user's vocabulary, not implementation or database vocabulary.
- Reduce choices until each remaining choice changes a user outcome.
- Treat "do not build" as a first-class product decision.
- Prefer progressive disclosure over exposing all power at once.
- Make empty, error, permission, and success states explain what the user can do next.
- Do not let visual polish hide unclear product structure.
- Do not let technical feasibility become the product rationale unless it changes user value or risk.
- Do not create a full PRD, roadmap, or strategy doc unless explicitly requested.

## Product Acceptance Review

Before handing off a user-visible feature, check:

- the main path can be explained without internal terms
- the first screen or entry point makes the next action obvious
- important states do not dead-end the user
- scope cuts did not remove required behavior
- acceptance criteria describe user-visible outcomes
- unresolved product choices are routed to `$noootwo-workflow` or the user

## Reference Map

Read `references/product-playbook.md` when a task needs deeper product critique, product option framing, IA/state checklist, acceptance criteria examples, or anti-pattern review.
