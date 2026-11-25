# 0036 — Mandate gate before any write

## Status

Accepted on 2026-11-25 as the candidate for workspace `0.36.0`.

## Context

The suite had no intake decision between "the user described a problem" and
"the agent changed files". Two rules produced that gap:

- `noootwo-workflow` treated a completed Fan-out Gate as plan acceptance:
  "The recorded Gate result completes the plan; only then is it accepted and
  execution-ready", and "Plan acceptance authorizes local implementation".
  The acceptance was the agent's own; no human token was involved.
- User acceptance existed only at the publication boundary — push,
  protected-main integration, tag, or publish. Local edits were implicitly
  authorized by arriving at an owner.

The reported failure is therefore structural, not a tone problem: a statement,
question, or critique matched an owner, the owner found work to do, and the
turn ended with a diff instead of a proposal. The same symptom appears in
public reports; `openai/codex` #2101 describes an agent that "will often dive
into making changes right away and lacks a good way to manage or edit a plan
before executing".

## Decision

1. Every request names one mandate before owner matching:
   `answer | diagnose | propose | edit | publish`. Each level authorizes only
   its own actions; `propose` may read and plan but writes nothing, and `edit`
   never includes publication.
2. Classification uses the **diff-summary test**, not confidence or tone.
   Before the first write, state `<file or region> + <what changes> +
   <observable result>`. A sentence that needs "or", a new product, visual,
   copy, or structure choice, a new element, or an acceptance the agent cannot
   state is `propose`. If the mandate cannot be read, the gate fails closed to
   the lower level.
3. `edit` is direct only under the user's two conditions: an explicit free-rein
   or exactness grant, or a request that names target, change, and observable
   result with no material choice left.
4. A proposal is one short block — understanding, mandate, approach, will
   change, will not change, acceptance — and the turn ends after presenting
   it. At most three questions, each with a recommendation; an abstract
   complaint gets candidate causes and the cheapest check before a proposal.
5. Approval requires that the proposal's only remaining question is go/no-go.
   "Continue" is not an answer while a decision is open. Approval covers the
   presented scope; new scope returns to the gate; reversible detail inside
   the approved scope stays a `Ruling`.
6. `noootwo-workflow` owns the gate through Step 0 and
   `references/mandate-gate.md`. `noootwo-design`, `noootwo-code-health`,
   `noootwo-tdd`, `noootwo-debug`, and `noootwo-product` carry one entry
   pointer each, because each is reachable directly. `noootwo-ask` explains
   the vocabulary to the human.
7. No new skill, no schema change, no host feature dependency, and no change
   to the public set of twelve. The cost is one intake line, plus one short
   proposal when the gate fires.

## Research basis

Official and community mechanisms converge on separating deliberation from
write authority:

- Claude Code documents plan mode as reading and proposing but making "no
  edits until you approve", and recommends interviewing until a spec exists
  before building in a fresh session.
- Cursor's Plan Mode produces a reviewable plan and builds only when the user
  clicks to build; it also names the cheap path for quick changes.
- Kiro's Specs use approval gates between requirement, design, and task
  phases, with `Quick Spec` as an explicit gate-free mode.
- GitHub Spec Kit states that "a decision to proceed does not automatically
  start implementation".
- Microsoft HAX Guideline 10 requires disambiguation or graceful degradation
  when the user's goal is uncertain: "in ambiguous situations, less can be
  more".
- The OpenAI Agents SDK marks approvals per tool call and fails closed when
  arguments cannot be inspected — the transferable rule is fail-closed
  authority, not the SDK surface.

The counterexample matters: Armin Ronacher's analysis of plan mode, and tools
that removed it, show that a host UI mode is not required. A reviewable plan
plus an explicit go is the portable mechanism, which is what this decision
implements.

Full source levels, boundaries, and access limits live in
[`docs/reference/mandate-gate-evidence.md`](../reference/mandate-gate-evidence.md).
No controlled study measures this gate; adoption rests on the local failure,
the recurring public symptom, and mechanism-level official guidance. No
quality, speed, or token improvement is claimed.

## Rejected alternatives

- **A thirteenth `noootwo-plan` skill.** The public set is fixed and the gate
  is a routing decision, not a capability with its own artifact.
- **Depending on a harness plan mode.** Availability differs by harness and
  version, and the official Codex manual was unreachable during this pass
  (HTTP 403). The rule must work in any harness.
- **Requiring a proposal for every change.** This adds ceremony to one-line
  fixes and trains the user to approve reflexively. The diff-summary test
  keeps the cheap path cheap.
- **Keyword-based detection of complaints.** The suite already rejects
  routing from keywords alone; wording is a signal, the diff summary decides.
- **Treating "continue" as approval while a decision is open.** That is the
  re-ask/drift failure ADR-0032 already closed on the product side.
- **A global always-on rule outside the skill package.** It would not be
  versioned with the suite; the installed skills and the nearest `AGENTS.md`
  carry the rule instead.

## Consequences

- A statement, critique, or question now ends at a proposal with zero writes.
  The user pays one short read and one reply before implementation starts.
- Approved work does not re-ask for reversible details; the existing `Ruling`
  mechanism absorbs them.
- The gate adds one line to every workflow turn and one bullet to five
  specialist bodies. Four of those bodies sit at or near the 120-line cap, so
  the change includes compression rather than appended prose.
- Residual risk: the model can classify `edit` too eagerly. The eval contracts
  cover the four observable failure modes; the behavioral improvement still
  needs a fresh-session paired run.

## Verification

- `python scripts/validate_skill_workspace.py .` enforces the description,
  line, reference, and capability-map budgets after the edits.
- Six new eval contracts in `skills/noootwo-workflow/evals/prompts/` cover
  observation-without-write, vague change, explicit edit, open grant,
  approved-scope ruling, and "continue" without a decision.
- The release record holds the validator, discovery, eval-structure, and
  install evidence for the exact commit.
- Behavioral proof — a fresh-session baseline versus the new skill — remains
  open and is named as a gap until measured.
