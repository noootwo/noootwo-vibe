# Product Decision Layers

Use this when a product request is vague, feature-list-shaped, backend-shaped, or ready to hand off to design.

## Layer Order

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

## Backend-Shaped Flow Correction

Backend-shaped requests expose internal objects before user intent. Correct them before design:

- Replace object names with user tasks.
- Replace status flags with what the user sees and can do next.
- Group fields by decision moment, not database table.
- Hide advanced or destructive choices until context exists.
- Make success visible as user progress, not only saved data.
- Turn errors into recovery paths, not system explanations.

## Product-to-Design Readiness

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

## Handoff Quality Checks

A useful handoff lets `$noootwo-design` choose visual structure without inventing product scope:

- Good: "First-time teacher uploads a worksheet, sees extraction progress, fixes low-confidence fields, and publishes only after review."
- Weak: "Build upload page, history list, detail page, dashboard, settings."
- Good: "Payment failure state lets the parent retry, switch method, or keep the reserved seat for 10 minutes."
- Weak: "Show error toast on pay API failure."

## What Not To Hand Off

Do not hand off as design-ready when:

- the real user is still "admin", "user", or "customer" without context
- the request is only a module list or navigation sitemap
- the main path mirrors tables, CRUD endpoints, or status enums
- empty, permission, onboarding, payment, AI trust, or error recovery changes the core screen structure
- acceptance is written as component names, DOM shape, or API fields
