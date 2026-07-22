## UI/Design Workflow

Use `$noootwo-design` for UI/frontend visual changes, app screens, redesigns, design reviews, and design-to-implementation handoff after the product path is clear enough.

If requirements, feature scope, user flow, information architecture, interaction model, states, acceptance criteria, usability, or cognitive-cost choices are unclear, route to `$noootwo-product` first.

Keep the default path light:

- For small polish that preserves the current UI direction, inspect the current UI and existing `.noootwo/system.md` or `.noootwo/design-tokens.md` only when present.
- Do not bootstrap or fill the whole `.noootwo/` harness for local spacing, typography, hierarchy, or copy polish.
- For new UI structure, new hierarchy, redesign, design-system work, or implementation-bound handoff, read the relevant `.noootwo/` files and follow `$noootwo-design`.

For non-trivial design work, route by task structure. If multiple reasonable visual directions exist, present options and stop until the user chooses or explicitly delegates. If the task is implementation-bound, do not edit UI files before the approved design spec and implementation plan exist.

For non-quick UI work, carry the Product-to-Design Handoff when available and declare the Design Read before choosing a look.
For high-character, niche, premium, selected, or previously rejected style work, record Style Evidence Check before trusting style prose.

Do not claim `ready` without `.noootwo/review.md` and artifact/screenshot/preview evidence. If the artifact has layout, responsive, typography, or generic-drift defects, return to the earlier fixing stage instead of calling it polished.

Keep detailed Noootwo Design workflow rules inside the `$noootwo-design` skill; do not duplicate them here.
