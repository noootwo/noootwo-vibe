# Project Status

- Repository: `noootwo/noootwo-vibe`
- Branch model: feature work on `codex/*`, default branch `main`
- Public skill set: `noootwo-ask`, `noootwo-workflow`, `noootwo-product`, `noootwo-design`, `noootwo-tdd`, `noootwo-code-health`, `noootwo-state`, `noootwo-debug`, `noootwo-research`, `noootwo-onboard`
- Release model: independently versioned child skills listed in `skills.json`
- Root `SKILL.md`: intentionally absent so default skill discovery lists all child skills
- Invocation model: `noootwo-ask` is user-invoked; the other nine are model-invoked

## Current Validation Surface

Last verified: 2026-09-24 on this worktree.

- `python scripts/validate_skill_workspace.py .` — includes the authoring budgets: `description` ≤ 200 characters, `SKILL.md` ≤ 120 lines, ≤ 12 reference files each named by a pointer, `short_description` 25–64 characters, no `default_prompt`, and no bare `$noootwo-` reference inside a skill body
- `python scripts/validate_skill_workspace.py .` — also enforces the capability bridge: every skill named in a `SKILL.md` must exist, every public skill must appear in the `docs/agents/invocation.md` capability map, and every skill named there must exist
- `python <skill-creator>/scripts/quick_validate.py skills/noootwo-*` for all ten skills
- `npx -y skills add . --list` and `--full-depth` — must list ten skills
- `python -m py_compile` on the design and state scripts
- `sh -n skills/noootwo-state/scripts/noootwo-state.sh`
- `python skills/noootwo-state/scripts/noootwo_state.py --self-test`
- `git diff --check`
- Behaviour measurement: `docs/experiments/skill-behaviour-2026-09-11.md`
- `node --check` on `skills/noootwo-design/scripts/extract_design_tokens.mjs`, plus an end-to-end extraction against a foreign product site and a domestic design system
- `node --check` on the `CHECK_JS` payload from `skills/noootwo-design/scripts/check_visual_gates.py`; the advisory interface rules still need an artifact run with Playwright for end-to-end proof
- `docs/agents/borrow-audit.md` maps the prior art each skill was compared against; the Product Design plugin maps primarily to `noootwo-product`, and motion-web maps primarily to `noootwo-design`.
- `noootwo-code-health` now follows the Fowler refactoring health loop; the deciding sources and boundaries are recorded in `docs/reference/borrowed-skills.md` and ADR 0015.
- `noootwo-code-health` is the renamed `noootwo-review` skill (`v0.14.0`). The old `noootwo-review@v0.13.0` tag remains as history; current docs and routing use the new name.

## Active Risks

- The five specialist skills were rewritten to `docs/agents/skill-authoring.md` in one pass. The behaviour measurement in `docs/experiments/` is the evidence for that rewrite; it is scenario-based, not a statistical claim about rework rates.
- Deterministic enforcement — an engine, edit hooks, or detector rules as `pbakaus/impeccable` uses — is deliberately absent. It is the remaining structural gap between this suite and that project, recorded in [ADR 0006](adr/0006-skill-authoring-standard-and-router.md) for separate evaluation.
- `noootwo-ask` is user-invoked through `policy.allow_implicit_invocation: false`. The repository does not set `disable-model-invocation`, because it ships as a Codex plugin and that validator requires the field to be `false`.
- Skill budgets are defaults. Raising one is a deliberate change to `docs/agents/skill-authoring.md` and the validator together, with the reason recorded.
- Quick polish must stay lightweight: Design Read, Design Contract, and artifact gates must not become full-harness cost for a small local tweak.
- The Product-to-Design Handoff must not carry an unsettled decision that would change the real user, main path, states, acceptance, or trust boundary.
- `noootwo-debug`, `noootwo-research`, and `noootwo-onboard` are written from a research pass, not from a measured behaviour probe. Their gates are asserted, not yet shown to change what an agent does; the probes below are the evidence that would settle them.
- The capability bridge is enforced mechanically at the name level only. It cannot check ordering, hand-off content, or the loop rules; those stay review questions.
- `noootwo-code-health` now owns the Fowler refactoring health loop, including preparatory review, post-green review, and triggered Structure Sweeps. The workflow model is evidence-backed, but its effect on real rework and structural-debt closure is still asserted rather than measured.
- `noootwo-workflow` now treats review as part of done and checks that every structural finding has a disposition before closing a non-direct code change. This routing behavior needs the new workflow eval run before it is treated as stable.
- `noootwo-tdd` now separates the adding-function hat from the refactoring hat and no longer defers a large touched file by default. The two-hats and debt-disposition behavior still needs scenario measurement.
- `noootwo-design` adds case capture and a motion language. The extractor needs Node 22+ and a local Chrome; without both, a deep pass records a degraded capture rather than inventing values.
- `noootwo-code-health/SKILL.md` is at the 120-line limit. `planned`: the next review change must compress or replace an existing line before adding another.
- The largest skill files are the design extractor and the design translation/craft references (roughly 500-742 lines). This release does not touch them; `opportunity`: split only when that path is next changed and the context cost is proven.
- The motion rules added to `check_visual_gates.py` are advisory by design. An intentional brand curve can trip one, so a finding needs screenshot or DOM confirmation before it changes a decision.
- The native motion guidance in `translate.md` is drawn from platform documentation, not from a measured SwiftUI or Compose project. A device check is still owed.
- Motion register and sourcing were added after the first motion pass, so the seven motion, four interface-quality, and four case-capture scenarios are newer than the rest and have not been run either.
- The motion library map records licences, dependencies, and maintenance state as of 2026-09-22. Registry entries and platform APIs move; a pass re-checks them before adopting a tool.
- The interface checks added to `check_visual_gates.py` are advisory and web-only. Flutter, SwiftUI, and Compose accessibility and state parity are prose gates until a real device or preview artifact is reviewed.
- The screenshot/design-image intake is a contract, not a vision pipeline. It records what is visible and marks the rest as inferred or missing; it does not invent interaction or accessibility states from a still image.
- Several motion libraries publish genuine agent-readable indexes as of the 2026-09-17 probe. An index can disappear or move, so a pass records what it actually read.
- The `noReducedMotion` advisory rule reads `document.styleSheets`, which cannot inspect cross-origin stylesheets. A site that handles reduced motion in a CDN stylesheet can therefore produce a false finding; it stays advisory for that reason.
- A project already in flight in `deep` mode will be asked for motion values it never recorded the first time. That is a behaviour change for in-flight work, not a defect, and it appears only when `--deep-mode`, `--implementation-gate`, or `--motion-gate` is passed.
- The free case-library access results were probed on 2026-09-16 and 2026-09-17. Gates and plans change without notice, so a pass records its own reachability result rather than trusting the recorded one.
- `noootwo-design` sits at 117 of 120 `SKILL.md` lines and 11 of 12 reference files. The next addition must compress existing prose or replace a reference rather than add another.

## Next Actions

- Run the workspace validator after any change to skill layout, versions, metadata, descriptions, or references.
- Re-run `docs/experiments/` scenarios when a skill's flow changes, and record the result beside the previous run.
- Run the `noootwo-debug` scenarios under `skills/noootwo-debug/evals/prompts/` on seeded bugs with a hidden verifier and a decoy, and record the result in `docs/experiments/`.
- Run the `noootwo-research` scenarios under `skills/noootwo-research/evals/prompts/`, including the case where research should not fire, and record the result in `docs/experiments/`.
- Run the `noootwo-onboard` scenarios under `skills/noootwo-onboard/evals/prompts/`, and the optimization scenario under `skills/noootwo-code-health/evals/prompts/`.
- Run the new refactoring-workflow, preparatory-refactoring, structural-debt, two-hats, and review-after-every-change scenarios.
- Run the seven motion, four interface-quality, and four case-capture scenarios under `skills/noootwo-design/evals/prompts/`, and record the results in `docs/experiments/`.
- Exercise `extract_design_tokens.mjs` and the advisory motion rules on a real project artifact, and record the false-positive rate for the deliberately-deviating brand-curve case.
- Update `docs/releases/` and per-skill tags when publishing changed skills.
