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
        for key in (
            "planner_runtime_seconds",
            "source_acquisition_runtime_seconds",
            "extraction_runtime_seconds",
            "scoring_runtime_seconds",
            "max_candidate_runtime_seconds",
            "max_source_task_runtime_seconds",
        ):
            self.assertIsInstance(summary[key], (int, float))
            self.assertGreaterEqual(summary[key], 0)
        phase_total = (
            summary["planner_runtime_seconds"]
            + summary["source_acquisition_runtime_seconds"]
            + summary["extraction_runtime_seconds"]
            + summary["scoring_runtime_seconds"]
        )
        self.assertLessEqual(phase_total, summary["total_runtime_seconds"] + 0.001)
        self.assertEqual(
            summary["phase_runtime_measurement_mode"],
            "planner_observed_source_extraction_scoring_estimated_from_remaining_wall_time",
        )


if __name__ == "__main__":
    unittest.main()
