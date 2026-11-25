from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SlideFlowContractTests(unittest.TestCase):
    def test_skill_contract(self) -> None:
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn('name: slide-flow', text)
        for mode in ("editable_pptx", "image_deck", "html_deck", "template_edit", "image_to_editable"):
            self.assertIn(mode, text)
        for gate in ("Gate A", "Gate B", "Gate C", "Gate D", "Gate E", "Gate F", "Gate G"):
            self.assertIn(gate, text)
        self.assertIn("one primary", text.lower())
        self.assertIn("Presentations", text)
        self.assertIn("template-creator", text)
        self.assertIn("univer-cli", text)
        self.assertIn("visual_asset", text)
        self.assertIn("Research fallback", text)
        self.assertIn("academic-ppt-master", text)
        self.assertIn("Gate H", text)
        self.assertIn("Scientific SVG", text)
        self.assertIn("micro-task", text)

    def test_github_ecosystem(self) -> None:
        text = (ROOT / "references" / "github-ppt-skills.md").read_text(encoding="utf-8")
        for repo in ("anthropics/skills", "hugohe3/ppt-master", "getsentry/skills", "claude-office-skills/skills"):
            self.assertIn(repo, text)
        self.assertIn("AGPL", text)
        self.assertIn("reference only", text)
        self.assertIn("Official/plugin skills found locally", text)
        self.assertIn("M1n-n9/academic-ppt-master", text)
        self.assertIn("c-narcissus/paper-framework-figure-studio-pro", text)

    def test_handoff_schema(self) -> None:
        text = (ROOT / "references" / "handoff-schemas.md").read_text(encoding="utf-8")
        for field in ("output_mode", "deck_profile", "quality_tier", "style_contract", "render"):
            self.assertIn(field, text)

    def test_v20_modules(self) -> None:
        for name in ("task-intelligence.md", "design-intelligence.md", "competition-excellence-mode.md", "visual-qa-protocol.md"):
            self.assertTrue((ROOT / "references" / name).is_file(), name)
        self.assertTrue((ROOT / "scripts" / "check_visual_plan.py").is_file())
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Gate K", skill)
        self.assertIn("scope lock", skill.lower())

    def test_v13_modules(self) -> None:
        for name in (
            "research-competition-profile.md",
            "scientific-visual-intelligence.md",
            "evidence-registry.md",
            "pdf-submission-qa.md",
            "design-reference-library.md",
            "benchmark-and-judge.md",
            "capability-verification.md",
        ):
            self.assertTrue((ROOT / "references" / name).is_file(), name)
        self.assertTrue((ROOT / "scripts" / "check_slide_plan.py").is_file())
        self.assertTrue((ROOT / "scripts" / "check_pdf.py").is_file())
        self.assertIn("research_competition", (ROOT / "references" / "deck-profiles.md").read_text(encoding="utf-8"))
        self.assertIn("Gate J", (ROOT / "references" / "quality-gates.md").read_text(encoding="utf-8"))
        self.assertTrue((ROOT / "references" / "scientific-svg-generation.md").is_file())
        self.assertTrue((ROOT / "references" / "skill-strength-matrix.md").is_file())
        self.assertTrue((ROOT / "scripts" / "check_svg.py").is_file())


if __name__ == "__main__":
    unittest.main()
