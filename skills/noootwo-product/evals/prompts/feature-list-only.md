# Eval Prompt: Feature List Only

Use `$noootwo-product` on a request that lists screens only: "We need login, dashboard, user management, order list, order detail, settings, notifications, and reports."

Expected behavior:

- Detect that the request is feature-list-shaped.
- Run a Product Checkpoint or Product Choice Challenge before design.
- Ask or assume the decisive real-user scenario.
- Convert the list into IA/main path, interaction model, states, and scope cuts.
- Define acceptance criteria as observable user outcomes.

Failure signals:

- Turns the screen list into a sitemap without user context.
- Leaves labels as backend/admin terms when user language is knowable.
- Sends the list directly to `$noootwo-design` as ready.
