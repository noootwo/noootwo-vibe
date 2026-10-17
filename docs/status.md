# Project Status

- Repository: `noootwo/noootwo-vibe`
- Branch model: feature work on `codex/*`, default branch `main`
- Public skill set: `noootwo-ask`, `noootwo-workflow`, `noootwo-product`, `noootwo-design`, `noootwo-tdd`, `noootwo-code-health`, `noootwo-release`, `noootwo-state`, `noootwo-debug`, `noootwo-research`, `noootwo-onboard`
- Release model: independently versioned child skills listed in `skills.json`
- Root `SKILL.md`: intentionally absent so default skill discovery lists all child skills
- Invocation model: `noootwo-ask` is user-invoked; the other ten are model-invoked

## Current Validation Surface

Last verified: 2026-10-18 on this worktree for workspace, skill, script-syntax, design smoke, local discovery, and clean-install checks.

- `python scripts/validate_skill_workspace.py .` — includes the authoring budgets: `description` ≤ 200 characters, `SKILL.md` ≤ 120 lines, ≤ 12 reference files each named by a pointer, `short_description` 25–64 characters, no `default_prompt`, and no bare `$noootwo-` reference inside a skill body
- `python scripts/validate_skill_workspace.py .` — also enforces the capability bridge: every skill named in a `SKILL.md` must exist, every public skill must appear in the `docs/agents/invocation.md` capability map, and every skill named there must exist
- `python <skill-creator>/scripts/quick_validate.py skills/noootwo-*` for all eleven skills
- `npx -y skills add . --list` and `--full-depth` — must list eleven skills
- `python -m py_compile` on the design and state scripts
- `sh -n skills/noootwo-state/scripts/noootwo-state.sh`
- `python skills/noootwo-state/scripts/noootwo_state.py --self-test`
- `git diff --check`
- Behaviour measurement: `docs/experiments/skill-behaviour-2026-09-11.md`
- `node --check` on `skills/noootwo-design/scripts/extract_design_tokens.mjs`, plus an end-to-end extraction against a foreign product site and a domestic design system
- `node --check` on the `CHECK_JS` payload from `skills/noootwo-design/scripts/check_visual_gates.py`; the advisory interface rules still need an artifact run with Playwright for end-to-end proof
- `python skills/noootwo-design/scripts/eval_noootwo_artifacts.py <project> --scenario leave-simple-justified` — validates a justified no-motion result
- `python skills/noootwo-design/scripts/eval_noootwo_artifacts.py <project> --scenario craft-only-justified` — validates a craft-only intervention
- `python skills/noootwo-design/scripts/eval_noootwo_artifacts.py <project> --scenario add-moment-proof` — validates an authored moment and its evidence
- `python skills/noootwo-design/scripts/eval_noootwo_artifacts.py <project> --scenario explicit-motion-request-honored` — verifies an explicit motion request cannot pass as zero motion
- `python skills/noootwo-design/scripts/validate_noootwo_readiness.py <project> --motion-gate` — validates the intervention decision, user motion intent, implementation tool, library/material decision, and the conditional motion contract
- `docs/agents/borrow-audit.md` maps the prior art each skill was compared against; the Product Design plugin maps primarily to `noootwo-product`, and motion-web maps primarily to `noootwo-design`.
- `docs/adr/0018-contextual-design-intervention.md` records `leave simple | craft only | add moment` as the design decision before motion, source research, or new material.
- `docs/adr/0019-systemic-close-in-debug.md` records the Systemic Close and its eight questions, proportional-response rule, and academic basis from Reason, Leveson, Argyris, Google SRE, and Hollnagel.
- `docs/adr/0019-code-health-integration-read.md` records the pre-implementation Integration Read and Change Shape, including the trigger, skip rule, research evidence, and boundaries.
- `docs/adr/0020-verification-depth-follows-blast-radius.md` records the Change Check / Escalated Check / Release Check split, escalation triggers, CI evidence rule, research basis, and selective-testing boundary.
- `noootwo-code-health` now follows the Fowler refactoring health loop, the bounded Integration Read, and the Change Check / Release Check split; the deciding sources, boundaries, and stop rules are recorded in `docs/reference/borrowed-skills.md`, ADR 0015, ADR 0019, and ADR 0020.
- `noootwo-code-health` is the renamed `noootwo-review` skill (`v0.14.0` rename, currently `v0.17.0`). The old `noootwo-review@v0.13.0` tag remains as history; current docs and routing use the new name.
- `noootwo-release` owns versioning, tags, immutable artifacts, deployment traces, provenance, rollback, and release health; code-health keeps the ship-readiness gate. Release now requires a Release Check for the exact commit.
- Release batch `0.18.0` was published on 2026-10-09 from commit `7469470cf368aff43be44af096ed7d5f352d4270`. Child tags: `noootwo-ask@v0.5.0`, `noootwo-workflow@v0.17.0`, `noootwo-product@v0.10.1`, `noootwo-design@v0.19.0`, `noootwo-tdd@v0.5.0`, `noootwo-code-health@v0.16.0`, `noootwo-research@v0.6.1`, `noootwo-onboard@v0.4.1`. A clean install found eleven skills, and both local install roots match the released child versions.
- Release batch `0.19.0` was published on 2026-10-18 from commit `5d62af29526026c27ef487468223a3b67fbd5978`. Child tags: `noootwo-ask@v0.5.1`, `noootwo-workflow@v0.18.0`, `noootwo-tdd@v0.6.0`, `noootwo-code-health@v0.17.0`, `noootwo-release@v0.2.0`, `noootwo-design@v0.19.1`, `noootwo-debug@v0.5.0`. A clean install from GitHub found eleven skills; both `~/.agents/skills` and `~/.codex/skills` match every released child version. Design fixes the explicit-motion-request downgrade; debug adds the Systemic Close; the code-development skills add Change Check / Release Check depth.

## Active Risks

- The five specialist skills were rewritten to `docs/agents/skill-authoring.md` in one pass. The behaviour measurement in `docs/experiments/` is the evidence for that rewrite; it is scenario-based, not a statistical claim about rework rates.
- Deterministic enforcement — an engine, edit hooks, or detector rules as `pbakaus/impeccable` uses — is deliberately absent. It is the remaining structural gap between this suite and that project, recorded in [ADR 0006](adr/0006-skill-authoring-standard-and-router.md) for separate evaluation.
- `noootwo-ask` is user-invoked through `policy.allow_implicit_invocation: false`. The repository does not set `disable-model-invocation`, because it ships as a Codex plugin and that validator requires the field to be `false`.
- Skill budgets are defaults. Raising one is a deliberate change to `docs/agents/skill-authoring.md` and the validator together, with the reason recorded.
- Quick polish must stay lightweight: Design Read, Design Contract, and artifact gates must not become full-harness cost for a small local tweak.
- The Product-to-Design Handoff must not carry an unsettled decision that would change the real user, main path, states, acceptance, or trust boundary.
- `noootwo-debug`, `noootwo-research`, and `noootwo-onboard` are written from a research pass, not from a measured behaviour probe. Their gates are asserted, not yet shown to change what an agent does; the probes below are the evidence that would settle them.
- `noootwo-debug` now requires a Systemic Close after a proven fix. The risk is over-expansion: a trivial defect can be turned into an architecture program. The proportional-response rule and `simple-one-off-keeps-proportion` eval are written but not yet measured.
- The capability bridge is enforced mechanically at the name level only. It cannot check ordering, hand-off content, or the loop rules; those stay review questions.
- `noootwo-code-health` owns the Fowler refactoring health loop and the pre-implementation Integration Read. The mechanism is evidence-backed, but the real effect on rework, seam choice, and structural-debt closure is still asserted rather than measured.
- The Integration Read can over-trigger on ordinary local changes. The skip rule is explicit, but the positive, skip, and product-boundary evals must run before the trigger is treated as stable.
- `noootwo-workflow` now treats review as part of done and checks that every structural finding has a disposition before closing a non-direct code change. This routing behavior needs the new workflow eval run before it is treated as stable.
- The verification-depth rule reduces per-requirement scope, but its real effect on token and time cost is not measured. The new Change Check, escalation, release-once, and TDD relevant-suite evals are written but not yet run.
- Selective verification can miss dynamic or unmapped dependencies. The escalation triggers and the full Release Check are the guard; a project with a weak affected-test map must escalate sooner.
- `noootwo-tdd` now separates the adding-function hat from the refactoring hat, returns to workflow when the implementation seam is unsettled, and uses relevant-test proof instead of a full suite. The two-hats, return-on-unsettled-shape, and relevant-suite behavior still need scenario measurement.
- `noootwo-release` now consumes the Release Check evidence. Its version, artifact, deployment-trace, rollback, and provenance rules are evidence-backed, but the release evals and a real deployment trace still need to be run before the behavior is treated as proven.
- `noootwo-design` now starts with a contextual intervention decision before motion, source research, or material work. A real-project regression on 2026-10-10 showed an explicit motion request being silently downgraded to `craft only`; `v0.19.1` adds a user-intent gate and implementation-tool evidence. The model still needs scenario measurement to prove the fix. The extractor needs Node 22+ and a local Chrome; without both, a deep pass records a degraded capture rather than inventing values.
- `noootwo-code-health/SKILL.md` is at 118/120 lines. The next change must still compress or replace an existing line before adding another.
- The largest skill files are the design extractor and the design translation/craft references (roughly 500-742 lines). This release does not touch them; `opportunity`: split only when that path is next changed and the context cost is proven.
- The motion rules added to `check_visual_gates.py` are advisory by design. An intentional brand curve can trip one, so a finding needs screenshot or DOM confirmation before it changes a decision.
- The native motion guidance in `translate.md` is drawn from platform documentation, not from a measured SwiftUI or Compose project. A device check is still owed.
- Motion register and sourcing were added after the first motion pass. The new contextual-intervention scenarios join the existing motion, interface-quality, and case-capture scenarios and still need behaviour measurement.
- The motion library map records licences, dependencies, and maintenance state as of 2026-09-22; Shaders and Paper Shaders were checked on 2026-10-09. Registry entries and platform APIs move; a pass re-checks them before adopting a tool.
- The interface checks added to `check_visual_gates.py` are advisory and web-only. Flutter, SwiftUI, and Compose accessibility and state parity are prose gates until a real device or preview artifact is reviewed.
- The screenshot/design-image intake is a contract, not a vision pipeline. It records what is visible and marks the rest as inferred or missing; it does not invent interaction or accessibility states from a still image.
- Several motion libraries publish genuine agent-readable indexes as of the 2026-09-17 probe. An index can disappear or move, so a pass records what it actually read.
- The `noReducedMotion` advisory rule reads `document.styleSheets`, which cannot inspect cross-origin stylesheets. A site that handles reduced motion in a CDN stylesheet can therefore produce a false finding; it stays advisory for that reason.
- A project already in flight in `deep` mode will now be asked for an intervention decision and user motion intent it never recorded. That is a behaviour change for in-flight work, not a defect, and it appears only when `--deep-mode`, `--implementation-gate`, or `--motion-gate` is passed. A requested motion outcome now requires `add moment` or explicit user acceptance of no authored motion.
- The free case-library access results were probed on 2026-09-16 and 2026-09-17. Gates and plans change without notice, so a pass records its own reachability result rather than trusting the recorded one.
- `noootwo-design` sits at 119 of 120 `SKILL.md` lines and 11 of 12 reference files. The next change must replace or compress existing prose before adding a line or using the final reference slot.
- The `0.19.0` batch passed workspace, skill, script-syntax, design smoke, local discovery, GitHub clean-install, and both local-root version checks. Model behaviour evals for Change Check / Release Check, the explicit-motion-request fix, and Systemic Close remain unrun. The installer reported `noootwo-workflow` as High Risk (`Gen`) and Med Risk (`Snyk`), with Med Risk also reported for design, debug, product, release, and research; no independent security audit was performed.

## Next Actions

- Run the workspace validator after any change to skill layout, versions, metadata, descriptions, or references.
- Re-run `docs/experiments/` scenarios when a skill's flow changes, and record the result beside the previous run.
- Run the `noootwo-debug` scenarios under `skills/noootwo-debug/evals/prompts/` on seeded bugs with a hidden verifier and a decoy, including `systemic-close-required`, `recurring-bug-double-loop`, `near-miss-fragile-success`, and `simple-one-off-keeps-proportion`; record whether the close finds concrete latent paths without bloating the fix.
- Run the `noootwo-research` scenarios under `skills/noootwo-research/evals/prompts/`, including the case where research should not fire, and record the result in `docs/experiments/`.
- Run the `noootwo-onboard` scenarios under `skills/noootwo-onboard/evals/prompts/`, and the optimization scenario under `skills/noootwo-code-health/evals/prompts/`.
- Run the new Integration Read positive, skip, and product-boundary scenarios under `skills/noootwo-code-health/evals/prompts/`.
- Run the new Change Check, blast-radius escalation, and release-once scenarios under `skills/noootwo-code-health/evals/prompts/`.
- Run the new refactoring-workflow, preparatory-refactoring, structural-debt, two-hats, and review-after-every-change scenarios.
- Run the TDD relevant-suite scenario and confirm the full suite is reserved for the Release Check.
- Run the new release scenarios under `skills/noootwo-release/evals/prompts/` and the workflow release-routing scenario.
- Run the six contextual-intervention scenarios, then the existing motion, interface-quality, and case-capture scenarios under `skills/noootwo-design/evals/prompts/`, and record the results in `docs/experiments/`.
- Run the explicit-motion-request and installed-motion-runtime scenarios against a real project with `motion` already installed; the expected result is an artifact-visible authored move using the right tool, or a recorded equivalent/rejection.
- Exercise `extract_design_tokens.mjs` and the advisory motion rules on a real project artifact, and record the false-positive rate for the deliberately-deviating brand-curve case.
- For the next release, update the changed skill VERSIONs, mirrors, release notes, and child tags before pushing; the `0.19.0` batch is already published.
