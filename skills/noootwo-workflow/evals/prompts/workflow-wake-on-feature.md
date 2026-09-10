# Eval Prompt: Workflow Wakes On Feature Work

Give the agent a new feature request: "Add export-to-PDF to the settings page and update the docs."

Expected behavior:

- Invoke `$noootwo-workflow` before editing files.
- Run lifecycle guardrails at the lightest useful level and classify the work (feature, medium/large).
- Read nearest repo truth (AGENTS.md, README, docs/status.md, related files) before planning.
- When product ambiguity appears (who exports, why, what the export must contain), explicitly invoke `$noootwo-product` instead of asking repeated product questions itself.
- When docs are affected, explicitly invoke `$noootwo-docs` before closing.

Failure signals:

- Starts editing files without invoking `$noootwo-workflow`.
- Treats the task as direct work despite cross-file behavior and docs impact.
- Asks product questions inside Workflow instead of routing to Product.
- Closes the work without a docs decision.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals.
