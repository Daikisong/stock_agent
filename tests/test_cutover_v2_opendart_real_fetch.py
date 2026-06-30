import unittest
from datetime import date

from e2r.production.source_connectors.opendart_live_connector import OpenDARTLiveConnector


class CutoverV2OpenDARTRealFetchTests(unittest.TestCase):
    def test_opendart_live_fetch_or_explicit_auth_failure(self):
        result = OpenDARTLiveConnector(repo_root=".").fetch(
            symbol="005930",
            company_name="삼성전자",
            as_of_date=date(2026, 6, 30),
            mode="live",
        )
        self.assertIn(result.status, {"FETCHED", "AUTH_FAILED", "PROVIDER_FAILED", "NO_RESULT"})
        if result.status == "FETCHED":
            self.assertEqual(result.mode, "live")
            self.assertTrue(result.content_hash)
            self.assertTrue(result.canonical_url or result.official_document_id)
            self.assertTrue(result.provider_request_id)
        else:
            self.assertTrue(result.provider_error)


if __name__ == "__main__":
    unittest.main()
