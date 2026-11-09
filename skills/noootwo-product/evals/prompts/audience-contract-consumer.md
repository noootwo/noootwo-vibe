# Eval: Audience contract for a consumer surface

Prompt: "Polish the first screen of our consumer habit tracker. The current draft has a 'How it works' panel listing the model, embedding pipeline, API latency, and database sync status."

Expected:

- Treats "consumer" as a starting point, not a complete audience; names the primary user, moment, familiarity, frequency, and error cost.
- Derives low density, plain language, one primary action, and defaults-first settings.
- Removes model, embedding, API, database, framework, and internal-status detail from the product surface.
- Keeps at most one short trust or privacy line where it helps the user act, not a technical explainer panel.
- Hands off an explicit Audience Contract and Interaction Posture to design.

Fails when: it keeps the panel as "transparency"; replaces it with more technical proof; exposes settings before a recurring user decision; or uses terms such as "LLM pipeline", "embedding", or "API latency" on first use.
