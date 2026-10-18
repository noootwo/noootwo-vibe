# Eval: The Release Verification Ledger dedupes, closes, and seals

Prompt: "We finished four features, each with a green Change Check. Create the pending verification list for the release, check each repeated item once, publish, then clear the list."

Expected:

- Opens one Release Verification Ledger for checks that must be decided at the release boundary.
- Keeps requirement-level detail in the completed Change Checks instead of copying every point into the ledger.
- Dedupes by the same check and evidence boundary; one full-suite, contract, migration, or deployment check is not repeated per feature.
- Runs the remaining items once through the Release Check against the exact candidate commit and records evidence, owner, and status.
- Seals the completed ledger into the immutable release record before resetting the open working ledger.

Fails when: it turns the ledger into a second task tracker, duplicates cross-cutting checks per feature, treats the ledger as a replacement for Change Checks, or deletes the completed evidence instead of sealing it.
