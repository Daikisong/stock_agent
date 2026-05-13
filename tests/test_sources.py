from datetime import date
from pathlib import Path
import unittest

from e2r.models import Market, SourceTier
from e2r.sources import (
    COMPANY_NEWS_QUERY_TEMPLATES,
    ConsensusCSVConnector,
    KRXConnector,
    MissingCredentialError,
    NaverNewsConnector,
    OpenDARTConnector,
    ReportSearchConnector,
    SECEdgarConnector,
)
from e2r.sources.report_search import is_recognized_report_domain


ROOT = Path(__file__).resolve().parents[1]


class SourceConnectorTests(unittest.TestCase):
    def test_krx_fixture_connector_filters_instruments_and_prices_as_of_date(self):
        connector = KRXConnector(fixture_root=ROOT / "data/raw/krx")

        instruments = connector.list_instruments(Market.KR, date(2023, 7, 27))
        bars = connector.get_price_bars("267260", date(2023, 7, 1), date(2023, 7, 31), date(2023, 7, 26))
        low_52w, high_52w = connector.get_52_week_range("267260", date(2023, 7, 27))

        self.assertTrue(any(item.symbol == "267260" for item in instruments))
        self.assertEqual([bar.date for bar in bars], [date(2023, 7, 26)])
        self.assertEqual(low_52w, 66000)
        self.assertEqual(high_52w, 72000)

    def test_opendart_normalizes_contract_fields_without_inventing_missing_values(self):
        connector = OpenDARTConnector(fixture_root=ROOT / "data/raw/opendart")

        disclosures = connector.get_disclosures("103590", date(2023, 11, 1), date(2023, 11, 30), date(2023, 11, 27))
        evidence = connector.to_evidence(disclosures[0])

        fields = disclosures[0].parsed_fields
        self.assertAlmostEqual(fields["contract_amount_to_prior_sales"], 0.3707)
        self.assertEqual(fields["contract_duration_months"], 60)
        self.assertEqual(fields["counterparty"], "미국 에너지 회사 계약내용: 초고압 변압기 공급 계약기간 2026.01.01 ~ 2030.12.31 선수금 조건 수주잔고 반영")
        self.assertTrue(fields["prepayment_exists"])
        self.assertTrue(fields["backlog_mentioned"])
        self.assertNotIn("is_cancellable", fields)
        self.assertEqual(evidence.source_tier, SourceTier.TIER_0)

    def test_live_connectors_report_missing_credentials_clearly(self):
        with self.assertRaises(MissingCredentialError):
            OpenDARTConnector(api_key=None).require_live_credentials()
        with self.assertRaises(MissingCredentialError):
            NaverNewsConnector(client_id=None, client_secret=None).require_live_credentials()

    def test_naver_news_templates_and_event_normalization(self):
        connector = NaverNewsConnector(fixture_root=ROOT / "data/raw/naver_news")

        requests = connector.build_company_search_requests("HD현대일렉트릭", date(2023, 7, 27))
        news = connector.get_news("267260", date(2023, 7, 1), date(2023, 7, 31), date(2023, 7, 27))

        self.assertEqual(len(requests), len(COMPANY_NEWS_QUERY_TEMPLATES))
        self.assertIn("수주잔고", requests[0].params["query"])
        self.assertEqual(news[0].parsed_fields["event_type"], "backlog")
        self.assertIn("판가", news[0].parsed_fields["asp_comment"])

    def test_report_search_recognizes_broker_pdf_domains(self):
        connector = ReportSearchConnector(fixture_root=ROOT / "data/raw/report_search")

        results = connector.search_reports("HD현대일렉트릭", date(2023, 7, 27))

        self.assertTrue(results[0].is_pdf)
        self.assertTrue(results[0].is_recognized_report_domain)
        self.assertTrue(is_recognized_report_domain(results[0].url))

    def test_sec_companyfacts_fixture_maps_to_financial_actual(self):
        connector = SECEdgarConnector(fixture_root=ROOT / "data/raw/sec_edgar")

        actuals = connector.get_financial_actuals("NVDA", date(2023, 5, 25))

        self.assertEqual(len(actuals), 1)
        self.assertEqual(actuals[0].sales, 26974000000)
        self.assertEqual(actuals[0].fcf, 3808000000)

    def test_consensus_csv_connector_loads_fcf_and_street_revision_fields(self):
        connector = ConsensusCSVConnector(fixture_root=ROOT / "data/raw/consensus")

        consensus = connector.get_consensus("267260", date(2023, 7, 27))
        revisions = connector.get_consensus_revisions("267260", date(2023, 7, 27))

        self.assertEqual(consensus[0].fcf_e, 430000)
        self.assertEqual(revisions[0].street_high_eps_revision_1m, 40)
        self.assertEqual(revisions[0].street_low_eps_revision_1m, 20)


if __name__ == "__main__":
    unittest.main()
