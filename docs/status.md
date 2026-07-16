# Project Status

- Repository: `noootwo/noootwo-vibe`
- Branch model: feature work on `codex/*`, default branch `main`
- Public skill set: `noootwo-workflow`, `noootwo-product`, `noootwo-design`, `noootwo-review`, `noootwo-docs`
- Release model: independently versioned child skills listed in `skills.json`
- Root `SKILL.md`: intentionally absent so default skill discovery lists all child skills

## Current Validation Surface

Last verified: 2026-07-17 on the current worktree for the `v0.7.0` five-skill Product addition.

- `python scripts/validate_skill_workspace.py .`
- `npx -y skills add . --list`
- `npx -y skills add . --list --full-depth`
- per-skill `npx -y skills add ./skills/<skill> --list`
- `python /Users/notwo/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/<skill>`
- `python -m py_compile scripts/validate_skill_workspace.py scripts/sync_local_install.py skills/noootwo-design/scripts/*.py`
- local sync duplicate-cleanup test using temporary `agents` and `codex` skill roots
- color-calibration content contract check for pure-gray SaaS, high-contrast exceptions, error-form safety, dark mode boundaries, and PDF color-system mechanisms
- performance-review content contract check for frontend loading, frontend rendering, backend/API latency, database/query cost, algorithm/runtime hotspots, and safety boundaries
- Product content contract check for five-skill versions, README/skills manifest, Product Choice Challenge, Design route-back, Review architecture lens, ADR, release notes, and no `noootwo-architecture`
- Noootwo Design harness checks under `skills/noootwo-design/scripts/`

Latest result: workspace validation, Python compile, quick validation for all five skills, aggregate discovery, full-depth discovery, per-skill discovery for all five skills, content contract, local sync duplicate-cleanup test, `git diff --check`, and Noootwo Design harness pending-readiness check passed. The `npx` discovery commands emitted existing npm config warnings but exited successfully and found the expected skills.

## Active Risks

- GitHub plugin-style ingestion is treated as packaging metadata; `skills` CLI discovery is the verified installation surface.
- `noootwo-product` is new in `v0.7.0`; it must stay lightweight and default to Product Checkpoint rather than large PRDs.
- `noootwo-design` contains the previous design workflow and must remain self-contained for single-skill publishing.
- `noootwo-workflow` `v0.7.0` routes unclear product paths to Product before Design or implementation.
- `noootwo-review` `v0.7.0` keeps architecture, technical judgment, testing, performance, and maintainability as review lenses; do not add `noootwo-architecture`.
- `noootwo-design` `v0.7.0` focuses on UI/frontend execution after product path clarity; quick polish should not require full `.noootwo/` harness completion.
- `noootwo-review` performance review remains an evidence-first, on-demand reference; it should report verification gaps instead of speculative optimization claims.
- `noootwo-design` color-system calibration remains an on-demand reference; it should not become a default quick-mode gate.
- Local sync should prefer `~/.agents/skills` as the single user-level Noootwo skill root and remove duplicate `noootwo-*` copies from `~/.codex/skills` when the agent-root copy exists.
- The new project audit templates should stay minimal; do not turn them into automatic full scaffolding without evidence from repeated use.
- Lean review must not claim current-repo token, dollar, or speed savings without a measured baseline.

## Next Actions

- Run full validation after every skill layout or metadata change.
- Update `docs/releases/` and per-skill tags when publishing changed skills.
