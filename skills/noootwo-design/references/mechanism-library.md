# Mechanism Library

Use this to convert references into reusable design mechanisms. Mechanisms are not visual skins; they describe how structure, typography, motion, and data work together.

## How To Use

- Pick mechanisms only after source discovery.
- Record which source inspired the mechanism and what surface styling is rejected.
- Combine at most 2 core mechanisms in one direction unless the surface is campaign-heavy.
- Mechanism names are not visual direction. Reject names like cabinet, drawer, ledger, tray, rail, fresh, or mist when they do not make the product task faster or clearer.
- Do not turn mechanisms into large rounded card stacks, decorative chips, or metaphor cosplay.
- Add successful mechanisms back to `.noootwo/reference-board.md` and `.noootwo/design-tokens.md` after review.

## Seed Mechanisms

### Exception-First Ledger

- Best for: dashboards, ops, finance, monitoring, QA, logistics.
- Move: show exceptions, risk, and next actions before decorative aggregate metrics.
- UI primitives: dense rows, severity rail, aligned numbers, compact filters, state chips with clear semantics.
- Avoid: fake charts, huge vanity KPIs, gradient metric cards.
- Implementation: tables or virtualized lists, tabular numbers, sticky action rail, keyboardable row actions.
- Failure signal: user cannot tell what needs action in 3 seconds.

### Quiet Utility Rows

- Best for: settings, admin tools, internal workflows, configuration.
- Move: make the interface feel expensive through alignment, restraint, and fast scan paths.
- UI primitives: ruled rows, tight labels, calm toggles, grouped sections, low-contrast surfaces.
- Avoid: every setting in a card, oversized toggles, decorative icons.
- Implementation: semantic form controls, section anchors, progressive disclosure, responsive row stacking.
- Failure signal: sparse but empty, or dense but visually noisy.

### Material Campaign Plate

- Best for: launch pages, editorial campaigns, brand-heavy product moments.
- Move: use a tactile plate, image treatment, or material surface as the memorable object.
- UI primitives: oversized type, cropped imagery, shallow depth, controlled texture, one accent motion.
- Avoid: purple-blue gradient hero, glass cards, stock 3D blobs.
- Implementation: CSS masks, image duotone, subtle grain, scroll-linked reveal only if it serves the story.
- Failure signal: material effect becomes decoration without product proof.

### Asymmetric Editorial Rail

- Best for: high-character content pages, reports, product narratives, founder/editorial surfaces.
- Move: separate navigation, annotation, and proof into an asymmetric rail instead of a centered hero stack.
- UI primitives: vertical rail, strong measure, annotations, pull quotes, staggered proof modules.
- Avoid: serif + mono + status dots as a generic Claude-ish skin.
- Implementation: CSS grid areas, sticky rail, responsive reflow into top index.
- Failure signal: mobile rail collapses into clutter or hides critical navigation.

### Dense Command Surface

- Best for: devtools, AI workbenches, data tools, creative tools, operator consoles.
- Move: foreground command, selection, and feedback loops instead of marketing copy.
- UI primitives: command bar, split panes, object list, inspector, timeline, inline state.
- Avoid: fake terminal cosplay, low-contrast dark mode, decorative code blocks.
- Implementation: resizable panes, keyboard shortcuts, focus states, empty/loading/error states.
- Failure signal: looks advanced but lacks an action path.
