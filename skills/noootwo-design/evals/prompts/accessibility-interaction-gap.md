# Eval Prompt: Accessibility And Interaction Gap

Use `$noootwo-design` on a screen with icon-only buttons, a clickable `div`, no visible focus treatment, a drag-only reorder control, and a status message that appears without an announcement.

Expected behavior:

- Name the platform and its accessibility equivalents before changing the visual layer.
- Give every control an accessible name and a keyboard, switch, remote, or platform-equivalent path.
- Restore visible focus, correct semantics, announced async feedback, stable touch targets, and a non-gesture path for reorder.
- Keep the visual direction intact while making the interaction accessible.

Failure signals:

- Treats accessibility as only a contrast check.
- Adds ARIA or Flutter semantics without fixing the interaction path.
- Leaves a hover-only, gesture-only, or colour-only critical action in place.
- Breaks the design direction to satisfy a generic checklist.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals.
