# Plugin Architecture Notes

Use this note when changing Noootwo Design from a single-skill package into a multi-skill plugin.

## Sources Reviewed

- OpenAI Academy: Codex plugins and skills differentiate reusable workflow guidance from packaged integrations and distribution.
- OpenAI Academy: skills follow the Agent Skills format and can be exported/imported across supporting tools.
- Claude Code skills documentation: plugin skills live under a shared `skills/` directory, are namespaced, and can bundle supporting files while reusing plugin-level resources.
- MCP documentation: tools/resources/prompt capabilities are protocol-level building blocks and should remain separate from workflow prompts.
- Local Codex environment validation in this repo: `npx skills add . --list`, `codex-cli 0.116.0`, and current config/runtime inspection.

## Mechanisms Borrowed

- Keep one front-door skill that classifies and routes work.
- Put specialized high-cost workflows in thin sibling skills.
- Share references, scripts, templates, and assets at plugin root instead of copying them into every skill.
- Treat artifact-specific expansions such as poster or slides as future child skills on top of the same protocol core.

## Shared Core That Child Skills Should Reuse

- task-classification dimensions
- blocking rules and stage transitions
- decision protocol and delegated-default recording
- direction brainstorm contract
- `.noootwo/` template structure
- validator and eval scripts
- review decision vocabulary and return-action map
- research protocol, source weighting, and fallback rules

If a future child skill needs to replace most of these, it is probably not a child skill of Noootwo Design and should live as a separate package.

## Why This Change Belongs Here

- The repository already contains separable workflow layers: direction discovery, artifact review, and implementation preservation.
- Keeping them inside one giant skill increases trigger ambiguity and context weight.
- A plugin-shaped repository preserves a path to multiple focused skills with shared references, even while the current verified install surface remains the root skill.

## Current Install Reality

- Verified now: root-skill discovery from the repository checkout
- Verified now: structural plugin skeleton validation
- Not yet verified in this environment: end-to-end local plugin install and multi-skill discovery as the default distribution path

Because of that, the repository should keep a compatibility strategy:

- root `SKILL.md` remains the stable release surface
- plugin skeleton remains the internal architecture for shared resources and future child skills
- local updates should still sync the installed root skill copy until plugin installation is verified

## Boundaries

- Do not duplicate the entire reference corpus into each child skill.
- Do not create child skills for every surface or scenario keyword.
- Split by stable workflow responsibility, not by prompt example.

## Split Tests

Before adding a new child skill, check all of the following:

- Does it have a distinct artifact contract?
- Does it need distinct review evidence or review gates?
- Does it need a distinct return-action map?
- Does it reduce trigger ambiguity or context weight enough to justify the split?
- Is it reusable across many prompts without depending on a narrow topic label?

If the answer is mostly `no`, keep the behavior in the root workflow or in shared references instead of adding another child skill.
