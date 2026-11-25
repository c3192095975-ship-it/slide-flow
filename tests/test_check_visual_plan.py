from __future__ import annotations
import json, subprocess, sys, tempfile, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class VisualPlanTests(unittest.TestCase):
    def run_check(self, specs, plan=None):
        with tempfile.TemporaryDirectory() as d:
            sp=Path(d)/'specs.json'; sp.write_text(json.dumps(specs),encoding='utf-8')
            cmd=[sys.executable,str(ROOT/'scripts'/'check_visual_plan.py'),'--specs',str(sp)]
            if plan is not None:
                pp=Path(d)/'plan.json'; pp.write_text(json.dumps(plan),encoding='utf-8'); cmd += ['--plan',str(pp)]
            return subprocess.run(cmd,capture_output=True,text=True)
    def test_valid_visual_spec(self):
        v={"visual_id":"V1","slide_id":"S1","visual_type":"mechanism","purpose":"explain feedback","source_data_or_asset":"method notes","output_format":"svg","editability_requirement":"editable_in_ppt","caption_or_source_note":"Conceptual diagram","source_type":"concept"}
        self.assertEqual(self.run_check({"visuals":[v]}).returncode,0)
    def test_data_chart_requires_data_source_type(self):
        v={"visual_id":"V1","slide_id":"S1","visual_type":"data_chart","purpose":"compare","source_data_or_asset":"unknown","output_format":"svg","editability_requirement":"editable_in_ppt"}
        self.assertEqual(self.run_check({"visuals":[v]}).returncode,1)
    def test_png_not_editable(self):
        v={"visual_id":"V1","slide_id":"S1","visual_type":"concept","purpose":"show concept","source_data_or_asset":"brief","output_format":"png","editability_requirement":"editable_in_ppt"}
        self.assertEqual(self.run_check({"visuals":[v]}).returncode,1)
if __name__ == '__main__': unittest.main()
