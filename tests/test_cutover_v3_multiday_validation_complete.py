import unittest

from e2r.production.cutover_v3 import ProductionCutoverV3Config, _multiday_validation_v3
from tests.cutover_v3_test_helpers import fake_provider_matrix, fake_v3_base, fake_v3_frozen_base


class CutoverV3MultidayValidationCompleteTests(unittest.TestCase):
    def test_multiday_pass_requires_live_frozen_and_repeat_counts(self):
        bases = [fake_v3_base(f"2026-06-{day:02d}") for day in range(24, 29)]
        frozen_bases = [
            fake_v3_frozen_base(f"2026-06-{day:02d}", run_index=run_index)
            for day in range(15, 29)
            for run_index in (1, 2, 3)[: (3 if day < 18 else 1)]
        ]
        report = _multiday_validation_v3(
            base_bundles=bases,
            frozen_bundles=frozen_bases,
            provider_matrix=fake_provider_matrix(),
            config=ProductionCutoverV3Config(as_of_date="2026-06-30", live_shadow_days=5),
        )
        self.assertEqual(report["summary"]["status"], "MULTIDAY_SHADOW_PASS")
        self.assertGreaterEqual(report["summary"]["five_day_live_official_shadow_count"], 5)
        self.assertGreaterEqual(report["summary"]["frozen_replay_day_count"], 10)
        self.assertEqual(report["summary"]["repeat_variance"], 0)
        self.assertEqual(report["summary"]["source_corpus_repeat_variance"], 0)
        self.assertEqual(report["summary"]["replay_input_repeat_variance"], 0)
        repeat_rows = [row for row in report["frozen_rows"] if row.get("run_kind") == "frozen_repeat_group"]
        self.assertTrue(repeat_rows)
        self.assertTrue(all(row["source_corpus_repeat_variance"] == 0 for row in repeat_rows))
        self.assertTrue(all(row["replay_input_repeat_variance"] == 0 for row in repeat_rows))


if __name__ == "__main__":
    unittest.main()
