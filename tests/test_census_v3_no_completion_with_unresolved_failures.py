import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3NoCompletionWithUnresolvedFailuresTests(unittest.TestCase):
    def test_unresolved_failures_empty_for_pass(self):
        self.assertEqual(census_v3_artifacts()["self_repair"]["iterations"][0]["unresolved_failures"], [])


if __name__ == "__main__":
    unittest.main()
