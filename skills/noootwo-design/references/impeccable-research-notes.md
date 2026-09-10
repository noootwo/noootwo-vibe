# Impeccable 2026 Mechanism Research

Recorded 2026-09 after a fresh pass over upstream `pbakaus/impeccable` (skill v4.3.1 / CLI 4.1.0, https://github.com/pbakaus/impeccable). Use this note when updating Noootwo Design's workflow, review gates, scripts, or public design-quality claims. It explains why that skill feels stronger than the prompt-only `.impeccable.md` version we borrowed from earlier (see `impeccable-style-details.md` for the distilled craft rules).

## What Changed Upstream

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

## Why It Reads Stronger

- Quality checks are **measurable and repeatable** instead of depending on whether a reviewer happens to notice an AI tell.
- **Prevention happens at edit time**, not only in review.
- The guidance is **specific and opinionated**: absolute bans (eyebrow above every heading, gradient text, cards-as-lazy-container, system display face, emoji/unicode icons) remove the decisions that converge on AI-generated output.
- **Cost is bounded**: batched verification and at-most-one confirm round cap how much review can burn.
- **Review is separated from generation**, reducing self-certification bias.

## Mechanisms To Borrow (not wording or dependencies)

1. **Enumerated deterministic anti-slop scan**
   Extend `scripts/check_visual_gates.py` (already Playwright-based) with a small named rule set: overused fonts, gradient text, AI palette, cream/beige default, nested cards, monotonous spacing, bounce/elastic easing, pulsing dots, icon-tile stacks, hero-eyebrow chips, kicker-above-heading, numbered section labels, hard offset shadows, system display face, emoji-only icons, dark glow/radial halo, side-tab borders. Run it as evidence before `ready`; treat findings as advisory until confirmed by screenshot/DOM review. This converts `review-gates.md` flags into reproducible findings.
2. **Enforce durable truth split**
   We already have `.noootwo/product-facts.md`, `system.md`, `design-tokens.md`, briefs, and surfaces. The discipline to borrow: visual contracts must be derived from product facts + existing system evidence; no aesthetic decisions are inferred inside the design contract without a recorded evidence path. `noootwo_status.py` should report missing or stale product-facts as a gate.
3. **Craft floor with absolute bans**
   Keep `anti-slop.md` and `review-gates.md`; make sure the force-return rules include new absolute bans that are hard to miss: no eyebrow/kicker above every heading, no numbered section markers as decoration, no hard offset shadows unless the world is truly neobrutalist, no system display face for an own-world page, no emoji/unicode glyphs standing in for icons, no cream/beige default surface, no gradient text. Add the cheap "built vs assembled" check: theme the browser surfaces the model usually skips (text selection, caret, custom scrollbars, focus ring, underline offset, tabular numerals).
4. **Bounded verification loop**
   In `review-rubric.md` loop rules, prefer one batched inspection (desktop + mobile on web, shipped device classes on native) followed by one fix batch and at most one confirm round. Do not spend polish loops on a direction that needs a structural pivot.
5. **Separated final reviewer**
   Prefer final review from a reviewer that does not inherit the generator's framing when the harness supports a fresh agent. Without one, step fully out of the build context before evaluating and disclose substitution in one line at finish. The generator never self-certifies `ready`.
6. **Drift, reported not silently repaired**
   `noootwo_status.py` should flag when `.noootwo/design-tokens.md`, active spec, or system file is stale against the rendered artifact. Report it; do not repair as a side effect of an unrelated design task unless the user asks.

## What We Are NOT Borrowing

- The Rust engine, `npx` shim, provider-native finder, live browser variant server, or hook manifests. Adding those would make Noootwo Design heavy and harness-specific.
- Impeccable's command vocabulary, site styling, brand voice, or leaked prompt wording.
- Any dependency that makes `quick` mode require a toolchain. The deterministic scan stays an optional production/review tool; quick polish still works from existing evidence.

## Risks And Counterexamples

- Over-structuring small tasks increases cost. Keep `quick` free of any new scan requirement.
- Static scans can false-positive on deliberate choices (brand font, dark mode, editorial marquee). Findings must be confirmed in artifact review before they can block `ready`.
- Requiring subagents or Playwright would break quick/non-interactive flows; treat these as optional evidence, never a mandatory gate.
- Don't let "deterministic findings exist" replace visual judgment: a clean scan is evidence, not proof of design quality.

## Cost Boundary

- `quick`: no scan, no new files.
- `standard`: use the enumerated gates as a checklist in the artifact review; batched verification applies.
- `deep` / `production`: may run the deterministic scan (when tooling is available), consume findings as evidence, and record drift checks.
- `review`: scans are evidence, never sole authority.

## Verification Plan

- A Noootwo eval scenario should include a "generic slop" artifact that trips at least two enumerated gates; the review must cite both finding and confirmed screenshot evidence before `ready`.
- A "wise deviation" scenario (e.g., deliberate dark-glow brand, intentional Inter brand font) must not be blocked without artifact evidence.
- After updating scripts or gates, run the workspace validator and the readiness/eval scripts, and record the result in `docs/status.md` if the change is user-facing.

## Source Notes

- Reviewed: upstream `README.md`, `AGENTS.md`, `skill/SKILL.src.md`, `skill/reference/craft-floor.md`, `skill/reference/init.md`, `skill/reference/audit.md`, `skill/reference/hooks.md`, `PRODUCT.md`, `DESIGN.md`, and `crates/foundation/src/registry.rs` (rule list). Access: GitHub clone, no access limitations.
- Evidence level: official upstream source with running artifacts (detector, CLI, extension, tests).
- Boundary: borrowed mechanisms (repeatable checks, bounded loops, separated reviewer, durable truth split, drift reporting) were extracted; no commands, engine, wording, or styling were copied.
