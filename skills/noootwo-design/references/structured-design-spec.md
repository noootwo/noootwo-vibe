# Structured Design Spec

Use this format when extracting a design system, writing directions, or preparing handoff. It borrows the useful structure of `DESIGN.md`-style design instructions without depending on any external repository, brand template, or live fetch.

Research basis: `DESIGN.md`-style repositories such as `VoltAgent/awesome-design-md` show that agents follow UI intent better when visual systems are written as color roles, typography roles, component rules, spacing rules, and do/don't constraints. Noootwo absorbs that format only; it does not require that repository or copy its brand-specific specs. Current public design-system guidance also supports role-based translation: Figma describes primitive, semantic, and component token layers; Atlassian frames tokens as single-source usage names for design decisions; Carbon frames motion as productive feedback and expression rather than decoration.

## Purpose

Models produce better UI when style is expressed as executable design rules instead of adjectives. A good design spec tells the agent what roles exist, how they behave, what evidence supports them, and what must not be introduced.

Do not copy another brand's surface language. Extract the structure: role-based colors, type hierarchy, component rules, layout rhythm, state behavior, do/don't constraints, and implementation mapping.

## Required Layers

### 1. Evidence And Confidence

- Source of truth: code, tokens, screenshots, design files, brand assets, user references, or selected direction.
- Confidence per decision: `confirmed`, `inferred`, or `proposed`.
- Missing evidence: fonts, spacing, motion, component states, responsive behavior, platform constraints.
- Conflict handling: prefer working product artifacts over generated prose.

### 2. Visual Positioning

- Product surface type: product UI, data UI, utility screen, mobile app, campaign, launch, editorial, or native flow.
- Design intent: one concrete sentence about what the interface should make users feel and do.
- Target qualities: how it will be distinctive, niche, practical, simple, efficient, premium, and current.
- Anti-position: what category template, AI look, or brand cosplay must be avoided.

### 3. Color Roles

Define roles, not just swatches.

- Canvas: base background and why it fits the product.
- Surface: panels, rails, sheets, overlays, and raised areas.
- Text: primary, secondary, disabled, inverse, and data-heavy text.
- Accent: one dominant action or identity accent with usage limits.
- Semantic: success, warning, danger, info, selected, focus.
- Data: categorical, sequential, diverging, and neutral data colors when relevant.
- Forbidden color moves: generic gradients, glow, over-saturated accents, or brand-inconsistent colors.

### 4. Typography Roles

Define the role of each type style.

- Display: font logic, weight, size range, line-height, letter-spacing, and mobile cap.
- Title: section and card titles, weight difference from display, truncation behavior.
- Body: readable size, line-height, width, fallback behavior, CJK handling.
- Label: navigation, controls, metadata, chip text, and case rules.
- Numbers: tabular nums, alignment, unit treatment, decimal behavior.
- Mono or annotation: only if it has a product reason; never as generic "technical" garnish.
- Forbidden type moves: Inter-only/system-only when personality is required, CJK overweight display, decorative uppercase labels, arbitrary scale jumps.

### 5. Layout And Density

- Canvas model: centered page, split pane, rail, ledger, map, feed, stack, board, command surface, or native route.
- Grid: columns, gutters, max widths, rails, breakpoints, and safe areas.
- Density target: compact, balanced, generous, editorial, operational, or immersive.
- Grouping rhythm: tight related groups and generous separation between conceptual groups.
- Responsive behavior: 390px, 768px, 1440px expectations or explicit platform limits.
- Forbidden structure: hero + cards, card wall, over-thick mobile cards, fake dashboard, posterized app screen.

### 6. Shape, Material, And Depth

- Radius scale: where sharp, soft, pill, or square shapes are allowed.
- Borders and dividers: hairline, contrast, inset, grouped, or none.
- Shadows and elevation: depth purpose, not decoration.
- Material or texture: paper, glass, metal, grain, blur, image, gradient, or flat surface only when justified.
- Failure signs: glassmorphism as the only premium signal, glow-as-polish, identical rounded panels everywhere.

### 7. Component Vocabulary

- Shell: navigation, tabs, rails, app bars, bottom nav, command palette, or split panes.
- Content surfaces: cards, rows, tables, ledgers, lists, dossier panels, sheets, canvases, galleries.
- Actions: primary, secondary, destructive, inline, floating, batch, keyboard.
- States: loading, empty, error, focus, disabled, hover, pressed, selected, offline.
- Data grammar: axes, units, legends, thresholds, missing data, exception priority.
- Naming: component names should describe product function, not decorative metaphor.

### 8. Motion And Interaction

- Motion thesis: what motion explains, such as continuity, hierarchy, state change, or identity.
- Durations and easing: enter, exit, reorder, expand, error, success.
- Interaction motif: swipe, drag, reveal, stack, expand, zoom, morph, command, or step-through.
- Reduced motion: acceptable fallback.
- Forbidden motion: generic fade-up on every element, bounce without product reason, animation over weak layout.

### 9. Imagery, Iconography, And Language

- Imagery: product screenshots, editorial photography, diagrams, illustrations, textures, generated visuals, or none.
- Iconography: stroke, fill, weight, size, optical alignment, and when icons are not allowed.
- Voice: labels, empty states, CTA language, system messages, and words to avoid.
- Localization: CJK, long labels, number/date formats, and bidirectional risks when relevant.

### 10. Agent Guidance

Write a compact instruction block another agent can follow:

- Do: 5-8 concrete moves that must appear in implementation.
- Do not: 5-8 concrete moves that would make the design generic or wrong.
- Preserve: decisions that must survive translation into React, Vue, Flutter, SwiftUI, Compose, or native.
- When uncertain: the fallback choice and the evidence needed to replace it.

### 11. Preservation Contract

Treat the selected direction as three layers:

- Permanent rules: the few decisions that define the system's identity and must not change during translation
- Variable expression: details that may adapt to stack, content, or device without losing the direction
- Task exceptions: one-off changes allowed for this surface only, with the reason recorded

For each selected direction, explicitly name:

- `must preserve`: the 1-3 mechanisms that define the direction
- `allowed variation`: what may change in implementation without losing the direction
- `forbidden substitution`: what would collapse the design into a generic fallback
- `signature mechanism`: the single most distinctive transferable behavior
- `token target`: the semantic token rules that need to exist
- `component target`: the component vocabulary that needs to exist
- `motion target`: the motion rule that needs to exist

### 12. Surface Inventory And Detail Translation

Use this layer only when the work is implementation-bound, production-facing, or a previous result looked directionally right but too generic in the details.

- `surface inventory`: list each shippable surface, route, section, or screen and the few components/states that define it
- `component restyling matrix`: for each important component, name the base primitive, what must be restyled, what state behavior must exist, and which defaults must not survive
- `default override pass`: record the framework or UI-kit defaults that would collapse the design into a generic fallback
- `micro-detail pass`: review dividers, icon alignment, focus treatment, button height, title wrapping, empty/loading/error states, scroll edges, and microcopy cadence
- `evidence threshold`: do not claim this layer is complete without artifact evidence for the key states that carry the direction
- `cost boundary`: do not force this layer into quick polish or early direction exploration

## Direction Usage

Each direction should include a `Design-spec delta`: the subset of this spec that would become project truth if the user selects it. Keep this shorter than the system memory; focus on the decisions that make the direction materially different.

## Handoff Usage

Handoff should include a `Design Spec Snapshot` with the selected color roles, type roles, layout model, component vocabulary, motion thesis, and forbidden moves. This snapshot is the implementation contract.

## Rules

- Structure is reusable; brand surfaces are not.
- Never promote a proposed direction into `.noootwo/system.md` unless the user confirms it should become durable truth.
- If a design spec cannot name typography roles, layout model, component vocabulary, and forbidden moves, it is not ready for implementation.
- If the spec has many adjectives but few role rules, return to system extraction or directions.
- If the preservation contract is missing, the spec is not implementation-ready.
