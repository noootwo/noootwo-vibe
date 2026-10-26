# Eval: A prose direction menu is not a design decision

Prompt: "Give me three directions for a calm but distinctive personal finance dashboard, then let me choose one."

Context: The runtime supports static HTML previews and the project has enough content for realistic samples.

Expected:

- Produces three materially different, openable low-cost samples rather than a text-only menu.
- Records each sample path, what it proves, and that it was viewed.
- Recommends one direction and stops for the user's choice.

Fails when: it presents only names, adjectives, or prose descriptions; it starts the final implementation; or it claims a sample exists without a viewable artifact.
