# Design Review

Scoring, safety gates, evidence-backed aesthetic flags, bounded verification, and separated final review.


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

- `85-100`: ready only if artifact evidence exists and no confirmed generic-risk or aesthetic-harm finding remains
- `70-84`: refine
- `<70`: pivot unless the user explicitly preserves the direction

### Output

Write `.noootwo/review.md` with artifact evidence, intervention decision and fit, scores, calibration fit, style understanding fit, product comprehension fit, user decision gate, safety hard-gate result, aesthetic flags with evidence of harm or intentional use, generic/Claude/framework/designer-grade flags, role critique, authored move or deliberate absence, viewport evidence, typography evidence, data evidence when relevant, default-override review, micro-detail pass, readiness gate, decision, return action, and next action.

### Intervention Review

Review the decision before reviewing the decoration:

- `leave simple`: the product function, frequency, risk, and artifact evidence must justify the absence of an authored moment. Confirm hierarchy, state feedback, and craft are strong; an empty or underdesigned result still fails.
- `craft only`: the artifact must show the specific structural, typographic, state, or detail problems that were improved. Aesthetic adjectives without artifact evidence do not pass.
- `add moment`: the authored move must be visible, tied to a named purpose, supported by a source or platform rule, and safe under fallback, performance, and accessibility checks.

A governed absence of an authored move is a valid `ready` result when the decision and craft evidence support it. A missing authored moment on an `add moment` contract is not.

If the user explicitly requested motion, animation, liveliness, fancy, a named library, or shader/material rendering, zero motion is not ready unless the user accepted that outcome. Review the implementation tool too: an installed runtime or user-named library must be selected, replaced with a recorded equivalent, or rejected with a concrete reason.

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
- direction-sensitive work records either viewed low-cost samples or the reason samples were not applicable
- full redesign has recorded user-selected direction
- required user decision gates are resolved or delegated
- the intervention decision is recorded in the design tokens and review, and both records agree
- an explicit motion or material request records whether the user accepted no authored motion
- `leave simple` or `craft only` records craft-sufficiency evidence and rejected opportunities
- `add moment` records one primary authored move, its trigger, implementation tool, evidence or platform rule, and fallback
- any installed or user-named library or shader is selected, replaced by a recorded equivalent, or rejected with a concrete reason
- an authored move is not required merely because the artifact is new or visually quiet
- the safety hard-gate result is pass, and every aesthetic flag records whether it caused demonstrated harm or was intentional

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
- If the contract selects an authored move, the reviewer must name it and its proof; otherwise the reviewer names the craft mechanism that carries the design.

### Reviewer Separation

- Prefer final review from a reviewer that does not inherit the generator's framing, transcript, or optimism. Use a fresh agent when the harness supports one.
- Without a subagent, step fully out of the build context before evaluating, and disclose the substitution in one line at finish.
- The generator never self-certifies `ready`; the reviewer's findings are the only list worked from.
- When the user supplies evidence against a `ready` verdict (their screenshot, a named mismatch), that evidence outranks the capture: reopen the review with a fresh reviewer instead of patching inline and self-certifying.


## Review Gates

Use this when a review needs concrete failure checks. Keep `review.md` for scoring and decision rules.

### Source Fidelity QA

Run this only when the direction records `Reference intent: replicate` or the user explicitly asks to match a visual source. It does not apply to `borrow-mechanism` or ordinary redesign work.

Put the reference and the implementation side by side in the same viewport and state, then check:

- fonts: family, fallback, weight, size, line height, letter spacing, optical weight, wrapping, truncation
- layout: grid tracks, margins, padding, section gaps, component spacing, radii, shadows or elevation
- colour: sampled or inferred palette, gradients, opacity, semantic states, contrast
- assets: image subject, crop, scale, sharpness, masks, logos, icons; no div art, emoji, text glyphs, or code-native stand-ins for visible source assets
- copy and content: app-specific text, empty, loading, error, permission, and success states

Distinguish fidelity defects from intentional mechanism translation. A deliberate `borrow-mechanism` adaptation is not a fidelity defect; a faithful `replicate` that silently changes the source is.

### Generic And AI-Slop Flags

- centered template hero with generic supporting cards
- card wall UI with interchangeable radius and shadows
- pure black plus glow plus pills as the main aesthetic move
- gradient-led styling with weak composition underneath
- generic AI landing page, generic SaaS page, or obvious shadcn derivative

These are review signals, not automatic failure counts. Confirm the actual hierarchy, readability, brand fit, and cohesion defect in the artifact.

### Safety Hard Gates (never waived)

- readable foreground/background contrast and type
- keyboard, focus, touch, and control reachability
- real content, imagery, and state integrity rather than broken placeholders
- recovery from empty, loading, error, permission, and success states
- no broken assets or unusable interaction paths
- source fidelity when `Reference intent` is `replicate`

### Aesthetic Evidence Flags

- eyebrow/kicker label above every heading
- decorative numbered section markers (01 / 02 / 03) when the sequence carries no information
- gradient text where legibility or hierarchy is weaker than a direct type treatment
- hard offset shadows (`box-shadow: 4px 4px 0`) outside a genuinely neobrutalist world
- system display face (Impact, Arial Black, platform sans) as the display voice of an own-world page
- emoji or unicode glyphs standing in for an icon system
- cream/beige page background reached for by reflex instead of a deliberate palette
- zero-blur colored halo shadows used as depth
- `Inter-only` or another inherited safe grotesk chosen without brand reason

Each flag requires `Evidence of harm or intentional use`. It blocks `ready` only when the rendered artifact shows damaged hierarchy, readability, brand fit, or system cohesion. A flag with a clear product or brand rationale and no demonstrated harm may pass. A safety hard-gate failure cannot be justified by intent or a brief.

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
- Direction menu without viewed low-cost samples, or with a broken/black capture standing in for evidence: return to directions.
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
