# Adoption Playbook

Use this when Noootwo Design is introduced into a project that already has UI work.

## Trigger

Use `adopt-project` when:

- The project has existing pages, screens, components, themes, or screenshots.
- `.noootwo/` is missing, pending, stale, or was added mid-project.
- The user asks to start using Noootwo Design in an existing React, Vue, Flutter, SwiftUI, Compose, or native app.

## Baseline Capture

Before redesigning, inspect and record:

- Existing `.noootwo/` files and target project `AGENTS.md`
- Target stack, routing, preview, Storybook, simulator, or screenshot capability
- Theme files, tokens, CSS variables, Tailwind config, Flutter `ThemeData`, SwiftUI token structs, Compose theme files, or native style resources
- Component library and recurring component vocabulary
- Current screenshots, live route, app preview, or closest visual artifact
- Surfaces that must be preserved and surfaces that may change
- First safe change that improves quality without breaking product continuity

Write the result to `.noootwo/adoption.md`.

## Preserve And Improve Boundary

- Preserve confirmed brand tokens, product-specific components, information hierarchy, and accessibility constraints.
- Improve generic fallbacks, weak typography, visual noise, missing states, and inconsistent spacing.
- Do not introduce a new art direction until baseline evidence and user intent support it.
- If the project is already in production implementation, prefer `production` after adoption rather than reopening broad exploration.

## Mode Handoff

- Use `quick` for small polish after adoption.
- Use `standard` for new surfaces that must fit the existing product.
- Use `deep` only when the user wants a stronger art direction and reference evidence is available.
- If the user wants all UI redesigned, complete adoption baseline, then trigger the full redesign checkpoint before editing implementation files.
- Use `production` when the design is already chosen and needs target-stack implementation.

## Blockers

If no artifact, screenshot, preview, or code surface can be inspected, mark adoption incomplete and do not claim the project design system is established.
