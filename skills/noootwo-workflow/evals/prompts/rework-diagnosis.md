# Eval: Diagnose rework

Prompt: after a UI implementation, the user says "this is not what I meant at all."

Expected:

- The agent names the failed layer before changing anything: product, design, implementation, or docs.
- It invokes the skill that owns that layer, by loading its `SKILL.md`.
- Product understanding routes to `noootwo-product`; wrong visual direction routes to `noootwo-design`; right intent with wrong execution routes to the design detail pass or `noootwo-review`.
- It states the layer and the invoked skill in one line.

Fails when: it makes another cosmetic edit; it routes a product misunderstanding to design; it reads the rejection as a request for more features.
