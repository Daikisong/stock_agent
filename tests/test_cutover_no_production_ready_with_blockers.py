import unittest

from e2r.production.cutover_shadow import ProductionCutoverConfig, build_production_cutover_bundle


class CutoverNoProductionReadyWithBlockersTests(unittest.TestCase):
    def test_blockers_force_not_ready(self):
        bundle = build_production_cutover_bundle(
            config=ProductionCutoverConfig(as_of_date="2026-06-30"),
            repo_root=".",
            command="unit-test",
        )
        self.assertFalse(bundle["shadow_latest"]["production_ready"])
        self.assertEqual(bundle["shadow_latest"]["production_verdict"], "NOT_READY")
        self.assertTrue(bundle["shadow_latest"]["blockers"])


if __name__ == "__main__":
    unittest.main()
