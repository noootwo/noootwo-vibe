# Eval Prompt: Generic Shadcn Default UI

Use `$noootwo-design` on a React/Vue UI draft that is technically tidy but looks like an unmodified shadcn-style card wall.

Expected behavior:

- Identify generic framework/default component smell in Artifact Review.
- Return to Design Contract, implementation plan, or artifact with a specific anti-slop action.
- Define semantic token roles, component behavior, state treatment, and forbidden substitutions.
- Preserve useful structure while removing default visual sameness.
- Choose `craft only` when structure, typography, density, and state behavior solve the problem; do not add a motion or material signature merely to prove distinctiveness.

Failure signals:

- Calls the result ready because it is clean and modern.
- Only changes palette, radius, or shadows.
- Replaces one generic template with another.
