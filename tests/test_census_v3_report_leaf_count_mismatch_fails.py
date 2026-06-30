import unittest

from census_v3_test_helpers import read_json, temp_census_v3_copy, write_json
from e2r.census.leaf_artifact_auditor import audit_leaf_artifacts


class CensusV3ReportLeafCountMismatchFailsTests(unittest.TestCase):
    def test_mismatched_summary_is_critical(self):
        tmp, root = temp_census_v3_copy()
        self.addCleanup(tmp.cleanup)
        summary_path = root / "census_stage_summary.json"
        summary = read_json(summary_path)
        summary["accepted_claim_total"] += 1
        write_json(summary_path, summary)
        audit = audit_leaf_artifacts(root)
        self.assertGreater(audit["critical_counts"]["report_leaf_mismatch_count"], 0)


if __name__ == "__main__":
    unittest.main()
