# Project Status

- Repository: `noootwo/noootwo-vibe`
- Branch model: feature work on `codex/*`, default branch `main`
- Public skill set: `noootwo-workflow`, `noootwo-docs`, `noootwo-review`, `noootwo-design`
- Release model: independently versioned child skills listed in `skills.json`
- Root `SKILL.md`: intentionally absent so default skill discovery lists all child skills

## Current Validation Surface

Last verified: 2026-07-03 on `codex/noootwo-vibe-monorepo`.

- `python scripts/validate_skill_workspace.py .`
- `npx -y skills add . --list`
- `npx -y skills add . --list --full-depth`
- per-skill `npx -y skills add ./skills/<skill> --list`
- Noootwo Design harness checks under `skills/noootwo-design/scripts/`

Latest result: all workspace, discovery, Python compile, skill quick validation, and design harness bootstrap checks passed. The fresh pending design harness correctly remains non-ready until workflow fields are completed.

## Active Risks

- GitHub plugin-style ingestion is treated as packaging metadata; `skills` CLI discovery is the verified installation surface.
- `noootwo-design` contains the previous design workflow and must remain self-contained for single-skill publishing.
- New workflow/docs/review skills should stay concise and avoid becoming long always-loaded manuals.

## Next Actions

- Run full validation after every skill layout or metadata change.
- Update `docs/releases/` and per-skill tags when publishing changed skills.
