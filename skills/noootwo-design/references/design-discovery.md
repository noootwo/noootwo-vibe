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

1. **Context query builder** — derive search queries from product type, user task, platform, target stack, audience, and constraints.
2. **Source accessibility check** — record which pools are reachable; use the fallback ladder when they are not, and record the substitution.
3. **Community signal mining** — search the design pools the research skill names, including product-flow libraries, design systems, curated galleries, and the domestic fallback.
4. **Source weighting** — rank evidence by credibility and by fit to this surface.
5. **Influence discovery** — when useful, find relevant designers, studios, products, movements, architecture, exhibition, or spatial systems.
6. **Pattern clustering** — cluster findings into three to five mechanism groups instead of listing examples.
7. **Style evidence check** — record the style claim, the visual evidence, the anti-example, the borrowed mechanism, the implementation translation, the confidence, and whether a spike is needed. The check shape lives in `direction.md`.
8. **Mechanism transfer** — translate each cluster into UI primitives: grid, rail, surface, type scale, data grammar, state model, motion primitive, native component vocabulary.
9. **Preservation contract** — state what must survive translation, what may vary, and what must never be substituted.
10. **Fit scoring** — score each candidate territory for scenario fit, practicality, distinctiveness, implementation cost, and brand risk.
11. **Artifact spike** — produce two or three small visual spikes for the best territories before investing in a polished draft. One spike only means low confidence.
12. **Evaluator pass** — reject slop, trend cosplay, artist or designer cosplay, crude styling, weak utility, typography failure, responsive failure, and stack-incredible directions.

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
- Evidence levels
- Style Evidence Check
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

Then update `.noootwo/reference-board.md` with the selected sources and mechanisms.

The readiness validator reads this file field by field. Keep the section and field names exactly as listed. If source accessibility, URL or artifact evidence, evidence levels, the Style Evidence Check, or rejected surfaces are missing, return to discovery before drafting — a missing field is a failed gate, not a formatting detail.
