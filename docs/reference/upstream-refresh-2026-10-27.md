# Upstream Skill Refresh, 2026-10-27

## Decision

Refresh the Noootwo skill model against current upstream practice and adopt only mechanisms that reduce a concrete failure without adding mandatory ceremony. The decision covers `noootwo-product`, `noootwo-design`, `noootwo-code-health`, and `noootwo-workflow`.

What would have flipped the decision: evidence that the proposed mechanisms mostly increase process cost, do not change observable agent behavior, or conflict with the Noootwo ownership model.

## Finding

Superpowers V7 did not replace its TDD, systematic-debugging, simplicity, and evidence-before-claims philosophy. Its meaningful evolution is a stronger collaboration and execution protocol: ground the first response in project evidence, replay intent, expose agent-selected defaults, approve a design before building, check a plan for unresolved decisions, and keep approved work moving through recorded rulings rather than routine re-approval.

Huashu Design 3.0 adds a complementary design mechanism: improve the candidate pool and show real artifacts instead of accumulating aesthetic prohibitions. Its strongest transferable idea is evidence-backed direction selection: cheap visual samples, same-medium references, inspected artifacts, factual linting, and an appearance record. Its full style library and heavyweight gates should not be copied.

The safe synthesis is proportional: keep TDD, verification, accessibility, real-state evidence, and separated review; replace non-safety aesthetic bans with evidence-dependent flags; require visual samples only when a direction choice is materially unresolved; and require a builder check only for non-obvious or expensive handoffs.

## Evidence

### Superpowers

- Repository and current release: `https://github.com/obra/superpowers`, `v7.0.0` on 2026-10-10 and `v7.0.1` on 2026-10-21. Current reviewed commit: `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`. Licence: MIT. Evidence level: repository, release source, and test/eval artifacts.
- README and skill sources continue to state TDD, systematic investigation over ad hoc fixes, complexity reduction, and verification before completion.
- V7 adds or sharpens: project-first intake, intent playback, one decisive question in the first exchange, explicit ownership of platform/language/library/medium choices, public agent-selected defaults, proportional ceremony, a fresh builder check, design approval before implementation, disposable spikes by default, decision-complete plans, `Review Focus`, compaction-safe progress ledgers, and rulings rather than stalls for reversible plan conflicts.
- Maintainer-linked eval evidence: 176 blind-graded conversations; design approved before build `1/24 -> 23/24`; step skipped without consent `24/24 -> 3/24`; first response prematurely settled implementation `24/24 -> 4/24`; request echoed back `0/24 -> 14/24`; spike/no-ceremony cases `15/16 -> 16/16`. Evidence level: maintainer-run eval, not independent replication.
- Counterexample: `technicalpickles/dotfiles#78` pinned `6.4.2` because V7's fixed opening interaction felt intrusive. `v7.0.1` moved back toward evidence-grounded first responses. This supports copying the mechanism, not the template.
- Do not copy: mandatory brainstorming for every creative task, fixed playback length, checkbox-like question formats, one subagent and one commit per task, full 15-skill ceremony, or `docs/superpowers/*` as project truth.

### Huashu Design

- Repository: `https://github.com/alchaincyf/huashu-design`; `v3.0.0` was released on 2026-10-17 and peels to commit `798c4235ebff03d5c45e3c8affdf5e9d18f9dfa7`. The default branch later advanced to `4fc7bfdbd5ec3fa2d43ce7a6433de60976a5e4b1`; that HEAD is not the reviewed release baseline. Licence: MIT. Evidence level: release tag, skill source, references, and visible case artifacts.
- The supplied WeChat article `https://mp.weixin.qq.com/s/gR3tDBD8-4hLJWj-x2b1Yw` redirected to a `wappoc_appmsgcaptcha` page with `环境异常` and a verification prompt; no article body was available. GitHub release evidence and the visible case artifacts were used as the fallback. This is recorded as an access limitation.
- Core philosophy: add better candidates and visible evidence rather than accumulating aesthetic bans. The author reports a small internal blind-test narrative: forced metaphor won 1 of 4, more bans won 0 of 2, options won 2 of 2. Evidence level: author-run, tiny sample; confidence in the numbers is low, confidence in the direction is medium.
- Mechanisms: three complementary candidate sources; cheap thumbnail exploration; three genuinely different directions; same-medium reference selection; capture and actually inspect the artifact; derive layout, type ratio, and palette proportion from observed evidence; reject broken or black screenshots as evidence; keep linting factual; evolve repeated solutions through `observed -> verified -> reference/check -> script -> engine default`; keep an appearance ledger.
- Visible cases inspected: a full-bleed museum artwork page with provenance; a birding app using real bird photography and a seasonal notebook grammar; a recipe app built like a book page with marginal notes; a long-scroll deck that locates each slide inside the original work. These demonstrate real assets and medium-native structure, not surface mimicry.
- Do not copy: the complete style library, mandatory six polished candidates, a universal three-direction hard gate, visual gates on every task, global memory by default, or the video/PPT/motion toolchain.

### Other Upstream Signals

- `pbakaus/impeccable` advanced from the locally recorded `v4.3.1` to `v4.7.0`; both `skill-v4.7.0` and `cli-v4.7.0` peel to `aeeb3d8c30b5f95aeeb3e893b0f1a308af8fdb8f` (2026-10-19). Relevant mechanisms: code-first skeletons for app screens and docs; direction cards the user can inspect; familiar controls for work surfaces with one branded signature detail; real work visible on landing first screens; actual touch/device verification; and progressive disclosure instead of banner-heavy instruction.
- `emilkowalski/skills` added useful worst-case-data, mobile-native, and animation-performance checks. These are recorded as secondary P2 opportunities, not adopted in this pass.
- `mattpocock/skills` and `anthropics/skills` did not add a mechanism that changes this pass's ownership or routing decisions.

## Mechanism

- Product: grounded first response; facts versus proposals; how-decision ownership; one decisive question when one gap controls the build, while retaining the existing one-round frontier for multiple independent gaps.
- Design: options over bans; real low-cost samples before an unresolved direction choice; same-medium references; inspected-artifact evidence; factual linting; evidence-dependent aesthetic flags with non-negotiable accessibility and state-integrity floors.
- Implementation: a fresh builder check for non-obvious or cross-session handoffs; a plan that records interfaces, assertions, verification, review focus, and rulings; reversible plan conflicts are resolved and recorded instead of restarting approval.
- Persistence: deep research and ADRs go through `noootwo-state`; a project-local appearance ledger is the future P2 location, never silent global memory.

## Boundary

- The Superpowers eval is a maintainer artifact and does not establish universal gains.
- The Huashu test story is too small to prove aesthetic superiority; it supports candidate diversification and artifact evidence only.
- The Noootwo package already has three-direction exploration, Style Evidence Check, reference capture, artifact review, facts-first product work, and proportional routing. The adoption must strengthen these rather than duplicate them.
- `noootwo-design/SKILL.md` and reference budgets are nearly full; update existing references rather than adding another default gate or style library.
- Safety, accessibility, real content, readable type, and complete interaction states remain hard gates. A deliberate cream palette, system display face, gradient, or numbered marker can pass when the artifact supports it and it causes no actual harm.

## Counterexample

- Fixed first-response scripts can become formulaic and intrusive; V7.0.1 had to correct this.
- More aesthetic rules can produce pale, cold, overly tidy work and still converge on a shared safe mean.
- Full design-direction ceremony taxes quick or already-settled work.
- A global appearance memory can create privacy, portability, and accidental homogenization risk.

## Confidence

- Superpowers collaboration mechanism: medium. Strong repository evidence and visible eval artifacts, but maintainer-run and not independently replicated.
- Huashu options-over-bans mechanism: medium. Clear repository philosophy and visible cases; the quantitative blind-test narrative is low-confidence, author-run evidence.
- Impeccable design mechanisms: medium. Current repository and release evidence, with limited independent outcome data.
- Overall adoption decision: high for preserving safety floors and proportionality; medium for expected behavior improvement until the new evals run.

## Adoption

- P0: grounded Product response, how-decision ownership, visual direction samples, same-medium inspected evidence, evidence-dependent aesthetic flags.
- P1: conditional Builder Check, decision-complete plan record, `Review Focus`, ruling ledger.
- P2, deferred: project-local `.noootwo/appearance-ledger.md`, worst-case-data scenarios, real touch/device checks, stronger standard controls for tool surfaces.

Rejected: mandatory fixed opener, mandatory six polished directions, universal full ceremony, global appearance memory, an expanded style library, or claiming UI-quality improvement without paired artifacts and evaluation.

## Open

- Run the new behavior probes against baseline and candidate skill sets before treating the mechanisms as measured improvements.
- Re-check Superpowers and Huashu releases before the next durable refresh; both projects are moving quickly.
