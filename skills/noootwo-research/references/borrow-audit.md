# Borrow Audit

Every research pass is also a chance to check whether an existing skill already solves the problem better. Borrow mechanisms, not wording, prompts, or surface styling.

## Sources to compare against

- **The local skill set first**: the Noootwo skills, and any installed local skills the project already uses. A mechanism already present is duplicated effort, not a finding.
- **Well-regarded public skill suites**: `obra/superpowers`, `pbakaus/impeccable`, `mattpocock/skills`, `anthropics/skills`.
- **Research-shaped prior art**: `dzhng/deep-research` for breadth and depth control, `mvanhorn/last30days` for recency windows and multi-source aggregation.
- **The domain's own best projects**: the repositories and products the research pass already surfaced.

Read the actual file or repository. A README description is a lead, not evidence of how the mechanism works.

## What counts as a mechanism

A mechanism is repeatable and transferable: a gate, a checklist, a source ladder, a scoring rule, a detector, a bounded loop, a separated reviewer, a durable-truth split, a handoff contract, an evidence format.

Not mechanisms: a writing style, a tone, a command name, a brand surface, a leaked prompt, a proprietary workflow description.

## The adoption gate

Adopt only when all four hold:

1. **It prevents a repeated, concrete failure.** Name the failure it prevents; if you cannot, it is taste, not a fix.
2. **It fits the budget.** Description ≤200 characters, `SKILL.md` ≤120 lines, ≤12 reference files, and an entry that stays short.
3. **It keeps the cheap mode cheap.** A mechanism that taxes `quick` work to help `deep` work is priced wrong.
4. **It becomes checkable.** A rule, a template, a script, or an eval scenario — not a paragraph of encouragement.

When a candidate fails a criterion, record the rejection and the reason. Written rejections stop the same proposal from returning every quarter.

## Output

```markdown
Borrow Audit

| Mechanism | Source | Failure it prevents | Budget fit | Adopt or reject | Reason |
| --- | --- | --- | --- | --- | --- |

Adopted
- mechanism → the exact rule, reference, or eval changed.

Rejected
- mechanism → the criterion it failed.

Proposals
- structural change that needs an ADR before anyone implements it.
```

## Where the audit lands

- Mechanisms adopted now: the skill body, a reference, or an eval scenario, plus a release note.
- Structural proposals — a new skill, a new gate, a change of ownership: recorded as an ADR candidate, not implemented in the same pass.
- The pass itself: recorded in the repository's research ledger so the next reader knows what was compared and when.

## Do not copy

- Leaked, unofficial, or private prompts and internal documents.
- Proprietary workflow descriptions, brand voice, or marketing language.
- Surface styling, exact layouts, logos, or "in the style of X" direction.
- A dependency, engine, or toolchain only because a well-regarded project has one.
- A mechanism whose cost is invisible in the source project because it has different scale, staffing, or harness support.
