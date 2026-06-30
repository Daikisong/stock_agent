import unittest

from census_v3_test_helpers import read_json, temp_census_v3_copy, write_json
from e2r.census.leaf_artifact_auditor import audit_leaf_artifacts


class CensusV3DetectEmptyBaselineTests(unittest.TestCase):
    def test_empty_baseline_summary_is_critical(self):
        tmp, root = temp_census_v3_copy()
        self.addCleanup(tmp.cleanup)
        summary_path = root / "baseline_inputs_summary.json"
        summary = read_json(summary_path)
        summary["empty_baseline_inputs_count"] = 1
        write_json(summary_path, summary)
        audit = audit_leaf_artifacts(root)
        self.assertGreater(audit["critical_counts"]["empty_baseline_inputs_count"], 0)


if __name__ == "__main__":
    unittest.main()
