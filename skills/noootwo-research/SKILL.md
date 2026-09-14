---
name: noootwo-research
description: "Use when a decision needs evidence that only exists outside the repo: a design direction, a stack or library choice, a competitor or user expectation, or prior art. Extract mechanisms, not surfaces."
---

# Noootwo Research

Settle a decision with evidence from outside the repository, or say plainly that the evidence does not settle it. Research unblocks a decision; it does not produce reading notes.

Not every unknown is a research task. Read the repo, config, docs, and code first — a fact already written down is a lookup. Research starts when the answer only exists outside.

## 1. Name the decision

```
Decision:   <the choice this unblocks>
Would flip: <what evidence would change the answer>
Not enough: <what would leave the decision unchanged>
```

No decision named means no research. "Learn about X" is not a decision; "which of these two libraries do we adopt" is.

**Done when:** the decision and what would flip it are written down.

## 2. Size it

- `quick` — a directed lookup, one or two sources. One sentence plus the source, in the conversation, no file.
- `standard` — a real comparison across several sources. An evidence brief in the conversation, no file.
- `deep` — a high-cost or high-risk decision, a direction already rejected, or a claim you will publish. Write `.noootwo/research/<slug>.md` and require visible artifacts.

Size by the cost of being wrong, not by how interesting the question is.

**Done when:** the dial is named and its proof of done is stated.

## 3. Frame the queries

Derive three to six queries that separate the candidates instead of describing the topic: by product type, task, platform, audience, constraint, and the anti-pattern being avoided.

Then fan out — breadth across independent sources first, depth into the two or three that survive. Read `references/research-method.md` for the query pattern, the breadth and depth discipline, and the follow-up rule.

**Done when:** the query set is written, and each query maps to a candidate or a constraint.

## 4. Find the sources

Read `references/source-pools.md` for the pool matching the domain: design and UI, product and market, tech stack and libraries, or community signal. Prefer, in order: official docs and platform guidance; a running artifact, repository, screenshot, or benchmark; a credible hands-on report; community discussion with a visible artifact; a single post.

Record the access result when a pool is unreachable, and use the fallback ladder rather than skipping the pass.

**Done when:** every deciding claim traces to a named source with an evidence level, or is marked as not found.

## 5. Extract mechanisms, not surfaces

For each source, record the mechanism, why it transfers, its boundary, and what must not be copied. A source is useful when you can say what it does, not what it looks like.

For a stack or library decision, read `references/tech-selection.md` and score the candidates on adoption, maintenance health, size and performance, licence, API fit, migration cost, and the honest alternative of choosing the boring option.

**Done when:** each finding names a repeatable mechanism, its applicability, and its boundary.

## 6. Verify

- Two independent sources for any claim that decides something; one source is a lead.
- Recency matters for "current", "popular", and "advanced" claims; record the date of the evidence.
- A screenshot, repository, artifact, benchmark, or running example beats prose describing one.
- Hunt the counterexample: a case where the mechanism fails, or a well-regarded project that rejected it.
- Weak signals — one post, a moodboard, a trend essay — may suggest a direction and never decide one.

**Done when:** deciding claims have two independent sources, and each has its counterexample recorded or explicitly absent.

## 7. Record

- `quick` and `standard` — one brief in the conversation: decision, finding, sources with evidence levels, the mechanism, the boundary, the counterexample, the confidence, and what would change the answer.
- `deep` — the same brief at `.noootwo/research/<slug>.md`, plus the visible artifacts and the sources that were unreachable.

Confidence is `high`, `medium`, or `low`. Missing visual or artifact evidence caps confidence at `low`, and a `low` finding does not become a contract or an implementation plan.

**Done when:** the brief exists in the right place with its evidence levels and its confidence.

## 8. Survey prior art

While in the sources anyway, check whether an existing skill already solves this better. Read `references/borrow-audit.md`: it covers comparing the local skill set and well-regarded public skills, the four-part adoption gate, and the do-not-copy list.

Adopt only what prevents a repeated, concrete failure, fits the budget, keeps the cheap mode cheap, and becomes a checkable rule or eval. Record rejections with their reason.

**Done when:** each candidate mechanism is adopted, rejected with a reason, or recorded as a proposal.

## 9. Hand off

Report the finding and its boundary. When the decision is a product decision, invoke the `noootwo-product` skill: read its `SKILL.md` and follow it. When the finding changes a durable fact, invoke the `noootwo-docs` skill to place it. When it changes a visual direction, invoke the `noootwo-design` skill.

When the request is not research at all — a local lookup, a bug, or an implementation — say so in one line and re-route instead of running a pass.

**Done when:** the finding is delivered, its boundary is stated, and the owning skill is invoked or recorded as not applying.

## Reference

- `references/research-method.md` — question framing, query fan-out, breadth and depth, the evidence ladder, verification, and anti-patterns.
- `references/source-pools.md` — where to look by domain, the fallback ladder, and the access record.
- `references/tech-selection.md` — evaluating libraries and stacks, and when to choose the boring option.
- `references/borrow-audit.md` — comparing existing skills and public prior art, the adoption gate, and the do-not-copy list.
