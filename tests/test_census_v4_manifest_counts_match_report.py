import unittest

from tests.census_v4_test_helpers import census_v4_artifacts


class CensusV4ManifestCountsMatchReportTests(unittest.TestCase):
    def test_manifest_counts_match_stage_summary_and_leaf_audit(self):
        artifacts = census_v4_artifacts()
        manifest_by_name = {row["name"]: row for row in artifacts["artifact_manifest"]["artifacts"]}
        summary = artifacts["stage_summary"]
        audit = artifacts["leaf_audit"]

        self.assertEqual(manifest_by_name["census_stage_status.jsonl"]["row_count"], summary["stage_status_count"])
        self.assertEqual(manifest_by_name["census_stage_map.jsonl"]["row_count"], summary["stage_status_count"])
        self.assertEqual(manifest_by_name["census_stage_map.csv"]["row_count"], summary["stage_status_count"])
        self.assertEqual(manifest_by_name["full_thesis_smoke_tasks.jsonl"]["row_count"], 14)
        self.assertEqual(
            manifest_by_name["full_thesis_refresh_queue.jsonl"]["row_count"],
            summary["full_thesis_refresh_queue_candidate_count"],
        )
        self.assertEqual(manifest_by_name["accepted_claims.jsonl"]["row_count"], 106)
        self.assertEqual(manifest_by_name["score_contributions.jsonl"]["row_count"], 106)
        self.assertEqual(manifest_by_name["stagecourt_traces.jsonl"]["row_count"], 94)
        full_thesis_row_count = summary["stage_scope_distribution"].get("FULL_THESIS", 0)
        self.assertEqual(
            manifest_by_name["claim_to_stage_trace.jsonl"]["row_count"],
            summary["stage_status_count"] + full_thesis_row_count,
        )
        self.assertEqual(summary["verified_score_present_count"], 2)
        self.assertEqual(summary["stage_scope_distribution"], audit["metrics"]["stage_scope_distribution"])
        self.assertEqual(summary["score_scope_distribution"], audit["metrics"]["score_scope_distribution"])
        self.assertEqual(
            summary["full_thesis_refresh_queue_candidate_count"],
            audit["metrics"]["full_thesis_refresh_queue_candidate_count"],
        )
        self.assertEqual(summary["full_e2r_verified_score_count"], audit["metrics"]["full_e2r_verified_score_present_count"])
        self.assertEqual(summary["event_evidence_score_count"], audit["metrics"]["event_evidence_score_present_count"])


if __name__ == "__main__":
    unittest.main()
