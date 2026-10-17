# Eval: TDD uses the relevant test command

Prompt: "Add one validation rule to the billing module. The repo has a full suite that takes 40 minutes; the billing package suite takes 90 seconds and there is a nearest API integration test."

Expected:

- Watches the new test fail for the right reason.
- Makes the minimal implementation and runs the billing package suite.
- Adds the nearest API integration test because the change crosses that boundary.
- Leaves the 40-minute full suite to the Release Check.

Fails when: it runs the full suite after the red-green step without a release boundary, or runs only the new test and ignores the nearest boundary.
