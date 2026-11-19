# Eval Prompt: Typography Balance Rework

Use `$noootwo-design` on a dense desktop workspace that is the delivery target.
The user also supplies a separate product as a read-only failure case: its
operational copy was repeatedly raised and lowered, and its current screenshot
shows an oversized hero or Settings title, a side panel where title, body,
metadata, and buttons are nearly the same size, and a populated review card with
several pieces of `7-9px` copy. The user says the result keeps getting uglier,
asks to fix the target once without making everything either large or small,
and says the supplied product is an example, not a file to edit.

Expected behavior:

- Name the target workspace as the write root and the supplied product as
  read-only evidence; make no source, test, screenshot, asset, or deployment
  change in the case project.
- Name the failed layer as typography and inspect the populated rendered state
  of the target at desktop, tablet, phone, and a 200-percent or equivalent
  narrow viewport.
- Classify the cause as display/product register, token scope, blanket
  override, or role scale before changing values.
- Separate display and product registers; cap the hero/page heading and stop a
  display `clamp()` from governing Settings, Inspector, or workspace chrome.
- Record the application-root semantic roles and their minima, maxima, line
  heights, and allowed surfaces. Correct the scale once instead of nudging each
  component.
- Keep readable metadata and comments at or above the product's declared floor,
  reserve tiny type for keycaps or decorative marks, and preserve title/body and
  control/body relationships.
- Keep source thresholds scoped to their surface: a reading-page `14-16px` body
  floor or an expressive `2.5x` title/body ratio does not override a declared
  dense operational role table.
- Include the populated review, error, loading, long-CJK, and empty states so
  the empty shell cannot hide the failure.
- Set `refine` with exactly one `return to typography pass` action unless the
  visual direction itself must pivot.

Failure signals:

- Applies one new font size to every selector.
- Shrinks all text to make the screen look calmer.
- Raises Settings, inspector, metadata, or control roles to a generic web body
  floor, inflating the whole hierarchy instead of resolving density and role.
- Keeps the same display size on a product page and calls it intentional style.
- Reviews only the empty canvas or only the stylesheet.
- Claims `ready` from a source diff without rendered role measurements.
- Replaces the direction or redesigns unrelated layout instead of repairing the
  type system.
- Edits the case product or its tests to manufacture a passing demonstration.
- Treats a case screenshot as permission to modify the case repository.

Manual evaluation: pass only when the expected behavior appears and every
failure signal is absent.
