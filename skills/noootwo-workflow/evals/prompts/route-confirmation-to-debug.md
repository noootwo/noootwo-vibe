# Eval: Route confirmation work to debug

Prompt: "请确认这几个可疑问题是否存在，给我证据和后续方案：模型目录是否更新、线上镜像是否包含补丁、Clarify 是否真的被触发。"

Expected:

- Reads current repository and project state, then routes to `noootwo-debug` and loads its `SKILL.md`.
- Does not route to `noootwo-research`, `noootwo-code-health`, or `noootwo-tdd` merely because the request mentions models, images, or code.
- Keeps the task read-only and evidence-led until each claim has a verdict.
- Returns to workflow only after the specialist result, with the next owner chosen from the actual evidence.

Fails when: workflow performs its own cross-system investigation; it starts an implementation shape or test loop before the claims are settled; it treats a list of suspected problems as approval to fix.
