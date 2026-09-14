# Hypotheses

Use this when hypotheses multiply, the failure will not reproduce on demand, or three have already been refuted.

## The ledger

One block per hypothesis. Write it before investigating, not after:

```
H1: <falsifiable statement about the cause>
    predicts:   <what I will observe if this is true>
    refuted by: <what I will observe if this is false>
    test:       <cheapest experiment that separates the two>
    result:     CONFIRMED <evidence> | REFUTED <what I actually saw>
```

Two rules make the ledger work:

- **State the refuting observation first.** A hypothesis you cannot falsify is a belief. Writing "here is what would prove me wrong" before looking is what keeps the search honest.
- **Prefer the cheapest discriminating test, not the most likely hypothesis.** Order the ledger by how fast a test separates candidates, not by how plausible they feel.

Record refutations. The ledger's job is to make `RULED OUT` a real list, so nobody re-tests a dead theory at hour three.

## Designing the experiment

- One variable. Two changes at once cannot tell you which one mattered.
- Aim to refute. A test that passes for three different reasons has taught you nothing.
- Prefer a test that moves the failure. "It stopped happening" is weak; "the failure moved from CP03 to CP05" is a measurement.
- Predict before running. Write the expected output down; a result with no expectation cannot disagree with you.
- Note the cost. A two-second repro supports fifty experiments; a five-minute one supports six, and after six you will start guessing to save time.

## Assumption audit — run at three refutations

When three hypotheses die, the problem is usually a false premise rather than a missing idea. Interrogate the ground:

- Is this the code that actually ran — branch, commit, uncommitted change, a shadowing duplicate file?
- Is the build fresh — dist artifacts, caches, `node_modules`, `__pycache__`, a Docker layer, a service worker, a CDN copy, a hot reload that did not reload?
- Is it the right process, port, container, region, or instance, and am I reading the logs from the one that failed?
- Which config actually loaded, and is the value visible to the process rather than only to my shell?
- Is the failure even mine — dependency, proxy, platform, or the test itself?
- Is the test wrong, or asserting the wrong thing, or passing for the wrong reason?
- Did I misread the requirement — is this behaviour actually correct?
- Did a dependency, API, or schema change under me?

Then re-read the original error literally, word by word. Most long debugging sessions are one unexamined `[assumed]` wearing an `[observed]` badge.

## Intermittent failures

Intermittent is a measurement problem before it is a cause problem.

- Measure the rate: loop the repro, count failures out of ten or a hundred.
- Suspect, in order: execution order, time and timezone, concurrency, shared mutable state, resource limits, network, cache warm-up.
- Log with timestamps and identifiers so runs can be correlated rather than guessed at.
- Hunt for a starting state that makes it deterministic — run it single-threaded, fix the clock, seed the random, empty the cache. A deterministic repro is worth a week of speculation.

## Escalating instead of thrashing

Past roughly six refuted hypotheses, or when experiments start repeating, stop and report:

```
Confirmed:  <what the evidence already proves>
Ruled out:  <hypotheses and the experiment that killed each>
Remaining:  <top candidates, ranked by cost of the next discriminating test>
Needed:     <access, logs, a reproduction, a decision>
```

This is a complete result, not a failure. Continuing to guess spends the user's time to avoid saying "here is the boundary of what the evidence supports".
