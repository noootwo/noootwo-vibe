---
name: noootwo-tdd
description: "Use for any behavior-changing code: feature, bug fix, or refactor; owns the red-green-refactor loop and test quality. Direct one-file changes keep the same loop, just smaller."
---

# Noootwo TDD

Own the test-first loop for code development. This skill does not decide product scope, architecture, release, or submit; it produces a small, verified behavior change and returns to `noootwo-workflow` for the next step.

## When this runs

Run for any code that changes behavior: a new feature, a bug fix, or a refactor. Do not run for throwaway spikes, generated code, pure config, or no-op docs unless the user explicitly opts in to behavior-code rules.

## The loop

1. Write one failing test for the missing behavior.
2. Run it and watch it fail for the right reason: the behavior is missing, not a typo, setup error, or an existing defect.
3. Write the smallest implementation that makes that test pass.
4. Run the test again and confirm green, then run the closest full test command.
5. Refactor only after green, and keep green. Do not add behavior while refactoring.

A test that passes immediately proves nothing. If the failure is an existing bug or an unrelated layer, stop and return to `noootwo-workflow`; do not write around it here.

## Hard rules

- Never write production code first.
- Never add tests after implementation as a substitute.
- Never accept "manual test passed", "too simple to test", or "spirit not ritual".
- One behavior per test; split an `and` test.
- Assert real behavior, not mock behavior. Mock only slow or external dependencies.
- Derive expected values independently; do not reuse the code under test to compute them.
- For non-trivial logic, mutate the production code once and confirm at least one test fails.
- Test-only helpers stay in test utilities, not production classes.

## References

- `references/test-quality.md` — what makes a test honest and capable of catching the break.
- `references/refactor-safety.md` — behavior-preserving refactor discipline and the green baseline.

## Done when

The test was seen failing for the right reason, the minimal implementation made it green, the full relevant test command is green, and no untested behavior change was smuggled in.

## Hand off

When sequencing, scope, submit, release, or the next specialist is uncertain, return to `noootwo-workflow` by reading its `SKILL.md` and following it.

Missing skill fallback: first try `npx -y skills add noootwo/noootwo-vibe --global --agent codex --skill <name> --yes`; if install fails, take the smallest direct fallback and mark the record `skill-missing: <name>` (for persistence, write the owning file directly).
