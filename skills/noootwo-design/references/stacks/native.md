# Native App Playbook

Use this for SwiftUI, Jetpack Compose, or platform-native UI implementation.

## Artifact Path

- Prefer Xcode previews, simulator screenshots, Compose previews, emulator screenshots, or recorded interactions.
- If previews are blocked, provide reference frames plus native token/component/motion mapping.

## Token Mapping

- Map direction into platform tokens: color, typography, spacing, shape, elevation/surface, motion, and component vocabulary.
- Preserve dynamic type, reduced motion, safe areas, accessibility labels, and platform interaction idioms.

## SwiftUI Moves

- Use native navigation, sheets, matched geometry, sensory feedback, and adaptive layout where appropriate.
- Avoid forcing web landing-page structure into an app screen.
- Keep SF Symbols or custom iconography consistent with the chosen direction.

## Jetpack Compose Moves

- Use Material theme overrides, shared elements, animated content, adaptive layout, and state-driven surfaces.
- Preserve Android navigation and interaction expectations unless the product intentionally departs from them.

## Smell Checks

- Default list/form styling when the task asks for distinctive design
- Web cards and hero sections copied into a native shell
- No plan for dynamic type, reduced motion, safe areas, or accessibility
- Motion primitives named but not tied to the product interaction

## Verification

- Review previews/screenshots when possible.
- Check platform states, accessibility, dark/light mode if relevant, and motion fallback.
