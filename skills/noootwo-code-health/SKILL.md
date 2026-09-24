---
name: noootwo-code-health
description: "Use after non-direct code changes and before submit/release, and when code should become more elegant or healthy: refactoring workflows, structural debt, review, optimization, and acceptance."
---

# Noootwo Code Health

Keep code elegant and healthy: judge the change, then improve the structure it exposed. Architecture, test strategy, performance, maintainability, refactoring, optimization, and acceptance live here as review lenses.

## When this runs

- After every non-direct behavior change, before the work is reported done.
- Before implementation when the existing structure makes the change hard: preparatory refactoring comes first.
- Before submit or release, and when the same implementation is rejected twice.
- When the same area is revised repeatedly, context cost grows, or a structure trigger fires.

A code change reaching submit or release without a review decision is not closed.

## Scope

- Default change review scope is the current diff, its nearest callers, tests, and boundary.
- Refactoring inside the touched path is part of reviewing the change, not scope expansion.
- A full-project Structure Sweep runs only on a trigger or when the user explicitly asks.
- Ask before changing product behavior or choosing between real tradeoffs.

## Two hats

Never mix behavior change with cleanup. The adding-function hat changes behavior and tests; the refactoring hat preserves observable behavior and requires a green baseline. Switch hats deliberately, keep each step small, and return to green after every refactoring step.

## Healthy cycle

Read `references/refactoring-workflows.md` before structural work. Use all six workflows together: preparatory before a hard change; TDD, litter-pickup, and comprehension while working; planned for a known larger area; long-term for restructuring that spans iterations. Planned-only refactoring is a smell. Refactor where the economic payback is credible, not everywhere a smell appears.

## Lenses

Pick before reading widely. State which you applied and which you skipped.

| Lens | Looks for |
| --- | --- |
| `correctness` | behaviour, contracts, data integrity, security, migrations, release breakage |
| `testability` | missing or brittle proof for changed behaviour |
| `architecture boundary` | ownership, public interfaces, module boundaries, duplicated truth |
| `structure health` | file/module/directory shape, cycles, duplication, dead code, context cost, repeated edit friction |
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

1. Read changed files, nearest tests, callers, public interfaces, behavior docs, and the structure the change touched.
2. Name the behavior that must stay true and the evidence proving it.
3. Use code smells to investigate, not to justify a mechanical rewrite.
4. Choose the smallest catalog move that removes the real pressure, then run the relevant tests.
5. Fix what can be fixed safely now; record every other structural finding with a disposition.

## Refactoring work

When structure needs to change without changing behavior, read `references/refactoring-workflows.md` and `references/refactoring-loop.md` and follow them. Do not bundle semantic changes with cleanup. After refactoring, rerun the full relevant test command and return through `references/review-gate.md`.

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
- a large file, directory, or module that the current change made harder to understand or modify
- structural debt recorded as "future improvement" with no trigger or disposition

Agent-generated failure modes: broad files, premature wrappers, hidden state, tests that mirror implementation details, and claims of stability without a proving command.

## Output

Lead with findings ordered by severity: file and line, why it matters, concrete failure mode, smallest fix. If none, say so and name remaining verification gaps.

Structured review includes applied/skipped lenses, evidence read, findings, verification gaps, re-test evidence, acceptance state, refactoring disposition, and handoff owners.

Refactoring disposition: `fixed now`, `opportunity`, `planned`, `long-term`, or `accepted`; every structural finding gets one.

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
- `references/refactoring-workflows.md` — two hats, the six workflows, code smells, catalog vocabulary, structural health, and the debt ledger.

Missing skill fallback: first try `npx -y skills add noootwo/noootwo-vibe --global --agent codex --skill <name> --yes`; if install fails, take the smallest direct fallback and mark the record `skill-missing: <name>` (for persistence, write the owning file directly).
