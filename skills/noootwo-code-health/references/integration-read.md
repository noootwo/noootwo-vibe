# Integration Read

Use this before implementation when the change's shape is not obvious. The output is a compact **Change Shape**: where the change enters the existing code, what stays stable, and what the smallest honest first step is.

This is a design decision, not a design document and not an implementation manual. It exists to make the later TDD loop cheap and to keep the change reversible.

## Run or skip

Run the read when one or more is true:

- the user asks how a requirement should be implemented, including backend design or frontend integration;
- the change crosses a module, package, service, layer, or frontend/backend boundary;
- it adds or changes a public interface, API, event, shared type, schema, migration, or data owner;
- several callers, teams, or surfaces depend on the area;
- it introduces a dependency, platform feature, background process, or infrastructure;
- the existing structure makes the requested change hard;
- the smallest first behavior slice is not clear.

Skip it when the change is local and the seam is obvious, with no contract, data, or migration impact. Also skip the code-shape branch when the blocker belongs elsewhere:

- product behavior or acceptance is unsettled -> `noootwo-product`;
- UI direction or visual language is unsettled -> `noootwo-design`;
- the cause of a failure is unproven -> `noootwo-debug`;
- the answer exists only outside the repository -> `noootwo-research`.

## Read the current shape

Read the smallest evidence that can change the decision:

- the nearest modules, callers, and tests;
- public interfaces, events, shared types, schemas, and data ownership;
- existing patterns that already solve a similar problem;
- validation commands and the closest executable proof;
- constraints from `AGENTS.md`, ADRs, specs, `docs/status.md`, or release state;
- the design or product handoff when one exists.

Name the current behavior that must stay true before proposing a new one.

## Change Shape

Keep the output short enough to review in one pass. For a small change, a handful of lines is enough.

```markdown
Change Shape

Intent and invariants
- what must become true, and what must not break.

Seam and ownership
- where the change enters; which module, service, or layer owns it; what stays stable.

Contracts
- interface, data, event, schema, migration, and compatibility changes.

Reuse
- existing patterns or abstractions to use; any new concept and the current pressure that justifies it.

Reversibility
- one-way doors, rollout or fallback path, and what can be deferred.

Test seam
- where TDD proves the behavior, including the boundary or integration proof.

First slice
- the smallest behavior change and the condition for stopping before the next slice.

Rejected
- alternatives considered, or why no real alternative existed.
```

A Change Shape can end in direct TDD, a preparatory refactor, a product/design/research handoff, or a decision to stop. If it contains a material, hard-to-reverse, or competing technical tradeoff, present the smallest set of options with a recommendation and wait for the user's choice before TDD. A reversible, low-risk shape can proceed. The shape changes no behavior by itself.

## Sizing

- Small: keep the shape in the conversation; do not create a document.
- Medium or cross-session: invoke the `noootwo-state` skill so the next owner can read it: read its `SKILL.md` and follow it.
- Risky or one-way door: invoke the `noootwo-state` skill for an ADR or the owning decision record: read its `SKILL.md` and follow it; include the rejected alternatives and the evidence.
- If the shape has no real tradeoff and an obvious implementation, do not write it down; proceed to TDD.

## Boundary

- `noootwo-product` owns what should exist and for whom.
- `noootwo-design` owns the visual and interaction system when direction is unsettled.
- `noootwo-research` owns decisions that only outside evidence can settle.
- `noootwo-code-health` owns the software shape: seam, ownership, contracts, reuse, reversibility, and test seam.
- `noootwo-tdd` owns the failing test and the smallest implementation at the chosen seam.
- `noootwo-state` owns where a durable shape or decision is stored.
- `noootwo-release` owns version, artifact, deployment trace, rollback, and release health.

## Failure modes

- **Big design up front**: producing a broad architecture before the first slice. Keep the shape tied to the current requirement.
- **Speculative generality**: adding extension points or abstractions for future features that are not yet needed.
- **Diagram theater**: drawing boxes instead of naming the seam, contract, owner, and test.
- **Implementation manual**: writing code-shaped steps instead of decision-shaped constraints.
- **No rejected option**: if no alternative existed, say so; if alternatives existed, record why they lost.
- **Over-triggering**: running the read for a local, obvious change and slowing the work without changing the decision.

## Evidence basis

This method combines four mechanisms:

- evolutionary design still contains planned design before a particular task, and favors reversible decisions (Martin Fowler, *Is Design Dead?*, 2004);
- preparatory refactoring makes a hard change easy before the behavior change (Martin Fowler, *Workflows of Refactoring*, 2014);
- design documents identify design issues while they are cheap and compare alternatives, while mini design docs cover incremental improvements; skip them when the solution is obvious (Design Docs at Google);
- seams and design for testability let behavior change without editing it in place (Michael Feathers, *Working Effectively with Legacy Code*, 2005).

The counterexamples are explicit: YAGNI rejects speculative features, and Google's design-doc guidance rejects documentation when there is no real tradeoff or when the doc is only an implementation manual.
