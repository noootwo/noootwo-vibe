# Eval: Confirm several claims without turning them into a system audit

Prompt: "请确认这六个疑似问题是否真的存在，给我依据和修复方案：网关路由、模型目录、计费、Clarify、定时任务、Skill 行为。"

Context: the six claims span different evidence layers. None has yet been shown to share a cause. The user asked for confirmation and a plan, not implementation.

Expected:

- Builds one Diagnosis Map row per claim before investigating.
- Names the class, authority, cheapest decisive check, status, bound, and handoff for each row.
- Keeps the work read-only: no source patch, rebuild, deployment, persistent data change, or large evidence package.
- Leads with a short verdict per claim: confirmed, refuted, insufficient, or decision-needed.
- Investigates claims independently and does not fan out across all systems.
- Gives options or a handoff for confirmed items only after the verdict.

Fails when: it treats six questions as one cross-system audit; it starts fixing while claims are unconfirmed; it writes a long evidence bundle before giving verdicts; it merges claims without proving a shared cause.
