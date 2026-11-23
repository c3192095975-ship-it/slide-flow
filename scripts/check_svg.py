#!/usr/bin/env python3
"""Structural checks for editable scientific SVG assets."""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check SlideFlow SVG assets.")
    parser.add_argument("--svg", required=True)
    parser.add_argument("--spec", help="Optional VisualSpec JSON")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args(argv)
    path = Path(args.svg).expanduser()
    errors: list[str] = []
    warnings: list[str] = []
    checks: dict[str, dict] = {}
    if not path.is_file():
        print(f"status: fail\nerror: SVG not found: {path}")
        return 1
    text = path.read_text(encoding="utf-8", errors="replace")
    try:
        root = ET.fromstring(text)
    except ET.ParseError as exc:
        print(f"status: fail\nerror: invalid SVG XML: {exc}")
        return 1
    root_tag = root.tag.split("}")[-1].lower()
    checks["root"] = {"status": "pass" if root_tag == "svg" else "fail", "tag": root.tag}
    if root_tag != "svg":
        errors.append("root element is not svg")
    local_names = [node.tag.split("}")[-1].lower() for node in root.iter()]
    image_count = local_names.count("image")
    text_count = local_names.count("text")
    group_count = local_names.count("g")
    path_count = local_names.count("path")
    checks["elements"] = {"image": image_count, "text": text_count, "g": group_count, "path": path_count}
    if image_count:
        errors.append(f"embedded <image> elements found: {image_count}")
    if re.search(r"data:image/|base64,", text, re.I):
        errors.append("embedded raster/base64 data found")
    if text_count == 0:
        warnings.append("no <text> elements found; editable text may be absent")
    if group_count == 0:
        warnings.append("no <g> groups found; editability may be poor")
    if path_count <= 1 and text_count == 0 and group_count == 0:
        errors.append("SVG looks like a single non-editable path")
    if args.spec:
        try:
            spec = json.loads(Path(args.spec).expanduser().read_text(encoding="utf-8"))
            if spec.get("vector_required") and image_count:
                errors.append("VisualSpec requires vector but SVG embeds raster images")
            if spec.get("editable_text_required") and text_count == 0:
                errors.append("VisualSpec requires editable text but no <text> found")
            if spec.get("raster_embedded") is False and image_count:
                errors.append("VisualSpec says raster_embedded=false but <image> exists")
        except Exception as exc:
            warnings.append(f"cannot parse VisualSpec: {exc}")
    status = "pass" if not errors else "fail"
    payload = {"status": status, "errors": errors, "warnings": warnings, "checks": checks}
    if args.format == "json":
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"status: {status}")
        print(f"image elements: {image_count}")
        print(f"text elements: {text_count}")
        print(f"groups: {group_count}")
        print(f"paths: {path_count}")
        print(f"errors: {len(errors)}")
        for item in errors:
            print(f"- {item}")
        print(f"warnings: {len(warnings)}")
        for item in warnings:
            print(f"- {item}")
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
