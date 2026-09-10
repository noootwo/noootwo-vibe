# Review Rubric

Review is mandatory before delivery. Review as an evaluator, not as the generator defending its own draft.

Prefer lived evidence: prototype, running page, screenshot set, simulator preview, target-stack prototype, or recorded interaction. If no artifact evidence exists, the decision is `needs artifact` unless the user explicitly accepted a handoff-only limitation.

## Scoring

Score on 100 points:

- `design_quality`: 35
- `originality`: 30
- `craft`: 15
- `functionality`: 10
- `artifact_evidence`: 5
- `stack_native_craft`: 5

Thresholds:

- `85-100`: ready only if artifact evidence exists and generic-risk flags are 0-1
- `70-84`: refine
- `<70`: pivot unless the user explicitly preserves the direction

## Output

Write `.noootwo/review.md` with artifact evidence, scores, calibration fit, style understanding fit, product comprehension fit, user decision gate, generic/Claude/framework/designer-grade flags, role critique, memorable move, viewport evidence, typography evidence, data evidence when relevant, default-override review, micro-detail pass, readiness gate, decision, return action, and next action.

## Gates To Read When Relevant

- Generic, Claude-like, framework, influence/cosplay, and forced-return checks: [review-gates.md](review-gates.md)
- Typography checks: [typography-craft-rubric.md](typography-craft-rubric.md)
- Responsive checks: [responsive-visual-gates.md](responsive-visual-gates.md)
- Dashboard, analytics, ops, finance, admin, or metric-heavy UI: [data-ui-rubric.md](data-ui-rubric.md)
- Deep or style-sensitive work: [taste-fit-matrix.md](taste-fit-matrix.md)

## Readiness Gate

Before `ready`, confirm:

- `.noootwo/directions.md`, `.noootwo/review.md`, and `.noootwo/design-tokens.md` are not pending
- required files do not contain unresolved `TBD`
- review records artifact evidence and a decision
- high-character work records style understanding fit against visual evidence
- product UI work records product comprehension fit against the Product-to-Design Handoff or known main path
- review records typography evidence
- review records responsive or platform evidence
- implementation-bound work records default-override review and micro-detail review when generic drift was a risk
- full redesign has recorded user-selected direction
- required user decision gates are resolved or delegated

If this fails, use `needs artifact` or `refine`, not `ready`.

## Decisions

- `ready`: direction is strong, style evidence matches the rendered artifact, product comprehension is intact, craft is credible, output avoids generic fallbacks, and evidence is sufficient.
- `refine`: direction is right but execution, hierarchy, proof, or specificity is weak.
- `pivot`: direction is generic, misunderstood, mismatched, derivative, impractical, or structurally wrong.
- `needs artifact`: design may be promising but cannot be judged from current evidence.

Non-ready work needs exactly one primary return action: `return to discovery`, `return to directions`, `return to approved spec`, `return to artifact`, `return to responsive pass`, `return to typography pass`, `return to stack pass`, or `return to handoff`.

If multiple return actions are plausible and the choice changes cost, scope, or visual direction, ask the user before reworking.

## Loop Rules

- Verify in bounded passes, not an open-ended loop: build fully, inspect once with a batched round (desktop and mobile together on web; the shipped device classes on native), fix everything the inspection shows in one batch, then confirm with at most one more round and stop.
- Maximum 2 full review loops before escalating the trade-off to the user.
- Separate "cleaner than before" from "distinctive enough to keep".
- Do not spend polish loops on a direction that needs a structural pivot.
- Do not spend polish loops on an artifact whose style evidence and rendered result do not match.
- If the reviewer cannot name the memorable move, the design cannot be `ready`.

## Reviewer Separation

- Prefer final review from a reviewer that does not inherit the generator's framing, transcript, or optimism. Use a fresh agent when the harness supports one.
- Without a subagent, step fully out of the build context before evaluating, and disclose the substitution in one line at finish.
- The generator never self-certifies `ready`; the reviewer's findings are the only list worked from.
- When the user supplies evidence against a `ready` verdict (their screenshot, a named mismatch), that evidence outranks the capture: reopen the review with a fresh reviewer instead of patching inline and self-certifying.
