# Borrowed Skills and Prior Art

A retained record of every external skill, skill suite, and prior-art project this workspace has compared against or borrowed a mechanism from. This is the project-centric companion to two existing records:

- `docs/agents/borrow-audit.md` — the per-skill adopt/reject maintenance map.
- `references/research-basis.md` — the research basis and source index.

Borrowing rule (from `AGENTS.md`): borrow repeatable mechanisms, never leaked prompts, proprietary wording, or surface styling. A permissive license still does not permit copying prompts, brand wording, or surface styling.

## Skill suites and individual agent skills

- **`obra/superpowers`** — the most-copied skill suite in the ecosystem. Borrowed `systematic-debugging` (Iron Law: no fix before root-cause investigation; four-phase loop; three failed fixes means question the architecture; fresh-evidence completion gate), `test-driven-development` (observe RED, minimal GREEN, full suite, mutation check), `using-superpowers` (a capability about operating the suite belongs in its own skill), `verification-before-completion`, `writing-skills`, `brainstorming`, `executing-plans`, `writing-plans`, and requesting/receiving code review. Landed in `noootwo-debug`, `noootwo-tdd`, `noootwo-workflow`, `noootwo-onboard`, `noootwo-product`, and `noootwo-review`. Status: adopted.

- **`pbakaus/impeccable`** (`https://github.com/pbakaus/impeccable`, v4.3.1 / CLI 4.1.0) — source-first design system. Borrowed: engine + context loader separation, source-first workflows, bounded verification, and craft rules for design. Rejected: vendoring the engine/CLI and deterministic scan scripts (fails the budget and cheap-mode criteria). Landed in `noootwo-design`. Status: adopted mechanisms, rejected toolchain.

- **`anthropics/skills`** — `frontend-design` (explicit aesthetic direction, a memorable visual move, strong typography, deliberate motion, avoid generic AI aesthetics) and `webapp-testing`. Landed in `noootwo-design`. Status: adopted for design; no mechanism taken from `webapp-testing`.

- **`mattpocock/skills`** — writing-for-agents authoring standard with enforced budgets. Landed in ADR 0006 and `docs/agents/skill-authoring.md`. Status: adopted.

- **`dzhng/deep-research`** — breadth-first fan-out, then depth into the survivors, with one capped follow-up round. Landed in `noootwo-research` `research-method.md`. Status: adopted.

- **`mvanhorn/last30days`** — recency window for "current" claims, multi-source aggregation, engagement over volume. Landed in `noootwo-research` `research-method.md` and `source-pools.md`. Status: adopted.

- **`feitangyuan/motion-web`** (`https://github.com/feitangyuan/motion-web`, CC BY-NC 4.0) — motion as a main material, "a great mechanic on a default page is a failed page", stillness ratio as a timeline signal rather than an easing problem, and following lag as `speed / k`. Landed in `noootwo-design` motion language. Status: adopted mechanisms only; no SKILL/cases/scripts/assets copied.

- **`DietrichGebert/ponytail`** (`https://github.com/DietrichGebert/ponytail`, MIT) — seven-rung minimal-code review ladder and lean-review tags. Vendored as a `SOURCE.md` record only, not the full repo. Landed in `noootwo-review` lean-review lens. Status: adopted.

- **`OpenAI Product Design` plugin** (private) — minimum brief, project-local product context, Explore/Design/Build boundary, existing-flow audit, and "screenshots are not QA by themselves". Landed in `noootwo-product` and the product-to-design handoff. Status: adopted mechanisms; plugin structure/prompts not copied.

- **`LottieFiles/motion-design-skill`** — timing, easing, choreography, registers, and the three-layer model. Landed in `noootwo-design` motion language. Status: adopted.

- **`kylezantos/design-motion-principles`** — the frequency gate and the audit stance for motion. Landed in `noootwo-design`. Status: adopted.

- **`Meet-Miyani/compose-skill`** — Compose animation APIs, `AnimationSpec`, and local-state rules. Landed in `noootwo-design`. Status: adopted.

- **`199-biotechnologies/motion-dev-animations-skill`** — spring physics and gesture work. Landed in `noootwo-design`. Status: adopted.

- **`bendrape1-byte/silk-design`** — consistency as a craft mechanism. Borrowed the consistency mechanism; rejected its "never ship a static page" default. Landed in `noootwo-design`. Status: counterexample.

- **`ddruids/mobbin-skill`**, **`dembrandt`**, **`designlang`**, **`tinte`** — design prior art compared during the design skill passes. Landed in `noootwo-design`. Status: compared.

- **`gskinnerTeam/flutter-wonderous-app`** (`https://github.com/gskinnerTeam/flutter-wonderous-app`) — real-app motion and animation evidence. Landed in `noootwo-design` `evidence.md`. Status: evidence source.

- **`antfu/skills`**, **`vercel-labs/skills`**, **`vuejs-ai/skills`**, **`flutter/agent-plugins`** — skill collections and plugin ecosystems compared for packaging and discovery. Landed in `references/research-basis.md`. Status: compared.

## Repos borrowed as mechanism (not agent skills)

- **`shadcn-ui/ui`** (`https://github.com/shadcn-ui/ui`, MIT) — cloneable product source for token, component anatomy, and state behaviour. Landed in `noootwo-design` translation guidance. Status: adopted.

- **`material-foundation/material-color-utilities`** (`https://github.com/material-foundation/material-color-utilities`) — color-engineering reference (OKLCH/HCT as practical tools, not mandatory dependencies). Landed in `noootwo-design` craft guidance. Status: adopted.

## Local installed skills (mechanism sources, not shipped)

These informed mechanism design but were never copied into the workspace.

- **Superpowers local skills**: `using-superpowers`, `systematic-debugging`, `verification-before-completion`, `writing-plans`, `requesting-code-review`, `writing-good-tests`, `brainstorming`, `executing-plans`, `optimize`, `audit` — hard gates, red flags, output contracts, verification-before-completion, and progressive disclosure.
- **`pua` / `pua-debugging`** — a motivation layer, not a method; it names `superpowers:systematic-debugging` as its paired method. Borrowed the anti-rationalization table and the structured exit report. The coercive rhetoric and level system were not borrowed.
- **bundled `documents` skill** — render/test evidence before completion claims.
- **`Kungfu`** — JSON Schema and hash bindings; **`TRACE`** — append-only NDJSON; **`Claude Code` SessionStore** — append/load session state; **`mnemo`** — JSONL source plus Markdown projection. Landed in `noootwo-state` persistence design.

## Methodology and practice sources (not skills)

Borrowed as ideas, not as skill bodies: Diataxis (docs layering), Nygard-style ADRs, Google Engineering Practices and GitHub review guidance, Martin Fowler / refactoring.com (behavior-preserving refactors, internal quality), DORA small-batch delivery, Shape Up, Google Ventures Design Sprint (map/sketch/decide/prototype/test convergence), producttalk Opportunity Solution Trees, NN/g AI-design study guide, and Microsoft Human-AI Interaction guidelines.

## Reference pools (evidence sources, not skills)

Design galleries, design systems, and product-flow libraries used as evidence pools: Apple HIG, Material 3, Fluent 2, IBM Carbon, Atlassian, Ant Design, Semi, Arco, TDesign, Vant, NutUI, Shopify Polaris, GitHub Primer, Mobbin, Refero, Siteinspire, ScreensDesign, Pttrns, Appshots, Awwwards, Savee, Codrops, Motion, GSAP, Rive, easings.net, cubic-bezier.com, transitions.dev, Animata, React Bits, and the domestic fallback set (MasterGo, 即时设计, UI 中国, 站酷, 花瓣, 掘金, B 站, 小红书, V2EX).

The authoritative adopt/reject detail and license boundaries live in `docs/agents/borrow-audit.md`; the per-domain source pools and reachability notes live in `skills/noootwo-research/references/source-pools.md`.
