import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3EventTaxonomyTests(unittest.TestCase):
    def test_event_taxonomy_contains_official_market_ledger(self):
        events = census_v3_artifacts()["events"]
        categories = {row["event_category"] for row in events}
        self.assertIn("CensusAssessmentEvent", categories)
        self.assertIn("OfficialEvent", categories)
        self.assertIn("MarketAnomalyEvent", categories)
        self.assertIn("ExistingClaimEvent", categories)
        assessment_events = [row for row in events if row["event_category"] == "CensusAssessmentEvent"]
        self.assertTrue(assessment_events)
        self.assertTrue(all(not row["score_evidence_allowed"] for row in assessment_events))


if __name__ == "__main__":
    unittest.main()
