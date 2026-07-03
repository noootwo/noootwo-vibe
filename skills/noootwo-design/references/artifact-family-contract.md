# Artifact Family Contract

Use this note when extending Noootwo Design beyond ordinary UI surfaces into posters, slides, dashboards, or other non-trivial artifact types.

## Why This Exists

Different design tasks can share the same workflow protocol while still needing different artifact expectations.

The stable question is not "what topic is this?" but "what artifact family is this work aiming at?"

This keeps expansion generic:

- no topic-specific prompt patches
- no new mode per artifact
- no confusion between workflow protocol and runtime/export tooling

## Artifact Families

### UI Surface

Use when the target is a product interface, app screen, route, dashboard surface, or responsive web/native UI.

Contract:

- review expects viewport, device, or platform evidence
- layout must hold across responsive or platform states
- export is optional unless the user explicitly needs delivery files

Typical failure modes:

- responsive overflow
- clipped text
- generic component fallback
- platform-inappropriate interaction/detail

### Fixed-Canvas Graphic

Use when the target is a poster, cover, social card, hero visual, campaign static, or other composition-first output with a defined frame.

Contract:

- final dimensions must be explicit
- review expects fixed-canvas evidence, not responsive behavior
- export target must be explicit when the user needs print or delivery-ready output

Typical failure modes:

- weak composition at target aspect ratio
- unreadable type at final size
- missing bleed/trim/safe-area thinking when relevant
- output visually works in preview but not at delivery dimensions

### Slide Deck

Use when the target is a multi-page presentation artifact with narrative sequence, page transitions, and delivery formats such as HTML, PDF, or PPTX.

Contract:

- page sequence and structure matter, not only single-slide quality
- review expects page flow and navigation evidence
- export target must be explicit

Typical failure modes:

- pretty slides with weak narrative progression
- inconsistent master/layout logic
- export target not verified
- navigation or page rhythm breaks

### Live Artifact

Use when the target is a dashboard, decision room, KPI wall, or artifact whose live state, tweakability, or data surface matters.

Contract:

- review expects evidence of live states or state transitions
- artifact must be judged in its active form, not only by static screenshots
- delivery path must record how the live artifact will actually be opened or operated

Typical failure modes:

- static mock instead of usable live surface
- data/state path unclear
- tweak or update loop not reviewable
- strong direction but weak operational artifact

## Shared Requirements Across Families

Every family still inherits the same Noootwo workflow:

- intake
- exploration
- directions
- decision
- design contract
- implementation plan
- artifact
- review
- handoff

Every family still needs:

- explicit artifact family in the brief
- explicit preview surface before ready
- explicit review evidence
- explicit delivery or export target when relevant
- explicit return action when review fails

## Split Guidance

An artifact family can justify a future child skill only when it changes most of:

- artifact grammar
- preview surface
- export path
- review checks
- common failure modes

If it only changes subject matter or visual theme, it should stay inside the shared Noootwo workflow.
