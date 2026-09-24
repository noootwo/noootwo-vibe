# Eval: Structural debt gets a disposition

Prompt: "We are preparing a release. This 1,200-line module has not been touched in months, but two recent features both required edits in it."

Expected:

- Runs a Structure Sweep because a release and repeated edits are real triggers.
- Identifies the module as structural pressure when it makes future changes harder, not merely because it is large.
- Proposes the smallest safe move or a bounded planned-refactoring pass, and keeps the current release behavior-preserving.
- Records the result as `fixed now`, `opportunity`, `planned`, `long-term`, or `accepted` through `noootwo-state`.

Fails when: it says the module is out of scope and drops it, or it starts a multi-day rewrite inside the release pass.
