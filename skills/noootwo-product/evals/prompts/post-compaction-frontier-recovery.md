# Eval: Frontier recovery after compaction

Prompt: the session re-entered after a compaction. The summary lists
`balance_placement` and `onboarding_shape` under "still needs confirmation",
but the recited ledger shows `balance_placement: 顶栏胶囊 + 账户菜单` and
`onboarding_shape: 轻量两步`, both answered, plus one untouched decision about
backend scope. The user says "继续".

Expected:

- Rebuilds the frontier from the ledger and current artifacts; the summary is
  treated as a lead, not authority.
- Re-asks nothing that has a ledger answer and corrects the summary in the
  recap.
- Asks only the genuinely open decision, reciting the settled list first.

Fails when: it repeats the summary's open list; it re-asks an answered decision
to "confirm" it; it silently drops a settled entry; or it restarts discovery
from the beginning.
