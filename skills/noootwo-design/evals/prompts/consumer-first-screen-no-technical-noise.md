# Eval: Consumer first screen rejects technical noise

Prompt: "Review this habit tracker first screen. It shows a 'Powered by GPT-4o' badge, an 'Embedding sync: 42ms' chip, a 'How it works' accordion, and a prominent Settings button."

Expected:

- Fails the comprehension gate and names the primary user, first screen, and evidence.
- Removes model names, embedding and latency detail, and the implementation explainer from the product surface.
- Keeps one primary action and moves settings behind a secondary entry unless a recurring user decision requires them.
- Applies the note budget: any retained note must prevent an error, explain a consequence, support recovery, or teach a term needed now.
- Returns to the artifact, or to `noootwo-product` if the audience or main path is unsettled.

Fails when: it keeps the technical badges as "trust signals"; only restyles them; or marks the screen ready.
