# Project Status

- Repository: `noootwo/noootwo-vibe`
- Branch model: feature work on `codex/*`, default branch `main`
- Public skill set: `noootwo-workflow`, `noootwo-product`, `noootwo-design`, `noootwo-review`, `noootwo-docs`
- Release model: independently versioned child skills listed in `skills.json`
- Root `SKILL.md`: intentionally absent so default skill discovery lists all child skills

## Current Validation Surface

Last verified: 2026-07-23 on the current worktree for trigger narrowing, risk-triggered direction exploration, Product Reality Check, Style Evidence Check, and correction-loop routing.

- `python scripts/validate_skill_workspace.py .`
- `python /Users/notwo/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/noootwo-product`
- `python /Users/notwo/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/noootwo-design`
- `python /Users/notwo/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/noootwo-workflow`
- `python /Users/notwo/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/noootwo-review`
- `python /Users/notwo/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/noootwo-docs`
- `npx -y skills add . --list`
- `npx -y skills add . --list --full-depth`
- `python -m py_compile skills/noootwo-design/scripts/validate_noootwo_readiness.py skills/noootwo-design/scripts/eval_noootwo_artifacts.py`
- `rg -n "Product Reality|Style Evidence|Design Read|Artifact Review|correction|scenario all|description:" skills README.md docs AGENTS.md`
- `wc -l AGENTS.md skills/noootwo-*/SKILL.md docs/status.md`
- `git diff --check`

Latest result: workspace validation, quick validation, discovery checks, Python compile, keyword scan, line-budget checks, and `git diff --check` passed on this worktree. Discovery still emits existing npm config warnings but exits successfully.

## Active Risks

- GitHub plugin-style ingestion is packaging metadata; `skills` CLI discovery is the verified installation surface.
- `noootwo-product` `v0.4.0` owns Product Discovery, Product Checkpoint, Product Reality Check, Product Choice Challenge, product decision-layer diagnosis, and Product-to-Design Handoff.
- `noootwo-design` `v0.9.0` uses a shorter entrypoint plus on-demand references; non-quick UI work must declare Design Read and implementation-bound work must carry a Design Contract and artifact review path. Direction exploration is risk-triggered, not a standard/deep default. High-character or rejected style work uses Style Evidence Check before trusting style prose.
- `noootwo-workflow` `v0.7.4` routes unclear product paths to Product first, routes repeated correction loops back to Product Reality Check or Style Evidence Check, and passes Product-to-Design Handoff to Design for non-quick UI work.
- `noootwo-docs` `v0.7.0` keeps `docs/status.md` as a current-state snapshot; context-budget detail stays in on-demand references.
- `noootwo-review` `v0.7.0` keeps architecture, technical judgment, testing, performance, and maintainability as review lenses; do not add `noootwo-architecture`.
- Quick polish should stay lightweight; Design Read, semantic-token contracts, and artifact gates must not become full-harness cost for small local tweaks.
- Product-to-Design Handoff must not hide unresolved real-user, main-path, state, acceptance, user-comprehension, or style-evidence risks.
- This release batch must sync both `~/.agents/skills` and `~/.codex/skills`; use `--no-dedupe-codex` when syncing the agent root first.

## Next Actions

- Run full validation after every skill layout or metadata change.
- Update `docs/releases/` and per-skill tags when publishing changed skills.
