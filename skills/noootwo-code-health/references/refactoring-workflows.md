# Refactoring Workflows

The healthy-cycle model distilled from Martin Fowler's *Refactoring* (2nd edition), the online catalog, and the workflows of refactoring material. It is the philosophy the review gate follows.

## First Principle

- **Refactoring (noun)** — a change to internal structure that makes code easier to understand and cheaper to modify without changing observable behavior.
- **Refactoring (verb)** — restructuring by a series of small, behavior-preserving transformations.
- A refactoring is deliberately small, often too small to be worth doing alone. A sequence of them produces a significant restructuring.
- The system stays working after every step. It must not be broken for hours or days while a large restructuring happens.
- Refactoring is a disciplined technique, not a synonym for restructuring, cleanup, rewriting, or a long-lived branch with red tests.
- The point is economic: refactoring pays for itself by making later changes faster and cheaper. If there is no credible payback, do not refactor it.

## Two Hats

Wear one hat at a time.

| Refactoring hat | Adding-function hat |
| --- | --- |
| small behavior-preserving transformations | behavior change, new tests, or changed contracts |
| starts from a green test baseline | may add tests and make tests fail |
| a failing test means the refactoring step is wrong | a failing test is expected during red |
| no new feature is smuggled in | no unrelated cleanup is bundled in |

Switch hats frequently when the work calls for it, but never wear both at once. In the TDD loop, red and green are the adding-function hat; the refactor step is the refactoring hat. After every refactoring step, the baseline returns to green.

If the behavior has no credible automated proof, the refactoring hat cannot be worn safely. Add the test first through `noootwo-tdd`, or record an explicit verification gap in place of pretending the refactor is proven.

## The Six Workflows

| Workflow | Trigger | What it does | Boundary |
| --- | --- | --- | --- |
| TDD Refactoring | a behavior change is green | use the post-green moment to improve the structure that the change exposed | the test loop stays owned by `noootwo-tdd`; the structural move follows `refactoring-loop.md` |
| Litter-Pickup Refactoring | you are already working in messy code | make a small improvement while you are there; leave the code better than you found it | do not turn it into a full cleanup; stop before the yak shave |
| Comprehension Refactoring | you had to work to understand what the code does | move that understanding into names, functions, and boundaries so the next reader does not rebuild it | clarify behavior you have evidence for; do not invent a new model |
| Preparatory Refactoring | the current structure makes the desired change hard | make the change easy, then make the easy change | stay behavior-preserving; do not start the feature until the preparatory step is green |
| Planned Refactoring | a larger area needs dedicated attention | give a known problem a bounded, planned pass with a rough end-state | planned-only refactoring is a smell; it means the daily workflows are not happening enough |
| Long-Term Refactoring | the restructuring spans iterations or months | agree on a rough end-state and rough plan, then move toward it through ordinary work | keep the system working; use Branch by Abstraction or another safe interim structure |

This is a cycle, not a menu. Preparatory refactoring comes before a hard change; TDD refactoring comes after green; litter-pickup and comprehension refactoring happen whenever the code is being touched; planned and long-term refactoring handle the work that cannot honestly fit in one touch.

## Code Smells

A code smell is a surface indication that usually corresponds to a deeper problem. It is quick to spot, it is not automatically a defect, and some smells are fine in context.

- Use smells to start an investigation, not to justify a mechanical rewrite.
- The deeper question is always: does this structure make the next real change harder, riskier, or more expensive?
- Common signals include long functions, large modules or classes, duplicated logic, long parameter lists, divergent change, shotgun surgery, feature envy, data clumps, primitive obsession, repeated switches, speculative generality, dead code, and comments that explain code that should be clearer.
- Repository-level smells include directory sprawl, import cycles, unclear ownership, duplicated truths, test gaps, config/doc drift, and files that force unrelated context to load.

## Catalog As Vocabulary

Use the catalog to name transformations, then choose the smallest one that resolves the real pressure. The online catalog is at `https://refactoring.com/catalog/`; these are the high-frequency moves:

- Extract Function, Inline Function, Extract Variable, Inline Variable
- Change Function Declaration, Encapsulate Variable, Move Function, Move Field
- Introduce Parameter Object, Combine Functions into Class, Combine Functions into Transform, Split Phase
- Replace Nested Conditional with Guard Clauses, Replace Conditional with Polymorphism
- Replace Loop with Pipeline, Replace Primitive with Object, Separate Query from Modifier
- Remove Dead Code, Remove Middle Man, Replace Subclass with Delegate

Named moves are shared vocabulary, not a mandate to apply the whole catalog. One concept per step; run the relevant tests after each step.

## Structural Health

Review starts with the current change, but it must not become blind to structure. Look for structural pressure in this order:

1. The code touched by the current change.
2. The nearest callers, tests, public interface, and module boundary.
3. The same concept implemented more than once.
4. The touched area already causing repeated edits, context cost, or review confusion.
5. Repository-level debt only in a triggered Structure Sweep or when release risk makes it relevant.

Structural evidence includes file and function size, directory depth, ownership, import direction and cycles, fan-in/fan-out, duplication, dead exports, test gaps, duplicated config or docs, and the amount of unrelated context a future agent must load.

## Debt Ledger

Do not turn every smell into a refactoring backlog. Record only what cannot be safely resolved in this pass, and give each item a different disposition:

| Disposition | Meaning | Next move |
| --- | --- | --- |
| opportunity | noticed in an area that is likely to be touched again | revisit when that area is next changed; do not schedule a ceremony for it |
| planned | a larger area needs dedicated attention | schedule a bounded planned-refactoring pass |
| long-term | one pass cannot reach the end-state | record the rough end-state and move toward it through ordinary work |
| accepted | stable, rarely touched, and not worth the investment now | record the reason and the condition that would reopen it |

Persist the ledger through `noootwo-state`; do not create a private review file. The ledger is memory, not a tax on every change.

## When Not To Refactor

- The area is stable, rarely changed, and the payback is not credible.
- There is no test or other behavior evidence and the test cannot be added safely yet.
- The only reason is taste, naming preference, or a hypothetical future variant.
- The change would mix behavior change with cleanup.
- The plan is a big-bang rewrite that keeps the system broken for a long time.

These are not reasons to ignore the problem. They are reasons to record an accepted risk, an opportunity, or a long-term direction instead of forcing a refactor now.

## Applying It In Review

- Before implementation: if the structure blocks the change, invoke the preparatory workflow and make the change easy first.
- After green: switch to the refactoring hat, use TDD, litter-pickup, and comprehension workflows on the touched code.
- Before reporting done: every finding is fixed now, scheduled with a trigger, or accepted with a reason.
- Before release: run a Structure Sweep, resolve or disposition the debt that could break safe change, and keep the system working.
