# Impeccable Style Details To Borrow

Use this as craft guidance distilled from current impeccable design skills. Borrow the mechanisms, not the dependency or wording.

## Typography

- Do not default to Inter, Roboto, Arial, Open Sans, or system fonts when the brief asks for personality.
- Pair with real contrast: serif/sans, wide/condensed, humanist/geometric, editorial/body, or restrained mono accent.
- Use a small, explicit type scale. App UI needs predictable `rem` roles; campaign UI can use fluid display sizes.
- Body text should normally be at least 16px on web.
- Use `tabular-nums` for aligned values and operational data.

## Color

- Avoid pure `#000` and `#fff` as the main palette unless a specific brand system requires them.
- Tint neutrals toward the chosen brand mood.
- Prefer OKLCH or `color-mix()` where web stack support allows.
- Do not use the AI palette: cyan/purple/blue gradients, neon-on-dark, glow accents, or gradient text as the main idea.
- Dominant color plus sharp accent is usually stronger than evenly spread decorative color.

## Composition And Space

- Create rhythm with tight related groups and generous separation between groups.
- Do not apply the same padding everywhere.
- Use asymmetry, rails, rules, and structured density when they clarify hierarchy.
- Avoid identical card grids, nested cards, centered hero templates, and card walls as a default structure.
- A sophisticated layout can be dense if the data, labels, and actions are organized.

## Motion

- Motion should explain state, continuity, emphasis, or identity.
- One well-orchestrated transition is better than many generic fade-ups.
- Avoid bounce/elastic easing unless the product explicitly wants playful physicality.
- Do not put motion on top of a generic layout and call it premium.

## Review

Ask whether the interface would be instantly recognized as AI-generated. If yes, return to directions or artifact instead of polishing.
