# Design Direction

Finding and comparing directions, checking style evidence, and translating references into mechanisms.


## Direction Exploration

Direction work explores materially different art directions before drafting. Use [structured-design-spec.md](system.md) so every direction can become a concrete design language, not a vibe. Use [style-evidence-check.md](direction.md) for high-character, niche, premium, user-selected, or previously rejected directions.

### When

Produce 3 directions only when the choice would materially change implementation:

- the user asks to explore, choose, theme, style, or make the UI more distinctive
- the work is a full redesign, fresh visual language, or "start over" request
- multiple plausible structures, densities, moods, or component languages fit the product
- high-character, premium, niche, unusual, selected, or previously rejected style needs evidence before implementation
- the user strongly rejects the current style as generic, not advanced, not unique, or not matching the chosen direction

Skip directions for `quick`, `review`, `extract-system`, handoff-only, explicit stay-close polish, and standard work where product path plus visual posture already make one implementation path clear.

Directions are a user-facing decision menu, not internal notes. Present the menu, recommend one direction, and wait for user selection before implementation unless the user explicitly delegates the choice.

For full redesign requests such as "redo all UI", "start over", "all design from scratch", or "do not use the current visual language", the direction menu is a hard blocking checkpoint.

### User-Facing Direction Shape

Write `.noootwo/directions.md` with:

- recommended direction and why
- full redesign trigger when relevant
- Style Evidence Check for high-character directions: style claim, visual evidence, anti-example, borrowed mechanism, implementation translation, confidence, and artifact/spike required
- user selected direction, or `not selected yet`
- user decision gate: whether a choice is required, the exact question, options, recommendation, user selection, and whether the user delegated the choice
- 3 named directions
- surface type and why the chosen source pool fits
- for each direction: source evidence, borrowed mechanism, anti-example, design-spec delta, type/color/density, component/shape language, motion thesis, artifact strategy, and mimicry risk to reject
- for each direction: must-preserve, allowed-variation, forbidden-substitution, token target, component target, and motion target

### Internal Preflight

Before drafting, confirm:

- the 3 directions differ in type, structure, density, mood, component language, and motion
- each direction has a design-spec delta: color roles, type roles, layout model, component vocabulary, motion thesis, and forbidden moves
- each direction states what must survive translation into tokens and implementation, what may vary, and what must never be substituted
- product UI directions use product/design-system evidence, while campaign UI directions may use more experimental art-direction evidence
- each direction names how it becomes reviewable
- each direction includes at least one openable case link the user can inspect
- high-character directions have visual evidence or are explicitly marked low confidence with a spike requirement
- each direction has stack translation
- each direction defines font logic, scale, weight roles, line-height, letter-spacing, and mobile display cap
- no direction is only a palette swap
- no direction defaults to generic SaaS, shadcn-card-wall, or Flutter/native defaults without product reason
- no influence-led direction imitates a designer/artist signature style instead of translating mechanisms
- if options are materially different, `User selected option` or `User delegated choice to agent` is recorded before drafting

If 3 directions share the same opening structure or component skeleton, redo exploration.

If a direction cannot be summarized as implementation rules another agent could follow, return to directions before drafting.

If a direction's evidence and claimed style point to different mechanisms, return to style discovery before writing the spec.

If a required decision is unresolved, do not create artifacts, edit Flutter routes, write handoff, or enter production.


## Style Evidence Check

Use this when a requested direction is high-character, premium, niche, unusual, user-selected, or previously rejected. The goal is to avoid confident style prose that the agent cannot actually draw or implement.

This is not a new full workflow. It tightens `agentic-style-discovery.md`, `direction-exploration.md`, `detail-translation-pass.md`, and `review-rubric.md`.

### Check Shape

```markdown
Style Evidence Check
- Style claim:
- Visual evidence:
- Anti-example:
- Borrowed mechanism:
- Implementation translation:
- Confidence: high | medium | low
- Artifact/spike required:
```

### Field Rules

- `Style claim`: the user's taste target in concrete terms, not only adjectives.
- `Visual evidence`: real screenshot, reference case, visual sample, user-provided image, or spike artifact. If none exists, say `missing`.
- `Anti-example`: a visible pattern that would prove the agent misunderstood the direction.
- `Borrowed mechanism`: transferable layout, type, material, density, interaction, or state behavior.
- `Implementation translation`: how that mechanism becomes tokens, components, spacing, motion, native controls, or artifact structure.
- `Confidence`: `low` unless evidence and translation are both clear.
- `Artifact/spike required`: what visual proof must exist before `ready`.

### Hard Rules

- Do not turn "premium", "niche", "unique", or "advanced" into a confident design spec without visual evidence.
- If evidence contradicts the proposed spec, return to style discovery instead of polishing implementation.
- If only one weak reference exists, mark low confidence and require a spike or artifact review.
- For product UI, product-flow evidence outranks pure art-direction shots.
- For campaign or editorial surfaces, visual novelty can weigh more, but implementation translation still must be named.


## Style Calibration

Use this before direction exploration for standard or deep UI work. Keep it short.

### Purpose

Style calibration turns vague taste requests into a compact taste contract. It should help the user choose a direction, not become a long questionnaire.

### When To Run

Run for:

- new UI, major redesign, brand-heavy work, high-end or niche UI
- Claude Design-like requests
- Flutter/native/app work where stack-native craft matters
- tasks with taste adjectives but no visual references

Skip for `quick`, `review`, `extract-system`, `handoff-only`, or explicit "stay close" work.

### Output

Write `.noootwo/style-calibration.md` with:

- one style thesis
- 5-7 dials: novelty, brand safety, density, typography contrast, motion presence, surface/material character, composition risk
- 1-2 reference mechanisms from [verified-ui-casebook.md](evidence.md) when useful, with case links the user can open
- one recommended calibration
- what this rules out

### Defaults

- Novelty: 4/5 for deep, 3/5 for standard
- Brand safety: 3/5 unless the user asks for conservative work
- Typography contrast: deliberate; avoid inherited system stacks unless confirmed
- Motion: purposeful; never garnish
- Composition: avoid default centered hero plus card grid

### Direction Link

Each direction must state:

- how it follows the calibration
- which dial it pushes hardest
- which generic pattern the calibration rules out

If all 3 directions could use the same generic SaaS layout, redo calibration.


## Taste Fit Matrix

Use this to convert "advanced", "niche", "minimal", "fashionable", and "premium" into reviewable criteria.

Score each dimension from 1-5.

### Dimensions

- `distinctive`: structure and component language avoid category templates.
- `niche`: the design has a specific subculture, industry, medium, or behavior source without cosplay.
- `practical`: the core user task is understandable within 3 seconds.
- `minimal`: every visible layer contributes to task, hierarchy, state, or brand memory.
- `efficient`: information density, operation path, and state feedback make work faster.
- `premium`: proportion, weight, spacing, material, type, and color count feel controlled.
- `fashionable`: current visual signals are present without overusing trend skins.
- `credible`: the target stack can implement the direction without fake screenshots or impossible motion.

### Failure Modes

- `AI gradient SaaS`: purple/blue/cyan gradient, large rounded cards, centered hero, generic metrics.
- `styled but crude`: has a strong look, but weight, spacing, type, or responsive behavior is poor.
- `unique but impractical`: visually different, but the primary task is slower or unclear.
- `minimal but empty`: lots of space and little utility, with no strong proportion or function.
- `fashionable but unusable`: follows visual trends at the expense of reading, actions, or states.
- `efficient but generic`: works, but looks like any default UI kit surface.
- `premium cosplay`: luxury cues pasted onto a product that needs clarity or speed.
- `mobile app posterization`: app screen reads like a static poster or dribbble shot, not a usable mobile product.
- `visual metaphor cosplay`: product words or metaphors drive surface styling without improving the task.
- `chip/status overload`: too many pills, badges, status labels, and icon blocks compete for attention.

### Gate

- Deep mode directions should average at least 4 across `distinctive`, `practical`, `premium`, and `credible` before artifact spike.
- Product UI cannot pass if `practical` or `credible` is below 3.
- A direction with high `fashionable` but low `efficient` should be limited to campaign or editorial surfaces.


## Mechanism Library

Use this to convert references into reusable design mechanisms. Mechanisms are not visual skins; they describe how structure, typography, motion, and data work together.

### How To Use

- Pick mechanisms only after source discovery.
- Record which source inspired the mechanism and what surface styling is rejected.
- Combine at most 2 core mechanisms in one direction unless the surface is campaign-heavy.
- Mechanism names are not visual direction. Reject names like cabinet, drawer, ledger, tray, rail, fresh, or mist when they do not make the product task faster or clearer.
- Do not turn mechanisms into large rounded card stacks, decorative chips, or metaphor cosplay.
- Add successful mechanisms back to `.noootwo/reference-board.md` and `.noootwo/design-tokens.md` after review.

### Seed Mechanisms

#### Exception-First Ledger

- Best for: dashboards, ops, finance, monitoring, QA, logistics.
- Move: show exceptions, risk, and next actions before decorative aggregate metrics.
- UI primitives: dense rows, severity rail, aligned numbers, compact filters, state chips with clear semantics.
- Avoid: fake charts, huge vanity KPIs, gradient metric cards.
- Implementation: tables or virtualized lists, tabular numbers, sticky action rail, keyboardable row actions.
- Failure signal: user cannot tell what needs action in 3 seconds.

#### Quiet Utility Rows

- Best for: settings, admin tools, internal workflows, configuration.
- Move: make the interface feel expensive through alignment, restraint, and fast scan paths.
- UI primitives: ruled rows, tight labels, calm toggles, grouped sections, low-contrast surfaces.
- Avoid: every setting in a card, oversized toggles, decorative icons.
- Implementation: semantic form controls, section anchors, progressive disclosure, responsive row stacking.
- Failure signal: sparse but empty, or dense but visually noisy.

#### Material Campaign Plate

- Best for: launch pages, editorial campaigns, brand-heavy product moments.
- Move: use a tactile plate, image treatment, or material surface as the memorable object.
- UI primitives: oversized type, cropped imagery, shallow depth, controlled texture, one accent motion.
- Avoid: purple-blue gradient hero, glass cards, stock 3D blobs.
- Implementation: CSS masks, image duotone, subtle grain, scroll-linked reveal only if it serves the story.
- Failure signal: material effect becomes decoration without product proof.

#### Asymmetric Editorial Rail

- Best for: high-character content pages, reports, product narratives, founder/editorial surfaces.
- Move: separate navigation, annotation, and proof into an asymmetric rail instead of a centered hero stack.
- UI primitives: vertical rail, strong measure, annotations, pull quotes, staggered proof modules.
- Avoid: serif + mono + status dots as a generic Claude-ish skin.
- Implementation: CSS grid areas, sticky rail, responsive reflow into top index.
- Failure signal: mobile rail collapses into clutter or hides critical navigation.

#### Dense Command Surface

- Best for: devtools, AI workbenches, data tools, creative tools, operator consoles.
- Move: foreground command, selection, and feedback loops instead of marketing copy.
- UI primitives: command bar, split panes, object list, inspector, timeline, inline state.
- Avoid: fake terminal cosplay, low-contrast dark mode, decorative code blocks.
- Implementation: resizable panes, keyboard shortcuts, focus states, empty/loading/error states.
- Failure signal: looks advanced but lacks an action path.


## Reference Board

Use this for `deep` mode and high-end, niche, rare, brand-heavy, or Claude Design-like work. Build it from [agentic-style-discovery.md](research.md), not from generic moodboard collection.

### Core Rule

Deep mode must collect or explicitly declare the absence of 3-5 real source mechanisms before generating a high-character direction.

### Reference Shape

For each reference, record:

- Source and evidence type
- Evidence level from [agentic-style-discovery.md](research.md)
- Mechanism to borrow
- Do-not-copy boundary for influence sources
- Design-system translation: color roles, type roles, layout model, component vocabulary, motion thesis, or data/state grammar
- UI primitive mapping: grid, rail, surface, type scale, state model, motion primitive, data grammar, or stack-native move
- Rejected surface styling
- Preservation contract: what must survive, what may vary, and what must never be substituted

### Good Mechanisms

- Typography contrast and reading rhythm
- Spatial composition and density strategy
- Component vocabulary that differs from library defaults
- Material, texture, imagery, or background treatment
- Motion or interaction motif tied to the product job
- Data visualization grammar with real units and states
- Stack-native implementation move, such as slivers, shared transitions, canvas rendering, Rive, or GSAP timeline

### Bad References

- Aesthetic adjectives without visible examples
- Single screenshots with no reusable mechanism
- Brand styling copied from another product
- Designer/artist signature-style mimicry or "in the style of X" references
- Generic AI, SaaS, or "Claude-ish" patterns used as proof of quality
- Awwwards or Dribbble-style visual experiments used as product UX truth

### Output

Record the discovery process in `.noootwo/style-discovery.md`, the selected source mechanisms in `.noootwo/reference-board.md`, and the mechanism transfer plus preservation contract in `.noootwo/directions.md`.


## Style Lineages

Use these lineages when the brand needs a stronger point of view or when brand evidence is incomplete. Borrow the logic, not the decoration. For most new work, redesigns, and style-sensitive tasks, start from one of these lineages unless the current brand system already provides equally strong direction.

### Rules

- Pick one lineage per direction
- Keep the lineage aligned with the product and audience
- Use these as fallback structure, not as permission to ignore confirmed brand assets
- Prefer open or broadly available type options when naming examples
- Extend the lineage across typography, color, component language, motion, and interaction
- If you choose not to use a lineage, explain why the current brand system is already strong enough
- Treat example stacks as starting points, not defaults to repeat across every generation

### Neo Editorial

- Best for: launches, thought-leadership surfaces, product stories, and premium marketing pages
- Type logic: expressive serif accent plus restrained sans plus optional mono note
- Example stack: `Instrument Serif`, `Instrument Sans`, `IBM Plex Mono`
- Color logic: restrained base palette with one deliberate editorial accent
- Density: medium with sharp contrast between compact detail and generous headline space
- Shape language: rules, columns, asymmetry, cropped imagery, restrained radius
- Component vocabulary: editorial rails, inset callouts, caption systems, split panels
- Motion: paced reveals, parallax-light transitions, restrained fades, no busy chrome
- Interaction motif: page-as-storytelling, section pivots, visual pull-quotes, evidence inserts
- Image treatment: art-directed product crops, strong negative space, editorial pacing
- Avoid: centered template heroes, card walls, soft-glow futurism

### Industrial System

- Best for: workbenches, dashboards, operational tools, and infra products
- Type logic: sturdy grotesk plus mono instrumentation
- Example stack: `Space Grotesk`, `IBM Plex Mono`
- Color logic: restrained neutrals with functional signal colors, not mood gradients
- Density: medium-high to high
- Shape language: rails, panels, hairlines, measured corners, utilitarian emphasis
- Component vocabulary: consoles, inspector panes, meters, timelines, segmented command surfaces
- Motion: state-driven transitions, instrument-like responsiveness, no ornamental flourish
- Interaction motif: inspect, compare, monitor, route, configure
- Image treatment: product evidence over decoration, diagrams over moodboards
- Avoid: floating cards, luxury gloss, glassmorphism, ornamental gradients

### Quiet Luxury Product

- Best for: premium consumer products, polished product pages, booking or commerce surfaces
- Type logic: calm sans with a disciplined serif display
- Example stack: `Manrope`, `Fraunces`
- Color logic: low-noise neutrals with one tactile accent color and material-sensitive contrast
- Density: medium, with precision rather than emptiness
- Shape language: large planes, clean seams, restrained curves, tactile material contrast
- Component vocabulary: framed showcases, layered detail panels, premium selectors, material-led CTAs
- Motion: soft but intentional easing, tactile reveals, cinematic detail transitions
- Interaction motif: browse, compare, savor, commit
- Image treatment: high-trust photography, careful cropping, low-noise backdrops
- Avoid: black-and-glow futurism, oversized pills, faux-minimal emptiness

### Precise Minimalism

- Best for: settings, utilities, developer tools, or calm product surfaces that need restraint
- Type logic: neutral sans with a secondary contrast move in case, width, or mono accent
- Example stack: `Public Sans`, `IBM Plex Mono`
- Color logic: calm neutrals with sparing semantic accents
- Density: medium-high, compact but readable
- Shape language: strict alignment, light separators, subtle radius, almost no ornamental chrome
- Component vocabulary: structured lists, utility panels, dense forms, status rows
- Motion: quiet state transitions, focus-led interaction, almost invisible animation
- Interaction motif: adjust, confirm, scan, complete
- Image treatment: sparse or none; rely on structure and copy
- Avoid: empty luxury space, repetitive cards, decorative gradients

### Ceremonial Launch

- Best for: campaign pages, showcases, cultural products, and moments that need theatrical framing
- Type logic: high-contrast display mixed with disciplined body text
- Example stack: `Syne`, `Source Serif 4`, `IBM Plex Mono`
- Color logic: dramatic contrast, poster-like accents, controlled theatrical color breaks
- Density: variable by section, with obvious pacing changes
- Shape language: stage-like framing, oversized type, deliberate contrast, controlled drama
- Component vocabulary: acts, scene breaks, marquee cards, framed callouts, ceremonial CTAs
- Motion: scene transitions, reveal beats, bold staging, controlled spectacle
- Interaction motif: unveil, announce, celebrate, frame
- Image treatment: poster-like crops, bold framing, episodic sections
- Avoid: default SaaS modules, fake dashboard proof, timid hierarchy

### Tone Extremes

Use one tone extreme together with a lineage so each direction has a strong emotional posture, not just a structural label.

- `brutally minimal`: severe restraint, ruthless hierarchy, almost no ornament, precision over comfort
- `maximalist chaos`: layered density, collage energy, controlled overload, deliberate visual tension
- `retro-futuristic`: nostalgic forms with speculative details, optimistic drama, stylized contrast
- `organic/natural`: softer geometry, tactile pacing, living textures, material warmth
- `luxury/refined`: deliberate polish, slow rhythm, premium typography, controlled detail
- `editorial`: page-as-storytelling, strong pacing, art-directed crops, hierarchy through typography
- `brutalist/raw`: rough edges, blunt contrast, structural honesty, unapologetic weight
- `art deco/geometric`: decorative geometry, formal symmetry breaks, ornamental precision
- `industrial/utilitarian`: measurable clarity, mechanical logic, state-driven motion, practical density

### Pairing Rule

- Each direction should usually be `1 lineage + 1 tone extreme`
- Only omit a lineage or tone extreme when the brand system already supplies an equally strong alternative
