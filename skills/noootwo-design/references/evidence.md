# Design Evidence

Verified cases and distilled craft rules from reference design skills.


## Verified Ui Casebook

Use this reference for evidence-backed patterns. Borrow the mechanism, not the surface decoration.

### Case Selection Rules

- Prefer official docs, public repositories, credible hands-on writeups, or posts with visible artifacts.
- A case is useful only if it reveals a repeatable mechanism: design-system setup, visual reference use, code-native artifact, screenshot review, motion primitive, or stack-native component vocabulary.
- Do not copy brand styling, layout, artwork, or proprietary product language.

### Claude Design Official Flow

- Evidence: Anthropic launch and help-center material describe design system setup from codebase, design files, screenshots, decks, brand assets, and iteration on first versions.
- Source links: https://www.anthropic.com/news/claude-design-anthropic-labs and https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design
- Mechanism to borrow: durable system memory, first artifact, conversational iteration, inline/direct editing, and structured handoff.
- Risk to avoid: treating generated rules as brand truth when real product evidence exists.

### Anthropic Harness Engineering

- Evidence: Anthropic's design harness writeup describes generator/evaluator separation, design and originality as high-value criteria, and visual inspection through browser tooling.
- Source link: https://www.anthropic.com/engineering/harness-design-long-running-apps
- Mechanism to borrow: independent evaluator, screenshot/live artifact review, explicit `refine` and `pivot` decisions, and repeated loops when the direction is promising.
- Risk to avoid: loops that only rewrite prose without looking at the actual artifact.

### Anthropic Frontend Design Skill

- Evidence: Anthropic's public skill asks for an explicit aesthetic direction, a memorable visual move, strong typography, deliberate motion, and avoidance of generic AI aesthetics.
- Source link: https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md
- Mechanism to borrow: make the aesthetic point of view concrete before implementation and reject safe default font/layout choices.
- Risk to avoid: copying the wording without requiring a real artifact or stack translation.

### Paper Plus Claude Code

- Evidence: public workflow reports show better design iteration when a visual canvas, screenshots, or drawn annotations are paired with Claude Code.
- Source links: https://x.com/felixleezd/status/2039731306612060186 and https://aifounderkit.com/ai-tools/paper-ai-design-tool/
- Mechanism to borrow: visual canvas as shared state, fast directional variants, and annotation-driven refinement.
- Risk to avoid: assuming a text-only brief can replace visible design evidence.

### Thoughtbot Design Sprint With Claude Code

- Evidence: Thoughtbot describes rapid prototyping with Claude Code inside a design sprint context, using prototypes to move from concept to decision.
- Source link: https://thoughtbot.com/blog/rapid-prototyping-with-claude-code-how-we-transformed-our-design-sprint-process
- Mechanism to borrow: prototype early, test assumptions through artifact review, and let the artifact reveal missing states and content.
- Risk to avoid: over-investing in polish before validating the core interaction and hierarchy.

### Flutter Wonderous And gskinner Work

- Evidence: `flutter-wonderous-app` and gskinner Flutter showcases demonstrate high visual fidelity, custom transitions, effects, and authored motion in Flutter.
- Source links: https://github.com/gskinnerTeam/flutter-wonderous-app and https://flutter.gskinner.com/
- Mechanism to borrow: Flutter can support premium visual systems when the design uses slivers, custom painting, rich motion, careful imagery, and stack-native layout primitives.
- Risk to avoid: defaulting to `Scaffold + AppBar + Card + ListView` and then expecting prompt adjectives to create high-end output.

### Rive Across Product Stacks

- Evidence: Rive supports interactive animation assets across Web, Flutter, iOS, Android, React, and React Native.
- Source link: https://rive.app/
- Mechanism to borrow: use authored motion assets as product identity when static components are not enough.
- Risk to avoid: treating animation as garnish on a generic layout.

### React Motion And GSAP

- Evidence: Motion for React and GSAP/ScrollTrigger provide production-grade primitives for layout transitions, gesture motion, and scroll-driven staging.
- Source links: https://motion.dev/docs/react-layout-animations and https://gsap.com/docs/v3/Plugins/ScrollTrigger/
- Mechanism to borrow: make motion part of the direction thesis: reveal, compare, unfold, inspect, stage, or transform.
- Risk to avoid: adding low-value fade/slide presets after the page already looks generic.

### SwiftUI And Jetpack Compose Native Motion

- Evidence: platform docs expose native animation and transition primitives such as matched geometry, shared elements, and adaptive Material motion.
- Source links: https://developer.android.com/develop/ui/compose/animation/shared-elements and platform animation documentation for the target Apple framework.
- Mechanism to borrow: preserve platform idioms while using native transitions, surface layering, typography, and haptics to express the art direction.
- Risk to avoid: forcing a web landing-page composition into a native app shell.

### How To Use The Casebook

- Pick 1-2 cases as mechanism references before direction exploration.
- Record the selected mechanisms in `.noootwo/brief.md` or `.noootwo/directions.md`.
- During review, check whether the implementation actually used the mechanism, not whether it superficially resembles the case.


## Claude Design Principles

Use this reference to align Noootwo Design with the public, repeatable parts of Claude Design without copying any private prompt.

### What To Copy

- Design system memory comes before task work.
- Real artifacts come before handoff prose.
- First versions exist to expose direction risk quickly.
- Evaluation is separate from generation.
- Handoff preserves naming, intent, constraints, and review evidence.

### What Not To Copy

- Do not copy leaked or unofficial prompts.
- Do not imitate a fixed Claude-looking style such as serif headline, pills, status dots, container soup, or card-heavy layouts.
- Do not treat a generated design system as a second source of truth when the real product already has code, tokens, screenshots, or brand files.
- Do not let polish hide generic structure.

### Public Signal Summary

- Anthropic's Claude Design materials emphasize codebase and asset ingestion, design-system setup, first-version generation, iteration, and handoff: https://www.anthropic.com/news/claude-design-anthropic-labs
- Anthropic's engineering writeup on design harnesses emphasizes generator/evaluator separation, high weighting for design and originality, and visual inspection with browser tooling: https://www.anthropic.com/engineering/harness-design-long-running-apps
- External workflow reports consistently show better outcomes when the model receives screenshots, annotated visual references, code-native artifacts, and repeated critique cycles.
- External critiques consistently warn about token cost, generic convergence, handoff drift, and generated design systems diverging from real product truth.

### Operating Rules

- Establish the durable system first, with source confidence for every major rule.
- Gather visual references before inventing a style when the user wants a high-end, niche, or unusually distinctive result.
- Build or specify a reviewable artifact before judging design quality.
- Prefer a quick first artifact over a perfect written description when direction risk is high.
- Evaluate the artifact as if created by another designer: inspect the result, name the weak generic moves, and return to directions or draft instead of defending it.
- Handoff only after the review gate passes.

### Source-Of-Truth Rules

- Record where every durable system rule came from: code, token file, screenshot, design file, brand guide, user statement, or inference.
- Mark confidence as `confirmed`, `inferred`, or `missing`.
- Keep experimental direction choices out of `.noootwo/system.md` unless the user promotes them into durable brand truth.
- If a generated design system conflicts with real code or screenshots, the real artifact wins.

### Generic Convergence Risks

Flag these as Claude-like convergence, even if they look polished:

- container soup with many nested rounded panels
- serif display headline plus generic sans body without product-specific reason
- pill chips, status dots, and soft cards as the main identity
- tidy but interchangeable SaaS sections
- screenshot-free review that praises cleanliness instead of lived quality
- handoff that drops component names, states, motion intent, or implementation risks


## Impeccable Craft Signals

Use this as craft guidance distilled from `pbakaus/impeccable` v4.7.0. Borrow the mechanisms, not the dependency, command vocabulary, or surface styling. For the 2026 mechanism-level pass and its evidence limits, read [Impeccable Research Notes](#impeccable-research-notes).

### Typography

- `Inter-only`, Roboto-only, Arial-only, Open Sans-only, or system-only type is an aesthetic flag when the brief asks for personality. Keep it only when brand continuity, platform convention, or rendered hierarchy makes it intentional.
- Pair with real contrast: serif/sans, wide/condensed, humanist/geometric, editorial/body, or restrained mono accent.
- Use a small, explicit type scale. App UI needs predictable `rem` roles; campaign UI can use fluid display sizes.
- Body text should normally be at least 16px on web.
- Use `tabular-nums` for aligned values and operational data.
- A system display face (Impact, Arial Black, platform sans) is a flag for an own-world voice; pass it only when the artifact shows the face belongs to the brand or medium.

### Color

- Pure `#000` and `#fff` are palette signals. Keep them when the brand, document mode, contrast need, or native platform makes them deliberate.
- Tint neutrals toward the chosen brand mood.
- Prefer OKLCH or `color-mix()` where web stack support allows.
- Cyan/purple/blue gradients, neon-on-dark, glow accents, or gradient text are flags when they carry no brand or content reason.
- Dominant color plus sharp accent is usually stronger than evenly spread decorative color.
- Cream or beige is a flag when it reads as the default "tasteful" surface; pass it when the palette and hierarchy prove intent.

### Composition And Space

- Create rhythm with tight related groups and generous separation between groups.
- Uniform padding is a rhythm flag; confirm that it flattens grouping before blocking `ready`.
- Use asymmetry, rails, rules, and structured density when they clarify hierarchy.
- Identical card grids, nested cards, centered hero templates, and card walls are convergence signals; judge the rendered structure before failing them.
- A sophisticated layout can be dense if the data, labels, and actions are organized.
- Eyebrow/kicker labels above every heading and decorative numbered section markers are aesthetic flags. Keep them when they carry real sequence, navigation, or brand meaning without weakening hierarchy.

### Motion

- Motion should explain state, continuity, emphasis, or identity.
- One well-orchestrated transition is better than many generic fade-ups.
- Bounce or elastic easing is a flag unless the artifact shows playful physicality belongs to the product.
- Motion over a generic layout is a review signal, not proof that a different layout is required.

### Detail Evidence Flags

- Gradient text is a flag when it weakens legibility or hierarchy compared with direct type treatment.
- Zero-blur colored halos and hard offset shadows are flags when they fail to communicate depth, state, or a coherent world.
- Emoji or Unicode glyphs standing in for an icon system are a flag when they break consistency, recognition, or accessibility.
- Glass or blur decoration is a flag when it has no material role.
- Theme the browser surfaces models usually skip: text selection, caret, custom scrollbars, focus rings, underline offsets, and tabular numerals.

### Review

Ask whether the interface would be instantly recognized as AI-generated. If yes, inspect why before returning to directions or artifact. A detector-style finding is only a lead; record the observed harm or the intentional use that survives review. WCAG, contrast, keyboard/touch reachability, real content and assets, state integrity, and interaction recovery remain hard gates.


## Impeccable Research Notes

Recorded 2026-10-27 against `pbakaus/impeccable` v4.7.0 (`skill-v4.7.0` and `cli-v4.7.0`, commit `aeeb3d8c30b5f95aeeb3e893b0f1a308af8fdb8f`, released 2026-10-19). The evidence is official source plus inspectable release artifacts; no independent outcome study establishes a quality gain.

### Current Mechanisms

- **Durable truth split.** Product facts, visual worlds, and per-surface briefs remain distinct; a design contract should be derived from them instead of inventing brand truth from the current screen.
- **Code-first artifact evidence.** App screens and documentation surfaces start from implementable skeletons that a reviewer can inspect, rather than from prose about the intended style.
- **Direction cards.** Candidate directions remain choices the user can see and compare. A menu is useful only when it carries enough visible structure to support the choice.
- **Familiar control grammar with one signature.** Work surfaces keep controls users already know, then use one authored mechanism to carry identity. This prevents both generic kit output and novelty that taxes the task.
- **Real work first.** Landing and product surfaces should expose actual product evidence, content, or interaction early instead of replacing it with decorative explanation.
- **Device and medium checks.** Review includes the shipped viewport or device class when reachable; a desktop DOM scan cannot prove native touch, hover, or material behavior.
- **Progressive disclosure.** On-demand guidance moves behind the current branch instead of becoming a banner-heavy permanent checklist.
- **Measured finding mechanisms.** Upstream's deterministic findings remain useful as reproducible leads. Noootwo keeps its optional advisory checks and requires artifact evidence before a finding blocks `ready`.

### Mechanisms Adopted

1. Keep the product/system/surface truth split aligned with `.noootwo/product-facts.md`, `.noootwo/system.md`, `.noootwo/design-tokens.md`, and the active brief.
2. Require code-first low-cost direction samples when a direction choice is materially unresolved.
3. Prefer familiar control grammar plus one visible authored mechanism over a whole-surface restyle with no task logic.
4. Keep one batched inspection and at most one confirm round; do not turn review into an open-ended polish loop.
5. Use a reviewer that did not generate the artifact when the harness allows it.
6. Treat repeated aesthetic findings as evidence prompts, not universal prohibitions. The flag blocks only when the rendered artifact shows damaged hierarchy, readability, brand fit, or system cohesion.

### Rejected Or Deferred

- The Rust engine, CLI, extension, hooks, provider-specific live-variant server, and command vocabulary would add a toolchain tax and a second routing surface.
- Absolute anti-pattern bans, a universal style library, and brand-specific copies are rejected. They can replace judgment with a different safe mean.
- Worst-case data, mobile-native, and animation-performance checks remain P2 until they are justified by a concrete local failure and a cheap check.

### Safety Floor

Evidence flags never waive WCAG contrast, readable hierarchy, keyboard/focus/touch reachability, real content and assets, state completeness, or recovery from empty, loading, error, permission, and success states. Intentional cream, system display type, gradient text, decorative numbering, eyebrow labels, offset shadows, colored halos, emoji icons, or Inter-only type may pass when the artifact demonstrates product or brand fit and no safety or cohesion harm.

### Evidence Boundary

- Upstream v4.7.0 is a moving target; this note records the named tags and commit above.
- The repository shows mechanisms and release practice, not an independent controlled test of UI quality.
- Noootwo must not claim a general quality improvement until the fixture and reviewer evidence in `docs/experiments/2026-10-27-upstream-adoption.md` are recorded, and even then the claim is limited to the exercised workflow and evidence gates.
