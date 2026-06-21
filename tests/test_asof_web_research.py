from datetime import date, datetime
from pathlib import Path
import tempfile
import unittest

from e2r.cheap_scan.models import CheapScanCandidate, RecommendedNextLayer
from e2r.features import FeatureEngineeringInput
from e2r.llm import FakeThemeRouteProvider, ThemeRouteOutput
from e2r.models import Market, Stage
from e2r.research.asof_web_research import (
    AsOfWebResearchConfig,
    AsOfWebResearchRunner,
    RetrospectiveSnapshotSearchProvider,
    fixture_text_by_url_for_candidate,
)
from e2r.research.report_snapshot_store import ReportSnapshotStore
from e2r.research.search_provider import SearchResult
from e2r.research.search_snapshot_store import SearchSnapshot, SearchSnapshotStore


class _Provider:
    def __init__(self, results):
        self.results = tuple(results)

    def search(self, query, as_of_date, max_results=10):
        return self.results[:max_results]


class _QueryOnlyProvider:
    def __init__(self, query: str, result: SearchResult) -> None:
        self.query = query
        self.result = result
        self.queries: list[str] = []

    def search(self, query, as_of_date, max_results=10):
        self.queries.append(query)
        if query == self.query:
            return (self.result,)
        return ()


class _DefaultThenQueryProvider:
    def __init__(self, default_result: SearchResult, query: str, query_result: SearchResult) -> None:
        self.default_result = default_result
        self.query = query
        self.query_result = query_result
        self.queries: list[str] = []

    def search(self, query, as_of_date, max_results=10):
        self.queries.append(query)
        if query == self.query:
            return (self.query_result,)
        return (self.default_result,)


class AsOfWebResearchTests(unittest.TestCase):
    def test_snapshot_provider_and_fixture_text_include_symbol_only_matches(self):
        with tempfile.TemporaryDirectory() as root:
            root_path = Path(root)
            search_store = SearchSnapshotStore(root_path / "search")
            report_store = ReportSnapshotStore(root_path / "reports")
            url = "https://example.com/hynix-guard"
            report_store.save_text_snapshot(
                url=url,
                title="C06 guard",
                text="SK하이닉스 guard source",
                fetched_at=datetime(2024, 7, 11, 8),
                as_of_date=date(2024, 7, 11),
                symbol="000660",
                company_name="000660",
                source_type="broker_report",
            )
            search_store.save_snapshot(
                SearchSnapshot(
                    query="000660 C06 guard",
                    search_date=date(2024, 7, 11),
                    title="C06 guard",
                    url=url,
                    snippet="000660 C06 guard",
                    published_at=datetime(2024, 7, 11, 8),
                    fetched_at=datetime(2024, 7, 11, 8),
                    source_type="broker_report",
                    extracted_text_hash="hash",
                    evidence_ids=(),
                    symbol="000660",
                    company_name="000660",
                )
            )

            provider = RetrospectiveSnapshotSearchProvider(
                store=search_store,
                symbol="000660",
                company_name="SK하이닉스",
            )
            results = provider.search("SK하이닉스 C06 guard", date(2024, 7, 11), max_results=10)
            fixture_text = fixture_text_by_url_for_candidate(
                store=report_store,
                symbol="000660",
                company_name="SK하이닉스",
            )

        self.assertEqual(tuple(item.url for item in results), (url,))
        self.assertIn(url, fixture_text)

    def test_snapshot_provider_falls_back_to_latest_symbol_snapshot_for_generic_query(self):
        with tempfile.TemporaryDirectory() as root:
            store = SearchSnapshotStore(Path(root) / "search")
            older_url = "https://example.com/c23-green"
            latest_url = "https://example.com/r13-guard"
            store.save_snapshot(
                SearchSnapshot(
                    query="유한양행 000100 C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION approval_to_revenue_bridge",
                    search_date=date(2024, 8, 20),
                    title="C23 green fixture",
                    url=older_url,
                    snippet="유한양행 C23 green fixture approval_to_revenue_bridge",
                    published_at=datetime(2024, 8, 20, 8),
                    fetched_at=datetime(2024, 8, 20, 8),
                    source_type="broker_report",
                    extracted_text_hash="older",
                    evidence_ids=(),
                    symbol="000100",
                    company_name="유한양행",
                )
            )
            store.save_snapshot(
                SearchSnapshot(
                    query="유한양행 000100 R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW missing_cashflow_bridge",
                    search_date=date(2024, 8, 30),
                    title="R13 guard fixture",
                    url=latest_url,
                    snippet="유한양행 R13 guard fixture missing_cashflow_bridge",
                    published_at=datetime(2024, 8, 30, 8),
                    fetched_at=datetime(2024, 8, 30, 8),
                    source_type="broker_report",
                    extracted_text_hash="latest",
                    evidence_ids=(),
                    symbol="000100",
                    company_name="유한양행",
                )
            )

            provider = RetrospectiveSnapshotSearchProvider(
                store=store,
                symbol="000100",
                company_name="유한양행",
            )
            generic = provider.search("유한양행 ASP 상승", date(2024, 8, 30), max_results=10)
            explicit = provider.search("유한양행 C23 approval_to_revenue_bridge", date(2024, 8, 30), max_results=10)

        self.assertEqual(tuple(item.url for item in generic), (latest_url,))
        self.assertEqual(tuple(item.url for item in explicit), (older_url,))

    def test_future_published_result_is_rejected(self):
        with tempfile.TemporaryDirectory() as root:
            text_path = Path(root) / "report.txt"
            text_path.write_text(_strong_report_text(), encoding="utf-8")
            candidate = _candidate()
            result = AsOfWebResearchRunner().run(
                candidate=candidate,
                search_provider=_Provider(
                    [
                        SearchResult(
                            title="테스트 미래 리포트 PDF",
                            url="https://example.com/future.pdf",
                            published_at=datetime(2023, 8, 2, 8, 0),
                            is_pdf=True,
                            is_report_domain=True,
                            confidence=0.9,
                        )
                    ]
                ),
                fixture_text_by_url={"https://example.com/future.pdf": text_path},
                config=AsOfWebResearchConfig(as_of_date=date(2023, 8, 1)),
            )

        self.assertGreater(result.rejected_future_count, 8)
        self.assertEqual(result.rejected_future_count, result.pipeline_result.budget_tracker.total_queries_used)
        self.assertFalse(result.pipeline_result.web_result.evidence)

    def test_undated_document_cannot_create_green_alone(self):
        with tempfile.TemporaryDirectory() as root:
            text_path = Path(root) / "report.txt"
            text_path.write_text(_strong_report_text(), encoding="utf-8")
            candidate = _candidate()
            result = AsOfWebResearchRunner().run(
                candidate=candidate,
                search_provider=_Provider(
                    [
                        SearchResult(
                            title="테스트 수주잔고 OPM Review PDF",
                            url="https://example.com/report.pdf",
                            published_at=None,
                            is_pdf=True,
                            is_report_domain=True,
                            confidence=0.95,
                        )
                    ]
                ),
                fixture_text_by_url={"https://example.com/report.pdf": text_path},
                config=AsOfWebResearchConfig(as_of_date=date(2023, 8, 1)),
            )

        self.assertGreater(result.date_unverified_count, 0)
        self.assertNotEqual(result.pipeline_result.stage.stage, Stage.STAGE_3_GREEN)

    def test_reconstructed_snapshot_metadata_marks_not_strict_pit(self):
        with tempfile.TemporaryDirectory() as root:
            text_path = Path(root) / "report.txt"
            text_path.write_text(_strong_report_text(), encoding="utf-8")
            candidate = _candidate()
            result = AsOfWebResearchRunner().run(
                candidate=candidate,
                search_provider=_Provider(
                    [
                        SearchResult(
                            title="테스트 수주잔고 OPM Review PDF",
                            url="https://example.com/report.pdf",
                            published_at=datetime(2023, 7, 27, 8, 0),
                            query="테스트 수주잔고 OPM 수출 비중 PDF",
                            is_pdf=True,
                            is_report_domain=True,
                            confidence=0.95,
                        )
                    ]
                ),
                fixture_text_by_url={"https://example.com/report.pdf": text_path},
                config=AsOfWebResearchConfig(
                    as_of_date=date(2023, 8, 1),
                    save_reconstructed_snapshots=True,
                    reconstructed_snapshot_root=Path(root) / "snapshots",
                ),
            )
            content = result.reconstructed_snapshot_paths[0].read_text(encoding="utf-8")

        self.assertTrue(result.reconstructed_snapshot_paths)
        self.assertIn('"point_in_time_status": "retrospective_reconstructed"', content)
        self.assertIn('"strict_pit_proof": false', content)

    def test_score_gap_expansion_uses_llm_query_under_asof_filter(self):
        query = "테스트 2023 2Q EPS OP FCF 목표주가 상향 리포트"
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(
                    status="needs_more_evidence",
                    missing_information=("revision estimate consensus target price EPS OP FCF",),
                    suggested_queries=(query,),
                ),
            ]
        )
        with tempfile.TemporaryDirectory() as root:
            text_path = Path(root) / "report.txt"
            text_path.write_text(_strong_report_text(), encoding="utf-8")
            provider = _QueryOnlyProvider(
                query,
                SearchResult(
                    title="테스트 2Q 추정치 상향 리포트",
                    url="https://example.com/asof-gap-report.pdf",
                    published_at=datetime(2023, 7, 27, 8, 0),
                    query=query,
                    is_pdf=True,
                    is_report_domain=True,
                    confidence=0.95,
                ),
            )

            result = AsOfWebResearchRunner().run(
                candidate=_candidate(),
                search_provider=provider,
                fixture_text_by_url={"https://example.com/asof-gap-report.pdf": text_path},
                config=AsOfWebResearchConfig(
                    as_of_date=date(2023, 8, 1),
                    theme_route_provider=route_provider,
                    max_theme_expansion_rounds=0,
                ),
            )

        self.assertIn(query, provider.queries)
        self.assertIn(query, result.pipeline_result.expansion_queries_run)
        self.assertTrue(any("revision" in item for item in route_provider.calls[1].score_gap_context))
        self.assertGreaterEqual(result.pipeline_result.score.diagnostic_scores["revision_score"], 80.0)
        self.assertGreater(result.date_verified_count, 0)

    def test_base_feature_input_feeds_asof_web_research_context(self):
        with tempfile.TemporaryDirectory() as root:
            text_path = Path(root) / "report.txt"
            text_path.write_text(_strong_report_text(), encoding="utf-8")
            candidate = _candidate()
            base_feature_input = FeatureEngineeringInput(
                symbol=candidate.symbol,
                as_of_date=candidate.as_of_date,
                company_name=candidate.company_name,
                sector_context="전기장비",
                agent_extracted_fields={"official_bridge_already_seen": True},
            )

            result = AsOfWebResearchRunner().run(
                candidate=candidate,
                search_provider=_Provider(
                    [
                        SearchResult(
                            title="테스트 수주잔고 OPM Review PDF",
                            url="https://example.com/report.pdf",
                            published_at=datetime(2023, 7, 27, 8, 0),
                            is_pdf=True,
                            is_report_domain=True,
                            confidence=0.95,
                        )
                    ]
                ),
                fixture_text_by_url={"https://example.com/report.pdf": text_path},
                config=AsOfWebResearchConfig(as_of_date=date(2023, 8, 1)),
                base_feature_input=base_feature_input,
            )

        self.assertEqual(result.pipeline_result.feature_input.sector_context, "전기장비")
        self.assertTrue(result.pipeline_result.feature_input.agent_extracted_fields["official_bridge_already_seen"])

    def test_date_unverified_report_triggers_llm_expansion_for_verified_source(self):
        query = "테스트 날짜확인 2023 2Q EPS OP FCF 목표주가 리포트"
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(
                    status="needs_more_evidence",
                    missing_information=("date-unverified document evidence",),
                    suggested_queries=(query,),
                ),
            ]
        )
        with tempfile.TemporaryDirectory() as root:
            undated_path = Path(root) / "undated_report.txt"
            dated_path = Path(root) / "dated_report.txt"
            undated_path.write_text(_strong_report_text(), encoding="utf-8")
            dated_path.write_text(_strong_report_text(), encoding="utf-8")
            provider = _DefaultThenQueryProvider(
                SearchResult(
                    title="테스트 수주잔고 OPM Review PDF",
                    url="https://example.com/undated-report.pdf",
                    published_at=None,
                    is_pdf=True,
                    is_report_domain=True,
                    confidence=0.95,
                ),
                query,
                SearchResult(
                    title="테스트 날짜확인 2Q 추정치 상향 리포트",
                    url="https://example.com/dated-report.pdf",
                    published_at=datetime(2023, 7, 27, 8, 0),
                    query=query,
                    is_pdf=True,
                    is_report_domain=True,
                    confidence=0.95,
                ),
            )

            result = AsOfWebResearchRunner().run(
                candidate=_candidate(),
                search_provider=provider,
                fixture_text_by_url={
                    "https://example.com/undated-report.pdf": undated_path,
                    "https://example.com/dated-report.pdf": dated_path,
                },
                config=AsOfWebResearchConfig(
                    as_of_date=date(2023, 8, 1),
                    theme_route_provider=route_provider,
                    max_theme_expansion_rounds=0,
                ),
            )

        self.assertIn(query, provider.queries)
        self.assertIn(query, result.pipeline_result.expansion_queries_run)
        self.assertGreater(result.date_unverified_count, 0)
        self.assertGreater(result.date_verified_count, 0)
        self.assertTrue(
            any(
                "date-unverified document evidence" in context
                for call in route_provider.calls
                for context in call.score_gap_context
            )
        )


def _candidate():
    return CheapScanCandidate(
        symbol="123456",
        company_name="테스트",
        market=Market.KR,
        as_of_date=date(2023, 8, 1),
        reason_codes=("DISC_SUPPLY_CONTRACT",),
        disclosure_event_score=70.0,
        cheap_scan_total_score=31.5,
        recommended_next_layer=RecommendedNextLayer.EVENT_SEARCH,
    )


def _strong_report_text() -> str:
    return """
2023.07.27
현재주가: 10000
목표주가: 18000
목표주가 상향: 45%
FY1 매출액: 1000
FY1 영업이익: 200
FY1 EPS: 1200
FY2 매출액: 1600
FY2 영업이익: 420
FY2 EPS: 2600
PER: 6
PBR: 1.1
ROE: 20%
OPM: 20%
계약금액/매출: 30%
계약기간: 48개월
수주잔고/매출: 180%
CAPA 증가율: 25%
ASP 상승과 리드타임 장기화 구조적 공급부족 리레이팅
"""


if __name__ == "__main__":
    unittest.main()
