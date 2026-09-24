# Noootwo Vibe Maintenance

This repository is a multi-skill workspace. The root is not a published skill; the public skills live under `skills/` and are listed in `skills.json`.

## Task Start

1. Decide whether the work is `direct` (a tiny localized edit with an obvious check) or needs a skill. Direct work still passes the lifecycle guardrails internally; it needs no ceremony.
2. For anything else, invoke the skill that owns the work, then follow it. To invoke one, read its `SKILL.md` and follow it — a skill you only considered has not run.
3. Which skill, and the order to run them in: read `docs/agents/invocation.md`. When you are unsure, start with `noootwo-workflow`.

## Writing Skills

Every skill, `AGENTS.md`, and pointed-at doc is written to `docs/agents/skill-authoring.md`. Read it before writing or reviewing one. The budgets in it are enforced by `python scripts/validate_skill_workspace.py .`, which must pass after any change to skill layout, versions, metadata, descriptions, or references.

## Repository Rules

- Keep the public skill set exactly: `noootwo-ask`, `noootwo-workflow`, `noootwo-product`, `noootwo-design`, `noootwo-tdd`, `noootwo-code-health`, `noootwo-state`, `noootwo-debug`, `noootwo-research`, `noootwo-onboard`.
- `noootwo-workflow` schedules; specialists do the work. Do not let a route, mode, or reference in `noootwo-workflow` take over the method owned by a specialist skill.
- Durable project state and context are written through `noootwo-state`; specialists produce content and invoke `noootwo-state` to choose the form and location.
- When a named skill is missing, follow `docs/agents/dependency-fallback.md`: try to install it, and on failure take the smallest direct fallback and mark the record `skill-missing: <name>`.
- Do not add `noootwo-architecture`; architecture, technical judgment, testing strategy, performance and optimization, and maintainability stay under `noootwo-code-health`. Do not add a separate performance skill.
- Every capability has one owner. When a skill needs another's capability, it invokes it and reads its `SKILL.md`; the capability map in `docs/agents/invocation.md` is the source of truth, and the validator enforces it.
- Only `noootwo-ask` is user-invoked. Every other skill stays reachable by the model and by its siblings.
- Do not add a root `SKILL.md`; it prevents default discovery of all child skills.
- `noootwo-workflow` may route to other installed skills as execution resources; it does not add them to the Noootwo public set or capability map.
- Keep per-skill versions in `skills/<skill>/VERSION` and mirror them in `skills.json`.
- Record a durable change to the skill model as an ADR in `docs/adr/`.

## Research Rule

Before changing `noootwo-design` aesthetics, workflow modes, stack playbooks, review gates, public claims, or a stack or library choice, settle it with the `noootwo-research` skill rather than from memory: invoke it, read its `SKILL.md`, and follow it.

- Prefer official docs, framework docs, designer and developer community evidence, and artifacts with visible screenshots or running examples.
- Use X/Twitter, Reddit, HN, Figma, Flutter, React, Vue, and native app communities as signals, not as single-source truth.
- If preferred foreign sources are inaccessible, use domestic fallback sources and record the access limits, source levels, and why the fallback is acceptable.
- Borrow repeatable mechanisms, not leaked prompts, proprietary wording, or surface styling.
- Weigh skill usage cost and engineering feasibility before adding gates, scripts, or required artifacts.
- Do not claim a UI-quality improvement without artifact or screenshot review, and run readiness validation when `.noootwo/` deliverables are involved.
