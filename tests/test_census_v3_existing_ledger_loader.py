import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3ExistingLedgerLoaderTests(unittest.TestCase):
    def test_existing_ledger_claims_loaded_from_leaf_artifacts(self):
        self.assertGreater(len(census_v3_artifacts()["accepted_claims"]), 0)
        self.assertEqual(census_v3_artifacts()["leaf_audit"]["metrics"]["accepted_claim_count"], len(census_v3_artifacts()["accepted_claims"]))


if __name__ == "__main__":
    unittest.main()
