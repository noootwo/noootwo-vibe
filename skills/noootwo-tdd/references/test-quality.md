# Test Quality

A test is useful only when it can fail for the right reason and can be rerun by someone else.

## Before writing

- Name the production change that would make this test fail. If you cannot, the test is decoration.
- Choose one observable behavior, not a private implementation detail.
- State the expected result from the contract or example, not by running the implementation.

## While writing

- Prefer real objects and real inputs. Mock only boundaries that are slow, flaky, external, or expensive.
- If a mock is unavoidable, mirror the real interface closely enough that the test would catch a contract change.
- Do not assert that a mock was called unless that call is the observable side effect.
- Do not parse logs, source text, or snapshots as the primary proof; assert output, state, side effects, or exit status.
- Keep test setup small and local. One behavior, one test name without `and`.

## After green

- Run the full relevant suite, not only the new test.
- Mutate a behavior-bearing line once and verify a test fails. Restore it immediately.
- Leave a guard only where it protects a real boundary. Do not add coverage for framework behavior or generated plumbing.

## Red flags

- Test passes on first run.
- Failure is a typo, import error, or environment issue and the implementation is already present.
- Test asserts implementation details while missing the user-visible behavior.
- Mock setup is longer than the code under test and never exercises real behavior.
