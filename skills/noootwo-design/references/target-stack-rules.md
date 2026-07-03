# Target Stack Rules

Noootwo Design should choose the fastest path to a reviewable artifact without losing stack-native design quality.

Read [canvas-artifact-loop.md](canvas-artifact-loop.md) before choosing a path.

## Decision Order

1. If the target stack exists locally and can reasonably be run or inspected, work in that stack.
2. If the target stack exists but cannot be run, produce a stack-native implementation plan plus the closest visual artifact available.
3. If the stack is unknown or the work is pure direction exploration, use an HTML-native prototype to validate the visual direction.
4. If the output is only a handoff, explain why no artifact can be produced and mark the review accordingly.

## Web, React, Vue, Or Nuxt

Use when the design is headed into an existing browser-based product or a web prototype.

Read [web-react-vue.md](stacks/web-react-vue.md).

Rules:

- extract tokens, routes, components, CSS variables, and existing UI vocabulary first
- build or update a browser-visible artifact whenever possible
- use screenshots or browser inspection for review
- express novelty through structure, rhythm, typography, component language, and motion, not only palette changes
- avoid unmodified UI-kit defaults such as generic shadcn-style cards, pills, and Lucide-icon grids
- specify motion through real primitives when relevant: CSS transitions, Motion, GSAP, Vue transitions, or framework-native equivalents

## HTML-Native Prototype

Use when direction approval is needed before production implementation, the stack is ambiguous, or the target stack is too slow to validate visually.

Rules:

- optimize for visual fidelity and decision quality
- make interaction flows believable enough to review density, hierarchy, and motion posture
- treat the prototype as a direction artifact, not production code
- include stack translation notes before handoff
- critique the prototype before polishing it

## Flutter

Use when the target app is Flutter or when Flutter will implement the approved design.

Read [flutter.md](stacks/flutter.md).

Rules:

- do not default to text-only handoff if a Flutter artifact can be run, previewed, or screenshotted
- translate the chosen direction into Flutter primitives: `ThemeData`, `ThemeExtension`, `CustomScrollView`, slivers, `Hero`, implicit or explicit animations, `CustomPainter`, Rive/Lottie, gestures, and platform density
- avoid default `Scaffold + AppBar + Card + ListView` composition unless the product explicitly needs it
- record how typography, shape, spacing, motion, and imagery map to widgets and theme tokens
- review real screenshots when possible; otherwise provide a visual prototype plus Flutter-specific mapping
- keep platform affordances: touch targets, safe areas, navigation model, performance, accessibility, and text scale

## SwiftUI Or Jetpack Compose

Use when the approved design will be implemented in native iOS, macOS, Android, or Compose Multiplatform.

Read [native.md](stacks/native.md).

Rules:

- preserve platform idioms instead of forcing web page structure into an app shell
- translate the direction into native primitives: navigation, sheets, lists, shared transitions, surface layering, typography, haptics, and state feedback
- review previews, simulator screenshots, or emulator screenshots when possible
- when previews are blocked, produce reference frames plus implementation notes that name native components and transitions
- avoid generic native defaults when the brief asks for distinctive or high-character UI

## Existing Application Refinement

Use when improving an existing product surface.

Rules:

- extract the current system and constraints first
- still produce 3 directions for major redesigns unless the user explicitly asks for minor polish
- keep at least one direction close enough to the current system to be feasible
- make the artifact show before/after risk, not just final polish

## Handoff-Only Fallback

Use only when an artifact cannot be produced in the current environment or the user explicitly asks for handoff only.

Required contents:

- why the artifact is blocked or out of scope
- chosen direction and visual intent
- stack-native component, token, layout, and motion mapping
- states: loading, empty, error, focus, hover/pressed, disabled, and responsive/platform variants
- screenshot review checklist for the implementation agent
- acceptance criteria that preserve the strongest design decisions
