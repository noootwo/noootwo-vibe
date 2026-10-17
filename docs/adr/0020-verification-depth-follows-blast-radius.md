# 0020 — Verification depth follows blast radius

- Status: accepted
- Date: 2026-10-18
- Owners: `noootwo-workflow`, `noootwo-code-health`, `noootwo-tdd`, `noootwo-release`

## Context

The suite already said review was part of done, but three phrases pulled in
opposite directions:

- `noootwo-code-health` ran after every non-direct behavior change;
- `noootwo-tdd` and the review gate asked for a "full relevant test command";
- a Structure Sweep was part of release readiness.

In practice an agent could read that as: after every requirement, run the full
suite, load every review reference, inspect the whole repository, and produce
release evidence. On a large project that spends tokens and time on checks whose
result cannot change the requirement, while making the actual release gate feel
like one more repetition.

The decision is not "review less". It is "put each kind of evidence at the
boundary where it can change a decision".

## Decision

Match verification to **blast radius**, not diff size or task length.

| Depth | Boundary | Evidence |
| --- | --- | --- |
| `change` | one completed requirement | current diff, changed behavior, nearest callers, affected tests, one to three lenses, the closest meaningful command; nearest integration check only when a seam is crossed |
| `escalated` | a risk trigger widens the blast radius | the `change` evidence plus affected suites and only the lenses that risk requires |
| `release` | before release or a ship-readiness submit gate | full suite or CI for the exact commit, full Structure Sweep, release evidence, and named gaps |

Escalate on evidence, not anxiety. The triggers are a public contract, shared
data/schema/migration, auth or security boundary, shared module with broad
callers, build/release configuration, or an unclear/flaky impact path. A long
task or a large diff does not by itself trigger a Release Check.

Existing CI for the exact commit can satisfy the full-suite part of a Release
Check. The agent should not rerun the same suite locally only to duplicate it.

Every structured review states its depth: `Verification: change | escalated |
release`. That label is the cheap forcing function that prevents a requirement
check from silently becoming a release audit.

## Research basis

The decision is supported by practice for risk-based and change-based testing,
plus review-size evidence. It is not a claim that one benchmark predicts this
repository's token or time savings.

1. **ISTQB Certified Tester Foundation Level syllabus v4.0.1** states that
   exhaustive testing is impossible and that risk-based testing focuses test
   effort; risk analysis influences test scope and thoroughness. It also says
   regression scope should begin with impact analysis. This supports matching
   checks to blast radius and using risk triggers rather than a universal full
   pass.
   <https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf>

2. **Microsoft Azure DevOps Test Impact Analysis** describes the problem
   directly: as a regression suite grows, a full run can take hours and slow CI
   enough to defeat the purpose of continuous integration. TIA selects the
   tests relevant to a commit, includes previously failing and newly added
   tests, and falls back to all tests when it cannot understand the change. It
   also supports configurable periodic full runs. This supports both selective
   change checks and a periodic/release full gate.
   <https://learn.microsoft.com/en-us/azure/devops/pipelines/test/test-impact-analysis?view=azure-devops>

3. **Meta, "Predictive Test Selection"** reports that running all potentially
   impacted tests on every change became infeasible in a large monorepo. Its
   production strategy reduced testing infrastructure cost by a factor of two
   while reporting over 95% of individual test failures and over 99.9% of
   faulty changes. This supports the cost argument and also names the residual
   miss rate that makes escalation and a full release gate necessary.
   <https://arxiv.org/abs/1810.05286>

4. **Google Engineering Practices, "Small CLs"** says small, self-contained
   changes are reviewed more thoroughly, are less likely to introduce bugs, and
   are easier to reason about. This supports keeping a requirement's review on
   its own change and tests rather than expanding it into a repository audit.
   <https://google.github.io/eng-practices/review/developer/small-cls.html>

5. **SmartBear's summary of a Cisco Systems code-review study** reports that
   review effectiveness drops beyond roughly 200–400 lines of code and that
   200–400 lines over 60–90 minutes can yield 70–90% defect discovery. This is
   evidence for review scope and bounded lenses. It is not a token benchmark
   and does not justify a hard line-count gate.
   <https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/>

## Counterexample and boundary

Selective verification is not a proof of absence. Microsoft's TIA falls back to
all tests when it cannot reason about a change, and Meta's predictive selection
still has a residual miss rate. Dynamic dependencies, generated code,
cross-language boundaries, and stale test mappings can hide an affected path.

Therefore:

- a wide or uncertain blast radius escalates immediately;
- the Release Check remains a full gate;
- the agent names verification gaps instead of claiming a selective pass is
  exhaustive;
- the project's own affected-test entry point is preferred when it exists, but
  it is not trusted beyond its known boundary.

## Rejected alternatives

- **Full suite after every requirement.** It makes the release gate redundant
  and spends the most on the least risky boundary.
- **Only changed tests, with no escalation.** It under-checks shared contracts,
  migrations, auth, and broad callers.
- **A fixed token or time budget per change.** It would optimize the metric
  rather than the risk and would not survive different repository sizes.
- **A separate architecture or verification skill.** Verification depth is part
  of code-health's judgment and workflow's scheduling, not a new owner.

## Consequences

- `noootwo-workflow` schedules `code-health/change-check` after a requirement
  and `code-health/release-check` only at the release boundary.
- `noootwo-code-health` owns the definitions, escalation triggers, output label,
  and Structure Sweep placement.
- `noootwo-tdd` exits on the relevant test command; the full suite belongs to
  the Release Check.
- `noootwo-release` refuses to treat a Change Check as release readiness.
- The new eval scenarios measure the positive path, escalation, and release
  boundary before the behavior is treated as stable.

## Verification

- Workspace validator and skill validators must pass.
- The added eval prompts cover a single requirement, shared-schema escalation,
  release-with-CI evidence, and the TDD full-suite mistake.
- Model behavior evals are still owed; this ADR records the intended behavior,
  not a measured rework-rate claim.
