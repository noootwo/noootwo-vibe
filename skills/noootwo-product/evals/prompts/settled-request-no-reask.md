# Eval: Do not re-open a settled request

Prompt: "Add a keyboard-accessible command to export the current report as PDF. Put it in the existing File menu, keep the current permission rules, show progress and an error with retry, and test the success, permission-denied, and retry paths. The repo already uses the platform PDF service."

Expected:

- States that the product frontier is empty instead of running a ceremonial interview.
- Preserves the stated platform and interaction decisions.
- Produces the checkpoint or proceeds to the next owning skill with no repeated product question.
- Treats remaining implementation details as bounded defaults rather than user decisions.

Fails when: it re-asks facts already supplied; it invents a discovery round; it changes the settled permission or delivery behavior; or it blocks on a low-impact preference.
