# Eval Prompt: Implementation Planning Gate

Use `$noootwo-design` after the user has selected a direction from `.noootwo/directions.md`. Prepare to implement it in a React/Vue/Flutter project.

Expected behavior:

- Create or update `.noootwo/specs/active-design.md` as the approved design contract.
- Ask for approval if the selected direction has unresolved scope, cost, target-stack, or artifact-path decisions.
- Create `.noootwo/plans/active-implementation.md` before editing UI files.
- Include file/module scope, token mapping tasks, component tasks, verification plan, and screenshot/preview method.
- Only implement after the plan is approved or the user delegates execution.

Failure signals:

- Starts editing UI files immediately after direction selection without a spec or plan.
- Hides open design decisions in prose.
- Does not define how the result will be visually verified.
