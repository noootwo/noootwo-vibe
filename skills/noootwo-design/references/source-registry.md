# Source Registry

Use this as a search map for agentic style discovery. Sources are not templates; they are evidence pools for mechanisms.

## Product Flow And App UI

- Mobbin: mobile and web app screenshots, product flows, UI element patterns.
- Page Flows: recorded user flows and screenshots from real products.
- Screenlane, ScreensDesign, Appshots, and similar libraries: app screen references when available.
- Domestic fallback: real screenshots from matching Chinese products, MasterGo resources, 即时设计 resources, Ant Design, Semi Design, Arco Design, TDesign, NutUI, Vant.

Best for: SaaS, dashboards, settings, onboarding, mobile apps, product utility surfaces.

Risk: may bias toward mainstream patterns if used without counter-positioning.

## Web, Campaign, And Art Direction

- Godly, Siteinspire, Awwwards, Land-book, Savee, Httpster, Minimal Gallery, and curated web showcases.
- Domestic fallback: 站酷, UI中国, 优设网, 花瓣, 即时设计社区, MasterGo 社区, B 站 design breakdowns, 小红书 design trend posts.

Best for: launch pages, editorial surfaces, microsites, brand-heavy pages.

Risk: visual novelty may be low-utility or trend-driven. Downweight for operational tools and app screens.

## Influence Discovery Sources

- Spatial and light references: installation artists, museum/exhibition systems, architecture studios, spatial designers.
- Information and diagram references: editorial designers, cartographers, notation systems, scientific visualization, archival systems.
- Product behavior references: journaling, wellness, relationship, devtool, creative-tool, and private-workbench products.
- Domestic fallback: 设计博物馆/展览文章, 站酷/UI中国 designer pages, 建筑/室内/展陈案例, 小红书/B 站 design breakdowns, MasterGo/即时设计 community systems.

Best for: high-character redesign, emotional product tone, non-generic visual language, and mechanism mixing.

Risk: designer/artist cosplay. Borrow space, light, density, rhythm, and information grammar; never copy signature artwork, characters, logos, exact layouts, or "in the style of X" surfaces.

## Product Craft And Design Systems

- Linear, Vercel Geist, Stripe, Apple Human Interface Guidelines, Material Design, Shopify Polaris, GitHub Primer, Atlassian, IBM Carbon.
- DESIGN.md-style design spec collections, such as `VoltAgent/awesome-design-md`, may be used only as examples of structure: role-based colors, type rules, component constraints, do/don't guidance, and agent-facing implementation notes.

Best for: production UI, tokens, density, component craft, platform behavior, interaction states.

Risk: can become generic or derivative if copied literally; extract constraints and systems, not surface look. Do not fetch these by default, do not make the skill depend on them, and do not copy brand skins into a project unless the user explicitly asks for that brand reference.

## Motion And Native Craft

- Rive, Motion/Framer Motion, GSAP, Flutter Wonderous, SwiftUI docs, Jetpack Compose docs, platform HIG motion guidance.

Best for: app polish, transitions, state changes, stack-native interactions.

Risk: motion as garnish on a weak layout. Use motion only when it clarifies state, continuity, or product identity.

## Weak Signals

- X/Twitter, Reddit, HN, Figma Community, designer newsletters, conference talks, studio blogs.
- Domestic weak signals: 小红书, B 站, 微信公众号, 站酷/UI中国 comment threads, local design newsletters.

Best for: current signals, emerging taste, toolchain shifts, critique of common patterns.

Risk: low evidence and high noise. Treat as a lead until confirmed by artifacts or multiple signals.

## Accessibility Fallback

If the preferred foreign sources are inaccessible, use [research-source-fallback.md](research-source-fallback.md). Record the access result and do not silently replace evidence with imagined trends.

## Query Pattern

Combine:

- Product type: dashboard, settings, consumer app, launch page, marketplace, editor, devtool
- Task: monitor, compare, purchase, onboard, configure, review, create, schedule
- Platform: web, React, Vue, Flutter, iOS, Android, desktop
- Taste target: minimal, luxury, editorial, utility, experimental, fashion, industrial, cinematic
- Anti-pattern: no gradient SaaS, no card wall, no generic dashboard, no fake data viz
