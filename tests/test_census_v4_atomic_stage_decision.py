import json
import tempfile
import unittest
from pathlib import Path

from e2r.census.census_v4_auditor import audit_census_v4_leaf_artifacts
from tests.census_v4_test_helpers import census_v4_artifacts


class CensusV4AtomicStageDecisionTests(unittest.TestCase):
    def test_leaf_audit_has_no_atomic_mismatch(self):
        audit = census_v4_artifacts()["leaf_audit"]
        self.assertEqual(audit["critical_counts"]["stage_trace_stage_mismatch_count"], 0)
        self.assertEqual(audit["critical_counts"]["stage_trace_scope_mismatch_count"], 0)
        self.assertEqual(audit["critical_counts"]["stage_trace_score_scope_mismatch_count"], 0)
        self.assertEqual(audit["critical_counts"]["stage_trace_score_interval_mismatch_count"], 0)
        self.assertEqual(audit["critical_counts"]["stage_trace_score_status_mismatch_count"], 0)
        self.assertEqual(audit["critical_counts"]["stage_trace_claim_set_mismatch_count"], 0)
        self.assertEqual(audit["critical_counts"]["stage_trace_contribution_set_mismatch_count"], 0)
        self.assertEqual(audit["critical_counts"]["stagecourt_score_recompute_mismatch_count"], 0)
        self.assertEqual(audit["critical_counts"]["stagecourt_score_contribution_ref_missing_count"], 0)

    def test_every_scored_row_points_to_atomic_decision(self):
        for row in census_v4_artifacts()["stage_rows"]:
            if row["score_scale"] != "NO_SCORE":
                self.assertTrue(row["atomic_stage_decision_id"])
                self.assertTrue(row["stagecourt_trace_id"])
                self.assertTrue(row["accepted_claim_ids"])
                self.assertTrue(row["score_contribution_ids"])

    def test_atomic_decision_carries_stage_and_score_scope(self):
        for row in census_v4_artifacts()["atomic_rows"]:
            self.assertIn(row["stage_scope"], {"CENSUS_EVENT_BOARD", "FULL_THESIS"})
            if row["stage_scope"] == "FULL_THESIS":
                self.assertEqual(row["score_scope"], "FULL_E2R_100")
            else:
                self.assertIn(row["score_scope"], {"NO_SCORE", "EVENT_WEIGHTED_PARTIAL"})

    def test_stagecourt_score_interval_must_match_deterministic_recompute(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            _write_jsonl(
                root / "stagecourt_traces.jsonl",
                [
                    {
                        "stagecourt_trace_id": "SCT-MISMATCH",
                        "symbol": "005930",
                        "candidate_event_id": "CEV4-X",
                        "source_cutover_date": "2026-07-01",
                        "primary_archetype": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                        "score_interval": {"lower": 99.0, "upper": 99.0},
                        "score_contribution_ids": ["SCON-A", "SCON-B"],
                    }
                ],
            )
            _write_jsonl(
                root / "score_contributions.jsonl",
                [
                    {
                        "score_contribution_id": "SCON-A",
                        "component_key": "eps_fcf_explosion",
                        "criterion_id": "unit_eps",
                        "raw_points": 20.0,
                        "max_points": 20.0,
                        "support_claim_ids": ["CLM-A"],
                    },
                    {
                        "score_contribution_id": "SCON-B",
                        "component_key": "earnings_visibility",
                        "criterion_id": "unit_visibility",
                        "raw_points": 6.6667,
                        "max_points": 20.0,
                        "support_claim_ids": ["CLM-B"],
                    },
                ],
            )

            audit = audit_census_v4_leaf_artifacts(root)

        self.assertEqual(audit["critical_counts"]["stagecourt_score_recompute_mismatch_count"], 1)
        sample = audit["metrics"]["stagecourt_score_recompute_mismatch_samples"][0]
        self.assertEqual(sample["stagecourt_trace_id"], "SCT-MISMATCH")
        self.assertEqual(sample["score_interval_lower"], 99.0)
        self.assertGreater(sample["recomputed_verified_score"], 0.0)
        self.assertNotEqual(sample["score_interval_lower"], sample["recomputed_verified_score"])


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
