# Project Health Review

Use this when the question is broader than a code diff: can this project be safely changed, verified, reviewed, released, and handed off by future agents?

## Review Surface

| Area | Risk question |
| --- | --- |
| Validation entry | Is there a known command or checklist that proves core health? |
| Tests | Are behavior-critical paths covered or at least discoverable? |
| CI | Does automation run the release-relevant checks? |
| Module boundaries | Can likely changes be made without loading unrelated areas? |
| Release path | Can version, tag, publish, and install steps be reproduced? |
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
- `$noootwo-docs`: documentation/source-of-truth gap.
```

## Boundaries

- Do not write docs in the review result; identify the defect and owner.
- Do not invent architecture work without evidence from code, tests, or repeated friction.
- Do not treat missing process as a blocker if the current task has a clear, low-risk verification path.
- Do not expand a narrow code review into a full project audit unless requested or release risk is present.

## Quick Checks

- Search for validation commands in README, package files, scripts, CI, and docs/reference.
- Search for performance budgets, benchmark commands, load tests, tracing/metrics docs, and query-plan workflows when the project has performance-sensitive paths.
- Compare version sources against release notes and manifest files.
- Inspect the largest or most changed files only when they are in the current path.
- Look for repeated rules across README, AGENTS, status, prompts, schemas, and config.
- Check whether release claims have tags, commands, or CI evidence.
