from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check_svg.py"


class CheckSvgTests(unittest.TestCase):
    def test_valid_vector_svg(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            svg = base / "asset.svg"
            svg.write_text('<svg xmlns="http://www.w3.org/2000/svg"><g id="nodes"><rect width="10" height="10"/></g><g id="labels"><text x="0" y="0">Input</text></g></svg>', encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), "--svg", str(svg)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout)

    def test_embedded_image_fails(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            svg = base / "bad.svg"
            spec = base / "spec.json"
            svg.write_text('<svg xmlns="http://www.w3.org/2000/svg"><image href="data:image/png;base64,AAAA"/></svg>', encoding="utf-8")
            spec.write_text(json.dumps({"vector_required": True, "raster_embedded": False, "editable_text_required": True}), encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), "--svg", str(svg), "--spec", str(spec)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn("image", result.stdout)
            self.assertIn("base64", result.stdout)


if __name__ == "__main__":
    unittest.main()
