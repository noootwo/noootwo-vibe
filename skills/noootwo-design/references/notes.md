# Design Working Notes

Research notes and cost boundaries behind the design workflow.


## Case Capture And Motion Notes

Recorded 2026-09 after a research pass over public design skills, a live-source extraction probe, and an access test of the free case libraries. Use this note when changing the reference-capture path, the motion language, the extractor, or the readiness gates.

### What The Failure Was

Two linked gaps, both measured on this worktree before the change:

- Direction came from the built-in style lineages rather than from real cases, so a direction could be justified by a seed name alone.
- Motion was contract-shaped and content-free: the Motion section of `design-tokens.md` was eight `TBD` fields, `system.md` named the fields without reference values, `craft.md` carried motion only as aphorisms, `check_visual_gates.py` had zero motion rules, and no eval scenario targeted motion. The `translate.md` motion citation pointed at a Carbon page that now returns HTTP 000.

### Access Test Results

Measured 2026-09-16 to 2026-09-17 from this machine, by HTTP probe and by rendering each page in a real headless Chrome:

- Free and reachable without a login: ScreensDesign `explore/` pages, which show real mobile app screens by screen type with direct image URLs.
- Free with an account: Pttrns, which now states its full pattern library is free.
- Free to preview: Refero, which returns real search results anonymously and then gates further pages behind a login.
- Free but web-only: the Siteinspire MCP endpoint at `https://www.siteinspire.com/api/mcp`, which answers without credentials, exposes eight read-only tools, and returns real screenshot URLs. Its robots file allowlists user-directed agent user agents for that path.
- Blocked: Screenlane, Page Flows, Land-book, and UXArchive return a Cloudflare challenge that a real headless browser also fails to clear. `minimal.gallery` does not resolve.
- Paid and agent-native: the Mobbin MCP, available on Pro and above with the free tier explicitly excluding search, flows, and MCP; and the Refero MCP, which requires a paid plan.
- Corrected metadata claim: among the design systems checked, only Ant Design publishes a genuine `llms.txt`. Polaris, Fluent 2, TDesign, Semi, Arco, 即时设计, and MasterGo return an application shell or a 404 at that path.

### Mechanisms Borrowed

- **Case querying and batching** — from `ddruids/mobbin-skill` (MIT): write queries as what is visible on screen, resolve the platform, route screens separately from flows, and record observations after every two or three queries. The batching rule exists because screens are large enough to be dropped from context before they are written down.
- **Real-value capture** — from `dembrandt` and `designlang` / `design-extract` (both MIT): render the page, read computed styles from the DOM, and emit colour, type, spacing, shape, motion, and breakpoint values as tokens, with an optional DTCG export.
- **Drift gate** — from `dembrandt`: keep a baseline and compare against it after the build rather than trusting that the tokens survived.
- **Motion language** — from `LottieFiles/motion-design-skill` (MIT): three motion layers, four personality archetypes with concrete durations and curves, an element-based duration table, distance scaling, entering longer than exiting, a choreography budget, and a troubleshooting table.
- **Frequency gate and audit stance** — from `kylezantos/design-motion-principles` (MIT): ask how often the interaction is triggered before animating it, and treat reduced motion as mandatory rather than optional.
- **Native motion vocabulary** — from `Meet-Miyani/compose-skill` (MIT): the Compose API-selection and `AnimationSpec` tables, and the rule that animation state stays local UI state instead of entering a ViewModel or reducer.
- **Reference lock and anti-averaging** — from the public Refero agent skill (MIT): lock the build target before drafting, and let one reference dominate instead of averaging several into a safe middle.

### Rejected

- **Monet.Design as a case source** — it is described as an open-source Mobbin successor but is a registry of React components, which is the component-library category this suite deliberately treats as a fallback rather than a design source.
- **Paid MCP endpoints** — the free path must work without a subscription, so Mobbin Pro and the Refero MCP are recorded as optional accelerators only.
- **Adopting dembrandt, designlang, or Playwright as required dependencies** — the extractor reproduces the mechanism with the Chrome already on the machine and Node's built-in WebSocket.
- **Copying the Mobbin skill's tool names** — those tools belong to an MCP this suite does not ship.

### Motion Source Pool Notes

Added after the first motion pass, because a motion language without sources of ideas still asks the agent to invent.

Probed 2026-09-17: several motion and component libraries publish genuine agent-readable indexes rather than marketing pages. Motion serves `motion.dev/llms.txt`; GSAP serves its documentation as markdown under `gsap.com/llms.txt`; Aceternity UI serves both an index and a JSON catalog at `ui.aceternity.com/api/components`, reporting 111 components, 176 examples, and a last-updated date; Magic UI, React Bits, Animata, and 21st.dev each serve an index file as well. That is the cheap path to real motion ideas: read the index, open a few examples in the target register, and record the mechanism.

Curated demonstration sites stay human-facing: Codrops, Awwwards, Savee, Recent, and Dribbble. Capture them in a browser like any other reference.

**Register is the correction that keeps this honest.** The first motion pass carried personality archetypes and a frequency gate, both of which push toward restraint. On a marketing or portfolio surface that push is wrong: motion is part of the product there. So motion now names a register — Invisible, Quiet, Present, Expressive, Theatrical — set by the surface rather than by the mood, with product UI defaulting to Quiet and Theatrical requiring an explicit decision.

`bendrape1-byte/silk-design` (MIT) is the counterexample kept on purpose. It reaches for motion by default and states "never ship a static page", which is right for the surfaces it targets and wrong as a universal rule. Its transferable mechanism is consistency: one reveal configuration reused everywhere is what reads as craft. Its default is not adopted.

Two sources that this environment cannot reach are recorded rather than silently cited: `react-spring.dev` does not resolve, and the View Transitions documentation on `developer.chrome.com` does not resolve either. LottieFiles and Uiverse return 403, and `motion-primitives.com` rate-limits.

### Extractor Boundary

`scripts/extract_design_tokens.mjs` needs Node 22 or newer and a local Chrome. It drives Chrome over the DevTools Protocol, evaluates a collection function in the page, then hovers up to three interactive elements to record the deltas. Verified end to end against a foreign product site and a domestic design system: unusual font weights, sub-pixel letter spacing, thousands-scale radii, multi-value transitions, and hover colour swaps all survive the extraction.

When Node or Chrome is missing, the pass degrades to screenshots plus a recorded limitation. It never substitutes invented values for observed ones.

### Cost Boundary

- `quick`: no capture, no motion contract, no extractor.
- `standard`: motion contract applies; reference capture does not.
- `deep`: capture, extractor, reference lock, and the full motion contract apply.
- `production`: the motion contract is checked before handoff, and the artifact is compared against the captured values.
- Automated motion findings stay advisory and need a screenshot or DOM confirmation before they change a review decision.

### Verification Plan

Four motion scenarios and four case-capture scenarios live under `evals/prompts/`. The readiness validator reads `.noootwo/reference-board.md` per source and the Motion section of `.noootwo/design-tokens.md` field by field when `--deep-mode` or `--implementation-gate` is passed.


## Workflow Research Notes

Use this note when changing Noootwo Design's workflow, review gates, AGENTS integration, or public claims.

### Sources Reviewed

- Figma resource library and blog material on design systems as shared source of truth, workflow alignment, prototype validation, and implementation drift.
- Smashing Magazine articles on UI critique, prototype review, and design-to-development loss of detail.

### Mechanisms Borrowed

- Externalize uncertainty before implementation rather than letting it remain implicit in the model.
- Use compared directions and reviewable artifacts as decision objects.
- Treat critique as part of the production loop, not only as a final score.
- Preserve design intent through explicit implementation contracts and drift checks.

### Why These Changes Belong In Noootwo Design

- The repeated failure mode was not missing inspiration; it was skipping exploration, communication, and verification.
- A task-structure protocol is more robust than adding case-by-case prompt clauses.
- Artifact-first review is the most reliable way to catch layout defects, typography drift, and generic fallback before handoff.

### Risks And Counterexamples

- Over-structuring small tasks can slow down minor polish work.
- Long questionnaires reduce velocity and often do not improve outcomes.
- Requiring deep exploration for every design request would make the skill too expensive for ordinary tasks.

### Cost Boundary

- `quick` keeps a lightweight path and should not absorb deep exploration costs.
- `standard` pays for brief + direction + decision + artifact + review when the task is direction-sensitive.
- `deep` pays for stronger source discovery and stronger evidence.
- `production` pays for contract-to-implementation preservation and drift checks.

### Verification Plan

- Validator checks workflow closure rather than only file existence.
- Eval prompts target generic failure modes rather than specific surface categories.
- Review templates require artifact evidence, findings, decision, and return action.

### Source Notes

- Figma emphasizes that design systems act as a shared source of truth between design and engineering, reducing drift during implementation and review.
- Figma guidance on UX validation recommends keeping documentation visual and tied to a working prototype whenever possible.
- Smashing Magazine critique guidance supports recurring, structured critique throughout the product process rather than only at the end.
- Smashing Magazine's design-to-technology case study explicitly warns that static documents alone lose detail across the handoff chain.


## Plugin Architecture Notes

Use this note when changing how `noootwo-design` fits inside `noootwo-vibe`.

### Current State

- `noootwo-design` is one public child skill under the `noootwo-vibe` workspace.
- The repository root has no `SKILL.md` so default skill discovery lists all public child skills.
- Design-specific references, scripts, assets, and eval prompts live inside `skills/noootwo-design/` so the design skill can be installed or published independently.
- Former public design child skills are now internal Noootwo Design responsibilities:
  - style discovery
  - artifact review
  - detail translation

### Mechanisms Preserved

- Keep one design front door that classifies design work.
- Keep high-cost research and detail-preservation flows optional and mode-bound.
- Share design resources inside the `noootwo-design` skill package, not at the monorepo root.
- Split future design artifact families only when the artifact contract, evidence surface, or review gates materially differ.

### Boundaries

- Do not reintroduce `noootwo-style-discovery`, `noootwo-design-review`, or `noootwo-detail-translation` as public skills without an explicit product decision.
- Do not move design harness scripts back to the workspace root; that would break single-skill publishing.
- Do not add root compatibility `SKILL.md`; that would hide child skills in default `skills` CLI discovery.


## Plugin Vs Skill Research Notes

Use this note when deciding whether a Noootwo capability should become a public skill, an internal reference, or an integration/plugin.

### Stable Distinction

- `skill`: reusable workflow, sequencing, review, formatting, or judgment.
- `plugin/integration`: external tool access, app connection, MCP server, or connected data source.
- `AGENTS.md`: short always-on project guidance and routing hints.

### Current Noootwo Vibe Decision

Noootwo Vibe publishes five workflow skills:

- `noootwo-workflow`
- `noootwo-product`
- `noootwo-design`
- `noootwo-review`
- `noootwo-docs`

Noootwo Design remains a skill because its value is workflow and judgment, not external system access. If future design work needs Figma, Slides, Drive, asset search, or other connected systems, add those as integrations around the skill family instead of making the design skill a giant tool manual.

### Split Test

Before adding any new public skill, require a clear yes for most of these:

- It has a distinct workflow contract.
- It has a distinct review or evidence surface.
- It reduces trigger ambiguity or context weight.
- It is reusable across many prompts.
- It can be validated independently.

If not, keep the behavior as an internal reference or mode inside an existing skill.


## Workflow Cost Model

Use this to prevent Noootwo Design from becoming too expensive for ordinary UI work.

### Modes

- `quick`: local polish. No source mining, no 3 directions, no spike comparison, no full harness completion. Use current UI, existing system/tokens when present, and one artifact or screenshot when available.
- `standard`: normal UI design. Light calibration, 3 directions, 1 artifact, typography and responsive review before ready.
- `deep`: high-end, niche, brand-heavy, Claude Design-like, or major redesign work. Source accessibility, evidence-backed discovery, 2-3 artifact spikes, screenshot comparison, typography and responsive gates.
- `production`: approved design implementation. Token mapping, stack playbook, screenshot or preview acceptance.
- `detail-translation`: not a standalone mode. It is an implementation-stage reinforcement layer for surfaces that otherwise drift back to defaults.
- `adopt-project`: first use in an existing project. Capture baseline and constraints before redesigning.

### Cost Controls

- Do not run deep mode just because a task is visual.
- Do not bootstrap or complete the entire `.noootwo/` harness for quick polish.
- Do not add a new mode for full redesign. Use the full redesign checkpoint inside `deep` or `adopt-project -> deep`.
- If the user asks for minor polish or to preserve the current system, use `quick`.
- If the user path, feature scope, interaction model, states, or acceptance criteria are unclear, route to `$noootwo-product` before design escalation.
- If the user asks to redo all UI or abandon the current visual language, the cost of discovery and user direction selection is intentional. Stop at the direction menu before implementation.
- For non-quick UI implementation, the approved design spec and implementation plan are intentional cost controls. They are cheaper than reworking a bad UI after code is written.
- Use the detail-translation layer only for implementation-bound work, production review, or post-review drift. Do not make it the default cost of quick polish or early direction exploration.
- Use readiness validation for delivery and handoff confidence, not as the first step of ordinary UI work.
- Skip the spec/plan gate only for quick polish, explicit handoff-only work, or explicit user approval to proceed without the gate.
- If time or environment blocks source mining, screenshots, or target-stack previews, record the limitation and reduce readiness confidence.
- If only 1 deep spike is possible, mark the exploration as low-confidence and do not claim full territory comparison.
- Prefer existing project preview tools before adding new dependencies.

### Escalation

Escalate from standard to deep only when the user asks for strong taste, niche/high-end direction, brand shift, or a previous standard result was too generic.

De-escalate from deep when the user prioritizes speed, implementation certainty, or staying close to an existing shipped interface.

## Product Design And Motion Web Borrow Notes

Recorded 2026-09-18 after comparing the OpenAI Product Design plugin and `feitangyuan/motion-web` with the current skill. The full suite map lives in `docs/agents/borrow-audit.md`.

### What Is Borrowed

- Product Design's Explore / Design / Build boundary and Source Fidelity QA are added only where they fit Noootwo's project-local model. `replicate` is a reference intent, not the default; `borrow-mechanism` stays the default.
- motion-web's "still frame and motion are co-equal completion criteria" and "stillness ratio is a timeline signal" are rewritten into `motion.md` and a light optional probe in `extract_design_tokens.mjs`.

### What Is Rejected

- Product Design's global user context, Sites/Browser-specific workflow, prototype templates, and share/deploy paths.
- motion-web's full cases, scripts, assets, and Playwright oracle suite; the source is CC BY-NC 4.0 and out of cost scope.

### Cost Boundary

- The new motion probe is optional and only used for motion-heavy or explicitly diagnostic passes.
- Source Fidelity QA runs only for `Reference intent: replicate`.
- No new required dependency or reference file is added.
