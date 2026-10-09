# Eval Prompt: Motion Contract Missing

Use `$noootwo-design` on deep UI work whose intervention decision is `add moment`, but whose `.noootwo/design-tokens.md` carries no motion values and whose artifact is static after the build.

Expected behavior:

- Read `references/motion.md` and fill personality, signature easing, a millisecond duration scale, the three layers, choreography, and the reduced-motion fallback.
- Keep the recorded intervention decision and evidence; do not use this eval to force motion on a justified `leave simple` or `craft only` result.
- Derive the archetype from the direction's style lineage, or record why it is overridden.
- Treat the missing motion language as an incomplete direction, not as a later polish task.
- Keep entering the review path with motion named among the artifact's defects.

Failure signals:

- Marks the artifact `ready` because the layout and typography are sound.
- Invents durations without naming the archetype or the lineage they came from.
- Treats motion as a finishing pass to add after the layout is settled.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals. The matching artifact check is `python scripts/validate_noootwo_readiness.py <project> --deep-mode`.
