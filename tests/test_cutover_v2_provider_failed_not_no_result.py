import unittest
from datetime import date

from e2r.production.source_connectors.companyguide_live_connector import CompanyGuideLiveConnector


class CutoverV2ProviderFailedNotNoResultTests(unittest.TestCase):
    def test_unimplemented_live_provider_returns_provider_failed(self):
        result = CompanyGuideLiveConnector(repo_root=".").fetch(
            symbol="005930",
            company_name="삼성전자",
            as_of_date=date(2026, 6, 30),
            mode="live",
        )
        self.assertEqual(result.status, "PROVIDER_FAILED")
        self.assertIn("NOT_READY", result.provider_error)


if __name__ == "__main__":
    unittest.main()
