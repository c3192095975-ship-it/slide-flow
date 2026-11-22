#!/usr/bin/env python3
"""Structural PDF QA for SlideFlow delivery checks."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def run(cmd: list[str]) -> tuple[int, str, str]:
    p = subprocess.run(cmd, capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check a SlideFlow PDF delivery file.")
    parser.add_argument("--pdf", required=True)
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--no-render", action="store_true", help="Skip first-page rendering")
    args = parser.parse_args(argv)
    path = Path(args.pdf).expanduser()
    errors: list[str] = []
    warnings: list[str] = []
    checks: dict[str, dict] = {}
    if not path.is_file():
        print(f"status: fail\nerror: PDF not found: {path}")
        return 1
    data = path.read_bytes()
    checks["header"] = {"status": "pass" if data.startswith(b"%PDF") else "fail", "value": data[:8].decode("latin1", "replace")}
    if not data.startswith(b"%PDF"):
        errors.append("file does not start with %PDF")
    if not data.rstrip().endswith(b"%%EOF"):
        warnings.append("file does not end with %%EOF marker")
    checks["size"] = {"status": "pass", "bytes": len(data)}

    pdfinfo = shutil.which("pdfinfo")
    if pdfinfo:
        code, out, err = run([pdfinfo, str(path)])
        info = {}
        for line in out.splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                info[key.strip()] = value.strip()
        checks["pdfinfo"] = {"status": "pass" if code == 0 else "fail", "pages": info.get("Pages"), "page_size": info.get("Page size"), "encrypted": info.get("Encrypted")}
        if code != 0:
            errors.append(f"pdfinfo failed: {err.strip()[:200]}")
        if info.get("Encrypted", "").lower() == "yes":
            errors.append("PDF is encrypted")
        if not info.get("Pages"):
            warnings.append("page count unavailable")
    else:
        checks["pdfinfo"] = {"status": "not_checked", "reason": "pdfinfo not found"}
        warnings.append("pdfinfo not available")

    pdftotext = shutil.which("pdftotext")
    if pdftotext:
        code, out, err = run([pdftotext, str(path), "-"])
        text = out.strip()
        checks["text"] = {"status": "pass" if code == 0 else "fail", "characters": len(text)}
        if code != 0:
            warnings.append(f"pdftotext failed: {err.strip()[:160]}")
        elif not text:
            warnings.append("PDF has no extractable text; may be image-only")
    else:
        checks["text"] = {"status": "not_checked", "reason": "pdftotext not found"}
        warnings.append("pdftotext not available; searchable-text check skipped")

    pdftoppm = shutil.which("pdftoppm")
    if args.no_render:
        checks["render"] = {"status": "not_checked", "reason": "render skipped by --no-render"}
        warnings.append("first-page render check skipped")
    elif pdftoppm:
        with tempfile.TemporaryDirectory(prefix="slideflow-pdf-") as td:
            prefix = Path(td) / "page"
            code, out, err = run([pdftoppm, "-f", "1", "-singlefile", "-png", str(path), str(prefix)])
            image = prefix.with_suffix(".png")
            checks["render"] = {"status": "pass" if code == 0 and image.is_file() else "fail", "first_page_rendered": image.is_file()}
            if code != 0 or not image.is_file():
                errors.append(f"first page render failed: {err.strip()[:160]}")
    else:
        checks["render"] = {"status": "not_checked", "reason": "pdftoppm not found"}
        warnings.append("pdftoppm not available; visual render check skipped")

    status = "pass" if not errors else "fail"
    payload = {"status": status, "errors": errors, "warnings": warnings, "checks": checks}
    if args.format == "json":
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"status: {status}")
        print(f"file: {path}")
        for key, value in checks.items():
            print(f"- {key}: {value.get('status')}")
        print(f"errors: {len(errors)}")
        for item in errors:
            print(f"- {item}")
        print(f"warnings: {len(warnings)}")
        for item in warnings:
            print(f"- {item}")
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
