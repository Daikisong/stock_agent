from datetime import date
from pathlib import Path
import unittest
from unittest.mock import patch

from e2r.cheap_scan import DataGoKrFSCConnector, KoreaCheapScanSources
from e2r.llm import FakeLLMProvider, ThemeRouteOutput
from e2r.models import Market
from e2r.pipeline.e2r_standard_flow import DIAGNOSTIC_REPLAY_MODES, E2R_STANDARD, E2RStandardConfig, E2RStandardFlow
from e2r.research.search_budget import SearchBudget
from e2r.research.search_provider import EmptySearchProvider
from e2r.sources import KINDConnector, KRXConnector, OpenDARTConnector


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_ROOT = ROOT / "data/raw/korea_cheap_scan"
AS_OF = date(2024, 5, 21)


class E2RStandardFlowTests(unittest.TestCase):
    def test_e2r_standard_flow_exists_and_is_default_name(self):
        result = E2RStandardFlow().run(
            E2RStandardConfig(
                as_of_date=AS_OF,
                sources=_sources(),
                universe_limit=2,
                report_radar_enabled=False,
                browser_provider=EmptySearchProvider(),
                free_search_provider=EmptySearchProvider(),
                search_budget=SearchBudget(max_total_queries_per_day=3, max_queries_per_symbol=3),
            )
        )

        self.assertEqual(result.flow_name, E2R_STANDARD)
        self.assertGreaterEqual(result.cheap_scan.instruments_scanned, 1)
        self.assertTrue(result.candidates)
        self.assertIn("official_only", DIAGNOSTIC_REPLAY_MODES)
        self.assertIn("case_fixture", DIAGNOSTIC_REPLAY_MODES)
        self.assertIn("hybrid", DIAGNOSTIC_REPLAY_MODES)

    def test_standard_flow_passes_official_context_into_web_research(self):
        result = E2RStandardFlow().run(
            E2RStandardConfig(
                as_of_date=AS_OF,
                sources=_sources(),
                universe_limit=2,
                report_radar_enabled=False,
                browser_provider=EmptySearchProvider(),
                free_search_provider=EmptySearchProvider(),
                search_budget=SearchBudget(max_total_queries_per_day=3, max_queries_per_symbol=3),
            )
        )

        self.assertTrue(result.web_results)
        result_evidence_ids = {item.evidence_id for item in result.evidence}
        self.assertTrue(any(item.parsed_fields.get("claim_ledger_version") for item in result.evidence))
        for web_result in result.web_results:
            feature_input = web_result.feature_input
            self.assertEqual(feature_input.as_of_date, AS_OF)
            self.assertEqual(feature_input.sector_context, "전기장비")
            self.assertTrue(feature_input.price_bars)
            self.assertTrue(feature_input.disclosures)
            self.assertEqual(web_result.feature_result.source_fields["large_sector_id"], "L1_INDUSTRIALS_INFRA_DEFENSE_GRID")
            self.assertIn(
                web_result.feature_result.source_fields["canonical_archetype_id"],
                {"C01_ORDER_BACKLOG_MARGIN_BRIDGE", "C02_POWER_GRID_DATACENTER_CAPEX"},
            )
            self.assertIn("archetype_weight:", web_result.score.scoring_version)
            self.assertGreater(
                web_result.score.diagnostic_scores["evidence_contract_required_primitive_count_capped"],
                0.0,
            )
            self.assertIn("evidence_contract_required_primitives", web_result.feature_result.source_fields)
            self.assertTrue(set(web_result.score.evidence_ids).issubset(result_evidence_ids))

    def test_diagnostic_modes_are_not_default_production_flow(self):
        self.assertEqual(E2RStandardFlow.flow_name, E2R_STANDARD)
        self.assertNotIn(E2R_STANDARD, DIAGNOSTIC_REPLAY_MODES)

    def test_optional_llm_layer_runs_without_overriding_stage(self):
        provider = FakeLLMProvider()
        result = E2RStandardFlow().run(
            E2RStandardConfig(
                as_of_date=AS_OF,
                sources=_sources(),
                universe_limit=2,
                report_radar_enabled=False,
                browser_provider=EmptySearchProvider(),
                free_search_provider=EmptySearchProvider(),
                search_budget=SearchBudget(max_total_queries_per_day=3, max_queries_per_symbol=3),
                llm_enabled=True,
                llm_provider=provider,
            )
        )

        self.assertTrue(result.llm_outputs)
        self.assertTrue(all(item.attempted_stage_override is None for item in result.llm_outputs))

    def test_fixture_standard_flow_defaults_theme_rebalance_off(self):
        with patch.dict("os.environ", {}, clear=True):
            config = E2RStandardConfig(as_of_date=AS_OF)

        self.assertFalse(config.theme_rebalance_enabled)
        self.assertTrue(config.theme_evidence_review_enabled)
        self.assertIsNone(config.top_candidates)

    def test_live_standard_flow_defaults_theme_rebalance_on_and_uses_codex_provider(self):
        with patch.dict("os.environ", {}, clear=True), patch(
            "e2r.llm.codex_theme_provider.CodexCLIThemeRouteProvider.route",
            return_value=ThemeRouteOutput(status="no_transition"),
        ) as route:
            config = E2RStandardConfig(
                as_of_date=AS_OF,
                sources=_sources(),
                universe_limit=2,
                fixture_mode=False,
                report_radar_enabled=False,
                browser_provider=EmptySearchProvider(),
                free_search_provider=EmptySearchProvider(),
                search_budget=SearchBudget(max_total_queries_per_day=3, max_queries_per_symbol=3),
            )
            result = E2RStandardFlow().run(config)

        self.assertTrue(config.theme_rebalance_enabled)
        self.assertTrue(result.web_results)
        self.assertGreater(route.call_count, 0)

    def test_theme_rebalance_can_use_codex_provider_from_env(self):
        with patch.dict("os.environ", {"E2R_THEME_ROUTE_PROVIDER": "codex"}, clear=False), patch(
            "e2r.llm.codex_theme_provider.CodexCLIThemeRouteProvider.route",
            return_value=ThemeRouteOutput(status="no_transition"),
        ) as route:
            result = E2RStandardFlow().run(
                E2RStandardConfig(
                    as_of_date=AS_OF,
                    sources=_sources(),
                    universe_limit=2,
                    report_radar_enabled=False,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                    search_budget=SearchBudget(max_total_queries_per_day=3, max_queries_per_symbol=3),
                    theme_rebalance_enabled=True,
                )
            )

        self.assertTrue(result.web_results)
        self.assertGreater(route.call_count, 0)


def _sources() -> KoreaCheapScanSources:
    return KoreaCheapScanSources(
        krx=KRXConnector(fixture_root=FIXTURE_ROOT / "krx"),
        opendart=OpenDARTConnector(fixture_root=FIXTURE_ROOT / "opendart"),
        kind=KINDConnector(fixture_root=FIXTURE_ROOT / "kind"),
        fsc=DataGoKrFSCConnector(fixture_root=FIXTURE_ROOT / "data_go_kr_fsc"),
    )


if __name__ == "__main__":
    unittest.main()
