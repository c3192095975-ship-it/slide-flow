# Slide Flow v1.3 Audit Report

## 1. Current architecture

- `SKILL.md` is the main router and stage contract.
- `references/output-modes.md` selects authoring/delivery format.
- `references/deck-profiles.md` defines presentation genres.
- `references/capability-model.md` defines capability slots and fallback.
- `references/quality-gates.md` defines Gates A-H.
- `references/handoff-schemas.md` defines project, story, style, render and fallback records.
- `scripts/discover_slide_skills.py` scans installed skills and classifies `ppt_core`, `ppt_auxiliary`, and `not_ppt`.
- `scripts/check_quality.py` was not added to slide-flow; current deterministic checks are mainly capability discovery and document QA contracts.
- Tests currently cover the skill contract and discovery fixtures only.

## 2. Capabilities that already exist

- PPT output-mode routing (editable PPTX, image deck, HTML, template edit, image-to-editable, hybrid).
- Deck profiles for academic talk, thesis defense, pitch, consulting, training, product launch, social deck, business review, template deck.
- Quality tiers and Gate A-H.
- One-primary-per-stage and conflict rules.
- Official/plugin preference (`Presentations`, `template-creator`, `documents`, `pdf`, `univer-cli`).
- Scoped research fallback.
- Visual asset and SVG-first guidance.
- GitHub PPT ecosystem research.
- Capability discovery and PPT relevance filtering.
- Handoff schemas and story/style/render records.

## 3. Requirements that are already present

| Requirement | Status | Evidence |
|---|---|---|
| Task profile and output mode | Present | `SKILL.md` sections 4-6; `output-modes.md` |
| Story and evidence planning | Partial | story/content stages exist; no complete evidence registry artifact |
| Visual intelligence | Partial | visual_direction and visual_asset exist; visual type selection is not formalized |
| Design consistency | Present | style contract and Gate D/E |
| Production separation | Present | authoring/delivery distinction described but not enforced by schema/script |
| Research competition | Missing | no competition profile |
| Evidence registry | Partial | evidence references and fallback logs, no standalone schema/checker |
| PDF submission QA | Missing | no PDF checker or delivery gate |
| Design reference library | Missing | no metadata schema or provenance rules |
| Capability verification | Partial | discovery checks metadata and dependencies, no smoke tests |
| Benchmark and judge simulation | Missing | no benchmark set or scoring/rubric artifact |
| Automated regression | Partial | contract and discovery tests only |

## 4. Concrete gaps and risks

1. A presentation can pass Gate A-F while its final PDF is not checked.
2. `SlidePlan`, `VisualSpec`, and `EvidenceRecord` exist only as prose concepts; they are not validated.
3. A competition deck cannot consume official rules because there is no competition profile.
4. `authoring_format` and `delivery_format` are described but not checked in a schema/gate.
5. The visual system has no formal decision tree for mechanism, data, architecture, experiment, comparison, and multi-panel figures.
6. There is no design reference metadata or copyright boundary beyond a prose note.
7. Capability discovery can report a skill as available without a smoke test of its actual command or output contract.
8. There is no benchmark or human rubric to compare versions.

## 5. Minimum-change plan

1. Add `research_competition` profile and rubric mapping artifact.
2. Add `scientific-visual-intelligence.md` with VisualSpec and visual type decisions.
3. Add `evidence-registry.md` with claim/source/visual/slide mapping.
4. Add `pdf-submission-qa.md` and a PDF structural checker.
5. Add `design-reference-library.md` with provenance and copyright rules.
6. Add `benchmark-and-judge.md` with a small benchmark set and human rubric.
7. Add executable `check_slide_plan.py` and `check_pdf.py`.
8. Keep existing router and stage model; add gates and artifact schemas rather than rewrite.
