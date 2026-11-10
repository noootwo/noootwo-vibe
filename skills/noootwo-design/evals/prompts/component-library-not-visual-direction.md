# Eval: A component demo is implementation evidence, not art direction

Prompt: "The shadcn/ui demo looks clean. Use it as the design direction for our customer support inbox."

Expected behavior:

- Classifies the library as `implementation resource`, not `product evidence` or `visual direction`.
- Auditions a real support inbox, a data-UI product, or a platform convention for the workflow.
- Uses the library only for component anatomy, accessibility plumbing, and implementation cost after the direction is set.
- Records the default component language that must be restyled or rejected.
- Captures and inspects the primary product evidence.

Failure signals:

- Treats a clean component demo as proof of a good inbox design.
- Copies default cards, radii, shadows, and spacing as the visual concept.
- Skips real workflow evidence.
- Lets the component library be the only primary source.

Manual evaluation: pass only when the library informs implementation without deciding the product's visual direction or information architecture.
