# noootwo-tdd Releases

## v0.6.1

- Added the package-wide context lifecycle and compressed the always-loaded description.
- Red-green-refactor, relevant-test proof, and the Release Check boundary are unchanged.

## v0.6.0

- Replaced the ambiguous "full relevant test command" with the relevant test command for the touched behavior and nearest boundary.
- The full suite is now owned by the Release Check; TDD uses the project's affected-test entry point, the package or module suite, and the nearest integration test when a seam is crossed.
- Updated the test-quality guidance, refactor safety, and evals to keep one requirement's proof proportional.

## v0.5.0

- When the implementation shape or seam is unsettled, TDD now returns to `noootwo-workflow` instead of inventing architecture inside the red-green loop.

## v0.4.0

- Updated the post-green review handoff from `noootwo-review` to `noootwo-code-health`.

## v0.3.0

- Aligned the refactor step with the review healthy cycle: red and green are the adding-function hat, the post-green refactor is the refactoring hat, and the two never mix.
- Removed the blanket "large file may defer" rule. A large touched area now gets a small comprehension or litter-pickup improvement where safe, while larger restructuring is dispositioned instead of ignored.

## v0.2.0

- Added a public model-invoked TDD skill owning red-green-refactor and test quality.
- Requires watching a failing test fail for the right reason before implementation.
- Requires the smallest implementation, a full relevant test command, and refactoring only after green.
- Adds hard rules against production-first, tests-after, manual-test-only, and implementation-detail assertions.
- Adds exception boundaries: throwaway, generated, config-only, and no-op docs need explicit user opt-out.
