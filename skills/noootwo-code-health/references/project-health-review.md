# Project Health Review

Use this when the question is broader than a code diff: can this project be safely changed, verified, reviewed, released, and handed off by future agents?

## Structure Sweep

Run a Structure Sweep when at least one trigger is true:

- a release or release-candidate is being prepared;
- the same area has been revised repeatedly or has caused repeated review confusion;
- a file, module, directory, or dependency graph has grown enough to increase context cost;
- a new package, module, or boundary was introduced;
- the user asks for a whole-project health review;
- the debt ledger contains a `planned` or `long-term` item that is now due.

The sweep is bounded. Read the repository shape, not every line: ownership, directory depth, import direction and cycles, fan-in/fan-out, duplicated concepts, dead code, test gaps, config/docs duplication, and context cost. Report a ranked debt ledger and recommend the smallest safe move for the top items. Do not turn the sweep into a rewrite.

The ledger is not a backlog of every smell. Follow the disposition model in [refactoring-workflows.md](refactoring-workflows.md): `opportunity` is picked up on the next visit, `planned` gets a bounded pass, `long-term` records a rough end-state and moves through ordinary work, and `accepted` records why the code is not worth changing now.

## Review Surface

| Area | Risk question |
| --- | --- |
| Agent entry | Is there an `AGENTS.md` or equivalent with short always-on rules, skill routing, and repo constraints? |
| Public usage | Does the README state the purpose, install or run basics, and the validation entrypoint? |
| Decisions | Are durable workflow and architecture choices recorded as ADRs or a decision log, separate from status? |
| Current state | Is there a status document naming the active state, the last validation, and the next actions? |
| Validation entry | Is there a known command or checklist that proves core health? |
| Tests | Are behavior-critical paths covered or at least discoverable? |
| CI | Does automation run the release-relevant checks? |
| Module boundaries | Can likely changes be made without loading unrelated areas? |
| Release path | Can version, tag, publish, and install steps be reproduced? |
| Releases | Do release notes or a changelog record version history and migration notes? |
| Versions | Is the version source of truth explicit, with a stated release policy? |
| Runtime/preview | Can a reviewer or agent inspect the result locally? |
| Performance baseline | Are there budgets, benchmarks, traces, query plans, or load checks for performance-sensitive paths? |
| Observability | Can latency, errors, saturation, slow queries, and hot paths be inspected after release? |
| Context cost | Do future agents need to load huge files, duplicated docs, or unrelated references? |
| Source of truth | Are commands, versions, schemas, and project state maintained in one owner? |
| Risk log | Are known gaps visible in status, issues, or release notes? |

## Defect Classes

- `verification gap`: no clear command or evidence path.
- `automation gap`: CI or scripts do not cover what release depends on.
- `boundary risk`: module ownership is unclear or too broad.
- `release risk`: versioning, tag, migration, or install steps cannot be repeated.
- `performance gap`: no budget, benchmark, trace, query plan, load check, or observable metric for a performance-sensitive path.
- `context cost`: future work requires loading excessive or duplicated context.
- `truth drift`: the same fact lives in multiple sources or contradicts itself.

## Output Contract

```markdown
Findings
- [P1] Code/behavior defect - path:line
  Why it matters; failure mode; smallest fix.

Project Defects
- [verification gap|automation gap|boundary risk|release risk|performance gap|context cost|truth drift] title
  Evidence; impact; owner skill; smallest fix.

Verification Gaps
- command not found/run; risk.

Handoff
- `$noootwo-workflow`: routing/process gap.
- `$noootwo-state`: documentation/source-of-truth gap.
```

## Boundaries

- Do not write docs in the review result; identify the defect and owner.
- Do not invent architecture work without evidence from code, tests, or repeated friction.
- Do not treat missing process as a blocker if the current task has a clear, low-risk verification path.
- Do not expand a narrow code review into a full project audit unless a Structure Sweep trigger is present.

## Quick Checks

- Search for validation commands in README, package files, scripts, CI, and docs/reference.
- Search for performance budgets, benchmark commands, load tests, tracing/metrics docs, and query-plan workflows when the project has performance-sensitive paths.
- Compare version sources against release notes and manifest files.
- Inspect the largest or most changed files in the current path during change review; inspect repository-wide shape during a triggered Structure Sweep.
- Look for repeated rules across README, AGENTS, status, prompts, schemas, and config.
- Check whether release claims have tags, commands, or CI evidence.
