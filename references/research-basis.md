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
- Refactoring: `https://refactoring.com/`

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

## Boundaries

- Do not add a root `SKILL.md`; it degrades default child-skill discovery.
- Do not make every specialized workflow a public skill. Public skills should be stable, reusable, and easy to trigger.
- Do not duplicate long reference material across child skills.
- Do not claim plugin-style discovery as the primary install path until it is verified in the target runtime.
- Do not promote every useful practice into a default gate; default paths must stay cheap and references should load only when relevant.
- Do not import another skill's full process wholesale. Borrow the repeatable control mechanism and adapt it to Noootwo Vibe's four-skill model.
- Do not let project-health review take over docs or workflow. It reports defects and routes ownership.
