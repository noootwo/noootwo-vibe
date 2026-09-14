# Evidence Chain

The artifact that closes Gate A. It is short on purpose: if it does not fit on one screen, the investigation is not finished.

## The chain

```
Symptom:      <observed behaviour + the raw failure line>
Repro:        <exact command> → <observed output / exit code> (reliable | n/10)
Localized:    CP01 … CPnn — first checkpoint where actual ≠ expected
Cause:        <A → B → C, ending in the symptom>
Discriminate: <the cheapest experiment that would refute the cause>
Result:       <what actually happened>
Falsified:    <competitor> — refuted by <experiment>
Toggle:       <revert → symptom returns; restore → symptom goes>
Scope:        <files / behaviour allowed to change>
```

## What counts as a link

A link holds two things: the action, and real output from the action. Reasoning without output is a note, not a link.

- Quote the failing assertion, the exit code, the log line, the file and line you read. Kept short, kept exact.
- Label every claim `[observed]`, `[inferred]`, or `[assumed]`. An `[assumed]` inside the chain is a hole.
- Record what you expected to see before you look. A checkpoint without a prediction cannot disagree with you.
- Write down refutations. They stop the next person — often you, an hour later — from re-testing a dead theory.
- Timestamp observations when order matters; two facts in the wrong order produce the wrong cause.

## The coverage test

List every fact you observed, including the ones that do not fit: it only happens on Tuesdays, one customer, the second request, after a restart. Tick each one the cause explains.

An unticked fact means the chain is incomplete, not approximately right. Either extend the cause or keep investigating — a cause that explains most of the evidence is a coincidence with good PR.

## The toggle

The cheapest causality proof there is, and the step that gets skipped.

- **Code fix** — stash or revert the change, run the repro, restore the change, run it again.
- **Config or data fix** — point the value back at the old one and re-run.
- **Cannot revert in place** — run the repro against the pre-fix commit in a separate worktree.

Record both runs. If the symptom does not flip, the cause is wrong or there is a second one; reopen Gate A rather than adding another change on top.

## Worked example

```
Symptom:      Settings shows "0 selected" after a reload although the choice persisted.
Repro:        npm test -- settings-store  → 1 failing, 8/8 runs, ~2s
Localized:    CP01 store.load() reads 3 rows from disk          ✓
              CP02 store.normalize() returns []                 ✗
Cause:        normalize() drops entries whose id is a number; persisted ids are numbers
              → loaded list is empty → the view renders 0 selected.
              The write path was never wrong; the reader's schema assumption was.
Discriminate: feed normalize() a hand-written payload with numeric ids.
Result:       returns [] — the cause survived. The failing behaviour moved to the reader.
Falsified:    "the writer saves an empty list" — refuted by CP01 reading 3 rows from disk.
Toggle:       restore the numeric-id branch → passes; revert → fails again.
Scope:        src/store/normalize.ts only; no change to the persistence format.
```

Note what the chain rules out. "The writer saves nothing" was the intuitive cause, and CP01 killed it for the cost of one log line. That is the whole point of tracing the path in one pass.

## Shortcuts and what they cost

| Shortcut | Cost |
| --- | --- |
| Read the symptom, pattern-match a familiar cause, edit | fixes a bug that may not be this one |
| "It's probably X" | no experiment, no proof, no chain |
| Change three things, run once | nothing learned about which one mattered |
| Suppress the symptom — catch and ignore, add a retry, raise the timeout, add a null guard | a loud bug becomes a silent one, further from its cause |
| Fix at the point of the crash | the cause stays upstream and returns through another path |
| Keep a test that passes both ways | it tests nothing and it will hide the next regression |
| Skip the toggle because the fix "obviously" worked | throws away the cheapest proof available |

## When evidence is genuinely unavailable

No logs, no repro, no access: the chain has a named gap, and that is an honest result.

Report the gap explicitly — what you could not observe, what you tried, what would close it. Then choose between instrumentation now (log the boundary, wait for the next occurrence) and a scoped mitigation that stops the damage without claiming to be the fix. Never present the best-supported guess as a proven cause; that is the failure this chain exists to prevent.
