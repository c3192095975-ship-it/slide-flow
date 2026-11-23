# SlideFlow Handoff Schemas

## Project state

```yaml
flow_mode: BYPASS | LIGHT | FULL
output_mode: editable_pptx | image_deck | html_deck | template_edit | image_to_editable | hybrid_delivery
deck_profile: academic_talk | thesis_defense | pitch | consulting | training | product_launch | social_deck | business_review | template_deck
quality_tier: draft | presentation_ready | executive_ready | publish_ready
source_mode: topic | document | paper | template | url | existing_pptx | screenshots | mixed
phase: brief | story | content | visual | exemplar | production | render | visual_qa | accessibility | delivery
primary_skill:
auxiliary_skill:
micro_task_id:
visual_asset_owner:
fallback_owner:
fallback_scope:
fallback_trigger_gate:
fallback_return_to:
story_outline:
style_contract:
template_path:
source_assets: []
rendered_path:
open_issues: []
next_phase:
next_primary_skill:
```

## Story outline

```markdown
# Story Outline

## Central message
## Audience and action
## Slide sequence
| Slide | Title/message | Evidence/assets | Visual intent | Notes |
```

## Style contract

```yaml
slide_size: 16:9
margins:
palette:
typography:
title:
body:
cards:
charts:
source_line:
footer:
```

## Render QA

```yaml
renderer:
file:
slides_checked:
overflow: pass | fail
alignment: pass | fail
fonts: pass | fail
images: pass | fail
contrast: pass | fail
accessibility: pass | fail | not_checked
open_issues: []
```

## Handoff

```text
SlideFlow handoff
- Output mode:
- Profile/tier:
- Stage:
- Artifacts:
- Gate result:
- Open issues:
- Next stage:
- Next primary skill:
```

## Visual asset manifest

```csv
asset_id,slide_id,asset_type,source_path,generator,license,format,editable,source_data,notes
```

## Fallback log

```yaml
trigger_gate:
primary_owner:
fallback_owner:
scope:
return_to:
invalidated_artifacts: []
checks_to_rerun: []
result: pass | fail | pending
```

## Micro-task assignment

```yaml
micro_task_id:
slide_id:
task_type:
primary_skill:
auxiliary_skills: []
output_contract:
  format: svg | png | native_shape | pptx
  editable: true
return_to: slide-flow
```

## SVG asset record

```yaml
visual_id:
source_type: paper | data | user_asset | reference | concept
source_location:
conceptual: true
vector_required: true
raster_embedded: false
editable_text_required: true
ppt_conversion_required: true
validation_status: pending | pass | fail
```
