# Project Status

- Repository: `noootwo/noootwo-vibe`
- Branch model: feature work on `codex/*`, default branch `main`
- Public skill set: `noootwo-ask`, `noootwo-workflow`, `noootwo-product`, `noootwo-design`, `noootwo-review`, `noootwo-docs`
- Release model: independently versioned child skills listed in `skills.json`
- Root `SKILL.md`: intentionally absent so default skill discovery lists all child skills
- Invocation model: `noootwo-ask` is user-invoked; the other five are model-invoked

## Current Validation Surface

Last verified: 2026-09-11 on this worktree.

- `python scripts/validate_skill_workspace.py .` — includes the authoring budgets: `description` ≤ 200 characters, `SKILL.md` ≤ 120 lines, ≤ 12 reference files each named by a pointer, `short_description` 25–64 characters, no `default_prompt`, and no bare `$noootwo-` reference inside a skill body
- `python <skill-creator>/scripts/quick_validate.py skills/noootwo-*` for all six skills
- `npx -y skills add . --list` and `--full-depth` — must list six skills
- `python -m py_compile` on the design scripts
- `git diff --check`
- Behaviour measurement: `docs/experiments/skill-behaviour-2026-09-11.md`

## Active Risks

- The five specialist skills were rewritten to `docs/agents/skill-authoring.md` in one pass. The behaviour measurement in `docs/experiments/` is the evidence for that rewrite; it is scenario-based, not a statistical claim about rework rates.
- Deterministic enforcement — an engine, edit hooks, or detector rules as `pbakaus/impeccable` uses — is deliberately absent. It is the remaining structural gap between this suite and that project, recorded in [ADR 0006](adr/0006-skill-authoring-standard-and-router.md) for separate evaluation.
- `noootwo-ask` is user-invoked through `policy.allow_implicit_invocation: false`. The repository does not set `disable-model-invocation`, because it ships as a Codex plugin and that validator requires the field to be `false`.
- Skill budgets are defaults. Raising one is a deliberate change to `docs/agents/skill-authoring.md` and the validator together, with the reason recorded.
- Quick polish must stay lightweight: Design Read, Design Contract, and artifact gates must not become full-harness cost for a small local tweak.
- The Product-to-Design Handoff must not carry an unsettled decision that would change the real user, main path, states, acceptance, or trust boundary.

## Next Actions

- Run the workspace validator after any change to skill layout, versions, metadata, descriptions, or references.
- Re-run `docs/experiments/` scenarios when a skill's flow changes, and record the result beside the previous run.
- Update `docs/releases/` and per-skill tags when publishing changed skills.
