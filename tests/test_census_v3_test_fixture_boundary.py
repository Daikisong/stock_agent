import unittest

from census_v3_test_helpers import _test_leaf_bundle
from e2r.census.census_runner_v3 import CensusV3RunConfig
from e2r.census.census_runner_v4 import CensusV4RunConfig
from tests.census_v4_test_helpers import census_v4_test_support_kwargs


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

        v4_support = census_v4_test_support_kwargs()
        unsafe_v4_support = {key: value for key, value in v4_support.items() if key != "test_mode"}
        with self.assertRaisesRegex(ValueError, "test_mode=True"):
            CensusV4RunConfig(as_of_date="2026-07-01", **unsafe_v4_support)

        v4_serialized = CensusV4RunConfig(as_of_date="2026-07-01", **v4_support).to_dict()
        self.assertTrue(v4_serialized["test_mode"])
        self.assertTrue(v4_serialized["test_replay_acceptance_paths_injected"])
        self.assertNotIn("test_all_archetype_replay_acceptance_path", v4_serialized)


if __name__ == "__main__":
    unittest.main()
