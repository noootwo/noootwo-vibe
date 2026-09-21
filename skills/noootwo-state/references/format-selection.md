# Format Selection

Choose the storage form from the request properties only. Do not use the content's subject matter.

## Request properties

- `fact_type`: `state | event | decision | narrative | release | evidence | procedure`
- `query_profile`: `field | tail | search | human`
- `mutability`: `current | append-only | immutable`
- `lifespan`: `hot | durable | cold`

## Rules

| Condition | Form |
| --- | --- |
| `query_profile` is `field` or `tail`, and `mutability` is `current` | JSON current snapshot |
| `mutability` is `append-only`, and `fact_type` is `event` | JSONL event history |
| `query_profile` is `human`, or `fact_type` is `narrative`, `decision`, or `release` | Markdown owning layer |
| `lifespan` is `cold`, and `query_profile` is `search` | cold evidence file or reference path |
| `fact_type` is `procedure` | Markdown procedure layer |

When properties conflict, prefer the form required by the most constrained property: `append-only` wins over `current`, `human` wins over `field` when a narrative must be read whole.

## Boundaries

- A structured fact that is only ever read by people should still be Markdown.
- A small current fact read by a routing loop should be JSON even when a human could also read it.
- An immutable record is never rewritten in place; append a successor event and mark the old record superseded.
- A machine-readable snapshot is not duplicated into Markdown; Markdown is generated or linked, not maintained as a second authority.

## Rejection

If the request lacks enough properties to choose a form, ask only for the missing abstract property, not for an explanation of the content.
