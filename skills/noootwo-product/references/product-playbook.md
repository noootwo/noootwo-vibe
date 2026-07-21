# Product Playbook

Use this when the compact `Product Checkpoint` is not enough.

For layer diagnosis and Product-to-Design readiness, use `product-decision-layers.md` first. This playbook gives deeper discovery, option framing, state, acceptance, and anti-pattern checks.

## Practice Basis

- User-centered product work starts from user needs, context, and mental models before implementation shape.
- Good AI-assisted product work makes assumptions explicit, proposes alternatives, asks only the choice that changes the result, and converges before implementation.
- Low-friction products reduce exposed concepts, use familiar language, and make the next action obvious.
- Product work should cut scope as deliberately as it adds scope.
- Product discovery should move from outcome to opportunity, then to solution options and validation signals.
- Good shaping names the appetite, no-gos, and likely rabbit holes before a team commits to build.
- Fast product exploration can borrow sprint mechanics: map the path, sketch alternatives, decide, prototype only when useful, and test the riskiest assumption.

## Product Discovery Template

Use this when starting from a product idea, not from an already-selected feature path.

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

Ask one question at a time only when the answer changes the recommended first loop. If the user delegates the decision, state the assumption and proceed.

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
