import unittest

from e2r.production.cutover_shadow import ProductionCutoverConfig, build_production_cutover_bundle


class CutoverStaticLogicAuditTests(unittest.TestCase):
    def test_static_critical_counts_are_zero_without_ready_overclaim(self):
        bundle = build_production_cutover_bundle(
            config=ProductionCutoverConfig(as_of_date="2026-06-30"),
            repo_root=".",
            command="unit-test",
        )
        summary = bundle["static_logic_audit"]["summary"]
        self.assertEqual(summary["snapshot_only_counted_as_live_count"], 0)
        self.assertEqual(summary["production_ready_with_blockers_count"], 0)
        self.assertEqual(summary["critical_count_sum"], 0)


if __name__ == "__main__":
    unittest.main()
