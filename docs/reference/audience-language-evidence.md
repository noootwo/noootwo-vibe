# Audience, Language, And Information Exposure

Use this when changing how Product or Design decides audience-derived density,
vocabulary, settings, or technical-detail placement. It is a research record,
not a product brief and not a universal UI checklist.

## Decision

Should Noootwo make the primary user's familiarity, frequency, error cost, and
shared vocabulary an explicit input to interaction posture and information
exposure before UI work?

**Would flip:** evidence that trained operators need raw implementation names in
ordinary product UI, or that hiding setup and technical evidence behind a
second layer improves comprehension without hiding the main path.

**Not enough:** a single product example, a trend post, or a visual preference.

## Finding

Yes. Audience is a decision input, not a demographic label. The usable
dimensions are the specific role and moment, domain familiarity, usage
frequency, error or decision cost, environment, shared vocabulary, and whether
the surface optimizes first-use learning or repeated speed. B2C/B2B is too
coarse to decide density or language.

The practical consequence is a small contract, not a persona program:

- what the user must understand or decide now;
- what they already know and which words they share;
- what stays on the first screen, what waits behind one clear second layer, and
  what stays in code or developer docs;
- whether the surface should optimize learning or throughput.

Technical detail is not automatically noise. It is evidence when the user is
evaluating integration, security, performance, compatibility, or risk. The
ordering rule is outcome, then decision evidence, then implementation detail.

## Evidence

### Users are not a binary novice/expert split

NN/g's novice-versus-expert analysis says learnability remains important because
users rarely become true experts on any one site, while frequent expert work
also needs efficiency, shortcuts, and higher information density. It names
"training wheels" interfaces: a simplified path for new users and more power
for loyal users. This supports conditional density and expert affordances, not
one universal UI.

Source: [NN/g — Novice vs. Expert Users](https://www.nngroup.com/articles/novice-vs-expert-users/), 2000-02-05.

### Experts still prefer plain language

NN/g's analysis of professionals in IT, medicine, and academia found that experts
want concise, scannable information without unnecessary jargon. The same
article notes that even people in one industry do not share the same vocabulary
level, and that a technical term is useful when the audience shares its precise
meaning. Its working guidance is roughly a 6th-8th grade reading level for
general audiences and 10th-12th for experts; text beyond 12th grade requires too
much effort even for highly educated readers.

Source: [NN/g — Plain Language Is for Everyone, Even Experts](https://www.nngroup.com/articles/plain-language-experts/), 2017-10-08.

### Progressive disclosure has a split rule

NN/g's progressive-disclosure guidance puts frequently needed features on the
first display and rarely used or advanced features behind one clear second
layer. The entry must have strong information scent. Designs beyond two
disclosure levels typically have low usability. This supports "visible /
secondary / hidden" as an information budget, not an excuse to bury the main
path.

Source: [NN/g — Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/), 2006-12-03.

W3C's cognitive-accessibility guidance independently supports removing
unnecessary content, limiting interruptions, using short chunks, avoiding
unexplained acronyms and jargon, and keeping the page purpose and controls
familiar and consistent.

Source: [W3C — Making Content Usable for People with Cognitive and Learning Disabilities](https://www.w3.org/TR/coga-usable/), W3C Working Group Note, 2021-04-29.

### Familiar words and mental models beat explanation

NN/g's "match between the system and the real world" heuristic says the system
should speak the user's language with familiar words, phrases, and concepts
rather than system-oriented terms, and should follow real-world conventions.
Its mental-model guidance says users predict system behavior from prior
experience; a mismatch causes persistent errors, and explanation cannot replace
a familiar interaction model.

Sources: [NN/g — Match Between the System and the Real World](https://www.nngroup.com/articles/match-system-real-world/), 2018-07-01; [NN/g — Mental Models](https://www.nngroup.com/articles/mental-models/), reviewed 2026-09-01.

Microsoft's style guidance independently recommends simple words with precise
meanings, removing words that add no substance, one term for one concept, and
avoiding vague verbs and unnecessary adverbs.

Source: [Microsoft Style Guide — Use simple words, concise sentences](https://learn.microsoft.com/en-us/style-guide/word-choice/use-simple-words-concise-sentences), last updated 2022-06-24.

### Simplicity is work, not a style

GOV.UK's design principles say service design starts with user needs, and that
making something simple to use is harder than making it look simple, especially
when the underlying system is complex. Its "understand context" principle asks
who the user is, where they are, and what they already know; "this is for
everyone" treats legibility and inclusion as design constraints.

Source: [GOV.UK — Government Design Principles](https://www.gov.uk/guidance/government-design-principles), updated 2025-04-02.

ISO 24495-1 defines plain language by reader outcome: the intended reader can
get what they need (relevant), find it, understand it on first reading, and act
on it. The public `danyuchn/iso-24495-skill` implementation makes audience and
purpose the first step, then rewrites without dropping facts or precision.

Sources: ISO 24495-1:2023 (standard, not reproduced); [danyuchn/iso-24495-skill](https://github.com/danyuchn/iso-24495-skill), MIT, commit `113656b0a6a6cbeb3b3c2bb7cf3bc29349cb05cf`, 2026-08-13.

## Adopted mechanisms

1. **Audience Contract** in Product: primary role and moment, familiarity and
   shared vocabulary, frequency, error cost, learning-versus-throughput stance,
   and visible/secondary/hidden information.
2. **Interaction Posture** derived from the contract: density, language,
   main-path shape, settings stance, expert affordances, and help stance.
3. **One primary audience per surface.** Multiple audiences get separate paths
   or layers instead of an averaged middle.
4. **Three-layer information order:** outcome -> decision evidence ->
   implementation detail. Implementation names stay in code, runbooks, and
   developer docs unless they are the user's work object.
5. **Comprehension Gate** in Design review: first-screen purpose and next
   action, user vocabulary, technical-term justification, note budget, density
   fit, settings stance, and error recovery.
6. **Note budget:** a visible note must prevent an error, explain a consequence,
   support recovery, or teach a term needed now; otherwise it is deleted.

## Boundaries and counterexamples

- High-frequency operational tools may trade some learnability for efficiency,
  density, keyboard control, and batch actions. Density is not the defect;
  unexplained implementation language is.
- Shared domain terms are valid compression. `incision` is appropriate for
  surgeons; `order_sync_status` is not appropriate for warehouse operators just
  because they are "expert users".
- Developer tools, API products, security reviews, and technical purchasing
  pages need technical evidence. Removing it would fail relevance. Put it after
  the outcome and keep it inspectable.
- Progressive disclosure beyond two levels tends to lose users. Do not hide the
  main path, the price, the primary action, or the evidence required for the
  current decision.
- A new interaction can beat a familiar one, but it must help the user form a
  correct mental model quickly. Novelty is not a reason to make the first
  screen harder.

## Prior art

- [`content-designer/ux-writing-skill`](https://github.com/content-designer/ux-writing-skill), MIT, 258 stars on 2026-11-09, commit `98cacde4ba2dd10ed28df43a8d53eef1e321c539`: strong microcopy, error-message, tone, and plain-language patterns. It does not own product scope, interaction posture, or artifact review.
- [`danyuchn/iso-24495-skill`](https://github.com/danyuchn/iso-24495-skill), MIT, 157 stars on 2026-11-09, commit `113656b0a6a6cbeb3b3c2bb7cf3bc29349cb05cf`: reader-outcome plain-language rewriting with audience first. It does not cover density, settings, technical evidence, or UI review.
- [`Mindrally/skills` UX design](https://github.com/Mindrally/skills/tree/main/ux-design), Apache-2.0, 301 stars on 2026-11-09: lists user research, progressive disclosure, and cognitive-load management as principles. It does not turn them into an audience-to-interface gate.

No single public skill found in this pass combined audience-derived interaction
posture, information exposure, and an artifact-level comprehension gate. The
mechanisms were adopted; no prompt, wording, or skill structure was copied.

## Access record

- NN/g, GOV.UK, Microsoft Learn, and W3C pages were reachable and read on 2026-11-09.
- GitHub repository metadata and `SKILL.md` files were read through the GitHub API on 2026-11-09.
- Apple HIG and Carbon docs were not used as deciding sources in this pass; no claim depends on them.
- The ISO standard text was not purchased or reproduced. Only its publicly described principles and the MIT skill implementation were used.

## Confidence

- **High:** audience is multi-dimensional; expert status does not imply shared
  implementation vocabulary; first-screen core plus one secondary layer;
  plain language helps experts too.
- **Medium:** the exact ordering of technical evidence for every technical
  buyer; the boundary between shared domain language and internal language
  varies by team.
- **Low:** any claim that these rules reduce rework, time, or token cost. No
  fresh-session behavior measurement has been run.

## What remains unproven

The new eval contracts are prompts, not measured behavior. A fresh-session run
against a no-skill baseline is still required before claiming comprehension,
quality, speed, token, or rework improvement.
