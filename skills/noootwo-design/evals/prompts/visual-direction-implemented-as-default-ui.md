# Eval Prompt: Visual Direction Implemented As Default UI

Use `$noootwo-design` after a user selected a distinctive direction, but the implemented artifact looks like UI-kit defaults with a palette or radius change.

Expected behavior:

- Review style understanding fit against the selected direction and visual evidence.
- Name the missing borrowed mechanisms and default fallback that survived implementation.
- Return to style discovery, design contract, implementation plan, or artifact with one action.
- Avoid restarting from a new unrelated style unless the selected direction is proven wrong.

Failure signals:

- Calls the artifact ready because it is clean.
- Only asks for more polish, shadows, or color changes.
- Ignores that the style evidence and rendered result do not match.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals. The matching artifact check is `python scripts/eval_noootwo_artifacts.py <project> --scenario visual-direction-implemented-as-default-ui`.
