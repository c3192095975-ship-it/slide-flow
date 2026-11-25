# Benchmark and Judge Simulation

## Benchmark task families
1. paper-to-academic-talk; 2. research-competition deck; 3. experiment-results briefing; 4. technical pitch; 5. existing PPT redesign; 6. scoped two-slide redesign; 7. PPTX-to-PDF delivery; 8. image-PPT-to-editable-PPTX; 9. data-driven chart slides; 10. template-constrained deck.

## Benchmark case contract
Each case includes stable `case_id` and version; source inputs and permitted tools; task class/scope/expected format; locked content/assets and constraints; required evidence/visual deliverables; deterministic assertions; human rubric/severity thresholds; known limitations.

## Evaluation
Score 1–5 for narrative logic, scientific accuracy, evidence completeness, visual appropriateness, hierarchy/consistency, readability, audience fit, editability and delivery. Declare profile-specific weights before evaluation.

Track pass rate by task family, blocker/major count, unsupported-claim count, source-output fidelity, editability, visual rubric distribution, execution cost and repair count.

## Regression policy
Run fixed cases after changes to routing, prompts, scripts or templates. Compare with the previous version. A higher average score cannot hide a new blocker or scientific-accuracy regression.

## Judge simulation
Challenge contribution specificity, evidence strength, baselines/controls, reproducibility, prototype maturity, limitations and non-specialist comprehension. Advisory only; cannot predict actual scores or replace official judges.
