# Research Basis

Use this note when changing Noootwo Vibe repository structure, skill packaging, release model, or public workflow claims.

## Local Evidence

- `npx skills add . --list` finds only the root skill when a root `SKILL.md` exists.
- `npx skills add <repo-without-root-skill> --list` finds child skills under `skills/` by default.
- `npx skills add . --list --full-depth` finds child skills even when a root skill exists.
- Single child skill discovery works with `npx skills add ./skills/<skill> --list`.

## External Practice Signals

Checked on 2026-07-03.

- Codex skill anatomy guidance: skills should keep `SKILL.md` concise, use direct `references/`, `scripts/`, and `assets/`, and avoid auxiliary per-skill documentation that adds clutter.
- Diataxis documentation system: separates tutorials, how-to guides, reference, and explanation. Noootwo Vibe adapts this into README, AGENTS, status, ADR, guide, reference, and release layers.
- Architecture Decision Records: Nygard-style ADR practice and the public ADR community repository both support keeping durable architecture decisions short, dated, and separate from operational logs.
- Refactoring practice: Refactoring.com and Martin Fowler's writing on internal quality support small behavior-preserving refactors, evidence-backed code health work, and avoiding speculative rewrites.
- Semantic Versioning and GitHub release/tag practices support independent version files and release tags for separately published child skills.
- GitHub repository rename documentation supports updating local remotes after a repository rename instead of relying on redirects as the durable configuration.

Second-pass non-design skill review, checked on 2026-07-03:

- Agent Skills and Claude skill guidance reinforce progressive disclosure: keep the entry skill focused, route to resources, scripts, and examples only when needed, and evaluate skills against realistic tasks.
- Existing mature local skills such as `using-superpowers`, `systematic-debugging`, `verification-before-completion`, `writing-plans`, `requesting-code-review`, and the bundled `documents` skill show useful mechanisms: strong trigger metadata, non-negotiable gates for fragile work, red-flag lists, explicit output contracts, and render/test evidence before completion claims.
- Diataxis and developer-documentation guidance reinforce documentation by user need and task type rather than by dumping all facts into README.
- Google Engineering Practices and GitHub review guidance support small reviewable changes, clear reviewer expectations, and concrete defect findings over preference-heavy review.
- Fowler's refactoring and internal-quality writing supports behavior-preserving refactors, evidence-backed code-health work, and rejecting speculative architecture without current pressure.

Access note: `https://adr.github.io/` failed during the live check with a TLS connection error, so the ADR signal was verified through `https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions` and `https://github.com/architecture-decision-record/architecture-decision-record` instead.

Source index for the second pass:

- Agent Skills: `https://agentskills.io/`
- Anthropic Claude Code skills: `https://docs.anthropic.com/en/docs/claude-code/skills`
- Diataxis: `https://diataxis.fr/`
- Google Engineering Practices review docs: `https://google.github.io/eng-practices/review/`
- GitHub pull request review docs: `https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests`
- Fowler on internal quality: `https://martinfowler.com/articles/is-quality-worth-cost.html`
- Refactoring: `https://refactoring.com/`

Third-pass project governance enhancement, checked on 2026-07-03:

- Agent Skills and Claude skill documentation continue to support short skill bodies with direct supporting files and realistic task evaluation, which maps to project audits living in `references/` instead of default `SKILL.md` text.
- DORA's small-batch delivery capability supports a workflow that audits foundation, then makes the smallest verifiable process patch instead of generating a full scaffold.
- Diataxis supports separating current state, durable decisions, how-to procedures, and reference facts; this underpins the docs audit categories and first-adoption flow.
- Google Engineering Practices and GitHub review guidance support concrete findings, reviewable change size, and evidence-backed review, which maps to `Project Defects` rather than preference-heavy project commentary.
- Fowler/refactoring practice supports treating internal quality as a cost-of-change issue and rejecting speculative rewrites without current pressure.
- Local mature skills informed the mechanism design: red flags, hard gates, output contracts, verification-before-completion, and progressive disclosure. No wording or full process was copied wholesale.

Source index for the third pass:

- Agent Skills specification: `https://agentskills.io/specification`
- Anthropic Claude Code skills: `https://docs.anthropic.com/en/docs/claude-code/skills`
- DORA working in small batches: `https://dora.dev/capabilities/working-in-small-batches/`
- Diataxis: `https://diataxis.fr/`
- Google Engineering Practices review docs: `https://google.github.io/eng-practices/review/reviewer/looking-for.html`
- GitHub pull request review docs: `https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests`
- Fowler on internal quality: `https://martinfowler.com/articles/is-quality-worth-cost.html`

Fourth-pass debug skill research, checked on 2026-09-14:

- `obra/superpowers` (`skills/systematic-debugging`, plus `root-cause-tracing`, `defense-in-depth`, and `verification-before-completion`) is the most-copied debug skill in the ecosystem. It contributes the Iron Law — no fix before root-cause investigation — the four-phase loop, the rule that three failed fixes mean questioning the architecture rather than attempting a fourth, and a gate against claiming completion without fresh evidence. Its weakness, for this workspace, is that "evidence" stays a process promise: nothing requires the raw output to appear.
- The locally installed `pua` and `pua-debugging` skills are a motivation layer, not a method — `pua-debugging` names `superpowers:systematic-debugging` as the method it pairs with. Two mechanisms transferred: the anti-rationalization table, and the structured exit report (confirmed facts, ruled-out options, narrowed scope, next step, handoff). The coercive rhetoric and the level system did not.
- `ujjwal502/debugduck` contributes the mechanisms that survived into `noootwo-debug`: predict every checkpoint before instrumenting and trace the whole path in one pass, a hypothesis ledger with per-hypothesis refutation, `[observed]`/`[inferred]`/`[assumed]` labels on claims, and the toggle test as the cheapest causality proof. Its `evals/RESULTS.md` is the strongest available measurement: on four seeded bugs with decoys, the no-skill agent reproduced 4/4 and found the true root cause 4/4, while the measured gap appeared in proving the fix (toggle 4/4 vs 2/4; failing-first regression test 3/3 vs 0/3).
- `wshobson/agents` `parallel-debugging` states confirming and falsifying evidence for every hypothesis before investigating it, and `developer-essentials/skills/debugging-strategies` adds symptom-to-first-move routing. The multi-agent topology was not adopted.
- `nai0om/buddhist-method` (name three plausible causes before touching anything) and `summerliuuu/no-no-debug` (log errors, review them, gate before changing code) supplied supporting discipline, not structure.
- `anthropics/skills` publishes no general debugging skill; the nearest is `webapp-testing`. No mechanism was taken from it.

The design consequence recorded here and in [ADR 0007](../adr/0007-add-debug-skill-and-normalize-workflow.md): skill weight goes to proving the cause, proving the fix, and keeping the fix the size of the cause — not to re-teaching reproduction, which current models already perform.

Access note: `raw.githubusercontent.com` intermittently returned empty bodies during this pass, so file contents were read through the GitHub contents API instead. The `pua` family is no longer installed; its `SKILL.md` files were read from the local backup snapshots under `~/.codex/skills_cleanup_backup_*` and `~/.codex/skills_backup_*`.

Fifth-pass borrow audit, checked on 2026-09-14:

Run as part of the `noootwo-research` work recorded in [ADR 0008](../adr/0008-add-research-and-onboard-skills-and-the-capability-bridge.md). The question was not "what is interesting" but "which mechanism prevents a repeated, concrete failure in this suite".

| Mechanism | Source | Failure it prevents | Gate result |
| --- | --- | --- | --- |
| breadth-first fan-out, then depth into the survivors, with one capped follow-up round | `dzhng/deep-research` | reading the first result deeply and locking in the wrong candidate | adopted → `research-method.md` |
| recency window for "current" claims, multi-source aggregation, and engagement over volume | `mvanhorn/last30days` | deciding a "what is popular / advanced now" question from stale training memory | adopted → `research-method.md`, `source-pools.md` |
| package "how to operate this suite" as its own skill instead of hiding it in a router or scheduler | `obra/superpowers` `using-superpowers` | the meta capability becoming invisible and the scheduler accumulating method | adopted → `noootwo-onboard` |
| state confirming and falsifying evidence before investigating | `wshobson/agents` `parallel-debugging` | investigations that can only confirm | already adopted → `noootwo-debug` `hypotheses.md` |
| process skill before implementation skill when two apply | `obra/superpowers` `using-superpowers` | implementation starting before the ordering decision is made | already adopted → `noootwo-workflow` route order |
| hard gate against claiming completion without fresh evidence | `obra/superpowers` `verification-before-completion` | self-reported success | already adopted → `noootwo-debug` Gate B |
| writing-for-agents authoring standard with enforced budgets | `mattpocock/skills` | skill bodies drifting into policy documents | already adopted → ADR 0006 |
| enumerate deterministic detector rules and run them at edit time | `pbakaus/impeccable` | mechanical slop reaching review | rejected: fails the budget and cheap-mode criteria; tracked in ADR 0006 |
| a separate performance skill | ecosystem performance skills are domain packs (WordPress, Core Web Vitals, scroll jank); `obra/superpowers` ships none | — | rejected: `AGENTS.md` and ADR 0005 already assign performance to `noootwo-code-health`; adopted the missing optimization loop instead |
| coercive pressure rhetoric and a level system | local `pua` / `pua-debugging` | thrashing and premature giving-up | rejected in ADR 0007; the anti-rationalization table and the structured exit report were the parts worth keeping |
| vendoring an engine, CLI, or hook manifests | `pbakaus/impeccable` | — | rejected: would make quick mode depend on a toolchain |

Adopted in this pass: the research skill itself (`research-method.md`, `source-pools.md`, `tech-selection.md`, `borrow-audit.md`), `noootwo-onboard`, the review optimization loop, the capability bridge in `docs/agents/invocation.md`, and the validator's bridge invariants.

Proposals recorded, not implemented: a machine-readable capability manifest (rejected for now — the map plus string-level validator checks is enough, and a second source of truth costs more than it returns); and ordering, hand-off content, and loop-rule enforcement beyond name checks, which no cheap check can decide.

Access note: this pass reused the source list above. Star counts and README descriptions were treated as leads; every adopted mechanism was read in the source file or repository before adoption.
- Refactoring: `https://refactoring.com/`

Fourth-pass lean-review enhancement, checked on 2026-07-06:

- The user-provided PDF `为什么你的AI代码越来越冗余？答案在这套七层流程里.pdf` describes Ponytail's seven-layer reduction process and frames the problem as AI-generated over-engineering, dependency growth, and token-cost bloat.
- Ponytail's public repository is MIT licensed and was checked at commit `40e50d9e03242aa5dd53ac771950f9127362b25f`.
- Ponytail's corrected public benchmark language distinguishes average agentic results from earlier single-shot claims. Noootwo Review should cite the benchmark as external evidence, not as automatic savings for a current repository.
- The useful reusable mechanism is the ordered reduction ladder plus safety floor, not Ponytail's full plugin runtime, hooks, benchmarks, assets, or cross-editor packaging.

Source index for the fourth pass:

- Local PDF: `/Users/notwo/Downloads/为什么你的AI代码越来越冗余？答案在这套七层流程里.pdf`
- Ponytail repository: `https://github.com/DietrichGebert/ponytail`
- Ponytail license: `https://github.com/DietrichGebert/ponytail/blob/main/LICENSE`
- Ponytail source note: `skills/noootwo-code-health/references/external/ponytail/SOURCE.md`

Fifth-pass design color-system calibration, checked on 2026-07-06:

- The user-provided PDF `你的UI廉价，错在颜色.pdf` argues that UI quality often depends on subtle color temperature flowing through neutral surfaces, shadows, text hierarchy, semantic states, gradients, icons, and illustrations.
- The reusable mechanism is role-based color calibration and artifact review, not the PDF's absolute wording such as "never use pure neutrals" or "premium UI has no exceptions."
- Material Color Utilities supports HCT, tonal palettes, dynamic colors, and contrast-aware utilities as practical color-system mechanisms.
- WCAG contrast and use-of-color guidance provides the safety floor: text must remain readable and color cannot be the only way to communicate information.
- MDN `color-mix()` and OKLCH/Oklab guidance supports perceptual color spaces for gradients and chroma-preserving mixes when a project can use them.
- Carbon, Atlassian, and Figma design-system guidance supports semantic/role-based tokens instead of hard-coded values.
- Tailwind v4 is a current framework signal that modern CSS theming can use CSS variables, `color-mix()`, and OKLCH values without requiring a heavy design-token runtime.

Source index for the fifth pass:

- Local PDF: `/Users/notwo/Downloads/你的UI廉价，错在颜色.pdf`
- Material Color Utilities: `https://github.com/material-foundation/material-color-utilities`
- WCAG contrast minimum: `https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html`
- WCAG use of color: `https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html`
- MDN color-mix: `https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/color-mix`
- MDN OKLCH: `https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/oklch`
- Carbon color tokens: `https://carbondesignsystem.com/elements/color/tokens/`
- Atlassian design tokens: `https://atlassian.design/foundations/tokens/design-tokens/`
- Figma semantic systems: `https://www.figma.com/blog/the-future-of-design-systems-is-semantic/`
- Tailwind v4: `https://tailwindcss.com/blog/tailwindcss-v4`

Sixth-pass performance-review enhancement, checked on 2026-07-06:

- Core Web Vitals frames frontend user experience around loading, responsiveness, and visual stability; useful review targets are LCP, INP, and CLS rather than vague "fast enough" claims.
- Lighthouse CI and WebPageTest show repeatable web-performance mechanisms: lab reports, budgets, waterfalls, traces, and regression checks.
- Google SRE's four golden signals support backend/service review around latency, traffic, errors, and saturation.
- OpenTelemetry provides the common observability model for traces, metrics, and logs across distributed systems.
- k6 supports repeatable API/system load tests, but Noootwo Review should only route to existing project commands or recommend a smallest viable check; it should not vendor k6.
- PostgreSQL `EXPLAIN` represents the database-query evidence model: review needs query plans, cardinality, index behavior, and realistic row counts before recommending query/index changes.
- JMH, BenchmarkDotNet, Criterion.rs, and pytest-benchmark show that algorithm/runtime performance should use language-appropriate benchmark harnesses instead of intuition-only rewrites.
- Local mature skills such as `optimize`, `audit`, and `systematic-debugging` reinforced the same mechanism: measure before optimizing, locate the bottleneck, and preserve correctness.

Source index for the sixth pass:

- Core Web Vitals: `https://web.dev/articles/vitals`
- Lighthouse CI: `https://github.com/GoogleChrome/lighthouse-ci`
- WebPageTest: `https://www.webpagetest.org/`
- Google SRE monitoring: `https://sre.google/sre-book/monitoring-distributed-systems/`
- OpenTelemetry: `https://opentelemetry.io/`
- k6: `https://k6.io/docs/`
- PostgreSQL EXPLAIN: `https://www.postgresql.org/docs/current/using-explain.html`
- JMH: `https://openjdk.org/projects/code-tools/jmh/`
- BenchmarkDotNet: `https://benchmarkdotnet.org/`
- Criterion.rs: `https://bheisler.github.io/criterion.rs/book/`
- pytest-benchmark: `https://pytest-benchmark.readthedocs.io/`

Seventh-pass lightweight-trigger redesign, checked on 2026-07-09:

- The user-provided `grill-me` research screenshot framed the useful mechanism as a small "before action" decision control, not the external project's tone or popularity.
- Agent Skills and Claude Code skills continue to support progressive disclosure: entry instructions should be short, while deeper references load only when needed.
- Google Engineering Practices continues to support concrete review expectations and scope control: reviewers should inspect design, functionality, complexity, tests, naming, and comments as relevant, not as an unbounded checklist.
- Existing Noootwo local evidence shows `noootwo-design` already has many references, a full `.noootwo/` harness, readiness scripts, and eval prompts; adding another default gate would raise friction for quick polish.

Source index for the seventh pass:

- User-provided screenshot: `/var/folders/s8/hsvb57g10c989g2lc4zdps100000gn/T/codex-clipboard-79f6f2ee-26ee-47fb-92c3-1eaf6fa226b1.png`
- Agent Skills specification: `https://agentskills.io/specification`
- Anthropic Claude Code skills: `https://docs.anthropic.com/en/docs/claude-code/skills`
- Google Engineering Practices review docs: `https://google.github.io/eng-practices/review/reviewer/looking-for.html`

Source index for the eighth pass:

- Google People + AI Guidebook user needs and mental models: `https://pair.withgoogle.com/`
- Microsoft Human-AI interaction guidelines: `https://www.microsoft.com/en-us/research/blog/guidelines-for-human-ai-interaction-design/`
- Nielsen Norman Group AI UX and product design guidance: `https://www.nngroup.com/articles/designing-ai-study-guide/`
- Superpowers brainstorming skill local reference: `/Users/notwo/.codex/plugins/cache/openai-api-curated/superpowers/11c74d6b/skills/brainstorming/SKILL.md`

Ninth-pass product discovery routing, checked on 2026-07-17:

- Product Talk opportunity-solution-tree practice supports moving from outcome to opportunities, solution options, and experiments instead of jumping from an idea straight to implementation.
- Shape Up supports naming appetite, no-gos, and rabbit holes before committing to a shaped build.
- Google Ventures Design Sprint practice supports fast map/sketch/decide/prototype/test cycles, but Noootwo Product should borrow the convergence mechanism rather than make every product idea pay a full sprint cost.
- Local `brainstorming` skill analysis showed useful mechanisms: context-first exploration, one question at a time, multiple options with tradeoffs, recommended default, and design convergence. The heavy parts to avoid for Product are mandatory spec writing, commits, and formal user-review gates for every idea.

Source index for the ninth pass:

- Product Talk opportunity solution trees: `https://www.producttalk.org/opportunity-solution-trees/`
- Shape Up chapter 2, Principles of Shaping: `https://basecamp.com/shapeup/1.1-chapter-02`
- GV Design Sprint: `https://www.thesprintbook.com/the-design-sprint`
- Local brainstorming skill reference: `/Users/notwo/.agents/skills/brainstorming/SKILL.md`

Packaging and one-click installation pass, checked on 2026-08-12:

- The official `skills` CLI supports repository shorthand, explicit child-skill selection with `--skill '*'`, global installation with `--global`, agent targeting with `--agent`, and update commands. The tested local installation copied every Noootwo child skill into the standard `.agents/skills` layout.
- `antfu/skills`, `vuejs-ai/skills`, and `flutter/agent-plugins` publish independent child directories under `skills/` and document a one-command aggregate install. Antfu explicitly uses `--skill='*'`; Flutter targets the universal `.agents/skills` location and also exposes native plugin metadata.
- The Agent Skills specification requires each published unit to be a directory containing `SKILL.md`; `scripts/`, `references/`, and `assets/` are optional supporting directories. This matches the Noootwo Vibe child-skill layout.
- The `skills` CLI resolves repository shorthand against the repository default branch. Therefore the default branch, not only a feature branch, must contain the published multi-skill workspace for `npx skills add noootwo/noootwo-vibe ...` to be a reliable one-click command.

Source index for the packaging pass:

- `skills` CLI: `https://github.com/vercel-labs/skills`
- Agent Skills specification: `https://agentskills.io/specification`
- Antfu skills collection: `https://github.com/antfu/skills`
- Vue skills collection: `https://github.com/vuejs-ai/skills`
- Flutter agent plugins: `https://github.com/flutter/agent-plugins`

## Mechanisms Borrowed

- Keep publishable units independently addressable under `skills/`.
- Keep root metadata, validation, docs, and release policy separate from child skill bodies.
- Keep skill bodies concise and push deep guidance into direct `references/` files.
- Use per-skill versions and tag prefixes so child skills can release independently.
- Use docs layering: README for stable usage, AGENTS for always-on routing, docs/status for volatile state, ADRs for durable decisions.
- Use code-quality guidance as review heuristics, not as permission for broad rewrites. Evidence comes from changed files, tests, caller impact, and repeated friction.
- Use mature-skill mechanisms as structure, not wording: hard gates, red flags, concise default bodies, handoff packets, and verification evidence.
- For non-design skills, optimize for agent control and cost: task classification, facts ownership, code-health risk classes, and explicit stop conditions reduce unnecessary context loading and rework.
- Make `workflow` the entry point for project onboarding: skill inventory, foundation health, gap planning, and closure. Keep docs/review as owners of their respective fixes.
- Prefer audit plus minimal templates over automatic scaffolding. Missing foundation should produce the smallest useful AGENTS/status/ADR/release/validation patch.
- Add lean review as a Noootwo Review lens for over-engineering: delete, reuse, standard library, native platform, installed dependency, shrink fragmented code, then minimum new code.
- Preserve safety before reduction: validation, error handling, security, accessibility, business invariants, and necessary checks are not bloat.
- Keep external sources as selected references with license and source notes; avoid vendoring whole repositories unless the runtime needs executable code.
- Add color-system calibration as a Noootwo Design lens for brand temperature, neutral roles, shadow hue, semantic harmonization, gradient boundaries, icon/illustration token inheritance, and contrast proof.
- Treat OKLCH/HCT as recommended color-engineering tools when practical, not mandatory dependencies.
- Add performance review as a Noootwo Review lens for frontend loading/rendering, backend/API latency, database/query cost, algorithm/runtime hotspots, resource use, and performance regression risk.
- Require performance evidence: baseline, budget, trace, profile, query plan, benchmark, production metric, or an explicit verification gap.
- Add workflow alignment checkpoints only where one unresolved decision can change implementation.
- Make review capability lens-based so narrow diffs stay focused while broader work can explicitly choose project-health, performance, lean, release, or AI-code/context-cost review.
- Keep Noootwo Design quick mode lightweight; full `.noootwo/` harness completion belongs to standard, deep, production, adoption, review, or handoff work.
- Add Product Checkpoints for real-user product scope, user paths, state models, cognitive-cost risks, and user-behavior acceptance criteria before UI or implementation when those choices are unclear.
- Borrow the Product Choice Challenge mechanism from brainstorming-style skills: make 2-3 meaningful options visible with a recommended default, but do not import the heavy always-on spec workflow.
- Add Product Discovery as the product-shaped replacement for generic brainstorming when the user starts from a software product idea, blank project, broad product vision, or first-loop question.

## Boundaries

- Do not add a root `SKILL.md`; it degrades default child-skill discovery.
- Do not make every specialized workflow a public skill. Public skills should be stable, reusable, and easy to trigger.
- Do not duplicate long reference material across child skills.
- Do not claim plugin-style discovery as the primary install path until it is verified in the target runtime.
- Do not promote every useful practice into a default gate; default paths must stay cheap and references should load only when relevant.
- Do not import another skill's full process wholesale. Borrow the repeatable control mechanism and adapt it to Noootwo Vibe's current skill model.
- Do not let project-health review take over docs or workflow. It reports defects and routes ownership.
- Do not claim current-repo token, dollar, or speed savings from lean review unless there is a measured before/after baseline.
- Do not let lean review become code golf. Smaller code is only acceptable when required behavior and safety are preserved.
- Do not turn color-system calibration into a universal ban on pure white, pure black, pure gray, platform system colors, or exact brand neutrals.
- Do not use color temperature to override accessibility, semantic-state recognizability, data readability, product context, or artifact evidence.
- Do not claim faster load time, lower latency, lower CPU/memory, throughput gain, or cost reduction without before/after evidence.
- Do not let performance review justify speculative rewrites, unsafe caching, weaker validation, weaker accessibility, broken data consistency, or removal of diagnostic logging.
- Do not convert the alignment checkpoint into a long questionnaire.
- Do not make every UI change pay the cost of full `.noootwo/` readiness validation.
- Do not make every code review a full project audit; choose lenses from the change and evidence.
- Do not make every product clarification a full PRD; use a Product Choice Challenge only when one choice materially changes the user path or build scope.
- Do not let generic brainstorming become the owner of product discovery when Noootwo Product can identify the first user, first loop, no-gos, rabbit holes, and validation signal.
