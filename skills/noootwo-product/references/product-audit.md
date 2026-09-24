# Product Audit

Use this when the user asks to audit, critique, or fix an existing product flow: onboarding, checkout, settings, first run, or a specific task path. It extends the product interview into existing UX without turning a product decision into a code or visual review.

## Minimum brief

Before asking frontier questions, write the smallest brief that can be checked against the actual flow:

- real user and moment of use
- the task the flow should complete
- the first loop and its observable outcome
- the states that matter: empty, loading, error, permission, success
- the open decision that actually blocks the next step

If a fact is already in the repo, read it before asking. Ask only for decisions, not discoverable facts.

## Project-local product context

When the same product context will be reused by design or research, invoke the `noootwo-state` skill to persist it; submit the following content as an abstract record instead of writing `.noootwo/product-context.md` directly:

- product URL or app entry point
- target platform and main task
- current screenshots or captured flow steps
- existing tokens, design system, component sources, or brand material when present
- access limits observed during this pass

This is project-local, not a global user profile. Do not copy unrelated past projects into it.

## Existing-flow audit

1. Name the flow and the goal being judged.
2. Capture the steps in order; wait for each screen to settle before accepting a screenshot.
3. Reject blank, loading, blocked, cropped, or wrong-state captures.
4. Keep every finding tied to a step.
5. Separate these findings:
   - product-flow friction: the task is unclear, too long, or blocked
   - state/acceptance gaps: empty, error, permission, success states do not name the next action
   - visual or interaction defects: route to `noootwo-design`
   - code or performance defects: route to `noootwo-code-health`
6. Rank by severity and product leverage, not by how easy the screenshot was to obtain.

## Output

Use the following shape:

```markdown
Product Flow Audit
- Flow:
- Goal:
- Captured steps:
- Findings:
  - [severity] step N: what differs, evidence, impact, fix owner
- Product decision needed:
- Handoff:
```

When the flow cannot be accessed or captured, say so and record the limitation; do not call an indirect web search an audit.
