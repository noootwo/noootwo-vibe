# noootwo-design Releases

## v0.10.0

- Rewrote skill triggers with concrete UI verbs/nouns and explicit cross-routing back to Product and Workflow.
- Added bounded verification to review rules: build fully, one batched inspection round, one fix batch, at most one confirm round.
- Added separated final review: prefer a fresh reviewer that does not inherit the generator's framing; the generator never self-certifies `ready`.
- Added hard bans and a browser-surfaces check to review gates (eyebrow/kicker, numbered section markers, gradient text, hard offset shadows, system display face, emoji icons, cream/beige default, zero-blur halo).
- Recorded the impeccable 2026 research note as the evidence basis for these mechanisms; deterministic scan scripts deferred.


## v0.9.1

- Routed unresolved real-user, main-path, state, acceptance, audience, or use-context decisions back to `noootwo-product` Decision Interview before UI implementation.
- Clarified that Design consumes a ready Product-to-Design Handoff and keeps visual taste/brand decisions in directions or Style Evidence Check after product path clarity.
- Preserved quick polish and existing design quality gates without adding a default interview to every UI task.

## v0.9.0

- Added Style Evidence Check as a targeted high-risk layer for premium, niche, unusual, selected, or previously rejected style work.
- Folded style evidence into existing discovery, direction exploration, detail translation, artifact review, `.noootwo/` templates, readiness validation, and explicit eval prompts instead of adding a parallel workflow.
- Added review fields for style understanding fit and product comprehension fit, while keeping quick polish exempt from full harness cost.
- Narrowed the trigger metadata and entrypoint reference map so ordinary UI work does not load the full deep-mode reference set.
- Changed direction exploration from a standard/deep default into a risk-triggered step for unresolved style/structure, full redesign, user-requested exploration, or strong style rejection.
- Added `visual-direction-implemented-as-default-ui` as an opt-in artifact eval scenario; high-risk style scenarios remain outside default `--scenario all`.

## v0.8.0

- Shortened `SKILL.md` from 218 lines to a compact entrypoint focused on routing, hard stops, Design Read, Design Contract, Artifact Review, anti-slop rules, and reference routing.
- Added `references/design-read-and-contract.md` with Noootwo's stack-neutral Design Read, variance/motion/density dials, semantic token contract, anti-slop translation, and micro-detail checks.
- Updated `.noootwo/` harness templates to carry Product-to-Design Handoff, Design Read, Design Contract, and Artifact Review fields.
- Added design eval prompts for missing Design Read, generic shadcn/default UI, and pretty drafts without implementation-ready contracts.

## v0.7.0

- Narrowed `noootwo-design` to UI, visual systems, frontend execution, artifact review, and handoff after product path clarity.
- Added explicit route-back behavior to `noootwo-product` when feature scope, user flow, IA, interaction model, states, acceptance criteria, usability, or cognitive-cost decisions are unresolved.
- Updated design cost and AGENTS guidance without increasing quick-mode `.noootwo` harness requirements.

## v0.6.0

- Lowered default quick-mode friction: small polish now reads current UI and existing system/tokens when present, without bootstrapping or completing the full `.noootwo/` harness.
- Clarified that readiness and artifact eval scripts are delivery/handoff validation tools, not entry requirements for every UI task.
- Shortened the project `AGENTS.md` snippet and OpenAI prompt so non-trivial gates remain available without making local UI polish feel like a full design-system adoption.

## v0.5.0

- Added `references/color-system-calibration.md` as an on-demand lens for brand-aware neutral temperature, shadow hue, text hierarchy, semantic color harmonization, gradient boundaries, icon/illustration token inheritance, dark mode, grayscale checks, and contrast proof.
- Connected color calibration to the design spec, `.noootwo/design-tokens.md` template, detail-translation pass, and review gates without making it a default quick-mode cost.
- Explicitly rejected absolute color rules: pure white, pure black, pure gray, platform colors, and exact brand neutrals remain valid when product context, accessibility, or artifact evidence supports them.

## v0.4.0

- Aligned `noootwo-design` version with the unified Noootwo Vibe `0.4.0` skill set.
- No design workflow, harness, or readiness-gate behavior changed in this release.

## v0.3.0

- Aligned `noootwo-design` version with the unified Noootwo Vibe `0.3.0` skill set.
- No design workflow, harness, or readiness-gate behavior changed in this release.

## v0.1.18

- Moved Noootwo Design into the `noootwo-vibe` multi-skill workspace as a self-contained child skill.
- Folded style discovery, design artifact review, and detail translation into internal Noootwo Design workflows instead of separate public skills.
