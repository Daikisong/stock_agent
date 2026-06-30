import unittest

from census_v3_test_helpers import read_jsonl, temp_census_v3_copy, write_jsonl
from e2r.census.leaf_artifact_auditor import audit_leaf_artifacts


class CensusV3AllUnknownFailsTests(unittest.TestCase):
    def test_all_unknown_is_critical(self):
        tmp, root = temp_census_v3_copy()
        self.addCleanup(tmp.cleanup)
        rows = read_jsonl(root / "census_stage_status.jsonl")
        for row in rows:
            row["base_stage"] = "Unknown"
        write_jsonl(root / "census_stage_status.jsonl", rows)
        audit = audit_leaf_artifacts(root)
        self.assertGreater(audit["critical_counts"]["all_unknown_count"], 0)


if __name__ == "__main__":
    unittest.main()
