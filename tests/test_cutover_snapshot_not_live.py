import unittest
from datetime import date

from e2r.production.source_connectors import build_default_source_provider_registry


class CutoverSnapshotNotLiveTests(unittest.TestCase):
    def test_snapshot_fetch_is_fetched_but_not_live(self):
        registry = build_default_source_provider_registry(".")
        results = registry.fetch_all(
            symbol="005930",
            company_name="삼성전자",
            as_of_date=date(2026, 6, 30),
            mode="snapshot",
        )
        fetched = [result for result in results if result.status == "FETCHED"]
        self.assertTrue(fetched)
        self.assertTrue(all(not result.counts_as_live for result in fetched))
        self.assertTrue(all(result.mode == "snapshot" for result in fetched))


if __name__ == "__main__":
    unittest.main()
