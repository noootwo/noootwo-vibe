# Eval: Resume from current project state

Prompt: a project already has `.noootwo/product-facts.md`, design artifacts, and green tests; the user says "review this component change before submission".

Expected:

- Workflow reads current state through `noootwo-state` if present, git status, and current artifacts.
- It does not rerun `noootwo-product` or `noootwo-design`.
- It routes the changed code through `noootwo-review`, or through `noootwo-tdd` first if tests are missing.

Fails when: it restarts the full product/design lifecycle, or assumes the project is at an earlier stage.
