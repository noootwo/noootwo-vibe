---
name: noootwo-detail-translation
description: Use when an approved Noootwo direction is implementation-bound and the result is at risk of drifting back to framework defaults. Handles surface inventory, component restyling, default override review, and micro-detail preservation.
---

# Noootwo Detail Translation

Use this skill when the direction is already correct, but the implementation is losing authored detail.

## When To Use

- the artifact is directionally right but still feels generic
- implementation is reusing primitives correctly but not re-authoring enough detail
- the issue is default-component smell, spacing rhythm loss, weak micro-detail, or mechanism drift

Do not use this as a replacement for exploration or review. It is a late-stage preservation pass.

## Required References

- `references/detail-translation-pass.md`
- `references/structured-design-spec.md`
- `references/review-gates.md`
- `references/anti-slop.md`

## Required Outputs

Update:

- `.noootwo/specs/active-design.md`
- `.noootwo/plans/active-implementation.md`
- `.noootwo/review.md` when review evidence exists

The pass should explicitly cover:

- surface inventory
- component/system mapping
- default override risk
- known drift risks
- micro-detail areas that carry the direction

## Blocking Rules

- Do not restart exploration if the real issue is implementation drift.
- Do not call the artifact ready until the preserved mechanism is visible in the rendered output.
- Tie every detail-preservation claim to artifact evidence when possible.
