# Eval Prompt: Use The Installed Motion Runtime Where It Is The Right Tool

Use `$noootwo-design` on a React or Vue project that already depends on `motion`, where the selected authored move needs layout, presence, reflow, spring, or gesture-aware behavior.

Expected behavior:

- Read the project dependencies before choosing an implementation.
- Select the installed Motion runtime for the capability it uniquely provides instead of hand-writing a weaker CSS-only imitation.
- Record the tool decision as `selected: motion` or provide a concrete `equivalent alternative` or `rejected with reason`.
- Keep the authored move limited to one primary interaction and one optional support.
- Verify the behavior in the running artifact and keep reduced-motion behavior intact.

Failure signals:

- Ignores an installed runtime and reports "no new dependency" as the design goal.
- Uses only generic `transition` or component-library defaults when the requested move needs layout or presence behavior.
- Adds a second runtime without a reason.
- Never records whether the installed library was selected, replaced, or rejected.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals.
