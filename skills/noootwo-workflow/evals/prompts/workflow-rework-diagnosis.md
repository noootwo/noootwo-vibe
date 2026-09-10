# Eval Prompt: Workflow Rework Diagnosis

Tell the agent the user strongly rejected the previous output ("this is not what I meant at all") after a UI implementation.

Expected behavior:

- Diagnose the failed layer before another small edit: product misunderstanding, style understanding, implementation translation, artifact review, or unclear evidence.
- Explicitly invoke the matching skill: `$noootwo-product` (Clarity Gate or Product Reality Check), `$noootwo-design` (Style Evidence Check or detail pass), `$noootwo-review`, or `$noootwo-docs`.
- State the diagnosis and the invoked skill in one short line.
- Do not keep polishing the same layer or making cosmetic edits.

Failure signals:

- Makes another small edit without a layer diagnosis.
- Routes to Design for a product misunderstanding.
- Treats the rejection as an instruction to add more features.

Manual evaluation: pass only when the response names the failed layer and invokes the matching skill.
