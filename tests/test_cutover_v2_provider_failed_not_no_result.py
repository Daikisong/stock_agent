import unittest
from datetime import date

from e2r.production.source_connectors.companyguide_live_connector import CompanyGuideLiveConnector


class CutoverV2ProviderFailedNotNoResultTests(unittest.TestCase):
    def test_companyguide_live_provider_fetches_or_explicitly_fails(self):
        result = CompanyGuideLiveConnector(repo_root=".").fetch(
            symbol="005930",
            company_name="삼성전자",
            as_of_date=date(2026, 6, 30),
            mode="live",
        )
        self.assertIn(result.status, {"FETCHED", "PROVIDER_FAILED"})
        self.assertNotEqual(result.status, "NO_RESULT")
        if result.status == "FETCHED":
            self.assertTrue(result.provider_request_id)
            self.assertTrue(result.content_hash)
            self.assertTrue(result.canonical_url)
        else:
            self.assertTrue(result.provider_error)


if __name__ == "__main__":
    unittest.main()
