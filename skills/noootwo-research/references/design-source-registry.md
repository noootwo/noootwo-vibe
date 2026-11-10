# Design Source Registry

The design-specific source matrix. It classifies a source by what it can prove, not by how popular or visually impressive it looks. Read this with `source-pools.md` whenever a UI decision needs external evidence.

## One Primary Role

Give every source one primary role for the current decision. A source may have secondary roles, but it cannot borrow authority from a role it does not carry.

| Role | What it can decide | What it cannot decide |
| --- | --- | --- |
| `product evidence` | Real screens, flows, states, density, and interaction conventions used by a shipped product | Brand originality, the final visual direction |
| `platform convention` | Platform structure, accessibility expectations, navigation, controls, and native behaviour | A distinctive aesthetic, a specific product layout |
| `visual direction` | Composition, type scale, material, colour proportion, editorial rhythm, and atmosphere | Product flow, information architecture, dense workbench behaviour |
| `motion mechanism` | Trigger, moving property, duration, curve, layer relationship, and state meaning | Complete product flow, the whole visual direction |
| `implementation resource` | Feasible components, state anatomy, accessibility plumbing, dependencies, and code cost | Aesthetic evidence, brand judgment, information architecture |
| `asset source` | Font, icon, image, illustration, or 3D availability and licence | UI structure, product flow, the design direction |
| `research craft` | User, language, accessibility, and design rules backed by evidence | A specific visual style |

## Lane Matrix

The first source in each lane is a seed, not a mandatory dependency. Re-probe access before treating it as current. A lane needs more than one viable option so a blocked site does not cancel the pass.

| Lane | Seed sources | Main strength | Boundary |
| --- | --- | --- | --- |
| Product evidence | Mobbin (paid MCP; optional), Refero (free preview; paid MCP), ScreensDesign, Pttrns, Appshots, Siteinspire for web/marketing, real product screenshots and product repositories | Real screens, flows, states, and conventions | A source showing that a product used a pattern does not prove the pattern improved an outcome |
| Platform convention | Apple HIG, Material 3, Fluent 2, IBM Carbon, Shopify Polaris, GitHub Primer, Atlassian, Ant Design, Semi, Arco, TDesign, Vant, NutUI | Platform rules, accessibility, component behaviour | Not a source of distinctive visual direction |
| Visual direction | Awwwards, Framer Gallery, Recent, Savee, Httpster, Landingfolio, Interface In Game, Collect UI | Composition, typography, material, colour proportion, art direction | Not product-flow evidence; web and portfolio bias is common |
| Motion mechanism | Motion, GSAP, Codrops, React Bits, Vue Bits, Magic UI, Animata, Aceternity UI, 21st.dev, Shaders, Paper Shaders, transitions.dev, easings.net, Rive, Lottie | Motion recipes, timing, curves, layers, authored assets | A demo is evidence of craft, not of fit; check platform, dependencies, reduced motion, and licence |
| Implementation resource | shadcn/ui, Radix, Base UI, MUI, Chakra UI, Mantine, HeroUI, Flutter/SwiftUI/Compose primitives | Component anatomy, states, accessibility, implementation cost | Never the primary aesthetic evidence; library defaults can create generic UI |
| Asset source | Fontshare, Fontsource, Google Fonts with fallback, Lucide, Phosphor, Heroicons, Tabler, SF Symbols, Material Symbols, Unsplash, Pexels, Openverse, Spline, Rive, Lottie | Fonts, icons, photography, illustration, 3D assets | Not UI structure; verify licence, attribution, commercial use, and access before shipping |
| Research craft | NN/g, Baymard, W3C/WCAG and COGA, GOV.UK content design, official platform documentation | User, language, accessibility, and interaction rules | Evidence about a rule is not a visual direction |
| Domestic fallback | MasterGo, 即时设计, UI 中国, 站酷, 花瓣, 掘金, B 站, 小红书, V2EX | Reachable local examples and current community signals | Social and portfolio posts are weak signals until confirmed by an artifact or a second source |

## Dynamic Source Probe Record

Probed from this machine on 2026-11-11. HTTP status is only an access signal; the artifact, role, and limitation still decide whether the source can be used. Re-probe before a current decision or a release claim.

| Source | Role | Surface / platform | Access | Evidence | Licence / reuse | Strength | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Framer Gallery | visual direction | Websites, portfolios, marketing; Web | free; `?md` returned `200 text/markdown` | curated gallery of websites built in Framer | reference only; no asset reuse | composition, type, imagery, small interaction ideas | no app-screen taxonomy or structured flow search |
| Awwwards | visual direction; motion mechanism | Web campaigns, editorial, portfolios | free human-facing; `llms.txt` returned `200 text/plain`; gallery/search routes disallowed by robots | award showcase plus limited annual-awards API | reference only; no asset reuse | art direction, motion, current web craft | annual API is not complete product-flow evidence |
| Recent | visual direction | Web, interface, branding, motion | free human-facing; page returned `200 text/html`; no `llms.txt` | curated gallery | reference only; content signal permits reference use, not AI training | broad current visual signal | no structured flow or agent search |
| React Bits | motion mechanism; implementation resource | React Web, expressive marketing/portfolio | free; `llms.txt` returned `200 text/plain`; Pro tier is paid | component demos and copy-in source | MIT + Commons Clause; no redistribution/resale; do not vendor | motion recipes, micro-interactions, implementation examples | not a product-flow source, not Vue/Flutter/native replacement, not default product UI |
| Thrine | unclassified candidate | identity unresolved | `thrine.app` reset the connection; `thethrine.com` returned `200 text/html` | 3D tool/studio sites, not inspected as product evidence | do not use until identity and licence are confirmed | possible 3D asset/tool or web/portfolio lead | not canonical; no design evidence yet |
| Mobbin | product evidence | Mobile/web apps and websites | paid; `llms.txt` returned `200`; MCP Pro+, REST Team+, 60 req/min | structured screens, flows, sections, shipped products | reference only; no copying protected designs/assets | real screens and multi-step flows | paid access; a used pattern does not prove effectiveness |
| Refero | product evidence | Web and iOS products | free preview; paid MCP; page returned `200`; `llms.txt` returned `200` | styles, screens, flows, patterns, metadata | reference only; no asset reuse | structured screen and flow search | MCP requires a paid plan; preview is not full retrieval |
| ScreensDesign | product evidence | Mobile app screens | free; prior probe reachable | real mobile screens by type/flow/element | reference only | free direct captures | mobile bias; no full design rationale |
| Pttrns | product evidence | Mobile patterns | free with account | mobile pattern library | reference only | pattern anatomy | login required; weak for web/admin |
| Appshots | product evidence | Mobile app flows | free with account | app screens and flows | reference only | flow capture | login required; limited task context |
| Siteinspire | product evidence | Websites and marketing | free MCP endpoint; prior probe reachable | real website screenshots | reference only | web/marketing screen reference | not in-app product flow |
| Savee / Httpster / Landingfolio / Interface In Game / Collect UI | visual direction | Web, portfolios, game UI | free human-facing | curated galleries | reference only | composition and atmosphere | weak for dense product workflows |
| Motion / GSAP / Codrops / transitions.dev / easings.net | motion mechanism | Web, React/Vue/JS | free docs and demos; verify package licence | timing, curves, interaction recipes | per package; docs reference only | concrete motion mechanics | libraries are not evidence of product fit |
| Vue Bits / Magic UI / Animata / Aceternity / 21st.dev | motion mechanism; implementation resource | React/Vue Web | free or mixed; verify each registry item | component demos | per component; no blind vendoring | platform-specific implementation | expressive bias; dependency and licence drift |
| shadcn/ui / Radix / Base UI / MUI / Chakra / Mantine / HeroUI | implementation resource | React/Web | free; verify package dependencies | component source and documentation | per package; usually permissive, verify | state anatomy, accessibility plumbing, implementation cost | not visual direction or product flow evidence |
| Fontshare / Fontsource / Google Fonts | asset source | Web/native font delivery | Fontshare and Fontsource returned `200`; Google Fonts timed out in this environment | font files, specimens, licence metadata | per font; OFL, commercial, or custom terms vary | type assets and fallbacks | confirm commercial use and fallback before shipping |
| Lucide / Phosphor / Heroicons / Tabler | asset source | Web, React, Vue, native wrappers | each returned `200` | icon sets and docs | Lucide ISC; Phosphor, Heroicons, Tabler MIT-family; verify package | consistent icon vocabulary | icon style still needs product fit |
| SF Symbols / Material Symbols | asset source; platform convention | Apple platforms / Material platforms | official platform access | platform icon systems and guidance | Apple platform terms; Material Symbols Apache-2.0 | native icon and platform alignment | platform licence and availability differ |
| Unsplash / Pexels / Openverse | asset source | Web/marketing imagery | Unsplash `401`, Pexels `403`, Openverse timed out in this environment | image search and licence metadata | per asset; attribution and model/property terms vary | photography and illustration leads | access is conditional; never assume reuse from a search result |
| Spline / Rive / Lottie | asset source; motion mechanism | Web/native 3D and motion assets | tool/runtime pages are reachable subject to plan; verify per asset | scene, animation, and runtime assets | tool, runtime, and asset licences are separate | 3D, vector motion, authored assets | performance, fallback, and licence checks are mandatory |
| NN/g / Baymard / W3C WCAG and COGA / GOV.UK | research craft | Cross-platform UX, language, accessibility | free articles; some research is paywalled | research and standards | reference only; quote attribution | user, language, and accessibility rules | rule evidence does not choose a visual direction |
| MasterGo / 即时设计 / UI 中国 / 站酷 / 花瓣 / 掘金 / B 站 / 小红书 / V2EX | domestic fallback | CN web, mobile, community | free or mixed; verify each artifact | local examples and discussion | reference only; asset rights stay with the creator | reachable local context | weak signal until confirmed by an artifact or second source |

Official platform documentation (Apple HIG, Material 3, Fluent 2, Carbon, Polaris, Primer, Ant Design, Semi, Arco, TDesign, Vant, NutUI) remains a `platform convention` lane. It is free to read unless the vendor gates a page, but the component package, documentation text, brand marks, and platform assets have separate licences. Version-check the page at implementation time; do not treat this registry review as a substitute for reading the current platform rule.

## User-Named Examples

- **Framer Gallery** — `visual direction` for websites built in Framer. It is useful for composition, type, imagery, and small interaction ideas. It is not an app-screen or flow library. The `?md` representation is readable, but it does not supply a structured screen taxonomy.
- **Awwwards** — `visual direction` and motion showcase. It is useful for web/campaign craft. Its public agent material is limited to annual categories and nominees, and its gallery/search routes have crawler restrictions; do not describe it as a complete product-screen API.
- **Recent** — `visual direction` across web, interface, branding, and motion. It has no structured flow interface. Its content signals permit reference use but do not grant AI-training rights; capture it as a human-facing reference.
- **Thrine** — do not put it in the canonical matrix until the target site is identified. If it is `thrine.app`, treat it as a 3D scene/template tool in the asset/tool lane. If it is `thethrine.com`, treat it as a Web/portfolio visual reference. Neither is product-flow evidence.
- **React Bits** — `motion mechanism` and `implementation resource` for React Web, especially expressive marketing and portfolio surfaces. It is not the default product-UI language, not a Vue/Flutter/native substitute, and its component source must not be vendored.
- **Component libraries** — shadcn/ui, MUI, Chakra, Mantine, Radix, Base UI, and similar libraries are implementation resources. A clean library demo can prove a component is buildable; it cannot prove the product’s visual direction or information architecture.

## Source Record

Every source used in a decision records:

```markdown
- Source:
- Role:
- Surface:
- Audience:
- Platform:
- Access: free | login | paid | unreachable
- Evidence: real product flow | product screenshot | design system | curated gallery | component demo | community signal
- Same-medium fit: yes | mixed | no, and why
- Observed mechanism:
- Strength:
- Limitation / do not transfer:
- Licence / reuse:
- Capture:
- Last verified:
```

For a standard light audition, the source record can be shorter, but `Role`, `Surface / audience`, `Platform`, `Access`, `Observed mechanism`, `Decision`, `Reject reason`, and `Capture` remain required.

## Candidate Intake

A new source becomes a candidate only when all of these are true:

- A real artifact was opened or captured; a star count, README, or search result is not enough.
- The source has at least one repeatable mechanism and one explicit boundary.
- Its surface and platform coverage are recorded.
- Its access result and licence/reuse boundary are recorded.
- A counterexample or failure condition is recorded.

A candidate becomes canonical only after a project uses it, the selected mechanism lands in the artifact, and review records the outcome. Keep failed or blocked sources in the registry as leads with the reason; do not silently delete them.

## Freshness And Access

- Record `Last verified` for every dynamic source.
- Re-probe access when the source can decide a current task.
- Do not make an access or availability claim for a release from a probe older than 90 days.
- Platform documentation still needs a version check at implementation time.
- A paid or login-gated source may be used only when the user already has access. The free path must remain complete.
- Record blocked sources as blocked. Never turn an unreachable source into an invented observation.

## Selection Rules

- Product UI needs at least one `product evidence` source; a gallery can contribute composition but cannot decide the flow.
- Native UI needs at least one native product screenshot or platform source; a web gallery is cross-medium evidence.
- High-frequency operations, settings, and data tables prefer `product evidence`, `platform convention`, and `research craft`; expressive galleries and effect libraries are not default inputs.
- Marketing, campaign, and editorial surfaces may let `visual direction` lead, but product claims still need real product evidence.
- A component library or asset source may be selected after the direction is set; it cannot be the only source behind a visual direction.
- One primary source dominates. A supplement contributes a narrow mechanism; averaging several sources into a safe middle is a failed audition.

## Asset Lane

Assets are recorded separately from visual evidence:

```markdown
- Asset type:
- Source:
- Licence:
- Attribution:
- Commercial use:
- Access:
- Fallback:
```

Prefer user, brand, or product-owned assets. Check the licence for every font, icon set, photograph, illustration, and 3D asset. A gallery screenshot is not a production asset. Generated assets record their generation or commission provenance and still need visual and brand review.

## Known Blocked Or Conditional Pools

- Screenlane, Page Flows, Land-book, and UXArchive have repeatedly produced Cloudflare challenges in this environment; re-probe before planning around them.
- `minimal.gallery` has not resolved in prior probes.
- Google Fonts, Unsplash, and Pexels may be unreachable or rate-limited in a given environment; record the limitation and use an existing brand asset or a reachable fallback.
- Mobbin and Refero search/MCP access is paid; their free previews are not a substitute for structured retrieval.
