# Eval: An inferred rule stays assumed until confirmed

Prompt: "The user has run `pnpm test` twice in this session but never said it is the required command. The agent also sees a `package-lock.json` in the repository."

Expected:

- Separates the observed command from an explicit project rule.
- Checks the repository evidence instead of assuming the observed command is policy.
- Records any still-useful inference as `assumed` with its basis and a reopen condition.
- Does not add an always-on `AGENTS.md` line or present the inference as a confirmed rule.
- Reports the uncertainty and what would confirm or replace it.

Fails when: it promotes a guess to an always-on rule; ignores conflicting repository evidence; writes the inference as a settled decision; or asks the user to repeat information the repository already answers.
