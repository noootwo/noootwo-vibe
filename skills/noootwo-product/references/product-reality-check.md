# Product Reality Check

Use this when product output risks sounding like a PM while still missing the user's lived situation. It is a short diagnostic, not a full PRD and not a default step for every product question.

## When To Trigger

Run this for:

- greenfield ideas before the first loop is trusted
- user feedback like "this is hard to understand", "not from the user's angle", or "still dumb AI"
- broad feature lists that look complete but lack a moment of use
- repeated correction loops where small edits are no longer improving the product
- Product-to-Design Handoff when comprehension risk would change the first screen

Skip it for narrow scope clarification, small copy changes, and already-validated product paths.

## Check Shape

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

## Field Rules

- `Real user`: name the role plus pressure. "User", "admin", or "customer" is not enough.
- `Moment of use`: the exact situation where the product becomes useful or confusing.
- `Current alternative`: what the user does today without this product. If unknown, say unknown rather than inventing it.
- `First loop`: start, action, feedback, and proof that the result mattered.
- `User comprehension check`: whether the user can tell what to do next, why it matters, what changed, and how to recover.
- `Naive-AI failure`: the likely wrong product a generic model would build, such as a module list, dashboard-first flow, CRUD sitemap, premature AI agent, or status-enum UI.
- `Decision`: `keep` if the product path is understandable, `revise` if the path is wrong, `ask` if one product choice blocks progress, or `stop` if the premise is not supported.
- `Return action`: one of `return to discovery`, `return to checkpoint`, `return to choice challenge`, `return to handoff`, or `return to workflow`.

## Reality Tests

Ask these before handing off:

- Would the real user understand the first screen without internal terms?
- Does the first loop produce feedback the user can see and value?
- Are empty, error, permission, loading, and success states understandable from the user's side?
- Did we cut features because they are not needed now, or only because they are hard to build?
- Are we preserving a user outcome, or merely arranging modules?

## Anti-Hallucination Rules

- Do not invent personas, market behavior, analytics, constraints, or willingness to pay.
- Mark missing evidence as `unknown` and route to a Product Choice Challenge when it changes the product.
- Treat user criticism as a signal to locate the failed layer, not proof that every requested feature should be added.
- Do not hide a weak product behind visual direction. If product comprehension fails, return before design.
