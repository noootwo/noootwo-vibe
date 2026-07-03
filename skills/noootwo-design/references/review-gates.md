# Review Gates

Use this when a review needs concrete failure checks. Keep `review-rubric.md` for scoring and decision rules.

## Generic And AI-Slop Flags

- `Inter-only` or `system-only` typography without brand reason
- centered template hero with generic supporting cards
- card wall UI with interchangeable radius and shadows
- pure black plus glow plus pills as the main aesthetic move
- gradient-led styling with weak composition underneath
- generic AI landing page, generic SaaS page, or obvious shadcn derivative

If 2 or more flags are present, the design cannot be `ready`. If 3 or more are present, default to `pivot`.

## Designer-Grade Failure Flags

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

## Claude-Like And Framework Smell

- too many nested rounded containers without structural purpose
- serif headline plus generic sans body plus pills/status dots without product reason
- Claude-ish serif plus mono annotations plus dossier panels plus status dots as a replacement template
- clean panels replacing a real layout idea
- first screen that could describe any AI product after swapping the logo
- Web/React/Vue: unmodified UI-kit components, shadcn-like card walls, Lucide icon grids, generic fade-up motion
- Flutter: default `Scaffold + AppBar + Card + ListView`, Material seed colors without art direction, no sliver or native motion strategy in a high-character app
- SwiftUI/Compose/native: default platform surfaces without token reinterpretation or native transition/state feedback

## Forced Return Rules

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
