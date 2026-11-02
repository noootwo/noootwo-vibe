# Modocc Route Audit, 2026-11-03

## Scope

Measure how the Noootwo skills were invoked across the real Codex history of
`/Users/notwo/Desktop/mine/own/app/modocc`, the brand-asset prototype worked in
two threads on 2026-11-02 and 2026-11-03.

The unit of evidence is the local Codex session log under `~/.codex/sessions`.
The audit is read-only, prints aggregates and command-path counts only, and
never emits message, tool-output, argument, environment, or credential content.
It describes this project, this model, and this configuration for this period.

The snapshot below was taken on 2026-11-03. The second thread was still
appending when the preliminary scan ran, so these figures supersede the smaller
preliminary numbers cited in the plan.

## Method

```bash
python3 skills/noootwo-state/scripts/audit_codex_context.py \
  --cwd /Users/notwo/Desktop/mine/own/app/modocc --json --top-turns 5
```

Skill-body reads were counted with a one-off scan over the five matched session
files. It matches `noootwo-<skill>/SKILL.md` inside recorded
`function_call`/`custom_tool_call` arguments, counts one read per command per
skill, and prints only the skill name and timestamp. Local times below are
`+08:00`; the session timestamps are UTC.

## Aggregate

| Metric | Value |
| --- | ---: |
| Sessions / threads | 5 / 2 |
| Turns | 19 |
| Unique responses | 2,371 |
| Compactions | 28 |
| Tool calls | 3,458 |
| Tool output | 137.8 MB |
| Outputs over 16 KiB | 522 |
| Repeated exec groups / extra calls | 33 / 145 |
| Input tokens | 422.96M |
| Uncached input | 13.19M |
| Output tokens | 2.32M |
| Reasoning output | 0.91M |
| Nominal total | 425.28M |

Cached input is 409.76M of the input total. It is re-sent once per response,
which is why the response count and the compaction count matter more than any
single file size.

## Skill-body reads

- 44 read commands referenced at least one Noootwo `SKILL.md`.
- Mentions: product 22, design 22, research 21, workflow 6, state 3, release 3,
  TDD 1, code-health 1, debug 1, ask 0, onboard 0.
- 14 of the 44 commands reloaded the product, design, and research trio
  together in one command; the three singles at 16:50 and 17:30 local are the
  same block written differently.
- The first reads happen at 16:07 local, before any `@` mention: the model found
  product, design, and research by itself.
- 21 of the 28 compactions were followed within 60 seconds by a skill-body read
  (median 7.1 s, range 4.4-32.6 s).
- Engineering owners enter late: TDD at 03:19 local, code-health at 03:42,
  release at 03:43 and 04:02, all inside the second thread.

## Phase mapping

1. **No skill specified (16:07-16:50).** The model discovers and reads product,
   design, and research on its own, then produces the research, product-design,
   brand, and agent-design documents plus the first prototype. Discovery worked;
   the three design-stage bodies become the working set.
2. **Skills `@`-mentioned (16:56-17:20).** The mentions confirm skills that are
   already read, and the same artifacts are regenerated with evidence. Ownership
   does not change because a mention is emphasis, not routing.
3. **No further mentions.** The product/design/research trio keeps being
   reloaded as a block after compactions, while the authentication, server,
   implementation, and deployment work runs with no engineering owner until
   late in the second thread.

## What this shows and does not show

- Shows a routing failure, not a capability failure: product, design, and
  research contributed throughout, and debug entered correctly when the request
  changed shape.
- Shows that reloading skill bodies was the dominant recovery move: 44 body
  reads against 28 compactions, with 21 compactions followed by a reload.
- Shows that the project kept no `.noootwo/state/`, so no capsule existed as a
  recovery entrypoint.
- Does not show any token, time, or rework saving for the new rules; that needs
  a fresh-session run against a no-skill baseline. It does not generalise beyond
  this project, model, and configuration.
