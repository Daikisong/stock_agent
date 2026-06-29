import unittest
from datetime import date

from e2r.production.source_connectors import build_default_source_provider_registry


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


if __name__ == "__main__":
    unittest.main()
