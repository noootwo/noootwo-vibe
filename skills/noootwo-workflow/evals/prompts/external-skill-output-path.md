# Eval: An external skill cannot choose the project's document layout

Prompt: "Use the brainstorming skill to settle this feature, then use its writing-plans skill to plan the work. Save the spec and plan."

Expected:

- Uses the external skills only as execution resources for their method.
- Routes durable artifacts through `noootwo-state`.
- Stores the accepted specification in `docs/specs/` and the implementation sequence in `docs/plans/`.
- Treats any `docs/superpowers/` default path from the external skill as a read-only legacy convention, not the new destination.

Fails when: it creates new project truth under `docs/superpowers/`, lets the external skill override the project's document ownership, or writes the spec and plan directly without the state owner.
