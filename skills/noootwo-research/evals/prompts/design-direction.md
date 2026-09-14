# Eval: A design direction blocked by an unknown

Prompt: "Make the pricing page feel more premium. I do not want another generic SaaS look."

Expected:

- The agent treats this as a decision that needs outside evidence, not as an implementation task, and invokes the `noootwo-research` skill by loading its `SKILL.md`.
- It names the decision and what evidence would flip it before searching.
- It sizes the pass, and for high-character work chooses `deep`.
- It draws on the design and UI source pools, records source accessibility, and uses the fallback ladder if the preferred pools are unreachable.
- It records evidence levels and prefers artifacts and screenshots over prose.
- It finds a counterexample or states explicitly that none was found.
- Each finding names a mechanism and a do-not-copy boundary rather than an adjective.

Fails when: it lists adjectives such as clean, modern, or premium; it copies a named brand's surface; one source decides the direction; it produces `.noootwo/style-discovery.md` with fields missing; it starts editing UI before the research brief exists.
