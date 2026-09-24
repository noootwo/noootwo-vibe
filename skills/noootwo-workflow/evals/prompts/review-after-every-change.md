# Eval: Review is part of done

Prompt: "Add a small validated export option, make sure tests pass, and tell me when it is done."

Expected:

- Routes the behavior change through `noootwo-tdd`.
- After green, returns to `noootwo-review` before reporting the work done.
- The review checks the touched path, chooses a refactoring workflow when structure pressure exists, and disposes of every structural finding.
- Only then reports the result and asks for acceptance before submit or release.

Fails when: it reports done immediately after the tests pass, or treats review as optional until release.
