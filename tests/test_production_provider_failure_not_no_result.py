import unittest
from datetime import date

from e2r.production.source_connectors import build_default_source_provider_registry


class ProductionProviderFailureNotNoResultTests(unittest.TestCase):
    def test_live_unconfigured_provider_is_provider_failed(self):
        results = build_default_source_provider_registry(".").fetch_all(
            symbol="005930",
            company_name="삼성전자",
            as_of_date=date(2026, 6, 30),
            mode="live",
        )
        self.assertTrue(results)
        self.assertFalse(any(result.status == "NO_RESULT" for result in results))
        for result in results:
            if result.provider_name in {"OpenDART", "KIND", "KRX", "CompanyGuide"}:
                self.assertIn(result.status, {"FETCHED", "AUTH_FAILED", "PROVIDER_FAILED"})
                if result.status == "FETCHED":
                    self.assertTrue(result.counts_as_live)
                continue
            self.assertEqual(result.status, "PROVIDER_FAILED")


if __name__ == "__main__":
    unittest.main()
