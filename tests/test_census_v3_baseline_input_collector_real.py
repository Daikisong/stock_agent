import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3BaselineInputCollectorRealTests(unittest.TestCase):
    def test_baseline_wires_at_least_five_source_families(self):
        metrics = census_v3_artifacts()["leaf_audit"]["metrics"]
        self.assertGreaterEqual(metrics["baseline_source_family_wired_count"], 5)
        self.assertIn("OpenDART", metrics["source_family_attempt_counts"])
        self.assertIn("ExistingEvidenceOSLedger", metrics["source_family_attempt_counts"])


if __name__ == "__main__":
    unittest.main()
