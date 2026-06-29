import unittest

from e2r.production.cutover_shadow import ProductionCutoverConfig, build_production_cutover_bundle


class CutoverResearchMemoryUsagePolicyTests(unittest.TestCase):
    def test_source_proxy_counts_do_not_score(self):
        bundle = build_production_cutover_bundle(
            config=ProductionCutoverConfig(as_of_date="2026-06-30"),
            repo_root=".",
            command="unit-test",
        )
        summary = bundle["research_memory_usage_audit"]["summary"]
        self.assertEqual(summary["source_proxy_to_score_count"], 0)
        self.assertEqual(summary["source_proxy_to_A2_count"], 0)


if __name__ == "__main__":
    unittest.main()
