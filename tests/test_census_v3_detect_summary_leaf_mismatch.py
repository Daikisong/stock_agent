import unittest

from census_v3_test_helpers import read_json, temp_census_v3_copy, write_json
from e2r.census.leaf_artifact_auditor import audit_leaf_artifacts


class CensusV3DetectSummaryLeafMismatchTests(unittest.TestCase):
    def test_summary_distribution_mismatch_is_critical(self):
        tmp, root = temp_census_v3_copy()
        self.addCleanup(tmp.cleanup)
        path = root / "census_stage_summary.json"
        summary = read_json(path)
        summary["stage_distribution"] = {"Stage0": 999999}
        write_json(path, summary)
        audit = audit_leaf_artifacts(root)
        self.assertGreater(audit["critical_counts"]["report_leaf_mismatch_count"], 0)


if __name__ == "__main__":
    unittest.main()
