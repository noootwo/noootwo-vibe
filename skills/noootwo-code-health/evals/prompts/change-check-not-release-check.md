# Eval: One requirement gets a Change Check

Prompt: "Add a validated export option. The backend endpoint and the client form are done, tests for both pass, and the project has a large full test suite. Tell me when the requirement is done."

Expected:

- Labels the pass `Verification: change`.
- Reviews the current diff, changed behavior, nearest callers, and the tests for the endpoint and form.
- Uses one to three lenses and the closest meaningful command set.
- Does not run the full repository suite, a whole-project Structure Sweep, or release evidence.
- Reports the result and asks for acceptance before submit or release.

Fails when: it treats the existence of a large suite as a reason to run it, turns the requirement into a release readiness audit, or skips the scoped review after green.
