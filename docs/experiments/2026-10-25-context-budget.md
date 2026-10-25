# Context Budget A/B, 2026-10-25

## Scope

Compare the published `0.22.0` skill package with the candidate `0.23.0`
package. The unit of evaluation is the whole skill package used on unrelated
projects, not a cleanup of one project's documentation.

The candidate keeps all eleven public skills, the state/event schemas, the
append-only history, and the existing acceptance and verification rules. It
adds bounded reads and cold evidence handles through `noootwo-workflow`,
`noootwo-state`, and `noootwo-onboard`.

## Method

- Baseline: isolated `0.22.0` skill home.
- Candidate: isolated `0.23.0` skill home.
- Runner: `codex exec --json --ephemeral -s read-only`
- Model: `cloudbase/deepseek/deepseek-flash`
- Reasoning: `max`
- Prompt, model, configuration, starting commit, and worktree were identical
  within each pair.
- Two pairs ran per project. The final candidate showed the same direction in
  both pairs, so no third pair was added.

Fixed project starts:

| Project | Commit | Task |
| --- | --- | --- |
| `kungfu-trader-community` | `773c6c5` | Decide whether KI-126 recurred and whether duplicate registration is needed |
| `flutter-ifs-app` | `afbf8f0` | From SPEC-011 and the implementation, name the next smallest acceptance slice |
| `unimport` | `631f833` | Review direct-file support boundaries, test gaps, and the smallest next action |

All runs were read-only. No pilot business files, production data,
configuration, or deployment state changed.

Several earlier runs are intentionally excluded. They exposed a candidate
routing cascade that loaded adjacent specialist bodies before evidence and
increased token use. The final workflow gate was then added, and only runs from
the synced final candidate are reported below.

## Token Gate

`total_tokens` is `input_tokens + output_tokens` from the terminal usage
record. `uncached` is `input_tokens - cached_input_tokens`.

| Project | Pair | Baseline total | Candidate total | Delta | Baseline uncached | Candidate uncached | Delta |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Kungfu | 1 | 734,229 | 176,714 | -75.9% | 110,177 | 48,824 | -55.7% |
| Kungfu | 2 | 431,110 | 213,762 | -50.4% | 109,653 | 43,736 | -60.1% |
| Flutter | 1 | 608,155 | 509,365 | -16.2% | 94,984 | 63,279 | -33.4% |
| Flutter | 2 | 1,036,500 | 469,663 | -54.7% | 108,300 | 39,035 | -64.0% |
| Unimport | 1 | 513,085 | 347,589 | -32.3% | 65,798 | 57,646 | -12.4% |
| Unimport | 2 | 836,688 | 517,604 | -38.1% | 79,271 | 76,487 | -3.5% |

Results:

- Median of all six paired total-token deltas: **-44.3%**.
- Median of the three task-level medians: **-32.3%**.
- Median of all six paired uncached-input deltas: **-44.6%**.
- No project pair worsened total tokens; the smallest saving was **16.2%**.
- No project pair worsened uncached input; the smallest saving was **3.5%**.

This clears the predeclared 10% median saving and the 10% no-regression
limits. The result is package evidence for these three fixed tasks, not a
claim that every future task will save the same amount.

## Quality Review

| Project | Baseline result | Candidate result | Decision |
| --- | --- | --- | --- |
| Kungfu | KI-126 is not proven recurrent; do not duplicate it | Same verdict, with fix ancestry and missing production recheck | Pass |
| Flutter | Rename UI is the first reusable vertical slice | Same slice, existing PATCH reused, no delete/create expansion | Pass |
| Unimport | Extension regex misclassifies dotted directories; tests miss the boundary | Same P1/P2/P3 findings and `stat().isFile()` next action | Pass |

History integrity, duplicate detection, verification obligations, and
read-only scope did not regress in the reviewed outputs.

## Behavior Probes

The final candidate ran all ten behavior scenarios against the baseline:

| Probe | Candidate behavior | Result |
| --- | --- | --- |
| 01 vague feature frontier | Asked one current user/time question instead of inventing six modules | Pass |
| 02 cross-file docs route | Planned implementation, tests, and doc synchronization without editing | Pass |
| 03 vague UI | Asked for the dashboard audience before styling | Pass |
| 04 rework | Diagnosed the product layer before another visual attempt | Pass |
| 05 submit | Reported that no visible cross-file diff exists before planning around it | Pass |
| 06 docs only | Reported no typo, ran the project check, and left the tree clean | Pass |
| 07 bounded long history | Returned TTL `15m` and reopen condition `>60s` with two source paths | Pass |
| 08 post-compaction | Rejected `HEAD=deadbeef` and refused untrustworthy D-17 provenance | Pass |
| 09 cold output | Found `required cache config is missing` and kept full output behind a hash | Pass |
| 10 unrelated goal | Recommended a new session and did not reuse the completed release goal | Pass |

Behavior probes are not a token benchmark. Probe 09 intentionally costs more
turns because it must preserve a 32,451-byte cold artifact; its pass condition
is the bounded live diagnosis plus complete evidence handle.

## Reproduction

The test harness is external to the repository:

```text
/tmp/noootwo-context-eval/run_pair.sh
/tmp/noootwo-context-eval/run_scenario_pair.sh
```

The result JSONL, answers, fixed worktrees, and prompt fixtures remain under
`/tmp/noootwo-context-eval/`. They are evidence for this candidate, not
repository artifacts.
