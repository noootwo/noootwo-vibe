---
name: noootwo-workflow
description: "Use to run one multi-step task: a feature, a cross-file change, a bug, a refactor, a release, a handoff, or rework after a rejected fix. Owns the loop and invokes the other skills."
---

# Noootwo Workflow

Run one task through one controlled loop:

`read repo truth -> route -> plan -> build -> verify -> close`

## 1. Read repo truth

Pick the smallest read that covers the risk:

- `direct` — the current file, changed-file context, and the nearest instructions.
- `project` — `AGENTS.md`, README, `docs/status.md`, package/build metadata, nearest tests.
- `decision` — ADRs, specs, release notes, public contracts, migrations, design artifacts.

**Done when:** you can name the files that constrain this change, or state that none do.

## 2. Route

Classify the task, then invoke the skill that owns it:

| The task | Invoke |
| --- | --- |
| Real user, first loop, scope, main path, states, or acceptance unsettled | `noootwo-product` |
| UI, visual, artifact, or frontend work with the product path settled | `noootwo-design` |
| Code reaching submit or release; risky, public-contract, or wide-blast-radius diffs | `noootwo-review` |
| Behaviour, project state, release facts, or agent instructions changed | `noootwo-docs` |

To invoke one, read its `SKILL.md` and follow it. Naming the skill is the instruction — a skill you only considered has not run. When a specialist is unavailable, say so in one line and follow the closest fallback.

Route once per trigger, at the moment it arrives. When two skills apply, run product first, then design, then review and docs.

While a product decision is unsettled, the loop stops: no file edits, no design, no implementation plan, and no handoff to design until the product skill returns a confirmed shared understanding.

**Done when:** every specialist trigger has either been invoked or recorded as not applying.

## 3. Choose the mode

- `direct` — one narrow change with an obvious check. State the change and the check, then do it.
- `planned` — several files or a public behaviour change. Write a short plan first.
- `diagnostic` — a bug, failure, or regression. Record the reproduction and the root cause before any fix.
- `release` — list version files, manifests, tags, install targets, and verification commands before publishing.
- `onboarding` — audit the project's skills and foundation before proposing work. Read `references/project-skill-audit.md` and `references/project-foundation-check.md`; add the smallest missing file from `references/minimal-foundation-templates.md`.
- `recovery` — a previous attempt drifted or failed. Diagnose before rebuilding.

**Done when:** the mode, its scope, and its proof of done are stated.

## 4. Build in slices

Keep each slice independently reviewable and testable. Prefer existing repo patterns over new abstractions. Load only the files the current slice needs — search first, then read bounded ranges.

Use TDD or repro-first when the change touches behaviour, a public interface, a regression, or data. When no practical test exists, name the manual scenario before editing.

**Done when:** every slice has run its check.

## 5. Close

Answer each before calling the work done:

- Did the closest meaningful verification run, or is the gap explicit?
- Did a specialist need to inspect this, and was it invoked?
- Did behaviour, state, or release facts change, and did `noootwo-docs` place them?
- What risk or follow-up remains?

Then report: what changed, what was verified, what was documented, and what is still open.

**Done when:** all four answers are given and the report matches them.

## Rework

When the user rejects a previous attempt, diagnose the layer before changing anything:

| The failure looks like | Layer | Invoke |
| --- | --- | --- |
| They wanted something different, or the scope is wrong | product | `noootwo-product` |
| The direction or the visual language is wrong | design | `noootwo-design` |
| The intent was right and the execution is not | implementation | `noootwo-design` detail pass, or `noootwo-review` |
| Documents no longer match reality | docs | `noootwo-docs` |

State the layer in one line, then invoke. Do not polish the same layer again.

## Reference

- `references/workflow-playbook.md` — routing matrix, handoff packets, cost controls, and stop conditions.
- `references/project-skill-audit.md` — deciding which skills a project needs.
- `references/project-foundation-check.md` — checking process health and handoff readiness.
- `references/minimal-foundation-templates.md` — the smallest missing foundation files.
