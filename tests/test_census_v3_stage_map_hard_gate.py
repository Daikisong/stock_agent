import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3StageMapHardGateTests(unittest.TestCase):
    def test_hard_gate_passes(self):
        audit = census_v3_artifacts()["leaf_audit"]
        self.assertEqual(audit["verdict"], "PASS")
        self.assertEqual(audit["critical_count"], 0)


if __name__ == "__main__":
    unittest.main()
