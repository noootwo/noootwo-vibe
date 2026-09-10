# Noootwo Vibe Maintenance

This repository is a multi-skill workspace. The root is not a published skill; the public skills live under `skills/` and are listed in `skills.json`.

## Mandatory Task-Start Check

At the start of every task, before editing any file:

1. Decide whether the work is `direct` (tiny localized edit with an obvious check) or needs a Noootwo skill.
2. `direct` work still passes lifecycle guardrails internally; no ceremony required.
3. Non-direct work must explicitly invoke the matching skill by name (`$noootwo-workflow`, `$noootwo-product`, `$noootwo-design`, `$noootwo-review`, or `$noootwo-docs`) before implementation. "Considering" a skill is not routing; invoke it.
4. If a specialist skill is needed but not available, say so in one line and follow the closest fallback instead of silently skipping.

## Skill Routing

- Use `$noootwo-workflow` when the task is: a new feature or product idea; multi-file or cross-skill change; bugfix or failing check; refactor; release/version/tag/publish; onboarding or handoff from another agent; recovery after repeated failed fixes; correction-loop routing after a user rejection; or any work that needs product/design/docs/review to cooperate. Workflow owns routing and lifecycle guardrails.
- Use `$noootwo-product` when real user, scenario, first loop, scope, IA/main path, interaction model, states, acceptance criteria, or product choices are unclear; for greenfield ideas, feature-list-only requests, backend-shaped flows, or explicit requests for grill-style/detailed confirmation. Product owns the Decision Interview; Workflow must not ask repeated product questions itself.
- Use `$noootwo-design` when UI, visual direction, artifact review, `.noootwo/` deliverables, design systems, or frontend implementation are in scope, and the product path is clear. Unresolved real-user, main-path, state, acceptance, audience, or use-context decisions return to `$noootwo-product`.
- Use `$noootwo-review` before submit or release of code changes, for architecture-boundary/performance/lean/dependency judgment, risky or public-contract diffs, or diagnosing why a change keeps being rejected.
- Use `$noootwo-docs` when behavior, state, release facts, product decisions, or agent instructions change and README/AGENTS/docs/status/ADR/release notes must stay truthful. Behavior or release-fact changes without a docs decision are not closed.

Routing is an invocation, not a thought: when more than one skill applies, start with `$noootwo-workflow`, then explicitly invoke the specialist (`$noootwo-product` -> `$noootwo-design` -> `$noootwo-review`/`$noootwo-docs`) at the moment its trigger matches, and close back through `$noootwo-workflow`.

## Repository Rules

- Keep the public skill set exactly: `noootwo-workflow`, `noootwo-product`, `noootwo-design`, `noootwo-review`, `noootwo-docs` unless the user explicitly changes the product model.
- Do not add `noootwo-architecture`; architecture, technical judgment, testing strategy, performance, and maintainability stay under `$noootwo-review`.
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
