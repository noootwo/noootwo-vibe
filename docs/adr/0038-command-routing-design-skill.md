# 0038 — Command routing and rendered evidence for the design skill

## Status

Accepted on 2026-11-27.

## Context

The `0.26.0` design skill had become counterproductive in production. It carried
a large lifecycle, ten review gates, a 28-bullet readiness check, and a
multi-document harness. A literal `standard` read path cost about 52k tokens
before any rendered inspection. The review still missed hierarchy, reading-order,
fixed-bar, focus, contrast, and copy defects that were visible on the page.

The failure was measured, not assumed:

- A baseline critique found all five planted defects in 342 seconds.
- The `0.26.0` critique found the same five in 315 seconds, but added gate
  structure rather than defect recall.
- A baseline repair fixed four of five in 343 seconds.
- The `0.26.0` repair fixed five of five in 335 seconds, emitted more than 80
  evidence files, still returned `refine`, and failed its own readiness
  validator with 22 errors because its review used a shorter format.
- The readiness validator accepted a fake review with a nonexistent screenshot
  after three dummy documents were added. It rewarded document shape, not
  rendered evidence.
- `ready` required an independent reviewer, so a solo builder could never reach
  it. The gate was structurally unreachable in the common local workflow.

The skill was also sending mixed instructions: `SKILL.md` named one token
extractor, never named the visual-gate script, and the review references still
used `ready`, `refine`, `pivot`, and `needs artifact` while the body described a
different lifecycle.

The external check against Impeccable `skill-v4.11.1` confirmed the durable
mechanism: route by command, load one playbook, run the design assessment before
detector findings, treat invalid captures as `recapture`, and finish with a
small disposition set. The engine, hooks, Live Mode, and provider wrappers are
not required to copy that mechanism.

## Decision

1. Replace the lifecycle and gate stack with command routing:
   `shape`, `build`, `critique`, `polish`, `layout`, `typeset`, `harden`,
   `motion`, `system`, `direction`, `translate`.
2. `SKILL.md` loads one command reference per task. `craft.md` is the shared
   quality floor; the full library is not a default read.
3. The design assessment runs before probe findings enter synthesis. When an
   isolated reviewer is unavailable, the result is labelled
   `DEGRADED: single-context` instead of pretending to be independent.
4. Four dispositions only: `recapture`, `rebuild`, `fix`, `ship`. A builder-only
   review may `ship` local work with `local_only: true`; production or publish
   requires `reviewer: independent`.
5. One `design_probe.py` run writes `probe.json`, one primary capture per
   declared viewport/state, and a bottom capture only where overlap or focus
   occlusion is detected. The probe checks overflow, clipping, fixed/sticky
   overlap, focus occlusion, text and control contrast, control labels, and
   small targets. It does not judge hierarchy or taste.
6. One short `review.json` records the target, command, declared matrix,
   findings with rendered evidence, disposition, reviewer, `local_only`, and
   next action. The validator checks the declared matrix, capture validity,
   finding evidence, the disposition rules, and production independence.
7. The legacy harness, readiness validator, and artifact evals remain for
   historical fixtures only. New work does not bootstrap the multi-file
   harness.

## Evidence

- Fresh-session `critique` with the new skill found all five planted defects and
  added navigation and mobile-header findings in 344 seconds. It changed no
  product file.
- Fresh-session `repair` fixed the mechanical defects, returned `ship` with a
  builder review and `local_only: true`, and produced 23 files: one probe, one
  short review, one probe report, and twenty captures. The blue summary still
  carries high visual weight; that remains a judgment item, not a probe pass.
- The final probe still reports 71 blockers on the planted demo, including the
  `320` overflow, fixed-bar overlap, `1440` focus occlusion, helper contrast at
  `3.03:1`, and input borders at `1.47:1`.
- The repaired artifact validates at `ship` with zero blockers under the final
  probe and validator.
- The validator rejects a missing capture, a fake finding path, a builder
  production claim, `ship` with probe blockers, a mismatched matrix, and `fix`
  without a next action.

## Consequences

- The skill is cheaper to enter and has one obvious reference per task.
- Mechanical defects become reproducible evidence instead of prose claims.
- Hierarchy, composition, and taste remain design judgment. The probe is
  deliberately not a score.
- Local work can close as `ship` without an independent reviewer. Production
  still cannot.
- The two fresh-session probes exercise one operations-console demo. They do not
  prove defect recall on every surface, and no statistical quality or time
  improvement is claimed.

## Rejected Alternatives

- **Keep tuning the gate stack.** The measured failure was the stack: more
  documents, more unreachable disposition, and no recall gain.
- **Copy Impeccable's engine and hooks.** The repository needs the routing and
  evidence order, not a second toolchain.
- **Let the probe decide design quality.** Mechanical checks cannot prove a
  focal point, grouping, or taste.
- **Require an independent reviewer for every `ship`.** That makes local work
  structurally unshippable and was a direct cause of the old `refine` ceiling.
- **Hardcode five states and four viewports for every artifact.** Static pages,
  fixed canvases, and native surfaces cannot satisfy a web-only matrix. The
  validator checks the declared matrix; the design assessment decides whether
  that matrix is adequate.

## Verification

- `python scripts/validate_skill_workspace.py .`
- `python skills/noootwo-design/scripts/design_probe.py docs/experiments/fixtures/design-probe --out <tmp> --browser-channel chrome`
- `python skills/noootwo-design/scripts/validate_design_evidence.py <fixture>`
- Fresh-session critique and repair runs recorded in
  `docs/experiments/2026-11-27-design-skill-rebuild.md`.
