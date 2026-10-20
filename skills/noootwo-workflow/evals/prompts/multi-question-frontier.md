# Eval: Keep independent questions on separate frontiers

Prompt: "一次性确认：计费是否算错、定时任务是否漏跑、Clarify 是否只在本地修了、Skill 是否有路由问题。能一起查就一起查，最后给方案。"

Context: the four questions may share infrastructure, but no shared cause has been proven. "Can be checked together" is not evidence that they should be one investigation.

Expected:

- Gives each claim its own status and evidence path.
- Orders by prerequisite, cost, and impact rather than merging them into a repository-wide sweep.
- Allows a later merge only after evidence proves a shared cause.
- Stops with a short verdict and options before implementation, even if some claims remain insufficient.

Fails when: it treats the four claims as one defect; it spends the budget on the largest shared subsystem before testing a cheaper discriminating claim; it fixes one item because the others are hard to observe.
