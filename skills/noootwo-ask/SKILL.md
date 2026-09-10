---
name: noootwo-ask
description: "Find the right Noootwo skill for your situation, and the order to run them in."
---

# Ask Noootwo

You do not remember every skill, so ask.

Five skills do the work; this one tells you which to reach for. A **flow** is a path through them. Most work runs along the main flow; the rest is an on-ramp or standalone.

## The main flow: idea to shipped

1. `$noootwo-product` — settle what should exist: real user, first loop, scope, main path, states, acceptance. Run this whenever those are unclear. It ends on a shared understanding you confirm.
2. `$noootwo-design` — turn the settled product path into interface: direction, typography, colour, layout, motion, and a Design Contract. Reach for it on any UI, visual, artifact, or frontend work.
3. `$noootwo-review` — judge the code before it ships: correctness, testability, architecture boundaries, lean, performance, release readiness.
4. `$noootwo-docs` — place what changed in the owning document. Reach for it whenever behaviour, project state, release facts, or agent instructions changed.

## On-ramps

Start here, then merge onto the main flow.

- **Anything multi-step, cross-file, or risky** → `$noootwo-workflow`. It owns the loop from reading repo truth to closing out, and it invokes the other skills as their triggers arrive. Start here when you are unsure where to start.
- **Something is broken** → `$noootwo-workflow` first: establish the reproduction and root cause before reaching for a fix.
- **The last attempt was rejected** → `$noootwo-workflow`. It diagnoses which layer failed — product, design, implementation, or evidence — and routes to the skill that owns it, instead of another round of the same polish.
- **Releasing or tagging** → `$noootwo-workflow` for sequencing, `$noootwo-review` before the tag, `$noootwo-docs` for release notes.

## Standalone

- `$noootwo-product` alone, when you want the interview and nothing else.
- `$noootwo-design` alone, for a visual critique of something already built.
- `$noootwo-review` alone, to review a branch or PR against a fixed point.
- `$noootwo-docs` alone, for a documentation audit or a stale-claim cleanup.

## Choosing between two

| Situation | Reach for |
| --- | --- |
| The user or the first loop is unclear | `$noootwo-product` |
| The product path is settled and the interface is not | `$noootwo-design` |
| The code is written and needs judgment before shipping | `$noootwo-review` |
| Something changed and documents must stay true | `$noootwo-docs` |
| You are unsure, or the task spans several of the above | `$noootwo-workflow` |

`$noootwo-design` returns to `$noootwo-product` when the real user, main path, states, or acceptance turn out to be unsettled. `$noootwo-review` returns to `$noootwo-product` for behaviour choices and to `$noootwo-workflow` for sequencing.
