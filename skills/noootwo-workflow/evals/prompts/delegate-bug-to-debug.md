# Eval: Delegate a bug to debug

Prompt: "Checkout throws when the cart is empty. Fix it and update anything that needs updating."

Expected:

- The agent schedules the task rather than performing the diagnosis itself: it invokes the `noootwo-debug` skill by loading its `SKILL.md`.
- It does not edit code before the cause gate closes, and it states that the loop is stopped while the cause is unproven.
- It keeps the parts workflow owns: ordering, the declared fix scope, handoffs, and the docs decision.
- When the cause is proven and the fix lands, it invokes the `noootwo-state` skill for the behaviour change and the `noootwo-code-health` skill before submit.

Fails when: workflow performs its own diagnosis and writes the fix; it proposes a fix before the cause gate closes; it closes the task with no docs or review decision.
