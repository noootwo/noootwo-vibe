# Eval: Shared contract serializes

Prompt: "Requirement A adds a new `status` field to the account API; requirement B consumes it from the mobile client. Run both now."

Expected:

- Marks the API schema/client contract as shared.
- Chooses `contract-first`: land the backward-compatible API and generated client first, rebase both, then parallelize.
- Uses expand/contract or a compatibility period for the data shape.

Fails when: it treats different file names as independence, or lets the consumer build against an unmerged contract.
