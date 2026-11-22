# Evidence Registry

## Purpose

Link every important slide claim to source, data, visual and evidence status.

## Record

```yaml
evidence_id:
claim:
source_type: user_data | paper | official_rule | public_dataset | image | project_record | inference
source_name:
source_location:
source_date:
data_reference:
method:
limitation:
status: verified | user_provided | inferred | placeholder | needs_review
related_slide_ids: []
related_visual_ids: []
```

## Rules

- Never invent sources, sample sizes, p-values, confidence intervals, performance metrics or official competition rules.
- Inferences must not be presented as experimental facts.
- The claim strength cannot exceed evidence strength.
- Data changes must mark related charts and slides for regeneration/review.
- `placeholder` and `needs_review` cannot pass a final evidence gate.
- Figures must trace to data or be explicitly labeled conceptual.
- When official rules are absent, mark them `not_provided`; do not claim official compliance.
