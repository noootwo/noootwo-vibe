# Eval: Same file is not a permanent lock

Prompt: "Two small changes both touch `settings.ts`, but one edits the theme parser and the other edits the validation table. Can they run in parallel?"

Expected:

- Inspects semantic overlap rather than banning parallel work because the file name matches.
- Chooses `parallel` when the regions and contracts are independent, with small PRs and a conflict check.
- Escalates to `serialize` if the changes share a symbol, generated output, or migration.

Fails when: it creates permanent file ownership or a lock file, or declares independence without checking the shared meaning.
