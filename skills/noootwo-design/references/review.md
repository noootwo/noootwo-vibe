# Design Review

Scoring, gates, hard bans, bounded verification, and separated final review.


## Review Rubric

Review is mandatory before delivery. Review as an evaluator, not as the generator defending its own draft.

Prefer lived evidence: prototype, running page, screenshot set, simulator preview, target-stack prototype, or recorded interaction. If no artifact evidence exists, the decision is `needs artifact` unless the user explicitly accepted a handoff-only limitation.

### Scoring

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

### Output

Write `.noootwo/review.md` with artifact evidence, scores, calibration fit, style understanding fit, product comprehension fit, user decision gate, generic/Claude/framework/designer-grade flags, role critique, memorable move, viewport evidence, typography evidence, data evidence when relevant, default-override review, micro-detail pass, readiness gate, decision, return action, and next action.

### Gates To Read When Relevant

- Generic, Claude-like, framework, influence/cosplay, and forced-return checks: [review](review.md)
- Typography checks: [craft](craft.md)
- Responsive checks: [craft](craft.md)
- Dashboard, analytics, ops, finance, admin, or metric-heavy UI: [craft](craft.md)
- Deep or style-sensitive work: [direction](direction.md)

### Readiness Gate

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

### Decisions

- `ready`: direction is strong, style evidence matches the rendered artifact, product comprehension is intact, craft is credible, output avoids generic fallbacks, and evidence is sufficient.
- `refine`: direction is right but execution, hierarchy, proof, or specificity is weak.
- `pivot`: direction is generic, misunderstood, mismatched, derivative, impractical, or structurally wrong.
- `needs artifact`: design may be promising but cannot be judged from current evidence.

Non-ready work needs exactly one primary return action: `return to discovery`, `return to directions`, `return to approved spec`, `return to artifact`, `return to responsive pass`, `return to typography pass`, `return to stack pass`, or `return to handoff`.

If multiple return actions are plausible and the choice changes cost, scope, or visual direction, ask the user before reworking.

### Loop Rules

- Verify in bounded passes, not an open-ended loop: build fully, inspect once with a batched round (desktop and mobile together on web; the shipped device classes on native), fix everything the inspection shows in one batch, then confirm with at most one more round and stop.
- Maximum 2 full review loops before escalating the trade-off to the user.
- Separate "cleaner than before" from "distinctive enough to keep".
- Do not spend polish loops on a direction that needs a structural pivot.
- Do not spend polish loops on an artifact whose style evidence and rendered result do not match.
- If the reviewer cannot name the memorable move, the design cannot be `ready`.

### Reviewer Separation

- Prefer final review from a reviewer that does not inherit the generator's framing, transcript, or optimism. Use a fresh agent when the harness supports one.
- Without a subagent, step fully out of the build context before evaluating, and disclose the substitution in one line at finish.
- The generator never self-certifies `ready`; the reviewer's findings are the only list worked from.
- When the user supplies evidence against a `ready` verdict (their screenshot, a named mismatch), that evidence outranks the capture: reopen the review with a fresh reviewer instead of patching inline and self-certifying.


## Review Gates

Use this when a review needs concrete failure checks. Keep `review.md` for scoring and decision rules.

### Generic And AI-Slop Flags

- `Inter-only` or `system-only` typography without brand reason
- centered template hero with generic supporting cards
- card wall UI with interchangeable radius and shadows
- pure black plus glow plus pills as the main aesthetic move
- gradient-led styling with weak composition underneath
- generic AI landing page, generic SaaS page, or obvious shadcn derivative

### Hard Bans (no brief earns them back)

- eyebrow/kicker label above every heading
- decorative numbered section markers (01 / 02 / 03) when the sequence carries no information
- gradient text; emphasis comes from weight or size
- hard offset shadows (`box-shadow: 4px 4px 0`) outside a genuinely neobrutalist world
- system display face (Impact, Arial Black, platform sans) as the display voice of an own-world page
- emoji or unicode glyphs standing in for an icon system
- cream/beige page background reached for by reflex instead of a deliberate palette
- zero-blur colored halo shadows used as depth

If 2 or more flags are present, the design cannot be `ready`. If 3 or more are present, default to `pivot`.

### Color Calibration Flags

Use [craft](craft.md) before applying these flags. They are not automatic failures; they block `ready` only when they visibly damage hierarchy, brand fit, artifact cohesion, or accessibility.

- `dead neutral stack`: canvas, surface, border, and muted text use generic black/white/gray values without product reason.
- `foreign semantic color`: error, warning, success, selected, or focus colors look imported from another system or fail non-color communication.
- `black-shadow sticker`: shadows read as pasted black overlays instead of depth, boundary, or state.
- `gradient endpoint drift`: one or more gradient stops drift into pure white, dead gray, or an unrelated hue without direction rationale.
- `icon gray drift`: icons or illustration shadows/highlights use a separate gray family instead of inheriting text or surface tokens.

Do not flag deliberate high-contrast, document/editor, data-heavy, native-system, brand-specified, or platform accessibility neutrals as defects without artifact evidence.

### Designer-Grade Failure Flags

- `AI gradient SaaS`
- `styled but crude`
- `unique but impractical`
- `minimal but empty`
- `fashionable but unusable`
- `efficient but generic`
- `premium cosplay`
- `CJK display overweight`
- `mobile app posterization`
- `over-thick card stack`
- `chip/status overload`
- `decorative uppercase English labels`
- `visual metaphor cosplay`
- `designer/artist cosplay`
- `signature-style mimicry`
- `beautiful but unfit for product task`
- `Flutter demo feel`
- `style preserved only at the surface, not in the mechanism`
- `tokens exist but the signature mechanism is gone`
- `component and motion vocabulary drifted away from the source mechanism`

Any `styled but crude`, `unique but impractical`, `fashionable but unusable`, `designer/artist cosplay`, `signature-style mimicry`, or `beautiful but unfit for product task` flag prevents `ready`.
Any `style preserved only at the surface, not in the mechanism`, `tokens exist but the signature mechanism is gone`, or `component and motion vocabulary drifted away from the source mechanism` flag prevents `ready`.

### Claude-Like And Framework Smell

- too many nested rounded containers without structural purpose
- serif headline plus generic sans body plus pills/status dots without product reason
- Claude-ish serif plus mono annotations plus dossier panels plus status dots as a replacement template
- clean panels replacing a real layout idea
- first screen that could describe any AI product after swapping the logo
- Web/React/Vue: unmodified UI-kit components, shadcn-like card walls, Lucide icon grids, generic fade-up motion
- Flutter: default `Scaffold + AppBar + Card + ListView`, Material seed colors without art direction, no sliver or native motion strategy in a high-character app
- SwiftUI/Compose/native: default platform surfaces without token reinterpretation or native transition/state feedback

### Browser Surfaces Check

Theme the browser surfaces models usually skip: text selection, caret, custom scrollbars, focus rings, underline offsets, and tabular numerals in data. Unthemed defaults on a styled page are a strong "assembled, not built" signal and block `ready` when the page claims craft.

### Forced Return Rules

- Missing type contrast, density stance, component vocabulary, motion thesis, or background/detail thesis: return to directions.
- Direction menu without openable case links or source evidence: return to directions.
- Missing artifact strategy, stack translation, or visual proof: return to directions or stack translation.
- Implementation-bound work missing surface inventory or detail translation constraints: return to approved spec.
- Implementation-bound work missing component restyling matrix or default override pass: return to implementation plan.
- Artifact is close but still generic and no micro-detail pass was recorded: return to artifact or enable the detail-translation gate.
- Missing deep source evidence or spike comparison: return to discovery or artifact.
- Missing token mapping in production: return to `.noootwo/design-tokens.md`.
- Missing preservation contract: return to directions or approved spec.
- Failed typography: return to typography pass.
- Failed responsive check: return to responsive pass.
- Generic direction: return to directions, not polish.
