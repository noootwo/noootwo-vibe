# Code Quality Playbook

Use this when reviewing maintainability, planning a refactor, or deciding whether code structure should change.

## Contents

- Practice Basis
- Evidence Sources
- Review Lens Selector
- Risk Model
- Lean-Review Lens
- Performance-Review Lens
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
- Lean code practice reduces unnecessary code only after understanding behavior and protecting validation, safety, accessibility, and checks.
- Performance practice favors baselines, budgets, profiling, traces, query plans, and before/after verification over speculative optimization.

## Evidence Sources

- current changed files and tests
- nearest callers and public interfaces
- repeated edit friction
- failing or missing checks
- module size and responsibility drift
- release or migration risk
- performance baselines, budgets, traces, profiles, query plans, benchmarks, or production metrics
- docs that describe the changed behavior
- generated code paths, prompts, schemas, or config that may duplicate logic

## Review Lens Selector

Select lenses before expanding the review surface:

| Lens | Use when | Evidence |
| --- | --- | --- |
| `correctness` | behavior, contract, data, security, migration, or release breakage is plausible | changed code, callers, tests, schemas, migrations, release files |
| `testability` | behavior is changed but hard to prove | nearest tests, commands, fixtures, manual scenarios |
| `architecture boundary` | responsibility may belong in another module, API, or package | module ownership, public interfaces, repeated edits |
| `lean/bloat` | code may be redundant, speculative, or dependency-heavy | imports, dependency manifest, local helpers, actual use count |
| `performance` | user latency, rendering, query, throughput, CPU, memory, or cost may regress | baseline, trace, profile, query plan, benchmark, metric |
| `project health` | safe change, release, CI, status, or handoff may be weak | README, AGENTS, docs/status, CI, scripts, release notes |
| `AI-code/context cost` | generated structure may force future agents to load too much or trust duplicated rules | file size, wrapper layers, prompts, schemas, docs overlap |
| `release readiness` | version, tag, publish, install, rollback, or user-visible release note matters | manifest, VERSION, tags, release docs, install checks |

For a narrow diff, two or three lenses are usually enough. Do not turn an implementation review into a project audit unless the user asked for it or release/project-health evidence makes it necessary.

## Risk Model

Classify each issue before proposing a fix:

| Risk | Question |
| --- | --- |
| `correctness` | Can this produce wrong behavior, data loss, security exposure, or broken releases? |
| `changeability` | Will the next likely change require unrelated files or hidden knowledge? |
| `reviewability` | Is the change too broad, indirect, or mixed to review safely? |
| `testability` | Is the behavior hard to prove with a focused command? |
| `operability` | Will failure be hard to diagnose in CI, deploy, or runtime? |
| `performance` | Will this create measurable user latency, render jank, resource cost, query cost, throughput, or algorithm/runtime risk? |
| `context cost` | Does the structure force agents to load too much unrelated material? |

Do not file a finding just because a different style is possible. Tie every finding to one of these risks.

## Lean-Review Lens

Use `lean-code-review.md` when the risk is unnecessary code expansion rather than a conventional correctness defect:

- speculative functionality or configuration
- local code duplicating project helpers
- hand-rolled standard-library behavior
- custom platform features where native APIs fit
- new dependency when an installed dependency or a few lines suffice
- one-use abstraction layers, factories, adapters, or wrappers
- fragmented helper code that makes future agents load more context

Report these as `Lean Findings`. Keep safety-related code even when it is longer.

## Performance-Review Lens

Use `performance-review.md` when the risk is slow or expensive behavior rather than structure alone:

- frontend loading: LCP, INP, CLS, bundle size, image/font loading, render-blocking assets
- frontend rendering: rerenders, layout thrashing, long tasks, animation jank, memory leaks
- backend/API: p95/p99 latency, timeouts, payload size, unbounded concurrency, cache correctness
- database/query: N+1, missing pagination, query plans, index evidence, slow-query visibility
- algorithm/runtime: complexity growth, CPU or memory hotspots, allocation churn, benchmark validity

Report these as `Performance Findings` when there is evidence or credible risk. If evidence is missing, report a performance verification gap instead of claiming a speedup.

## Project-Health Lens

Use `project-health-review.md` when the risk is not inside one code block but in the project system around it:

- missing validation entrypoint or test command
- CI not covering release-relevant checks
- missing performance budgets, benchmarks, load tests, traces, dashboards, or slow-query visibility for performance-sensitive paths
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
Review Scope
- Applied lenses: correctness, testability, ...
- Skipped lenses: performance skipped because the changed path is not runtime-sensitive.
- Evidence read: changed files, nearest tests, public interfaces, relevant docs.

Findings
- [P1] Short title - path:line
  Why it matters, concrete failure mode, smallest fix.

Open Questions
- Only questions that block a correct decision.

Verification Gaps
- Commands not run or behavior not covered.

Performance Findings
- Only for measured or credible performance risk, with baseline/profiler/query-plan/benchmark evidence or an explicit verification gap.

Performance Verification Gaps
- Missing baseline, budget, trace, profiler output, query plan, benchmark, or production metric.

Project Defects
- Only for project-health gaps that affect safe change, release, handoff, or context cost.

Lean Findings
- Only for over-engineering or bloat findings with a concrete smaller replacement.

Handoff
- `$noootwo-workflow`: sequencing, release, or unresolved decision ownership.
- `$noootwo-docs`: documentation/source-of-truth update ownership.
- `$noootwo-design`: artifact or UI-quality review ownership.

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
