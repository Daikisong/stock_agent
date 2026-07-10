import unittest

from census_v3_test_helpers import _test_leaf_bundle
from e2r.census.census_runner_v3 import CensusV3RunConfig


class CensusV3TestFixtureBoundaryTests(unittest.TestCase):
    def test_leaf_bundle_injection_is_explicitly_test_only(self):
        bundle = _test_leaf_bundle()

        with self.assertRaisesRegex(ValueError, "test_mode=True"):
            CensusV3RunConfig(as_of_date="2026-07-01", test_leaf_bundle=bundle)

        config = CensusV3RunConfig(
            as_of_date="2026-07-01",
            test_mode=True,
            test_leaf_bundle=bundle,
        )
        serialized = config.to_dict()
        self.assertTrue(serialized["test_mode"])
        self.assertTrue(serialized["test_leaf_bundle_injected"])
        self.assertNotIn("test_leaf_bundle", serialized)


if __name__ == "__main__":
    unittest.main()
