import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3SourceTaskExecutionNotFakeTests(unittest.TestCase):
    def test_evidence_os_accepted_executions_have_claims(self):
        executions = census_v3_artifacts()["source_task_executions"]
        accepted = [row for row in executions if row.get("status") == "EVIDENCE_OS_ACCEPTED"]
        self.assertGreater(len(accepted), 0)
        self.assertTrue(all(row.get("accepted_claim_ids") for row in accepted))


if __name__ == "__main__":
    unittest.main()
