# Long-Turn Cost Audit, 2026-11-02

## Scope

Measure where the Noootwo skills actually spent context in the real Codex
history of two related projects and their harness:

| Project | Role in the history |
| --- | --- |
| `kungfu-community` / `kungfu-trader-community` | the community product carried across a directory rename |
| `kungfu-harness` | the harness project beside it |

The unit of evidence is the local Codex session log under `~/.codex/sessions`
on this machine. The audit is read-only, uses no project business files, and
prints aggregates only. It is a description of these three projects, this
model and configuration, and this period. It is not a universal claim about
Noootwo, other repositories, or the platform.

The figures below are the snapshot taken at `2026-11-02 05:07` (`+08:00`). The
`kungfu-community` history was still appending during the audit, so a rerun
reads slightly higher there; the direction of every finding is unchanged.

## Method

```bash
python3 skills/noootwo-state/scripts/audit_codex_context.py --cwd <project> --json --top-turns 5
```

Token figures are the terminal usage records, deduplicated by
`(thread, response)`. `uncached` is `input - cached`. Tool output is measured
from the recorded function output payloads. Per-turn attribution uses the
`turn_id` on usage records and completed tool items. Command-name evidence
comes from a one-off local scan that matched command text and counted
output bytes; it never printed arguments or output.

## Aggregate Result

| Metric | community | trader | harness | combined |
| --- | ---: | ---: | ---: | ---: |
| Sessions | 2 | 9 | 26 | 37 |
| Turns | 34 | 165 | 115 | 314 |
| Unique responses | 2,446 | 16,498 | 21,201 | 40,145 |
| Compactions | 75 | 402 | 620 | 1,097 |
| Tool calls | 5,220 | 31,744 | 42,943 | 79,907 |
| Tool output | 52 MB | 304 MB | 573 MB | 930 MB |
| Outputs over 16 KiB | 941 | 4,758 | 9,113 | 14,812 |
| Repeated exec groups | 89 | 901 | 1,144 | 2,134 |
| Repeated exec extras | 231 | 2,676 | 3,664 | 6,571 |
| Input tokens | 396.0M | 2,636.0M | 3,315.6M | 6,347.6M |
| Uncached input | 32.1M | 165.4M | 257.3M | 454.8M |
| Output tokens | 2.9M | 18.3M | 22.1M | 43.3M |
| Reasoning output | 1.2M | 7.2M | 8.3M | 16.7M |
| Nominal total | 398.9M | 2,654.3M | 3,337.7M | 6,390.9M |

The cache-hit rate is 92.8% of input. The cached share is not free: it is
re-sent once per model response, and the number of responses is what makes a
long turn expensive. Uncached input plus output, the part that cannot be
amortised, is roughly 498M tokens for these three projects.

## Turn Shape

The largest turns, not the largest files, dominate:

| Project | Turn | Total | Uncached | Responses | Tool calls | Over 16 KiB | Repeat extras | Compactions | Span |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| harness | `442fa0841259` | 556.8M | 55.0M | 3,574 | 7,121 | 1,963 | 617 | 127 | 10.4 h |
| harness | `9e4ee7b40f81` | 491.6M | 25.7M | 3,118 | 4,428 | 781 | 439 | 62 | 8.8 h |
| harness | `3c81911c8397` | 414.4M | 36.4M | 2,581 | 5,445 | 1,266 | 498 | 85 | 6.6 h |
| trader | `d278fa481a56` | 166.9M | 11.6M | 1,003 | 1,957 | 363 | 96 | 28 | 2.4 h |
| community | `5f30f976c73f` | 153.5M | 13.1M | 920 | 1,902 | 381 | 57 | 31 | 2.7 h |

Each large turn also contains many compactions. Compaction is where the turn
loses its own history; without a refreshed capsule the next response pays to
rediscover what it already knew.

## Repeated Reads

Commands whose text mentioned a hot document, with the tool output they
produced:

| Named in command | Calls | Output |
| --- | ---: | ---: |
| `project-status.md` | 1,920 | 42.3 MB |
| `docs/system/README.md` | 771 | 19.4 MB |
| `SKILL.md` | 1,680 | 20.1 MB |
| `AGENTS.md` | 374 | 5.8 MB |
| `.noootwo` | 42 | 286 KB |

The project instruction is to stay current with `project-status.md`; the
observed behaviour is re-reading an 8,648-line status timeline instead of
reading the slice the current step needs. The capsule existed in the harness
but was last written on 2026-10-29, and the community project had no active
capsule at all, so the cheapest recovery path in the package was the least
used one.

## What Changed

The mechanism adopted from this evidence is recorded in
[ADR 0026](../adr/0026-long-turn-context-checkpoints.md):

- a behaviour-triggered checkpoint in `noootwo-workflow` (compaction, repeat
  read or repeat verification command, two failed loops without new evidence,
  terminal claim while reading continues);
- capsule-first long-turn recovery and anti-drift read rules in
  `noootwo-state`;
- per-turn totals in `audit_codex_context.py` so this table can be re-run as a
  regression measure.

Rejected: a fixed token or step budget, global truncation, a summarising
subagent per turn, and a new context skill.

## Unproven

- The behaviour rules have deterministic checks and three new eval prompts,
  but no fresh model sessions have been run, so no token, time, or rework
  reduction is claimed for them.
- The audit describes these three projects only. The per-turn numbers will
  move with model, tooling, and task mix.
- Nothing here says a project may skip a required verification. The reopen
  condition is part of the checkpoint, and the evidence and verification
  gates are unchanged.

## Reproduction

```bash
python3 skills/noootwo-state/scripts/audit_codex_context.py --self-test
python3 skills/noootwo-state/scripts/audit_codex_context.py --cwd /Users/notwo/Desktop/work/kungfu-harness --json --top-turns 5
python3 skills/noootwo-state/scripts/audit_codex_context.py --cwd /Users/notwo/Desktop/work/kungfu-trader-community --json --top-turns 5
python3 skills/noootwo-state/scripts/audit_codex_context.py --cwd /Users/notwo/Desktop/work/kungfu-community --json --top-turns 5
```

The per-turn output contains only hashes, counts, byte sizes, and durations.
