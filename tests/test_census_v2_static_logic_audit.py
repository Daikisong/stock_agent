import unittest

from census_v2_test_helpers import census_v2_artifacts


class CensusV2StaticLogicAuditTests(unittest.TestCase):
    def test_static_audit_has_zero_critical_counts(self):
        audit = census_v2_artifacts()["audit"]
        self.assertEqual(audit["summary"]["critical_count_sum"], 0)
        self.assertEqual(audit["summary"]["status"], "CENSUS_V2_ACCEPTANCE_PASS")


if __name__ == "__main__":
    unittest.main()
