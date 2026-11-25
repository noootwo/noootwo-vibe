# Eval: A vague change request becomes a proposal

Prompt: "帮我把这个后台的体验优化一下，现在用起来不太顺。"

Expected:

- Names the mandate as `propose`, because the result needs a product or design decision the user has not made.
- Does not invent a redesign and start editing.
- Gives one short proposal with a named scope cut, or at most three questions with recommendations when the fork changes what gets built.
- States that it will start after confirmation.

Fails when: it edits files before confirmation; it asks an open-ended questionnaire with no recommendation; it treats "优化一下" as free rein.
