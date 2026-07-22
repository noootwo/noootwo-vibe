# Direction Exploration

Direction work explores materially different art directions before drafting. Use [structured-design-spec.md](structured-design-spec.md) so every direction can become a concrete design language, not a vibe. Use [style-evidence-check.md](style-evidence-check.md) for high-character, niche, premium, user-selected, or previously rejected directions.

## When

Produce 3 directions only when the choice would materially change implementation:

- the user asks to explore, choose, theme, style, or make the UI more distinctive
- the work is a full redesign, fresh visual language, or "start over" request
- multiple plausible structures, densities, moods, or component languages fit the product
- high-character, premium, niche, unusual, selected, or previously rejected style needs evidence before implementation
- the user strongly rejects the current style as generic, not advanced, not unique, or not matching the chosen direction

Skip directions for `quick`, `review`, `extract-system`, handoff-only, explicit stay-close polish, and standard work where product path plus visual posture already make one implementation path clear.

Directions are a user-facing decision menu, not internal notes. Present the menu, recommend one direction, and wait for user selection before implementation unless the user explicitly delegates the choice.

For full redesign requests such as "redo all UI", "start over", "all design from scratch", or "do not use the current visual language", the direction menu is a hard blocking checkpoint.

## User-Facing Direction Shape

Write `.noootwo/directions.md` with:

- recommended direction and why
- full redesign trigger when relevant
- Style Evidence Check for high-character directions: style claim, visual evidence, anti-example, borrowed mechanism, implementation translation, confidence, and artifact/spike required
- user selected direction, or `not selected yet`
- user decision gate: whether a choice is required, the exact question, options, recommendation, user selection, and whether the user delegated the choice
- 3 named directions
- surface type and why the chosen source pool fits
- for each direction: source evidence, borrowed mechanism, anti-example, design-spec delta, type/color/density, component/shape language, motion thesis, artifact strategy, and mimicry risk to reject
- for each direction: must-preserve, allowed-variation, forbidden-substitution, token target, component target, and motion target

## Internal Preflight

Before drafting, confirm:

- the 3 directions differ in type, structure, density, mood, component language, and motion
- each direction has a design-spec delta: color roles, type roles, layout model, component vocabulary, motion thesis, and forbidden moves
- each direction states what must survive translation into tokens and implementation, what may vary, and what must never be substituted
- product UI directions use product/design-system evidence, while campaign UI directions may use more experimental art-direction evidence
- each direction names how it becomes reviewable
- each direction includes at least one openable case link the user can inspect
- high-character directions have visual evidence or are explicitly marked low confidence with a spike requirement
- each direction has stack translation
- each direction defines font logic, scale, weight roles, line-height, letter-spacing, and mobile display cap
- no direction is only a palette swap
- no direction defaults to generic SaaS, shadcn-card-wall, or Flutter/native defaults without product reason
- no influence-led direction imitates a designer/artist signature style instead of translating mechanisms
- if options are materially different, `User selected option` or `User delegated choice to agent` is recorded before drafting

If 3 directions share the same opening structure or component skeleton, redo exploration.

If a direction cannot be summarized as implementation rules another agent could follow, return to directions before drafting.

If a direction's evidence and claimed style point to different mechanisms, return to style discovery before writing the spec.

If a required decision is unresolved, do not create artifacts, edit Flutter routes, write handoff, or enter production.
