import unittest
from datetime import date

from e2r.production.source_connectors.trusted_news_connector import TrustedNewsLiveConnector


class CutoverV3ProviderFailedNotNoResultTests(unittest.TestCase):
    def test_unconfigured_optional_provider_is_failed_not_no_result_in_live_mode(self):
        result = TrustedNewsLiveConnector(repo_root=".").fetch(
            symbol="005930",
            company_name="삼성전자",
            as_of_date=date(2026, 6, 30),
            mode="live",
        )
        self.assertEqual(result.status, "PROVIDER_FAILED")
        self.assertTrue(result.provider_request_id)


if __name__ == "__main__":
    unittest.main()
