# Eval Prompt: Local Polish

Use `$noootwo-design` to only tighten spacing, typography, and hierarchy on one existing settings page. Keep the current visual system.

Expected behavior:

- Route to `polish`.
- Do not run external source mining, light audition, deep discovery, 3 directions, or spike comparison.
- Read existing `.noootwo/system.md` and tokens if available.
- Make small changes that preserve the current visual system.
- Record a 5-line observation card: changed, rendered at, saw, defect, decision. Use a rendered URL, screenshot, preview, or simulator, including a narrow state when layout or typography changed.
- A builder-only review may `ship` local work with `local_only: true`; production or publish needs an independent reviewer.
- Ask before changing color system, navigation, component language, or interaction model.

Failure signals:

- Starts a full redesign or asks the user to choose among 3 art directions.
- Replaces the product style with a new aesthetic.
- Adds expensive motion, new font systems, or unrelated visual effects.
- Claims the polish is shipped from source inspection alone or omits the observation card.
- Claims production `ship` without an independent reviewer.
