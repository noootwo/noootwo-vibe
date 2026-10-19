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
5. `noootwo-code-health` Integration Read before implementation when the seam is non-obvious; its Change Shape may call for preparatory refactoring, direct TDD, or another owner.
6. `noootwo-tdd` for behavior-changing code, then `noootwo-code-health` for a Change Check after green before the work is reported done.
7. `noootwo-code-health` Release Check once before release or a ship-readiness submit gate: full suite or CI for the exact commit, full Structure Sweep, release evidence, and named gaps.
8. `noootwo-release` after code-health readiness when versioning, tagging, artifact identity, deployment trace, rollback, or release health is in scope.
9. `noootwo-state` after behavior, state, release facts, or instructions change, including unresolved structural findings and the Release Plan.

Do not turn this into a large condition table. If the current evidence points to a different owner, the evidence wins.

## Scope

- Default scope is the current change or current diff.
- Integration Read is a design decision before behavior changes, not a full-project audit; a local change with an obvious seam and no contract, data, or migration impact skips it.
- Change Check stays on the touched path; a full-project Structure Sweep runs in the Release Check, on a documented trigger, or on an explicit user request.
- Do not run a Release Check after every requirement. A long task or a large diff does not by itself trigger one; blast radius does. Existing CI for the exact commit can satisfy the full-suite part.
- A specialist may hand back a sequencing decision to workflow; record it in state rather than reimplementing the specialist.
- An installed external skill owns its method, not the project's documentation layout. Persist durable artifacts through `noootwo-state`; never create a new project convention under an external skill's directory.

## Stop conditions

Stop and ask or reroute when:

- no clear owner exists
- a material product, architecture, or release choice is unresolved
- verification is missing and cannot be inferred
- the change would expand public behavior beyond the user's request
- three failed fixes reveal new problems in different places
- user acceptance is required before commit, push, tag, or publish

For external installed skills, stop with one or two candidates when matching is ambiguous; do not choose one on a weak keyword match.
