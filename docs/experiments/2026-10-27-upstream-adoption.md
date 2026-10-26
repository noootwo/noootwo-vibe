# Upstream Adoption Experiment, 2026-10-27

Revision 4 records the subsequent `0.24.0` release preparation; revision 3 added the eval-contract check, and revision 2 corrected reproduction commands. Earlier findings are unchanged.

## Scope

Validate the Superpowers V7, Huashu Design 3.0, and Impeccable 4.7.0 mechanism
refresh in four existing skills: `noootwo-product`, `noootwo-design`,
`noootwo-code-health`, and `noootwo-workflow`.

The pass tests workflow and evidence-gate mechanics with deterministic probes
and one rendered design fixture. It does not claim a general UI-quality gain or
an independent benchmark of the upstream projects.

## Upstream Baseline

| Source | Reviewed baseline | Evidence level | Access and limits |
| --- | --- | --- | --- |
| Superpowers | `v7.0.1`, commit `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`, released 2026-10-21 | Repository, release, and maintainer-run eval artifacts | The linked 176-conversation evaluation is maintainer-run, not independent replication. |
| Huashu Design | `v3.0.0`, commit `798c4235ebff03d5c45e3c8affdf5e9d18f9dfa7`, released 2026-10-17 | Release source, references, and visible case artifacts | The supplied WeChat article redirected to a verification page with `环境异常`; GitHub source and visible cases were the fallback. The reported blind-test numbers are a tiny author-run sample. |
| Impeccable | `v4.7.0`, commit `aeeb3d8c30b5f95aeeb3e893b0f1a308af8fdb8f`, released 2026-10-19 | Repository, release artifacts, and craft guidance | No independent controlled UI-quality study was found. |

The full source and decision record is
[`docs/reference/upstream-refresh-2026-10-27.md`](../reference/upstream-refresh-2026-10-27.md).
Rulings and rejected alternatives are in
[`ADR 0025`](../adr/0025-evidence-backed-design-and-decision-complete-execution.md).

## Adopted

- Product: grounded first response, facts versus proposals, one controlling
  question or all independent root decisions in one round, explicit user-owned
  how decisions, and agent defaults with reason and reopen condition.
- Design: real low-cost samples before an unresolved direction choice,
  weak-runtime fallback of one full sample plus two lightweight variants,
  same-medium inspected references, and evidence-dependent aesthetic flags.
- Code Health: a conditional Builder Check for non-obvious, cross-session,
  expensive, or cross-boundary handoffs, plus decision-complete plans with
  `Interfaces`, ordered steps, assertions, verification, `Review Focus`, and an
  initial ruling ledger.
- Workflow: reversible ambiguities in approved execution become recorded
  rulings and work continues. Security, privacy, irreversible changes, data
  loss, external side effects or spend, user-owned decisions, and plan
  invalidation remain stop boundaries.

Safety gates remain non-negotiable: WCAG and contrast, readable hierarchy,
keyboard/focus/touch reachability, real content and assets, state completeness,
and recovery from error, empty, loading, permission, and success states.

## Rejected And Deferred

Rejected: fixed opener scripts, mandatory six polished candidates, universal
deep-design ceremony, global appearance memory, a larger style library,
routine re-approval for reversible implementation details, and copying prompts,
templates, brand surfaces, or assets.

Deferred to P2: `.noootwo/appearance-ledger.md`, project-local only and never
global by default. Also deferred: worst-case-data checks, mobile-native checks,
and stronger standard controls for tool surfaces.

## Design Fixture

The fixture under
[`docs/experiments/fixtures/upstream-adoption-2026-10-27/`](fixtures/upstream-adoption-2026-10-27/)
contains three real low/mid-fidelity desktop-web directions:

- `01-field-ledger.html`: institutional field ledger; intentional cream paper,
  system display face, eyebrow labels, and numbered records.
- `02-split-desk.html`: split research desk with utility rail, record list, and
  selected-record inspector.
- `03-living-atlas.html`: spatial archive with map-led navigation and a
  persistent record context.

All three were rendered in local Chromium through Playwright at `1440x900` and
captured under `captures/`. An initial capture of the living-atlas direction
clipped the decorative map at the right edge. The decoration was moved from
`right: -90px` to `right: 0`, the capture was regenerated, and the final image
was inspected.

An independent reviewer that did not generate the fixture found no P0-P3
issues in the regenerated captures. The reviewer confirmed that the fixture
narrowly supports `ready` for its declared 1440x900 static desktop scope. It
does not establish responsive, interaction, focus, non-happy-path, runtime, or
production-polish quality.

## Verification

Executed from the repository root on 2026-10-27:

| Check | Command | Result |
| --- | --- | --- |
| Workspace budgets and capability bridge | `python3 scripts/validate_skill_workspace.py .` | Pass |
| All eleven skill validators | `for dir in skills/noootwo-*; do [ -f "$dir/SKILL.md" ] || continue; /usr/bin/python3 /Users/notwo/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$dir"; done` | 11/11 valid |
| Python syntax | `python3 -m py_compile scripts/*.py skills/*/scripts/*.py` | Pass |
| Design extractor syntax | `node --check skills/noootwo-design/scripts/extract_design_tokens.mjs` | Pass |
| Fixture readiness | `python3 skills/noootwo-design/scripts/validate_noootwo_readiness.py docs/experiments/fixtures/upstream-adoption-2026-10-27 --deep-mode --strict-workflow --style-evidence` | Pass |
| Direction samples are real | `python3 skills/noootwo-design/scripts/eval_noootwo_artifacts.py docs/experiments/fixtures/upstream-adoption-2026-10-27 --scenario direction-samples-not-prose` | Pass |
| Same-medium evidence fields | `python3 skills/noootwo-design/scripts/eval_noootwo_artifacts.py docs/experiments/fixtures/upstream-adoption-2026-10-27 --scenario same-medium-mechanism` | Pass |
| Intentional aesthetic flags | `python3 skills/noootwo-design/scripts/eval_noootwo_artifacts.py docs/experiments/fixtures/upstream-adoption-2026-10-27 --scenario intentional-aesthetic-flags-pass` | Pass |
| Existing no-motion review | `python3 skills/noootwo-design/scripts/eval_noootwo_artifacts.py docs/experiments/fixtures/upstream-adoption-2026-10-27 --scenario leave-simple-justified` | Pass |
| Desktop visual gate, field ledger | `uv run --with playwright python skills/noootwo-design/scripts/check_visual_gates.py docs/experiments/fixtures/upstream-adoption-2026-10-27/directions/01-field-ledger.html --viewport desktop:1440x900` | Pass; no overflow, offscreen critical elements, clipped text, motion, or interface findings |
| Desktop visual gate, split desk | `uv run --with playwright python skills/noootwo-design/scripts/check_visual_gates.py docs/experiments/fixtures/upstream-adoption-2026-10-27/directions/02-split-desk.html --viewport desktop:1440x900` | Pass; no findings |
| Desktop visual gate, living atlas | `uv run --with playwright python skills/noootwo-design/scripts/check_visual_gates.py docs/experiments/fixtures/upstream-adoption-2026-10-27/directions/03-living-atlas.html --viewport desktop:1440x900` | Pass; no findings |
| Eval scenario contracts | Structural check for title, prompt, expected behavior, failure signal, and no unresolved placeholder across the 16 new prompt files | 16/16 complete |
| Project state | `python3 skills/noootwo-state/scripts/noootwo_state.py check` | Pass |
| Patch whitespace | `git diff --check` | Pass |

Negative probes used temporary copies of the fixture:

- A prose-only direction menu was rejected because it had no real sample path.
- An effectively black PNG was rejected as visual evidence.
- A truncated PNG was rejected as visual evidence.
- A source marked `Artifact inspected: no` was rejected.
- A `ready` review with observed hierarchy and readability damage was rejected.

The weak-runtime fallback was accepted only after recording one full sample plus
two lightweight variants.

## Behavior Scenarios

Sixteen opt-in scenario definitions were added or updated:

- Product: grounded first round, independent frontiers in one round, settled
  request with no re-ask, and user-owned how decisions with agent defaults.
- Design: prose menu rejection, viewed sample selection, weak-runtime fallback,
  same-medium mechanism transfer, broken capture rejection, intentional flags
  passing, and demonstrated harm blocking `ready`.
- Code Health: unresolved interface stops the Builder Check, a closed plan goes
  directly to TDD, and a plan missing required decision-complete fields is not
  ready.
- Workflow: a reversible approved-plan conflict becomes a ruling and continues;
  real security, irreversible, external-side-effect, or user-owned conflicts
  stop.

A deterministic contract check confirmed that all 16 prompt files contain a
prompt, expected behavior, a failure signal, and no unresolved placeholder.
This run also executed the deterministic Design artifact probes above. It did
not run fresh model sessions for every prompt scenario, so it makes no
baseline-versus-candidate behavior, speed, or token claim. The prompt files are
the reproducible contracts for that later measurement.

## Limits

- Upstream evidence is maintainer or author evidence, not independent outcome
  research.
- The fixture is static desktop-web evidence at one viewport. Mobile,
  interaction, focus, error recovery, and runtime behavior remain unverified.
- The fixture proves that the evidence and readiness gates can reject bad
  evidence and accept a narrowly scoped reviewed artifact. It does not prove
  that the resulting UI is better across projects.
- At measurement time, no commit, tag, push, publication, or root workspace
  version bump had been made. Release preparation and publication evidence are
  recorded separately from these experiment results.
