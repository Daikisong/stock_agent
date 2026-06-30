import unittest

from e2r.census.lifecycle_refresh import adjudicate_lifecycle


class CensusV3ActiveOldContractCurrentTests(unittest.TestCase):
    def test_accepted_ledger_event_can_remain_current_without_recent_cutoff(self):
        decision = adjudicate_lifecycle(event={"score_evidence_eligible": True}, as_of_date="2026-07-01")
        self.assertEqual(decision.temporal_status, "CURRENT")
        self.assertTrue(decision.score_eligible)


if __name__ == "__main__":
    unittest.main()
