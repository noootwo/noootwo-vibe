# Project Status

- Repository: `noootwo/noootwo-vibe`
- Branch model: feature work on `codex/*`, default branch `main`
- Public skill set: `noootwo-workflow`, `noootwo-docs`, `noootwo-review`, `noootwo-design`
- Release model: independently versioned child skills listed in `skills.json`
- Root `SKILL.md`: intentionally absent so default skill discovery lists all child skills

## Current Validation Surface

Last verified: 2026-07-06 on `codex/noootwo-vibe-monorepo` for the `v0.5.0` color-system calibration and performance-review enhancements.

- `python scripts/validate_skill_workspace.py .`
- `npx -y skills add . --list`
- `npx -y skills add . --list --full-depth`
- per-skill `npx -y skills add ./skills/<skill> --list`
- `python /Users/notwo/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/<skill>`
- color-calibration content contract check for pure-gray SaaS, high-contrast exceptions, error-form safety, dark mode boundaries, and PDF live-system mechanisms
- performance-review content contract check for frontend loading, frontend rendering, backend/API latency, database/query cost, algorithm/runtime hotspots, and safety boundaries
- Noootwo Design harness checks under `skills/noootwo-design/scripts/`

Latest result: workspace validation, Python compile, skill quick validation, aggregate discovery, full-depth discovery, per-skill discovery, color-calibration content contract checks, performance-review content contract checks, and Noootwo Design bootstrap/readiness checks passed.

## Active Risks

- GitHub plugin-style ingestion is treated as packaging metadata; `skills` CLI discovery is the verified installation surface.
- `noootwo-design` contains the previous design workflow and must remain self-contained for single-skill publishing.
- Workflow/docs `v0.5.0` are version-aligned only and should stay concise at the entry point.
- `noootwo-review` `v0.5.0` adds performance review as an evidence-first, on-demand reference; it should report verification gaps instead of speculative optimization claims.
- `noootwo-design` `v0.5.0` adds color-system calibration as an on-demand reference; it should not become a default quick-mode gate.
- The new project audit templates should stay minimal; do not turn them into automatic full scaffolding without evidence from repeated use.
- Lean review must not claim current-repo token, dollar, or speed savings without a measured baseline.

## Next Actions

- Run full validation after every skill layout or metadata change.
- Update `docs/releases/` and per-skill tags when publishing changed skills.
