# Mandate Gate

Decide what the request authorizes before any owner matches or any file changes. A problem report is evidence about a layer, not an order to change it.

## Name the mandate

Write one line at intake:

```
Mandate: answer | diagnose | propose | edit | publish
Basis: <the user's words that grant it>
```

- `answer` — respond from what is already known; no reads and no writes.
- `diagnose` — read-only evidence; no writes.
- `propose` — read and draft, then stop; no writes.
- `edit` — local edits inside the named scope.
- `publish` — push, protected-main integration, tag, or publish.

Each level authorizes only its own actions. `propose` includes reading but not editing. `edit` never includes `publish`.

A statement, opinion, complaint, question, or request to confirm/review/explain defaults to `answer` or `diagnose`. A change request whose result is not already settled defaults to `propose`. `edit` requires both an explicit mandate and a diff summary that needs no invented decision.

## The diff-summary test

Before the first write, write the change as one sentence:

`<file or region> + <what changes> + <observable result>`

- If the sentence needs "or", a new product, visual, copy, or structure choice, a new element, or an acceptance you cannot state, the mandate is `propose`.
- If you can write it verbatim, and the user could not reasonably answer "I did not ask you to change that", the mandate is `edit`.
- If the mandate cannot be read, fail closed: take the lower level and present a proposal.

Two conditions authorize `edit` without a proposal:

1. The user granted free rein — "直接做", "你定", "自由发挥", "不用问我" — or named the exact change and said to do it.
2. The request names the target, the change, and the observable result, and no material choice remains.

An open-ended grant records its delegated scope and the stop boundaries that still apply: irreversible migration or data loss, security or privacy impact, external side effects or spend, and publication.

## Propose

```
Understanding: <the problem in the user's words>
Mandate: answer | diagnose | propose
Approach: <3-5 one-line steps>
Will change: <files or behaviour>
Will not change: <explicit scope cut>
Acceptance: <what will be observable>
Ready when you confirm; tell me which line to change.
```

- One proposal per turn, not an interview.
- Ask at most three questions, each with a recommendation, and only when the fork changes what gets built.
- An abstract complaint gets two or three candidate causes, the cheapest check for each, and one recommendation.
- End the turn after the proposal. No write may occur in the same turn that presents it.

## Approve

- Approval exists only when the proposal's remaining question is go/no-go. "继续", "可以", "执行", "按这个来" then approve it.
- If a decision is still open, "继续" is not an answer; ask the open question once.
- Approval covers the presented scope only. A new file, behaviour, visual direction, or public copy is a new scope and returns to the gate.
- Inside approved scope, reversible detail is a `Ruling`, not a new approval.

## Cost

The gate costs one line, and one short proposal only when it fires. Keep the cheap path cheap:

- Skip the proposal when the diff-summary test passes.
- Do not ask again after approval.
- Do not attach a plan to a one-line fix.
- Do not restate the request as a questionnaire.
- Do not treat a critique as a work order.

## Close

Before reporting done, answer: "What mandate did this turn carry, and did every write stay inside it?" A turn at `answer`, `diagnose`, or `propose` ends with zero writes.
