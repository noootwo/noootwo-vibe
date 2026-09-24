# 0016 — Rename review to code-health

## Status

Accepted.

## Context

The review skill now owns a continuous health loop: change review, preparatory
and post-green refactoring, structure sweeps, structural dispositions,
optimization, project health, and acceptance. The name `review` describes only
one mode and pulls the model toward reviewing the current diff instead of
maintaining the codebase over time.

The user's preferred language for the outcome is "优雅" (elegant), but elegance
is a goal rather than a routing boundary. It is subjective and does not describe
the loop, the evidence, or the gates.

## Decision

- Rename `noootwo-review` to `noootwo-code-health`.
- Use `Noootwo Code Health（优雅代码）` as the display name.
- Put "elegant" and "healthy" in the description as trigger language, while the
  skill name remains the operational owner of the loop.
- Continue the version line at `0.14.0`; keep `noootwo-review@v0.13.0` and
  `docs/releases/noootwo-review.md` as history.
- Update current routing, capability map, sibling references, tags, and release
  notes. Historical ADRs and experiment records may keep the old name.

## Consequences

- The skill name now describes the capability rather than one moment in its
  lifecycle.
- "Elegance" remains a user-facing goal and trigger word without becoming a
  subjective gate.
- Every current reference to `noootwo-review` becomes a broken bridge; the
  rename release updates them together and records the old name as historical.
