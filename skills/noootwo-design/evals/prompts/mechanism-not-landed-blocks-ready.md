# Eval: A borrowed mechanism that did not land blocks ready

Prompt: "Review this settings page. The reference board says we borrowed progressive disclosure and a persistent save state, but the rendered page only has a card wrapper and a generic save button."

Expected behavior:

- Opens the artifact and the selected reference records.
- Runs Mechanism Landing QA for each selected primary or supplement.
- Records `missing` or `swallowed` for mechanisms absent from the artifact, with evidence.
- Explains what user outcome should have improved, such as comprehension or state recognition.
- Returns to the artifact or approved spec instead of calling the page ready.
- Does not demand pixel-level similarity or confuse fidelity with mechanism translation.

Failure signals:

- Marks the page ready because the tokens and card styling resemble the reference.
- Cites filenames or the reference board as landing evidence.
- Treats a visible decoration as a landed product mechanism.
- Fixes the copy instead of the missing interaction structure.
- Claims the reference was "implemented" without checking the rendered artifact.

Manual evaluation: pass only when at least one missing mechanism blocks `ready` and the return action matches the failure.
