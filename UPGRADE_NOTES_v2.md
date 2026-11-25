# Slide Flow 2.0 Upgrade Notes

## What changed
- Adaptive task routing and complexity tiers.
- Scope lock for existing-deck edits; unselected slides are immutable by default.
- Design intelligence with semantic composition and scientific figure grammar.
- Competition Excellence Mode for judge comprehension and evidence-risk review.
- Two-layer visual QA protocol with severity-based repair.
- Capability states distinguish declared, discovered, smoke-tested and verified.
- New VisualSpec checker and regression-oriented benchmark guidance.

## Compatibility
This is an additive upgrade. Existing output modes, deck profiles, evidence registry, PDF QA, SVG protocol, skill discovery and handoff conventions are retained.

## Validation performed
- Python unit tests: 15 passed.
- Slide plan + evidence registry example: pass.
- VisualSpec + layout diversity example: pass, no warnings.
- SVG example: pass, no warnings.
- PDF sample: structural and render checks pass.

## Important limits
Automated checks cannot prove scientific correctness, visual excellence, accessibility in every presentation environment, or official competition compliance. Human review remains required. Any unavailable check must be reported as `not_checked`.
