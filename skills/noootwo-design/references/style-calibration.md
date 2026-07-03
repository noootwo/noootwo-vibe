# Style Calibration

Use this before direction exploration for standard or deep UI work. Keep it short.

## Purpose

Style calibration turns vague taste requests into a compact taste contract. It should help the user choose a direction, not become a long questionnaire.

## When To Run

Run for:

- new UI, major redesign, brand-heavy work, high-end or niche UI
- Claude Design-like requests
- Flutter/native/app work where stack-native craft matters
- tasks with taste adjectives but no visual references

Skip for `quick`, `review`, `extract-system`, `handoff-only`, or explicit "stay close" work.

## Output

Write `.noootwo/style-calibration.md` with:

- one style thesis
- 5-7 dials: novelty, brand safety, density, typography contrast, motion presence, surface/material character, composition risk
- 1-2 reference mechanisms from [verified-ui-casebook.md](verified-ui-casebook.md) when useful, with case links the user can open
- one recommended calibration
- what this rules out

## Defaults

- Novelty: 4/5 for deep, 3/5 for standard
- Brand safety: 3/5 unless the user asks for conservative work
- Typography contrast: deliberate; avoid inherited system stacks unless confirmed
- Motion: purposeful; never garnish
- Composition: avoid default centered hero plus card grid

## Direction Link

Each direction must state:

- how it follows the calibration
- which dial it pushes hardest
- which generic pattern the calibration rules out

If all 3 directions could use the same generic SaaS layout, redo calibration.
