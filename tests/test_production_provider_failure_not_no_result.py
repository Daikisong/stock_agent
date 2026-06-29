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
        self.assertTrue(all(result.status == "PROVIDER_FAILED" for result in results))


if __name__ == "__main__":
    unittest.main()
