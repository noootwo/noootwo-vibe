# Design Discovery

The discovery pass that produces `.noootwo/style-discovery.md`, and the contract that file must satisfy.

Source pools, access records, and the fallback ladder belong to the `noootwo-research` skill — invoke it: read its `SKILL.md` and follow it. This file owns only what is design-specific: which surfaces need discovery, how to weight evidence for taste, how to translate influences into mechanisms, and what the artifact must contain.

## When

Run a light audition for every `standard` and `deep` UI task. `standard` uses `.noootwo/reference-board.md` with 2–3 candidates and one primary screenshot. `deep` adds the full `.noootwo/style-discovery.md` pass, 3–5 captured sources, fit scoring, and 2–3 spikes. `quick` does not source externally. `production` uses the locked references and returns to discovery only when drift or a changed surface invalidates them.

The audition is not optional for `standard`; it is the difference between selecting a reference and inheriting a model default.

## Surface routing

Classify the surface before choosing sources:

- **Dashboards, settings, workbenches, analytics, admin, devtools** — prioritise real product flows, real screenshots, design systems, data UI rules, and task evidence. Community and gallery evidence cannot decide these.
- **Mobile and native app screens** — prioritise native product screenshots, platform guidelines, motion and native craft, and stack-specific previews.
- **Campaign, launch, editorial, microsite** — curated visual galleries and experiments can carry more weight, but record what cannot transfer to product UI.

The primary reference for each material mechanism should use the target medium: an app for an app, a deck for a deck, an editorial page for an editorial page. Cross-medium sources may suggest a mechanism, but record the lower same-medium fit and do not let them carry the whole direction.

## The pass

1. **Context query builder** — derive search queries from product type, user task, platform, target stack, audience, and constraints. Write each query as what is visible on screen, not as an abstract goal: `[product category] + [screen type] + [visible UI components] + [user state or action]`. `trust patterns` and `good onboarding` are not queries; `signup screen with progress indicator, phone number input, security message, and continue button` is.
2. **Surface and audience routing** — name the surface kind and the Audience Contract. Choose the source lanes before seeing a good-looking candidate; a gallery cannot become task evidence simply because it has a strong composition.
3. **Ledger read** — if `.noootwo/appearance-ledger.md` exists, read only the matching surface/audience heading. Reuse a recorded mechanism or rejection only as a lead; current evidence still wins.
4. **Intervention decision** — decide `leave simple`, `craft only`, or `add moment` before choosing expressive motion or material. The decision can remove expressive sources from scope; it cannot remove the task/platform audition for a standard UI task.
5. **Audition scope** — `standard`: 2–3 candidates from at least two roles, one primary screenshot, one primary plus at most one narrow supplement. `deep`: 3–5 sources, at least one same-medium source, full capture, fit scoring, and 2–3 spikes.
6. **Source accessibility check** — record which pools are reachable; use the fallback ladder when they are not, and record the substitution. A paid or login-gated source is optional, never the free path.
7. **Source-role selection** — select by role, not by site prestige. Product UI needs real product evidence; native needs a native or platform source; marketing may let visual direction lead; a component library is implementation evidence, not a visual direction.
8. **Community signal mining** — search the design pools the research skill names, including product-flow libraries, design systems, curated galleries, and the domestic fallback.
9. **Case capture** — resolve the platform (app or web), route each query to single screens or to multi-step flows, then run two or three queries at a time and write the observations down before starting the next batch. Screens are large; a batch that is not recorded is a batch that gets dropped.
10. **Source weighting** — rank evidence by role, credibility, and fit to this surface. A high-novelty gallery is still weak evidence for a dense workbench.
11. **Influence discovery** — when useful, find relevant designers, studios, products, movements, architecture, exhibition, or spatial systems.
12. **Pattern clustering** — cluster findings into three to five mechanism groups instead of listing examples.
13. **Style evidence check** — record the style claim, the visual evidence, the anti-example, the borrowed mechanism, the implementation translation, the confidence, and whether a spike is needed. The check shape lives in `direction.md`.
14. **Mechanism transfer** — translate each cluster into UI primitives: grid, rail, surface, type scale, data grammar, state model, motion primitive, native component vocabulary.
15. **Preservation contract** — state what must survive translation, what may vary, and what must never be substituted.
16. **Reference lock** — name the build target, primary, supplements, rejected candidates, and what must not drift before drafting.
17. **Fit scoring** — score each candidate territory for scenario, audience, platform, practicality, distinctiveness, implementation credibility, and brand risk.
18. **Artifact spike** — produce two or three small visual spikes for the best territories before investing in a polished draft. One spike only means low confidence.
19. **Evaluator pass** — reject slop, trend cosplay, artist or designer cosplay, crude styling, weak utility, typography failure, responsive failure, and stack-incredible directions.

## Audition tiers

### Standard light audition

Use this for every non-quick UI task, including settings, dashboards, tables, consumer screens, native screens, and marketing pages.

- Pick 2–3 candidates from at least two source roles.
- For product UI, include at least one `product evidence` source with a real screen or flow.
- For native UI, include at least one native product screen or platform guideline.
- For high-frequency work, use task evidence, platform guidance, and data-UI sources before any expressive gallery or effect library.
- Capture one inspectable screen or section for each candidate; record `capture: unreachable` when access fails, but never select an uninspected primary.
- Choose one primary and at most one narrow supplement. Do not average three sources into a safe middle.
- Record the rejected candidates and why they were not selected. This is the defixation step, not optional prose.
- Do not run the full extractor unless the selected primary needs live token values.

### Deep audition

Use this for high-character, brand-heavy, niche, premium, or previously rejected work.

- Pick 3–5 sources, with at least one `same-medium: yes`.
- Capture every source the direction leans on; record access, licence, inspected evidence, and observed values.
- Run the existing fit scoring, reference lock, preservation contract, and 2–3 artifact spikes.
- A blocked source narrows the evidence; it does not cancel the pass and it never becomes an invented observation.

## Audience and source routing

| Audience / surface | Primary evidence | Permitted support | Reject as primary |
| --- | --- | --- | --- |
| Consumer first-use | Real consumer products, platform guidance | Gallery for composition, type, material, atmosphere | Admin density, implementation jargon, effect-library demos |
| Trained operations / admin | Real operations products, data UI, design systems | Gallery for a narrow type or colour mechanism | Marketing hero, expressive motion, generic component gallery |
| Technical buyer | Real product, official docs, performance/security evidence | Gallery for composition; implementation detail after the outcome | Jargon-first hero, decorative technical badges |
| Native app | Native product screens, Apple HIG/Material/native docs | Web/editorial sources for a cross-medium mechanism | Web layout transplanted directly; React-only effect library |
| Marketing / editorial | Awwwards, Framer Gallery, Recent, Savee, editorial references | Real product evidence for claims; React Bits only for a justified motion moment | Fake product UI, copied brand assets, gallery-as-flow evidence |

## Source evidence and licence

Use the `noootwo-research` skill's `design-source-registry.md` for the lane definitions and source boundaries. Record the source role before opening candidates:

- `product evidence` — real screens, flows, states, density, and task conventions.
- `platform convention` — platform guidance and native behaviour.
- `visual direction` — composition, type, material, colour, and atmosphere only.
- `motion mechanism` — trigger, duration, curve, layer, and state meaning only.
- `implementation resource` — components, accessibility plumbing, and dependency cost only.
- `asset source` — font, icon, image, illustration, or 3D licence and availability only.
- `research craft` — user, language, accessibility, and design-rule evidence only.

Every selected source records `Last verified` and `Licence / reuse`. A component demo is evidence of craft, not fit. A gallery is evidence of visual direction, not product flow. A component library is evidence of implementation, not a design direction.

## Case capture

Every reference the direction leans on gets captured locally, so the direction can be re-opened, re-checked, and compared after the build.

For each source, write `.noootwo/references/<slug>/source.md` and capture `NN-<label>.png` beside it. `source.md` records:

- `url`: the page or artifact the reference came from.
- `captured`: date, and the tool used.
- `evidence level`: the rung from the weighting table below.
- `same-medium fit`: `yes`, `no`, or `mixed`, against the target artifact.
- `accessibility`: `reachable`, `login required`, `fallback`, or `unreachable`, with the result actually observed in this pass.
- `artifact inspected`: `yes` or `no`, based on opening the capture and reading the actual composition.
- `observed evidence`: the layout, type ratio, palette proportion, density, state grammar, or motion behavior actually seen.
- `attribution and licence`: product or studio name, and any stated reuse limit.
- `capture`: the screenshot paths, or `unreachable` when none could be taken.
- `reference intent`: `replicate`, `redesign`, or `borrow-mechanism`, and why.
- `role`: `product evidence`, `platform convention`, `visual direction`, `motion mechanism`, `implementation resource`, `asset source`, or `research craft`.
- `surface and audience`: the exact surface and Audience Contract this source is meant to serve.
- `decision`: `primary`, `supplement`, or `rejected`, with the reason.
- `last verified`: the date of the access and artifact check.

Take the screenshot in the same extractor pass that captures the values: `scripts/extract_design_tokens.mjs <url> --screenshot .noootwo/references/<slug>/NN-<label>.png`.

When a source is unreachable or behind a login, record `capture: unreachable`, keep the URL, and continue with the sources that remain. A blocked source narrows the evidence; it never cancels the pass.

A screenshot path is not evidence until it was opened. A black, broken, placeholder, or loading capture records `artifact inspected: no` and cannot support a style claim. Captured screenshots are personal reference held in the project's `.noootwo/` harness. They are not committed, not redistributed, and never a target to reproduce pixel for pixel. Borrow the mechanism — space, density, rhythm, state grammar, motion behaviour — and leave the artwork, brand assets, and exact composition behind.

When the intervention decision is `add moment`, the capture set includes motion or material examples: two or three references in the same register, each recorded as a mechanism — trigger, moving property, duration, curve, layer relationship, and what it communicates. The register and the sourcing procedure live in [motion](motion.md); the pool of motion libraries and showcases lives in the `noootwo-research` skill's source pools. A component library's demo is strong evidence of craft and weak evidence of fit, so it is adapted or dropped rather than pasted.

## Screenshot And Design-Image Intake

When the user supplies a screenshot, design image, Figma frame, or device capture instead of a live URL, run the same discovery discipline on the image before writing UI code.

Record these fields in `.noootwo/style-discovery.md` or the reference's `source.md`:

- `viewport`: source width, height, device family, scale, safe area, and whether it is a desktop, tablet, phone, or mixed board.
- `layout`: grid, margins, gutters, container behaviour, alignment model, and the elements that establish hierarchy.
- `typography`: visible families if identifiable, size relationships, weight, case, line height, measure, and numeric treatment. Mark inferred values as inferred.
- `colour and material`: canvas, surface, text, accent, semantic roles, border, shadow, texture, and light direction.
- `components and states`: inventory of the components shown and which states are visible. Missing states are gaps, not defaults.
- `imagery and iconography`: subject, crop, aspect ratio, treatment, icon family and weight, and whether the asset is real or decorative.
- `motion cues`: any arrows, trails, before/after frames, scroll position, or annotation that implies timing, trigger, or direction. Never infer a full motion system from a still image alone.
- `provenance and licence`: who supplied the image, whether it is a design file, screenshot, generated concept, or public reference, and any reuse boundary.
- `confidence`: confirmed, inferred, or proposed, with the missing evidence named.

For a Figma or other design-file source, read variables, styles, and component names when access exists before relying on pixels. For Flutter, SwiftUI, or Compose work, capture the target frame in a real preview or device when possible and map the image to platform tokens rather than translating web pixel values directly.

An image shows appearance; it does not prove interaction, accessibility, responsive behaviour, or data states. Those remain explicit gaps until a running artifact, design file, or user decision supplies them.

## Reference lock

Before drafting, name the target and the invariants:

```markdown
Reference Lock
- Build target: existing UI | user screenshot | design file | captured reference | approved spike
- Reference intent: replicate | redesign | borrow-mechanism
- Primaries: the one or two sources that carry the direction
- Must not drift: canvas, typography, accent roles, layout, media, density, motion
- Rejected surface styling: what is deliberately not taken
```

Without a lock, a direction is still prose. When references conflict, pick one dominant direction and let the others contribute narrow details; averaging them into a safe middle is the failure this step exists to prevent.

After the build, capture the finished surface the same way and compare it against the captured baseline with `scripts/extract_design_tokens.mjs --compare`. Drift is reported, not silently repaired.

## Influence discovery

Use it only for deep, full-redesign, or high-character work, or when previous directions were too generic. For each influence record:

- `source`: designer, studio, product, movement, architecture or spatial system, exhibition, or real product.
- `why relevant`: product fit, emotional fit, interaction fit, audience fit.
- `borrowable mechanisms`: space, light, density, composition, typography, interaction, information organisation, material, rhythm.
- `do not copy`: signature visuals, artwork, characters, logos, named brand skins, exact compositions, personal style markers.
- `translation`: colour roles, type roles, layout model, component vocabulary, motion thesis, data and state grammar.
- `risk`: mimicry, brand mismatch, legal or ethical risk, implementation cost, utility loss.

Never output "in the style of X" as a direction. Output a mechanism mix — for example: atmosphere from spatial light, information grammar from an internal map, interaction efficiency from a private journal app.

## Evidence weighting for taste

1. Real product flow, running product, or target-stack screenshot.
2. Public design system or platform guideline.
3. Curated gallery with a visible artifact and a source URL.
4. Community discussion with a visible artifact.
5. A single post, moodboard image, or portfolio shot.

Rungs 4–5 may influence art direction for campaign work and must not decide a dashboard, settings page, workbench, or native screen. High visual novelty with low product evidence is a lead, not a direction.

The weighting is role-aware. A gallery at rung 3 can be the primary source for a marketing page's composition; it cannot be the primary source for a dashboard's flow. A component demo is stronger than a screenshot for state anatomy and weaker than a real product for task fit.

## Fit scoring

Score each territory 1–5 on scenario fit, practicality and task clarity, distinctiveness, implementation credibility, and brand risk (where 5 means low risk). Discard anything with practicality below 3 for product UI, or implementation credibility below 3 for production work.

## Required output

For `standard`, write `.noootwo/reference-board.md` with `Mode: standard`, 2–3 candidates, one primary capture, rejected candidates, and `Landed as` for the selected mechanism. Do not create the full deep record.

For `deep`, write `.noootwo/style-discovery.md` with:

- Source accessibility
- Intervention decision
- Surface type
- Audience contract
- Search queries
- Source pool
- Source roles
- Foreign sources tried
- Domestic fallback sources when used
- Evidence URLs or screenshots
- Capture directory
- Evidence levels
- Same-medium fit and inspected evidence for every primary source
- Style Evidence Check
- Reference lock
- Pattern clusters
- Borrowed mechanisms
- Influence shortlist when used
- Rejected mimicry
- Rejected candidates and reasons
- Design-system translation
- Preservation contract
- Rejected surfaces
- Fit scores
- Spike comparison
- Recommended territories

Then update `.noootwo/reference-board.md` with every selected and rejected candidate, each source's role, capture path, fit decision, and what it landed as. Read or create `.noootwo/appearance-ledger.md` only through the matching surface/audience section; write an outcome entry after review.

The readiness validator reads this file field by field. Keep the section and field names exactly as listed. If source accessibility, URL or artifact evidence, the capture directory, evidence levels, the Style Evidence Check, the reference lock, or rejected surfaces are missing, return to discovery before drafting — a missing field is a failed gate, not a formatting detail.
