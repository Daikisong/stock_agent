from datetime import date
from pathlib import Path
import unittest

from e2r.models import Market
from e2r.research.report_parser import parse_research_report_file


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


if __name__ == "__main__":
    unittest.main()
