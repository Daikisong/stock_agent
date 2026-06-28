from dataclasses import dataclass, field
from datetime import date, datetime
from email.message import Message
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from e2r.agentic import (
    CodexCLIAgenticEvidenceProvider,
    PrimitiveStateV2,
    PrimitiveStatus,
    ScoreContributionV2,
    load_evidence_contracts,
)
from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS
from e2r.evidence_ids import stable_consensus_evidence_id, stable_news_evidence_id
from e2r.models import Market, ScoreSnapshot, Stage
from e2r.features import FeatureEngineeringResult
from e2r.llm import CodexCLIThemeRouteProvider, EvidenceSlotStatus, FakeThemeRouteProvider, ThemeRouteOutput
from e2r.research import EmptySearchProvider
from e2r.research.browser_search_provider import BrowserSearchProvider
from e2r.research.free_web_research_runner import (
    AgenticEvidenceRuntimeTrace,
    FreeWebResearchInput,
    FreeWebResearchRunner,
    _ScoreGapExpansionResult,
    _FixedQueryPlanner,
    _asof_safe_theme_query,
    _combined_score_gap_context,
    _material_score_gaps,
    _post_gap_top_results,
    _post_score_gap_expansion_allowed,
    _record_agentic_workflow_metrics,
    _agentic_score_contribution_diagnostics,
    _agentic_score_contribution_archetype_id,
    _agentic_score_contributions_from_trace,
    _score_gap_audit_event,
    _score_gap_reason_codes,
    _score_gap_score_block_reason,
    _score_gap_missing_information,
    _score_gap_progress_diagnostics,
    _score_gap_state_repeated_rejection_reasons,
    _score_gap_state_signature,
    _stage_gate_missing_information,
    _field_matches_source_backed_slot,
    _source_field_contract_gap_context,
    _theme_route_contract_gap_context,
    _theme_route_provider_for_timeout,
    _with_score_gap_expansion_diagnostics,
    _with_agentic_score_contributions,
)
from e2r.research.manual_source_provider import ManualSource, ManualSourceProvider
from e2r.research.naver_search_provider import NaverFreeSearchProvider
from e2r.research.query_planner import QueryPlan, QuerySpec
from e2r.research.search_budget import SearchBudget
from e2r.research.search_provider import FixtureSearchProvider, SearchResult
from e2r.red_team import RedTeamAssessment
from e2r.scoring import ScoringPayload


ROOT = Path(__file__).resolve().parents[1]
HTML_ROOT = ROOT / "data/raw/search_html"
TEXT_ROOT = HTML_ROOT / "text"

HD_REPORT_URL = "https://ssl.pstatic.net/imgstock/upload/research/company/hd_줄을서시오.pdf"
HYOSUNG_REPORT_URL = "https://hanaw.com/download/research/hyosung_low_margin_cleanup.pdf"
ILJIN_DISCLOSURE_URL = "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=202311270001"
ILJIN_REPORT_URL = "https://file.alphasquare.co.kr/media/pdfs/iljin_transformer_capa.pdf"
ZOOM_NEWS_URL = "https://news.example.com/zoom-pandemic-eps"
ZOOM_REPORT_URL = "https://file.alphasquare.co.kr/media/pdfs/zoom_q2_2020_review.pdf"
ZOOM_SEC_URL = "https://www.sec.gov/Archives/edgar/data/zoom/q2-2020-10q"
SMCI_GUIDANCE_URL = "https://reuters.example.com/smci-raised-guidance"
SMCI_ACCOUNTING_URL = "https://news.example.com/smci-accounting-issue"


@dataclass
class TimeoutRecordingThemeProvider:
    timeout_seconds: float = 180.0
    observed_timeouts: list[float] = field(default_factory=list)

    def route(self, inputs):
        self.observed_timeouts.append(float(self.timeout_seconds))
        return ThemeRouteOutput(status="no_transition")


class FreeWebResearchRunnerTests(unittest.TestCase):
    def test_agentic_workflow_metrics_records_fallback_full_map_and_empty_mapper_output(self):
        metrics = {
            "mapping_prefilter_original_task_count": 0,
            "mapping_prefilter_filtered_task_count": 0,
            "mapping_prefilter_skipped_input_count": 0,
            "mapping_prefilter_fallback_full_map_count": 0,
            "mapping_empty_output_count": 0,
            "mapping_empty_output_retry_count": 0,
            "mapping_empty_output_recovered_count": 0,
            "mapping_empty_output_summaries": [],
            "mapping_empty_output_retry_summaries": [],
            "mapping_prefilter_fallback_full_map_summaries": [],
        }

        _record_agentic_workflow_metrics(
            "agentic_evidence_mapping_prefilter_complete",
            {
                "document_id": "DOC-A",
                "mapping_prefilter_original_task_count": 18,
                "mapping_prefilter_filtered_task_count": 7,
                "mapping_prefilter_skipped_input_count": 1,
                "mapping_prefilter_fallback_full_map_count": 2,
                "mapping_prefilter_reason_by_claim": (
                    {
                        "claim_id": "CLM-A",
                        "raw_assertion_id": "RA-A",
                        "fallback_full_map": True,
                        "reason": "fallback_full_map_unstructured_source",
                        "original_candidate_count": 9,
                    },
                    {
                        "claim_id": "CLM-B",
                        "raw_assertion_id": "RA-B",
                        "fallback_full_map": False,
                        "reason": "unstructured_claim_semantic_topic_matches_primitive_family",
                        "original_candidate_count": 9,
                    },
                ),
            },
            metrics=metrics,
        )
        _record_agentic_workflow_metrics(
            "agentic_evidence_mapping_chunk_empty_retry_start",
            {
                "document_id": "DOC-A",
                "round_index": 1,
                "retry_index": 1,
                "chunk_index": 2,
                "mapping_input_count": 3,
            },
            metrics=metrics,
        )
        _record_agentic_workflow_metrics(
            "agentic_evidence_mapping_chunk_empty_retry_recovered",
            {
                "document_id": "DOC-A",
                "round_index": 1,
                "retry_index": 1,
                "chunk_index": 2,
                "mapping_input_count": 3,
                "mapping_output_count": 2,
            },
            metrics=metrics,
        )
        _record_agentic_workflow_metrics(
            "agentic_evidence_mapping_chunk_complete",
            {
                "document_id": "DOC-A",
                "round_index": 1,
                "chunk_index": 2,
                "mapping_input_count": 3,
                "mapping_output_count": 0,
            },
            metrics=metrics,
        )

        self.assertEqual(metrics["mapping_prefilter_original_task_count"], 18)
        self.assertEqual(metrics["mapping_prefilter_filtered_task_count"], 7)
        self.assertEqual(metrics["mapping_prefilter_skipped_input_count"], 1)
        self.assertEqual(metrics["mapping_prefilter_fallback_full_map_count"], 2)
        self.assertEqual(metrics["mapping_empty_output_count"], 1)
        self.assertEqual(metrics["mapping_empty_output_retry_count"], 1)
        self.assertEqual(metrics["mapping_empty_output_recovered_count"], 1)
        self.assertIn("fallback_full_map", metrics["mapping_prefilter_fallback_full_map_summaries"][0])
        self.assertIn("empty_mapper_retry", metrics["mapping_empty_output_retry_summaries"][0])
        self.assertIn("document=DOC-A", metrics["mapping_empty_output_summaries"][0])

    def test_score_gap_reason_code_marks_score_as_raw_reference(self):
        score = ScoreSnapshot(
            symbol="123456",
            as_of_date=date(2026, 6, 12),
            eps_fcf_explosion_score=20.0,
            earnings_visibility_score=15.0,
            bottleneck_pricing_score=15.0,
            market_mispricing_score=10.0,
            valuation_rerating_score=10.0,
            capital_allocation_score=4.0,
            information_confidence_score=4.0,
            risk_penalty=0.0,
            total_score=78.0,
        )

        codes = _score_gap_reason_codes(score, ("missing_revision_source",))

        self.assertIn("RAW_SCORE_TOTAL_BEFORE_GAP:78.0", codes)
        self.assertFalse(any(item.startswith("SCORE_TOTAL:") for item in codes))

    def test_score_gap_missing_information_coerces_numeric_diagnostic_strings(self):
        score = ScoreSnapshot(
            symbol="123456",
            as_of_date=date(2026, 6, 12),
            eps_fcf_explosion_score=20.0,
            earnings_visibility_score=20.0,
            bottleneck_pricing_score=20.0,
            market_mispricing_score=15.0,
            valuation_rerating_score=15.0,
            capital_allocation_score=5.0,
            information_confidence_score=5.0,
            risk_penalty=0.0,
            total_score=100.0,
            diagnostic_scores={"revision_score": 90.0, "contract_required_for_green": 0.0},
        )
        diagnostics = dict(score.diagnostic_scores)
        diagnostics["revision_score"] = "44"
        diagnostics["contract_required_for_green"] = "1"
        diagnostics["contract_quality"] = "unknown"
        object.__setattr__(score, "diagnostic_scores", diagnostics)

        gaps = _score_gap_missing_information(score)

        self.assertIn("revision estimate consensus target price EPS OP FCF", gaps)
        self.assertIn("contract backlog RPO prepayment order allocation", gaps)

    def test_combined_score_gap_context_drops_fcf_gap_when_agentic_cash_bridge_is_present(self):
        score = ScoreSnapshot(
            symbol="123456",
            as_of_date=date(2026, 6, 12),
            eps_fcf_explosion_score=20.0,
            earnings_visibility_score=20.0,
            bottleneck_pricing_score=20.0,
            market_mispricing_score=15.0,
            valuation_rerating_score=15.0,
            capital_allocation_score=5.0,
            information_confidence_score=5.0,
            risk_penalty=0.0,
            total_score=100.0,
            diagnostic_scores={"estimate_missing_fcf_source": 100.0},
        )
        trace = AgenticEvidenceRuntimeTrace(
            status="completed",
            primitive_states=(
                PrimitiveStateV2("cash_or_revision_conversion", PrimitiveStatus.PRESENT_CURRENT),
                PrimitiveStateV2("memory_price_increase_mentioned", PrimitiveStatus.UNKNOWN),
            ),
        )

        gaps = _combined_score_gap_context(score, RedTeamAssessment.empty("123456", date(2026, 6, 12)), trace)

        self.assertFalse(any("selected_fcf_source_missing" in item for item in gaps))
        self.assertTrue(any("agentic primitive gap:memory_price_increase_mentioned" in item for item in gaps))

    def test_combined_score_gap_context_keeps_fcf_gap_when_agentic_cash_bridge_is_unknown(self):
        score = ScoreSnapshot(
            symbol="123456",
            as_of_date=date(2026, 6, 12),
            eps_fcf_explosion_score=20.0,
            earnings_visibility_score=20.0,
            bottleneck_pricing_score=20.0,
            market_mispricing_score=15.0,
            valuation_rerating_score=15.0,
            capital_allocation_score=5.0,
            information_confidence_score=5.0,
            risk_penalty=0.0,
            total_score=100.0,
            diagnostic_scores={"estimate_missing_fcf_source": 100.0},
        )
        trace = AgenticEvidenceRuntimeTrace(
            status="completed",
            primitive_states=(PrimitiveStateV2("cash_or_revision_conversion", PrimitiveStatus.UNKNOWN),),
        )

        gaps = _combined_score_gap_context(score, RedTeamAssessment.empty("123456", date(2026, 6, 12)), trace)

        self.assertTrue(any("selected_fcf_source_missing" in item for item in gaps))

    def test_combined_score_gap_context_includes_agentic_rejection_reasons(self):
        score = ScoreSnapshot(
            symbol="123456",
            as_of_date=date(2026, 6, 12),
            eps_fcf_explosion_score=20.0,
            earnings_visibility_score=20.0,
            bottleneck_pricing_score=20.0,
            market_mispricing_score=15.0,
            valuation_rerating_score=15.0,
            capital_allocation_score=5.0,
            information_confidence_score=5.0,
            risk_penalty=0.0,
            total_score=100.0,
        )
        trace = AgenticEvidenceRuntimeTrace(
            status="completed",
            primitive_states=(PrimitiveStateV2("hbm_capacity_pre_sold", PrimitiveStatus.UNKNOWN),),
            eligibility_rejection_summaries=(
                "MAP-1|claim=CLM-1|primitive=hbm_capacity_pre_sold|mapping_status=ACCEPTED|"
                "eligibility_reasons=temporal_not_allowed:HISTORICAL",
            ),
            rejected_mapping_summaries=(
                "MAP-2|claim=CLM-2|primitive=memory_price_increase_mentioned|status=REJECTED|"
                "reason=price increase not directly stated",
            ),
        )

        gaps = _combined_score_gap_context(score, RedTeamAssessment.empty("123456", date(2026, 6, 12)), trace)

        self.assertTrue(any(item.startswith("agentic primitive gap:hbm_capacity_pre_sold") for item in gaps))
        self.assertTrue(any("agentic eligibility rejection:" in item for item in gaps))
        self.assertTrue(any("temporal_not_allowed:HISTORICAL" in item for item in gaps))
        self.assertTrue(any("agentic mapping rejection:" in item for item in gaps))

    def test_free_web_research_defaults_evidence_review_on_for_gap_expansion(self):
        inputs = FreeWebResearchInput(
            company_name="테스트",
            symbol="123456",
            sector=None,
            market=Market.KR,
            as_of_date=date(2024, 1, 1),
            theme_route_provider=FakeThemeRouteProvider(),
        )

        self.assertTrue(inputs.theme_rebalance_enabled)
        self.assertTrue(inputs.theme_evidence_review_enabled)
        self.assertEqual(inputs.max_theme_expansion_rounds, 2)
        self.assertEqual(inputs.top_results, 60)
        self.assertEqual(inputs.post_parse_gap_expansion_max_queries, 10)
        self.assertEqual(inputs.llm_query_retry_max, 2)
        self.assertEqual(inputs.score_gap_query_retry_max, 2)
        self.assertEqual(inputs.max_score_gap_expansion_rounds, 2)
        self.assertTrue(inputs.agentic_mapper_self_consistency_use_batch)
        self.assertEqual(inputs.agentic_mapper_batch_max_tasks, 12)
        self.assertEqual(inputs.theme_route_search_result_limit, 80)
        self.assertEqual(inputs.theme_route_document_limit, 32)
        self.assertEqual(inputs.theme_route_document_excerpt_chars, 1200)
        self.assertEqual(inputs.theme_evidence_review_timeout_seconds, 60.0)
        self.assertEqual(inputs.post_gap_fetch_results_per_query, 5)
        self.assertEqual(inputs.post_gap_fetch_min_results, 20)
        self.assertIsNone(inputs.agentic_provider_timeout_seconds)
        self.assertTrue(inputs.require_valid_theme_route_for_scoring)
        self.assertTrue(inputs.require_resolved_score_gaps_for_scoring)

    def test_free_web_research_rejects_unbounded_retry_settings(self):
        with self.assertRaisesRegex(ValueError, "llm_query_retry_max must be bounded"):
            FreeWebResearchInput(
                company_name="테스트",
                symbol="123456",
                sector=None,
                market=Market.KR,
                as_of_date=date(2024, 1, 1),
                llm_query_retry_max=None,
            )
        with self.assertRaisesRegex(ValueError, "score_gap_query_retry_max must be bounded"):
            FreeWebResearchInput(
                company_name="테스트",
                symbol="123456",
                sector=None,
                market=Market.KR,
                as_of_date=date(2024, 1, 1),
                score_gap_query_retry_max=None,
            )
        with self.assertRaisesRegex(ValueError, "top_results must be bounded"):
            FreeWebResearchInput(
                company_name="테스트",
                symbol="123456",
                sector=None,
                market=Market.KR,
                as_of_date=date(2024, 1, 1),
                top_results=None,
            )
        with self.assertRaisesRegex(ValueError, "theme_evidence_review_timeout_seconds must be positive"):
            FreeWebResearchInput(
                company_name="테스트",
                symbol="123456",
                sector=None,
                market=Market.KR,
                as_of_date=date(2024, 1, 1),
                theme_evidence_review_timeout_seconds=0,
            )
        with self.assertRaisesRegex(ValueError, "agentic_mapper_batch_max_tasks must be positive"):
            FreeWebResearchInput(
                company_name="테스트",
                symbol="123456",
                sector=None,
                market=Market.KR,
                as_of_date=date(2024, 1, 1),
                agentic_mapper_batch_max_tasks=0,
            )
        with self.assertRaisesRegex(ValueError, "agentic_evidence_document_limit must be positive"):
            FreeWebResearchInput(
                company_name="테스트",
                symbol="123456",
                sector=None,
                market=Market.KR,
                as_of_date=date(2024, 1, 1),
                agentic_evidence_document_limit=0,
            )
        with self.assertRaisesRegex(ValueError, "agentic_provider_timeout_seconds must be positive"):
            FreeWebResearchInput(
                company_name="테스트",
                symbol="123456",
                sector=None,
                market=Market.KR,
                as_of_date=date(2024, 1, 1),
                agentic_provider_timeout_seconds=0,
            )

    def test_theme_evidence_review_timeout_uses_shorter_codex_provider_copy(self):
        provider = CodexCLIThemeRouteProvider(timeout_seconds=180.0)

        bounded = _theme_route_provider_for_timeout(provider, timeout_seconds=45.0)
        already_short = _theme_route_provider_for_timeout(provider, timeout_seconds=240.0)
        fake = FakeThemeRouteProvider()

        self.assertIsNot(bounded, provider)
        self.assertEqual(bounded.timeout_seconds, 45.0)
        self.assertIs(already_short, provider)
        self.assertIs(_theme_route_provider_for_timeout(fake, timeout_seconds=45.0), fake)

    def test_agentic_provider_timeout_uses_shorter_codex_provider_copy(self):
        provider = CodexCLIAgenticEvidenceProvider(timeout_seconds=180.0)

        inputs = FreeWebResearchInput(
            company_name="타임아웃테스트",
            symbol="123456",
            sector=None,
            market=Market.KR,
            as_of_date=date(2026, 6, 26),
            agentic_evidence_enabled=True,
            agentic_claim_extractor_provider=provider,
            agentic_claim_adjudicator_provider=provider,
            agentic_primitive_mapper_provider=provider,
            agentic_follow_up_planner_provider=provider,
            agentic_provider_timeout_seconds=7.0,
        )

        self.assertIsNot(inputs.agentic_claim_extractor_provider, provider)
        self.assertEqual(inputs.agentic_claim_extractor_provider.timeout_seconds, 7.0)
        self.assertEqual(inputs.agentic_claim_adjudicator_provider.timeout_seconds, 7.0)
        self.assertEqual(inputs.agentic_primitive_mapper_provider.timeout_seconds, 7.0)
        self.assertEqual(inputs.agentic_follow_up_planner_provider.timeout_seconds, 7.0)

    def test_initial_theme_rebalance_route_uses_configured_timeout(self):
        provider = TimeoutRecordingThemeProvider(timeout_seconds=180.0)

        FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=EmptySearchProvider(),
            query_planner=_FixedQueryPlanner(
                QueryPlan(
                    company_name="타임아웃테스트",
                    symbol="123456",
                    sector=None,
                    market=Market.KR,
                    as_of_date=date(2026, 6, 26),
                    queries=(),
                )
            ),
        ).run(
            FreeWebResearchInput(
                company_name="타임아웃테스트",
                symbol="123456",
                sector=None,
                market=Market.KR,
                as_of_date=date(2026, 6, 26),
                theme_rebalance_enabled=True,
                theme_route_provider=provider,
                theme_evidence_review_timeout_seconds=12.0,
                max_theme_expansion_rounds=1,
                require_valid_theme_route_for_scoring=False,
                require_resolved_score_gaps_for_scoring=False,
            )
        )

        self.assertTrue(provider.observed_timeouts)
        self.assertEqual(set(provider.observed_timeouts), {12.0})

    def test_llm_route_input_is_compacted_with_query_coverage(self):
        as_of = date(2026, 6, 8)
        queries = tuple(
            QuerySpec(
                group="test",
                query=f"테스트압축 쿼리{i}",
                priority=i,
                company_name="테스트압축",
                symbol="123450",
                sector=None,
                market=Market.KR,
                as_of_date=as_of,
            )
            for i in range(3)
        )
        plan = QueryPlan(
            company_name="테스트압축",
            symbol="123450",
            sector=None,
            market=Market.KR,
            as_of_date=as_of,
            queries=queries,
        )
        results_by_query = {
            query.query: tuple(
                SearchResult(
                    title=f"테스트압축 {query.query} 리포트 {index}",
                    url=f"https://example.com/{query.priority}/{index}",
                    snippet="테스트압축 목표주가 상향 EPS 상향 HBM 수요",
                    source="fixture-research",
                    published_at=datetime(2026, 6, 8, 8),
                    query=query.query,
                    is_report_domain=True,
                    confidence=0.9,
                )
                for index in range(8)
            )
            for query in queries
        }
        route_provider = FakeThemeRouteProvider(output=ThemeRouteOutput(status="no_transition"))

        FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=FixtureSearchProvider(results_by_query=results_by_query),
            query_planner=_FixedQueryPlanner(plan),
        ).run(
            FreeWebResearchInput(
                company_name="테스트압축",
                symbol="123450",
                sector=None,
                market=Market.KR,
                as_of_date=as_of,
                top_results=3,
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                theme_evidence_review_enabled=False,
                theme_route_search_result_limit=5,
                require_valid_theme_route_for_scoring=False,
                require_resolved_score_gaps_for_scoring=False,
            )
        )

        self.assertEqual(len(route_provider.calls), 1)
        llm_results = route_provider.calls[0].search_results
        self.assertEqual(len(llm_results), 5)
        self.assertEqual({item.query for item in llm_results}, {query.query for query in queries})

    def test_score_gap_expansion_blocks_when_search_makes_no_progress(self):
        as_of = date(2026, 6, 8)
        query = QuerySpec(
            group="test",
            query="테스트라운드 최초",
            priority=1,
            company_name="테스트라운드",
            symbol="123451",
            sector=None,
            market=Market.KR,
            as_of_date=as_of,
        )
        plan = QueryPlan(
            company_name="테스트라운드",
            symbol="123451",
            sector=None,
            market=Market.KR,
            as_of_date=as_of,
            queries=(query,),
        )
        gap_query = "테스트라운드 EPS FCF 컨센서스 상향 리포트"
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(status="needs_more_evidence", suggested_queries=(gap_query,)),
            ]
        )
        phase_events: list[dict] = []

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=FixtureSearchProvider(results_by_query={gap_query: ()}),
            query_planner=_FixedQueryPlanner(plan),
        ).run(
            FreeWebResearchInput(
                company_name="테스트라운드",
                symbol="123451",
                sector=None,
                market=Market.KR,
                as_of_date=as_of,
                top_results=3,
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
                max_score_gap_expansion_rounds=1,
                require_valid_theme_route_for_scoring=True,
                require_resolved_score_gaps_for_scoring=True,
                phase_event_sink=phase_events.append,
            )
        )

        self.assertEqual(result.stage.stage, Stage.STAGE_0)
        self.assertFalse(result.theme_route_diagnostics["score_valid"])
        self.assertEqual(result.theme_route_diagnostics["score_blocked_reason"], "score_gap_no_progress")
        self.assertNotIn("post_score_gap_warning_reason", result.theme_route_diagnostics)
        self.assertEqual(result.score.diagnostic_scores["score_valid"], 0.0)
        self.assertEqual(result.score.diagnostic_scores["score_blocked_by_score_gap"], 100.0)
        self.assertEqual(result.theme_route_diagnostics["post_score_gap_expansion_status"], "no_progress")
        self.assertEqual(result.theme_route_diagnostics["post_score_gap_expansion_count"], 1)
        self.assertTrue(any(event["phase"] == "post_score_gap_stop_no_progress" for event in phase_events))

    def test_provider_error_theme_route_blocks_score_and_stage(self):
        route_provider = FakeThemeRouteProvider(
            output=ThemeRouteOutput(
                status="provider_error",
                blocked_reason="codex cli returned no valid route json",
            )
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=EmptySearchProvider(),
        ).run(
            FreeWebResearchInput(
                company_name="테스트",
                symbol="123456",
                sector=None,
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                theme_evidence_review_enabled=False,
            )
        )

        self.assertEqual(result.stage.stage, Stage.STAGE_0)
        self.assertEqual(result.score.total_score, 0.0)
        self.assertFalse(result.theme_route_diagnostics["score_valid"])
        self.assertEqual(result.theme_route_diagnostics["score_blocked_reason"], "theme_route_provider_error")
        self.assertEqual(result.score.diagnostic_scores["score_valid"], 0.0)
        self.assertEqual(result.score.diagnostic_scores["score_blocked_by_theme_route"], 100.0)
        self.assertIn("raw_score_total_before_theme_route_block", result.score.diagnostic_scores)

    def test_uncapped_llm_retry_stops_on_repeated_non_executable_queries(self):
        route_provider = FakeThemeRouteProvider(
            output=ThemeRouteOutput(
                status="needs_more_evidence",
                suggested_queries=("테스트 after:2027-01-01 미래 발간 리포트",),
            )
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=EmptySearchProvider(),
        ).run(
            FreeWebResearchInput(
                company_name="테스트",
                symbol="123456",
                sector=None,
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                theme_evidence_review_enabled=False,
            )
        )

        self.assertGreaterEqual(len(route_provider.calls), 2)
        self.assertTrue(any(item.reason == "future_query_rejected" for item in result.skipped_queries))
        self.assertEqual(result.expansion_queries_run, ())

    def test_llm_retry_can_be_capped_explicitly_for_fixtures(self):
        route_provider = FakeThemeRouteProvider(
            output=ThemeRouteOutput(
                status="needs_more_evidence",
                suggested_queries=("테스트 after:2027-01-01 미래 발간 리포트",),
            )
        )

        FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=EmptySearchProvider(),
        ).run(
            FreeWebResearchInput(
                company_name="테스트",
                symbol="123456",
                sector=None,
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                theme_evidence_review_enabled=False,
                llm_query_retry_max=0,
            )
        )

        self.assertEqual(len(route_provider.calls), 1)

    def test_browser_search_provider_parses_fixture_html(self):
        provider = BrowserSearchProvider(
            fixture_html_by_query={
                "HD현대일렉트릭 수주잔고 OPM 수출 비중 PDF": HTML_ROOT / "hd_hyundai_electric_report_search.html"
            }
        )

        results = provider.search("HD현대일렉트릭 수주잔고 OPM 수출 비중 PDF", date(2023, 7, 27), max_results=3)

        self.assertEqual(results[0].title, "HD현대일렉트릭 줄을 서시오")
        self.assertTrue(results[0].is_pdf)
        self.assertTrue(results[0].is_report_domain)
        self.assertEqual(provider.classify_result_type(results[0].url, results[0].title, results[0].snippet), "report")

    def test_hd_fixture_html_reaches_stage_3_green(self):
        result = _run_free(
            company_name="HD현대일렉트릭",
            symbol="267260",
            sector="power_equipment",
            market=Market.KR,
            as_of_date=date(2023, 7, 27),
            fixture_html={
                "HD현대일렉트릭 수주잔고 OPM 수출 비중 PDF": HTML_ROOT / "hd_hyundai_electric_report_search.html",
            },
            fixture_text={
                HD_REPORT_URL: TEXT_ROOT / "hd_hyundai_electric_report.txt",
            },
        )

        self.assertEqual(result.stage.stage, Stage.STAGE_3_GREEN)
        self.assertEqual(result.feature_result.shortage_type.value, "structural")
        self.assertTrue(any(item.source_type == "research_report" for item in result.web_result.evidence))
        self.assertIn("HD현대일렉트릭 수주잔고 OPM 수출 비중 PDF", result.web_result.queries_run)

    def test_hyosung_fixture_html_reaches_stage_3_green(self):
        result = _run_free(
            company_name="효성중공업",
            symbol="298040",
            sector="power_equipment",
            market=Market.KR,
            as_of_date=date(2023, 11, 15),
            fixture_html={
                "효성중공업 컨센서스 상회 Review PDF": HTML_ROOT / "hyosung_heavy_report_search.html",
            },
            fixture_text={
                HYOSUNG_REPORT_URL: TEXT_ROOT / "hyosung_heavy_report.txt",
            },
        )

        self.assertEqual(result.stage.stage, Stage.STAGE_3_GREEN)
        self.assertGreaterEqual(result.score.diagnostic_scores["revision_score"], 50)

    def test_iljin_fixture_html_extracts_contract_and_becomes_candidate(self):
        result = _run_free(
            company_name="일진전기",
            symbol="103590",
            sector="power_equipment",
            market=Market.KR,
            as_of_date=date(2023, 11, 27),
            fixture_html={
                "일진전기 단일판매 공급계약": HTML_ROOT / "iljin_contract_search.html",
            },
            fixture_text={
                ILJIN_DISCLOSURE_URL: TEXT_ROOT / "iljin_contract.txt",
                ILJIN_REPORT_URL: TEXT_ROOT / "iljin_transformer_report.txt",
            },
        )

        disclosure_fields = result.web_result.parsed_disclosures[0].parsed_fields
        self.assertEqual(disclosure_fields["contract_duration_months"], 60)
        self.assertAlmostEqual(disclosure_fields["contract_amount_to_prior_sales"], 0.55)
        self.assertIn(result.stage.stage, {Stage.STAGE_2, Stage.STAGE_3_GREEN, Stage.STAGE_3_YELLOW})

    def test_zoom_fixture_html_marks_one_off_and_stage_3_red(self):
        result = _run_free(
            company_name="Zoom",
            symbol="ZM",
            sector="software",
            market=Market.US,
            as_of_date=date(2020, 9, 1),
            fixture_html={
                "Zoom 영업이익 컨센서스 상회": HTML_ROOT / "zoom_one_off_search.html",
            },
            fixture_text={
                ZOOM_NEWS_URL: TEXT_ROOT / "zoom_one_off_news.txt",
                ZOOM_REPORT_URL: TEXT_ROOT / "zoom_q2_2020_report.txt",
                ZOOM_SEC_URL: TEXT_ROOT / "zoom_sec_disclosure.txt",
            },
        )

        self.assertEqual(result.feature_result.shortage_type.value, "one_off")
        self.assertGreaterEqual(result.score.diagnostic_scores["one_off_shortage_risk"], 80)
        self.assertEqual(result.stage.stage, Stage.STAGE_3_RED)

    def test_smci_fixture_html_stays_4b_without_v2_hard_break_claim(self):
        fixture_html = {
            "SMCI 영업이익 컨센서스 상회": HTML_ROOT / "smci_4b_4c_search.html",
            "SMCI 회계 이슈": HTML_ROOT / "smci_4b_4c_search.html",
        }
        fixture_text = {
            SMCI_GUIDANCE_URL: TEXT_ROOT / "smci_guidance_raise.txt",
            SMCI_ACCOUNTING_URL: TEXT_ROOT / "smci_accounting_issue.txt",
        }

        stage4b = _run_free(
            company_name="SMCI",
            symbol="SMCI",
            sector="ai_server",
            market=Market.US,
            as_of_date=date(2024, 1, 18),
            stage_context="4B",
            previous_stage=Stage.STAGE_3_GREEN,
            fixture_html=fixture_html,
            fixture_text=fixture_text,
        )
        stage4c = _run_free(
            company_name="SMCI",
            symbol="SMCI",
            sector="ai_server",
            market=Market.US,
            as_of_date=date(2024, 8, 28),
            stage_context="4C",
            previous_stage=Stage.STAGE_4B,
            fixture_html=fixture_html,
            fixture_text=fixture_text,
        )

        self.assertEqual(stage4b.stage.stage, Stage.STAGE_4B)
        self.assertEqual(stage4c.stage.stage, Stage.STAGE_4B)
        self.assertFalse(stage4c.red_team.has_hard_break)

    def test_search_budget_skips_queries_after_symbol_limit(self):
        result = _run_free(
            company_name="HD현대일렉트릭",
            symbol="267260",
            sector="power_equipment",
            market=Market.KR,
            as_of_date=date(2023, 7, 27),
            fixture_html={
                "HD현대일렉트릭 수주잔고 OPM 수출 비중 PDF": HTML_ROOT / "hd_hyundai_electric_report_search.html",
            },
            fixture_text={HD_REPORT_URL: TEXT_ROOT / "hd_hyundai_electric_report.txt"},
            budget=SearchBudget(max_total_queries_per_day=1, max_queries_per_symbol=1),
        )

        self.assertEqual(result.budget_tracker.total_queries_used, 1)
        self.assertTrue(result.skipped_queries)
        self.assertTrue(all(item.reason == "daily_query_budget_exhausted" or item.reason == "symbol_query_budget_exhausted" for item in result.skipped_queries))

    def test_naver_free_provider_builds_requests_without_credentials(self):
        provider = NaverFreeSearchProvider(client_id="", client_secret="", fixture_mode=False, live_enabled=True)

        results = provider.search("HD현대일렉트릭 목표주가 상향 EPS 상향 PDF", date(2023, 7, 27), max_results=3)

        self.assertEqual(results, ())
        self.assertIn("missing_naver_credentials", provider.errors)
        self.assertEqual({request.params["display"] for request in provider.built_requests}, {3})

    def test_naver_free_provider_default_display_uses_api_maximum(self):
        provider = NaverFreeSearchProvider(client_id="", client_secret="", fixture_mode=False, live_enabled=True)

        provider.search("테스트전자 컨센서스 리포트", date(2026, 6, 8))

        self.assertEqual({request.params["display"] for request in provider.built_requests}, {100})

    def test_naver_response_normalizer_filters_future_results(self):
        payload = {
            "items": [
                {
                    "title": "<b>HD현대일렉트릭</b> 목표주가 상향",
                    "originallink": "https://news.example.com/hd",
                    "description": "컨센서스 상회",
                    "pubDate": "Thu, 27 Jul 2023 08:00:00 +0900",
                },
                {
                    "title": "미래 리포트",
                    "link": "https://news.example.com/future",
                    "description": "future",
                    "pubDate": "Thu, 28 Jul 2023 08:00:00 +0900",
                },
            ]
        }

        results = NaverFreeSearchProvider.normalize_response(
            payload,
            query="HD현대일렉트릭 목표주가 상향 EPS 상향 PDF",
            as_of_date=date(2023, 7, 27),
            source="Naver News",
        )

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "HD현대일렉트릭 목표주가 상향")
        self.assertTrue(results[0].is_news)

    def test_manual_source_provider_is_optional_fallback(self):
        manual = ManualSourceProvider(
            sources=(
                ManualSource(
                    title="ManualCorp 수주잔고 Review PDF",
                    url="manual://manualcorp-report",
                    source="Manual Fixture",
                    published_at="2023-07-27T08:00:00",
                    queries=("ManualCorp 수주잔고 OPM 수출 비중 PDF",),
                    text=(TEXT_ROOT / "hd_hyundai_electric_report.txt").read_text(encoding="utf-8"),
                    is_report_domain=True,
                    is_pdf=True,
                ),
            )
        )

        result = FreeWebResearchRunner(
            browser_provider=BrowserSearchProvider(),
            free_search_provider=EmptySearchProvider(),
            manual_source_provider=manual,
        ).run(
            FreeWebResearchInput(
                company_name="ManualCorp",
                symbol="MANUAL",
                sector="power_equipment",
                market=Market.KR,
                as_of_date=date(2023, 7, 27),
            )
        )

        self.assertTrue(result.web_result.parsed_reports)
        self.assertTrue(any(item.url == "manual://manualcorp-report" for item in result.web_result.search_results))

    def test_report_title_snippet_forward_estimate_flows_to_consensus_proxy(self):
        url = "https://finance.example.com/research/company_read.naver?nid=77"
        as_of = date(2026, 6, 8)
        plan = QueryPlan(
            company_name="테스트전자",
            symbol="123456",
            sector="semiconductor",
            market=Market.KR,
            as_of_date=as_of,
            queries=(
                QuerySpec(
                    group="fixture",
                    query="테스트전자 2Q Review 영업이익 컨센서스 PDF",
                    priority=1,
                    company_name="테스트전자",
                    symbol="123456",
                    sector="semiconductor",
                    market=Market.KR,
                    as_of_date=as_of,
                ),
            ),
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "테스트전자 2Q Review 영업이익 컨센서스 PDF": (
                    SearchResult(
                        title="테스트전자 종목분석 - 2Q26 영업이익 70조원 예상",
                        url=url,
                        snippet="목표주가 87만원으로 상향. HBM 수요 증가와 실적 전망치 상향",
                        source="fixture-research",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트전자 2Q Review 영업이익 컨센서스 PDF",
                        rank=1,
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                )
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
            query_planner=_FixedQueryPlanner(plan),
        ).run(
            FreeWebResearchInput(
                company_name="테스트전자",
                symbol="123456",
                sector="semiconductor",
                market=Market.KR,
                as_of_date=as_of,
                top_results=5,
                fixture_text_by_url={url: "테스트전자는 HBM 수요 증가를 근거로 리포트가 발간됐다."},
            )
        )

        self.assertEqual(len(result.web_result.parsed_reports), 1)
        report = result.web_result.parsed_reports[0]
        self.assertEqual(report.fy1_op, 70_000_000_000_000.0)
        self.assertEqual(report.target_price, 870000)
        self.assertEqual(len(result.feature_input.consensus), 1)
        self.assertEqual(result.feature_input.consensus[0].op_e, 70_000_000_000_000.0)
        self.assertEqual(result.feature_input.consensus[0].target_price, 870000)
        self.assertFalse(result.feature_input.consensus_revisions)
        self.assertTrue(any(item.source_type == "consensus" for item in result.web_result.evidence))
        self.assertIn(
            stable_consensus_evidence_id(
                symbol="123456",
                estimate_date=date(2026, 6, 8),
                fiscal_year=2026,
                source="report_proxy",
            ),
            {item.evidence_id for item in result.web_result.evidence},
        )
        self.assertEqual(result.score.diagnostic_scores["evidence_family_consensus"], 0.0)
        self.assertEqual(result.score.diagnostic_scores["evidence_family_consensus_proxy"], 1.0)
        self.assertNotIn("financial_actuals_from_text", report.parsed_fields)

    def test_power_equipment_report_forward_estimate_flows_to_consensus_proxy(self):
        url = "https://finance.example.com/research/power_equipment_report?nid=88"
        provider = FixtureSearchProvider(
            results_by_query={
                "테스트전력 2Q Review 영업이익 컨센서스 PDF": (
                    SearchResult(
                        title="테스트전력 종목분석 - 2027년 영업이익 2,400억원 전망",
                        url=url,
                        snippet="목표주가 12만원으로 상향. 북미 전력망 투자와 변압기 수주잔고 반영",
                        source="fixture-research",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트전력 2Q Review 영업이익 컨센서스 PDF",
                        rank=1,
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                )
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트전력",
                symbol="654321",
                sector="power_equipment",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={url: "테스트전력은 리드타임 장기화와 수주잔고 증가를 근거로 리포트가 발간됐다."},
            )
        )

        self.assertEqual(len(result.web_result.parsed_reports), 1)
        report = result.web_result.parsed_reports[0]
        self.assertEqual(report.fy1_op, 240_000_000_000.0)
        self.assertEqual(report.target_price, 120000)
        self.assertEqual(len(result.feature_input.consensus), 1)
        self.assertEqual(result.feature_input.consensus[0].fiscal_year, 2027)
        self.assertEqual(result.feature_input.consensus[0].op_e, 240_000_000_000.0)
        self.assertEqual(result.feature_input.consensus[0].target_price, 120000)
        self.assertFalse(result.feature_input.consensus_revisions)
        self.assertTrue(any(item.source_type == "consensus" for item in result.web_result.evidence))
        self.assertIn(
            stable_consensus_evidence_id(
                symbol="654321",
                estimate_date=date(2026, 6, 8),
                fiscal_year=2027,
                source="report_proxy",
            ),
            {item.evidence_id for item in result.web_result.evidence},
        )
        self.assertEqual(result.score.diagnostic_scores["evidence_family_consensus"], 0.0)
        self.assertEqual(result.score.diagnostic_scores["evidence_family_consensus_proxy"], 1.0)
        self.assertNotIn("hbm_context_mentioned", report.parsed_fields)
        self.assertNotIn("financial_actuals_from_text", report.parsed_fields)

    def test_fetch_unavailable_search_hit_becomes_snippet_only_evidence(self):
        provider = FixtureSearchProvider(
            results_by_query={
                "NAVER 데이터센터 수주": (
                    SearchResult(
                        title="NAVER, 엔비디아와 AI 데이터센터 협력",
                        url="https://news.example.com/naver-ai-dc",
                        snippet="GPU 클라우드 매출 확대 기대",
                        source="fixture-news",
                        query="NAVER 데이터센터 수주",
                        confidence=0.8,
                    ),
                )
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="NAVER",
                symbol="035420",
                sector="platform",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=3,
            )
        )

        self.assertEqual(len(result.web_result.parsed_news), 1)
        news = result.web_result.parsed_news[0]
        self.assertTrue(news.parsed_fields["search_snippet_only"])
        self.assertTrue(news.parsed_fields["search_snippet_date_unverified"])
        self.assertFalse(news.parsed_fields["green_allowed_by_date"])
        self.assertTrue(result.web_result.evidence)
        self.assertEqual(result.score.diagnostic_scores["snippet_only_green_block"], 100.0)
        self.assertEqual(result.score.diagnostic_scores["evidence_family_news"], 0.0)
        self.assertNotEqual(result.stage.stage, Stage.STAGE_3_GREEN)

    def test_live_page_fetch_promotes_search_hit_to_full_news_evidence(self):
        provider = FixtureSearchProvider(
            results_by_query={
                "NAVER 데이터센터 수주": (
                    SearchResult(
                        title="NAVER AI 데이터센터 협력",
                        url="https://example.com/naver-ai",
                        snippet="GPU 클라우드 매출 확대",
                        source="example",
                        query="NAVER 데이터센터 수주",
                        confidence=0.8,
                    ),
                )
            }
        )
        html = """
        <html><body>
        NAVER 데이터센터 엔비디아 GPU 인프라 투자와 클라우드 매출 성장률 40%가 확인됐다.
        </body></html>
        """

        with tempfile.TemporaryDirectory() as tmpdir:
            with patch("e2r.research.page_fetcher.request.urlopen", return_value=_FakeHTTPResponse(html)):
                result = FreeWebResearchRunner(
                    browser_provider=EmptySearchProvider(),
                    free_search_provider=provider,
                ).run(
                    FreeWebResearchInput(
                        company_name="NAVER",
                        symbol="035420",
                        sector="platform",
                        market=Market.KR,
                        as_of_date=date(2026, 6, 8),
                        top_results=3,
                        live_page_fetch_enabled=True,
                        page_fetch_cache_directory=tmpdir,
                    )
                )

        self.assertEqual(len(result.web_result.parsed_news), 1)
        fields = result.web_result.parsed_news[0].parsed_fields
        self.assertFalse(fields["search_snippet_only"])
        self.assertTrue(fields["document_type_inferred_from_fetched_text"])
        self.assertEqual(fields["claim_ledger_version"], "e2r-claim-ledger-v1")
        self.assertGreater(fields["compiled_claim_count"], 0)
        self.assertTrue(result.web_result.fetched_documents[0].ok)
        self.assertGreater(result.score.diagnostic_scores["evidence_family_news"], 0.0)
        self.assertGreater(result.score.diagnostic_scores["claim_backed_claim_count_capped"], 0.0)
        self.assertEqual(result.score.diagnostic_scores.get("snippet_only_green_block", 0.0), 0.0)

    def test_theme_rebalance_enabled_without_provider_uses_default_codex_provider(self):
        with patch(
            "e2r.llm.codex_theme_provider.CodexCLIThemeRouteProvider.route",
            return_value=ThemeRouteOutput(status="no_transition"),
        ) as route:
            result = FreeWebResearchRunner(
                browser_provider=EmptySearchProvider(),
                free_search_provider=EmptySearchProvider(),
            ).run(
                FreeWebResearchInput(
                    company_name="NAVER",
                    symbol="035420",
                    sector="platform",
                    market=Market.KR,
                    as_of_date=date(2026, 6, 8),
                    theme_rebalance_enabled=True,
                )
            )

        self.assertIsNotNone(result.theme_route)
        self.assertEqual(result.theme_route.status, "no_transition")
        self.assertGreater(route.call_count, 0)
        self.assertEqual(result.theme_route_diagnostics["theme_rebalance_status"], "completed")
        self.assertEqual(result.expansion_queries_run, ())

    def test_theme_route_provider_auto_enables_rebalance(self):
        route_provider = FakeThemeRouteProvider(output=ThemeRouteOutput(status="no_transition"))

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=EmptySearchProvider(),
        ).run(
            FreeWebResearchInput(
                company_name="테스트기업",
                symbol="000001",
                sector=None,
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                theme_route_provider=route_provider,
            )
        )

        self.assertGreaterEqual(len(route_provider.calls), 2)
        self.assertFalse(route_provider.calls[0].score_gap_context)
        self.assertTrue(any(call.score_gap_context for call in route_provider.calls[1:]))
        self.assertEqual(result.theme_route.status, "no_transition")
        self.assertEqual(result.theme_route_diagnostics["theme_rebalance_status"], "completed")

    def test_theme_route_expands_asof_safe_queries_only(self):
        route_provider = FakeThemeRouteProvider(
            output=ThemeRouteOutput(
                status="transition_detected",
                transition_detected=True,
                route_confidence=0.8,
                emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                suggested_queries=(
                    "AI 클라우드 매출",
                    "NAVER AI 데이터센터 매출 2027",
                    "NAVER after:2026-06-09 미래 발간 리포트",
                ),
                evidence_slots=(
                    EvidenceSlotStatus(
                        slot="cloud_revenue",
                        status="present",
                        evidence_refs=("news:035420:2026-06-08:fixture-news:test",),
                        confidence=0.8,
                    ),
                ),
            )
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "NAVER 데이터센터 수주": (
                    SearchResult(
                        title="NAVER AI 데이터센터 투자",
                        url="https://news.example.com/naver-ai-dc-trigger",
                        snippet="엔비디아 GPU 협력",
                        source="fixture-news",
                        query="NAVER 데이터센터 수주",
                        confidence=0.8,
                    ),
                ),
                "NAVER AI 클라우드 매출": (
                    SearchResult(
                        title="NAVER AI 클라우드 매출 성장",
                        url="https://news.example.com/naver-ai-cloud-sales",
                        snippet="클라우드 매출 성장률 40%",
                        source="fixture-news",
                        query="NAVER AI 클라우드 매출",
                        confidence=0.8,
                    ),
                ),
                "NAVER AI 데이터센터 매출 2027": (
                    SearchResult(
                        title="NAVER AI 데이터센터 2027 매출 전망",
                        url="https://news.example.com/naver-ai-dc-2027e",
                        snippet="2026년 현재 공개된 2027년 매출 전망",
                        source="fixture-news",
                        query="NAVER AI 데이터센터 매출 2027",
                        confidence=0.8,
                    ),
                ),
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="NAVER",
                symbol="035420",
                sector="platform",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=1,
            )
        )

        self.assertEqual(result.expansion_queries_run, ("NAVER AI 클라우드 매출", "NAVER AI 데이터센터 매출 2027"))
        self.assertTrue(any(item.reason == "future_query_rejected" for item in result.skipped_queries))
        query_texts = tuple(spec.query for spec in result.web_result.query_plan.queries)
        self.assertIn("NAVER AI 클라우드 매출", query_texts)
        self.assertIn("NAVER AI 데이터센터 매출 2027", query_texts)
        self.assertEqual(result.score.diagnostic_scores["theme_rebalance_enabled"], 100.0)
        self.assertEqual(result.score.diagnostic_scores["llm_deep_research_completed"], 100.0)

    def test_asof_query_validator_allows_forward_estimate_period_but_blocks_future_publication_filter(self):
        self.assertEqual(
            _asof_safe_theme_query("테스트 2027년 영업이익 전망", date(2026, 6, 8)),
            "테스트 2027년 영업이익 전망",
        )
        self.assertIsNone(
            _asof_safe_theme_query("테스트 after:2026-06-09 발간 리포트", date(2026, 6, 8))
        )

    def test_theme_route_reasks_llm_when_expansion_query_is_duplicate(self):
        retry_url = "https://news.example.com/test-initial-theme-retry"
        duplicate_query = "테스트초기 수주잔고"
        retry_query = "테스트초기 클라우드 매출 성장률"
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.7,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    suggested_queries=(duplicate_query,),
                ),
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.8,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    suggested_queries=(retry_query,),
                ),
                ThemeRouteOutput(status="no_transition"),
            ]
        )
        provider = FixtureSearchProvider(
            results_by_query={
                retry_query: (
                    SearchResult(
                        title="테스트초기 클라우드 매출 성장",
                        url=retry_url,
                        snippet="클라우드 매출 성장률 42%",
                        source="fixture-news",
                        query=retry_query,
                        confidence=0.8,
                    ),
                ),
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트초기",
                symbol="900001",
                sector="platform",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={retry_url: "테스트초기 클라우드 매출 성장률 42%와 AI 인프라 매출이 확인됐다."},
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=1,
            )
        )

        self.assertIn(retry_query, result.expansion_queries_run)
        self.assertTrue(any(item.reason == "duplicate_theme_query" for item in result.skipped_queries))
        self.assertTrue(any("duplicate_theme_query" in item for item in route_provider.calls[1].score_gap_context))
        self.assertEqual(len(result.web_result.parsed_news), 1)

    def test_theme_route_continues_after_empty_expansion_round(self):
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.7,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    suggested_queries=("AI 매출 확인",),
                    missing_information=("cloud_revenue",),
                ),
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.8,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    suggested_queries=("클라우드 매출 성장률",),
                    evidence_slots=(
                        EvidenceSlotStatus(
                            slot="cloud_revenue",
                            status="present",
                            evidence_refs=("news:035420:2026-06-08:fixture-news:cloud",),
                            confidence=0.8,
                        ),
                    ),
                ),
            ]
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "NAVER AI 매출 확인": (),
                "NAVER 클라우드 매출 성장률": (
                    SearchResult(
                        title="NAVER 클라우드 매출 성장률 40%",
                        url="https://news.example.com/naver-cloud-growth",
                        snippet="AI 클라우드 매출 성장률 40%와 GPU 인프라 투자",
                        source="fixture-news",
                        query="NAVER 클라우드 매출 성장률",
                        confidence=0.8,
                    ),
                ),
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="NAVER",
                symbol="035420",
                sector="platform",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=2,
            )
        )

        self.assertGreaterEqual(len(route_provider.calls), 2)
        self.assertEqual(result.expansion_queries_run, ("NAVER AI 매출 확인", "NAVER 클라우드 매출 성장률"))
        self.assertEqual(len(result.web_result.parsed_news), 1)
        self.assertTrue(result.web_result.parsed_news[0].parsed_fields["gpu_cloud_revenue_visible"])

    def test_theme_evidence_review_receives_fetched_documents(self):
        url = "https://news.example.com/naver-ai-cloud"
        route_ref = stable_news_evidence_id(
            symbol="035420",
            published_date=date(2026, 6, 8),
            source="fixture-news",
            source_url=url,
            title="NAVER AI 클라우드 매출 성장",
        )
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.7,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    suggested_queries=(),
                    missing_information=("cloud_revenue",),
                ),
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.85,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    evidence_slots=(
                        EvidenceSlotStatus(
                            slot="cloud_revenue",
                            status="present",
                            evidence_refs=(route_ref,),
                            confidence=0.8,
                        ),
                    ),
                    missing_information=("fcf_impact",),
                ),
            ]
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "NAVER 데이터센터 수주": (
                    SearchResult(
                        title="NAVER AI 클라우드 매출 성장",
                        url=url,
                        snippet="클라우드 매출 성장률 40%",
                        source="fixture-news",
                        query="NAVER 데이터센터 수주",
                        confidence=0.8,
                    ),
                )
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="NAVER",
                symbol="035420",
                sector="platform",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={
                    url: "NAVER AI 클라우드 매출 성장률 40%와 데이터센터 GPU 인프라 투자가 확인됐다."
                },
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
                theme_evidence_review_enabled=True,
            )
        )

        self.assertGreaterEqual(len(route_provider.calls), 2)
        review_input = route_provider.calls[1]
        self.assertEqual(len(review_input.documents), 1)
        self.assertIn("클라우드 매출 성장률 40%", review_input.documents[0].text_excerpt)
        self.assertFalse(result.web_result.parsed_news[0].parsed_fields["search_snippet_only"])
        self.assertEqual(result.theme_route_diagnostics["theme_evidence_review_status"], "completed")
        self.assertEqual(result.score.diagnostic_scores["green_unlock_evidence_score"], 100.0)

    def test_theme_evidence_review_provider_error_records_timeout_without_overwriting_route(self):
        url = "https://news.example.com/sk-hynix-hbm"
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.72,
                    emerging_theme_id="AI_HBM_DATACENTER_MEMORY",
                    large_sector_id="R2_AI_SEMICONDUCTOR_ELECTRONICS",
                    canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    suggested_queries=("SK하이닉스 HBM 추가 근거",),
                ),
                ThemeRouteOutput(status="provider_error", blocked_reason="codex_cli_timeout"),
            ]
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "SK하이닉스 HBM": (
                    SearchResult(
                        title="SK하이닉스 HBM 고객 배정",
                        url=url,
                        snippet="HBM 고객 allocation",
                        source="fixture-news",
                        query="SK하이닉스 HBM",
                        confidence=0.8,
                    ),
                ),
                "SK하이닉스 HBM 추가 근거": (
                    SearchResult(
                        title="SK하이닉스 HBM 추가 고객 배정",
                        url=f"{url}?extra=1",
                        snippet="HBM 추가 고객 allocation",
                        source="fixture-news",
                        query="SK하이닉스 HBM 추가 근거",
                        confidence=0.8,
                    ),
                )
            }
        )
        plan = QueryPlan(
            company_name="SK하이닉스",
            symbol="000660",
            sector="semiconductor",
            market=Market.KR,
            as_of_date=date(2026, 6, 21),
            queries=(
                QuerySpec(
                    group="fixture",
                    query="SK하이닉스 HBM",
                    priority=1,
                    company_name="SK하이닉스",
                    symbol="000660",
                    sector="semiconductor",
                    market=Market.KR,
                    as_of_date=date(2026, 6, 21),
                ),
            ),
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
            query_planner=_FixedQueryPlanner(plan),
        ).run(
            FreeWebResearchInput(
                company_name="SK하이닉스",
                symbol="000660",
                sector="semiconductor",
                market=Market.KR,
                as_of_date=date(2026, 6, 21),
                top_results=1,
                fixture_text_by_url={
                    url: "SK하이닉스 HBM 고객 배정 원문",
                    f"{url}?extra=1": "SK하이닉스 HBM 추가 고객 배정 원문",
                },
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=1,
                require_resolved_score_gaps_for_scoring=False,
                theme_evidence_review_enabled=True,
                theme_evidence_review_timeout_seconds=30.0,
            )
        )

        self.assertGreaterEqual(len(route_provider.calls), 2)
        self.assertNotEqual(result.theme_route.status, "provider_error")
        self.assertEqual(result.theme_route_diagnostics["theme_evidence_review_status"], "provider_error")
        self.assertEqual(result.theme_route_diagnostics["theme_evidence_review_blocked_reason"], "codex_cli_timeout")
        self.assertEqual(result.theme_route_diagnostics["theme_evidence_review_timeout_seconds"], 30.0)
        self.assertEqual(result.theme_route_diagnostics["score_blocked_reason"], "theme_route_needs_more_evidence")

    def test_theme_route_document_anchor_can_back_route_without_legacy_field_score(self):
        url = "https://news.example.com/samsung-hbm-document"
        as_of = date(2026, 6, 21)
        plan = QueryPlan(
            company_name="삼성전자",
            symbol="005930",
            sector="semiconductor",
            market=Market.KR,
            as_of_date=as_of,
            queries=(
                QuerySpec(
                    group="fixture",
                    query="삼성전자 HBM",
                    priority=1,
                    company_name="삼성전자",
                    symbol="005930",
                    sector="semiconductor",
                    market=Market.KR,
                    as_of_date=as_of,
                ),
            ),
        )

        class DocumentAnchorRouteProvider:
            def __init__(self):
                self.calls = []

            def route(self, inputs):
                self.calls.append(inputs)
                if inputs.documents:
                    document_ref = next(ref for ref in inputs.documents[0].evidence_ids if str(ref).startswith("document_anchor:"))
                    return ThemeRouteOutput(
                        status="transition_detected",
                        transition_detected=True,
                        route_confidence=0.86,
                        emerging_theme_id="AI_HBM_DATACENTER_MEMORY",
                        large_sector_id="R2_AI_SEMICONDUCTOR_ELECTRONICS",
                        canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                        normalized_parsed_fields={"customer_allocation": True},
                        evidence_slots=(
                            EvidenceSlotStatus(
                                slot="customer_allocation",
                                status="present",
                                evidence_refs=(document_ref,),
                                confidence=0.8,
                            ),
                        ),
                    )
                return ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.72,
                    emerging_theme_id="AI_HBM_DATACENTER_MEMORY",
                    suggested_queries=(),
                )

        route_provider = DocumentAnchorRouteProvider()
        provider = FixtureSearchProvider(
            results_by_query={
                "삼성전자 HBM": (
                    SearchResult(
                        title="삼성전자 원문 문서",
                        url=url,
                        snippet="원문 확인",
                        source="fixture-web",
                        query="삼성전자 HBM",
                        confidence=0.8,
                    ),
                )
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
            query_planner=_FixedQueryPlanner(plan),
        ).run(
            FreeWebResearchInput(
                company_name="삼성전자",
                symbol="005930",
                sector="semiconductor",
                market=Market.KR,
                as_of_date=as_of,
                top_results=1,
                fixture_text_by_url={
                    url: "삼성전자 원문 문서다. "
                    "이 문장은 parser가 점수 primitive를 직접 만들지 않아야 한다."
                },
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
                max_score_gap_expansion_rounds=0,
                theme_evidence_review_enabled=True,
            )
        )

        review_call = next(call for call in route_provider.calls if call.documents)
        self.assertTrue(any(ref.startswith("document_anchor:") for ref in review_call.documents[0].evidence_ids))
        self.assertEqual(result.theme_route_diagnostics["theme_evidence_gate_status"], "source_backed")
        self.assertEqual(result.theme_route_diagnostics["theme_document_ref_available_count"], 1)
        self.assertEqual(result.theme_route_diagnostics["theme_evidence_ref_match_count"], 1)
        self.assertEqual(result.feature_result.payload.canonical_archetype_id, "C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertNotIn("customer_allocation", result.feature_input.agent_extracted_fields)

    def test_post_parse_gap_expansion_runs_review_suggested_report_query(self):
        initial_url = "https://news.example.com/test-electronics-hbm"
        report_url = "https://finance.example.com/research/company_read.naver?nid=990"
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.72,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    missing_information=("consensus_report_bridge",),
                ),
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.82,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    missing_information=("컨센서스 리포트",),
                    suggested_queries=("테스트전자 목표주가 상향 EPS 추정치 컨센서스 리포트",),
                ),
            ]
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "테스트전자 데이터센터 수주": (
                    SearchResult(
                        title="테스트전자 HBM 데이터센터 수요 확대",
                        url=initial_url,
                        snippet="AI 데이터센터 수요가 확대된다.",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트전자 데이터센터 수주",
                        is_news=True,
                        confidence=0.8,
                    ),
                ),
                "테스트전자 목표주가 상향 EPS 추정치 컨센서스 리포트": (
                    SearchResult(
                        title="테스트전자 종목분석 - 2Q26 영업이익 70조원 예상",
                        url=report_url,
                        snippet="목표주가 87만원으로 상향. HBM 수요와 EPS 추정치 상향",
                        source="fixture-research",
                        published_at=datetime(2026, 6, 8, 9),
                        query="테스트전자 목표주가 상향 EPS 추정치 컨센서스 리포트",
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                ),
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트전자",
                symbol="123456",
                sector="semiconductor",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={
                    initial_url: "테스트전자는 HBM 데이터센터 수요 확대를 보도했다.",
                    report_url: "테스트전자는 HBM 수요 증가와 EPS 추정치 상향을 근거로 리포트가 발간됐다.",
                },
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
                theme_evidence_review_enabled=True,
            )
        )

        self.assertIn("테스트전자 목표주가 상향 EPS 추정치 컨센서스 리포트", result.expansion_queries_run)
        self.assertGreaterEqual(result.theme_route_diagnostics["post_parse_gap_expansion_count"], 1)
        self.assertEqual(len(result.web_result.parsed_reports), 1)
        self.assertEqual(len(result.feature_input.consensus), 1)
        self.assertIn(
            stable_consensus_evidence_id(
                symbol="123456",
                estimate_date=date(2026, 6, 8),
                fiscal_year=2026,
                source="report_proxy",
            ),
            {item.evidence_id for item in result.web_result.evidence},
        )

    def test_post_parse_gap_expansion_reasks_llm_when_query_is_duplicate(self):
        initial_url = "https://news.example.com/test-post-parse-demand"
        report_url = "https://finance.example.com/research/test-post-parse-retry"
        duplicate_query = "테스트후속 수주잔고"
        retry_query = "테스트후속 EPS OP FCF 추정치 상향 컨센서스 리포트"
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(
                    status="needs_more_evidence",
                    missing_information=("consensus_report_bridge",),
                    suggested_queries=(duplicate_query,),
                ),
                ThemeRouteOutput(
                    status="needs_more_evidence",
                    missing_information=("consensus_report_bridge",),
                    suggested_queries=(retry_query,),
                ),
                ThemeRouteOutput(status="no_transition"),
            ]
        )
        provider = FixtureSearchProvider(
            results_by_query={
                duplicate_query: (
                    SearchResult(
                        title="테스트후속 데이터센터 수요",
                        url=initial_url,
                        snippet="AI 데이터센터 수요가 확대된다.",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query=duplicate_query,
                        is_news=True,
                        confidence=0.8,
                    ),
                ),
                retry_query: (
                    SearchResult(
                        title="테스트후속 추정치 상향 리포트",
                        url=report_url,
                        snippet="EPS 상향 30%, 영업이익 추정치 상향 32%, FCF 상향 24%",
                        source="fixture-research",
                        published_at=datetime(2026, 6, 8, 9),
                        query=retry_query,
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                ),
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트후속",
                symbol="900002",
                sector="semiconductor",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={
                    initial_url: "테스트후속은 AI 데이터센터 수요 확대를 보도했다.",
                    report_url: (
                        "테스트후속 리포트. EPS 상향 30%, 영업이익 추정치 상향 32%, "
                        "FCF 상향 24%, 목표주가 상향 14%."
                    ),
                },
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
                theme_evidence_review_enabled=True,
            )
        )

        self.assertIn(retry_query, result.expansion_queries_run)
        self.assertTrue(any(item.reason == "duplicate_post_parse_gap_query" for item in result.skipped_queries))
        self.assertTrue(any("duplicate_post_parse_gap_query" in item for item in route_provider.calls[2].score_gap_context))
        self.assertTrue(result.feature_input.consensus_revisions)
        self.assertGreaterEqual(result.score.diagnostic_scores["revision_score"], 80.0)

    def test_post_parse_gap_expansion_runs_contract_quality_query_from_missing_slot(self):
        initial_url = "https://news.example.com/test-memory-hbm"
        contract_url = "https://news.example.com/test-memory-hbm-contract-quality"
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.74,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    missing_information=("contract_quality",),
                ),
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.84,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    missing_information=("HBM 장기공급계약 선수금 수주잔고 RPO",),
                    suggested_queries=("테스트메모리 장기공급계약 선수금 수주잔고 RPO",),
                    evidence_slots=(
                        EvidenceSlotStatus(
                            slot="contract_quality",
                            status="missing",
                            missing_reason="장기공급계약의 선수금, 물량, 기간, RPO 확인 필요",
                        ),
                    ),
                ),
            ]
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "테스트메모리 데이터센터 수주": (
                    SearchResult(
                        title="테스트메모리 HBM 데이터센터 수요",
                        url=initial_url,
                        snippet="엔비디아 GPU 수요와 HBM 공급 확대",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트메모리 데이터센터 수주",
                        is_news=True,
                        confidence=0.8,
                    ),
                ),
                "테스트메모리 장기공급계약 선수금 수주잔고 RPO": (
                    SearchResult(
                        title="테스트메모리 HBM 장기공급계약과 선수금 확인",
                        url=contract_url,
                        snippet="사상 최대 수주잔고, 최소 물량 보장, 선수금이 확인됐다.",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 9),
                        query="테스트메모리 장기공급계약 선수금 수주잔고 RPO",
                        is_news=True,
                        confidence=0.9,
                    ),
                ),
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트메모리",
                symbol="654321",
                sector="semiconductor",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={
                    initial_url: "테스트메모리는 HBM 수요와 GPU 고객 확대를 보도했다.",
                    contract_url: (
                        "테스트메모리는 HBM 장기공급계약과 선수금, 최소 물량 보장, "
                        "사상 최대 수주잔고를 확인했다."
                    ),
                },
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
                theme_evidence_review_enabled=True,
            )
        )

        self.assertIn("테스트메모리 장기공급계약 선수금 수주잔고 RPO", result.expansion_queries_run)
        self.assertGreaterEqual(result.theme_route_diagnostics["post_parse_gap_expansion_count"], 1)
        parsed_fields = [item.parsed_fields for item in result.web_result.parsed_news]
        self.assertTrue(any(fields.get("prepayment_exists") for fields in parsed_fields))
        self.assertTrue(any(fields.get("record_backlog") for fields in parsed_fields))

    def test_post_parse_gap_expansion_does_not_synthesize_query_without_llm_suggestion(self):
        initial_url = "https://news.example.com/test-memory-hbm-no-suggestion"
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.74,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    missing_information=("contract_quality",),
                ),
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.84,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    missing_information=("contract_quality", "backlog_or_rpo", "prepayment"),
                    suggested_queries=(),
                    evidence_slots=(
                        EvidenceSlotStatus(
                            slot="contract_quality",
                            status="missing",
                            missing_reason="LLM did not provide a follow-up query",
                        ),
                    ),
                ),
            ]
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "테스트메모리 데이터센터 수주": (
                    SearchResult(
                        title="테스트메모리 HBM 데이터센터 수요",
                        url=initial_url,
                        snippet="엔비디아 GPU 수요와 HBM 공급 확대",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트메모리 데이터센터 수주",
                        is_news=True,
                        confidence=0.8,
                    ),
                ),
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트메모리",
                symbol="654321",
                sector="semiconductor",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={
                    initial_url: "테스트메모리는 HBM 수요와 GPU 고객 확대를 보도했다.",
                },
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
                theme_evidence_review_enabled=True,
            )
        )

        self.assertEqual(result.theme_route_diagnostics["post_parse_gap_expansion_count"], 0)
        self.assertNotIn("테스트메모리 장기공급계약 선수금 수주잔고 RPO", result.expansion_queries_run)

    def test_revision_gap_expansion_searches_estimate_change_from_llm_query(self):
        initial_url = "https://news.example.com/test-electronics-ai-demand"
        revision_url = "https://finance.example.com/research/test-electronics-revision"
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.74,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    missing_information=("revision",),
                ),
                ThemeRouteOutput(
                    status="transition_detected",
                    transition_detected=True,
                    route_confidence=0.84,
                    emerging_theme_id="AI_INFRA_PLATFORM_DATACENTER",
                    missing_information=("이전 추정치 대비 EPS OP FCF 컨센서스 상향률",),
                    suggested_queries=("테스트전자 EPS OP FCF 추정치 상향 컨센서스 변화 리포트",),
                    evidence_slots=(
                        EvidenceSlotStatus(
                            slot="revision",
                            status="missing",
                            missing_reason="이전 추정치와 현재 추정치 비교가 필요",
                        ),
                    ),
                ),
            ]
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "테스트전자 데이터센터 수주": (
                    SearchResult(
                        title="테스트전자 AI 데이터센터 수요",
                        url=initial_url,
                        snippet="AI 수요가 확대된다.",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트전자 데이터센터 수주",
                        is_news=True,
                        confidence=0.8,
                    ),
                ),
                "테스트전자 EPS OP FCF 추정치 상향 컨센서스 변화 리포트": (
                    SearchResult(
                        title="테스트전자 종목분석 - 추정치 대폭 상향",
                        url=revision_url,
                        snippet="EPS 상향 35%, 영업이익 추정치 상향 40%, FCF 상향 25%",
                        source="fixture-research",
                        published_at=datetime(2026, 6, 8, 9),
                        query="테스트전자 EPS OP FCF 추정치 상향 컨센서스 변화 리포트",
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                ),
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트전자",
                symbol="123456",
                sector="semiconductor",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={
                    initial_url: "테스트전자는 AI 데이터센터 수요 확대를 보도했다.",
                    revision_url: (
                        "테스트전자 리포트. EPS 상향 35%, 영업이익 추정치 상향 40%, "
                        "FCF 상향 25%, 목표주가 상향 20%. 원문 기반 추정치 비교."
                    ),
                },
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
                theme_evidence_review_enabled=True,
            )
        )

        self.assertIn("테스트전자 EPS OP FCF 추정치 상향 컨센서스 변화 리포트", result.expansion_queries_run)
        self.assertGreaterEqual(result.theme_route_diagnostics["post_parse_gap_expansion_count"], 1)
        self.assertTrue(result.feature_input.consensus_revisions)
        self.assertGreaterEqual(result.score.diagnostic_scores["revision_score"], 80.0)

    def test_score_gap_expansion_searches_low_revision_after_initial_score(self):
        initial_url = "https://news.example.com/test-score-gap-demand"
        revision_url = "https://finance.example.com/research/test-score-gap-revision"
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(
                    status="needs_more_evidence",
                    missing_information=("revision estimate consensus target price EPS OP FCF",),
                    suggested_queries=("테스트스코어 EPS OP FCF 추정치 상향 컨센서스 변화 리포트",),
                ),
                ThemeRouteOutput(status="no_transition"),
            ]
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "테스트스코어 데이터센터 수주": (
                    SearchResult(
                        title="테스트스코어 데이터센터 수요",
                        url=initial_url,
                        snippet="데이터센터 수요가 확대된다.",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트스코어 데이터센터 수주",
                        is_news=True,
                        confidence=0.8,
                    ),
                ),
                "테스트스코어 EPS OP FCF 추정치 상향 컨센서스 변화 리포트": (
                    SearchResult(
                        title="테스트스코어 추정치 상향 리포트",
                        url=revision_url,
                        snippet="EPS 상향 33%, 영업이익 추정치 상향 36%, FCF 상향 28%",
                        source="fixture-research",
                        published_at=datetime(2026, 6, 8, 9),
                        query="테스트스코어 EPS OP FCF 추정치 상향 컨센서스 변화 리포트",
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                ),
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트스코어",
                symbol="777777",
                sector="semiconductor",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={
                    initial_url: "테스트스코어는 데이터센터 수요 확대를 보도했다.",
                    revision_url: (
                        "테스트스코어 리포트. EPS 상향 33%, 영업이익 추정치 상향 36%, "
                        "FCF 상향 28%, 목표주가 상향 18%."
                    ),
                },
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
                theme_evidence_review_enabled=True,
            )
        )

        self.assertEqual(result.theme_route_diagnostics["post_parse_gap_expansion_count"], 0)
        self.assertGreaterEqual(result.theme_route_diagnostics["post_score_gap_expansion_count"], 1)
        self.assertIn("테스트스코어 EPS OP FCF 추정치 상향 컨센서스 변화 리포트", result.expansion_queries_run)
        self.assertTrue(any("revision" in item for item in route_provider.calls[2].score_gap_context))
        self.assertTrue(result.feature_input.consensus_revisions)
        self.assertGreaterEqual(result.score.diagnostic_scores["revision_score"], 80.0)

    def test_score_gap_incremental_fetch_is_bounded_when_initial_fetch_is_uncapped(self):
        as_of = date(2026, 6, 8)
        initial_query = "테스트스코어 데이터센터 수주"
        gap_query = "테스트스코어 EPS OP FCF 추정치 상향 컨센서스 변화 리포트"
        plan = QueryPlan(
            company_name="테스트스코어",
            symbol="777777",
            sector="semiconductor",
            market=Market.KR,
            as_of_date=as_of,
            queries=(
                QuerySpec(
                    group="discovery",
                    query=initial_query,
                    priority=10,
                    company_name="테스트스코어",
                    symbol="777777",
                    sector="semiconductor",
                    market=Market.KR,
                    as_of_date=as_of,
                ),
            ),
        )
        initial_results = tuple(
            SearchResult(
                title=f"테스트스코어 데이터센터 수요 {index}",
                url=f"https://news.example.com/test-score-gap-demand-{index}",
                snippet="테스트스코어 데이터센터 수요가 확대된다.",
                source="fixture-news",
                published_at=datetime(2026, 6, 8, 8),
                query=initial_query,
                rank=index,
                is_news=True,
                confidence=0.8,
            )
            for index in range(30)
        )
        gap_results = tuple(
            SearchResult(
                title=f"테스트스코어 추정치 상향 리포트 {index}",
                url=f"https://finance.example.com/research/test-score-gap-revision-{index}",
                snippet="테스트스코어 EPS 상향 33%, 영업이익 추정치 상향 36%, FCF 상향 28%",
                source="fixture-research",
                published_at=datetime(2026, 6, 8, 9),
                query=gap_query,
                rank=index,
                is_report_domain=True,
                confidence=0.9,
            )
            for index in range(12)
        )
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(
                    status="needs_more_evidence",
                    missing_information=("revision estimate consensus target price EPS OP FCF",),
                    suggested_queries=(gap_query,),
                ),
                ThemeRouteOutput(status="no_transition"),
            ]
        )
        phase_events = []

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=FixtureSearchProvider(
                results_by_query={
                    initial_query: initial_results,
                    gap_query: gap_results,
                }
            ),
            query_planner=_FixedQueryPlanner(plan),
        ).run(
            FreeWebResearchInput(
                company_name="테스트스코어",
                symbol="777777",
                sector="semiconductor",
                market=Market.KR,
                as_of_date=as_of,
                top_results=60,
                fixture_text_by_url={
                    item.url: (
                        "테스트스코어 리포트. EPS 상향 33%, 영업이익 추정치 상향 36%, "
                        "FCF 상향 28%, 목표주가 상향 18%."
                    )
                    for item in gap_results
                },
                post_gap_fetch_min_results=6,
                post_gap_fetch_results_per_query=3,
                max_theme_expansion_rounds=0,
                max_score_gap_expansion_rounds=1,
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                require_resolved_score_gaps_for_scoring=False,
                phase_event_sink=phase_events.append,
            )
        )

        selected_by_gap_query = [
            item for item in result.web_result.selected_results
            if item.result.query == gap_query
        ]
        start_events = [
            event for event in phase_events
            if event["phase"] == "post_score_gap_web_research_start"
        ]
        self.assertEqual(start_events[-1]["gap_fetch_mode"], "incremental")
        self.assertEqual(start_events[-1]["top_results_override"], 6)
        merged_complete_events = [
            event for event in phase_events
            if event["phase"] == "post_score_gap_web_research_complete"
        ]
        new_only_complete_events = [
            event for event in phase_events
            if event["phase"] == "post_score_gap_web_research_new_only_complete"
        ]
        self.assertEqual(merged_complete_events[-1]["fetched_document_count"], len(initial_results) + 6)
        self.assertEqual(new_only_complete_events[-1]["query_count"], 1)
        self.assertEqual(new_only_complete_events[-1]["fetched_document_count"], 6)
        self.assertEqual(new_only_complete_events[-1]["selected_result_count"], 6)
        self.assertEqual(len(selected_by_gap_query), 6)
        self.assertEqual(len(result.web_result.selected_results), len(initial_results) + 6)
        self.assertEqual(len(result.web_result.fetched_documents), len(result.web_result.selected_results))
        self.assertLess(len(result.web_result.fetched_documents), len(initial_results) + len(gap_results))
        self.assertGreaterEqual(result.score.diagnostic_scores["revision_score"], 80.0)

    def test_score_gap_round_limit_blocks_even_after_fetching_gap_queries(self):
        as_of = date(2026, 6, 8)
        initial_query = "테스트라운드 데이터센터 수주"
        gap_query = "테스트라운드 EPS OP 추정치 상향 리포트"
        initial_url = "https://news.example.com/test-round-limit-demand"
        gap_url = "https://finance.example.com/research/test-round-limit-revision"
        plan = QueryPlan(
            company_name="테스트라운드",
            symbol="777778",
            sector="semiconductor",
            market=Market.KR,
            as_of_date=as_of,
            queries=(
                QuerySpec(
                    group="discovery",
                    query=initial_query,
                    priority=10,
                    company_name="테스트라운드",
                    symbol="777778",
                    sector="semiconductor",
                    market=Market.KR,
                    as_of_date=as_of,
                ),
            ),
        )
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(
                    status="needs_more_evidence",
                    missing_information=("revision estimate consensus target price EPS OP",),
                    suggested_queries=(gap_query,),
                ),
                ThemeRouteOutput(status="no_transition"),
            ]
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=FixtureSearchProvider(
                results_by_query={
                    initial_query: (
                        SearchResult(
                            title="테스트라운드 데이터센터 수요",
                            url=initial_url,
                            snippet="테스트라운드 데이터센터 수요가 확대된다.",
                            source="fixture-news",
                            published_at=datetime(2026, 6, 8, 8),
                            query=initial_query,
                            is_news=True,
                            confidence=0.8,
                        ),
                    ),
                    gap_query: (
                        SearchResult(
                            title="테스트라운드 추정치 상향 리포트",
                            url=gap_url,
                            snippet="테스트라운드 EPS 상향 33%, 영업이익 추정치 상향 36%, 목표주가 상향 18%",
                            source="fixture-research",
                            published_at=datetime(2026, 6, 8, 9),
                            query=gap_query,
                            is_report_domain=True,
                            confidence=0.9,
                        ),
                    ),
                }
            ),
            query_planner=_FixedQueryPlanner(plan),
        ).run(
            FreeWebResearchInput(
                company_name="테스트라운드",
                symbol="777778",
                sector="semiconductor",
                market=Market.KR,
                as_of_date=as_of,
                top_results=5,
                fixture_text_by_url={
                    initial_url: "테스트라운드 데이터센터 수요 확대.",
                    gap_url: "테스트라운드 리포트. EPS 상향 33%, 영업이익 추정치 상향 36%, 목표주가 상향 18%.",
                },
                max_theme_expansion_rounds=0,
                max_score_gap_expansion_rounds=1,
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                require_resolved_score_gaps_for_scoring=True,
            )
        )

        self.assertEqual(result.theme_route_diagnostics["post_score_gap_expansion_status"], "round_limit_reached")
        self.assertEqual(result.theme_route_diagnostics["score_blocked_reason"], "score_gap_round_limit")
        self.assertEqual(result.stage.stage, Stage.STAGE_0)
        self.assertEqual(result.score.total_score, 0.0)
        self.assertEqual(result.score.diagnostic_scores["score_valid"], 0.0)
        self.assertEqual(result.score.diagnostic_scores["score_blocked_by_score_gap"], 100.0)
        self.assertIn("raw_score_total_before_score_gap_block", result.score.diagnostic_scores)
        self.assertGreater(result.score.diagnostic_scores["raw_score_total_before_score_gap_block"], 0.0)

    def test_post_gap_top_results_uses_targeted_gap_limit(self):
        inputs = FreeWebResearchInput(
            company_name="테스트",
            symbol="123456",
            sector=None,
            market=Market.KR,
            as_of_date=date(2026, 6, 8),
            top_results=60,
            post_gap_fetch_min_results=12,
            post_gap_fetch_results_per_query=4,
        )
        specs = tuple(
            QuerySpec(
                group="post_score_gap",
                query=f"테스트 gap query {index}",
                priority=170 + index,
                company_name="테스트",
                symbol="123456",
                sector=None,
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
            )
            for index in range(5)
        )

        self.assertEqual(_post_gap_top_results(inputs, specs), 20)

    def test_score_gap_expansion_reasks_llm_when_query_is_empty(self):
        initial_url = "https://news.example.com/test-retry-demand"
        revision_url = "https://finance.example.com/research/test-retry-revision"
        query = "테스트재요청 EPS OP FCF 추정치 상향 컨센서스 변화 리포트"
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(
                    status="needs_more_evidence",
                    missing_information=("revision estimate consensus target price EPS OP FCF",),
                    suggested_queries=(),
                ),
                ThemeRouteOutput(
                    status="needs_more_evidence",
                    missing_information=("revision estimate consensus target price EPS OP FCF",),
                    suggested_queries=(query,),
                ),
                ThemeRouteOutput(status="no_transition"),
            ]
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "테스트재요청 데이터센터 수주": (
                    SearchResult(
                        title="테스트재요청 데이터센터 수요",
                        url=initial_url,
                        snippet="데이터센터 수요가 확대된다.",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query="테스트재요청 데이터센터 수주",
                        is_news=True,
                        confidence=0.8,
                    ),
                ),
                query: (
                    SearchResult(
                        title="테스트재요청 추정치 상향 리포트",
                        url=revision_url,
                        snippet="EPS 상향 31%, 영업이익 추정치 상향 34%, FCF 상향 29%",
                        source="fixture-research",
                        published_at=datetime(2026, 6, 8, 9),
                        query=query,
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                ),
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트재요청",
                symbol="777778",
                sector="semiconductor",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={
                    initial_url: "테스트재요청은 데이터센터 수요 확대를 보도했다.",
                    revision_url: (
                        "테스트재요청 리포트. EPS 상향 31%, 영업이익 추정치 상향 34%, "
                        "FCF 상향 29%, 목표주가 상향 17%."
                    ),
                },
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
            )
        )

        self.assertIn(query, result.expansion_queries_run)
        self.assertTrue(
            any(
                "previous score-gap route returned no suggested_queries" in item
                for item in route_provider.calls[3].score_gap_context
            )
        )
        self.assertGreaterEqual(result.score.diagnostic_scores["revision_score"], 80.0)

    def test_score_gap_expansion_reasks_llm_when_query_is_duplicate(self):
        initial_url = "https://news.example.com/test-duplicate-demand"
        revision_url = "https://finance.example.com/research/test-duplicate-revision"
        duplicate_query = "테스트중복 데이터센터 수주"
        retry_query = "테스트중복 EPS OP FCF 추정치 상향 컨센서스 변화 리포트"
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(
                    status="needs_more_evidence",
                    missing_information=("revision estimate consensus target price EPS OP FCF",),
                    suggested_queries=(duplicate_query,),
                ),
                ThemeRouteOutput(
                    status="needs_more_evidence",
                    missing_information=("revision estimate consensus target price EPS OP FCF",),
                    suggested_queries=(retry_query,),
                ),
                ThemeRouteOutput(status="no_transition"),
            ]
        )
        provider = FixtureSearchProvider(
            results_by_query={
                duplicate_query: (
                    SearchResult(
                        title="테스트중복 데이터센터 수요",
                        url=initial_url,
                        snippet="데이터센터 수요가 확대된다.",
                        source="fixture-news",
                        published_at=datetime(2026, 6, 8, 8),
                        query=duplicate_query,
                        is_news=True,
                        confidence=0.8,
                    ),
                ),
                retry_query: (
                    SearchResult(
                        title="테스트중복 추정치 상향 리포트",
                        url=revision_url,
                        snippet="EPS 상향 32%, 영업이익 추정치 상향 37%, FCF 상향 26%",
                        source="fixture-research",
                        published_at=datetime(2026, 6, 8, 9),
                        query=retry_query,
                        is_report_domain=True,
                        confidence=0.9,
                    ),
                ),
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트중복",
                symbol="777779",
                sector="semiconductor",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={
                    initial_url: "테스트중복은 데이터센터 수요 확대를 보도했다.",
                    revision_url: (
                        "테스트중복 리포트. EPS 상향 32%, 영업이익 추정치 상향 37%, "
                        "FCF 상향 26%, 목표주가 상향 16%."
                    ),
                },
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
            )
        )

        self.assertIn(retry_query, result.expansion_queries_run)
        self.assertTrue(any(item.reason == "duplicate_score_gap_query" for item in result.skipped_queries))
        self.assertTrue(
            any("duplicate_score_gap_query" in item for item in route_provider.calls[3].score_gap_context)
        )
        self.assertGreaterEqual(result.score.diagnostic_scores["revision_score"], 80.0)

    def test_material_score_gap_without_llm_queries_blocks_score_and_stage(self):
        route_provider = FakeThemeRouteProvider(
            outputs=[
                ThemeRouteOutput(status="no_transition"),
                ThemeRouteOutput(
                    status="needs_more_evidence",
                    missing_information=("selected revision source missing",),
                    suggested_queries=(),
                ),
                ThemeRouteOutput(
                    status="needs_more_evidence",
                    missing_information=("selected revision source missing",),
                    suggested_queries=(),
                ),
            ]
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=EmptySearchProvider(),
        ).run(
            FreeWebResearchInput(
                company_name="테스트보류",
                symbol="999998",
                sector="software",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
            )
        )

        self.assertEqual(result.stage.stage, Stage.STAGE_0)
        self.assertEqual(result.score.total_score, 0.0)
        self.assertEqual(result.score.diagnostic_scores["score_valid"], 0.0)
        self.assertEqual(result.score.diagnostic_scores["score_blocked_by_score_gap"], 100.0)
        self.assertEqual(result.theme_route_diagnostics["score_blocked_reason"], "score_gap_llm_no_suggested_queries")
        self.assertEqual(result.theme_route_diagnostics["post_score_gap_expansion_status"], "llm_no_suggested_queries")
        self.assertIn("raw_score_total_before_score_gap_block", result.score.diagnostic_scores)
        self.assertTrue(result.theme_route_diagnostics["material_score_gap_unresolved_gaps"])

    def test_score_gap_diagnostics_always_include_material_unresolved_gaps(self):
        diagnostics = _with_score_gap_expansion_diagnostics(
            {"score_blocked_reason": "theme_route_needs_more_evidence"},
            _ScoreGapExpansionResult(
                status="no_progress",
                unresolved_gaps=(
                    "agentic primitive gap:customer_preorder_or_allocation; status:UNKNOWN",
                    "nonmaterial note",
                ),
                rejection_reasons=("score_gap_state_repeated",),
            ),
            ("SK하이닉스 HBM 고객 배정",),
        )

        self.assertEqual(
            diagnostics["material_score_gap_unresolved_gaps"],
            ("agentic primitive gap:customer_preorder_or_allocation; status:UNKNOWN",),
        )
        self.assertEqual(diagnostics["score_blocked_reason"], "theme_route_needs_more_evidence")

    def test_score_gap_progress_diagnostics_explain_new_documents_without_score_progress(self):
        previous = AgenticEvidenceRuntimeTrace(
            status="completed",
            document_ids=("DOC-A", "DOC-B"),
            claim_ids=("CLM-A",),
            mapping_ids=("MAP-A",),
            rejected_mapping_ids=("MAP-OLD-REJECTED",),
            rejected_mapping_summaries=(
                "MAP-OLD-REJECTED|claim=CLM-A|primitive=qualification_status|status=REJECTED|reason=old",
            ),
            eligibility_rejection_summaries=("old eligibility rejection",),
        )
        current = AgenticEvidenceRuntimeTrace(
            status="partial_error",
            document_ids=("DOC-C", "DOC-D"),
            claim_ids=("CLM-C",),
            mapping_ids=(),
            rejected_mapping_count=1,
            rejected_mapping_ids=("MAP-C-REJECTED",),
            rejected_mapping_summaries=(
                "MAP-C-REJECTED|claim=CLM-C|primitive=qualification_status|status=REJECTED|reason=target_scope_not_allowed:CUSTOMER",
            ),
            eligibility_rejection_summaries=(
                "MAP-C-REJECTED|claim=CLM-C|primitive=qualification_status|mapping_status=REJECTED|eligibility_reasons=source_date_missing",
            ),
            mapping_prefilter_original_task_count=18,
            mapping_prefilter_filtered_task_count=7,
            mapping_prefilter_skipped_input_count=1,
            mapping_prefilter_fallback_full_map_count=2,
            mapping_prefilter_fallback_full_map_summaries=(
                "fallback_full_map|document=DOC-C|claim=CLM-C|reason=fallback_full_map_unstructured_source",
            ),
            mapping_empty_output_count=1,
            mapping_empty_output_retry_count=2,
            mapping_empty_output_recovered_count=1,
            mapping_empty_output_summaries=(
                "empty_mapper_output|phase=agentic_evidence_mapping_chunk_complete|document=DOC-D",
            ),
            mapping_empty_output_retry_summaries=(
                "empty_mapper_retry|phase=agentic_evidence_mapping_chunk_empty_retry_recovered|document=DOC-C",
            ),
            skipped_existing_document_count=2,
            error_count=1,
            errors=("DOC-D:ValueError:claim_extractor_provider_error:usage_limit",),
        )

        diagnostics = _score_gap_progress_diagnostics(
            previous_trace=previous,
            current_trace=current,
            previous_signature=("total=0", "gap=qualification_status"),
            current_signature=("total=0", "gap=qualification_status"),
        )

        self.assertFalse(diagnostics["post_score_gap_score_state_changed"])
        self.assertEqual(diagnostics["post_score_gap_progress_reason"], "score_gap_new_claims_without_accepted_mappings")
        self.assertEqual(diagnostics["post_score_gap_new_document_count"], 2)
        self.assertEqual(diagnostics["post_score_gap_new_document_ids"], ("DOC-C", "DOC-D"))
        self.assertEqual(diagnostics["post_score_gap_new_claim_count"], 1)
        self.assertEqual(diagnostics["post_score_gap_new_claim_ids"], ("CLM-C",))
        self.assertEqual(diagnostics["post_score_gap_new_accepted_mapping_count"], 0)
        self.assertEqual(diagnostics["post_score_gap_new_rejected_mapping_count"], 1)
        self.assertEqual(diagnostics["post_score_gap_new_rejected_mapping_ids"], ("MAP-C-REJECTED",))
        self.assertIn(
            "target_scope_not_allowed:CUSTOMER",
            diagnostics["post_score_gap_new_rejected_mapping_summaries"][0],
        )
        self.assertIn(
            "source_date_missing",
            diagnostics["post_score_gap_new_eligibility_rejection_summaries"][0],
        )
        self.assertEqual(diagnostics["post_score_gap_new_trace_status"], "partial_error")
        self.assertEqual(diagnostics["post_score_gap_new_trace_error_count"], 1)
        self.assertIn("usage_limit", diagnostics["post_score_gap_new_trace_errors"][0])
        self.assertEqual(diagnostics["post_score_gap_new_trace_skipped_existing_document_count"], 2)
        self.assertEqual(diagnostics["post_score_gap_new_trace_mapping_prefilter_original_task_count"], 18)
        self.assertEqual(diagnostics["post_score_gap_new_trace_mapping_prefilter_filtered_task_count"], 7)
        self.assertEqual(diagnostics["post_score_gap_new_trace_mapping_prefilter_skipped_input_count"], 1)
        self.assertEqual(diagnostics["post_score_gap_new_trace_mapping_prefilter_fallback_full_map_count"], 2)
        self.assertIn(
            "fallback_full_map",
            diagnostics["post_score_gap_new_trace_mapping_prefilter_fallback_full_map_summaries"][0],
        )
        self.assertEqual(diagnostics["post_score_gap_new_trace_mapping_empty_output_count"], 1)
        self.assertEqual(diagnostics["post_score_gap_new_trace_mapping_empty_output_retry_count"], 2)
        self.assertEqual(diagnostics["post_score_gap_new_trace_mapping_empty_output_recovered_count"], 1)
        self.assertIn(
            "empty_mapper_output",
            diagnostics["post_score_gap_new_trace_mapping_empty_output_summaries"][0],
        )
        self.assertIn(
            "empty_mapper_retry",
            diagnostics["post_score_gap_new_trace_mapping_empty_output_retry_summaries"][0],
        )
        self.assertFalse(diagnostics["post_score_gap_primitive_state_changed"])
        self.assertEqual(diagnostics["post_score_gap_primitive_delta_summaries"], ())
        self.assertEqual(
            _score_gap_state_repeated_rejection_reasons(diagnostics),
            ("score_gap_state_repeated", "score_gap_new_claims_without_accepted_mappings"),
        )

    def test_score_gap_progress_diagnostics_flags_append_only_document_reprocessing(self):
        diagnostics = _score_gap_progress_diagnostics(
            previous_trace=AgenticEvidenceRuntimeTrace(
                status="completed",
                document_ids=("DOC-A",),
                claim_ids=("CLM-A",),
            ),
            current_trace=AgenticEvidenceRuntimeTrace(
                status="completed",
                document_ids=("DOC-A", "DOC-B"),
                claim_ids=("CLM-A", "CLM-B"),
            ),
            previous_signature=("total=80", "gap=revision"),
            current_signature=("total=80", "gap=revision"),
        )

        self.assertTrue(diagnostics["post_score_gap_append_only_violation"])
        self.assertEqual(diagnostics["post_score_gap_reprocessed_document_count"], 1)
        self.assertEqual(diagnostics["post_score_gap_reprocessed_document_ids"], ("DOC-A",))
        self.assertEqual(
            diagnostics["post_score_gap_progress_reason"],
            "score_gap_reprocessed_existing_documents",
        )
        self.assertEqual(
            _score_gap_state_repeated_rejection_reasons(diagnostics),
            ("score_gap_state_repeated", "score_gap_reprocessed_existing_documents"),
        )

    def test_score_gap_progress_diagnostics_explain_accepted_mapping_without_score_state_change(self):
        previous = AgenticEvidenceRuntimeTrace(
            status="completed",
            document_ids=("DOC-A",),
            claim_ids=("CLM-A",),
            mapping_ids=("MAP-A",),
            primitive_states=(
                PrimitiveStateV2(
                    "customer_preorder_or_allocation",
                    PrimitiveStatus.PRESENT_CURRENT,
                    support_claim_ids=("CLM-A",),
                ),
                PrimitiveStateV2(
                    "qualification_status",
                    PrimitiveStatus.UNKNOWN,
                    materiality_remaining_points=8.0,
                ),
            ),
        )
        current = AgenticEvidenceRuntimeTrace(
            status="completed",
            document_ids=("DOC-B",),
            claim_ids=("CLM-B",),
            mapping_ids=("MAP-B",),
            skipped_existing_document_count=1,
            primitive_states=(
                PrimitiveStateV2(
                    "customer_preorder_or_allocation",
                    PrimitiveStatus.PRESENT_CURRENT,
                    support_claim_ids=("CLM-B",),
                ),
                PrimitiveStateV2(
                    "qualification_status",
                    PrimitiveStatus.UNKNOWN,
                    materiality_remaining_points=8.0,
                ),
            ),
        )
        merged = AgenticEvidenceRuntimeTrace(
            status="completed",
            document_ids=("DOC-A", "DOC-B"),
            claim_ids=("CLM-A", "CLM-B"),
            mapping_ids=("MAP-A", "MAP-B"),
            skipped_existing_document_count=1,
            primitive_states=(
                PrimitiveStateV2(
                    "customer_preorder_or_allocation",
                    PrimitiveStatus.PRESENT_CURRENT,
                    support_claim_ids=("CLM-A", "CLM-B"),
                ),
                PrimitiveStateV2(
                    "qualification_status",
                    PrimitiveStatus.UNKNOWN,
                    materiality_remaining_points=8.0,
                ),
            ),
        )

        diagnostics = _score_gap_progress_diagnostics(
            previous_trace=previous,
            current_trace=current,
            merged_trace=merged,
            previous_signature=("total=0", "gap=qualification_status"),
            current_signature=("total=0", "gap=qualification_status"),
            previous_score_contributions=(
                ScoreContributionV2.build(
                    component_key="earnings_visibility",
                    criterion_id="agentic_v2_rubric_earnings_visibility",
                    raw_points=0.0,
                    max_points=20.0,
                    support_claim_ids=(),
                    cap_reason="qualification_status:primitive_status:UNKNOWN",
                ),
            ),
            current_score_contributions=(
                ScoreContributionV2.build(
                    component_key="earnings_visibility",
                    criterion_id="agentic_v2_rubric_earnings_visibility",
                    raw_points=0.0,
                    max_points=20.0,
                    support_claim_ids=(),
                    cap_reason="qualification_status:primitive_status:UNKNOWN",
                ),
            ),
        )

        self.assertEqual(
            diagnostics["post_score_gap_progress_reason"],
            "score_gap_evidence_progress_without_score_state_change",
        )
        self.assertFalse(diagnostics["post_score_gap_score_state_changed"])
        self.assertTrue(diagnostics["post_score_gap_primitive_state_changed"])
        self.assertEqual(diagnostics["post_score_gap_new_accepted_mapping_ids"], ("MAP-B",))
        self.assertEqual(
            diagnostics["post_score_gap_primitive_delta_summaries"],
            (
                "customer_preorder_or_allocation:PRESENT_CURRENT->PRESENT_CURRENT; "
                "support+=CLM-B",
            ),
        )
        self.assertEqual(
            diagnostics["post_score_gap_unchanged_gap_primitive_summaries"],
            ("qualification_status:UNKNOWN; support=0; counter=0; materiality=8.0",),
        )
        self.assertFalse(diagnostics["post_score_gap_score_contribution_changed"])
        self.assertEqual(diagnostics["post_score_gap_score_contribution_delta_summaries"], ())

    def test_score_gap_progress_diagnostics_uses_contract_materiality_for_unchanged_gaps(self):
        previous = AgenticEvidenceRuntimeTrace(
            status="completed",
            primitive_states=(
                PrimitiveStateV2("hbm_capacity_pre_sold", PrimitiveStatus.UNKNOWN),
                PrimitiveStateV2("qualification_status", PrimitiveStatus.UNKNOWN),
            ),
        )
        current = AgenticEvidenceRuntimeTrace(
            status="completed",
            primitive_states=(
                PrimitiveStateV2("hbm_capacity_pre_sold", PrimitiveStatus.UNKNOWN),
                PrimitiveStateV2("qualification_status", PrimitiveStatus.UNKNOWN),
            ),
        )

        diagnostics = _score_gap_progress_diagnostics(
            previous_trace=previous,
            current_trace=current,
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            previous_signature=("total=70", "gap=hbm_capacity_pre_sold"),
            current_signature=("total=70", "gap=hbm_capacity_pre_sold"),
        )

        summaries = diagnostics["post_score_gap_unchanged_gap_primitive_summaries"]
        self.assertIn(
            "hbm_capacity_pre_sold:UNKNOWN; support=0; counter=0; materiality=5.0",
            summaries,
        )
        self.assertIn(
            "qualification_status:UNKNOWN; support=0; counter=0; materiality=0.0",
            summaries,
        )

    def test_score_gap_progress_diagnostics_report_score_contribution_delta(self):
        diagnostics = _score_gap_progress_diagnostics(
            previous_trace=AgenticEvidenceRuntimeTrace(status="completed"),
            current_trace=AgenticEvidenceRuntimeTrace(status="completed"),
            previous_signature=("total=0",),
            current_signature=("total=10",),
            previous_score_contributions=(
                ScoreContributionV2.build(
                    component_key="earnings_visibility",
                    criterion_id="agentic_v2_rubric_earnings_visibility",
                    raw_points=0.0,
                    max_points=20.0,
                    support_claim_ids=(),
                    cap_reason="qualification_status:primitive_status:UNKNOWN",
                ),
            ),
            current_score_contributions=(
                ScoreContributionV2.build(
                    component_key="earnings_visibility",
                    criterion_id="agentic_v2_rubric_earnings_visibility",
                    raw_points=10.0,
                    max_points=20.0,
                    support_claim_ids=("CLM-B",),
                ),
            ),
        )

        self.assertTrue(diagnostics["post_score_gap_score_state_changed"])
        self.assertTrue(diagnostics["post_score_gap_score_contribution_changed"])
        self.assertEqual(
            diagnostics["post_score_gap_score_contribution_delta_summaries"],
            (
                "earnings_visibility/agentic_v2_rubric_earnings_visibility:raw=0.0->10.0; "
                "support+=CLM-B; cap=qualification_status:primitive_status:UNKNOWN->none",
            ),
        )

    def test_score_gap_audit_event_records_round_delta_artifact(self):
        progress = {
            "post_score_gap_progress_reason": "score_gap_changed_score_state",
            "post_score_gap_score_state_changed": True,
            "post_score_gap_new_document_ids": ("DOC-B",),
            "post_score_gap_new_claim_ids": ("CLM-B",),
            "post_score_gap_new_accepted_mapping_ids": ("MAP-B",),
            "post_score_gap_primitive_state_changed": True,
            "post_score_gap_primitive_delta_summaries": (
                "qualification_status:UNKNOWN->PRESENT_CURRENT; support+=CLM-B",
            ),
            "post_score_gap_unchanged_gap_primitive_summaries": (),
            "post_score_gap_score_contribution_changed": True,
            "post_score_gap_score_contribution_delta_summaries": (
                "earnings_visibility/agentic_v2_rubric_earnings_visibility:raw=0.0->10.0; support+=CLM-B",
            ),
        }

        event = _score_gap_audit_event(
            inputs=FreeWebResearchInput(
                company_name="삼성전자",
                symbol="005930",
                sector=None,
                market=Market.KR,
                as_of_date=date(2026, 6, 26),
            ),
            round_index=1,
            expansion=_ScoreGapExpansionResult(
                status="executed",
                queries_run=("삼성전자 HBM qualification",),
                unresolved_gaps=("agentic primitive gap:qualification_status; status:UNKNOWN",),
            ),
            progress_diagnostics=progress,
            previous_signature=("total=0", "gap=qualification_status"),
            current_signature=("total=10",),
        )

        self.assertTrue(str(event["event_id"]).startswith("SGAUD-"))
        self.assertEqual(event["symbol"], "005930")
        self.assertEqual(event["round_index"], 1)
        self.assertEqual(event["progress_reason"], "score_gap_changed_score_state")
        self.assertEqual(event["new_claim_ids"], ("CLM-B",))
        self.assertIn("support+=CLM-B", event["primitive_delta_summaries"][0])
        self.assertIn("raw=0.0->10.0", event["score_contribution_delta_summaries"][0])
        self.assertNotEqual(event["previous_score_gap_signature_hash"], event["current_score_gap_signature_hash"])

    def test_agentic_score_contribution_diagnostics_explain_caps_and_support(self):
        contributions = (
            ScoreContributionV2.build(
                component_key="earnings_visibility",
                criterion_id="agentic_v2_rubric_earnings_visibility",
                raw_points=0.0,
                max_points=20.0,
                support_claim_ids=(),
                cap_reason="qualification_status:primitive_status:UNKNOWN",
            ),
            ScoreContributionV2.build(
                component_key="bottleneck_pricing",
                criterion_id="agentic_v2_rubric_bottleneck_pricing",
                raw_points=10.0,
                max_points=20.0,
                support_claim_ids=("CLM-SUPPORT",),
            ),
        )

        diagnostics = _agentic_score_contribution_diagnostics(contributions)

        self.assertEqual(diagnostics["agentic_score_contribution_v2_count"], 2)
        self.assertEqual(diagnostics["agentic_score_contribution_v2_nonzero_count"], 1)
        self.assertEqual(
            diagnostics["agentic_score_contribution_v2_cap_summaries"],
            (
                "earnings_visibility/agentic_v2_rubric_earnings_visibility:raw=0.0; "
                "cap=qualification_status:primitive_status:UNKNOWN",
            ),
        )
        self.assertEqual(
            diagnostics["agentic_score_contribution_v2_support_summaries"],
            (
                "bottleneck_pricing/agentic_v2_rubric_bottleneck_pricing:raw=10.0; "
                "claims=CLM-SUPPORT",
            ),
        )

    def test_agentic_score_contributions_use_trace_archetype_over_feature_fallback(self):
        trace = AgenticEvidenceRuntimeTrace(
            status="completed",
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            primitive_states=(
                PrimitiveStateV2(
                    primitive_id="customer_preorder_or_allocation",
                    status=PrimitiveStatus.PRESENT_CURRENT,
                    support_claim_ids=("CLM-C06-CUSTOMER",),
                    support_mapping_ids=("MAP-C06-CUSTOMER",),
                    support_source_family_ids=("SRC-C06-CUSTOMER",),
                ),
                PrimitiveStateV2(
                    primitive_id="hbm_capacity_pre_sold",
                    status=PrimitiveStatus.PRESENT_CURRENT,
                    support_claim_ids=("CLM-C06-CAPACITY",),
                    support_mapping_ids=("MAP-C06-CAPACITY",),
                    support_source_family_ids=("SRC-C06-CAPACITY",),
                ),
                PrimitiveStateV2(
                    primitive_id="revenue_visibility_contract",
                    status=PrimitiveStatus.PRESENT_CURRENT,
                    support_claim_ids=("CLM-C06-REVENUE",),
                    support_mapping_ids=("MAP-C06-REVENUE",),
                    support_source_family_ids=("SRC-C06-REVENUE",),
                ),
            ),
        )

        rubric_archetype = _agentic_score_contribution_archetype_id(
            "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
            trace,
        )
        contributions = _agentic_score_contributions_from_trace(
            components={
                "eps_fcf_explosion": 20.0,
                "earnings_visibility": 20.0,
                "bottleneck_pricing": 20.0,
                "market_mispricing": 15.0,
                "valuation_rerating": 15.0,
                "capital_allocation": 5.0,
                "information_confidence": 5.0,
            },
            canonical_archetype_id=rubric_archetype,
            trace=trace,
        )

        self.assertEqual(rubric_archetype, "C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertTrue(any(item.raw_points > 0.0 for item in contributions))
        cap_reasons = " ".join(str(item.cap_reason or "") for item in contributions)
        self.assertNotIn("roe:primitive_missing_from_state", cap_reasons)
        self.assertTrue(
            any("CLM-C06-CUSTOMER" in item.support_claim_ids for item in contributions)
        )

    def test_agentic_score_contribution_quarantines_legacy_parser_score_audit_count(self):
        trace = AgenticEvidenceRuntimeTrace(
            status="completed",
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            primitive_states=(
                PrimitiveStateV2(
                    primitive_id="customer_preorder_or_allocation",
                    status=PrimitiveStatus.PRESENT_CURRENT,
                    support_claim_ids=("CLM-C06-CUSTOMER",),
                    support_mapping_ids=("MAP-C06-CUSTOMER",),
                    support_source_family_ids=("SRC-C06-CUSTOMER",),
                ),
                PrimitiveStateV2(
                    primitive_id="hbm_capacity_pre_sold",
                    status=PrimitiveStatus.PRESENT_CURRENT,
                    support_claim_ids=("CLM-C06-CAPACITY",),
                    support_mapping_ids=("MAP-C06-CAPACITY",),
                    support_source_family_ids=("SRC-C06-CAPACITY",),
                ),
            ),
        )
        feature_result = FeatureEngineeringResult(
            payload=ScoringPayload(
                symbol="005930",
                as_of_date=date(2026, 6, 28),
                components={
                    "eps_fcf_explosion": 20.0,
                    "earnings_visibility": 20.0,
                    "bottleneck_pricing": 20.0,
                    "market_mispricing": 15.0,
                    "valuation_rerating": 15.0,
                    "capital_allocation": 5.0,
                    "information_confidence": 5.0,
                },
                diagnostic_scores={
                    "score_valid": 100.0,
                    "legacy_parser_score_claim_without_v2_count_capped": 7.0,
                },
                canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            ),
            industrial_sub_scores=None,
            shortage_type=None,
            red_team_signals=None,
            source_fields={
                "legacy_parser_score_claim_fields_without_v2": "hbm_capacity_pre_sold,customer_preorder_or_allocation",
            },
        )

        updated = _with_agentic_score_contributions(feature_result, trace)

        self.assertEqual(updated.payload.diagnostic_scores["legacy_parser_score_claim_without_v2_count_capped"], 0.0)
        self.assertEqual(
            updated.payload.diagnostic_scores["legacy_parser_score_claim_without_v2_quarantined_count_capped"],
            7.0,
        )
        self.assertEqual(
            updated.source_fields["legacy_parser_score_claim_fields_quarantined_by_v2"],
            "hbm_capacity_pre_sold,customer_preorder_or_allocation",
        )
        self.assertEqual(updated.source_fields["legacy_parser_score_claim_fields_without_v2"], "")
        self.assertGreater(len(updated.payload.score_contributions_v2), 0)

    def test_score_gap_expansion_does_not_stop_just_because_total_score_is_high(self):
        inputs = FreeWebResearchInput(
            company_name="테스트고점수",
            symbol="888888",
            sector="software",
            market=Market.KR,
            as_of_date=date(2026, 6, 8),
            theme_rebalance_enabled=True,
            theme_route_provider=FakeThemeRouteProvider(outputs=(ThemeRouteOutput(status="no_transition"),)),
            theme_evidence_review_enabled=True,
        )
        score = ScoreSnapshot(
            symbol="888888",
            as_of_date=date(2026, 6, 8),
            eps_fcf_explosion_score=20.0,
            earnings_visibility_score=20.0,
            bottleneck_pricing_score=20.0,
            market_mispricing_score=15.0,
            valuation_rerating_score=15.0,
            capital_allocation_score=5.0,
            information_confidence_score=5.0,
            risk_penalty=0.0,
            total_score=99.0,
            diagnostic_scores={"revision_score": 0.0},
        )

        self.assertTrue(_post_score_gap_expansion_allowed(inputs, score))

    def test_score_gap_expansion_is_not_disabled_by_query_budget_object(self):
        inputs = FreeWebResearchInput(
            company_name="테스트예산",
            symbol="888887",
            sector="software",
            market=Market.KR,
            as_of_date=date(2026, 6, 8),
            budget=SearchBudget(max_total_queries_per_day=1, max_queries_per_symbol=1),
            theme_rebalance_enabled=True,
            theme_route_provider=FakeThemeRouteProvider(outputs=(ThemeRouteOutput(status="no_transition"),)),
            theme_evidence_review_enabled=True,
        )
        score = ScoreSnapshot(
            symbol="888887",
            as_of_date=date(2026, 6, 8),
            eps_fcf_explosion_score=20.0,
            earnings_visibility_score=20.0,
            bottleneck_pricing_score=20.0,
            market_mispricing_score=15.0,
            valuation_rerating_score=15.0,
            capital_allocation_score=5.0,
            information_confidence_score=5.0,
            risk_penalty=0.0,
            total_score=99.0,
            diagnostic_scores={"revision_score": 0.0},
        )

        self.assertTrue(_post_score_gap_expansion_allowed(inputs, score))

    def test_score_gap_context_includes_fcf_valuation_and_evidence_family_gaps(self):
        score = ScoreSnapshot(
            symbol="888889",
            as_of_date=date(2026, 6, 8),
            eps_fcf_explosion_score=20.0,
            earnings_visibility_score=20.0,
            bottleneck_pricing_score=20.0,
            market_mispricing_score=15.0,
            valuation_rerating_score=15.0,
            capital_allocation_score=5.0,
            information_confidence_score=5.0,
            risk_penalty=0.0,
            total_score=90.0,
            diagnostic_scores={
                "revision_score": 100.0,
                "structural_visibility_quality": 100.0,
                "contract_quality": 100.0,
                "backlog_rpo_visibility": 100.0,
                "capa_constraint": 100.0,
                "asp_pricing_power": 100.0,
                "actual_profit_conversion_score": 80.0,
                "sector_visibility_score": 80.0,
                "sector_bottleneck_score": 80.0,
                "medium_term_revision_visibility": 80.0,
                "fcf_quality_score": 20.0,
                "valuation_score": 20.0,
                "domain_specific_evidence_score": 20.0,
                "evidence_family_price": 0.0,
                "evidence_family_financial_actual": 0.0,
                "evidence_family_disclosure": 0.0,
                "evidence_family_research_report": 0.0,
                "evidence_family_consensus": 0.0,
                "evidence_family_consensus_proxy": 0.0,
                "evidence_family_consensus_revision": 0.0,
                "evidence_family_consensus_revision_proxy": 0.0,
                "evidence_family_news": 0.0,
                "evidence_family_search_snippet_news": 0.0,
                "estimate_missing_revision_source": 100.0,
                "estimate_missing_fcf_source": 100.0,
            },
        )

        gaps = _score_gap_missing_information(score)

        self.assertTrue(any("selected_revision_source_missing" in item for item in gaps))
        self.assertTrue(any("selected_fcf_source_missing" in item for item in gaps))
        self.assertTrue(any("FCF conversion" in item for item in gaps))
        self.assertTrue(any("valuation PER PBR" in item for item in gaps))
        self.assertTrue(any("domain-specific operating KPI" in item for item in gaps))
        self.assertTrue(any("inventory receivables" in item for item in gaps))
        self.assertTrue(any("consensus revision EPS OP FCF" in item for item in gaps))

    def test_score_gap_missing_information_does_not_treat_consensus_proxy_as_independent_family(self):
        score = ScoreSnapshot(
            symbol="999997",
            as_of_date=date(2026, 6, 8),
            eps_fcf_explosion_score=20.0,
            earnings_visibility_score=20.0,
            bottleneck_pricing_score=20.0,
            market_mispricing_score=15.0,
            valuation_rerating_score=15.0,
            capital_allocation_score=5.0,
            information_confidence_score=5.0,
            risk_penalty=0.0,
            total_score=90.0,
            diagnostic_scores={
                "revision_score": 100.0,
                "structural_visibility_quality": 100.0,
                "contract_quality": 100.0,
                "backlog_rpo_visibility": 100.0,
                "capa_constraint": 100.0,
                "asp_pricing_power": 100.0,
                "actual_profit_conversion_score": 100.0,
                "fcf_quality_score": 100.0,
                "valuation_score": 100.0,
                "domain_specific_evidence_score": 100.0,
                "medium_term_revision_visibility": 100.0,
                "sector_visibility_score": 100.0,
                "sector_bottleneck_score": 100.0,
                "evidence_family_price": 1.0,
                "evidence_family_financial_actual": 1.0,
                "evidence_family_disclosure": 1.0,
                "evidence_family_research_report": 1.0,
                "evidence_family_consensus": 0.0,
                "evidence_family_consensus_proxy": 1.0,
                "evidence_family_consensus_revision": 0.0,
                "evidence_family_consensus_revision_proxy": 1.0,
                "evidence_family_news": 1.0,
            },
        )

        gaps = _score_gap_missing_information(score)

        self.assertTrue(any("consensus FY1 FY2" in item for item in gaps))
        self.assertTrue(any("consensus revision EPS OP FCF" in item for item in gaps))

    def test_independent_evidence_family_gap_is_material_when_llm_cannot_expand(self):
        inputs = FreeWebResearchInput(
            company_name="테스트증거부족",
            symbol="888887",
            sector="software",
            market=Market.KR,
            as_of_date=date(2026, 6, 8),
            theme_rebalance_enabled=True,
            theme_route_provider=FakeThemeRouteProvider(outputs=(ThemeRouteOutput(status="no_transition"),)),
        )
        gap = "missing independent evidence families for stage gate: research_report, consensus_revision; expand source-backed evidence for these families"
        expansion = _ScoreGapExpansionResult(
            status="llm_no_suggested_queries",
            unresolved_gaps=(gap,),
            rejection_reasons=("llm_returned_no_suggested_queries",),
        )

        self.assertEqual(_material_score_gaps((gap,)), (gap,))
        self.assertEqual(
            _score_gap_score_block_reason(inputs=inputs, expansion=expansion),
            "score_gap_llm_no_suggested_queries",
        )

        round_limit = _ScoreGapExpansionResult(
            status="round_limit_reached",
            unresolved_gaps=(gap,),
            rejection_reasons=("max_score_gap_expansion_rounds_reached",),
        )
        self.assertEqual(
            _score_gap_score_block_reason(inputs=inputs, expansion=round_limit, queries_run_count=0),
            "score_gap_round_limit",
        )
        self.assertEqual(
            _score_gap_score_block_reason(inputs=inputs, expansion=round_limit, queries_run_count=1),
            "score_gap_round_limit",
        )

        provider_error = _ScoreGapExpansionResult(
            status="provider_error",
            unresolved_gaps=(gap,),
            blocked_reason="codex_cli_timeout",
        )
        self.assertEqual(
            _score_gap_score_block_reason(inputs=inputs, expansion=provider_error, queries_run_count=0),
            "score_gap_provider_error",
        )

        agentic_no_executable = _ScoreGapExpansionResult(
            status="agentic_follow_up_no_executable_searches",
            unresolved_gaps=(gap,),
            rejection_reasons=("future_query_rejected",),
        )
        self.assertEqual(
            _score_gap_score_block_reason(inputs=inputs, expansion=agentic_no_executable, queries_run_count=0),
            "score_gap_no_executable_searches",
        )

        agentic_no_queries = _ScoreGapExpansionResult(
            status="agentic_follow_up_no_suggested_queries",
            unresolved_gaps=(gap,),
            rejection_reasons=("agentic_follow_up_no_suggested_queries",),
        )
        self.assertEqual(
            _score_gap_score_block_reason(inputs=inputs, expansion=agentic_no_queries, queries_run_count=0),
            "score_gap_llm_no_suggested_queries",
        )

        no_progress_with_evidence_delta = _ScoreGapExpansionResult(
            status="no_progress",
            unresolved_gaps=(gap,),
            rejection_reasons=(
                "score_gap_state_repeated",
                "score_gap_evidence_progress_without_score_state_change",
            ),
            diagnostic_details={
                "post_score_gap_progress_reason": "score_gap_evidence_progress_without_score_state_change",
                "post_score_gap_score_state_changed": False,
                "post_score_gap_primitive_state_changed": True,
                "post_score_gap_score_contribution_changed": True,
            },
        )
        self.assertEqual(
            _score_gap_score_block_reason(
                inputs=inputs,
                expansion=no_progress_with_evidence_delta,
                queries_run_count=1,
            ),
            "score_gap_material_gaps_pending",
        )

    def test_stage_gate_failures_are_returned_as_llm_gap_context(self):
        score = ScoreSnapshot(
            symbol="888886",
            as_of_date=date(2026, 6, 8),
            eps_fcf_explosion_score=20.0,
            earnings_visibility_score=20.0,
            bottleneck_pricing_score=20.0,
            market_mispricing_score=15.0,
            valuation_rerating_score=15.0,
            capital_allocation_score=5.0,
            information_confidence_score=5.0,
            risk_penalty=0.0,
            total_score=95.0,
            diagnostic_scores={
                "score_valid": 100.0,
                "revision_score": 0.0,
                "structural_visibility_quality": 100.0,
                "contract_quality": 100.0,
                "report_date_confidence": 100.0,
            },
        )

        gaps = _stage_gate_missing_information(score, RedTeamAssessment.empty("888886", date(2026, 6, 8)))

        self.assertTrue(any("failed_stage3_revision" in item for item in gaps))
        self.assertTrue(any("consensus revision" in item for item in gaps))
        self.assertTrue(any("missing independent evidence families" in item for item in gaps))

    def test_evidence_contract_stage_gate_failures_are_material_llm_gap_context(self):
        green_gate_score = ScoreSnapshot(
            symbol="888884",
            as_of_date=date(2026, 6, 8),
            eps_fcf_explosion_score=20.0,
            earnings_visibility_score=20.0,
            bottleneck_pricing_score=20.0,
            market_mispricing_score=15.0,
            valuation_rerating_score=15.0,
            capital_allocation_score=5.0,
            information_confidence_score=5.0,
            risk_penalty=0.0,
            total_score=95.0,
            diagnostic_scores={
                "score_valid": 100.0,
                "revision_score": 100.0,
                "structural_visibility_quality": 100.0,
                "contract_quality": 100.0,
                "cross_evidence_family_count": 4.0,
                "report_date_confidence": 100.0,
                "date_unverified_snippet_news_count_capped": 0.0,
                "date_unverified_document_count_capped": 0.0,
                "domain_specific_evidence_score": 100.0,
                "evidence_contract_green_gate_required_primitive_count_capped": 3.0,
                "evidence_contract_green_gate_present_primitive_count_capped": 2.0,
                "evidence_contract_green_gate_missing_primitive_count_capped": 1.0,
                "evidence_contract_green_gate_coverage_pct": 66.6667,
            },
        )
        guard_score = ScoreSnapshot(
            symbol="888883",
            as_of_date=date(2026, 6, 8),
            eps_fcf_explosion_score=20.0,
            earnings_visibility_score=20.0,
            bottleneck_pricing_score=20.0,
            market_mispricing_score=15.0,
            valuation_rerating_score=15.0,
            capital_allocation_score=5.0,
            information_confidence_score=5.0,
            risk_penalty=0.0,
            total_score=95.0,
            diagnostic_scores={
                "score_valid": 100.0,
                "revision_score": 100.0,
                "structural_visibility_quality": 100.0,
                "contract_quality": 100.0,
                "cross_evidence_family_count": 4.0,
                "report_date_confidence": 100.0,
                "date_unverified_snippet_news_count_capped": 0.0,
                "date_unverified_document_count_capped": 0.0,
                "domain_specific_evidence_score": 100.0,
                "evidence_contract_green_gate_required_primitive_count_capped": 3.0,
                "evidence_contract_green_gate_present_primitive_count_capped": 3.0,
                "evidence_contract_green_gate_missing_primitive_count_capped": 0.0,
                "evidence_contract_green_gate_coverage_pct": 100.0,
                "evidence_contract_guard_present_primitive_count_capped": 1.0,
            },
        )
        guard_unverified_score = ScoreSnapshot(
            symbol="888881",
            as_of_date=date(2026, 6, 8),
            eps_fcf_explosion_score=20.0,
            earnings_visibility_score=20.0,
            bottleneck_pricing_score=20.0,
            market_mispricing_score=15.0,
            valuation_rerating_score=15.0,
            capital_allocation_score=5.0,
            information_confidence_score=5.0,
            risk_penalty=0.0,
            total_score=95.0,
            diagnostic_scores={
                "score_valid": 100.0,
                "revision_score": 100.0,
                "structural_visibility_quality": 100.0,
                "contract_quality": 100.0,
                "cross_evidence_family_count": 4.0,
                "report_date_confidence": 100.0,
                "date_unverified_snippet_news_count_capped": 0.0,
                "date_unverified_document_count_capped": 0.0,
                "domain_specific_evidence_score": 100.0,
                "evidence_contract_guard_required_primitive_count_capped": 1.0,
                "evidence_contract_guard_missing_primitive_count_capped": 1.0,
            },
        )

        green_gate_gaps = _stage_gate_missing_information(
            green_gate_score,
            RedTeamAssessment.empty("888884", date(2026, 6, 8)),
        )
        guard_gaps = _stage_gate_missing_information(
            guard_score,
            RedTeamAssessment.empty("888883", date(2026, 6, 8)),
        )
        guard_unverified_gaps = _stage_gate_missing_information(
            guard_unverified_score,
            RedTeamAssessment.empty("888881", date(2026, 6, 8)),
        )

        self.assertTrue(any("failed_evidence_contract_positive_coverage" in item for item in green_gate_gaps))
        self.assertTrue(any("evidence contract Green gate primitive coverage failed" in item for item in green_gate_gaps))
        self.assertTrue(any("failed_evidence_contract_guard_present" in item for item in guard_gaps))
        self.assertTrue(any("evidence contract guard primitive is present" in item for item in guard_gaps))
        self.assertTrue(any("failed_evidence_contract_guard_unverified" in item for item in guard_unverified_gaps))
        self.assertTrue(any("evidence contract guard primitive is missing or unverified" in item for item in guard_unverified_gaps))
        self.assertTrue(_material_score_gaps(green_gate_gaps))
        self.assertTrue(_material_score_gaps(guard_gaps))
        self.assertTrue(_material_score_gaps(guard_unverified_gaps))

    def test_score_gap_no_progress_signature_tracks_contract_primitive_names(self):
        score = ScoreSnapshot(
            symbol="888882",
            as_of_date=date(2026, 6, 8),
            eps_fcf_explosion_score=20.0,
            earnings_visibility_score=20.0,
            bottleneck_pricing_score=20.0,
            market_mispricing_score=15.0,
            valuation_rerating_score=15.0,
            capital_allocation_score=5.0,
            information_confidence_score=5.0,
            risk_penalty=0.0,
            total_score=95.0,
            diagnostic_scores={
                "score_valid": 100.0,
                "revision_score": 100.0,
                "structural_visibility_quality": 100.0,
                "contract_quality": 100.0,
                "cross_evidence_family_count": 4.0,
                "report_date_confidence": 100.0,
                "date_unverified_snippet_news_count_capped": 0.0,
                "date_unverified_document_count_capped": 0.0,
                "domain_specific_evidence_score": 100.0,
                "evidence_contract_green_gate_required_primitive_count_capped": 3.0,
                "evidence_contract_green_gate_present_primitive_count_capped": 2.0,
                "evidence_contract_green_gate_missing_primitive_count_capped": 1.0,
                "evidence_contract_green_gate_coverage_pct": 66.6667,
            },
        )
        red_team = RedTeamAssessment.empty("888882", date(2026, 6, 8))
        before = {
            "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            "evidence_contract_required_primitives": "hbm_capacity_pre_sold,customer_preorder_or_allocation,hbm_capacity_constraint",
            "evidence_contract_positive_missing_primitives": "hbm_capacity_pre_sold",
            "evidence_contract_green_gate_missing_primitives": "hbm_capacity_pre_sold",
        }
        after = {
            **before,
            "evidence_contract_positive_missing_primitives": "customer_preorder_or_allocation",
            "evidence_contract_green_gate_missing_primitives": "customer_preorder_or_allocation",
        }

        self.assertNotEqual(
            _score_gap_state_signature(score, red_team, before),
            _score_gap_state_signature(score, red_team, after),
        )

    def test_price_only_and_emerging_theme_guards_are_returned_as_llm_gap_context(self):
        score = ScoreSnapshot(
            symbol="888885",
            as_of_date=date(2026, 6, 8),
            eps_fcf_explosion_score=20.0,
            earnings_visibility_score=20.0,
            bottleneck_pricing_score=20.0,
            market_mispricing_score=15.0,
            valuation_rerating_score=15.0,
            capital_allocation_score=5.0,
            information_confidence_score=5.0,
            risk_penalty=0.0,
            total_score=95.0,
            diagnostic_scores={
                "score_valid": 100.0,
                "revision_score": 90.0,
                "structural_visibility_quality": 90.0,
                "contract_quality": 90.0,
                "price_only_blowoff_score": 80.0,
                "snippet_only_green_block": 100.0,
                "emerging_theme_active": 100.0,
                "llm_deep_research_completed": 0.0,
                "green_unlock_evidence_score": 0.0,
                "date_unverified_snippet_news_count_capped": 1.0,
            },
        )

        gaps = tuple(
            dict.fromkeys(
                (
                    *_score_gap_missing_information(score),
                    *_stage_gate_missing_information(score, RedTeamAssessment.empty("888885", date(2026, 6, 8))),
                )
            )
        )

        self.assertTrue(any("price-only blowoff" in item for item in gaps))
        self.assertTrue(any("failed_positive_stage_price_only_blowoff" in item for item in gaps))
        self.assertTrue(any("snippet-only" in item for item in gaps))
        self.assertTrue(any("emerging-theme deep research" in item for item in gaps))
        self.assertTrue(any("Green unlock" in item for item in gaps))

    def test_theme_route_canonical_is_applied_to_scoring_without_keyword_hardcode(self):
        url = "https://news.example.com/company-route-noise"
        route_ref = stable_news_evidence_id(
            symbol="000001",
            published_date=date(2026, 6, 8),
            source="fixture-news",
            source_url=url,
            title="테스트기업 실적 회복과 시장 관련기사",
        )
        route_provider = FakeThemeRouteProvider(
            output=ThemeRouteOutput(
                status="transition_detected",
                transition_detected=True,
                route_confidence=0.82,
                large_sector_id="L9_MOBILITY_TRANSPORT_LEISURE",
                canonical_archetype_id="C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
                evidence_slots=(
                    EvidenceSlotStatus(
                        slot="route_basis",
                        status="present",
                        evidence_refs=(route_ref,),
                        confidence=0.8,
                    ),
                ),
            )
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "테스트기업 데이터센터 수주": (
                    SearchResult(
                        title="테스트기업 실적 회복과 시장 관련기사",
                        url=url,
                        snippet="본문은 테스트기업 사업 회복, 하단에는 SK하이닉스 HBM 메모리 기사",
                        source="fixture-news",
                        query="테스트기업 데이터센터 수주",
                        confidence=0.8,
                    ),
                )
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트기업",
                symbol="000001",
                sector=None,
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={
                    url: (
                        "테스트기업은 본업 실적 회복을 보도했다.\n"
                        "관련기사: SK하이닉스 HBM 메모리 공급부족과 엔비디아 수요."
                    )
                },
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
            )
        )

        self.assertEqual(result.feature_input.canonical_archetype_id, "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE")
        self.assertEqual(result.feature_result.source_fields["canonical_archetype_id"], "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE")
        self.assertEqual(result.score.diagnostic_scores["theme_route_applied_to_scoring"], 100.0)

    def test_theme_route_semiconductor_alias_is_normalized_before_scoring(self):
        url = "https://news.example.com/hbm-alias-route"
        route_ref = stable_news_evidence_id(
            symbol="000660",
            published_date=date(2026, 5, 14),
            source="fixture-news",
            source_url=url,
            title="SK하이닉스 HBM 엔비디아 공급 확대",
        )
        route_provider = FakeThemeRouteProvider(
            output=ThemeRouteOutput(
                status="transition_detected",
                transition_detected=True,
                route_confidence=0.86,
                large_sector_id="semiconductors",
                canonical_archetype_id="ai_hbm_structural_memory_supplier",
                evidence_slots=(
                    EvidenceSlotStatus(
                        slot="hbm_revenue_bridge",
                        status="present",
                        evidence_refs=(route_ref,),
                        confidence=0.8,
                    ),
                ),
                normalized_parsed_fields={"hbm_demand_mentioned": True},
            )
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "SK하이닉스 데이터센터 수주": (
                    SearchResult(
                        title="SK하이닉스 HBM 엔비디아 공급 확대",
                        url=url,
                        snippet="HBM 수요와 메모리 공급 확대",
                        source="fixture-news",
                        query="SK하이닉스 데이터센터 수주",
                        confidence=0.8,
                    ),
                )
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="SK하이닉스",
                symbol="000660",
                sector=None,
                market=Market.KR,
                as_of_date=date(2026, 5, 14),
                top_results=5,
                fixture_text_by_url={url: "SK하이닉스 HBM 수요와 메모리 공급 확대가 확인됐다."},
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
            )
        )

        self.assertEqual(result.feature_result.source_fields["large_sector_id"], "L2_AI_SEMICONDUCTOR_ELECTRONICS")
        self.assertEqual(result.feature_result.source_fields["canonical_archetype_id"], "C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertEqual(result.score.diagnostic_scores["theme_route_applied_to_scoring"], 100.0)

    def test_theme_route_canonical_without_source_backed_slot_is_not_applied_to_scoring(self):
        url = "https://news.example.com/company-route-no-source-slot"
        route_provider = FakeThemeRouteProvider(
            output=ThemeRouteOutput(
                status="transition_detected",
                transition_detected=True,
                route_confidence=0.82,
                large_sector_id="L9_MOBILITY_TRANSPORT_LEISURE",
                canonical_archetype_id="C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
                normalized_parsed_fields={"gpu_cloud_revenue_visible": True},
                missing_information=("route_basis_source_backed_evidence",),
            )
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "테스트기업 데이터센터 수주": (
                    SearchResult(
                        title="테스트기업 실적 회복과 시장 관련기사",
                        url=url,
                        snippet="본문은 테스트기업 사업 회복, 하단에는 SK하이닉스 HBM 메모리 기사",
                        source="fixture-news",
                        query="테스트기업 데이터센터 수주",
                        confidence=0.8,
                    ),
                )
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트기업",
                symbol="000001",
                sector=None,
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={
                    url: (
                        "테스트기업은 본업 실적 회복을 보도했다.\n"
                        "관련기사: SK하이닉스 HBM 메모리 공급부족과 엔비디아 수요."
                    )
                },
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
            )
        )

        self.assertIsNone(result.feature_input.canonical_archetype_id)
        self.assertEqual(result.feature_input.agent_extracted_fields, {})
        self.assertNotEqual(result.feature_result.source_fields["canonical_archetype_id"], "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE")
        self.assertEqual(result.theme_route.status, "needs_more_evidence")
        self.assertIsNone(result.theme_route_diagnostics["canonical_archetype_id"])
        self.assertEqual(result.theme_route_diagnostics["theme_evidence_gate_status"], "no_evidence_slots")
        self.assertEqual(result.score.diagnostic_scores["theme_route_applied_to_scoring"], 0.0)
        self.assertEqual(result.stage.stage, Stage.STAGE_0)
        self.assertFalse(result.theme_route_diagnostics["score_valid"])
        self.assertEqual(result.theme_route_diagnostics["score_blocked_reason"], "theme_route_needs_more_evidence")
        self.assertEqual(result.score.diagnostic_scores["score_blocked_by_theme_route"], 100.0)

    def test_source_backed_theme_route_normalized_fields_enter_feature_input(self):
        url = "https://news.example.com/naver-ai-cloud-source-backed"
        route_ref = stable_news_evidence_id(
            symbol="035420",
            published_date=date(2026, 6, 8),
            source="fixture-news",
            source_url=url,
            title="NAVER AI 데이터센터 협력",
        )
        route_provider = FakeThemeRouteProvider(
            output=ThemeRouteOutput(
                status="transition_detected",
                transition_detected=True,
                route_confidence=0.82,
                large_sector_id="L8_PLATFORM_CONTENT_SW_SECURITY",
                canonical_archetype_id="C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
                normalized_parsed_fields={
                    "gpu_cloud_revenue_visible": True,
                    "cloud_revenue_growth_visible": True,
                    "cloud_revenue_growth_pct": 40.0,
                    "unbacked_margin_bridge": True,
                },
                evidence_slots=(
                    EvidenceSlotStatus(
                        slot="cloud_revenue",
                        status="present",
                        evidence_refs=(route_ref,),
                        confidence=0.82,
                    ),
                ),
            )
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "NAVER 데이터센터 수주": (
                    SearchResult(
                        title="NAVER AI 데이터센터 협력",
                        url=url,
                        snippet="엔비디아 GPU 인프라 협력",
                        source="fixture-news",
                        query="NAVER 데이터센터 수주",
                        confidence=0.8,
                    ),
                )
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="NAVER",
                symbol="035420",
                sector="platform",
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={url: "NAVER는 엔비디아 GPU 데이터센터 협력을 발표했다."},
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
            )
        )

        self.assertTrue(result.feature_input.agent_extracted_fields["gpu_cloud_revenue_visible"])
        self.assertNotIn("unbacked_margin_bridge", result.feature_input.agent_extracted_fields)
        self.assertEqual(result.theme_route_diagnostics["theme_evidence_gate_status"], "source_backed")
        self.assertEqual(result.theme_route_diagnostics["agent_field_claim_ledger_version"], "e2r-claim-ledger-v1")
        self.assertIn("gpu_cloud_revenue_visible", result.theme_route_diagnostics["agent_field_claim_ids_by_primitive"])
        self.assertNotIn("unbacked_margin_bridge", result.theme_route_diagnostics["agent_field_claim_ids_by_primitive"])
        self.assertEqual(result.theme_route_diagnostics["agent_field_evidence_refs_by_field"]["gpu_cloud_revenue_visible"], (route_ref,))
        contract_context = result.theme_route_diagnostics["evidence_contract_gap_context"][0]
        self.assertIn("C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", contract_context)
        self.assertIn("arpu_growth_pct", contract_context)
        self.assertIn("operating_leverage_visible", contract_context)
        self.assertEqual(result.score.diagnostic_scores["theme_route_applied_to_scoring"], 100.0)
        self.assertGreater(result.score.diagnostic_scores["agent_extracted_field_count_capped"], 0.0)

    def test_source_backed_slot_matching_rejects_token_only_overlap(self):
        self.assertTrue(
            _field_matches_source_backed_slot(
                "cloud_revenue_growth_pct",
                ("cloud_revenue",),
            )
        )
        self.assertTrue(
            _field_matches_source_backed_slot(
                "customer_preorder_or_allocation",
                ("customer",),
            )
        )
        self.assertFalse(
            _field_matches_source_backed_slot(
                "unbacked_margin_bridge",
                ("margin_quality",),
            )
        )
        self.assertFalse(
            _field_matches_source_backed_slot(
                "cloud_revenue_growth_pct",
                ("revenue_cloud",),
            )
        )
        self.assertFalse(
            _field_matches_source_backed_slot(
                "margin",
                ("margin_quality",),
            )
        )

    def test_theme_route_contract_gap_context_marks_source_backed_primitives_present(self):
        route = ThemeRouteOutput(
            status="transition_detected",
            transition_detected=True,
            route_confidence=0.82,
            canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            normalized_parsed_fields={"hbm_capacity_pre_sold": True},
            evidence_slots=(
                EvidenceSlotStatus(
                    slot="hbm_capacity_pre_sold",
                    status="present",
                    evidence_refs=("news:000660:2024-04-25:reuters:hbm",),
                    confidence=0.9,
                ),
            ),
        )

        context = _theme_route_contract_gap_context(route)[0]
        missing = context.split("missing_positive_primitives=", 1)[1].split("; guard_primitives", 1)[0]

        self.assertIn("C06_HBM_MEMORY_CUSTOMER_CAPACITY", context)
        self.assertIn("customer_preorder_or_allocation", missing)
        self.assertNotIn("hbm_capacity_pre_sold", missing)

    def test_theme_route_contract_gap_context_ignores_unbacked_normalized_fields(self):
        route = ThemeRouteOutput(
            status="transition_detected",
            transition_detected=True,
            route_confidence=0.82,
            canonical_archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            normalized_parsed_fields={"hbm_capacity_pre_sold": True},
        )

        context = _theme_route_contract_gap_context(route)[0]
        missing = context.split("missing_positive_primitives=", 1)[1].split("; guard_primitives", 1)[0]

        self.assertIn("hbm_capacity_pre_sold", missing)

    def test_theme_route_contract_gap_context_covers_every_archetype(self):
        contracts = load_evidence_contracts()

        self.assertEqual(set(contracts), set(CANONICAL_ARCHETYPE_IDS))
        for canonical_archetype_id, contract in contracts.items():
            with self.subTest(canonical_archetype_id=canonical_archetype_id):
                context = _theme_route_contract_gap_context(
                    ThemeRouteOutput(
                        status="transition_detected",
                        transition_detected=True,
                        route_confidence=0.82,
                        canonical_archetype_id=canonical_archetype_id,
                    )
                )[0]

                missing_positive = context.split("missing_positive_primitives=", 1)[1].split(
                    "; missing_green_gate_primitives",
                    1,
                )[0]
                missing_green_gate = context.split("missing_green_gate_primitives=", 1)[1].split(
                    "; guard_primitives_to_check",
                    1,
                )[0]
                guard_context = context.split("guard_primitives_to_check=", 1)[1].split(
                    "; present_guard_primitives",
                    1,
                )[0]

                self.assertIn(f"archetype_evidence_contract:{canonical_archetype_id}", context)
                self.assertIn(f"bridge_group={contract.runtime_bridge_group}", context)
                for primitive in contract.required_primitives:
                    self.assertIn(primitive, context)
                for axis in contract.required_bridge_axes:
                    self.assertIn(axis, context)
                for primitive in contract.positive_primitives:
                    self.assertIn(primitive, missing_positive)
                if not contract.positive_primitives:
                    self.assertEqual(missing_positive, "none")
                for primitive in contract.green_gate_primitives:
                    self.assertIn(primitive, missing_green_gate)
                for primitive in contract.guard_primitives:
                    self.assertIn(primitive, guard_context)
                if not contract.guard_primitives:
                    self.assertEqual(guard_context, "none")

    def test_source_field_contract_gap_context_uses_resolved_runtime_archetype(self):
        context = _source_field_contract_gap_context(
            {
                "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
                "evidence_contract_runtime_bridge_group": "software_platform_recurring_revenue_bridge",
                "evidence_contract_required_primitives": "arr_growth_visible,nrr,retention_or_renewal,rpo_to_sales,recurring_margin_leverage",
                "evidence_contract_missing_primitives": "nrr,rpo_to_sales",
                "evidence_contract_positive_primitives": "arr_growth_visible,nrr,retention_or_renewal,rpo_to_sales,recurring_margin_leverage",
                "evidence_contract_positive_missing_primitives": "nrr,rpo_to_sales",
                "evidence_contract_guard_primitives": "",
                "evidence_contract_guard_present_primitives": "",
                "evidence_contract_required_bridge_axes": "software_retention,customer,margin",
            }
        )[0]

        self.assertIn("C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", context)
        self.assertIn("missing_required_primitives=nrr,rpo_to_sales", context)
        self.assertIn("missing_positive_primitives=nrr,rpo_to_sales", context)
        self.assertIn("guard_primitives_to_check=none", context)
        self.assertIn("required_bridge_axes=software_retention,customer,margin", context)

    def test_source_field_contract_gap_context_covers_every_archetype(self):
        contracts = load_evidence_contracts()

        for canonical_archetype_id, contract in contracts.items():
            with self.subTest(canonical_archetype_id=canonical_archetype_id):
                context = _source_field_contract_gap_context(
                    {
                        "canonical_archetype_id": canonical_archetype_id,
                        "evidence_contract_runtime_bridge_group": contract.runtime_bridge_group,
                        "evidence_contract_required_primitives": ",".join(contract.required_primitives),
                        "evidence_contract_missing_primitives": ",".join(contract.required_primitives),
                        "evidence_contract_positive_primitives": ",".join(contract.positive_primitives),
                        "evidence_contract_positive_missing_primitives": ",".join(contract.positive_primitives),
                        "evidence_contract_green_gate_primitives": ",".join(contract.green_gate_primitives),
                        "evidence_contract_green_gate_missing_primitives": ",".join(contract.green_gate_primitives),
                        "evidence_contract_guard_primitives": ",".join(contract.guard_primitives),
                        "evidence_contract_guard_present_primitives": ",".join(contract.guard_primitives),
                        "evidence_contract_required_bridge_axes": ",".join(contract.required_bridge_axes),
                    }
                )[0]

                self.assertIn(f"archetype_evidence_contract:{canonical_archetype_id}", context)
                self.assertIn(f"bridge_group={contract.runtime_bridge_group}", context)
                for primitive in contract.required_primitives:
                    self.assertIn(primitive, context)
                for axis in contract.required_bridge_axes:
                    self.assertIn(axis, context)
                if contract.positive_primitives:
                    for primitive in contract.positive_primitives:
                        self.assertIn(primitive, context)
                else:
                    self.assertIn("positive_primitives=none", context)
                    self.assertIn("missing_positive_primitives=none", context)
                for primitive in contract.green_gate_primitives:
                    self.assertIn(primitive, context)
                if contract.guard_primitives:
                    for primitive in contract.guard_primitives:
                        self.assertIn(primitive, context)
                else:
                    self.assertIn("guard_primitives_to_check=none", context)
                    self.assertIn("present_guard_primitives=none", context)

    def test_low_confidence_theme_route_canonical_is_not_applied_to_scoring(self):
        url = "https://news.example.com/company-route-low-confidence"
        route_provider = FakeThemeRouteProvider(
            output=ThemeRouteOutput(
                status="mixed_route",
                transition_detected=True,
                route_confidence=0.40,
                large_sector_id="L9_MOBILITY_TRANSPORT_LEISURE",
                canonical_archetype_id="C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
                evidence_slots=(
                    EvidenceSlotStatus(
                        slot="route_basis",
                        status="present",
                        evidence_refs=("news:000001:2026-06-08:fixture:route",),
                        confidence=0.8,
                    ),
                ),
            )
        )
        provider = FixtureSearchProvider(
            results_by_query={
                "테스트기업 데이터센터 수주": (
                    SearchResult(
                        title="테스트기업 실적 회복과 시장 관련기사",
                        url=url,
                        snippet="본문은 테스트기업 사업 회복",
                        source="fixture-news",
                        query="테스트기업 데이터센터 수주",
                        confidence=0.8,
                    ),
                )
            }
        )

        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=provider,
        ).run(
            FreeWebResearchInput(
                company_name="테스트기업",
                symbol="000001",
                sector=None,
                market=Market.KR,
                as_of_date=date(2026, 6, 8),
                top_results=5,
                fixture_text_by_url={url: "테스트기업은 본업 실적 회복을 보도했다."},
                theme_rebalance_enabled=True,
                theme_route_provider=route_provider,
                max_theme_expansion_rounds=0,
            )
        )

        self.assertIsNone(result.feature_input.canonical_archetype_id)
        self.assertNotEqual(result.feature_result.source_fields["canonical_archetype_id"], "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE")
        self.assertEqual(result.theme_route.status, "needs_more_evidence")
        self.assertIsNone(result.theme_route_diagnostics["canonical_archetype_id"])
        self.assertEqual(result.theme_route_diagnostics["theme_evidence_gate_status"], "no_matching_evidence_refs")
        self.assertEqual(result.score.diagnostic_scores["theme_route_applied_to_scoring"], 0.0)
        self.assertEqual(result.stage.stage, Stage.STAGE_0)
        self.assertFalse(result.theme_route_diagnostics["score_valid"])
        self.assertEqual(result.theme_route_diagnostics["score_blocked_reason"], "theme_route_needs_more_evidence")
        self.assertEqual(result.score.diagnostic_scores["score_blocked_by_theme_route"], 100.0)


def _run_free(
    *,
    company_name,
    symbol,
    sector,
    market,
    as_of_date,
    fixture_html,
    fixture_text,
    stage_context=None,
    previous_stage=None,
    budget=None,
):
    return FreeWebResearchRunner(
        browser_provider=BrowserSearchProvider(fixture_html_by_query=fixture_html),
        free_search_provider=EmptySearchProvider(),
    ).run(
        FreeWebResearchInput(
            company_name=company_name,
            symbol=symbol,
            sector=sector,
            market=market,
            as_of_date=as_of_date,
            stage_context=stage_context,
            previous_stage=previous_stage,
            budget=budget or SearchBudget(),
            fixture_text_by_url=fixture_text,
        )
    )


class _FakeHTTPResponse:
    def __init__(self, body: str, content_type: str = "text/html; charset=utf-8") -> None:
        self._body = body.encode("utf-8")
        self.headers = Message()
        self.headers["Content-Type"] = content_type

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        return None

    def read(self, size: int = -1) -> bytes:
        if size is None or size < 0:
            return self._body
        return self._body[:size]


if __name__ == "__main__":
    unittest.main()
