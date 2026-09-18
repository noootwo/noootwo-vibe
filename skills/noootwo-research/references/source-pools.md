# Source Pools

Where to look, by domain, and what to do when a pool is unreachable. Sources are evidence pools, not templates.

## Access record

Record source access before drafting a `deep` brief:

- Foreign pools tried: URL, access result, and whether artifacts or screenshots were visible.
- Fallback pool used: URL, access result, and evidence level.
- Evidence captured: screenshot path, repository URL, product page, design system URL, benchmark, or an explicit limitation.

If no URL, screenshot, artifact, or platform documentation can be recorded, the pass has no evidence and must not produce a brief that claims to decide something.

## Design and UI

Probed 2026-09-17 by HTTP request and by rendering each page in a real headless browser. Reachability is what this probe observed; re-check it in your own pass and record the result, because a source can change without notice.

### Agent skills and plugin prior art

- **OpenAI Product Design plugin** — accessible in the local plugin cache for this workspace. It is a private plugin, not a copyable skill. Borrow its mechanisms and description technique: minimum brief, project-local product context, Explore / Design / Build boundary, existing-flow audit, and the rule that screenshots are not QA by themselves. Do not copy its plugin structure, Sites/Browser workflow, prototype templates, prompts, or brand wording. Use it primarily when changing `noootwo-product` or the product-to-design handoff.
- **`feitangyuan/motion-web`** — reachable at `https://github.com/feitangyuan/motion-web`, licensed CC BY-NC 4.0. Borrow mechanisms and ideas only: motion is a main material, a great mechanic on a default page is a failed page, stillness ratio is a timeline signal rather than an easing problem, and following lag is `speed / k`. Do not copy its SKILL, cases, scripts, assets, or prompts into a commercial skill.

Order the search by what survives without a subscription, and treat the domestic pool as first-class rather than as a consolation.

Order the search by what survives without a subscription, and treat the domestic pool as first-class rather than as a consolation.

### Product flows and app screens

- **Free and reachable without a login** — ScreensDesign (`/explore/` and its screen-type, flow, and element indexes). Real mobile app screens with direct image URLs. No free agent interface; capture in a browser.
- **Free with an account** — Pttrns (mobile patterns), Appshots (flows and apps). Both gate the library behind a signup; a logged-in browser session is enough.
- **Free preview only** — Refero. Anonymous search returns real results and then gates the remainder behind a login. Its MCP is a paid plan, so treat it as human-facing evidence.
- **Paid and agent-native** — the Mobbin MCP (`https://api.mobbin.com/mcp`, Pro and above) and the Refero MCP (`https://api.refero.design/mcp`). The Mobbin free tier explicitly excludes search, flows, and MCP. Use these only when the user already has access; the free path must not depend on them.
- **Blocked, do not plan around** — Screenlane, Page Flows, Land-book, and UXArchive answer with a Cloudflare challenge that a real headless browser also fails to clear. `minimal.gallery` does not resolve. Record them as unreachable rather than as candidates.

### Web, campaign, and art direction

- **Free and agent-readable** — the Siteinspire MCP at `https://www.siteinspire.com/api/mcp`. It answers without credentials, exposes eight read-only tools, and returns real screenshot URLs; its robots file allowlists user-directed agent user agents on that path. Its coverage is websites and marketing surfaces, not in-app product screens.
- **Free and human-facing** — Awwwards, Savee, Recent (formerly Godly), Httpster, Landingfolio, Interface In Game, Collect UI. Browse or capture them in a browser; none publishes an agent interface.

### Product craft, design systems, and real product code

This tier decides product UI when no case library is reachable, and it is the only tier that always works offline.

- **Design systems and platform guidance** — Apple HIG, Material 3, Fluent 2, Shopify Polaris, GitHub Primer, IBM Carbon, Atlassian, Ant Design, Semi, Arco, TDesign, Vant, NutUI.
- **Publish status of `llms.txt`** — only Ant Design serves a genuine `llms.txt`. Polaris, Fluent 2, TDesign, Semi, 即时设计, and MasterGo return an application shell or a 404 at that path, so do not describe them as agent-indexed.
- **Cloneable product source** — reading the real implementation outranks a screenshot for tokens, component anatomy, and state behaviour. Permissive or readable examples: shadcn/ui (MIT), Supabase (Apache-2.0), Appsmith (Apache-2.0), Grafana (AGPL-3.0), Plane (AGPL-3.0), Outline, Chatwoot, Directus, n8n.

### Motion and native craft

Probed 2026-09-17. Decide the register before searching: a source only transfers inside its own register, and the register rule lives in the design skill's `references/motion.md`.

- **Published platform values** — Material 3 motion overview, easing-and-duration, transitions, transition patterns, and the M3 Expressive motion theming article; Apple HIG motion. All reachable, all carrying real duration, easing, and spring values. The Carbon motion page is currently unreachable; do not cite it.
- **Libraries that publish agent-readable indexes** — Motion (`motion.dev/llms.txt`), GSAP (`gsap.com/llms.txt`, docs served as markdown), Aceternity UI (`ui.aceternity.com/llms.txt` plus a JSON catalog at `ui.aceternity.com/api/components` reporting component counts and a last-updated date), Magic UI, React Bits, Animata (`animata.design/llms.txt`, open source and shadcn-installable), and 21st.dev. All reachable and genuine as of the probe; these are index files, not marketing pages.
- **Curated demos and interaction showcases** — Codrops, Awwwards, Savee, Recent, Dribbble. Human-facing; capture in a browser.
- **Restrained and designed register** — easings.net, cubic-bezier.com, transitions.dev, and the published demos of vaulted primitives such as Vaul and Sonner. Use these when the target is Quiet or Present rather than Expressive.
- **Distilled skills worth imitating** (MIT, read before writing a motion language): `LottieFiles/motion-design-skill` for timing, easing, choreography, registers, and the three-layer model; `kylezantos/design-motion-principles` for the frequency gate and the audit stance; `Meet-Miyani/compose-skill` for Compose animation APIs, `AnimationSpec`, and local-state rules; `199-biotechnologies/motion-dev-animations-skill` for spring physics and gesture work; `bendrape1-byte/silk-design` for consistency as a craft mechanism, and as a counterexample to motion-by-default.
- **Unreachable from this environment** — `react-spring.dev` does not resolve, `developer.chrome.com` View Transitions docs do not resolve, LottieFiles and Uiverse return 403, and `motion-primitives.com` rate-limits. Use the platform's own documentation for view transitions instead of citing a blocked page.
- **Implementation references** — Motion, GSAP, Rive, Flutter Wonderous, SwiftUI animation docs, Jetpack Compose state-animation docs.

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
