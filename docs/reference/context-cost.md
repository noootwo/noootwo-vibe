# Context Cost Research Brief

- Status: accepted for candidate `0.23.0`
- Date: 2026-10-25
- Decision: optimize the whole Noootwo package with a bounded context lifecycle while preserving append-only history, provenance, and current quality gates
- Would flip it: paired real-project probes show a quality, historical-integrity, or acceptance regression; or candidate `total_tokens` does not fall by at least 10% without a task worsening by more than 10%
- Confidence: medium for the mechanism and for these three fixed tasks; the paired package gate passed on 2026-10-25, but it is not a universal saving guarantee

## Evidence

| Source | Level | Finding used | Boundary |
| --- | --- | --- | --- |
| [Chroma, *Context Rot*](https://research.trychroma.com/context-rot), 2025-07-14 | vendor technical report across 18 models | Performance varies with input length even on simple tasks; semantic ambiguity and distractors can degrade it further. A large advertised window does not imply uniform attention. | Measures model behavior, not this skill package. It does not justify one universal token threshold. |
| [Anthropic, *Effective context engineering for AI agents*](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), 2025-09-29 | platform engineering guidance | Treat context as finite; retrieve just in time; compact with high fidelity; use structured notes; reserve subagents for isolated work; find the smallest high-signal token set. | Vendor practice, not an independent controlled study. |
| [ACE, arXiv 2510.04618](https://arxiv.org/abs/2510.04618), 2025-10-06 | research preprint | Incremental, structured context updates preserve useful detail and resist brevity bias and context collapse better than repeated whole-context rewriting. | Reported gains are benchmark-specific and not a promise for Noootwo. |
| [Agentic Context Management, arXiv 2607.21503](https://arxiv.org/abs/2607.21503), 2026-07-23 | research preprint | Treat context as a lifecycle: decide what to retain, structure it by type, consolidate with provenance, select the current need, anticipate the next, and compact to a budget. | Single-author preprint; its benchmark scores were not independently replicated here. |
| [ACM for Long Horizon Tasks, arXiv 2607.23809](https://arxiv.org/abs/2607.23809), 2026-07-26 | research preprint | Offload discarded content to external memory and retrieve it on demand; effective management can reduce peak token pressure and improve consistency. | Weakest evidence is the transfer from its trained agent setup to static skill instructions. |
| [The Complexity Trap, arXiv 2508.21433](https://arxiv.org/abs/2508.21433), 2025-08-29 | SWE-bench comparison | Simple observation masking halved cost relative to raw history and matched or slightly exceeded LLM summarization in tested agents. | Narrow agent/model set; masking can remove evidence if provenance is not retained. |
| [Compression Method Matters, arXiv 2603.23527](https://arxiv.org/abs/2603.23527), 2026-03-06 | controlled compression study, 5,400 calls | Aggressive compression is benchmark- and structure-dependent; saving input tokens does not reliably reduce total cost because outputs can expand. | It tests prompt compression, not this package's retrieval protocol. |
| [Compaction Laundering, arXiv 2610.29869](https://arxiv.org/abs/2610.29869), 2026-10-21 | security preprint | Flattening provenance before compaction made forged approvals survive 87-100% of attempts in five harnesses; role-typed harnesses were 0%; a code-level provenance check caught 77%. | New, unreplicated security result; exact rates should not be generalized as a package effect. |
| [Cognition, *Don't Build Multi-Agents*](https://cognition.ai/blog/dont-build-multi-agents), 2025-06-12 | engineering experience | Agents that make dependent decisions need shared context and conflict resolution; parallel subagents can propagate incompatible implicit decisions. A single-threaded agent is the simple default. | Engineering position, not a controlled benchmark; Anthropic reports the opposite benefit for isolated research work. |

All nine source URLs returned HTTP 200 on 2026-10-25. The arXiv abstracts were read directly; the Chroma, Anthropic, and Cognition findings were checked against the visible article text. No paywall or access fallback was needed.

## Mechanisms Adopted

1. **Bounded selection before reading.** Read the current skill, the request, and only the reference sections or evidence that can change the current decision.
2. **Compression as a view, not a rewrite.** The capsule carries goal, stage, settled and unsettled decisions, blockers, next trigger, evidence handles, and a source state hash. Append-only events remain authoritative.
3. **Lossless cold storage.** Raw outputs above 16 KiB are written before reasoning; the live context receives the path, command, exit status, hash, and a bounded tail.
4. **Incremental state changes.** Append only when a durable field changed, and store the actual changed values. A read or unchanged check creates no history event.
5. **Single-writer default.** Keep dependent decisions in one context. Isolate only independent read-only research or review, and return a bounded summary plus provenance.
6. **Post-compaction verification.** Restore the capsule, then check the current commit, worktree, and newest evidence before trusting it.
7. **Progressive disclosure.** For references above about 200 lines, read headings or query hits before the matching section.
8. **No manual Lean mode.** The rules adapt to task depth, so quality paths do not depend on the user remembering to enable a cheaper mode.

## Counterexamples And Rejected Alternatives

- **Aggressive summarization of everything.** Rejected because summarization can drop domain detail and prompt compression has benchmark-dependent output effects. Noootwo keeps raw history and cold evidence.
- **A new context-optimization skill.** Rejected because it adds a permanent description, routing branch, and another place to drift. The capability belongs to `noootwo-workflow` and `noootwo-state`.
- **Subagents as a default fan-out.** Rejected because dependent actions carry implicit decisions that can diverge. The capability remains available only for independent read-only work.
- **A fixed token or line cap on all work.** Rejected because a hard cap can truncate the one decisive evidence item. The 80-line and 16 KiB values are default live-view boundaries with an explicit cold handle, not quality limits on stored evidence.
- **Clearing tool output without a handle.** Rejected because it destroys provenance and makes a later decision unreprovable.
- **Manual Lean mode.** Rejected because it shifts the optimization burden to the user and makes comparisons ambiguous.

## Package Consequence

The public set stays at eleven skills. `noootwo-workflow` owns reading depth and scheduling; `noootwo-state` owns the capsule, file inspection, cold capture, source hashes, and audit. All model-invoked skills carry the same compact lifecycle rule. The state and event schemas are unchanged, so rollback is a package-version rollback rather than a data migration.

## Verification Boundary

Static and deterministic checks establish API shape, budgets, and script behavior. The package gate adds six paired runs across the three named projects at fixed commits, with the same model and configuration. All ten behavior probes passed, every pair reduced `total_tokens` and uncached input, the median of all six total-token deltas was `-44.3%`, and the median of task-level medians was `-32.3%`. No acceptance, historical-integrity, duplicate-detection, verification, or rework regression was found.

The result is recorded in [the 2026-10-25 experiment](../experiments/2026-10-25-context-budget.md). It clears the package's 10% release gate for those tasks; it does not establish a universal percentage for other repositories or models.

If later evidence shows that the 80-line default hides decisive context, the fix is to lower selection precision or add a trigger to reopen the source, not to remove the cold-evidence boundary or weaken verification.
