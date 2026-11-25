# Task Intelligence and Adaptive Routing

## Objective
Choose the smallest workflow that can safely satisfy the user's actual request. Do not force a full-deck pipeline onto a micro-task.

## Task classes
- `create`: create a new deck from a brief, source documents, research, or data.
- `redesign`: materially change narrative and/or visual design of an existing deck.
- `edit_scoped`: modify explicitly selected slides or elements only.
- `polish`: improve typography, spacing, hierarchy, and consistency without changing claims.
- `convert`: change delivery format while preserving content and page order.
- `review`: inspect, score, and report without modifying source files.
- `recover`: repair a broken or partially generated deck.

## Routing matrix
| Class | Default route | Required protection |
|---|---|---|
| create | FULL | establish story, evidence, style contract, exemplar |
| redesign | FULL or LIGHT by scope | preserve verified content and assets |
| edit_scoped | BYPASS or LIGHT | lock all unselected slides |
| polish | BYPASS or LIGHT | do not rewrite claims or invent visuals |
| convert | LIGHT | preserve page count/order; compare source and output |
| review | LIGHT | read-only; no silent edits |
| recover | LIGHT, escalate to FULL only if needed | make a copy before repair |

## Scope lock
Before editing an existing deck, record source file/version, editable slides/elements, immutable slides/elements, locked claims/data, output format and delivery constraints. If the user says "only these slides", all others are immutable. Ask one concise clarification only when ambiguity could cause destructive edits.

## Adaptive phase skipping
Skip a phase only when its output already exists, is current, and passes its relevant gate. Record `reused`, `skipped_with_reason`, or `executed`; never imply a skipped check passed.

## Complexity tiers
- `micro`: one text/shape/color fix; no project scaffolding.
- `small`: one to three slides, conversion, or focused QA.
- `standard`: 4–12 slides or a coherent redesign.
- `large`: full deck, multiple output formats, substantial research/data/visual work.

Evidence uncertainty, template constraints, scientific risk and editability requirements can raise the tier regardless of slide count.

## Minimal startup contract
`task_class`, `scope`, `output_mode`, `profile`, `quality_tier`, `source_mode`, `locked_items`, `required_phases`, `primary_skill`.
Do not print internal reasoning or the full capability inventory.
