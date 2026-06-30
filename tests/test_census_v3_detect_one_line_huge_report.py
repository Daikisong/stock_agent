import unittest

from census_v3_test_helpers import temp_census_v3_copy
from e2r.census.leaf_artifact_auditor import audit_leaf_artifacts


class CensusV3DetectOneLineHugeReportTests(unittest.TestCase):
    def test_one_line_large_markdown_report_is_critical(self):
        tmp, root = temp_census_v3_copy()
        self.addCleanup(tmp.cleanup)
        (root / "bad_report.md").write_text("x" * 600, encoding="utf-8")
        audit = audit_leaf_artifacts(root)
        self.assertGreater(audit["critical_counts"]["one_line_large_report_count"], 0)


if __name__ == "__main__":
    unittest.main()
