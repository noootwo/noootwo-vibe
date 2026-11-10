# noootwo-design Releases

## v0.22.0

- Added the source-role matrix through `noootwo-research`: product evidence, platform convention, visual direction, motion mechanism, implementation resource, asset source, and research craft. A source can inform only the role it actually carries.
- Every `standard` and `deep` UI task now runs a reference audition. Standard uses 2-3 candidates, at least two roles, one inspected primary capture, and at most one narrow supplement. Deep uses 3-5 sources, one selected same-medium source, full capture and licence records, fit scoring, a reference lock, and 2-3 spikes. `quick` skips external audition; `production` uses locked references.
- Added `.noootwo/reference-board.md` as the unified standard/deep record with role, access, evidence, same-medium fit, inspected state, observed mechanism, fit, decision, rejection reason, capture, licence, landed result, verification date, copy boundary, and preservation contract. Legacy `Source N` headings remain readable.
- Added project-local `.noootwo/appearance-ledger.md` for reviewed accepted and rejected reference decisions. It is read by matching surface/audience section and never becomes global memory or a second state root.
- Added Mechanism Landing QA: every selected primary or supplement must record artifact evidence, the improved user outcome, and a `landed`, `decoration`, `swallowed`, or `missing` verdict. A non-landed mechanism blocks `ready`.
- Product UI needs a selected product-evidence source and cannot let a gallery, component demo, effect library, or asset source carry the primary direction. Native work needs a selected native or platform-specific source.
- Added asset-lane boundaries for fonts, icons, imagery, illustration, and 3D, including licence, attribution, commercial use, access, and fallback.
- Added `--reference-audition` to the readiness validator; `--deep-mode` implies it. The existing board, templates, bootstrap profiles, status output, and reference capture path are compatible with old deep records once the new fields are supplied.
- Added seven prompt contracts and standard positive/negative fixtures. They are deterministic contracts, not fresh-session behavior evidence.
- Migration: an existing project claiming `ready` or entering `deep` must add the audition fields, an inspected primary capture, a project-local appearance ledger, and mechanism-landing evidence. No bulk migration is required.

## v0.21.0

- Design Read now consumes the Product Audience Contract, and the Design Contract adds `Information exposure`: what is visible, secondary, or excluded, ordered as `outcome → decision evidence → implementation detail`.
- Artifact Review adds a `Comprehension Gate` for first-screen purpose and next action, evidence-backed user vocabulary, technical-term justification, note budget, density fit, settings stance, and error recovery.
- Added a note budget: every visible note, helper, badge, or explainer must prevent an error, explain a consequence, support recovery, or teach a term needed now; otherwise it is deleted.
- Implementation names, service or database details, framework or model names, internal IDs or flags, and design rationale stay out of the product surface unless they are the user's work object. Technical evidence remains available to technical buyers after the outcome it supports.
- `ready` now requires `Comprehension gate: pass`; the readiness validator rejects a missing or failed gate on product UI work. Consumer and first-use surfaces stay default-led; trained operational surfaces may remain dense and keyboard-first without licensing implementation jargon.
- Quick work that changes copy, notes, settings, or visible technical data now runs the same gate.
- Added three opt-in eval contracts for consumer technical noise, operations density without implementation jargon, and a failed gate blocking `ready`. They are not yet a fresh-session behavior measurement.
- Migration: completed projects that use readiness validation must record the Comprehension Gate and its evidence before claiming `ready`.

## v0.20.1

- Recorded `pbakaus/impeccable` v4.8.0 as an integration and maintenance refresh, not a new design philosophy; its only `SKILL.src.md` change at the tag is the launcher fallback reading `craft-floor.md` before a UI edit.
- Added OIL UI v0.30.0 research notes and reference-only mechanisms: design north star, one focal object and primary action, five-axis tone calibration, concrete-engine direction generation, one memory point with subtraction, optional landing/showcase image comps, and visual-spec conflict disclosure.
- Rejected or deferred mandatory image generation, universal `85:10:5` palettes, OIL UI's default single-direction replacement, required subagents, and copying its prompts, scripts, assets, plugin wrapper, or Pro workflows.
- The Return rule now resumes from the capsule and current artifacts after a handoff or compaction and reloads the design body only when design owns the next step.
- No workflow step, readiness gate, or migration changed; the release refreshes evidence and mechanism vocabulary and adds that recovery sentence.

## v0.20.0

- A materially unresolved direction choice now needs real low-cost samples before selection: three by default, or one fuller sample plus two lightweight variants when the runtime is weak.
- Direction records now carry the sample path, what it proves, and whether it was viewed. A prose-only menu cannot satisfy the choice gate.
- Deep references prefer the target medium and record `Same-medium fit`, `Artifact inspected`, and `Observed evidence`; black, broken, or unopened captures are not style evidence.
- Non-safety aesthetic patterns are now evidence-dependent flags rather than universal bans. Cream or beige, system display faces, gradient text, decorative numbering, eyebrow labels, offset shadows, colored halos, emoji icons, and Inter-only type may pass when inspected evidence shows intent and no harm.
- WCAG, contrast, readable hierarchy, keyboard and touch reachability, real content and assets, state integrity, and interaction recovery remain non-waivable safety gates.
- Extended readiness, artifact evals, harness templates, and the reference board; added a three-direction desktop fixture and deterministic negative probes. The fixture does not prove mobile, interaction, runtime, or cross-project quality.

## v0.19.2

- Added the package-wide context lifecycle and compressed the always-loaded description.
- Long visual references are now read by heading or query hit first; the design method, artifact gates, and readiness contract are unchanged.

## v0.19.1

- Fixed a real-project failure where an explicit user request for motion was silently downgraded to `craft only`, producing only a few CSS transitions while an installed Motion runtime and the recommended material options were left unused.
- Added a User Intent Gate: explicit requests for motion, animation, liveliness, fancy, a named library, or shader/material rendering default the requested scope to `add moment`. `leave simple` or `craft only` now requires the user to accept no authored motion.
- Added implementation-tool and library/material decision records to the motion contract and review. An installed or user-named runtime must be selected, replaced by a recorded equivalent, or rejected with a concrete reason.
- Added two manual evals, one artifact-eval scenario, and readiness/status coverage for explicit motion intent, zero-motion downgrades, and installed-runtime use.
- Migration: completed projects using `--motion-gate` must add `User motion intent`, `User accepted no authored motion`, `Motion trigger and implementation tool`, and `Library or material decision` to the Motion section and review.

## v0.19.0

- Replaced the implicit "add motion when the direction carries it" posture with a contextual intervention decision: `leave simple`, `craft only`, or `add moment`.
- Added product-function, frequency, task-risk, emotional, brand, platform, and performance context to the Design Read.
- Added a bounded opportunity sweep, four gates, candidate caps, and a required rejected-candidate ledger. Source research and new tools start only after a candidate survives.
- Added minimum-intervention rules so hierarchy, platform feedback, state continuity, and craft are tried before motion, shaders, sound, or haptics.
- Made `leave simple` and `craft only` valid readiness outcomes with craft-sufficiency evidence instead of forcing motion values or an authored move.
- Added conditional `add moment` requirements: one primary move, at most one support, source or platform evidence, boundary, and fallback.
- Added Shaders, Paper Shaders, and optional sensory-material boundaries. Shaders Pro is never required; all expressive materials need static or platform fallbacks.
- Added four contextual-intervention evals, three artifact-eval scenarios, and readiness validation for intervention records.
- Migration: projects using `--motion-gate`, `--deep-mode`, or `--implementation-gate` must record the intervention decision. Full motion values are now required only for `add moment`.

## v0.18.0

- Updated current references from `noootwo-review` to `noootwo-code-health`; no design behavior changed.

## v0.17.0

- Added an Interaction and Accessibility Gate to `craft.md` with web, Flutter, SwiftUI, and Compose equivalents for accessible names, keyboard paths, focus, touch targets, state without colour alone, announcements, text scale, reduced motion, and destructive actions.
- Added a Data Presentation Matrix for paths, time, numbers, status, badges, icons, and missing data.
- Added a Component State Matrix and an Asset and Performance Budget to `translate.md`, including Flutter-specific image, list, semantics, text-scale, and reduced-motion notes.
- Added screenshot and design-image intake to `design-discovery.md`, so an image source is extracted into viewport, layout, type, colour, component, state, image, motion-cue, provenance, and confidence fields before implementation.
- Extended the web-only `check_visual_gates.py` with seven advisory interface checks: missing accessible names, missing alt text, unstable image dimensions, `transition: all`, removed outlines with no focus rule, small narrow-viewport touch targets, and disabled or limited zoom. Findings never block `ready` without source, accessibility-tree, or keyboard confirmation, and Flutter, SwiftUI, and Compose use the platform gates instead.
- Added four eval scenarios: screenshot reference without extraction, accessibility and interaction gap, long content and localization, and Flutter motion and state parity.

## v0.16.0

- Added `references/motion-libraries.md`, an on-demand map from the motion register to the smallest web, Flutter, SwiftUI, or Compose tool that can carry it.
- The map records copy-in registries, runtime primitives, licence boundaries, dependency cost, maintenance state, reduced-motion fallbacks, and the domestic access path.
- `motion.md` and `translate.md` now point to the map, and `translate.md` gained the per-platform motion ladder. Quick work stays unchanged.
- Added the `library-demo-into-quiet-product` eval so a flashy registry demo cannot be pasted into a quiet product surface without the register, licence, dependency, and retuning checks.

## v0.15.0

- Durable directions, token sets, and review outcomes now hand off to `noootwo-state`; design's own `.noootwo/` working artifacts remain design-owned.

## v0.14.0

- Rewrote the motion philosophy so the still page and motion are co-equal completion criteria.
- Added Source Fidelity QA for explicit `replicate` references, and a `Reference intent` field in discovery.
- Added an optional `--probe-motion` mode to `extract_design_tokens.mjs` for stillness-ratio evidence without new dependencies.
- Sharpened the description toward reference replication and motion handfeel fixes.

## v0.13.0

- Added `references/motion.md`: four personality archetypes with real durations, curves, and overshoot; the lineage-to-archetype mapping; a signature motion identity of one curve, three durations, and one entrance pattern; an element duration table with distance scaling and enter-longer-than-exit; an easing catalog; material modifiers; the three motion layers; choreography and stagger budgets; the frequency gate; reduced motion; and a troubleshooting table.
- Motion stopped being an empty contract. `craft.md` gained a motion rubric with four hard bans, `translate.md` gained the Compose, SwiftUI, and Flutter mapping plus per-platform reduced-motion signals, and `system.md` now points at the reference values.
- Added `scripts/extract_design_tokens.mjs`: a zero-dependency extractor that drives the local Chrome over the DevTools Protocol, reads computed styles, probes interactive elements for hover deltas, and emits markdown, raw JSON, and optional W3C DTCG tokens.
- Case capture is now part of deep mode: every source lands in `.noootwo/references/<slug>/` with provenance, accessibility result, and licence; an unreachable source is recorded and the pass continues.
- Added reference lock and anti-averaging: name the build target and what must not drift, and let one reference dominate rather than averaging several.
- Harness contract: `reference-board.md` gained `Capture path` and `Landed as` per source, `style-discovery.md` gained `Capture directory` and a `Reference Lock` section, `design-tokens.md` carries a required motion contract, and `references/README.md` documents the capture directory.
- Gates: the readiness validator checks the new fields under `--deep-mode` and `--implementation-gate`, and `check_visual_gates.py` gained five advisory motion rules that need screenshot or DOM confirmation before they change a decision.
- Fixed a stale citation: the Carbon motion page is unreachable, so the motion sources now point at Material 3 motion and Apple HIG motion.
- Added a motion register — Invisible, Quiet, Present, Expressive, Theatrical — set by the surface rather than the mood, so restraint and expressiveness are both available and neither is the silent default.
- Added the motion sourcing procedure: fix the register, collect two or three examples in it, record each as trigger, moving property, duration, curve, layer relationship, and meaning, then adapt rather than paste.
- Added library selection guidance, including when CSS alone is enough and why scroll-hijacking libraries belong on marketing surfaces rather than product screens.
- Recorded `bendrape1-byte/silk-design` as a counterexample: its consistency mechanism is borrowed, its "never ship a static page" default is not.
- Added six motion and four case-capture eval scenarios.


## v0.12.0

- Moved the research method and source pools out to `noootwo-research`; the design skill now invokes it instead of carrying its own research file.
- Added `references/design-discovery.md` for what stays design-specific: surface routing, the discovery pass, influence discovery, evidence weighting for taste, fit scoring, and the `.noootwo/style-discovery.md` output contract.
- The artifact contract is unchanged: `.noootwo/style-discovery.md` and `.noootwo/reference-board.md` keep their paths and field names because the readiness, bootstrap, status, and eval scripts read them field by field.
- Added a return rule naming the layer and the owning skill for work that is not design.


## v0.11.0

- Rewrote the body as a six-step flow — size, Design Read, direction, Design Contract, build, review — each with a completion criterion.
- Cut the description from 584 to 195 characters and added the explicit return path: an unsettled product path invokes `noootwo-product`.
- Consolidated 45 reference files into 9 grouped references, each named by a pointer: intake, direction, research, system, craft, review, translate, evidence, notes.
- Carried forward the crafted review rules: bounded verification, hard bans, the browser-surfaces check, and separated final review.


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
