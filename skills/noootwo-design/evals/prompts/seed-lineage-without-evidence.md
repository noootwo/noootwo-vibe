# Eval Prompt: Seed Lineage Without Evidence

Use `$noootwo-design` when the response picks a style lineage such as Quiet Luxury Product or Precise Minimalism and treats it as the evidence for a high-character direction.

Expected behavior:

- Treat the lineage as a starting point, not as evidence.
- Find a real reference, a design system, or a running artifact before trusting the direction.
- Take the lineage's motion archetype from `references/motion.md`, and record it with the direction.
- Mark confidence low and require a spike when no visual evidence exists.

Failure signals:

- Ships the direction on the strength of the lineage name alone.
- Names an archetype but never records the duration scale or signature curve.
- Produces a direction whose only justification is that it matches a seed.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals.
