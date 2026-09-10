# Design Translation

Turning an approved direction into stack-native implementation, assets, and handoff.


## Detail Translation Pass

Use this when the chosen direction is visually right but the implemented UI still feels generic, AI-like, or too dependent on framework defaults.

This is not a new mode. It is an implementation-stage reinforcement layer for `production` work, or for review loops where the artifact is close but still feels like a polished default.

Do not use this pass to rescue a misunderstood style. If the visual evidence, selected direction, and implementation contract do not describe the same mechanisms, return to `style-evidence-check.md` or style discovery first.

### Research Basis

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

### Problem Pattern

Typical failure shape:

- direction and screenshots look promising
- token choices are mostly correct
- component defaults survive into final UI
- states, spacing, dividers, icons, and motion timings drift back to framework norms
- default grays, default error red, pure-black shadows, pure-white gradient endpoints, or icon gray stacks survive without product reason
- the page reads as "close to the intended style" instead of feeling fully authored

This pass exists to stop that last-mile drift.

### Mechanisms To Borrow

#### 1. Surface Inventory

Before implementation, list each surface that must ship:

- route, screen, panel, section, sheet, or modal
- primary task on that surface
- components that define its feel
- required states that must be reviewed
- obvious default fallback to avoid

This prevents the implementer from designing only the hero state and leaving the rest to defaults.

#### 2. Component Restyling Matrix

For each important component, record:

- base primitive or source component
- tokens that must change
- state behavior that must exist
- detail rules that matter to the direction
- defaults that must be removed or overridden

This prevents "used the right component, wrong expression" failures.

#### 3. Default Override Pass

Run an explicit pass for framework or UI-kit defaults that often survive translation:

- web: generic card walls, default shadcn radius/shadow treatment, Lucide-icon-grid identity, generic fade-up
- Flutter: `Scaffold + AppBar + Card + ListView`, seed-color surfaces, poster-like cards, decorative chips
- native: stock platform surfaces without token reinterpretation, default transitions without state intent

This pass is useful because many "AI-looking" results are technically customized, but still visibly anchored to starter defaults.

#### 4. Micro-Detail Pass

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

#### 5. Color Calibration Pass

Use [color-system-calibration.md](craft.md) when color drift is part of the generic feel. Check:

- neutral temperature across canvas, surface, border, and muted text
- shadow hue and whether depth should be shadow, glow, border, or plane contrast
- semantic colors and subtle state backgrounds, especially error, warning, success, focus, and selected
- gradient endpoints and mesh bases staying inside the token family
- icons inheriting text tokens and illustrations sharing the UI shadow/highlight family
- contrast proof and explicit exceptions for pure white, pure black, platform grays, or exact brand neutrals

This pass calibrates the token system. It must not turn into a blanket ban on pure neutrals or a replacement for typography, layout, and artifact review.

### Cost And Applicability

- `quick`: do not require this pass
- `standard`: optional, only after the direction is already stable
- `deep`: useful when high-character craft is the point of the exercise
- `production`: recommended whenever the work is implementation-bound
- `review`: require it when the artifact is directionally right but still feels generic

### Risks And Counterexamples

- Risk: turning this into a mandatory early-stage checklist makes Noootwo too expensive.
  - Response: keep it out of quick mode and early direction exploration.
- Risk: writing too many detail bullets without artifact proof creates fake precision.
  - Response: tie the pass to screenshots, previews, or simulator/device evidence.
- Risk: confusing this with pixel-perfect mimicry of a reference.
  - Response: preserve mechanism and authored detail, not a copied brand surface.

### Verification

Record proof in `.noootwo/review.md` or handoff:

- artifact path or URL
- surfaces reviewed
- states reviewed
- defaults removed
- highest-impact authored detail
- remaining generic drift, if any

If the reviewer cannot say which details are authored and which defaults were intentionally removed, the pass is incomplete.


## Handoff Bundle

The handoff bundle translates design intent into implementation-ready instructions.

### Required Files

- `.noootwo/handoff/implementation.md`
- `.noootwo/handoff/acceptance.md`
- `.noootwo/handoff/assets.md`

### `implementation.md`

Must include:

- design intent
- design decisions that must survive implementation
- preservation contract: must preserve, allowed variation, forbidden substitution, signature mechanism, token target, component target, and motion target
- chosen direction
- design spec snapshot: color roles, type roles, layout model, component vocabulary, motion thesis, and forbidden moves
- layout map
- surface inventory
- component responsibilities
- component restyling matrix
- interaction and state notes
- motion guidance
- default override pass
- micro-detail pass
- stack-specific implementation notes
- artifact reviewed and review evidence
- token mapping from `.noootwo/design-tokens.md`
- artifact verification requirements
- edge states: loading, empty, error, focus, disabled, hover or pressed
- implementation risks
- user decisions confirmed, delegated, or still blocking
- implementation priority order

### `acceptance.md`

Must include:

- what "done" means visually
- state and interaction checks
- responsive or platform checks
- accessibility or clarity checks
- screenshot or preview checks
- default override checks
- micro-detail checks
- regression risks to watch

### `assets.md`

Must include:

- required brand assets
- approved fallbacks
- source links or origin notes
- unresolved asset gaps

### Rules

- Write for another agent or engineer who was not present in the design conversation
- Prefer concrete rules over taste-only commentary
- If something is still uncertain, mark it as a decision point instead of hiding it
- Preserve component names, motion intent, state behavior, and implementation risks from the review
- Preserve the signature mechanism, not only the visible surface style
- Do not let handoff become a style moodboard; it must tell the implementer what to build and what not to lose
- If the selected design spec cannot be translated into tokens and component rules, return to production mapping before implementation
- If a user decision is still open, mark it as blocking instead of choosing silently in handoff


## Asset Protocol

Brand recognition comes from assets before style commentary.

### Required Asset Order

1. Logo
2. Product imagery or UI screenshots
3. Core brand colors
4. Typography or font guidance
5. Brand guidelines or design system links

### Workflow

1. Ask whether the user already has the assets
2. Search official sources before using third-party mirrors
3. Record every confirmed asset in `.noootwo/handoff/assets.md`
4. Explicitly mark missing assets and the fallback you chose

### What To Record

For each asset, capture:

- `Asset`
- `Required?`
- `Source`
- `Usage intent`
- `Gaps or risks`

### Rules

- Do not fake a logo if the real logo is required
- Do not claim a product visual language without product visuals or screenshots
- If assets are missing, say so in the handoff bundle
- For digital products, UI screenshots often matter more than abstract brand adjectives


## Canvas Artifact Loop

Use this reference whenever a design result must be judged visually.

### Core Rule

A design cannot be marked `ready` without a reviewable artifact or explicit evidence that an artifact cannot be produced in the current environment.

### Artifact Types

- Web, React, Vue, or Nuxt: running browser page, Storybook story, local route, static HTML prototype, or screenshot set.
- Flutter: simulator/device screenshot, golden-style screenshot, recorded interaction, or a small target-stack prototype.
- SwiftUI: Xcode preview, simulator screenshot, recorded interaction, or platform-specific implementation notes with reference frames.
- Jetpack Compose: preview screenshot, emulator screenshot, recorded interaction, or platform-specific implementation notes with reference frames.
- Ambiguous stack: HTML-native prototype plus stack translation notes.
- Blocked environment: annotated wireframe, reference board, and precise acceptance checklist.

### Workflow

1. Declare the intended artifact before drafting.
2. Build the fastest first artifact that can expose hierarchy, density, typography, motion posture, and component vocabulary.
3. Review the artifact, not just the written plan.
4. If implementation detail drift is the risk, run the detail-translation pass on the artifact: surface inventory, component restyling, default overrides, and micro-detail review.
5. If the artifact is generic, return to directions or stack translation.
6. If the artifact is directionally right but weak, return to draft.
7. Only produce handoff after the artifact passes review or the user accepts an explicit limitation.

### Wireframe Mode

Use wireframe mode when the direction is still uncertain or token/time budget is tight.

- Keep fidelity low enough to explore structure quickly.
- Preserve the key differentiators: density, opening move, component vocabulary, and interaction thesis.
- Do not judge final craft from wireframe mode.
- Exit wireframe mode before handoff unless the user explicitly wants only concept exploration.

### Polish Mode

Use polish mode only after the direction is fundamentally right.

- Refine typography, spacing, rhythm, contrast, state surfaces, and motion timing.
- Review component defaults and micro-details, not only page composition.
- Check responsive or platform-specific breakpoints.
- Remove generic library defaults.
- Preserve the one unforgettable move.

### Screenshot Review Requirements

When screenshots or live previews are available, record:

- artifact path, URL, simulator, or screenshot location
- viewport or device size
- interaction state reviewed
- strongest authored move
- generic fallback flags
- mismatch between design intent and rendered output

### Blocked Artifact Rules

If a live artifact cannot be produced:

- record why it is blocked
- produce the closest visual substitute
- include stack-native translation notes
- mark review as `needs artifact` unless the user explicitly accepts a text-only handoff


## Target Stack Rules

Noootwo Design should choose the fastest path to a reviewable artifact without losing stack-native design quality.

Read [canvas-artifact-loop.md](translate.md) before choosing a path.

### Decision Order

1. If the target stack exists locally and can reasonably be run or inspected, work in that stack.
2. If the target stack exists but cannot be run, produce a stack-native implementation plan plus the closest visual artifact available.
3. If the stack is unknown or the work is pure direction exploration, use an HTML-native prototype to validate the visual direction.
4. If the output is only a handoff, explain why no artifact can be produced and mark the review accordingly.

### Web, React, Vue, Or Nuxt

Use when the design is headed into an existing browser-based product or a web prototype.

Read [web-react-vue.md](translate.md).

Rules:

- extract tokens, routes, components, CSS variables, and existing UI vocabulary first
- build or update a browser-visible artifact whenever possible
- use screenshots or browser inspection for review
- express novelty through structure, rhythm, typography, component language, and motion, not only palette changes
- avoid unmodified UI-kit defaults such as generic shadcn-style cards, pills, and Lucide-icon grids
- specify motion through real primitives when relevant: CSS transitions, Motion, GSAP, Vue transitions, or framework-native equivalents

### HTML-Native Prototype

Use when direction approval is needed before production implementation, the stack is ambiguous, or the target stack is too slow to validate visually.

Rules:

- optimize for visual fidelity and decision quality
- make interaction flows believable enough to review density, hierarchy, and motion posture
- treat the prototype as a direction artifact, not production code
- include stack translation notes before handoff
- critique the prototype before polishing it

## Flutter

Use when the target app is Flutter or when Flutter will implement the approved design.

Read [flutter.md](translate.md).

Rules:

- do not default to text-only handoff if a Flutter artifact can be run, previewed, or screenshotted
- translate the chosen direction into Flutter primitives: `ThemeData`, `ThemeExtension`, `CustomScrollView`, slivers, `Hero`, implicit or explicit animations, `CustomPainter`, Rive/Lottie, gestures, and platform density
- avoid default `Scaffold + AppBar + Card + ListView` composition unless the product explicitly needs it
- record how typography, shape, spacing, motion, and imagery map to widgets and theme tokens
- review real screenshots when possible; otherwise provide a visual prototype plus Flutter-specific mapping
- keep platform affordances: touch targets, safe areas, navigation model, performance, accessibility, and text scale

### SwiftUI Or Jetpack Compose

Use when the approved design will be implemented in native iOS, macOS, Android, or Compose Multiplatform.

Read [native.md](translate.md).

Rules:

- preserve platform idioms instead of forcing web page structure into an app shell
- translate the direction into native primitives: navigation, sheets, lists, shared transitions, surface layering, typography, haptics, and state feedback
- review previews, simulator screenshots, or emulator screenshots when possible
- when previews are blocked, produce reference frames plus implementation notes that name native components and transitions
- avoid generic native defaults when the brief asks for distinctive or high-character UI

### Existing Application Refinement

Use when improving an existing product surface.

Rules:

- extract the current system and constraints first
- still produce 3 directions for major redesigns unless the user explicitly asks for minor polish
- keep at least one direction close enough to the current system to be feasible
- make the artifact show before/after risk, not just final polish

### Handoff-Only Fallback

Use only when an artifact cannot be produced in the current environment or the user explicitly asks for handoff only.

Required contents:

- why the artifact is blocked or out of scope
- chosen direction and visual intent
- stack-native component, token, layout, and motion mapping
- states: loading, empty, error, focus, hover/pressed, disabled, and responsive/platform variants
- screenshot review checklist for the implementation agent
- acceptance criteria that preserve the strongest design decisions


## Web React Vue

Use this when the target artifact is browser-based.

### Artifact Path

- Prefer a running route, Storybook story, static HTML prototype, or local component preview.
- Record the URL or file path in `.noootwo/review.md`.
- Review desktop and mobile viewports when possible.

### Token Mapping

- Map approved direction into CSS variables, Tailwind theme values, UnoCSS theme values, or framework theme files.
- Define color, type, spacing, radius, surface, shadow, motion, and component vocabulary.
- Avoid one-off inline values when the design decision should become reusable.

### Implementation Moves

- Use real typography loading instead of accidental system stacks.
- Use headless or existing components, but reinterpret the visual layer.
- For React, use Motion or CSS transitions when motion carries the concept.
- For Vue/Nuxt, use `<Transition>`, `<TransitionGroup>`, CSS transitions, or existing animation utilities.
- Use GSAP only when scroll staging, timelines, or choreography justify the dependency.

### Smell Checks

- Unmodified shadcn-like card wall
- Lucide icon grid as the main visual identity
- Generic fade-up animation on a generic layout
- Hero plus cards as the default first screen
- CSS values that are impossible to maintain as tokens

### Verification

- Capture screenshots or inspect the running page.
- Check responsive breakpoints, focus states, empty/loading/error states, contrast, and reduced motion.


## Flutter

Use this when the target stack is Flutter.

### Artifact Path

- Prefer running the app, a focused route, a widget preview harness, golden-style screenshot, or simulator/device screenshots.
- A real Flutter artifact should come before HTML proxy when Flutter tooling is available.
- If execution is blocked, provide an HTML-native visual prototype plus Flutter-specific token, widget, and motion mapping, and mark it as fallback.
- Record screenshot or blocker details in `.noootwo/review.md`.
- Do not mark Flutter work stack-native ready when the only artifact is an HTML phone-shell proxy.
- Deep Flutter work needs at least one real route/widget preview, simulator/device screenshot, or golden-style screenshot before `stack_native_craft` can be treated as strong.
- Full Flutter redesign work should not start implementation until the user selected a direction from the 3-direction menu, unless the user explicitly delegated that choice.

### Token Mapping

- Map approved direction into `ThemeData`, `ColorScheme`, `TextTheme`, and `ThemeExtension` where useful.
- Define spacing, radius, surface, shadow/elevation, motion duration/easing, and component vocabulary.
- Keep text scale, safe areas, touch targets, and accessibility in scope.
- Record font fallback, display/body contrast, text scale behavior, and tabular numeric behavior when relevant.

### Implementation Moves

- Use `CustomScrollView`, slivers, and composed layout primitives for distinctive structure.
- Use `Hero`, implicit animations, explicit animations, gestures, or page transitions when motion carries meaning.
- Use `CustomPainter`, shaders, Rive, or Lottie only when they support the chosen art direction.
- Prefer reusable widgets and theme extensions over one-off styling.

### Smell Checks

- Default `Scaffold + AppBar + Card + ListView` for a high-character screen
- Material seed color without art direction
- Generic large-radius cards and shadows
- Oversized CJK headlines, decorative uppercase English labels, and thick rounded card stacks that make the screen feel like a poster
- Chip/status overload where every fact becomes a pill, badge, or icon block
- Bottom navigation that looks like a demo asset instead of a restrained platform control
- Visual metaphor cosplay where names like cabinet, drawer, ledger, tray, or rail do not make the task faster or clearer
- Motion as decorative garnish
- Ignoring text scale, safe area, performance, or accessibility

### Verification

- Review at least one phone viewport when possible.
- Check text scale, safe area, touch targets, overflow, loading/empty/error states, reduced motion feasibility, and frame-risk effects.
- Check whether the screen feels like a mature mobile app: clear task path, restrained navigation, controlled CJK type scale, useful density, and platform-credible interaction states.
- Record whether `ThemeData`, `TextTheme`, `ThemeExtension`, slivers, `CustomPainter`, Rive, or other stack-native moves were actually used.
- If only an HTML proxy was reviewed, the decision is `needs artifact`, `refine`, or fallback-ready only by explicit user acceptance.


## Native

Use this for SwiftUI, Jetpack Compose, or platform-native UI implementation.

### Artifact Path

- Prefer Xcode previews, simulator screenshots, Compose previews, emulator screenshots, or recorded interactions.
- If previews are blocked, provide reference frames plus native token/component/motion mapping.

### Token Mapping

- Map direction into platform tokens: color, typography, spacing, shape, elevation/surface, motion, and component vocabulary.
- Preserve dynamic type, reduced motion, safe areas, accessibility labels, and platform interaction idioms.

### SwiftUI Moves

- Use native navigation, sheets, matched geometry, sensory feedback, and adaptive layout where appropriate.
- Avoid forcing web landing-page structure into an app screen.
- Keep SF Symbols or custom iconography consistent with the chosen direction.

### Jetpack Compose Moves

- Use Material theme overrides, shared elements, animated content, adaptive layout, and state-driven surfaces.
- Preserve Android navigation and interaction expectations unless the product intentionally departs from them.

### Smell Checks

- Default list/form styling when the task asks for distinctive design
- Web cards and hero sections copied into a native shell
- No plan for dynamic type, reduced motion, safe areas, or accessibility
- Motion primitives named but not tied to the product interaction

### Verification

- Review previews/screenshots when possible.
- Check platform states, accessibility, dark/light mode if relevant, and motion fallback.
