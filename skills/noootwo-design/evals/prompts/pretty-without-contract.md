# Eval Prompt: Pretty Without Contract

Use `$noootwo-design` on a visually appealing mockup that has no implementation-ready Design Contract.

Expected behavior:

- Refuse to treat attractive prose or a single image as implementation-ready.
- Produce or request a Design Contract with structure, type scale, color/token roles, component behavior, state treatment, motion, anti-slop risks, and artifact/review path.
- Identify which decisions must become semantic tokens or component rules.
- Route to implementation only after the contract and plan exist or the user explicitly skips the gate.

Failure signals:

- Hands off style adjectives as if they were build instructions.
- Omits state behavior, token roles, or artifact review path.
- Lets implementation invent the design system from the mockup.
