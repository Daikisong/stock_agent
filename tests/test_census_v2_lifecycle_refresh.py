import unittest

from e2r.census.lifecycle_refresh import adjudicate_lifecycle


class CensusV2LifecycleRefreshTests(unittest.TestCase):
    def test_old_stored_source_requires_refresh_and_is_not_score(self):
        decision = adjudicate_lifecycle(
            event={"source_family": "ReportRadar", "published_at": "2023-07-27", "score_evidence_eligible": False},
            as_of_date="2026-07-01",
        )
        self.assertEqual(decision.temporal_status, "HISTORICAL")
        self.assertFalse(decision.score_eligible)
        self.assertTrue(decision.followup_required)

    def test_accepted_claim_ledger_event_is_current_score_eligible(self):
        decision = adjudicate_lifecycle(
            event={"source_family": "ExistingEvidenceOSLedger", "score_evidence_eligible": True},
            as_of_date="2026-07-01",
        )
        self.assertEqual(decision.temporal_status, "CURRENT")
        self.assertTrue(decision.score_eligible)


if __name__ == "__main__":
    unittest.main()
