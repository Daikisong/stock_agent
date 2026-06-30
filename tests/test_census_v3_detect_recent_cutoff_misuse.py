import unittest

from census_v3_test_helpers import read_jsonl, temp_census_v3_copy, write_jsonl
from e2r.census.leaf_artifact_auditor import audit_leaf_artifacts


class CensusV3DetectRecentCutoffMisuseTests(unittest.TestCase):
    def test_recent_cutoff_flag_is_critical(self):
        tmp, root = temp_census_v3_copy()
        self.addCleanup(tmp.cleanup)
        rows = read_jsonl(root / "census_stage_status.jsonl")
        rows[0]["recent_lookback_cutoff_used"] = True
        write_jsonl(root / "census_stage_status.jsonl", rows)
        audit = audit_leaf_artifacts(root)
        self.assertGreater(audit["critical_counts"]["recent_lookback_used_as_stage_cutoff_count"], 0)


if __name__ == "__main__":
    unittest.main()
