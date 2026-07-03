---
name: noootwo-review
description: Use for code quality, maintainability, refactoring discipline, architecture hygiene, implementation review, test strategy review, and preventing AI-generated code from becoming unstable, over-abstracted, hard to change, or expensive to reason about.
---

# Noootwo Review

Use this skill when the project needs code to stay easy to understand, change, test, and review.

## Review Stance

Prioritize concrete risk over aesthetic preference:

- behavioral regressions
- unclear ownership or module boundaries
- changes that are too large to review safely
- duplication that causes repeated edits or drift
- abstractions with no current pressure
- missing tests around shared behavior
- files that force agents to load too much context
- docs, comments, or names that hide the real model

## First Pass

1. Read the changed files and their nearest tests/usages.
2. Identify the user-visible behavior that must remain true.
3. Identify the smallest structure that supports the current requirement.
4. Separate defects from future improvements.
5. Prefer local fixes unless the same friction appears in multiple places.

## Refactoring Rules

- Refactor only with a reason tied to changeability, correctness, reviewability, or repeated friction.
- Keep behavior-preserving refactors separate from behavior changes when practical.
- Add tests before risky refactors when the behavior is not already covered.
- Extract abstractions only when they remove real duplication or clarify an existing concept.
- Prefer focused modules and explicit interfaces over large multi-purpose files.
- Keep generated or AI-assisted code boring at the boundaries: predictable names, simple data flow, clear failure paths.

## Output For Reviews

Lead with findings, ordered by severity. For each finding, include:

- exact file/line when available
- why it matters
- concrete failure mode or maintenance cost
- smallest actionable fix

If there are no findings, say so and note remaining test or verification gaps.

## Closure Gate

Before approving or finishing work, verify:

- tests or checks cover the changed behavior
- module boundaries match current responsibility
- no speculative framework or dependency was added
- public docs or release notes were routed to `$noootwo-docs` when needed
- broader workflow or skill routing was routed to `$noootwo-workflow` when needed

For deeper guidance, read `references/code-quality-playbook.md` when planning a refactor, reviewing architecture, or deciding whether to split files.
