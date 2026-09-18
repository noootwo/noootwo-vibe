# Eval: Motion probe for a dead stretch

Prompt: "This page feels like it has a long dead stretch in the scroll animation. Tell me whether the problem is the easing curve."

Expected:

- The agent does not change the curve before evidence.
- It uses `scripts/extract_design_tokens.mjs --probe-motion <selector>` when the page is reachable, or records the limitation.
- It reports stillness ratio and observed duration.
- It explains that a high stillness ratio is a timeline problem, not an easing problem.
- The motion finding remains advisory until a screenshot or DOM review confirms it.

Fails when: it changes the easing curve without sampling; it claims a dead stretch is fixed by a softer spring; it makes the probe a hard readiness gate.
