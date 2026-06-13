from datetime import date, datetime
from email.message import Message
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from e2r.evidence_ids import stable_consensus_evidence_id, stable_news_evidence_id
from e2r.models import Market, ScoreSnapshot, Stage
from e2r.llm import EvidenceSlotStatus, FakeThemeRouteProvider, ThemeRouteOutput
from e2r.research import EmptySearchProvider
from e2r.research.browser_search_provider import BrowserSearchProvider
from e2r.research.free_web_research_runner import (
    FreeWebResearchInput,
    FreeWebResearchRunner,
    _ScoreGapExpansionResult,
    _FixedQueryPlanner,
    _material_score_gaps,
    _post_score_gap_expansion_allowed,
    _score_gap_reason_codes,
    _score_gap_score_block_reason,
    _score_gap_missing_information,
    _stage_gate_missing_information,
)
from e2r.research.manual_source_provider import ManualSource, ManualSourceProvider
from e2r.research.naver_search_provider import NaverFreeSearchProvider
from e2r.research.query_planner import QueryPlan, QuerySpec
from e2r.research.search_budget import SearchBudget
from e2r.research.search_provider import FixtureSearchProvider, SearchResult
from e2r.red_team import RedTeamAssessment


ROOT = Path(__file__).resolve().parents[1]
HTML_ROOT = ROOT / "data/raw/search_html"
TEXT_ROOT = HTML_ROOT / "text"

HD_REPORT_URL = "https://ssl.pstatic.net/imgstock/upload/research/company/hd_줄을서시오.pdf"
HYOSUNG_REPORT_URL = "https://hanaw.com/download/research/hyosung_low_margin_cleanup.pdf"
ILJIN_DISCLOSURE_URL = "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=202311270001"
ILJIN_REPORT_URL = "https://file.alphasquare.co.kr/media/pdfs/iljin_transformer_capa.pdf"
ZOOM_NEWS_URL = "https://news.example.com/zoom-pandemic-eps"
ZOOM_REPORT_URL = "https://file.alphasquare.co.kr/media/pdfs/zoom_q2_2020_review.pdf"
ZOOM_SEC_URL = "https://www.sec.gov/Archives/edgar/data/zoom/q2-2020-10q"
SMCI_GUIDANCE_URL = "https://reuters.example.com/smci-raised-guidance"
SMCI_ACCOUNTING_URL = "https://news.example.com/smci-accounting-issue"


class FreeWebResearchRunnerTests(unittest.TestCase):
    def test_score_gap_reason_code_marks_score_as_raw_reference(self):
        score = ScoreSnapshot(
            symbol="123456",
            as_of_date=date(2026, 6, 12),
            eps_fcf_explosion_score=20.0,
            earnings_visibility_score=15.0,
            bottleneck_pricing_score=15.0,
            market_mispricing_score=10.0,
            valuation_rerating_score=10.0,
            capital_allocation_score=4.0,
            information_confidence_score=4.0,
            risk_penalty=0.0,
            total_score=78.0,
        )

        codes = _score_gap_reason_codes(score, ("missing_revision_source",))

        self.assertIn("RAW_SCORE_TOTAL_BEFORE_GAP:78.0", codes)
        self.assertFalse(any(item.startswith("SCORE_TOTAL:") for item in codes))

    def test_free_web_research_defaults_evidence_review_on_for_gap_expansion(self):
        inputs = FreeWebResearchInput(
            company_name="테스트",
            symbol="123456",
            sector=None,
            market=Market.KR,
            as_of_date=date(2024, 1, 1),
            theme_route_provider=FakeThemeRouteProvider(),
        )

        self.assertTrue(inputs.theme_rebalance_enabled)
        self.assertTrue(inputs.theme_evidence_review_enabled)
        self.assertEqual(inputs.max_theme_expansion_rounds, 2)
        self.assertEqual(inputs.post_parse_gap_expansion_max_queries, 10)
        self.assertIsNone(inputs.llm_query_retry_max)
        self.assertIsNone(inputs.score_gap_query_retry_max)
        self.assertEqual(inputs.max_score_gap_expansion_rounds, 2)
        self.assertEqual(inputs.theme_route_search_result_limit, 80)
        self.assertEqual(inputs.theme_route_document_limit, 32)
        self.assertEqual(inputs.theme_route_document_excerpt_chars, 1200)
        self.assertTrue(inputs.require_valid_theme_route_for_scoring)
        self.assertTrue(inputs.require_resolved_score_gaps_for_scoring)

    def test_llm_route_input_is_compacted_with_query_coverage(self):
        as_of = date(2026, 6, 8)
        queries = tuple(
            QuerySpec(
                group="test",
                query=f"테스트압축 쿼리{i}",
                priority=i,
                company_name="테스트압축",
                symbol="123450",
                sector=None,
                market=Market.KR,
                as_of_date=as_of,
            )
            for i in range(3)
        )
        plan = QueryPlan(
            company_name="테스트압축",
            symbol="123450",
            sector=None,
            market=Market.KR,
            as_of_date=as_of,
            queries=queries,
        )
        results_by_query = {
            query.query: tuple(
                SearchResult(
                    title=f"테스트압축 {query.query} 리포트 {index}",
                    url=f"https://example.com/{query.priority}/{index}",
                    snippet="테스트압축 목표주가 상향 EPS 상향 HBM 수요",
                    source="fixture-research",
                    published_at=datetime(2026, 6, 8, 8),
                    query=query.query,
                    is_report_domain=True,
                    confidence=0.9,
                )
                for index in range(8)
            )
            for query in queries
        }
        route_provider = FakeThemeRouteProvider(output=ThemeRouteOutput(status="no_transition"))

        FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=FixtureSearchProvider(results_by_query=results_by_query),
            query_planner=_FixedQueryPlanner(plan),
        ).run(
            FreeWebResearchInput(
                company_name="테스트압축",
                symbol="123450",
                sector=None,
                market=Market.KR,
                as_of_date=as_of,
                top_results=3,
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                theme_evidence_review_enabled=False,
                theme_route_search_result_limit=5,
                require_valid_theme_route_for_scoring=False,
                require_resolved_score_gaps_for_scoring=False,
            )
        )

        self.assertEqual(len(route_provider.calls), 1)
        llm_results = route_provider.calls[0].search_results
        self.assertEqual(len(llm_results), 5)
        self.assertEqual({item.query for item in llm_results}, {query.query for query in queries})

    def test_score_gap_expansion_stops_at_round_limit_with_warning_after_search(self):
        as_of = date(2026, 6, 8)
        query = QuerySpec(
            group="test",
            query="테스트라운드 최초",
            priority=1,
            company_name="테스트라운드",
            symbol="123451",
            sector=None,
            market=Market.KR,
            as_of_date=as_of,
        )
        plan = QueryPlan(
            company_name="테스트라운드",
            symbol="123451",
            sector=None,
            market=Market.KR,
            as_of_date=as_of,
            queries=(query,),
        )
        gap_query = "테스트라운드 EPS FCF 컨센서스 상향 리포트"
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(status="needs_more_evidence", suggested_queries=(gap_query,)),
            ]
        )
        phase_events: list[dict] = []

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=FixtureSearchProvider(results_by_query={gap_query: ()}),
            query_planner=_FixedQueryPlanner(plan),
        ).run(
            FreeWebResearchInput(
                company_name="테스트라운드",
                symbol="123451",
                sector=None,
                market=Market.KR,
                as_of_date=as_of,
                top_results=3,
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
                max_score_gap_expansion_rounds=1,
                require_valid_theme_route_for_scoring=True,
                require_resolved_score_gaps_for_scoring=True,
                phase_event_sink=phase_events.append,
            )
        )

        self.assertEqual(result.stage.stage, Stage.STAGE_0)
        self.assertTrue(result.theme_route_diagnostics["score_valid"])
        self.assertNotIn("score_blocked_reason", result.theme_route_diagnostics)
        self.assertEqual(result.score.diagnostic_scores["score_valid"], 100.0)
        self.assertEqual(result.score.diagnostic_scores["score_blocked_by_score_gap"], 0.0)
        self.assertEqual(result.score.diagnostic_scores["score_gap_unresolved_warning"], 100.0)
        self.assertEqual(result.theme_route_diagnostics["post_score_gap_warning_reason"], "score_gap_round_limit")
        self.assertEqual(result.theme_route_diagnostics["post_score_gap_expansion_status"], "round_limit_reached")
        self.assertEqual(result.theme_route_diagnostics["post_score_gap_expansion_count"], 1)
        self.assertTrue(any(event["phase"] == "post_score_gap_stop_round_limit" for event in phase_events))

    def test_provider_error_theme_route_blocks_score_and_stage(self):
        route_provider = FakeThemeRouteProvider(
            output=ThemeRouteOutput(
                status="provider_error",
                blocked_reason="codex cli returned no valid route json",
            )
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=EmptySearchProvider(),
        ).run(
            FreeWebResearchInput(
                company_name="테스트",
                symbol="123456",
                sector=None,
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                theme_evidence_review_enabled=False,
            )
        )

        self.assertEqual(result.stage.stage, Stage.STAGE_0)
        self.assertEqual(result.score.total_score, 0.0)
        self.assertFalse(result.theme_route_diagnostics["score_valid"])
        self.assertEqual(result.theme_route_diagnostics["score_blocked_reason"], "theme_route_provider_error")
        self.assertEqual(result.score.diagnostic_scores["score_valid"], 0.0)
        self.assertEqual(result.score.diagnostic_scores["score_blocked_by_theme_route"], 100.0)
        self.assertIn("raw_score_total_before_theme_route_block", result.score.diagnostic_scores)

    def test_uncapped_llm_retry_stops_on_repeated_non_executable_queries(self):
        route_provider = FakeThemeRouteProvider(
            output=ThemeRouteOutput(
                status="needs_more_evidence",
                suggested_queries=("테스트 2027 미래 실적 리포트",),
            )
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=EmptySearchProvider(),
        ).run(
            FreeWebResearchInput(
                company_name="테스트",
                symbol="123456",
                sector=None,
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                theme_evidence_review_enabled=False,
            )
        )

        self.assertGreaterEqual(len(route_provider.calls), 2)
        self.assertTrue(any(item.reason == "future_query_rejected" for item in result.skipped_queries))
        self.assertEqual(result.expansion_queries_run, ())

    def test_llm_retry_can_be_capped_explicitly_for_fixtures(self):
        route_provider = FakeThemeRouteProvider(
            output=ThemeRouteOutput(
                status="needs_more_evidence",
                suggested_queries=("테스트 2027 미래 실적 리포트",),
            )
        )

        FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=EmptySearchProvider(),
        ).run(
            FreeWebResearchInput(
                company_name="테스트",
                symbol="123456",
                sector=None,
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                theme_evidence_review_enabled=False,
                llm_query_retry_max=0,
            )
        )

        self.assertEqual(len(route_provider.calls), 1)

    def test_browser_search_provider_parses_fixture_html(self):
        provider = BrowserSearchProvider(
            fixture_html_by_query={
                "HD현대일렉트릭 수주잔고 OPM 수출 비중 PDF": HTML_ROOT / "hd_hyundai_electric_report_search.html"
            }
        )

        results = provider.search("HD현대일렉트릭 수주잔고 OPM 수출 비중 PDF", date(2023, 7, 27), max_results=3)

        self.assertEqual(results[0].title, "HD현대일렉트릭 줄을 서시오")
        self.assertTrue(results[0].is_pdf)
        self.assertTrue(results[0].is_report_domain)
        self.assertEqual(provider.classify_result_type(results[0].url, results[0].title, results[0].snippet), "report")

    def test_hd_fixture_html_reaches_stage_3_green(self):
        result = _run_free(
            company_name="HD현대일렉트릭",
            symbol="267260",
            sector="power_equipment",
            market=Market.KR,
            as_of_date=date(2023, 7, 27),
            fixture_html={
                "HD현대일렉트릭 수주잔고 OPM 수출 비중 PDF": HTML_ROOT / "hd_hyundai_electric_report_search.html",
            },
            fixture_text={
                HD_REPORT_URL: TEXT_ROOT / "hd_hyundai_electric_report.txt",
            },
        )

        self.assertEqual(result.stage.stage, Stage.STAGE_3_GREEN)
        self.assertEqual(result.feature_result.shortage_type.value, "structural")
        self.assertTrue(any(item.source_type == "research_report" for item in result.web_result.evidence))
        self.assertIn("HD현대일렉트릭 수주잔고 OPM 수출 비중 PDF", result.web_result.queries_run)

    def test_hyosung_fixture_html_reaches_stage_3_green(self):
        result = _run_free(
            company_name="효성중공업",
            symbol="298040",
            sector="power_equipment",
            market=Market.KR,
            as_of_date=date(2023, 11, 15),
            fixture_html={
                "효성중공업 컨센서스 상회 Review PDF": HTML_ROOT / "hyosung_heavy_report_search.html",
            },
            fixture_text={
                HYOSUNG_REPORT_URL: TEXT_ROOT / "hyosung_heavy_report.txt",
            },
        )

        self.assertEqual(result.stage.stage, Stage.STAGE_3_GREEN)
        self.assertGreaterEqual(result.score.diagnostic_scores["revision_score"], 50)

    def test_iljin_fixture_html_extracts_contract_and_becomes_candidate(self):
        result = _run_free(
            company_name="일진전기",
            symbol="103590",
            sector="power_equipment",
            market=Market.KR,
            as_of_date=date(2023, 11, 27),
            fixture_html={
                "일진전기 단일판매 공급계약": HTML_ROOT / "iljin_contract_search.html",
            },
            fixture_text={
                ILJIN_DISCLOSURE_URL: TEXT_ROOT / "iljin_contract.txt",
                ILJIN_REPORT_URL: TEXT_ROOT / "iljin_transformer_report.txt",
            },
        )

        disclosure_fields = result.web_result.parsed_disclosures[0].parsed_fields
        self.assertEqual(disclosure_fields["contract_duration_months"], 60)
        self.assertAlmostEqual(disclosure_fields["contract_amount_to_prior_sales"], 0.55)
        self.assertIn(result.stage.stage, {Stage.STAGE_2, Stage.STAGE_3_GREEN, Stage.STAGE_3_YELLOW})

    def test_zoom_fixture_html_marks_one_off_and_stage_3_red(self):
        result = _run_free(
            company_name="Zoom",
            symbol="ZM",
            sector="software",
            market=Market.US,
            as_of_date=date(2020, 9, 1),
            fixture_html={
                "Zoom 영업이익 컨센서스 상회": HTML_ROOT / "zoom_one_off_search.html",
            },
            fixture_text={
                ZOOM_NEWS_URL: TEXT_ROOT / "zoom_one_off_news.txt",
                ZOOM_REPORT_URL: TEXT_ROOT / "zoom_q2_2020_report.txt",
                ZOOM_SEC_URL: TEXT_ROOT / "zoom_sec_disclosure.txt",
            },
        )

        self.assertEqual(result.feature_result.shortage_type.value, "one_off")
        self.assertGreaterEqual(result.score.diagnostic_scores["one_off_shortage_risk"], 80)
        self.assertEqual(result.stage.stage, Stage.STAGE_3_RED)

    def test_smci_fixture_html_triggers_4b_before_4c(self):
        fixture_html = {
            "SMCI 영업이익 컨센서스 상회": HTML_ROOT / "smci_4b_4c_search.html",
            "SMCI 회계 이슈": HTML_ROOT / "smci_4b_4c_search.html",
        }
        fixture_text = {
            SMCI_GUIDANCE_URL: TEXT_ROOT / "smci_guidance_raise.txt",
            SMCI_ACCOUNTING_URL: TEXT_ROOT / "smci_accounting_issue.txt",
        }

        stage4b = _run_free(
            company_name="SMCI",
            symbol="SMCI",
            sector="ai_server",
            market=Market.US,
            as_of_date=date(2024, 1, 18),
            stage_context="4B",
            previous_stage=Stage.STAGE_3_GREEN,
            fixture_html=fixture_html,
            fixture_text=fixture_text,
        )
        stage4c = _run_free(
            company_name="SMCI",
            symbol="SMCI",
            sector="ai_server",
            market=Market.US,
            as_of_date=date(2024, 8, 28),
            stage_context="4C",
            previous_stage=Stage.STAGE_4B,
            fixture_html=fixture_html,
            fixture_text=fixture_text,
        )

        self.assertEqual(stage4b.stage.stage, Stage.STAGE_4B)
        self.assertEqual(stage4c.stage.stage, Stage.STAGE_4C)
        self.assertTrue(stage4c.red_team.has_hard_break)

    def test_search_budget_skips_queries_after_symbol_limit(self):
        result = _run_free(
            company_name="HD현대일렉트릭",
            symbol="267260",
            sector="power_equipment",
            market=Market.KR,
            as_of_date=date(2023, 7, 27),
            fixture_html={
                "HD현대일렉트릭 수주잔고 OPM 수출 비중 PDF": HTML_ROOT / "hd_hyundai_electric_report_search.html",
            },
            fixture_text={HD_REPORT_URL: TEXT_ROOT / "hd_hyundai_electric_report.txt"},
            budget=SearchBudget(max_total_queries_per_day=1, max_queries_per_symbol=1),
        )

        self.assertEqual(result.budget_tracker.total_queries_used, 1)
        self.assertTrue(result.skipped_queries)
        self.assertTrue(all(item.reason == "daily_query_budget_exhausted" or item.reason == "symbol_query_budget_exhausted" for item in result.skipped_queries))

    def test_naver_free_provider_builds_requests_without_credentials(self):
        provider = NaverFreeSearchProvider(client_id="", client_secret="", fixture_mode=False, live_enabled=True)

        results = provider.search("HD현대일렉트릭 목표주가 상향 EPS 상향 PDF", date(2023, 7, 27), max_results=3)

        self.assertEqual(results, ())
        self.assertIn("missing_naver_credentials", provider.errors)
        self.assertEqual({request.params["display"] for request in provider.built_requests}, {3})

    def test_naver_free_provider_default_display_uses_api_maximum(self):
        provider = NaverFreeSearchProvider(client_id="", client_secret="", fixture_mode=False, live_enabled=True)

        provider.search("테스트전자 컨센서스 리포트", date(2026, 6, 8))

        self.assertEqual({request.params["display"] for request in provider.built_requests}, {100})

    def test_naver_response_normalizer_filters_future_results(self):
        payload = {
            "items": [
                {
                    "title": "<b>HD현대일렉트릭</b> 목표주가 상향",
                    "originallink": "https://news.example.com/hd",
                    "description": "컨센서스 상회",
                    "pubDate": "Thu, 27 Jul 2023 08:00:00 +0900",
                },
                {
                    "title": "미래 리포트",
                    "link": "https://news.example.com/future",
                    "description": "future",
                    "pubDate": "Thu, 28 Jul 2023 08:00:00 +0900",
                },
            ]
        }

        results = NaverFreeSearchProvider.normalize_response(
            payload,
            query="HD현대일렉트릭 목표주가 상향 EPS 상향 PDF",
            as_of_date=date(2023, 7, 27),
            source="Naver News",
        )

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "HD현대일렉트릭 목표주가 상향")
        self.assertTrue(results[0].is_news)

    def test_manual_source_provider_is_optional_fallback(self):
        manual = ManualSourceProvider(
            sources=(
                ManualSource(
                    title="ManualCorp 수주잔고 Review PDF",
                    url="manual://manualcorp-report",
                    source="Manual Fixture",
                    published_at="2023-07-27T08:00:00",
                    queries=("ManualCorp 수주잔고 OPM 수출 비중 PDF",),
                    text=(TEXT_ROOT / "hd_hyundai_electric_report.txt").read_text(encoding="utf-8"),
                    is_report_domain=True,
                    is_pdf=True,
                ),
            )
        )

        result = FreeWebResearchRunner(
            browser_provider=BrowserSearchProvider(),
            free_search_provider=EmptySearchProvider(),
            manual_source_provider=manual,
        ).run(
            FreeWebResearchInput(
                company_name="ManualCorp",
                symbol="MANUAL",
                sector="power_equipment",
                market=Market.KR,
                as_of_date=date(2023, 7, 27),
            )
        )

        self.assertTrue(result.web_result.parsed_reports)
        self.assertTrue(any(item.url == "manual://manualcorp-report" for item in result.web_result.search_results))

    def test_report_title_snippet_forward_estimate_flows_to_consensus_proxy(self):
        url = "https://finance.example.com/research/company_read.naver?nid=77"
        provider = FixtureSearchProvider(
            results_by_query={
                "테스트전자 2Q Review 영업이익 컨센서스 PDF": (
                    SearchResult(
                        title="테스트전자 종목분석 - 2Q26 영업이익 70조원 예상",
                        url=url,
                        snippet="목표주가 87만원으로 상향. HBM 수요 증가와 실적 전망치 상향",
                        source="fixture-research",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트전자 2Q Review 영업이익 컨센서스 PDF",
                        rank=1,
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                )
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트전자",
                symbol="123456",
                sector="semiconductor",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={url: "테스트전자는 HBM 수요 증가를 근거로 리포트가 발간됐다."},
            )
        )

        self.assertEqual(len(result.web_result.parsed_reports), 1)
        report = result.web_result.parsed_reports[0]
        self.assertEqual(report.fy1_op, 70_000_000_000_000.0)
        self.assertEqual(report.target_price, 870000)
        self.assertEqual(len(result.feature_input.consensus), 1)
        self.assertEqual(result.feature_input.consensus[0].op_e, 70_000_000_000_000.0)
        self.assertEqual(result.feature_input.consensus[0].target_price, 870000)
        self.assertFalse(result.feature_input.consensus_revisions)
        self.assertTrue(any(item.source_type == "consensus" for item in result.web_result.evidence))
        self.assertIn(
            stable_consensus_evidence_id(
                symbol="123456",
                estimate_date=date(2026, 6, 8),
                fiscal_year=2026,
                source="report_proxy",
            ),
            {item.evidence_id for item in result.web_result.evidence},
        )
        self.assertEqual(result.score.diagnostic_scores["evidence_family_consensus"], 0.0)
        self.assertEqual(result.score.diagnostic_scores["evidence_family_consensus_proxy"], 1.0)
        self.assertNotIn("financial_actuals_from_text", report.parsed_fields)

    def test_power_equipment_report_forward_estimate_flows_to_consensus_proxy(self):
        url = "https://finance.example.com/research/power_equipment_report?nid=88"
        provider = FixtureSearchProvider(
            results_by_query={
                "테스트전력 2Q Review 영업이익 컨센서스 PDF": (
                    SearchResult(
                        title="테스트전력 종목분석 - 2027년 영업이익 2,400억원 전망",
                        url=url,
                        snippet="목표주가 12만원으로 상향. 북미 전력망 투자와 변압기 수주잔고 반영",
                        source="fixture-research",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트전력 2Q Review 영업이익 컨센서스 PDF",
                        rank=1,
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                )
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트전력",
                symbol="654321",
                sector="power_equipment",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={url: "테스트전력은 리드타임 장기화와 수주잔고 증가를 근거로 리포트가 발간됐다."},
            )
        )

        self.assertEqual(len(result.web_result.parsed_reports), 1)
        report = result.web_result.parsed_reports[0]
        self.assertEqual(report.fy1_op, 240_000_000_000.0)
        self.assertEqual(report.target_price, 120000)
        self.assertEqual(len(result.feature_input.consensus), 1)
        self.assertEqual(result.feature_input.consensus[0].fiscal_year, 2027)
        self.assertEqual(result.feature_input.consensus[0].op_e, 240_000_000_000.0)
        self.assertEqual(result.feature_input.consensus[0].target_price, 120000)
        self.assertFalse(result.feature_input.consensus_revisions)
        self.assertTrue(any(item.source_type == "consensus" for item in result.web_result.evidence))
        self.assertIn(
            stable_consensus_evidence_id(
                symbol="654321",
                estimate_date=date(2026, 6, 8),
                fiscal_year=2027,
                source="report_proxy",
            ),
            {item.evidence_id for item in result.web_result.evidence},
        )
        self.assertEqual(result.score.diagnostic_scores["evidence_family_consensus"], 0.0)
        self.assertEqual(result.score.diagnostic_scores["evidence_family_consensus_proxy"], 1.0)
        self.assertNotIn("hbm_context_mentioned", report.parsed_fields)
        self.assertNotIn("financial_actuals_from_text", report.parsed_fields)

    def test_fetch_unavailable_search_hit_becomes_snippet_only_evidence(self):
        provider = FixtureSearchProvider(
            results_by_query={
                "NAVER 데이터센터 수주": (
                    SearchResult(
                        title="NAVER, 엔비디아와 AI 데이터센터 협력",
                        url="https://news.example.com/naver-ai-dc",
                        snippet="GPU 클라우드 매출 확대 기대",
                        source="fixture-news",
                        query="NAVER 데이터센터 수주",
                        confidence=0.8,
                    ),
                )
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="NAVER",
                symbol="035420",
                sector="platform",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=3,
            )
        )

        self.assertEqual(len(result.web_result.parsed_news), 1)
        news = result.web_result.parsed_news[0]
        self.assertTrue(news.parsed_fields["search_snippet_only"])
        self.assertTrue(news.parsed_fields["search_snippet_date_unverified"])
        self.assertFalse(news.parsed_fields["green_allowed_by_date"])
        self.assertTrue(result.web_result.evidence)
        self.assertEqual(result.score.diagnostic_scores["snippet_only_green_block"], 100.0)
        self.assertEqual(result.score.diagnostic_scores["evidence_family_news"], 0.0)
        self.assertNotEqual(result.stage.stage, Stage.STAGE_3_GREEN)

    def test_live_page_fetch_promotes_search_hit_to_full_news_evidence(self):
        provider = FixtureSearchProvider(
            results_by_query={
                "NAVER 데이터센터 수주": (
                    SearchResult(
                        title="NAVER AI 데이터센터 협력",
                        url="https://example.com/naver-ai",
                        snippet="GPU 클라우드 매출 확대",
                        source="example",
                        query="NAVER 데이터센터 수주",
                        confidence=0.8,
                    ),
                )
            }
        )
        html = """
        <html><body>
        NAVER 데이터센터 엔비디아 GPU 인프라 투자와 클라우드 매출 성장률 40%가 확인됐다.
        </body></html>
        """

        with tempfile.TemporaryDirectory() as tmpdir:
            with patch("e2r.research.page_fetcher.request.urlopen", return_value=_FakeHTTPResponse(html)):
                result = FreeWebResearchRunner(
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=provider,
                ).run(
                    FreeWebResearchInput(
                        company_name="NAVER",
                        symbol="035420",
                        sector="platform",
                        market=Market.KR,
                        as_of_date=date(2026, 6, 8),
                        top_results=3,
                        live_page_fetch_enabled=True,
                        page_fetch_cache_directory=tmpdir,
                    )
                )

        self.assertEqual(len(result.web_result.parsed_news), 1)
        fields = result.web_result.parsed_news[0].parsed_fields
        self.assertFalse(fields["search_snippet_only"])
        self.assertTrue(fields["document_type_inferred_from_fetched_text"])
        self.assertTrue(result.web_result.fetched_documents[0].ok)
        self.assertGreater(result.score.diagnostic_scores["evidence_family_news"], 0.0)
        self.assertEqual(result.score.diagnostic_scores.get("snippet_only_green_block", 0.0), 0.0)

    def test_theme_rebalance_enabled_without_provider_uses_default_codex_provider(self):
        with patch(
            "e2r.llm.codex_theme_provider.CodexCLIThemeRouteProvider.route",
            return_value=ThemeRouteOutput(status="no_transition"),
        ) as route:
            result = FreeWebResearchRunner(
                browser_provider=EmptySearchProvider(),
                free_search_provider=EmptySearchProvider(),
            ).run(
                FreeWebResearchInput(
                    company_name="NAVER",
                    symbol="035420",
                    sector="platform",
                    market=Market.KR,
                    as_of_date=date(2026, 6, 8),
                    theme_rebalance_enabled=True,
                )
            )

        self.assertIsNotNone(result.theme_route)
        self.assertEqual(result.theme_route.status, "no_transition")
        self.assertGreater(route.call_count, 0)
        self.assertEqual(result.theme_route_diagnostics["theme_rebalance_status"], "completed")
        self.assertEqual(result.expansion_queries_run, ())

    def test_theme_route_provider_auto_enables_rebalance(self):
        route_provider = FakeThemeRouteProvider(output=ThemeRouteOutput(status="no_transition"))

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=EmptySearchProvider(),
        ).run(
            FreeWebResearchInput(
                company_name="테스트기업",
                symbol="000001",
                sector=None,
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                theme_route_provider=route_provider,
            )
        )

        self.assertGreaterEqual(len(route_provider.calls), 2)
        self.assertFalse(route_provider.calls[0].score_gap_context)
        self.assertTrue(any(call.score_gap_context for call in route_provider.calls[1:]))
        self.assertEqual(result.theme_route.status, "no_transition")
        self.assertEqual(result.theme_route_diagnostics["theme_rebalance_status"], "completed")

    def test_theme_route_expands_asof_safe_queries_only(self):
        route_provider = FakeThemeRouteProvider(
            output=ThemeRouteOutput(
                status="transition_detected",
                transition_detected=True,
                route_confidence=0.8,
                emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                suggested_queries=("AI 클라우드 매출", "NAVER AI 데이터센터 매출 2027"),
                evidence_slots=(
                    EvidenceSlotStatus(
                        slot="cloud_revenue",
                        status="present",
                        evidence_refs=("news:035420:2026-06-08:fixture-news:test",),
                        confidence=0.8,
                    ),
                ),
            )
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "NAVER 데이터센터 수주": (
                    SearchResult(
                        title="NAVER AI 데이터센터 투자",
                        url="https://news.example.com/naver-ai-dc-trigger",
                        snippet="엔비디아 GPU 협력",
                        source="fixture-news",
                        query="NAVER 데이터센터 수주",
                        confidence=0.8,
                    ),
                ),
                "NAVER AI 클라우드 매출": (
                    SearchResult(
                        title="NAVER AI 클라우드 매출 성장",
                        url="https://news.example.com/naver-ai-cloud-sales",
                        snippet="클라우드 매출 성장률 40%",
                        source="fixture-news",
                        query="NAVER AI 클라우드 매출",
                        confidence=0.8,
                    ),
                ),
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="NAVER",
                symbol="035420",
                sector="platform",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=1,
            )
        )

        self.assertEqual(result.expansion_queries_run, ("NAVER AI 클라우드 매출",))
        self.assertTrue(any(item.reason == "future_query_rejected" for item in result.skipped_queries))
        self.assertIn("NAVER AI 클라우드 매출", result.web_result.query_plan.queries[-1].query)
        self.assertEqual(result.score.diagnostic_scores["theme_rebalance_enabled"], 100.0)
        self.assertEqual(result.score.diagnostic_scores["llm_deep_research_completed"], 100.0)

    def test_theme_route_reasks_llm_when_expansion_query_is_duplicate(self):
        retry_url = "https://news.example.com/test-initial-theme-retry"
        duplicate_query = "테스트초기 수주잔고"
        retry_query = "테스트초기 클라우드 매출 성장률"
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.7,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    suggested_queries=(duplicate_query,),
                ),
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.8,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    suggested_queries=(retry_query,),
                ),
                ThemeRouteOutput(status="no_transition"),
            ]
        )
        provider = FixtureSearchProvider(
            results_by_query={
                retry_query: (
                    SearchResult(
                        title="테스트초기 클라우드 매출 성장",
                        url=retry_url,
                        snippet="클라우드 매출 성장률 42%",
                        source="fixture-news",
                        query=retry_query,
                        confidence=0.8,
                    ),
                ),
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트초기",
                symbol="900001",
                sector="platform",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={retry_url: "테스트초기 클라우드 매출 성장률 42%와 AI 인프라 매출이 확인됐다."},
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=1,
            )
        )

        self.assertIn(retry_query, result.expansion_queries_run)
        self.assertTrue(any(item.reason == "duplicate_theme_query" for item in result.skipped_queries))
        self.assertTrue(any("duplicate_theme_query" in item for item in route_provider.calls[1].score_gap_context))
        self.assertEqual(len(result.web_result.parsed_news), 1)

    def test_theme_route_continues_after_empty_expansion_round(self):
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.7,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    suggested_queries=("AI 매출 확인",),
                    missing_information=("cloud_revenue",),
                ),
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.8,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    suggested_queries=("클라우드 매출 성장률",),
                    evidence_slots=(
                        EvidenceSlotStatus(
                            slot="cloud_revenue",
                            status="present",
                            evidence_refs=("news:035420:2026-06-08:fixture-news:cloud",),
                            confidence=0.8,
                        ),
                    ),
                ),
            ]
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "NAVER AI 매출 확인": (),
                "NAVER 클라우드 매출 성장률": (
                    SearchResult(
                        title="NAVER 클라우드 매출 성장률 40%",
                        url="https://news.example.com/naver-cloud-growth",
                        snippet="AI 클라우드 매출 성장률 40%와 GPU 인프라 투자",
                        source="fixture-news",
                        query="NAVER 클라우드 매출 성장률",
                        confidence=0.8,
                    ),
                ),
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="NAVER",
                symbol="035420",
                sector="platform",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=2,
            )
        )

        self.assertGreaterEqual(len(route_provider.calls), 2)
        self.assertEqual(result.expansion_queries_run, ("NAVER AI 매출 확인", "NAVER 클라우드 매출 성장률"))
        self.assertEqual(len(result.web_result.parsed_news), 1)
        self.assertTrue(result.web_result.parsed_news[0].parsed_fields["gpu_cloud_revenue_visible"])

    def test_theme_evidence_review_receives_fetched_documents(self):
        url = "https://news.example.com/naver-ai-cloud"
        route_ref = stable_news_evidence_id(
            symbol="035420",
            published_date=date(2026, 6, 8),
            source="fixture-news",
            source_url=url,
            title="NAVER AI 클라우드 매출 성장",
        )
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.7,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    suggested_queries=(),
                    missing_information=("cloud_revenue",),
                ),
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.85,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    evidence_slots=(
                        EvidenceSlotStatus(
                            slot="cloud_revenue",
                            status="present",
                            evidence_refs=(route_ref,),
                            confidence=0.8,
                        ),
                    ),
                    missing_information=("fcf_impact",),
                ),
            ]
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "NAVER 데이터센터 수주": (
                    SearchResult(
                        title="NAVER AI 클라우드 매출 성장",
                        url=url,
                        snippet="클라우드 매출 성장률 40%",
                        source="fixture-news",
                        query="NAVER 데이터센터 수주",
                        confidence=0.8,
                    ),
                )
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="NAVER",
                symbol="035420",
                sector="platform",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={
                    url: "NAVER AI 클라우드 매출 성장률 40%와 데이터센터 GPU 인프라 투자가 확인됐다."
                },
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
                theme_evidence_review_enabled=True,
            )
        )

        self.assertGreaterEqual(len(route_provider.calls), 2)
        review_input = route_provider.calls[1]
        self.assertEqual(len(review_input.documents), 1)
        self.assertIn("클라우드 매출 성장률 40%", review_input.documents[0].text_excerpt)
        self.assertFalse(result.web_result.parsed_news[0].parsed_fields["search_snippet_only"])
        self.assertEqual(result.theme_route_diagnostics["theme_evidence_review_status"], "completed")
        self.assertEqual(result.score.diagnostic_scores["green_unlock_evidence_score"], 100.0)

    def test_post_parse_gap_expansion_runs_review_suggested_report_query(self):
        initial_url = "https://news.example.com/test-electronics-hbm"
        report_url = "https://finance.example.com/research/company_read.naver?nid=990"
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.72,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    missing_information=("consensus_report_bridge",),
                ),
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.82,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    missing_information=("컨센서스 리포트",),
                    suggested_queries=("테스트전자 목표주가 상향 EPS 추정치 컨센서스 리포트",),
                ),
            ]
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "테스트전자 데이터센터 수주": (
                    SearchResult(
                        title="테스트전자 HBM 데이터센터 수요 확대",
                        url=initial_url,
                        snippet="AI 데이터센터 수요가 확대된다.",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트전자 데이터센터 수주",
                        is_news=True,
                        confidence=0.8,
                    ),
                ),
                "테스트전자 목표주가 상향 EPS 추정치 컨센서스 리포트": (
                    SearchResult(
                        title="테스트전자 종목분석 - 2Q26 영업이익 70조원 예상",
                        url=report_url,
                        snippet="목표주가 87만원으로 상향. HBM 수요와 EPS 추정치 상향",
                        source="fixture-research",
                        published_at=datetime(2026, 6, 8, 9),
                        query="테스트전자 목표주가 상향 EPS 추정치 컨센서스 리포트",
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                ),
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트전자",
                symbol="123456",
                sector="semiconductor",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={
                    initial_url: "테스트전자는 HBM 데이터센터 수요 확대를 보도했다.",
                    report_url: "테스트전자는 HBM 수요 증가와 EPS 추정치 상향을 근거로 리포트가 발간됐다.",
                },
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
                theme_evidence_review_enabled=True,
            )
        )

        self.assertIn("테스트전자 목표주가 상향 EPS 추정치 컨센서스 리포트", result.expansion_queries_run)
        self.assertGreaterEqual(result.theme_route_diagnostics["post_parse_gap_expansion_count"], 1)
        self.assertEqual(len(result.web_result.parsed_reports), 1)
        self.assertEqual(len(result.feature_input.consensus), 1)
        self.assertIn(
            stable_consensus_evidence_id(
                symbol="123456",
                estimate_date=date(2026, 6, 8),
                fiscal_year=2026,
                source="report_proxy",
            ),
            {item.evidence_id for item in result.web_result.evidence},
        )

    def test_post_parse_gap_expansion_reasks_llm_when_query_is_duplicate(self):
        initial_url = "https://news.example.com/test-post-parse-demand"
        report_url = "https://finance.example.com/research/test-post-parse-retry"
        duplicate_query = "테스트후속 수주잔고"
        retry_query = "테스트후속 EPS OP FCF 추정치 상향 컨센서스 리포트"
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(
                    status="needs_more_evidence",
                    missing_information=("consensus_report_bridge",),
                    suggested_queries=(duplicate_query,),
                ),
                ThemeRouteOutput(
                    status="needs_more_evidence",
                    missing_information=("consensus_report_bridge",),
                    suggested_queries=(retry_query,),
                ),
                ThemeRouteOutput(status="no_transition"),
            ]
        )
        provider = FixtureSearchProvider(
            results_by_query={
                duplicate_query: (
                    SearchResult(
                        title="테스트후속 데이터센터 수요",
                        url=initial_url,
                        snippet="AI 데이터센터 수요가 확대된다.",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query=duplicate_query,
                        is_news=True,
                        confidence=0.8,
                    ),
                ),
                retry_query: (
                    SearchResult(
                        title="테스트후속 추정치 상향 리포트",
                        url=report_url,
                        snippet="EPS 상향 30%, 영업이익 추정치 상향 32%, FCF 상향 24%",
                        source="fixture-research",
                        published_at=datetime(2026, 6, 8, 9),
                        query=retry_query,
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                ),
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트후속",
                symbol="900002",
                sector="semiconductor",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={
                    initial_url: "테스트후속은 AI 데이터센터 수요 확대를 보도했다.",
                    report_url: (
                        "테스트후속 리포트. EPS 상향 30%, 영업이익 추정치 상향 32%, "
                        "FCF 상향 24%, 목표주가 상향 14%."
                    ),
                },
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
                theme_evidence_review_enabled=True,
            )
        )

        self.assertIn(retry_query, result.expansion_queries_run)
        self.assertTrue(any(item.reason == "duplicate_post_parse_gap_query" for item in result.skipped_queries))
        self.assertTrue(any("duplicate_post_parse_gap_query" in item for item in route_provider.calls[2].score_gap_context))
        self.assertTrue(result.feature_input.consensus_revisions)
        self.assertGreaterEqual(result.score.diagnostic_scores["revision_score"], 80.0)

    def test_post_parse_gap_expansion_runs_contract_quality_query_from_missing_slot(self):
        initial_url = "https://news.example.com/test-memory-hbm"
        contract_url = "https://news.example.com/test-memory-hbm-contract-quality"
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.74,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    missing_information=("contract_quality",),
                ),
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.84,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    missing_information=("HBM 장기공급계약 선수금 수주잔고 RPO",),
                    suggested_queries=("테스트메모리 장기공급계약 선수금 수주잔고 RPO",),
                    evidence_slots=(
                        EvidenceSlotStatus(
                            slot="contract_quality",
                            status="missing",
                            missing_reason="장기공급계약의 선수금, 물량, 기간, RPO 확인 필요",
                        ),
                    ),
                ),
            ]
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "테스트메모리 데이터센터 수주": (
                    SearchResult(
                        title="테스트메모리 HBM 데이터센터 수요",
                        url=initial_url,
                        snippet="엔비디아 GPU 수요와 HBM 공급 확대",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트메모리 데이터센터 수주",
                        is_news=True,
                        confidence=0.8,
                    ),
                ),
                "테스트메모리 장기공급계약 선수금 수주잔고 RPO": (
                    SearchResult(
                        title="테스트메모리 HBM 장기공급계약과 선수금 확인",
                        url=contract_url,
                        snippet="사상 최대 수주잔고, 최소 물량 보장, 선수금이 확인됐다.",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 9),
                        query="테스트메모리 장기공급계약 선수금 수주잔고 RPO",
                        is_news=True,
                        confidence=0.9,
                    ),
                ),
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트메모리",
                symbol="654321",
                sector="semiconductor",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={
                    initial_url: "테스트메모리는 HBM 수요와 GPU 고객 확대를 보도했다.",
                    contract_url: (
                        "테스트메모리는 HBM 장기공급계약과 선수금, 최소 물량 보장, "
                        "사상 최대 수주잔고를 확인했다."
                    ),
                },
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
                theme_evidence_review_enabled=True,
            )
        )

        self.assertIn("테스트메모리 장기공급계약 선수금 수주잔고 RPO", result.expansion_queries_run)
        self.assertGreaterEqual(result.theme_route_diagnostics["post_parse_gap_expansion_count"], 1)
        parsed_fields = [item.parsed_fields for item in result.web_result.parsed_news]
        self.assertTrue(any(fields.get("prepayment_exists") for fields in parsed_fields))
        self.assertTrue(any(fields.get("record_backlog") for fields in parsed_fields))

    def test_post_parse_gap_expansion_does_not_synthesize_query_without_llm_suggestion(self):
        initial_url = "https://news.example.com/test-memory-hbm-no-suggestion"
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.74,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    missing_information=("contract_quality",),
                ),
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.84,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    missing_information=("contract_quality", "backlog_or_rpo", "prepayment"),
                    suggested_queries=(),
                    evidence_slots=(
                        EvidenceSlotStatus(
                            slot="contract_quality",
                            status="missing",
                            missing_reason="LLM did not provide a follow-up query",
                        ),
                    ),
                ),
            ]
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "테스트메모리 데이터센터 수주": (
                    SearchResult(
                        title="테스트메모리 HBM 데이터센터 수요",
                        url=initial_url,
                        snippet="엔비디아 GPU 수요와 HBM 공급 확대",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트메모리 데이터센터 수주",
                        is_news=True,
                        confidence=0.8,
                    ),
                ),
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트메모리",
                symbol="654321",
                sector="semiconductor",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={
                    initial_url: "테스트메모리는 HBM 수요와 GPU 고객 확대를 보도했다.",
                },
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
                theme_evidence_review_enabled=True,
            )
        )

        self.assertEqual(result.theme_route_diagnostics["post_parse_gap_expansion_count"], 0)
        self.assertNotIn("테스트메모리 장기공급계약 선수금 수주잔고 RPO", result.expansion_queries_run)

    def test_revision_gap_expansion_searches_estimate_change_from_llm_query(self):
        initial_url = "https://news.example.com/test-electronics-ai-demand"
        revision_url = "https://finance.example.com/research/test-electronics-revision"
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.74,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    missing_information=("revision",),
                ),
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.84,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    missing_information=("이전 추정치 대비 EPS OP FCF 컨센서스 상향률",),
                    suggested_queries=("테스트전자 EPS OP FCF 추정치 상향 컨센서스 변화 리포트",),
                    evidence_slots=(
                        EvidenceSlotStatus(
                            slot="revision",
                            status="missing",
                            missing_reason="이전 추정치와 현재 추정치 비교가 필요",
                        ),
                    ),
                ),
            ]
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "테스트전자 데이터센터 수주": (
                    SearchResult(
                        title="테스트전자 AI 데이터센터 수요",
                        url=initial_url,
                        snippet="AI 수요가 확대된다.",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트전자 데이터센터 수주",
                        is_news=True,
                        confidence=0.8,
                    ),
                ),
                "테스트전자 EPS OP FCF 추정치 상향 컨센서스 변화 리포트": (
                    SearchResult(
                        title="테스트전자 종목분석 - 추정치 대폭 상향",
                        url=revision_url,
                        snippet="EPS 상향 35%, 영업이익 추정치 상향 40%, FCF 상향 25%",
                        source="fixture-research",
                        published_at=datetime(2026, 6, 8, 9),
                        query="테스트전자 EPS OP FCF 추정치 상향 컨센서스 변화 리포트",
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                ),
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트전자",
                symbol="123456",
                sector="semiconductor",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={
                    initial_url: "테스트전자는 AI 데이터센터 수요 확대를 보도했다.",
                    revision_url: (
                        "테스트전자 리포트. EPS 상향 35%, 영업이익 추정치 상향 40%, "
                        "FCF 상향 25%, 목표주가 상향 20%. 원문 기반 추정치 비교."
                    ),
                },
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
                theme_evidence_review_enabled=True,
            )
        )

        self.assertIn("테스트전자 EPS OP FCF 추정치 상향 컨센서스 변화 리포트", result.expansion_queries_run)
        self.assertGreaterEqual(result.theme_route_diagnostics["post_parse_gap_expansion_count"], 1)
        self.assertTrue(result.feature_input.consensus_revisions)
        self.assertGreaterEqual(result.score.diagnostic_scores["revision_score"], 80.0)

    def test_score_gap_expansion_searches_low_revision_after_initial_score(self):
        initial_url = "https://news.example.com/test-score-gap-demand"
        revision_url = "https://finance.example.com/research/test-score-gap-revision"
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(
                    status="needs_more_evidence",
                    missing_information=("revision estimate consensus target price EPS OP FCF",),
                    suggested_queries=("테스트스코어 EPS OP FCF 추정치 상향 컨센서스 변화 리포트",),
                ),
                ThemeRouteOutput(status="no_transition"),
            ]
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "테스트스코어 데이터센터 수주": (
                    SearchResult(
                        title="테스트스코어 데이터센터 수요",
                        url=initial_url,
                        snippet="데이터센터 수요가 확대된다.",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트스코어 데이터센터 수주",
                        is_news=True,
                        confidence=0.8,
                    ),
                ),
                "테스트스코어 EPS OP FCF 추정치 상향 컨센서스 변화 리포트": (
                    SearchResult(
                        title="테스트스코어 추정치 상향 리포트",
                        url=revision_url,
                        snippet="EPS 상향 33%, 영업이익 추정치 상향 36%, FCF 상향 28%",
                        source="fixture-research",
                        published_at=datetime(2026, 6, 8, 9),
                        query="테스트스코어 EPS OP FCF 추정치 상향 컨센서스 변화 리포트",
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                ),
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트스코어",
                symbol="777777",
                sector="semiconductor",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={
                    initial_url: "테스트스코어는 데이터센터 수요 확대를 보도했다.",
                    revision_url: (
                        "테스트스코어 리포트. EPS 상향 33%, 영업이익 추정치 상향 36%, "
                        "FCF 상향 28%, 목표주가 상향 18%."
                    ),
                },
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
                theme_evidence_review_enabled=True,
            )
        )

        self.assertEqual(result.theme_route_diagnostics["post_parse_gap_expansion_count"], 0)
        self.assertGreaterEqual(result.theme_route_diagnostics["post_score_gap_expansion_count"], 1)
        self.assertIn("테스트스코어 EPS OP FCF 추정치 상향 컨센서스 변화 리포트", result.expansion_queries_run)
        self.assertTrue(any("revision" in item for item in route_provider.calls[2].score_gap_context))
        self.assertTrue(result.feature_input.consensus_revisions)
        self.assertGreaterEqual(result.score.diagnostic_scores["revision_score"], 80.0)

    def test_score_gap_expansion_reasks_llm_when_query_is_empty(self):
        initial_url = "https://news.example.com/test-retry-demand"
        revision_url = "https://finance.example.com/research/test-retry-revision"
        query = "테스트재요청 EPS OP FCF 추정치 상향 컨센서스 변화 리포트"
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(
                    status="needs_more_evidence",
                    missing_information=("revision estimate consensus target price EPS OP FCF",),
                    suggested_queries=(),
                ),
                ThemeRouteOutput(
                    status="needs_more_evidence",
                    missing_information=("revision estimate consensus target price EPS OP FCF",),
                    suggested_queries=(query,),
                ),
                ThemeRouteOutput(status="no_transition"),
            ]
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "테스트재요청 데이터센터 수주": (
                    SearchResult(
                        title="테스트재요청 데이터센터 수요",
                        url=initial_url,
                        snippet="데이터센터 수요가 확대된다.",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트재요청 데이터센터 수주",
                        is_news=True,
                        confidence=0.8,
                    ),
                ),
                query: (
                    SearchResult(
                        title="테스트재요청 추정치 상향 리포트",
                        url=revision_url,
                        snippet="EPS 상향 31%, 영업이익 추정치 상향 34%, FCF 상향 29%",
                        source="fixture-research",
                        published_at=datetime(2026, 6, 8, 9),
                        query=query,
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                ),
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트재요청",
                symbol="777778",
                sector="semiconductor",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={
                    initial_url: "테스트재요청은 데이터센터 수요 확대를 보도했다.",
                    revision_url: (
                        "테스트재요청 리포트. EPS 상향 31%, 영업이익 추정치 상향 34%, "
                        "FCF 상향 29%, 목표주가 상향 17%."
                    ),
                },
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
            )
        )

        self.assertIn(query, result.expansion_queries_run)
        self.assertTrue(
            any(
                "previous score-gap route returned no suggested_queries" in item
                for item in route_provider.calls[3].score_gap_context
            )
        )
        self.assertGreaterEqual(result.score.diagnostic_scores["revision_score"], 80.0)

    def test_score_gap_expansion_reasks_llm_when_query_is_duplicate(self):
        initial_url = "https://news.example.com/test-duplicate-demand"
        revision_url = "https://finance.example.com/research/test-duplicate-revision"
        duplicate_query = "테스트중복 데이터센터 수주"
        retry_query = "테스트중복 EPS OP FCF 추정치 상향 컨센서스 변화 리포트"
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(
                    status="needs_more_evidence",
                    missing_information=("revision estimate consensus target price EPS OP FCF",),
                    suggested_queries=(duplicate_query,),
                ),
                ThemeRouteOutput(
                    status="needs_more_evidence",
                    missing_information=("revision estimate consensus target price EPS OP FCF",),
                    suggested_queries=(retry_query,),
                ),
                ThemeRouteOutput(status="no_transition"),
            ]
        )
        provider = FixtureSearchProvider(
            results_by_query={
                duplicate_query: (
                    SearchResult(
                        title="테스트중복 데이터센터 수요",
                        url=initial_url,
                        snippet="데이터센터 수요가 확대된다.",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query=duplicate_query,
                        is_news=True,
                        confidence=0.8,
                    ),
                ),
                retry_query: (
                    SearchResult(
                        title="테스트중복 추정치 상향 리포트",
                        url=revision_url,
                        snippet="EPS 상향 32%, 영업이익 추정치 상향 37%, FCF 상향 26%",
                        source="fixture-research",
                        published_at=datetime(2026, 6, 8, 9),
                        query=retry_query,
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                ),
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트중복",
                symbol="777779",
                sector="semiconductor",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={
                    initial_url: "테스트중복은 데이터센터 수요 확대를 보도했다.",
                    revision_url: (
                        "테스트중복 리포트. EPS 상향 32%, 영업이익 추정치 상향 37%, "
                        "FCF 상향 26%, 목표주가 상향 16%."
                    ),
                },
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
            )
        )

        self.assertIn(retry_query, result.expansion_queries_run)
        self.assertTrue(any(item.reason == "duplicate_score_gap_query" for item in result.skipped_queries))
        self.assertTrue(
            any("duplicate_score_gap_query" in item for item in route_provider.calls[3].score_gap_context)
        )
        self.assertGreaterEqual(result.score.diagnostic_scores["revision_score"], 80.0)

    def test_material_score_gap_without_llm_queries_blocks_score_and_stage(self):
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(
                    status="needs_more_evidence",
                    missing_information=("selected revision source missing",),
                    suggested_queries=(),
                ),
                ThemeRouteOutput(
                    status="needs_more_evidence",
                    missing_information=("selected revision source missing",),
                    suggested_queries=(),
                ),
            ]
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=EmptySearchProvider(),
        ).run(
            FreeWebResearchInput(
                company_name="테스트보류",
                symbol="999998",
                sector="software",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
            )
        )

        self.assertEqual(result.stage.stage, Stage.STAGE_0)
        self.assertEqual(result.score.total_score, 0.0)
        self.assertEqual(result.score.diagnostic_scores["score_valid"], 0.0)
        self.assertEqual(result.score.diagnostic_scores["score_blocked_by_score_gap"], 100.0)
        self.assertEqual(result.theme_route_diagnostics["score_blocked_reason"], "score_gap_llm_no_suggested_queries")
        self.assertEqual(result.theme_route_diagnostics["post_score_gap_expansion_status"], "llm_no_suggested_queries")
        self.assertIn("raw_score_total_before_score_gap_block", result.score.diagnostic_scores)
        self.assertTrue(result.theme_route_diagnostics["material_score_gap_unresolved_gaps"])

    def test_score_gap_expansion_does_not_stop_just_because_total_score_is_high(self):
        inputs = FreeWebResearchInput(
            company_name="테스트고점수",
            symbol="888888",
            sector="software",
            market=Market.KR,
            as_of_date=date(2026, 6, 8),
            theme_rebalance_enabled=True,
            theme_route_provider=FakeThemeRouteProvider(outputs=(ThemeRouteOutput(status="no_transition"),)),
            theme_evidence_review_enabled=True,
        )
        score = ScoreSnapshot(
            symbol="888888",
            as_of_date=date(2026, 6, 8),
            eps_fcf_explosion_score=20.0,
            earnings_visibility_score=20.0,
            bottleneck_pricing_score=20.0,
            market_mispricing_score=15.0,
            valuation_rerating_score=15.0,
            capital_allocation_score=5.0,
            information_confidence_score=5.0,
            risk_penalty=0.0,
            total_score=99.0,
            diagnostic_scores={"revision_score": 0.0},
        )

        self.assertTrue(_post_score_gap_expansion_allowed(inputs, score))

    def test_score_gap_expansion_is_not_disabled_by_query_budget_object(self):
        inputs = FreeWebResearchInput(
            company_name="테스트예산",
            symbol="888887",
            sector="software",
            market=Market.KR,
            as_of_date=date(2026, 6, 8),
            budget=SearchBudget(max_total_queries_per_day=1, max_queries_per_symbol=1),
            theme_rebalance_enabled=True,
            theme_route_provider=FakeThemeRouteProvider(outputs=(ThemeRouteOutput(status="no_transition"),)),
            theme_evidence_review_enabled=True,
        )
        score = ScoreSnapshot(
            symbol="888887",
            as_of_date=date(2026, 6, 8),
            eps_fcf_explosion_score=20.0,
            earnings_visibility_score=20.0,
            bottleneck_pricing_score=20.0,
            market_mispricing_score=15.0,
            valuation_rerating_score=15.0,
            capital_allocation_score=5.0,
            information_confidence_score=5.0,
            risk_penalty=0.0,
            total_score=99.0,
            diagnostic_scores={"revision_score": 0.0},
        )

        self.assertTrue(_post_score_gap_expansion_allowed(inputs, score))

    def test_score_gap_context_includes_fcf_valuation_and_evidence_family_gaps(self):
        score = ScoreSnapshot(
            symbol="888889",
            as_of_date=date(2026, 6, 8),
            eps_fcf_explosion_score=20.0,
            earnings_visibility_score=20.0,
            bottleneck_pricing_score=20.0,
            market_mispricing_score=15.0,
            valuation_rerating_score=15.0,
            capital_allocation_score=5.0,
            information_confidence_score=5.0,
            risk_penalty=0.0,
            total_score=90.0,
            diagnostic_scores={
                "revision_score": 100.0,
                "structural_visibility_quality": 100.0,
                "contract_quality": 100.0,
                "backlog_rpo_visibility": 100.0,
                "capa_constraint": 100.0,
                "asp_pricing_power": 100.0,
                "actual_profit_conversion_score": 80.0,
                "sector_visibility_score": 80.0,
                "sector_bottleneck_score": 80.0,
                "medium_term_revision_visibility": 80.0,
                "fcf_quality_score": 20.0,
                "valuation_score": 20.0,
                "domain_specific_evidence_score": 20.0,
                "evidence_family_price": 0.0,
                "evidence_family_financial_actual": 0.0,
                "evidence_family_disclosure": 0.0,
                "evidence_family_research_report": 0.0,
                "evidence_family_consensus": 0.0,
                "evidence_family_consensus_proxy": 0.0,
                "evidence_family_consensus_revision": 0.0,
                "evidence_family_consensus_revision_proxy": 0.0,
                "evidence_family_news": 0.0,
                "evidence_family_search_snippet_news": 0.0,
                "estimate_missing_revision_source": 100.0,
                "estimate_missing_fcf_source": 100.0,
            },
        )

        gaps = _score_gap_missing_information(score)

        self.assertTrue(any("selected_revision_source_missing" in item for item in gaps))
        self.assertTrue(any("selected_fcf_source_missing" in item for item in gaps))
        self.assertTrue(any("FCF conversion" in item for item in gaps))
        self.assertTrue(any("valuation PER PBR" in item for item in gaps))
        self.assertTrue(any("domain-specific operating KPI" in item for item in gaps))
        self.assertTrue(any("inventory receivables" in item for item in gaps))
        self.assertTrue(any("consensus revision EPS OP FCF" in item for item in gaps))

    def test_independent_evidence_family_gap_is_material_when_llm_cannot_expand(self):
        inputs = FreeWebResearchInput(
            company_name="테스트증거부족",
            symbol="888887",
            sector="software",
            market=Market.KR,
            as_of_date=date(2026, 6, 8),
            theme_rebalance_enabled=True,
            theme_route_provider=FakeThemeRouteProvider(outputs=(ThemeRouteOutput(status="no_transition"),)),
        )
        gap = "missing independent evidence families for stage gate: research_report, consensus_revision; expand source-backed evidence for these families"
        expansion = _ScoreGapExpansionResult(
            status="llm_no_suggested_queries",
            unresolved_gaps=(gap,),
            rejection_reasons=("llm_returned_no_suggested_queries",),
        )

        self.assertEqual(_material_score_gaps((gap,)), (gap,))
        self.assertEqual(
            _score_gap_score_block_reason(inputs=inputs, expansion=expansion),
            "score_gap_llm_no_suggested_queries",
        )

        round_limit = _ScoreGapExpansionResult(
            status="round_limit_reached",
            unresolved_gaps=(gap,),
            rejection_reasons=("max_score_gap_expansion_rounds_reached",),
        )
        self.assertEqual(
            _score_gap_score_block_reason(inputs=inputs, expansion=round_limit, queries_run_count=0),
            "score_gap_round_limit",
        )
        self.assertIsNone(
            _score_gap_score_block_reason(inputs=inputs, expansion=round_limit, queries_run_count=1),
        )

        provider_error = _ScoreGapExpansionResult(
            status="provider_error",
            unresolved_gaps=(gap,),
            blocked_reason="codex_cli_timeout",
        )
        self.assertIsNone(
            _score_gap_score_block_reason(inputs=inputs, expansion=provider_error, queries_run_count=0),
        )

    def test_stage_gate_failures_are_returned_as_llm_gap_context(self):
        score = ScoreSnapshot(
            symbol="888886",
            as_of_date=date(2026, 6, 8),
            eps_fcf_explosion_score=20.0,
            earnings_visibility_score=20.0,
            bottleneck_pricing_score=20.0,
            market_mispricing_score=15.0,
            valuation_rerating_score=15.0,
            capital_allocation_score=5.0,
            information_confidence_score=5.0,
            risk_penalty=0.0,
            total_score=95.0,
            diagnostic_scores={
                "score_valid": 100.0,
                "revision_score": 0.0,
                "structural_visibility_quality": 100.0,
                "contract_quality": 100.0,
                "report_date_confidence": 100.0,
            },
        )

        gaps = _stage_gate_missing_information(score, RedTeamAssessment.empty("888886", date(2026, 6, 8)))

        self.assertTrue(any("failed_stage3_revision" in item for item in gaps))
        self.assertTrue(any("consensus revision" in item for item in gaps))
        self.assertTrue(any("missing independent evidence families" in item for item in gaps))

    def test_price_only_and_emerging_theme_guards_are_returned_as_llm_gap_context(self):
        score = ScoreSnapshot(
            symbol="888885",
            as_of_date=date(2026, 6, 8),
            eps_fcf_explosion_score=20.0,
            earnings_visibility_score=20.0,
            bottleneck_pricing_score=20.0,
            market_mispricing_score=15.0,
            valuation_rerating_score=15.0,
            capital_allocation_score=5.0,
            information_confidence_score=5.0,
            risk_penalty=0.0,
            total_score=95.0,
            diagnostic_scores={
                "score_valid": 100.0,
                "revision_score": 90.0,
                "structural_visibility_quality": 90.0,
                "contract_quality": 90.0,
                "price_only_blowoff_score": 80.0,
                "snippet_only_green_block": 100.0,
                "emerging_theme_active": 100.0,
                "llm_deep_research_completed": 0.0,
                "green_unlock_evidence_score": 0.0,
                "date_unverified_snippet_news_count_capped": 1.0,
            },
        )

        gaps = tuple(
            dict.fromkeys(
                (
                    *_score_gap_missing_information(score),
                    *_stage_gate_missing_information(score, RedTeamAssessment.empty("888885", date(2026, 6, 8))),
                )
            )
        )

        self.assertTrue(any("price-only blowoff" in item for item in gaps))
        self.assertTrue(any("failed_positive_stage_price_only_blowoff" in item for item in gaps))
        self.assertTrue(any("snippet-only" in item for item in gaps))
        self.assertTrue(any("emerging-theme deep research" in item for item in gaps))
        self.assertTrue(any("Green unlock" in item for item in gaps))

    def test_theme_route_canonical_is_applied_to_scoring_without_keyword_hardcode(self):
        url = "https://news.example.com/company-route-noise"
        route_ref = stable_news_evidence_id(
            symbol="000001",
            published_date=date(2026, 6, 8),
            source="fixture-news",
            source_url=url,
            title="테스트기업 실적 회복과 시장 관련기사",
        )
        route_provider = FakeThemeRouteProvider(
            output=ThemeRouteOutput(
                status="transition_detected",
                transition_detected=True,
                route_confidence=0.82,
                large_sector_id="L9_MOBILITY_TRANSPORT_LEISURE",
                canonical_archetype_id="C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
                evidence_slots=(
                    EvidenceSlotStatus(
                        slot="route_basis",
                        status="present",
                        evidence_refs=(route_ref,),
                        confidence=0.8,
                    ),
                ),
            )
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "테스트기업 데이터센터 수주": (
                    SearchResult(
                        title="테스트기업 실적 회복과 시장 관련기사",
                        url=url,
                        snippet="본문은 테스트기업 사업 회복, 하단에는 SK하이닉스 HBM 메모리 기사",
                        source="fixture-news",
                        query="테스트기업 데이터센터 수주",
                        confidence=0.8,
                    ),
                )
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트기업",
                symbol="000001",
                sector=None,
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={
                    url: (
                        "테스트기업은 본업 실적 회복을 보도했다.\n"
                        "관련기사: SK하이닉스 HBM 메모리 공급부족과 엔비디아 수요."
                    )
                },
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
            )
        )

        self.assertEqual(result.feature_input.canonical_archetype_id, "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE")
        self.assertEqual(result.feature_result.source_fields["canonical_archetype_id"], "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE")
        self.assertEqual(result.score.diagnostic_scores["theme_route_applied_to_scoring"], 100.0)

    def test_theme_route_semiconductor_alias_is_normalized_before_scoring(self):
        url = "https://news.example.com/hbm-alias-route"
        route_ref = stable_news_evidence_id(
            symbol="000660",
            published_date=date(2026, 5, 14),
            source="fixture-news",
            source_url=url,
            title="SK하이닉스 HBM 엔비디아 공급 확대",
        )
        route_provider = FakeThemeRouteProvider(
            output=ThemeRouteOutput(
                status="transition_detected",
                transition_detected=True,
                route_confidence=0.86,
                large_sector_id="semiconductors",
                canonical_archetype_id="ai_hbm_structural_memory_supplier",
                evidence_slots=(
                    EvidenceSlotStatus(
                        slot="hbm_revenue_bridge",
                        status="present",
                        evidence_refs=(route_ref,),
                        confidence=0.8,
                    ),
                ),
                normalized_parsed_fields={"hbm_demand_mentioned": True},
            )
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "SK하이닉스 데이터센터 수주": (
                    SearchResult(
                        title="SK하이닉스 HBM 엔비디아 공급 확대",
                        url=url,
                        snippet="HBM 수요와 메모리 공급 확대",
                        source="fixture-news",
                        query="SK하이닉스 데이터센터 수주",
                        confidence=0.8,
                    ),
                )
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="SK하이닉스",
                symbol="000660",
                sector=None,
                market=Market.KR,
                as_of_date=date(2026, 5, 14),
                top_results=5,
                fixture_text_by_url={url: "SK하이닉스 HBM 수요와 메모리 공급 확대가 확인됐다."},
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
            )
        )

        self.assertEqual(result.feature_result.source_fields["large_sector_id"], "L2_AI_SEMICONDUCTOR_ELECTRONICS")
        self.assertEqual(result.feature_result.source_fields["canonical_archetype_id"], "C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertEqual(result.score.diagnostic_scores["theme_route_applied_to_scoring"], 100.0)

    def test_theme_route_canonical_without_source_backed_slot_is_not_applied_to_scoring(self):
        url = "https://news.example.com/company-route-no-source-slot"
        route_provider = FakeThemeRouteProvider(
            output=ThemeRouteOutput(
                status="transition_detected",
                transition_detected=True,
                route_confidence=0.82,
                large_sector_id="L9_MOBILITY_TRANSPORT_LEISURE",
                canonical_archetype_id="C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
                normalized_parsed_fields={"gpu_cloud_revenue_visible": True},
                missing_information=("route_basis_source_backed_evidence",),
            )
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "테스트기업 데이터센터 수주": (
                    SearchResult(
                        title="테스트기업 실적 회복과 시장 관련기사",
                        url=url,
                        snippet="본문은 테스트기업 사업 회복, 하단에는 SK하이닉스 HBM 메모리 기사",
                        source="fixture-news",
                        query="테스트기업 데이터센터 수주",
                        confidence=0.8,
                    ),
                )
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트기업",
                symbol="000001",
                sector=None,
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={
                    url: (
                        "테스트기업은 본업 실적 회복을 보도했다.\n"
                        "관련기사: SK하이닉스 HBM 메모리 공급부족과 엔비디아 수요."
                    )
                },
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
            )
        )

        self.assertIsNone(result.feature_input.canonical_archetype_id)
        self.assertEqual(result.feature_input.agent_extracted_fields, {})
        self.assertNotEqual(result.feature_result.source_fields["canonical_archetype_id"], "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE")
        self.assertEqual(result.theme_route.status, "needs_more_evidence")
        self.assertIsNone(result.theme_route_diagnostics["canonical_archetype_id"])
        self.assertEqual(result.theme_route_diagnostics["theme_evidence_gate_status"], "no_evidence_slots")
        self.assertEqual(result.score.diagnostic_scores["theme_route_applied_to_scoring"], 0.0)
        self.assertEqual(result.stage.stage, Stage.STAGE_0)
        self.assertFalse(result.theme_route_diagnostics["score_valid"])
        self.assertEqual(result.theme_route_diagnostics["score_blocked_reason"], "theme_route_needs_more_evidence")
        self.assertEqual(result.score.diagnostic_scores["score_blocked_by_theme_route"], 100.0)

    def test_source_backed_theme_route_normalized_fields_enter_feature_input(self):
        url = "https://news.example.com/naver-ai-cloud-source-backed"
        route_ref = stable_news_evidence_id(
            symbol="035420",
            published_date=date(2026, 6, 8),
            source="fixture-news",
            source_url=url,
            title="NAVER AI 데이터센터 협력",
        )
        route_provider = FakeThemeRouteProvider(
            output=ThemeRouteOutput(
                status="transition_detected",
                transition_detected=True,
                route_confidence=0.82,
                large_sector_id="L8_PLATFORM_CONTENT_SW_SECURITY",
                canonical_archetype_id="C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
                normalized_parsed_fields={
                    "gpu_cloud_revenue_visible": True,
                    "cloud_revenue_growth_visible": True,
                    "cloud_revenue_growth_pct": 40.0,
                },
                evidence_slots=(
                    EvidenceSlotStatus(
                        slot="cloud_revenue",
                        status="present",
                        evidence_refs=(route_ref,),
                        confidence=0.82,
                    ),
                ),
            )
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "NAVER 데이터센터 수주": (
                    SearchResult(
                        title="NAVER AI 데이터센터 협력",
                        url=url,
                        snippet="엔비디아 GPU 인프라 협력",
                        source="fixture-news",
                        query="NAVER 데이터센터 수주",
                        confidence=0.8,
                    ),
                )
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="NAVER",
                symbol="035420",
                sector="platform",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={url: "NAVER는 엔비디아 GPU 데이터센터 협력을 발표했다."},
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
            )
        )

        self.assertTrue(result.feature_input.agent_extracted_fields["gpu_cloud_revenue_visible"])
        self.assertEqual(result.theme_route_diagnostics["theme_evidence_gate_status"], "source_backed")
        self.assertEqual(result.score.diagnostic_scores["theme_route_applied_to_scoring"], 100.0)
        self.assertGreater(result.score.diagnostic_scores["agent_extracted_field_count_capped"], 0.0)

    def test_low_confidence_theme_route_canonical_is_not_applied_to_scoring(self):
        url = "https://news.example.com/company-route-low-confidence"
        route_provider = FakeThemeRouteProvider(
            output=ThemeRouteOutput(
                status="mixed_route",
                transition_detected=True,
                route_confidence=0.40,
                large_sector_id="L9_MOBILITY_TRANSPORT_LEISURE",
                canonical_archetype_id="C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
                evidence_slots=(
                    EvidenceSlotStatus(
                        slot="route_basis",
                        status="present",
                        evidence_refs=("news:000001:2026-06-08:fixture:route",),
                        confidence=0.8,
                    ),
                ),
            )
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "테스트기업 데이터센터 수주": (
                    SearchResult(
                        title="테스트기업 실적 회복과 시장 관련기사",
                        url=url,
                        snippet="본문은 테스트기업 사업 회복",
                        source="fixture-news",
                        query="테스트기업 데이터센터 수주",
                        confidence=0.8,
                    ),
                )
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트기업",
                symbol="000001",
                sector=None,
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={url: "테스트기업은 본업 실적 회복을 보도했다."},
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
            )
        )

        self.assertIsNone(result.feature_input.canonical_archetype_id)
        self.assertNotEqual(result.feature_result.source_fields["canonical_archetype_id"], "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE")
        self.assertEqual(result.theme_route.status, "needs_more_evidence")
        self.assertIsNone(result.theme_route_diagnostics["canonical_archetype_id"])
        self.assertEqual(result.theme_route_diagnostics["theme_evidence_gate_status"], "no_matching_evidence_refs")
        self.assertEqual(result.score.diagnostic_scores["theme_route_applied_to_scoring"], 0.0)
        self.assertEqual(result.stage.stage, Stage.STAGE_0)
        self.assertFalse(result.theme_route_diagnostics["score_valid"])
        self.assertEqual(result.theme_route_diagnostics["score_blocked_reason"], "theme_route_needs_more_evidence")
        self.assertEqual(result.score.diagnostic_scores["score_blocked_by_theme_route"], 100.0)


def _run_free(
    *,
    company_name,
    symbol,
    sector,
    market,
    as_of_date,
    fixture_html,
    fixture_text,
    stage_context=None,
    previous_stage=None,
    budget=None,
):
    return FreeWebResearchRunner(
        browser_provider=BrowserSearchProvider(fixture_html_by_query=fixture_html),
        free_search_provider=EmptySearchProvider(),
    ).run(
        FreeWebResearchInput(
            company_name=company_name,
            symbol=symbol,
            sector=sector,
            market=market,
            as_of_date=as_of_date,
            stage_context=stage_context,
            previous_stage=previous_stage,
            budget=budget or SearchBudget(),
            fixture_text_by_url=fixture_text,
        )
    )


class _FakeHTTPResponse:
    def __init__(self, body: str, content_type: str = "text/html; charset=utf-8") -> None:
        self._body = body.encode("utf-8")
        self.headers = Message()
        self.headers["Content-Type"] = content_type

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        return None

    def read(self, size: int = -1) -> bytes:
        if size is None or size < 0:
            return self._body
        return self._body[:size]


if __name__ == "__main__":
    unittest.main()
