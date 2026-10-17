# Eval: Review is part of done

Prompt: "Add a small validated export option, make sure tests pass, and tell me when it is done."

Expected:

- Routes the behavior change through `noootwo-tdd`.
- After green, returns to `noootwo-code-health` for a Change Check before reporting the work done.
- The review checks the touched path with one to three lenses, chooses a refactoring workflow when structure pressure exists, and disposes of every structural finding.
- It does not run the full suite or a whole-project Structure Sweep unless a risk trigger or release boundary appears.
- Only then reports the result and asks for acceptance before submit or release.

Fails when: it reports done immediately after the tests pass, treats review as optional until release, or turns the Change Check into a Release Check.
