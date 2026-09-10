# Design Craft

The craft floor: anti-slop, typography, colour, responsive behaviour, and data UI.


## Anti Slop

Noootwo Design should not produce work that looks instantly AI-generated or generically SaaS.

### Default Failure Patterns

- `Inter-only`, `system-only`, or a single safe grotesk with no contrast.
  Replace with a type system that creates tension through serif, mono, width, density, or case contrast.
- `Pure black + white + glow + rounded-full`.
  Replace with a defined surface system, restrained contrast, and shape rules that fit the product.
- `Hero + supporting copy + CTA + 3 benefit cards`.
  Replace with a first screen that expresses the product's point of view through structure, proof, or interaction.
- `All-card layouts with large radii and interchangeable shadows`.
  Replace with stronger planes, rails, rules, asymmetry, or denser content groupings.
- `Purple/blue/cyan gradients without brand reason`.
  Replace with brand-backed color discipline, tonal contrast, or restrained accent color.
- `Glassmorphism as the only premium signal`.
  Replace with typography, spacing, imagery, and composition doing the heavy lifting.
- Decorative charts, fake metrics, filler testimonials, or emoji iconography.
  Replace with real product evidence, real UI, or deliberately abstract visual language.
- Designer or artist cosplay: borrowing a famous signature look, exact composition, artwork language, or personal style marker.
  Replace with mechanism transfer: spatial rhythm, light behavior, density, information grammar, interaction model, or material logic.

### Typography Rules

- Typography must be chosen, not inherited accidentally.
- Avoid defaulting to Inter unless the current brand already uses Inter and the work must stay inside that system.
- Use no more than two core families plus an optional mono accent.
- Every direction needs one explicit source of contrast:
  - serif vs sans
  - sans vs mono
  - compressed vs wide
  - dense vs airy hierarchy
  - uppercase display vs sentence-case body
- If the product needs character, do not solve it with color alone. Start with typography and rhythm.
- If motion, color, and components do not reinforce the same point of view as the type system, the direction is incomplete.

### Density And Composition Rules

- Clean is not enough. The layout needs a point of view.
- Avoid turning every section into the same centered stack with the same spacing rhythm.
- Introduce deliberate density changes between sections so the page has momentum.
- Use stronger alignment systems than "cards floating in space".
- Prefer unexpected layouts, overlaps, diagonals, or grid breaks when they support the chosen direction.
- Asymmetry is useful when it clarifies hierarchy, not when it is decorative.
- Large empty space is only valid when the product tone earns it.
- Controlled density is as valid as generous negative space; choose one deliberately instead of drifting into neutral spacing.

### Color, Motion, And Detail Rules

- Dominant color with sharp accents is usually stronger than timid evenly distributed color.
- Motion should create one or two high-impact moments, not a spray of generic micro-interactions.
- Backgrounds should create atmosphere or depth; avoid defaulting to flat emptiness unless the direction truly earns it.
- Component language must feel designed for the context, not inherited from a UI kit without modification.
- Stack-native primitives should carry the direction; do not force every framework into the same web-card layout.
- A screenshot-free design review is not enough for ready status unless the user explicitly accepted an artifact limitation.

### First-Screen Taboos

- Do not start with a template hero if the product has a more specific opening move.
- Do not use centered logo, centered headline, centered paragraph, centered buttons by default.
- Do not use fake dashboards or fake activity as the only proof of sophistication.
- Do not let the strongest visual move be a gradient, blur, or shadow.
- Do not let motion exist as a garnish after the layout has already settled into a generic shape.
- Do not let the background collapse into a generic solid fill if the direction calls for texture, pattern, atmosphere, or depth.
- Do not let Claude-like polish become the style: nested containers, pills, status dots, and tasteful serif headlines are not a point of view by themselves.
- Do not use "in the style of X" as a direction. Name the transferable mechanism and the do-not-copy boundary instead.

### Self-Check

Before calling a design ready, ask:

- Would this still feel specific if the logo disappeared?
- What is the one unforgettable thing in this direction?
- Is the strongest decision typography, composition, product evidence, or all three?
- Does the first screen avoid the default AI landing-page pattern?
- Does this look like a product with a design system, or like a prompt artifact?
- Was this judged from a rendered artifact, screenshot, preview, or an explicit artifact limitation?


## Frontend Aesthetic Principles

Use this reference to keep design directions bold, coordinated, and memorable.

### Core Premise

- Pick a clear aesthetic direction before drafting
- Calibrate the style target before generating directions when the taste target is ambiguous
- Commit to a strong point of view rather than averaging multiple safe choices
- Every direction should answer: what is the one unforgettable thing?
- When the user asks for high-end or niche UI, ground the direction in visual references or verified mechanisms, not abstract adjectives alone
- The final judgment must happen against an artifact, screenshot, or preview whenever possible

### What Must Work Together

Treat these as one system, not separate layers:

- typography
- color and theme
- motion
- spatial composition
- backgrounds and visual details
- component language

If these do not point toward the same mood, the design is not ready.

### Direction Rules

- Choose a tone extreme, not a vague middle
- Tie the direction back to the chosen style calibration dials
- Distinguish directions through structure, density, motion, and detail treatment, not just palette changes
- Make the first screen feel authored for the product, not assembled from common SaaS modules
- Declare the artifact strategy and stack-native design move before drafting

### High-Value Aesthetic Moves

- Pair characterful display typography with disciplined supporting text
- Let one dominant color or contrast move lead the composition
- Use one or two high-impact motion moments instead of many low-value micro-interactions
- Use asymmetry, overlap, diagonal flow, or controlled density when they strengthen the chosen direction
- Build atmosphere with textures, patterns, layered transparencies, borders, grain, or depth when the direction calls for it

### Default Failure Modes

Avoid these unless the brand explicitly requires them:

- overused system-safe font stacks
- predictable hero plus cards structures
- timid evenly distributed palettes
- motion added after the layout is already generic
- component styling that feels inherited from a kit without reinterpretation
- flat, contextless backgrounds where the direction needs atmosphere

### Preflight Questions

Before entering draft mode, confirm:

- What is the tone extreme?
- Which style calibration does this direction inherit?
- What is the one unforgettable thing?
- What is the typography contrast?
- What is the motion thesis?
- What is the background/detail thesis?
- What makes the component language specific to this product?
- What artifact will prove the design works?
- What stack-native primitive carries the direction?


## Typography Craft Rubric

Use this before marking standard or deep UI work ready. Typography must prove intentional hierarchy, not just a font change.

### Required Decisions

Record these in `.noootwo/directions.md`, `.noootwo/review.md`, or `.noootwo/design-tokens.md`:

- Font choice and fallback: why the family fits the product, and what fallback preserves metrics.
- Display/body contrast: family, width, weight, case, or rhythm contrast.
- Type scale: fixed `rem` scale for dense app UI; fluid `clamp()` only where display text benefits.
- Weight roles: which weights serve headings, labels, body, captions, and numbers.
- Line-height and line length: headings tight but not clipped; body readable; long text constrained with `ch` where useful.
- Letter spacing: intentional small-caps/uppercase tracking; avoid default-everywhere or over-tight display text.
- Mobile display cap: max title size and wrapping behavior at phone width.
- Numeric behavior: `tabular-nums` for tables, metrics, ledgers, timers, and aligned values.

### Failure Flags

Any of these prevents `ready`:

- Overweight display type that crushes the composition.
- Display headline clips, overflows, or creates accidental orphan words on mobile.
- CJK display text is oversized or overweight enough to make the app feel like a poster instead of a product screen.
- Chinese and English labels fight for attention, especially when uppercase English labels are decorative rather than functional.
- Body text below 16px on web without a product-specific density reason.
- Arbitrary type sizes that do not follow a scale.
- More than 2-3 families without a clear system reason.
- Lazy monospace as the only signal for technical, industrial, or premium mood.
- Display/body contrast is absent, or too similar to read as a decision.
- Letter spacing is visibly random or makes text harder to read.
- Mobile app hierarchy depends on huge bold CJK type instead of a controlled scale, spacing, and state model.

### Review Action

- If the concept is right but type craft fails, set decision `refine` and `Return action: return to typography pass`.
- If typography is the main point of view and it fails structurally, set decision `pivot` or return to directions.
- Do not let clean spacing compensate for weak type hierarchy.


## Color System Calibration

Use this when a UI feels cheap, assembled, template-like, or visually detached because the color system does not carry a coherent product temperature across surfaces, text, shadows, semantic states, gradients, icons, or illustration.

This is a calibration lens, not a universal aesthetic law. Do not replace artifact review, typography, density, layout, component behavior, motion, or accessibility checks with color tweaks.

### Research Basis

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

### When To Use

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

### Calibration Contract

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

### Mechanisms

#### 1. Brand-Aware Neutral Temperature

If the brand or selected direction has a clear hue temperature, let the neutral ramp lean subtly toward it. The shift should be quiet enough that the user reads it as surface quality, not as a colored background.

Useful targets:

- light canvas and surface: slight hue bias, stable luminance hierarchy
- border and divider: same family as the surface, not a random default gray
- muted text: same temperature family as body text, with enough luminance contrast
- dark theme: colored dark neutrals, not simply `#000` plus gray panels

Use OKLCH or HCT when practical because hue, chroma, and lightness/tone are easier to reason about than RGB. Do not force a new color toolchain if the project already has a working token pipeline.

#### 2. Shadows And Depth

Shadows should express depth, separation, or state. They are not a generic premium filter.

Review these details:

- black shadows on light tinted surfaces can look like pasted overlays
- low-alpha brand/environment-tinted shadows often integrate better with warm or cool systems
- `0 0 0 1px` shadow-border can avoid layout shift, but it must still pass visible boundary needs
- in dark mode, depth may need glow, border, or tonal contrast instead of heavier black shadow
- some operational or flat systems should use borders and planes instead of shadows

#### 3. Text Hierarchy

Text tokens may lean warm or cool, but readability wins.

Rules:

- primary text must remain clearly readable against its surface
- muted text cannot become low-contrast decorative gray
- data-heavy text should prioritize scanning, alignment, and contrast over brand temperature
- disabled text and placeholder text should not become indistinguishable from normal muted text
- CJK body text needs stronger practical contrast than many decorative mockups imply

#### 4. Semantic Harmonization

Semantic colors must keep their category meaning. Harmonization means nudging color temperature and subtle backgrounds into the system, not making danger, warning, or success ambiguous.

Check:

- danger remains recognizably danger
- warning remains recognizably warning
- success remains recognizably success
- subtle state backgrounds belong to the canvas/surface family
- focus rings and error states do not rely on hue alone
- every semantic state has a non-color cue when needed: text, icon, border, message, or layout change

#### 5. Gradients

Gradients should stay inside the token family unless the selected direction intentionally breaks the field.

Review:

- both endpoints should belong to the same calibrated system
- avoid drifting from a branded stop into pure white or dead gray by accident
- use perceptual interpolation when gradients visibly band, gray out, or lose chroma
- mesh gradients need a base token plus related color points, not a brand blob over generic white
- gradient direction should support light, material, or composition logic

#### 6. Icons And Illustration

Icons usually inherit text tokens. Do not invent a parallel gray stack for icon strokes unless the product system explicitly requires it.

For illustrations:

- shadows, highlights, paper, skin, fabric, objects, or environment colors should share the UI temperature family
- avoid pure black and pure white as default illustration extremes unless the style deliberately calls for them
- illustration color must not weaken product UI contrast or state recognition
- generated or stock imagery should be reviewed against the surrounding token system before handoff

### Safety Exceptions

Pure white, pure black, or platform grays are acceptable when they are intentional and evidenced:

- high-contrast or accessibility mode
- document, editor, terminal, code, or data-heavy reading surface
- native platform components where system colors are part of the product fit
- brand guidelines specify exact neutrals
- print/export, charts, or legal/compliance views require stronger contrast
- photographic, editorial, or campaign composition needs true white/black as part of the art direction
- existing product tokens already prove the neutral system works

Do not flag these as defects just because they are pure neutrals. Flag only when they create visible generic drift, broken hierarchy, brand detachment, or accessibility risk.

### Review Output

When this lens is used in review, include a compact `Color Calibration` section:

- `temperature`: warm, cool, chromatic, deliberately neutral, or mixed
- `fits product`: yes, no, partial, or needs evidence
- `token drift`: dead neutral stack, foreign semantic color, black-shadow sticker, gradient endpoint drift, icon gray drift, illustration drift, or none
- `accessibility`: contrast proof available, needs contrast check, or fails contrast
- `artifact evidence`: screenshot, preview, simulator, recorded interaction, or accepted limitation
- `action`: keep, calibrate tokens, return to design tokens, return to artifact, or do not change

Do not estimate quality gains, conversion gains, token savings, or cost savings from color calibration unless there is measured before/after evidence.


## Responsive Visual Gates

Use this before `ready` on any non-trivial UI artifact. A design that clips on common viewports is not ready, even if the desktop screenshot looks strong.

### Required Viewports

Record screenshot, preview, or limitation evidence for:

- Phone: `390px` wide or nearest native device.
- Tablet or narrow desktop: `768px` wide.
- Desktop: `1440px` wide.
- Text scale or browser zoom: at least one check for 200% zoom, larger system text, or explicit limitation.

### Hard Fail Checks

Any of these forces `refine`:

- `document.documentElement.scrollWidth > window.innerWidth` on a web artifact.
- Key headline, nav, primary action, or critical data is clipped.
- Mobile display headline wraps into an unreadable block or pushes the task below an unreasonable first screen.
- Main navigation, primary action, or recovery action is inaccessible.
- Text scale breaks touch targets, state labels, or dense rows.
- Flutter/native preview ignores safe area, text scale, or platform chrome.

### Review Action

- Use `Return action: return to responsive pass` when the direction is good but viewport adaptation fails.
- Use `Return action: return to stack pass` when the failure is caused by target-stack layout behavior.
- If responsive evidence is unavailable, record the limitation and choose `needs artifact` or `refine`, not `ready`.

### Lightweight Automation

Use `scripts/check_visual_gates.py` when a local URL or static HTML file is available. The script checks overflow and obvious clipped text across the required viewports. It is a guardrail, not a substitute for design judgment.


## Data Ui Rubric

Use this for dashboards, analytics, monitoring, finance, ops workbenches, admin panels, and any UI where charts or metrics carry product meaning.

### Core Rule

Charts and metrics cannot be decorative. They must help the user decide, diagnose, compare, prioritize, or act.

### Required Checks

- Axes, units, scale, range, and time window are clear or intentionally omitted with a stated reason.
- Data state is visible: live, stale, simulated, empty, loading, partial, error, or degraded.
- Priority is clear: the user can tell which exception, metric, or segment matters first.
- Action path is visible: inspect, filter, acknowledge, drill down, compare, export, resolve, or hand off.
- Anomaly and threshold logic is named when shown.
- Color carries meaning beyond decoration and does not rely on hue alone.
- Dense layouts still preserve scanning rhythm and focus order.

### Failure Flags

- Bars, lines, maps, or gauges with no labels, units, or decision role.
- Hero marketing headline dominating an operational surface.
- Metrics that look precise but lack source, state, or time window.
- Empty dashboard chrome replacing a real workflow.
- Decorative data shapes used to make the UI feel advanced.

### Review Decision

- If the interface is visually strong but the data is decorative, mark `refine`.
- If the surface claims to be a workbench but lacks a credible action path, mark `pivot`.
- If no artifact proves data hierarchy and interaction states, mark `needs artifact`.
