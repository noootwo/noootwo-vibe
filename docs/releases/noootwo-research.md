# noootwo-research Releases

## v0.4.0

- Deep briefs now persist through `noootwo-state` instead of `.noootwo/research/<slug>.md`, and durable findings hand off to the state skill.

## v0.3.0

- Added OpenAI Product Design plugin and `feitangyuan/motion-web` to the prior-art source pool with licence boundaries.
- Reframed source pools as a broader prior-art map for the whole Noootwo suite, not only design and motion.
- Sharpened the description toward "whether to borrow a public skill".

## v0.2.0

- Reordered the design and UI source pools by what survives without a subscription, with a domestic-first emphasis, and recorded the access probe of 2026-09-16 and 2026-09-17.
- Recorded which product-flow libraries are free without a login, which need an account, which are preview-only, which are paid, and which are blocked by a Cloudflare challenge that a real browser also fails to clear.
- Added the motion and native craft pool: published Material 3 and Apple HIG motion values, and the public motion skills worth imitating.
- Corrected a metadata claim: only Ant Design publishes a genuine `llms.txt` among the design systems checked; the others return an application shell or a 404 at that path.
- Expanded the motion pool: libraries that publish genuine agent-readable indexes (Motion, GSAP, Aceternity UI with its JSON catalog, Magic UI, React Bits, Animata, 21st.dev), curated demonstration sites, restrained-register references, and the sources this environment cannot reach.


## v0.1.0

- Initial public skill: settle a decision that only outside evidence can settle, or say plainly that the evidence does not.
- Fires on a named decision, not on a topic: the pass states what would flip the answer and what would leave it unchanged.
- Three cost dials: `quick` and `standard` answer in the conversation; `deep` writes `.noootwo/research/<slug>.md` and requires visible artifacts.
- Owns the shared source pools moved out of `noootwo-design` — design and UI, product and market, tech stack, community signal — plus the access record and the fallback ladder.
- Added `tech-selection.md` for library and stack choices, and `borrow-audit.md` for surveying existing skills and public prior art.
- Verification rules: two independent sources for any deciding claim, recency for "current" claims, artifacts over prose, and a counterexample hunt.
- The design-specific discovery flow stayed in `noootwo-design` as `design-discovery.md`; this skill supplies the sources and the method.
