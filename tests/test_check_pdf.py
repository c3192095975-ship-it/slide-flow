from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check_pdf.py"
SAMPLE = ROOT / "examples" / "research-competition" / "sample-delivery.pdf"


class CheckPdfTests(unittest.TestCase):
    def test_sample_pdf_structure(self) -> None:
        self.assertTrue(SAMPLE.is_file())
        result = subprocess.run([sys.executable, str(SCRIPT), "--pdf", str(SAMPLE), "--no-render"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("header: pass", result.stdout)

    def test_missing_pdf_fails(self) -> None:
        result = subprocess.run([sys.executable, str(SCRIPT), "--pdf", "/tmp/does-not-exist-slide-flow.pdf"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("PDF not found", result.stdout)


if __name__ == "__main__":
    unittest.main()
