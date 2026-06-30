import unittest

from census_v2_test_helpers import census_v2_artifacts


class CensusV2SourceTimelineTests(unittest.TestCase):
    def test_every_eligible_symbol_has_timeline_and_assessment_event_is_not_score(self):
        artifacts = census_v2_artifacts()
        eligible = [row for row in artifacts["universe"] if row.get("eligible_for_census")]
        timelines = artifacts["timelines"]
        self.assertEqual(len(timelines), len(eligible))
        first = timelines[0]
        assessment = [event for event in first["events"] if event["event_type"] == "CensusAssessmentEvent"]
        self.assertEqual(len(assessment), 1)
        self.assertFalse(assessment[0]["score_evidence_eligible"])

    def test_timeline_contains_claim_source_and_candidate_source_lanes(self):
        artifacts = census_v2_artifacts()
        score_timelines = [row for row in artifacts["timelines"] if row["score_evidence_event_count"] > 0]
        candidate_timelines = [row for row in artifacts["timelines"] if row["candidate_event_count"] > 0]
        self.assertGreater(len(score_timelines), 0)
        self.assertGreater(len(candidate_timelines), len(score_timelines))


if __name__ == "__main__":
    unittest.main()
