import unittest

from census_v3_test_helpers import read_jsonl, temp_census_v3_copy, write_jsonl
from e2r.census.leaf_artifact_auditor import audit_leaf_artifacts


class CensusV3DetectThresholdLooseningTests(unittest.TestCase):
    def test_single_stage_bucket_still_fails_even_if_report_claims_pass(self):
        tmp, root = temp_census_v3_copy()
        self.addCleanup(tmp.cleanup)
        rows = read_jsonl(root / "census_stage_status.jsonl")
        for row in rows:
            row["base_stage"] = "Stage0"
            row["census_status"] = "SCANNED"
        write_jsonl(root / "census_stage_status.jsonl", rows)
        audit = audit_leaf_artifacts(root)
        self.assertGreater(audit["critical_counts"]["single_stage_bucket_count"], 0)
        self.assertGreater(audit["critical_counts"]["single_status_bucket_count"], 0)


if __name__ == "__main__":
    unittest.main()
