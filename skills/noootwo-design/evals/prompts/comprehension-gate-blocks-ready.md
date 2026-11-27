# Eval: Strong visuals do not pass a failed copy and audience check

Prompt: "The landing page looks strong, but a first-time visitor cannot tell what the product does. The hero says 'Orchestrate multi-agent retrieval pipelines' and the only action is 'View docs'."

Expected:

- Records the first screen, the primary user, and the failed user task.
- Names the failed layer: audience/value is unclear, or the artifact copy and action are wrong.
- Returns to `noootwo-product` when the primary user or value is unsettled; otherwise returns to the artifact.
- Replaces the implementation-led hero with the user outcome and one primary action, while keeping any needed technical proof in a second layer.
- Refuses `ship` even when layout, typography, or visual direction are strong.

Fails when: it approves the page because the visuals are strong; says "clarify the copy" without a return action; or marks it shipped.
