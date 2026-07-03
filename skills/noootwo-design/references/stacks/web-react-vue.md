# Web, React, Vue, And Nuxt Playbook

Use this when the target artifact is browser-based.

## Artifact Path

- Prefer a running route, Storybook story, static HTML prototype, or local component preview.
- Record the URL or file path in `.noootwo/review.md`.
- Review desktop and mobile viewports when possible.

## Token Mapping

- Map approved direction into CSS variables, Tailwind theme values, UnoCSS theme values, or framework theme files.
- Define color, type, spacing, radius, surface, shadow, motion, and component vocabulary.
- Avoid one-off inline values when the design decision should become reusable.

## Implementation Moves

- Use real typography loading instead of accidental system stacks.
- Use headless or existing components, but reinterpret the visual layer.
- For React, use Motion or CSS transitions when motion carries the concept.
- For Vue/Nuxt, use `<Transition>`, `<TransitionGroup>`, CSS transitions, or existing animation utilities.
- Use GSAP only when scroll staging, timelines, or choreography justify the dependency.

## Smell Checks

- Unmodified shadcn-like card wall
- Lucide icon grid as the main visual identity
- Generic fade-up animation on a generic layout
- Hero plus cards as the default first screen
- CSS values that are impossible to maintain as tokens

## Verification

- Capture screenshots or inspect the running page.
- Check responsive breakpoints, focus states, empty/loading/error states, contrast, and reduced motion.
