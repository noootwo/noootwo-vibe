# 0034 — Typography role balance and rendered-evidence review

## Status

Accepted on 2026-11-19.

## Context

Two opposite failures recurred in the same product:

- Operational copy had accumulated at `6-10px`, including review text, image
  captions, optimistic actions, and Inspector help.
- A later readability correction assigned one blanket size to hundreds of
  unrelated selectors. Titles, body copy, metadata, controls, and comments lost
  their roles.
- A second scoping error left the semantic tokens inside the workspace shell, so
  Settings and other application pages fell back to `15-16px` browser defaults.
- Expressive `clamp()` headings remained on product pages, producing a `112px`
  landing title and a `62px` Settings title in the same application.

The existing design review could see a screenshot and still miss this because it
did not require a rendered role table, a display/share bound, or a resized
narrow-layout check. The correction loop then changed individual font sizes,
which made the hierarchy worse each round.

The product was supplied as a case, not as a delivery target. It stays read-only
evidence; this decision changes the design skill, not that project.

The decisive evidence is in
[typography-balance-evidence.md](../reference/typography-balance-evidence.md):
Apple, Material, Fluent, Carbon, WCAG 2.2, CSS `clamp()`, and W3C CJK guidance.
Carbon's fixed product versus fluid expressive split and WCAG's 200-percent
resize requirement are the two strongest constraints.

The 2026-11-19 prior-art pass also reviewed Huashu Design `v3.3.0`, Impeccable
`skill-v4.10.0`, Anthropic `frontend-design`, Antfu Design `2026.06.22`, and
Superpowers `v7.0.2` at source. Huashu and Antfu independently support compact
dense roles and hierarchy limits; Impeccable and Anthropic support bounded
expressive type and rendered review; Superpowers supplies no typography method.
None supplies a universal body floor. Huashu's critique/fallback `2.5x` ratio
conflicts with its own `1.2` dashboard rule when universalized; its web/deck
minima, Impeccable's reading-size guidance, and Anthropic's line-length rule
stay scoped to their surfaces.

## Decision

1. `noootwo-design` treats display type and product type as two registers.
   Expressive display may use fluid `clamp()` values with a cap; operational
   surfaces use fixed semantic roles.
2. A typography contract names display, page title, local title, body, control,
   label, annotation, keycap, and numeric roles. It also names each role's line
   height, minimum, maximum, and which surface may use it.
3. Type tokens have one application-wide source. Route-scoped token blocks only
   override with a documented product exception; they never become the only
   place a role exists.
4. Readable operational text has a product-specific floor. `10px` is reserved
   for non-reading keycaps or badges; metadata starts at `11px` in a dense
   desktop tool, and body/control roles start at `12px` unless the product
   records a different density contract. Numeric floors and title ratios from a
   reading, marketing, expressive, or mobile-reading surface do not override
   that contract.
5. Hierarchy is checked as a relationship: local title to body, page title to
   body, and heading rendered height as a share of the viewport. A display
   heading below roughly one fifth of the viewport is the target; an operational
   page heading is much smaller.
6. Typography review uses rendered computed values from the actual populated
   state, not a source search alone. Evidence covers desktop, tablet, phone, and
   a narrow viewport equivalent to 200-percent page zoom.
7. A blanket selector that assigns one font size across unrelated roles is not a
   type scale. The correction is a role rebuild and one consolidated pass, not
   repeated component-by-component nudges.
8. The design target is named before reading or editing. A project supplied as a
   case, reference, or comparison is read-only evidence and is never patched to
   demonstrate a skill change.
9. Durable typography choices and repeated user corrections are persisted
   through `noootwo-state`; the shortest always-on rule goes in the nearest
   `AGENTS.md`. No new docs, memory, typography, or project-status skill is
   introduced.

## Consequences

- Design review can block `ready` on a measured role collision, unreadable copy,
  an unbounded display title, or a resize failure.
- Dense tools may use compact `11-12px` metadata and body copy while consumer
  surfaces use larger values; the rule is role and density, not a universal
  pixel floor.
- Existing screenshots remain useful, but a screenshot without computed roles
  and resize evidence cannot prove typography readiness.
- A case product's source, tests, screenshots, and deployment remain untouched;
  the skill repository is the deliverable when the user asks to improve the
  skill.
- The skill adds one eval and one reference gate, not a new design system or
  dependency.

## Rejected Alternatives

- **Raise every font.** It flattens hierarchy and makes dense surfaces louder.
- **Shrink every font.** It restores the original unreadable `6-10px` failure.
- **Apply one `clamp()` across the app.** Product pages need fixed roles; fluid
  text belongs to expressive surfaces.
- **Use the login scale for Settings.** Authentication has a different input
  and focus contract from daily configuration work.
- **Treat a reading-page `14-16px` body floor or an expressive `2.5x`
  title/body ratio as universal.** Both are valid on their own surfaces and
  destructive when lifted into dense operational chrome.
- **Add a typography skill.** Typography is part of design ownership; a second
  skill would split one capability and inflate discovery load.
- **Patch the example product.** Changing the case to prove the skill would
  confuse evidence with the deliverable and create unreviewed product drift.
- **Restore `noootwo-docs` or add project-memory storage.** Existing
  `noootwo-state` already owns progress, durable rules, and document placement.
- **Copy Lovart's surface.** Only the separation of display, product copy, and
  compact controls transfers; private assets, exact layout, and styling do not.

## Verification

- The evidence brief is persisted through `noootwo-state` as
  `typography_balance_2026_11_19`.
- `skills/noootwo-design/evals/prompts/typography-balance-rework.md` exercises a
  rejected all-small/all-large correction together with the target boundary.
- The supplied case's rendered screenshots and computed values were inspected
  as evidence. No case source, test, screenshot, asset, or deployment is part of
  this release.
- The prior-art pass read the published Huashu Design `v3.3.0`, Impeccable
  `skill-v4.10.0`, Anthropic `frontend-design`, Antfu Design `2026.06.22`, and
  Superpowers `v7.0.2` sources. Their mechanisms and surface boundaries are
  recorded in [typography-balance-evidence.md](../reference/typography-balance-evidence.md).
- `python scripts/validate_skill_workspace.py .` must pass after the skill,
  reference, and version changes.

The eval contract is structural until it runs in a fresh model session; this ADR
does not claim a measured behavior improvement.

## Amendment 2026-11-25

- The `11-12px` band remains a dense-desktop house floor, not a universal
  readability standard. It applies only to metadata and body roles that pass
  CJK wrapping, contrast, and 200-percent resize checks; `10px` stays reserved
  for non-reading keycaps, badges, and decorative marks.
- CJK line length is measured in characters or `em`, not `ch`. Latin prose uses
  roughly `45-75ch`; CJK prose targets roughly `30-45` characters per line.
- The WCAG 2.2 reflow check is `320` CSS px, not a `200%` zoom of a wide
  viewport. A `390px` phone screenshot is supporting evidence, not a substitute.
