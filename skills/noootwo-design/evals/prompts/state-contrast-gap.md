# Eval Prompt: State Contrast Gap

Use `$noootwo-design` on a checkout form where the primary button's focus ring
is hidden behind a sticky footer and the inline error message is only `3.4:1`
against its surface. The page has no clipping, overflow, or spacing defect, and
the default button and body text contrast pass. The user says the form looks
polished and asks whether it can ship.

Expected behavior:

- Test the default, hover, focus, active, disabled, loading, error, and success
  states, not only the default screenshot.
- Apply the WCAG 2.2 AA checks: `1.4.3` text contrast for the error message,
  `1.4.11` non-text contrast for focus and control boundaries, and `2.4.11`
  focus not obscured by sticky chrome.
- Name the hidden focus ring and the error-message text contrast as separate
  blocking defects with evidence.
- Return to the artifact, repair the owning styles and sticky offset, and
  re-check the states before `ship`.

Failure signals:

- Checks only the default state or only the default-state contrast.
- Accepts the focus ring because it exists in the stylesheet but is not visible
  in the rendered state.
- Treats the error message as decorative or exempt.
- Declares shipping because the page has no layout defect.

Manual evaluation: pass only when the response catches both state failures and
blocks `ship`.
