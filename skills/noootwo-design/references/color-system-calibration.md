# Color System Calibration

Use this when a UI feels cheap, assembled, template-like, or visually detached because the color system does not carry a coherent product temperature across surfaces, text, shadows, semantic states, gradients, icons, or illustration.

This is a calibration lens, not a universal aesthetic law. Do not replace artifact review, typography, density, layout, component behavior, motion, or accessibility checks with color tweaks.

## Research Basis

- The user-provided PDF `/Users/notwo/Downloads/你的UI廉价，错在颜色.pdf` argues that polished UI often comes from color temperature flowing through neutral surfaces, shadows, text hierarchy, semantic colors, gradients, icons, and illustrations instead of only appearing as a brand accent.
- Material Color Utilities describes HCT, tonal palettes, dynamic colors, and contrast-aware color utilities for theme generation and state changes.
  - Source: https://github.com/material-foundation/material-color-utilities
  - Evidence level: official implementation
- WCAG contrast guidance requires readable text contrast and warns against using color alone to communicate information.
  - Sources: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html and https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html
  - Evidence level: standard
- MDN guidance for `color-mix()` recommends perceptually uniform spaces such as Oklab for even gradients and Oklch when preserving chroma through color mixing matters.
  - Source: https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/color-mix
  - Evidence level: platform documentation
- Carbon, Atlassian, and Figma design-system guidance support role-based and semantic tokens instead of hard-coded visual values.
  - Sources: https://carbondesignsystem.com/elements/color/tokens/, https://atlassian.design/foundations/tokens/design-tokens/, https://www.figma.com/blog/the-future-of-design-systems-is-semantic/
  - Evidence level: official design-system guidance
- Tailwind v4 uses modern CSS features such as `color-mix()` and exposes OKLCH-based palette values, which supports using perceptual color spaces for practical UI theming.
  - Source: https://tailwindcss.com/blog/tailwindcss-v4
  - Evidence level: framework documentation

Borrow the repeatable mechanism: role-based color temperature and artifact checks. Do not borrow absolute claims such as "never use pure neutrals" or "premium UI has no exceptions."

## When To Use

Use this reference for:

- cheap, generic, or assembled visual feel where layout is mostly acceptable
- brand color that looks pasted onto otherwise dead gray UI
- light or dark themes with flat neutral ramps
- mismatched semantic states, especially default error red on a strongly warm or cool system
- black-shadow sticker effects, glow-as-polish, or generic UI-kit elevation
- gradients with endpoints that drift outside the token family
- icon or illustration colors that look imported from another product
- implementation-bound token mapping, design-system extraction, or artifact review

Do not require this for every quick polish task. Escalate only when color drift is part of the observed problem or the selected direction depends on color-system coherence.

## Calibration Contract

Before proposing color changes, inspect the current evidence:

- Existing tokens, theme files, Tailwind config, CSS variables, `ThemeData`, SwiftUI token structs, Compose theme, or platform style resources.
- Screenshots, previews, or artifacts for at least one representative surface.
- Product context: utility, data-dense tool, editor, marketing surface, consumer app, native flow, or brand-heavy page.
- Accessibility constraints, platform high-contrast modes, and existing brand guidelines.

Record color decisions as roles:

- `neutral temperature`: warm, cool, chromatic, deliberately neutral, or unknown.
- `canvas`: base app/page field and the reason it fits the product.
- `surface`: panels, rails, sheets, cards, overlays, raised areas.
- `border`: hairlines, dividers, input edges, focus boundaries.
- `text`: primary, secondary, muted, disabled, inverse, data-heavy text.
- `accent`: dominant action or identity color with usage limits.
- `semantic`: success, warning, danger, info, selected, focus.
- `shadow hue`: depth or glow color family, alpha, and when shadow should be absent.
- `gradient boundary`: allowed stops and forbidden endpoints.
- `icon/illustration color source`: whether icons inherit text tokens and whether illustration shadows/highlights share the UI token family.
- `contrast proof`: the text/background and state pairs that must pass contrast checks.
- `color exceptions`: where pure white, pure black, or platform/system colors are intentionally allowed.

## Mechanisms

### 1. Brand-Aware Neutral Temperature

If the brand or selected direction has a clear hue temperature, let the neutral ramp lean subtly toward it. The shift should be quiet enough that the user reads it as surface quality, not as a colored background.

Useful targets:

- light canvas and surface: slight hue bias, stable luminance hierarchy
- border and divider: same family as the surface, not a random default gray
- muted text: same temperature family as body text, with enough luminance contrast
- dark theme: colored dark neutrals, not simply `#000` plus gray panels

Use OKLCH or HCT when practical because hue, chroma, and lightness/tone are easier to reason about than RGB. Do not force a new color toolchain if the project already has a working token pipeline.

### 2. Shadows And Depth

Shadows should express depth, separation, or state. They are not a generic premium filter.

Review these details:

- black shadows on light tinted surfaces can look like pasted overlays
- low-alpha brand/environment-tinted shadows often integrate better with warm or cool systems
- `0 0 0 1px` shadow-border can avoid layout shift, but it must still pass visible boundary needs
- in dark mode, depth may need glow, border, or tonal contrast instead of heavier black shadow
- some operational or flat systems should use borders and planes instead of shadows

### 3. Text Hierarchy

Text tokens may lean warm or cool, but readability wins.

Rules:

- primary text must remain clearly readable against its surface
- muted text cannot become low-contrast decorative gray
- data-heavy text should prioritize scanning, alignment, and contrast over brand temperature
- disabled text and placeholder text should not become indistinguishable from normal muted text
- CJK body text needs stronger practical contrast than many decorative mockups imply

### 4. Semantic Harmonization

Semantic colors must keep their category meaning. Harmonization means nudging color temperature and subtle backgrounds into the system, not making danger, warning, or success ambiguous.

Check:

- danger remains recognizably danger
- warning remains recognizably warning
- success remains recognizably success
- subtle state backgrounds belong to the canvas/surface family
- focus rings and error states do not rely on hue alone
- every semantic state has a non-color cue when needed: text, icon, border, message, or layout change

### 5. Gradients

Gradients should stay inside the token family unless the selected direction intentionally breaks the field.

Review:

- both endpoints should belong to the same calibrated system
- avoid drifting from a branded stop into pure white or dead gray by accident
- use perceptual interpolation when gradients visibly band, gray out, or lose chroma
- mesh gradients need a base token plus related color points, not a brand blob over generic white
- gradient direction should support light, material, or composition logic

### 6. Icons And Illustration

Icons usually inherit text tokens. Do not invent a parallel gray stack for icon strokes unless the product system explicitly requires it.

For illustrations:

- shadows, highlights, paper, skin, fabric, objects, or environment colors should share the UI temperature family
- avoid pure black and pure white as default illustration extremes unless the style deliberately calls for them
- illustration color must not weaken product UI contrast or state recognition
- generated or stock imagery should be reviewed against the surrounding token system before handoff

## Safety Exceptions

Pure white, pure black, or platform grays are acceptable when they are intentional and evidenced:

- high-contrast or accessibility mode
- document, editor, terminal, code, or data-heavy reading surface
- native platform components where system colors are part of the product fit
- brand guidelines specify exact neutrals
- print/export, charts, or legal/compliance views require stronger contrast
- photographic, editorial, or campaign composition needs true white/black as part of the art direction
- existing product tokens already prove the neutral system works

Do not flag these as defects just because they are pure neutrals. Flag only when they create visible generic drift, broken hierarchy, brand detachment, or accessibility risk.

## Review Output

When this lens is used in review, include a compact `Color Calibration` section:

- `temperature`: warm, cool, chromatic, deliberately neutral, or mixed
- `fits product`: yes, no, partial, or needs evidence
- `token drift`: dead neutral stack, foreign semantic color, black-shadow sticker, gradient endpoint drift, icon gray drift, illustration drift, or none
- `accessibility`: contrast proof available, needs contrast check, or fails contrast
- `artifact evidence`: screenshot, preview, simulator, recorded interaction, or accepted limitation
- `action`: keep, calibrate tokens, return to design tokens, return to artifact, or do not change

Do not estimate quality gains, conversion gains, token savings, or cost savings from color calibration unless there is measured before/after evidence.
