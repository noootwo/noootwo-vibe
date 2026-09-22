# Design Discovery

The discovery pass that produces `.noootwo/style-discovery.md`, and the contract that file must satisfy.

Source pools, access records, and the fallback ladder belong to the `noootwo-research` skill — invoke it: read its `SKILL.md` and follow it. This file owns only what is design-specific: which surfaces need discovery, how to weight evidence for taste, how to translate influences into mechanisms, and what the artifact must contain.

## When

Run this in `deep` mode and for high-character, niche, premium, brand-heavy, or previously rejected work. `quick`, `standard`, and `production` do not pay this cost.

## Surface routing

Classify the surface before choosing sources:

- **Dashboards, settings, workbenches, analytics, admin, devtools** — prioritise real product flows, real screenshots, design systems, data UI rules, and task evidence. Community and gallery evidence cannot decide these.
- **Mobile and native app screens** — prioritise native product screenshots, platform guidelines, motion and native craft, and stack-specific previews.
- **Campaign, launch, editorial, microsite** — curated visual galleries and experiments can carry more weight, but record what cannot transfer to product UI.

## The pass

1. **Context query builder** — derive search queries from product type, user task, platform, target stack, audience, and constraints. Write each query as what is visible on screen, not as an abstract goal: `[product category] + [screen type] + [visible UI components] + [user state or action]`. `trust patterns` and `good onboarding` are not queries; `signup screen with progress indicator, phone number input, security message, and continue button` is.
2. **Source accessibility check** — record which pools are reachable; use the fallback ladder when they are not, and record the substitution.
3. **Community signal mining** — search the design pools the research skill names, including product-flow libraries, design systems, curated galleries, and the domestic fallback.
4. **Case capture** — resolve the platform (app or web), route each query to single screens or to multi-step flows, then run two or three queries at a time and write the observations down before starting the next batch. Screens are large; a batch that is not recorded is a batch that gets dropped.
5. **Source weighting** — rank evidence by credibility and by fit to this surface.
6. **Influence discovery** — when useful, find relevant designers, studios, products, movements, architecture, exhibition, or spatial systems.
7. **Pattern clustering** — cluster findings into three to five mechanism groups instead of listing examples.
8. **Style evidence check** — record the style claim, the visual evidence, the anti-example, the borrowed mechanism, the implementation translation, the confidence, and whether a spike is needed. The check shape lives in `direction.md`.
9. **Mechanism transfer** — translate each cluster into UI primitives: grid, rail, surface, type scale, data grammar, state model, motion primitive, native component vocabulary.
10. **Preservation contract** — state what must survive translation, what may vary, and what must never be substituted.
11. **Reference lock** — name the build target and what must not drift before drafting.
12. **Fit scoring** — score each candidate territory for scenario fit, practicality, distinctiveness, implementation cost, and brand risk.
13. **Artifact spike** — produce two or three small visual spikes for the best territories before investing in a polished draft. One spike only means low confidence.
14. **Evaluator pass** — reject slop, trend cosplay, artist or designer cosplay, crude styling, weak utility, typography failure, responsive failure, and stack-incredible directions.

## Case capture

Every reference the direction leans on gets captured locally, so the direction can be re-opened, re-checked, and compared after the build.

For each source, write `.noootwo/references/<slug>/source.md` and capture `NN-<label>.png` beside it. `source.md` records:

- `url`: the page or artifact the reference came from.
- `captured`: date, and the tool used.
- `evidence level`: the rung from the weighting table below.
- `accessibility`: `reachable`, `login required`, `fallback`, or `unreachable`, with the result actually observed in this pass.
- `attribution and licence`: product or studio name, and any stated reuse limit.
- `capture`: the screenshot paths, or `unreachable` when none could be taken.
- `reference intent`: `replicate`, `redesign`, or `borrow-mechanism`, and why.

Take the screenshot in the same extractor pass that captures the values: `scripts/extract_design_tokens.mjs <url> --screenshot .noootwo/references/<slug>/NN-<label>.png`.

When a source is unreachable or behind a login, record `capture: unreachable`, keep the URL, and continue with the sources that remain. A blocked source narrows the evidence; it never cancels the pass.

Captured screenshots are personal reference held in the project's `.noootwo/` harness. They are not committed, not redistributed, and never a target to reproduce pixel for pixel. Borrow the mechanism — space, density, rhythm, state grammar, motion behaviour — and leave the artwork, brand assets, and exact composition behind.

When the direction carries motion, the capture set includes motion examples: two or three references in the same register, each recorded as a mechanism — trigger, moving property, duration, curve, layer relationship, and what it communicates. The register and the sourcing procedure live in [motion](motion.md); the pool of motion libraries and showcases lives in the `noootwo-research` skill's source pools. A component library's demo is strong evidence of craft and weak evidence of fit, so it is adapted or dropped rather than pasted.

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

## Fit scoring

Score each territory 1–5 on scenario fit, practicality and task clarity, distinctiveness, implementation credibility, and brand risk (where 5 means low risk). Discard anything with practicality below 3 for product UI, or implementation credibility below 3 for production work.

## Required output

Write `.noootwo/style-discovery.md` with:

- Source accessibility
- Surface type
- Search queries
- Source pool
- Foreign sources tried
- Domestic fallback sources when used
- Evidence URLs or screenshots
- Capture directory
- Evidence levels
- Style Evidence Check
- Reference lock
- Pattern clusters
- Borrowed mechanisms
- Influence shortlist when used
- Rejected mimicry
- Design-system translation
- Preservation contract
- Rejected surfaces
- Fit scores
- Spike comparison
- Recommended territories

Then update `.noootwo/reference-board.md` with the selected sources and mechanisms, including each source's capture path and what it landed as.

The readiness validator reads this file field by field. Keep the section and field names exactly as listed. If source accessibility, URL or artifact evidence, the capture directory, evidence levels, the Style Evidence Check, the reference lock, or rejected surfaces are missing, return to discovery before drafting — a missing field is a failed gate, not a formatting detail.
