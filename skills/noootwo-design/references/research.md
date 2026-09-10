# Design Research

The research pass required before changing aesthetics, and the source pools it draws from.


## Research Protocol

Use this before changing Noootwo Design's aesthetics, workflow, stack playbooks, review gates, project integration, or public claims.

### Source Standard

- Start with official docs or primary sources when available.
- Add developer and designer community signals from places like X/Twitter, Reddit, HN, Figma, Flutter, React, Vue, iOS, Android, and product design communities.
- If foreign sources are inaccessible, use domestic fallback sources and record the access limitation instead of skipping research.
- Prefer sources with screenshots, running artifacts, repositories, videos, or hands-on reports.
- Treat single social posts as leads, not proof.
- Do not copy leaked prompts, proprietary designs, brand styling, or surface decoration.

### What To Extract

- Repeatable mechanism: design-system memory, reference board, canvas artifact, screenshot review, token mapping, stack-native motion, evaluator loop, or handoff structure.
- Evidence level: official, verified artifact, credible hands-on report, community signal, or unverified anecdote.
- Applicability: which stack, mode, or project stage it helps.
- Boundary: what should not be copied or overgeneralized.
- Cost and feasibility: whether the mechanism belongs in quick, standard, deep, production, or only as an optional check.
- Skill change: the concrete rule, template, script, or test that should change.

### Required Notes

When a change depends on research, record:

- Sources reviewed
- Mechanism borrowed
- Risks or counterexamples
- Why the change belongs in Noootwo Design
- How artifact or screenshot review will verify it
- Whether the change increases skill cost and which mode should pay that cost

### Decision Rule

If research only produces style adjectives, do not change the skill. Convert the finding into a testable mechanism or leave it out.

Do not add high-cost requirements to quick or standard mode unless they prevent a concrete, repeated failure.


## Research Source Fallback

Use this before deep-mode style discovery. The goal is to keep research real when the agent cannot access the usual international source pool.

### Accessibility Check

Record source access in `.noootwo/style-discovery.md` before drafting:

- Foreign sources tried: URL, access result, and whether screenshots or artifacts were visible.
- Domestic fallback used: URL, access result, and evidence level.
- Evidence captured: screenshot path, product page URL, gallery URL, design system URL, or explicit limitation.

If no URL, screenshot, product artifact, or platform documentation can be recorded, the work has no research evidence and must not enter deep-mode draft.

### Preferred Foreign Sources

- Product flows: Mobbin, Page Flows, Screenlane, ScreensDesign, Appshots.
- Web and campaign art direction: Godly, Siteinspire, Awwwards, Land-book, Savee, Httpster, Minimal Gallery.
- Product craft and systems: Linear, Vercel Geist, Stripe, Apple HIG, Material, Shopify Polaris, GitHub Primer, Atlassian, IBM Carbon.
- Motion and native craft: Rive, GSAP, Motion, Flutter Wonderous, SwiftUI docs, Jetpack Compose docs.

### Domestic Fallback Sources

- Product and tool ecosystems: MasterGo, 即时设计, Ant Design, Semi Design, Arco Design, TDesign, NutUI, Vant.
- Design communities and resources: UI中国, 站酷, 优设网, 花瓣, 即时设计社区, MasterGo 社区.
- Trend and weak-signal sources: 小红书 design posts, B 站 design breakdowns, 微信公众号 design essays, X/Twitter mirrors when available.
- Real product evidence: screenshots from Chinese SaaS, fintech, content, ecommerce, devtool, and app products that match the target task.

Domestic social posts, portfolio shots, and trend essays are weak signals. They can suggest taste, but product UI decisions need confirmation from real screenshots, design systems, or multiple independent sources.

### Evidence Weighting

Use this ranking:

1. Real product flow, running product, or target-stack screenshot.
2. Public design system or platform guideline.
3. Curated gallery with visible artifact and source URL.
4. Designer/developer community discussion with visible artifact.
5. Single social post, moodboard image, or portfolio shot.

For dashboards, settings, workbenches, and utility UI, do not let category 4-5 evidence decide the direction. For campaign or launch work, category 3-5 can influence art direction but must still pass usability and implementation checks.


## Source Registry

Use this as a search map for agentic style discovery. Sources are not templates; they are evidence pools for mechanisms.

### Product Flow And App UI

- Mobbin: mobile and web app screenshots, product flows, UI element patterns.
- Page Flows: recorded user flows and screenshots from real products.
- Screenlane, ScreensDesign, Appshots, and similar libraries: app screen references when available.
- Domestic fallback: real screenshots from matching Chinese products, MasterGo resources, 即时设计 resources, Ant Design, Semi Design, Arco Design, TDesign, NutUI, Vant.

Best for: SaaS, dashboards, settings, onboarding, mobile apps, product utility surfaces.

Risk: may bias toward mainstream patterns if used without counter-positioning.

### Web, Campaign, And Art Direction

- Godly, Siteinspire, Awwwards, Land-book, Savee, Httpster, Minimal Gallery, and curated web showcases.
- Domestic fallback: 站酷, UI中国, 优设网, 花瓣, 即时设计社区, MasterGo 社区, B 站 design breakdowns, 小红书 design trend posts.

Best for: launch pages, editorial surfaces, microsites, brand-heavy pages.

Risk: visual novelty may be low-utility or trend-driven. Downweight for operational tools and app screens.

### Influence Discovery Sources

- Spatial and light references: installation artists, museum/exhibition systems, architecture studios, spatial designers.
- Information and diagram references: editorial designers, cartographers, notation systems, scientific visualization, archival systems.
- Product behavior references: journaling, wellness, relationship, devtool, creative-tool, and private-workbench products.
- Domestic fallback: 设计博物馆/展览文章, 站酷/UI中国 designer pages, 建筑/室内/展陈案例, 小红书/B 站 design breakdowns, MasterGo/即时设计 community systems.

Best for: high-character redesign, emotional product tone, non-generic visual language, and mechanism mixing.

Risk: designer/artist cosplay. Borrow space, light, density, rhythm, and information grammar; never copy signature artwork, characters, logos, exact layouts, or "in the style of X" surfaces.

### Product Craft And Design Systems

- Linear, Vercel Geist, Stripe, Apple Human Interface Guidelines, Material Design, Shopify Polaris, GitHub Primer, Atlassian, IBM Carbon.
- DESIGN.md-style design spec collections, such as `VoltAgent/awesome-design-md`, may be used only as examples of structure: role-based colors, type rules, component constraints, do/don't guidance, and agent-facing implementation notes.

Best for: production UI, tokens, density, component craft, platform behavior, interaction states.

Risk: can become generic or derivative if copied literally; extract constraints and systems, not surface look. Do not fetch these by default, do not make the skill depend on them, and do not copy brand skins into a project unless the user explicitly asks for that brand reference.

### Motion And Native Craft

- Rive, Motion/Framer Motion, GSAP, Flutter Wonderous, SwiftUI docs, Jetpack Compose docs, platform HIG motion guidance.

Best for: app polish, transitions, state changes, stack-native interactions.

Risk: motion as garnish on a weak layout. Use motion only when it clarifies state, continuity, or product identity.

### Weak Signals

- X/Twitter, Reddit, HN, Figma Community, designer newsletters, conference talks, studio blogs.
- Domestic weak signals: 小红书, B 站, 微信公众号, 站酷/UI中国 comment threads, local design newsletters.

Best for: current signals, emerging taste, toolchain shifts, critique of common patterns.

Risk: low evidence and high noise. Treat as a lead until confirmed by artifacts or multiple signals.

### Accessibility Fallback

If the preferred foreign sources are inaccessible, use [research](research.md). Record the access result and do not silently replace evidence with imagined trends.

### Query Pattern

Combine:

- Product type: dashboard, settings, consumer app, launch page, marketplace, editor, devtool
- Task: monitor, compare, purchase, onboard, configure, review, create, schedule
- Platform: web, React, Vue, Flutter, iOS, Android, desktop
- Taste target: minimal, luxury, editorial, utility, experimental, fashion, industrial, cinematic
- Anti-pattern: no gradient SaaS, no card wall, no generic dashboard, no fake data viz


## Agentic Style Discovery

Use this in deep mode before high-character UI. The goal is to discover usable style mechanisms with agent capabilities: search, source weighting, clustering, optional influence discovery, mechanism transfer, artifact spikes, and critique.

### Workflow

1. `Context Query Builder`: derive search queries from product type, user task, platform, target stack, audience, and constraints.
2. `Source Accessibility Check`: record which preferred foreign sources are reachable; if blocked, use [research](research.md).
3. `Surface Type Routing`: classify product UI, data UI, utility UI, native screen, campaign, launch, or editorial before selecting sources.
4. `Community Signal Mining`: search source pools from [research](research.md), including product-flow libraries, design systems, curated web galleries, domestic fallback sources, Figma/community signals, and developer forums.
5. `Source Weighting`: rank evidence by credibility and task fit.
6. `Influence Discovery` when useful: find relevant designers, artists, studios, products, movements, architecture, exhibition systems, or spatial references.
7. `Pattern Clustering`: cluster findings into 3-5 mechanism groups instead of listing examples.
8. `Style Evidence Check`: record the style claim, visual evidence, anti-example, borrowed mechanism, implementation translation, confidence, and spike need.
9. `Mechanism Transfer`: translate each cluster into UI primitives such as grid, rail, surface, type scale, data grammar, state model, motion primitive, or native component vocabulary.
10. `Preservation Contract`: state what must survive translation, what may vary, and what must never be substituted.
11. `Fit Scoring`: score each candidate for scenario fit, practicality, distinctiveness, implementation cost, and brand risk.
12. `Artifact Spike`: produce 2-3 small visual spikes for the best territories before investing in a polished draft. If only 1 spike is possible, mark low confidence.
13. `Evaluator Pass`: reject AI slop, trend cosplay, artist/designer cosplay, crude styling, weak utility, typography failure, responsive failure, and stack-incredible directions.

### Influence Discovery

Use influence discovery only for deep/full redesign/high-character work or when prior directions were too generic.

For each influence source, record:

- `source`: designer, artist, studio, product, art movement, architecture/spatial system, exhibition, or real product
- `why relevant`: product fit, emotional fit, interaction fit, or audience fit
- `borrowable mechanisms`: space, light, density, composition, typography, interaction, information organization, material, rhythm
- `do not copy`: signature visuals, artwork, characters, logos, named brand skins, exact compositions, or personal style markers
- `translation`: color roles, type roles, layout model, component vocabulary, motion thesis, data/state grammar
- `risk`: mimicry, brand mismatch, legal/ethical risk, implementation cost, utility loss

Do not output "in the style of X" as a direction. Output a mechanism mix, for example: `base atmosphere from spatial light + information grammar from internal map + interaction efficiency from private journal app`.

### Source Weighting

Use this default ranking:

1. Real product flows and app screenshots
2. Running product artifacts or public product pages
3. Design system and platform documentation
4. High-quality curated galleries
5. Designer/developer community discussion with visible artifacts
6. Single social post or Dribbble-style shot

High visual novelty with low product evidence can inspire campaign pages, but it cannot decide a tool, dashboard, or native app UI by itself.

### Style Evidence Check

For every high-character territory, record:

- `style claim`: the taste target in concrete terms
- `visual evidence`: openable reference, screenshot, user image, visual sample, or spike
- `anti-example`: what would prove the style was misunderstood
- `borrowed mechanism`: the transferable visual or interaction mechanism
- `implementation translation`: how it maps to tokens, components, spacing, motion, native controls, or artifact structure
- `confidence`: high, medium, or low
- `artifact/spike required`: what must be seen before ready

If visual evidence is missing, the territory can stay exploratory only with `low confidence`. Do not promote it into a Design Contract or implementation plan until evidence or a spike exists.

### Surface Routing

- Dashboards, settings, workbenches, analytics, admin, devtools: prioritize product flows, real screenshots, design systems, data UI rules, and task evidence.
- Mobile or native app screens: prioritize native product screenshots, platform guidelines, motion/native craft, and stack-specific previews.
- Campaign, launch, editorial, microsite: curated web galleries and visual experiments can carry more weight, but still record what cannot transfer to product UI.

### Fit Scoring

Score each territory from 1-5:

- Scenario fit
- Practicality and task clarity
- Distinctiveness
- Implementation credibility
- Brand risk, where 5 means low risk

Discard any territory with practicality below 3 for product UI, or implementation credibility below 3 for production work.

### Required Output

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

If source accessibility, URL/artifact evidence, evidence levels, Style Evidence Check, or rejected surfaces are missing, return to discovery before drafting.
