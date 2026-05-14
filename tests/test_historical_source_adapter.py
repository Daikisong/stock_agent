from datetime import date, datetime
from pathlib import Path
import tempfile
import unittest

from e2r.backtest.historical_source_adapter import HistoricalPointInTimeSourceAdapter
from e2r.models import Market
from e2r.research.report_snapshot_store import ReportSnapshotStore
from e2r.research.search_provider import SearchResult
from e2r.research.search_snapshot_store import SearchSnapshotStore, snapshot_from_search_result


class HistoricalSourceAdapterTests(unittest.TestCase):
    def test_adapter_filters_snapshots_point_in_time(self):
        with tempfile.TemporaryDirectory() as root:
            root_path = Path(root)
            search_store = SearchSnapshotStore(root_path / "search")
            report_store = ReportSnapshotStore(root_path / "reports")
            search_store.save_snapshot(
                snapshot_from_search_result(
                    SearchResult(title="HD현대일렉트릭 Review PDF", url="https://example.com/hd.pdf", confidence=0.9),
                    query="HD현대일렉트릭 Review PDF",
                    search_date=date(2023, 7, 27),
                    symbol="267260",
                    company_name="HD현대일렉트릭",
                )
            )
            report_store.save_text_snapshot(
                url="https://example.com/hd.pdf",
                title="HD현대일렉트릭 Review PDF",
                text="수주잔고 OPM 목표주가 상향",
                fetched_at=datetime(2023, 7, 27, 9, 0),
                as_of_date=date(2023, 7, 27),
                symbol="267260",
                company_name="HD현대일렉트릭",
            )

            adapter = HistoricalPointInTimeSourceAdapter(
                search_snapshot_root=root_path / "search",
                report_snapshot_root=root_path / "reports",
            )
            before = adapter.build(as_of_date=date(2023, 7, 1), market=Market.KR)
            after = adapter.build(as_of_date=date(2023, 8, 1), market=Market.KR)

        self.assertFalse(before.coverage.search_snapshot_available)
        self.assertTrue(after.coverage.search_snapshot_available)
        self.assertEqual(after.sources.list_instruments(Market.KR, date(2023, 8, 1))[0].symbol, "267260")
        self.assertIn("https://example.com/hd.pdf", after.fixture_text_by_url)

    def test_snapshot_provider_does_not_return_future_results(self):
        with tempfile.TemporaryDirectory() as root:
            store = SearchSnapshotStore(root)
            store.save_snapshot(
                snapshot_from_search_result(
                    SearchResult(title="미래 리포트", url="https://example.com/future.pdf", confidence=0.9),
                    query="미래 리포트",
                    search_date=date(2024, 1, 1),
                    symbol="000000",
                    company_name="미래회사",
                )
            )
            adapter = HistoricalPointInTimeSourceAdapter(search_snapshot_root=root, report_snapshot_root=root)
            bundle = adapter.build(as_of_date=date(2023, 12, 31), market=Market.KR)

        self.assertEqual(bundle.search_provider.search("미래회사 Review PDF", date(2023, 12, 31)), ())
        self.assertIn("search_snapshot_unavailable", bundle.coverage.limitations())


if __name__ == "__main__":
    unittest.main()
