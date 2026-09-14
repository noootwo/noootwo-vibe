# ADR 0008: Add Research And Onboard Skills, Keep Performance In Review, And Build The Capability Bridge

- Status: accepted
- Date: 2026-09-14

## Context

Three pressures met in the same week.

**Research was real but trapped.** `noootwo-design` already carried a deep research machine — source standard, fallback ladder, source registry, agentic style discovery, fit scoring, and a `.noootwo/style-discovery.md` contract. It was design-only, and it fired only when a human asked for it or when `AGENTS.md`'s design-specific rule applied. Tech-stack and market research had no home at all, so the same work was re-explained every time.

**The scheduler still did work.** [ADR 0007](0007-add-debug-skill-and-normalize-workflow.md) declared `noootwo-workflow` a scheduler, but its `onboarding` mode carried a 242-line procedure across three references. Reading them showed a second problem: `project-foundation-check.md` audited agent entry, README, status, ADRs, releases, validation, tests, CI, versions, and risk — the same surface as `noootwo-review`'s `project-health-review.md`, with a different output contract. One fact, two owners, which is the `truth drift` defect the review lens itself exists to catch.

**Optimization mis-routed.** `noootwo-debug`'s description claimed "slower than expected", so "make this faster" entered a flow whose gate demands a reproducible failure and a proven cause. But `AGENTS.md` and [ADR 0005](0005-add-product-skill-and-keep-architecture-as-review-lens.md) already assign performance to `noootwo-review`, and the wider ecosystem agrees: `obra/superpowers` ships fourteen skills and none of them is a performance skill, while the standalone performance skills in the ecosystem are domain packs (WordPress, Core Web Vitals, scroll jank) rather than a general optimization capability. `noootwo-review` had a performance *lens* — judging risk — but no optimization *loop*.

**The bridge was prose.** Cross-skill calls existed only as sentences inside bodies. Nothing stated what a caller hands over, what it gets back, what it keeps, or what happens when two skills call each other. Real cycles existed (`design ↔ review`, `docs ↔ design`) with no re-entry rule, and one `noootwo-docs` instruction invoked three skills at once, against the invocation model's own one-skill-per-instruction rule.

Research pass, 2026-09-14: `obra/superpowers` (including `using-superpowers`, which packages "how to operate this suite" as its own skill rather than hiding it in a router), `pbakaus/impeccable`, `mattpocock/skills`, `dzhng/deep-research` (breadth and depth control, follow-up recursion), `mvanhorn/last30days` (recency window, multi-source aggregation, engagement weighting), `anthropics/skills`, and the installed local pool. The mechanisms were extracted; wording, prompts, and surfaces were not.

## Decision

1. Add `noootwo-research` as the eighth public skill. It fires when a decision is blocked by something only outside evidence can settle, names the decision and the evidence that would flip it, sizes the pass into `quick` / `standard` / `deep`, and owns the shared source pools. It extracts mechanisms rather than surfaces, requires two independent sources and a counterexample before a claim decides anything, and records confidence so a `low` finding cannot become a contract.
2. Add `noootwo-onboard` as the ninth public skill, and decompose the old onboarding: the foundation health surface merges into `noootwo-review`'s project-health lens, while the skill audit and the minimal foundation templates become the new skill. This follows `using-superpowers`: a capability about operating the suite belongs in its own skill, not inside the scheduler.
3. Keep performance and optimization in `noootwo-review`. Add `references/optimization-loop.md` and the trigger words, and correct `noootwo-debug`'s boundary so a regression goes to debug and an improvement goal goes to review. No performance skill is added.
4. Migrate design's research in layers: the method and source pools move to `noootwo-research`, the aesthetic discovery flow stays in `noootwo-design` as `references/design-discovery.md`. The `.noootwo/style-discovery.md` and `.noootwo/reference-board.md` contract is frozen — four design scripts read those files field by field.
5. Build the capability bridge. `docs/agents/invocation.md` carries the capability map, the call contract, the loop rules, and the shared-material rule. Every skill body gets a one-hop return rule. `scripts/validate_skill_workspace.py` enforces the mechanical half: a skill named in a body must exist, every public skill must appear in the capability map, and every skill named in the map must exist.
6. Every research pass also runs a borrow audit against the local skill set and well-regarded public skills, behind a four-part adoption gate: it prevents a repeated concrete failure, it fits the budget, it keeps the cheap mode cheap, and it becomes a checkable rule or eval. Structural proposals become ADR candidates rather than same-pass changes.

## Consequences

- The suite carries two more always-loaded descriptions, about 380 characters total, in exchange for two distinct triggers that fire without the scheduler running first.
- `noootwo-workflow` drops to a single reference and stops duplicating the health surface; `noootwo-review` grows to absorb it.
- `noootwo-debug` sits at 117 of its 120 lines, so its boundary sentence went into an existing paragraph rather than a new section.
- The bridge is enforced at the name level only. Ordering, hand-off content, and the loop rules stay review questions, recorded in `docs/status.md` as an honest limit.
- `noootwo-research` and `noootwo-onboard` are written from a research pass, not from a measured behaviour probe. Until the eval scenarios under each skill run and are recorded, no claim is made that they change agent behaviour.
- The `AGENTS.md` design-specific rule became a general research rule, so design, workflow, stack, review-gate, and public-claim changes all route through one owner.
