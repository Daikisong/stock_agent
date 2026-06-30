import unittest

from census_v3_test_helpers import temp_census_v3_copy, write_jsonl
from e2r.census.leaf_artifact_auditor import audit_leaf_artifacts


class CensusV3DetectReportOnlyPassTests(unittest.TestCase):
    def test_report_only_without_claims_or_tasks_cannot_pass(self):
        tmp, root = temp_census_v3_copy()
        self.addCleanup(tmp.cleanup)
        for name in ("accepted_claims.jsonl", "score_contributions.jsonl", "source_tasks.jsonl", "source_task_executions.jsonl"):
            write_jsonl(root / name, [])
        audit = audit_leaf_artifacts(root)
        self.assertGreater(audit["critical_counts"]["accepted_claim_total_zero_count"], 0)
        self.assertGreater(audit["critical_counts"]["source_task_total_zero_count"], 0)


if __name__ == "__main__":
    unittest.main()
