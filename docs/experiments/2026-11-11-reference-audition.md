# Reference Audition Experiment, 2026-11-11

## Scope

Implement and test the source-role matrix, two-tier reference audition,
project-local appearance ledger, and mechanism-landing gate for Noootwo Design.
This experiment checks deterministic workflow contracts and fixture behavior. It
does not claim a general UI-quality improvement or a fresh-session model-behavior
gain.

## Source Probe

The design-specific source matrix is
`skills/noootwo-research/references/design-source-registry.md`.

Probes from this machine on 2026-11-11:

| Source | Result | Decision |
| --- | --- | --- |
| Framer Gallery `?md` | `200 text/markdown` | `visual direction`; no product-flow search |
| Awwwards `llms.txt` | `200 text/plain`; robots disallows gallery/search routes | `visual direction` and limited annual-awards API |
| Recent | `200 text/html`; no `llms.txt`; content signal allows reference, not AI training | `visual direction` only |
| React Bits `llms.txt` | `200 text/plain`; React copy-in; free and Pro tiers | `motion mechanism` / `implementation resource` for React Web |
| Thrine | `thrine.app` connection reset; `thethrine.com` `200 text/html` | unclassified until identity and licence are confirmed |
| Mobbin `llms.txt` | `200 text/plain`; MCP Pro+; REST Team+; 60 req/min | paid optional product evidence |
| Refero | `200 text/html`; MCP requires a paid plan | paid optional product evidence |
| Fontshare, Fontsource, Lucide, Phosphor, Heroicons, Tabler | `200` | asset lane; verify per-asset or per-package licence |
| Google Fonts | timeout | conditional asset path; record limitation |
| Unsplash | `401` | conditional; do not assume reuse |
| Pexels | `403` | conditional; do not assume reuse |
| Openverse | timeout | conditional; do not assume reuse |

The probe is an access signal, not a licence grant or an effectiveness claim.

## Implemented Contracts

- New research reference `design-source-registry.md` with seven roles, lanes,
  candidate intake, 90-day freshness, asset records, and named source boundaries.
- Standard light audition: 2-3 candidates, two roles, one inspected primary, at
  most one supplement, and visible rejected candidates.
- Deep audition: 3-5 sources, one same-medium source, full capture and licence
  records, fit scoring, lock, and spikes.
- `.noootwo/reference-board.md` unified for standard and deep; legacy `Source N`
  headings remain readable.
- `.noootwo/appearance-ledger.md` project-local, section-read, review-written,
  never global and never a second state root.
- Mechanism Landing QA: `landed`, `decoration`, `swallowed`, or `missing` with
  artifact evidence and a named user outcome.
- `validate_noootwo_readiness.py --reference-audition`; `--deep-mode` implies it.
- Bootstrap profiles, status, templates, and seven eval prompts.

## Fixtures And Probes

Positive:

- `docs/experiments/fixtures/reference-audition-2026-11-11/` uses a standard
  product-UI surface, two source roles, an inspected primary, one supplement, one
  rejected candidate, and a project-local ledger.
- `docs/experiments/fixtures/upstream-adoption-2026-10-27/` is updated to the new
  fields while retaining `## Source N` headings to test compatibility.

Negative:

- `docs/experiments/fixtures/reference-audition-2026-11-11-negative/` has one
  candidate, a gallery-only primary, no product evidence, an unreachable primary,
  an unknown licence, a stale date, and a pending global-scope ledger.

Deterministic probes exercise:

- standard candidate-count failure;
- product UI without product evidence;
- gallery-only primary;
- component-library-only primary;
- uninspected or missing primary capture;
- deep missing same-medium evidence or licence;
- legacy `Source` heading compatibility;
- missing or pending ledger;
- mechanism missing from the artifact while review claims `ready`.

## Verification

Final local run on 2026-11-11:

| Check | Result |
| --- | --- |
| `python3 scripts/validate_skill_workspace.py .` | pass: 12 public skills, budgets, references, capability map |
| `uv run --with pyyaml python <skill-creator>/scripts/quick_validate.py skills/noootwo-<name>` for all twelve skills | pass: `Skill is valid!` for each |
| `npx -y skills add . --list` | pass: found and listed 12 skills |
| `python3 -m py_compile` on workspace, design, and state Python scripts | pass |
| `node --check skills/noootwo-design/scripts/extract_design_tokens.mjs` | pass |
| `sh -n skills/noootwo-state/scripts/noootwo-state.sh` and both state self-tests | pass |
| Existing Design artifact evals: `direction-samples-not-prose`, `same-medium-mechanism`, `intentional-aesthetic-flags-pass`, and `leave-simple-justified` | pass after accepting both legacy and new reference-board field names |
| `git diff --check` | pass |
| `validate_noootwo_readiness.py docs/experiments/fixtures/reference-audition-2026-11-11 --reference-audition` | pass |
| `validate_noootwo_readiness.py docs/experiments/fixtures/upstream-adoption-2026-10-27 --deep-mode --strict-workflow --style-evidence` | pass; legacy `Source N` headings remain readable |
| `validate_noootwo_readiness.py docs/experiments/fixtures/reference-audition-2026-11-11-negative --reference-audition` | expected fail: candidate count, product evidence, gallery primary, unreachable/uninspected capture, unknown licence, stale date, and non-local pending ledger |

Targeted negative probes also produced the expected rejection for:

- product UI without a selected product-evidence source;
- a gallery as primary direction;
- a component library as primary direction;
- a missing primary capture;
- a primary capture recorded as uninspected;
- a missing appearance ledger;
- a selected mechanism marked `decoration` while review claimed `ready`;
- a deep audition without a selected same-medium source;
- `Licence / reuse: not licensed`;
- a non-image path used as the primary capture;
- an empty `Reject reason` on a rejected candidate.

The 90-day freshness rule applies to remote, login-gated, and paid sources. A
local rendered artifact is still re-opened when the task needs it, but it does
not become stale merely because its file date is old.

The negative probes also caught and fixed two parser defects before final
validation: empty fields could previously consume the next line, and the
existing `same-medium-mechanism` eval only understood the older
`Observed evidence` / `Borrowed mechanism` names. Field reads are now line-bounded,
and the eval accepts both the legacy and current labels.

Bootstrap probes generated `reference-board.md` and a project-local
`appearance-ledger.md` for `minimal`, `deep`, `production`, and `full`; a fresh
full harness still failed readiness with its expected pending blockers. Status
read the positive fixture as `review` with the ledger complete, and the upgraded
deep fixture as `deep`, without a false `review decision is not ready` blocker.

The fixture checks prove deterministic gate behavior, not that a model will
choose the right source or that the resulting UI is better. Visual quality is
claimed only after a rendered artifact or inspected screenshot is reviewed.

## Limits

- No fresh-session model comparison was run for the seven new prompt contracts.
- The positive fixture reuses local rendered direction captures. It proves the
  contract and path resolution, not that a local fixture is a shipped product or
  that the UI is better.
- Source access and licence terms change. The registry date is 2026-11-11 and must
  be re-probed for a later decision or release claim.
- The validator is structural. It cannot prove that a chosen gallery is relevant,
  that a selected product screen is the right audience evidence, or that a
  mechanism genuinely improves comprehension without a review judgment.
