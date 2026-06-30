import unittest

from census_v3_test_helpers import read_jsonl, temp_census_v3_copy, write_jsonl
from e2r.census.leaf_artifact_auditor import audit_leaf_artifacts


class CensusV3DetectProviderFailureFinalRedTests(unittest.TestCase):
    def test_provider_pending_with_final_score_is_critical(self):
        tmp, root = temp_census_v3_copy()
        self.addCleanup(tmp.cleanup)
        rows = read_jsonl(root / "census_stage_status.jsonl")
        rows[0]["census_status"] = "PENDING_PROVIDER"
        rows[0]["base_stage"] = "Red"
        rows[0]["verified_score"] = 1.0
        write_jsonl(root / "census_stage_status.jsonl", rows)
        audit = audit_leaf_artifacts(root)
        self.assertGreater(audit["critical_counts"]["provider_failed_final_score_count"], 0)


if __name__ == "__main__":
    unittest.main()
