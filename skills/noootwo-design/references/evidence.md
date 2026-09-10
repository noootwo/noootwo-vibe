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


## Impeccable Style Details

Use this as craft guidance distilled from current impeccable design skills. Borrow the mechanisms, not the dependency or wording. For the 2026 mechanism-level pass (durable truth split, deterministic detectors, bounded verification, separated reviewer), read [evidence](evidence.md).

### Typography

- Do not default to Inter, Roboto, Arial, Open Sans, or system fonts when the brief asks for personality.
- Pair with real contrast: serif/sans, wide/condensed, humanist/geometric, editorial/body, or restrained mono accent.
- Use a small, explicit type scale. App UI needs predictable `rem` roles; campaign UI can use fluid display sizes.
- Body text should normally be at least 16px on web.
- Use `tabular-nums` for aligned values and operational data.
- Do not set an own-world display voice in a system face (Impact, Arial Black, platform sans); source or self-host a face whose character matches the approved lettering.

### Color

- Avoid pure `#000` and `#fff` as the main palette unless a specific brand system requires them.
- Tint neutrals toward the chosen brand mood.
- Prefer OKLCH or `color-mix()` where web stack support allows.
- Do not use the AI palette: cyan/purple/blue gradients, neon-on-dark, glow accents, or gradient text as the main idea.
- Dominant color plus sharp accent is usually stronger than evenly spread decorative color.
- Do not reach for cream/beige as the default "tasteful" AI surface; choose a background from a deliberate palette.

### Composition And Space

- Create rhythm with tight related groups and generous separation between groups.
- Do not apply the same padding everywhere.
- Use asymmetry, rails, rules, and structured density when they clarify hierarchy.
- Avoid identical card grids, nested cards, centered hero templates, and card walls as a default structure.
- A sophisticated layout can be dense if the data, labels, and actions are organized.
- No eyebrow/kicker above every heading, and no decorative numbered section markers unless the sequence carries information.

### Motion

- Motion should explain state, continuity, emphasis, or identity.
- One well-orchestrated transition is better than many generic fade-ups.
- Avoid bounce/elastic easing unless the product explicitly wants playful physicality.
- Do not put motion on top of a generic layout and call it premium.

### Detail And Hard-Edge Refusals

- No gradient text; emphasis comes from weight or size.
- No zero-blur hard offset shadows unless the world is truly neobrutalist.
- No emoji/unicode glyphs standing in for an icon system.
- No glass/blur decoration without a specific effect.
- Theme the browser surfaces models usually skip: text selection, caret, custom scrollbars, focus rings, underline offsets, and tabular numerals.

### Review

Ask whether the interface would be instantly recognized as AI-generated. If yes, return to directions or artifact instead of polishing. Confirm detector-style findings against a rendered screenshot before they block `ready`.


## Impeccable Research Notes

Recorded 2026-09 after a fresh pass over upstream `pbakaus/impeccable` (skill v4.3.1 / CLI 4.1.0, https://github.com/pbakaus/impeccable). Use this note when updating Noootwo Design's workflow, review gates, scripts, or public design-quality claims. It explains why that skill feels stronger than the prompt-only `.impeccable.md` version we borrowed from earlier (see `evidence.md` for the distilled craft rules).

### What Changed Upstream

Impeccable stopped being "one design-context file plus a few commands" and became a source-first system:

- **Durable truth split.** One-time `init` writes `PRODUCT.md` (users, jobs, constraints, evidence, platform, voice) and keeps visual worlds in `DESIGN.md` plus per-surface briefs. Product truth is not confused with surface decoration.
- **Engine + context loader.** A small self-contained binary (`impeccable context`) resolves and loads `PRODUCT.md`, `DESIGN.md`, the matching surface brief, and native guidance at the start of each session. The skill references that loaded context instead of re-deriving it.
- **Deterministic detectors.** 61 named rules (side-tab, overused-font, ai-color-palette, cream-palette, nested-cards, gradient-text, hero-eyebrow-chip, kicker-above-heading, numbered-section-labels, hard offset shadows, etc.) run from a Rust CLI, browser extension, and in-editor hook with no LLM and no API key. Findings are reproducible and CI-able.
- **Edit-time hook.** The design hook auto-runs the detector after UI file edits and surfaces findings, so mechanical mistakes are caught while editing, not only in an end-of-turn review.
- **Live browser mode.** Visual variants are iterated in a real browser session instead of only from screenshots.
- **Craft floor as a separate reference.** A `craft-floor.md` is loaded only when about to edit UI. It carries absolute bans and shipping reflexes (contrast, depth, spacing, type, motion, states, browser surfaces).
- **Bounded verification.** "Build fully, inspect once with a batched round (desktop and mobile together), fix everything in one batch, confirm with at most one more round, stop." Review is batched rather than an endless polish loop.
- **Separated finish reviewer.** Final review uses a reviewer that does not inherit the generator's framing/transcript when a subagent is available; the generator cannot self-certify.
- **Doctor / drift.** `doctor` reports drift between recorded artifacts and what the current version expects, without repairing it as a side effect.

### Why It Reads Stronger

- Quality checks are **measurable and repeatable** instead of depending on whether a reviewer happens to notice an AI tell.
- **Prevention happens at edit time**, not only in review.
- The guidance is **specific and opinionated**: absolute bans (eyebrow above every heading, gradient text, cards-as-lazy-container, system display face, emoji/unicode icons) remove the decisions that converge on AI-generated output.
- **Cost is bounded**: batched verification and at-most-one confirm round cap how much review can burn.
- **Review is separated from generation**, reducing self-certification bias.

### Mechanisms To Borrow (not wording or dependencies)

1. **Enumerated deterministic anti-slop scan**
   Extend `scripts/check_visual_gates.py` (already Playwright-based) with a small named rule set: overused fonts, gradient text, AI palette, cream/beige default, nested cards, monotonous spacing, bounce/elastic easing, pulsing dots, icon-tile stacks, hero-eyebrow chips, kicker-above-heading, numbered section labels, hard offset shadows, system display face, emoji-only icons, dark glow/radial halo, side-tab borders. Run it as evidence before `ready`; treat findings as advisory until confirmed by screenshot/DOM review. This converts `review.md` flags into reproducible findings.
2. **Enforce durable truth split**
   We already have `.noootwo/product-facts.md`, `system.md`, `design-tokens.md`, briefs, and surfaces. The discipline to borrow: visual contracts must be derived from product facts + existing system evidence; no aesthetic decisions are inferred inside the design contract without a recorded evidence path. `noootwo_status.py` should report missing or stale product-facts as a gate.
3. **Craft floor with absolute bans**
   Keep `craft.md` and `review.md`; make sure the force-return rules include new absolute bans that are hard to miss: no eyebrow/kicker above every heading, no numbered section markers as decoration, no hard offset shadows unless the world is truly neobrutalist, no system display face for an own-world page, no emoji/unicode glyphs standing in for icons, no cream/beige default surface, no gradient text. Add the cheap "built vs assembled" check: theme the browser surfaces the model usually skips (text selection, caret, custom scrollbars, focus ring, underline offset, tabular numerals).
4. **Bounded verification loop**
   In `review.md` loop rules, prefer one batched inspection (desktop + mobile on web, shipped device classes on native) followed by one fix batch and at most one confirm round. Do not spend polish loops on a direction that needs a structural pivot.
5. **Separated final reviewer**
   Prefer final review from a reviewer that does not inherit the generator's framing when the harness supports a fresh agent. Without one, step fully out of the build context before evaluating and disclose substitution in one line at finish. The generator never self-certifies `ready`.
6. **Drift, reported not silently repaired**
   `noootwo_status.py` should flag when `.noootwo/design-tokens.md`, active spec, or system file is stale against the rendered artifact. Report it; do not repair as a side effect of an unrelated design task unless the user asks.

### What We Are NOT Borrowing

- The Rust engine, `npx` shim, provider-native finder, live browser variant server, or hook manifests. Adding those would make Noootwo Design heavy and harness-specific.
- Impeccable's command vocabulary, site styling, brand voice, or leaked prompt wording.
- Any dependency that makes `quick` mode require a toolchain. The deterministic scan stays an optional production/review tool; quick polish still works from existing evidence.

### Risks And Counterexamples

- Over-structuring small tasks increases cost. Keep `quick` free of any new scan requirement.
- Static scans can false-positive on deliberate choices (brand font, dark mode, editorial marquee). Findings must be confirmed in artifact review before they can block `ready`.
- Requiring subagents or Playwright would break quick/non-interactive flows; treat these as optional evidence, never a mandatory gate.
- Don't let "deterministic findings exist" replace visual judgment: a clean scan is evidence, not proof of design quality.

### Cost Boundary

- `quick`: no scan, no new files.
- `standard`: use the enumerated gates as a checklist in the artifact review; batched verification applies.
- `deep` / `production`: may run the deterministic scan (when tooling is available), consume findings as evidence, and record drift checks.
- `review`: scans are evidence, never sole authority.

### Verification Plan

- A Noootwo eval scenario should include a "generic slop" artifact that trips at least two enumerated gates; the review must cite both finding and confirmed screenshot evidence before `ready`.
- A "wise deviation" scenario (e.g., deliberate dark-glow brand, intentional Inter brand font) must not be blocked without artifact evidence.
- After updating scripts or gates, run the workspace validator and the readiness/eval scripts, and record the result in `docs/status.md` if the change is user-facing.

### Source Notes

- Reviewed: upstream `README.md`, `AGENTS.md`, `skill/SKILL.src.md`, `skill/reference/craft-floor.md`, `skill/reference/init.md`, `skill/reference/audit.md`, `skill/reference/hooks.md`, `PRODUCT.md`, `DESIGN.md`, and `crates/foundation/src/registry.rs` (rule list). Access: GitHub clone, no access limitations.
- Evidence level: official upstream source with running artifacts (detector, CLI, extension, tests).
- Boundary: borrowed mechanisms (repeatable checks, bounded loops, separated reviewer, durable truth split, drift reporting) were extracted; no commands, engine, wording, or styling were copied.
