# Project Status

- Repository: `noootwo/noootwo-vibe`
- Branch model: feature work on `codex/*`, default branch `main`
- Public skill set: `noootwo-ask`, `noootwo-workflow`, `noootwo-product`, `noootwo-design`, `noootwo-review`, `noootwo-docs`, `noootwo-debug`, `noootwo-research`, `noootwo-onboard`
- Release model: independently versioned child skills listed in `skills.json`
- Root `SKILL.md`: intentionally absent so default skill discovery lists all child skills
- Invocation model: `noootwo-ask` is user-invoked; the other eight are model-invoked

## Current Validation Surface

Last verified: 2026-09-17 on this worktree.

- `python scripts/validate_skill_workspace.py .` — includes the authoring budgets: `description` ≤ 200 characters, `SKILL.md` ≤ 120 lines, ≤ 12 reference files each named by a pointer, `short_description` 25–64 characters, no `default_prompt`, and no bare `$noootwo-` reference inside a skill body
- `python scripts/validate_skill_workspace.py .` — also enforces the capability bridge: every skill named in a `SKILL.md` must exist, every public skill must appear in the `docs/agents/invocation.md` capability map, and every skill named there must exist
- `python <skill-creator>/scripts/quick_validate.py skills/noootwo-*` for all nine skills
- `npx -y skills add . --list` and `--full-depth` — must list nine skills
- `python -m py_compile` on the design scripts
- `git diff --check`
- Behaviour measurement: `docs/experiments/skill-behaviour-2026-09-11.md`
- `node --check` on `skills/noootwo-design/scripts/extract_design_tokens.mjs`, plus an end-to-end extraction against a foreign product site and a domestic design system

## Active Risks

- The five specialist skills were rewritten to `docs/agents/skill-authoring.md` in one pass. The behaviour measurement in `docs/experiments/` is the evidence for that rewrite; it is scenario-based, not a statistical claim about rework rates.
- Deterministic enforcement — an engine, edit hooks, or detector rules as `pbakaus/impeccable` uses — is deliberately absent. It is the remaining structural gap between this suite and that project, recorded in [ADR 0006](adr/0006-skill-authoring-standard-and-router.md) for separate evaluation.
- `noootwo-ask` is user-invoked through `policy.allow_implicit_invocation: false`. The repository does not set `disable-model-invocation`, because it ships as a Codex plugin and that validator requires the field to be `false`.
- Skill budgets are defaults. Raising one is a deliberate change to `docs/agents/skill-authoring.md` and the validator together, with the reason recorded.
- Quick polish must stay lightweight: Design Read, Design Contract, and artifact gates must not become full-harness cost for a small local tweak.
- The Product-to-Design Handoff must not carry an unsettled decision that would change the real user, main path, states, acceptance, or trust boundary.
- `noootwo-debug` v0.1.1, `noootwo-research` v0.1.0, and `noootwo-onboard` v0.1.0 are written from a research pass, not from a measured behaviour probe. Their gates are asserted, not yet shown to change what an agent does; the probes below are the evidence that would settle them.
- The capability bridge is enforced mechanically at the name level only. It cannot check ordering, hand-off content, or the loop rules; those stay review questions.
- `noootwo-review` now owns optimization work. The boundary with `noootwo-debug` is a description change and one sentence in each body, not yet a measured routing result.
- `noootwo-design` v0.13.0 adds case capture and a motion language. The extractor needs Node 22+ and a local Chrome; without both, a deep pass records a degraded capture rather than inventing values.
- The motion rules added to `check_visual_gates.py` are advisory by design. An intentional brand curve can trip one, so a finding needs screenshot or DOM confirmation before it changes a decision.
- The native motion guidance in `translate.md` is drawn from platform documentation, not from a measured SwiftUI or Compose project. A device check is still owed.
- Motion register and sourcing were added after the first motion pass, so the six motion eval scenarios are newer than the rest and have not been run either.
- Several motion libraries publish genuine agent-readable indexes as of the 2026-09-17 probe. An index can disappear or move, so a pass records what it actually read.
- The `noReducedMotion` advisory rule reads `document.styleSheets`, which cannot inspect cross-origin stylesheets. A site that handles reduced motion in a CDN stylesheet can therefore produce a false finding; it stays advisory for that reason.
- A project already in flight in `deep` mode will be asked for motion values it never recorded the first time. That is a behaviour change for in-flight work, not a defect, and it appears only when `--deep-mode`, `--implementation-gate`, or `--motion-gate` is passed.
- The free case-library access results were probed on 2026-09-16 and 2026-09-17. Gates and plans change without notice, so a pass records its own reachability result rather than trusting the recorded one.
- `noootwo-design` sits at 110 of 120 `SKILL.md` lines and 10 of 12 reference files. The next addition must compress existing prose.

## Next Actions

- Run the workspace validator after any change to skill layout, versions, metadata, descriptions, or references.
- Re-run `docs/experiments/` scenarios when a skill's flow changes, and record the result beside the previous run.
- Run the `noootwo-debug` scenarios under `skills/noootwo-debug/evals/prompts/` on seeded bugs with a hidden verifier and a decoy, and record the result in `docs/experiments/`.
- Run the `noootwo-research` scenarios under `skills/noootwo-research/evals/prompts/`, including the case where research should not fire, and record the result in `docs/experiments/`.
- Run the `noootwo-onboard` scenarios under `skills/noootwo-onboard/evals/prompts/`, and the optimization scenario under `skills/noootwo-review/evals/prompts/`.
- Run the six motion and four case-capture scenarios under `skills/noootwo-design/evals/prompts/`, and record the results in `docs/experiments/`.
- Exercise `extract_design_tokens.mjs` and the advisory motion rules on a real project artifact, and record the false-positive rate for the deliberately-deviating brand-curve case.
- Update `docs/releases/` and per-skill tags when publishing changed skills.
