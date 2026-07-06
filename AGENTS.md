# Noootwo Vibe Maintenance

This repository is a multi-skill workspace. The root is not a published skill; the public skills live under `skills/` and are listed in `skills.json`.

## Skill Routing

- Use `$noootwo-workflow` for multi-step AI development workflow, project skill audits, foundation health checks, task routing, planning, release sequencing, and keeping work controlled.
- Use `$noootwo-docs` for README, AGENTS, docs/status, ADRs, guides, reference docs, release notes, documentation audits, and documentation hygiene.
- Use `$noootwo-review` for code quality, lean review, over-engineering, dependency bloat, project-health defects, maintainability, refactoring discipline, test strategy, and implementation review.
- Use `$noootwo-design` for UI/design work, `.noootwo/` deliverables, artifact review, screenshot critique, visual systems, and design handoff.

## Repository Rules

- Keep the public skill set exactly: `noootwo-workflow`, `noootwo-docs`, `noootwo-review`, `noootwo-design` unless the user explicitly changes the product model.
- Keep skill bodies concise; move deeper guidance to direct `references/` files and load them only when needed.
- Do not add a root `SKILL.md`; it prevents default discovery of all child skills.
- Keep per-skill versions in `skills/<skill>/VERSION` and mirror them in `skills.json`.
- Run `python scripts/validate_skill_workspace.py .` after changing skill layout, versions, metadata, or repository URLs.

## Design-Specific Rule

Before changing `$noootwo-design` aesthetics, workflow modes, stack playbooks, review gates, AGENTS integration, or claims about design quality, do a current research pass.

- Prefer official docs, framework docs, designer/developer community evidence, and artifacts with visible screenshots or running examples.
- Use X/Twitter, Reddit, HN, Figma, Flutter, React, Vue, and native app communities as signals, not as single-source truth.
- If preferred foreign sources are inaccessible, use domestic fallback sources and record access limits, source levels, and why the fallback is acceptable.
- Borrow repeatable mechanisms, not leaked prompts, proprietary wording, or surface styling.
- Consider skill usage cost and engineering feasibility before adding gates, scripts, or required artifacts.
- Do not claim a UI-quality improvement without artifact or screenshot review, and run readiness validation when `.noootwo/` deliverables are involved.
