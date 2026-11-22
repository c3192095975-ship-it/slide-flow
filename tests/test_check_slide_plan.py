from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check_slide_plan.py"


class CheckSlidePlanTests(unittest.TestCase):
    def test_valid_plan_and_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            plan = {
                "profile": "research_competition",
                "authoring_format": "editable_pptx",
                "delivery_format": "pdf",
                "slides": [{
                    "slide_id": "S01",
                    "title": "Title",
                    "takeaway": "Takeaway",
                    "claim": "Claim",
                    "evidence_ids": ["E01"],
                    "visual_type": "data_chart",
                    "visual_spec_id": "V01",
                    "data_source": "results.csv",
                }],
            }
            evidence = {"evidence": [{"evidence_id": "E01", "status": "user_provided"}]}
            (base / "plan.json").write_text(json.dumps(plan), encoding="utf-8")
            (base / "evidence.json").write_text(json.dumps(evidence), encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), "--plan", str(base / "plan.json"), "--evidence", str(base / "evidence.json")], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout)

    def test_missing_evidence_fails(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            plan = {
                "profile": "research_competition",
                "authoring_format": "editable_pptx",
                "delivery_format": "pdf",
                "slides": [{
                    "slide_id": "S01",
                    "title": "Title",
                    "takeaway": "Takeaway",
                    "claim": "Claim",
                    "evidence_ids": ["E99"],
                    "visual_type": "text_only",
                }],
            }
            evidence = {"evidence": [{"evidence_id": "E01", "status": "user_provided"}]}
            (base / "plan.json").write_text(json.dumps(plan), encoding="utf-8")
            (base / "evidence.json").write_text(json.dumps(evidence), encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), "--plan", str(base / "plan.json"), "--evidence", str(base / "evidence.json")], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn("E99", result.stdout)


if __name__ == "__main__":
    unittest.main()
