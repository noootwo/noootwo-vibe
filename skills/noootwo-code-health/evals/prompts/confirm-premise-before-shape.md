# Eval: Confirm a disputed premise before shaping the change

Prompt: "先设计一下怎么修：旧模型应该已经被同步删除了，但线上还能选到；另外不确定新版镜像有没有带 Clarify 补丁。直接给后端和前端接入方案。"

Expected:

- Recognizes that the premise contains two unproven facts: the catalog deletion and the live image contents.
- Routes those facts to `noootwo-debug` or `noootwo-release` before producing an Integration Read or Change Shape.
- Does not design around a defect that may not exist or a deployment that may not be current.
- Starts the Change Shape only for the confirmed behavior and constraint, then names the seam, contract, test seam, and first slice.

Fails when: it designs a migration or frontend flow from the suspected state; it assumes local source equals deployment; it expands the fix before proving which layer is wrong.
