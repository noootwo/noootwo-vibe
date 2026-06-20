## UI/Design Workflow

Use `$noootwo-design` to lead all UI-related work in this project, including UI/UX design, frontend visual changes, app screens, redesigns, design reviews, and design-to-implementation handoff.

Read Noootwo's project design context from `.noootwo/` before making UI decisions:

- `.noootwo/system.md`
- `.noootwo/design-tokens.md`
- `.noootwo/adoption.md`
- `.noootwo/brief.md`
- `.noootwo/style-calibration.md`
- `.noootwo/style-discovery.md`
- `.noootwo/reference-board.md`
- `.noootwo/directions.md`
- `.noootwo/review.md`
- `.noootwo/handoff/`

Before non-trivial UI implementation, run or inspect:

- `python scripts/noootwo_status.py .`
- `.noootwo/specs/active-design.md`
- `.noootwo/plans/active-implementation.md`

For non-trivial design work, route by task structure first:

- if the task keeps the existing system and scope is small, `quick` may be enough
- if the task introduces a new structure, new hierarchy, or multiple viable directions, do not implement before exploration and a direction decision
- if the task is implementation-bound, do not edit UI files before the approved design spec and implementation plan exist

If multiple reasonable directions exist, present options and stop until the user chooses or explicitly delegates the choice.

Do not claim `ready` without `.noootwo/review.md` and artifact/screenshot/preview evidence. If the artifact has layout, responsive, typography, or generic-drift defects, return to the earlier fixing stage instead of calling it polished.

Keep detailed Noootwo Design workflow rules inside the `$noootwo-design` skill; do not duplicate them here.
