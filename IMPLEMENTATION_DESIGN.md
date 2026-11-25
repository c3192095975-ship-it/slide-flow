# Slide Flow v2.0 Implementation Design

## 1. Target architecture

```text
Task Intelligence
  -> Story and Evidence Planning
  -> Visual Intelligence
  -> Design Intelligence
  -> Production
  -> Multi-layer QA
  -> Delivery and Evaluation
```

The Skill Router remains the bottom layer. It discovers, selects, and invokes one primary skill per stage.

## 2. Modules

### Task Intelligence

Inputs: goal, audience, duration, competition rules, delivery format.

Outputs: `SlidePlan`, profile, tier, authoring/delivery formats, missing-input list.

### Story and Evidence Planning

Inputs: paper, data, project notes, official rules.

Outputs: story outline, per-slide claim, evidence registry, rule-to-slide mapping.

### Visual Intelligence

Inputs: per-slide claim, data, evidence type, editability requirement.

Outputs: `VisualSpec`, asset manifest, visual decisions and rejected visual options.

### Design Intelligence

Inputs: page purpose, visual type, brand/template constraints.

Outputs: layout direction, style contract, reference-library match.

### Production

Uses one primary PPT engine at a time. It consumes existing story, visual and design artifacts.

### Multi-layer QA

- Machine QA: file, page, overflow, fonts, images, links, resolution.
- Content QA: claim-evidence, data-chart, citation, units.
- Expert QA: scientific validity, visual hierarchy, audience fit, persuasion.
- Delivery QA: PPTX/PDF page parity, PDF text/searchability, packaging.

## 3. Data objects

### SlidePlan

```json
{
  "profile": "research_competition",
  "authoring_format": "editable_pptx",
  "delivery_format": "pdf",
  "slides": [
    {
      "slide_id": "S01",
      "title": "...",
      "takeaway": "...",
      "claim": "...",
      "evidence_ids": ["E01"],
      "visual_type": "mechanism",
      "visual_spec_id": "V01",
      "speaker_notes": "..."
    }
  ]
}
```

### VisualSpec

Includes visual type, purpose, data source, labels, units, layout, editability, output format, caption and QA checks.

### EvidenceRecord

Includes evidence ID, claim, source type, location, excerpt/data reference, method, limitations, status, related slides and visuals.

### DeliverySpec

Includes authoring format, delivery format, page size, page count, font embedding, searchable text, image resolution and export profile.

## 4. Integration with existing stages

- Add `research_competition` to deck profiles.
- Add `visual_decision` and `visual_asset` to stage 3/3.5.
- Add evidence registry between content and visual direction.
- Add `pdf_delivery_qa` after render/visual QA and before final delivery.
- Add Gate I: PDF delivery and Gate J: Research competition rubric.
- Keep Gate A-H and scoped research fallback.

## 5. Failure paths

- Missing rules: use generic research-competition checks and label non-official.
- Missing data: mark placeholder or concept diagram; do not fabricate experiments.
- PDF tool missing: keep source, report `not_checked`.
- Skill unavailable: fallback to same-capability alternative or baseline.
- Visual/copy failure: return to the affected stage with a recorded fallback log.

## 6. Test strategy

- Contract tests for new schemas and gates.
- `check_slide_plan.py` fixtures for missing claims, evidence and visual specs.
- `check_pdf.py` fixtures when `pdfinfo`/`pdftoppm` are available; skip explicitly otherwise.
- Existing discovery tests must remain green.
- One research-competition example with rules, slide plan, evidence registry and QA report.
