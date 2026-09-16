# Eval Prompt: Motion Without A Reduced-Motion Path

Use `$noootwo-design` on an artifact that animates entrances, parallax, and ambient layers with no reduced-motion handling in CSS or in the native target.

Expected behavior:

- Treat the missing fallback as a hard ban, not a nicety.
- Name the fallback per platform: `prefers-reduced-motion`, Reduce Motion, Remove animations, or `MediaQuery.disableAnimations`.
- Preserve state information in the fallback so nothing is conveyed by the missing motion alone.
- Record the fallback in the motion section of `.noootwo/design-tokens.md`.

Failure signals:

- Notes the gap and still calls the artifact ready.
- Adds a reduced-motion query that removes all feedback, including state changes.
- Claims reduced motion is out of scope for a native target.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals. The matching artifact check is `python scripts/check_visual_gates.py <target>`.
