# 0021 — Release Verification Ledger consolidates release-bound verification

## Status

Accepted.

## Context

After verification depth moved to Change Check / Escalated Check / Release
Check, several requirements can reach a release with their local proof already
closed. The remaining work is cross-cutting: one full suite for the exact
commit, shared compatibility or migration checks, artifact and provenance
checks, deployment markers, rollback, and release health. Those checks arrive
from different features and otherwise get rediscovered, repeated, or lost.

This verification queue is distinct from the append-only Release Ledger in
`references/artifacts.md`, which records the release identity that was produced.

Google SRE reports that a curated launch checklist helped produce reproducibly
reliable launches; Microsoft deployment gates collect health signals and block
promotion until the required gates pass in the same evaluation window. Checklist
evidence also has a boundary: the WHO surgical checklist study found improved
outcomes, while Ontario's mandatory-adoption study found no significant
improvement. A checklist is a control surface, not proof that the work was
performed. Ownership, evidence, and revalidation against the actual candidate
are what make it useful.

## Decision

1. `noootwo-release` owns one **Release Verification Ledger** for the next release.
2. The ledger contains only checks that must be decided at the release boundary:
   cross-cutting evidence, a requirement check that cannot be re-established at
   the candidate, or a known blocking gap. Detailed requirement verification
   stays closed in its Change Check.
3. Dedupe by the check, exact boundary, and evidence command or path — not by
   wording. Five features covered by one suite produce one item.
4. Before choosing a version or tag, reconcile the ledger against the exact
   release-candidate commit, merge duplicates, supersede obsolete items, and
   name every owner and release condition.
5. The Release Check consumes each remaining item once and records the evidence,
   owner, and status. `open` or `blocked` items stop the release; an
   `accepted gap` needs a consequence, owner, and release condition.
6. Seal the completed ledger into the release record with version, commit,
   artifact identity, and release ID. Reset the open working ledger only after
   the sealed copy exists. Sealed evidence is never deleted.
7. `noootwo-state` chooses the storage path and form; release owns the lifecycle
   and the release decision.
8. The `noootwo-workflow` close gate routes a newly discovered release-bound
   check or gap to `noootwo-release`; workflow schedules the handoff and does
   not duplicate the ledger method.

## Evidence brief

Decision: adopt a release-bound ledger with explicit reconcile, consume, seal,
and reset steps rather than carrying every requirement's verification forward.

What would flip it: evidence that a separate ledger increases duplicate work,
goes stale faster than the release record, or fails to improve release
readiness compared with the Release Plan alone.

Findings:

- Google SRE's *Reliable Product Launches at Scale* says a curated launch
  checklist was useful for reproducibly reliable launches. The abridged
  checklist groups architecture, reliability, security, automation, rollout,
  and schedule checks (`https://sre.google/sre-book/reliable-product-launches/`,
  `https://sre.google/sre-book/launch-checklist/`).
- Microsoft Azure deployment gates collect external health signals before or
  after deployment and continue re-evaluating until all required gates pass in
  the same interval; timeout blocks promotion
  (`https://learn.microsoft.com/en-us/azure/devops/pipelines/release/approvals/gates?view=azure-devops`).
  This supports a single release-bound aggregate with evidence and a stop
  condition.
- The WHO Surgical Safety Checklist study reported complications falling from
  11.0% to 7.0% and death from 1.5% to 0.8% after introduction
  (`https://pubmed.ncbi.nlm.nih.gov/19144931/`). The mechanism is a short,
  explicit set of checks with a shared execution moment.
- The counterexample is Ontario's mandatory checklist adoption: across 109,341
  pre-adoption and 106,370 post-adoption procedures, mortality and complication
  changes were not statistically significant
  (`https://pubmed.ncbi.nlm.nih.gov/24620866/`). Checklist presence alone is not
  evidence of adherence or outcome, so this design requires owner, status,
  evidence, and exact-commit revalidation.

Confidence: **medium-high** for the lifecycle mechanism and **medium** for cost
savings, because no direct token/time benchmark exists for this repository.

## Rejected alternatives

- **Copy every requirement's detailed checks into one list**: duplicates work and
  turns the ledger into a second task tracker.
- **Keep only the Release Plan**: a plan names the release shape but not the
  accumulated open checks and their evidence.
- **Clear the list after release without retaining it**: destroys provenance and
  makes the release record unable to explain what was verified.
- **A new release-verification-ledger skill**: release engineering already owns the lifecycle;
  a second skill would split the decision from the release record.

## Consequences

- A release now has one visible open queue before the Release Plan and one
  sealed evidence record after it.
- Requirement-level Change Checks stay local and cheap; only release-bound
  checks cross into the ledger.
- The ledger adds a small reconciliation step, but removes repeated full-suite,
  contract, migration, and deployment checks across features.
- The new eval measures dedupe, scoping, exact-commit evidence, sealing, and
  reset behavior; model behavior measurement is still required.
