import unittest

from e2r.research_brain.v2_llm_planner import planner_provider_status
from research_brain_v2_test_helpers import load_json


class ResearchBrainV2ReadinessVerdictTests(unittest.TestCase):
    def test_report_verdict_is_shadow_ready_not_production_ready(self):
        verdict = load_json("docs/operational/research_brain_v2_readiness_verdict.json")
        summary = verdict["summary"]
        self.assertEqual(summary["production_verdict"], "READY_FOR_SHADOW_DAILY_RUN")
        self.assertTrue(summary["ready_for_shadow_daily_run"])
        self.assertFalse(summary["production_ready"])
        self.assertIn("PRODUCTION_READY requires at least 5 frozen daily runs", summary["production_blockers"])

    def test_fake_provider_blocks_production_ready_status(self):
        status = planner_provider_status(real_provider_available=True, fake_provider_used=True)
        self.assertEqual(status["readiness_effect"], "fake_provider_blocks_production_ready")


if __name__ == "__main__":
    unittest.main()
