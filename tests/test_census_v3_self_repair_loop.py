import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3SelfRepairLoopTests(unittest.TestCase):
    def test_self_repair_records_resolved_failures(self):
        log = census_v3_artifacts()["self_repair"]
        self.assertEqual(log["final_status"], "PASS")
        self.assertGreaterEqual(len(log["iterations"][0]["resolved_failures"]), 1)


if __name__ == "__main__":
    unittest.main()
