---
name: noootwo-product
description: "Use before design or build when user, first loop, scope, main path, states, or acceptance are unsettled; also for new ideas, feature lists, backend flows, and auditing existing UX."
---

# Noootwo Product

Settle what should exist before anything is designed or built. This is a product decision navigator, not a PRD generator.

## The flow

### 1. Read what is already true

Read the request, `AGENTS.md`, README, `docs/status.md`, active specs, screenshots, analytics, and the current UI. Note the real user, scenario, outcome, constraints, and what is still unknown.

Finding facts is your job. Ask the user only for decisions. When a fact exists only outside the repository — a competitor's behaviour, a user expectation, prior art — invoke the `noootwo-research` skill: read its `SKILL.md` and follow it.

**Done when:** every discoverable fact bearing on the next step has a source, or is recorded as not found.

### 2. Check what is settled

A decision is **settled** when it is made and confirmed; otherwise it is **unsettled**. Check these in order, skipping whatever the request or the repo already settles:

real user and moment of use → outcome → first loop → scope and non-goals → main path → interaction and state behaviour → observable acceptance.

**Done when:** you can name every unsettled decision, or state that none remain.

When none remain, produce a `Product Checkpoint` from `references/product-flow.md` and stop.

### 3. Grill the frontier

The **frontier** is every decision that is answerable now, because its prerequisites are settled.

Ask the whole frontier in one round. For a single unsettled decision, one question is the round.

Format each question:

```
❓ **Q1 - <title>**: <the decision, with 2-3 options>

➡️ <your recommendation, and why>
```

Separate questions with a horizontal rule, and open the round with a short recap of what is already settled.

Then wait. A request to build, start, or continue is not an answer; only an explicit choice or explicit delegation settles a decision. Record a delegated decision as an assumption.

After the answers, recompute the frontier. Settled decisions unblock their dependents; keep a dependent question parked until its prerequisite is answered. Ask the next round only once the previous one is answered.

**Done when:** the frontier is empty — every decision is settled, delegated, deferred, rejected, or carried as a named risk.

### 4. Confirm shared understanding

Summarise what is settled, what was assumed, what is deferred, what was rejected, and any risk still carried. Then say the check in plain words: this first loop solves X for Y, and deliberately does not solve A or B.

Ask once whether that matches what they meant. On no, reopen only the mismatched branch.

**Done when:** the user confirms the summary, or delegates the final call.

### 5. Hand off

Produce the `Product-to-Design Handoff` from `references/product-flow.md`: real user, scenario, main path, states, scope cuts, acceptance criteria, open decisions, design constraints.

Hand off when every material decision is settled or delegated and no carried risk would change the main path, trust boundary, scope, or acceptance.

When UI work is next, invoke the `noootwo-design` skill: read its `SKILL.md` and follow it.

## Existing-flow audit

When the user asks to audit, critique, or fix an existing onboarding or product flow, read `references/product-audit.md` after the current facts are clear. Capture the flow before judging it, keep every finding tied to a step, and separate product-flow friction from visual or code defects.

## Reality check

Read `references/product-reality-check.md` when the loop is unproven, the user is confused, or the direction has already been rejected once.

## Rules

- Start from the user's situation and vocabulary, not the database model or the requester's preference.
- Treat `should not exist` as a first-class decision.
- Prefer progressive disclosure over exposing every capability at once.
- Make empty, error, permission, and success states name the next action.
- Treat strong criticism as evidence about which layer failed, and name that layer before changing anything.

## Reference

- `references/product-flow.md` — decision layers, grilling detail, and the Product Checkpoint, Discovery, Choice Challenge, and handoff templates.
- `references/product-reality-check.md` — the check for unproven, confusing, or rejected product paths.
- `references/product-audit.md` — minimum brief, project-local product context, and existing-flow audit for onboarding and product surfaces.

## Return

When the request is not a product decision, name the layer and invoke the owner in one hop: `noootwo-debug` for a failure, `noootwo-research` for outside evidence, `noootwo-design` for a visual system, `noootwo-code-health` for code or performance judgment, `noootwo-onboard` for an unfamiliar project.

Missing skill fallback: first try `npx -y skills add noootwo/noootwo-vibe --global --agent codex --skill <name> --yes`; if install fails, take the smallest direct fallback and mark the record `skill-missing: <name>` (for persistence, write the owning file directly).
