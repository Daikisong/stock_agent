import unittest

from census_v2_test_helpers import census_v2_artifacts


class CensusV2ExistingClaimLedgerReuseTests(unittest.TestCase):
    def test_existing_claim_ledger_reused_only_for_universe_symbols(self):
        artifacts = census_v2_artifacts()
        eligible_symbols = {row["symbol"] for row in artifacts["universe"] if row.get("eligible_for_census")}
        claim_symbols = {row["symbol"] for row in artifacts["accepted_claims"]}
        self.assertGreater(len(claim_symbols), 0)
        self.assertTrue(claim_symbols <= eligible_symbols)

    def test_claim_rows_are_not_source_proxy(self):
        for row in census_v2_artifacts()["accepted_claims"]:
            self.assertFalse(row["source_proxy_only"])
            self.assertFalse(row["evidence_url_pending"])
            self.assertTrue(row["score_evidence_eligible"])


if __name__ == "__main__":
    unittest.main()
