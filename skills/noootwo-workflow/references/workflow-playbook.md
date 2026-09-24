# Workflow Playbook

Compact guardrail and handoff packet reference. Routing and scheduling live in `route-by-signal.md`, `workflow-state.md`, and `orchestration.md`.

## Lightweight guardrails

- Read repo truth before deciding; smallest read that covers risk.
- Do not edit while product or debug is unresolved.
- Behavior-changing code uses `noootwo-tdd` before review.
- Non-direct behavior changes return to `noootwo-code-health` after green, before the work is reported done.
- Review/refactor/optimization must re-run tests, dispose of structural findings, and stop for user acceptance before submit or publish.
- Update docs through `noootwo-state` when facts change.
- Direct single-file work stays direct; do not add ceremony.

## Handoff packets

Keep packets short. Workflow carries scope and sequencing; the specialist owns method.

### To `noootwo-tdd`

- Behavior to change:
- Current test command:
- Scope boundary:
- What workflow still owns:

### To `noootwo-code-health`

- Behavior or structure changed:
- Files and nearest tests:
- Risk class:
- Refactoring workflow considered: preparatory | TDD | litter-pickup | comprehension | planned | long-term
- Verification command:
- Structural findings and disposition:
- Refactor/acceptance state:
- Specific judgment requested:

### To `noootwo-debug`

- Symptom and raw failure:
- Expected vs actual:
- Reproduction command or steps:
- Environment or boundary suspected:
- What changed since it last worked:

### To `noootwo-product`

- Raw product idea:
- Real user or suspected user:
- Unclear product choice:
- Current flow or artifact evidence:
- Acceptance or state question:

### To `noootwo-design`

- UI/artifact surface:
- Real user and scenario:
- Main path:
- States and acceptance:
- Current design evidence:
- Direction uncertainty:
- Reviewable artifact path:

### To `noootwo-state`

- Changed fact:
- Fact type: state | event | decision | narrative | release | evidence | procedure
- Query profile: field | tail | search | human
- Mutability: current | append-only | immutable
- Lifespan: hot | durable | cold

### To `noootwo-research`

- Decision this unblocks:
- What would change the answer:
- Domain:
- Cost dial: quick | standard | deep
- Constraints:
