#!/usr/bin/env python3
"""Validate a SlidePlan and optional evidence registry."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate SlideFlow slide plan and evidence records.")
    parser.add_argument("--plan", required=True, help="slide-plan JSON path")
    parser.add_argument("--evidence", help="evidence-registry JSON path")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args(argv)

    errors: list[str] = []
    warnings: list[str] = []
    plan_path = Path(args.plan).expanduser()
    if not plan_path.is_file():
        print(f"status: fail\nerror: plan not found: {plan_path}")
        return 1
    try:
        plan = load_json(plan_path)
    except Exception as exc:
        print(f"status: fail\nerror: cannot parse plan: {exc}")
        return 1

    for key in ("profile", "authoring_format", "delivery_format", "slides"):
        if key not in plan:
            errors.append(f"missing top-level field: {key}")
    slides = plan.get("slides", [])
    if not isinstance(slides, list) or not slides:
        errors.append("slides must be a non-empty list")
        slides = []

    evidence_ids: set[str] = set()
    evidence_status: dict[str, str] = {}
    if args.evidence:
        evidence_path = Path(args.evidence).expanduser()
        if not evidence_path.is_file():
            errors.append(f"evidence registry not found: {evidence_path}")
        else:
            try:
                evidence_data = load_json(evidence_path)
                records = evidence_data.get("evidence", evidence_data if isinstance(evidence_data, list) else [])
                for record in records:
                    if not isinstance(record, dict):
                        continue
                    eid = str(record.get("evidence_id", "")).strip()
                    if not eid:
                        errors.append("evidence record missing evidence_id")
                        continue
                    if eid in evidence_ids:
                        errors.append(f"duplicate evidence_id: {eid}")
                    evidence_ids.add(eid)
                    status = str(record.get("status", "")).strip()
                    evidence_status[eid] = status
                    if status in {"placeholder", "needs_review"}:
                        errors.append(f"evidence {eid} is not final: {status}")
                    if status not in {"verified", "user_provided", "inferred", "placeholder", "needs_review"}:
                        warnings.append(f"unknown evidence status for {eid}: {status or 'empty'}")
            except Exception as exc:
                errors.append(f"cannot parse evidence registry: {exc}")

    seen_slide_ids: set[str] = set()
    visual_ids: set[str] = set()
    for index, slide in enumerate(slides, start=1):
        if not isinstance(slide, dict):
            errors.append(f"slide {index} is not an object")
            continue
        sid = str(slide.get("slide_id", "")).strip()
        if not sid:
            errors.append(f"slide {index} has no slide_id")
        elif sid in seen_slide_ids:
            errors.append(f"duplicate slide_id: {sid}")
        seen_slide_ids.add(sid)
        for field in ("title", "takeaway", "claim", "visual_type"):
            if not str(slide.get(field, "")).strip():
                errors.append(f"slide {sid or index} missing {field}")
        eids = slide.get("evidence_ids", [])
        if not isinstance(eids, list) or not eids:
            errors.append(f"slide {sid or index} has no evidence_ids")
            eids = []
        for eid in eids:
            eid = str(eid)
            if evidence_ids and eid not in evidence_ids:
                errors.append(f"slide {sid or index} references unknown evidence_id: {eid}")
        visual_type = str(slide.get("visual_type", "")).strip()
        if visual_type not in {"text_only", "none", "data_chart", "mechanism", "concept", "experiment_design", "system_architecture", "real_asset", "comparison", "multi_panel"}:
            warnings.append(f"slide {sid or index} has unknown visual_type: {visual_type}")
        if visual_type not in {"text_only", "none"}:
            vid = str(slide.get("visual_spec_id", "")).strip()
            if not vid:
                errors.append(f"slide {sid or index} needs visual_spec_id")
            elif vid in visual_ids:
                errors.append(f"duplicate visual_spec_id: {vid}")
            visual_ids.add(vid)
        if visual_type == "data_chart" and not slide.get("data_source"):
            errors.append(f"slide {sid or index} has data_chart without data_source")
        if visual_type in {"mechanism", "concept"} and slide.get("conceptual") is not True:
            warnings.append(f"slide {sid or index} uses conceptual visual without conceptual=true")
        if slide.get("authoring_format") and slide.get("authoring_format") != plan.get("authoring_format"):
            warnings.append(f"slide {sid or index} overrides authoring_format")
        if slide.get("delivery_format") and slide.get("delivery_format") != plan.get("delivery_format"):
            warnings.append(f"slide {sid or index} overrides delivery_format")

    status = "pass" if not errors else "fail"
    payload = {
        "status": status,
        "errors": errors,
        "warnings": warnings,
        "slide_count": len(slides),
        "evidence_count": len(evidence_ids),
    }
    if args.format == "json":
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"status: {status}")
        print(f"slides: {len(slides)}")
        print(f"evidence: {len(evidence_ids)}")
        print(f"errors: {len(errors)}")
        for item in errors:
            print(f"- {item}")
        print(f"warnings: {len(warnings)}")
        for item in warnings:
            print(f"- {item}")
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
