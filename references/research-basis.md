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

Access note: `https://adr.github.io/` failed during the live check with a TLS connection error, so the ADR signal was verified through `https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions` and `https://github.com/architecture-decision-record/architecture-decision-record` instead.

## Mechanisms Borrowed

- Keep publishable units independently addressable under `skills/`.
- Keep root metadata, validation, docs, and release policy separate from child skill bodies.
- Keep skill bodies concise and push deep guidance into direct `references/` files.
- Use per-skill versions and tag prefixes so child skills can release independently.
- Use docs layering: README for stable usage, AGENTS for always-on routing, docs/status for volatile state, ADRs for durable decisions.
- Use code-quality guidance as review heuristics, not as permission for broad rewrites. Evidence comes from changed files, tests, caller impact, and repeated friction.

## Boundaries

- Do not add a root `SKILL.md`; it degrades default child-skill discovery.
- Do not make every specialized workflow a public skill. Public skills should be stable, reusable, and easy to trigger.
- Do not duplicate long reference material across child skills.
- Do not claim plugin-style discovery as the primary install path until it is verified in the target runtime.
- Do not promote every useful practice into a default gate; default paths must stay cheap and references should load only when relevant.
