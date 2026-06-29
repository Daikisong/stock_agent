import unittest

from e2r.production.cutover_shadow import ProductionCutoverConfig, build_production_cutover_bundle


class CutoverSlaBudgetTests(unittest.TestCase):
    def test_sla_report_has_bounded_fetch_config(self):
        bundle = build_production_cutover_bundle(
            config=ProductionCutoverConfig(as_of_date="2026-06-30", max_fetches_per_task=3),
            repo_root=".",
            command="unit-test",
        )
        summary = bundle["sla_report"]["summary"]
        self.assertEqual(summary["unbounded_fetch_config_count"], 0)
        self.assertLessEqual(summary["total_runtime_seconds"], summary["max_total_runtime_seconds"])


if __name__ == "__main__":
    unittest.main()
