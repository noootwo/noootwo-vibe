# Project Status

- Repository: `noootwo/noootwo-vibe`
- Branch model: feature work on `codex/*`, default branch `main`
- Public skill set: `noootwo-workflow`, `noootwo-product`, `noootwo-design`, `noootwo-review`, `noootwo-docs`
- Release model: independently versioned child skills listed in `skills.json`
- Root `SKILL.md`: intentionally absent so default skill discovery lists all child skills

## Current Validation Surface

Last verified: 2026-07-21 on the current worktree for the context-budget update plus Antfu-style product/design workflow refactor.

- `python scripts/validate_skill_workspace.py .`
- `python /Users/notwo/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/noootwo-product`
- `python /Users/notwo/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/noootwo-design`
- `python /Users/notwo/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/noootwo-workflow`
- `npx -y skills add . --list`
- `npx -y skills add . --list --full-depth`
- `python -m py_compile scripts/validate_skill_workspace.py scripts/sync_local_install.py skills/noootwo-design/scripts/bootstrap_noootwo_harness.py skills/noootwo-design/scripts/validate_noootwo_readiness.py skills/noootwo-design/scripts/eval_noootwo_artifacts.py skills/noootwo-design/scripts/noootwo_status.py`
- Design harness bootstrap with `--profile full`, followed by expected readiness failure on the pending template.
- `rg -n "Design Read|Product-to-Design|anti-slop|dials|semantic token|handoff" skills docs README.md AGENTS.md`
- `wc -l AGENTS.md skills/noootwo-product/SKILL.md skills/noootwo-design/SKILL.md skills/noootwo-workflow/SKILL.md`
- `git diff --check`

Latest result: workspace validation, quick validation, discovery checks, Python compile, harness bootstrap/readiness expectation, keyword scan, line-budget checks, and `git diff --check` passed on this worktree. Discovery still emits existing npm config warnings but exits successfully.

## Active Risks

- GitHub plugin-style ingestion is packaging metadata; `skills` CLI discovery is the verified installation surface.
- `noootwo-product` `v0.3.0` owns Product Discovery, Product Checkpoint, Product Choice Challenge, product decision-layer diagnosis, and Product-to-Design Handoff.
- `noootwo-design` `v0.8.0` uses a shorter entrypoint plus on-demand references; non-quick UI work must declare Design Read and implementation-bound work must carry a Design Contract and artifact review path.
- `noootwo-workflow` `v0.7.3` routes unclear product paths to Product first and passes Product-to-Design Handoff to Design for non-quick UI work.
- `noootwo-docs` `v0.7.0` keeps `docs/status.md` as a current-state snapshot; context-budget detail stays in on-demand references.
- `noootwo-review` `v0.7.0` keeps architecture, technical judgment, testing, performance, and maintainability as review lenses; do not add `noootwo-architecture`.
- Quick polish should stay lightweight; Design Read, semantic-token contracts, and artifact gates must not become full-harness cost for small local tweaks.
- Product-to-Design Handoff must not hide unresolved real-user, main-path, state, or acceptance decisions.
- Local sync should prefer `~/.agents/skills` as the single user-level Noootwo skill root when publishing or syncing later.

## Next Actions

- Run full validation after every skill layout or metadata change.
- Update `docs/releases/` and per-skill tags when publishing changed skills.
