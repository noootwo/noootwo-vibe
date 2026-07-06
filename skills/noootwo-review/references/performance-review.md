# Performance Review

Use this when reviewing performance risk, slow behavior, latency, throughput, rendering jank, resource use, database/query cost, algorithm hotspots, or performance regression risk.

This is a review lens, not a command to optimize everything. Performance work must be evidence-first: measure, localize, change the smallest thing, then verify before/after.

## Practice Basis

- Core Web Vitals focus frontend user experience on loading, responsiveness, and visual stability.
  - Source: https://web.dev/articles/vitals
  - Evidence level: official guidance
- Lighthouse CI and WebPageTest provide repeatable lab checks, budgets, traces, waterfalls, and regression signals for web performance.
  - Sources: https://github.com/GoogleChrome/lighthouse-ci and https://www.webpagetest.org/
  - Evidence level: official/open-source tooling
- Google SRE's four golden signals frame service health around latency, traffic, errors, and saturation.
  - Source: https://sre.google/sre-book/monitoring-distributed-systems/
  - Evidence level: established SRE practice
- OpenTelemetry provides a vendor-neutral model for traces, metrics, and logs across distributed systems.
  - Source: https://opentelemetry.io/
  - Evidence level: CNCF project
- k6 supports repeatable API and system load tests.
  - Source: https://k6.io/docs/
  - Evidence level: open-source tooling
- Database query plans such as PostgreSQL `EXPLAIN` show whether a query is using indexes, scans, joins, and row estimates as expected.
  - Source: https://www.postgresql.org/docs/current/using-explain.html
  - Evidence level: official database documentation
- JMH, BenchmarkDotNet, Criterion.rs, and pytest-benchmark are established benchmark harnesses for language/runtime-specific hot paths.
  - Sources: https://openjdk.org/projects/code-tools/jmh/, https://benchmarkdotnet.org/, https://bheisler.github.io/criterion.rs/book/, https://pytest-benchmark.readthedocs.io/
  - Evidence level: official or established tooling

Borrow the mechanism: budgets, reproducible measurement, traces/profiles/query plans, before/after verification, and explicit uncertainty. Do not vendor these tools into Noootwo Review.

## When To Use

Use this reference when the task or code mentions:

- performance, slow, latency, throughput, p95, p99, timeout, load, stress, capacity
- LCP, INP, CLS, TBT, FCP, bundle size, render, rerender, jank, layout thrash
- N+1, query plan, index, cache, pagination, payload size, connection pool
- CPU, memory, allocation, algorithm complexity, hotspot, benchmark, profiler
- performance regression, budget, monitoring, trace, metrics, Web Vitals, Lighthouse, k6

Do not require this for every review. Use it only when performance affects user experience, release risk, cost, scalability, or the current change touches a performance-sensitive path.

## Evidence Ladder

Apply this order before recommending changes:

1. `impact`: What user, request, workflow, or resource is slow or at risk?
2. `baseline`: Is there a current metric, budget, trace, benchmark, query plan, or report?
3. `scope`: Is the issue frontend loading, frontend rendering, backend/API, database/query, algorithm/runtime, or infrastructure saturation?
4. `localize`: Use the nearest available evidence: Lighthouse/WebPageTest/DevTools, React/Vue profiler, server logs/traces, OpenTelemetry, k6, query plans, language profiler, or benchmark harness.
5. `smallest fix`: Recommend the smallest change that targets the measured bottleneck.
6. `verify`: Name the command, benchmark, trace, query plan, or manual scenario that proves before/after.
7. `monitor`: Decide whether this needs a budget, CI check, dashboard, alert, or release note.

If a rung is missing, report a verification gap instead of guessing.

## Review Surfaces

### Frontend Loading

Look for:

- oversized JS/CSS bundles, unused dependencies, route code that is not split
- unoptimized images, missing dimensions, missing responsive sources, above-fold lazy loading
- render-blocking scripts/styles, unnecessary third-party scripts, font loading issues
- poor LCP, INP, CLS, FCP, or TBT evidence

Prefer fixes such as code splitting, removing unused imports, image resizing/formatting, reserving media dimensions, deferring non-critical work, and adding a repeatable budget. Do not chase scores while breaking accessibility or content correctness.

### Frontend Rendering

Look for:

- repeated rerenders, expensive derived state, unstable props, missing virtualization for long lists
- layout thrashing from interleaved DOM reads/writes
- animation of layout properties instead of transform/opacity
- long tasks blocking input or causing visible jank
- memory leaks from subscriptions, observers, timers, or retained large data

Require profiler, trace, or a realistic interaction path before recommending large rewrites. Memoization is only a fix when the rerender cost is real and the dependency model stays correct.

### Backend/API

Look for:

- high p95/p99 latency, timeouts, large payloads, chatty request patterns, sync work in request paths
- missing pagination, missing streaming for large responses, missing compression where appropriate
- unbounded concurrency, connection pool exhaustion, retry storms, or uninstrumented slow paths
- cache proposals that lack invalidation, authorization, or data freshness rules

Use SRE-style signals: latency, traffic, errors, and saturation. Do not approve a cache, queue, batch job, or async rewrite unless correctness and failure modes are explicit.

### Database And Query

Look for:

- N+1 queries, missing pagination/limits, full scans on growing tables, wrong join shape
- indexes proposed without query evidence or write-cost discussion
- missing query plan, stale row estimates, large sorts, lock contention, or transaction scope issues
- application loops that duplicate database aggregation or filtering already available in the database

Prefer `EXPLAIN`/query-plan evidence and realistic cardinality. Do not recommend an index, denormalization, cache, or query rewrite without naming the query and the verification path.

### Algorithm And Runtime

Look for:

- suspicious complexity on growing inputs, repeated work inside loops, avoidable allocation churn
- CPU or memory hotspots in profiled code paths
- micro-optimizations without benchmark or user impact
- benchmark code that is not representative of production input shape

Require benchmark/profiler evidence before algorithm rewrites unless the complexity bug is obvious and directly tied to input growth. Prefer standard libraries or existing dependencies when they solve the measured problem safely.

## Safety Floor

Performance fixes must not remove or weaken:

- validation, authorization, authentication, rate limiting, or injection protection
- accessibility semantics, focus behavior, labels, or readable contrast
- data integrity, transaction safety, idempotency, or ordering guarantees
- error handling that preserves debuggability and safe failure
- business invariants or required audit/logging behavior
- tests that prove correctness of a non-trivial behavior

If code looks slower because it protects one of these, mark it as `safety-keep` or report the real bottleneck elsewhere.

## Output Contract

Use `Performance Findings` when the user asks for performance review or the current change introduces credible performance risk:

```markdown
Performance Findings
- [P1] Short title - path:line
  Surface: frontend loading | frontend rendering | backend/API | database/query | algorithm/runtime
  Evidence: metric, trace, profile, query plan, benchmark, or `missing evidence`
  Impact: affected user path, endpoint, table, job, or input shape
  Bottleneck: measured or likely bottleneck, with uncertainty if not measured
  Smallest fix: concrete action
  Verification: command, benchmark, trace, query plan, or manual scenario
  Monitoring: budget, CI, dashboard, alert, or `not needed`

Performance Verification Gaps
- Missing baseline, budget, trace, profiler output, query plan, benchmark, or production metric.

Honesty Boundary
- Do not claim faster load time, lower latency, lower CPU, lower memory, or cost reduction without before/after evidence.
```

For narrow diffs, keep performance findings after correctness findings and before optional cleanup. A correctness or security issue outranks a performance issue unless the performance defect blocks users or release.

## Project-Level Performance Defects

When reviewing the whole project, report these under `Project Defects`:

- no performance budget for release-sensitive frontend surfaces
- no load/benchmark entrypoint for performance-sensitive backend or algorithm paths
- no production metrics, traces, logs, or slow-query visibility for known hot paths
- CI cannot detect performance regressions that the release depends on
- database query performance cannot be inspected because query plans or realistic fixtures are unavailable

Route ownership:

- `$noootwo-workflow`: decide whether performance work belongs in current scope, release gates, or future hardening.
- `$noootwo-docs`: record stable performance commands, budgets, dashboards, or known gaps in the right documentation layer.
- `$noootwo-review`: classify findings and verify performance fixes preserve correctness.
