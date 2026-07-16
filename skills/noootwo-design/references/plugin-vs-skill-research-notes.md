# Skill Packaging Research Notes

Use this note when deciding whether a Noootwo capability should become a public skill, an internal reference, or an integration/plugin.

## Stable Distinction

- `skill`: reusable workflow, sequencing, review, formatting, or judgment.
- `plugin/integration`: external tool access, app connection, MCP server, or connected data source.
- `AGENTS.md`: short always-on project guidance and routing hints.

## Current Noootwo Vibe Decision

Noootwo Vibe publishes five workflow skills:

- `noootwo-workflow`
- `noootwo-product`
- `noootwo-design`
- `noootwo-review`
- `noootwo-docs`

Noootwo Design remains a skill because its value is workflow and judgment, not external system access. If future design work needs Figma, Slides, Drive, asset search, or other connected systems, add those as integrations around the skill family instead of making the design skill a giant tool manual.

## Split Test

Before adding any new public skill, require a clear yes for most of these:

- It has a distinct workflow contract.
- It has a distinct review or evidence surface.
- It reduces trigger ambiguity or context weight.
- It is reusable across many prompts.
- It can be validated independently.

If not, keep the behavior as an internal reference or mode inside an existing skill.
