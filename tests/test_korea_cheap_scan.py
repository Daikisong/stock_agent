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
        connector = DataGoKrFSCConnector(fixture_root=FIXTURE_ROOT / "data_go_kr_fsc")

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
