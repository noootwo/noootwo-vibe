# Eval Prompt: Workflow Invokes Specialists

Give the agent a multi-skill task: a UI change with an unclear product path, followed by a code change that must be submitted.

Expected behavior:

- Invoke `$noootwo-workflow` first.
- When the product path is unclear, explicitly invoke `$noootwo-product` (not just "consider" it).
- After product convergence, explicitly invoke `$noootwo-design` for the UI work with a Product-to-Design Handoff.
- Before submit, explicitly invoke `$noootwo-review` for the code change.
- If any specialist skill is unavailable, say so in one line and follow the closest fallback.

Failure signals:

- Claims to have "considered" a skill without invoking it.
- Routes UI work to Design without product convergence.
- Submits code without a review decision.
- Silently substitutes Workflow's own judgment for a specialist skill.

Manual evaluation: pass only when the response shows explicit invocations at each trigger point.
