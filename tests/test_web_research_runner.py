from datetime import date, datetime
from pathlib import Path
import tempfile
import unittest

from e2r.features import DeterministicFeatureEngineer, FeatureEngineeringInput
from e2r.models import Market, Stage
from e2r.red_team import RedTeamEngine
from e2r.research import (
    FixtureSearchProvider,
    PageFetcher,
    PDFTextExtractor,
    RequestOnlySearchProvider,
    SearchResult,
    WebResearchInput,
    WebResearchRunner,
)
from e2r.staging import StageClassificationInput, StageClassifier


HD_REPORT_URL = "https://ssl.pstatic.net/imgstock/upload/research/company/hd_줄을서시오.pdf"
HD_DISCLOSURE_URL = "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=202307270001"
HD_NEWS_URL = "https://news.example.com/hd-power-shortage"

HD_REPORT_TEXT = """
발행일 2023.07.27
증권사: HistoricalBroker
애널리스트: Fixture Analyst
제목: HD현대일렉트릭 줄을 서시오

현재가 69,600원
목표주가 95,000원
목표주가 상향 25%
상승여력 36%
FY1 매출액 3,300,000 영업이익 620,000 EPS 13,500
FY2 매출액 3,800,000 영업이익 720,000 EPS 15,800
PER 6.3배
PBR 1.4배
ROE 22%
OPM 18.8%

영업이익 YoY 220%
EPS YoY 210%
FCF 증가율 170%
EPS 상향 35%
영업이익 추정치 상향 38%
FCF 질 점수 95

수주잔고 3,720,000
신규수주 1,230,000
수주잔고/매출 155%
계약기간 60개월
계약 매출액 대비 55%
선수금 있음
해지 불가
사상 최대 수주잔고

CAPA 증가율 35%
CAPA utilization 96%
CAPA 선점 3년
CAPA 부족으로 리드타임 24개월 이상이다.
ASP YoY 18%
판가 전가 확인
구조적 공급부족이 지속된다.
멀티플 상향과 리레이팅 구간이다.
OPM 개선폭 9%
CAPEX/매출 20%
투자포인트: 수주잔고 확대|마진 개선|북미 전력망 병목
리스크: 증설 지연|원가 변동
"""

HD_DISCLOSURE_TEXT = """
단일판매·공급계약체결
계약금액 2,900억원
최근매출액 대비 55%
계약기간 2023.07.27 ~ 2028.07.26
계약상대방: 북미 전력망 고객
계약내용: 초고압 변압기 장기공급계약
선수금 조건, 수주잔고 반영, 해지 불가
"""

HD_NEWS_TEXT = """
HD현대일렉트릭은 북미 전력기기 공급 부족과 변압기 리드타임 장기화로 판가 상승이 이어진다고 보도됐다.
"""


class WebResearchRunnerTests(unittest.TestCase):
    def test_query_planner_search_rank_fetch_parse_hd_like_report(self):
        result = _run_hd_web_research()

        self.assertIn("HD현대일렉트릭 수주잔고 OPM 수출 비중 PDF", result.queries_run)
        self.assertEqual(result.selected_results[0].result.title, "HD현대일렉트릭 줄을 서시오")
        self.assertGreater(result.selected_results[0].score, 50)
        self.assertTrue(result.fetched_documents[0].ok)

        report = result.parsed_reports[0]
        self.assertEqual(report.current_price, 69600)
        self.assertEqual(report.target_price, 95000)
        self.assertEqual(report.target_revision_pct, 25)
        self.assertEqual(report.order_backlog_to_sales, 155)
        self.assertEqual(report.opm, 18.8)
        self.assertTrue(report.shortage_mentioned)
        self.assertEqual(report.parsed_fields["lead_time_months"], 24)
        self.assertTrue(any(item.source_type == "research_report" for item in result.evidence))

    def test_hyosung_like_margin_recovery_report_produces_evidence(self):
        url = "https://hanaw.com/download/research/hyosung_low_margin_cleanup.pdf"
        text = """
발행일 2023.11.15
증권사: Hana Research
제목: 효성중공업 저마진 수주 정리
목표주가 210,000원
목표주가 상향 30%
PER 7.2배
PBR 1.1배
OPM 11.5%
OPM 개선폭 6%
저마진 수주 정리 이후 영업이익률 회복이 확인된다.
"""
        runner = _runner(
            {
                "효성중공업 컨센서스 상회 Review PDF": (
                    SearchResult(
                        title="효성중공업 저마진 수주 정리",
                        url=url,
                        source="Hana Research",
                        published_at=datetime(2023, 11, 15, 8),
                        query="효성중공업 컨센서스 상회 Review PDF",
                        rank=1,
                        is_pdf=True,
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                )
            },
            {url: text},
        )

        result = runner.run(WebResearchInput("효성중공업", "298040", "power_equipment", Market.KR, date(2023, 11, 15)))

        self.assertEqual(result.parsed_reports[0].target_revision_pct, 30)
        self.assertEqual(result.parsed_reports[0].est_per, 7.2)
        self.assertEqual(result.parsed_reports[0].parsed_fields["opm_expansion_pctp"], 6)
        self.assertTrue(result.evidence)

    def test_iljin_like_contract_disclosure_extracts_contract_terms(self):
        url = "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=202311270001"
        text = """
단일판매·공급계약체결
계약금액 2,025억원
최근매출액 대비 37.07%
계약기간 2026.01.01 ~ 2030.12.31
계약상대방: 미국 에너지 회사
계약내용: 초고압 변압기 공급
선수금 조건 수주잔고 반영
"""
        runner = _runner(
            {
                "일진전기 단일판매 공급계약": (
                    SearchResult(
                        title="일진전기 단일판매 공급계약 공시",
                        url=url,
                        source="OpenDART",
                        published_at=datetime(2023, 11, 27, 8),
                        query="일진전기 단일판매 공급계약",
                        rank=1,
                        is_disclosure=True,
                        confidence=0.95,
                    ),
                )
            },
            {url: text},
        )

        result = runner.run(WebResearchInput("일진전기", "103590", "power_equipment", Market.KR, date(2023, 11, 27)))
        fields = result.parsed_disclosures[0].parsed_fields

        self.assertAlmostEqual(fields["contract_amount_to_prior_sales"], 0.3707)
        self.assertEqual(fields["contract_duration_months"], 60)
        self.assertTrue(fields["prepayment_exists"])
        self.assertTrue(any(item.source_type == "disclosure" for item in result.evidence))

    def test_zoom_like_one_off_demand_news_is_marked_one_off(self):
        url = "https://news.example.com/zoom-pandemic-eps"
        text = "팬데믹과 코로나 재택근무 일회성 수요로 EPS YoY 400% 증가가 보도됐다."
        runner = _runner(
            {
                "Zoom 영업이익 컨센서스 상회": (
                    SearchResult(
                        title="Zoom 영업이익 컨센서스 상회, 팬데믹 일회성 수요",
                        url=url,
                        source="Naver News",
                        published_at=datetime(2020, 9, 1, 8),
                        query="Zoom 영업이익 컨센서스 상회",
                        rank=1,
                        is_news=True,
                        confidence=0.8,
                    ),
                )
            },
            {url: text},
        )

        result = runner.run(WebResearchInput("Zoom", "ZM", "software", Market.US, date(2020, 9, 1)))
        fields = result.parsed_news[0].parsed_fields

        self.assertEqual(fields["shortage_type"], "one_off")
        self.assertGreaterEqual(fields["one_off_shortage_risk"], 90)
        self.assertTrue(any(item.parsed_fields.get("shortage_type") == "one_off" for item in result.evidence))

    def test_smci_like_accounting_issue_emits_red_team_candidate(self):
        url = "https://news.example.com/smci-accounting-issue"
        text = "SMCI 회계 이슈와 감사의견 관련 신뢰 훼손 우려가 보도됐다."
        runner = _runner(
            {
                "SMCI 회계 이슈": (
                    SearchResult(
                        title="SMCI 회계 이슈",
                        url=url,
                        source="Naver News",
                        published_at=datetime(2024, 8, 28, 8),
                        query="SMCI 회계 이슈",
                        rank=1,
                        is_news=True,
                        confidence=0.85,
                    ),
                )
            },
            {url: text},
        )

        result = runner.run(WebResearchInput("SMCI", "SMCI", "ai_server", Market.US, date(2024, 8, 28), stage_context="4B"))

        self.assertTrue(result.red_team_findings)
        self.assertEqual(result.red_team_findings[0].risk_type, "accounting_or_trust_issue")
        self.assertTrue(any(item.parsed_fields.get("accounting_or_trust_issue") for item in result.evidence))

    def test_request_only_provider_records_request_without_live_call(self):
        provider = RequestOnlySearchProvider(provider_name="bing")

        results = provider.search("HD현대일렉트릭 목표주가 상향 EPS 상향 PDF", date(2023, 7, 27), max_results=3)

        self.assertEqual(results, ())
        self.assertEqual(provider.built_requests[0].url, "https://api.bing.microsoft.com/v7.0/search")
        self.assertEqual(provider.built_requests[0].params["count"], 3)

    def test_pdf_text_extractor_uses_txt_fixture_without_pdf_dependency(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            txt_path = Path(tmpdir) / "report.txt"
            txt_path.write_text("목표주가 95,000원", encoding="utf-8")

            result = PDFTextExtractor().extract_text(Path(tmpdir) / "report.pdf")

            self.assertTrue(result.ok)
            self.assertIn("목표주가", result.text)

    def test_web_research_output_can_reach_stage_3_green(self):
        web_result = _run_hd_web_research()
        feature_input = FeatureEngineeringInput(
            symbol="267260",
            as_of_date=date(2023, 7, 27),
            disclosures=web_result.parsed_disclosures,
            research_reports=web_result.parsed_reports,
            news_items=web_result.parsed_news,
        )
        feature_result = DeterministicFeatureEngineer().engineer(feature_input)
        score = feature_result.score()
        red_team = RedTeamEngine().assess(feature_result.red_team_signals)
        stage = StageClassifier().classify(
            StageClassificationInput(
                score=score,
                red_team=red_team,
                theme_regime_score=80,
                company_event_score=80,
                high_quality_company_event=True,
                evidence_ids=tuple(item.evidence_id for item in web_result.evidence),
            )
        )

        self.assertGreaterEqual(score.total_score, 85)
        self.assertEqual(feature_result.shortage_type.value, "structural")
        self.assertEqual(stage.stage, Stage.STAGE_3_GREEN)


def _run_hd_web_research():
    return _runner(
        {
            "HD현대일렉트릭 수주잔고 OPM 수출 비중 PDF": (
                SearchResult(
                    title="HD현대일렉트릭 줄을 서시오",
                    url=HD_REPORT_URL,
                    source="HistoricalBroker Research",
                    published_at=datetime(2023, 7, 27, 8),
                    query="HD현대일렉트릭 수주잔고 OPM 수출 비중 PDF",
                    rank=1,
                    is_pdf=True,
                    is_report_domain=True,
                    confidence=0.95,
                ),
            ),
            "HD현대일렉트릭 단일판매 공급계약": (
                SearchResult(
                    title="HD현대일렉트릭 단일판매 공급계약 공시",
                    url=HD_DISCLOSURE_URL,
                    source="OpenDART",
                    published_at=datetime(2023, 7, 27, 8),
                    query="HD현대일렉트릭 단일판매 공급계약",
                    rank=1,
                    is_disclosure=True,
                    confidence=0.95,
                ),
            ),
            "HD현대일렉트릭 공급부족": (
                SearchResult(
                    title="HD현대일렉트릭 공급부족과 판가 상승",
                    url=HD_NEWS_URL,
                    source="Naver News",
                    published_at=datetime(2023, 7, 27, 8),
                    query="HD현대일렉트릭 공급부족",
                    rank=1,
                    is_news=True,
                    confidence=0.8,
                ),
            ),
        },
        {
            HD_REPORT_URL: HD_REPORT_TEXT,
            HD_DISCLOSURE_URL: HD_DISCLOSURE_TEXT,
            HD_NEWS_URL: HD_NEWS_TEXT,
        },
    ).run(WebResearchInput("HD현대일렉트릭", "267260", "power_equipment", Market.KR, date(2023, 7, 27)))


def _runner(results_by_query, fixture_text_by_url):
    return WebResearchRunner(
        search_provider=FixtureSearchProvider(results_by_query=results_by_query),
        page_fetcher=PageFetcher(fixture_text_by_url=fixture_text_by_url),
    )


if __name__ == "__main__":
    unittest.main()
