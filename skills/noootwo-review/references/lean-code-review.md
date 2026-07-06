# Lean Code Review

Use this when reviewing over-engineering, code bloat, redundant abstraction, avoidable dependencies, or AI-generated code expansion. This is inspired by Ponytail's seven-rung minimal-code ladder, adapted for Noootwo Review.

## Goal

Find code that can be deleted, reused, replaced by existing capability, or collapsed without weakening correctness. The best result is not the shortest code; it is the smallest code that preserves the required behavior and safety.

## Seven-Rung Check

Stop at the first rung that solves the real requirement:

1. `delete`: Does this need to exist for the current request? If it is speculative, remove it.
2. `reuse`: Does this project already have a helper, type, component, pattern, or base class? Reuse it.
3. `stdlib`: Does the language standard library cover it? Use the standard API.
4. `native`: Does the platform already provide it? Use browser, OS, database, framework, CSS, HTML, or runtime capabilities.
5. `installed-dep`: Does an already-installed dependency solve it? Use it before adding another dependency.
6. `shrink`: Can fragmented code be merged while staying readable? Collapse needless wrappers, one-use functions, and scattered glue.
7. `minimum`: Only then write the smallest new code that runs and can be verified.

Run the ladder after understanding the task and the actual code path. A tiny change in the wrong layer is still a defect.

## Safety Floor

Never recommend deleting:

- input validation at trust boundaries
- error handling that prevents data loss or hides failures safely
- authentication, authorization, injection protection, or other security checks
- accessibility behavior and semantic UI needed by users
- business invariants, assertions, and data integrity checks
- the smallest test or self-check that proves non-trivial logic
- behavior the user explicitly requested

If code looks verbose but protects one of these, mark it `safety-keep` or leave it out of lean findings.

## Lean Finding Tags

| Tag | Use when | Replacement |
| --- | --- | --- |
| `delete` | dead code, speculative option, unused feature | nothing |
| `reuse` | equivalent project code already exists | named local helper/module |
| `stdlib` | hand-rolled behavior exists in standard library | named standard API |
| `native` | custom/dependency code duplicates platform capability | named platform feature |
| `installed-dep` | new dependency duplicates an existing installed dependency | existing package/API |
| `yagni` | abstraction, config, factory, adapter, or layer has one real use | inline or defer |
| `shrink` | same behavior can be expressed with less scattered code | shorter local form |
| `safety-keep` | apparent bloat is required for safety or correctness | keep, with reason |

## Output Contract

```markdown
Lean Findings
- [tag] path:line
  Cut/keep: what changes.
  Why: concrete redundancy or safety reason.
  Replacement: smallest replacement, or `none`.
  Verification: command/test needed, or `covered by existing check`.

Net Reduction Estimate
- lines: -N possible, or `not estimated`
- dependencies: -N possible, or `none`

Honesty Boundary
- Do not claim current-repo token, dollar, or speed savings without a measured baseline.
```

If there is nothing safe to reduce, say `Lean already. Ship.` and still list any verification gaps.

## Review Method

1. Read the changed code, nearest callers, imports, dependency manifest, and tests.
2. Identify required behavior and safety constraints before flagging removals.
3. Apply the seven-rung check in order.
4. File only findings with a concrete smaller replacement or a clear `safety-keep` reason.
5. Separate lean findings from correctness findings; use the normal review output for correctness bugs.

## Common Mistakes

- Replacing required validation with fewer lines.
- Calling code bloat just because it is unfamiliar.
- Recommending a standard API without checking project runtime support.
- Adding a new dependency to reduce local code.
- Estimating token or cost savings for the current repo without a measured before/after baseline.
