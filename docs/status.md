# Project Status

- Repository: `noootwo/noootwo-vibe`
- Branch model: feature work on `codex/*`, default branch `main`
- Public skill set: `noootwo-workflow`, `noootwo-product`, `noootwo-design`, `noootwo-review`, `noootwo-docs`
- Release model: independently versioned child skills listed in `skills.json`
- Root `SKILL.md`: intentionally absent so default skill discovery lists all child skills

## Current Validation Surface

Last verified: 2026-09-10 on the current worktree for mandatory task-start skill invocation, routing-as-invocation across Product/Design/Review/Docs, grilling-style frontier-round Decision Interview (fact self-serve, fixed question format, frontier-empty confirmation gate), single-gap light interview, workflow rework diagnosis, hard submit/release review and docs triggers, impeccable-derived bounded verification and hard bans in Design review, one-command five-skill installation, Product Reality Check, Style Evidence Check, and correction-loop routing.

- `python scripts/validate_skill_workspace.py .`
- `python /Users/notwo/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/noootwo-product`
- `python /Users/notwo/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/noootwo-design`
- `python /Users/notwo/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/noootwo-workflow`
- `python /Users/notwo/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/noootwo-review`
- `python /Users/notwo/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/noootwo-docs`
- `npx -y skills add . --list`
- `npx -y skills add . --list --full-depth`
- `python -m py_compile skills/noootwo-design/scripts/validate_noootwo_readiness.py skills/noootwo-design/scripts/eval_noootwo_artifacts.py`
- `rg -n "Decision Interview|Product-to-Design|Style Evidence|Product Reality|question|fixed questionnaire|description:" skills README.md docs AGENTS.md .codex-plugin/plugin.json`
- `wc -l AGENTS.md skills/noootwo-*/SKILL.md docs/status.md`
- `git diff --check`

Latest result: workspace validation, all five quick validations, aggregate and per-skill discovery, a clean five-skill install into a temporary Codex target, Python compile, line-budget checks, and `git diff --check` passed on this worktree. Discovery still emits existing npm config warnings but exits successfully.

## Active Risks

- GitHub plugin-style ingestion is packaging metadata; `skills` CLI discovery is the verified installation surface.
- `noootwo-product` `v0.6.0` owns the adaptive Product Clarity Gate, light single-question interview for one material gap, and deep Decision Interview built on grilling mechanics: decision tree, frontier rounds with fixed question format, fact self-serve, recomputed frontier after each round, decision ledger, and an explicit shared-understanding/intent-fit confirmation gate before handoff. Clear, detailed requests bypass interview ceremony; only unresolved material choices block implementation or design handoff.
- `noootwo-design` `v0.10.0` uses a shorter entrypoint plus on-demand references; non-quick UI work must declare Design Read and implementation-bound work must carry a Design Contract and artifact review path. Review now uses bounded verification (batched inspection, one fix batch, at most one confirm round), hard bans (eyebrow/kicker, numbered section markers, gradient text, hard offset shadows, system display face, emoji icons, cream/beige default, zero-blur halo), a browser-surfaces check, and separated final review. Direction exploration is risk-triggered. Unresolved user/path/state/acceptance/audience/use-context decisions return to Product. Deterministic anti-slop scanning scripts are deferred to a later round.
- `noootwo-workflow` `v0.8.0` owns mandatory task-start routing with routing-as-invocation (explicitly invoke specialists, never only "consider" them), rework diagnosis after user rejection, compact handoff packets, preservation of deep-confirmation intent, and execution blocking only while `waiting_on: user_answer`.
- `noootwo-review` `v0.8.0` adds a hard pre-submit/release review trigger, rework diagnosis lens, and risk-class handoff to Workflow specialists.
- `noootwo-docs` `v0.8.0` adds a hard docs decision trigger for behavior/state/release/agent-instruction changes and keeps `docs/status.md` as a current-state snapshot.
- Quick polish should stay lightweight; Design Read, semantic-token contracts, and artifact gates must not become full-harness cost for small local tweaks.
- Product-to-Design Handoff must not hide unresolved real-user, main-path, state, acceptance, user-comprehension, or style-evidence risks.
- Decision Interview must not become a fixed questionnaire or default ceremony for small code fixes, quick UI polish, docs tweaks, or detailed briefs whose product path is already clear. Frontier rounds replace one-question-at-a-time in deep mode; they must not ask questions whose prerequisites are unsettled, and must stop once the path is ready and the user has selected or delegated every material choice.

## Next Actions

- Run full validation after every skill layout or metadata change.
- Update `docs/releases/` and per-skill tags when publishing changed skills.
