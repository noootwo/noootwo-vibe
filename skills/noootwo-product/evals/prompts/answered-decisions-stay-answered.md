# Eval: Answered decisions stay answered

Prompt: a product interview already answered two rounds. Round 1 settled
`balance_placement: 账号行内常显` and `onboarding_shape: 轻量三步引导`; round 2
settled `quota_retry: 充值后手动再发`. New exploration now surfaces one genuinely
new independent decision about the empty-model state.

Expected:

- Recomputes the frontier as answerable-now minus answered, and asks only the
  new decision id.
- Recites the settled list as `id: answer` lines before the question.
- Keeps the answered wording and options frozen; the new question does not
  reopen or relabel them.
- Records the new answer with its id when it arrives.

Fails when: it re-asks `balance_placement`, `onboarding_shape`, or `quota_retry`;
it presents regenerated options for an answered id; it drops the settled list
from the round; or it treats an earlier answer as an open preference.
