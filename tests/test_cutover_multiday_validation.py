import unittest

from e2r.production.cutover_shadow import ProductionCutoverConfig, build_production_cutover_bundle


class CutoverMultidayValidationTests(unittest.TestCase):
    def test_multiday_report_exposes_required_counts(self):
        bundle = build_production_cutover_bundle(
            config=ProductionCutoverConfig(as_of_date="2026-06-30"),
            repo_root=".",
            command="unit-test",
        )
        summary = bundle["multiday_validation"]["summary"]
        self.assertIn("day_count", summary)
        self.assertIn("repeat_variance", summary)
        self.assertEqual(summary["required_frozen_day_count"], 10)


if __name__ == "__main__":
    unittest.main()
