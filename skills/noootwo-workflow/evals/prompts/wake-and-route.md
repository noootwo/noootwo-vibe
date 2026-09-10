# Eval: Wake and route

Prompt: "Add export-to-PDF to the settings page and update the docs."

Expected:

- The agent invokes `noootwo-workflow` before editing anything.
- It reads the nearest repo truth and names the mode and its proof of done.
- Where product questions are unsettled (who exports, why, what the export contains) it invokes the `noootwo-product` skill rather than asking them itself.
- For the doc change it invokes the `noootwo-docs` skill before closing.
- Each specialist is invoked by loading its `SKILL.md`, not merely named.

Fails when: it edits without the workflow; it treats the task as direct despite cross-file behaviour and a docs impact; it asks product questions inside the workflow; it closes with no docs decision.
