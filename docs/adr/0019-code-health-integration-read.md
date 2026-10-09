# 0019 — Code health shapes non-obvious changes before implementation

## Status

Accepted.

## Context

`noootwo-code-health` already owned preparatory refactoring, but only when the
existing structure was known to make a change hard. The first implementation
shape — where a backend behavior belongs, how a frontend consumes it, which
interface or data owner changes, what stays stable, and what the smallest first
slice is — was therefore decided implicitly inside TDD or implementation.

That produced the failure this decision addresses:

- backend and frontend integration decisions were made at code-write time;
- new abstractions appeared before the existing seam had been read;
- contracts, migration, reversibility, and test seams were discovered late;
- the review pass could judge the result but could not prevent avoidable rework;
- and the model had no stable instruction to reach code-health when the user
  asked "how should this be implemented?" rather than "review this diff".

Architecture already lived inside code-health as a lens. The missing piece was
the lifecycle position: code-health needed a bounded entry before implementation,
not a new public architecture skill.

## Decision

1. Add the **Integration Read** as a code-health mode before implementation when
   a change's seam or integration shape is non-obvious.
2. Produce a compact **Change Shape** instead of a full design document:
   intent and invariants, seam and ownership, interface/data/event contracts,
   reuse, reversibility and compatibility, test seam, smallest first slice, and
   rejected alternatives or why none existed.
3. Trigger the read for cross-boundary or contract-bearing changes, migrations,
   new dependencies, multiple callers, hard existing structure, or an unclear
   smallest first step.
4. Skip the read for an obvious local change with no contract, data, or migration
   impact. A local change proceeds directly to TDD.
5. Let the Change Shape end in direct TDD, a preparatory refactor, a product,
   design, or research handoff, or a stopped change. A material,
   hard-to-reverse, or competing technical tradeoff is presented with a
   recommendation and waits for the user's choice; a reversible low-risk shape
   can proceed. The shape changes no behavior by itself.
6. Schedule the read through `noootwo-workflow`: code-health/shape before TDD
   when the seam is non-obvious, then code-health/review after green.
7. Make TDD return to workflow when the implementation shape or seam is
   unsettled; TDD does not invent architecture inside the red-green loop.
8. Keep architecture, integration design, seams, test strategy, maintainability,
   performance, and optimization inside code-health. Do not add a separate
   architecture skill.
9. Persist a durable or risky Change Shape through `noootwo-state`; keep small
   shapes in the conversation.

## Evidence brief

The decision was settled through a `deep` research pass. Search engines were
bot-challenged or returned unusable results, so the deciding evidence came from
direct primary or official pages, accessed on 2026-10-09.

- Martin Fowler, *Is Design Dead?* (May 2004) states that evolutionary design
  still has room for designing before coding, and that most of that design
  happens in the iterations before a particular task. It also argues for
  reducing irreversibility: defer a decision or make it reversible instead of
  trying to get every decision right now. This is the strongest direct support
  for a pre-implementation, reversible Change Shape.
- Martin Fowler, *Workflows of Refactoring* (8 January 2014) separates
  preparations from the behavior change: make the change easy, then make the
  easy change. Code-health already had preparatory refactoring, but the read
  that decides whether it applies was missing.
- Martin Fowler, *Branch By Abstraction* (7 January 2014) and *Strangler Fig*
  (22 August 2024) provide repeatable mechanisms for integrating change into an
  existing system gradually while the system keeps working. These support the
  seam, ownership, compatibility, and first-slice fields.
- Michael Feathers, *Working Effectively with Legacy Code* excerpt (21 January
  2005) frames seams and design for testability as the way to change behavior
  without being trapped by the current structure. This supports making the test
  seam an explicit output.
- Google Engineering Practices, *What to look for in a code review* (accessed
  2026-10-09) says the most important review concern is the overall design:
  whether interactions make sense, where the change belongs, and whether it
  integrates well with the rest of the system. Code-health already owned that
  judgment; this decision moves a cheap version of it before the code exists.
- Design Docs at Google (accessed 2026-10-09) documents the mechanism and the
  boundary: design documents identify design issues while changes are still
  cheap, compare trade-offs and alternatives, and can be mini documents for
  incremental improvements. It also says to skip a design document when the
  solution is obvious, has no real trade-off, or the document would be only an
  implementation manual.
- Thoughtworks Lightweight Architecture Decision Records (Radar update, 15 May
  2018) supports persisting important architectural decisions with context and
  consequences in source control when the decision is durable or risky.
- Martin Fowler, *Yagni* (26 May 2015), and *Design Stamina Hypothesis*
  (20 June 2007), set the counterexample and the confidence limit. Yagni rejects
  speculative features and abstractions; the design-stamina hypothesis is
  explicitly a hypothesis without objective proof. The decision therefore
  adopts a small, current-need read, not big design up front and not an
  architecture rewrite.
- *Is Design Dead?* also warns that evolutionary design becomes ad-hoc tactical
  decisions when no one keeps the design whole, and that the balance between
  planned and evolutionary design has not been measured. That is why the read
  is bounded, evidence-based, and paired with post-green review.

## Rejections

- **A new `noootwo-architecture` skill**: architecture already has an owner as a
  code-health lens, and a second skill would split the seam decision from the
  structure that has to preserve it.
- **A mandatory design document for every change**: the design-doc evidence and
  the existing direct-edit rule both reject that cost.
- **Product-first behavior design inside code-health**: product still owns what
  should exist and for whom; code-health shapes the software once that is
  settled.
- **Letting TDD invent the architecture**: TDD owns proof and implementation at
  a chosen seam, not the seam decision.

## Confidence

- **High**: a bounded pre-implementation integration decision belongs to
  code-health, and the existing workflow can schedule it without a new skill.
- **Medium**: the exact trigger threshold and the effect on rework are not yet
  measured. The skip rule and the positive, skip, and product-boundary evals are
  the first control.
- What would change the answer: evals showing that the read over-triggers on
  simple changes without improving integration quality, or evidence that
  product, design, and TDD already make the same seam decisions reliably. The
  response would be to narrow the trigger or move the decision back into the
  owning stage, not to add another skill.

## Consequences

- Code-health becomes a two-pass owner: shape before implementation when the
  seam is non-obvious, review after green.
- Workflow gains a pre-TDD scheduling branch and a close-gate check for it.
- TDD gains a boundary: unsettled shape returns to workflow.
- The public skill set, capability ownership, and "no separate architecture
  skill" rule do not change.
- The main remaining risk is over-triggering. The skip rule, the `Change Shape`
  output contract, and the new evals are the first guard; behavior measurement
  is still owed.
