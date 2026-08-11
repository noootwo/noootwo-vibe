---
name: noootwo-product
description: "Use for product discovery and product decisions before design or implementation: Decision Interview, real user, scenario, first loop, scope, IA/main path, interaction/state model, acceptance criteria, Product Reality Check, Product Choice Challenge, and Product-to-Design Handoff. Trigger for greenfield ideas, unclear or rejected product direction, feature-list-only requests, backend-shaped flows, UI work missing product path, or explicit requests for detailed sequential requirement confirmation."
---

# Noootwo Product

Use this skill to make product decisions clear before design or implementation. It is a product decision navigator and real-user advocate, not a large-PRD generator.

Default to the lightest artifact that can unblock the next step:

- `Decision Interview` only when a material product decision is still unresolved, high-risk, contradictory, or the user explicitly asks for sequential confirmation.
- `Product Discovery` after the material greenfield choices are settled, for blank-project starts, broad product visions, or feature brainstorms.
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
4. Run the Clarity Gate below before choosing an output. A detailed request that already answers the relevant product decisions is clear; do not manufacture missing questions.
5. Enter Decision Interview only when the Clarity Gate says `one-material-gap`, `ambiguous/high-risk`, or `explicit-interview`. Otherwise choose Discovery, Checkpoint, Handoff, or direct implementation.
6. Use Product Reality Check before handoff only when a greenfield path is still unproven or user-confusing, the direction was strongly criticized, or the output is likely to produce a fake-PM answer.
7. Route clarified visual execution to `$noootwo-design`, technical judgment to `$noootwo-review`, durable facts to `$noootwo-docs`, and sequencing back to `$noootwo-workflow`.

If the Clarity Gate finds one material gap, ask one decisive question with 2-3 options and one recommended default, then wait. A recommended default is not a user decision. Treat a request to build, start, continue, or use best practices as permission to work only after the product path is confirmed; it is not delegation of unresolved product choices. Only explicit language such as "you decide", "choose for me", or "use your recommended default and proceed" counts as delegation, and the resulting assumption must be recorded. If the Clarity Gate finds multiple dependent gaps, high risk, a rejected direction, or an explicit request for step-by-step confirmation, use `deep Decision Interview`: keep a cumulative decision ledger, recap what is already confirmed before each next question, explain why the question matters, and continue with conditional follow-ups until the path is ready.

## Clarity Gate

Decision Interview is risk-triggered, not a mandatory stage for every product request. Classify the latest request after checking repo truth:

- `clear`: the user has supplied, or the repo reliably establishes, the real user or existing target, scenario, outcome, scope boundary, main path, relevant states, and observable acceptance. There is no contradiction or material product choice left. Skip Decision Interview.
- `one-material-gap`: one unresolved choice could change the first loop, scope, trust boundary, main path, states, or acceptance. Use a light one-question interview.
- `ambiguous/high-risk`: several dependent choices are missing, the request conflicts with current truth, the direction was rejected, or the choice affects trust, permissions, data, payment, or irreversible scope. Use deep Decision Interview.
- `explicit-interview`: the user explicitly asks to confirm requirements step by step, grill the details, or keep asking until the result matches their intent. Use deep Decision Interview even if the request looks mostly clear.

Clarity rules:

- Treat details explicitly supplied by the user as confirmed unless they conflict or are genuinely ambiguous. Do not ask the user to repeat known facts.
- Do not turn technical implementation choices, naming choices, or low-impact preferences into Product questions when the user-visible path is already clear. Record a local implementation assumption when appropriate.
- If the request is `clear`, produce the smallest useful `Product Checkpoint`, `Product-to-Design Handoff`, or direct implementation route. Do not show an empty interview ledger.
- If the request is `one-material-gap`, ask only that question. Do not expand a light question into a full checklist.
- If the request is `ambiguous/high-risk` or `explicit-interview`, use the waiting and ledger rules below.

## Execution Gate

When activated, Decision Interview is an interactive gate, not a report that the agent can complete alone. When the Clarity Gate says `clear`, this section does not apply.

- When the gate is open, the current response must be a `Decision Interview Turn`: one question, the relevant facts, the current ledger, and the reason the question matters.
- While `Interview state: awaiting_user_answer`, do not implement, edit files, create a design, write an implementation plan, hand off to Design, or present a final product conclusion. Read-only inspection of repo truth is allowed when it informs the next question.
- Do not treat silence, `continue`, `start`, `build it`, `help me do it`, or `follow best practices` as an answer to the current question. Re-state or narrow the same question when needed.
- Every material decision must be either explicitly selected by the user or explicitly delegated. The agent's recommendation, a guessed preference, or the original goal statement cannot close the decision.
- If a user answer contains several choices, classify all of them in the ledger but ask at most one follow-up question for the highest-impact unresolved choice.
- After the user answers, keep the interview state as `awaiting_user_answer` whenever another material choice remains. Only change it to `converged` after the path is ready and the final intent-fit check is confirmed, or to `delegated` after explicit delegation.

The following is a semantic contract, not text that must be printed verbatim. Machine-facing state names remain canonical in the handoff, but normal user-facing responses must use the user's language and natural wording.

For example, in a Chinese conversation, render the waiting turn as:

```markdown
需求确认（第一个关键问题）
- 已确认：
- 已查到的事实：
- 现在需要确认：
- 为什么重要：
- 可选方案：
- 我的建议（尚未选择）：
- 请你确认：
- 当前状态：等待你的确认
```

Use equivalent labels in the user's primary language. Do not expose raw labels such as `Interview state`, `Facts checked`, or `blocked on user confirmation` unless the user asks for the internal state or the response is a machine-facing handoff. Do not append a solution, implementation steps, file edits, or a handoff in the same waiting turn.

## Presentation Language

- Infer the presentation language from the latest user message and prefer the user's own vocabulary. If the user writes Chinese, use Chinese headings and explanations; if English, use English; if the user mixes languages, follow the dominant language while preserving intentional mixed-language terms.
- Do not force the whole response into one language. Keep code, API names, file paths, package names, product names, and exact enum/state values unchanged when they need to remain copyable.
- Translate structural labels and explanatory prose, not technical identifiers. Explain an unfamiliar technical identifier in the user's language on first use when it matters.
- Use natural sentences and only show fields that carry information. The ledger and handoff may keep canonical English keys for interoperability, but they are not the default user-facing format.
- The artifact templates below describe required meaning, not fixed display text. Localize their headings and field labels whenever they are shown to the user.

## Decision Interview

Use this when product ambiguity is high enough that acting now would likely waste work: greenfield ideas with an unspecified first user or loop, vague requirements, feature-list-only requests, backend-shaped flows, rejected product direction, or UI/implementation work missing `real user`, `main path`, `states`, or `acceptance criteria`.

Rules:

- Inspect repo truth, current UI, docs, screenshots, analytics, or support notes first.
- Do not ask the user for facts that can be discovered from the environment.
- Ask only product tradeoffs that materially change scope, IA, flow, states, or acceptance.
- Ask one highest-impact question at a time; include 2-3 meaningful options and one recommended default.
- Wait for the user's answer by default. A build request or an instruction to continue does not override this wait. When the user explicitly delegates the current choice, record the assumption and continue.
- In `deep Decision Interview`, begin each turn with a short `confirmed so far` recap, name the one open decision, and state how its answer changes the plan.
- Show the relevant discoverable facts that shaped the current question; do not make the user restate facts already present in the repo or current flow.
- After each answer, classify it as confirmed, delegated assumption, deferred, rejected, active risk, or still ambiguous; use the result to choose the next question instead of restarting a checklist.
- Use the following decision gates in order, skipping only a gate settled by repo evidence or an explicit user answer: real user and moment of use, user outcome, first loop, scope and non-goals, main path and IA, interaction and state behavior, then observable acceptance. These are routing gates, not a questionnaire to dump into one response.
- Before handoff, summarize confirmed decisions, assumptions, deferred items, rejected ideas, active risks, and the next artifact. Add a brief intent-fit check: what user problem the first loop solves and what it intentionally does not solve.
- In deep mode, ask one explicit final intent-fit confirmation after the convergence summary unless the user delegated the final decision. Do not infer final fit from earlier goal statements. If the answer is no, reopen only the highest-impact mismatch; if yes, stop. Do not ask again unless a new contradiction appears.
- Do not hand off with an unresolved active risk that would change the main path, trust boundary, scope, or acceptance. Resolve it with a decision, owner, and evidence; get explicit user acceptance; or mark it as an intentional out-of-scope cut.
- Stop as soon as `real user`, `scenario`, `main path`, `scope cuts`, `states`, and `acceptance criteria` are enough for Product-to-Design Handoff or implementation planning, every material choice is explicit or delegated, the final intent fit is confirmed or delegated, and no unresolved material risk remains.

Do not turn Decision Interview into a fixed questionnaire. If the next question would not change the plan, proceed with a stated assumption only when the user has explicitly delegated that level of detail. Otherwise, leave it as a non-material open note and keep the agent from inventing a product decision.

## Product Discovery

Use for ideas before the product path exists. Make alternatives visible, then converge to the smallest first loop that can test real behavior.

When Decision Interview is triggered, Product Discovery is a later convergence artifact. The first response must be a `Decision Interview Turn`; do not fill in a recommended first loop and start design or implementation before the user confirms the material choices.

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

Use as the default compact product output for an existing, mostly known, or explicitly detailed product path. When the Clarity Gate says `clear`, produce it directly without Decision Interview.

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

Use this only when risk is high enough to justify the extra check: blank-product discovery with an unproven user loop, vague "stand in the user's shoes" requests, user confusion, repeated correction, or AI-looking product decisions.

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

Decision Interview may run several Product Choice Challenge turns, but each turn must resolve only one decision. Showing the recommended option does not count as `user chose`.

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
- Decision Interview either stopped because the path is ready and all material choices were explicitly selected or delegated, or it was skipped because the Clarity Gate found no material unresolved product choice
- Deep Decision Interview recapped the accumulated decisions, separated deferred from rejected items, resolved or explicitly accepted material risks, and passed the intent-fit check before stopping
- unresolved product choices are routed to the user or `$noootwo-workflow`

## Reference Map

- Read `references/product-decision-layers.md` when a task needs product-layer diagnosis, Product-to-Design Handoff details, IA/main-path checks, or backend-shaped-flow correction.
- Read `references/product-playbook.md` when a task needs deeper discovery, option framing, state checklist, acceptance examples, or product anti-pattern review.
- Read `references/product-reality-check.md` when a product answer feels PM-shaped but may still be hard for the real user to understand or trust.
