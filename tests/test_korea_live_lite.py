from datetime import date, datetime
import io
import json
from pathlib import Path
from types import SimpleNamespace
import tempfile
import unittest
from unittest.mock import patch
import zipfile

from e2r.cheap_scan import DataGoKrFSCConnector, KoreaCheapScanSources
from e2r.cheap_scan.models import CheapScanCandidate, RecommendedNextLayer
from e2r.cli.review_korea_run import (
    KoreaRunReviewSummary,
    _targeted_score_audit_failures,
    _targeted_score_changes,
    _targeted_score_states,
    build_review_summary,
    main as review_korea_run_main,
    render_review_summary,
)
from e2r.features import DeterministicFeatureEngineer, FeatureEngineeringInput
from e2r.llm import FakeThemeRouteProvider, ThemeRouteOutput
from e2r.models import DisclosureEvent, Market, ScoreContribution, ScoreSnapshot, Stage
from e2r.pipeline.korea_live_lite import (
    KoreaLiveLiteBudget,
    KoreaLiveLiteConfig,
    KoreaLiveLiteRunner,
    _base_feature_input_for_candidate,
    _consensus_connector_revisions_for_candidate,
    _consensus_connector_snapshots_for_candidate,
    _execute_company_guide_for_candidates,
    _execute_naver_finance_for_candidates,
    _default_agentic_evidence_enabled,
    _official_follow_up_source_provider,
    _opendart_financial_statement_call_reserve,
    _query_planner_for_candidate,
    _execute_opendart_detail_fetches,
    _result_score_valid,
    _score_blocked_status,
    _score_gap_audit_events_from_rows,
    _score_gap_source_route_plans_from_rows,
    _score_state_contract_findings_for_outputs,
    _stage_output_row,
    _sources_with_date_disclosures,
    _targeted_smoke_result_row,
    _theme_route_row,
    build_opendart_date_range_requests,
    plan_opendart_detail_fetches,
)
from e2r.research.search_provider import EmptySearchProvider, FixtureSearchProvider, SearchResult
from e2r.score_validity import score_state_contract_violations
from e2r.sources import ConsensusCSVConnector, KINDConnector, KRXConnector, OpenDARTConnector
from e2r.sources.http_client import HttpClientStats, HttpResult


AS_OF = date(2024, 5, 21)


class KoreaLiveLiteTests(unittest.TestCase):
    def setUp(self) -> None:
        self._codex_theme_route_patch = patch(
            "e2r.llm.codex_theme_provider.CodexCLIThemeRouteProvider.route",
            return_value=ThemeRouteOutput(status="no_transition"),
        )
        self.codex_theme_route = self._codex_theme_route_patch.start()
        self.addCleanup(self._codex_theme_route_patch.stop)

    def test_live_lite_config_validates_budgets(self):
        with self.assertRaises(ValueError):
            KoreaLiveLiteBudget(max_opendart_calls_per_day=-1)
        with self.assertRaises(ValueError):
            KoreaLiveLiteConfig(as_of_date=AS_OF, top_candidates=0)
        with self.assertRaises(ValueError):
            KoreaLiveLiteConfig(as_of_date=AS_OF, allow_parallel_live_requests=False, max_global_live_workers=2)
        with self.assertRaises(ValueError):
            KoreaLiveLiteConfig(as_of_date=AS_OF, post_parse_gap_expansion_max_queries=-1)
        with self.assertRaisesRegex(ValueError, "top_results must be bounded"):
            KoreaLiveLiteConfig(as_of_date=AS_OF, top_results=None)
        with self.assertRaisesRegex(ValueError, "score_gap_query_retry_max must be bounded"):
            KoreaLiveLiteConfig(as_of_date=AS_OF, score_gap_query_retry_max=None)
        with self.assertRaises(ValueError):
            KoreaLiveLiteConfig(as_of_date=AS_OF, score_gap_query_retry_max=-1)
        with self.assertRaises(ValueError):
            KoreaLiveLiteConfig(as_of_date=AS_OF, opendart_detail_fetch_max_per_symbol=-1)
        with self.assertRaises(ValueError):
            KoreaLiveLiteConfig(as_of_date=AS_OF, max_score_gap_expansion_rounds=-1)
        with self.assertRaises(ValueError):
            KoreaLiveLiteConfig(as_of_date=AS_OF, theme_route_search_result_limit=-1)
        with self.assertRaises(ValueError):
            KoreaLiveLiteConfig(as_of_date=AS_OF, theme_route_document_limit=-1)
        with self.assertRaises(ValueError):
            KoreaLiveLiteConfig(as_of_date=AS_OF, theme_route_document_excerpt_chars=0)
        with self.assertRaises(ValueError):
            KoreaLiveLiteConfig(as_of_date=AS_OF, theme_evidence_review_timeout_seconds=0)
        with self.assertRaises(ValueError):
            KoreaLiveLiteConfig(as_of_date=AS_OF, agentic_mapper_self_consistency_rounds=0)
        with self.assertRaises(ValueError):
            KoreaLiveLiteConfig(as_of_date=AS_OF, agentic_mapper_self_consistency_min_agreement=0)
        with self.assertRaises(ValueError):
            KoreaLiveLiteConfig(
                as_of_date=AS_OF,
                agentic_mapper_self_consistency_rounds=2,
                agentic_mapper_self_consistency_min_agreement=3,
            )
        with self.assertRaises(ValueError):
            KoreaLiveLiteConfig(as_of_date=AS_OF, agentic_mapper_batch_max_tasks=0)
        with self.assertRaises(ValueError):
            KoreaLiveLiteConfig(as_of_date=AS_OF, agentic_evidence_document_limit=0)
        with self.assertRaises(ValueError):
            KoreaLiveLiteConfig(as_of_date=AS_OF, agentic_max_raw_assertions_per_run=0)
        with self.assertRaises(ValueError):
            KoreaLiveLiteConfig(as_of_date=AS_OF, agentic_provider_timeout_seconds=0)

    def test_live_lite_default_search_budget_is_uncapped(self):
        budget = KoreaLiveLiteBudget()
        config = KoreaLiveLiteConfig(as_of_date=AS_OF)

        self.assertIsNone(budget.max_opendart_calls_per_day)
        self.assertIsNone(budget.max_krx_calls_per_day)
        self.assertIsNone(budget.max_data_go_kr_calls_per_day)
        self.assertIsNone(budget.max_naver_search_calls_per_day)
        self.assertIsNone(budget.max_naver_finance_calls_per_day)
        self.assertIsNone(budget.max_company_guide_calls_per_day)
        self.assertIsNone(budget.max_symbols_for_event_search)
        self.assertIsNone(budget.max_symbols_for_deep_research)
        self.assertIsNone(budget.max_opendart_detail_fetches_per_run)
        self.assertIsNone(config.top_candidates)
        self.assertEqual(config.max_results_per_query, 100)
        self.assertEqual(config.top_results, 60)
        self.assertEqual(config.max_theme_expansion_rounds, 2)
        self.assertEqual(config.max_score_gap_expansion_rounds, 2)
        self.assertEqual(config.post_parse_gap_expansion_max_queries, 10)
        self.assertEqual(config.score_gap_query_retry_max, 2)
        self.assertEqual(config.theme_route_search_result_limit, 80)
        self.assertEqual(config.theme_route_document_limit, 32)
        self.assertEqual(config.theme_route_document_excerpt_chars, 1200)
        self.assertEqual(config.theme_evidence_review_timeout_seconds, 60.0)
        self.assertEqual(config.agentic_mapper_self_consistency_rounds, 3)
        self.assertEqual(config.agentic_mapper_self_consistency_min_agreement, 2)
        self.assertTrue(config.agentic_mapper_self_consistency_use_batch)
        self.assertEqual(config.agentic_mapper_batch_max_tasks, 12)
        self.assertEqual(config.agentic_evidence_document_limit, 12)
        self.assertEqual(config.agentic_max_raw_assertions_per_run, 72)
        self.assertIsNone(config.agentic_provider_timeout_seconds)

    def test_timeout_diagnostic_smoke_preset_is_bounded_and_explicit(self):
        config = KoreaLiveLiteConfig.smoke_preset("timeout_diagnostic", as_of_date=AS_OF)

        self.assertEqual(config.live_smoke_preset_used, "timeout_diagnostic")
        self.assertEqual(config.universe_limit, 1)
        self.assertEqual(config.max_results_per_query, 20)
        self.assertEqual(config.top_results, 5)
        self.assertEqual(config.max_theme_expansion_rounds, 1)
        self.assertEqual(config.max_score_gap_expansion_rounds, 0)
        self.assertEqual(config.theme_route_search_result_limit, 5)
        self.assertEqual(config.theme_route_document_limit, 1)
        self.assertEqual(config.post_parse_gap_expansion_max_queries, 0)
        self.assertEqual(config.score_gap_query_retry_max, 0)
        self.assertEqual(config.theme_evidence_review_timeout_seconds, 5.0)
        self.assertEqual(config.agentic_mapper_self_consistency_rounds, 1)
        self.assertEqual(config.agentic_mapper_self_consistency_min_agreement, 1)
        self.assertEqual(config.agentic_mapper_batch_max_tasks, 3)
        self.assertEqual(config.agentic_evidence_document_limit, 1)
        self.assertEqual(config.agentic_max_raw_assertions_per_run, 1)
        self.assertEqual(config.agentic_provider_timeout_seconds, 5.0)

    def test_live_lite_defaults_agentic_evidence_on_for_live_non_fixture_runs(self):
        live_config = KoreaLiveLiteConfig(
            as_of_date=AS_OF,
            fixture_mode=False,
            live_enabled=True,
            theme_rebalance_enabled=True,
        )
        explicit_off = KoreaLiveLiteConfig(
            as_of_date=AS_OF,
            fixture_mode=False,
            live_enabled=True,
            theme_rebalance_enabled=True,
            agentic_evidence_enabled=False,
        )
        fixture_config = KoreaLiveLiteConfig(
            as_of_date=AS_OF,
            fixture_mode=True,
            live_enabled=True,
            theme_rebalance_enabled=True,
        )

        self.assertTrue(_default_agentic_evidence_enabled(live_config, effective_fixture_mode=False))
        self.assertFalse(_default_agentic_evidence_enabled(explicit_off, effective_fixture_mode=False))
        self.assertFalse(_default_agentic_evidence_enabled(fixture_config, effective_fixture_mode=True))

    def test_targeted_smoke_uncapped_symbol_budget_does_not_break_opendart_reserve(self):
        config = KoreaLiveLiteConfig(
            as_of_date=AS_OF,
            targeted_smoke_enabled=True,
            targeted_smoke_symbol="000660",
            targeted_smoke_company="SK하이닉스",
            budget=KoreaLiveLiteBudget(
                max_opendart_calls_per_day=8,
                max_symbols_for_event_search=None,
                max_symbols_for_deep_research=None,
            ),
        )

        reserve = _opendart_financial_statement_call_reserve(config)

        self.assertGreater(reserve, 0)

    def test_targeted_query_planner_preserves_sector_context(self):
        candidate = CheapScanCandidate(
            symbol="005930",
            company_name="삼성전자",
            market=Market.KR,
            as_of_date=AS_OF,
            reason_codes=("TARGETED_SMOKE",),
            cheap_scan_total_score=0.0,
            recommended_next_layer=RecommendedNextLayer.EVENT_SEARCH,
            candidate_source_path="targeted_smoke",
            test_injected=True,
            production_candidate=False,
        )
        config = KoreaLiveLiteConfig(
            as_of_date=AS_OF,
            targeted_smoke_queries=("삼성전자 HBM",),
        )

        plan = _query_planner_for_candidate(candidate, config, sector_context="반도체").plan()

        self.assertEqual(plan.sector, "반도체")
        self.assertTrue(plan.queries)
        self.assertEqual({item.sector for item in plan.queries}, {"반도체"})

    def test_live_lite_tiny_smoke_preset_keeps_research_budget_uncapped(self):
        config = KoreaLiveLiteConfig.smoke_preset("tiny", as_of_date=AS_OF)

        self.assertEqual(config.universe_limit, 50)
        self.assertIsNone(config.budget.max_naver_search_calls_per_day)
        self.assertIsNone(config.budget.max_symbols_for_event_search)
        self.assertIsNone(config.budget.max_symbols_for_deep_research)
        self.assertIsNone(config.budget.max_opendart_detail_fetches_per_run)
        self.assertFalse(config.allow_parallel_live_requests)
        self.assertEqual(config.max_global_live_workers, 1)
        self.assertEqual(config.live_smoke_preset_used, "tiny")

    def test_standard_shadow_preset_is_uncapped_like_operation(self):
        config = KoreaLiveLiteConfig.smoke_preset("standard_shadow", as_of_date=AS_OF)

        self.assertIsNone(config.universe_limit)
        self.assertIsNone(config.budget.max_naver_search_calls_per_day)
        self.assertIsNone(config.budget.max_symbols_for_event_search)
        self.assertIsNone(config.budget.max_symbols_for_deep_research)
        self.assertIsNone(config.budget.max_opendart_detail_fetches_per_run)
        self.assertEqual(config.live_smoke_preset_used, "standard_shadow")

    def test_live_mode_defaults_theme_rebalance_on(self):
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "DATA_GO_KR_SERVICE_KEY": "DATA_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }
        with patch.dict("os.environ", env, clear=True):
            config = KoreaLiveLiteConfig(as_of_date=AS_OF, fixture_mode=False, live_enabled=True)

        self.assertTrue(config.theme_rebalance_enabled)

    def test_missing_credentials_do_not_crash_and_mark_fixture_fallback(self):
        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", {}, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    env_file=None,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        self.assertTrue(result.run_log.effective_fixture_mode)
        self.assertIn("OPENDART_API_KEY", result.run_log.missing_credentials)
        self.assertIn("NAVER_CLIENT_ID", result.run_log.missing_credentials)

    def test_fixture_live_lite_run_writes_candidate_evidence_brief_and_log(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

            self.assertTrue(result.candidates_path.exists())
            self.assertTrue(result.evidence_path.exists())
            self.assertTrue(result.brief_path.exists())
            self.assertTrue(result.run_log_path.exists())
            self.assertIsNotNone(result.phase_log_path)
            self.assertTrue(result.phase_log_path.exists())
            phase_lines = result.phase_log_path.read_text(encoding="utf-8").strip().splitlines()
            self.assertTrue(any('"phase": "start"' in line for line in phase_lines))
            self.assertEqual(result.run_log.phase_log_path, str(result.phase_log_path))
            self.assertTrue(result.calibration_json_path.exists())
            self.assertTrue(result.calibration_md_path.exists())
            self.assertIn("E2R Morning Brief", result.brief_path.read_text(encoding="utf-8"))
            self.assertIn("cheap_scan_score", result.calibration_md_path.read_text(encoding="utf-8"))
            candidates_json = json.loads(result.candidates_path.read_text(encoding="utf-8"))
            calibration_json = json.loads(result.calibration_json_path.read_text(encoding="utf-8"))
            run_log_json = json.loads(result.run_log_path.read_text(encoding="utf-8"))
            self.assertGreaterEqual(len(candidates_json["candidates"]), 1)
            self.assertIn("near_miss_top_50", calibration_json)
            self.assertIn("diagnostic_reason_distribution", calibration_json)
            self.assertGreaterEqual(len(run_log_json["planned_opendart_detail_requests"]), 1)
            self.assertIn("audit_findings", run_log_json)
            self.assertIn("rate_limit_waits", run_log_json)
            self.assertIn("rate_limit_skips", run_log_json)
            self.assertIn("actual_http_requests_by_source", run_log_json)
            self.assertIn("logical_queries_by_source", run_log_json)
            self.assertIn("max_concurrency_used_by_source", run_log_json)
            self.assertIn("score_state_contract_findings", run_log_json)
            self.assertIn("score_gap_audit_events", run_log_json)
            self.assertIn("score_gap_source_route_plans", run_log_json)
            self.assertEqual(result.run_log.score_gap_audit_events, ())
            self.assertEqual(result.run_log.score_gap_source_route_plans, ())
            self.assertEqual(run_log_json["score_state_contract_findings"], [])
            self.assertEqual(result.run_log.score_state_contract_findings, ())
            self.assertEqual(run_log_json["source_modes"]["stock_issuance"], "disabled_optional")
            self.assertEqual(run_log_json["source_modes"]["krx_openapi"], "disabled_optional")
            self.assertTrue(
                any(item["source_name"] == "data_go_kr_fsc_stock_issuance" for item in run_log_json["source_license_metadata"])
            )
            self.assertTrue(any(item["source_name"] == "krx_openapi" for item in run_log_json["source_license_metadata"]))

    def test_live_lite_works_without_stock_issuance_api_and_detects_dilution_from_opendart(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    enable_stock_issuance_source=False,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        candidate = _candidate(result, "666666")
        self.assertIn("DISC_RIGHTS_OFFERING", candidate.reason_codes)
        self.assertGreater(candidate.risk_event_score, 0)
        self.assertEqual(result.run_log.source_modes["stock_issuance"], "disabled_optional")
        self.assertIn("stock issuance API is disabled_optional", " ".join(result.run_log.notes))

    def test_review_cli_summarizes_fixture_run(self):
        with tempfile.TemporaryDirectory() as output_dir:
            KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

            summary = build_review_summary(output_dir, AS_OF.isoformat())
            rendered = render_review_summary(summary)

        self.assertGreater(summary.total_candidates, 0)
        self.assertIn("opendart", summary.source_modes)
        self.assertIn("total candidates", rendered)
        self.assertIn("manual review required", rendered)

    def test_review_cli_renders_targeted_score_state_drivers(self):
        summary = KoreaRunReviewSummary(
            as_of_date=AS_OF.isoformat(),
            total_candidates=1,
            event_search_count=0,
            deep_research_count=0,
            targeted_score_states=(
                "009999 stage=0 stage_status=pending_invalid_score stage_final=False display_stage=pending stage_pending_reason=theme_route_provider_error visible_score=pending valid=False reason=theme_route_provider_error fingerprint=abc input_fingerprint=input123 drivers=score_invalid:theme_route_provider_error",
            ),
        )

        rendered = render_review_summary(summary)

        self.assertIn("targeted score states", rendered)
        self.assertIn("stage_status=pending_invalid_score", rendered)
        self.assertIn("stage_final=False", rendered)
        self.assertIn("display_stage=pending", rendered)
        self.assertIn("stage_pending_reason=theme_route_provider_error", rendered)
        self.assertIn("visible_score=pending", rendered)
        self.assertIn("score_invalid:theme_route_provider_error", rendered)

    def test_review_cli_prefers_visible_score_over_compat_score_total(self):
        states = _targeted_score_states(
            (
                {
                    "symbol": "009999",
                    "stage": Stage.STAGE_3_YELLOW,
                    "visible_score": 65,
                    "score_total": 12,
                    "score_valid": True,
                    "score_fingerprint": "scorefp",
                    "research_input_fingerprint": "inputfp",
                    "score_variability_drivers": ("research_input_fingerprint:inputfp",),
                },
            )
        )

        self.assertEqual(len(states), 1)
        self.assertIn("visible_score=65", states[0])
        self.assertIn("stage_status=final", states[0])
        self.assertIn("stage_final=True", states[0])
        self.assertIn("display_stage=3-Yellow", states[0])
        self.assertIn("stage_pending_reason=none", states[0])
        self.assertIn("contract=valid_score_alias_mismatch:score_total", states[0])
        self.assertNotIn("score=12", states[0])

    def test_review_cli_does_not_display_invalid_compat_score_as_visible(self):
        states = _targeted_score_states(
            (
                {
                    "symbol": "009999",
                    "stage": "0",
                    "score_total": 82,
                    "score_valid": False,
                    "score_blocked_reason": "score_gap_unresolved",
                    "raw_score_before_block": 82,
                    "score_fingerprint": "blocked-scorefp",
                    "research_input_fingerprint": "inputfp",
                    "score_variability_drivers": ("raw_score_before_block:82",),
                },
                {
                    "symbol": "008888",
                    "stage": "0",
                    "score": 77,
                    "score_blocked_reason": "theme_route_unresolved",
                    "score_fingerprint": "blocked-scorefp-2",
                    "research_input_fingerprint": "inputfp-2",
                    "score_variability_drivers": ("score_invalid:theme_route_unresolved",),
                },
            )
        )

        self.assertEqual(len(states), 2)
        self.assertIn(
            "009999 stage=0 stage_status=pending_invalid_score stage_final=False display_stage=pending stage_pending_reason=score_gap_unresolved visible_score=pending",
            states[0],
        )
        self.assertIn(
            "008888 stage=0 stage_status=pending_invalid_score stage_final=False display_stage=pending stage_pending_reason=theme_route_unresolved visible_score=pending",
            states[1],
        )
        self.assertIn("contract=invalid_compat_score_present:score_total", states[0])
        self.assertIn("contract=invalid_compat_score_present:score", states[1])
        self.assertNotIn("visible_score=82", " | ".join(states))
        self.assertNotIn("visible_score=77", " | ".join(states))

    def test_review_cli_uses_explicit_stage_output_status_for_pending_rows(self):
        states = _targeted_score_states(
            (
                {
                    "symbol": "005930",
                    "stage": "0",
                    "stage_output_status": "pending_agentic_evidence",
                    "stage_is_final": False,
                    "stage_display_stage": None,
                    "stage_pending_reason": "PENDING_MATERIAL_GAPS",
                    "visible_score": None,
                    "score_valid": False,
                    "score_blocked_reason": "theme_route_needs_more_evidence",
                    "score_fingerprint": "scorefp",
                    "research_input_fingerprint": "inputfp",
                    "agentic_evidence_status": "provider_error",
                    "agentic_evidence_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "agentic_evidence_archetype_source": "context_contract_relevance",
                },
            )
        )

        self.assertEqual(len(states), 1)
        self.assertIn(
            "005930 stage=0 stage_status=pending_agentic_evidence stage_final=False display_stage=pending stage_pending_reason=PENDING_MATERIAL_GAPS visible_score=pending",
            states[0],
        )
        self.assertNotIn("display_stage=0", states[0])
        self.assertIn("agentic_status=provider_error", states[0])
        self.assertIn("agentic_archetype=C06_HBM_MEMORY_CUSTOMER_CAPACITY", states[0])
        self.assertIn("agentic_source=context_contract_relevance", states[0])

    def test_review_cli_does_not_display_conflicting_valid_aliases_as_visible(self):
        states = _targeted_score_states(
            (
                {
                    "symbol": "006666",
                    "stage": "3-Yellow",
                    "score": 82,
                    "score_total": 90,
                    "score_valid": True,
                    "score_fingerprint": "legacy-conflict-scorefp",
                    "research_input_fingerprint": "inputfp",
                    "score_variability_drivers": ("legacy_alias_conflict",),
                },
            )
        )
        changes = _targeted_score_changes(
            (
                {
                    "symbol": "006666",
                    "score": 82,
                    "score_total": 90,
                    "score_valid": True,
                    "score_fingerprint": "legacy-conflict-scorefp",
                    "research_input_fingerprint": "inputfp",
                },
            ),
            (
                {
                    "symbol": "006666",
                    "visible_score": 65,
                    "score_valid": True,
                    "score_fingerprint": "valid-scorefp",
                    "research_input_fingerprint": "inputfp",
                },
            ),
        )

        self.assertEqual(len(states), 1)
        self.assertIn(
            "006666 stage=3-Yellow stage_status=pending_invalid_score stage_final=False display_stage=pending stage_pending_reason=score_alias_conflict visible_score=pending valid=False reason=score_alias_conflict",
            states[0],
        )
        self.assertIn("contract=score_alias_conflict,valid_visible_score_missing", states[0])
        self.assertNotIn("visible_score=82", states[0])
        self.assertNotIn("visible_score=90", states[0])
        self.assertIn("change=score_became_valid", changes[0])
        self.assertIn("before=pending", changes[0])
        self.assertIn("after=65", changes[0])
        self.assertIn("score_alias_conflict", changes[0])

    def test_review_cli_treats_score_without_validity_as_pending(self):
        states = _targeted_score_states(
            (
                {
                    "symbol": "007777",
                    "stage": "3-Yellow",
                    "score_total": 82,
                    "score_fingerprint": "legacy-scorefp",
                    "research_input_fingerprint": "legacy-inputfp",
                },
            )
        )
        changes = _targeted_score_changes(
            (
                {
                    "symbol": "007777",
                    "score_total": 82,
                    "score_fingerprint": "legacy-scorefp",
                    "research_input_fingerprint": "legacy-inputfp",
                },
            ),
            (
                {
                    "symbol": "007777",
                    "visible_score": 65,
                    "score_valid": True,
                    "score_fingerprint": "new-scorefp",
                    "research_input_fingerprint": "new-inputfp",
                },
            ),
        )

        self.assertIn(
            "007777 stage=3-Yellow stage_status=pending_invalid_score stage_final=False display_stage=pending stage_pending_reason=score_valid_missing visible_score=pending",
            states[0],
        )
        self.assertIn("contract=invalid_compat_score_present:score_total", states[0])
        self.assertNotIn("visible_score=82", states[0])
        self.assertIn("before=pending", changes[0])
        self.assertIn("after=65", changes[0])
        self.assertIn("score_valid_missing", changes[0])

    def test_live_lite_run_log_contract_audit_catches_legacy_compat_score_rows(self):
        findings = _score_state_contract_findings_for_outputs(
            as_of_date=AS_OF,
            candidates=(),
            targeted_smoke_results=(
                {
                    "symbol": "005930",
                    "stage": "2",
                    "visible_score": None,
                    "score_total": 68.9,
                    "score_valid": True,
                },
            ),
        )

        self.assertIn("targeted_smoke_results[0]:valid_visible_score_missing", findings)

    def test_live_lite_run_log_contract_audit_requires_visible_score_field(self):
        findings = _score_state_contract_findings_for_outputs(
            as_of_date=AS_OF,
            candidates=(),
            targeted_smoke_results=(
                {
                    "symbol": "000660",
                    "stage": "0",
                    "score_valid": False,
                    "score_blocked_reason": "theme_route_provider_error",
                },
            ),
        )

        self.assertIn("targeted_smoke_results[0]:visible_score_field_missing", findings)

    def test_score_gap_audit_events_from_rows_are_append_only_and_deduped(self):
        targeted_events = (
            {
                "event_id": "SGAUD-1",
                "symbol": "005930",
                "round_index": 0,
                "progress_reason": "score_gap_changed_score_state",
            },
        )
        theme_events = (
            {
                "event_id": "SGAUD-1",
                "symbol": "005930",
                "round_index": 0,
                "progress_reason": "score_gap_changed_score_state",
            },
            {
                "event_id": "SGAUD-2",
                "symbol": "000660",
                "round_index": 1,
                "progress_reason": "score_gap_new_documents_without_claims",
            },
        )

        events = _score_gap_audit_events_from_rows(
            (
                {
                    "symbol": "005930",
                    "post_score_gap_audit_events": targeted_events,
                },
            ),
            (
                {
                    "symbol": "005930",
                    "post_score_gap_audit_events": theme_events,
                },
            ),
        )

        self.assertEqual([item["event_id"] for item in events], ["SGAUD-1", "SGAUD-2"])
        self.assertEqual(events[0]["row_path"], "targeted_smoke_results")
        self.assertEqual(events[1]["row_path"], "theme_routes")
        self.assertEqual(events[1]["progress_reason"], "score_gap_new_documents_without_claims")

    def test_score_gap_source_route_plans_from_rows_are_deduped_and_enriched(self):
        targeted_plan = {
            "task_id": "runtime-follow-up",
            "primitive_gap": "hbm_capacity_pre_sold",
            "query": "TargetIssuer capacity official",
            "selected_candidate_ids": ("SRC-1",),
            "stop_reason": "first_official_candidate",
        }
        theme_plan = {
            "task_id": "runtime-follow-up",
            "primitive_gap": "hbm_capacity_pre_sold",
            "query": "TargetIssuer capacity official",
            "selected_candidate_ids": ("SRC-1",),
            "stop_reason": "first_official_candidate",
        }
        second_theme_plan = {
            "task_id": "runtime-follow-up-revenue",
            "primitive_gap": "revenue_visibility_contract",
            "query": "TargetIssuer revenue contract",
            "selected_candidate_ids": ("SRC-2", "SRC-3"),
            "stop_reason": "source_quorum_two_independent_tier2",
        }

        plans = _score_gap_source_route_plans_from_rows(
            (
                {
                    "symbol": "000660",
                    "post_score_gap_source_route_plans": (targeted_plan,),
                },
            ),
            (
                {
                    "symbol": "000660",
                    "post_score_gap_source_route_plans": (theme_plan, second_theme_plan),
                },
            ),
        )

        self.assertEqual(
            [item["task_id"] for item in plans],
            ["runtime-follow-up", "runtime-follow-up-revenue"],
        )
        self.assertEqual(plans[0]["row_path"], "targeted_smoke_results")
        self.assertEqual(plans[1]["row_path"], "theme_routes")
        self.assertEqual(plans[1]["stop_reason"], "source_quorum_two_independent_tier2")

    def test_review_cli_classifies_targeted_score_changes(self):
        changes = _targeted_score_changes(
            (
                {
                    "symbol": "009999",
                    "visible_score": 82,
                    "score_valid": True,
                    "score_fingerprint": "score-a",
                    "research_input_fingerprint": "input-a",
                    "component_scores": {"earnings_visibility": 18},
                },
            ),
            (
                {
                    "symbol": "009999",
                    "visible_score": 65,
                    "score_valid": True,
                    "score_fingerprint": "score-b",
                    "research_input_fingerprint": "input-b",
                    "score_components": {"earnings_visibility_score": 10},
                },
            ),
        )

        self.assertEqual(len(changes), 1)
        self.assertIn("change=input_changed", changes[0])
        self.assertIn("before=82", changes[0])
        self.assertIn("after=65", changes[0])
        self.assertIn("delta=-17", changes[0])
        self.assertIn("component_delta:earnings_visibility=-8", changes[0])

    def test_review_cli_flags_unexplained_targeted_score_delta(self):
        failures = _targeted_score_audit_failures(
            (
                {
                    "symbol": "005930",
                    "visible_score": 92,
                    "score_valid": True,
                    "score_fingerprint": "score-a",
                    "research_input_fingerprint": "input-a",
                    "score_contribution_ledger": [
                        {
                            "component_key": "total",
                            "criterion_id": "verified_score",
                            "raw_points": 92,
                            "max_points": 100,
                            "support_claim_ids": ["CLM-SAME"],
                        }
                    ],
                },
            ),
            (
                {
                    "symbol": "005930",
                    "visible_score": 63,
                    "score_valid": True,
                    "score_fingerprint": "score-b",
                    "research_input_fingerprint": "input-a",
                    "score_contribution_ledger": [
                        {
                            "component_key": "total",
                            "criterion_id": "verified_score",
                            "raw_points": 63,
                            "max_points": 100,
                            "support_claim_ids": ["CLM-SAME"],
                        }
                    ],
                },
            ),
        )

        self.assertEqual(failures, ("005930:critical:total/verified_score=-29",))

    def test_review_cli_keeps_missing_targeted_score_rows_visible(self):
        changes = _targeted_score_changes(
            (
                {
                    "symbol": "009999",
                    "visible_score": 82,
                    "score_valid": True,
                    "score_fingerprint": "score-a",
                    "research_input_fingerprint": "input-a",
                },
            ),
            (),
        )

        self.assertEqual(len(changes), 1)
        self.assertIn("009999 change=missing_after_state", changes[0])

    def test_review_cli_exit_gate_fails_on_score_delta_audit(self):
        with tempfile.TemporaryDirectory() as previous_dir, tempfile.TemporaryDirectory() as current_dir:
            previous_root = Path(previous_dir) / "korea_live_lite"
            current_root = Path(current_dir) / "korea_live_lite"
            previous_root.mkdir()
            current_root.mkdir()
            for root in (previous_root, current_root):
                (root / f"{AS_OF.isoformat()}_candidates.json").write_text('{"candidates":[]}', encoding="utf-8")
                (root / f"{AS_OF.isoformat()}_evidence.json").write_text('{"evidence":[]}', encoding="utf-8")
                (root / f"{AS_OF.isoformat()}_brief.md").write_text("", encoding="utf-8")
            (previous_root / f"{AS_OF.isoformat()}_run_log.json").write_text(
                json.dumps(
                    {
                        "targeted_smoke_results": [
                            {
                                "symbol": "005930",
                                "visible_score": 92,
                                "score_valid": True,
                                "score_fingerprint": "score-a",
                                "research_input_fingerprint": "input-a",
                                "score_contribution_ledger": [
                                    {
                                        "component_key": "total",
                                        "criterion_id": "verified_score",
                                        "raw_points": 92,
                                        "max_points": 100,
                                        "support_claim_ids": ["CLM-SAME"],
                                    }
                                ],
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            (current_root / f"{AS_OF.isoformat()}_run_log.json").write_text(
                json.dumps(
                    {
                        "targeted_smoke_results": [
                            {
                                "symbol": "005930",
                                "visible_score": 63,
                                "score_valid": True,
                                "score_fingerprint": "score-b",
                                "research_input_fingerprint": "input-a",
                                "score_contribution_ledger": [
                                    {
                                        "component_key": "total",
                                        "criterion_id": "verified_score",
                                        "raw_points": 63,
                                        "max_points": 100,
                                        "support_claim_ids": ["CLM-SAME"],
                                    }
                                ],
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )

            stdout = io.StringIO()
            with patch("sys.stdout", new=stdout):
                exit_code = review_korea_run_main(
                    [
                        AS_OF.isoformat(),
                        "--output-directory",
                        current_dir,
                        "--previous-output-directory",
                        previous_dir,
                        "--fail-on-score-delta-audit",
                    ]
                )

        self.assertEqual(exit_code, 2)
        self.assertIn("targeted score audit failures: 005930:critical:total/verified_score=-29", stdout.getvalue())

    def test_review_summary_compares_previous_output_directory(self):
        with tempfile.TemporaryDirectory() as previous_dir, tempfile.TemporaryDirectory() as current_dir:
            previous_root = Path(previous_dir) / "korea_live_lite"
            current_root = Path(current_dir) / "korea_live_lite"
            previous_root.mkdir()
            current_root.mkdir()
            for root in (previous_root, current_root):
                (root / f"{AS_OF.isoformat()}_candidates.json").write_text('{"candidates":[]}', encoding="utf-8")
                (root / f"{AS_OF.isoformat()}_evidence.json").write_text('{"evidence":[]}', encoding="utf-8")
                (root / f"{AS_OF.isoformat()}_brief.md").write_text("", encoding="utf-8")
            (previous_root / f"{AS_OF.isoformat()}_run_log.json").write_text(
                json.dumps(
                    {
                        "targeted_smoke_results": [
                            {
                                "symbol": "009999",
                                "visible_score": 82,
                                "score_valid": True,
                                "score_fingerprint": "score-a",
                                "research_input_fingerprint": "input-a",
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            (current_root / f"{AS_OF.isoformat()}_run_log.json").write_text(
                json.dumps(
                    {
                        "targeted_smoke_results": [
                            {
                                "symbol": "009999",
                                "visible_score": 65,
                                "score_valid": True,
                                "score_fingerprint": "score-b",
                                "research_input_fingerprint": "input-b",
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )

            summary = build_review_summary(
                current_dir,
                AS_OF.isoformat(),
                previous_output_directory=previous_dir,
            )
            rendered = render_review_summary(summary)

        self.assertEqual(len(summary.targeted_score_changes), 1)
        self.assertIn("change=input_changed", summary.targeted_score_changes[0])
        self.assertEqual(summary.score_state_contract_findings, ())
        self.assertIn("targeted score changes", rendered)
        self.assertIn("score state contract: ok", rendered)
        self.assertIn("delta=-17", rendered)

    def test_review_summary_reports_score_state_contract_findings_with_paths(self):
        with tempfile.TemporaryDirectory() as output_dir:
            root = Path(output_dir) / "korea_live_lite"
            root.mkdir()
            (root / f"{AS_OF.isoformat()}_candidates.json").write_text(
                json.dumps(
                    {
                        "candidates": [
                            {
                                "symbol": "005930",
                                "score": 82,
                                "score_valid": True,
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            (root / f"{AS_OF.isoformat()}_evidence.json").write_text('{"evidence":[]}', encoding="utf-8")
            (root / f"{AS_OF.isoformat()}_brief.md").write_text("", encoding="utf-8")
            (root / f"{AS_OF.isoformat()}_run_log.json").write_text(
                json.dumps(
                    {
                        "targeted_smoke_results": [
                            {
                                "symbol": "009999",
                                "visible_score": 65,
                                "score_total": 12,
                                "score_valid": True,
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )

            summary = build_review_summary(output_dir, AS_OF.isoformat())
            rendered = render_review_summary(summary)

        self.assertIn("candidates[0]:valid_visible_score_missing", summary.score_state_contract_findings)
        self.assertIn("candidates[0]:visible_score_field_missing", summary.score_state_contract_findings)
        self.assertIn("targeted_smoke_results[0]:valid_score_alias_mismatch:score_total", summary.score_state_contract_findings)
        self.assertIn("score state contract:", rendered)
        self.assertIn("candidates[0]:valid_visible_score_missing", rendered)
        self.assertIn("candidates[0]:visible_score_field_missing", rendered)
        self.assertIn("targeted_smoke_results[0]:valid_score_alias_mismatch:score_total", rendered)

    def test_opendart_disclosure_collection_is_date_based_not_per_symbol(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        self.assertGreater(result.cheap_scan.instruments_scanned, 1)
        self.assertEqual(result.run_log.source_call_counts["opendart_disclosure_date_range"], 1)
        self.assertEqual(result.run_log.source_call_counts["opendart_symbol_disclosure_calls"], 0)

    def test_date_based_disclosure_collection_contains_multiple_symbols(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        disclosure_symbols = {item.symbol for item in result.evidence if item.source_type == "disclosure"}
        self.assertGreaterEqual(len(disclosure_symbols), 3)
        self.assertIn("111111", disclosure_symbols)
        self.assertIn("222222", disclosure_symbols)

    def test_no_disclosure_instrument_is_still_evaluated_by_price_sensor(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        candidate = _candidate(result, "444444")
        self.assertEqual(candidate.recommended_next_layer.value, "event_search")
        self.assertIn("PRICE_VOLUME_SPIKE", candidate.reason_codes)
        self.assertFalse(any(code.startswith("DISC_") for code in candidate.reason_codes))
        self.assertEqual(candidate.evidence_ids, ())

    def test_no_disclosure_instrument_can_become_event_search_via_financial_rules(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        candidate = _candidate(result, "777777")
        self.assertEqual(candidate.recommended_next_layer.value, "event_search")
        self.assertIn("FIN_OP_TURNAROUND", candidate.reason_codes)
        self.assertIn("FIN_FCF_TURNAROUND", candidate.reason_codes)
        self.assertFalse(any(code.startswith("DISC_") for code in candidate.reason_codes))

    def test_page_request_builder_emits_page_metadata(self):
        requests = build_opendart_date_range_requests(
            date(2024, 5, 20),
            date(2024, 5, 21),
            AS_OF,
            page_count=50,
            max_pages=3,
        )

        self.assertEqual([item.params["page_no"] for item in requests], [1, 2, 3])
        self.assertTrue(all(item.params["page_count"] == 50 for item in requests))
        self.assertTrue(all(item.params["bgn_de"] == "20240520" for item in requests))
        self.assertTrue(all(item.params["end_de"] == "20240521" for item in requests))

    def test_opendart_detail_fetch_requests_are_planned_only_for_watch_disclosures(self):
        watch = _disclosure("111111", "단일판매·공급계약체결", "202405210001")
        ignored = _disclosure("222222", "투자설명서", "202405210002")

        requests = plan_opendart_detail_fetches((watch, ignored), AS_OF)

        self.assertEqual(len(requests), 1)
        self.assertEqual(requests[0].url, "https://opendart.fss.or.kr/api/document.xml")
        self.assertEqual(requests[0].params["rcept_no"], "202405210001")
        self.assertEqual(requests[0].params["symbol"], "111111")
        self.assertNotIn("crtfc_key", requests[0].params)

    def test_opendart_detail_fetch_executes_with_cap_and_writes_text_cache(self):
        detail_xml = """
        <DOCUMENT>
          <SECTION-1>
            계약금액: 4,000억원
            최근매출액 대비: 45%
            계약기간: 2024.05.21 ~ 2027.05.20
            계약상대방: 북미 유틸리티
            계약내용: 초고압변압기
          </SECTION-1>
        </DOCUMENT>
        """
        http_client = MockHttpClient(
            json_by_url_token={
                "opendart": {
                    "total_page": 1,
                    "list": [
                        {
                            "stock_code": "111111",
                            "corp_name": "한전변압기",
                            "report_nm": "단일판매·공급계약체결",
                            "rcept_no": "202405210091",
                            "rcept_dt": "20240521",
                        },
                        {
                            "stock_code": "222222",
                            "corp_name": "케이전력",
                            "report_nm": "신규시설투자",
                            "rcept_no": "202405210092",
                            "rcept_dt": "20240521",
                        },
                    ],
                }
            },
            text_by_url_token={"202405210091": detail_xml, "202405210092": detail_xml},
        )
        env = {"OPENDART_API_KEY": "OPENDART_SECRET"}

        with tempfile.TemporaryDirectory() as output_dir, tempfile.TemporaryDirectory() as cache_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    cache_directory=cache_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    http_client=http_client,
                    budget=KoreaLiveLiteBudget(max_opendart_detail_fetches_per_run=1),
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

            detail_cache_dir = Path(cache_dir) / "opendart_detail" / AS_OF.isoformat()
            self.assertTrue((detail_cache_dir / "202405210091.xml").exists())
            self.assertTrue((detail_cache_dir / "202405210091.txt").exists())

        self.assertEqual(len(result.run_log.executed_opendart_detail_requests), 1)
        self.assertTrue(result.run_log.skipped_opendart_detail_requests)
        self.assertEqual(
            result.run_log.skipped_opendart_detail_requests[0]["reason"],
            "global_detail_fetch_cap_reached",
        )
        self.assertEqual(result.run_log.opendart_detail_fetch_policy["per_symbol_cap"], 3)
        self.assertTrue(result.run_log.opendart_detail_fetch_policy["stop_on_resolved_report_type"])
        self.assertEqual(result.run_log.source_call_counts["opendart_detail_fetches"], 1)
        detail_evidence = [item for item in result.evidence if item.source_name == "OpenDART detail"]
        self.assertEqual(len(detail_evidence), 1)
        self.assertEqual(detail_evidence[0].parsed_fields["contract_amount_to_prior_sales"], 0.45)
        self.assertGreaterEqual(detail_evidence[0].confidence, 0.7)

    def test_opendart_detail_fetch_stops_after_resolved_report_type_per_symbol(self):
        detail_xml = """
        <DOCUMENT>
          <SECTION-1>
            계약금액: 4,000억원
            최근매출액 대비: 45%
            계약기간: 2024.05.21 ~ 2027.05.20
          </SECTION-1>
        </DOCUMENT>
        """
        disclosures = (
            _disclosure("111111", "단일판매·공급계약체결", "202405210091"),
            _disclosure("111111", "단일판매·공급계약체결", "202405210092"),
            _disclosure("111111", "신규시설투자", "202405210093"),
        )
        planned = plan_opendart_detail_fetches(disclosures, AS_OF)
        http_client = MockHttpClient(
            json_by_url_token={},
            text_by_url_token={
                "202405210091": detail_xml,
                "202405210092": detail_xml,
                "202405210093": detail_xml,
            },
        )
        env = {"OPENDART_API_KEY": "OPENDART_SECRET"}

        with tempfile.TemporaryDirectory() as cache_dir, patch.dict("os.environ", env, clear=True):
            detail_events, executed, skipped = _execute_opendart_detail_fetches(
                base_disclosures=disclosures,
                planned_requests=planned,
                as_of_date=AS_OF,
                config=KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    cache_directory=cache_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    opendart_detail_fetch_max_per_symbol=3,
                    opendart_detail_fetch_stop_on_resolved_report_type=True,
                ),
                http_client=http_client,
                built_requests=[],
                source_call_counts={"opendart_detail_fetches": 0},
            )

        self.assertEqual([item.rcept_no for item in detail_events], ["202405210091", "202405210093"])
        self.assertEqual([item.params["rcept_no"] for item in executed], ["202405210091", "202405210093"])
        self.assertEqual(skipped[0]["rcept_no"], "202405210092")
        self.assertEqual(skipped[0]["reason"], "report_type_already_resolved_for_symbol")

    def test_opendart_detail_fetch_per_symbol_cap_skips_remaining_requests(self):
        detail_xml = "<DOCUMENT><SECTION-1>계약금액: 4,000억원</SECTION-1></DOCUMENT>"
        disclosures = (
            _disclosure("111111", "단일판매·공급계약체결", "202405210091"),
            _disclosure("111111", "신규시설투자", "202405210092"),
        )
        planned = plan_opendart_detail_fetches(disclosures, AS_OF)
        http_client = MockHttpClient(
            json_by_url_token={},
            text_by_url_token={"202405210091": detail_xml, "202405210092": detail_xml},
        )
        env = {"OPENDART_API_KEY": "OPENDART_SECRET"}

        with tempfile.TemporaryDirectory() as cache_dir, patch.dict("os.environ", env, clear=True):
            detail_events, executed, skipped = _execute_opendart_detail_fetches(
                base_disclosures=disclosures,
                planned_requests=planned,
                as_of_date=AS_OF,
                config=KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    cache_directory=cache_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    opendart_detail_fetch_max_per_symbol=1,
                ),
                http_client=http_client,
                built_requests=[],
                source_call_counts={"opendart_detail_fetches": 0},
            )

        self.assertEqual(len(detail_events), 1)
        self.assertEqual([item.params["rcept_no"] for item in executed], ["202405210091"])
        self.assertEqual(skipped[0]["rcept_no"], "202405210092")
        self.assertEqual(skipped[0]["reason"], "per_symbol_detail_fetch_cap_reached")

    def test_agentic_official_follow_up_provider_uses_opendart_detail_disclosures(self):
        detail = DisclosureEvent(
            symbol="111111",
            source="OpenDART detail",
            report_type="단일판매·공급계약체결",
            title="한전변압기 단일판매 공급계약",
            published_at=datetime(2024, 5, 21, 9, 0),
            observed_at=datetime(2024, 5, 21, 9, 0),
            available_at=datetime(2024, 5, 21, 9, 0),
            as_of_date=AS_OF,
            rcept_no="202405210091",
            raw_text="계약금액: 4,000억원\n계약상대방: 북미 유틸리티\n계약기간: 2024.05.21 ~ 2027.05.20",
            parsed_fields={"detail_fetched": True, "contract_amount_to_prior_sales": 0.45},
        )
        sources = _sources_with_date_disclosures(
            KoreaCheapScanSources(opendart=OpenDARTConnector(fixture_mode=True)),
            (detail,),
        )
        candidate = CheapScanCandidate(
            symbol="111111",
            company_name="한전변압기",
            market=Market.KR,
            as_of_date=AS_OF,
        )

        provider = _official_follow_up_source_provider(
            config=KoreaLiveLiteConfig(as_of_date=AS_OF),
            sources=sources,
            candidate=candidate,
            detail_disclosures=(detail,),
        )
        self.assertIsNotNone(provider)
        results = provider.search("계약금액 북미 유틸리티", AS_OF, max_results=5)
        urls = {item.url for item in results}

        self.assertIn("opendart-detail://111111/202405210091", urls)
        self.assertIn("계약상대방", provider.fixture_text_by_url()["opendart-detail://111111/202405210091"])

    def test_event_and_deep_research_symbol_budgets_are_respected(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    budget=KoreaLiveLiteBudget(
                        max_symbols_for_event_search=1,
                        max_symbols_for_deep_research=0,
                        max_naver_search_calls_per_day=1,
                    ),
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        skipped_reasons = {item.reason for item in result.run_log.skipped_candidates}
        self.assertIn("deep_research_symbol_budget_exhausted", skipped_reasons)
        self.assertIn("event_search_symbol_budget_exhausted", skipped_reasons)
        self.assertLessEqual(result.run_log.source_call_counts["naver_search_queries"], 1)
        self.assertTrue(result.run_log.skipped_queries)
        self.assertLessEqual(len(result.web_results), 1)

    def test_stage_3_green_requires_cross_evidence_in_live_lite(self):
        url = "https://ssl.pstatic.net/imgstock/upload/research/company/price_report.pdf"
        provider = FixtureSearchProvider(
            results_by_query={
                "가격만강세 수주잔고": (
                    SearchResult(
                        title="가격만강세 줄을 서시오",
                        url=url,
                        source="FixtureBroker",
                        published_at=datetime(2024, 5, 21, 8),
                        query="가격만강세 수주잔고",
                        rank=1,
                        is_pdf=True,
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                )
            }
        )
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    budget=KoreaLiveLiteBudget(
                        max_symbols_for_event_search=10,
                        max_symbols_for_deep_research=10,
                        max_naver_search_calls_per_day=100,
                    ),
                    browser_provider=provider,
                    free_search_provider=EmptySearchProvider(),
                    fixture_text_by_url={url: STRONG_SINGLE_REPORT_TEXT},
                )
            )

        stage_by_symbol = {item.stage.symbol: item.stage for item in result.web_results}
        self.assertEqual(stage_by_symbol["444444"].stage, Stage.STAGE_3_YELLOW)
        self.assertIn("at least two independent evidence types", " ".join(stage_by_symbol["444444"].stage_reason))

    def test_targeted_smoke_without_evidence_is_not_production_or_green(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    targeted_smoke_enabled=True,
                    targeted_smoke_symbol="009999",
                    targeted_smoke_company="스모크테스트",
                    budget=KoreaLiveLiteBudget(
                        max_symbols_for_event_search=20,
                        max_symbols_for_deep_research=20,
                        max_naver_search_calls_per_day=100,
                    ),
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )
            brief_text = result.brief_path.read_text(encoding="utf-8")

        self.assertFalse(any(item.candidate_source_path == "targeted_smoke" for item in result.candidates))
        self.assertTrue(result.run_log.targeted_smoke_results)
        smoke = next(item for item in result.run_log.targeted_smoke_results if item["symbol"] == "009999")
        self.assertEqual(smoke["status"], "evidence_pending_expansion")
        self.assertFalse(smoke["production_candidate"])
        self.assertNotEqual(smoke["stage"], Stage.STAGE_3_GREEN.value)
        self.assertNotIn("스모크테스트", brief_text)

    def test_targeted_smoke_runs_even_when_event_symbol_budget_is_zero(self):
        url = "https://news.example.com/smoke"
        provider = FixtureSearchProvider(
            results_by_query={
                "스모크테스트 수주잔고": (
                    SearchResult(
                        title="스모크테스트 수주잔고 증가",
                        url=url,
                        snippet="수주잔고와 매출 성장",
                        source="fixture-news",
                        query="스모크테스트 수주잔고",
                        confidence=0.8,
                    ),
                )
            }
        )
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    targeted_smoke_enabled=True,
                    targeted_smoke_symbol="009999",
                    targeted_smoke_company="스모크테스트",
                    targeted_smoke_queries=("스모크테스트 수주잔고",),
                    budget=KoreaLiveLiteBudget(
                        max_symbols_for_event_search=0,
                        max_symbols_for_deep_research=0,
                        max_naver_search_calls_per_day=10,
                    ),
                    browser_provider=provider,
                    free_search_provider=EmptySearchProvider(),
                    fixture_text_by_url={url: "스모크테스트 수주잔고 증가와 매출 성장"},
                )
            )

        smoke = next(item for item in result.run_log.targeted_smoke_results if item["symbol"] == "009999")
        self.assertEqual(smoke["status"], "evidence_found")
        self.assertFalse(any(item.candidate_source_path == "targeted_smoke" for item in result.candidates))

    def test_targeted_smoke_only_runs_injected_candidate_and_skips_production_candidates(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    targeted_smoke_enabled=True,
                    targeted_smoke_only=True,
                    targeted_smoke_symbol="009999",
                    targeted_smoke_company="스모크테스트",
                    targeted_smoke_queries=("스모크테스트 수주잔고",),
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        self.assertEqual(tuple(item.stage.symbol for item in result.web_results), ("009999",))
        self.assertTrue(result.run_log.targeted_smoke_results)
        self.assertEqual(result.cheap_scan.instruments_scanned, 0)
        self.assertFalse(result.candidates)
        self.assertFalse(result.run_log.skipped_candidates)

    def test_targeted_smoke_marks_score_invalid_when_theme_route_provider_errors(self):
        url = "https://news.example.com/smoke-route-error"
        provider = FixtureSearchProvider(
            results_by_query={
                "스모크테스트 수주잔고": (
                    SearchResult(
                        title="스모크테스트 수주잔고 증가",
                        url=url,
                        snippet="수주잔고와 매출 성장",
                        source="fixture-news",
                        query="스모크테스트 수주잔고",
                        confidence=0.8,
                    ),
                )
            }
        )
        route_provider = FakeThemeRouteProvider(
            output=ThemeRouteOutput(
                status="provider_error",
                blocked_reason="provider returned no valid route json",
            )
        )
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    targeted_smoke_enabled=True,
                    targeted_smoke_symbol="009999",
                    targeted_smoke_company="스모크테스트",
                    targeted_smoke_queries=("스모크테스트 수주잔고",),
                    budget=KoreaLiveLiteBudget(
                        max_symbols_for_event_search=0,
                        max_symbols_for_deep_research=0,
                        max_naver_search_calls_per_day=10,
                    ),
                    browser_provider=provider,
                    free_search_provider=EmptySearchProvider(),
                    fixture_text_by_url={url: "스모크테스트 수주잔고 증가와 매출 성장"},
                    theme_rebalance_enabled=True,
                    theme_route_provider=route_provider,
                    theme_evidence_review_enabled=False,
                )
            )

        smoke = next(item for item in result.run_log.targeted_smoke_results if item["symbol"] == "009999")
        self.assertEqual(smoke["status"], "score_blocked_theme_route")
        self.assertFalse(smoke["score_valid"])
        self.assertIsNone(smoke["visible_score"])
        self.assertIsNone(smoke["score_total"])
        self.assertEqual(smoke["score_blocked_reason"], "theme_route_provider_error")
        self.assertEqual(smoke["theme_route_blocked_reason"], "provider returned no valid route json")
        self.assertEqual(smoke["theme_route_timeout_seconds"], 60.0)
        self.assertIsNotNone(smoke["raw_score_total_before_theme_route_block"])
        self.assertEqual(smoke["stage"], Stage.STAGE_0)
        self.assertEqual(smoke["stage_output_status"], "pending_invalid_score")
        self.assertFalse(smoke["stage_is_final"])
        self.assertIsNone(smoke["stage_display_stage"])
        self.assertEqual(smoke["stage_pending_reason"], "theme_route_provider_error")
        self.assertIn("score_invalid:theme_route_provider_error", smoke["score_variability_drivers"])
        self.assertIn("theme_rebalance_status:provider_error", smoke["score_variability_drivers"])
        self.assertIn("theme_route_status:provider_error", smoke["score_variability_drivers"])

    def test_targeted_smoke_validity_uses_score_snapshot_even_if_diagnostics_string_is_true(self):
        score = ScoreSnapshot(
            symbol="009999",
            as_of_date=AS_OF,
            eps_fcf_explosion_score=0,
            earnings_visibility_score=0,
            bottleneck_pricing_score=0,
            market_mispricing_score=0,
            valuation_rerating_score=0,
            capital_allocation_score=0,
            information_confidence_score=0,
            risk_penalty=0,
            total_score=0,
            diagnostic_scores={
                "score_valid": 0.0,
                "score_blocked_by_score_gap": 100.0,
                "raw_score_total_before_score_gap_block": 68.9,
            },
        )
        result = SimpleNamespace(score=score, theme_route_diagnostics={"score_valid": "true"})

        self.assertFalse(_result_score_valid(result))
        self.assertEqual(_score_blocked_status("score_gap_llm_no_suggested_queries"), "score_blocked_score_gap")

    def test_theme_route_row_exposes_agentic_stage_court_runtime_output(self):
        candidate = SimpleNamespace(
            symbol="009999",
            company_name="스모크테스트",
            candidate_source_path="targeted_smoke",
        )
        result = SimpleNamespace(
            theme_route_diagnostics={
                "agentic_evidence_enabled": True,
                "agentic_evidence_required_for_scoring": True,
                "agentic_evidence_provider_configured": True,
                "theme_evidence_review_status": "provider_error",
                "theme_evidence_review_blocked_reason": "codex_cli_timeout",
                "theme_evidence_review_timeout_seconds": 30.0,
                "agentic_evidence_status": "completed",
                "agentic_evidence_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "agentic_evidence_archetype_source": "theme_route_hint",
                "agentic_evidence_max_raw_assertions_per_run": 8,
                "agentic_evidence_raw_assertion_budget_limited": False,
                "agentic_evidence_raw_assertion_budget_limit": 8,
                "agentic_evidence_block_reason": None,
                "agentic_evidence_claim_ids": ("CLM-1", "CLM-2"),
                "agentic_evidence_mapping_ids": ("MAP-ACCEPTED",),
                "agentic_evidence_mapper_self_consistency_rounds": 3,
                "agentic_evidence_mapper_self_consistency_min_agreement": 2,
                "agentic_evidence_mapper_self_consistency_use_batch": False,
                "agentic_evidence_mapper_batch_max_tasks": 12,
                "agentic_evidence_rejected_mapping_ids": ("MAP-REJECTED",),
                "agentic_evidence_rejected_mapping_summaries": (
                    "MAP-REJECTED|claim=CLM-1|primitive=customer_preorder_or_allocation|status=REJECTED",
                ),
                "agentic_evidence_eligibility_rejection_summaries": (
                    "MAP-ACCEPTED|claim=CLM-2|primitive=hbm_capacity_pre_sold|mapping_status=ACCEPTED|eligibility_reasons=temporal_not_allowed:HISTORICAL",
                ),
                "agentic_evidence_document_selection_summaries": (
                    "DOC-1|source=NEWS|score=5.00|matched=customer,allocation|url=https://example.com/hbm",
                ),
                "agentic_stage_court_runtime_stage": "3-Yellow",
                "agentic_stage_court_runtime_investigation_status": "PENDING",
                "agentic_stage_court_runtime_score_status": "PENDING_MATERIAL_GAPS",
                "agentic_score_contribution_v2_count": 2,
                "agentic_score_contribution_v2_nonzero_count": 1,
                "agentic_score_contribution_v2_cap_summaries": (
                    "earnings_visibility/agentic_v2_rubric_earnings_visibility:raw=0.0; cap=qualification_status:primitive_status:UNKNOWN",
                ),
                "agentic_score_contribution_v2_support_summaries": (
                    "bottleneck_pricing/agentic_v2_rubric_bottleneck_pricing:raw=10.0; claims=CLM-SUPPORT",
                ),
                "post_score_gap_primitive_state_changed": True,
                "post_score_gap_primitive_delta_summaries": (
                    "customer_preorder_or_allocation:PRESENT_CURRENT->PRESENT_CURRENT; support+=CLM-NEW",
                ),
                "post_score_gap_unchanged_gap_primitive_summaries": (
                    "qualification_status:UNKNOWN; support=0; counter=0; materiality=8.0",
                ),
                "post_score_gap_score_contribution_changed": False,
                "post_score_gap_score_contribution_delta_summaries": (),
                "post_score_gap_audit_events": (
                    {
                        "event_id": "SGAUD-1",
                        "round_index": 0,
                        "progress_reason": "score_gap_new_accepted_mappings_without_score_state_change",
                    },
                ),
            },
            feature_result=SimpleNamespace(
                source_fields={
                    "agentic_score_contribution_v2_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "agentic_score_contribution_v2_archetype_mismatch": "C21_BALANCE_SHEET_CAPITAL_RETURN->C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                }
            ),
            theme_route=None,
            stage=SimpleNamespace(stage=Stage.STAGE_3_YELLOW),
            legacy_stage_before_agentic_court=SimpleNamespace(stage=Stage.STAGE_3_GREEN),
        )

        row = _theme_route_row(candidate, result)

        self.assertTrue(row["agentic_evidence_enabled"])
        self.assertTrue(row["agentic_evidence_required_for_scoring"])
        self.assertTrue(row["agentic_evidence_provider_configured"])
        self.assertEqual(row["theme_evidence_review_status"], "provider_error")
        self.assertEqual(row["theme_evidence_review_blocked_reason"], "codex_cli_timeout")
        self.assertEqual(row["theme_evidence_review_timeout_seconds"], 30.0)
        self.assertEqual(row["agentic_evidence_mapper_self_consistency_rounds"], 3)
        self.assertEqual(row["agentic_evidence_mapper_self_consistency_min_agreement"], 2)
        self.assertFalse(row["agentic_evidence_mapper_self_consistency_use_batch"])
        self.assertEqual(row["agentic_evidence_mapper_batch_max_tasks"], 12)
        self.assertEqual(row["agentic_evidence_archetype_id"], "C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertEqual(row["agentic_evidence_archetype_source"], "theme_route_hint")
        self.assertEqual(row["agentic_evidence_max_raw_assertions_per_run"], 8)
        self.assertFalse(row["agentic_evidence_raw_assertion_budget_limited"])
        self.assertEqual(row["agentic_evidence_raw_assertion_budget_limit"], 8)
        self.assertIsNone(row["agentic_evidence_block_reason"])
        self.assertEqual(row["agentic_evidence_claim_ids"], ("CLM-1", "CLM-2"))
        self.assertEqual(row["agentic_evidence_mapping_ids"], ("MAP-ACCEPTED",))
        self.assertEqual(row["agentic_evidence_rejected_mapping_ids"], ("MAP-REJECTED",))
        self.assertIn("primitive=customer_preorder_or_allocation", row["agentic_evidence_rejected_mapping_summaries"][0])
        self.assertIn(
            "temporal_not_allowed:HISTORICAL",
            row["agentic_evidence_eligibility_rejection_summaries"][0],
        )
        self.assertIn("matched=customer,allocation", row["agentic_evidence_document_selection_summaries"][0])
        self.assertEqual(row["agentic_stage_court_runtime_stage"], "3-Yellow")
        self.assertEqual(row["agentic_stage_court_runtime_investigation_status"], "PENDING")
        self.assertEqual(row["agentic_stage_court_runtime_score_status"], "PENDING_MATERIAL_GAPS")
        self.assertEqual(row["agentic_score_contribution_v2_count"], 2)
        self.assertEqual(row["agentic_score_contribution_v2_nonzero_count"], 1)
        self.assertIn(
            "qualification_status:primitive_status:UNKNOWN",
            row["agentic_score_contribution_v2_cap_summaries"][0],
        )
        self.assertIn("claims=CLM-SUPPORT", row["agentic_score_contribution_v2_support_summaries"][0])
        self.assertEqual(
            row["agentic_score_contribution_v2_archetype_id"],
            "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        )
        self.assertEqual(
            row["agentic_score_contribution_v2_archetype_mismatch"],
            "C21_BALANCE_SHEET_CAPITAL_RETURN->C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        )
        self.assertEqual(row["legacy_stage_before_agentic_court"], "3-Green")
        self.assertEqual(row["final_stage_after_agentic_court"], "3-Yellow")
        self.assertEqual(row["stage_output_status"], "pending_agentic_evidence")
        self.assertFalse(row["stage_is_final"])
        self.assertIsNone(row["stage_display_stage"])
        self.assertEqual(row["stage_pending_reason"], "PENDING_MATERIAL_GAPS")
        self.assertTrue(row["post_score_gap_primitive_state_changed"])
        self.assertEqual(
            row["post_score_gap_primitive_delta_summaries"],
            ("customer_preorder_or_allocation:PRESENT_CURRENT->PRESENT_CURRENT; support+=CLM-NEW",),
        )
        self.assertEqual(
            row["post_score_gap_unchanged_gap_primitive_summaries"],
            ("qualification_status:UNKNOWN; support=0; counter=0; materiality=8.0",),
        )
        self.assertFalse(row["post_score_gap_score_contribution_changed"])
        self.assertEqual(row["post_score_gap_score_contribution_delta_summaries"], ())
        self.assertEqual(row["post_score_gap_audit_events"][0]["event_id"], "SGAUD-1")

    def test_stage_output_row_marks_pending_investigation_even_when_score_valid(self):
        result = SimpleNamespace(
            theme_route_diagnostics={
                "agentic_stage_court_runtime_score_status": "FINAL_WITH_NONMATERIAL_GAPS",
                "agentic_stage_court_runtime_investigation_status": "PENDING",
            },
            stage=SimpleNamespace(stage=Stage.STAGE_3_YELLOW),
        )

        row = _stage_output_row(result, score_valid=True, blocked_reason=None)

        self.assertEqual(row["stage_output_status"], "pending_agentic_evidence")
        self.assertFalse(row["stage_is_final"])
        self.assertIsNone(row["stage_display_stage"])
        self.assertEqual(row["stage_pending_reason"], "PENDING")

    def test_targeted_smoke_hides_invalid_score_components(self):
        score = ScoreSnapshot(
            symbol="009999",
            as_of_date=AS_OF,
            eps_fcf_explosion_score=0,
            earnings_visibility_score=0,
            bottleneck_pricing_score=0,
            market_mispricing_score=0,
            valuation_rerating_score=0,
            capital_allocation_score=0,
            information_confidence_score=0,
            risk_penalty=0,
            total_score=0,
            diagnostic_scores={
                "score_valid": 0.0,
                "score_blocked_by_score_gap": 100.0,
                "raw_eps_fcf_before_score_gap_block": 16.0,
                "raw_earnings_visibility_before_score_gap_block": 14.0,
                "raw_bottleneck_pricing_before_score_gap_block": 15.0,
                "raw_market_mispricing_before_score_gap_block": 11.0,
                "raw_valuation_rerating_before_score_gap_block": 12.0,
                "raw_capital_allocation_before_score_gap_block": 4.0,
                "raw_information_confidence_before_score_gap_block": 5.0,
                "raw_risk_penalty_before_score_gap_block": 0.0,
                "raw_score_total_before_score_gap_block": 77.0,
            },
        )
        candidate = SimpleNamespace(
            symbol="009999",
            company_name="스모크테스트",
            candidate_source_path="targeted_smoke",
            test_injected=True,
            production_candidate=False,
        )
        result = SimpleNamespace(
            theme_route_diagnostics={
                "score_valid": False,
                "score_blocked_reason": "score_gap_no_executable_searches",
                "agentic_stage_court_runtime_score_status": "INVALID_EVIDENCE",
                "agentic_stage_court_verified_score": 77.0,
                "agentic_stage_court_potential_score_upper_bound": 85.0,
            },
            web_result=SimpleNamespace(evidence=(), queries_run=()),
            score=score,
            stage=SimpleNamespace(stage=Stage.STAGE_0, stage_reason=("score was marked invalid before stage classification",)),
            feature_result=SimpleNamespace(payload=SimpleNamespace(large_sector_id=None, canonical_archetype_id=None), source_fields={}),
            feature_input=FeatureEngineeringInput(symbol="009999", as_of_date=AS_OF),
            expansion_queries_run=(),
            red_team=SimpleNamespace(
                risk_level=SimpleNamespace(value="low"),
                soft_4b_score=0.0,
                soft_4b_status=SimpleNamespace(value="none"),
                thesis_break_score=0.0,
                has_hard_break=False,
                evidence_ids=(),
                findings=(),
            ),
        )

        row = _targeted_smoke_result_row(candidate, result)

        self.assertFalse(row["score_valid"])
        self.assertIsNone(row["visible_score"])
        self.assertIsNone(row["score_total"])
        self.assertIsInstance(row["score_fingerprint"], str)
        self.assertIsNone(row["score_components"])
        self.assertIsInstance(row["research_input_fingerprint"], str)
        self.assertEqual(row["raw_score_before_block"], 77.0)
        self.assertEqual(row["score_status"], "INVALID_EVIDENCE")
        self.assertEqual(row["verified_score"], 77.0)
        self.assertEqual(row["provisional_score"], 77.0)
        self.assertEqual(row["score_interval_lower"], 77.0)
        self.assertEqual(row["score_interval_upper"], 85.0)
        self.assertEqual(row["stage_output_status"], "pending_invalid_score")
        self.assertFalse(row["stage_is_final"])
        self.assertIsNone(row["stage_display_stage"])
        self.assertEqual(row["stage_pending_reason"], "score_gap_no_executable_searches")
        self.assertEqual(row["raw_score_components_before_block"]["eps_fcf_explosion_score"], 16.0)
        self.assertEqual(row["score_evidence_ids"], ())
        self.assertIn("score_invalid:score_gap_no_executable_searches", row["score_variability_drivers"])
        self.assertIn("score_gap_blocked:score_gap_no_executable_searches", row["score_variability_drivers"])
        self.assertIn(f"research_input_fingerprint:{row['research_input_fingerprint']}", row["score_variability_drivers"])
        self.assertEqual(score_state_contract_violations(row), ())

    def test_targeted_smoke_explains_valid_score_variability_inputs(self):
        component_scores = {
            "eps_fcf_explosion": 20,
            "earnings_visibility": 10,
            "bottleneck_pricing": 12,
            "market_mispricing": 8,
            "valuation_rerating": 9,
            "capital_allocation": 2,
            "information_confidence": 4,
        }
        component_claims = {key: (f"CLM-{key}",) for key, value in component_scores.items() if value > 0}
        score = ScoreSnapshot(
            symbol="009999",
            as_of_date=AS_OF,
            eps_fcf_explosion_score=component_scores["eps_fcf_explosion"],
            earnings_visibility_score=component_scores["earnings_visibility"],
            bottleneck_pricing_score=component_scores["bottleneck_pricing"],
            market_mispricing_score=component_scores["market_mispricing"],
            valuation_rerating_score=component_scores["valuation_rerating"],
            capital_allocation_score=component_scores["capital_allocation"],
            information_confidence_score=component_scores["information_confidence"],
            risk_penalty=0,
            total_score=65,
            diagnostic_scores={
                "score_valid": 100.0,
                "score_claim_backed_required": 100.0,
                "claim_backed_claim_count_capped": float(len(component_claims)),
                "score_claim_backed_component_ratio": 100.0,
                "orphan_score_component_count_capped": 0.0,
                "estimate_missing_fcf_source": 100.0,
                "estimate_missing_revision_source": 100.0,
                "estimate_missing_op_source": 100.0,
                "estimate_conflict_count_capped": 2.0,
                "cross_evidence_family_count": 4.0,
                "evidence_family_price": 1.0,
                "evidence_family_financial_actual": 1.0,
                "evidence_family_disclosure": 0.0,
                "evidence_family_research_report": 1.0,
                "evidence_family_consensus": 1.0,
                "evidence_family_consensus_revision": 0.0,
                "evidence_family_news": 0.0,
                "evidence_family_consensus_proxy": 0.0,
                "evidence_family_consensus_structured": 1.0,
                "evidence_family_consensus_revision_proxy": 1.0,
                "evidence_family_search_snippet_news": 1.0,
            },
            score_contribution_claim_ids=component_claims,
            score_contribution_ledger=tuple(
                ScoreContribution(
                    component_key=key,
                    criterion_id=key,
                    raw_points=value,
                    max_points=20 if key in {"eps_fcf_explosion", "earnings_visibility", "bottleneck_pricing"} else 15 if key in {"market_mispricing", "valuation_rerating"} else 5,
                    support_claim_ids=component_claims[key],
                )
                for key, value in component_scores.items()
            ),
        )
        candidate = SimpleNamespace(
            symbol="009999",
            company_name="스모크테스트",
            candidate_source_path="targeted_smoke",
            test_injected=True,
            production_candidate=False,
        )
        result = SimpleNamespace(
            theme_route_diagnostics={
                "score_valid": True,
                "theme_rebalance_status": "completed",
                "theme_route_status": "transition_detected",
                "theme_evidence_gate_status": "source_backed",
                "theme_evidence_review_status": "completed",
                "theme_evidence_review_blocked_reason": None,
                "theme_evidence_review_timeout_seconds": 60.0,
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "post_score_gap_expansion_count": 0,
                "post_score_gap_expansion_status": "not_attempted",
                "post_score_gap_unresolved_gaps": (
                    "agentic primitive gap:hbm_capacity_pre_sold; status:UNKNOWN",
                ),
                "post_score_gap_rejection_reasons": ("max_score_gap_expansion_rounds_reached",),
                "post_score_gap_blocked_reason": "score_gap_round_limit",
                "post_score_gap_progress_reason": "score_gap_new_claims_without_accepted_mappings",
                "post_score_gap_score_state_changed": False,
                "post_score_gap_new_document_count": 2,
                "post_score_gap_new_document_ids": ("DOC-4", "DOC-5"),
                "post_score_gap_new_claim_count": 1,
                "post_score_gap_new_claim_ids": ("CLM-NEW",),
                "post_score_gap_new_accepted_mapping_count": 0,
                "post_score_gap_new_accepted_mapping_ids": (),
                "post_score_gap_new_rejected_mapping_count": 1,
                "post_score_gap_new_rejected_mapping_ids": ("MAP-NEW-REJECTED",),
                "post_score_gap_new_rejected_mapping_summaries": (
                    "MAP-NEW-REJECTED|claim=CLM-NEW|primitive=qualification_status|status=REJECTED|reason=target_scope_not_allowed:CUSTOMER",
                ),
                "post_score_gap_new_eligibility_rejection_summaries": (
                    "MAP-NEW-REJECTED|claim=CLM-NEW|primitive=qualification_status|mapping_status=REJECTED|eligibility_reasons=source_date_missing",
                ),
                "post_score_gap_new_trace_status": "partial_error",
                "post_score_gap_new_trace_skipped_existing_document_count": 3,
                "post_score_gap_new_trace_mapping_prefilter_original_task_count": 12,
                "post_score_gap_new_trace_mapping_prefilter_filtered_task_count": 4,
                "post_score_gap_new_trace_mapping_prefilter_skipped_input_count": 0,
                "post_score_gap_new_trace_mapping_prefilter_fallback_full_map_count": 1,
                "post_score_gap_new_trace_mapping_prefilter_fallback_full_map_summaries": (
                    "fallback_full_map|document=DOC-5|claim=CLM-NEW|reason=fallback_full_map_unstructured_source",
                ),
                "post_score_gap_new_trace_mapping_empty_output_count": 1,
                "post_score_gap_new_trace_mapping_empty_output_retry_count": 2,
                "post_score_gap_new_trace_mapping_empty_output_recovered_count": 1,
                "post_score_gap_new_trace_mapping_empty_output_summaries": (
                    "empty_mapper_output|phase=agentic_evidence_mapping_chunk_complete|document=DOC-5",
                ),
                "post_score_gap_new_trace_mapping_empty_output_retry_summaries": (
                    "empty_mapper_retry|phase=agentic_evidence_mapping_chunk_empty_retry_recovered|document=DOC-5",
                ),
                "post_score_gap_new_trace_error_count": 1,
                "post_score_gap_new_trace_errors": (
                    "DOC-5:ValueError:claim_extractor_provider_error:usage_limit",
                ),
                "post_score_gap_primitive_state_changed": True,
                "post_score_gap_primitive_delta_summaries": (
                    "customer_preorder_or_allocation:PRESENT_CURRENT->PRESENT_CURRENT; support+=CLM-NEW",
                ),
                "post_score_gap_unchanged_gap_primitive_summaries": (
                    "qualification_status:UNKNOWN; support=0; counter=0; materiality=8.0",
                ),
                "post_score_gap_score_contribution_changed": False,
                "post_score_gap_score_contribution_delta_summaries": (),
                "post_score_gap_audit_events": (
                    {
                        "event_id": "SGAUD-1",
                        "round_index": 0,
                        "progress_reason": "score_gap_new_accepted_mappings_without_score_state_change",
                    },
                ),
                "agentic_evidence_enabled": True,
                "agentic_evidence_required_for_scoring": True,
                "agentic_evidence_provider_configured": True,
                "agentic_evidence_status": "completed",
                "agentic_evidence_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "agentic_evidence_archetype_source": "theme_route_canonical",
                "agentic_evidence_mapper_batch_max_tasks": 12,
                "agentic_evidence_max_raw_assertions_per_run": 8,
                "agentic_evidence_raw_assertion_budget_limited": False,
                "agentic_evidence_raw_assertion_budget_limit": 8,
                "agentic_evidence_block_reason": None,
                "agentic_evidence_document_ids": ("DOC-1", "DOC-2", "DOC-3"),
                "agentic_evidence_skipped_existing_document_count": 2,
                "agentic_evidence_claim_count": 4,
                "agentic_evidence_claim_ids": ("CLM-1", "CLM-2", "CLM-3", "CLM-4"),
                "agentic_evidence_accepted_mapping_count": 3,
                "agentic_evidence_mapping_prefilter_original_task_count": 40,
                "agentic_evidence_mapping_prefilter_filtered_task_count": 18,
                "agentic_evidence_mapping_prefilter_skipped_input_count": 2,
                "agentic_evidence_mapping_prefilter_fallback_full_map_count": 1,
                "agentic_evidence_mapping_prefilter_fallback_full_map_summaries": (
                    "fallback_full_map|document=DOC-2|claim=CLM-2|reason=fallback_full_map_unstructured_source",
                ),
                "agentic_evidence_mapping_empty_output_count": 1,
                "agentic_evidence_mapping_empty_output_retry_count": 2,
                "agentic_evidence_mapping_empty_output_recovered_count": 1,
                "agentic_evidence_mapping_empty_output_summaries": (
                    "empty_mapper_output|phase=agentic_evidence_mapping_chunk_complete|document=DOC-2",
                ),
                "agentic_evidence_mapping_empty_output_retry_summaries": (
                    "empty_mapper_retry|phase=agentic_evidence_mapping_chunk_empty_retry_recovered|document=DOC-2",
                ),
                "agentic_evidence_mapping_ids": ("MAP-1", "MAP-2", "MAP-3"),
                "agentic_evidence_rejected_mapping_count": 1,
                "agentic_evidence_rejected_mapping_ids": ("MAP-REJECTED",),
                "agentic_evidence_rejected_mapping_summaries": (
                    "MAP-REJECTED|claim=CLM-1|primitive=hbm_capacity_pre_sold|status=REJECTED",
                ),
                "agentic_evidence_eligibility_rejection_summaries": (
                    "MAP-ACCEPTED|claim=CLM-2|primitive=contract_visibility|mapping_status=ACCEPTED|eligibility_reasons=source_date_missing",
                ),
                "agentic_evidence_document_selection_summaries": (
                    "DOC-2|source=IR|score=7.00|matched=hbm,capacity,sold|url=https://example.com/ir",
                ),
                "agentic_stage_court_runtime_stage": "3-Yellow",
                "agentic_stage_court_runtime_investigation_status": "COMPLETE",
                "agentic_stage_court_runtime_score_status": "FINAL",
                "agentic_score_contribution_v2_count": 2,
                "agentic_score_contribution_v2_nonzero_count": 1,
                "agentic_score_contribution_v2_cap_summaries": (
                    "earnings_visibility/agentic_v2_rubric_earnings_visibility:raw=0.0; cap=qualification_status:primitive_status:UNKNOWN",
                ),
                "agentic_score_contribution_v2_support_summaries": (
                    "bottleneck_pricing/agentic_v2_rubric_bottleneck_pricing:raw=10.0; claims=CLM-SUPPORT",
                ),
            },
            web_result=SimpleNamespace(evidence=(), queries_run=()),
            score=score,
            stage=SimpleNamespace(stage=Stage.STAGE_2, stage_reason=("valid but incomplete evidence",)),
            legacy_stage_before_agentic_court=SimpleNamespace(stage=Stage.STAGE_3_GREEN),
            feature_result=SimpleNamespace(
                payload=SimpleNamespace(large_sector_id="R2_AI_SEMICONDUCTOR_ELECTRONICS", canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY"),
                source_fields={
                    "estimate_selected_eps_source": "company_guide_snapshot",
                    "claim_ledger_claim_ids": ",".join(claim_id for ids in component_claims.values() for claim_id in ids),
                    "claim_ledger_score_eligible_claim_ids": ",".join(claim_id for ids in component_claims.values() for claim_id in ids),
                    "claim_ledger_claim_ids_by_primitive": json.dumps(
                        {key: list(value) for key, value in component_claims.items()},
                        ensure_ascii=False,
                        sort_keys=True,
                    ),
                    "evidence_contract_runtime_bridge_group": "hbm_memory_customer_capacity_bridge",
                    "evidence_contract_required_primitives": "hbm_capacity_pre_sold",
                    "evidence_contract_present_primitives": "hbm_capacity_pre_sold",
                    "evidence_contract_missing_primitives": "",
                    "agentic_score_contribution_v2_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "agentic_score_contribution_v2_archetype_mismatch": "C21_BALANCE_SHEET_CAPITAL_RETURN->C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                },
            ),
            feature_input=FeatureEngineeringInput(symbol="009999", as_of_date=AS_OF),
            expansion_queries_run=(),
            red_team=SimpleNamespace(
                risk_level=SimpleNamespace(value="low"),
                soft_4b_score=0.0,
                soft_4b_status=SimpleNamespace(value="none"),
                thesis_break_score=0.0,
                has_hard_break=False,
                evidence_ids=(),
                findings=(),
            ),
        )

        row = _targeted_smoke_result_row(candidate, result)

        self.assertTrue(row["score_valid"])
        self.assertEqual(row["visible_score"], 65)
        self.assertEqual(row["score_total"], 65)
        self.assertEqual(row["stage_output_status"], "final")
        self.assertTrue(row["stage_is_final"])
        self.assertEqual(row["stage_display_stage"], Stage.STAGE_2.value)
        self.assertIsNone(row["stage_pending_reason"])
        self.assertIsInstance(row["research_input_fingerprint"], str)
        self.assertIn("estimate_source_missing:fcf", row["score_variability_drivers"])
        self.assertIn("estimate_source_missing:revision", row["score_variability_drivers"])
        self.assertIn("estimate_source_missing:op", row["score_variability_drivers"])
        self.assertIn("input_missing:research_report", row["score_variability_drivers"])
        self.assertIn("llm_expansion_query_count:0", row["score_variability_drivers"])
        self.assertIn("score_gap_expansion_status:not_attempted", row["score_variability_drivers"])
        self.assertIn(f"research_input_fingerprint:{row['research_input_fingerprint']}", row["score_variability_drivers"])
        self.assertEqual(row["score_claim_backed_required"], 100.0)
        self.assertEqual(row["score_claim_backed_component_ratio"], 100.0)
        self.assertIsNone(row["legacy_parser_score_claim_without_v2_count"])
        self.assertEqual(row["legacy_parser_score_claim_fields_without_v2"], ())
        self.assertEqual(set(row["score_contribution_claim_ids"]), set(component_claims))
        self.assertEqual(len(row["score_contribution_ledger"]), len(component_claims))
        self.assertEqual(row["cross_evidence_family_count"], 4.0)
        self.assertEqual(row["evidence_family_consensus"], 1.0)
        self.assertEqual(row["evidence_family_consensus_revision"], 0.0)
        self.assertEqual(row["evidence_family_consensus_revision_proxy"], 1.0)
        self.assertEqual(
            row["evidence_family_present_families"],
            ("price", "financial_actual", "research_report", "consensus"),
        )
        self.assertEqual(
            row["evidence_family_missing_families"],
            ("disclosure", "consensus_revision", "news"),
        )
        self.assertEqual(
            row["evidence_family_proxy_present_families"],
            ("consensus_structured", "consensus_revision_proxy", "search_snippet_news"),
        )
        self.assertTrue(row["agentic_evidence_enabled"])
        self.assertTrue(row["agentic_evidence_required_for_scoring"])
        self.assertTrue(row["agentic_evidence_provider_configured"])
        self.assertEqual(row["agentic_evidence_status"], "completed")
        self.assertEqual(row["theme_evidence_review_status"], "completed")
        self.assertIsNone(row["theme_evidence_review_blocked_reason"])
        self.assertEqual(row["theme_evidence_review_timeout_seconds"], 60.0)
        self.assertEqual(row["agentic_evidence_archetype_id"], "C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertEqual(row["agentic_evidence_archetype_source"], "theme_route_canonical")
        self.assertEqual(row["agentic_evidence_mapper_batch_max_tasks"], 12)
        self.assertEqual(row["agentic_evidence_max_raw_assertions_per_run"], 8)
        self.assertFalse(row["agentic_evidence_raw_assertion_budget_limited"])
        self.assertEqual(row["agentic_evidence_raw_assertion_budget_limit"], 8)
        self.assertIsNone(row["agentic_evidence_block_reason"])
        self.assertEqual(row["agentic_evidence_document_ids"], ("DOC-1", "DOC-2", "DOC-3"))
        self.assertEqual(row["agentic_evidence_skipped_existing_document_count"], 2)
        self.assertEqual(row["agentic_evidence_claim_count"], 4)
        self.assertEqual(row["agentic_evidence_claim_ids"], ("CLM-1", "CLM-2", "CLM-3", "CLM-4"))
        self.assertEqual(row["agentic_evidence_accepted_mapping_count"], 3)
        self.assertEqual(row["agentic_evidence_mapping_prefilter_original_task_count"], 40)
        self.assertEqual(row["agentic_evidence_mapping_prefilter_filtered_task_count"], 18)
        self.assertEqual(row["agentic_evidence_mapping_prefilter_skipped_input_count"], 2)
        self.assertEqual(row["agentic_evidence_mapping_prefilter_fallback_full_map_count"], 1)
        self.assertIn(
            "fallback_full_map",
            row["agentic_evidence_mapping_prefilter_fallback_full_map_summaries"][0],
        )
        self.assertEqual(row["agentic_evidence_mapping_empty_output_count"], 1)
        self.assertEqual(row["agentic_evidence_mapping_empty_output_retry_count"], 2)
        self.assertEqual(row["agentic_evidence_mapping_empty_output_recovered_count"], 1)
        self.assertIn("empty_mapper_output", row["agentic_evidence_mapping_empty_output_summaries"][0])
        self.assertIn("empty_mapper_retry", row["agentic_evidence_mapping_empty_output_retry_summaries"][0])
        self.assertEqual(row["agentic_evidence_mapping_ids"], ("MAP-1", "MAP-2", "MAP-3"))
        self.assertEqual(row["agentic_evidence_rejected_mapping_count"], 1)
        self.assertEqual(row["agentic_evidence_rejected_mapping_ids"], ("MAP-REJECTED",))
        self.assertIn("primitive=hbm_capacity_pre_sold", row["agentic_evidence_rejected_mapping_summaries"][0])
        self.assertIn("source_date_missing", row["agentic_evidence_eligibility_rejection_summaries"][0])
        self.assertIn("matched=hbm,capacity,sold", row["agentic_evidence_document_selection_summaries"][0])
        self.assertEqual(row["agentic_stage_court_runtime_stage"], "3-Yellow")
        self.assertEqual(row["agentic_stage_court_runtime_investigation_status"], "COMPLETE")
        self.assertEqual(row["agentic_stage_court_runtime_score_status"], "FINAL")
        self.assertEqual(row["agentic_score_contribution_v2_count"], 2)
        self.assertEqual(row["agentic_score_contribution_v2_nonzero_count"], 1)
        self.assertIn(
            "qualification_status:primitive_status:UNKNOWN",
            row["agentic_score_contribution_v2_cap_summaries"][0],
        )
        self.assertIn("claims=CLM-SUPPORT", row["agentic_score_contribution_v2_support_summaries"][0])
        self.assertEqual(
            row["agentic_score_contribution_v2_archetype_id"],
            "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        )
        self.assertEqual(
            row["agentic_score_contribution_v2_archetype_mismatch"],
            "C21_BALANCE_SHEET_CAPITAL_RETURN->C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        )
        self.assertEqual(
            row["post_score_gap_unresolved_gaps"],
            ("agentic primitive gap:hbm_capacity_pre_sold; status:UNKNOWN",),
        )
        self.assertEqual(row["post_score_gap_rejection_reasons"], ("max_score_gap_expansion_rounds_reached",))
        self.assertEqual(row["post_score_gap_blocked_reason"], "score_gap_round_limit")
        self.assertEqual(row["post_score_gap_progress_reason"], "score_gap_new_claims_without_accepted_mappings")
        self.assertFalse(row["post_score_gap_score_state_changed"])
        self.assertEqual(row["post_score_gap_new_document_count"], 2)
        self.assertEqual(row["post_score_gap_new_document_ids"], ("DOC-4", "DOC-5"))
        self.assertEqual(row["post_score_gap_new_claim_count"], 1)
        self.assertEqual(row["post_score_gap_new_claim_ids"], ("CLM-NEW",))
        self.assertEqual(row["post_score_gap_new_accepted_mapping_count"], 0)
        self.assertEqual(row["post_score_gap_new_accepted_mapping_ids"], ())
        self.assertEqual(row["post_score_gap_new_rejected_mapping_count"], 1)
        self.assertEqual(row["post_score_gap_new_rejected_mapping_ids"], ("MAP-NEW-REJECTED",))
        self.assertIn("target_scope_not_allowed:CUSTOMER", row["post_score_gap_new_rejected_mapping_summaries"][0])
        self.assertIn("source_date_missing", row["post_score_gap_new_eligibility_rejection_summaries"][0])
        self.assertEqual(row["post_score_gap_new_trace_status"], "partial_error")
        self.assertEqual(row["post_score_gap_new_trace_skipped_existing_document_count"], 3)
        self.assertEqual(row["post_score_gap_new_trace_mapping_prefilter_original_task_count"], 12)
        self.assertEqual(row["post_score_gap_new_trace_mapping_prefilter_filtered_task_count"], 4)
        self.assertEqual(row["post_score_gap_new_trace_mapping_prefilter_skipped_input_count"], 0)
        self.assertEqual(row["post_score_gap_new_trace_mapping_prefilter_fallback_full_map_count"], 1)
        self.assertIn(
            "fallback_full_map",
            row["post_score_gap_new_trace_mapping_prefilter_fallback_full_map_summaries"][0],
        )
        self.assertEqual(row["post_score_gap_new_trace_mapping_empty_output_count"], 1)
        self.assertEqual(row["post_score_gap_new_trace_mapping_empty_output_retry_count"], 2)
        self.assertEqual(row["post_score_gap_new_trace_mapping_empty_output_recovered_count"], 1)
        self.assertIn("empty_mapper_output", row["post_score_gap_new_trace_mapping_empty_output_summaries"][0])
        self.assertIn("empty_mapper_retry", row["post_score_gap_new_trace_mapping_empty_output_retry_summaries"][0])
        self.assertEqual(row["post_score_gap_new_trace_error_count"], 1)
        self.assertIn("usage_limit", row["post_score_gap_new_trace_errors"][0])
        self.assertTrue(row["post_score_gap_primitive_state_changed"])
        self.assertEqual(
            row["post_score_gap_primitive_delta_summaries"],
            ("customer_preorder_or_allocation:PRESENT_CURRENT->PRESENT_CURRENT; support+=CLM-NEW",),
        )
        self.assertEqual(
            row["post_score_gap_unchanged_gap_primitive_summaries"],
            ("qualification_status:UNKNOWN; support=0; counter=0; materiality=8.0",),
        )
        self.assertFalse(row["post_score_gap_score_contribution_changed"])
        self.assertEqual(row["post_score_gap_score_contribution_delta_summaries"], ())
        self.assertEqual(row["post_score_gap_audit_events"][0]["event_id"], "SGAUD-1")
        self.assertEqual(row["legacy_stage_before_agentic_court"], "3-Green")
        self.assertEqual(row["final_stage_after_agentic_court"], "2")
        self.assertTrue(row["claim_ledger_claim_ids"])
        self.assertIn("stage4b_overlay_gate_passed", row["stage4_transition_diagnostics"])
        self.assertEqual(score_state_contract_violations(row), ())

    def test_top_trading_value_probe_selects_highest_value_without_production_pollution(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    top_trading_value_probe_enabled=True,
                    top_trading_value_probe_count=2,
                    budget=KoreaLiveLiteBudget(
                        max_symbols_for_event_search=0,
                        max_symbols_for_deep_research=0,
                        max_naver_search_calls_per_day=20,
                    ),
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        probe_rows = tuple(result.run_log.top_trading_value_probe_candidates)
        self.assertEqual([item["symbol"] for item in probe_rows], ["222222", "444444"])
        self.assertTrue(all(item["candidate_source_path"] == "top_trading_value_probe" for item in probe_rows))
        self.assertTrue(all(item["production_candidate"] is False for item in probe_rows))
        self.assertFalse(any(item.candidate_source_path == "top_trading_value_probe" for item in result.candidates))
        probe_results = [item for item in result.run_log.targeted_smoke_results if item["candidate_source_path"] == "top_trading_value_probe"]
        self.assertEqual({item["symbol"] for item in probe_results}, {"222222", "444444"})
        self.assertTrue(all("score_total" in item for item in probe_results))
        self.assertTrue(all("stage_reason" in item for item in probe_results))
        self.assertTrue(all("scoring_canonical_archetype_id" in item for item in probe_results))
        self.assertTrue(all("post_score_gap_expansion_count" in item for item in probe_results))
        self.assertTrue(all(item["feature_input_counts"]["price_bars"] > 0 for item in probe_results))

    def test_report_radar_candidate_path_respects_budget_and_records_source_path(self):
        url = "https://ssl.pstatic.net/imgstock/upload/research/company/radar_report.pdf"
        provider = FixtureSearchProvider(
            results_by_query={
                "가격만강세 목표주가 상향 EPS 상향 PDF": (
                    SearchResult(
                        title="가격만강세 컨센서스 상회 Review PDF",
                        url=url,
                        snippet="목표주가 상향 EPS 상향 수주잔고 OPM",
                        source="FixtureBroker",
                        published_at=datetime(2024, 5, 21, 8),
                        query="가격만강세 목표주가 상향 EPS 상향 PDF",
                        rank=1,
                        is_pdf=True,
                        is_report_domain=True,
                        confidence=0.8,
                    ),
                )
            }
        )
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    report_radar_enabled=True,
                    report_radar_universe_limit=1,
                    active_watchlist_symbols=("444444",),
                    budget=KoreaLiveLiteBudget(
                        max_symbols_for_event_search=20,
                        max_symbols_for_deep_research=20,
                        max_naver_search_calls_per_day=100,
                    ),
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=provider,
                )
            )

        self.assertTrue(result.run_log.report_radar_candidates)
        self.assertTrue(any(item.candidate_source_path == "report_radar" for item in result.candidates))
        self.assertLessEqual(result.run_log.source_call_counts["naver_search_queries"], 100)

    def test_stage_3_green_is_blocked_by_hard_parser_audit_finding(self):
        url = "https://ssl.pstatic.net/imgstock/upload/research/company/kepower_report.pdf"
        provider = FixtureSearchProvider(
            results_by_query={
                "케이전력 장기공급계약 매출액 대비": (
                    SearchResult(
                        title="케이전력 Review PDF",
                        url=url,
                        source="FixtureBroker",
                        published_at=datetime(2024, 5, 21, 8),
                        query="케이전력 장기공급계약 매출액 대비",
                        rank=1,
                        is_pdf=True,
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                )
            }
        )
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    budget=KoreaLiveLiteBudget(
                        max_symbols_for_event_search=10,
                        max_symbols_for_deep_research=10,
                        max_naver_search_calls_per_day=100,
                    ),
                    browser_provider=provider,
                    free_search_provider=EmptySearchProvider(),
                    fixture_text_by_url={url: IMPOSSIBLE_CONTRACT_REPORT_TEXT},
                )
            )

        stage_by_symbol = {item.stage.symbol: item.stage for item in result.web_results}
        self.assertEqual(stage_by_symbol["222222"].stage, Stage.STAGE_3_YELLOW)
        self.assertEqual(stage_by_symbol["222222"].grade, "parser-audit-blocked")
        self.assertTrue(any(item.code == "contract_ratio_too_high" for item in result.run_log.audit_findings))
        self.assertIn("manual_review_required", " ".join(result.run_log.notes))

    def test_hard_risk_candidate_is_not_escalated_to_green(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        hard_risk = next(candidate for candidate in result.candidates if candidate.symbol == "555555")
        self.assertEqual(hard_risk.recommended_next_layer.value, "none")
        self.assertNotIn("555555", {item.stage.symbol for item in result.web_results})

    def test_mocked_opendart_live_pagination_flows_into_disclosure_evidence(self):
        http_client = MockHttpClient(
            json_by_url_token={
                "page_no=1": {
                    "total_page": 2,
                    "list": [
                        {
                            "stock_code": "111111",
                            "corp_name": "한전변압기",
                            "report_nm": "단일판매·공급계약체결",
                            "rcept_no": "202405210091",
                            "rcept_dt": "20240521",
                        }
                    ],
                },
                "page_no=2": {
                    "total_page": 2,
                    "list": [
                        {
                            "stock_code": "222222",
                            "corp_name": "케이전력",
                            "report_nm": "신규시설투자",
                            "rcept_no": "202405210092",
                            "rcept_dt": "20240521",
                        }
                    ],
                },
            }
        )
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "DATA_GO_KR_SERVICE_KEY": "DATA_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    env_file=None,
                    http_client=http_client,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        disclosure_symbols = {item.symbol for item in result.evidence if item.source_type == "disclosure"}
        self.assertIn("111111", disclosure_symbols)
        self.assertIn("222222", disclosure_symbols)
        self.assertEqual(result.run_log.source_modes["opendart"], "live_executed")
        self.assertGreaterEqual(result.run_log.live_requests_executed, 2)
        self.assertGreaterEqual(result.run_log.cache_writes, 2)

    def test_mocked_naver_live_search_flows_into_news_evidence(self):
        url = "https://news.example.com/live-naver-contract"
        http_client = MockHttpClient(
            json_by_url_token={
                "opendart": {"total_page": 1, "list": []},
                "openapi.naver.com": {
                    "items": [
                        {
                            "title": "가격만강세 수주잔고 공급부족",
                            "originallink": url,
                            "link": url,
                            "description": "가격만강세 수주잔고와 공급부족 뉴스",
                            "pubDate": "Tue, 21 May 2024 08:00:00 +0900",
                        }
                    ]
                },
            }
        )
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "DATA_GO_KR_SERVICE_KEY": "DATA_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    http_client=http_client,
                    budget=KoreaLiveLiteBudget(
                        max_symbols_for_event_search=10,
                        max_symbols_for_deep_research=10,
                        max_naver_search_calls_per_day=20,
                    ),
                    browser_provider=EmptySearchProvider(),
                    fixture_text_by_url={url: "가격만강세 수주잔고 공급부족과 판가 상승이 보도됐다."},
                )
            )

        self.assertEqual(result.run_log.source_modes["naver_search"], "live_executed")
        self.assertTrue(any(item.source_type == "news" for item in result.evidence))
        self.assertGreaterEqual(self.codex_theme_route.call_count, 1)
        self.assertIn("completed", result.run_log.theme_route_status_counts)

    def test_request_only_sources_are_marked_when_live_credentials_exist(self):
        http_client = MockHttpClient(json_by_url_token={"opendart": {"total_page": 1, "list": []}})
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "KRX_OPENAPI_KEY": "KRX_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    env_file=None,
                    http_client=http_client,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        self.assertEqual(result.run_log.source_modes["krx"], "request_only")
        self.assertEqual(result.run_log.source_modes["krx_openapi"], "disabled_optional")
        self.assertEqual(result.run_log.source_modes["data_go_kr"], "request_only")
        self.assertIn("krx", result.run_log.request_only_sources)
        self.assertIn("data_go_kr", result.run_log.request_only_sources)
        self.assertNotIn("krx_openapi", result.run_log.request_only_sources)

    def test_krx_openapi_request_only_when_explicitly_enabled(self):
        http_client = MockHttpClient(json_by_url_token={"opendart": {"total_page": 1, "list": []}})
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "KRX_OPENAPI_KEY": "KRX_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    enable_krx_openapi_source=True,
                    http_client=http_client,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        self.assertEqual(result.run_log.source_modes["krx_openapi"], "request_only")
        self.assertIn("krx_openapi", result.run_log.request_only_sources)

    def test_mocked_data_go_live_listed_items_and_prices_feed_cheap_scan(self):
        http_client = MockHttpClient(
            json_by_url_token={
                "GetKrxListedInfoService": DATA_GO_LISTED_ITEMS_PAYLOAD,
                "GetStockSecuritiesInfoService": DATA_GO_STOCK_PRICE_PAYLOAD,
                "GetFinaStatInfoService": DATA_GO_FINANCIAL_PAYLOAD,
                "opendart": {"total_page": 1, "list": []},
            }
        )
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "DATA_GO_KR_SERVICE_KEY": "DATA_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    http_client=http_client,
                    budget=KoreaLiveLiteBudget(
                        max_data_go_kr_calls_per_day=10,
                        max_symbols_for_event_search=10,
                        max_symbols_for_deep_research=10,
                    ),
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        candidate = _candidate(result, "999999")
        self.assertEqual(candidate.company_name, "라이브전력")
        self.assertEqual(candidate.recommended_next_layer.value, "event_search")
        self.assertIn("PRICE_VOLUME_SPIKE", candidate.reason_codes)
        self.assertEqual(result.run_log.source_modes["data_go_kr"], "live_executed")
        self.assertEqual(result.run_log.source_call_counts["data_go_kr_calls"], 5)
        self.assertEqual(result.run_log.source_call_counts["data_go_kr_financial_actual_calls"], 3)
        self.assertTrue(any(item.source_type == "financial_actual" and item.symbol == "999999" for item in result.evidence))
        self.assertNotIn("data_go_kr", result.run_log.request_only_sources)

    def test_targeted_smoke_only_uses_direct_data_go_price_without_full_universe(self):
        http_client = MockHttpClient(
            json_by_url_token={
                "GetStockSecuritiesInfoService": DATA_GO_STOCK_PRICE_PAYLOAD,
                "GetFinaStatInfoService": DATA_GO_FINANCIAL_PAYLOAD,
                "opendart": {"total_page": 1, "list": []},
            }
        )
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "DATA_GO_KR_SERVICE_KEY": "DATA_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    http_client=http_client,
                    budget=KoreaLiveLiteBudget(
                        max_data_go_kr_calls_per_day=10,
                        max_symbols_for_event_search=0,
                        max_symbols_for_deep_research=0,
                    ),
                    targeted_smoke_enabled=True,
                    targeted_smoke_only=True,
                    targeted_smoke_symbol="999999",
                    targeted_smoke_company="라이브전력",
                    targeted_smoke_queries=("라이브전력 실적",),
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                    theme_rebalance_enabled=False,
                    company_guide_enabled=False,
                )
            )

        stock_price_requests = [request for request in result.run_log.built_requests if "GetStockSecuritiesInfoService" in request.url]
        self.assertEqual(len(stock_price_requests), 1)
        self.assertEqual(stock_price_requests[0].params["likeSrtnCd"], "999999")
        self.assertEqual(stock_price_requests[0].params["numOfRows"], 1000)
        self.assertNotIn("pageNo", stock_price_requests[0].params)
        financial_requests = [request for request in result.run_log.built_requests if "GetFinaStatInfoService" in request.url]
        self.assertEqual(len(financial_requests), 3)
        self.assertTrue(all(request.params["likeSrtnCd"] == "999999" for request in financial_requests))
        self.assertFalse(any("corpNm" in request.params for request in financial_requests))
        self.assertFalse(any("GetKrxListedInfoService" in request.url for request in result.run_log.built_requests))
        self.assertEqual(result.run_log.source_modes["data_go_kr"], "live_targeted")
        self.assertEqual(result.run_log.source_call_counts["data_go_kr_calls"], 4)
        smoke = next(item for item in result.run_log.targeted_smoke_results if item["symbol"] == "999999")
        self.assertEqual(smoke["feature_input_counts"]["price_bars"], 2)
        self.assertTrue(any(item.source_type == "financial_actual" and item.symbol == "999999" for item in result.evidence))

    def test_opendart_single_account_live_financials_feed_base_feature_input(self):
        http_client = MockHttpClient(
            json_by_url_token={
                "GetKrxListedInfoService": DATA_GO_LISTED_ITEMS_PAYLOAD,
                "GetStockSecuritiesInfoService": DATA_GO_STOCK_PRICE_PAYLOAD,
                "GetFinaStatInfoService": DATA_GO_FINANCIAL_PAYLOAD,
                "fnlttSinglAcnt": OPENDART_SINGLE_ACCOUNT_PAYLOAD,
                "opendart": OPENDART_DISCLOSURE_WITH_CORP_PAYLOAD,
            }
        )
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "DATA_GO_KR_SERVICE_KEY": "DATA_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    http_client=http_client,
                    budget=KoreaLiveLiteBudget(
                        max_data_go_kr_calls_per_day=10,
                        max_opendart_calls_per_day=10,
                        max_symbols_for_event_search=10,
                        max_symbols_for_deep_research=10,
                    ),
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        self.assertEqual(result.run_log.source_call_counts["opendart_financial_statement_calls"], 5)
        self.assertTrue(
            any(
                item.source_type == "financial_actual"
                and item.symbol == "999999"
                and item.title == "Reported financials 2024-03-31"
                for item in result.evidence
            )
        )
        self.assertTrue(
            any(
                item.source_type == "financial_actual"
                and item.symbol == "999999"
                and item.source_name == "OpenDART single account"
                and item.parsed_fields["operating_profit"] == 25000000000.0
                and item.parsed_fields["cashflow_from_operations"] == 30000000000.0
                and item.parsed_fields["capex"] == 7000000000.0
                and item.parsed_fields["fcf"] == 23000000000.0
                and item.parsed_fields["equity"] == 80000000000.0
                for item in result.evidence
            )
        )

    def test_opendart_single_account_uses_corp_code_map_when_recent_disclosure_missing(self):
        http_client = MockHttpClient(
            json_by_url_token={
                "GetStockSecuritiesInfoService": DATA_GO_STOCK_PRICE_PAYLOAD,
                "GetFinaStatInfoService": {"response": {"body": {"items": {"item": []}, "totalCount": 0}}},
                "fnlttSinglAcnt": OPENDART_SINGLE_ACCOUNT_PAYLOAD,
                "opendart": {"total_page": 1, "list": []},
            },
            bytes_by_url_token={
                "corpCode.xml": _opendart_corp_code_zip(
                    (
                        ("00199999", "라이브전력", "999999", "20240501"),
                        ("00188888", "다른회사", "888888", "20240501"),
                    )
                )
            },
        )
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "DATA_GO_KR_SERVICE_KEY": "DATA_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    http_client=http_client,
                    budget=KoreaLiveLiteBudget(
                        max_data_go_kr_calls_per_day=10,
                        max_opendart_calls_per_day=10,
                        max_opendart_detail_fetches_per_run=0,
                        max_symbols_for_event_search=0,
                        max_symbols_for_deep_research=0,
                    ),
                    targeted_smoke_enabled=True,
                    targeted_smoke_only=True,
                    targeted_smoke_symbol="999999",
                    targeted_smoke_company="라이브전력",
                    targeted_smoke_queries=("라이브전력 실적",),
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                    theme_rebalance_enabled=False,
                    company_guide_enabled=False,
                )
            )

        corp_code_requests = [request for request in result.run_log.built_requests if "corpCode.xml" in request.url]
        self.assertEqual(len(corp_code_requests), 1)
        self.assertNotIn("crtfc_key", corp_code_requests[0].params)
        opendart_financial_requests = [request for request in result.run_log.built_requests if "fnlttSinglAcntAll" in request.url]
        self.assertEqual(len(opendart_financial_requests), 5)
        self.assertTrue(all(request.params["corp_code"] == "00199999" for request in opendart_financial_requests))
        self.assertEqual(result.run_log.source_call_counts["opendart_company_code_calls"], 1)
        self.assertEqual(result.run_log.source_call_counts["opendart_financial_statement_calls"], 5)
        smoke = next(item for item in result.run_log.targeted_smoke_results if item["symbol"] == "999999")
        self.assertGreaterEqual(smoke["feature_input_counts"]["financial_actuals"], 1)
        self.assertTrue(
            any(
                item.source_type == "financial_actual"
                and item.symbol == "999999"
                and item.source_name == "OpenDART single account"
                for item in result.evidence
            )
        )

    def test_selected_candidate_opendart_disclosures_feed_base_feature_input(self):
        http_client = MockHttpClient(
            json_by_url_token={
                "GetStockSecuritiesInfoService": DATA_GO_STOCK_PRICE_PAYLOAD,
                "GetFinaStatInfoService": {"response": {"body": {"items": {"item": []}, "totalCount": 0}}},
                "corp_code=00199999": OPENDART_DISCLOSURE_WITH_CORP_PAYLOAD,
                "fnlttSinglAcnt": {"status": "000", "message": "정상", "list": []},
                "opendart": {"total_page": 1, "list": []},
            },
            bytes_by_url_token={
                "corpCode.xml": _opendart_corp_code_zip(
                    (
                        ("00199999", "라이브전력", "999999", "20240501"),
                        ("00188888", "다른회사", "888888", "20240501"),
                    )
                )
            },
        )
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "DATA_GO_KR_SERVICE_KEY": "DATA_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    http_client=http_client,
                    targeted_smoke_enabled=True,
                    targeted_smoke_only=True,
                    targeted_smoke_symbol="999999",
                    targeted_smoke_company="라이브전력",
                    targeted_smoke_queries=("라이브전력 실적",),
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                    theme_rebalance_enabled=False,
                    company_guide_enabled=False,
                )
            )

        smoke = next(item for item in result.run_log.targeted_smoke_results if item["symbol"] == "999999")
        self.assertEqual(result.run_log.source_call_counts["opendart_company_code_calls"], 1)
        self.assertEqual(result.run_log.source_call_counts["opendart_symbol_disclosure_calls"], 1)
        self.assertEqual(smoke["feature_input_counts"]["disclosures"], 1)
        self.assertTrue(
            any(
                item.source_type == "disclosure"
                and item.symbol == "999999"
                and item.title == "분기보고서"
                for item in result.evidence
            )
        )

    def test_opendart_disclosure_scan_reserves_budget_for_financial_actuals(self):
        disclosure_payload = dict(OPENDART_DISCLOSURE_WITH_CORP_PAYLOAD)
        disclosure_payload["total_page"] = 99
        http_client = MockHttpClient(
            json_by_url_token={
                "GetKrxListedInfoService": DATA_GO_LISTED_ITEMS_PAYLOAD,
                "GetStockSecuritiesInfoService": DATA_GO_STOCK_PRICE_PAYLOAD,
                "GetFinaStatInfoService": DATA_GO_FINANCIAL_PAYLOAD,
                "fnlttSinglAcnt": OPENDART_SINGLE_ACCOUNT_PAYLOAD,
                "opendart": disclosure_payload,
            }
        )
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "DATA_GO_KR_SERVICE_KEY": "DATA_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    http_client=http_client,
                    budget=KoreaLiveLiteBudget(
                        max_data_go_kr_calls_per_day=10,
                        max_opendart_calls_per_day=4,
                        max_opendart_detail_fetches_per_run=0,
                        max_symbols_for_event_search=10,
                        max_symbols_for_deep_research=10,
                    ),
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        self.assertEqual(result.run_log.source_call_counts["opendart_disclosure_date_range"], 1)
        self.assertEqual(result.run_log.source_call_counts["opendart_financial_statement_calls"], 3)
        self.assertTrue(
            any(
                item.source_type == "financial_actual"
                and item.symbol == "999999"
                and item.source_name == "OpenDART single account"
                for item in result.evidence
            )
        )

    def test_data_go_scan_reserves_budget_for_candidate_financial_actuals(self):
        http_client = MockHttpClient(
            json_by_url_token={
                "GetKrxListedInfoService": DATA_GO_LISTED_ITEMS_PAYLOAD,
                "GetStockSecuritiesInfoService": DATA_GO_STOCK_PRICE_PAYLOAD,
                "GetFinaStatInfoService": DATA_GO_FINANCIAL_PAYLOAD,
                "opendart": OPENDART_DISCLOSURE_WITH_CORP_PAYLOAD,
            }
        )
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "DATA_GO_KR_SERVICE_KEY": "DATA_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    http_client=http_client,
                    targeted_smoke_enabled=True,
                    targeted_smoke_symbol="999999",
                    targeted_smoke_company="라이브전력",
                    budget=KoreaLiveLiteBudget(
                        max_data_go_kr_calls_per_day=5,
                        max_opendart_calls_per_day=10,
                        max_opendart_detail_fetches_per_run=0,
                        max_symbols_for_event_search=0,
                        max_symbols_for_deep_research=0,
                        max_naver_search_calls_per_day=10,
                    ),
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        self.assertEqual(result.run_log.source_call_counts["data_go_kr_calls"], 5)
        self.assertEqual(result.run_log.source_call_counts["data_go_kr_financial_actual_calls"], 3)
        smoke = next(item for item in result.run_log.targeted_smoke_results if item["symbol"] == "999999")
        self.assertGreaterEqual(smoke["feature_input_counts"]["financial_actuals"], 1)

    def test_base_feature_input_loads_local_consensus_connector_as_independent_family(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "kr_consensus.csv").write_text(
                "\n".join(
                    (
                        "symbol,as_of_date,fiscal_year,op_e,eps_e,fcf_e,analyst_count,target_price,source",
                        "009999,2024-05-20,2024,1200,340,800,5,70000,fixture-consensus",
                    )
                ),
                encoding="utf-8",
            )
            (root / "kr_consensus_revisions.csv").write_text(
                "\n".join(
                    (
                        "symbol,as_of_date,fiscal_year,eps_revision_1m,op_revision_1m,fcf_revision_1m,"
                        "target_price_revision_1m,analyst_count_change,source",
                        "009999,2024-05-20,2024,12.5,18.0,9.0,7.5,2,fixture-consensus",
                    )
                ),
                encoding="utf-8",
            )
            for name in ("us_consensus.csv", "us_consensus_revisions.csv"):
                (root / name).write_text("symbol,as_of_date,fiscal_year,source\n", encoding="utf-8")

            candidate = CheapScanCandidate(
                symbol="009999",
                company_name="테스트반도체",
                market=Market.KR,
                as_of_date=AS_OF,
                reason_codes=("TARGETED_SMOKE",),
                cheap_scan_total_score=0.0,
                recommended_next_layer=RecommendedNextLayer.EVENT_SEARCH,
                candidate_source_path="targeted_smoke",
                test_injected=True,
                production_candidate=False,
            )
            config = KoreaLiveLiteConfig(
                as_of_date=AS_OF,
                consensus_connector=ConsensusCSVConnector(fixture_root=root),
            )

            feature_input = _base_feature_input_for_candidate(
                candidate=candidate,
                sources=KoreaCheapScanSources(),
                instruments=(),
                config=config,
                connector_consensus=_consensus_connector_snapshots_for_candidate(candidate, config),
                connector_consensus_revisions=_consensus_connector_revisions_for_candidate(candidate, config),
            )

            self.assertIsNotNone(feature_input)
            assert feature_input is not None
            self.assertEqual(len(feature_input.consensus), 1)
            self.assertEqual(len(feature_input.consensus_revisions), 1)
            self.assertEqual(feature_input.consensus[0].source, "fixture-consensus")
            self.assertEqual(feature_input.consensus_revisions[0].source, "fixture-consensus")
            self.assertEqual(feature_input.consensus[0].op_e, 1200.0)
            self.assertEqual(feature_input.consensus_revisions[0].op_revision_1m, 18.0)
            engineered = DeterministicFeatureEngineer().engineer(feature_input)
            self.assertEqual(engineered.payload.diagnostic_scores["evidence_family_consensus"], 1.0)
            self.assertEqual(engineered.payload.diagnostic_scores["evidence_family_consensus_revision"], 1.0)
            self.assertEqual(engineered.payload.diagnostic_scores["evidence_family_consensus_proxy"], 0.0)
            self.assertEqual(engineered.payload.diagnostic_scores["evidence_family_consensus_revision_proxy"], 0.0)

    def test_company_guide_empty_snapshot_consensus_is_counted_without_hiding_recent_reports(self):
        candidate = CheapScanCandidate(
            symbol="999999",
            company_name="라이브전력",
            market=Market.KR,
            as_of_date=AS_OF,
            reason_codes=("TARGETED_SMOKE",),
            cheap_scan_total_score=0.0,
            recommended_next_layer=RecommendedNextLayer.EVENT_SEARCH,
            candidate_source_path="targeted_smoke",
            test_injected=True,
            production_candidate=False,
        )
        http_client = MockHttpClient(
            json_by_url_token={
                "c1080001_data.aspx?cmp_cd=999999": {
                    "lists": [
                        {
                            "RPT_ID": 24052101,
                            "ANL_DT": "24/05/21",
                            "IDX": "20240521.000001",
                            "RPT_TITLE": "라이브전력 실적 가시성 확대",
                            "TARGET_PRC": "120,000",
                            "RECOMM": "Buy",
                            "COMMENT": "목표주가 상향 및 EPS 상향",
                            "PAGE_CNT": 5,
                            "FILE_NM": "1F00120240521_999999.pdf",
                            "CLOSE_PRC": "85,000",
                            "EPS": 12345.0,
                            "BRK_NM_SHORT_KOR": "테스트증권",
                            "ANL_NM_KOR": "홍길동",
                            "PRC_ACTION_TYP_NM": "목표주가 상향",
                            "EPS_ACTION_TYP_NM": "추정EPS 상향",
                            "RECOMM_ACTION_TYP_NM": "변동없음",
                        }
                    ]
                },
            },
            text_by_url_token={
                "c1010001.aspx?cmp_cd=999999": _company_guide_empty_consensus_html(),
            },
        )
        config = KoreaLiveLiteConfig(
            as_of_date=AS_OF,
            fixture_mode=False,
            live_enabled=True,
            budget=KoreaLiveLiteBudget(max_company_guide_calls_per_day=2),
            http_client=http_client,
        )
        source_call_counts = {
            "company_guide_snapshot_calls": 0,
            "company_guide_snapshot_empty_consensus_count": 0,
            "company_guide_recent_report_calls": 0,
        }
        source_modes: dict[str, str] = {}
        fallback_reasons: dict[str, str] = {}

        data = _execute_company_guide_for_candidates(
            candidates=(candidate,),
            config=config,
            effective_fixture_mode=False,
            http_client=http_client,
            built_requests=[],
            source_call_counts=source_call_counts,
            source_modes=source_modes,
            fallback_reasons=fallback_reasons,
        )

        self.assertEqual(source_modes["company_guide"], "live_executed")
        self.assertNotIn("company_guide", fallback_reasons)
        self.assertEqual(source_call_counts["company_guide_snapshot_calls"], 1)
        self.assertEqual(source_call_counts["company_guide_snapshot_empty_consensus_count"], 1)
        self.assertEqual(source_call_counts["company_guide_recent_report_calls"], 1)
        self.assertEqual(len(data["999999"].consensus), 0)
        self.assertEqual(len(data["999999"].consensus_revisions), 0)
        self.assertEqual(len(data["999999"].research_reports), 1)

    def test_company_guide_empty_consensus_keeps_structured_broker_target_revision(self):
        candidate = CheapScanCandidate(
            symbol="999999",
            company_name="라이브전력",
            market=Market.KR,
            as_of_date=AS_OF,
            reason_codes=("TARGETED_SMOKE",),
            cheap_scan_total_score=0.0,
            recommended_next_layer=RecommendedNextLayer.EVENT_SEARCH,
            candidate_source_path="targeted_smoke",
            test_injected=True,
            production_candidate=False,
        )
        http_client = MockHttpClient(
            json_by_url_token={},
            text_by_url_token={
                "c1010001.aspx?cmp_cd=999999": _company_guide_empty_consensus_with_broker_targets_html(),
            },
        )
        config = KoreaLiveLiteConfig(
            as_of_date=AS_OF,
            fixture_mode=False,
            live_enabled=True,
            budget=KoreaLiveLiteBudget(max_company_guide_calls_per_day=1),
            http_client=http_client,
        )
        source_call_counts = {
            "company_guide_snapshot_calls": 0,
            "company_guide_snapshot_empty_consensus_count": 0,
            "company_guide_recent_report_calls": 0,
        }
        source_modes: dict[str, str] = {}
        fallback_reasons: dict[str, str] = {}

        data = _execute_company_guide_for_candidates(
            candidates=(candidate,),
            config=config,
            effective_fixture_mode=False,
            http_client=http_client,
            built_requests=[],
            source_call_counts=source_call_counts,
            source_modes=source_modes,
            fallback_reasons=fallback_reasons,
        )

        revisions = data["999999"].consensus_revisions
        self.assertEqual(source_modes["company_guide"], "live_executed")
        self.assertNotIn("company_guide", fallback_reasons)
        self.assertEqual(source_call_counts["company_guide_snapshot_calls"], 1)
        self.assertEqual(source_call_counts["company_guide_snapshot_empty_consensus_count"], 1)
        self.assertEqual(source_call_counts["company_guide_recent_report_calls"], 0)
        self.assertEqual(len(data["999999"].consensus), 0)
        self.assertEqual(len(revisions), 1)
        self.assertEqual(revisions[0].source, "company_guide_snapshot")
        self.assertEqual(revisions[0].target_price_revision_1m, 10.0)
        self.assertEqual(revisions[0].analyst_count_change, 2)
        self.assertTrue(revisions[0].parsed_fields["company_guide_broker_target_revision_structured"])
        self.assertTrue(revisions[0].parsed_fields["structured_consensus_revision_source"])
        self.assertNotIn("consensus_proxy_created", revisions[0].parsed_fields)
        engineered = DeterministicFeatureEngineer().engineer(
            FeatureEngineeringInput(
                symbol="999999",
                company_name="라이브전력",
                as_of_date=AS_OF,
                consensus_revisions=revisions,
            )
        )
        diagnostics = engineered.payload.diagnostic_scores
        self.assertEqual(diagnostics["evidence_family_consensus"], 0.0)
        self.assertEqual(diagnostics["evidence_family_consensus_revision"], 1.0)
        self.assertEqual(diagnostics["evidence_family_consensus_revision_proxy"], 0.0)

    def test_naver_finance_item_main_feeds_structured_consensus_snapshot(self):
        candidate = CheapScanCandidate(
            symbol="999999",
            company_name="라이브전력",
            market=Market.KR,
            as_of_date=AS_OF,
            reason_codes=("TARGETED_SMOKE",),
            cheap_scan_total_score=0.0,
            recommended_next_layer=RecommendedNextLayer.EVENT_SEARCH,
            candidate_source_path="targeted_smoke",
            test_injected=True,
            production_candidate=False,
        )
        http_client = MockHttpClient(
            json_by_url_token={},
            text_by_url_token={
                "item/main.nhn?code=999999": _naver_finance_item_main_consensus_html("2024.05.21"),
            },
        )
        config = KoreaLiveLiteConfig(
            as_of_date=AS_OF,
            fixture_mode=False,
            live_enabled=True,
            budget=KoreaLiveLiteBudget(max_naver_finance_calls_per_day=1),
            http_client=http_client,
        )
        source_call_counts = {"naver_finance_item_main_calls": 0}
        source_modes: dict[str, str] = {}
        fallback_reasons: dict[str, str] = {}

        data = _execute_naver_finance_for_candidates(
            candidates=(candidate,),
            config=config,
            effective_fixture_mode=False,
            http_client=http_client,
            built_requests=[],
            source_call_counts=source_call_counts,
            source_modes=source_modes,
            fallback_reasons=fallback_reasons,
        )

        consensus = data["999999"].consensus
        self.assertEqual(source_modes["naver_finance"], "live_executed")
        self.assertNotIn("naver_finance", fallback_reasons)
        self.assertEqual(source_call_counts["naver_finance_item_main_calls"], 1)
        self.assertEqual(len(consensus), 1)
        self.assertEqual(consensus[0].source, "naver_finance_item_main")
        self.assertEqual(consensus[0].fiscal_year, 2025)
        self.assertEqual(consensus[0].sales_e, 1_200_000.0)
        self.assertEqual(consensus[0].op_e, 120_000.0)
        self.assertEqual(consensus[0].eps_e, 12_345.0)
        self.assertEqual(consensus[0].target_price, 120_000.0)
        self.assertTrue(consensus[0].parsed_fields["structured_consensus_source"])
        self.assertNotIn("consensus_proxy_created", consensus[0].parsed_fields)
        engineered = DeterministicFeatureEngineer().engineer(
            FeatureEngineeringInput(
                symbol="999999",
                company_name="라이브전력",
                as_of_date=AS_OF,
                consensus=consensus,
            )
        )
        diagnostics = engineered.payload.diagnostic_scores
        self.assertEqual(diagnostics["evidence_family_consensus"], 1.0)
        self.assertEqual(diagnostics["evidence_family_consensus_structured"], 1.0)
        self.assertEqual(diagnostics["evidence_family_consensus_proxy"], 0.0)

    def test_naver_finance_future_item_main_date_is_not_score_eligible(self):
        candidate = CheapScanCandidate(
            symbol="999999",
            company_name="라이브전력",
            market=Market.KR,
            as_of_date=AS_OF,
            reason_codes=("TARGETED_SMOKE",),
            cheap_scan_total_score=0.0,
            recommended_next_layer=RecommendedNextLayer.EVENT_SEARCH,
            candidate_source_path="targeted_smoke",
            test_injected=True,
            production_candidate=False,
        )
        http_client = MockHttpClient(
            json_by_url_token={},
            text_by_url_token={
                "item/main.nhn?code=999999": _naver_finance_item_main_consensus_html("2024.05.22"),
            },
        )
        config = KoreaLiveLiteConfig(
            as_of_date=AS_OF,
            fixture_mode=False,
            live_enabled=True,
            budget=KoreaLiveLiteBudget(max_naver_finance_calls_per_day=1),
            http_client=http_client,
        )
        source_call_counts = {"naver_finance_item_main_calls": 0}
        source_modes: dict[str, str] = {}
        fallback_reasons: dict[str, str] = {}

        data = _execute_naver_finance_for_candidates(
            candidates=(candidate,),
            config=config,
            effective_fixture_mode=False,
            http_client=http_client,
            built_requests=[],
            source_call_counts=source_call_counts,
            source_modes=source_modes,
            fallback_reasons=fallback_reasons,
        )

        self.assertEqual(data, {})
        self.assertEqual(source_modes["naver_finance"], "fallback")
        self.assertEqual(source_call_counts["naver_finance_item_main_calls"], 1)
        self.assertEqual(
            fallback_reasons["naver_finance"],
            "naver_finance_item_main_parse_failed:ValueError",
        )

    def test_company_guide_live_enrichment_feeds_consensus_and_reports_to_pipeline(self):
        http_client = MockHttpClient(
            json_by_url_token={
                "GetKrxListedInfoService": DATA_GO_LISTED_ITEMS_PAYLOAD,
                "GetStockSecuritiesInfoService": DATA_GO_STOCK_PRICE_PAYLOAD,
                "GetFinaStatInfoService": DATA_GO_FINANCIAL_PAYLOAD,
                "opendart": {"total_page": 1, "list": []},
                "c1080001_data.aspx?cmp_cd=999999": {
                    "lists": [
                        {
                            "RPT_ID": 24052101,
                            "ANL_DT": "24/05/21",
                            "IDX": "20240521.000001",
                            "RPT_TITLE": "라이브전력 실적 가시성 확대",
                            "TARGET_PRC": "120,000",
                            "RECOMM": "Buy",
                            "COMMENT": "수주잔고 증가<br/>목표주가 상향 및 EPS 상향",
                            "PAGE_CNT": 5,
                            "FILE_NM": "1F00120240521_999999.pdf",
                            "CLOSE_PRC": "85,000",
                            "EPS": 12345.0,
                            "BRK_NM_SHORT_KOR": "테스트증권",
                            "ANL_NM_KOR": "홍길동",
                            "PRC_ACTION_TYP_NM": "목표주가 상향",
                            "EPS_ACTION_TYP_NM": "추정EPS 상향",
                            "RECOMM_ACTION_TYP_NM": "변동없음",
                        }
                    ]
                },
            },
            text_by_url_token={
                "c1010001.aspx?cmp_cd=999999": _company_guide_live_lite_consensus_html(),
            },
        )
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "DATA_GO_KR_SERVICE_KEY": "DATA_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    http_client=http_client,
                    targeted_smoke_enabled=True,
                    targeted_smoke_symbol="999999",
                    targeted_smoke_company="라이브전력",
                    budget=KoreaLiveLiteBudget(
                        max_data_go_kr_calls_per_day=5,
                        max_opendart_calls_per_day=10,
                        max_opendart_detail_fetches_per_run=0,
                        max_symbols_for_event_search=0,
                        max_symbols_for_deep_research=0,
                        max_naver_search_calls_per_day=10,
                        max_company_guide_calls_per_day=2,
                    ),
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        smoke = next(item for item in result.run_log.targeted_smoke_results if item["symbol"] == "999999")
        self.assertEqual(result.run_log.source_modes["company_guide"], "live_executed")
        self.assertEqual(result.run_log.source_call_counts["company_guide_snapshot_calls"], 1)
        self.assertEqual(result.run_log.source_call_counts["company_guide_recent_report_calls"], 1)
        self.assertEqual(smoke["feature_input_counts"]["consensus"], 1)
        self.assertEqual(smoke["feature_input_counts"]["consensus_revisions"], 1)
        self.assertEqual(smoke["feature_input_counts"]["research_reports"], 1)
        self.assertIn("failed_green_gates", smoke)
        self.assertIn("stage_gate_diagnostics", smoke)
        self.assertIn("failed_gate_names", smoke["stage_gate_diagnostics"])
        self.assertTrue(any(item.source_type == "consensus" and item.symbol == "999999" for item in result.evidence))
        self.assertTrue(any(item.source_type == "consensus_revision" and item.symbol == "999999" for item in result.evidence))
        self.assertTrue(any(item.source_type == "research_report" and item.symbol == "999999" for item in result.evidence))

    def test_live_lite_can_run_with_data_go_v2_endpoint_config(self):
        http_client = MockHttpClient(
            json_by_url_token={
                "GetKrxListedInfoService": DATA_GO_LISTED_ITEMS_PAYLOAD,
                "GetStockSecuritiesInfoService": DATA_GO_STOCK_PRICE_PAYLOAD,
                "opendart": {"total_page": 1, "list": []},
            }
        )
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "DATA_GO_KR_SERVICE_KEY": "DATA_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }
        sources = KoreaCheapScanSources(
            krx=KRXConnector(),
            opendart=OpenDARTConnector(),
            kind=KINDConnector(),
            fsc=DataGoKrFSCConnector(
                financial_info_service_path="GetFinaStatInfoService_V2/getSummFinaStat_V2",
                disclosure_info_service_path="GetDiscInfoService_V2/getDiviDiscInfo_V2",
                corp_basic_info_service_path="GetCorpBasicInfoService_V2/getCorpOutline_V2",
            ),
        )

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    sources=sources,
                    http_client=http_client,
                    budget=KoreaLiveLiteBudget(max_data_go_kr_calls_per_day=10),
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        self.assertEqual(result.run_log.source_modes["data_go_kr"], "live_executed")
        self.assertEqual(result.run_log.source_modes["stock_issuance"], "disabled_optional")

    def test_data_go_live_budget_is_respected_and_falls_back_before_calls(self):
        http_client = MockHttpClient(
            json_by_url_token={
                "GetKrxListedInfoService": DATA_GO_LISTED_ITEMS_PAYLOAD,
                "GetStockSecuritiesInfoService": DATA_GO_STOCK_PRICE_PAYLOAD,
                "opendart": {"total_page": 1, "list": []},
            }
        )
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "DATA_GO_KR_SERVICE_KEY": "DATA_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    http_client=http_client,
                    budget=KoreaLiveLiteBudget(max_data_go_kr_calls_per_day=1),
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )

        self.assertEqual(result.run_log.source_modes["data_go_kr"], "fallback")
        self.assertEqual(result.run_log.fallback_reasons["data_go_kr"], "data_go_kr_budget_too_low_for_universe_and_price")
        self.assertLessEqual(result.run_log.source_call_counts["data_go_kr_calls"], 1)
        self.assertFalse(any("GetKrxListedInfoService" in item.url for item in http_client.requests))

    def test_data_go_live_failure_falls_back_without_logging_key(self):
        http_client = MockHttpClient(json_by_url_token={"opendart": {"total_page": 1, "list": []}})
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "DATA_GO_KR_SERVICE_KEY": "DATA_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    http_client=http_client,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )
            run_log_text = result.run_log_path.read_text(encoding="utf-8")

        self.assertEqual(result.run_log.source_modes["data_go_kr"], "fallback")
        self.assertEqual(result.run_log.fallback_reasons["data_go_kr"], "data_go_kr_listed_items_failed")
        self.assertGreaterEqual(result.run_log.live_requests_failed, 1)
        self.assertNotIn("DATA_SECRET", run_log_text)

    def test_api_keys_are_not_written_to_run_log(self):
        http_client = MockHttpClient(json_by_url_token={"opendart": {"total_page": 1, "list": []}})
        env = {
            "OPENDART_API_KEY": "OPENDART_SECRET",
            "DATA_GO_KR_SERVICE_KEY": "DATA_SECRET",
            "NAVER_CLIENT_ID": "NAVER_ID",
            "NAVER_CLIENT_SECRET": "NAVER_SECRET",
        }

        with tempfile.TemporaryDirectory() as output_dir, patch.dict("os.environ", env, clear=True):
            result = KoreaLiveLiteRunner().run(
                KoreaLiveLiteConfig(
                    as_of_date=AS_OF,
                    output_directory=output_dir,
                    fixture_mode=False,
                    live_enabled=True,
                    http_client=http_client,
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=EmptySearchProvider(),
                )
            )
            run_log_text = result.run_log_path.read_text(encoding="utf-8")

        self.assertNotIn("OPENDART_SECRET", run_log_text)
        self.assertNotIn("NAVER_SECRET", run_log_text)
        self.assertNotIn("DATA_SECRET", run_log_text)


STRONG_SINGLE_REPORT_TEXT = """
발행일 2024.05.21
증권사: FixtureBroker
애널리스트: Fixture Analyst
제목: 가격만강세 줄을 서시오
현재가 8,100원
목표주가 18,000원
목표주가 상향 60%
상승여력 120%
FY1 매출액 3,300,000 영업이익 620,000 EPS 13,500
FY2 매출액 3,800,000 영업이익 720,000 EPS 15,800
PER 4.0배
PBR 0.8배
ROE 28%
OPM 22.0%
영업이익 YoY 300%
EPS YoY 260%
FCF 증가율 220%
EPS 상향 55%
영업이익 추정치 상향 50%
FCF 질 점수 95
수주잔고 5,000,000
신규수주 2,000,000
수주잔고/매출 220%
계약기간 72개월
계약 매출액 대비 80%
선수금 있음
해지 불가
사상 최대 수주잔고
CAPA 증가율 45%
CAPA utilization 98%
CAPA 선점 3년
CAPA 부족으로 리드타임 24개월 이상이다.
ASP YoY 25%
판가 전가 확인
구조적 공급부족이 지속된다.
멀티플 상향과 리레이팅 구간이다.
OPM 개선폭 12%
CAPEX/매출 20%
투자포인트: 수주잔고 확대|마진 개선|북미 전력망 병목
리스크: 증설 지연|원가 변동
"""

IMPOSSIBLE_CONTRACT_REPORT_TEXT = STRONG_SINGLE_REPORT_TEXT.replace("가격만강세", "케이전력").replace("계약 매출액 대비 80%", "계약 매출액 대비 600%")

DATA_GO_LISTED_ITEMS_PAYLOAD = {
    "response": {
        "body": {
            "items": {
                "item": [
                    {
                        "basDt": "20240521",
                        "srtnCd": "A999999",
                        "isinCd": "KR7999990000",
                        "itmsNm": "라이브전력",
                        "corpNm": "라이브전력",
                        "mrktCtg": "KOSDAQ",
                    }
                ]
            },
            "totalCount": 1,
            "numOfRows": 1000,
            "pageNo": 1,
        }
    }
}

DATA_GO_STOCK_PRICE_PAYLOAD = {
    "response": {
        "body": {
            "items": {
                "item": [
                    {
                        "basDt": "20240301",
                        "srtnCd": "999999",
                        "itmsNm": "라이브전력",
                        "mkp": "10000",
                        "hipr": "11000",
                        "lopr": "9000",
                        "clpr": "10000",
                        "trqu": "10000",
                        "trPrc": "100000000",
                        "mrktTotAmt": "100000000000",
                    },
                    {
                        "basDt": "20240521",
                        "srtnCd": "999999",
                        "itmsNm": "라이브전력",
                        "mkp": "15000",
                        "hipr": "16200",
                        "lopr": "14900",
                        "clpr": "16000",
                        "trqu": "60000",
                        "trPrc": "900000000",
                        "mrktTotAmt": "160000000000",
                    },
                ]
            },
            "totalCount": 2,
            "numOfRows": 1000,
            "pageNo": 1,
        }
    }
}

DATA_GO_FINANCIAL_PAYLOAD = {
    "response": {
        "body": {
            "items": {
                "item": [
                    {
                        "bizYear": "2023",
                        "srtnCd": "999999",
                        "corpNm": "라이브전력",
                        "saleAmt": "100000000000",
                        "bzopPft": "25000000000",
                        "crtmNpf": "20000000000",
                        "eps": "1200",
                        "opm": "25",
                    }
                ]
            },
            "totalCount": 1,
            "numOfRows": 10,
            "pageNo": 1,
        }
    }
}

OPENDART_DISCLOSURE_WITH_CORP_PAYLOAD = {
    "total_page": 1,
    "list": [
        {
            "corp_code": "00199999",
            "corp_name": "라이브전력",
            "stock_code": "999999",
            "corp_cls": "Y",
            "report_nm": "분기보고서",
            "rcept_no": "20240521000001",
            "rcept_dt": "20240521",
        }
    ],
}

OPENDART_SINGLE_ACCOUNT_PAYLOAD = {
    "status": "000",
    "message": "정상",
    "list": [
        {
            "corp_code": "00199999",
            "bsns_year": "2023",
            "reprt_code": "11011",
            "fs_div": "CFS",
            "fs_nm": "연결재무제표",
            "sj_div": "IS",
            "account_nm": "매출액",
            "thstrm_amount": "100,000,000,000",
        },
        {
            "corp_code": "00199999",
            "bsns_year": "2023",
            "reprt_code": "11011",
            "fs_div": "CFS",
            "fs_nm": "연결재무제표",
            "sj_div": "IS",
            "account_nm": "영업이익(손실)",
            "thstrm_amount": "25,000,000,000",
        },
        {
            "corp_code": "00199999",
            "bsns_year": "2023",
            "reprt_code": "11011",
            "fs_div": "CFS",
            "fs_nm": "연결재무제표",
            "sj_div": "IS",
            "account_nm": "당기순이익",
            "thstrm_amount": "20,000,000,000",
        },
        {
            "corp_code": "00199999",
            "bsns_year": "2023",
            "reprt_code": "11011",
            "fs_div": "CFS",
            "fs_nm": "연결재무제표",
            "sj_div": "BS",
            "account_nm": "자본총계",
            "thstrm_amount": "80,000,000,000",
        },
        {
            "corp_code": "00199999",
            "bsns_year": "2023",
            "reprt_code": "11011",
            "fs_div": "CFS",
            "fs_nm": "연결재무제표",
            "sj_div": "CF",
            "account_nm": "영업활동현금흐름",
            "thstrm_amount": "30,000,000,000",
        },
        {
            "corp_code": "00199999",
            "bsns_year": "2023",
            "reprt_code": "11011",
            "fs_div": "CFS",
            "fs_nm": "연결재무제표",
            "sj_div": "CF",
            "account_nm": "유형자산의 취득",
            "thstrm_amount": "5,000,000,000",
        },
        {
            "corp_code": "00199999",
            "bsns_year": "2023",
            "reprt_code": "11011",
            "fs_div": "CFS",
            "fs_nm": "연결재무제표",
            "sj_div": "CF",
            "account_nm": "무형자산의 취득",
            "thstrm_amount": "2,000,000,000",
        },
    ],
}

def _candidate(result, symbol):
    for candidate in result.candidates:
        if candidate.symbol == symbol:
            return candidate
    raise AssertionError(f"candidate {symbol} not found")


def _disclosure(symbol, title, rcept_no):
    timestamp = datetime(2024, 5, 21, 9)
    return DisclosureEvent(
        symbol=symbol,
        source="OpenDART",
        report_type=title,
        title=title,
        published_at=timestamp,
        observed_at=timestamp,
        available_at=timestamp,
        as_of_date=AS_OF,
        rcept_no=rcept_no,
        raw_text=title,
        parsed_fields={},
    )


def _company_guide_live_lite_consensus_html():
    return """
    <p class="disc table">[기준:2024.05.21]</p>
    <table id="cTB15">
      <tr>
        <td rowspan="2"><span>4.10</span></td>
        <th>투자의견</th><th>목표주가<span>(원)</span></th><th>EPS<span>(원)</span></th>
        <th>PER<span>(배)</span></th><th>추정기관수</th>
      </tr>
      <tr>
        <td><b>4.10</b></td><td>120,000</td><td>12,345</td><td>9.72</td><td>7</td>
      </tr>
    </table>
    <table id="cTB24">
      <tbody>
        <tr>
          <td>테스트증권</td><td>24/05/21</td><td>120,000</td><td>100,000</td>
          <td><span>20.00</span></td><td>Buy</td><td>Buy</td>
        </tr>
      </tbody>
    </table>
    """


def _company_guide_empty_consensus_html():
    return """
    <p class="disc table">[기준:2024.05.21]</p>
    <table id="cTB15">
      <tr>
        <th>투자의견</th><th>목표주가<span>(원)</span></th><th>EPS<span>(원)</span></th>
        <th>PER<span>(배)</span></th><th>추정기관수</th>
      </tr>
      <tr><td colspan="5">최근3개월 이내에 제시된 의견이 없습니다</td></tr>
    </table>
    <table id="cTB24">
      <tbody></tbody>
    </table>
    """


def _company_guide_empty_consensus_with_broker_targets_html():
    return """
    <p class="disc table">[기준:2024.05.21]</p>
    <table id="cTB15">
      <tr>
        <th>투자의견</th><th>목표주가<span>(원)</span></th><th>EPS<span>(원)</span></th>
        <th>PER<span>(배)</span></th><th>추정기관수</th>
      </tr>
      <tr><td colspan="5">최근3개월 이내에 제시된 의견이 없습니다</td></tr>
    </table>
    <table id="cTB24">
      <tbody>
        <tr>
          <td>테스트증권</td><td>24/05/21</td><td>120,000</td><td>100,000</td>
          <td><span>20.00</span></td><td>Buy</td><td>Buy</td>
        </tr>
        <tr>
          <td>두번째증권</td><td>24/05/10</td><td>110,000</td><td>110,000</td>
          <td><span>0.00</span></td><td>Buy</td><td>Buy</td>
        </tr>
      </tbody>
    </table>
    """


def _naver_finance_item_main_consensus_html(page_date: str):
    return f"""
    <em class="date">{page_date} <span>기준(KRX 장마감)</span></em>
    <table summary="기업실적분석에 관한표이며 주요재무정보를 최근 연간 실적, 분기 실적에 따라 정보를 제공합니다.">
      <caption>기업실적분석 테이블</caption>
      <thead>
        <tr>
          <th>주요재무정보</th><th colspan="4">최근 연간 실적</th><th colspan="2">최근 분기 실적</th>
        </tr>
        <tr>
          <th></th>
          <th>2022.12</th><th>2023.12</th><th>2024.12</th><th>2025.12 (E)</th>
          <th>2024.03</th><th>2024.06 (E)</th>
        </tr>
        <tr>
          <th></th><th>IFRS연결</th><th>IFRS연결</th><th>IFRS연결</th><th>IFRS연결</th><th>IFRS연결</th><th>IFRS연결</th>
        </tr>
      </thead>
      <tbody>
        <tr><th>매출액</th><td>800,000</td><td>900,000</td><td>1,000,000</td><td>1,200,000</td><td>250,000</td><td>300,000</td></tr>
        <tr><th>영업이익</th><td>50,000</td><td>70,000</td><td>90,000</td><td>120,000</td><td>20,000</td><td>30,000</td></tr>
        <tr><th>당기순이익</th><td>40,000</td><td>60,000</td><td>80,000</td><td>100,000</td><td>18,000</td><td>28,000</td></tr>
        <tr><th>ROE(지배주주)</th><td>5.0</td><td>6.0</td><td>7.0</td><td>8.0</td><td>7.5</td><td></td></tr>
        <tr><th>EPS(원)</th><td>8,000</td><td>9,000</td><td>10,000</td><td>12,345</td><td>2,000</td><td>3,000</td></tr>
        <tr><th>PER(배)</th><td>12.0</td><td>11.0</td><td>10.0</td><td>9.72</td><td>11.0</td><td>12.0</td></tr>
        <tr><th>BPS(원)</th><td>40,000</td><td>45,000</td><td>50,000</td><td>60,000</td><td>52,000</td><td></td></tr>
        <tr><th>PBR(배)</th><td>2.0</td><td>1.9</td><td>1.8</td><td>1.7</td><td>1.8</td><td></td></tr>
      </tbody>
    </table>
    <p>컨센서스(E) : 최근 3개월간 증권사에서 발표한 전망치의 평균값입니다.</p>
    <table summary="투자의견 정보" class="rwidth">
      <caption>투자의견</caption>
      <tr>
        <th>투자의견<span class="bar">l</span>목표주가</th>
        <td><span><em>4.10</em>매수</span><span class="bar">l</span><em>120,000</em></td>
      </tr>
    </table>
    """


def _opendart_corp_code_zip(rows):
    body = ["<?xml version=\"1.0\" encoding=\"UTF-8\"?>", "<result>"]
    for corp_code, corp_name, stock_code, modify_date in rows:
        body.extend(
            [
                "  <list>",
                f"    <corp_code>{corp_code}</corp_code>",
                f"    <corp_name>{corp_name}</corp_name>",
                f"    <stock_code>{stock_code}</stock_code>",
                f"    <modify_date>{modify_date}</modify_date>",
                "  </list>",
            ]
        )
    body.append("</result>")
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        archive.writestr("CORPCODE.xml", "\n".join(body).encode("utf-8"))
    return buffer.getvalue()


class MockHttpClient:
    def __init__(self, json_by_url_token, text_by_url_token=None, bytes_by_url_token=None):
        self.json_by_url_token = dict(json_by_url_token)
        self.text_by_url_token = dict(text_by_url_token or {})
        self.bytes_by_url_token = dict(bytes_by_url_token or {})
        self.stats = HttpClientStats()
        self.requests = []

    def get_json(self, request, *, cache_path=None):
        self.requests.append(request)
        url = request.url + "?" + "&".join(f"{key}={value}" for key, value in request.params.items())
        for token, payload in self.json_by_url_token.items():
            if token in url:
                self.stats.live_requests_executed += 1
                if cache_path is not None:
                    self.stats.cache_writes += 1
                return HttpResult(ok=True, status_code=200, json_data=payload, text=json.dumps(payload), cache_path=str(cache_path) if cache_path else None)
        self.stats.live_requests_failed += 1
        return HttpResult(ok=False, error="mock_response_not_found")

    def get_text(self, request, *, cache_path=None):
        self.requests.append(request)
        url = request.url + "?" + "&".join(f"{key}={value}" for key, value in request.params.items())
        for token, text in self.text_by_url_token.items():
            if token in url:
                self.stats.live_requests_executed += 1
                if cache_path is not None:
                    path = Path(cache_path)
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text(text, encoding="utf-8")
                    self.stats.cache_writes += 1
                return HttpResult(ok=True, status_code=200, text=text, cache_path=str(cache_path) if cache_path else None)
        self.stats.live_requests_failed += 1
        return HttpResult(ok=False, error="mock_text_response_not_found")

    def get_bytes(self, request, *, cache_path=None):
        self.requests.append(request)
        url = request.url + "?" + "&".join(f"{key}={value}" for key, value in request.params.items())
        for token, payload in self.bytes_by_url_token.items():
            if token in url:
                self.stats.live_requests_executed += 1
                if cache_path is not None:
                    path = Path(cache_path)
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_bytes(payload)
                    self.stats.cache_writes += 1
                return HttpResult(ok=True, status_code=200, bytes_data=payload, cache_path=str(cache_path) if cache_path else None)
        self.stats.live_requests_failed += 1
        return HttpResult(ok=False, error="mock_bytes_response_not_found")


if __name__ == "__main__":
    unittest.main()
