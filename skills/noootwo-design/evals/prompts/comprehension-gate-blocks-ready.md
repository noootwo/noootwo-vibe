# Eval: Strong visuals do not pass a failed comprehension gate

Prompt: "The landing page looks strong, but a first-time visitor cannot tell what the product does. The hero says 'Orchestrate multi-agent retrieval pipelines' and the only action is 'View docs'."

Expected:

- Records `Comprehension gate: fail` with the first screen and user task tested.
- Names the failed layer: audience/value is unclear, or the artifact copy and action are wrong.
- Returns to `noootwo-product` when the primary user or value is unsettled; otherwise returns to the artifact.
- Replaces the implementation-led hero with the user outcome and one primary action, while keeping any needed technical proof in a second layer.
- Refuses `ready` even when layout, typography, or visual direction are strong.

Fails when: it scores the page high because the visuals are strong; says "clarify the copy" without a return action; or marks it ready.
