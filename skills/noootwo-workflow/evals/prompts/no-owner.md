# Eval: Stop when no skill owns the request

Prompt: "帮我规划一个自媒体内容矩阵。"

Expected:

- Workflow checks available skill descriptions and finds no clear single owner.
- It stops and reports the gap with one or two closest candidates.
- It does not invent a new Noootwo skill or silently choose a weak external match.

Fails when: it guesses a code, design, or docs skill and starts executing.
