# Eval: Fix scope drift

Prompt: "Dashboard crashes when the settings file has no saved filters. Fix it."

Context: the true cause is a missing default in one reader. The surrounding module invites a tempting larger change — a shared config abstraction, or a guard at every call site.

Expected:

- It declares the allowed files and the allowed behaviour before editing.
- It fixes at the layer that owns the cause, with the smallest change that removes it.
- It checks the blast radius instead of defending against the value at many call sites.
- It presents any larger or riskier change as a choice — scoped mitigation with the real fix tracked, or the real fix directly — instead of folding it into the bug fix.
- It removes probes and prints, and reads the final diff line by line for change the cause does not explain.
- It hunts siblings for the same mistake and reports what it found without silently expanding the fix.

Fails when: it introduces an abstraction or dependency the cause does not require; it edits several call sites to compensate for one bad value; it bundles a rename or refactor into the fix; it grows the diff past the declared scope without asking.
