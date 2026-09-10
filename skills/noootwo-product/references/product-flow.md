# Product Flow

Decision layers, grilling detail, and the report templates Product produces.


## Product Decision Layers

Use this when a product request is vague, feature-list-shaped, backend-shaped, or ready to hand off to design.

### Layer Order

Good product decisions move from user reality to surface behavior:

| Layer | Question | Output |
| --- | --- | --- |
| User | Who has the real need? | real user and situation |
| Context | When and why does this matter? | scenario and pressure |
| Outcome | What result is the user trying to get? | job/outcome |
| Opportunity | What gap is worth testing first? | problem/opportunity |
| Scope | What exists now, waits, or should not exist? | should exist and scope cuts |
| IA/main path | Where does the user start and finish? | entry, steps, feedback |
| Interaction model | How does the user act and recover? | action model and recovery model |
| State model | What must be understood in every state? | loading, empty, error, success, permission, offline |
| Acceptance | What user behavior proves it works? | observable acceptance criteria |
| Validation | What should be learned before more scope? | first validation signal |

If an upper layer is unclear, do not solve it by adding UI surface or implementation detail.

### Backend-Shaped Flow Correction

Backend-shaped requests expose internal objects before user intent. Correct them before design:

- Replace object names with user tasks.
- Replace status flags with what the user sees and can do next.
- Group fields by decision moment, not database table.
- Hide advanced or destructive choices until context exists.
- Make success visible as user progress, not only saved data.
- Turn errors into recovery paths, not system explanations.

### Product-to-Design Readiness

Design handoff is ready only when these are concrete enough:

- `real user`: role, context, and pressure are named.
- `scenario`: the moment of use is specific.
- `main path`: entry, steps, and success feedback are known.
- `states`: relevant loading, empty, error, success, permission, and boundary states are listed.
- `scope cuts`: deferred or forbidden work is explicit.
- `acceptance criteria`: at least the primary user-visible outcome is testable.
- `open product decisions`: unresolved choices are listed instead of hidden.
- `design constraints`: brand, platform, content, trust, accessibility, localization, or data constraints are named.

If any required field is unknown and would change the UI structure, return to Product Checkpoint or Product Choice Challenge.

### Handoff Quality Checks

A useful handoff lets `$noootwo-design` choose visual structure without inventing product scope:

- Good: "First-time teacher uploads a worksheet, sees extraction progress, fixes low-confidence fields, and publishes only after review."
- Weak: "Build upload page, history list, detail page, dashboard, settings."
- Good: "Payment failure state lets the parent retry, switch method, or keep the reserved seat for 10 minutes."
- Weak: "Show error toast on pay API failure."

### What Not To Hand Off

Do not hand off as design-ready when:

- the real user is still "admin", "user", or "customer" without context
- the request is only a module list or navigation sitemap
- the main path mirrors tables, CRUD endpoints, or status enums
- empty, permission, onboarding, payment, AI trust, or error recovery changes the core screen structure
- acceptance is written as component names, DOM shape, or API fields


## Product Playbook

Use this when the compact `Product Checkpoint` is not enough.

For layer diagnosis and Product-to-Design readiness, use `product-decision-layers.md` first. This playbook gives deeper discovery, option framing, state, acceptance, and anti-pattern checks.

Use `product-reality-check.md` when output may be PM-shaped but user-confusing, naive-AI, assumption-heavy, or repeatedly corrected.

### Practice Basis

- User-centered product work starts from user needs, context, and mental models before implementation shape.
- Good AI-assisted product work makes assumptions explicit, proposes alternatives, asks only the choice that changes the result, and converges before implementation.
- Low-friction products reduce exposed concepts, use familiar language, and make the next action obvious.
- Product work should cut scope as deliberately as it adds scope.
- Product discovery should move from outcome to opportunity, then to solution options and validation signals.
- Good shaping names the appetite, no-gos, and likely rabbit holes before a team commits to build.
- Fast product exploration can borrow sprint mechanics: map the path, sketch alternatives, decide, prototype only when useful, and test the riskiest assumption.

### Grilling Detail

The flow in `SKILL.md` is the source of truth for the steps. This section adds the detail the steps do not carry.

**Depth.** One unsettled decision makes a single-question round. Several dependent decisions make a multi-question round. There is no separate mode to select; the frontier decides.

**Facts and decisions.** Finding facts is the agent's job. A question that the repo, the docs, a screenshot, analytics, or the current UI can answer is not a question for the user. Show the facts that shaped a question, with their source, so the user does not restate them.

**The ledger.** Track each decision as it settles, so a round never restarts from the beginning:

```markdown
Decision Ledger
- Settled:
- Assumed (delegated):
- Deferred:
- Rejected:
- Carried risks, with owner and evidence:
- Next frontier:
```

**Presentation.** Write in the user's language and vocabulary. Keep code, API names, file paths, product names, and exact state identifiers unchanged. Do not print internal state names such as `settled`, `frontier`, or `shared understanding` as raw labels unless the user asks how the process works. A Chinese conversation reads like this:

```markdown
需求确认（本轮）
- 已确认：
- 已查到的事实：
- 本轮需要确认：
- 为什么重要：
- 可选方案：
- 我的建议（尚未选择）：
- 当前状态：等待你的确认
```

**Waiting.** While a decision is unsettled the agent may read files, and does nothing else: no edits, no design, no implementation plan, no handoff. A recommendation is an option, not approval. Only an explicit choice or explicit delegation settles a decision.

**Carried risks.** A risk is settled only with a decision, an owner, and evidence — or explicit user acceptance, or conversion into a deliberate scope cut. "Handled" without evidence is not a resolution.

### Product Discovery Template

Use this when starting from a product idea, not from an already-selected feature path.

When nothing is unsettled, this template may be produced directly. If a material product choice is still open, ask the interview question first rather than presenting a completed discovery as if it were user-approved.

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

Ask the settled frontier when any answer changes the recommended first loop, scope, main path, states, or acceptance: one question for a single material gap, the whole frontier in one round for several dependent gaps. If the user has not explicitly delegated the decision, wait for the answer even when the user has asked to start implementation. State a delegated assumption and proceed only after explicit delegation.

### Frontier Question Template

```markdown
Frontier Question
- Facts checked:
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

### User Lens

Check these before proposing scope:

- Who is the real user and what pressure are they under?
- What do they already understand before arriving here?
- What words would they use for this task?
- What do they need to decide now, and what can wait?
- What would make them feel stuck, unsafe, or unsure?
- What is the smallest result that feels complete from their side?

If these answers are mostly invented, mark them unknown and ask or narrow the product path. Do not turn weak assumptions into confident product strategy.

### Scope Lens

Classify each proposed item:

- `must exist`: required for the current user outcome
- `can wait`: useful but not needed for the first complete path
- `hide behind progressive disclosure`: useful only after context or intent is clear
- `should not exist`: confusing, premature, developer-facing, or not tied to user value

Do not keep a feature because it is easy to implement. Keep it only if it improves the user outcome.

### Greenfield Scope Lens

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

### IA And Flow Lens

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

### Acceptance Criteria

Write acceptance as observable user behavior:

- Good: "A first-time student can open a locked resource and understand that joining the course is required before access."
- Weak: "Render a permission dialog with `courseId` and `status`."
- Good: "After upload failure, the teacher can retry without reselecting the file."
- Weak: "Show error toast on API 500."

Include technical criteria only after the user-visible behavior is clear.

### Handoff Templates

#### Product-to-Design Handoff

- Real user:
- Scenario:
- Main path:
- States:
- Scope cuts:
- Acceptance criteria:
- Open product decisions:
- Design constraints:

#### To the review skill

- Product behavior to preserve:
- Acceptance criteria:
- Risky edge states:
- Technical judgment requested:

#### To the docs skill

- Stable product decision:
- Owning doc layer:
- User-facing language or migration note:
- Evidence or date:
