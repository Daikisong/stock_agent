import unittest
import json
import tempfile
from pathlib import Path

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

    def test_frozen_repeat_variance_uses_watchlist_score_stage_hash(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            watchlist = {
                "rows": [
                    {
                        "candidate_event_id": "CE-LIVE-DART-000001-20260619000001",
                        "verified_score": 4.4,
                        "score_valid_status": "FINAL_WITH_NONMATERIAL_GAPS",
                        "base_stage": "1",
                        "accepted_claim_ids": ["CLM-1"],
                        "score_contribution_ids": ["SCON-1"],
                    }
                ]
            }
            for index in range(1, 4):
                run = root / f"frozen-2026-06-19-r{index}"
                run.mkdir()
                (run / "daily_watchlist.json").write_text(json.dumps(watchlist), encoding="utf-8")
                audit = {
                    "final_status": "IMPLEMENTATION_MERGED",
                    "metadata": {"git_head_sha": "sha", "repo_dirty": False},
                    "config": {"mode": "frozen_replay", "as_of_date": "2026-06-19"},
                    "summary": {
                        "candidate": {
                            "total_candidate_event_count": 50,
                            "production_eligible_candidate_event_count": 50,
                            "fixture_candidate_event_count_in_production": 0,
                        },
                        "source": {"provider_failure_count": 0, "snapshot_only_counted_as_live_count": 0},
                        "planner": {"real_planner_success_count": 0, "fake_frozen_provider_used_count": 0},
                        "extraction": {"accepted_claim_count": 50},
                        "score_stage": {
                            "deterministic_scorer_output_count": 50,
                            "run_specific_summary_noise": index,
                        },
                        "static": {"critical_count_sum": 0},
                    },
                }
                (run / "audit_summary.json").write_text(json.dumps(audit), encoding="utf-8")

            bundle = build_production_cutover_bundle(
                config=ProductionCutoverConfig(
                    as_of_date="2026-06-30",
                    validation_output_root=str(root),
                ),
                repo_root=".",
                command="unit-test",
            )
            repeat_rows = {
                row["as_of_date"]: row for row in bundle["multiday_validation"]["repeat_rows"]
            }
            self.assertEqual(repeat_rows["2026-06-19"]["repeat_variance"], 0)
            self.assertEqual(repeat_rows["2026-06-19"]["unique_score_stage_hash_count"], 1)


if __name__ == "__main__":
    unittest.main()
