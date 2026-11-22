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
