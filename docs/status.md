# Project Status

- Repository: `noootwo/noootwo-vibe`
- Branch model: feature work on `codex/*`, default branch `main`
- Public skill set: `noootwo-workflow`, `noootwo-docs`, `noootwo-review`, `noootwo-design`
- Release model: independently versioned child skills listed in `skills.json`
- Root `SKILL.md`: intentionally absent so default skill discovery lists all child skills

## Current Validation Surface

Last verified: 2026-07-10 on the current worktree for the `v0.6.1` lifecycle-guardrail workflow and pre-submit review gate changes.

- `python scripts/validate_skill_workspace.py .`
- `npx -y skills add . --list`
- `npx -y skills add . --list --full-depth`
- per-skill `npx -y skills add ./skills/<skill> --list`
- `python /Users/notwo/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/<skill>`
- `python -m py_compile scripts/validate_skill_workspace.py scripts/sync_local_install.py skills/noootwo-design/scripts/*.py`
- color-calibration content contract check for pure-gray SaaS, high-contrast exceptions, error-form safety, dark mode boundaries, and PDF color-system mechanisms
- performance-review content contract check for frontend loading, frontend rendering, backend/API latency, database/query cost, algorithm/runtime hotspots, and safety boundaries
- Noootwo Design harness checks under `skills/noootwo-design/scripts/`

Latest result: workspace validation, quick validation for `noootwo-workflow` and `noootwo-review`, aggregate discovery, full-depth discovery, and per-skill discovery for changed skills passed. The `npx` discovery commands emitted existing npm config warnings but exited successfully and found the expected skills.

## Active Risks

- GitHub plugin-style ingestion is treated as packaging metadata; `skills` CLI discovery is the verified installation surface.
- `noootwo-design` contains the previous design workflow and must remain self-contained for single-skill publishing.
- `noootwo-workflow` `v0.6.1` adds lifecycle guardrails; these must stay short decisions and should not become an always-visible checklist for small edits.
- `noootwo-review` `v0.6.1` adds a pre-submit review gate; small diffs should be self-reviewed and directly fixed, while broad or risky diffs need structured review.
- `noootwo-design` `v0.6.0` lowers quick-mode default cost; quick polish should not require full `.noootwo/` harness completion.
- `noootwo-review` performance review remains an evidence-first, on-demand reference; it should report verification gaps instead of speculative optimization claims.
- `noootwo-design` color-system calibration remains an on-demand reference; it should not become a default quick-mode gate.
- The new project audit templates should stay minimal; do not turn them into automatic full scaffolding without evidence from repeated use.
- Lean review must not claim current-repo token, dollar, or speed savings without a measured baseline.

## Next Actions

- Run full validation after every skill layout or metadata change.
- Update `docs/releases/` and per-skill tags when publishing changed skills.
