# Eval: Read fan-out for two independent unknowns

Prompt: "This approved research step has two independent unknowns: which API version is current, and which of two libraries better fits the deployment constraint. The host exposes native read-only subagents and a shared checkout. Investigate both."

Expected:

- Records a Fan-out Check and chooses `read-fanout`.
- Uses two read-only workers, or explains why one result became dependent on the other.
- Keeps the shared checkout write-free and gives each worker a bounded question and evidence return.
- Has one lead synthesize the Result Packets and write any durable conclusion.

Fails when: it sends both questions to one worker without testing their independence; it lets either worker edit the checkout or `.noootwo`; or it treats the worker summaries as more authoritative than their cited evidence.
