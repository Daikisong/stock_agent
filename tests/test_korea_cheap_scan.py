from datetime import date
from pathlib import Path
import unittest

from e2r.cheap_scan import (
    DataGoKrFSCConnector,
    KoreaCheapScanConfig,
    KoreaCheapScanSources,
    KoreaCheapScanner,
    RecommendedNextLayer,
)
from e2r.cheap_scan.query_escalation import queries_for_candidate, queries_for_reason_codes
from e2r.models import Market
from e2r.research.search_budget import SearchBudget
from e2r.research.search_provider import EmptySearchProvider
from e2r.sources import KINDConnector, KRXConnector, OpenDARTConnector


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_ROOT = ROOT / "data/raw/korea_cheap_scan"
AS_OF = date(2024, 5, 21)


class KoreaCheapScanTests(unittest.TestCase):
    def test_supply_contract_amount_to_sales_becomes_event_search_candidate(self):
        result = _run_scan()
        candidate = _candidate(result, "111111")

        self.assertIn("DISC_SUPPLY_CONTRACT", candidate.reason_codes)
        self.assertIn("DISC_CONTRACT_TO_SALES_10P", candidate.reason_codes)
        self.assertEqual(candidate.recommended_next_layer, RecommendedNextLayer.EVENT_SEARCH)
        self.assertGreater(candidate.disclosure_event_score, 40)

    def test_long_term_contract_with_price_volume_spike_becomes_deep_research_candidate(self):
        candidate = _candidate(_run_scan(), "222222")

        self.assertIn("DISC_LONG_TERM_CONTRACT", candidate.reason_codes)
        self.assertIn("PRICE_VOLUME_SPIKE", candidate.reason_codes)
        self.assertIn("PRICE_GAP_WITH_DISCLOSURE", candidate.reason_codes)
        self.assertEqual(candidate.recommended_next_layer, RecommendedNextLayer.DEEP_RESEARCH)

    def test_facility_investment_and_capa_increase_becomes_event_search_candidate(self):
        candidate = _candidate(_run_scan(), "333333")

        self.assertIn("DISC_FACILITY_INVESTMENT", candidate.reason_codes)
        self.assertIn("DISC_CAPA_INCREASE", candidate.reason_codes)
        self.assertEqual(candidate.recommended_next_layer, RecommendedNextLayer.EVENT_SEARCH)

    def test_rights_offering_is_risk_candidate_not_green_escalation(self):
        candidate = _candidate(_run_scan(), "666666")

        self.assertIn("DISC_RIGHTS_OFFERING", candidate.reason_codes)
        self.assertGreaterEqual(candidate.risk_event_score, 40)
        self.assertEqual(candidate.disclosure_event_score, 0)
        self.assertNotEqual(candidate.recommended_next_layer, RecommendedNextLayer.DEEP_RESEARCH)

    def test_high_price_run_without_disclosure_does_not_escalate_to_deep_research(self):
        candidate = _candidate(_run_scan(), "444444")

        self.assertIn("PRICE_60D_TOP_PERCENTILE", candidate.reason_codes)
        self.assertNotEqual(candidate.recommended_next_layer, RecommendedNextLayer.DEEP_RESEARCH)

    def test_managed_or_trading_halt_issue_is_marked_as_risk(self):
        candidate = _candidate(_run_scan(), "555555")

        self.assertIn("RISK_MANAGED_ISSUE", candidate.reason_codes)
        self.assertIn("RISK_TRADING_HALT", candidate.reason_codes)
        self.assertEqual(candidate.recommended_next_layer, RecommendedNextLayer.NONE)
        self.assertEqual(candidate.dropped_reason, "hard_risk_status")

    def test_query_escalation_emits_reason_specific_templates(self):
        queries = queries_for_reason_codes("한전변압기", ("DISC_SUPPLY_CONTRACT", "DISC_FACILITY_INVESTMENT"))

        self.assertIn("한전변압기 장기공급계약 매출액 대비", queries)
        self.assertIn("한전변압기 단일판매 공급계약 계약기간", queries)
        self.assertIn("한전변압기 신규시설투자 CAPA 증설", queries)

    def test_dilution_risk_queries_include_red_team_fallback_terms(self):
        queries = queries_for_reason_codes("희석테크", ("DISC_RIGHTS_OFFERING", "DISC_CONVERTIBLE_BOND", "DISC_BOND_WITH_WARRANT"))

        self.assertIn("희석테크 유상증자", queries)
        self.assertIn("희석테크 전환사채", queries)
        self.assertIn("희석테크 신주인수권부사채", queries)
        self.assertIn("희석테크 보호예수 해제", queries)
        self.assertIn("희석테크 오버행", queries)
        self.assertIn("희석테크 CB 리픽싱", queries)

    def test_scanner_processes_kospi_kosdaq_fixture_universe_and_ranks_candidates(self):
        result = _run_scan()

        self.assertGreaterEqual(result.instruments_scanned, 7)
        self.assertGreaterEqual(len(result.candidates), 6)
        self.assertEqual(result.candidates[0].symbol, "222222")
        self.assertGreaterEqual(result.candidates[0].cheap_scan_total_score, result.candidates[-1].cheap_scan_total_score)

    def test_as_of_date_filters_future_disclosures(self):
        candidate = _candidate(_run_scan(), "111111")

        self.assertNotIn("DISC_RIGHTS_OFFERING", candidate.reason_codes)
        self.assertTrue(all("202405220001" not in evidence_id for evidence_id in candidate.evidence_ids))

    def test_fsc_connector_builds_requests_and_loads_fixture_instruments(self):
        connector = DataGoKrFSCConnector(fixture_root=FIXTURE_ROOT / "data_go_kr_fsc", enable_stock_issuance_source=True)

        request = connector.build_listed_items_request(Market.KR, AS_OF)
        issuance_request = connector.build_stock_issuance_request("666666", AS_OF)
        instruments = connector.list_instruments(Market.KR, AS_OF)
        bars = connector.get_price_bars("888888", AS_OF, AS_OF, AS_OF)
        issuance = connector.get_stock_issuance_records("666666", AS_OF)

        self.assertIn("1160100", request.url)
        self.assertEqual(request.params["basDt"], "20240521")
        self.assertEqual(issuance_request.params["likeSrtnCd"], "666666")
        self.assertEqual(instruments[0].symbol, "888888")
        self.assertEqual(bars[0].close, 1050)
        self.assertEqual(issuance[0]["issuance_type"], "rights_offering")

    def test_fsc_approved_v2_request_builders_use_configured_endpoints(self):
        connector = DataGoKrFSCConnector()

        financial = connector.build_financial_info_request("111111", AS_OF)
        disclosure = connector.build_disclosure_info_request("111111", AS_OF, AS_OF, AS_OF)
        corp_basic = connector.build_corp_basic_info_request("111111", AS_OF)

        self.assertIn("GetFinaStatInfoService_V2/getSummFinaStat_V2", financial.url)
        self.assertIn("GetDiscInfoService_V2/getDiviDiscInfo_V2", disclosure.url)
        self.assertIn("GetCorpBasicInfoService_V2/getCorpOutline_V2", corp_basic.url)
        self.assertEqual(financial.params["bizYear"], "2023")
        self.assertEqual(disclosure.params["basDt"], "20240521")

    def test_fsc_legacy_endpoint_aliases_still_work_when_configured(self):
        connector = DataGoKrFSCConnector(
            financial_info_service_path="GetCorpFinanceInfoService/getCorpFinanceInfo",
            disclosure_info_service_path="GetCorpDisclosureInfoService/getDisclosureInfo",
            corp_basic_info_service_path="GetCorpBasicInfoService/getCorpBasicInfo",
        )

        self.assertIn("GetCorpFinanceInfoService/getCorpFinanceInfo", connector.build_financial_info_request("111111", AS_OF).url)
        self.assertIn("GetCorpDisclosureInfoService/getDisclosureInfo", connector.build_disclosure_info_request("111111", AS_OF, AS_OF, AS_OF).url)
        self.assertIn("GetCorpBasicInfoService/getCorpBasicInfo", connector.build_corp_basic_info_request("111111", AS_OF).url)

    def test_krx_approved_openapi_request_builders_use_data_dbg_urls(self):
        connector = KRXConnector(openapi_key="KRX_SECRET")
        requests = (
            connector.build_openapi_kospi_daily_trading_request(AS_OF),
            connector.build_openapi_kosdaq_daily_trading_request(AS_OF),
            connector.build_openapi_kospi_issue_base_info_request(AS_OF),
            connector.build_openapi_kosdaq_issue_base_info_request(AS_OF),
            connector.build_openapi_kospi_index_daily_trading_request(AS_OF),
            connector.build_openapi_kosdaq_index_daily_trading_request(AS_OF),
        )

        urls = [request.url for request in requests]
        self.assertIn("https://data-dbg.krx.co.kr/svc/apis/sto/stk_bydd_trd", urls)
        self.assertIn("https://data-dbg.krx.co.kr/svc/apis/sto/ksq_bydd_trd", urls)
        self.assertIn("https://data-dbg.krx.co.kr/svc/apis/sto/stk_isu_base_info", urls)
        self.assertIn("https://data-dbg.krx.co.kr/svc/apis/sto/ksq_isu_base_info", urls)
        self.assertIn("https://data-dbg.krx.co.kr/svc/apis/idx/kospi_dd_trd", urls)
        self.assertIn("https://data-dbg.krx.co.kr/svc/apis/idx/kosdaq_dd_trd", urls)
        self.assertTrue(all(request.params["basDd"] == "20240521" for request in requests))
        self.assertTrue(all(request.headers["AUTH_KEY"] == "KRX_SECRET" for request in requests))
        self.assertTrue(all(request.credential_name == "KRX_OPENAPI_KEY" for request in requests))

    def test_stock_issuance_records_are_optional_by_default(self):
        connector = DataGoKrFSCConnector(fixture_root=FIXTURE_ROOT / "data_go_kr_fsc")

        self.assertEqual(connector.get_stock_issuance_records("666666", AS_OF), ())

    def test_escalate_candidates_to_web_research_uses_reason_code_query_groups(self):
        scanner = KoreaCheapScanner(_sources())
        candidate = _candidate(_run_scan(), "222222")
        budget = SearchBudget(max_total_queries_per_day=3, max_queries_per_symbol=3, max_deep_research_symbols=1)

        results = scanner.escalate_candidates_to_web_research(
            [candidate],
            budget,
            browser_provider=EmptySearchProvider(),
            free_search_provider=EmptySearchProvider(),
        )

        self.assertEqual(len(results), 1)
        self.assertIn("케이전력 장기공급계약 매출액 대비", results[0].web_result.queries_run)
        self.assertIn("케이전력 단일판매 공급계약 계약기간", queries_for_candidate(candidate).queries)
        self.assertIn(candidate.symbol, results[0].budget_tracker.deep_research_symbols)


def _sources() -> KoreaCheapScanSources:
    return KoreaCheapScanSources(
        krx=KRXConnector(fixture_root=FIXTURE_ROOT / "krx"),
        opendart=OpenDARTConnector(fixture_root=FIXTURE_ROOT / "opendart"),
        kind=KINDConnector(fixture_root=FIXTURE_ROOT / "kind"),
        fsc=DataGoKrFSCConnector(fixture_root=FIXTURE_ROOT / "data_go_kr_fsc"),
    )


def _run_scan():
    scanner = KoreaCheapScanner(_sources())
    return scanner.run(KoreaCheapScanConfig(as_of_date=AS_OF, markets=(Market.KR,)))


def _candidate(result, symbol):
    for candidate in result.candidates:
        if candidate.symbol == symbol:
            return candidate
    raise AssertionError(f"candidate {symbol} not found")


if __name__ == "__main__":
    unittest.main()
