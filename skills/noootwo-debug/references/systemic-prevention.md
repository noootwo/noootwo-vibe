# Systemic Prevention

The systemic close. The local fix proves why this instance broke; the close asks why the system allowed it, where the same conditions remain, and which barrier stops the class from returning.

This is not a second investigation. It consumes the proven evidence chain and asks eight questions in order.

## The eight questions

1. **What failed?** Restate the observed symptom and the raw failure.
2. **How did it fail?** Name the mechanism from the proven cause to the symptom.
3. **Why did it happen?** Identify the contributing conditions and latent conditions that made the mechanism reachable.
4. **Why was it not caught?** Name the missing or ineffective control: test, type, invariant, validation, review, observability, rollout guard, or runtime feedback.
5. **Where else?** Search for the same condition, assumption, helper, schema, boundary, or copy-paste pattern in sibling paths.
6. **What near-miss or fragile success shares it?** Look for paths that still work only because inputs, timing, environment, or traffic have not exercised the unsafe condition yet.
7. **What barrier prevents recurrence?** Choose the smallest durable barrier: remove the cause, make the invalid state unrepresentable, add an invariant or regression test, add a type/lint/schema rule, improve observability, or change a process or skill rule.
8. **How will the system learn if it returns?** Define the signal that would reveal a recurrence and the rule, test, eval, or review that should change if the same class appears again. This is the double-loop question: not only “fix the action”, but “change the governing condition that produced the action”.

## Causal layers

Use three layers, and keep them distinct:

| Layer | Question | Evidence |
| --- | --- | --- |
| Mechanism | How did this instance fail? | Existing evidence chain, repro, toggle, regression test |
| Control | Why did existing defenses allow it? | Failed or missing check, test, review, type, monitor, guard, rollout stage |
| Learning | Why did the process produce and tolerate the condition? | Repeated class, normalized workaround, missing eval, stale assumption, unclear ownership |

The mechanism is already proven before this step. Do not reopen Gate A unless the systemic pass discovers contradicting evidence.

## Proportionality

Scale the response to severity, recurrence, and reach:

- **Isolated, trivial, no shared condition** — record `no credible latent path` and the evidence for that conclusion, then stop.
- **One-off with a shared condition** — add the smallest barrier and record the owner.
- **Repeated or high-impact class** — require a real barrier, a verification path, and a learning-loop change; hand structural work to `noootwo-code-health`.
- **Unknown or cross-system class** — record uncertainty, add instrumentation if cheap, and hand the decision to the owning skill instead of inventing a root cause.

No prevention action may be justified only by “it might happen again”. A latent path needs a concrete condition, a reachable path, or an explicit `[hypothesis]` label with the experiment that would confirm it.

## Sibling and near-miss search

Search systematically, not by memory:

- grep for the failing symbol, helper, schema assumption, validation bypass, error suppression, timeout assumption, and copy-pasted branch;
- inspect callers, sibling implementations, mocks, migrations, and alternate entry points;
- compare working and failing paths to find the condition that separates them;
- inspect successful paths that share the same structure but have not failed yet;
- record each result as `affected`, `safe with reason`, `hypothesis`, or `not searched with reason`.

Absence of a sibling result is a finding only when the search scope is named.

## Recurrence barrier

Prefer barriers in this order:

1. remove the cause or make the invalid state impossible;
2. encode the invariant in a type, schema, parser, or boundary;
3. add a regression test that fails on the pre-fix code;
4. add a lint, static check, review gate, or eval;
5. add observability that detects the condition before the user does;
6. add a process or skill rule change when the failure is organizational rather than local.

A barrier without an owner, a verification path, and a disposition is not a barrier. An action item with no priority or review is how a systemic close becomes a wish list.

## Required output

```markdown
Systemic Close
- Causal layers: mechanism / control / learning
- Similar and latent paths: searched, affected, safe with reason, hypothesis, or not searched
- Near-miss or fragile success: named path and why it escaped
- Recurrence barrier: chosen barrier, owner, verification, and disposition
- Learning loop: signal and rule/test/eval/review that changes if this class returns
- Residual uncertainty: what remains unproven or unsearched
```

## Academic basis

The model is a synthesis, not a claim that one framework is sufficient:

- James Reason's system approach treats accidents as consequences of interacting latent conditions and failed defenses, not as a single unsafe act. That supports questions 3–4 and the control layer. Evidence level: peer-reviewed article. `Human error: models and management`, BMJ 2000, doi:10.1136/bmj.320.7237.768, `https://pmc.ncbi.nlm.nih.gov/articles/PMC1117770/`.
- Nancy Leveson's STAMP treats safety as a control problem: accidents arise when control structures fail to enforce constraints across components and interactions. That supports inspecting missing controls and the control layer in complex systems. Evidence level: academic book. `Engineering a Safer World: Systems Thinking Applied to Safety`, MIT Press, 2011, doi:10.7551/mitpress/8179.001.0001.
- Chris Argyris distinguishes single-loop correction from double-loop learning that changes governing assumptions and policies. That supports question 8 and the learning layer. Evidence level: practitioner-research article. `Double Loop Learning in Organizations`, Harvard Business Review, September 1977, `https://hbr.org/1977/09/double-loop-learning-in-organizations`.
- Google SRE's blameless postmortem practice connects root causes to preventive action, review, priority, and shared learning. That supports the recurrence barrier and the rule that prevention work must be reviewed rather than left as prose. Evidence level: official practice guide. `Postmortem Culture: Learning from Failure`, Google SRE Book, 2017, `https://sre.google/sre-book/postmortem-culture/`.
- Erik Hollnagel's Safety-II shifts attention from only what failed to how everyday performance succeeds and varies. That supports questions 5–6 and the near-miss/fragile-success search. Evidence level: academic book. `Safety-I and Safety-II: The Past and Future of Safety Management`, Ashgate/Routledge, 2014.

## Boundaries

- Do not blame an individual, team, or model; investigate conditions, information, incentives, and controls.
- Do not turn every bug into an architecture program. The systemic close is mandatory; the size of the response is proportional.
- Do not invent latent paths. A hypothesis stays a hypothesis until a concrete path or experiment supports it.
- Do not let a systemic finding expand the local fix. Route structural work to `noootwo-code-health`, product decisions to `noootwo-product`, release or deployment controls to `noootwo-release`, and durable facts to `noootwo-state`.
