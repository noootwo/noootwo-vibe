# Eval Prompt: Feature List Only

Use `$noootwo-product` on a request that lists screens only: "We need login, dashboard, user management, order list, order detail, settings, notifications, and reports."

Expected behavior:

- Detect that the request is feature-list-shaped.
- Run Decision Interview before Product Checkpoint or design because the list does not establish a real-user scenario.
- Ask for the decisive real-user scenario one question at a time and wait unless the user explicitly delegates it.
- Convert the list into IA/main path, interaction model, states, and scope cuts.
- Define acceptance criteria as observable user outcomes.

Failure signals:

- Turns the screen list into a sitemap without user context.
- Leaves labels as backend/admin terms when user language is knowable.
- Sends the list directly to `$noootwo-design` as ready.
- Treats the feature list or a recommended scenario as user approval.
