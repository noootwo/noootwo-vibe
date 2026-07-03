# Stage Roles

Use these roles to keep design work from collapsing into one model inventing, implementing, and defending the same idea.

## Role Sequence

- `Context Auditor`: reads code, screenshots, tokens, `AGENTS.md`, and `.noootwo/`; records facts and gaps; does not invent style.
- `Accessibility Scout`: checks whether preferred foreign sources are reachable, selects domestic fallback sources when needed, and records access limits.
- `Source Scout`: searches active design and developer sources for relevant product, platform, and visual signals.
- `Signal Curator`: weights sources, removes low-evidence shots, and flags trend skins that do not fit the task.
- `Mechanism Extractor`: converts sources into reusable mechanisms: grid, rail, surface, type scale, state model, motion primitive, data grammar.
- `Taste Strategist`: clusters mechanisms into 2-3 visual territories with fit scores.
- `Art Director`: chooses typography, proportion, color restraint, component language, material, and motion thesis.
- `Typography & Composition Editor`: checks type scale, weight roles, line-height, letter-spacing, mobile wrapping, spacing rhythm, and composition before polish.
- `Product Designer`: verifies task path, information architecture, states, efficiency, and usability.
- `Stack Craftsperson`: turns the direction into a React, Vue, Flutter, SwiftUI, Compose, native, or web artifact using stack-native primitives.
- `Design Director / Evaluator`: reviews the artifact only; decides `ready`, `refine`, `pivot`, or `needs artifact`.
- `Design System Steward`: promotes only reviewed decisions into tokens, components, and handoff.

## Rules

- Do not skip from user adjectives to UI generation in deep mode.
- Do not let the generator perform the final evaluation of its own artifact.
- Do not let a visual trend override product task clarity, platform craft, or accessibility.
- If a role lacks evidence, record the gap instead of pretending confidence.
- If foreign sources are blocked, use the domestic fallback path instead of skipping research.
- If typography or responsive behavior fails, return to the relevant pass instead of polishing around the defect.

## Output Mapping

- Context Auditor writes `.noootwo/adoption.md`, `.noootwo/system.md`, or `.noootwo/brief.md`.
- Accessibility Scout, Source Scout, Signal Curator, Mechanism Extractor, and Taste Strategist write `.noootwo/style-discovery.md` and `.noootwo/reference-board.md`.
- Art Director writes `.noootwo/directions.md`.
- Typography & Composition Editor contributes typography and layout evidence to `.noootwo/review.md`.
- Evaluator writes `.noootwo/review.md`, including the return action for any `refine` decision.
- Design System Steward writes `.noootwo/design-tokens.md` and `.noootwo/handoff/`.
