import unittest

from e2r.production.cutover_shadow import ProductionCutoverConfig, build_production_cutover_bundle
from tests.live_test_policy import requires_live_test


class ProductionCutoverFrozenRepeatabilityTests(unittest.TestCase):
    @requires_live_test
    def test_v4_frozen_repeat_variance_is_reported(self):
        bundle = build_production_cutover_bundle(
            config=ProductionCutoverConfig(as_of_date="2026-06-30"),
            repo_root=".",
            command="unit-test",
        )
        self.assertEqual(bundle["multiday_validation"]["summary"]["repeat_variance"], 0)


if __name__ == "__main__":
    unittest.main()
