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

Debug systemic-close pass, checked 2026-10-11:

- James Reason's system approach treats accidents as consequences of interacting latent conditions and failed defenses rather than a single unsafe act; it supports asking why existing controls allowed the defect and where the same condition remains (`Human error: models and management`, BMJ 2000, doi:10.1136/bmj.320.7237.768).
- Nancy Leveson's STAMP models safety as a control problem, where accidents arise when control structures fail to enforce constraints across components and interactions; it supports the failed-control layer for complex systems (`Engineering a Safer World`, MIT Press, 2011, doi:10.7551/mitpress/8179.001.0001).
- Chris Argyris's double-loop learning separates correcting an action from changing the governing assumptions and policies that produced it; it supports the learning-loop question (`Double Loop Learning in Organizations`, Harvard Business Review, September 1977).
- Google SRE's blameless postmortem practice connects root causes to preventive action, review, priority, and shared learning; it supports making recurrence barriers reviewable rather than leaving them as prose (`Postmortem Culture: Learning from Failure`, Google SRE Book, 2017).
- Erik Hollnagel's Safety-II shifts attention from only failures to how successful performance varies and can still carry latent unsafe conditions; it supports near-miss and fragile-success search (`Safety-I and Safety-II`, Ashgate/Routledge, 2014).

Source index for the debug systemic-close pass:

- Reason, `Human error: models and management`: `https://pmc.ncbi.nlm.nih.gov/articles/PMC1117770/`
- Leveson, `Engineering a Safer World`: `https://doi.org/10.7551/mitpress/8179.001.0001`
- Argyris, `Double Loop Learning in Organizations`: `https://hbr.org/1977/09/double-loop-learning-in-organizations`
- Google SRE, `Postmortem Culture: Learning from Failure`: `https://sre.google/sre-book/postmortem-culture/`
- Hollnagel, `Safety-I and Safety-II`: ISBN 9781472423085 (Ashgate/Routledge, 2014)

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

Verification-depth pass, checked 2026-10-18:

- ISTQB CTFL v4.0.1 supports risk-based testing and impact analysis for regression scope; exhaustive testing is impossible, so scope and thoroughness should follow risk.
- Microsoft Test Impact Analysis supports selecting tests relevant to a commit, falling back to all tests when the change cannot be understood, and running full tests periodically.
- Meta's Predictive Test Selection reports a 2x reduction in testing infrastructure cost while retaining over 95% of individual test failures and over 99.9% of faulty changes; the residual miss rate is a boundary, not a reason to skip the release gate.
- Google Engineering Practices' "Small CLs" and SmartBear's Cisco study support bounded review scope: small self-contained changes are reviewed more thoroughly, and review effectiveness drops beyond roughly 200–400 lines.
- Together these support a scoped Change Check after one requirement, risk-triggered escalation, and one full Release Check before shipping. They do not justify claiming a specific token or time saving for this repository.

Source index for the verification-depth pass:

- ISTQB CTFL syllabus v4.0.1: `https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf`
- Microsoft Test Impact Analysis: `https://learn.microsoft.com/en-us/azure/devops/pipelines/test/test-impact-analysis?view=azure-devops`
- Meta Predictive Test Selection: `https://arxiv.org/abs/1810.05286`
- Google Engineering Practices, Small CLs: `https://google.github.io/eng-practices/review/developer/small-cls.html`
- SmartBear code-review study summary: `https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/`

Release-ledger pass, checked 2026-10-18:

- Google SRE's *Reliable Product Launches at Scale* reports that a curated launch checklist helped produce reproducibly reliable launches. The abridged Launch Coordination Checklist groups architecture, reliability, security, automation, rollout, and schedule checks, which supports one release-bound aggregate instead of rediscovering the same cross-cutting checks per feature.
- Microsoft Azure deployment gates collect health signals before or after deployment and re-evaluate until all required gates pass in the same interval; timeout blocks promotion. This supports explicit evidence, a stop condition, and a single release-bound consumption point.
- The WHO Surgical Safety Checklist study reported complications falling from 11.0% to 7.0% and death from 1.5% to 0.8% after introduction, showing that a short explicit checklist can change outcomes.
- The counterexample is Ontario's mandatory checklist adoption: across 109,341 pre-adoption and 106,370 post-adoption procedures, mortality and complication changes were not statistically significant. Checklist presence alone is not proof of adherence, so the Release Verification Ledger requires owner, status, evidence, exact-commit revalidation, and an immutable sealed record.
- Together these support a release-bound ledger that dedupes by evidence boundary and closes once at release. They do not establish a measured token or time saving for this repository.

Source index for the release-verification-ledger pass:

- Google SRE, Reliable Product Launches at Scale: `https://sre.google/sre-book/reliable-product-launches/`
- Google SRE, Launch Coordination Checklist: `https://sre.google/sre-book/launch-checklist/`
- Microsoft Azure deployment gates: `https://learn.microsoft.com/en-us/azure/devops/pipelines/release/approvals/gates?view=azure-devops`
- WHO Surgical Safety Checklist study: `https://pubmed.ncbi.nlm.nih.gov/19144931/`
- Ontario surgical checklist counterexample: `https://pubmed.ncbi.nlm.nih.gov/24620866/`

Context-cost pass, checked 2026-10-25:

- All nine source URLs returned HTTP 200; the arXiv abstracts and the visible Chroma, Anthropic, and Cognition article text were read directly.
- Chroma's *Context Rot* report tests 18 models and finds performance varies with input length even on simple tasks; retrieval accuracy falls further as needle-question similarity decreases and distractors increase. This supports selecting only the current frontier, not treating a large context window as uniform attention.
- Anthropic's *Effective context engineering for AI agents* recommends just-in-time retrieval, high-fidelity compaction, structured notes, and the smallest set of high-signal tokens. It also reports subagent gains for isolated research, so isolation remains available for independent read-only work rather than becoming a default fan-out.
- ACE (arXiv 2510.04618) uses structured, incremental context updates to resist brevity bias and context collapse. This supports append-only events and itemized deltas instead of repeatedly rewriting a lossy summary.
- Agentic Context Management (arXiv 2607.21503 and 2607.23809) frames context as a lifecycle: ingest, scope, retain or forget with provenance, anticipate the next need, compact to a budget, and retrieve offloaded content on demand.
- The Complexity Trap (arXiv 2508.21433) finds simple observation masking halves cost relative to raw history and matches or slightly exceeds LLM summarization in its tested agents. This is a counterexample to mandatory expensive summaries and supports keeping raw evidence behind handles.
- Compression Method Matters (arXiv 2603.23527) finds aggressive prompt compression has benchmark-dependent output effects; token reduction can increase total inference cost. This rejects one universal aggressive compression ratio.
- Compaction Laundering (arXiv 2610.29869) reports that flattening role provenance before compaction let forged approvals survive 87-100% of attempts in five harnesses, while role-typed harnesses were 0%. This is a new, unreplicated security preprint, but it directly supports source hashes and typed evidence handles.
- Cognition's *Don't Build Multi-Agents* argues that dependent actions carry implicit decisions and that shared context plus conflict resolution matter. Its single-thread default resolves against Anthropic's isolated-research case by using one writer and isolating only read-only work.

The resulting mechanism is `write -> select -> compress -> isolate -> verify`. Static checks and this source pass do not establish a token saving; the package-level 10% paired-project gate remains the decision evidence. Full evidence levels, counterexamples, and limits are in `docs/reference/context-cost.md`.

Source index for the context-cost pass:

- Context Rot: `https://research.trychroma.com/context-rot`
- Anthropic context engineering: `https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents`
- ACE: `https://arxiv.org/abs/2510.04618`
- Agentic Context Management lifecycle: `https://arxiv.org/abs/2607.21503`
- ACM for long-horizon tasks: `https://arxiv.org/abs/2607.23809`
- The Complexity Trap: `https://arxiv.org/abs/2508.21433`
- Compression Method Matters: `https://arxiv.org/abs/2603.23527`
- Compaction Laundering: `https://arxiv.org/abs/2610.29869`
- Cognition, Don't Build Multi-Agents: `https://cognition.ai/blog/dont-build-multi-agents`

Upstream mechanism refresh, checked 2026-10-27:

- `obra/superpowers` `v7.0.1` resolves to commit `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`. Its important change is not a replacement of TDD or systematic debugging; it is a collaboration protocol around evidence-grounded intake, explicit ownership of platform/language/library/medium choices, approved plans, a fresh builder check for expensive handoffs, decision-complete plans, `Review Focus`, and rulings for reversible plan conflicts. The release-linked 176-conversation evaluation is maintainer-run, so it supports mechanism selection but not an independent quality or speed claim.
- `alchaincyf/huashu-design` `v3.0.0` resolves to commit `798c4235ebff03d5c45e3c8affdf5e9d18f9dfa7`. Its useful mechanism is options over accumulating prohibitions: cheap real samples, same-medium references, inspected artifact evidence, factual linting, and a future project-local appearance ledger. The author's small blind-test narrative is low-confidence evidence. The supplied WeChat article redirected to a verification page with `环境异常`; GitHub release source and visible case artifacts were the fallback.
- `pbakaus/impeccable` advanced from the recorded `v4.3.1` to `v4.7.0` at commit `aeeb3d8c30b5f95aeeb3e893b0f1a308af8fdb8f`. Relevant mechanisms are code-first samples, inspectable direction cards, familiar controls with one authored signature move, real work visible on the first screen, actual touch/device evidence, and progressive disclosure. The repository does not provide an independent controlled UI-quality study.
- Adopt: Product grounded response without a fixed script, user-owned how decisions, agent defaults with reopen conditions, low-cost direction samples, same-medium inspected evidence, evidence-dependent aesthetic flags, conditional Builder Check, decision-complete plans, `Review Focus`, and reversible-execution rulings.
- Preserve: one-round Product frontier, three directions when the choice is materially unresolved, safety/accessibility/state-integrity hard gates, Change Check and Release Check separation, and artifact review.
- Reject: fixed opener length, mandatory six polished candidates, universal deep-design ceremony, global appearance memory, an expanded style library, routine re-approval for reversible implementation details, and copying prompts, templates, brand surfaces, or visual assets.
- Evidence boundary: Superpowers and Impeccable are upstream/maintainer evidence; Huashu's quantitative narrative is a small author-run sample. The 2026-10-27 record and ADR 0025 carry the full version, commit, access, adoption, rejection, and confidence notes.

Source index for the upstream mechanism refresh:

- Superpowers: `https://github.com/obra/superpowers`
- Huashu Design: `https://github.com/alchaincyf/huashu-design`
- Impeccable: `https://github.com/pbakaus/impeccable`
- Supplied WeChat article, body inaccessible after redirect: `https://mp.weixin.qq.com/s/gR3tDBD8-4hLJWj-x2b1Yw`
- Durable research record: [upstream-refresh-2026-10-27](../docs/reference/upstream-refresh-2026-10-27.md)

Upstream mechanism refresh, checked 2026-11-03:

- `pbakaus/impeccable` `skill-v4.8.0` peels to commit `414603bf14c7a344edb466bb1f85690c77ce8b7d` (2026-10-26), after the recorded `v4.7.0` commit `aeeb3d8c30b5f95aeeb3e893b0f1a308af8fdb8f` (2026-10-19). The release adds host integrations (Devin, Replit Agent, Windsurf), GitHub Actions annotations, `--list-rules`, install digest checks, Cursor/Codex hook fixes, Live Mode repairs, Arabic `harden` support, detector accuracy work, and an advisory hard-offset-shadow finding. The `skill/SKILL.src.md` diff is one behavioral line: on launcher failure, read `craft-floor.md` before any UI edit. This is integration and maintenance work, not a new design philosophy. The useful boundary remains: app screens and documentation are code-first; generated comps belong to landing, campaign, and showcase surfaces.
- `oil-oil/oil-ui` `v0.30.0` resolves to commit `4e8d25f91727b3b08a3bbf60bac84d81f6ff6574` (2026-11-02; MIT). It is a host-neutral design skill, not only a DeepSeek Harness plugin. Mechanisms read from `SKILL.md` and its references: design north star, product facts before visual choices, one focal object and primary action per screen, five-axis tone calibration, concrete-engine direction generation, color drawn from product evidence, one default direction with comparison only when requested, one memory point plus subtraction, real screenshot review with an independent reviewer when available, and `.oil-ui/<task>` process isolation. v0.29.1 adds an optional generated-UI-comp path: 45–65 word prompts, five slots, `85:10:5` color range, `1024×1536` desktop landing comps, `measure_reference.py` sampling, no copying of vertical spacing from the comp, and cleanup of pseudo-Chinese. v0.30.0 surfaces conflicts among design docs, agent visual instructions, and code instead of silently merging them.
- Adopt for Noootwo Design: reference-only vocabulary for the design north star, five-axis tone calibration, concrete-engine direction generation, one focal object/action, one memory point, optional landing/showcase comps, and conflict disclosure. Do not duplicate mechanisms already covered by material direction samples, real screenshot inspection, or independent review.
- Reject or defer: making image generation mandatory, treating `85:10:5` as a universal ratio, replacing Noootwo's material-choice direction exploration with OIL UI's default, requiring subagents, and copying OIL UI's prompts, scripts, assets, plugin wrapper, or Pro workflows. The OIL UI gallery is an author-curated showcase, not an independent benchmark or proof of production quality.
- Evidence boundary: Impeccable and OIL UI are upstream or maintainer evidence; no independent controlled UI-quality study was found. The model mix of the OIL UI gallery is not evidence that a particular harness or model caused the showcased result.

Source index for the 2026-11-03 refresh:

- Impeccable: `https://github.com/pbakaus/impeccable`
- OIL UI: `https://github.com/oil-oil/oil-ui`
- DeepSeek Harness wrapper, not the core skill: `https://github.com/oil-oil/dsh-oil-ui`

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
- Use one bounded context lifecycle across the skill package: direct work skips state, resume starts from a capsule and at most three frontier entry points, and decision/evidence work reads only the source that can settle the step.
- Keep raw output above 16 KiB in cold evidence and carry its path, hash, source, and bounded tail into live context.
- Keep append-only events authoritative; a capsule is a derived read view, and a no-change check creates no event.
- Keep one writer for dependent work and isolate only independent read-only research or review.
- Ground an unresolved Product round in repo facts and separate observed facts from proposals before asking.
- Separate user-owned how decisions from reversible agent-selected defaults, and record the reason and reopen condition for each default.
- Prefer real, viewed direction samples and same-medium evidence when a visual choice is materially unresolved.
- Treat non-safety aesthetic patterns as evidence flags; keep accessibility, readability, content, and state integrity as hard gates.
- Use a fresh Builder Check only for non-obvious, cross-session, expensive, or cross-boundary handoffs.
- Record interfaces, assertions, verification, `Review Focus`, and reversible rulings in accepted implementation plans.

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

## Audience And Language Pass

Checked on 2026-11-09. The decision was how Product and Design should turn the
target user into interaction posture and information exposure without turning
every task into a persona study.

- NN/g novice/expert research supports conditional density and expert
  affordances; plain-language research supports concise language for experts
  while allowing evidence-backed shared domain terms; progressive-disclosure
  research supports one first layer of frequent content and one clear second
  layer, with low usability beyond two levels.
- W3C COGA independently supports clear page purpose, short chunks, removing
  unnecessary content, consistent controls, and no unexplained acronyms or
  jargon.
- GOV.UK Design Principles and Microsoft Style Guide independently support
  starting from user needs and context, using simple words with precise
  meanings, and doing the hard work to make things simple.
- ISO 24495-1 frames plain language by reader outcome: relevant, findable,
  understandable, and usable. The public MIT `danyuchn/iso-24495-skill` and
  `content-designer/ux-writing-skill` were compared as prior art; neither owns
  product scope, interaction posture, technical-evidence placement, or artifact
  review.
- The counterexamples constrain the rule: trained operators may need density and
  shared domain terms; technical buyers need architecture, security,
  performance, and compatibility evidence; and hiding the main path or required
  evidence behind progressive disclosure is a comprehension defect.

The full brief, source dates, access notes, and confidence are in
`docs/reference/audience-language-evidence.md`. The durable decision is ADR
0029. No fresh-session behavior or cost improvement is claimed.

Parallel-execution refresh, checked 2026-11-11:

- Local Codex history contained 62 session files and 2.56 GiB of data for
  October and November 2026. Deduplicated `function_call` records contained 29
  `spawn_agent`, 50 `wait_agent`, 1 `send_input`, and 1 `close_agent` call; 9
  session files contained a unique spawn. A one-session local Claude sample had
  zero `Task` or `Agent` calls. These are machine-local counts, not task or
  cross-harness statistics.
- `obra/superpowers` `v7.0.2` contributes two mechanisms: dispatch only
  independent tasks with no shared state, and give each fresh worker a
  self-contained brief with a terminal status; its progress ledger prevents
  completed work from being re-dispatched after compaction.
- Anthropic's multi-agent research system reports strong breadth-first research
  gains with much higher token use. Its companion guidance says most tasks
  remain single-agent. The result supports isolated research fan-out, not
  default write fan-out for coupled coding.
- OpenAI Agents SDK defaults concurrent subagents to 3, Claude Code recommends
  independent files/research/review while naming overhead, and Cursor and
  GitHub Copilot expose separate parallel coding environments. Capability and
  limits vary by harness, so the protocol must probe capabilities.
- Cognition's *Don't Build Multi-Agents* supplies the governing counterexample:
  dependent actions need shared context and conflict resolution. Noootwo keeps
  one integrator, one current-state writer, and serial/contract-first behavior
  for shared meaning. No worker or secondary worktree writes `.noootwo`;
  snapshot, event, and evidence writes serialize through the integrator because
  the state helper's read-modify-write path is not a multi-writer primitive.
  Agentless supplies a second warning that more agents do not by themselves
  improve outcomes.
- Adopt: a conditional Fan-out Gate, `read-fanout`, `write-fanout`,
  `requirement-parallel`, four independence questions, Worker Brief, Result
  Packet, three-worker default/four-worker maximum, linked-worktree lanes, and
  explicit compaction recovery rules for rejoin.
- Reject: universal fan-out, background shells as subagents, multiple writers
  in one checkout, worker-owned state, a separate orchestrator skill, a full DAG,
  and an unbounded worker pool.
- Evidence boundary: the local session audit shows the trigger gap, not a causal
  effect of the new rules. Fresh-session paired measurements remain open, so no
  speed, token, quality, or rework improvement is claimed.

Source index for the parallel-execution refresh:

- Superpowers: `https://github.com/obra/superpowers`
- Anthropic multi-agent research system: `https://www.anthropic.com/engineering/multi-agent-research-system`
- Anthropic multi-agent guidance: `https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them`
- Anthropic context engineering: `https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents`
- OpenAI Agents SDK: `https://openai.github.io/openai-agents-python/multi_agent/`
- Claude Code subagents: `https://code.claude.com/docs/en/sub-agents`
- Cursor parallel agents: `https://cursor.com/docs/agent/parallel-agents`
- GitHub Copilot coding agent: `https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent`
- Cognition, Don't Build Multi-Agents: `https://cognition.ai/blog/dont-build-multi-agents`
- Agentless: `https://arxiv.org/abs/2407.01489`

Decision-continuity pass, checked 2026-11-13:

- The problem recurs publicly with artifacts: `openai/codex` #54544 (repeats
  settled questions), #42611 (auto-compaction replays an answered message),
  #49022 (Active Goal lost, completed tasks resumed), #58369 (agent reopens
  explicit user decisions), #46175 (returns to earlier clarification state),
  #44648 (no question resolve/withdraw lifecycle); `anthropics/claude-code`
  #80938, #96422, #26771, #97906 describe the same class. These are user
  reports, not maintainer-confirmed diagnoses.
- Local artifact: the 2026-11-13 kungfu-harness session ran 9 compactions in
  2h22m; question rounds fired right after compactions, two decision ids were
  re-asked with regenerated option sets, and answers drifted. The project state
  held none of the decisions. Transcript and analysis recorded in
  `docs/reference/decision-ledger-evidence.md`.
- Anthropic's context-engineering guidance requires compaction to preserve
  architectural decisions, unresolved bugs, and implementation details, and
  warns aggressive compaction loses context needed later. Kiro's compaction
  documentation puts goals, decisions, and constraints in the always-preserved
  set with a session checkpoint; Claude Code supports custom compact
  instructions and per-session memory loads. Official vendor guidance, not
  independent measurement.
- Spec Kit's `clarify` command states "Exclude questions already answered",
  encodes answers back into the spec, and caps the session at five questions.
  Rasa forms ask only the first unfilled required slot. Both are the
  slot-filling dedupe mechanism applied at different scales.
- Superpowers `v7.0.2` `brainstorming` says never to reopen what the user
  already decided; `executing-plans` treats "the ledger" as the memory that
  makes work recoverable after compaction. Manus rewrites its todo list to
  recite objectives into the recent attention span. ACE (arXiv 2510.04618)
  names the failure mode: brevity bias and context collapse under iterative
  rewriting; structured incremental updates resist it. MADR gives changed
  decisions an explicit `superseded by` status instead of silent replacement.
- Adopt into `noootwo-product`: a Decision Ledger with stable ids and statuses,
  an ask gate that recomputes the frontier as answerable-now minus answered,
  frozen wording with evidence-cited supersede, per-round recitation of the
  settled list, and append-only entries persisted through `noootwo-state` when
  the work outlives the session.
- Reject: global cross-project memory, full-transcript replay, host-specific
  compaction hooks as a dependency (Codex has none), copying Spec Kit's
  five-question cap or Cline's file hierarchy, and letting a summary override
  the ledger.
- Evidence boundary: no independent controlled study measures the ask gate. The
  local transcript plus recurring public reports plus mechanism-level official
  guidance support adoption; no token, speed, or quality claim is attached.
  Full levels, boundaries, and counterexamples are in
  `docs/reference/decision-ledger-evidence.md`; the decision is ADR 0032.

Source index for the decision-continuity pass:

- Anthropic context engineering: `https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents`
- Kiro compaction: `https://kiro.dev/docs/compaction.md`
- Kiro IDE 1.0 compaction: `https://kiro.dev/docs/ide/whats-new-v1/compaction.md`
- Claude Code memory: `https://docs.claude.com/en/docs/claude-code/memory.md`
- GitHub Spec Kit clarify: `https://github.com/github/spec-kit/blob/main/templates/commands/clarify.md`
- Superpowers: `https://github.com/obra/superpowers`
- Manus: `https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus`
- ACE: `https://arxiv.org/abs/2510.04618`
- 12-Factor Agents: `https://github.com/humanlayer/12-factor-agents`
- MADR: `https://github.com/adr/madr`
