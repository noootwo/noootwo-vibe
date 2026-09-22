# Eval Prompt: Screenshot Reference Without Extraction

Use `$noootwo-design` on a design image, screenshot, or Figma frame and ask it to build the screen. Do not provide live URL access.

Expected behavior:

- Run the screenshot/design-image intake before writing UI code: viewport, grid, type relationships, colour roles, component inventory, visible states, imagery, provenance, and confidence.
- Mark inferred values as inferred and name the missing evidence, especially interaction, accessibility, responsive behaviour, and unseen states.
- Translate the image into platform tokens rather than copying web pixel values into Flutter, SwiftUI, or Compose.
- Build only after the extracted design read is visible.

Failure signals:

- Looks at the image and starts coding from visual memory.
- Invents hover, focus, keyboard, empty, loading, error, or data states from a still image without recording them as gaps.
- Copies the image's brand assets, artwork, or exact composition.
- Converts a desktop image into a mobile or native layout without a platform translation step.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals.
