import unittest

from tests.census_v4_test_helpers import by_symbol, census_v4_artifacts


class CensusV4SemanticGuardTests(unittest.TestCase):
    def test_share_buyback_trust_does_not_score_as_contract_quality(self):
        row = by_symbol(census_v4_artifacts()["stage_rows"], "473980")
        self.assertEqual(row["semantic_guard_status"], "BLOCKED")
        self.assertEqual(row["semantic_guard_class"], "share_buyback_trust_contract")
        self.assertEqual(row["score_scale"], "NO_SCORE")
        self.assertEqual(row["base_stage"], "Stage1")

    def test_pledge_contract_does_not_score_as_customer_contract(self):
        row = by_symbol(census_v4_artifacts()["stage_rows"], "043260")
        self.assertEqual(row["semantic_guard_status"], "BLOCKED")
        self.assertEqual(row["semantic_guard_class"], "pledge_or_collateral_contract")
        self.assertEqual(row["score_scale"], "NO_SCORE")
        self.assertEqual(row["base_stage"], "Stage1")

    def test_facility_investment_correction_does_not_score_as_capacity_expansion(self):
        row = by_symbol(census_v4_artifacts()["stage_rows"], "003090")
        self.assertEqual(row["semantic_guard_status"], "BLOCKED")
        self.assertEqual(row["semantic_guard_class"], "facility_investment_correction_followup_required")
        self.assertEqual(row["score_scale"], "NO_SCORE")
        self.assertEqual(row["event_evidence_score"], None)
        self.assertEqual(row["raw_contribution_score"], None)
        self.assertEqual(row["base_stage"], "Stage1")


if __name__ == "__main__":
    unittest.main()
