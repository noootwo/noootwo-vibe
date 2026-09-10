# Design System

Extracting, specifying, and stabilising a design system and its semantic tokens.


## Design System Setup

Set up `.noootwo/system.md` before task-specific design work. Use [system](system.md) so the result is a design contract, not a mood summary.

### Purpose

The design system memory is the durable source of truth for brand behavior, type, composition, and taste boundaries. Without it, drafts tend to be functional but generic.

The memory must not become a second source of truth. It records what is confirmed, what is inferred, and what is missing.

### Source Order

1. Existing `.noootwo/system.md`
2. Code, tokens, component names, and theme files in the current repo
3. Official product screenshots or internal screenshots
4. Brand guidelines, logos, press kits, or product pages
5. Design files, decks, annotated frames, or existing prototypes
6. User-provided references
7. Fallback lineages from [direction](direction.md) when brand evidence is incomplete

### Required Output

Update `.noootwo/system.md` with:

- `Status`
- `Updated From`
- `Source of truth`
- `Extracted from`
- `Confidence`
- `Missing evidence`
- `Published design system rules`
- `Structured design spec`
- `.noootwo/design-tokens.md` status
- `Brand primitives`
- `Preservation contract`
- `Product`
- `Audience and jobs`
- `Tone and language`
- `Type system`
- `Color roles`
- `Component patterns`
- `Layout density`
- `Motion language`
- `Shape, material, and depth`
- `Imagery, iconography, and language`
- `Agent design guidance`
- `Known generic fallbacks`
- `Forbidden combinations`
- `Platform constraints`
- `Target stack`
- `Rendering surface`
- `Stack-native component vocabulary`
- `Interaction grammar`
- `Motion primitives`
- `Visual reference library`
- `Refresh triggers`

### Confirmation Rules

- Prefer exact values from code over inferred values from screenshots
- Mark every inferred font, spacing rule, or motion rule as inferred
- If the brand type system is unknown, record the fallback lineage and why it was chosen
- Keep task-specific experiments out of the design system memory unless they are promoted into durable truth
- Record the generic fallbacks that repeatedly weaken outputs for this product
- If screenshots or code disagree with a generated system summary, prefer the actual artifact and record the conflict
- When implementation is likely, refresh `.noootwo/design-tokens.md` instead of leaving style choices only in prose
- Express colors, typography, layout, component vocabulary, motion, and states as role rules with usage limits
- Record permanent rules, variable expression, and task exceptions so reference-inspired work does not become generic during implementation
- If the system memory cannot produce a compact `Do` / `Do not` instruction block for another agent, it is not specific enough


## System Extraction

Persistent design memory lives in `.noootwo/system.md`.

Read [system](system.md) first when the file is missing, stale, or still pending extraction.
Use [system](system.md) to write extracted facts as role-based design instructions.

### Source Priority

1. Existing `.noootwo/system.md`
2. Code and tokens in the current repo
3. Current live product or internal screenshots
4. Brand guidelines or component libraries
5. Design files, decks, annotated frames, or existing prototypes
6. User-provided references
7. Industry fallback patterns

### What To Extract

- Brand primitives: colors, marks, imagery, and visual materials
- Source of truth, extraction sources, confidence level, and missing evidence
- Published design system rules or token/component conventions
- Current `.noootwo/design-tokens.md` status or gaps
- Structured design spec: visual positioning, target qualities, anti-position, role rules, and agent guidance
- Preservation contract: permanent rules, variable expression, and task-specific exceptions
- Product purpose and audience
- Tone and writing posture
- Type system: confirmed fonts, fallback logic, hierarchy, and contrast strategy
- Color roles: canvas, surface, text, accent, semantic, and data roles with usage limits
- Component patterns: recurring shells, cards, rails, panels, forms, navigation, and evidence patterns
- Layout density: spacing rhythm, information density, and preferred structural moves
- Motion language
- Shape, material, depth, imagery, iconography, and language rules
- Platform constraints
- Target stack, rendering surface, stack-native component vocabulary, interaction grammar, and motion primitives
- Visual reference library and what each reference is allowed to influence
- Known generic fallbacks that would degrade the work
- Forbidden combinations and "never do this" constraints
- Preservation contract: what must survive implementation, what may vary, and what must never be substituted

### Output Shape For `.noootwo/system.md`

- `Status`
- `Updated From`
- `Source of truth`
- `Extracted from`
- `Confidence`
- `Missing evidence`
- `Published design system rules`
- `Structured design spec`
- `.noootwo/design-tokens.md` status
- `Brand primitives`
- `Product`
- `Audience and jobs`
- `Tone and language`
- `Type system`
- `Color roles`
- `Component patterns`
- `Layout density`
- `Motion language`
- `Shape, material, and depth`
- `Imagery, iconography, and language`
- `Agent design guidance`
- `Known generic fallbacks`
- `Forbidden combinations`
- `Platform constraints`
- `Target stack`
- `Rendering surface`
- `Stack-native component vocabulary`
- `Interaction grammar`
- `Motion primitives`
- `Visual reference library`
- `Refresh triggers`
- `Preservation contract`

### Rules

- Prefer exact values from code over inferred values from screenshots
- If the current file says `Status: pending extraction`, treat it as missing
- Keep project truth separate from task-specific experimentation
- Mark inferred values as inferred
- Update the file only when new information is concrete enough to persist
- Never promote a generated direction into durable system truth unless the user confirms it should become part of the product system
- A usable extraction should let a second agent implement the design without seeing the inspiration source


## Structured Design Spec

Use this format when extracting a design system, writing directions, or preparing handoff. It borrows the useful structure of `DESIGN.md`-style design instructions without depending on any external repository, brand template, or live fetch.

For non-quick UI work, start with `intake.md`. The Design Read sets surface kind, audience, product posture, visual posture, variance, motion, density, and the existing system to preserve. This spec expands that read into implementation-ready roles.

Research basis: `DESIGN.md`-style repositories such as `VoltAgent/awesome-design-md` show that agents follow UI intent better when visual systems are written as color roles, typography roles, component rules, spacing rules, and do/don't constraints. Noootwo absorbs that format only; it does not require that repository or copy its brand-specific specs. Current public design-system guidance also supports role-based translation: Figma describes primitive, semantic, and component token layers; Atlassian frames tokens as single-source usage names for design decisions; Carbon frames motion as productive feedback and expression rather than decoration.

### Purpose

Models produce better UI when style is expressed as executable design rules instead of adjectives. A good design spec tells the agent what roles exist, how they behave, what evidence supports them, and what must not be introduced.

Do not copy another brand's surface language. Extract the structure: role-based colors, type hierarchy, component rules, layout rhythm, state behavior, do/don't constraints, and implementation mapping.

### Required Layers

#### 1. Design Read

- Surface kind: operational tool, dashboard, app shell, native screen, landing page, deck, fixed canvas, live artifact, editorial, campaign, or other.
- Audience: who must understand and reuse the surface.
- Product posture: the product stance the UI must communicate through use.
- Visual posture: the design language that supports the product posture.
- Variance, motion, density: 1-10 dials with the reason for each.
- Existing system to preserve: tokens, components, routes, brand assets, screenshots, or none found.

#### 2. Evidence And Confidence

- Source of truth: code, tokens, screenshots, design files, brand assets, user references, or selected direction.
- Confidence per decision: `confirmed`, `inferred`, or `proposed`.
- Missing evidence: fonts, spacing, motion, component states, responsive behavior, platform constraints.
- Conflict handling: prefer working product artifacts over generated prose.

#### 3. Visual Positioning

- Product surface type: product UI, data UI, utility screen, mobile app, campaign, launch, editorial, or native flow.
- Design intent: one concrete sentence about what the interface should make users feel and do.
- Target qualities: how it will be distinctive, niche, practical, simple, efficient, premium, and current.
- Anti-position: what category template, AI look, or brand cosplay must be avoided.

#### 4. Color Roles

Define roles, not just swatches.

- Canvas: base background and why it fits the product.
- Surface: panels, rails, sheets, overlays, and raised areas.
- Text: primary, secondary, disabled, inverse, and data-heavy text.
- Accent: one dominant action or identity accent with usage limits.
- Semantic: success, warning, danger, info, selected, focus.
- Data: categorical, sequential, diverging, and neutral data colors when relevant.
- Neutral temperature: warm, cool, chromatic, deliberately neutral, or unknown, with rationale.
- Contrast proof: the text/background and state pairs that must pass accessibility checks.
- Color exceptions: where pure white, pure black, platform/system colors, or exact brand neutrals are intentional.
- Forbidden color moves: generic gradients, glow, over-saturated accents, or brand-inconsistent colors.

#### 5. Typography Roles

Define the role of each type style.

- Display: font logic, weight, size range, line-height, letter-spacing, and mobile cap.
- Title: section and card titles, weight difference from display, truncation behavior.
- Body: readable size, line-height, width, fallback behavior, CJK handling.
- Label: navigation, controls, metadata, chip text, and case rules.
- Numbers: tabular nums, alignment, unit treatment, decimal behavior.
- Mono or annotation: only if it has a product reason; never as generic "technical" garnish.
- Forbidden type moves: Inter-only/system-only when personality is required, CJK overweight display, decorative uppercase labels, arbitrary scale jumps.

#### 6. Layout And Density

- Canvas model: centered page, split pane, rail, ledger, map, feed, stack, board, command surface, or native route.
- Grid: columns, gutters, max widths, rails, breakpoints, and safe areas.
- Density target: compact, balanced, generous, editorial, operational, or immersive.
- Grouping rhythm: tight related groups and generous separation between conceptual groups.
- Responsive behavior: 390px, 768px, 1440px expectations or explicit platform limits.
- Forbidden structure: hero + cards, card wall, over-thick mobile cards, fake dashboard, posterized app screen.

#### 7. Shape, Material, And Depth

- Radius scale: where sharp, soft, pill, or square shapes are allowed.
- Borders and dividers: hairline, contrast, inset, grouped, or none.
- Shadows and elevation: depth purpose, not decoration.
- Material or texture: paper, glass, metal, grain, blur, image, gradient, or flat surface only when justified.
- Failure signs: glassmorphism as the only premium signal, glow-as-polish, identical rounded panels everywhere.

#### 8. Component Vocabulary

- Shell: navigation, tabs, rails, app bars, bottom nav, command palette, or split panes.
- Content surfaces: cards, rows, tables, ledgers, lists, dossier panels, sheets, canvases, galleries.
- Actions: primary, secondary, destructive, inline, floating, batch, keyboard.
- States: loading, empty, error, focus, disabled, hover, pressed, selected, offline.
- Data grammar: axes, units, legends, thresholds, missing data, exception priority.
- Naming: component names should describe product function, not decorative metaphor.

#### 9. Motion And Interaction

- Motion thesis: what motion explains, such as continuity, hierarchy, state change, or identity.
- Durations and easing: enter, exit, reorder, expand, error, success.
- Interaction motif: swipe, drag, reveal, stack, expand, zoom, morph, command, or step-through.
- Reduced motion: acceptable fallback.
- Forbidden motion: generic fade-up on every element, bounce without product reason, animation over weak layout.

#### 10. Imagery, Iconography, And Language

- Imagery: product screenshots, editorial photography, diagrams, illustrations, textures, generated visuals, or none.
- Iconography: stroke, fill, weight, size, optical alignment, and when icons are not allowed.
- Voice: labels, empty states, CTA language, system messages, and words to avoid.
- Localization: CJK, long labels, number/date formats, and bidirectional risks when relevant.

#### 11. Agent Guidance

Write a compact instruction block another agent can follow:

- Do: 5-8 concrete moves that must appear in implementation.
- Do not: 5-8 concrete moves that would make the design generic or wrong.
- Preserve: decisions that must survive translation into React, Vue, Flutter, SwiftUI, Compose, or native.
- When uncertain: the fallback choice and the evidence needed to replace it.

#### 12. Preservation Contract

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

#### 13. Surface Inventory And Detail Translation

Use this layer only when the work is implementation-bound, production-facing, or a previous result looked directionally right but too generic in the details.

- `surface inventory`: list each shippable surface, route, section, or screen and the few components/states that define it
- `component restyling matrix`: for each important component, name the base primitive, what must be restyled, what state behavior must exist, and which defaults must not survive
- `default override pass`: record the framework or UI-kit defaults that would collapse the design into a generic fallback
- `micro-detail pass`: review dividers, icon alignment, focus treatment, button height, title wrapping, empty/loading/error states, scroll edges, and microcopy cadence
- `evidence threshold`: do not claim this layer is complete without artifact evidence for the key states that carry the direction
- `cost boundary`: do not force this layer into quick polish or early direction exploration

### Direction Usage

Each direction should include a `Design-spec delta`: the subset of this spec that would become project truth if the user selects it. Keep this shorter than the system memory; focus on the decisions that make the direction materially different.

### Handoff Usage

Handoff should include a `Design Spec Snapshot` with the selected color roles, type roles, layout model, component vocabulary, motion thesis, and forbidden moves. This snapshot is the implementation contract.

### Rules

- Structure is reusable; brand surfaces are not.
- Never promote a proposed direction into `.noootwo/system.md` unless the user confirms it should become durable truth.
- If a design spec cannot name typography roles, layout model, component vocabulary, and forbidden moves, it is not ready for implementation.
- If the spec has many adjectives but few role rules, return to system extraction or directions.
- If the preservation contract is missing, the spec is not implementation-ready.


## Artifact Family Contract

Use this note when extending Noootwo Design beyond ordinary UI surfaces into posters, slides, dashboards, or other non-trivial artifact types.

### Why This Exists

Different design tasks can share the same workflow protocol while still needing different artifact expectations.

The stable question is not "what topic is this?" but "what artifact family is this work aiming at?"

This keeps expansion generic:

- no topic-specific prompt patches
- no new mode per artifact
- no confusion between workflow protocol and runtime/export tooling

### Artifact Families

#### UI Surface

Use when the target is a product interface, app screen, route, dashboard surface, or responsive web/native UI.

Contract:

- review expects viewport, device, or platform evidence
- layout must hold across responsive or platform states
- export is optional unless the user explicitly needs delivery files

Typical failure modes:

- responsive overflow
- clipped text
- generic component fallback
- platform-inappropriate interaction/detail

#### Fixed-Canvas Graphic

Use when the target is a poster, cover, social card, hero visual, campaign static, or other composition-first output with a defined frame.

Contract:

- final dimensions must be explicit
- review expects fixed-canvas evidence, not responsive behavior
- export target must be explicit when the user needs print or delivery-ready output

Typical failure modes:

- weak composition at target aspect ratio
- unreadable type at final size
- missing bleed/trim/safe-area thinking when relevant
- output visually works in preview but not at delivery dimensions

#### Slide Deck

Use when the target is a multi-page presentation artifact with narrative sequence, page transitions, and delivery formats such as HTML, PDF, or PPTX.

Contract:

- page sequence and structure matter, not only single-slide quality
- review expects page flow and navigation evidence
- export target must be explicit

Typical failure modes:

- pretty slides with weak narrative progression
- inconsistent master/layout logic
- export target not verified
- navigation or page rhythm breaks

#### Live Artifact

Use when the target is a dashboard, decision room, KPI wall, or artifact whose live state, tweakability, or data surface matters.

Contract:

- review expects evidence of live states or state transitions
- artifact must be judged in its active form, not only by static screenshots
- delivery path must record how the live artifact will actually be opened or operated

Typical failure modes:

- static mock instead of usable live surface
- data/state path unclear
- tweak or update loop not reviewable
- strong direction but weak operational artifact

### Shared Requirements Across Families

Every family still inherits the same Noootwo workflow:

- intake
- exploration
- directions
- decision
- design contract
- implementation plan
- artifact
- review
- handoff

Every family still needs:

- explicit artifact family in the brief
- explicit preview surface before ready
- explicit review evidence
- explicit delivery or export target when relevant
- explicit return action when review fails

### Split Guidance

An artifact family can justify a future child skill only when it changes most of:

- artifact grammar
- preview surface
- export path
- review checks
- common failure modes

If it only changes subject matter or visual theme, it should stay inside the shared Noootwo workflow.
