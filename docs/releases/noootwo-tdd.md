# noootwo-tdd Releases

## v0.2.0

- Added a public model-invoked TDD skill owning red-green-refactor and test quality.
- Requires watching a failing test fail for the right reason before implementation.
- Requires the smallest implementation, a full relevant test command, and refactoring only after green.
- Adds hard rules against production-first, tests-after, manual-test-only, and implementation-detail assertions.
- Adds exception boundaries: throwaway, generated, config-only, and no-op docs need explicit user opt-out.
