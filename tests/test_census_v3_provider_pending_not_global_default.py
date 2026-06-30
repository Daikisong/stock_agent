import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3ProviderPendingNotGlobalDefaultTests(unittest.TestCase):
    def test_provider_pending_is_not_global_default(self):
        metrics = census_v3_artifacts()["leaf_audit"]["metrics"]
        self.assertLess(metrics["provider_pending_count"], metrics["eligible_symbol_count"] * 0.30)


if __name__ == "__main__":
    unittest.main()
