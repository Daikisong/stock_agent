import unittest

from e2r.census.census_v4_auditor import _sample_bundle_missing_scored_row_count, _stage_row_fingerprint
from tests.census_v4_test_helpers import census_v4_artifacts


class CensusV4SampleBundleContainsAllScoredRowsTests(unittest.TestCase):
    def test_sample_bundle_contains_all_scored_or_claim_backed_rows(self):
        artifacts = census_v4_artifacts()
        sample_fingerprints = {_stage_row_fingerprint(row) for row in artifacts["sample_rows"]}
        missing = []
        for row in artifacts["stage_rows"]:
            if row.get("score_scale") != "NO_SCORE" or row.get("accepted_claim_ids") or row.get("score_contribution_ids"):
                if _stage_row_fingerprint(row) not in sample_fingerprints:
                    missing.append(row.get("symbol"))
        self.assertEqual(missing, [])
        self.assertEqual(artifacts["leaf_audit"]["critical_counts"]["sample_bundle_missing_scored_row_count"], 0)

    def test_symbol_only_sample_row_is_not_enough(self):
        stage_row = {
            "symbol": "000001",
            "score_scale": "EVENT_WEIGHTED_PARTIAL",
            "accepted_claim_ids": ["CLM-1"],
            "score_contribution_ids": ["SCON-1"],
            "base_stage": "Stage1",
        }
        self.assertEqual(_sample_bundle_missing_scored_row_count([stage_row], [{"symbol": "000001"}]), 1)
        self.assertEqual(_sample_bundle_missing_scored_row_count([stage_row], [dict(stage_row)]), 0)


if __name__ == "__main__":
    unittest.main()
