# 0035 — Rendered layout geometry review

## Status

Accepted on 2026-11-23.

## Context

A dense desktop workspace exposed a repeated review failure. A toolbar's filter
chips were visibly too close to the top edge and had more space below. The
rendered container used `padding: 0 28px 14px`. The page composition looked
acceptable, so the review declared the work ready and spent its next correction
on unrelated areas. The actual defect was local, measurable, and still present.

The existing design review could see the screenshot but did not require a
layout-geometry table. Typography already had a rendered role table and a
measured failure blocked `ready` (ADR 0034). Layout had only qualitative phrases
such as "spacing rhythm", "controls do not overlap", and "micro-detail pass".
`scripts/check_visual_gates.py` checked horizontal overflow, off-screen critical
elements, clipped text, and advisory interface rules, but not top-versus-bottom
inset, inner-versus-outer gap, alignment anchors, or sibling overlap. A region
with `padding-top: 0` and `padding-bottom: 14px` could therefore pass.

The prior-art pass found useful mechanisms but no complete solution:

- Refactoring UI Skill separates generation from diagnosis, requires rendered
  evidence, uses a fixed sweep order, and requires a rule id for a finding. Its
  `§3.6` rule says spacing around a group must exceed spacing within it.
- `screen-by-screen` compares a number from the expected state with a number
  from the live DOM, forbids eyeballing as the only signal, re-measures after a
  fix, and sweeps all closed rows before acceptance.
- Oil UI uses an independent visual reviewer, 200-percent inspection, whole
  composition first, and left-edge anchor checks. Its review still depends on
  qualitative judgment.
- Taste Skill uses a browser gate across viewports and checks edges, collisions,
  off-viewport content, and repeated runs. It is optimized for marketing sites.
- Anthropic's long-running-app harness separates generator and evaluator and
  uses Playwright against the live page. Anthropic still reports that small
  layout issues survived that evaluator.
- Playwright and Storybook visual comparisons detect changes against a baseline;
  they do not prove that a layout is semantically correct.

The useful design philosophy is therefore constraint-driven measurement, not
more visual taste: separate generation from judgment, measure the named region,
cite the rule and number, re-measure the fix, and sweep before acceptance.

The toolbar project was examined only as a read-only case. No case source,
test, screenshot, asset, or deployment is part of this decision.

## Decision

1. `noootwo-design` treats rendered layout geometry as a review surface, not as
   an aesthetic impression. A screenshot alone cannot prove spacing, alignment,
   containment, or overlap.
2. Every region changed by the diff, named by the user, or declared by the
   contract gets a geometry row before `ready`. Standard, deep, and production
   work also covers at least one representative region per visible group.
3. The geometry row records the region owner and selector, container box,
   top/right/bottom/left insets, inner and outer gaps, alignment anchor,
   overlap/clip result, and verdict.
4. A single-row toolbar, tab strip, filter row, breadcrumb, or control cluster
   has matching vertical insets within tolerance unless the contract records an
   intentional attachment. When spacing alone communicates grouping, outer
   spacing exceeds inner spacing.
5. Source padding is a lead, not evidence. The rendered inset and populated
   state are authoritative. When no DOM or platform inspector exists, a measured
   screenshot crop or native geometry pass records the method and limitation.
6. Missing region coverage is incomplete evidence, not a pass. `ready` requires
   the table for the changed, user-named, and contract-declared regions.
7. After a geometry repair, the same selector and method are re-measured. All
   closed geometry rows are swept once before `ready`.
8. `scripts/check_visual_gates.py` measures explicit `--region NAME=SELECTOR`
   regions and `data-noootwo-region` elements, reports rendered insets, gaps,
   anchors, overlaps, and clipping, and fails on asymmetric single-row insets,
   sibling overlap, clipping, missing selectors, empty regions, or incomplete
   required coverage. Heuristic outer-gap and edge-scatter findings remain
   advisory.
9. Tolerance follows the local spacing token or a small rendering tolerance.
   The gate catches semantic imbalance such as `0` versus `14px`; it is not a
   mandate for pixel-perfect replication.
10. No new public skill is added. Layout judgment remains inside
    `noootwo-design`; persistence and project state continue through
    `noootwo-state`.

## Consequences

- A toolbar inset, group-spacing, alignment, overlap, or containment defect can
  block `ready` even when the page's overall composition looks calm.
- The review gains a small, bounded cost: only changed, user-named, and
  contract-declared regions need rows; `quick` work may use one targeted region.
- DOM-capable web work gets deterministic evidence. Native work uses the same
  table with platform-inspector or measured-capture evidence.
- Screenshots remain useful for composition, affordance, and visual direction.
  They are no longer sufficient proof of local layout correctness.
- The automation cannot infer every semantic region. A selector map or explicit
  region attribute is the reliable path; heuristic discovery remains advisory.
- The gate records a contract and a script, not a measured model-behavior
  improvement. The regression eval must run in a fresh session to test that.

## Rejected Alternatives

- **Add a layout-review skill.** Layout is part of design ownership; a second
  skill would split one capability and inflate discovery and state.
- **Keep screenshot-only review.** The failure is exactly the case where the
  screenshot looked acceptable while the local geometry was wrong.
- **Trust source padding.** Overrides, flex wrappers, margins, and generated
  components can change the rendered box.
- **Make pixel-perfect comparison the gate.** It creates false failures across
  platforms, fonts, and zoom; semantic invariants and token tolerance are the
  target.
- **Auto-segment every page and fail on every heuristic.** Region ownership and
  intentional asymmetry need a small contract; heuristics stay advisory.
- **Require Figma or a paid inspector.** The skill must work from a live DOM,
  platform preview, or measured capture without a vendor dependency.

## Verification

- `skills/noootwo-design/evals/prompts/layout-geometry-toolbar-miss.md` encodes
  the toolbar asymmetry and the expected return/re-measure loop.
- `scripts/check_visual_gates.py` can be run with
  `--region "toolbar=.contentToolbar" --require-geometry`; the JSON output
  carries geometry rows and hard failures.
- A local fixture with `padding: 0 28px 14px` must report top `0` and a larger
  bottom inset (the fixture reports `15px` because of its `1px` border), with an
  asymmetric vertical inset failure.
- `python scripts/validate_skill_workspace.py .` must pass after the skill,
  reference, eval, ADR, and version changes.

The eval contract is structural until it runs in a fresh model session; this ADR
does not claim a measured behavior improvement.
