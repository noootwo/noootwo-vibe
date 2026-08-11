# ADR 0002: Optimize non-design skills around control contracts

- Status: accepted
- Date: 2026-07-03

## Context

Noootwo Vibe's first public non-design skills established the four-skill model but were still skeletal. The next iteration needs to improve AI development efficiency without making every invocation load long manuals. Research across mature local skills and external practice showed the strongest reusable mechanisms are precise triggers, hard gates for fragile work, concise default instructions, focused reference files, explicit review/output contracts, and fresh verification evidence.

## Decision

Optimize `noootwo-workflow`, `noootwo-docs`, and `noootwo-review` to `v0.2.0` without changing `noootwo-design`. Keep each `SKILL.md` concise and move deeper guidance into one direct reference file per skill. Add clearer task modes, documentation ownership rules, code-health risk classes, AI-code risk checks, handoff packets, and stop conditions.

## Consequences

- Default skill invocations stay lightweight while complex tasks have stronger guidance on demand.
- Workflow, docs, and review now produce more explicit handoffs and verification expectations.
- At this decision point the public skill set remained four skills, and Noootwo Design remained unchanged; ADR 0005 later added `noootwo-product` as the fifth public skill.
