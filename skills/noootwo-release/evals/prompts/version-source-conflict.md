# Eval: Version source conflict

Prompt: "The package manifest says 2.4.1, VERSION says 2.5.0, and the latest tag is v2.4.0. Prepare the next release."

Expected:

- Names the conflict instead of silently picking a number.
- Selects one authoritative source according to the project policy or the documented precedence.
- Updates mirrors or records the migration so the sources agree.
- Records the chosen version source as a decision through `noootwo-state`.

Fails when: it invents a fourth version, uses the tag as the source, or leaves the conflict unresolved.
