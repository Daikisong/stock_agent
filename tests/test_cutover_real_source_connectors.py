import unittest
from datetime import date

from e2r.production.source_connectors import build_default_source_provider_registry
from e2r.production.cutover_shadow import ProductionCutoverConfig, build_production_cutover_bundle


class CutoverRealSourceConnectorsTests(unittest.TestCase):
    def test_live_mode_provider_failure_is_not_counted_as_live_fetch(self):
        registry = build_default_source_provider_registry(".")
        results = registry.fetch_all(
            symbol="005930",
            company_name="삼성전자",
            as_of_date=date(2026, 6, 30),
            mode="live",
        )
        report = registry.build_report(results)
        self.assertGreaterEqual(report["summary"]["provider_failure_count"], 1)
        self.assertEqual(report["summary"]["real_document_fetched_count"], 0)

    def test_shadow_report_exercises_official_provider_classes(self):
        bundle = build_production_cutover_bundle(
            config=ProductionCutoverConfig(as_of_date="2026-06-30"),
            repo_root=".",
            command="unit-test",
        )
        summary = bundle["source_connector_report"]["summary"]
        self.assertGreaterEqual(summary["dart_call_count"], 1)
        self.assertGreaterEqual(summary["kind_call_count"], 1)
        self.assertGreaterEqual(summary["krx_call_count"], 1)
        self.assertGreaterEqual(summary["companyguide_call_count"], 1)
        self.assertGreaterEqual(summary["issuer_ir_call_count"], 1)
        self.assertGreaterEqual(summary["trusted_news_call_count"], 1)
        self.assertGreaterEqual(summary["real_source_document_fetched_count"], 50)
        self.assertEqual(summary["snapshot_only_counted_as_live_count"], 0)


if __name__ == "__main__":
    unittest.main()
