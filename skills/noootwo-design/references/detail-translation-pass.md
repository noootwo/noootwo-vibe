# Detail Translation Pass

Use this when the chosen direction is visually right but the implemented UI still feels generic, AI-like, or too dependent on framework defaults.

This is not a new mode. It is an implementation-stage reinforcement layer for `production` work, or for review loops where the artifact is close but still feels like a polished default.

Do not use this pass to rescue a misunderstood style. If the visual evidence, selected direction, and implementation contract do not describe the same mechanisms, return to `style-evidence-check.md` or style discovery first.

## Research Basis

Sources reviewed for this mechanism:

- Figma semantic systems blog: design systems become more resilient when variables carry semantic meaning across context and mode, not only raw visual values.
  - Source: https://www.figma.com/blog/the-future-of-design-systems-is-semantic/
  - Evidence level: official
- Atlassian design tokens: tokens act as a single source of truth for design decisions, including modifiers and state-aware naming.
  - Source: https://atlassian.design/foundations/tokens/design-tokens/
  - Evidence level: official
- Material Color Utilities, WCAG, and MDN color mixing guidance support color-system calibration through role-based tones, contrast checks, and perceptual color spaces such as HCT or OKLCH when practical.
  - Sources: https://github.com/material-foundation/material-color-utilities, https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html, https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/color-mix
  - Evidence level: official implementation plus standards/platform documentation
- Carbon motion overview: components may include microinteractions, but product teams still need an overarching motion system so the product feels coherent rather than assembled.
  - Source: https://carbondesignsystem.com/elements/motion/overview/
  - Evidence level: official
- Android Compose Material 3 guidance: shape, theming, interaction state, and state animations are first-class implementation concerns rather than afterthought polish.
  - Sources: https://developer.android.com/develop/ui/compose/designsystems/material3 and https://developer.android.com/develop/ui/compose/styles/state-animations
  - Evidence level: official
- shadcn/ui and community response: open-code starter components are intentionally a starting point; teams that do not reinterpret them converge toward the same look.
  - Sources: https://github.com/shadcn-ui/ui, https://news.ycombinator.com/item?id=43542734
  - Evidence level: official plus community signal
- Community signal around AI-generated UI sameness: people repeatedly describe outputs as samey when prompts stop at palette/layout and do not specify per-component behavior or references.
  - Source: https://www.reddit.com/r/vibecoding/comments/1ta6r5y/why_do_all_aigenerated_websites_look_exactly_the/
  - Evidence level: community signal

## Problem Pattern

Typical failure shape:

- direction and screenshots look promising
- token choices are mostly correct
- component defaults survive into final UI
- states, spacing, dividers, icons, and motion timings drift back to framework norms
- default grays, default error red, pure-black shadows, pure-white gradient endpoints, or icon gray stacks survive without product reason
- the page reads as "close to the intended style" instead of feeling fully authored

This pass exists to stop that last-mile drift.

## Mechanisms To Borrow

### 1. Surface Inventory

Before implementation, list each surface that must ship:

- route, screen, panel, section, sheet, or modal
- primary task on that surface
- components that define its feel
- required states that must be reviewed
- obvious default fallback to avoid

This prevents the implementer from designing only the hero state and leaving the rest to defaults.

### 2. Component Restyling Matrix

For each important component, record:

- base primitive or source component
- tokens that must change
- state behavior that must exist
- detail rules that matter to the direction
- defaults that must be removed or overridden

This prevents "used the right component, wrong expression" failures.

### 3. Default Override Pass

Run an explicit pass for framework or UI-kit defaults that often survive translation:

- web: generic card walls, default shadcn radius/shadow treatment, Lucide-icon-grid identity, generic fade-up
- Flutter: `Scaffold + AppBar + Card + ListView`, seed-color surfaces, poster-like cards, decorative chips
- native: stock platform surfaces without token reinterpretation, default transitions without state intent

This pass is useful because many "AI-looking" results are technically customized, but still visibly anchored to starter defaults.

### 4. Micro-Detail Pass

Review details that change whether the UI feels authored:

- divider contrast, thickness, and inset logic
- icon size, weight, and optical alignment
- button height, padding, and pressed/hover/focus behavior
- title wrapping, line breaks, and truncation
- empty, loading, error, and disabled states
- focus treatment and keyboard/touch feedback
- scroll boundaries, sticky edges, and clipping
- microcopy cadence, label tone, and placeholder text

This should happen on artifacts, not only in prose.

### 5. Color Calibration Pass

Use [color-system-calibration.md](color-system-calibration.md) when color drift is part of the generic feel. Check:

- neutral temperature across canvas, surface, border, and muted text
- shadow hue and whether depth should be shadow, glow, border, or plane contrast
- semantic colors and subtle state backgrounds, especially error, warning, success, focus, and selected
- gradient endpoints and mesh bases staying inside the token family
- icons inheriting text tokens and illustrations sharing the UI shadow/highlight family
- contrast proof and explicit exceptions for pure white, pure black, platform grays, or exact brand neutrals

This pass calibrates the token system. It must not turn into a blanket ban on pure neutrals or a replacement for typography, layout, and artifact review.

## Cost And Applicability

- `quick`: do not require this pass
- `standard`: optional, only after the direction is already stable
- `deep`: useful when high-character craft is the point of the exercise
- `production`: recommended whenever the work is implementation-bound
- `review`: require it when the artifact is directionally right but still feels generic

## Risks And Counterexamples

- Risk: turning this into a mandatory early-stage checklist makes Noootwo too expensive.
  - Response: keep it out of quick mode and early direction exploration.
- Risk: writing too many detail bullets without artifact proof creates fake precision.
  - Response: tie the pass to screenshots, previews, or simulator/device evidence.
- Risk: confusing this with pixel-perfect mimicry of a reference.
  - Response: preserve mechanism and authored detail, not a copied brand surface.

## Verification

Record proof in `.noootwo/review.md` or handoff:

- artifact path or URL
- surfaces reviewed
- states reviewed
- defaults removed
- highest-impact authored detail
- remaining generic drift, if any

If the reviewer cannot say which details are authored and which defaults were intentionally removed, the pass is incomplete.
