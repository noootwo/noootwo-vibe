# Code Quality Playbook

Use this when reviewing maintainability, planning a refactor, or deciding whether code structure should change.

## Evidence Sources

- current changed files and tests
- nearest callers and public interfaces
- repeated edit friction
- failing or missing checks
- module size and responsibility drift
- release or migration risk

## Refactoring Heuristics

- Start from observable behavior and keep it covered.
- Prefer small behavior-preserving steps.
- Extract only a concept that already exists in the code.
- Split a file when responsibilities force unrelated context to be loaded together.
- Inline an abstraction when it hides simple flow or has only one weak use.
- Keep data transformation explicit at boundaries.
- Separate mechanical moves from semantic changes when possible.

## Review Severity

- `P0`: data loss, security, broken release, or user-blocking regression.
- `P1`: likely behavioral bug, brittle migration, or broken contract.
- `P2`: maintainability issue that will cause near-term mistakes.
- `P3`: optional cleanup or clarity improvement.

## Anti-Patterns

- architecture introduced for hypothetical future variants
- one file owning routing, data access, validation, formatting, and UI together
- duplicated source-of-truth constants or schemas
- comments explaining what code does instead of why a surprising choice exists
- tests that assert implementation details but miss user-visible behavior
