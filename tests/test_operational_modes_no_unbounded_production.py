import unittest

from e2r.research_brain.v3_schemas import production_daily_preset


class OperationalModesNoUnboundedProductionTests(unittest.TestCase):
    def test_production_daily_has_no_unbounded_defaults(self):
        preset = production_daily_preset()
        self.assertIsNotNone(preset.top_results)
        self.assertIsNotNone(preset.retry_max)
        self.assertIsNotNone(preset.max_fetches_per_task)
        self.assertFalse(preset.general_web_fallback_allowed)


if __name__ == "__main__":
    unittest.main()
