# Eval Prompt: Linear And Opacity-Only Motion

Use `$noootwo-design` on an artifact whose panels slide with `transition-timing-function: linear` and whose state changes fade opacity alone.

Expected behavior:

- Flag both as hard bans from `references/craft.md`, naming the element and the property.
- Replace the linear curve with a real easing family and pair the opacity change with position, scale, or colour.
- Confirm the finding against a screenshot, preview, or DOM inspection before it blocks `ready`.
- Record the corrected durations and curves in the motion section of the design tokens.

Failure signals:

- Reports the motion as "smooth" because it runs without jank.
- Blocks the artifact from an automated finding with no visual confirmation.
- Fixes the easing but leaves the meaningful state change carried by opacity alone.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals. The matching artifact check is `python scripts/check_visual_gates.py <target>`.
