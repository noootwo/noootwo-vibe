# Code Quality Playbook

Use this when reviewing maintainability, planning a refactor, or deciding whether code structure should change.

## Contents

- Practice Basis
- Evidence Sources
- Risk Model
- Project-Health Lens
- Refactoring Heuristics
- Refactor Decision Gate
- AI-Generated Code Smells
- Review Severity
- Anti-Patterns
- Review Output Template
- Refactor Plan Shape

## Practice Basis

- Refactoring practice favors small behavior-preserving steps backed by tests.
- Code review practice favors small, understandable changes and clear findings over broad preference lists.
- Internal quality pays down change cost; speculative architecture can increase it.
- Agent-written code needs extra checks for context cost, duplicated truths, and unjustified abstractions.

## Evidence Sources

- current changed files and tests
- nearest callers and public interfaces
- repeated edit friction
- failing or missing checks
- module size and responsibility drift
- release or migration risk
- docs that describe the changed behavior
- generated code paths, prompts, schemas, or config that may duplicate logic

## Risk Model

Classify each issue before proposing a fix:

| Risk | Question |
| --- | --- |
| `correctness` | Can this produce wrong behavior, data loss, security exposure, or broken releases? |
| `changeability` | Will the next likely change require unrelated files or hidden knowledge? |
| `reviewability` | Is the change too broad, indirect, or mixed to review safely? |
| `testability` | Is the behavior hard to prove with a focused command? |
| `operability` | Will failure be hard to diagnose in CI, deploy, or runtime? |
| `context cost` | Does the structure force agents to load too much unrelated material? |

Do not file a finding just because a different style is possible. Tie every finding to one of these risks.

## Project-Health Lens

Use `project-health-review.md` when the risk is not inside one code block but in the project system around it:

- missing validation entrypoint or test command
- CI not covering release-relevant checks
- unclear release/version/install path
- module boundaries that make future changes expensive
- duplicated project facts across docs, config, prompts, or scripts
- status/risk information only preserved in chat

Report these as `Project Defects` and route ownership instead of turning the code review into a docs rewrite.

## Refactoring Heuristics

- Start from observable behavior and keep it covered.
- Prefer small behavior-preserving steps.
- Extract only a concept that already exists in the code.
- Split a file when responsibilities force unrelated context to be loaded together.
- Inline an abstraction when it hides simple flow or has only one weak use.
- Keep data transformation explicit at boundaries.
- Separate mechanical moves from semantic changes when possible.

## Refactor Decision Gate

Refactor now only when at least one is true:

- current behavior is hard to verify because boundaries are unclear
- the same concept has at least two real implementations drifting apart
- repeated edits require loading unrelated context
- the current shape already caused a bug, missed test, or review confusion
- a small extraction will make the requested change safer now

Defer or reject when:

- the abstraction only supports hypothetical future variants
- the rewrite bundles behavior changes with cleanup without a test boundary
- the current file is large but the requested change touches one clear area
- the fix is mainly naming preference without failure mode

## AI-Generated Code Smells

- overly broad manager/controller/service files
- duplicated constants across code, docs, config, and prompts
- optimistic comments such as "fully validated" without commands
- catch-all error handling that hides the failing layer
- tests that assert snapshots or internals but not behavior
- adapters that pass through data without owning a real boundary
- configuration spread across multiple undocumented sources of truth

## Review Severity

- `P0`: data loss, security, broken release, or user-blocking regression.
- `P1`: likely behavioral bug, brittle migration, or broken contract.
- `P2`: maintainability issue that will cause near-term mistakes.
- `P3`: optional cleanup or clarity improvement.

Use the lowest severity that still reflects the actual failure mode. Do not inflate severity to force cleanup.

## Anti-Patterns

- architecture introduced for hypothetical future variants
- one file owning routing, data access, validation, formatting, and UI together
- duplicated source-of-truth constants or schemas
- comments explaining what code does instead of why a surprising choice exists
- tests that assert implementation details but miss user-visible behavior

## Review Output Template

Use this shape when a structured review is useful:

```markdown
Findings
- [P1] Short title - path:line
  Why it matters, concrete failure mode, smallest fix.

Open Questions
- Only questions that block a correct decision.

Verification Gaps
- Commands not run or behavior not covered.

Project Defects
- Only for project-health gaps that affect safe change, release, handoff, or context cost.

Summary
- One short paragraph only after findings.
```

If there are no findings, say that directly and still list verification gaps or residual risk.

## Refactor Plan Shape

When recommending a refactor, keep it small:

1. Behavior to preserve.
2. Test or command that proves preservation.
3. Mechanical move or extraction.
4. Minimal semantic change, if any.
5. Cleanup of docs/tests only if the public behavior or workflow changed.
