import unittest

from census_v3_test_helpers import read_jsonl, temp_census_v3_copy, write_jsonl
from e2r.census.leaf_artifact_auditor import audit_leaf_artifacts


class CensusV3DetectNewsSnippetScoreTests(unittest.TestCase):
    def test_snippet_contribution_is_critical(self):
        tmp, root = temp_census_v3_copy()
        self.addCleanup(tmp.cleanup)
        rows = read_jsonl(root / "score_contributions.jsonl")
        rows[0]["source_type"] = "snippet"
        write_jsonl(root / "score_contributions.jsonl", rows)
        audit = audit_leaf_artifacts(root)
        self.assertGreater(audit["critical_counts"]["news_snippet_to_score_count"], 0)


if __name__ == "__main__":
    unittest.main()
