import unittest

from census_v3_test_helpers import read_jsonl, temp_census_v3_copy, write_jsonl
from e2r.census.leaf_artifact_auditor import audit_leaf_artifacts


class CensusV3DetectSourceTaskReplayAsExecutionTests(unittest.TestCase):
    def test_parsed_replay_execution_is_critical(self):
        tmp, root = temp_census_v3_copy()
        self.addCleanup(tmp.cleanup)
        rows = read_jsonl(root / "source_task_executions.jsonl")
        rows[0]["status"] = "PARSED"
        rows[0]["accepted_claim_ids"] = []
        rows[0]["claim_producing_execution"] = False
        write_jsonl(root / "source_task_executions.jsonl", rows)
        audit = audit_leaf_artifacts(root)
        self.assertGreater(audit["critical_counts"]["source_task_fake_execution_count"], 0)


if __name__ == "__main__":
    unittest.main()
