---
name: noootwo-design-review
description: Use when reviewing screenshots, running artifacts, previews, HTML prototypes, or completed Noootwo deliverables. Diagnoses layout defects, typography issues, generic drift, mechanism loss, and chooses a concrete return action such as refine, pivot, or return to an earlier stage.
---

# Noootwo Design Review

Use this skill when the main job is critique rather than generation.

## When To Use

- reviewing screenshots or live previews
- judging whether a result is ready, refine, pivot, or needs artifact
- diagnosing layout defects, readability defects, or responsive issues
- identifying generic drift or mechanism loss after implementation

## Review Contract

Judge the artifact, not the prose.

Prefer:

- screenshot sets
- running pages
- simulator previews
- target-stack prototypes
- recorded interactions

If there is no artifact evidence, default to `needs artifact` unless the user explicitly accepts the limitation.

## Required References

- `references/review-rubric.md`
- `references/review-gates.md`
- `references/responsive-visual-gates.md`
- `references/typography-craft-rubric.md`
- `references/data-ui-rubric.md` when relevant
- `references/detail-translation-pass.md` when the artifact is close but generic

## Required Output

Update `.noootwo/review.md` with:

- artifact evidence
- strongest and weakest authored move
- generic drift checks
- layout/readability/responsive findings
- a decision
- exactly one primary return action

## Return Action Rules

Return to the earliest stage that can actually fix the problem:

- exploration
- directions
- approved spec
- implementation plan
- artifact
- responsive pass
- typography pass
- stack pass

Do not hide structural defects under vague “polish more” language.
