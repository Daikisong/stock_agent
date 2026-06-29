import unittest

from e2r.production.cutover_shadow import ProductionCutoverConfig, _readiness_blockers, build_production_cutover_bundle


class CutoverNoProductionReadyWithBlockersTests(unittest.TestCase):
    def test_blockers_force_not_ready(self):
        bundle = build_production_cutover_bundle(
            config=ProductionCutoverConfig(as_of_date="2026-06-30"),
            repo_root=".",
            command="unit-test",
        )
        self.assertFalse(bundle["shadow_latest"]["production_ready"])
        self.assertEqual(bundle["shadow_latest"]["production_verdict"], "NOT_READY")
        self.assertTrue(bundle["shadow_latest"]["blockers"])

    def test_a2_provider_gap_still_blocks_production_ready(self):
        blockers = _readiness_blockers(
            metadata={"repo_dirty": False},
            candidate_purity={
                "summary": {
                    "actual_krx_universe_count": 3972,
                    "production_eligible_candidate_event_count": 50,
                    "fixture_candidate_event_count_in_production": 0,
                    "cached_path_count": 0,
                    "sector_coverage": {
                        "summary": {
                            "active_large_sector_count": 9,
                            "unknown_sector_candidate_count": 0,
                        }
                    },
                }
            },
            source_connector_report={
                "summary": {
                    "real_source_document_fetched_count": 50,
                    "snapshot_only_document_count": 0,
                    "stored_snapshot_only_documents": 0,
                }
            },
            claim_extraction_audit={"summary": {"accepted_claim_count": 20}},
            planner_provider_report={
                "summary": {
                    "real_planner_success_count": 30,
                    "planner_provider_model_null_count": 0,
                    "planner_default_model_unpinned_count": 0,
                    "raw_prompt_response_file_missing_count": 0,
                }
            },
            score_meaning_audit={"summary": {"deterministic_scorer_output_count": 15}},
            memory_usage_audit={
                "summary": {
                    "A2_REAL_REPLAY_VERIFIED_count": 0,
                    "A2_source_provider_gap": True,
                }
            },
            config=ProductionCutoverConfig(as_of_date="2026-06-30"),
        )
        self.assertEqual(
            blockers,
            ["A2 real replay verified count is 0; explicit source/provider gap keeps cutover NOT_READY"],
        )


if __name__ == "__main__":
    unittest.main()
