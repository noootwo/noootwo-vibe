---
name: noootwo-code-health
description: "Use before a non-obvious change to shape its seam; after each change for a scoped review; before release for a full structure, performance, and acceptance gate."
---

# Noootwo Code Health

Keep code elegant and healthy: shape a non-obvious change into the existing code before implementation, then judge and improve the structure the change exposed. Architecture, seams, test strategy, performance, maintainability, refactoring, optimization, and acceptance live here as lenses.

## When this runs

- Before implementation of a non-obvious change: run an Integration Read and produce a Change Shape before TDD.
- After every non-direct behavior change: run a Change Check before the work is reported done.
- Before release or a ship-readiness submit gate: run a Release Check once for the exact commit.
- Before implementation when the existing structure makes the change hard: preparatory refactoring is a Change Shape disposition.
- When the same implementation is rejected twice, or a Structure Sweep trigger fires.

Skip the Integration Read for a local change with an obvious seam and no contract, data, or migration impact. A Change Check is not a Release Check.

## Verification depth

Match verification to **blast radius**, not diff size or task length.

- **Change Check** — the default after one requirement: current diff, changed behavior, nearest callers, and affected tests; one to three lenses; the closest meaningful command, plus the nearest integration check only when a seam is crossed. No full-suite or whole-repo audit.
- **Escalated Check** — when the change touches a public contract, shared data/schema/migration, auth or security boundary, shared module with broad callers, build/release config, or an unclear/flaky impact path: add the impacted suites and only the lenses that risk requires.
- **Release Check** — before release or a ship-readiness submit gate: full automated suite, full Structure Sweep, release evidence, and named verification gaps. Existing CI for the exact commit may satisfy it; do not rerun the same full suite locally.

Escalate on evidence, not anxiety. Stop when the evidence covers the blast radius; state the remaining gap instead of widening the audit.

## Scope

- Change Check scope is the current diff, nearest callers, tests, and boundary.
- Release Check scope is the full project and release surface.
- Integration Read scope is the nearest seams, contracts, data owners, and existing patterns.
- Refactoring inside the touched path is part of the change; a full Structure Sweep runs only on a trigger or explicit request.
- A disputed premise — whether behavior fails, which build ran, or what data exists — goes to `noootwo-debug` or `noootwo-release` before shaping.
- Ask before changing product behavior or choosing between real tradeoffs.

## Integration Read

Read `references/integration-read.md` before shaping a non-obvious change. Produce a compact **Change Shape**, not a design document or implementation manual:

- intent and invariants that must stay true;
- seam, owning boundary, and what stays stable;
- interface, data, event, and migration contracts;
- existing patterns to reuse and new concepts that current pressure justifies;
- reversibility and compatibility;
- test seam and the smallest first behavior slice;
- rejected alternatives, or why none existed.

The Change Shape is a decision before either hat. It can end in direct TDD, a preparatory refactor, a product/design/research handoff, or a stopped change. It changes no behavior itself.

## Two hats

Never mix behavior change with cleanup. The adding-function hat changes behavior and tests; the refactoring hat preserves observable behavior on a green baseline. Switch deliberately, keep each step small, and return to green after every refactoring step.

## Healthy cycle

Read `references/refactoring-workflows.md` before structural work. Use all six workflows together: preparatory before a hard change; TDD, litter-pickup, and comprehension while working; planned for a known larger area; long-term for restructuring across iterations. Planned-only refactoring is a smell. Refactor where payback is credible, not everywhere a smell appears.

## Lenses

Pick before reading widely. State which you applied and which you skipped.

| Lens | Looks for |
| --- | --- |
| `correctness` | behaviour, contracts, data integrity, security, migrations, release breakage |
| `testability` | missing or brittle proof for changed behaviour |
| `architecture boundary` | ownership, public interfaces, module boundaries, duplicated truth |
| `structure health` | file/module shape, cycles, duplication, dead code, context cost, repeated edit friction |
| `lean` | over-engineering, YAGNI, redundant code, context-cost growth |
| `performance` | loading, rendering, latency, query cost, hotspots, resource use |
| `project health` | validation entry points, CI, release path, docs drift, handoff risk |
| `release evidence` | version, artifact, deployment trace, rollback, release notes owned by `noootwo-release` |
| `rework diagnosis` | which layer failed — product, design, implementation, or evidence |

## Method

1. Read changed files, nearest tests, callers, interfaces, behavior docs, and the structure the change touched.
2. Name the behavior that must stay true and the evidence proving it.
3. Use code smells to investigate; choose the smallest catalog move that removes the real pressure.
4. Run the relevant tests, fix what is safe now, and record every other structural finding with a disposition.

## Refactoring and optimization

Refactoring needs `references/refactoring-workflows.md` and `references/refactoring-loop.md`; never bundle it with semantic change, and rerun the command that covered the refactored behavior and nearest boundary. Optimization needs `references/optimization-loop.md`: name the metric and budget, baseline, localize, prove before/after, leave a guard. A regression against a working state belongs to `noootwo-debug`.

## Output

For an Integration Read, lead with the Change Shape, one-way doors, smallest first slice, and what would change the shape. For a review, lead with findings ordered by severity: file and line, why it matters, failure mode, smallest fix. If none, say so and name verification gaps.

Include `Verification: change | escalated | release`, applied/skipped lenses, evidence read, re-test evidence, acceptance state, refactoring disposition, and handoff owners. Every structural finding gets `fixed now`, `opportunity`, `planned`, `long-term`, or `accepted`.

Severity: `P0` data loss, security, or broken release; `P1` likely behavioral bug or broken contract; `P2` near-term maintainability risk; `P3` optional cleanup.

## Hand off

- Change Shape ready for behavior change, or tests missing/brittle → invoke `noootwo-tdd` by reading its `SKILL.md` and following it.
- Product behavior or acceptance unclear → invoke `noootwo-product` by reading its `SKILL.md` and following it.
- Sequencing or scope control → invoke `noootwo-workflow` by reading its `SKILL.md` and following it.
- State, context, or duplicated truth → invoke `noootwo-state` by reading its `SKILL.md` and following it.
- Visual or artifact quality → invoke `noootwo-design` by reading its `SKILL.md` and following it.
- Unknown defect cause → invoke `noootwo-debug` by reading its `SKILL.md` and following it.
- Outside evidence needed → invoke `noootwo-research` by reading its `SKILL.md` and following it.
- Version, tag, artifact, deployment trace, rollback, or release health → invoke `noootwo-release` by reading its `SKILL.md` and following it.

## References

- `references/integration-read.md` — triggers, seam read, Change Shape, sizing, boundaries, and failure modes.
- `references/code-quality-playbook.md` — lens detail, severity, architecture, AI-code smells, and review output.
- `references/lean-code-review.md` — over-engineering, YAGNI, dependency bloat, and token-cost growth.
- `references/performance-review.md` — loading, rendering, latency, query cost, and regression risk.
- `references/optimization-loop.md` — metric, budget, baseline, localization, before/after proof, and guard.
- `references/project-health-review.md` — foundation, validation paths, CI, release risk, and module boundaries.
- `references/review-gate.md` — verification depth, scope, TDD preconditions, re-test, and user acceptance.
- `references/refactoring-loop.md` — behavior-preserving refactor steps and scope control.
- `references/refactoring-workflows.md` — two hats, the six workflows, code smells, catalog vocabulary, structural health, and the debt ledger.

Missing skill fallback: first try `npx -y skills add noootwo/noootwo-vibe --global --agent codex --skill <name> --yes`; if install fails, take the smallest direct fallback and mark the record `skill-missing: <name>` (for persistence, write the owning file directly).
