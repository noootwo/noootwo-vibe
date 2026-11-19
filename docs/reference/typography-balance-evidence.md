# Typography Balance Evidence

Use this when changing typography guidance, review gates, or a product surface
that oscillates between unreadably small copy and oversized display text. It is
a research record and an implementation brief, not a universal type scale.

## Decision

How should a dense product interface separate expressive display type from
operational text while keeping labels, body copy, controls, and comments
readable across viewports and text resizing?

**Would flip:** credible platform guidance showing that one fluid display scale
should govern both marketing headers and dense workspace chrome, or that text
below 11 CSS px remains readable in routine desktop software.

**Not enough:** one competitor screenshot, a trend post, or "make everything
larger" without role measurements and rendered evidence.

Size: `deep`. A rejected visual direction and a published skill rule depend on
the answer, so the brief is persisted through `noootwo-state`.

## Case Failure

The supplied case (`modocc`) accumulated three separate type systems:

1. Hardcoded `6-10px` microcopy across the Agent review card, Inspector, image
   captions, and toolbar.
2. A later "readability" pass that selected hundreds of unrelated elements and
   assigned one shared size, collapsing title, body, metadata, and control
   hierarchy into the same role.
3. Page-level typography tokens defined only inside `.workspace-shell`; Settings
   and other application pages fell back to the root `15px` value and browser
   defaults of `16px`.

The rendered result was not "everything is 2px too small". It was a broken role
model: a 112px landing headline, a 62px settings heading, 8px action buttons,
and 16px settings body text could all coexist in one product.

The case is evidence only, not the delivery target. Its source, tests,
screenshots, assets, and deployment are read-only for this skill change; the
lesson must transfer through the skill, not through unreviewed edits to the
example.

## Evidence

### Platform scales separate display from product text

Apple's Human Interface Guidelines describe macOS body text around 13pt, with
smaller caption and footnote roles and a practical floor near 10pt. The guidance
also asks for hierarchy through size, weight, and colour, not through making one
role carry every emphasis.

Source: [Apple HIG — Typography](https://developer.apple.com/design/human-interface-guidelines/typography),
accessed 2026-11-19. Evidence level: official platform guidance.

Material 3 publishes distinct role families: display `57/45/36`, headline
`32/28/24`, title `22/16/14`, body `16/14/12`, and label `14/12/11` in its
default scale. The important mechanism is the role split, not copying Google's
pixel values into a dense editor.

Source: [Material 3 — Type scale tokens](https://m3.material.io/styles/typography/type-scale-tokens),
accessed 2026-11-19. Evidence level: official design-system guidance.

Fluent 2 uses caption `10/12`, body `14`, subtitle `16/20`, title `24/28/32`,
and a much larger display register. It independently separates product copy
from display type and supplies several dense control roles.

Source: [Fluent 2 — Typography](https://fluent2.microsoft.design/typography),
accessed 2026-11-19. Evidence level: official design-system guidance.

### Product screens use stable type; expressive screens may use fluid type

IBM Carbon recommends fixed headings for product pages and reserves fluid
headings for expressive or editorial pages. Its type sets keep body copy at
`14-16px` and labels at `12-14px`, with size differences carrying known roles.

Source: [Carbon — Type sets](https://carbondesignsystem.com/elements/typography/type-sets/),
accessed 2026-11-19. Evidence level: official design-system guidance.

This is the direct counterexample to applying a landing-page `clamp()` headline
inside a settings page, an inspector, or a side panel.

### Text resizing is a hard accessibility requirement

WCAG 2.2 Success Criterion 1.4.4 requires text to resize up to 200 percent
without loss of content or functionality. Typography review therefore needs a
resized or narrow-layout pass, not only 1440px screenshots.

Source: [W3C — Understanding SC 1.4.4: Resize Text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html),
accessed 2026-11-19. Evidence level: normative accessibility guidance.

### `clamp()` is a bound, not a hierarchy

CSS `clamp(min, preferred, max)` guarantees only a lower and upper value. It
does not decide which text is display, title, body, label, or annotation. A
fluid value becomes a defect when it is applied by element shape rather than by
semantic role.

Source: [MDN — `clamp()`](https://developer.mozilla.org/en-US/docs/Web/CSS/clamp),
accessed 2026-11-19. Evidence level: implementation reference.

### CJK needs its own boundary

W3C requirements for Chinese text layout call out line height, punctuation,
line-breaking, and spacing behaviour that Latin-only display scales often
ignore. Large CJK display type also occupies a more uniform width per character,
so Western display ratios do not transfer one-for-one.

Source: [W3C — Requirements for Chinese Text Layout](https://www.w3.org/TR/clreq/),
accessed 2026-11-19. Evidence level: internationalization guidance.

## Adopted Mechanism

1. **Two registers.** Expressive surfaces may use a bounded display scale.
   Operational surfaces use fixed semantic roles. A display size never becomes
   a workspace title by convenience.
2. **One global token source.** Type tokens live at the application root so every
   route, panel, and overlay resolves the same role names.
3. **Role minima.** In this dense desktop product, `10px` is reserved for
   decorative keycaps and numeric badges; readable metadata is `11px`, controls
   and body copy are `12px`, emphasis copy is `13px`, panel titles are `14px`,
   and page titles are `28-34px`. Settings inputs are not stretched to the login
   input size.
4. **Hierarchy by relationship.** A local title is normally `1.15-1.5x` its body
   copy. A page title may be `2-3x` body copy. A marketing or login headline may
   be `3-4x`, but its rendered height must stay below roughly one fifth of the
   viewport. Decorative lettering sits outside the reading hierarchy.
5. **Full-surface measurement.** Review measures rendered font size, line
   height, heading height share, and overflow across the actual populated
   states. A source search for bad values is supporting evidence, not the
   review.
6. **One correction pass.** Fix the role model and every surface it affects in
   one batch, then confirm once. Repeated per-component size nudges are a
   symptom that the role model is still unsettled.
7. **One write target.** A case or comparison project stays read-only. The
   deliverable is the current repository, design system, document, or product
   the user explicitly named.

## Boundaries And Counterexamples

- Platform point sizes are not CSS pixels. Apple's 13pt guideline is direction,
  not a direct `13px` web token.
- Dense operational tools can validly use `11-12px` metadata where a consumer
  reading surface would use `14-16px`. The user, task, and viewing distance
  decide density; arbitrary shrinkage does not.
- Marketing, onboarding, and login screens can carry a large display statement.
  Their large type is not evidence that settings and tool panels need the same
  scale.
- Lovart is a useful product reference for restrained hierarchy, a clear canvas
  focus, and compact control chrome. Its private assets, exact styling, layouts,
  prompts, and component tree are not copied. Only the mechanism of separating
  display, product copy, and controls transfers.
- A bigger base font cannot repair missing hierarchy. When every role receives
  the same size, the interface gets louder without becoming clearer.
- `rem` conversion alone is not the goal. The check is whether every readable
  role survives browser zoom and a narrow viewport without clipping.
- A reference product's size values are evidence about role relationships, not
  a mandate to patch that product or copy its exact pixel scale.

## Observed Case Contract (`modocc`, Read-Only)

- Root tokens: micro/caption `11`, control/body/input `12`, body-large `13`,
  title `14`, keycap `10`.
- Login: label `13`, input `16`, heading at most `48`; decorative type capped at
  `168`.
- Home: hero at most `72`, section headings at most `30`.
- Application pages: heading at most `34`, card title `16`, body `12`, control
  `12`, input `12`.
- Workspace: panel title `14`, empty-state title at most `24`, chat body `13`,
  review body `12`, comments/captions `11`, keycaps `10`.
- Required evidence: desktop, tablet, phone, populated Agent review state, and a
  `720x450` narrow viewport as a 200-percent zoom equivalent.

## Verification

- The observed rendered states were used to derive the role relationships and
  failure flags; they are not modified deliverables.
- `skills/noootwo-design/evals/prompts/typography-balance-rework.md` turns the
  failure into a behavioral contract without editing the case project.
- No case-specific source, test, screenshot, asset, or deployment is included in
  this release.

## Confidence

- **High:** display and product text need different scales; one blanket size
  cannot preserve hierarchy; 200-percent resizing and narrow viewports are
  mandatory review states.
- **High:** hardcoded `6-9px` operational copy is below a defensible readable
  floor for this desktop product.
- **Medium:** the exact `12px` body floor for every dense web product. Density,
  language, viewing distance, and input device can move it by one step.
- **Low:** any claim that the rule alone prevents future rework. The eval is not
  a fresh-session behavior measurement.
