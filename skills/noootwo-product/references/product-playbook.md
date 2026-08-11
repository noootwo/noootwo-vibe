# Product Playbook

Use this when the compact `Product Checkpoint` is not enough.

For layer diagnosis and Product-to-Design readiness, use `product-decision-layers.md` first. This playbook gives deeper discovery, option framing, state, acceptance, and anti-pattern checks.

Use `product-reality-check.md` when output may be PM-shaped but user-confusing, naive-AI, assumption-heavy, or repeatedly corrected.

## Practice Basis

- User-centered product work starts from user needs, context, and mental models before implementation shape.
- Good AI-assisted product work makes assumptions explicit, proposes alternatives, asks only the choice that changes the result, and converges before implementation.
- Low-friction products reduce exposed concepts, use familiar language, and make the next action obvious.
- Product work should cut scope as deliberately as it adds scope.
- Product discovery should move from outcome to opportunity, then to solution options and validation signals.
- Good shaping names the appetite, no-gos, and likely rabbit holes before a team commits to build.
- Fast product exploration can borrow sprint mechanics: map the path, sketch alternatives, decide, prototype only when useful, and test the riskiest assumption.

## Decision Interview Notes

Use this when a product decision blocks progress. Choose the lightest depth that still protects the outcome:

- `light`: one or a few questions for ordinary ambiguity.
- `deep`: explicit user request for grill-style/detail confirmation, high-risk scope, a previously rejected interpretation, or several dependent product choices.

## Clarity Gate

Run this before starting the shared loop. Decision Interview is not a default ceremony.

- `clear`: the request and checked repo truth establish the user or existing target, scenario, outcome, scope boundary, main path, relevant states, and observable acceptance with no material contradiction. Skip the interview and produce a compact Checkpoint, Handoff, or direct route.
- `one-material-gap`: exactly one unresolved product choice would change user value, scope, main path, state behavior, trust, or acceptance. Run a light interview.
- `ambiguous/high-risk`: several dependent choices, conflicting facts, rejected direction, or trust/payment/permission/data scope. Run a deep interview.
- `explicit-interview`: the user asks for step-by-step confirmation or grill-style detail. Run a deep interview.

Do not manufacture gaps from technical implementation details or low-impact preferences. An explicit user statement is confirmed unless it conflicts with evidence or has more than one reasonable product meaning.

When the Clarity Gate selects light or deep, the shared loop is:

1. Inspect discoverable facts first.
2. Ask one material tradeoff.
3. Recommend a default with 2-3 meaningful options.
4. Stop and wait for the user's answer.
5. Record the answer or explicitly delegated assumption.
6. Stop when the path is ready for handoff or implementation.

Do not ask a fixed intake list. The next question must change first loop, scope, main path, state treatment, or acceptance.

## Execution Gate

When Decision Interview is active, the agent is in an awaiting-user state. The recommendation is an option, not approval. Do not apply this execution block to a clear request that was deliberately routed around the interview.

- A request to build, start, continue, or follow best practices does not answer the current product question.
- Only explicit delegation such as "you decide", "choose for me", or "use your recommended default and proceed" permits a delegated assumption.
- Until the current question is answered or explicitly delegated, allow read-only fact inspection only. Do not edit files, create a design, write an implementation plan, route to Design, or claim a final product direction.
- If another material choice remains after the answer, ask the next single conditional question and remain in the awaiting-user state.
- The first response for an ambiguous product request is an interview turn, not a completed Product Discovery, Product Checkpoint, or handoff.

This is an internal field contract, not literal user-facing copy. Render it in the user's language and hide raw machine-state labels unless the user asks for diagnostics or a handoff.

For a Chinese conversation, use this readable shape:

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

For any language, use the user's normal vocabulary for headings and prose. Preserve code, API names, file paths, product names, and exact state identifiers when they need to stay copyable; do not translate those mechanically.

For `deep` mode, use a cumulative decision ledger rather than a questionnaire:

```markdown
Decision Ledger
- Confirmed facts and decisions:
- Delegated assumptions:
- Deferred:
- Rejected:
- Active risks and resolution/owner/evidence:
- Next decision:
```

Each turn should:

1. Briefly recap the confirmed facts and decisions in the user's language.
2. Show the relevant discoverable facts that shaped the current question, with a source path or an explicit statement that no such fact was found.
3. Name the single highest-impact unresolved decision.
4. Explain why that decision matters and what it changes.
5. Ask one question with 2-3 meaningful options and a recommended default.
6. Classify the answer and use it to choose a conditional follow-up. Treat an active risk as a decision that needs resolution or explicit acceptance, not as a note to carry silently.

Do not repeat settled questions or ask small visual, technical, or naming details while user, scenario, first loop, scope, or acceptance remains unresolved. If an answer is ambiguous or conflicts with an earlier decision, ask one narrower follow-up instead of silently choosing.

For the final convergence pass:

- `deferred` means intentionally out of scope for this loop; do not treat it as a hidden requirement.
- `rejected` means explicitly ruled out; do not reintroduce it under a new label.
- `active risk` means a material uncertainty about user trust, scope, main path, or acceptance; resolve it with a decision, owner, and evidence, obtain explicit acceptance, or convert it into a deliberate scope cut before handoff. "Risk handled" without evidence is not a resolution.
- State the intent-fit check plainly: "This first loop solves X for Y in situation Z; it deliberately does not solve A/B."
- In deep mode, ask once whether that summary matches the user's intended problem unless the user delegated the final decision. Do not treat an earlier statement of the goal as the final fit confirmation. If the answer is no, reopen only the highest-impact mismatch.

End with a convergence summary covering confirmed decisions, assumptions, deferred items, rejected ideas, risk treatment, handoff readiness, and intent fit. Do not continue once no material decision remains.

## Product Discovery Template

Use this when starting from a product idea, not from an already-selected feature path.

If the Clarity Gate says `clear`, this template may be produced directly. If a material product choice is still open, ask the interview question first rather than presenting a completed discovery as if it were user-approved.

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

Field guidance:

- `Product truth checked`: request, repo docs, screenshots, support notes, analytics, or "blank project; request only".
- `Starting point`: keep the user's language visible so the idea does not get over-translated too early.
- `Real user and scenario`: include the moment of use, pressure, and why the user cares now.
- `Job/outcome`: phrase as the observable result, not a module name.
- `Opportunity`: the product gap worth testing first.
- `Constraints`: platform, time, compliance, budget, data availability, team ability, distribution, or trust boundaries.
- `Product directions`: two or three materially different paths. Do not list feature bundles that all solve the same problem the same way.
- `Recommended first loop`: the smallest path where a user can start, act, and receive useful feedback.
- `Scope cuts`: what not to build in this cycle.
- `Rabbit holes`: likely complexity traps, such as marketplace dynamics, heavy admin tooling, unclear AI quality, sync, permissions, or monetization before value.
- `First validation signal`: the behavior or evidence that would justify building the next slice.

Ask one question at a time when the answer changes the recommended first loop, scope, main path, states, or acceptance. If the user has not explicitly delegated the decision, wait for the answer even when the user has asked to start implementation. State a delegated assumption and proceed only after explicit delegation.

## Product Choice Challenge Template

```markdown
Product Choice Challenge
- Repo/product truth checked:
- Decision:
- Recommended default:
- Option A:
  - User understanding:
  - Operation cost:
  - Fit:
  - Risk:
- Option B:
  - User understanding:
  - Operation cost:
  - Fit:
  - Risk:
- Option C:
  - User understanding:
  - Operation cost:
  - Fit:
  - Risk:
- Outcome: user chose | user delegated to agent | no question needed
```

Use two options when the third is filler. Lead with the recommended default unless neutrality is required.

Use a Product Choice Challenge inside Product Discovery when one choice blocks convergence. Examples: personal tool vs collaboration product, local-first vs cloud-first, expert workflow vs beginner workflow, content product vs utility, marketplace vs single-player loop, or paid-first vs adoption-first.

## User Lens

Check these before proposing scope:

- Who is the real user and what pressure are they under?
- What do they already understand before arriving here?
- What words would they use for this task?
- What do they need to decide now, and what can wait?
- What would make them feel stuck, unsafe, or unsure?
- What is the smallest result that feels complete from their side?

If these answers are mostly invented, mark them unknown and ask or narrow the product path. Do not turn weak assumptions into confident product strategy.

## Scope Lens

Classify each proposed item:

- `must exist`: required for the current user outcome
- `can wait`: useful but not needed for the first complete path
- `hide behind progressive disclosure`: useful only after context or intent is clear
- `should not exist`: confusing, premature, developer-facing, or not tied to user value

Do not keep a feature because it is easy to implement. Keep it only if it improves the user outcome.

## Greenfield Scope Lens

When the repo is blank or the product is only an idea, scope the first loop by asking:

- Who has the strongest immediate pain or motivation?
- What can they do in one sitting?
- What feedback tells them the product worked?
- What data, content, or setup blocks first value?
- What does the user already do today instead?
- What must be true before this can be monetized or expanded?

Common premature scope:

- accounts, teams, permissions, and admin before there is a solo value loop
- dashboards before the repeated behavior exists
- community, marketplace, or creator economy before supply and demand are proven
- AI agents before quality, evaluation, and trust recovery are defined
- deep customization before the default outcome is valuable
- roadmap or monetization detail before first repeat use is plausible

## IA And Flow Lens

The main path should answer:

- where the user starts
- what the primary action is
- what information is needed before action
- what feedback confirms progress or success
- where advanced or destructive choices live
- how the user recovers from empty, error, permission, or partial states

Red flags:

- screens organized by database object instead of user task
- many equal-weight actions before the user has context
- labels that expose internal states, IDs, flags, or implementation terms
- success that is only visible as data changing somewhere else
- errors that explain the system but not the next user action
- flows that look tidy to the maker but cannot pass a first-time user comprehension check

## Acceptance Criteria

Write acceptance as observable user behavior:

- Good: "A first-time student can open a locked resource and understand that joining the course is required before access."
- Weak: "Render a permission dialog with `courseId` and `status`."
- Good: "After upload failure, the teacher can retry without reselecting the file."
- Weak: "Show error toast on API 500."

Include technical criteria only after the user-visible behavior is clear.

## Handoff Templates

### Product-to-Design Handoff

- Real user:
- Scenario:
- Main path:
- States:
- Scope cuts:
- Acceptance criteria:
- Open product decisions:
- Design constraints:

### To `$noootwo-review`

- Product behavior to preserve:
- Acceptance criteria:
- Risky edge states:
- Technical judgment requested:

### To `$noootwo-docs`

- Stable product decision:
- Owning doc layer:
- User-facing language or migration note:
- Evidence or date:
