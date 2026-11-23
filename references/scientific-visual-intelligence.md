# Scientific Visual Intelligence

## Visual decision flow

For each slide:

1. What is the single takeaway?
2. Is the page explaining a mechanism, method, data, structure, evidence or background?
3. Is real data/image/evidence available?
4. Which visual form is most direct?
5. Is a visual even necessary?
6. Which format preserves editability: native PPT, SVG, PDF or raster?
7. Will it remain readable in the final PDF?

## Visual types

- `mechanism`: causal/mechanistic explanation.
- `concept`: theory, hypotheses or conceptual model.
- `experiment_design`: workflow, apparatus, variables, controls.
- `data_chart`: real quantitative data.
- `system_architecture`: modules, data flow, algorithm structure.
- `real_asset`: photo, microscope image, prototype, original data image.
- `comparison`: baseline, ablation, before/after, robustness.
- `multi_panel`: A/B/C panels with explicit panel logic.
- `text_only`: no visual is clearer.

## Rules

- Do not require a visual on every slide.
- Do not fabricate experimental photos, microscope images or measured data.
- Data charts use real source data.
- Concept diagrams must be labeled as conceptual.
- Mechanism diagrams should communicate causal relationships, not just boxes.
- Prefer SVG for conceptual/vector assets; raster for photos and complex images.
- Convert SVG to PowerPoint shapes only when editability is actually verified.
- Labels, units, legends, sample sizes and uncertainty must be traceable.

## VisualSpec

```json
{
  "visual_id": "V01",
  "slide_id": "S03",
  "visual_type": "mechanism",
  "purpose": "explain the proposed feedback loop",
  "takeaway": "the loop reduces error under the tested condition",
  "source_data_or_asset": "user-provided experiment diagram",
  "required_elements": ["input", "processor", "feedback"],
  "labels_and_units": {},
  "layout": "left-to-right",
  "output_format": "svg",
  "editability_requirement": "editable_in_ppt",
  "caption_or_source_note": "Conceptual diagram based on user-provided method.",
  "validation_checks": ["labels match text", "arrows match method"]
}
```

## SVG and reference-image protocol

- Prefer SVG for mechanism, framework and conceptual diagrams when editability matters.
- Do not embed the reference PNG/JPG inside the SVG or claim a raster image is vector.
- Do not collapse the entire figure into one non-editable path.
- Keep labels as `<text>` and group connectors/nodes/labels separately.
- Verify PowerPoint “Convert to Shape” and inspect text/editability after import.
- Reference images may inform composition, hierarchy, spacing, palette and arrow semantics; they may not be copied without permission.
- Run `scripts/check_svg.py` before placing the asset into a slide.
