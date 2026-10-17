# Eval: Bugfix is a failing test before a fix

Prompt: "Empty email is accepted; it should be rejected."

Expected:

- The agent writes a test for the missing rejection behavior.
- It watches it fail for the right reason.
- It implements the minimal fix and runs the relevant suite for the touched behavior and nearest boundary.
- If the failure is an unrelated existing bug, it returns to workflow/debug rather than writing around it.

Fails when: it changes production code first, adds a test after, treats manual reproduction as sufficient, or runs the whole repository suite as the TDD exit.
