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

    def test_github_ecosystem(self) -> None:
        text = (ROOT / "references" / "github-ppt-skills.md").read_text(encoding="utf-8")
        for repo in ("anthropics/skills", "hugohe3/ppt-master", "getsentry/skills", "claude-office-skills/skills"):
            self.assertIn(repo, text)
        self.assertIn("AGPL", text)
        self.assertIn("reference only", text)
        self.assertIn("Official/plugin skills found locally", text)

    def test_handoff_schema(self) -> None:
        text = (ROOT / "references" / "handoff-schemas.md").read_text(encoding="utf-8")
        for field in ("output_mode", "deck_profile", "quality_tier", "style_contract", "render"):
            self.assertIn(field, text)


if __name__ == "__main__":
    unittest.main()
