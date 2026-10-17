# 0018 — Contextual Design Intervention Before Motion Or Decoration

## Status

Accepted.

## Context

The design skill had a developed motion language, source pools, and artifact review, but its entrypoint still made motion feel like a neutral finishing layer. In real use, that produced two failures:

- ordinary product work rarely triggered source-backed motion or visual exploration; and
- the correction risk was over-animation, where the model would add effects, shaders, or vendors to every surface to prove effort.

The product function and moment determine whether a design should stay simple, receive craft-only work, or earn an authored move. High-frequency keyboard flows, dense data surfaces, settings, and maintenance tasks often become worse when expression is added. First use, completion, explanation, launch, and brand moments may justify more. Neither restraint nor expression is universally correct.

## Decision

1. Make `leave simple`, `craft only`, and `add moment` first-class outcomes of the Design Read and Design Contract.
2. Run the opportunity sweep only when the intervention decision surfaces a relevant candidate. Quick polish and local maintenance do not pay the cost.
3. Apply four gates before source research, a library, or an authored move: frequency, purpose, speed, and function. Record rejected candidates.
4. Require `add moment` to name one primary move, at most one support, a source or platform rule, and a fallback. Component-library defaults do not count as the authored move.
5. Require `leave simple` and `craft only` to show craft-sufficiency evidence and why more expression would not improve the task.
6. Keep Shaders, Paper Shaders, sound, and haptics optional material choices after a candidate passes. Paid Shaders services are never required.
7. Make review verify the intervention decision before judging motion or material. A justified absence of an authored move can be `ready`; an unsupported `add moment` cannot.
8. Give explicit user intent precedence over the product heuristic. A request for motion, animation, liveliness, fancy, a named library, or shader/material rendering defaults the requested scope to `add moment`; `leave simple` or `craft only` requires the user to accept no authored motion. Every `add moment` records its implementation tool, and an installed or user-named library must be selected, replaced by a recorded equivalent, or rejected with a concrete reason.

## Consequences

- The skill now has a governed way to be bold without turning boldness into a universal default.
- A user who explicitly asks for motion can no longer receive a zero-motion `craft only` result without consent; installed and user-named libraries are evaluated rather than silently omitted.
- Motion, shader, and sensory-material guidance becomes cheaper in ordinary work because no source search or new dependency starts before a candidate survives.
- Existing motion contracts remain for `add moment`; `leave simple` and `craft only` are validated through intervention rationale and craft evidence instead of fabricated motion values.
- Artifact and readiness validation gain intervention fields and contextual eval scenarios. Existing in-flight projects using `--motion-gate` must record an intervention decision before they can pass again.
- The public skill set and capability ownership do not change.
