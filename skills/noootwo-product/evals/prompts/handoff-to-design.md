# Eval Prompt: Handoff To Design

Use `$noootwo-product` after a Product Checkpoint when the next step is UI design.

Expected behavior:

- Produce `Product-to-Design Handoff`.
- Include real user, scenario, main path, states, scope cuts, acceptance criteria, open product decisions, and design constraints.
- Mark handoff as not ready if required fields are unknown and would change UI structure.
- Route only clarified visual execution to `$noootwo-design`.

Failure signals:

- Writes a style brief instead of a product handoff.
- Hides unresolved scope or state decisions.
- Omits acceptance criteria or design constraints.
