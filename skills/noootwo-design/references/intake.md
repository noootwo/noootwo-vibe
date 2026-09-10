# Design Intake

Reading a request, declaring the Design Read, sizing the harness, and adopting an existing project.


## Design Read And Contract

Use this when Noootwo Design needs to turn a product handoff into stable UI direction without defaulting to a generic framework look.

### Research Basis

This mechanism borrows structure, not surface style:

- Antfu Skills: short entrypoint, on-demand references, design read, explicit variance/motion/density dials, semantic utility tokens, anti-slop hygiene, and micro-interaction details.
- Anthropic Skills guidance: keep `SKILL.md` small and load supporting files only when a task needs them.
- Layers-style product design: product decisions should move from user and context toward interaction and surface, not start at screen decoration.
- Agent Skills practice: use eval prompts to catch repeated skill failures.
- Community shadcn and AI-UI feedback: component copying converges toward sameness when teams do not create tokens, state behavior, and artifact review.

Do not copy Antfu's UnoCSS taste, private prompts, brand surfaces, or library-specific output. Noootwo is stack-neutral.

### Design Read

Before non-quick UI work, declare:

```markdown
Design Read
- Surface kind:
- Audience:
- Product posture:
- Visual posture:
- Variance:
- Motion:
- Density:
- Existing system to preserve:
```

Field rules:

- `Surface kind`: operational tool, dashboard, app shell, native screen, landing page, deck, fixed canvas, live artifact, editorial, or campaign.
- `Audience`: first-time, expert, maintainer, operator, buyer, creator, student, teacher, parent, admin, or other specific role.
- `Product posture`: what the product must communicate through use: trust, speed, control, calm, scrutiny, play, status, clarity, or another task-relevant stance.
- `Visual posture`: the visual language that supports the product posture, not a fashion label.
- `Variance`: 1-10. Low means symmetric and predictable; high means asymmetric and expressive.
- `Motion`: 1-10. Low means hover/active only; high means staged or spatial motion with reduced-motion fallback.
- `Density`: 1-10. Low means airy and guided; high means compact and repeated-use friendly.
- `Existing system to preserve`: tokens, components, routes, brand assets, screenshots, or "none found".

### Dial Defaults

Use these as defaults, then override only with product evidence:

| Surface | Variance | Motion | Density |
| --- | --- | --- | --- |
| Operational tool, devtool, admin, dashboard | 2-4 | 1-3 | 7-9 |
| Consumer app or native task flow | 3-6 | 2-5 | 4-7 |
| Landing, campaign, portfolio, editorial | 6-9 | 4-7 | 2-5 |
| Fixed canvas or deck | 5-9 | 1-6 | depends on format |

High variance must collapse cleanly on mobile. Motion above basic hover/active must honor reduced motion. High density must still preserve hit areas, readable line-height, and state clarity.

### Semantic Token Contract

Express stable visual decisions as roles:

- `canvas`: base page or route background.
- `surface`: panels, sheets, cards, rails, overlays, and raised regions.
- `text`: primary, secondary, muted, disabled, inverse, numeric, and code-like text.
- `accent`: one dominant action or identity role with usage limits.
- `semantic`: success, warning, danger, info, selected, focus.
- `data`: categorical, sequential, diverging, threshold, and missing-data colors when relevant.
- `shape`: radius scale and where sharp, soft, pill, or square is allowed.
- `depth`: border, divider, shadow, material, blur, and elevation roles.
- `motion`: durations, easing, continuity, state feedback, and reduced-motion fallback.

In code, map these to the stack's native system: CSS variables, UnoCSS shortcuts, Tailwind theme tokens, Flutter ThemeExtension, SwiftUI environment values, Compose theme objects, or existing project tokens. Avoid one-off raw values when the decision should survive across surfaces.

### Design Contract Template

```markdown
Design Contract
- Structure:
- Type scale:
- Color/token roles:
- Component behavior:
- State treatment:
- Motion:
- Anti-slop risks:
- Artifact/review path:
```

Rules:

- `Structure`: name the layout model, not "modern page".
- `Type scale`: define display, title, body, label, number, and mono/annotation roles when relevant.
- `Color/token roles`: define canvas, surface, text, accent, semantic, and data roles.
- `Component behavior`: state how shell, navigation, forms, lists, cards, tables, dialogs, and actions behave.
- `State treatment`: loading, empty, error, success, permission, focus, disabled, hover, pressed, selected, offline.
- `Motion`: what motion explains and what it must not distract from.
- `Anti-slop risks`: name the likely generic fallback for this stack and product.
- `Artifact/review path`: screenshot, running page, simulator, preview URL, fixed export, deck flow, recording, or accepted blocker.

### Anti-Slop Translation

Reject these unless the product context specifically justifies them:

- hero plus card wall as the default first screen
- unmodified shadcn-like or UI-kit default components
- framework-native starter shells, such as `Scaffold + AppBar + Card + ListView`, as the visual identity
- Inter-only or system-only typography when personality is required
- generic violet gradients, glow, glass, bokeh, decorative dots, fake dashboards, or fake-perfect metrics
- adjectives without tokens, state behavior, artifact evidence, or forbidden substitutions

### Micro-Detail Checks

Run these in production or review when the artifact is close but still feels default:

- nested radius is concentric
- icons are optically aligned and paired with labels when ambiguity exists
- technical values use tabular numbers and stable width
- long IDs/paths truncate visually but preserve full value in title or copy path
- focus, hover, pressed, disabled, loading, empty, and error states are visible enough to verify
- motion uses transform/opacity when possible and avoids `transition: all`
- compact surfaces preserve hit area and line-height
- copy is specific, not filler marketing language

### Readiness Boundary

Quick polish may only use a lightweight read and current UI evidence. Standard, deep, and production work must not proceed to implementation when the Design Read, Design Contract, or artifact/review path is missing.


## Brief Expansion

Turn a short ask into a design brief before building.

### Purpose

The brief defines the problem, audience, and constraints. It does not prescribe every solution detail.

### Output Shape For `.noootwo/brief.md`

- `Status`
- `Task`
- `Audience`
- `Primary job to be done`
- `Desired outcome`
- `Surface or flow`
- `Artifact expectation`
- `Reference sources`
- `Stack constraints`
- `Allowed implementation complexity`
- `Constraints`
- `Non-goals`
- `Tone extreme`
- `Aesthetic ambition`
- `Novelty target`
- `Brand-safety tolerance`
- `Motion appetite`
- `One unforgettable thing`
- `Must feel like`
- `Must not feel like`
- `Design objectives`
- `Success signals`
- `Open questions`

### Rules

- Keep the brief strategic and implementation-light
- Separate hard constraints from preferences
- If the user asks for "better" or "more polished", translate that into explicit design objectives
- If the ask is ambiguous, the brief should expose the ambiguity instead of hiding it
- If the user does not specify style ambition, default to a strong, opinionated direction and record that assumption explicitly
- If the user does not specify a memorable move, write a provisional `one unforgettable thing` so the draft has a non-generic center of gravity
- If the user wants high-end, niche, rare, or Claude Design-like work, require visual references or select credible mechanism references from [verified-ui-casebook.md](evidence.md)
- If the target stack is Flutter, SwiftUI, Compose, React, Vue, or another app framework, record the artifact expectation before direction work begins
- If the brief contains taste adjectives but no concrete style choices, run [style-calibration.md](direction.md) before direction exploration


## Fact First

Named products, brands, versions, launches, and recent technologies are facts, not vibes.

### When To Verify

Verify first if any of these are true:

- The task mentions a specific company, product, founder, launch, campaign, or versioned tool
- The task depends on current availability, release status, pricing, or specs
- You feel tempted to say "I think", "probably", or "as far as I remember"

### Workflow

1. Search authoritative sources first: official site, official newsroom, official docs, app stores, vendor changelog
2. Confirm the current state that matters to the design task:
   - existence
   - current version or product generation
   - positioning and announced capabilities
   - canonical naming
3. Write the result into `.noootwo/product-facts.md`
4. If the facts remain ambiguous, ask the user instead of inventing a premise

### Output Shape For `.noootwo/product-facts.md`

- `Status`
- `Project or brand`
- `Verified on`
- `Sources`
- `Current facts`
- `Design implications`
- `Unknowns that still need user input`

### Rules

- Do not start moodboards or prototypes on an unverified named product
- Record dates explicitly when the task depends on "latest" or "new"
- Prefer current official wording over remembered wording


## Project Integration

Use this reference when installing Noootwo Design into a project workflow.

### Standard `AGENTS.md`

Agents commonly read a root `AGENTS.md` as project context. Integrate the short `UI/Design Workflow` guidance from `assets/AGENTS.md` into the target project's root `AGENTS.md`.

The bootstrap script creates or merges this section by default:

```bash
python scripts/bootstrap_noootwo_harness.py /path/to/project
```

Use `--skip-agents` when the caller explicitly does not want `AGENTS.md` touched.

If the project has no `AGENTS.md`, create it from `assets/AGENTS.md`.
If the project already has `AGENTS.md`, merge in only the `## UI/Design Workflow` section from `assets/AGENTS.md`. Preserve existing project instructions and avoid overwriting unrelated sections.

### Purpose

The `AGENTS.md` snippet is only a project-level pointer. It tells agents that UI-related work is led by `$noootwo-design` and that project design context lives in `.noootwo/`. Detailed workflow rules stay inside the skill.

### Integration Rules

- Do not create custom project-guide filenames for agent context.
- Prefer the root `AGENTS.md`.
- Create `AGENTS.md` when it is missing unless `--skip-agents` is used.
- Merge the `## UI/Design Workflow` section when `AGENTS.md` already exists.
- Make merging idempotent; repeated bootstrap runs must not duplicate the section.
- Do not overwrite unrelated existing project instructions.
- Keep the snippet short; do not duplicate the skill's workflow.
- Mention `$noootwo-design` explicitly in UI/UX/frontend/app design instructions.
- If Noootwo is introduced mid-project, record adoption baseline in `.noootwo/adoption.md` before broad redesign.

### Good Trigger Language

Use concrete trigger words:

- UI design
- frontend design
- visual redesign
- screenshot review
- app screen
- React, Vue, Flutter, SwiftUI, Compose
- design system
- handoff

Avoid vague language like "make it better" without saying when to call the skill.


## Stage Roles

Use these roles to keep design work from collapsing into one model inventing, implementing, and defending the same idea.

### Role Sequence

- `Context Auditor`: reads code, screenshots, tokens, `AGENTS.md`, and `.noootwo/`; records facts and gaps; does not invent style.
- `Accessibility Scout`: checks whether preferred foreign sources are reachable, selects domestic fallback sources when needed, and records access limits.
- `Source Scout`: searches active design and developer sources for relevant product, platform, and visual signals.
- `Signal Curator`: weights sources, removes low-evidence shots, and flags trend skins that do not fit the task.
- `Mechanism Extractor`: converts sources into reusable mechanisms: grid, rail, surface, type scale, state model, motion primitive, data grammar.
- `Taste Strategist`: clusters mechanisms into 2-3 visual territories with fit scores.
- `Art Director`: chooses typography, proportion, color restraint, component language, material, and motion thesis.
- `Typography & Composition Editor`: checks type scale, weight roles, line-height, letter-spacing, mobile wrapping, spacing rhythm, and composition before polish.
- `Product Path Checker`: verifies that `$noootwo-product` has clarified task path, information architecture, states, efficiency, and usability before design execution; routes back when product choices are unresolved.
- `Stack Craftsperson`: turns the direction into a React, Vue, Flutter, SwiftUI, Compose, native, or web artifact using stack-native primitives.
- `Design Director / Evaluator`: reviews the artifact only; decides `ready`, `refine`, `pivot`, or `needs artifact`.
- `Design System Steward`: promotes only reviewed decisions into tokens, components, and handoff.

### Rules

- Do not skip from user adjectives to UI generation in deep mode.
- Do not let the generator perform the final evaluation of its own artifact.
- Do not let a visual trend override product task clarity, platform craft, or accessibility.
- Do not let design define feature scope, user flow, or acceptance criteria when `$noootwo-product` should own that decision.
- If a role lacks evidence, record the gap instead of pretending confidence.
- If foreign sources are blocked, use the domestic fallback path instead of skipping research.
- If typography or responsive behavior fails, return to the relevant pass instead of polishing around the defect.

### Output Mapping

- Context Auditor writes `.noootwo/adoption.md`, `.noootwo/system.md`, or `.noootwo/brief.md`.
- Accessibility Scout, Source Scout, Signal Curator, Mechanism Extractor, and Taste Strategist write `.noootwo/style-discovery.md` and `.noootwo/reference-board.md`.
- Art Director writes `.noootwo/directions.md`.
- Typography & Composition Editor contributes typography and layout evidence to `.noootwo/review.md`.
- Evaluator writes `.noootwo/review.md`, including the return action for any `refine` decision.
- Design System Steward writes `.noootwo/design-tokens.md` and `.noootwo/handoff/`.


## Adoption Playbook

Use this when Noootwo Design is introduced into a project that already has UI work.

### Trigger

Use `adopt-project` when:

- The project has existing pages, screens, components, themes, or screenshots.
- `.noootwo/` is missing, pending, stale, or was added mid-project.
- The user asks to start using Noootwo Design in an existing React, Vue, Flutter, SwiftUI, Compose, or native app.

### Baseline Capture

Before redesigning, inspect and record:

- Existing `.noootwo/` files and target project `AGENTS.md`
- Target stack, routing, preview, Storybook, simulator, or screenshot capability
- Theme files, tokens, CSS variables, Tailwind config, Flutter `ThemeData`, SwiftUI token structs, Compose theme files, or native style resources
- Component library and recurring component vocabulary
- Current screenshots, live route, app preview, or closest visual artifact
- Surfaces that must be preserved and surfaces that may change
- First safe change that improves quality without breaking product continuity

Write the result to `.noootwo/adoption.md`.

### Preserve And Improve Boundary

- Preserve confirmed brand tokens, product-specific components, information hierarchy, and accessibility constraints.
- Improve generic fallbacks, weak typography, visual noise, missing states, and inconsistent spacing.
- Do not introduce a new art direction until baseline evidence and user intent support it.
- If the project is already in production implementation, prefer `production` after adoption rather than reopening broad exploration.

### Mode Handoff

- Use `quick` for small polish after adoption.
- Use `standard` for new surfaces that must fit the existing product.
- Use `deep` only when the user wants a stronger art direction and reference evidence is available.
- If the user wants all UI redesigned, complete adoption baseline, then trigger the full redesign checkpoint before editing implementation files.
- Use `production` when the design is already chosen and needs target-stack implementation.

### Blockers

If no artifact, screenshot, preview, or code surface can be inspected, mark adoption incomplete and do not claim the project design system is established.
