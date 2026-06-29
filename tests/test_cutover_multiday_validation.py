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
        self.assertIn("live_official_dry_run_count", summary)
        self.assertIn("frozen_replay_day_count", summary)

    def test_frozen_replay_uses_snapshot_without_live_source_credit(self):
        bundle = build_production_cutover_bundle(
            config=ProductionCutoverConfig(
                as_of_date="2026-06-30",
                mode="frozen_replay",
                frozen_snapshot_dir="output/production_cutover/2026-06-30",
                output_dir="output/production_cutover/2026-06-30-frozen-unit",
            ),
            repo_root=".",
            command="unit-test-frozen",
        )
        source = bundle["source_connector_report"]["summary"]
        self.assertEqual(source["real_source_document_fetched_count"], 0)
        self.assertGreater(source["snapshot_only_document_count"], 0)
        self.assertEqual(source["snapshot_only_counted_as_live_count"], 0)
        rows = bundle["multiday_validation"]["rows"]
        frozen_rows = [row for row in rows if row["run_kind"] == "frozen"]
        self.assertTrue(frozen_rows)


if __name__ == "__main__":
    unittest.main()
