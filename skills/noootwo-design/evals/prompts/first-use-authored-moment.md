# Eval Prompt: First-Use Or Success Needs An Authored Moment

Use `$noootwo-design` on a first-run, onboarding, empty, or completion moment where users need one clear emotional or explanatory beat. Do not ask the agent for animation or a signature move.

Expected behavior:

- Name the user frequency, task risk, emotional payoff, and the specific experience gap.
- Select `add moment` only because the moment is rare and the action improves explanation, continuity, or emotional payoff.
- Choose one primary authored move and at most one supporting move.
- Name the source or platform evidence, the borrowed mechanism, the boundary, and the reduced-motion or no-motion fallback.
- Verify the result in a running artifact rather than describing the intended animation.

Failure signals:

- Waits for the user to request motion or a distinctive direction.
- Adds several unrelated effects, libraries, or animated elements.
- Uses decoration on a routine or high-frequency part of the flow.
- Claims the moment works without rendered evidence or a fallback.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals. The matching artifact check is `python scripts/eval_noootwo_artifacts.py <project> --scenario add-moment-proof`.
