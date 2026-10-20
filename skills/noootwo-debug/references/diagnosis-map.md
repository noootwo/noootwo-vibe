# Diagnosis Map

Use this when the request is to confirm suspected problems, find evidence for a claim, or recommend options before one failure is proven. It also applies when several questions arrive together: each claim gets its own authority and can stop independently.

The map is the scope. A system tour, cross-layer audit, patch, or evidence bundle is not.

## One row per claim

```
Question:       <the specific, falsifiable claim>
Class:          product | external | protocol | code-path | deployment | data | agent-process
Authority:      <the evidence allowed to settle this class>
Decisive check: <the cheapest observation that can change the status>
Status:         open | confirmed | refuted | insufficient | decision-needed
Stop / widen:   <why this check is enough, or the exact condition for one follow-up>
Handoff:        <none | product | research | code-health | tdd | release | state | workflow>
```

Write `The daily sync deletes retired models from the live catalog`, not `check the sync`. One row per claim; do not merge nearby questions just because they touch the same repository.

Order work by prerequisite, then cost, then impact if confirmed. An expensive question does not become cheaper by bundling it with five unrelated ones.

## Evidence authority

| Class | Authoritative evidence | Does not settle it |
| --- | --- | --- |
| `product` | The requirement, accepted spec, or explicit product decision | Current code, logs, or what the system happens to do |
| `external` | Official protocol or capability documentation plus a real invocation or artifact for this use | A local wrapper's assumption or a remembered API |
| `protocol` | Actual request and response, status, headers, wire trace, or endpoint logs | Static code reading alone |
| `code-path` | A runnable repro, checkpoint output, debugger state, or trace | Reading code and inferring what it probably does |
| `deployment` | Release record, exact commit, artifact digest, deployment marker, and live version or config | Local source, a CI plan, or an unverified build |
| `data` | A scoped query result with time, event order, idempotency record, or stored state | Schema comments or business-code intent |
| `agent-process` | Transcript, tool trace, loaded rule or skill version, and eval output | Unrelated business-repository code |

Authority is layer-specific. A product decision can constrain desired behavior; it does not prove what happened in one instance. Official documentation can define a protocol; it does not prove the live deployment supports it. When two authorities conflict, record `decision-needed` instead of collecting more of the weaker evidence.

## Read-only by default

While any requested claim is still being confirmed:

- read source, docs, logs, traces, and live read-only endpoints;
- run checks that observe without changing persistent state;
- create temporary captures outside the source tree only when needed.

Stop before a source edit, generated patch, test rewrite, image rebuild, deployment, persistent config or data mutation, or broad evidence package. Instrumentation is a mutation: name the prediction it separates and get permission first.

If the user says "confirm and fix", confirmation still comes first. Deliver the short verdict, then send only `confirmed` failures into the Incident Path. Refuted and insufficient claims do not earn a fix.

## Stop and widen

- Give each claim one decisive check.
- Allow one follow-up only when the result conflicts with an authority, is ambiguous, or leaves a required branch untested.
- Stop when every claim is `confirmed`, `refuted`, `insufficient`, or `decision-needed`; stop there even if more could be learned.
- Widen only for a named prerequisite of the same claim or a new user question.
- Stop when the next action enters a new system, changes code or deployment, or repeats evidence with no new discriminating power.
- Keep claims independent until evidence proves a shared cause. Proximity is not a shared cause.

## Output

Lead with the verdict, then the minimum evidence:

```
Diagnosis Map
Q1 [confirmed]    <claim> — <authority: decisive result>
Q2 [refuted]      <claim> — <authority: decisive result>
Q3 [insufficient] <claim> — <missing observation and what would close it>

Confirmed:
Refuted:
Insufficient:
Decision needed:
Options and tradeoffs:
Next owner:
```

A long report does not upgrade a status. `Insufficient` is a complete result when the next check would require access, mutation, or a new decision.

## Handoff

- A confirmed failure with a reproducible symptom -> Incident Path below, one mapped failure at a time.
- Desired behavior or acceptance unsettled -> `noootwo-product`.
- A decision that only outside evidence can settle -> `noootwo-research`.
- Settled facts need an implementation shape -> `noootwo-code-health`.
- Live version, artifact, or deployment truth is the question -> `noootwo-release`.
- The next sequence or owner is unclear -> `noootwo-workflow`.
- A durable fact changed -> `noootwo-state`.

Do not do a receiving skill's job inside the diagnosis. Hand over the settled map row and its evidence, then let that owner decide.
