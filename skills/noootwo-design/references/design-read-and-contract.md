# Design Read And Contract

Use this when Noootwo Design needs to turn a product handoff into stable UI direction without defaulting to a generic framework look.

## Research Basis

This mechanism borrows structure, not surface style:

- Antfu Skills: short entrypoint, on-demand references, design read, explicit variance/motion/density dials, semantic utility tokens, anti-slop hygiene, and micro-interaction details.
- Anthropic Skills guidance: keep `SKILL.md` small and load supporting files only when a task needs them.
- Layers-style product design: product decisions should move from user and context toward interaction and surface, not start at screen decoration.
- Agent Skills practice: use eval prompts to catch repeated skill failures.
- Community shadcn and AI-UI feedback: component copying converges toward sameness when teams do not create tokens, state behavior, and artifact review.

Do not copy Antfu's UnoCSS taste, private prompts, brand surfaces, or library-specific output. Noootwo is stack-neutral.

## Design Read

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

## Dial Defaults

Use these as defaults, then override only with product evidence:

| Surface | Variance | Motion | Density |
| --- | --- | --- | --- |
| Operational tool, devtool, admin, dashboard | 2-4 | 1-3 | 7-9 |
| Consumer app or native task flow | 3-6 | 2-5 | 4-7 |
| Landing, campaign, portfolio, editorial | 6-9 | 4-7 | 2-5 |
| Fixed canvas or deck | 5-9 | 1-6 | depends on format |

High variance must collapse cleanly on mobile. Motion above basic hover/active must honor reduced motion. High density must still preserve hit areas, readable line-height, and state clarity.

## Semantic Token Contract

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

## Design Contract Template

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

## Anti-Slop Translation

Reject these unless the product context specifically justifies them:

- hero plus card wall as the default first screen
- unmodified shadcn-like or UI-kit default components
- framework-native starter shells, such as `Scaffold + AppBar + Card + ListView`, as the visual identity
- Inter-only or system-only typography when personality is required
- generic violet gradients, glow, glass, bokeh, decorative dots, fake dashboards, or fake-perfect metrics
- adjectives without tokens, state behavior, artifact evidence, or forbidden substitutions

## Micro-Detail Checks

Run these in production or review when the artifact is close but still feels default:

- nested radius is concentric
- icons are optically aligned and paired with labels when ambiguity exists
- technical values use tabular numbers and stable width
- long IDs/paths truncate visually but preserve full value in title or copy path
- focus, hover, pressed, disabled, loading, empty, and error states are visible enough to verify
- motion uses transform/opacity when possible and avoids `transition: all`
- compact surfaces preserve hit area and line-height
- copy is specific, not filler marketing language

## Readiness Boundary

Quick polish may only use a lightweight read and current UI evidence. Standard, deep, and production work must not proceed to implementation when the Design Read, Design Contract, or artifact/review path is missing.
