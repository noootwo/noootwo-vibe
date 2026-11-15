# Project Memory

Use this when the user states a durable rule, repeats a correction, or the agent finds a stable project convention that future work must follow. A **project rule** is one sentence that changes future behavior in a named scope. It is not a task log, a transcript, or a global taste profile.

## Qualify

Capture a rule only when all five hold:

- durable — future tasks in this project or module will meet it again
- scoped — the place it applies is named
- actionable — an agent can follow or check it
- authoritative — the user stated it, corrected it, or accepted it; an inference needs evidence and a reopen condition
- non-duplicate — a search found no existing owner, or the existing owner is stale

Leave task-local instructions in the task. Do not memorize what the repository already makes obvious: package scripts, directory layout, schemas, and current code are lookups, not memory. Capture the user's rule or the reason that is not derivable from those sources.

## Place one fact once

| Fact | Owner |
| --- | --- |
| Short rule every future session must follow | nearest `AGENTS.md` |
| Current progress, stage, blocker, next trigger | `.noootwo/state/current.json` through the state helper |
| Durable choice with rationale or tradeoff | `docs/adr/` |
| Current project status, risks, next actions | `docs/status.md` |
| Accepted contract | `docs/specs/` |
| Implementation sequence | `docs/plans/` |
| Repeatable procedure | procedure layer or `docs/guides/` |
| Raw evidence or long source | cold evidence |

Link the always-on rule to one on-demand rationale when the reason matters. Do not copy the same rule into `AGENTS.md`, status, and an ADR.

## Capture in one turn

1. Reduce the instruction to one sentence: `Rule | Scope | Trigger | Source`.
2. Search the nearest `AGENTS.md`, ADRs, status, specs, and state for the same claim.
3. If it exists, update it in place. If it conflicts, record the supersede and remove the stale line in the same pass.
4. Write the smallest owning form. An explicit user rule goes in without asking the user to confirm their own words. An inferred rule is recorded as `assumed` with a reopen condition; promote it to an always-on line only when evidence or the user confirms it.
5. Report `remembered: <rule> -> <path>` in the close. If the rule is task-local, say that instead.
6. Ask only when scope or ownership is genuinely ambiguous, or the new rule conflicts with an existing accepted rule.

## Correction

A correction is evidence that an earlier rule, default, or assumption failed. Capture the reusable part, not the whole exchange:

- Trigger — the situation that exposed the failure
- Wrong behavior — what the earlier attempt did
- New rule — what to do instead
- Prevention check — how a future agent can tell it complied

Put the shortest positive form in the owning layer; keep the wrong behavior out of always-on text unless the prohibition is the only clear wording. If the same failure recurs after the rule is recorded, route it to `noootwo-debug` for a proven cause instead of stacking another rule.

## Boundary

- One project, one memory root. No global cross-project memory.
- No full transcript, daily log, or duplicated rule set in a hot file.
- Do not promote a one-off task instruction, a guessed taste, or a fact that is cheaper to look up.
- Do not let a compaction summary or a new session reopen a rule without new evidence; the owning record is the authority.

## Done when

The rule has one owning location, the shortest always-on form if needed, no stale duplicate, and a close report that names where it landed.
