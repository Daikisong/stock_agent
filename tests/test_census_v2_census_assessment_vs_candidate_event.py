import unittest

from census_v2_test_helpers import census_v2_artifacts


class CensusV2AssessmentVsCandidateEventTests(unittest.TestCase):
    def test_census_assessment_count_is_full_universe_but_candidate_event_is_selective(self):
        artifacts = census_v2_artifacts()
        eligible_count = sum(1 for row in artifacts["universe"] if row.get("eligible_for_census"))
        self.assertEqual(len(artifacts["events"]), eligible_count)
        self.assertLess(len(artifacts["candidate_events"]), eligible_count)
        self.assertGreater(len(artifacts["candidate_events"]), 0)

    def test_candidate_event_opens_investigation_not_score(self):
        artifacts = census_v2_artifacts()["candidate_events"]
        for event in artifacts:
            self.assertFalse(event["score_evidence_eligible"])
        self.assertGreater(len(artifacts), 0)


if __name__ == "__main__":
    unittest.main()
