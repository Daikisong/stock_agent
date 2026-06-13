from datetime import date
import io
from pathlib import Path
import unittest
import zipfile

from e2r.models import Market, SourceTier
from e2r.sources import (
    COMPANY_NEWS_QUERY_TEMPLATES,
    CompanyGuideConnector,
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

    def test_opendart_parses_corp_code_zip_by_stock_code(self):
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w") as archive:
            archive.writestr(
                "CORPCODE.xml",
                "\n".join(
                    (
                        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>",
                        "<result>",
                        "  <list>",
                        "    <corp_code>00126380</corp_code>",
                        "    <corp_name>삼성전자</corp_name>",
                        "    <stock_code>005930</stock_code>",
                        "    <modify_date>20240501</modify_date>",
                        "  </list>",
                        "  <list>",
                        "    <corp_code>00164779</corp_code>",
                        "    <corp_name>SK하이닉스</corp_name>",
                        "    <stock_code>000660</stock_code>",
                        "    <modify_date>20240501</modify_date>",
                        "  </list>",
                        "</result>",
                    )
                ).encode("utf-8"),
            )

        mapping = OpenDARTConnector.company_codes_by_stock_code(buffer.getvalue())

        self.assertEqual(mapping["005930"], "00126380")
        self.assertEqual(mapping["000660"], "00164779")

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

    def test_company_guide_parses_samsung_and_hynix_consensus_snapshot(self):
        connector = CompanyGuideConnector()
        as_of = date(2026, 6, 11)

        samsung = connector.parse_consensus_snapshot_html(
            _company_guide_consensus_html(
                opinion="4.04",
                target_price="437,500",
                eps="43,833",
                per="6.90",
                analyst_count="24",
                broker_rows=(
                    ("KB", "26/06/10", "530,000", "530,000", "0.00", "BUY", "BUY"),
                    ("현대차", "26/06/10", "440,000", "340,000", "29.41", "BUY", "BUY"),
                ),
            ),
            symbol="005930",
            as_of_date=as_of,
        )
        hynix = connector.parse_consensus_snapshot_html(
            _company_guide_consensus_html(
                opinion="4.00",
                target_price="2,751,667",
                eps="301,732",
                per="6.79",
                analyst_count="24",
                broker_rows=(
                    ("메리츠", "26/06/10", "2,950,000", "2,000,000", "47.50", "Buy", "Buy"),
                    ("신한투자", "26/06/09", "3,800,000", "3,800,000", "0.00", "매수", "매수"),
                ),
            ),
            symbol="000660",
            as_of_date=as_of,
        )

        self.assertEqual(samsung.consensus.target_price, 437500)
        self.assertEqual(samsung.consensus.eps_e, 43833)
        self.assertEqual(samsung.consensus.analyst_count, 24)
        self.assertEqual(samsung.broker_targets[1].broker, "현대차")
        self.assertEqual(samsung.broker_targets[1].target_price_revision_pct, 29.41)

        self.assertEqual(hynix.consensus.target_price, 2751667)
        self.assertEqual(hynix.consensus.eps_e, 301732)
        self.assertEqual(hynix.consensus.per_e, 6.79)
        self.assertEqual(hynix.broker_targets[0].target_price, 2950000)
        self.assertEqual(hynix.broker_targets[0].target_price_revision_pct, 47.50)

    def test_company_guide_recent_report_payloads_normalize_for_samsung_and_hynix(self):
        connector = CompanyGuideConnector()
        as_of = date(2026, 6, 11)

        samsung = connector.parse_recent_reports_payload(
            {
                "lists": [
                    {
                        "RPT_ID": 1104820,
                        "ANL_DT": "26/06/11",
                        "IDX": "20260611.046265",
                        "RPT_TITLE": "사이클을 넘어 구조적 확장으로, 역대급 레벨업의 시작",
                        "TARGET_PRC": "",
                        "RECOMM": None,
                        "COMMENT": "HBM 출하량 3배 급증<br/>선수주 후증설 패러다임 변화",
                        "PAGE_CNT": 5,
                        "FILE_NM": "1F18420260611_005930_a.pdf",
                        "CLOSE_PRC": "299,000",
                        "EPS": None,
                        "BRK_NM_SHORT_KOR": "스터닝밸류리서치",
                        "ANL_NM_KOR": "전영대",
                        "PRC_ACTION_TYP_NM": "목표주가 없음",
                        "EPS_ACTION_TYP_NM": "추정EPS 없음",
                        "RECOMM_ACTION_TYP_NM": "투자의견 없음",
                    },
                    {
                        "RPT_ID": 1104600,
                        "ANL_DT": "26/06/10",
                        "IDX": "20260610.046168",
                        "RPT_TITLE": "어닝파워 입증 및 주주환원을 통한 재평가 예상",
                        "TARGET_PRC": "420,000",
                        "RECOMM": "Buy",
                        "COMMENT": "메모리 선두업체<br/>투자의견 Buy, 적정주가 42만원",
                        "PAGE_CNT": 5,
                        "FILE_NM": "1F02220260610_005930.pdf",
                        "CLOSE_PRC": "299,000",
                        "EPS": 48448.0,
                        "BRK_NM_SHORT_KOR": "메리츠",
                        "ANL_NM_KOR": "김선우",
                        "PRC_ACTION_TYP_NM": "목표주가 상향",
                        "EPS_ACTION_TYP_NM": "추정EPS 상향",
                        "RECOMM_ACTION_TYP_NM": "변동없음",
                    },
                    {
                        "RPT_ID": 9999999,
                        "ANL_DT": "26/06/12",
                        "RPT_TITLE": "미래 날짜 리포트",
                    },
                ]
            },
            symbol="005930",
            as_of_date=as_of,
        )
        hynix = connector.parse_recent_reports_payload(
            {
                "lists": [
                    {
                        "RPT_ID": 1104601,
                        "ANL_DT": "26/06/10",
                        "IDX": "20260610.046169",
                        "RPT_TITLE": "끝 없는 재평가 (feat. ADR, 주주환원)",
                        "TARGET_PRC": "2,950,000",
                        "RECOMM": "Buy",
                        "COMMENT": "업사이클의 최대 Pure Player<br/>27년 초거대 주주환원",
                        "PAGE_CNT": 5,
                        "FILE_NM": "1F02220260610_000660.pdf",
                        "CLOSE_PRC": "2,101,000",
                        "EPS": 325071.0,
                        "BRK_NM_SHORT_KOR": "메리츠",
                        "ANL_NM_KOR": "김선우",
                        "PRC_ACTION_TYP_NM": "목표주가 상향",
                        "EPS_ACTION_TYP_NM": "추정EPS 상향",
                        "RECOMM_ACTION_TYP_NM": "변동없음",
                    },
                    {
                        "RPT_ID": 1104231,
                        "ANL_DT": "26/06/09",
                        "IDX": "20260609.045867",
                        "RPT_TITLE": "(깐부)치킨게임 시작",
                        "TARGET_PRC": "3,800,000",
                        "RECOMM": "매수",
                        "COMMENT": "본격적인 장기공급계약 체결 시작<br/>27년 HBM 수요 확대와 고객 다변화",
                        "PAGE_CNT": 10,
                        "FILE_NM": "1F01420260609_000660_c.pdf",
                        "CLOSE_PRC": "2,101,000",
                        "EPS": 329372.0,
                        "BRK_NM_SHORT_KOR": "미래에셋",
                        "ANL_NM_KOR": "김영건",
                        "PRC_ACTION_TYP_NM": "변동없음",
                        "EPS_ACTION_TYP_NM": "추정EPS 상향",
                        "RECOMM_ACTION_TYP_NM": "변동없음",
                    },
                ]
            },
            symbol="000660",
            as_of_date=as_of,
        )

        self.assertEqual(len(samsung), 2)
        self.assertEqual(samsung[1].target_price, 420000)
        self.assertEqual(samsung[1].fy1_eps, 48448)
        self.assertEqual(samsung[1].parsed_fields["target_price_action"], "목표주가 상향")

        self.assertEqual(hynix[0].target_price, 2950000)
        self.assertEqual(hynix[0].fy1_eps, 325071)
        self.assertEqual(hynix[1].broker, "미래에셋")
        self.assertIn("장기공급계약", hynix[1].raw_text or "")

    def test_company_guide_request_metadata_stays_fixture_first(self):
        connector = CompanyGuideConnector()

        snapshot = connector.build_snapshot_request("005930", date(2026, 6, 11))
        reports = connector.build_recent_reports_request("000660", date(2026, 6, 11), per_page=3, cur_page=1)

        self.assertTrue(snapshot.fixture_mode)
        self.assertEqual(snapshot.params["cmp_cd"], "005930")
        self.assertEqual(reports.url, "https://comp.wisereport.co.kr/company/ajax/c1080001_data.aspx")
        self.assertEqual(reports.params["cmp_cd"], "000660")
        self.assertEqual(reports.params["perPage"], 3)


def _company_guide_consensus_html(
    *,
    opinion: str,
    target_price: str,
    eps: str,
    per: str,
    analyst_count: str,
    broker_rows: tuple[tuple[str, str, str, str, str, str, str], ...],
) -> str:
    broker_html = "\n".join(
        f"""
        <tr>
          <td>{broker}</td><td>{final_date}</td><td>{target}</td><td>{previous_target}</td>
          <td><span>{revision}</span></td><td>{rating}</td><td>{previous_rating}</td>
        </tr>
        """
        for broker, final_date, target, previous_target, revision, rating, previous_rating in broker_rows
    )
    return f"""
    <p class="disc table">[기준:2026.06.10]</p>
    <table id="cTB15">
      <tr>
        <td rowspan="2"><span>{opinion}</span></td>
        <th>투자의견</th><th>목표주가<span>(원)</span></th><th>EPS<span>(원)</span></th>
        <th>PER<span>(배)</span></th><th>추정기관수</th>
      </tr>
      <tr>
        <td><b>{opinion}</b></td><td>{target_price}</td><td>{eps}</td><td>{per}</td><td>{analyst_count}</td>
      </tr>
    </table>
    <table id="cTB24">
      <thead>
        <tr><th>제공처</th><th>최종일자</th><th>목표가</th><th>직전목표가</th><th>변동률<span>(%)</span></th><th>투자의견</th><th>직전투자의견</th></tr>
      </thead>
      <tbody>{broker_html}</tbody>
    </table>
    """


if __name__ == "__main__":
    unittest.main()
