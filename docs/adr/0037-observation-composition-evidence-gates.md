# 0037 — Observation, composition, and evidence gates

## Status

Accepted on 2026-11-25. Superseded in part by
[ADR 0038](0038-command-routing-design-skill.md): the observation-first and
rendered-evidence principles remain, while the gate stack, `ready` ceiling, and
multi-document harness were replaced by command routing and a bounded probe.

## Context

Repeated UI reviews shared one failure shape. A page had a visible hierarchy,
reading-order, or local layout defect, but the review scored the surface first,
looked at the area named by the previous change, and spent its correction on an
unrelated detail. The rendered page was available; the review still missed what
the page showed.

The existing gates were not empty. `noootwo-design` already required artifact
evidence, a Comprehension Gate, typography evidence, a Layout Geometry Gate,
accessibility checks, and bounded re-review. The gap was the order and the
forcing function:

- `references/review.md` opened with a 100-point score table. It had no blind
  observation step before scoring.
- `review.md` contained no composition vocabulary for visual weight, proximity,
  Gestalt grouping, squint testing, or reading order. It could measure a toolbar
  inset while missing that the page had no focal point.
- `quick` work could "make the change, check it" with no rendered evidence
  record. The readiness validator was a delivery gate, not an ordinary UI step.
- An independent reviewer was preferred, not required. A builder could
  self-certify `ready`.
- The accessibility gate covered contrast, keyboard, focus, and touch, but not
  the WCAG 2.2 reflow, non-text contrast, text-spacing, focus-obscured,
  dragging, target-size, redundant-entry, or accessible-authentication deltas.

The prior-art pass reviewed `pbakaus/impeccable` `skill-v4.11.0` (commit
`88cfafae649164e6dc48b88d3c0c1bf6662eaade`, released 2026-11-24). Its current
method separates design judgment (Assessment A) from detector and browser
evidence (Assessment B), requires the design assessment before detector findings
enter synthesis, and treats a missing or invalid screenshot as
`disposition: recapture`. Its `layout` reference uses the squint test, reading
order, grouping, rhythm, structure, density, adaptation, and extremes. Its
finish reviewer requires desktop and mobile captures before review and refuses
to score malformed evidence. Version 4.11 adds save provenance, critique page
captures, and surface-specific context loading; it does not add a new design
rubric. The useful mechanism is the evidence order, not the Rust engine, CLI,
hooks, or Live Mode.

## Decision

1. `review.md` starts with an Observation Gate. The reviewer records 5-8 blind
   observations, up to three first-pass defects, one must-not-change item, and
   an evidence handle before opening the score table or automated findings.
2. `review.md` adds a Composition Pass for squint-based reading order, grouping
   and proximity, visual weight, rhythm, density, alignment and topology, and
   adaptation or extremes. A clean geometry table cannot pass it.
3. Render evidence becomes a hard gate. A missing, black, blank, stale, or
   wrong-region/state capture is `needs artifact`; a source read or DOM query is
   not observation evidence.
4. `ready` requires `Reviewer independence: independent reviewer`. A fresh
   session that sees only the artifact, contract, and evidence can serve. A
   builder-only review is capped at `refine`.
5. `quick` records a five-line observation card in the conversation: changed,
   rendered at, saw, defect, decision. It stays cheap, but it cannot claim
   `ready` from source inspection alone.
6. `craft.md` adds the WCAG 2.2 AA delta, a `320` CSS px reflow viewport, a
   language-aware line-length rule, a role-scoped `11-12px` dense-desktop floor,
   and the WCAG `24x24` target-size minimum with the larger product baseline
   kept separate.
7. The readiness validator and harness template require the Observation Gate,
   Composition Pass, and reviewer-independence record. `check_visual_gates.py`
   adds the `320` reflow viewport and moves its advisory small-target threshold
   from `40px` to the WCAG `24px` minimum.

## Consequences

- A calm overall screenshot no longer proves readiness. The reviewer must say
  what leads, what groups, what fails, and where it saw it.
- A layout or hierarchy defect can block `ready` before the score table exists,
  so the score cannot rationalize a miss.
- `quick` gains one evidence card, not a full harness. It does not require
  discovery, a direction menu, or a full `.noootwo/review.md`.
- A harness without a subagent can use a fresh session for independent review.
  If neither is available, the change can still be delivered as `refine`, but
  it cannot be called `ready`.
- Existing completed projects that use readiness validation must add the
  Observation Gate, Composition Pass, and reviewer-independence record before
  claiming `ready` again.
- The WCAG delta widens the accessibility gate but does not claim full WCAG
  conformance. Platform guidance and a real assistive-technology pass still
  decide cases the checklist cannot.

## Rejected Alternatives

- **Rewrite the review reference around Impeccable's full pipeline.** The
  engine, CLI, hooks, Live Mode, provider-specific agents, and 48-reference
  surface add a toolchain tax that the quick mode cannot carry.
- **Add a separate composition or accessibility skill.** Both are review
  dimensions of design; a new public skill would split one capability and add
  routing cost.
- **Keep the score first and add observations after.** Scores anchor judgment;
  the failure is exactly the score-first order.
- **Make every quick polish write a full review file.** The cheap mode must stay
  cheap. A five-line card plus rendered evidence is the bounded substitute.
- **Use a single global font-size or touch-target number.** Surface, language,
  role, and platform decide the value; the universal number creates false
  failures and misses CJK.

## Verification

- `composition-reading-order-miss.md` plants equal visual weight and a buried
  primary action with a clean geometry table.
- `reflow-320-miss.md` plants a `320` CSS px overflow that is absent at `390px`
  and `1440px`.
- `state-contrast-gap.md` plants a sticky-footer focus occlusion and an
  under-contrast error message with a clean default state.
- `layout-geometry-toolbar-miss.md` remains the local-inset regression.
- `quick-polish.md` now requires the observation card and reviewer independence.
- The readiness validator rejects `ready` without a passing Observation Gate,
  Composition Pass, and independent reviewer record.

These are deterministic contracts and fixtures. They have not been run in fresh
model sessions, so this decision claims a changed review mechanism, not a
measured reduction in missed UI defects.
