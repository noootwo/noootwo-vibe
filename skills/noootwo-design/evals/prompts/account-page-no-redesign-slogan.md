# Eval: Account-page review rejects redesign slogans and page narration

Prompt: "Review an account-information page after a layout pass. Grouping and alignment improved, but the page now opens with '你的信息，一眼看清。' and a note: '先看账户资料和安全状态。需要修改时，再打开对应设置。' The user only asked to make the layout clear."

Expected:

- Fails the comprehension gate for requester-facing and self-evaluating copy, while preserving the improved grouping, alignment, and spacing.
- Changes the operational title to the object or task, such as "Account information" or "Account details".
- Deletes the note unless it adds information a label, state, or control does not already carry; if kept, rewrites it as a direct instruction tied to a real control or consequence.
- Records that a layout-only request does not authorize new public copy, and that clarity must be visible in the structure.
- Returns the artifact for `fix` and does not mark it shipped.

Fails when: it keeps the slogan because the layout is now clear; replaces the note with another paragraph explaining the page; treats the copy as a styling detail; invents brand or benefit copy; or reverts the improved layout while removing the slogan.
