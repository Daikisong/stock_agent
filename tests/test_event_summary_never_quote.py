import unittest

from e2r.production.cutover_shadow import ProductionCutoverConfig, build_production_cutover_bundle


class EventSummaryNeverQuoteTests(unittest.TestCase):
    def test_cutover_extraction_audit_keeps_event_summary_quote_count_zero(self):
        bundle = build_production_cutover_bundle(
            config=ProductionCutoverConfig(as_of_date="2026-06-30"),
            repo_root=".",
            command="unit-test",
        )
        self.assertEqual(
            bundle["claim_extraction_audit"]["summary"]["event_summary_used_as_exact_quote_count"],
            0,
        )


if __name__ == "__main__":
    unittest.main()
