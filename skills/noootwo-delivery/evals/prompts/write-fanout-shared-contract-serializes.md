# Eval: Shared meaning prevents parallel write lanes

Prompt: "A write fan-out has two lanes. One adds a `status` field to the account schema; the other renders that field in settings. Both have separate files and tests. Start both now."

Expected:

- Finds the shared schema and component contract before dispatching both lanes.
- Chooses `contract-first` or `serialize`, with one contract owner and a compatibility period.
- Lands or settles the contract before the dependent lane writes against it.
- Rechecks independence after the contract is merged and records any remaining merge order.

Fails when: it treats different file names and tests as independence; it lets the consumer invent the field; or it merges the two lanes in an order that breaks `main`.
