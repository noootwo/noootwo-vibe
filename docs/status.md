# Project Status

- Repository: `noootwo/noootwo-vibe`
- Branch model: feature work on `codex/*`, default branch `main`
- Public skill set: `noootwo-workflow`, `noootwo-product`, `noootwo-design`, `noootwo-review`, `noootwo-docs`
- Release model: independently versioned child skills listed in `skills.json`
- Root `SKILL.md`: intentionally absent so default skill discovery lists all child skills

## Current Validation Surface

Last verified: 2026-08-12 on the current worktree for clarity-gated Product routing, explicit selection gating, deep sequential confirmation, adaptive user-language presentation, structured product-interview handoff, risk-evidence gating, decision-ledger convergence, trigger narrowing, one-command five-skill installation, Product Reality Check, Style Evidence Check, and correction-loop routing.

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
- `noootwo-product` `v0.5.3` owns the adaptive Product Clarity Gate, Decision Interview, explicit user-selection gating, deep sequential confirmation, Product Discovery, Product Checkpoint, Product Reality Check, Product Choice Challenge, product decision-layer diagnosis, and Product-to-Design Handoff. Clear, detailed requests bypass interview ceremony; only unresolved material choices block implementation or design handoff. User-facing interview turns follow the user's language while preserving useful technical identifiers. Deep mode shows relevant checked facts, keeps separate confirmed/assumed/deferred/rejected/active-risk states, asks conditional questions one at a time, and requires explicit final intent-fit confirmation plus risk evidence before handoff.
- `noootwo-design` `v0.9.1` uses a shorter entrypoint plus on-demand references; non-quick UI work must declare Design Read and implementation-bound work must carry a Design Contract and artifact review path. Direction exploration is risk-triggered, not a standard/deep default. High-character or rejected style work uses Style Evidence Check before trusting style prose, and unresolved user/path/state/acceptance/audience/use-context decisions return to Product.
- `noootwo-workflow` `v0.7.7` routes product-shaped work through Product Clarity Gate, preserves deep-confirmation intent and presentation language through the structured Product Interview Handoff packet, blocks execution only while `waiting_on: user_answer`, routes repeated correction loops back to Product Reality Check or Style Evidence Check, and passes Product-to-Design Handoff to Design for non-quick UI work only after convergence.
- `noootwo-docs` `v0.7.0` keeps `docs/status.md` as a current-state snapshot; context-budget detail stays in on-demand references.
- `noootwo-review` `v0.7.1` keeps architecture, technical judgment, testing, performance, maintainability, lean/context-cost, and skill-flow bloat as review lenses; do not add `noootwo-architecture`.
- Quick polish should stay lightweight; Design Read, semantic-token contracts, and artifact gates must not become full-harness cost for small local tweaks.
- Product-to-Design Handoff must not hide unresolved real-user, main-path, state, acceptance, user-comprehension, or style-evidence risks.
- Decision Interview must not become a fixed questionnaire or default ceremony for small code fixes, quick UI polish, docs tweaks, or detailed briefs whose product path is already clear. For a genuine product-direction gap, it is an explicit wait-for-selection gate: deep mode is reserved for detailed-confirmation requests, high-risk scope, rejected interpretations, or dependent product decisions, and must stop once the path is ready and the user has selected or delegated every material choice.

## Next Actions

- Run full validation after every skill layout or metadata change.
- Update `docs/releases/` and per-skill tags when publishing changed skills.
