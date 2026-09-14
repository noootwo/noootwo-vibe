---
name: noootwo-review
description: "Use to judge code before it ships, to diagnose rework, and to optimize speed, size, or cost. Covers correctness, testability, architecture, lean, performance, project health, and release readiness."
---

# Noootwo Review

Judge the change and the smallest structural move that removes real risk. This is a Tech Lead and QA Architect pass, not a style critique.

Architecture, test strategy, performance, and maintainability live here as lenses. Do not split them into a separate skill.

## When this runs

Run it whenever code reaches submit or release, and whenever a diff is risky, public-contract, or wide in blast radius. Run it when the user rejects the same implementation twice: the `rework diagnosis` lens classifies which layer failed and names the skill that owns it.

A code change that reaches submit or release without a review decision is not closed.

## Lenses

Pick before reading widely. A narrow diff uses the lenses that match it; a project audit or release review may use several. State which you applied and which you skipped.

| Lens | Looks for |
| --- | --- |
| `correctness` | behaviour, contracts, data integrity, security, migrations, release breakage |
| `testability` | missing or brittle proof for changed behaviour |
| `architecture boundary` | ownership, public interfaces, module boundaries, data ownership, duplicated truth |
| `lean` | over-engineering, YAGNI, unnecessary dependencies, redundant code, context-cost growth |
| `performance` | loading, rendering, latency, query cost, algorithmic hotspots, resource use |
| `project health` | validation entry points, CI, release path, docs drift, handoff risk |
| `release readiness` | versioning, tags, publish and install steps, rollback, user-visible notes |
| `rework diagnosis` | which layer failed — product, design, implementation, or evidence |

## Sizing

- **Small diff** — one to three lenses, self-review the changed files and the nearest tests, fix locally.
- **Medium, broad, or risky diff** — structured review. Always include `correctness` and `testability` when behaviour changes.
- **Release-bound diff** — add `release readiness` and the project-health evidence for versioning, tags, install, and rollback.

Make the smallest safe fix directly. Ask before a fix that expands scope, changes product behaviour, or chooses between real tradeoffs.

## Method

1. Read the changed files, the nearest tests, the callers, the public interfaces, and the docs describing the behaviour.
2. Name the behaviour that must stay true, and the evidence that proves it.
3. Classify the risk, then find the smallest structure that supports the current requirement.
4. Separate defects from future improvements.
5. Prefer a local fix unless the same friction appears in more than one place.

## Optimization work

When the request is to make something faster, smaller, or cheaper, this is a measured change rather than a bug hunt. Read `references/optimization-loop.md` and run it in order:

1. Name the metric and its budget before touching code.
2. Take a reproducible baseline with a named command.
3. Localize with a profile, trace, query plan, or bundle report — not with intuition.
4. Change the smallest thing that moves the metric.
5. Prove before and after, then leave the guard that keeps it.

Stop when the budget is met, or when the next change costs more than it returns. A metric that moved without an explanation is not a win; it is a coincidence to investigate. When the symptom is a regression against a previously working state, that is a failure with a cause — invoke the `noootwo-debug` skill instead.

**Done when:** the metric moved with a reproducible before/after, and a guard exists or its absence is recorded.

## What to look for

Concrete risk first:

- behavioural regressions
- unclear ownership or module boundaries
- changes too large to review safely
- duplication that causes repeated edits or drift
- abstractions with no current pressure
- missing tests around shared behaviour
- credible performance risk
- files that force an agent to load unrelated context
- skill instructions that make small tasks run long interviews or heavy gates
- product behaviour that changed without settled acceptance criteria

Agent-generated failure modes get their own attention: broad files, generic wrappers invented before the second use, hidden state and side effects, tests that mirror implementation details, and comments or docs that claim stability without a proving command.

## Output

Lead with findings, ordered by severity. For each: the file and line, why it matters, the concrete failure mode or maintenance cost, and the smallest fix.

If there are none, say so and name the remaining verification gaps.

For a structured review, include the applied lenses, the skipped lenses and why, the evidence read, the findings, the verification gaps, and the owning skill for anything handed off.

Severity: `P0` data loss, security, or a broken release; `P1` a likely behavioural bug or broken contract; `P2` a maintainability issue likely to cause near-term mistakes; `P3` optional cleanup.

## Hand off

- Product behaviour or acceptance unclear → invoke the `noootwo-product` skill.
- Sequencing or scope control needed → invoke the `noootwo-workflow` skill.
- Documentation or duplicated truth → invoke the `noootwo-docs` skill.
- Visual or artifact quality → invoke the `noootwo-design` skill.
- A defect's cause is unknown and the fix needs proof → invoke the `noootwo-debug` skill.
- The judgment needs outside evidence — a library, a benchmark, prior art → invoke the `noootwo-research` skill.

To invoke one, read its `SKILL.md` and follow it.

## Reference

- `references/code-quality-playbook.md` — refactors, architecture, splitting files, and repeated implementation friction.
- `references/lean-code-review.md` — over-engineering, YAGNI, dependency bloat, and token-cost growth.
- `references/performance-review.md` — loading, rendering, latency, query cost, and regression risk.
- `references/optimization-loop.md` — metric, budget, baseline, localization, before/after proof, and the guard.
- `references/project-health-review.md` — foundation, validation paths, CI, release risk, and module boundaries.
