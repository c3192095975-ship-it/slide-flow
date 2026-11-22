from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "discover_slide_skills.py"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class DiscoverSlideSkillsTests(unittest.TestCase):
    def test_capability_matrix(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            write(base / "a" / "story" / "SKILL.md", '---\nname: story\ndescription: "Presentation story outline and deck narrative."\n---\n')
            write(base / "b" / "pptx-edit" / "SKILL.md", '---\nname: pptx-edit\ndescription: "Edit pptx, patch deck, merge slides, render and visual QA."\n---\n')
            write(base / "c" / "html" / "SKILL.md", '---\nname: html\ndescription: "HTML presentation and reveal.js web deck."\n---\n')
            write(base / "d" / "image" / "SKILL.md", '---\nname: image\ndescription: "Image generation and image deck production."\n---\n')
            write(base / "e" / "access" / "SKILL.md", '---\nname: access\ndescription: "PowerPoint accessibility and WCAG alt text review."\n---\n')
            cmd = [sys.executable, str(SCRIPT), "--no-default-roots"]
            for name in "abcde":
                cmd += ["--root", str(base / name)]
            env = os.environ.copy(); env["PYTHONDONTWRITEBYTECODE"] = "1"
            data = json.loads(subprocess.run(cmd, check=True, capture_output=True, text=True, env=env).stdout)
            by = {s["name"]: s for s in data["skills"]}
            self.assertIn("story_outline", [c["name"] for c in by["story"]["capabilities"]])
            pptx_caps = [c["name"] for c in by["pptx-edit"]["capabilities"]]
            self.assertIn("pptx_editing", pptx_caps)
            self.assertIn("render_qa", pptx_caps)
            self.assertIn("html_deck", [c["name"] for c in by["html"]["capabilities"]])
            self.assertIn("image_generation", [c["name"] for c in by["image"]["capabilities"]])
            self.assertIn("accessibility", [c["name"] for c in by["access"]["capabilities"]])


if __name__ == "__main__":
    unittest.main()
