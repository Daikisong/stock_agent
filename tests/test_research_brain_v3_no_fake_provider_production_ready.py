import unittest
from pathlib import Path

from research_brain_v2_test_helpers import load_json


class ResearchBrainV3NoFakeProviderProductionReadyTests(unittest.TestCase):
    def test_fake_provider_blocks_production_ready(self):
        planner = load_json("docs/operational/research_brain_v3_real_planner_provider_report.json")
        verdict_text = Path("docs/operational/research_brain_v3_production_readiness_verdict.md").read_text(encoding="utf-8")
        self.assertGreater(planner["summary"]["fake_provider_used_count"], 0)
        self.assertIn("production_ready: False", verdict_text)
        self.assertIn("fake planner provider used", verdict_text)


if __name__ == "__main__":
    unittest.main()
