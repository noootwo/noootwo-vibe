# Optimization Loop

Making something faster, smaller, or cheaper. A regression against a previously working state is a different job — that is a failure with a cause, and it belongs to `noootwo-debug`.

## The loop

1. **Name the metric and the budget.** Latency, throughput, bundle size, memory, query count, cost per call, frame time. State the number that counts as done, and where it came from.
2. **Take a baseline.** A named command that reproduces the measurement on demand. Record the machine, the data size, and whether the run was cold or warm.
3. **Localize.** Profile, trace, query plan, bundle report, flame graph, load test. Find where the time or bytes actually go before deciding what to change.
4. **Change the smallest thing that moves the metric.** One variable at a time, at the layer the evidence points to.
5. **Prove before and after** with the same command on the same workload. Repeat enough runs to see past the noise.
6. **Leave a guard.** A budget check, a benchmark, a CI threshold, or an explicit note that none exists yet.

## Measurement rules

- A measurement without a command is an anecdote. Anything you cannot re-run does not count.
- One variable per experiment; simultaneous changes destroy causality and you will not know which one mattered.
- Know the noise floor. Run the baseline more than once before trusting a small delta.
- Compare like with like: same data size, same cache state, same concurrency, same device class.
- Micro-benchmarks that do not exercise the real workload are a hypothesis, not proof.
- A win that cannot be explained is a coincidence. Find the mechanism before shipping it.

## Where to look

| Layer | Signal to collect |
| --- | --- |
| Frontend | bundle report, Lighthouse CI, WebPageTest waterfall, Core Web Vitals field data, render profiling |
| Browser runtime | long tasks, layout thrash, re-render counts, unvirtualised lists, unnecessary network calls |
| Service | traces, latency percentiles (p50/p95/p99), saturation, queue depth, connection pooling |
| Database | `EXPLAIN` plans, index usage, N+1 query counts, row estimates against reality |
| Native | frame timing, jank, memory growth, startup phases, instrument traces |
| Algorithm | input-size scaling, complexity, allocation churn, benchmark harness (JMH, Criterion, pytest-benchmark) |

Measure in the environment that matters. A local win that does not survive staging or production is a local win.

## Output

```markdown
Optimization
- Metric and budget:
- Baseline: command; result; runs; conditions.
- Localized: where the cost actually is, with the artifact that shows it.
- Change: the smallest change, and why it targets that location.
- After: same command; result; runs.
- Mechanism: why the change moved the metric.
- Guard: benchmark, budget check, CI threshold, or "none yet".
- Remaining: what is still above budget, and what it would cost to fix.
```

## Anti-patterns

- Optimizing before measuring; the first guess is usually not the hot path.
- Micro-optimising code that the profile never shows.
- Caching to hide a query that should not be issued.
- Adding a dependency for a hot loop without measuring its own cost.
- Declaring a win from one noisy run, or from a benchmark on a different workload.
- Chasing a budget that was never agreed, until the change costs more than it returns.

## When to stop

Stop when the budget is met, when the next change costs more than it returns, or when the remaining cost is structural — that becomes an architecture decision, reported rather than smuggled into this pass. Say which one applies.
