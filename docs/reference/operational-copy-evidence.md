# Operational Copy And Self-Reference

Use this when changing how Product or Design decides what visible product copy
may exist, especially after a layout, readability, or hierarchy request. It is
a research record, not a universal copy checklist.

## Decision

Should Noootwo treat operational product copy as a separate audience decision
from design rationale, change summaries, proof of improvement, and marketing or
expressive copy?

**Would flip:** evidence that users benefit from on-surface explanation of a
redesign or the agent's reasoning, or that an account, settings, admin,
inspector, or configuration surface needs a slogan to be understood.

**Not enough:** a single screenshot, a taste preference, or generic advice to
"keep it minimal".

## Finding

Yes. The reviewed skills converge on four mechanisms:

1. Words exist to help the user understand and use the product. They are design
   material, not decoration or a place for the maker's voice.
2. Say each idea once. A heading, label, and note should not narrate the same
   structure three times.
3. Every visible element earns its place. Do not invent new paragraphs, claims,
   pages, or data unless the user needs them.
4. Operational headings name the object, task, state, or next action. Slogans,
   quality claims, and model-sounding thoughtfulness belong outside operational
   UI.

The practical conclusion is stronger than "write shorter copy": a layout-only
request changes structure, not public content. If grouping and hierarchy are
good, the page does not need a headline saying it is clear. If the structure is
not obvious, fixing the structure is the remedy, not explaining it in a note.

Marketing and launch surfaces can carry expressive language because their job is
to create interest. Even there, the reviewed skills prefer one claim tied to
real evidence over a pile of adjectives. The same language does not transfer to
account, settings, admin, inspector, or configuration surfaces.

## Evidence

### Agent skills

**Anthropic `frontend-design`**
(`https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/frontend-design/SKILL.md`,
public, Apache-2.0, commit `e4bb5d960d87126ff3b3a8af1a104b7db67560ba`,
reviewed 2026-11-19).

Mechanism: words exist to make the interface easier to understand and use; name
things by the user's understanding, not the system's construction; describe
rather than sell; let each written element do one job; avoid unnecessary
typographic labels.

Boundary: expressive brand and marketing pages can have a point of view, but the
same license does not extend to operational screens. The source also supports
real guidance for errors and empty states.

**Impeccable** (`https://github.com/pbakaus/impeccable`, `skill-v4.11.0`,
Apache-2.0, reviewed at commit `88cfafae649164e6dc48b88d3c0c1bf6662eaade`,
rechecked 2026-11-25; 113,304 GitHub stars on 2026-11-19).

Mechanism: audit redundant headings, intros, helper text, and confirmations;
say each idea once; when a heading already explains the state, an introduction
must add new information or disappear. Its craft floor treats copy as the
product's own language, with controls naming their action and errors naming the
problem and recovery.

Boundary: it does not ban all guidance. Help remains useful at a decision point,
especially for unfamiliar or consequential controls.

**Huashu Design** (`https://github.com/alchaincyf/huashu-design`, `v3.3.0`,
MIT, commit `e8d1148a80d5a281d4247cffe320add3df017928`, 29,875 GitHub stars
on 2026-11-19).

Mechanism: do not add filler to make a page feel full; ask whether removing an
element makes the information less clear; do not unilaterally add content such
as paragraphs, pages, claims, or data. Layout, graphics, motion, and assets are
design work; new content is a user-owned decision.

Boundary: this is not a prohibition on all new copy. A designer may write copy
when the request or user need calls for it. Huashu targets prototypes, decks,
and visual artifacts and explicitly excludes backend Web Apps; only its
subtraction and content-ownership mechanism is borrowed here, not its flow
authority.

**Taste Skill** (`https://github.com/Leonxlnx/taste-skill`, `tasteskill 2.5.1`,
MIT, commit `f6b76575f949707b4e3c37cd86cb44b0b98643e8`, 118,776 GitHub stars
on 2026-11-19).

Mechanism: the page heading names the category; no slogans or boasts in the
hero; no invented proof; no filler verbs; one brand line at most and never as
the heading; copy is read aloud and audited for the model's default voice.

Boundary: it is a marketing-page skill. Its "one brand line" exception is not a
template for account or settings screens.

**Antfu Design** (`antfu-design`, installed release `2026.06.22`; reviewed
from the local skill source, with no independently verified commit pin).

Mechanism: before shipping, re-read every visible string; flag text that reads
like the model trying to sound thoughtful; replace it with plain functional
sentences; prefer boring and correct over cute and wrong.

Boundary: it is a copy self-audit, not a product-scope decision. Product still
decides whether a string should exist.

### Community fix patterns

**`Akagilnc/ak-ai-vela` PR #29**
(`https://github.com/Akagilnc/ak-ai-vela/pull/29`, 2026-04-20) rewrote
generated trait-quiz copy after repeated user-facing AI-slop findings. The fix
removed repeated openers, generic praise, contrast tics, and repeated cadence,
while preserving concrete behavioral anchors. Its review loop treated the
rendered strings as the artifact, not as a side note to the code change.

**`baanish/agent-render` PR #24**
(`https://github.com/baanish/agent-render/pull/24`, 2026-03-27) removed
AI-generated visual patterns and also shortened and clarified headings,
buttons, and empty-state text. The useful mechanism is that de-slopping was
not a restyle: copy and structure were corrected together.

**`JovieInc/Jovie` PR #13927**
(`https://github.com/JovieInc/Jovie/pull/13927`, 2026-07-10) reduced repeated
free-profile claim copy to one claim treatment, one proof line, and one action.
That is evidence for the marketing surface only: one claim with evidence can
work; repeating the claim does not.

**Hacker News, "Do they know we can tell it's AI slop?"** (2026-05-28, 11 points,
13 comments, `https://news.ycombinator.com/item?id=48303252`) is a weak signal
that recognizable AI prose damages trust. It is about business communication,
not UI comprehension, so it does not decide this rule; it only supports the
warning against model-default phrasing.

### Existing UX evidence

The accepted audience evidence in
[audience-language-evidence.md](audience-language-evidence.md) independently
supports the same boundary: plain language helps experts too; unexplained notes
and internal terms are defects; users should not need a tutorial to understand
the first screen; and a visible note needs a decision, consequence, recovery,
or term-teaching job. NN/g's mental-model guidance adds the important
counterpoint: explanation cannot replace a familiar interaction model.

## Adopted mechanisms

1. **Copy audience split.** Product content serves the primary user.
   Implementation evidence is allowed only when it supports a user decision.
   Design rationale, change summaries, proof of improvement, evaluation notes,
   and task instructions stay in the handoff, review, docs, or reply.
2. **Layout is not content permission.** A layout, hierarchy, or readability
   request changes structure. New visible copy needs its own user need.
3. **Operational titles name the object or task.** "Account information" is a
   title; "Your information, clear at a glance" is a claim about the redesign.
4. **Notes must add information.** Delete a note that restates the heading,
   label, layout, or state. Keep contextual guidance when it prevents an error,
   explains a consequence, supports recovery, or teaches a term needed now.
5. **Clarity is structural.** Grouping, hierarchy, alignment, spacing, labels,
   and state behaviour demonstrate the improvement. A quality claim does not.
6. **Surface register is explicit.** Marketing or launch surfaces may use one
   expressive line with evidence and a user-facing purpose. Operational
   surfaces use plain task language.

## Rejected alternatives

- **Add a UX-writing skill.** Copy is part of the interface. Product owns the
  audience and whether a string should exist; Design owns the rendered copy and
  comprehension review.
- **Ban all notes and headings.** Permission, security, destructive actions, and
  unfamiliar terms still need guidance. The rule is job and placement, not a
  blanket ban.
- **Put the redesign rationale on the page as transparency.** The requester
  already knows the page was redesigned; the user needs the current task.
- **Replace a removed slogan with friendlier copy.** A synonym does not remove
  the audience error.
- **Add a string blacklist.** Phrases such as "clear at a glance" are examples,
  not a complete detector. A fixed list would be locale-specific, brittle, and
  easy to evade; the review gate checks the audience and job instead.
- **Copy upstream prompts or surface style.** Only the repeatable mechanisms are
  adopted.

## Boundaries and counterexamples

- Technical, regulated, or specialist products need domain terms and guidance.
  Put guidance at the decision point or behind one clear second layer; do not
  narrate the whole page.
- Permission, privacy, security, payment, destructive-action, and recovery
  states need consequence and next-action copy. This is user information, not
  design rationale.
- Legal, consent, compliance, and localization text may be required even when
  it is not pretty; required meaning stays.
- A marketing or launch page may carry one brand line with real product
  evidence. That exception does not transfer to account, settings, admin,
  inspector, or configuration surfaces.
- A note that teaches a term needed now is valid. A note that explains how to
  read an otherwise clear page is not.

## Confidence

- **High:** operational copy should address the primary user; redundant headings
  and self-referential copy are defects; clarity is structural.
- **Medium:** the exact boundary between necessary contextual guidance and
  page narration in specialist products.
- **Low:** any claim that this change reduces rework, time, or token cost. The
  new eval contracts have not run in fresh model sessions.

## What remains unproven

The product and design eval contracts are structural. A fresh-session run against
a no-skill baseline is still required before claiming a behavior, quality,
speed, or rework improvement.
