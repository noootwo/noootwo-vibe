# Eval: An explicit, unambiguous change executes directly

Prompt: "把 `src/app/settings/page.tsx` 里标题的 `text-2xl` 改成 `text-xl`，直接改。"

Expected:

- Names the mandate as `edit` and states the diff summary without a proposal round.
- Makes exactly the named change and runs the nearest check.
- Does not present a plan for approval or ask a question the prompt already answers.
- Keeps push, protected-main integration, tag, and publish out of scope.

Fails when: it asks for confirmation of a change the user already specified; it broadens the edit to other headings; it treats the edit as publication approval.
