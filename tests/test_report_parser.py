from datetime import date
from pathlib import Path
import unittest

from e2r.models import Market
from e2r.research.report_parser import parse_research_report_file, parse_research_report_text


ROOT = Path(__file__).resolve().parents[1]


class ResearchReportParserTests(unittest.TestCase):
    def test_korean_report_fixture_extracts_numeric_and_keyword_fields(self):
        result = parse_research_report_file(
            ROOT / "tests/fixtures/reports/hd_hyundai_electric_2023_07_27.txt",
            symbol="267260",
            market=Market.KR,
        )

        report = result.report
        fields = result.parsed_fields

        self.assertEqual(report.publish_date, date(2023, 7, 27))
        self.assertEqual(report.broker, "HistoricalBroker")
        self.assertEqual(report.analyst, "Fixture Analyst")
        self.assertEqual(report.current_price, 69600)
        self.assertEqual(report.target_price, 95000)
        self.assertEqual(report.target_revision_pct, 25)
        self.assertEqual(report.fy1_op, 620000)
        self.assertEqual(report.fy2_eps, 15800)
        self.assertEqual(report.est_per, 6.3)
        self.assertEqual(report.order_backlog_to_sales, 155)
        self.assertEqual(report.capa_increase_pct, 35)
        self.assertTrue(report.asp_increase_mentioned)
        self.assertTrue(report.lead_time_mentioned)
        self.assertTrue(report.shortage_mentioned)
        self.assertIn("수주잔고 확대", report.investment_points)
        self.assertEqual(result.evidence.source_type, "research_report")
        self.assertGreater(fields["parser_confidence"], 0.7)

    def test_qualitative_sector_fields_are_extracted_without_numeric_fabrication(self):
        text = """2024.05.16
제목: 삼양식품 Review
불닭 수출 비중 확대와 해외 채널 확장으로 반복 수요가 확인된다.
ASP 상승과 고마진 믹스 개선으로 OPM 개선이 이어진다.
"""
        result = parse_research_report_text(
            symbol="003230",
            market=Market.KR,
            text=text,
            metadata={"publish_date": date(2024, 5, 16), "as_of_date": date(2024, 5, 16)},
        )
        fields = result.parsed_fields

        self.assertTrue(fields["export_channel_expansion"])
        self.assertTrue(fields["overseas_channel_expansion"])
        self.assertTrue(fields["recurring_consumer_demand"])
        self.assertTrue(fields["pricing_power_mentioned"])
        self.assertNotIn("export_growth_pct", fields)

    def test_memory_qualitative_fields_are_extracted(self):
        text = """2024.04.01
제목: 삼성전자 메모리 리레이팅
HBM 수요 증가와 메모리 가격 상승, 공급조절이 확인된다.
"""
        result = parse_research_report_text(
            symbol="005930",
            market=Market.KR,
            text=text,
            metadata={"publish_date": date(2024, 4, 1), "as_of_date": date(2024, 4, 1)},
        )
        fields = result.parsed_fields

        self.assertTrue(fields["hbm_demand_mentioned"])
        self.assertTrue(fields["memory_price_increase_mentioned"])
        self.assertTrue(fields["supply_discipline_mentioned"])

    def test_hbm_sold_out_capacity_and_customer_allocation_are_generic_fields(self):
        text = """2026.06.09
제목: CASE HBM 공급 가시성
HBM 수요 폭증으로 고객 수요 대비 공급 충족률이 역대 최저 수준이다.
HBM4는 전량 판매됐고 중장기 물량 확보 요청과 장기공급계약 논의가 이어진다.
평균판매가격과 HBM 가격 상승도 확인된다.
"""
        result = parse_research_report_text(
            symbol="CASE",
            market=Market.KR,
            text=text,
            metadata={"publish_date": date(2026, 6, 9), "as_of_date": date(2026, 6, 9)},
        )
        fields = result.parsed_fields

        self.assertTrue(fields["hbm_context_mentioned"])
        self.assertTrue(fields["hbm_demand_mentioned"])
        self.assertTrue(fields["customer_preorder_or_allocation"])
        self.assertTrue(fields["capacity_precommitted"])
        self.assertTrue(fields["hbm_capacity_pre_sold"])
        self.assertTrue(fields["hbm_capacity_constraint"])
        self.assertTrue(fields["memory_price_increase_mentioned"])
        self.assertTrue(fields["revenue_visibility_contract"])

    def test_one_off_cost_reduction_is_not_one_off_shortage(self):
        text = """2026.06.09
제목: 삼성전자 HBM Review
HBM 수요 증가와 메모리 가격 상승이 확인되고, 전 분기 재고 관련 일회성 비용 감소로 영업이익이 개선됐다.
"""
        result = parse_research_report_text(
            symbol="005930",
            market=Market.KR,
            text=text,
            metadata={"publish_date": date(2026, 6, 9), "as_of_date": date(2026, 6, 9)},
        )
        fields = result.parsed_fields

        self.assertTrue(fields["hbm_demand_mentioned"])
        self.assertTrue(fields["memory_price_increase_mentioned"])
        self.assertNotIn("shortage_type", fields)
        self.assertNotIn("one_off_shortage", fields)
        self.assertNotIn("one_off_shortage_risk", fields)

    def test_forward_estimate_in_title_and_snippet_becomes_report_estimate_not_actual(self):
        result = parse_research_report_text(
            symbol="123456",
            market=Market.KR,
            text="본문에는 HBM 수요 증가와 실적 전망치 상향이 핵심이라고만 적혀 있다.",
            metadata={
                "title": "테스트전자 종목분석 - 2Q26 영업이익 70조원 예상",
                "snippet": "목표주가 87만원으로 상향. AI 수요와 공급 제약이 배경이다.",
                "publish_date": date(2026, 6, 8),
                "as_of_date": date(2026, 6, 8),
            },
        )

        report = result.report
        fields = result.parsed_fields

        self.assertEqual(report.fy1_op, 70_000_000_000_000.0)
        self.assertEqual(fields["fy1_fiscal_year"], 2026)
        self.assertEqual(report.target_price, 870000)
        self.assertTrue(fields["forward_estimate_present"])
        self.assertTrue(fields["estimate_upgrade_mentioned"])
        self.assertTrue(fields["target_price_upgrade_mentioned"])
        self.assertNotIn("actual_operating_profit", fields)
        self.assertNotIn("financial_actuals_from_text", fields)

    def test_forward_estimate_parser_is_not_semiconductor_specific(self):
        result = parse_research_report_text(
            symbol="654321",
            market=Market.KR,
            text="북미 전력망 투자와 변압기 리드타임 장기화로 수주잔고가 늘고 있다.",
            metadata={
                "title": "테스트전력 종목분석 - 2027년 영업이익 2,400억원 전망",
                "snippet": "목표주가 12만원으로 상향. 전력기기 수주잔고와 북미 매출 가시성 반영.",
                "publish_date": date(2026, 6, 8),
                "as_of_date": date(2026, 6, 8),
            },
        )

        report = result.report
        fields = result.parsed_fields

        self.assertEqual(report.fy1_op, 240_000_000_000.0)
        self.assertEqual(fields["fy1_fiscal_year"], 2027)
        self.assertEqual(report.target_price, 120000)
        self.assertTrue(fields["forward_estimate_present"])
        self.assertTrue(fields["target_price_upgrade_mentioned"])
        self.assertNotIn("hbm_context_mentioned", fields)
        self.assertNotIn("actual_operating_profit", fields)
        self.assertNotIn("financial_actuals_from_text", fields)

    def test_consumer_forward_estimates_parse_without_theme_tokens(self):
        result = parse_research_report_text(
            symbol="888888",
            market=Market.KR,
            text="해외 채널 확대와 반복 수요가 이어지고 고마진 믹스 개선이 예상된다.",
            metadata={
                "title": "테스트소비재 종목분석 - 2026년 매출 3조원 예상, 영업이익 4,800억원 예상",
                "snippet": "EPS 12,500원 추정. 목표주가 18만원으로 상향.",
                "publish_date": date(2026, 6, 8),
                "as_of_date": date(2026, 6, 8),
            },
        )

        report = result.report
        fields = result.parsed_fields

        self.assertEqual(report.fy1_sales, 3_000_000_000_000.0)
        self.assertEqual(report.fy1_op, 480_000_000_000.0)
        self.assertEqual(report.fy1_eps, 12500)
        self.assertEqual(report.target_price, 180000)
        self.assertTrue(fields["forward_estimate_present"])
        self.assertTrue(fields["overseas_channel_expansion"])
        self.assertTrue(fields["recurring_consumer_demand"])
        self.assertNotIn("hbm_context_mentioned", fields)
        self.assertNotIn("financial_actuals_from_text", fields)

    def test_consensus_beat_actual_language_is_not_forward_estimate(self):
        result = parse_research_report_text(
            symbol="777777",
            market=Market.KR,
            text="테스트소비재는 2026년 1분기 영업이익 1,200억원으로 컨센서스를 상회했다.",
            metadata={"publish_date": date(2026, 6, 8), "as_of_date": date(2026, 6, 8)},
        )

        fields = result.parsed_fields

        self.assertNotIn("forward_estimate_present", fields)
        self.assertNotIn("fy1_op", fields)
        self.assertNotIn("forward_op_estimate", fields)

    def test_invalid_negative_target_price_is_dropped_instead_of_crashing(self):
        result = parse_research_report_text(
            symbol="999999",
            market=Market.KR,
            text="목표주가 -3% 변동이라는 잘못된 스니펫이 섞였지만 HBM 수요 증가가 언급된다.",
            metadata={"publish_date": date(2026, 6, 8), "as_of_date": date(2026, 6, 8)},
        )

        self.assertIsNone(result.report.target_price)
        self.assertIn("target_price", result.parsed_fields["invalid_non_negative_fields"])

    def test_invalid_negative_target_price_metadata_is_dropped(self):
        result = parse_research_report_text(
            symbol="999998",
            market=Market.KR,
            text="목표주가 수치는 본문에 없다.",
            metadata={
                "publish_date": date(2026, 6, 8),
                "as_of_date": date(2026, 6, 8),
                "target_price": -1000,
            },
        )

        self.assertIsNone(result.report.target_price)
        self.assertIn("target_price", result.parsed_fields["invalid_non_negative_fields"])


if __name__ == "__main__":
    unittest.main()
