#!/usr/bin/env python3
"""Validate VisualSpecs and flag layout repetition in a SlideFlow plan."""
from __future__ import annotations
import argparse, json, sys
from collections import Counter
from pathlib import Path

VALID_TYPES = {"text_only", "none", "data_chart", "mechanism", "concept", "experiment_design", "system_architecture", "real_asset", "comparison", "multi_panel"}
REQUIRED = ("visual_id", "slide_id", "visual_type", "purpose", "source_data_or_asset", "output_format", "editability_requirement")

def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--specs", required=True, help="visual-specs JSON")
    ap.add_argument("--plan", help="optional slide-plan JSON for diversity checks")
    ap.add_argument("--format", choices=("text", "json"), default="text")
    args = ap.parse_args(argv)
    errors, warnings = [], []
    try:
        data = load(Path(args.specs))
    except Exception as exc:
        print(f"status: fail\nerror: cannot read specs: {exc}")
        return 1
    visuals = data.get("visuals") if isinstance(data, dict) else None
    if not isinstance(visuals, list) or not visuals:
        errors.append("visuals must be a non-empty list")
        visuals = []
    ids, slides = set(), set()
    for i, v in enumerate(visuals, 1):
        if not isinstance(v, dict):
            errors.append(f"visual {i} must be an object"); continue
        for field in REQUIRED:
            if not str(v.get(field, "")).strip(): errors.append(f"visual {i} missing {field}")
        vid = str(v.get("visual_id", "")).strip()
        sid = str(v.get("slide_id", "")).strip()
        if vid and vid in ids: errors.append(f"duplicate visual_id: {vid}")
        if vid: ids.add(vid)
        if sid: slides.add(sid)
        typ = v.get("visual_type")
        if typ not in VALID_TYPES: errors.append(f"{vid or i} has unsupported visual_type: {typ}")
        source_type = v.get("source_type")
        if typ == "data_chart" and source_type not in {"data", "user_data", "verified_data"}:
            errors.append(f"{vid or i}: data_chart must declare a data-backed source_type")
        if typ in {"mechanism", "concept"} and not v.get("caption_or_source_note"):
            warnings.append(f"{vid or i}: add a conceptual/source note")
        if v.get("editability_requirement") == "editable_in_ppt" and v.get("output_format") == "png":
            errors.append(f"{vid or i}: PNG cannot satisfy editable_in_ppt")
        if v.get("validation_status") == "pass" and not v.get("validation_checks"):
            warnings.append(f"{vid or i}: pass status without recorded validation_checks")
    diversity = None
    if args.plan:
        try: plan = load(Path(args.plan))
        except Exception as exc: errors.append(f"cannot read plan: {exc}"); plan = {}
        items = plan.get("slides", []) if isinstance(plan, dict) else []
        comps = [str(s.get("composition", "")).strip() for s in items if isinstance(s, dict) and str(s.get("composition", "")).strip()]
        if items and len(comps) < max(1, len(items) // 2):
            warnings.append("fewer than half of slides declare composition; layout diversity cannot be assessed")
        counts = Counter(comps)
        repeated = {k: n for k, n in counts.items() if n >= 4 and n / max(1, len(comps)) > 0.6}
        if repeated:
            warnings.append("dominant composition may be overused: " + ", ".join(f"{k}={n}" for k,n in repeated.items()))
        diversity = {"slides_with_composition": len(comps), "composition_counts": dict(counts), "dominant_repetition_flags": repeated}
    payload = {"status": "pass" if not errors else "fail", "visual_count": len(visuals), "errors": errors, "warnings": warnings, "layout_diversity": diversity}
    if args.format == "json": print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"status: {payload['status']}\nvisuals: {len(visuals)}\nerrors: {len(errors)}")
        for x in errors: print(f"- ERROR: {x}")
        print(f"warnings: {len(warnings)}")
        for x in warnings: print(f"- WARN: {x}")
    return 0 if not errors else 1

if __name__ == "__main__": sys.exit(main())
