# Eval: Demonstrated aesthetic harm blocks ready

Prompt: "The dashboard uses a cream background, eyebrow labels above every panel, and gradient titles. Ship it if it looks designed."

Context: The rendered desktop and mobile captures show washed-out hierarchy, clipped headings, and illegible small text. Keyboard focus is also missing.

Expected:

- Records the aesthetic flags with the observed harm rather than rejecting pattern names alone.
- Reports the safety hard-gate failure and the concrete readability and hierarchy defects.
- Chooses `refine` or `needs artifact`, not `ready`.
- Names one return action that addresses the demonstrated harm.

Fails when: it approves the artifact because the style was intentional; it lists flags without artifact evidence; or it treats the safety failure as a matter of taste.
