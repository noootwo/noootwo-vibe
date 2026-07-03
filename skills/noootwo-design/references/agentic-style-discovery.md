# Agentic Style Discovery

Use this in deep mode before high-character UI. The goal is to discover usable style mechanisms with agent capabilities: search, source weighting, clustering, optional influence discovery, mechanism transfer, artifact spikes, and critique.

## Workflow

1. `Context Query Builder`: derive search queries from product type, user task, platform, target stack, audience, and constraints.
2. `Source Accessibility Check`: record which preferred foreign sources are reachable; if blocked, use [research-source-fallback.md](research-source-fallback.md).
3. `Surface Type Routing`: classify product UI, data UI, utility UI, native screen, campaign, launch, or editorial before selecting sources.
4. `Community Signal Mining`: search source pools from [source-registry.md](source-registry.md), including product-flow libraries, design systems, curated web galleries, domestic fallback sources, Figma/community signals, and developer forums.
5. `Source Weighting`: rank evidence by credibility and task fit.
6. `Influence Discovery` when useful: find relevant designers, artists, studios, products, movements, architecture, exhibition systems, or spatial references.
7. `Pattern Clustering`: cluster findings into 3-5 mechanism groups instead of listing examples.
8. `Mechanism Transfer`: translate each cluster into UI primitives such as grid, rail, surface, type scale, data grammar, state model, motion primitive, or native component vocabulary.
9. `Preservation Contract`: state what must survive translation, what may vary, and what must never be substituted.
10. `Fit Scoring`: score each candidate for scenario fit, practicality, distinctiveness, implementation cost, and brand risk.
11. `Artifact Spike`: produce 2-3 small visual spikes for the best territories before investing in a polished draft. If only 1 spike is possible, mark low confidence.
12. `Evaluator Pass`: reject AI slop, trend cosplay, artist/designer cosplay, crude styling, weak utility, typography failure, responsive failure, and stack-incredible directions.

## Influence Discovery

Use influence discovery only for deep/full redesign/high-character work or when prior directions were too generic.

For each influence source, record:

- `source`: designer, artist, studio, product, art movement, architecture/spatial system, exhibition, or real product
- `why relevant`: product fit, emotional fit, interaction fit, or audience fit
- `borrowable mechanisms`: space, light, density, composition, typography, interaction, information organization, material, rhythm
- `do not copy`: signature visuals, artwork, characters, logos, named brand skins, exact compositions, or personal style markers
- `translation`: color roles, type roles, layout model, component vocabulary, motion thesis, data/state grammar
- `risk`: mimicry, brand mismatch, legal/ethical risk, implementation cost, utility loss

Do not output "in the style of X" as a direction. Output a mechanism mix, for example: `base atmosphere from spatial light + information grammar from internal map + interaction efficiency from private journal app`.

## Source Weighting

Use this default ranking:

1. Real product flows and app screenshots
2. Running product artifacts or public product pages
3. Design system and platform documentation
4. High-quality curated galleries
5. Designer/developer community discussion with visible artifacts
6. Single social post or Dribbble-style shot

High visual novelty with low product evidence can inspire campaign pages, but it cannot decide a tool, dashboard, or native app UI by itself.

## Surface Routing

- Dashboards, settings, workbenches, analytics, admin, devtools: prioritize product flows, real screenshots, design systems, data UI rules, and task evidence.
- Mobile or native app screens: prioritize native product screenshots, platform guidelines, motion/native craft, and stack-specific previews.
- Campaign, launch, editorial, microsite: curated web galleries and visual experiments can carry more weight, but still record what cannot transfer to product UI.

## Fit Scoring

Score each territory from 1-5:

- Scenario fit
- Practicality and task clarity
- Distinctiveness
- Implementation credibility
- Brand risk, where 5 means low risk

Discard any territory with practicality below 3 for product UI, or implementation credibility below 3 for production work.

## Required Output

Write `.noootwo/style-discovery.md` with:

- Source accessibility
- Surface type
- Search queries
- Source pool
- Foreign sources tried
- Domestic fallback sources when used
- Evidence URLs or screenshots
- Evidence levels
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

If source accessibility, URL/artifact evidence, evidence levels, or rejected surfaces are missing, return to discovery before drafting.
