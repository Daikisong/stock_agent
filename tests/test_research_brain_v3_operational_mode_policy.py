import unittest
from dataclasses import replace

from e2r.research_brain.v3_schemas import OperationalMode, OperationalModePreset, production_daily_preset


class ResearchBrainV3OperationalModePolicyTests(unittest.TestCase):
    def test_production_daily_preset_is_bounded(self):
        preset = production_daily_preset()
        self.assertEqual(preset.mode, OperationalMode.PRODUCTION_DAILY)
        self.assertIsNotNone(preset.top_results)
        self.assertIsNotNone(preset.retry_max)
        self.assertIsNotNone(preset.max_fetches_per_task)

    def test_unbounded_production_preset_rejected(self):
        preset = OperationalModePreset(
            mode=OperationalMode.PRODUCTION_DAILY,
            max_results_per_query=100,
            top_results=None,
            retry_max=2,
            max_fetches_per_task=5,
            general_web_fallback_allowed=False,
            fake_provider_allowed=False,
            production_readiness_allowed=True,
        )
        with self.assertRaises(ValueError):
            preset.validate()


if __name__ == "__main__":
    unittest.main()
