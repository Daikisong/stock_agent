from datetime import date
import unittest

from e2r.models import ResearchReport
from e2r.research.report_consensus_proxy import build_report_consensus_proxy
from e2r.research.report_parser import parse_research_report_text


class ReportConsensusProxyTests(unittest.TestCase):
    def test_creates_consensus_and_revision_from_explicit_report_fields(self):
        report = ResearchReport(
            symbol="267260",
            publish_date=date(2023, 7, 27),
            broker="broker",
            title="HD현대일렉트릭 Review",
            as_of_date=date(2023, 8, 1),
            target_price=110000,
            target_revision_pct=37,
            fy1_sales=27000,
            fy1_op=3100,
            fy1_eps=6200,
            fy2_sales=33000,
            fy2_op=4700,
            fy2_eps=9300,
            est_per=9,
            est_pbr=2.2,
        )

        result = build_report_consensus_proxy((report,), as_of_date=date(2023, 8, 1))

        self.assertEqual(len(result.consensus), 2)
        self.assertEqual(result.consensus[0].sales_e, 27000)
        self.assertEqual(result.consensus[1].fiscal_year, 2024)
        self.assertEqual(len(result.consensus_revisions), 1)
        self.assertEqual(result.consensus_revisions[0].target_price_revision_1m, 37)
        self.assertTrue(result.reports[0].parsed_fields["consensus_proxy_created"])

    def test_does_not_create_revision_from_missing_fields(self):
        report = ResearchReport(
            symbol="298040",
            publish_date=date(2023, 5, 15),
            broker="broker",
            title="효성중공업 Review",
            as_of_date=date(2023, 5, 15),
            parsed_fields={},
        )

        result = build_report_consensus_proxy((report,))

        self.assertFalse(result.consensus)
        self.assertFalse(result.consensus_revisions)
        self.assertNotIn("consensus_proxy_created", result.reports[0].parsed_fields)

    def test_non_finite_report_numbers_do_not_create_proxy_rows(self):
        report = ResearchReport(
            symbol="298040",
            publish_date=date(2023, 5, 15),
            broker="broker",
            title="효성중공업 Review",
            as_of_date=date(2023, 5, 15),
            fy1_op=float("nan"),
            fy1_eps=float("inf"),
            parsed_fields={
                "target_price_revision_pct": "nan",
                "parser_confidence": "nan",
                "source_url": "https://example.com/report.pdf",
            },
            raw_text="충분한 길이의 원문 " * 20,
        )

        result = build_report_consensus_proxy((report,))

        self.assertFalse(result.consensus)
        self.assertFalse(result.consensus_revisions)
        self.assertNotIn("consensus_proxy_created", result.reports[0].parsed_fields)

    def test_parsed_forward_estimate_report_creates_consensus_not_actuals(self):
        parsed = parse_research_report_text(
            symbol="123456",
            text="테스트전자 종목분석 - 2026년 영업이익 70조원 예상. 실적 전망치 상향.",
            metadata={"publish_date": date(2026, 6, 8), "as_of_date": date(2026, 6, 8)},
        )

        result = build_report_consensus_proxy((parsed.report,), as_of_date=date(2026, 6, 8))

        self.assertEqual(len(result.consensus), 1)
        self.assertEqual(result.consensus[0].fiscal_year, 2026)
        self.assertEqual(result.consensus[0].op_e, 70_000_000_000_000.0)
        self.assertFalse(result.consensus_revisions)
        self.assertTrue(result.reports[0].parsed_fields["consensus_proxy_created"])
        self.assertNotIn("actual_operating_profit", result.reports[0].parsed_fields)

    def test_target_price_only_report_creates_consensus_without_revision_pct(self):
        parsed = parse_research_report_text(
            symbol="123456",
            text="테스트전자 목표주가 87만원으로 상향. AI 수요를 반영했다.",
            metadata={"publish_date": date(2026, 6, 8), "as_of_date": date(2026, 6, 8)},
        )

        result = build_report_consensus_proxy((parsed.report,), as_of_date=date(2026, 6, 8))

        self.assertEqual(len(result.consensus), 1)
        self.assertEqual(result.consensus[0].target_price, 870000)
        self.assertFalse(result.consensus_revisions)
        self.assertTrue(result.reports[0].parsed_fields["target_price_upgrade_mentioned"])

    def test_power_equipment_forward_estimate_creates_consensus_proxy(self):
        parsed = parse_research_report_text(
            symbol="654321",
            text=(
                "테스트전력 종목분석 - 2027년 영업이익 2,400억원 전망. "
                "목표주가 12만원으로 상향. 북미 변압기 수주잔고와 리드타임 장기화."
            ),
            metadata={"publish_date": date(2026, 6, 8), "as_of_date": date(2026, 6, 8)},
        )

        result = build_report_consensus_proxy((parsed.report,), as_of_date=date(2026, 6, 8))

        self.assertEqual(len(result.consensus), 1)
        self.assertEqual(result.consensus[0].fiscal_year, 2027)
        self.assertEqual(result.consensus[0].op_e, 240_000_000_000.0)
        self.assertEqual(result.consensus[0].target_price, 120000)
        self.assertFalse(result.consensus_revisions)
        self.assertTrue(result.reports[0].parsed_fields["consensus_proxy_created"])
        self.assertNotIn("hbm_context_mentioned", result.reports[0].parsed_fields)


if __name__ == "__main__":
    unittest.main()
