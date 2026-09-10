# Noootwo Vibe Maintenance

This repository is a multi-skill workspace. The root is not a published skill; the public skills live under `skills/` and are listed in `skills.json`.

## Task Start

1. Decide whether the work is `direct` (a tiny localized edit with an obvious check) or needs a skill. Direct work still passes the lifecycle guardrails internally; it needs no ceremony.
2. For anything else, invoke the skill that owns the work, then follow it. To invoke one, read its `SKILL.md` and follow it — a skill you only considered has not run.
3. Which skill, and the order to run them in: read `docs/agents/invocation.md`. When you are unsure, start with `noootwo-workflow`.

## Writing Skills

Every skill, `AGENTS.md`, and pointed-at doc is written to `docs/agents/skill-authoring.md`. Read it before writing or reviewing one. The budgets in it are enforced by `python scripts/validate_skill_workspace.py .`, which must pass after any change to skill layout, versions, metadata, descriptions, or references.

## Repository Rules

- Keep the public skill set exactly: `noootwo-ask`, `noootwo-workflow`, `noootwo-product`, `noootwo-design`, `noootwo-review`, `noootwo-docs`.
- Do not add `noootwo-architecture`; architecture, technical judgment, testing strategy, performance, and maintainability stay under `noootwo-review`.
- Only `noootwo-ask` is user-invoked. Every other skill stays reachable by the model and by its siblings.
- Do not add a root `SKILL.md`; it prevents default discovery of all child skills.
- Keep per-skill versions in `skills/<skill>/VERSION` and mirror them in `skills.json`.
- Record a durable change to the skill model as an ADR in `docs/adr/`.

## Design-Specific Rule

Before changing `noootwo-design` aesthetics, workflow modes, stack playbooks, review gates, or claims about design quality, do a current research pass.

- Prefer official docs, framework docs, designer and developer community evidence, and artifacts with visible screenshots or running examples.
- Use X/Twitter, Reddit, HN, Figma, Flutter, React, Vue, and native app communities as signals, not as single-source truth.
- If preferred foreign sources are inaccessible, use domestic fallback sources and record the access limits, source levels, and why the fallback is acceptable.
- Borrow repeatable mechanisms, not leaked prompts, proprietary wording, or surface styling.
- Weigh skill usage cost and engineering feasibility before adding gates, scripts, or required artifacts.
- Do not claim a UI-quality improvement without artifact or screenshot review, and run readiness validation when `.noootwo/` deliverables are involved.
