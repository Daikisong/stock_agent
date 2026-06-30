import unittest

from e2r.production.cutover_v2 import _trigger_taxonomy


class CensusAssessmentTriggerNoForcedScoreTests(unittest.TestCase):
    def test_census_assessment_trigger_exists_without_forced_score(self):
        taxonomy = _trigger_taxonomy()
        census = [row for row in taxonomy["categories"] if row["trigger_category"] == "Census Assessment Trigger"][0]
        self.assertEqual(census["score_eligibility_policy"], "accepted_claim_required")


if __name__ == "__main__":
    unittest.main()
