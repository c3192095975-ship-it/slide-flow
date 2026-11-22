# PDF Submission QA

## Delivery separation

```yaml
authoring_format: editable_pptx
delivery_format: pdf
```

A PPTX is not automatically a valid PDF delivery. A generated PDF is not verified until checked.

## Checks

### File

- file opens;
- page count and order;
- page size/orientation;
- no accidental blank pages;
- file size reasonable;
- PDF metadata where required.

### Text and fonts

- fonts embedded or acceptably substituted;
- CJK/special symbols render;
- text not clipped or overflowing;
- searchable text when required.

### Images and charts

- resolution adequate;
- no severe compression artifacts;
- vector content preserved where expected;
- chart axes, labels and legends readable;
- multi-panel figures not cropped.

### Page layout

- margins and page bounds;
- no overlapping objects;
- contrast/readability;
- consistent visual style.

### Source/delivery parity

- PDF page count matches source;
- updated slides are present;
- final file is the latest version.

## Status values

- `pass`
- `warning`
- `fail`
- `not_checked`

`not_checked` must never be reported as pass.
