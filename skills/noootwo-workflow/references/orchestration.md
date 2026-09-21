# Orchestration

Workflow schedules one next owner at a time. It does not precompute a full DAG.

## Loop

`snapshot -> route one owner -> specialist runs -> collect result -> update state -> next step or stop`

Each cycle loads only what the current step needs. The specialist owns its method; workflow keeps order, scope, stop conditions, and handoffs.

## Precedence

Use this only to break a stage tie:

1. `noootwo-debug` for an unproven failure or regression.
2. `noootwo-research` for a decision that only outside evidence can settle.
3. `noootwo-product` for an unsettled real user, scope, main path, state, or acceptance.
4. `noootwo-design` for UI/visual/artifact work when the product path is settled but direction is not.
5. `noootwo-tdd` for behavior-changing code, then `noootwo-review` after green.
6. `noootwo-state` after behavior, state, release facts, or instructions change.
7. release ordering only when the user asks to tag or publish.

Do not turn this into a large condition table. If the current evidence points to a different owner, the evidence wins.

## Scope

- Default scope is the current change or current diff.
- Full-project review or large refactor requires an explicit user request.
- A specialist may hand back a sequencing decision to workflow; record it in state rather than reimplementing the specialist.

## Stop conditions

Stop and ask or reroute when:

- no clear owner exists
- a material product, architecture, or release choice is unresolved
- verification is missing and cannot be inferred
- the change would expand public behavior beyond the user's request
- three failed fixes reveal new problems in different places
- user acceptance is required before commit, push, tag, or publish

For external installed skills, stop with one or two candidates when matching is ambiguous; do not choose one on a weak keyword match.
