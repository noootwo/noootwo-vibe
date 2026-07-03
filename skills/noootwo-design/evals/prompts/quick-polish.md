# Eval Prompt: Quick Polish

Use `$noootwo-design` to only tighten spacing, typography, and hierarchy on one existing settings page. Keep the current visual system.

Expected behavior:

- Route to `quick`.
- Do not run full source mining, deep discovery, 3 directions, or spike comparison.
- Read existing `.noootwo/system.md` and tokens if available.
- Make small changes that preserve the current visual system.
- Ask before changing color system, navigation, component language, or interaction model.

Failure signals:

- Starts a full redesign or asks the user to choose among 3 art directions.
- Replaces the product style with a new aesthetic.
- Adds expensive motion, new font systems, or unrelated visual effects.
