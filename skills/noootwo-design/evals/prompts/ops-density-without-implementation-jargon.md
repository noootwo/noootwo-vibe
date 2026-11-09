# Eval: Operations density without implementation jargon

Prompt: "Review this support queue for trained agents. It uses compact rows and keyboard shortcuts, and labels items `AWAITING_AGENT`, `FF_ROUTING_V2`, and `ticket-svc degraded`."

Expected:

- Keeps the compact rows and keyboard shortcuts because the audience is trained and frequent.
- Replaces raw enum names, flag names, and service names with the agents' shared queue vocabulary, or moves them to a diagnostics view.
- Checks that every status label helps the agent decide or recover.
- Records a comprehension-gate result and keeps the high-density posture.
- Names the evidence for the agents' vocabulary rather than assuming all "expert" users understand internal names.

Fails when: it calls density itself a defect; makes the queue consumer-simple; or keeps raw flags and service names because "expert users will understand".
