---
name: noootwo-review
description: "Use before submit or release, and for risky, public-contract, wide-blast-radius, slow, bloated, or twice-rejected diffs; act as Tech Lead and QA Architect, not style critique."
---

# Noootwo Review

Judge the change and the smallest structural move that removes real risk. Architecture, test strategy, performance, maintainability, refactoring, optimization, and acceptance live here as review lenses.

## When this runs

Run when code reaches submit or release, when a diff is risky, public-contract, or wide in blast radius, and when the same implementation is rejected twice. A code change reaching submit or release without a review decision is not closed.

## Scope

- Default scope is the current change or current diff.
- Full-project review or large refactor runs only when the user explicitly asks for it.
- Make the smallest safe fix directly. Ask before expanding scope, changing product behavior, or choosing between real tradeoffs.

## Lenses

Pick before reading widely. State which you applied and which you skipped.

| Lens | Looks for |
| --- | --- |
| `correctness` | behaviour, contracts, data integrity, security, migrations, release breakage |
| `testability` | missing or brittle proof for changed behaviour |
| `architecture boundary` | ownership, public interfaces, module boundaries, duplicated truth |
| `lean` | over-engineering, YAGNI, redundant code, context-cost growth |
| `performance` | loading, rendering, latency, query cost, algorithmic hotspots, resource use |
| `project health` | validation entry points, CI, release path, docs drift, handoff risk |
| `release readiness` | versioning, tags, publish and install steps, rollback, user-visible notes |
| `rework diagnosis` | which layer failed — product, design, implementation, or evidence |

## Sizing

- Small diff — one to three lenses, self-review changed files and nearest tests, fix locally.
- Medium, broad, or risky diff — structured review; include correctness and testability when behavior changes.
- Release-bound diff — add release readiness and project-health evidence.

## Method

1. Read changed files, nearest tests, callers, public interfaces, and behavior docs.
2. Name the behavior that must stay true and the evidence proving it.
3. Classify risk, then find the smallest structure supporting the current requirement.
4. Separate defects from future improvements.
5. Prefer a local fix unless the same friction appears in more than one place.

## Refactoring work

When structure needs to change without changing behavior, read `references/refactoring-loop.md` and follow it. Do not bundle semantic changes with cleanup. After refactoring, rerun the full relevant test command and return through `references/review-gate.md`.

## Optimization work

When the request is faster, smaller, or cheaper, read `references/optimization-loop.md`. Name the metric and budget, baseline, localize, change the smallest thing, prove before/after, and leave a guard. A regression against a previously working state belongs to `noootwo-debug`.

## What to look for

- behavioural regressions
- unclear ownership or module boundaries
- changes too large to review safely
- duplication that causes repeated edits or drift
- abstractions with no current pressure
- missing tests around shared behaviour
- credible performance risk
- files that force unrelated context to load
- product behavior changed without settled acceptance
- redundant code left "for later"

Agent-generated failure modes: broad files, premature wrappers, hidden state, tests that mirror implementation details, and claims of stability without a proving command.

## Output

Lead with findings ordered by severity: file and line, why it matters, concrete failure mode, smallest fix. If none, say so and name remaining verification gaps.

Structured review includes applied/skipped lenses, evidence read, findings, verification gaps, re-test evidence, acceptance state, and handoff owners.

Severity: `P0` data loss, security, or broken release; `P1` likely behavioral bug or broken contract; `P2` near-term maintainability risk; `P3` optional cleanup.

## Hand off

- Missing or brittle tests → invoke `noootwo-tdd` by reading its `SKILL.md` and following it.
- Product behavior or acceptance unclear → invoke `noootwo-product`.
- Sequencing or scope control → invoke `noootwo-workflow`.
- State, context, or duplicated truth → invoke `noootwo-state`.
- Visual or artifact quality → invoke `noootwo-design`.
- Unknown defect cause → invoke `noootwo-debug`.
- Outside evidence needed → invoke `noootwo-research`.

## References

- `references/code-quality-playbook.md` — lens detail, severity, architecture, AI-code smells, and review output.
- `references/lean-code-review.md` — over-engineering, YAGNI, dependency bloat, and token-cost growth.
- `references/performance-review.md` — loading, rendering, latency, query cost, and regression risk.
- `references/optimization-loop.md` — metric, budget, baseline, localization, before/after proof, and guard.
- `references/project-health-review.md` — foundation, validation paths, CI, release risk, and module boundaries.
- `references/review-gate.md` — scope, TDD precondition, re-test, and user acceptance gate.
- `references/refactoring-loop.md` — behavior-preserving refactor steps and scope control.

Missing skill fallback: first try `npx -y skills add noootwo/noootwo-vibe --global --agent codex --skill <name> --yes`; if install fails, take the smallest direct fallback and mark the record `skill-missing: <name>` (for persistence, write the owning file directly).
