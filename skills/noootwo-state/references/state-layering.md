# State Layering

Choose one owning location for each persisted fact. The location follows the fact's properties, not its subject matter.

## Layers

| Layer | Owns | Does not own |
| --- | --- | --- |
| Hot entrypoint | short always-on rules and routing | long bodies, timelines, evidence |
| Current snapshot | what is true now and may change next | durable decisions, full history |
| Durable decision | an accepted choice and its consequence | temporary status |
| Procedure | how to repeat a task | field-level reference |
| Reference | exact fields, commands, schemas, manifests | narrative reasoning |
| Release record | versioned change and migration notes | current active work |
| Cold evidence | raw evidence, long logs, old notes | anything read on every task |

If a repository uses different names, map to responsibility instead of forcing these names.

## Fact classifier

| Fact type | Owning layer |
| --- | --- |
| `state` | structured current snapshot |
| `event` | append-only history |
| `decision` | durable decision record |
| `narrative` | Markdown owning layer |
| `release` | release record |
| `procedure` | procedure layer |
| `evidence` | cold evidence or reference path |

One fact, one owner. Link from another layer only when discovery would otherwise fail.

## Update pattern

1. Identify the changed fact.
2. Search for existing claims about the same fact.
3. Put the new truth in exactly one owning layer.
4. Link from other layers only when required.
5. Remove or revise stale claims in the same pass.
6. Keep hot files within budget; move detail to an on-demand or cold layer.

## Budget

Hot entrypoints and current snapshots stay small. Move old versions to release records, durable choices to decision records, repeatable steps to procedures, and raw evidence or long history out of the hot path.
