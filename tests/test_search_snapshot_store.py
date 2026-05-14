from datetime import date, datetime
import tempfile
import unittest

from e2r.research.report_snapshot_store import ReportSnapshotStore
from e2r.research.search_provider import SearchResult
from e2r.research.search_snapshot_store import SearchSnapshotStore, snapshot_from_search_result


class SearchSnapshotStoreTests(unittest.TestCase):
    def test_search_snapshot_store_filters_point_in_time(self):
        with tempfile.TemporaryDirectory() as root:
            store = SearchSnapshotStore(root)
            old = snapshot_from_search_result(
                SearchResult(title="HD현대일렉트릭 수주잔고", url="https://example.com/a", query="q"),
                query="q",
                search_date=date(2023, 7, 27),
                evidence_ids=("ev1",),
                symbol="267260",
                company_name="HD현대일렉트릭",
            )
            future = snapshot_from_search_result(
                SearchResult(title="미래 리포트", url="https://example.com/b", query="q"),
                query="q",
                search_date=date(2023, 8, 1),
            )
            store.save_snapshot((old, future))

            visible = store.load_snapshots(as_of_date=date(2023, 7, 27), query="q", symbol="267260")
            results = store.search_results(query="HD현대일렉트릭 Review PDF", as_of_date=date(2023, 7, 27))

        self.assertEqual(len(visible), 1)
        self.assertEqual(visible[0].title, "HD현대일렉트릭 수주잔고")
        self.assertIn("ev1", visible[0].evidence_ids)
        self.assertEqual(results[0].url, "https://example.com/a")

    def test_report_snapshot_store_writes_hash_and_filters_symbol(self):
        with tempfile.TemporaryDirectory() as root:
            store = ReportSnapshotStore(root)
            snapshot = store.save_text_snapshot(
                url="https://example.com/report.pdf",
                title="줄을 서시오",
                text="수주잔고와 OPM 개선",
                fetched_at=datetime(2023, 7, 27, 9, 0),
                as_of_date=date(2023, 7, 27),
                symbol="267260",
                company_name="HD현대일렉트릭",
                evidence_ids=("ev-report",),
            )
            loaded = store.load(as_of_date=date(2023, 7, 27), symbol="267260")
            fixture_text = store.fixture_text_by_url(as_of_date=date(2023, 7, 27), symbol="267260")

        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].extracted_text_hash, snapshot.extracted_text_hash)
        self.assertIn("ev-report", loaded[0].evidence_ids)
        self.assertIn("https://example.com/report.pdf", fixture_text)


if __name__ == "__main__":
    unittest.main()
