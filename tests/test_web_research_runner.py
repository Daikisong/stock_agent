from datetime import date, datetime
from email.message import Message
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from e2r.features import DeterministicFeatureEngineer, FeatureEngineeringInput
from e2r.models import Market, NewsItem, Stage
from e2r.red_team import RedTeamEngine
from e2r.research import (
    FixtureSearchProvider,
    PageFetcher,
    PDFTextExtractionResult,
    PDFTextExtractor,
    RequestOnlySearchProvider,
    SearchResult,
    SearchResultRanker,
    WebResearchInput,
    WebResearchRunner,
    extract_e2r_text_fields,
)
from e2r.research.query_planner import QueryPlan, QuerySpec
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
    def test_web_research_input_bounds_fetch_selection_by_default(self):
        inputs = WebResearchInput("테스트", "123456", "semiconductor", Market.KR, date(2026, 6, 8))

        self.assertEqual(inputs.max_results_per_query, 100)
        self.assertEqual(inputs.top_results, 60)
        with self.assertRaisesRegex(ValueError, "top_results must be bounded"):
            WebResearchInput("테스트", "123456", "semiconductor", Market.KR, date(2026, 6, 8), top_results=None)
        with self.assertRaisesRegex(ValueError, "top_results must be non-negative"):
            WebResearchInput("테스트", "123456", "semiconductor", Market.KR, date(2026, 6, 8), top_results=-1)

    def test_lightweight_text_extractor_recognizes_v12_common_bridge_aliases(self):
        fields = extract_e2r_text_fields(
            """
정책 승인과 프로젝트 수주, 회사 현금흐름 연결, implementation timeline이 확인된다.
spread expansion, ex-credit margin, utilization rate, inventory cycle이 보인다.
datacenter customer, HBM customer order, qualification confirmed, volume visibility도 확인된다.
HBM 수요 증가와 메모리 가격 상승, 공급조절, advanced packaging bottleneck, 중기 추정치 상향이 확인된다.
글로벌 유통망 확대와 플랫폼 유통 확대, 해외 채널 확대가 이어진다.
일반 장비도 CAPA 제약과 capacity bottleneck이 있고, 자사주 소각과 배당 확대가 있다.
CSM 성장, 준비금 안정, 손해율 개선, FDA 승인 후 매출 전환, 로열티와 보험급여가 확인된다.
ARR 성장, renewal, seat expansion, PF 익스포저 축소, 재무구조 개선, 현금 회수 가시성도 보인다.
valuation overheat, evidence source quality, thesis break, event spread risk가 남아 있다.
""",
            as_of_date=date(2024, 11, 20),
        )

        self.assertTrue(fields["policy_or_regulatory_confirmed"])
        self.assertTrue(fields["project_award_confirmed"])
        self.assertTrue(fields["direct_company_cash_route"])
        self.assertTrue(fields["implementation_timeline"])
        self.assertTrue(fields["spread_expansion"])
        self.assertTrue(fields["ex_credit_margin"])
        self.assertTrue(fields["utilization_rate"])
        self.assertTrue(fields["inventory_cycle"])
        self.assertTrue(fields["datacenter_customer"])
        self.assertTrue(fields["hbm_customer_order"])
        self.assertTrue(fields["qualification_confirmed"])
        self.assertTrue(fields["volume_visibility"])
        self.assertTrue(fields["cycle_demand_visibility"])
        self.assertTrue(fields["end_market_demand_visibility"])
        self.assertTrue(fields["supply_demand_tightness"])
        self.assertTrue(fields["cycle_to_revenue_bridge"])
        self.assertTrue(fields["advanced_packaging_bottleneck"])
        self.assertTrue(fields["platform_distribution_scale"])
        self.assertTrue(fields["brand_channel_expansion"])
        self.assertTrue(fields["overseas_channel_expansion"])
        self.assertTrue(fields["capacity_constraint"])
        self.assertTrue(fields["capa_shortage"])
        self.assertTrue(fields["capital_return_execution"])
        self.assertTrue(fields["dividend_visibility"])
        self.assertTrue(fields["csm_growth_visible"])
        self.assertTrue(fields["reserve_quality_visible"])
        self.assertTrue(fields["loss_ratio_quality"])
        self.assertTrue(fields["regulatory_approval_confirmed"])
        self.assertTrue(fields["approval_to_revenue_bridge"])
        self.assertTrue(fields["royalty_route"])
        self.assertTrue(fields["reimbursement_confirmed"])
        self.assertTrue(fields["arr_growth_visible"])
        self.assertTrue(fields["retention_or_renewal"])
        self.assertTrue(fields["seat_expansion_visible"])
        self.assertTrue(fields["pf_exposure_reduced"])
        self.assertTrue(fields["balance_sheet_repair"])
        self.assertTrue(fields["cash_collection_visible"])
        self.assertTrue(fields["valuation_overheat"])
        self.assertTrue(fields["evidence_source_quality"])
        self.assertTrue(fields["thesis_break_confirmed"])
        self.assertTrue(fields["event_spread_risk"])

    def test_lightweight_text_extractor_reads_internal_source_backed_field_block(self):
        fields = extract_e2r_text_fields(
            """
일반 본문에는 없는 검증된 내부 필드 블록이다.
E2R_SOURCE_BACKED_FIELD actual_op_yoy_pct=120.5
E2R_SOURCE_BACKED_FIELD hbm_capacity_pre_sold=true
E2R_SOURCE_BACKED_FIELD revenue_visibility_contract=true
E2R_SOURCE_BACKED_FIELD compiled_claim_ids=["CLM-DO-NOT-IMPORT"]
E2R_SOURCE_BACKED_FIELD source_url="https://example.com/do-not-import"
""",
            as_of_date=date(2024, 4, 25),
        )

        self.assertEqual(fields["actual_op_yoy_pct"], 120.5)
        self.assertTrue(fields["hbm_capacity_pre_sold"])
        self.assertTrue(fields["revenue_visibility_contract"])
        self.assertNotIn("compiled_claim_ids", fields)
        self.assertNotIn("source_url", fields)

    def test_source_backed_field_block_keeps_full_report_text_before_company_window_trim(self):
        query = "SK하이닉스 ASP 상승"
        url = "https://research.example.com/hynix-hbm-source-backed"
        text = """
SK하이닉스 HBM 리포트
SK하이닉스는 HBM 고객 물량과 매출 전환을 확인했다.
""" + ("\n본문 여백" * 120) + """
BEGIN_E2R_SOURCE_BACKED_FIELDS
E2R_SOURCE_BACKED_FIELD actual_op_yoy_pct=120.0
E2R_SOURCE_BACKED_FIELD hbm_capacity_pre_sold=true
E2R_SOURCE_BACKED_FIELD revenue_visibility_contract=true
END_E2R_SOURCE_BACKED_FIELDS
"""
        runner = WebResearchRunner(
            query_planner=_SingleQueryPlanner(query),
            search_provider=FixtureSearchProvider(
                results_by_query={
                    query: (
                        SearchResult(
                            title="SK하이닉스 HBM source-backed report",
                            url=url,
                            snippet="SK하이닉스 HBM 고객 물량",
                            published_at=datetime(2024, 4, 25, 8),
                            query=query,
                            rank=1,
                            is_report_domain=True,
                            confidence=0.8,
                        ),
                    )
                }
            ),
            page_fetcher=PageFetcher(fixture_text_by_url={url: text}),
        )

        output = runner.run(WebResearchInput("SK하이닉스", "000660", "semiconductor", Market.KR, date(2024, 4, 25)))

        fields = output.parsed_reports[0].parsed_fields
        self.assertEqual(fields["actual_op_yoy_pct"], 120.0)
        self.assertTrue(fields["hbm_capacity_pre_sold"])
        self.assertTrue(fields["revenue_visibility_contract"])
        self.assertIn("actual_op_yoy_pct", fields["compiled_claim_ids_by_primitive"])

    def test_red_team_source_backed_report_is_company_relevant(self):
        query = "삼양식품 thesis break"
        url = "https://research.example.com/samyang-redteam"
        text = """
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM guard fixture
삼양식품 (003230) R13 guard source-backed fixture

thesis_break_confirmed, valuation_overheat, missing_cashflow_bridge
BEGIN_E2R_SOURCE_BACKED_FIELDS
E2R_SOURCE_BACKED_FIELD thesis_break_confirmed=true
E2R_SOURCE_BACKED_FIELD valuation_overheat=true
E2R_SOURCE_BACKED_FIELD missing_cashflow_bridge=true
END_E2R_SOURCE_BACKED_FIELDS
"""
        runner = WebResearchRunner(
            query_planner=_SingleQueryPlanner(query),
            search_provider=FixtureSearchProvider(
                results_by_query={
                    query: (
                        SearchResult(
                            title="R13 guard fixture",
                            url=url,
                            snippet="삼양식품 thesis break valuation",
                            published_at=datetime(2024, 6, 18, 8),
                            query=query,
                            rank=1,
                            is_report_domain=True,
                            confidence=0.8,
                        ),
                    )
                }
            ),
            page_fetcher=PageFetcher(fixture_text_by_url={url: text}),
        )

        output = runner.run(WebResearchInput("삼양식품", "003230", "consumer", Market.KR, date(2024, 6, 18)))

        self.assertEqual(len(output.parsed_reports), 1)
        fields = output.parsed_reports[0].parsed_fields
        self.assertTrue(fields["thesis_break_confirmed"])
        self.assertTrue(fields["valuation_overheat"])
        self.assertTrue(fields["missing_cashflow_bridge"])

    def test_default_selection_does_not_cap_ranked_results(self):
        query = "테스트전자 리포트"
        results = tuple(
            SearchResult(
                title=f"테스트전자 성장 리포트 {index}",
                url=f"https://example.com/test-{index}",
                snippet="테스트전자 매출 성장과 FCF 개선",
                query=query,
                rank=index,
                is_news=True,
                confidence=0.8,
            )
            for index in range(1, 13)
        )
        runner = WebResearchRunner(
            query_planner=_SingleQueryPlanner(query),
            search_provider=FixtureSearchProvider(results_by_query={query: results}),
        )

        output = runner.run(WebResearchInput("테스트전자", "123456", "semiconductor", Market.KR, date(2026, 6, 8)))

        self.assertEqual(len(output.search_results), 12)
        self.assertEqual(len(output.selected_results), 12)
        self.assertFalse(any(item.reason == "not_selected" for item in output.dropped_results))

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

    def test_one_off_cost_reduction_does_not_create_shortage_risk(self):
        url = "https://news.example.com/samsung-hbm-profit"
        text = "삼성전자는 HBM 수요와 제품 가격 상승, 전 분기 재고 관련 일회성 비용 감소로 영업이익이 개선됐다."
        runner = _runner(
            {
                "삼성전자 영업이익 컨센서스 상회": (
                    SearchResult(
                        title="삼성전자 HBM 가격 상승과 일회성 비용 감소",
                        url=url,
                        source="Naver News",
                        published_at=datetime(2026, 6, 9, 8),
                        query="삼성전자 영업이익 컨센서스 상회",
                        rank=1,
                        is_news=True,
                        confidence=0.8,
                    ),
                )
            },
            {url: text},
        )

        result = runner.run(WebResearchInput("삼성전자", "005930", "semiconductor", Market.KR, date(2026, 6, 9)))
        fields = result.parsed_news[0].parsed_fields

        self.assertNotIn("shortage_type", fields)
        self.assertNotIn("one_off_shortage", fields)
        self.assertNotIn("pandemic_demand_spike", fields)
        self.assertNotIn("temporary_shortage", fields)
        self.assertNotIn("one_off_shortage_risk", fields)

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
        self.assertFalse(result.red_team_findings[0].is_hard_break)
        self.assertTrue(any(item.parsed_fields.get("accounting_or_trust_issue") for item in result.evidence))

    def test_worldex_audit_opinion_with_samsung_customer_mention_does_not_create_samsung_4c(self):
        url = "https://news.example.com/worldex-audit-opinion"
        text = "월덱스는 삼성전자를 주요 고객사로 두고 있으며 2020년 감사의견은 적정이었다."
        runner = _runner(
            {
                "삼성전자 감사의견": (
                    SearchResult(
                        title="월덱스 감사의견 적정",
                        url=url,
                        source="Naver News",
                        published_at=datetime(2026, 6, 9, 8),
                        query="삼성전자 감사의견",
                        rank=1,
                        is_news=True,
                        confidence=0.85,
                    ),
                )
            },
            {url: text},
        )

        web_result = runner.run(WebResearchInput("삼성전자", "005930", "semiconductor", Market.KR, date(2026, 6, 9)))
        contaminated_news = NewsItem(
            symbol="005930",
            sector="semiconductor",
            published_at=datetime(2026, 6, 9, 8),
            source="fixture-news",
            title="월덱스 감사의견 적정",
            as_of_date=date(2026, 6, 9),
            body=text,
            parsed_fields={"accounting_or_trust_issue": True},
        )
        feature_result = DeterministicFeatureEngineer().engineer(
            FeatureEngineeringInput(
                symbol="005930",
                company_name="삼성전자",
                sector_context="semiconductor",
                as_of_date=date(2026, 6, 9),
                news_items=(contaminated_news,),
            )
        )
        score = feature_result.score()
        red_team = RedTeamEngine().assess(feature_result.red_team_signals)
        stage = StageClassifier().classify(StageClassificationInput(score=score, red_team=red_team))

        self.assertEqual(web_result.parsed_news, ())
        self.assertEqual(web_result.red_team_findings, ())
        self.assertTrue(any(item.reason == "company_not_found_in_fetched_document" for item in web_result.dropped_results))
        self.assertEqual(
            score.diagnostic_scores["legacy_direct_score_field_without_v2_claim_count_capped"],
            1.0,
        )
        self.assertEqual(score.diagnostic_scores["research_axis_bridge_guard_risk"], 0.0)
        self.assertNotEqual(
            feature_result.source_fields["canonical_archetype_id"],
            "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION",
        )
        self.assertFalse(red_team.has_hard_break)
        self.assertFalse(any(item.risk_type == "accounting_or_trust_issue" for item in red_team.findings))
        self.assertNotEqual(stage.stage, Stage.STAGE_4C)

    def test_site_boilerplate_does_not_create_ai_or_accounting_route(self):
        url = "https://news.example.com/hyundai-auto-brief"
        text = """
        현대차는 하이브리드 수출과 완성차 마진 개선 기대가 보도됐다.
        항상 AI종목추천 서비스에 관심을 갖고 이용해주셔서 감사드립니다.
        대차·공매도 메뉴와 청와대·감사원 링크는 사이트 공통 하단이다.
        """
        runner = _runner(
            {
                "현대차 영업이익 컨센서스 상회": (
                    SearchResult(
                        title="현대차 하이브리드 수출과 마진 개선",
                        url=url,
                        source="Naver News",
                        published_at=datetime(2026, 6, 9, 8),
                        query="현대차 영업이익 컨센서스 상회",
                        rank=1,
                        is_news=True,
                        confidence=0.8,
                    ),
                )
            },
            {url: text},
        )

        web_result = runner.run(WebResearchInput("현대차", "005380", "auto", Market.KR, date(2026, 6, 9)))
        fields = web_result.parsed_news[0].parsed_fields
        feature_result = DeterministicFeatureEngineer().engineer(
            FeatureEngineeringInput(
                symbol="005380",
                company_name="현대차",
                sector_context="auto",
                as_of_date=date(2026, 6, 9),
                news_items=web_result.parsed_news,
            )
        )

        self.assertFalse(fields.get("accounting_or_trust_issue"))
        self.assertFalse(fields.get("emerging_theme_ai_infra_platform_datacenter"))
        self.assertNotEqual(feature_result.source_fields["sector_profile"], "AI_INFRA_PLATFORM")
        self.assertNotEqual(
            feature_result.source_fields["canonical_archetype_id"],
            "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION",
        )

    def test_related_article_defense_footer_does_not_route_hbm_news_to_c03(self):
        url = "https://news.example.com/sk-hynix-hbm"
        text = """
        SK하이닉스는 AI 데이터센터의 HBM 수요 증가와 메모리 가격 상승으로 실적 가시성이 개선되고 있다.
        엔비디아 차세대 가속기 물량 확대와 서버용 D램 공급부족도 수익성 개선 요인으로 언급됐다.
        많이 본 기사
        K-방산 수출 운명의 분수령, 폴란드 훈련서 K2·K9 전차와 자주포 전개.
        오늘의 주요뉴스
        """
        runner = _runner(
            {
                "SK하이닉스 데이터센터 수주": (
                    SearchResult(
                        title="SK하이닉스 HBM 수요와 메모리 가격 상승",
                        url=url,
                        snippet="엔비디아 AI 데이터센터 수요로 HBM 공급부족",
                        source="Naver News",
                        published_at=datetime(2026, 6, 9, 8),
                        query="SK하이닉스 데이터센터 수주",
                        rank=1,
                        is_news=True,
                        confidence=0.8,
                    ),
                )
            },
            {url: text},
        )

        web_result = runner.run(WebResearchInput("SK하이닉스", "000660", "semiconductor", Market.KR, date(2026, 6, 9)))
        fields = web_result.parsed_news[0].parsed_fields
        feature_result = DeterministicFeatureEngineer().engineer(
            FeatureEngineeringInput(
                symbol="000660",
                company_name="SK하이닉스",
                sector_context="semiconductor",
                as_of_date=date(2026, 6, 9),
                news_items=web_result.parsed_news,
            )
        )

        self.assertFalse(fields.get("government_customer"))
        self.assertEqual(feature_result.source_fields["sector_profile"], "MEMORY_HBM")
        self.assertNotEqual(feature_result.source_fields["canonical_archetype_id"], "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG")

    def test_request_only_provider_records_request_without_live_call(self):
        provider = RequestOnlySearchProvider(provider_name="bing")

        results = provider.search("HD현대일렉트릭 목표주가 상향 EPS 상향 PDF", date(2023, 7, 27), max_results=3)

        self.assertEqual(results, ())
        self.assertEqual(provider.built_requests[0].url, "https://api.bing.microsoft.com/v7.0/search")
        self.assertEqual(provider.built_requests[0].params["count"], 3)

    def test_ranker_prefers_query_intent_match_over_generic_old_report(self):
        query = "NAVER AI 데이터센터 클라우드 매출"
        generic_report = SearchResult(
            title="NAVER 목표주가 상향 Review PDF",
            url="https://finance.naver.com/research/company_read.naver?nid=1",
            snippet="NAVER 목표주가 리포트",
            source="research",
            published_at=datetime(2023, 1, 1, 8),
            query=query,
            rank=1,
            is_report_domain=True,
            is_pdf=True,
            confidence=0.8,
        )
        relevant_news = SearchResult(
            title="NAVER AI 데이터센터 클라우드 매출 성장",
            url="https://news.example.com/naver-ai-cloud",
            snippet="데이터센터 GPU 투자와 클라우드 매출 확대",
            source="fixture-news",
            published_at=datetime(2026, 6, 8, 8),
            query=query,
            rank=2,
            is_news=True,
            confidence=0.7,
        )

        ranked = SearchResultRanker().rank((generic_report, relevant_news), company_name="NAVER", as_of_date=date(2026, 6, 8))

        self.assertEqual(ranked[0].result.url, relevant_news.url)
        self.assertIn("query_intent_match", ranked[0].positive_reasons)
        self.assertIn("query_intent_mismatch", ranked[1].negative_reasons)

    def test_ranker_tie_breaks_by_url_not_provider_order(self):
        query = "테스트전자 목표주가 상향"
        first = SearchResult(
            title="테스트전자 목표주가 상향 Review",
            url="https://research.example.com/b.pdf",
            snippet="테스트전자 목표주가 상향",
            source="fixture-research",
            published_at=datetime(2026, 6, 8, 8),
            query=query,
            rank=1,
            is_report_domain=True,
            confidence=0.8,
        )
        second = SearchResult(
            title="테스트전자 목표주가 상향 Review",
            url="https://research.example.com/a.pdf",
            snippet="테스트전자 목표주가 상향",
            source="fixture-research",
            published_at=datetime(2026, 6, 8, 8),
            query=query,
            rank=1,
            is_report_domain=True,
            confidence=0.8,
        )

        ranked_forward = SearchResultRanker().rank((first, second), company_name="테스트전자", as_of_date=date(2026, 6, 8))
        ranked_reversed = SearchResultRanker().rank((second, first), company_name="테스트전자", as_of_date=date(2026, 6, 8))

        self.assertEqual([item.result.url for item in ranked_forward], [item.result.url for item in ranked_reversed])
        self.assertEqual(ranked_forward[0].result.url, "https://research.example.com/a.pdf")

    def test_selection_keeps_query_axis_coverage(self):
        runner = _runner(
            {
                "테스트전자 수주잔고": (
                    SearchResult(
                        title="테스트전자 수주잔고 사상 최대 Review PDF",
                        url="https://research.example.com/test-backlog-1.pdf",
                        snippet="테스트전자 수주잔고 OPM CAPA ASP",
                        source="fixture-research",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트전자 수주잔고",
                        rank=1,
                        is_report_domain=True,
                        is_pdf=True,
                        confidence=0.95,
                    ),
                    SearchResult(
                        title="테스트전자 수주잔고 장기공급계약 PDF",
                        url="https://research.example.com/test-backlog-2.pdf",
                        snippet="테스트전자 수주잔고 장기공급계약 CAPA",
                        source="fixture-research",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트전자 수주잔고",
                        rank=2,
                        is_report_domain=True,
                        is_pdf=True,
                        confidence=0.95,
                    ),
                ),
                "테스트전자 영업이익 컨센서스 상회": (
                    SearchResult(
                        title="테스트전자, 1분기 영업이익 컨센서스 상회",
                        url="https://news.example.com/test-op-beat",
                        snippet="테스트전자 영업이익 6.6조원, 컨센서스 상회",
                        source="fixture-news",
                        published_at=None,
                        query="테스트전자 영업이익 컨센서스 상회",
                        rank=1,
                        is_news=True,
                        confidence=0.8,
                    ),
                ),
            },
            {},
        )

        result = runner.run(WebResearchInput("테스트전자", "123456", "semiconductor", Market.KR, date(2026, 6, 8), top_results=2))
        selected_queries = {item.result.query for item in result.selected_results}

        self.assertIn("테스트전자 수주잔고", selected_queries)
        self.assertIn("테스트전자 영업이익 컨센서스 상회", selected_queries)

    def test_pdf_text_extractor_uses_txt_fixture_without_pdf_dependency(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            txt_path = Path(tmpdir) / "report.txt"
            txt_path.write_text("목표주가 95,000원", encoding="utf-8")

            result = PDFTextExtractor().extract_text(Path(tmpdir) / "report.pdf")

            self.assertTrue(result.ok)
            self.assertIn("목표주가", result.text)

    def test_page_fetcher_live_fetches_html_text_and_uses_cache(self):
        html = """
        <html>
          <head>
            <meta name="description" content="NAVER AI 클라우드 매출 성장률 40%">
            <script>window.secret = "ignore me";</script>
          </head>
          <body>
            <article><h1>NAVER 데이터센터</h1><p>엔비디아 GPU 인프라 투자와 AI 매출 성장률 40%</p></article>
          </body>
        </html>
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            fetcher = PageFetcher(live_enabled=True, cache_directory=tmpdir)
            with patch("e2r.research.page_fetcher.request.urlopen", return_value=_FakeHTTPResponse(html)):
                first = fetcher.fetch("https://example.com/naver-ai", as_of_date=date(2026, 6, 8))

            self.assertTrue(first.ok)
            self.assertIn("NAVER AI 클라우드 매출 성장률 40%", first.text)
            self.assertIn("NAVER 데이터센터", first.text)
            self.assertNotIn("ignore me", first.text)
            self.assertIsNotNone(first.source_path)

            with patch("e2r.research.page_fetcher.request.urlopen") as urlopen:
                second = fetcher.fetch("https://example.com/naver-ai", as_of_date=date(2026, 6, 8))

            self.assertTrue(second.ok)
            self.assertEqual(second.text, first.text)

    def test_page_fetcher_live_extracts_pdf_text_and_uses_cache(self):
        extractor = _FakePDFExtractor("HBM 완판과 고객 물량 배정")
        with tempfile.TemporaryDirectory() as tmpdir:
            fetcher = PageFetcher(
                live_enabled=True,
                cache_directory=tmpdir,
                pdf_text_extractor=extractor,
            )
            with patch(
                "e2r.research.page_fetcher.request.urlopen",
                return_value=_FakeHTTPResponse("%PDF-1.4 fixture", content_type="application/pdf"),
            ):
                first = fetcher.fetch("https://broker.example.com/hbm.pdf", as_of_date=date(2026, 6, 8))

            self.assertTrue(first.ok)
            self.assertIn("HBM 완판", first.text)
            self.assertEqual(extractor.payload_count, 1)
            self.assertIsNotNone(first.source_path)

            with patch("e2r.research.page_fetcher.request.urlopen") as urlopen:
                second = fetcher.fetch("https://broker.example.com/hbm.pdf", as_of_date=date(2026, 6, 8))

            self.assertTrue(second.ok)
            self.assertEqual(second.text, first.text)
            self.assertEqual(extractor.payload_count, 1)
            urlopen.assert_not_called()
            urlopen.assert_not_called()

    def test_page_fetcher_percent_encodes_non_ascii_live_url(self):
        with patch("e2r.research.page_fetcher.request.urlopen", return_value=_FakeHTTPResponse("본문")) as urlopen:
            result = PageFetcher(live_enabled=True).fetch(
                "https://example.com/search/하이닉스?q=HBM 고객",
                as_of_date=date(2026, 6, 8),
            )

        self.assertTrue(result.ok)
        request_arg = urlopen.call_args.args[0]
        self.assertEqual(
            request_arg.full_url,
            "https://example.com/search/%ED%95%98%EC%9D%B4%EB%8B%89%EC%8A%A4?q=HBM%20%EA%B3%A0%EA%B0%9D",
        )

    def test_page_fetcher_rejects_non_http_live_url(self):
        result = PageFetcher(live_enabled=True).fetch("manual://naver-ai", as_of_date=date(2026, 6, 8))

        self.assertFalse(result.ok)
        self.assertEqual(result.reason, "unsupported_url_scheme_for_live_fetch")

    def test_unknown_fetched_document_becomes_full_news_evidence(self):
        url = "https://example.com/naver-ai"
        text = "NAVER 데이터센터 엔비디아 GPU 인프라 투자와 클라우드 매출 성장률 40%가 확인됐다."
        runner = _runner(
            {
                "NAVER 데이터센터 수주": (
                    SearchResult(
                        title="NAVER AI 데이터센터 협력",
                        url=url,
                        snippet="GPU 클라우드 매출 확대",
                        source="example",
                        published_at=datetime(2026, 6, 8, 8),
                        query="NAVER 데이터센터 수주",
                        rank=1,
                        confidence=0.8,
                    ),
                )
            },
            {url: text},
        )

        result = runner.run(WebResearchInput("NAVER", "035420", "platform", Market.KR, date(2026, 6, 8)))

        self.assertEqual(len(result.parsed_news), 1)
        fields = result.parsed_news[0].parsed_fields
        self.assertFalse(fields["search_snippet_only"])
        self.assertTrue(fields["document_type_inferred_from_fetched_text"])
        self.assertTrue(fields["gpu_cloud_revenue_visible"])
        self.assertFalse(any(item.reason == "unknown_document_type" for item in result.dropped_results))
        self.assertTrue(any(item.source_type == "news" for item in result.evidence))

    def test_market_list_company_mention_is_not_company_relevant_evidence(self):
        url = "https://news.example.com/market-list"
        runner = _runner(
            {
                "알테오젠 ASP 상승": (
                    SearchResult(
                        title="코스피 마감, 시총 상위 알테오젠 하락",
                        url=url,
                        snippet="SK하이닉스 낸드 ASP 상승률 전망, 코스닥 시총 상위 알테오젠 하락",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="알테오젠 ASP 상승",
                        rank=1,
                        is_news=True,
                        confidence=0.8,
                    ),
                )
            },
            {url: "코스닥 시총 상위 종목 중 알테오젠은 하락했다. SK하이닉스 낸드 ASP 상승 전망이 언급됐다."},
        )

        result = runner.run(WebResearchInput("알테오젠", "196170", "biotech", Market.KR, date(2026, 6, 8)))

        self.assertEqual(result.parsed_news, ())
        self.assertTrue(any(item.reason == "company_not_found_in_fetched_document" for item in result.dropped_results))

    def test_other_company_report_is_dropped_when_target_only_appears_in_snippet(self):
        url = "https://finance.naver.com/research/company_read.naver?nid=89042"
        runner = _runner(
            {
                "SK하이닉스 데이터센터 수주": (
                    SearchResult(
                        title="디아이 종목분석 - 올해 신규 수주 가시화로 사상 최대 실적 예상",
                        url=url,
                        snippet="SK하이닉스 HBM 장비 수주잔고 관련 검색 결과",
                        source="Naver Finance Research",
                        published_at=datetime(2026, 6, 9, 8),
                        query="SK하이닉스 데이터센터 수주",
                        rank=1,
                        is_report_domain=True,
                        is_disclosure=True,
                        confidence=0.9,
                    ),
                )
            },
            {
                url: (
                    "디아이 종목분석 - 올해 신규 수주 가시화로 사상 최대 실적 예상\n"
                    "디아이는 반도체 검사장비 신규 수주와 사상 최대 실적이 예상된다.\n"
                    "증권 검색 자동완성: SK하이닉스 000660 매출 실적"
                )
            },
        )

        result = runner.run(WebResearchInput("SK하이닉스", "000660", "semiconductor", Market.KR, date(2026, 6, 9)))

        self.assertEqual(result.parsed_reports, ())
        self.assertEqual(result.parsed_disclosures, ())
        self.assertEqual(result.parsed_news, ())
        self.assertTrue(any(item.reason == "company_not_found_in_fetched_document" for item in result.dropped_results))

    def test_other_company_report_snippet_is_not_used_when_fetch_unavailable(self):
        url = "https://finance.naver.com/research/company_read.naver?nid=89043"
        runner = _runner(
            {
                "SK하이닉스 데이터센터 수주": (
                    SearchResult(
                        title="디아이 종목분석 - 올해 신규 수주 가시화로 사상 최대 실적 예상",
                        url=url,
                        snippet="SK하이닉스 HBM 장비 수주잔고 관련 검색 결과",
                        source="Naver Finance Research",
                        published_at=datetime(2026, 6, 9, 8),
                        query="SK하이닉스 데이터센터 수주",
                        rank=1,
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                )
            },
            {},
        )

        result = runner.run(WebResearchInput("SK하이닉스", "000660", "semiconductor", Market.KR, date(2026, 6, 9)))

        self.assertEqual(result.parsed_news, ())
        self.assertTrue(result.dropped_results)
        self.assertFalse(any(item.reason == "fetch_unavailable_snippet_evidence_used" for item in result.dropped_results))

    def test_other_company_article_is_dropped_when_target_only_appears_late(self):
        url = "https://news.example.com/alpha-build"
        body = (
            "알파건설은 해외 플랜트 수주잔고가 증가했다고 밝혔다. "
            "이번 계약은 건설 부문 매출과 영업이익 개선에 기여할 전망이다. "
            + "본문 내용 " * 400
            + "관련 종목 검색 영역: 알파전자 영업이익 컨센서스 상회"
        )
        runner = _runner(
            {
                "알파전자 수주잔고": (
                    SearchResult(
                        title="알파건설 해외 플랜트 수주잔고 증가",
                        url=url,
                        snippet="알파전자 수주잔고 검색 결과",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="알파전자 수주잔고",
                        rank=1,
                        is_news=True,
                        confidence=0.8,
                    ),
                )
            },
            {url: body},
        )

        result = runner.run(WebResearchInput("알파전자", "123456", "semiconductor", Market.KR, date(2026, 6, 8)))

        self.assertEqual(result.parsed_news, ())
        self.assertTrue(any(item.reason == "company_not_found_in_fetched_document" for item in result.dropped_results))

    def test_shorthand_title_is_kept_when_target_appears_in_lead_body(self):
        url = "https://news.example.com/alpha-foundry"
        body = "알파전자는 파운드리 수주잔고와 HBM 수요 증가로 영업이익 개선이 예상된다고 밝혔다."
        runner = _runner(
            {
                "알파전자 수주잔고": (
                    SearchResult(
                        title="알파 파운드리 5년 수주잔고 확대",
                        url=url,
                        snippet="파운드리 수주잔고 확대",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="알파전자 수주잔고",
                        rank=1,
                        is_news=True,
                        confidence=0.8,
                    ),
                )
            },
            {url: body},
        )

        result = runner.run(WebResearchInput("알파전자", "123456", "semiconductor", Market.KR, date(2026, 6, 8)))

        self.assertEqual(len(result.parsed_news), 1)
        self.assertTrue(result.parsed_news[0].parsed_fields["hbm_demand_mentioned"])

    def test_snippet_quarterly_financials_become_structured_fields(self):
        url = "https://news.example.com/test-electronics-2025-q1"
        runner = _runner(
            {
                "테스트전자 영업이익 컨센서스 상회": (
                    SearchResult(
                        title="테스트전자, 2025년 1분기 실적 발표",
                        url=url,
                        snippet="테스트전자는 연결 기준으로 매출 79.14조원, 영업이익 6.7조원의 2025년 1분기 실적을 발표했다. 영업이익은 컨센서스를 상회했다.",
                        source="fixture-search",
                        published_at=None,
                        query="테스트전자 영업이익 컨센서스 상회",
                        rank=1,
                        is_news=True,
                        confidence=0.8,
                    ),
                )
            },
            {},
        )

        result = runner.run(WebResearchInput("테스트전자", "123456", "semiconductor", Market.KR, date(2026, 6, 8)))

        self.assertEqual(len(result.parsed_news), 1)
        fields = result.parsed_news[0].parsed_fields
        self.assertTrue(fields["financial_actuals_from_text"])
        self.assertEqual(fields["reported_fiscal_year"], 2025)
        self.assertEqual(fields["reported_fiscal_quarter"], 1)
        self.assertAlmostEqual(fields["actual_sales"], 79.14 * 1_000_000_000_000.0)
        self.assertAlmostEqual(fields["actual_operating_profit"], 6.7 * 1_000_000_000_000.0)
        self.assertTrue(fields["earnings_beat_mentioned"])
        self.assertTrue(fields["search_snippet_only"])
        self.assertFalse(fields["green_allowed_by_date"])

    def test_stale_historical_report_is_not_used_as_current_research(self):
        url = "https://finance.example.com/research/company_read?nid=17"
        text = """
        알파전자 종목분석 - 영업이익 14조원으로 컨센서스 상회
        2Q17 잠정실적 Review: 알파전자의 17년 2분기 매출액은 60조원(YoY +18%),
        영업이익은 14조원(YoY +72%)로 컨센서스를 상회했다.
        목표주가 상향 20%
        """
        runner = _runner(
            {
                "알파전자 영업이익 컨센서스 상회": (
                    SearchResult(
                        title="알파전자 종목분석 - 영업이익 14조원으로 컨센서스 상회",
                        url=url,
                        source="fixture-research",
                        published_at=None,
                        query="알파전자 영업이익 컨센서스 상회",
                        rank=1,
                        is_report_domain=True,
                        confidence=0.8,
                    ),
                )
            },
            {url: text},
        )

        result = runner.run(WebResearchInput("알파전자", "123456", "semiconductor", Market.KR, date(2026, 6, 8)))

        self.assertEqual(result.parsed_reports, ())
        self.assertTrue(any(item.reason == "stale_research_report_inferred_period" for item in result.dropped_results))

    def test_target_price_news_is_not_forced_into_research_report_parser(self):
        url = "https://news.example.com/test-target-upgrade"
        text = "테스트전자는 실적 전망치 상향 조정과 함께 목표주가를 기존 26만원에서 33만원으로 상향했다. 영업이익 추정치 상향도 언급됐다."
        runner = _runner(
            {
                "테스트전자 목표주가 상향 EPS 상향 PDF": (
                    SearchResult(
                        title="테스트전자, 실적 전망치 상향 조정에 목표주가 상향",
                        url=url,
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트전자 목표주가 상향 EPS 상향 PDF",
                        rank=1,
                        confidence=0.8,
                    ),
                )
            },
            {url: text},
        )

        result = runner.run(WebResearchInput("테스트전자", "123456", "semiconductor", Market.KR, date(2026, 6, 8)))

        self.assertEqual(result.parsed_reports, ())
        self.assertEqual(len(result.parsed_news), 1)
        self.assertTrue(result.parsed_news[0].parsed_fields["estimate_upgrade_mentioned"])
        self.assertTrue(result.parsed_news[0].parsed_fields["target_price_upgrade_mentioned"])
        self.assertAlmostEqual(result.parsed_news[0].parsed_fields["target_price_revision_pct"], 26.9231, places=3)

    def test_target_price_revision_respects_korean_price_units(self):
        url = "https://news.example.com/test-target-unit-upgrade"
        text = "테스트전자는 목표주가를 기존 8만원에서 11만원으로 상향했다. 실적 전망치 상향도 언급됐다."
        runner = _runner(
            {
                "테스트전자 목표주가 상향 EPS 상향 PDF": (
                    SearchResult(
                        title="테스트전자 목표주가 상향",
                        url=url,
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트전자 목표주가 상향 EPS 상향 PDF",
                        rank=1,
                        confidence=0.8,
                    ),
                )
            },
            {url: text},
        )

        result = runner.run(WebResearchInput("테스트전자", "123456", "semiconductor", Market.KR, date(2026, 6, 8)))

        self.assertEqual(len(result.parsed_news), 1)
        self.assertAlmostEqual(result.parsed_news[0].parsed_fields["target_price_revision_pct"], 37.5, places=3)

    def test_forward_estimate_amount_is_not_actual_financial(self):
        url = "https://news.example.com/test-forward-estimate"
        text = "테스트전자는 2027년 영업이익 전망치를 395조원으로 상향했다. 실적 전망치 상향이 핵심이다."
        runner = _runner(
            {
                "테스트전자 영업이익 컨센서스 상회": (
                    SearchResult(
                        title="테스트전자 영업이익 전망치 상향",
                        url=url,
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트전자 영업이익 컨센서스 상회",
                        rank=1,
                        is_news=True,
                        confidence=0.8,
                    ),
                )
            },
            {url: text},
        )

        result = runner.run(WebResearchInput("테스트전자", "123456", "semiconductor", Market.KR, date(2026, 6, 8)))

        fields = result.parsed_news[0].parsed_fields
        self.assertTrue(fields["estimate_upgrade_mentioned"])
        self.assertNotIn("actual_operating_profit", fields)
        self.assertNotIn("financial_actuals_from_text", fields)

    def test_report_forward_estimate_amount_is_not_actual_financial(self):
        url = "https://finance.example.com/research/company_read?nid=77"
        text = "본문에는 HBM 수요 증가와 실적 전망치 상향이 핵심이라고만 적혀 있다."
        runner = _runner(
            {
                "테스트전자 영업이익 컨센서스 상회": (
                    SearchResult(
                        title="테스트전자 종목분석 - 2Q26 영업이익 70조원 예상",
                        url=url,
                        snippet="목표주가 87만원으로 상향",
                        source="fixture-research",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트전자 영업이익 컨센서스 상회",
                        rank=1,
                        is_report_domain=True,
                        confidence=0.8,
                    ),
                )
            },
            {url: text},
        )

        result = runner.run(WebResearchInput("테스트전자", "123456", "semiconductor", Market.KR, date(2026, 6, 8)))

        fields = result.parsed_reports[0].parsed_fields
        self.assertTrue(fields["estimate_upgrade_mentioned"])
        self.assertTrue(fields["forward_estimate_present"])
        self.assertEqual(fields["fy1_fiscal_year"], 2026)
        self.assertEqual(result.parsed_reports[0].fy1_op, 70_000_000_000_000.0)
        self.assertEqual(result.parsed_reports[0].target_price, 870000)
        self.assertTrue(fields["target_price_upgrade_mentioned"])
        self.assertNotIn("actual_operating_profit", fields)
        self.assertNotIn("financial_actuals_from_text", fields)

    def test_forward_estimate_yoy_is_not_actual_financial(self):
        url = "https://news.example.com/test-forward-yoy"
        text = "테스트전자는 2Q26 매출 전년 대비 40% 증가와 영업이익 70조원 달성이 예상된다고 밝혔다."
        runner = _runner(
            {
                "테스트전자 영업이익 컨센서스 상회": (
                    SearchResult(
                        title="테스트전자 2Q26 실적 전망 상향",
                        url=url,
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트전자 영업이익 컨센서스 상회",
                        rank=1,
                        is_news=True,
                        confidence=0.8,
                    ),
                )
            },
            {url: text},
        )

        result = runner.run(WebResearchInput("테스트전자", "123456", "semiconductor", Market.KR, date(2026, 6, 8)))

        fields = result.parsed_news[0].parsed_fields
        self.assertNotIn("actual_sales_yoy_pct", fields)
        self.assertNotIn("actual_op_yoy_pct", fields)
        self.assertNotIn("financial_actuals_from_text", fields)

    def test_market_list_article_does_not_leak_other_company_fields(self):
        url = "https://news.example.com/today-watchlist"
        text = """
        [오늘의 종목] 테스트전자·다른전자
        다른전자는 목표주가를 기존 10만원에서 20만원으로 상향했고 2027년 영업이익 전망치를 50조원으로 올렸다.
        테스트전자는 HBM 매출 성장과 데이터센터 수요가 확인됐다.
        """
        runner = _runner(
            {
                "테스트전자 수주잔고": (
                    SearchResult(
                        title="[오늘의 종목] 테스트전자·다른전자",
                        url=url,
                        snippet="다른전자는 목표주가 상향, 테스트전자는 HBM 매출 성장",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트전자 수주잔고",
                        rank=1,
                        is_news=True,
                        confidence=0.8,
                    ),
                )
            },
            {url: text},
        )

        result = runner.run(WebResearchInput("테스트전자", "123456", "semiconductor", Market.KR, date(2026, 6, 8)))

        fields = result.parsed_news[0].parsed_fields
        self.assertNotIn("target_price_revision_pct", fields)
        self.assertNotIn("actual_operating_profit", fields)
        self.assertTrue(fields["theme_business_link_mentioned"])

    def test_supply_contract_news_is_not_treated_as_disclosure_without_disclosure_context(self):
        url = "https://news.example.com/industry-lta"
        text = """
        테스트전자와 다른전자가 선급금과 최소 매출 보장이 포함된 장기공급계약을 확대한다.
        2Q26 실적은 매출액 87.3조원과 영업이익 70.0조원으로 전망된다.
        테스트전자는 HBM 수요와 장기계약 구조가 확인됐다.
        """
        runner = _runner(
            {
                "테스트전자 수주잔고": (
                    SearchResult(
                        title="'슈퍼 을' 테스트전자 장기공급계약 확대",
                        url=url,
                        snippet="테스트전자와 다른전자 장기공급계약 확대",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트전자 수주잔고",
                        rank=1,
                        is_news=True,
                        is_disclosure=True,
                        confidence=0.8,
                    ),
                )
            },
            {url: text},
        )

        result = runner.run(WebResearchInput("테스트전자", "123456", "semiconductor", Market.KR, date(2026, 6, 8)))

        self.assertEqual(result.parsed_disclosures, ())
        self.assertEqual(len(result.parsed_news), 1)
        fields = result.parsed_news[0].parsed_fields
        self.assertTrue(fields["multi_year_contract"])
        self.assertTrue(fields["minimum_revenue_guarantee"])
        self.assertTrue(fields["revenue_visibility_contract"])
        self.assertNotIn("actual_sales", fields)
        self.assertNotIn("actual_operating_profit", fields)
        self.assertNotIn("financial_actuals_from_text", fields)

    def test_industry_article_does_not_leak_peer_actual_financials(self):
        url = "https://news.example.com/k-sector-lta"
        text = """
        K반도체 장기공급계약 확대
        테스트전자는 선급금과 최소 매출 보장이 포함된 장기공급계약을 확대한다.
        다른전자는 2025년 1분기 실적이 매출액 87.3조원과 영업이익 70.0조원으로 발표됐다.
        테스트전자는 HBM 수요와 장기계약 구조가 확인됐다.
        """
        runner = _runner(
            {
                "테스트전자 수주잔고": (
                    SearchResult(
                        title="'슈퍼 을' K반도체 장기공급계약 확대",
                        url=url,
                        snippet="테스트전자와 다른전자 장기공급계약 확대",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트전자 수주잔고",
                        rank=1,
                        is_news=True,
                        confidence=0.8,
                    ),
                )
            },
            {url: text},
        )

        result = runner.run(WebResearchInput("테스트전자", "123456", "semiconductor", Market.KR, date(2026, 6, 8)))

        self.assertEqual(len(result.parsed_news), 1)
        fields = result.parsed_news[0].parsed_fields
        self.assertTrue(fields["multi_year_contract"])
        self.assertTrue(fields["minimum_revenue_guarantee"])
        self.assertTrue(fields["revenue_visibility_contract"])
        self.assertNotIn("actual_sales", fields)
        self.assertNotIn("actual_operating_profit", fields)
        self.assertNotIn("financial_actuals_from_text", fields)

    def test_sales_multiple_is_not_parsed_as_actual_sales_amount(self):
        url = "https://news.example.com/test-backlog-sales-multiple"
        text = "테스트전자는 파운드리 5년 수주잔고가 전년 매출 8배에 이른다고 밝혔다."
        runner = _runner(
            {
                "테스트전자 수주잔고": (
                    SearchResult(
                        title="테스트전자 파운드리 5년 수주잔고, 전년 매출 8배",
                        url=url,
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트전자 수주잔고",
                        rank=1,
                        is_news=True,
                        confidence=0.8,
                    ),
                )
            },
            {url: text},
        )

        result = runner.run(WebResearchInput("테스트전자", "123456", "semiconductor", Market.KR, date(2026, 6, 8)))

        self.assertEqual(len(result.parsed_news), 1)
        self.assertNotIn("actual_sales", result.parsed_news[0].parsed_fields)
        self.assertNotIn("financial_actuals_from_text", result.parsed_news[0].parsed_fields)

    def test_direct_company_body_context_is_kept_even_when_title_is_market_theme(self):
        url = "https://news.example.com/holding-direct-body"
        runner = _runner(
            {
                "SK스퀘어 수주잔고": (
                    SearchResult(
                        title="월가 AI 돈줄, 한국 반도체까지 흔든다",
                        url=url,
                        snippet="지분가치와 수주잔고 관련주 점검",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="SK스퀘어 수주잔고",
                        rank=1,
                        is_news=True,
                        confidence=0.8,
                    ),
                )
            },
            {
                url: (
                    "SK스퀘어는 직접 제조기업은 아니지만 SK하이닉스 지분가치와 연결된다. "
                    "SK스퀘어 포트폴리오 실적 개선과 자회사 가치가 부각됐다."
                )
            },
        )

        result = runner.run(WebResearchInput("SK스퀘어", "402340", "holding", Market.KR, date(2026, 6, 8)))

        self.assertEqual(len(result.parsed_news), 1)
        self.assertIn("지분가치", result.parsed_news[0].body)

    def test_market_disclosure_roundup_peer_contract_is_not_target_disclosure(self):
        url = "https://news.example.com/disclosure-roundup"
        text = """
        [주요공시] 대한항공, 태광산업, 테스트렌탈, 방산기업 외
        대한항공은 공급계약 계약금액을 공시했다.
        테스트렌탈은 자사주 소각과 렌탈 사업 수익성 개선을 밝혔다.
        방산기업은 KF-21 정부 수출 계약을 발표했다.
        """
        runner = _runner(
            {
                "테스트렌탈 단일판매 공급계약": (
                    SearchResult(
                        title="[주요공시] 대한항공, 태광산업, 테스트렌탈, 방산기업 외",
                        url=url,
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트렌탈 단일판매 공급계약",
                        rank=1,
                        is_news=True,
                        confidence=0.8,
                    ),
                )
            },
            {url: text},
        )

        result = runner.run(WebResearchInput("테스트렌탈", "001740", "렌탈 투자회사", Market.KR, date(2026, 6, 8)))

        self.assertEqual(result.parsed_disclosures, ())
        self.assertEqual(len(result.parsed_news), 1)
        self.assertNotIn("방산기업", result.parsed_news[0].body)
        self.assertNotIn("대한항공은 공급계약", result.parsed_news[0].body)
        self.assertFalse(result.parsed_news[0].parsed_fields.get("government_customer"))

    def test_market_disclosure_roundup_target_contract_can_remain_disclosure(self):
        url = "https://news.example.com/disclosure-roundup-target"
        text = """
        [주요공시] 여러 회사
        테스트전력은 단일판매 공급계약을 체결했다. 계약금액 500억원 계약상대방 북미 전력망 고객.
        다른회사는 방산 수출 계약을 발표했다.
        """
        runner = _runner(
            {
                "테스트전력 단일판매 공급계약": (
                    SearchResult(
                        title="[주요공시] 테스트전력 외",
                        url=url,
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트전력 단일판매 공급계약",
                        rank=1,
                        is_news=True,
                        confidence=0.8,
                    ),
                )
            },
            {url: text},
        )

        result = runner.run(WebResearchInput("테스트전력", "267260", "power_equipment", Market.KR, date(2026, 6, 8)))

        self.assertEqual(len(result.parsed_disclosures), 1)
        self.assertIn("테스트전력은 단일판매 공급계약", result.parsed_disclosures[0].raw_text)
        self.assertNotIn("다른회사는 방산", result.parsed_disclosures[0].raw_text)

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


class _SingleQueryPlanner:
    def __init__(self, query: str) -> None:
        self.query = query

    def plan(self, company_name, symbol, sector, market, as_of_date, stage_context=None):
        return QueryPlan(
            company_name=company_name,
            symbol=symbol,
            sector=sector,
            market=market,
            as_of_date=as_of_date,
            queries=(
                QuerySpec(
                    group="deep_research",
                    query=self.query,
                    priority=1,
                    company_name=company_name,
                    symbol=symbol,
                    sector=sector,
                    market=market,
                    as_of_date=as_of_date,
                ),
            ),
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


class _FakePDFExtractor:
    def __init__(self, text: str) -> None:
        self.text = text
        self.payload_count = 0

    def extract_text_from_bytes(self, payload: bytes) -> PDFTextExtractionResult:
        self.payload_count += 1
        return PDFTextExtractionResult(ok=True, text=self.text, extractor="fake")


if __name__ == "__main__":
    unittest.main()
