from datetime import date, datetime
from pathlib import Path
import tempfile
import unittest

from e2r.cheap_scan.models import CheapScanCandidate, RecommendedNextLayer
from e2r.llm import FakeThemeRouteProvider, ThemeRouteOutput
from e2r.models import Market, Stage
from e2r.research.asof_web_research import AsOfWebResearchConfig, AsOfWebResearchRunner
from e2r.research.search_provider import SearchResult


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
