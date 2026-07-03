# Canvas Artifact Loop

Use this reference whenever a design result must be judged visually.

## Core Rule

A design cannot be marked `ready` without a reviewable artifact or explicit evidence that an artifact cannot be produced in the current environment.

## Artifact Types

- Web, React, Vue, or Nuxt: running browser page, Storybook story, local route, static HTML prototype, or screenshot set.
- Flutter: simulator/device screenshot, golden-style screenshot, recorded interaction, or a small target-stack prototype.
- SwiftUI: Xcode preview, simulator screenshot, recorded interaction, or platform-specific implementation notes with reference frames.
- Jetpack Compose: preview screenshot, emulator screenshot, recorded interaction, or platform-specific implementation notes with reference frames.
- Ambiguous stack: HTML-native prototype plus stack translation notes.
- Blocked environment: annotated wireframe, reference board, and precise acceptance checklist.

## Workflow

1. Declare the intended artifact before drafting.
2. Build the fastest first artifact that can expose hierarchy, density, typography, motion posture, and component vocabulary.
3. Review the artifact, not just the written plan.
4. If implementation detail drift is the risk, run the detail-translation pass on the artifact: surface inventory, component restyling, default overrides, and micro-detail review.
5. If the artifact is generic, return to directions or stack translation.
6. If the artifact is directionally right but weak, return to draft.
7. Only produce handoff after the artifact passes review or the user accepts an explicit limitation.

## Wireframe Mode

Use wireframe mode when the direction is still uncertain or token/time budget is tight.

- Keep fidelity low enough to explore structure quickly.
- Preserve the key differentiators: density, opening move, component vocabulary, and interaction thesis.
- Do not judge final craft from wireframe mode.
- Exit wireframe mode before handoff unless the user explicitly wants only concept exploration.

## Polish Mode

Use polish mode only after the direction is fundamentally right.

- Refine typography, spacing, rhythm, contrast, state surfaces, and motion timing.
- Review component defaults and micro-details, not only page composition.
- Check responsive or platform-specific breakpoints.
- Remove generic library defaults.
- Preserve the one unforgettable move.

## Screenshot Review Requirements

When screenshots or live previews are available, record:

- artifact path, URL, simulator, or screenshot location
- viewport or device size
- interaction state reviewed
- strongest authored move
- generic fallback flags
- mismatch between design intent and rendered output

## Blocked Artifact Rules

If a live artifact cannot be produced:

- record why it is blocked
- produce the closest visual substitute
- include stack-native translation notes
- mark review as `needs artifact` unless the user explicitly accepts a text-only handoff
