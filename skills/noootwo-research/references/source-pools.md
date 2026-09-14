# Source Pools

Where to look, by domain, and what to do when a pool is unreachable. Sources are evidence pools, not templates.

## Access record

Record source access before drafting a `deep` brief:

- Foreign pools tried: URL, access result, and whether artifacts or screenshots were visible.
- Fallback pool used: URL, access result, and evidence level.
- Evidence captured: screenshot path, repository URL, product page, design system URL, benchmark, or an explicit limitation.

If no URL, screenshot, artifact, or platform documentation can be recorded, the pass has no evidence and must not produce a brief that claims to decide something.

## Design and UI

- **Product flow and app screens**: Mobbin, Page Flows, Screenlane, ScreensDesign, Appshots.
- **Web, campaign, and art direction**: Godly, Siteinspire, Awwwards, Land-book, Savee, Httpster, Minimal Gallery.
- **Product craft and design systems**: Linear, Vercel Geist, Stripe, Apple HIG, Material, Shopify Polaris, GitHub Primer, Atlassian, IBM Carbon.
- **Motion and native craft**: Rive, GSAP, Motion, Flutter Wonderous, SwiftUI docs, Jetpack Compose docs.
- **Influence discovery** (deep or high-character work only): spatial and light references from installation, exhibition, and architecture practice; information and diagram references from editorial design, cartography, notation systems, and scientific visualisation.

Best for: direction, layout, density, typography, motion, and native component vocabulary.
Risk: novelty without utility; designer or artist cosplay. Borrow space, light, density, rhythm, and information grammar — never signature artwork, characters, logos, exact layouts, or "in the style of X".

## Product and market

- Direct competitor products, including their pricing, onboarding, and changelog.
- Review sites and marketplace listings for the complaint pattern, not the star average.
- Public issue trackers and changelogs, which show what the product refuses to do.
- Community threads where users describe the workaround they built.
- Analytics, support tickets, and session recordings the project already owns.

Best for: real user, expectation, willingness to switch, and unmet need.
Risk: reviews are selected populations. A loud complaint is a lead; the pattern across sources is the finding.

## Tech stack and libraries

- Official docs, migration guides, and the changelog.
- The repository itself: release cadence, open-issue response time, contributor spread, and recent breaking changes.
- Package registries for download trend, version spread, and publish recency.
- Benchmarks, bundle-size reports, and the project's own performance doc.
- Real adopters: who uses it in production, at what scale, and what they complained about afterwards.

Best for: adoption, fit, cost, and risk. Read `tech-selection.md` for the scoring pass.
Risk: star counts reward age and marketing. Judge maintenance health and fit, not popularity alone.

## Community signal

- Developer and designer communities: X, Reddit, HN, Figma Community, framework forums.
- Domestic equivalents: 小红书, B 站, 微信公众号, 站酷, UI 中国, 掘金, 少数派, V2EX.
- Conference talks, studio blogs, and newsletters.

Best for: current signals, emerging taste, toolchain shifts, and critique of common patterns.
Risk: low evidence and high noise. Treat as a lead until confirmed by an artifact or a second independent source.

## Fallback ladder

When the preferred international pools are unreachable, do not skip the pass. Use these and record the substitution:

- **Design**: MasterGo, 即时设计, Ant Design, Semi Design, Arco Design, TDesign, NutUI, Vant; real screenshots from matching domestic products.
- **Community**: UI 中国, 站酷, 优设网, 花瓣, 掘金, B 站 breakdowns, 小红书 design posts, product WeChat accounts.
- **Tech**: the repository, official docs, and package registries are usually reachable even when review sites are not.

Domestic social posts, portfolio shots, and trend essays are weak signals: they can suggest taste, and a product decision still needs real screenshots, design systems, or multiple independent sources.

## Query pattern

Combine: product or component type; the user's task; platform and stack; audience and scale; the constraint that binds; and the anti-pattern being avoided.

Example: `(settings page | admin table) + (bulk edit | permission change) + (React | Vue) + (enterprise, 50k rows) + virtualised list constraint + no card wall`.
