# Synthetic QA Report

## SlidePlan validation

Command:

```bash
python3 scripts/check_slide_plan.py \
  --plan examples/research-competition/slide-plan.json \
  --evidence examples/research-competition/evidence-registry.json
```

Result:

```text
status: pass
slides: 3
evidence: 3
errors: 0
warnings: 0
```

## PDF structural validation

Command:

```bash
python3 scripts/check_pdf.py \
  --pdf examples/research-competition/sample-delivery.pdf
```

Observed checks in the current environment:

- header: pass
- size: pass
- pdfinfo: pass
- page render: pass
- searchable text: not_checked because `pdftotext` is unavailable
- errors: 0
- warnings: 1

`sample-delivery.pdf` is a minimal one-page fixture, not a finished competition deck.

## Manual checks still required

- Replace synthetic claims and evidence with user-supplied project materials.
- Add official competition rules if available.
- Review visual assets for scientific accuracy.
- Review the final PDF as a human reviewer.
- Confirm the final authoring and delivery formats.
