# Tech Selection

Choosing a library, framework, or platform. The output is a recommendation with its downside stated, not a feature list.

## What to collect

Collect the same evidence for every candidate before comparing them:

- **Fit**: does it solve the actual constraint, at the actual scale, on the actual stack?
- **Adoption**: download or dependency trend, notable production users, and how the project's own users describe it after a year.
- **Maintenance health**: release cadence, how fast issues receive a substantive reply, bus factor across contributors, and whether a company or foundation backs it.
- **Breaking-change history**: how often a minor upgrade forces work, and whether migration guides exist.
- **Size and performance**: bundle or binary cost, cold-start cost, and any published benchmark — measured on a comparable workload, not the project's own marketing chart.
- **API fit**: how much glue code the integration needs, and whether it fights the framework's idioms.
- **Licence and governance**: licence terms, patent clauses, and who can change the terms.
- **Migration cost**: what adoption takes now, and what getting out costs later.

## The comparison

Score each candidate 1–5 on fit, health, cost of adoption, cost of exit, and risk. Then state the tradeoff in one sentence per candidate: what you gain, what you give up.

Two rules keep the comparison honest:

- A candidate with no maintenance-health evidence is a `low` confidence recommendation, whatever its features.
- The incumbent — including the boring, already-installed option — is a candidate. Adoption cost is a real cost.

## When to choose the boring option

Prefer the established, well-documented, widely-deployed option when:

- the differentiating value is not in this layer;
- the team has no capacity to track an unstable dependency;
- the new option's advantage is theoretical at this project's scale;
- the exit cost is high and the project's own future is uncertain;
- the choice would be hard to reverse and easy to explain later.

Choose the newer option when the constraint genuinely cannot be met by the incumbent, and say which measurement shows that.

## Output

```markdown
Decision
- the library or stack choice this settles.

Recommendation
- the choice, and the one-sentence reason.

Comparison
- candidate: fit / health / adoption cost / exit cost / risk, with the evidence level for each.

Evidence
- docs, repository signal, benchmark, or adopter report, with dates.

Downside
- what this choice costs, and when it becomes the wrong choice.

Rejected
- the honest alternative and why it lost.

Exit
- what leaving this choice later would take.
```

## Anti-patterns

- Choosing by star count or by the first search result.
- Comparing feature lists instead of constraints.
- Adopting a library for one function that a few lines of local code would cover.
- Ignoring the migration path away from the choice, then discovering it during an incident.
- Treating a benchmark from the library's own README as independent evidence.
