# Plugin Vs Skill Research Notes

Use this note when deciding whether Noootwo Design should expand as a bigger root skill, a multi-skill plugin, or both.

## Sources Reviewed

- OpenAI Academy: `Plugins and skills`, published April 23, 2026
- OpenAI Academy: `Skills` resource on the Agent Skills format and cross-product portability
- GitHub Docs: `About agent skills` and `Adding agent skills for GitHub Copilot`
- Claude Code Docs: `Extend Claude with skills`
- Cursor Docs: `Rules` and `Model Context Protocol (MCP)` pages
- Local Codex runtime and CLI state in this environment:
  - `codex-cli 0.116.0`
  - `codex plugin --help`
  - `npx skills add . --list`
  - local `~/.codex/config.toml`

## Stable Distinction

- `plugin`
  - packages connections to tools, apps, MCP servers, or external information sources
  - is the right abstraction when Codex must pull data or act through integrations
  - usually has higher implementation and distribution complexity
- `skill`
  - packages a reusable workflow or playbook
  - is the right abstraction when the core value is process, sequencing, review, formatting, or judgment
  - uses `SKILL.md` and the Agent Skills format, which is portable across tools that support it

## Cross-Tool Pattern

- `OpenAI`
  - official guidance says plugins help Codex connect to tools and information sources
  - official guidance says skills teach Codex a repeatable process and can be combined with plugins
- `GitHub Copilot`
  - official guidance separates skills from repository custom instructions
  - custom instructions are for short, near-always-on guidance; skills are for richer task-specific workflows
- `Claude Code`
  - official guidance treats skills as reusable prompt-based capabilities that auto-load when relevant
  - the Agent Skills standard is explicitly shared across multiple AI tools
- `Cursor`
  - official docs clearly separate `Rules` from `MCP`
  - the official docs retrieval path for Cursor skill details was less reliable in this environment, but the surfaced taxonomy still points to the same mechanism split: persistent guidance vs reusable workflow vs external tool connection

Across tools, the durable pattern is the same:

- stable background guidance belongs in rules or custom instructions
- task-specific workflow logic belongs in skills
- external system access belongs in plugins, MCP servers, apps, or equivalent integration layers

## Trial And Usage Difference

- `plugin` trial path
  - verify install/discovery in the host product
  - verify tool/app connectivity
  - verify the plugin actually exposes the intended capabilities
  - test with real connected data or a local equivalent
- `skill` trial path
  - install/import the skill package
  - trigger it on representative tasks
  - pressure-test whether it changes agent behavior in the expected direction
  - validate the workflow output and failure recovery rules

In short: plugin trial is integration-first; skill trial is behavior-first.

## What This Means For Noootwo Design

- Noootwo Design's core value is still a design workflow protocol, so the stable default unit remains a `skill`.
- The repository can still evolve toward a `plugin` container when multiple related skills need shared resources, discoverability, or future integrated capabilities.
- That plugin layer should be treated as a packaging architecture, not as proof that the root workflow should stop being a skill.
- For future poster, PPT, or other graphic-design coverage, the first question should be whether the artifact contract changes. If not, keep it inside the root/front-door workflow.
- If the artifact contract does change, add a child skill for that artifact family rather than making the root skill larger.
- If future design work also needs connected systems such as Figma, Slides, Drive, or asset search, add that as plugin or MCP capability around the skill family rather than collapsing workflow and integration into one root skill.

## Current Local Reality

- The repository now contains a valid plugin skeleton with `.codex-plugin/plugin.json` and `skills/`.
- In this environment, `npx skills add . --list` still discovers only one root skill from the repository checkout.
- The local CLI verified during this refactor was `codex-cli 0.116.0`, and it did not expose a shell-usable `codex plugin add/list` install flow for direct local plugin iteration.
- The default personal marketplace file `~/.agents/plugins/marketplace.json` was not present during verification.

## Decision

- Keep `SKILL.md` at the repository root as the stable release and local-update surface.
- Keep the plugin skeleton as the shared-core architecture for child skills.
- Do not claim that this repo is already verified for end-to-end local multi-skill plugin installation until that flow is proven in the current Codex environment.
- Add future poster/slides/graphic-design capabilities as child skills only when they represent a stable workflow or artifact contract, not merely a new content topic.

## Access Notes

- OpenAI, GitHub, and Claude official pages were retrievable and sufficient for the stable distinction above.
- Cursor official docs were discoverable, but full text extraction through the current browsing path was less reliable than the other sources. The Cursor conclusion here is therefore based on official page taxonomy plus the broader cross-tool pattern, not on a richer line-by-line Cursor doc read.
