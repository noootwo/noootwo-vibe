# 0019 — Systemic Close After A Proven Debug Fix

## Status

Accepted.

## Context

`noootwo-debug` proved the current cause, bounded the fix, and verified it, but its close ended at the local repair. Real debugging repeatedly showed the same limitation: the immediate cause was fixed while the conditions that allowed it remained invisible. Sibling paths, near-miss paths, missing controls, and recurring classes were discovered later or not at all.

Fixing the instance is single-loop correction. The system also needs to ask why the system allowed the defect, why existing controls missed it, where the same condition remains, and which governing rule or barrier should change if the class returns.

## Decision

1. Add a `Systemic Close` as Step 8 of `noootwo-debug`; Step 7 closes the incident and places immediate handoffs. The final answer reports both the local proof and the systemic result.
2. Use eight ordered questions: what failed, how it failed, why it happened, why it was not caught, where else it exists, which near-miss or fragile success shares it, which recurrence barrier will stop it, and how the system will learn if it returns.
3. Separate mechanism, failed control, and learning layers. The evidence chain still owns the mechanism; a Systemic Close may not reopen Gate A without contradicting evidence.
4. Require sibling and near-miss search with a named search scope, and permit `no credible latent path` only as an evidenced disposition.
5. Make prevention proportional to severity, recurrence, and reach. A trivial one-off records disposition and stops; a repeated or high-impact class requires a real barrier, owner, verification, and learning-loop change.
6. Route structural work to `noootwo-code-health`, durable facts to `noootwo-state`, and release controls to `noootwo-release`. The debug skill owns the analysis, not an unbounded refactor.
7. Record the academic basis in `references/systemic-prevention.md`: Reason's latent conditions and defenses, Leveson's STAMP control model, Argyris's double-loop learning, Google SRE's blameless postmortem and preventive action, and Hollnagel's Safety-II view of successful performance and variability.

## Consequences

- A proven local fix is no longer the whole debug result. The skill must show whether the class can return and what evidence supports that claim.
- The default loop gains one analysis step, but its cost is scaled: a trivial isolated defect may produce a short `no credible latent path` close.
- The skill becomes better at preventing recurrence and discovering unexposed paths, at the cost of a larger close report for repeated or high-impact failures.
- Action items without an owner, verification, or disposition are explicitly not barriers.
- The public skill set, capability ownership, and the existing Gate A/Gate B model do not change.
