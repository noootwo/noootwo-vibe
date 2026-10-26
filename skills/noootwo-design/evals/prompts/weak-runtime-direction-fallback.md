# Eval: Preserve real samples in a weak runtime

Prompt: "The target environment can render one prototype well but only supports static screenshots for alternatives. We still need to choose between three directions."

Expected:

- Produces one fuller interactive or rendered sample plus two lightweight but genuinely different variants.
- Records the weak-runtime limitation and the fact that all three were viewed.
- Keeps sample paths and what each sample proves in the direction record.
- Stops for the user's choice.

Fails when: it downgrades the comparison to prose; it produces three polished screens by skipping core states; or it omits the limitation record.
