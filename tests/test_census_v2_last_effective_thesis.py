import unittest

from census_v2_test_helpers import census_v2_artifacts


class CensusV2LastEffectiveThesisTests(unittest.TestCase):
    def test_state_exists_for_every_eligible_symbol(self):
        artifacts = census_v2_artifacts()
        eligible = [row for row in artifacts["universe"] if row.get("eligible_for_census")]
        states = artifacts["thesis_states"]
        self.assertEqual(len(states), len(eligible))

    def test_active_source_pending_and_no_known_thesis_are_separate(self):
        statuses = {row["thesis_status"] for row in census_v2_artifacts()["thesis_states"]}
        self.assertIn("ACTIVE_THESIS", statuses)
        self.assertIn("SOURCE_PENDING", statuses)
        self.assertIn("NO_KNOWN_THESIS", statuses)


if __name__ == "__main__":
    unittest.main()
