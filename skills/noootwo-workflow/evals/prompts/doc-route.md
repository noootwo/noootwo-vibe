# Eval: Route a document request away from design and debug

Prompt: "整理这份项目说明，写成一份正式文档。"

Expected:

- The artifact shape is a written document.
- Workflow matches a document/writing installed skill, not `noootwo-design` or `noootwo-debug`.
- It invokes one owner and returns to the orchestration loop.

Fails when: it sends the request to design or debug because the user mentioned a project.
