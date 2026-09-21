# Eval: Route a slide deck to a presentation skill

Prompt: "帮我做一份产品发布会 PPT，先做结构和视觉方向。"

Expected:

- Workflow reads current state and available skill descriptions.
- It does not invoke `noootwo-review` or `noootwo-tdd`.
- It matches an installed presentation/slide/PPT owner and invokes that skill by reading its `SKILL.md`.
- If no presentation skill is installed, it stops with one or two candidates instead of choosing a code skill.

Fails when: it routes the task to code review/TDD, guesses a code skill, or invents a Noootwo PPT skill.
