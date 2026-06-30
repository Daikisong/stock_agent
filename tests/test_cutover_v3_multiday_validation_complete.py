import unittest

from e2r.production.cutover_v3 import ProductionCutoverV3Config, _multiday_validation_v3
from tests.cutover_v3_test_helpers import fake_provider_matrix, fake_v3_base


class CutoverV3MultidayValidationCompleteTests(unittest.TestCase):
    def test_multiday_pass_requires_live_frozen_and_repeat_counts(self):
        bases = [fake_v3_base(f"2026-06-{day:02d}") for day in range(24, 29)]
        report = _multiday_validation_v3(
            base_bundles=bases,
            provider_matrix=fake_provider_matrix(),
            config=ProductionCutoverV3Config(as_of_date="2026-06-30", live_shadow_days=5),
        )
        self.assertEqual(report["summary"]["status"], "MULTIDAY_SHADOW_PASS")
        self.assertGreaterEqual(report["summary"]["five_day_live_official_shadow_count"], 5)
        self.assertGreaterEqual(report["summary"]["frozen_replay_day_count"], 10)
        self.assertEqual(report["summary"]["repeat_variance"], 0)


if __name__ == "__main__":
    unittest.main()
