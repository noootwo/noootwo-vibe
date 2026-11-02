# Eval: Phase shift re-routes the owner

Prompt: "The design direction is approved and the mockups are done. Build the checkout page against it, then deploy it to production." The session read the product, design, and research skills earlier, and no product or visual decision is open.

Expected:

- Treats the design stage as settled and does not reload or re-run product, design, or research for the implementation step.
- Routes the implementation through the `noootwo-code-health` Integration Read when the seam is non-obvious, or directly to `noootwo-tdd` when it is obvious, before editing.
- After green, runs the `noootwo-code-health` Change Check and waits for its result before the release boundary.
- Routes deployment through `noootwo-release` after code-health readiness; workflow names the boundary but does not pick the version or deploy itself.
- Invokes each specialist by reading its `SKILL.md`, one owner at a time.

Fails when: the design skill stays the owner; the product, design, or research bodies are reloaded because they were read earlier; implementation or deployment runs with no engineering owner; or workflow owns the release plan itself.
