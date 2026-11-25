# Visual QA Protocol

## Two distinct QA layers
1. Deterministic: file integrity, dimensions, text extraction, overflow signals, image resolution, missing fonts/assets, page count/order and source-output correspondence.
2. Human/vision: hierarchy, balance, relevance, scientific semantics, readability at intended size and narrative flow.

A deterministic pass is not a visual-quality pass. A visual pass is not scientific validation.

## Render protocol
Render every page at presentation size and inspection resolution. Inspect a contact sheet and individual pages; inspect dense, chart-heavy, title, transition and closing pages individually. Re-render after material repairs. Record render environment and export settings.

## Source-to-PDF comparison
Verify page count/order; no missing or shifted objects; fonts/glyphs; chart/equation/footnote/citation legibility; no unexpected crop/transparency/color changes; PDF opens and page dimensions match submission rules.

## Severity
- `blocker`: wrong/missing content, corrupted file, unsupported claim, unreadable critical data, wrong page/order.
- `major`: clipping, missing assets, broken chart labels, materially weak hierarchy, incorrect scientific relationships.
- `minor`: small spacing, alignment or typographic inconsistency.
- `note`: optional polish.

## QA report fields
`artifact`, `render_environment`, `pages_checked`, `deterministic_status`, `visual_status`, `scientific_semantics_status`, `issues[]`, `not_checked[]`, `repair_actions[]`, `retest_status`. Use `not_checked` when unavailable; never silently convert unknown into pass.
