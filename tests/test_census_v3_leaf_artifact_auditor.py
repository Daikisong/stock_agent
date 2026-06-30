import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3LeafArtifactAuditorTests(unittest.TestCase):
    def test_leaf_auditor_recomputes_full_universe_counts(self):
        audit = census_v3_artifacts()["leaf_audit"]
        self.assertEqual(audit["verdict"], "PASS")
        self.assertEqual(audit["critical_count"], 0)
        self.assertGreater(audit["metrics"]["eligible_symbol_count"], 1000)
        self.assertEqual(audit["metrics"]["stage_status_count"], audit["metrics"]["eligible_symbol_count"])


if __name__ == "__main__":
    unittest.main()
