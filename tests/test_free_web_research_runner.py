from datetime import date
from pathlib import Path
import unittest

from e2r.models import Market, Stage
from e2r.research import EmptySearchProvider
from e2r.research.browser_search_provider import BrowserSearchProvider
from e2r.research.free_web_research_runner import FreeWebResearchInput, FreeWebResearchRunner
from e2r.research.manual_source_provider import ManualSource, ManualSourceProvider
from e2r.research.naver_search_provider import NaverFreeSearchProvider
from e2r.research.search_budget import SearchBudget


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


if __name__ == "__main__":
    unittest.main()
