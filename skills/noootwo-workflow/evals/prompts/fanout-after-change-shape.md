# Eval: The Fan-out Gate follows the settled change shape

Prompt: "Shape and implement this cross-module change. Two possible seams look independent, but nobody has settled the interface, owned files, or acceptance checks. Start four agents now so it is faster."

Expected:

- Runs `noootwo-code-health`'s Integration Read first because the seam is non-obvious.
- Uses the settled Change Shape to draft the plan, then runs the Fan-out Gate before accepting it as execution-ready.
- Uses the settled contracts and verification seams to test independence.
- Dispatches only the units that pass the Gate; unresolved or coupled units stay serial or stop for a decision.

Fails when: it starts workers before the seam and contracts are settled; it invents interfaces to make the units look independent; or it treats a speed request as permission to skip the shape.
