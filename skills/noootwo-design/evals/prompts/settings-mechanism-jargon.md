# Eval: Settings reject mechanism jargon

Prompt: "Review a settings panel that offers `WebGL 背景：自动 / L2 / 关闭`,
shows `自动档位 · L2 · 设备良好`, and adds a `重新检测` button. The primary
audience is a first-time consumer who opened Settings to reduce visual
distraction."

Expected:

- Fails the Comprehension Gate and names the primary user, the user task, and
  the rendered evidence.
- Replaces mechanism labels with the user's outcome, such as `动态效果`,
  `丰富背景`, and `关闭`.
- Removes tier, renderer, frame-rate, and re-detection controls unless a
  recurring user decision requires them; the default handles the rest.
- Keeps at most one setting for visual intensity and records the comprehension
  result in the review record.
- Returns `fix` and does not mark the panel shipped.

Fails when: it only renames the labels while keeping the WebGL/L2 model; treats
`WebGL`, `L2`, `Canvas`, or `重新检测` as transparency; or ships the panel
because the layout is clean.
