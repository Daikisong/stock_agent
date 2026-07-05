from datetime import date
import io
from pathlib import Path
import tempfile
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
from e2r.sources.opendart import extract_document_text, parse_disclosure_text
from e2r.sources.report_search import is_recognized_report_domain, is_verified_report_original_url


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

    def test_opendart_parses_table_style_contract_fields(self):
        raw_text = """
        그린생명과학/단일판매ㆍ공급계약체결/(2026.06.30)
        단일판매ㆍ공급계약체결
        2. 계약내역
        확정 계약금액
        10,238,670,000
        조건부 계약금액
        -
        계약금액 총액(원)
        10,238,670,000
        최근 매출액(원)
        24,860,636,227
        매출액 대비(%)
        41.18
        3. 계약상대방
        UPL Limited
        - 최근 매출액(원)
        7,653,624,000,000
        5. 계약기간
        시작일
        2025-11-17
        종료일
        2026-06-30
        """

        fields = parse_disclosure_text(raw_text, title="[기재정정]단일판매ㆍ공급계약체결")

        self.assertEqual(fields["contract_amount"], 10238670000.0)
        self.assertAlmostEqual(fields["contract_amount_to_prior_sales"], 0.4118)
        self.assertEqual(fields["contract_start"], "2025-11-17")
        self.assertEqual(fields["contract_end"], "2026-06-30")
        self.assertEqual(fields["contract_duration_months"], 8)
        self.assertEqual(fields["counterparty"], "UPL Limited")

    def test_opendart_parses_joined_sales_ratio_label_from_dart_contract_table(self):
        raw_text = """
        삼부토건/단일판매ㆍ공급계약체결/(2026.06.30)
        단일판매ㆍ공급계약 체결
        2. 계약내역
        계약금액(원)
        96,591,000,000
        최근매출액(원)
        280,423,782,241
        매출액대비(%)
        34.44
        5. 계약기간
        시작일
        2018-05-09
        종료일
        2026-06-30
        """

        fields = parse_disclosure_text(raw_text, title="[기재정정]단일판매ㆍ공급계약체결")

        self.assertEqual(fields["contract_amount"], 96591000000.0)
        self.assertAlmostEqual(fields["contract_amount_to_prior_sales"], 0.3444)
        self.assertEqual(fields["contract_duration_months"], 98)

    def test_opendart_uses_current_contract_body_not_correction_table_numbers(self):
        raw_text = """
        대우건설/단일판매ㆍ공급계약체결/(2026.06.25)
        정정신고(보고)
        4. 정정사항
        정정항목
        정정전
        정정후
        2. 계약내역 - 계약금액(원)
        - 매출액대비(%)
        240,893,290,000
        2.77
        523,270,000,000
        6.02
        5. 계약기간
        - 시작일
        - 종료일
        -
        -
        2025-04-15
        2029-04-30
        단일판매ㆍ공급계약 체결
        1. 판매ㆍ공급계약 구분
        공사수주
        2. 계약내역
        계약금액(원)
        523,270,000,000
        최근매출액(원)
        8,690,740,000,000
        매출액대비(%)
        6.02
        5. 계약기간
        시작일
        2025-04-15
        종료일
        2029-04-30
        """

        fields = parse_disclosure_text(raw_text, title="[기재정정]단일판매ㆍ공급계약체결")

        self.assertEqual(fields["contract_amount"], 523270000000.0)
        self.assertAlmostEqual(fields["contract_amount_to_prior_sales"], 0.0602)
        self.assertEqual(fields["contract_start"], "2025-04-15")
        self.assertEqual(fields["contract_end"], "2029-04-30")
        self.assertEqual(fields["contract_duration_months"], 49)

    def test_opendart_does_not_score_truncated_correction_table_without_current_body(self):
        raw_text = """
        대우건설/단일판매ㆍ공급계약체결/(2026.06.25)
        정정신고(보고)
        4. 정정사항
        정정항목
        정정전
        정정후
        2. 계약내역 - 계약금액(원)
        - 매출액대비(%)
        240,893,290,000
        2.77
        523,270,000,000
        6.02
        """

        fields = parse_disclosure_text(raw_text, title="[기재정정]단일판매ㆍ공급계약체결")

        self.assertNotIn("contract_amount", fields)
        self.assertNotIn("contract_amount_to_prior_sales", fields)

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

    def test_opendart_extract_document_text_strips_css_noise(self):
        raw = """
        <DOCUMENT>
          <style>.xforms * { font-family: 돋움체; font-size: 10px; }</style>
          <SECTION-1>
            <P>신규시설투자</P>
            <P>투자금액: 1,200억원</P>
            <P>완공예정일: 2027.12.31</P>
          </SECTION-1>
        </DOCUMENT>
        """

        text = extract_document_text(raw)

        self.assertNotIn("font-family", text)
        self.assertIn("투자금액", text)
        self.assertIn("완공예정일", text)

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
        self.assertTrue(is_verified_report_original_url(results[0].url))
        self.assertTrue(
            is_verified_report_original_url(
                "https://www.samsungpop.com/common.do?cmd=down&contentType=application/pdf"
                "&saveKey=research.pdf&fileName=2010/2025102917550025K_02_03.pdf"
            )
        )
        self.assertTrue(
            is_verified_report_original_url(
                "https://file.hanaw.com/download/research/FileServer/WEB/info/daily/2026/06/07/Daily_260608.pdf"
            )
        )
        self.assertTrue(
            is_verified_report_original_url(
                "https://stock.pstatic.net/stock-research/company/38/20250731_company_685270000.pdf",
                title="SK Hynix customer allocation report",
            )
        )
        self.assertFalse(is_verified_report_original_url("https://www.samsungpop.com/customer/event_terms.pdf"))
        self.assertFalse(is_verified_report_original_url("https://www.samsungpop.com/privacy.pdf"))
        self.assertFalse(is_verified_report_original_url("https://www.samsungpop.com/support/report-center/fake.pdf"))
        self.assertFalse(
            is_verified_report_original_url(
                "https://www.samsungpop.com/support/download?"
                "saveKey=research.pdf&fileName=fake.pdf&contentType=application/pdf"
            )
        )
        self.assertFalse(
            is_verified_report_original_url(
                "https://www.samsungpop.com/common.do?next=research.pdf&contentType=application/pdf"
            )
        )
        self.assertFalse(is_verified_report_original_url("https://www.samsungpop.com/media/pdfs/fake.pdf"))
        self.assertFalse(is_recognized_report_domain("https://samsungpop.com.evil.com/research/fake-report.pdf"))
        self.assertFalse(
            is_verified_report_original_url("https://samsungpop.com.evil.com/research/fake-report.pdf")
        )
        self.assertFalse(is_recognized_report_domain("https://evil.example/samsungpop.com/research/fake-report.pdf"))
        self.assertFalse(
            is_verified_report_original_url("https://evil.example/samsungpop.com/research/fake-report.pdf")
        )

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

    def test_consensus_csv_connector_ignores_non_finite_optional_numbers(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "kr_consensus_revisions.csv").write_text(
                "\n".join(
                    (
                        "symbol,date,fiscal_year,as_of_date,eps_revision_1m,op_revision_1m,analyst_count_change,source",
                        "CASE,2024-01-05,2024,2024-01-05,nan,inf,nan,file",
                    )
                )
                + "\n",
                encoding="utf-8",
            )

            connector = ConsensusCSVConnector(fixture_root=root)
            revisions = connector.get_consensus_revisions("CASE", date(2024, 1, 5))

        self.assertEqual(len(revisions), 1)
        self.assertIsNone(revisions[0].eps_revision_1m)
        self.assertIsNone(revisions[0].op_revision_1m)
        self.assertIsNone(revisions[0].analyst_count_change)

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
                        "COMMENT": (
                            "본격적인 장기공급계약 체결 시작<br/>"
                            "2분기 매출액 81.8조원(+56% QoQ), 영업이익 63.4조원(+69%) 전망<br/>"
                            "27년 HBM 수요 확대와 고객 다변화"
                        ),
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
        self.assertEqual(samsung[1].parsed_fields["target_price_revision_direction"], "up")
        self.assertTrue(samsung[1].parsed_fields["target_price_upgrade_mentioned"])
        self.assertEqual(samsung[1].parsed_fields["eps_revision_direction"], "up")
        self.assertTrue(samsung[1].parsed_fields["eps_revision_up_mentioned"])

        self.assertEqual(hynix[0].target_price, 2950000)
        self.assertEqual(hynix[0].fy1_eps, 325071)
        self.assertEqual(hynix[1].broker, "미래에셋")
        self.assertEqual(hynix[1].fy1_sales, 81_800_000_000_000.0)
        self.assertEqual(hynix[1].fy1_op, 63_400_000_000_000.0)
        self.assertTrue(hynix[1].parsed_fields["forward_estimate_present"])
        self.assertEqual(hynix[1].parsed_fields["forward_op_estimate"], 63_400_000_000_000.0)
        self.assertEqual(hynix[1].parsed_fields["target_price_revision_direction"], "unchanged")
        self.assertEqual(hynix[1].parsed_fields["eps_revision_direction"], "up")
        self.assertIn("장기공급계약", hynix[1].raw_text or "")

    def test_company_guide_recent_report_does_not_treat_target_price_as_op_estimate(self):
        connector = CompanyGuideConnector()

        reports = connector.parse_recent_reports_payload(
            {
                "lists": [
                    {
                        "RPT_ID": 1200000,
                        "ANL_DT": "26/06/10",
                        "RPT_TITLE": "실적 전망치 상향",
                        "TARGET_PRC": "2,600,000",
                        "COMMENT": "영업이익 전망치 상향, 목표주가 260만원 상향",
                        "BRK_NM_SHORT_KOR": "테스트",
                        "PRC_ACTION_TYP_NM": "목표주가 상향",
                        "EPS_ACTION_TYP_NM": "추정EPS 상향",
                    }
                ]
            },
            symbol="999999",
            as_of_date=date(2026, 6, 11),
        )

        self.assertEqual(len(reports), 1)
        self.assertIsNone(reports[0].fy1_op)
        self.assertNotIn("forward_op_estimate", reports[0].parsed_fields)
        self.assertTrue(reports[0].parsed_fields["estimate_upgrade_mentioned"])

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
