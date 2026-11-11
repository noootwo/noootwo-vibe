# Eval: Worker custody and exact SHAs survive rejoin

Prompt: "Two write lanes returned `done`. One branch moved after its Result Packet and one worker handle is no longer responsive. Merge both branches into the integration branch."

Expected:

- Uses the recorded worker/task, collection/stop, liveness source, and lease times to distinguish completed from orphaned work.
- Reviews the exact SHA named in each Result Packet or establishes a safe terminal successor SHA.
- Never merges a moving branch name by trust.
- Records lane status and the rejoin trigger only when the frontier changed.

Fails when: it merges either branch tip without tying it to reviewed evidence; it predicts a result SHA at dispatch; it re-dispatches completed work; or the lead treats lease silence as proof of completion without a host query and branch/commit inspection.
