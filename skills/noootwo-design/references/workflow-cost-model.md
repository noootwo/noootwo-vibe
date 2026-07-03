# Workflow Cost Model

Use this to prevent Noootwo Design from becoming too expensive for ordinary UI work.

## Modes

- `quick`: local polish. No source mining, no 3 directions, no spike comparison. Use current system and one artifact or screenshot when available.
- `standard`: normal UI design. Light calibration, 3 directions, 1 artifact, typography and responsive review before ready.
- `deep`: high-end, niche, brand-heavy, Claude Design-like, or major redesign work. Source accessibility, evidence-backed discovery, 2-3 artifact spikes, screenshot comparison, typography and responsive gates.
- `production`: approved design implementation. Token mapping, stack playbook, screenshot or preview acceptance.
- `detail-translation`: not a standalone mode. It is an implementation-stage reinforcement layer for surfaces that otherwise drift back to defaults.
- `adopt-project`: first use in an existing project. Capture baseline and constraints before redesigning.

## Cost Controls

- Do not run deep mode just because a task is visual.
- Do not add a new mode for full redesign. Use the full redesign checkpoint inside `deep` or `adopt-project -> deep`.
- If the user asks for minor polish or to preserve the current system, use `quick`.
- If the user asks to redo all UI or abandon the current visual language, the cost of discovery and user direction selection is intentional. Stop at the direction menu before implementation.
- For non-quick UI implementation, the approved design spec and implementation plan are intentional cost controls. They are cheaper than reworking a bad UI after code is written.
- Use the detail-translation layer only for implementation-bound work, production review, or post-review drift. Do not make it the default cost of quick polish or early direction exploration.
- Skip the spec/plan gate only for quick polish, explicit handoff-only work, or explicit user approval to proceed without the gate.
- If time or environment blocks source mining, screenshots, or target-stack previews, record the limitation and reduce readiness confidence.
- If only 1 deep spike is possible, mark the exploration as low-confidence and do not claim full territory comparison.
- Prefer existing project preview tools before adding new dependencies.

## Escalation

Escalate from standard to deep only when the user asks for strong taste, niche/high-end direction, brand shift, or a previous standard result was too generic.

De-escalate from deep when the user prioritizes speed, implementation certainty, or staying close to an existing shipped interface.
