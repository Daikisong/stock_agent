"""Free search-first E2R web research runner."""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field, is_dataclass, replace
from datetime import date, timedelta
from pathlib import Path
from time import sleep
from typing import Any, Callable, Mapping, Protocol, Sequence
from urllib.parse import unquote

from e2r.agentic import (
    AgenticEvidenceProviderBundle,
    AnchorType,
    ClaimAdjudicatorProvider,
    ClaimExtractionOutput,
    ClaimExtractorProvider,
    Directness,
    EntityRecord,
    EntityRegistry,
    EvidenceAnchor,
    EvidenceCompilationInput,
    EvidenceContractV2,
    EvidenceDocument,
    EvidenceWorkflowOrchestrator,
    FollowUpPlannerProvider,
    FollowUpPlanningInput,
    FollowUpPlanningOutput,
    MappingStatus,
    PrimitiveMapperProvider,
    PrimitiveStateV2,
    PrimitiveStatus,
    ScoreContributionV2,
    ScoreInterval,
    SourceAcquisitionTask,
    SourceCandidate,
    SourceRoutePlan,
    SourceType,
    StageCourtInput,
    StageCourtOutput,
    aggregate_primitive_states,
    AppendOnlyEvidenceLedger,
    build_component_score_contributions_from_rubric,
    build_agentic_evidence_provider_bundle_from_env,
    build_default_codex_agentic_evidence_provider_bundle,
    build_source_route_plan,
    candidate_target_alias_count,
    candidate_target_alias_present,
    cash_bridge_signal_count,
    claim_metadata_from_claims,
    compile_claims_from_primitives,
    decide_stage_court,
    decode_follow_up_planning_output,
    evidence_contract_gap_context,
    load_evidence_contracts_v2,
    task_primitive_operating_signal_count,
    validate_follow_up_plan,
)
from e2r.diagnostic_values import diagnostic_value
from e2r.features import DeterministicFeatureEngineer, FeatureEngineeringInput, FeatureEngineeringResult
from e2r.llm.codex_theme_provider import build_default_codex_theme_route_provider
from e2r.llm.theme_provider import ThemeRouteProvider
from e2r.llm.theme_router import LLMThemeRebalanceAgent
from e2r.llm.theme_schemas import ThemeRouteDocument, ThemeRouteInput, ThemeRouteOutput, ThemeRouteSearchResult, route_diagnostics
from e2r.models import Market, RedTeamFinding, ScoreSnapshot, Stage, StageSnapshot
from e2r.pipeline.evidence_builder import evidence_from_feature_domains
from e2r.red_team import RedTeamAssessment, RedTeamEngine
from e2r.research.browser_search_provider import BrowserSearchProvider
from e2r.research.manual_source_provider import ManualSourceProvider
from e2r.research.naver_search_provider import NaverFreeSearchProvider
from e2r.research.page_fetcher import PageFetcher
from e2r.research.pdf_text_extractor import PDFTextExtractor
from e2r.research.query_planner import QueryPlan, QueryPlanner, QuerySpec
from e2r.research.official_follow_up_provider import (
    CompositeFollowUpSourceProvider,
    FeatureInputFollowUpSourceProvider,
    ReportDocumentFollowUpSourceProvider,
)
from e2r.research.report_consensus_proxy import build_report_consensus_proxy
from e2r.research.search_budget import ResearchLayer, SearchBudget, SearchBudgetTracker
from e2r.research.search_provider import FixtureSearchProvider, SearchProvider, SearchResult
from e2r.research.search_result_ranker import RankedSearchResult, SearchResultRanker
from e2r.research.web_research_runner import WebResearchInput, WebResearchResult, WebResearchRunner
from e2r.stage_gate_diagnostics import diagnose_stage_gates
from e2r.staging import StageClassificationInput, StageClassifier


_SCORE_GAP_QUERY_RETRY_MAX = 2
_LLM_QUERY_RETRY_MAX = 2
_AGENTIC_EVIDENCE_DOCUMENT_LIMIT = 12
_AGENTIC_EVIDENCE_DOCUMENT_TEXT_LIMIT = 8_000
_AGENTIC_EVIDENCE_CHUNK_LIMIT_PER_DOCUMENT = 2
_AGENTIC_GENERIC_BRIDGE_PRIMITIVE_ALIASES: Mapping[str, tuple[str, ...]] = {
    "cash_or_revision_conversion": (
        "FCF",
        "free cash flow",
        "free_cash_flow",
        "cashflow",
        "cashflow_from_operations",
        "actual_cashflow_from_operations",
        "cfo",
        "fcf_revision",
        "fcf_revision_1m",
        "eps_revision",
        "eps_revision_1m",
        "op_revision",
        "op_revision_1m",
        "consensus_revision",
        "consensus_fcf_revision",
        "consensus_fcf_revision_1m",
        "consensus",
        "영업현금흐름",
        "영업 현금흐름",
        "자유현금흐름",
        "현금흐름",
        "현금흐름 전환",
        "FCF 전환",
        "컨센서스",
        "컨센서스 상향",
        "추정치 상향",
        "실적 추정치 상향",
    ),
}
_SCORE_GAP_PRESENT_PRIMITIVE_COVERAGE: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("selected_fcf_source_missing", ("cash_or_revision_conversion",)),
    ("fcf conversion", ("cash_or_revision_conversion",)),
    ("operating cash flow", ("cash_or_revision_conversion",)),
    ("selected_revision_source_missing", ("medium_term_revision_visibility",)),
)


class _SearchProviderWithDiagnostics(Protocol):
    errors: list[str]
    blocked: bool


@dataclass(frozen=True)
class SkippedQuery:
    """A query skipped because free-search budget or blocking rules fired."""

    query: str
    layer: ResearchLayer
    reason: str


@dataclass(frozen=True)
class FreeWebResearchInput:
    """One symbol request for the free web research pipeline."""

    company_name: str
    symbol: str
    sector: str | None
    market: Market
    as_of_date: date
    stage_context: str | None = None
    previous_stage: Stage | None = None
    company_aliases: tuple[str, ...] = field(default_factory=tuple)
    candidate_reason_codes: tuple[str, ...] = field(default_factory=tuple)
    budget: SearchBudget = field(default_factory=SearchBudget)
    max_results_per_query: int = 100
    top_results: int | None = 60
    fixture_text_by_url: Mapping[str, str | Path] = field(default_factory=dict)
    include_manual_sources: bool = True
    live_page_fetch_enabled: bool = False
    page_fetch_timeout_seconds: float = 10.0
    page_fetch_cache_directory: str | Path | None = None
    theme_rebalance_enabled: bool | None = None
    theme_route_provider: ThemeRouteProvider | None = None
    max_theme_expansion_rounds: int | None = 2
    max_score_gap_expansion_rounds: int | None = 2
    theme_route_search_result_limit: int | None = 80
    theme_route_document_limit: int | None = 32
    theme_route_document_excerpt_chars: int = 1_200
    theme_expansion_reserve_queries: int = 10
    theme_evidence_review_enabled: bool = True
    theme_evidence_review_timeout_seconds: float | None = 60.0
    post_parse_gap_expansion_enabled: bool = True
    post_parse_gap_expansion_max_queries: int | None = 10
    post_gap_fetch_results_per_query: int = 5
    post_gap_fetch_min_results: int = 20
    llm_query_retry_max: int | None = _LLM_QUERY_RETRY_MAX
    score_gap_query_retry_max: int | None = _SCORE_GAP_QUERY_RETRY_MAX
    require_valid_theme_route_for_scoring: bool | None = None
    require_resolved_score_gaps_for_scoring: bool | None = None
    base_feature_input: FeatureEngineeringInput | None = None
    agentic_evidence_enabled: bool | None = None
    agentic_claim_extractor_provider: ClaimExtractorProvider | None = None
    agentic_claim_adjudicator_provider: ClaimAdjudicatorProvider | None = None
    agentic_primitive_mapper_provider: PrimitiveMapperProvider | None = None
    agentic_follow_up_planner_provider: FollowUpPlannerProvider | None = None
    agentic_follow_up_source_provider: SearchProvider | None = None
    agentic_mapper_self_consistency_rounds: int = 3
    agentic_mapper_self_consistency_min_agreement: int = 2
    agentic_mapper_self_consistency_use_batch: bool = True
    agentic_mapper_batch_max_tasks: int = 12
    agentic_evidence_document_limit: int = _AGENTIC_EVIDENCE_DOCUMENT_LIMIT
    agentic_max_raw_assertions_per_run: int | None = 72
    agentic_provider_timeout_seconds: float | None = None
    phase_event_sink: Callable[[Mapping[str, Any]], None] | None = None

    def __post_init__(self) -> None:
        if self.theme_rebalance_enabled is None:
            object.__setattr__(self, "theme_rebalance_enabled", self.theme_route_provider is not None)
        if self.theme_rebalance_enabled is True and self.theme_route_provider is None:
            object.__setattr__(self, "theme_route_provider", build_default_codex_theme_route_provider(working_directory=Path.cwd()))
        if self.require_valid_theme_route_for_scoring is None:
            object.__setattr__(
                self,
                "require_valid_theme_route_for_scoring",
                self.theme_rebalance_enabled is True and self.theme_route_provider is not None,
            )
        if self.require_resolved_score_gaps_for_scoring is None:
            object.__setattr__(
                self,
                "require_resolved_score_gaps_for_scoring",
                self.theme_rebalance_enabled is True
                and self.theme_route_provider is not None
                and self.post_parse_gap_expansion_enabled is True,
            )
        if self.max_theme_expansion_rounds is not None and self.max_theme_expansion_rounds < 0:
            raise ValueError("max_theme_expansion_rounds must be non-negative")
        if self.max_score_gap_expansion_rounds is not None and self.max_score_gap_expansion_rounds < 0:
            raise ValueError("max_score_gap_expansion_rounds must be non-negative")
        if self.max_results_per_query <= 0:
            raise ValueError("max_results_per_query must be positive")
        if self.top_results is None:
            raise ValueError("top_results must be bounded")
        if self.top_results < 0:
            raise ValueError("top_results must be non-negative")
        if self.theme_route_search_result_limit is not None and self.theme_route_search_result_limit < 0:
            raise ValueError("theme_route_search_result_limit must be non-negative")
        if self.theme_route_document_limit is not None and self.theme_route_document_limit < 0:
            raise ValueError("theme_route_document_limit must be non-negative")
        if self.theme_route_document_excerpt_chars <= 0:
            raise ValueError("theme_route_document_excerpt_chars must be positive")
        if self.theme_expansion_reserve_queries < 0:
            raise ValueError("theme_expansion_reserve_queries must be non-negative")
        if self.theme_evidence_review_timeout_seconds is not None and self.theme_evidence_review_timeout_seconds <= 0:
            raise ValueError("theme_evidence_review_timeout_seconds must be positive when set")
        if self.post_parse_gap_expansion_max_queries is not None and self.post_parse_gap_expansion_max_queries < 0:
            raise ValueError("post_parse_gap_expansion_max_queries must be non-negative")
        if self.post_gap_fetch_results_per_query <= 0:
            raise ValueError("post_gap_fetch_results_per_query must be positive")
        if self.post_gap_fetch_min_results < 0:
            raise ValueError("post_gap_fetch_min_results must be non-negative")
        if self.llm_query_retry_max is None:
            raise ValueError("llm_query_retry_max must be bounded")
        if self.llm_query_retry_max < 0:
            raise ValueError("llm_query_retry_max must be non-negative")
        if self.score_gap_query_retry_max is None:
            raise ValueError("score_gap_query_retry_max must be bounded")
        if self.score_gap_query_retry_max < 0:
            raise ValueError("score_gap_query_retry_max must be non-negative")
        if self.agentic_mapper_self_consistency_rounds <= 0:
            raise ValueError("agentic_mapper_self_consistency_rounds must be positive")
        if self.agentic_mapper_self_consistency_min_agreement <= 0:
            raise ValueError("agentic_mapper_self_consistency_min_agreement must be positive")
        if self.agentic_mapper_self_consistency_min_agreement > self.agentic_mapper_self_consistency_rounds:
            raise ValueError(
                "agentic_mapper_self_consistency_min_agreement cannot exceed "
                "agentic_mapper_self_consistency_rounds"
            )
        if self.agentic_mapper_batch_max_tasks <= 0:
            raise ValueError("agentic_mapper_batch_max_tasks must be positive")
        if self.agentic_evidence_document_limit <= 0:
            raise ValueError("agentic_evidence_document_limit must be positive")
        if self.agentic_max_raw_assertions_per_run is not None and self.agentic_max_raw_assertions_per_run <= 0:
            raise ValueError("agentic_max_raw_assertions_per_run must be positive when set")
        if self.agentic_provider_timeout_seconds is not None and self.agentic_provider_timeout_seconds <= 0:
            raise ValueError("agentic_provider_timeout_seconds must be positive when set")
        if self.agentic_evidence_enabled is None:
            object.__setattr__(
                self,
                "agentic_evidence_enabled",
                bool(
                    self.agentic_claim_extractor_provider
                    or self.agentic_claim_adjudicator_provider
                    or self.agentic_primitive_mapper_provider
                    or self.agentic_follow_up_planner_provider
                ),
            )
        if self.agentic_evidence_enabled and not _has_agentic_evidence_providers(self):
            bundle = build_agentic_evidence_provider_bundle_from_env(working_directory=Path.cwd())
            if bundle is None:
                bundle = build_default_codex_agentic_evidence_provider_bundle(working_directory=Path.cwd())
            if bundle is not None:
                _apply_agentic_provider_bundle(self, bundle)
        _apply_agentic_provider_timeout(self)
        follow_up_providers: list[SearchProvider] = []
        if self.agentic_follow_up_source_provider is not None:
            follow_up_providers.append(self.agentic_follow_up_source_provider)
        if self.base_feature_input is not None:
            base_provider = FeatureInputFollowUpSourceProvider(
                feature_input=self.base_feature_input,
                market=self.market,
            )
            follow_up_providers.append(base_provider)
        report_document_provider = ReportDocumentFollowUpSourceProvider(
            symbol=self.symbol,
            company_name=self.company_name,
            market=self.market,
        )
        if report_document_provider.has_sources(self.as_of_date):
            follow_up_providers.append(report_document_provider)
        if follow_up_providers:
            object.__setattr__(
                self,
                "agentic_follow_up_source_provider",
                follow_up_providers[0]
                if len(follow_up_providers) == 1
                else CompositeFollowUpSourceProvider(tuple(follow_up_providers)),
            )


@dataclass(frozen=True)
class AgenticEvidenceRuntimeTrace:
    """Dual-run trace for Evidence OS v2 compilation over fetched documents."""

    status: str = "disabled"
    archetype_id: str | None = None
    archetype_source: str | None = None
    raw_assertion_budget_limited: bool = False
    raw_assertion_budget_limit: int | None = None
    document_count: int = 0
    raw_assertion_count: int = 0
    adjudicated_claim_count: int = 0
    accepted_mapping_count: int = 0
    rejected_mapping_count: int = 0
    mapping_prefilter_original_task_count: int = 0
    mapping_prefilter_filtered_task_count: int = 0
    mapping_prefilter_skipped_input_count: int = 0
    mapping_prefilter_fallback_full_map_count: int = 0
    mapping_empty_output_count: int = 0
    mapping_empty_output_retry_count: int = 0
    mapping_empty_output_recovered_count: int = 0
    mapping_empty_output_summaries: tuple[str, ...] = field(default_factory=tuple)
    mapping_empty_output_retry_summaries: tuple[str, ...] = field(default_factory=tuple)
    mapping_prefilter_fallback_full_map_summaries: tuple[str, ...] = field(default_factory=tuple)
    claim_ids: tuple[str, ...] = field(default_factory=tuple)
    mapping_ids: tuple[str, ...] = field(default_factory=tuple)
    rejected_mapping_ids: tuple[str, ...] = field(default_factory=tuple)
    rejected_mapping_summaries: tuple[str, ...] = field(default_factory=tuple)
    eligibility_rejection_summaries: tuple[str, ...] = field(default_factory=tuple)
    document_selection_summaries: tuple[str, ...] = field(default_factory=tuple)
    document_ids: tuple[str, ...] = field(default_factory=tuple)
    skipped_existing_document_count: int = 0
    primitive_states: tuple[PrimitiveStateV2, ...] = field(default_factory=tuple)
    error_count: int = 0
    errors: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class WebResearchPipelineResult:
    """Search-to-stage result for free web research."""

    web_result: WebResearchResult
    feature_input: FeatureEngineeringInput
    feature_result: FeatureEngineeringResult
    score: ScoreSnapshot
    red_team: RedTeamAssessment
    stage: StageSnapshot
    budget_tracker: SearchBudgetTracker
    skipped_queries: tuple[SkippedQuery, ...] = field(default_factory=tuple)
    provider_errors: tuple[str, ...] = field(default_factory=tuple)
    red_team_findings: tuple[RedTeamFinding, ...] = field(default_factory=tuple)
    theme_route: ThemeRouteOutput | None = None
    expansion_queries_run: tuple[str, ...] = field(default_factory=tuple)
    theme_route_diagnostics: Mapping[str, object] = field(default_factory=dict)
    agentic_evidence_trace: AgenticEvidenceRuntimeTrace = field(default_factory=AgenticEvidenceRuntimeTrace)
    agentic_stage_court: StageCourtOutput | None = None
    legacy_stage_before_agentic_court: StageSnapshot | None = None


@dataclass(frozen=True)
class _ScoreGapExpansionResult:
    specs: tuple[QuerySpec, ...] = ()
    queries_run: tuple[str, ...] = ()
    status: str = "not_attempted"
    unresolved_gaps: tuple[str, ...] = ()
    rejection_reasons: tuple[str, ...] = ()
    blocked_reason: str | None = None
    diagnostic_details: Mapping[str, object] = field(default_factory=dict)


class FreeWebResearchRunner:
    """Run free web search, parse selected documents, and classify E2R stage."""

    def __init__(
        self,
        *,
        browser_provider: SearchProvider | None = None,
        free_search_provider: SearchProvider | None = None,
        manual_source_provider: ManualSourceProvider | None = None,
        query_planner: QueryPlanner | None = None,
        ranker: SearchResultRanker | None = None,
        pdf_text_extractor: PDFTextExtractor | None = None,
        engineer: DeterministicFeatureEngineer | None = None,
    ) -> None:
        self._browser_provider = browser_provider or BrowserSearchProvider()
        self._free_search_provider = free_search_provider or NaverFreeSearchProvider()
        self._manual_provider = manual_source_provider
        self._planner = query_planner or QueryPlanner()
        self._ranker = ranker or SearchResultRanker()
        self._pdf_text_extractor = pdf_text_extractor or PDFTextExtractor()
        self._engineer = engineer or DeterministicFeatureEngineer()

    def run(self, inputs: FreeWebResearchInput) -> WebResearchPipelineResult:
        query_plan = self._planner.plan(
            company_name=inputs.company_name,
            symbol=inputs.symbol,
            sector=inputs.sector,
            market=inputs.market,
            as_of_date=inputs.as_of_date,
            stage_context=inputs.stage_context,
        )
        _emit_phase_event(inputs, "start", initial_query_count=len(query_plan.queries))
        tracker = SearchBudgetTracker(inputs.budget)
        results_by_query: dict[str, tuple[SearchResult, ...]] = {}
        skipped: list[SkippedQuery] = []
        provider_errors: list[str] = []
        final_query_specs: list[QuerySpec] = list(query_plan.queries)
        initial_query_limit = _initial_query_limit(inputs)

        for index, query_spec in enumerate(query_plan.queries):
            if initial_query_limit is not None and index >= initial_query_limit:
                skipped.append(SkippedQuery(query=query_spec.query, layer=_layer_for_query(query_spec, inputs.stage_context), reason="theme_expansion_reserve"))
                continue
            layer = _layer_for_query(query_spec, inputs.stage_context)
            decision = tracker.can_run(inputs.symbol, layer)
            if not decision.allowed:
                skipped.append(SkippedQuery(query=query_spec.query, layer=layer, reason=decision.reason or "budget_denied"))
                continue
            tracker.record_query(inputs.symbol, layer)
            results_by_query[query_spec.query] = self._search_providers(
                query_spec,
                inputs,
                tracker,
                provider_errors,
            )
            if tracker.stopped_reason:
                skipped.extend(
                    SkippedQuery(query=item.query, layer=_layer_for_query(item, inputs.stage_context), reason=tracker.stopped_reason)
                    for item in query_plan.queries
                    if item.query not in results_by_query
                )
                break
            if inputs.budget.sleep_seconds_between_queries:
                sleep(inputs.budget.sleep_seconds_between_queries)
        _emit_phase_event(
            inputs,
            "initial_search_complete",
            query_count=len(results_by_query),
            search_result_count=sum(len(items) for items in results_by_query.values()),
            stopped_reason=tracker.stopped_reason,
        )

        theme_route, theme_route_diagnostics, expansion_specs, expansion_queries_run = self._run_theme_rebalance(
            inputs=inputs,
            tracker=tracker,
            results_by_query=results_by_query,
            skipped=skipped,
            provider_errors=provider_errors,
        )
        final_query_specs.extend(expansion_specs)
        final_query_plan = replace(query_plan, queries=tuple(dict.fromkeys(final_query_specs)))

        text_mapping: dict[str, str | Path] = dict(inputs.fixture_text_by_url)
        if inputs.include_manual_sources and self._manual_provider is not None:
            text_mapping.update(self._manual_provider.fixture_text_by_url())
        text_mapping.update(_provider_fixture_text_by_url(inputs.agentic_follow_up_source_provider))

        _emit_phase_event(
            inputs,
            "web_research_initial_start",
            query_count=len(final_query_plan.queries),
            top_results=inputs.top_results,
        )
        web_result = self._run_web_research(
            inputs=inputs,
            query_plan=final_query_plan,
            results_by_query=results_by_query,
            text_mapping=text_mapping,
        )
        _emit_web_result_phase(inputs, "web_research_initial_complete", web_result)
        theme_route, theme_route_diagnostics = self._run_theme_evidence_review(
            inputs=inputs,
            web_result=web_result,
            existing_route=theme_route,
            existing_diagnostics=theme_route_diagnostics,
            expansion_queries_run=expansion_queries_run,
        )
        gap_specs, gap_queries = self._run_post_parse_gap_expansion(
            inputs=inputs,
            tracker=tracker,
            results_by_query=results_by_query,
            skipped=skipped,
            provider_errors=provider_errors,
            web_result=web_result,
            theme_route=theme_route,
        )
        if gap_specs:
            final_query_specs.extend(gap_specs)
            expansion_queries_run = tuple(dict.fromkeys((*expansion_queries_run, *gap_queries)))
            final_query_plan = replace(query_plan, queries=tuple(dict.fromkeys(final_query_specs)))
            gap_top_results = _post_gap_top_results(inputs, gap_specs)
            _emit_phase_event(
                inputs,
                "post_parse_gap_web_research_start",
                new_query_count=len(gap_specs),
                total_query_count=len(final_query_plan.queries),
                top_results_override=gap_top_results,
                gap_fetch_mode="incremental",
            )
            web_result = self._run_gap_web_research(
                inputs=inputs,
                query_plan=final_query_plan,
                base_web_result=web_result,
                gap_specs=gap_specs,
                results_by_query=results_by_query,
                text_mapping=text_mapping,
                top_results_override=gap_top_results,
            )
            _emit_web_result_phase(inputs, "post_parse_gap_web_research_complete", web_result)
            theme_route, theme_route_diagnostics = self._run_theme_evidence_review(
                inputs=inputs,
                web_result=web_result,
                existing_route=theme_route,
                existing_diagnostics=theme_route_diagnostics,
                expansion_queries_run=expansion_queries_run,
            )
        theme_route_diagnostics = dict(theme_route_diagnostics)
        theme_route_diagnostics["post_parse_gap_expansion_count"] = len(gap_queries)
        theme_route_diagnostics["post_parse_gap_expansion_queries"] = tuple(gap_queries)
        theme_route, theme_route_diagnostics = _gate_theme_route_to_web_evidence(
            route=theme_route,
            diagnostics=theme_route_diagnostics,
            web_result=web_result,
        )
        route_large_sector_id, route_canonical_archetype_id = _theme_route_scoring_ids(theme_route)
        agent_extracted_fields = _theme_route_agent_extracted_fields(theme_route)
        theme_route_diagnostics = dict(theme_route_diagnostics)
        agent_extracted_fields, agent_field_claim_diagnostics = _claim_backed_theme_route_agent_fields(
            route=theme_route,
            inputs=inputs,
            agent_extracted_fields=agent_extracted_fields,
        )
        theme_route_diagnostics.update(agent_field_claim_diagnostics)
        proxy = build_report_consensus_proxy(web_result.parsed_reports, as_of_date=inputs.as_of_date)
        web_result = _with_report_consensus_proxy_evidence(inputs=inputs, web_result=web_result, proxy=proxy)
        agentic_evidence_trace, agentic_evidence_diagnostics = _run_agentic_evidence_dual_run(
            inputs=inputs,
            web_result=web_result,
            theme_route=theme_route,
        )
        theme_route_diagnostics.update(agentic_evidence_diagnostics)
        feature_input = _merge_feature_input(
            inputs=inputs,
            web_result=web_result,
            proxy=proxy,
            route_large_sector_id=route_large_sector_id,
            route_canonical_archetype_id=route_canonical_archetype_id,
            agent_extracted_fields=agent_extracted_fields,
        )
        feature_result = self._engineer.engineer(feature_input)
        feature_result = _with_theme_route_diagnostics(feature_result, theme_route, theme_route_diagnostics)
        feature_result = _with_agentic_score_contributions(feature_result, agentic_evidence_trace)
        score = feature_result.score()
        red_team = RedTeamEngine().assess(feature_result.red_team_signals)
        score_gap_queries: tuple[str, ...] = ()
        score_gap_expansion_result = _ScoreGapExpansionResult(status="not_attempted")
        score_gap_round_index = 0
        seen_score_gap_signatures: set[tuple[str, ...]] = set()
        last_score_gap_progress_diagnostics: Mapping[str, object] = {}
        score_gap_audit_events: list[Mapping[str, object]] = []
        score_gap_source_route_plans: list[Mapping[str, object]] = []
        theme_route_diagnostics = dict(theme_route_diagnostics)
        theme_route_diagnostics["post_score_gap_expansion_count"] = 0
        theme_route_diagnostics["post_score_gap_expansion_queries"] = ()
        theme_route_diagnostics["post_score_gap_expansion_status"] = "not_attempted"
        theme_route_diagnostics["post_score_gap_unresolved_gaps"] = ()
        theme_route_diagnostics["post_score_gap_rejection_reasons"] = ()
        theme_route_diagnostics["post_score_gap_audit_events"] = ()
        theme_route_diagnostics["post_score_gap_source_route_plans"] = ()
        theme_route_diagnostics["post_score_gap_query_origins"] = ()
        theme_route_diagnostics["post_score_gap_deterministic_fallback_query_used"] = False
        while True:
            gap_signature = _score_gap_state_signature(score, red_team, feature_result.source_fields)
            if gap_signature in seen_score_gap_signatures:
                current_score_gaps = _combined_score_gap_context(
                    score,
                    red_team,
                    agentic_evidence_trace,
                    archetype_id=_follow_up_archetype_id(
                        theme_route,
                        source_fields=feature_result.source_fields,
                        inputs=inputs,
                    ),
                )
                score_gap_expansion_result = _ScoreGapExpansionResult(
                    status="no_progress",
                    unresolved_gaps=current_score_gaps,
                    rejection_reasons=_score_gap_state_repeated_rejection_reasons(
                        last_score_gap_progress_diagnostics
                    ),
                    diagnostic_details=last_score_gap_progress_diagnostics,
                )
                theme_route_diagnostics = _with_score_gap_expansion_diagnostics(
                    theme_route_diagnostics,
                    score_gap_expansion_result,
                    score_gap_queries,
                )
                theme_route_diagnostics["post_score_gap_audit_events"] = tuple(score_gap_audit_events)
                theme_route_diagnostics["post_score_gap_source_route_plans"] = tuple(score_gap_source_route_plans)
                _apply_score_gap_route_plan_query_origin_diagnostics(theme_route_diagnostics)
                _emit_phase_event(
                    inputs,
                    "post_score_gap_stop_no_progress",
                    round_index=score_gap_round_index,
                    score_gap_query_count=len(score_gap_queries),
                    unresolved_gap_count=len(score_gap_expansion_result.unresolved_gaps),
                    progress_reason=last_score_gap_progress_diagnostics.get("post_score_gap_progress_reason"),
                    new_document_count=last_score_gap_progress_diagnostics.get("post_score_gap_new_document_count"),
                    new_claim_count=last_score_gap_progress_diagnostics.get("post_score_gap_new_claim_count"),
                    new_accepted_mapping_count=last_score_gap_progress_diagnostics.get(
                        "post_score_gap_new_accepted_mapping_count"
                    ),
                    primitive_state_changed=last_score_gap_progress_diagnostics.get(
                        "post_score_gap_primitive_state_changed"
                    ),
                    primitive_delta_count=len(
                        tuple(
                            last_score_gap_progress_diagnostics.get(
                                "post_score_gap_primitive_delta_summaries",
                                (),
                            )
                            or ()
                        )
                    ),
                )
                break
            if (
                inputs.max_score_gap_expansion_rounds is not None
                and score_gap_round_index >= inputs.max_score_gap_expansion_rounds
            ):
                current_score_gaps = _combined_score_gap_context(
                    score,
                    red_team,
                    agentic_evidence_trace,
                    archetype_id=_follow_up_archetype_id(
                        theme_route,
                        source_fields=feature_result.source_fields,
                        inputs=inputs,
                    ),
                )
                score_gap_expansion_result = _ScoreGapExpansionResult(
                    status="round_limit_reached",
                    unresolved_gaps=current_score_gaps,
                    rejection_reasons=("max_score_gap_expansion_rounds_reached",),
                )
                theme_route_diagnostics = _with_score_gap_expansion_diagnostics(
                    theme_route_diagnostics,
                    score_gap_expansion_result,
                    score_gap_queries,
                )
                theme_route_diagnostics["post_score_gap_audit_events"] = tuple(score_gap_audit_events)
                theme_route_diagnostics["post_score_gap_source_route_plans"] = tuple(score_gap_source_route_plans)
                _apply_score_gap_route_plan_query_origin_diagnostics(theme_route_diagnostics)
                _emit_phase_event(
                    inputs,
                    "post_score_gap_stop_round_limit",
                    round_index=score_gap_round_index,
                    score_gap_query_count=len(score_gap_queries),
                    unresolved_gap_count=len(score_gap_expansion_result.unresolved_gaps),
                )
                break
            seen_score_gap_signatures.add(gap_signature)
            _emit_phase_event(
                inputs,
                "post_score_gap_round_start",
                round_index=score_gap_round_index,
                score_total=score.total_score,
                score_gap_query_count=len(score_gap_queries),
            )
            score_gap_expansion_result = self._run_post_score_gap_expansion(
                inputs=inputs,
                tracker=tracker,
                results_by_query=results_by_query,
                skipped=skipped,
                provider_errors=provider_errors,
                score=score,
                red_team=red_team,
                web_result=web_result,
                theme_route=theme_route,
                source_fields=feature_result.source_fields,
                agentic_evidence_trace=agentic_evidence_trace,
            )
            theme_route_diagnostics = _with_score_gap_expansion_diagnostics(
                theme_route_diagnostics,
                score_gap_expansion_result,
                score_gap_queries,
            )
            score_gap_source_route_plans.extend(_source_route_plan_diagnostics(score_gap_expansion_result))
            theme_route_diagnostics["post_score_gap_source_route_plans"] = tuple(score_gap_source_route_plans)
            _apply_score_gap_route_plan_query_origin_diagnostics(theme_route_diagnostics)
            if not score_gap_expansion_result.specs:
                break
            score_gap_queries = tuple(dict.fromkeys((*score_gap_queries, *score_gap_expansion_result.queries_run)))
            final_query_specs.extend(score_gap_expansion_result.specs)
            expansion_queries_run = tuple(dict.fromkeys((*expansion_queries_run, *score_gap_queries)))
            final_query_plan = replace(query_plan, queries=tuple(dict.fromkeys(final_query_specs)))
            score_gap_top_results = _post_gap_top_results(inputs, score_gap_expansion_result.specs)
            _emit_phase_event(
                inputs,
                "post_score_gap_web_research_start",
                round_index=score_gap_round_index,
                new_query_count=len(score_gap_expansion_result.specs),
                total_score_gap_query_count=len(score_gap_queries),
                top_results_override=score_gap_top_results,
                gap_fetch_mode="incremental",
            )
            text_mapping.update(_provider_fixture_text_by_url(inputs.agentic_follow_up_source_provider))
            web_result = self._run_gap_web_research(
                inputs=inputs,
                query_plan=final_query_plan,
                base_web_result=web_result,
                gap_specs=score_gap_expansion_result.specs,
                results_by_query=results_by_query,
                text_mapping=text_mapping,
                top_results_override=score_gap_top_results,
            )
            _emit_web_result_phase(inputs, "post_score_gap_web_research_complete", web_result)
            _emit_web_result_phase(
                inputs,
                "post_score_gap_web_research_new_only_complete",
                _web_research_result_for_queries(
                    web_result,
                    queries=score_gap_expansion_result.queries_run,
                ),
            )
            theme_route, theme_route_diagnostics = self._run_theme_evidence_review(
                inputs=inputs,
                web_result=web_result,
                existing_route=theme_route,
                existing_diagnostics=theme_route_diagnostics,
                expansion_queries_run=expansion_queries_run,
            )
            theme_route_diagnostics = dict(theme_route_diagnostics)
            theme_route_diagnostics["post_parse_gap_expansion_count"] = len(gap_queries)
            theme_route_diagnostics["post_parse_gap_expansion_queries"] = tuple(gap_queries)
            theme_route_diagnostics["post_score_gap_expansion_count"] = len(score_gap_queries)
            theme_route_diagnostics["post_score_gap_expansion_queries"] = tuple(score_gap_queries)
            theme_route_diagnostics["post_score_gap_expansion_status"] = score_gap_expansion_result.status
            theme_route_diagnostics["post_score_gap_unresolved_gaps"] = tuple(score_gap_expansion_result.unresolved_gaps)
            theme_route_diagnostics["post_score_gap_rejection_reasons"] = tuple(score_gap_expansion_result.rejection_reasons)
            theme_route_diagnostics["post_score_gap_source_route_plans"] = tuple(score_gap_source_route_plans)
            _apply_score_gap_route_plan_query_origin_diagnostics(theme_route_diagnostics)
            if score_gap_expansion_result.blocked_reason:
                theme_route_diagnostics["post_score_gap_blocked_reason"] = score_gap_expansion_result.blocked_reason
            theme_route, theme_route_diagnostics = _gate_theme_route_to_web_evidence(
                route=theme_route,
                diagnostics=theme_route_diagnostics,
                web_result=web_result,
            )
            route_large_sector_id, route_canonical_archetype_id = _theme_route_scoring_ids(theme_route)
            agent_extracted_fields = _theme_route_agent_extracted_fields(theme_route)
            theme_route_diagnostics = dict(theme_route_diagnostics)
            agent_extracted_fields, agent_field_claim_diagnostics = _claim_backed_theme_route_agent_fields(
                route=theme_route,
                inputs=inputs,
                agent_extracted_fields=agent_extracted_fields,
            )
            theme_route_diagnostics.update(agent_field_claim_diagnostics)
            proxy = build_report_consensus_proxy(web_result.parsed_reports, as_of_date=inputs.as_of_date)
            web_result = _with_report_consensus_proxy_evidence(inputs=inputs, web_result=web_result, proxy=proxy)
            previous_agentic_evidence_trace = agentic_evidence_trace
            previous_score_gap_signature = gap_signature
            previous_score_contributions_v2 = tuple(feature_result.payload.score_contributions_v2)
            next_agentic_evidence_trace, _ = _run_agentic_evidence_dual_run(
                inputs=inputs,
                web_result=_web_research_result_for_queries(
                    web_result,
                    queries=score_gap_expansion_result.queries_run,
                ),
                theme_route=theme_route,
                skip_document_ids=_agentic_trace_document_ids(agentic_evidence_trace),
                include_official_documents=False,
            )
            agentic_evidence_trace = _merge_agentic_evidence_runtime_traces(
                agentic_evidence_trace,
                next_agentic_evidence_trace,
            )
            agentic_evidence_diagnostics = _agentic_evidence_diagnostics(agentic_evidence_trace, inputs=inputs)
            theme_route_diagnostics.update(agentic_evidence_diagnostics)
            feature_input = _merge_feature_input(
                inputs=inputs,
                web_result=web_result,
                proxy=proxy,
                route_large_sector_id=route_large_sector_id,
                route_canonical_archetype_id=route_canonical_archetype_id,
                agent_extracted_fields=agent_extracted_fields,
            )
            feature_result = self._engineer.engineer(feature_input)
            feature_result = _with_theme_route_diagnostics(feature_result, theme_route, theme_route_diagnostics)
            feature_result = _with_agentic_score_contributions(feature_result, agentic_evidence_trace)
            score = feature_result.score()
            red_team = RedTeamEngine().assess(feature_result.red_team_signals)
            current_score_gap_signature = _score_gap_state_signature(score, red_team, feature_result.source_fields)
            last_score_gap_progress_diagnostics = _score_gap_progress_diagnostics(
                previous_trace=previous_agentic_evidence_trace,
                current_trace=next_agentic_evidence_trace,
                merged_trace=agentic_evidence_trace,
                archetype_id=_follow_up_archetype_id(
                    theme_route,
                    source_fields=feature_result.source_fields,
                    inputs=inputs,
                ),
                previous_signature=previous_score_gap_signature,
                current_signature=current_score_gap_signature,
                previous_score_contributions=previous_score_contributions_v2,
                current_score_contributions=tuple(feature_result.payload.score_contributions_v2),
            )
            score_gap_audit_events.append(
                _score_gap_audit_event(
                    inputs=inputs,
                    round_index=score_gap_round_index,
                    expansion=score_gap_expansion_result,
                    progress_diagnostics=last_score_gap_progress_diagnostics,
                    previous_signature=previous_score_gap_signature,
                    current_signature=current_score_gap_signature,
                )
            )
            theme_route_diagnostics.update(last_score_gap_progress_diagnostics)
            theme_route_diagnostics["post_score_gap_audit_events"] = tuple(score_gap_audit_events)
            score_gap_round_index += 1
        route_block_reason = _theme_route_score_block_reason(
            inputs=inputs,
            route=theme_route,
            diagnostics=theme_route_diagnostics,
            route_large_sector_id=route_large_sector_id,
            route_canonical_archetype_id=route_canonical_archetype_id,
        )
        score_gap_block_reason = _score_gap_score_block_reason(
            inputs=inputs,
            expansion=score_gap_expansion_result,
            queries_run_count=len(score_gap_queries),
        )
        if _score_gap_block_should_defer_to_stage_court(
            reason=score_gap_block_reason,
            trace=agentic_evidence_trace,
        ):
            theme_route_diagnostics["post_score_gap_deferred_to_stage_court"] = True
            theme_route_diagnostics["post_score_gap_deferred_reason"] = score_gap_block_reason
            score_gap_block_reason = None
        agentic_evidence_block_reason = _agentic_evidence_score_block_reason(
            inputs=inputs,
            score=score,
            trace=agentic_evidence_trace,
        )
        theme_route_diagnostics = dict(theme_route_diagnostics)
        theme_route_diagnostics.update(
            _agentic_score_contribution_diagnostics(feature_result.payload.score_contributions_v2)
        )
        theme_route_diagnostics["agentic_evidence_block_reason"] = agentic_evidence_block_reason
        if route_block_reason:
            feature_result = _clear_unconfirmed_theme_route_classification(feature_result)
            score, theme_route_diagnostics = _invalidate_score_for_theme_route(
                score=score,
                diagnostics=theme_route_diagnostics,
                reason=route_block_reason,
            )
            stage = _blocked_stage_for_theme_route(
                inputs=inputs,
                score=score,
                red_team=red_team,
                web_result=web_result,
                reason=route_block_reason,
            )
        elif score_gap_block_reason:
            score, theme_route_diagnostics = _invalidate_score_for_score_gap(
                score=score,
                diagnostics=theme_route_diagnostics,
                reason=score_gap_block_reason,
                expansion=score_gap_expansion_result,
            )
            stage = _blocked_stage_for_score_gap(
                inputs=inputs,
                score=score,
                red_team=red_team,
                web_result=web_result,
                reason=score_gap_block_reason,
            )
        elif agentic_evidence_block_reason:
            score, theme_route_diagnostics = _invalidate_score_for_agentic_evidence(
                score=score,
                diagnostics=theme_route_diagnostics,
                reason=agentic_evidence_block_reason,
            )
            stage = _blocked_stage_for_agentic_evidence(
                inputs=inputs,
                score=score,
                red_team=red_team,
                web_result=web_result,
                reason=agentic_evidence_block_reason,
            )
        else:
            score, theme_route_diagnostics = _mark_score_gap_warning_if_any(
                inputs=inputs,
                score=score,
                diagnostics=theme_route_diagnostics,
                expansion=score_gap_expansion_result,
                queries_run_count=len(score_gap_queries),
            )
            score, theme_route_diagnostics = _mark_score_valid_for_theme_route(
                inputs=inputs,
                score=score,
                diagnostics=theme_route_diagnostics,
            )
            stage = StageClassifier().classify(
                StageClassificationInput(
                    score=score,
                    red_team=red_team,
                    previous_stage=inputs.previous_stage,
                    theme_regime_score=_theme_regime_score(web_result, feature_input),
                    company_event_score=_company_event_score(web_result, feature_input),
                    high_quality_company_event=_high_quality_company_event(web_result, feature_input),
                    evidence_ids=tuple(item.evidence_id for item in web_result.evidence),
                )
            )
        agentic_stage_court = _agentic_stage_court_output(
            diagnostics=theme_route_diagnostics,
            trace=agentic_evidence_trace,
            score=score,
            inputs=inputs,
            theme_route=theme_route,
        )
        legacy_stage_before_agentic_court = None
        if agentic_stage_court is not None:
            theme_route_diagnostics = _with_agentic_stage_court_diagnostics(
                diagnostics=theme_route_diagnostics,
                stage_output=agentic_stage_court,
            )
            legacy_stage_before_agentic_court = stage
            stage = _stage_snapshot_from_agentic_stage_court(
                stage_output=agentic_stage_court,
                legacy_stage=stage,
                score=score,
                inputs=inputs,
            )
        theme_route_diagnostics = _with_stage_gate_diagnostics(theme_route_diagnostics, score, red_team)
        return WebResearchPipelineResult(
            web_result=web_result,
            feature_input=feature_input,
            feature_result=feature_result,
            score=score,
            red_team=red_team,
            stage=stage,
            budget_tracker=tracker,
            skipped_queries=tuple(skipped),
            provider_errors=tuple(dict.fromkeys(provider_errors + _provider_errors(self._browser_provider) + _provider_errors(self._free_search_provider))),
            red_team_findings=tuple(web_result.red_team_findings) + tuple(red_team.findings),
            theme_route=theme_route,
            expansion_queries_run=expansion_queries_run,
            theme_route_diagnostics=theme_route_diagnostics,
            agentic_evidence_trace=agentic_evidence_trace,
            agentic_stage_court=agentic_stage_court,
            legacy_stage_before_agentic_court=legacy_stage_before_agentic_court,
        )

    def _run_web_research(
        self,
        *,
        inputs: FreeWebResearchInput,
        query_plan: QueryPlan,
        results_by_query: Mapping[str, tuple[SearchResult, ...]],
        text_mapping: Mapping[str, str | Path],
        top_results_override: int | None = None,
    ) -> WebResearchResult:
        web_runner = WebResearchRunner(
            query_planner=_FixedQueryPlanner(query_plan),
            search_provider=FixtureSearchProvider(results_by_query=results_by_query),
            ranker=self._ranker,
            page_fetcher=PageFetcher(
                fixture_text_by_url=text_mapping,
                live_enabled=inputs.live_page_fetch_enabled,
                timeout_seconds=inputs.page_fetch_timeout_seconds,
                cache_directory=inputs.page_fetch_cache_directory,
                pdf_text_extractor=self._pdf_text_extractor,
            ),
            pdf_text_extractor=self._pdf_text_extractor,
        )
        return web_runner.run(
            WebResearchInput(
                company_name=inputs.company_name,
                symbol=inputs.symbol,
                sector=inputs.sector,
                market=inputs.market,
                as_of_date=inputs.as_of_date,
                stage_context=inputs.stage_context,
                company_aliases=inputs.company_aliases,
                max_results_per_query=inputs.max_results_per_query,
                top_results=top_results_override if top_results_override is not None else inputs.top_results,
            )
        )

    def _run_gap_web_research(
        self,
        *,
        inputs: FreeWebResearchInput,
        query_plan: QueryPlan,
        base_web_result: WebResearchResult,
        gap_specs: Sequence[QuerySpec],
        results_by_query: Mapping[str, tuple[SearchResult, ...]],
        text_mapping: Mapping[str, str | Path],
        top_results_override: int | None,
    ) -> WebResearchResult:
        gap_query_plan = replace(query_plan, queries=tuple(gap_specs))
        gap_results_by_query = {spec.query: tuple(results_by_query.get(spec.query, ())) for spec in gap_specs}
        gap_web_result = self._run_web_research(
            inputs=inputs,
            query_plan=gap_query_plan,
            results_by_query=gap_results_by_query,
            text_mapping=text_mapping,
            top_results_override=top_results_override,
        )
        return _merge_web_research_results(
            base=base_web_result,
            incremental=gap_web_result,
            combined_query_plan=query_plan,
        )

    def _search_providers(
        self,
        query_spec: QuerySpec,
        inputs: FreeWebResearchInput,
        tracker: SearchBudgetTracker,
        provider_errors: list[str],
    ) -> tuple[SearchResult, ...]:
        providers: list[SearchProvider] = [self._browser_provider, self._free_search_provider]
        if inputs.include_manual_sources and self._manual_provider is not None:
            providers.append(self._manual_provider)

        results: list[SearchResult] = []
        for provider in providers:
            found = tuple(provider.search(query_spec.query, inputs.as_of_date, inputs.max_results_per_query))
            results.extend(found)
            if _provider_blocked(provider):
                tracker.record_block("captcha_or_block_detected")
                provider_errors.append("captcha_or_block_detected")
                break
        unique: dict[str, SearchResult] = {}
        for item in results:
            unique.setdefault(item.url, item)
        return tuple(unique.values())

    def _search_agentic_follow_up_sources(
        self,
        *,
        spec: QuerySpec,
        inputs: FreeWebResearchInput,
        tracker: SearchBudgetTracker,
        provider_errors: list[str],
        task: SourceAcquisitionTask,
    ) -> tuple[SearchResult, ...]:
        official_results = _search_optional_provider(
            provider=inputs.agentic_follow_up_source_provider,
            query=spec.query,
            as_of_date=inputs.as_of_date,
            max_results=max(1, min(task.max_candidates, inputs.max_results_per_query)),
            provider_errors=provider_errors,
            error_prefix="agentic_follow_up_source_provider",
        )
        if official_results and _agentic_task_can_stop_after_official(task, official_results):
            return official_results
        web_results = self._search_providers(spec, inputs, tracker, provider_errors)
        by_url: dict[str, SearchResult] = {}
        for item in (*official_results, *web_results):
            by_url.setdefault(item.url, item)
        return tuple(by_url.values())

    def _run_theme_rebalance(
        self,
        *,
        inputs: FreeWebResearchInput,
        tracker: SearchBudgetTracker,
        results_by_query: dict[str, tuple[SearchResult, ...]],
        skipped: list[SkippedQuery],
        provider_errors: list[str],
    ) -> tuple[ThemeRouteOutput | None, Mapping[str, object], tuple[QuerySpec, ...], tuple[str, ...]]:
        if not inputs.theme_rebalance_enabled:
            return None, {}, (), ()
        if inputs.theme_route_provider is None:
            route = ThemeRouteOutput(status="disabled_no_provider", blocked_reason="theme_rebalance_enabled_without_provider")
            return route, _theme_route_run_diagnostics(route, (), "disabled_no_provider"), (), ()
        if tracker.stopped_reason:
            route = ThemeRouteOutput(status="provider_error", blocked_reason=tracker.stopped_reason)
            return route, _theme_route_run_diagnostics(route, (), tracker.stopped_reason), (), ()

        agent = LLMThemeRebalanceAgent(
            _theme_route_provider_for_timeout(
                inputs.theme_route_provider,
                timeout_seconds=inputs.theme_evidence_review_timeout_seconds,
            )
        )
        expansion_specs: list[QuerySpec] = []
        expansion_queries_run: list[str] = []
        seen_queries = set(results_by_query)
        seen_urls = {result.url for results in results_by_query.values() for result in results}
        route: ThemeRouteOutput | None = None
        status = "completed"
        round_index = 0
        retry_index = 0
        previous_rejections: tuple[str, ...] = ()
        seen_retry_failures: set[tuple[str, ...]] = set()
        while True:
            if inputs.max_theme_expansion_rounds is not None and round_index >= max(1, inputs.max_theme_expansion_rounds):
                break
            route_search_results = self._theme_route_search_results_from_queries(inputs, results_by_query)
            _emit_phase_event(
                inputs,
                "theme_rebalance_route_start",
                round_index=round_index,
                retry_index=retry_index,
                raw_search_result_count=len(_flatten_results(results_by_query)),
                llm_search_result_count=len(route_search_results),
                timeout_seconds=inputs.theme_evidence_review_timeout_seconds,
            )
            route = agent.route(
                ThemeRouteInput(
                    company_name=inputs.company_name,
                    symbol=inputs.symbol,
                    sector=inputs.sector,
                    market=inputs.market.value,
                    as_of_date=inputs.as_of_date,
                    stage_context=inputs.stage_context,
                    candidate_reason_codes=inputs.candidate_reason_codes,
                    search_results=route_search_results,
                    score_gap_context=_llm_query_retry_context(
                        phase="theme_expansion",
                        retry_index=retry_index,
                        previous_rejections=previous_rejections,
                    ),
                )
            )
            _emit_phase_event(
                inputs,
                "theme_rebalance_route_complete",
                round_index=round_index,
                retry_index=retry_index,
                status=route.status,
                blocked_reason=route.blocked_reason,
                timeout_seconds=inputs.theme_evidence_review_timeout_seconds,
            )
            if route.status in {"provider_error", "invalid_provider_output", "disabled_no_provider"}:
                status = route.status
                break
            if route.status == "no_transition" and not route.suggested_queries:
                break
            if inputs.max_theme_expansion_rounds is not None and inputs.max_theme_expansion_rounds <= 0:
                break

            query_specs = tuple(
                _theme_query_spec(
                    query=query,
                    inputs=inputs,
                    round_index=round_index,
                    query_index=query_index,
                )
                for query_index, query in enumerate(route.suggested_queries)
                if query.strip()
            )
            runnable_specs: list[QuerySpec] = []
            planned_queries = set(seen_queries)
            rejections: list[str] = []
            for spec in query_specs:
                safe_query = _asof_safe_theme_query(spec.query, inputs.as_of_date)
                if safe_query is None:
                    skipped.append(SkippedQuery(query=spec.query, layer=ResearchLayer.DEEP_RESEARCH, reason="future_query_rejected"))
                    rejections.append("future_query_rejected")
                    continue
                safe_query = _company_scoped_query(safe_query, inputs)
                if safe_query in planned_queries:
                    skipped.append(SkippedQuery(query=safe_query, layer=ResearchLayer.DEEP_RESEARCH, reason="duplicate_theme_query"))
                    rejections.append("duplicate_theme_query")
                    continue
                planned_queries.add(safe_query)
                runnable_specs.append(replace(spec, query=safe_query))

            ran_this_round = 0
            for spec in runnable_specs:
                decision = tracker.can_run(inputs.symbol, ResearchLayer.DEEP_RESEARCH)
                if not decision.allowed:
                    reason = decision.reason or "budget_denied"
                    skipped.append(SkippedQuery(query=spec.query, layer=ResearchLayer.DEEP_RESEARCH, reason=reason))
                    rejections.append(reason)
                    status = reason
                    continue
                tracker.record_query(inputs.symbol, ResearchLayer.DEEP_RESEARCH)
                results = self._search_providers(spec, inputs, tracker, provider_errors)
                results_by_query[spec.query] = results
                seen_queries.add(spec.query)
                seen_urls.update(item.url for item in results)
                expansion_specs.append(spec)
                expansion_queries_run.append(spec.query)
                ran_this_round += 1
                if tracker.stopped_reason:
                    status = tracker.stopped_reason
                    break
                if inputs.budget.sleep_seconds_between_queries:
                    sleep(inputs.budget.sleep_seconds_between_queries)

            if tracker.stopped_reason or ran_this_round == 0:
                if tracker.stopped_reason:
                    break
                if route.status == "no_transition":
                    break
                previous_rejections = tuple(dict.fromkeys(rejections or ("llm_returned_no_suggested_queries",)))
                if _only_budget_rejections(previous_rejections) or _retry_should_stop(
                    retry_index=retry_index,
                    max_retries=inputs.llm_query_retry_max,
                    previous_rejections=previous_rejections,
                    seen_failures=seen_retry_failures,
                ):
                    break
                retry_index += 1
                status = "needs_more_evidence"
                continue
            round_index += 1
            retry_index = 0
            previous_rejections = ()

        if route is None:
            route = ThemeRouteOutput(status="no_transition")
        diagnostics = dict(_theme_route_run_diagnostics(route, tuple(expansion_queries_run), status))
        diagnostics["theme_route_blocked_reason"] = route.blocked_reason
        diagnostics["theme_route_timeout_seconds"] = inputs.theme_evidence_review_timeout_seconds
        return route, diagnostics, tuple(expansion_specs), tuple(expansion_queries_run)

    def _run_theme_evidence_review(
        self,
        *,
        inputs: FreeWebResearchInput,
        web_result: WebResearchResult,
        existing_route: ThemeRouteOutput | None,
        existing_diagnostics: Mapping[str, object],
        expansion_queries_run: Sequence[str],
    ) -> tuple[ThemeRouteOutput | None, Mapping[str, object]]:
        if not inputs.theme_evidence_review_enabled:
            return existing_route, existing_diagnostics
        if not inputs.theme_rebalance_enabled or inputs.theme_route_provider is None:
            return existing_route, existing_diagnostics
        documents = _theme_route_documents(
            web_result,
            limit=inputs.theme_route_document_limit,
            excerpt_chars=inputs.theme_route_document_excerpt_chars,
        )
        diagnostics = dict(existing_diagnostics)
        if not documents:
            diagnostics["theme_evidence_review_status"] = "no_fetched_documents"
            return existing_route, diagnostics

        agent = LLMThemeRebalanceAgent(
            _theme_route_provider_for_timeout(
                inputs.theme_route_provider,
                timeout_seconds=inputs.theme_evidence_review_timeout_seconds,
            )
        )
        route_search_results = self._theme_route_search_results_from_web_result(inputs, web_result)
        _emit_phase_event(
            inputs,
            "theme_evidence_review_start",
            raw_ranked_result_count=len(web_result.ranked_results),
            llm_search_result_count=len(route_search_results),
            raw_document_count=len(web_result.fetched_documents),
            llm_document_count=len(documents),
            timeout_seconds=inputs.theme_evidence_review_timeout_seconds,
        )
        review = agent.route(
            ThemeRouteInput(
                company_name=inputs.company_name,
                symbol=inputs.symbol,
                sector=inputs.sector,
                market=inputs.market.value,
                as_of_date=inputs.as_of_date,
                stage_context=inputs.stage_context,
                candidate_reason_codes=inputs.candidate_reason_codes,
                current_large_sector_id=existing_route.large_sector_id if existing_route else None,
                current_canonical_archetype_id=existing_route.canonical_archetype_id if existing_route else None,
                search_results=route_search_results,
                documents=documents,
            )
        )
        _emit_phase_event(
            inputs,
            "theme_evidence_review_complete",
            status=review.status,
            blocked_reason=review.blocked_reason,
            llm_document_count=len(documents),
            timeout_seconds=inputs.theme_evidence_review_timeout_seconds,
        )
        if review.status in {"provider_error", "invalid_provider_output", "disabled_no_provider"} and existing_route is not None:
            diagnostics["theme_evidence_review_status"] = review.status
            diagnostics["theme_evidence_review_blocked_reason"] = review.blocked_reason
            diagnostics["theme_evidence_document_count"] = len(documents)
            diagnostics["theme_evidence_review_timeout_seconds"] = inputs.theme_evidence_review_timeout_seconds
            return existing_route, diagnostics

        merged = _merge_theme_routes(existing_route, review)
        diagnostics = dict(_theme_route_run_diagnostics(merged, expansion_queries_run, str(existing_diagnostics.get("theme_rebalance_status") or "completed")))
        diagnostics["theme_evidence_review_status"] = "completed"
        diagnostics["theme_evidence_document_count"] = len(documents)
        diagnostics["theme_evidence_review_timeout_seconds"] = inputs.theme_evidence_review_timeout_seconds
        return merged, diagnostics

    def _theme_route_search_results_from_queries(
        self,
        inputs: FreeWebResearchInput,
        results_by_query: Mapping[str, Sequence[SearchResult]],
    ) -> tuple[ThemeRouteSearchResult, ...]:
        ranked = self._ranker.rank(
            _flatten_results(results_by_query),
            company_name=inputs.company_name,
            as_of_date=inputs.as_of_date,
        )
        return tuple(
            ThemeRouteSearchResult.from_search_result(item.result)
            for item in _select_ranked_for_llm(ranked, inputs.theme_route_search_result_limit)
        )

    def _theme_route_search_results_from_web_result(
        self,
        inputs: FreeWebResearchInput,
        web_result: WebResearchResult,
    ) -> tuple[ThemeRouteSearchResult, ...]:
        return tuple(
            ThemeRouteSearchResult.from_search_result(item.result)
            for item in _select_ranked_for_llm(web_result.ranked_results, inputs.theme_route_search_result_limit)
        )

    def _run_post_parse_gap_expansion(
        self,
        *,
        inputs: FreeWebResearchInput,
        tracker: SearchBudgetTracker,
        results_by_query: dict[str, tuple[SearchResult, ...]],
        skipped: list[SkippedQuery],
        provider_errors: list[str],
        web_result: WebResearchResult,
        theme_route: ThemeRouteOutput | None,
    ) -> tuple[tuple[QuerySpec, ...], tuple[str, ...]]:
        if not _post_parse_gap_expansion_allowed(inputs, theme_route):
            return (), ()
        route = theme_route
        seen_queries = set(results_by_query)
        previous_rejections: tuple[str, ...] = ()
        seen_retry_failures: set[tuple[str, ...]] = set()
        retry_index = 0
        while True:
            query_texts = _post_parse_gap_queries(
                inputs=inputs,
                route=route,
            )
            if not query_texts:
                previous_rejections = ("llm_returned_no_suggested_queries",)
            else:
                specs: list[QuerySpec] = []
                queries_run: list[str] = []
                rejections: list[str] = []
                for query_index, query in enumerate(query_texts):
                    safe_query = _asof_safe_theme_query(query, inputs.as_of_date)
                    if safe_query is None:
                        skipped.append(SkippedQuery(query=query, layer=ResearchLayer.DEEP_RESEARCH, reason="future_query_rejected"))
                        rejections.append("future_query_rejected")
                        continue
                    safe_query = _company_scoped_query(safe_query, inputs)
                    if safe_query in seen_queries:
                        skipped.append(SkippedQuery(query=safe_query, layer=ResearchLayer.DEEP_RESEARCH, reason="duplicate_post_parse_gap_query"))
                        rejections.append("duplicate_post_parse_gap_query")
                        continue
                    decision = tracker.can_run(inputs.symbol, ResearchLayer.DEEP_RESEARCH)
                    if not decision.allowed:
                        reason = decision.reason or "budget_denied"
                        skipped.append(SkippedQuery(query=safe_query, layer=ResearchLayer.DEEP_RESEARCH, reason=reason))
                        rejections.append(reason)
                        continue
                    spec = _post_parse_gap_query_spec(query=safe_query, inputs=inputs, query_index=query_index)
                    tracker.record_query(inputs.symbol, ResearchLayer.DEEP_RESEARCH)
                    results = self._search_providers(spec, inputs, tracker, provider_errors)
                    results_by_query[spec.query] = results
                    seen_queries.add(spec.query)
                    specs.append(spec)
                    queries_run.append(spec.query)
                    if tracker.stopped_reason:
                        break
                    if inputs.budget.sleep_seconds_between_queries:
                        sleep(inputs.budget.sleep_seconds_between_queries)
                if specs or tracker.stopped_reason:
                    return tuple(specs), tuple(queries_run)
                previous_rejections = tuple(dict.fromkeys(rejections or ("suggested_queries_produced_no_new_searches",)))
                if _only_budget_rejections(previous_rejections):
                    break
            if _retry_should_stop(
                retry_index=retry_index,
                max_retries=inputs.llm_query_retry_max,
                previous_rejections=previous_rejections,
                seen_failures=seen_retry_failures,
            ):
                break
            route = _post_parse_gap_retry_route(
                inputs=inputs,
                web_result=web_result,
                existing_route=route,
                retry_index=retry_index + 1,
                previous_rejections=previous_rejections,
            )
            retry_index += 1
            if route.status in {"provider_error", "invalid_provider_output", "disabled_no_provider"}:
                break
        return (), ()

    def _run_post_score_gap_expansion(
        self,
        *,
        inputs: FreeWebResearchInput,
        tracker: SearchBudgetTracker,
        results_by_query: dict[str, tuple[SearchResult, ...]],
        skipped: list[SkippedQuery],
        provider_errors: list[str],
        score: ScoreSnapshot,
        red_team: RedTeamAssessment,
        web_result: WebResearchResult,
        theme_route: ThemeRouteOutput | None,
        source_fields: Mapping[str, Any],
        agentic_evidence_trace: AgenticEvidenceRuntimeTrace | None = None,
    ) -> _ScoreGapExpansionResult:
        if not _post_score_gap_expansion_allowed(inputs, score):
            return _ScoreGapExpansionResult(status="disabled")
        archetype_id = _follow_up_archetype_id(
            theme_route,
            source_fields=source_fields,
            inputs=inputs,
        )
        score_gaps = _combined_score_gap_context(
            score,
            red_team,
            agentic_evidence_trace,
            archetype_id=archetype_id,
        )
        if not score_gaps:
            return _ScoreGapExpansionResult(status="no_gaps")
        agentic_follow_up = self._run_agentic_follow_up_gap_expansion(
            inputs=inputs,
            tracker=tracker,
            results_by_query=results_by_query,
            skipped=skipped,
            provider_errors=provider_errors,
            score_gaps=score_gaps,
            agentic_evidence_trace=agentic_evidence_trace,
            archetype_id=archetype_id,
        )
        if agentic_follow_up is not None:
            return agentic_follow_up
        seen_queries = set(results_by_query)
        previous_rejections: tuple[str, ...] = ()
        seen_retry_failures: set[tuple[str, ...]] = set()
        retry_index = 0
        while True:
            route = _score_gap_route(
                inputs=inputs,
                score=score,
                score_gaps=_score_gap_context_for_retry(score_gaps, retry_index, previous_rejections),
                web_result=web_result,
                theme_route=theme_route,
                source_fields=source_fields,
            )
            query_texts = _post_parse_gap_queries(inputs=inputs, route=route)
            if route.status in {"provider_error", "invalid_provider_output", "disabled_no_provider"}:
                return _ScoreGapExpansionResult(
                    status=route.status,
                    unresolved_gaps=tuple(score_gaps),
                    blocked_reason=route.blocked_reason,
                )
            if not query_texts:
                previous_rejections = ("llm_returned_no_suggested_queries",)
                if _retry_should_stop(
                    retry_index=retry_index,
                    max_retries=inputs.score_gap_query_retry_max,
                    previous_rejections=previous_rejections,
                    seen_failures=seen_retry_failures,
                ):
                    return _ScoreGapExpansionResult(
                        status="llm_no_suggested_queries",
                        unresolved_gaps=tuple(score_gaps),
                        rejection_reasons=previous_rejections,
                    )
                retry_index += 1
                continue

            specs: list[QuerySpec] = []
            queries_run: list[str] = []
            rejections: list[str] = []
            for query_index, query in enumerate(query_texts):
                safe_query = _asof_safe_theme_query(query, inputs.as_of_date)
                if safe_query is None:
                    skipped.append(SkippedQuery(query=query, layer=ResearchLayer.DEEP_RESEARCH, reason="future_query_rejected"))
                    rejections.append("future_query_rejected")
                    continue
                safe_query = _company_scoped_query(safe_query, inputs)
                if safe_query in seen_queries:
                    skipped.append(SkippedQuery(query=safe_query, layer=ResearchLayer.DEEP_RESEARCH, reason="duplicate_score_gap_query"))
                    rejections.append("duplicate_score_gap_query")
                    continue
                decision = tracker.can_run(inputs.symbol, ResearchLayer.DEEP_RESEARCH)
                if not decision.allowed:
                    reason = decision.reason or "budget_denied"
                    skipped.append(SkippedQuery(query=safe_query, layer=ResearchLayer.DEEP_RESEARCH, reason=reason))
                    rejections.append(reason)
                    continue
                spec = _post_score_gap_query_spec(query=safe_query, inputs=inputs, query_index=query_index)
                tracker.record_query(inputs.symbol, ResearchLayer.DEEP_RESEARCH)
                results = self._search_providers(spec, inputs, tracker, provider_errors)
                results_by_query[spec.query] = results
                seen_queries.add(spec.query)
                specs.append(spec)
                queries_run.append(spec.query)
                if tracker.stopped_reason:
                    break
                if inputs.budget.sleep_seconds_between_queries:
                    sleep(inputs.budget.sleep_seconds_between_queries)
            if specs or tracker.stopped_reason:
                status = "executed" if specs else (tracker.stopped_reason or "stopped")
                return _ScoreGapExpansionResult(
                    specs=tuple(specs),
                    queries_run=tuple(queries_run),
                    status=status,
                    unresolved_gaps=tuple(score_gaps),
                    rejection_reasons=tuple(dict.fromkeys(rejections)),
                    blocked_reason=tracker.stopped_reason,
                )
            previous_rejections = tuple(dict.fromkeys(rejections or ("suggested_queries_produced_no_new_searches",)))
            if _only_budget_rejections(previous_rejections):
                return _ScoreGapExpansionResult(
                    status="budget_blocked",
                    unresolved_gaps=tuple(score_gaps),
                    rejection_reasons=previous_rejections,
                )
            if _retry_should_stop(
                retry_index=retry_index,
                max_retries=inputs.score_gap_query_retry_max,
                previous_rejections=previous_rejections,
                seen_failures=seen_retry_failures,
            ):
                return _ScoreGapExpansionResult(
                    status="no_executable_searches",
                    unresolved_gaps=tuple(score_gaps),
                    rejection_reasons=previous_rejections,
                )
            retry_index += 1
        return _ScoreGapExpansionResult(status="stopped", unresolved_gaps=tuple(score_gaps), rejection_reasons=previous_rejections)

    def _run_agentic_follow_up_gap_expansion(
        self,
        *,
        inputs: FreeWebResearchInput,
        tracker: SearchBudgetTracker,
        results_by_query: dict[str, tuple[SearchResult, ...]],
        skipped: list[SkippedQuery],
        provider_errors: list[str],
        score_gaps: Sequence[str],
        agentic_evidence_trace: AgenticEvidenceRuntimeTrace | None = None,
        archetype_id: str | None = None,
    ) -> _ScoreGapExpansionResult | None:
        planner = inputs.agentic_follow_up_planner_provider
        if planner is None:
            return None
        previous_rejections: tuple[str, ...] = ()
        seen_retry_failures: set[tuple[str, ...]] = set()
        retry_index = 0
        while True:
            planning_input = FollowUpPlanningInput(
                target_entity_id=_agentic_target_entity_id(inputs),
                as_of_date=inputs.as_of_date,
                primitive_states=_follow_up_primitive_states(score_gaps, agentic_evidence_trace, archetype_id=archetype_id),
                target_names=_agentic_follow_up_target_names(inputs),
                stage_gate_context=_score_gap_context_for_retry(score_gaps, retry_index, previous_rejections),
                existing_queries=tuple(results_by_query),
                max_queries=_agentic_follow_up_max_queries(inputs),
                max_candidates=max(1, min(inputs.max_results_per_query, 100)),
                max_fetches=max(1, inputs.post_gap_fetch_results_per_query),
            )
            try:
                raw_plan = planner.plan(planning_input)
                if isinstance(raw_plan, Mapping):
                    raw_plan = decode_follow_up_planning_output(raw_plan)
                plan = validate_follow_up_plan(planning_input, raw_plan)
            except Exception as exc:
                return _ScoreGapExpansionResult(
                    status="agentic_follow_up_provider_error",
                    unresolved_gaps=tuple(score_gaps),
                    rejection_reasons=(f"{type(exc).__name__}:{str(exc)[:160]}",),
                    blocked_reason="agentic_follow_up_provider_error",
                )
            if not plan.suggested_queries:
                plan_status = str(plan.status or "").strip()
                rejection_items: list[str] = []
                if plan_status and plan_status != "ok":
                    rejection_items.append(plan_status)
                if "query_task_alignment_rejected" not in rejection_items:
                    rejection_items.insert(0, "agentic_follow_up_no_suggested_queries")
                previous_rejections = tuple(dict.fromkeys(rejection_items))
                if _retry_should_stop(
                    retry_index=retry_index,
                    max_retries=inputs.score_gap_query_retry_max,
                    previous_rejections=previous_rejections,
                    seen_failures=seen_retry_failures,
                ):
                    return _ScoreGapExpansionResult(
                        status="agentic_follow_up_no_suggested_queries",
                        unresolved_gaps=tuple(score_gaps),
                        rejection_reasons=previous_rejections,
                    )
                retry_index += 1
                continue
            tasks = plan.tasks or (_default_agentic_follow_up_task(inputs, planning_input),)
            tasks = _tasks_with_target_aliases(tasks, planning_input.target_names)
            tasks = _tasks_with_contract_source_quorum(
                tasks,
                archetype_id=archetype_id,
                as_of_date=inputs.as_of_date,
            )
            seen_queries = set(results_by_query)
            specs: list[QuerySpec] = []
            queries_run: list[str] = []
            rejections: list[str] = []
            source_route_plans: list[Mapping[str, object]] = []
            task_query_counts: dict[str, int] = {}
            for query_index, query in enumerate(plan.suggested_queries[: planning_input.max_queries]):
                task = _agentic_follow_up_task_for_query(tasks, query_index)
                used_for_task = task_query_counts.get(task.task_id, 0)
                if used_for_task >= task.max_queries:
                    rejections.append(f"task_query_limit_reached:{task.task_id}")
                    continue
                safe_query = _asof_safe_theme_query(query, inputs.as_of_date)
                if safe_query is None:
                    skipped.append(SkippedQuery(query=query, layer=ResearchLayer.DEEP_RESEARCH, reason="future_query_rejected"))
                    rejections.append("future_query_rejected")
                    continue
                safe_query = _company_scoped_query(safe_query, inputs)
                if safe_query in seen_queries:
                    skipped.append(SkippedQuery(query=safe_query, layer=ResearchLayer.DEEP_RESEARCH, reason="duplicate_agentic_follow_up_query"))
                    rejections.append("duplicate_agentic_follow_up_query")
                    continue
                decision = tracker.can_run(inputs.symbol, ResearchLayer.DEEP_RESEARCH)
                if not decision.allowed:
                    reason = decision.reason or "budget_denied"
                    skipped.append(SkippedQuery(query=safe_query, layer=ResearchLayer.DEEP_RESEARCH, reason=reason))
                    rejections.append(reason)
                    continue
                spec = _post_score_gap_query_spec(query=safe_query, inputs=inputs, query_index=query_index)
                tracker.record_query(inputs.symbol, ResearchLayer.DEEP_RESEARCH)
                raw_results = self._search_agentic_follow_up_sources(
                    spec=spec,
                    inputs=inputs,
                    tracker=tracker,
                    provider_errors=provider_errors,
                    task=task,
                )
                route_plan = _route_agentic_follow_up_plan(task=task, results=raw_results)
                source_route_plans.append(
                    _agentic_follow_up_route_plan_summary(
                        task=task,
                        query=safe_query,
                        plan=route_plan,
                    )
                )
                selected_results = _search_results_for_route_plan(raw_results, route_plan)
                if not selected_results:
                    skipped.append(SkippedQuery(query=safe_query, layer=ResearchLayer.DEEP_RESEARCH, reason="agentic_source_router_selected_no_candidates"))
                    rejections.append("agentic_source_router_selected_no_candidates")
                    if tracker.stopped_reason:
                        break
                    continue
                results_by_query[spec.query] = selected_results
                seen_queries.add(spec.query)
                specs.append(spec)
                queries_run.append(spec.query)
                task_query_counts[task.task_id] = used_for_task + 1
                if tracker.stopped_reason:
                    break
                if inputs.budget.sleep_seconds_between_queries:
                    sleep(inputs.budget.sleep_seconds_between_queries)
            if specs or tracker.stopped_reason:
                return _ScoreGapExpansionResult(
                    specs=tuple(specs),
                    queries_run=tuple(queries_run),
                    status="agentic_follow_up_executed" if specs else (tracker.stopped_reason or "stopped"),
                    unresolved_gaps=tuple(score_gaps),
                    rejection_reasons=tuple(dict.fromkeys(rejections)),
                    blocked_reason=tracker.stopped_reason,
                    diagnostic_details={
                        "post_score_gap_source_route_plans": tuple(source_route_plans),
                        "post_score_gap_query_origins": tuple(
                            "llm_follow_up_planner_suggested_query"
                            for _query in queries_run
                        ),
                        "post_score_gap_deterministic_fallback_query_used": False,
                    } if source_route_plans else {},
                )
            previous_rejections = tuple(dict.fromkeys(rejections or ("agentic_follow_up_no_executable_searches",)))
            if _only_budget_rejections(previous_rejections):
                return _ScoreGapExpansionResult(
                    status="budget_blocked",
                    unresolved_gaps=tuple(score_gaps),
                    rejection_reasons=previous_rejections,
                )
            if _retry_should_stop(
                retry_index=retry_index,
                max_retries=inputs.score_gap_query_retry_max,
                previous_rejections=previous_rejections,
                seen_failures=seen_retry_failures,
            ):
                return _ScoreGapExpansionResult(
                    status="agentic_follow_up_no_executable_searches",
                    unresolved_gaps=tuple(score_gaps),
                    rejection_reasons=previous_rejections,
            )
            retry_index += 1


def _theme_route_provider_for_timeout(
    provider: ThemeRouteProvider,
    *,
    timeout_seconds: float | None,
) -> ThemeRouteProvider:
    if timeout_seconds is None:
        return provider
    current_timeout = getattr(provider, "timeout_seconds", None)
    if current_timeout is None:
        return provider
    try:
        current = float(current_timeout)
        requested = float(timeout_seconds)
    except (TypeError, ValueError):
        return provider
    if current <= 0 or requested <= 0:
        return provider
    effective_timeout = min(current, requested)
    if effective_timeout == current:
        return provider
    if not is_dataclass(provider):
        return provider
    try:
        return replace(provider, timeout_seconds=effective_timeout)
    except TypeError:
        return provider


def _agentic_follow_up_task_for_query(
    tasks: Sequence[SourceAcquisitionTask],
    query_index: int,
) -> SourceAcquisitionTask:
    if not tasks:
        raise ValueError("at least one follow-up task is required")
    return tasks[min(query_index, len(tasks) - 1)]


def _tasks_with_target_aliases(
    tasks: Sequence[SourceAcquisitionTask],
    target_names: Sequence[str],
) -> tuple[SourceAcquisitionTask, ...]:
    aliases = tuple(dict.fromkeys(str(item).strip() for item in target_names if str(item).strip()))
    if not aliases:
        return tuple(tasks)
    enriched: list[SourceAcquisitionTask] = []
    for task in tasks:
        merged = tuple(dict.fromkeys((*task.target_aliases, *aliases)))
        enriched.append(replace(task, target_aliases=merged))
    return tuple(enriched)


def _has_agentic_evidence_providers(inputs: FreeWebResearchInput) -> bool:
    return bool(
        inputs.agentic_claim_extractor_provider is not None
        and inputs.agentic_claim_adjudicator_provider is not None
        and inputs.agentic_primitive_mapper_provider is not None
    )


def _combined_score_gap_context(
    score: ScoreSnapshot,
    red_team: RedTeamAssessment,
    agentic_evidence_trace: AgenticEvidenceRuntimeTrace | None = None,
    *,
    archetype_id: str | None = None,
) -> tuple[str, ...]:
    score_gaps = _filter_score_gaps_covered_by_agentic_primitives(
        _score_gap_missing_information(score),
        agentic_evidence_trace,
    )
    return tuple(
        dict.fromkeys(
            (
                *_agentic_primitive_gap_context(agentic_evidence_trace, archetype_id=archetype_id),
                *_agentic_rejection_gap_context(agentic_evidence_trace),
                *score_gaps,
                *_stage_gate_missing_information(score, red_team),
            )
        )
    )


def _filter_score_gaps_covered_by_agentic_primitives(
    gaps: Sequence[str],
    agentic_evidence_trace: AgenticEvidenceRuntimeTrace | None = None,
) -> tuple[str, ...]:
    if agentic_evidence_trace is None or not agentic_evidence_trace.primitive_states:
        return tuple(gaps)
    present_primitives = {
        state.primitive_id
        for state in agentic_evidence_trace.primitive_states
        if state.status == PrimitiveStatus.PRESENT_CURRENT
    }
    if not present_primitives:
        return tuple(gaps)
    filtered: list[str] = []
    for gap in gaps:
        gap_text = str(gap or "").casefold()
        covered = any(
            marker in gap_text and any(primitive_id in present_primitives for primitive_id in primitive_ids)
            for marker, primitive_ids in _SCORE_GAP_PRESENT_PRIMITIVE_COVERAGE
        )
        if not covered:
            filtered.append(gap)
    return tuple(filtered)


def _agentic_primitive_gap_context(
    agentic_evidence_trace: AgenticEvidenceRuntimeTrace | None,
    *,
    archetype_id: str | None = None,
) -> tuple[str, ...]:
    if agentic_evidence_trace is None or not agentic_evidence_trace.primitive_states:
        return ()
    gaps: list[str] = []
    for state in _ordered_agentic_primitive_states(agentic_evidence_trace.primitive_states, archetype_id=archetype_id):
        if state.status == PrimitiveStatus.PRESENT_CURRENT:
            continue
        materiality = _agentic_primitive_materiality_remaining(
            state.primitive_id,
            archetype_id=archetype_id,
            existing_materiality=state.materiality_remaining_points,
        )
        gaps.append(
            "agentic primitive gap:"
            f"{state.primitive_id}; status:{state.status.value}; "
            f"materiality:{round(float(materiality), 4)}; "
            f"evidence_need: source-backed current claim for {state.primitive_id}"
        )
    return tuple(dict.fromkeys(gaps))


def _agentic_rejection_gap_context(
    agentic_evidence_trace: AgenticEvidenceRuntimeTrace | None,
) -> tuple[str, ...]:
    if agentic_evidence_trace is None:
        return ()
    items: list[str] = []
    for summary in agentic_evidence_trace.eligibility_rejection_summaries[:8]:
        items.append(f"agentic eligibility rejection:{_agentic_compact_gap_context(summary)}")
    for summary in agentic_evidence_trace.rejected_mapping_summaries[:6]:
        items.append(f"agentic mapping rejection:{_agentic_compact_gap_context(summary)}")
    return tuple(dict.fromkeys(items))


def _agentic_compact_gap_context(value: object, *, max_chars: int = 280) -> str:
    clean = re.sub(r"\s+", " ", str(value or "")).strip()
    if len(clean) <= max_chars:
        return clean
    return f"{clean[: max_chars - 3].rstrip()}..."


def _follow_up_primitive_states(
    score_gaps: Sequence[str],
    agentic_evidence_trace: AgenticEvidenceRuntimeTrace | None = None,
    *,
    archetype_id: str | None = None,
) -> tuple[PrimitiveStateV2, ...]:
    if agentic_evidence_trace is not None and agentic_evidence_trace.primitive_states:
        ordered_states = _ordered_agentic_primitive_states(
            agentic_evidence_trace.primitive_states,
            archetype_id=archetype_id,
        )
        score_gap_states = _score_gap_follow_up_states(
            score_gaps,
            existing_primitive_ids=tuple(state.primitive_id for state in ordered_states),
        )
        missing = tuple(
            _follow_up_material_state(state, archetype_id=archetype_id)
            for state in ordered_states
            if state.status != PrimitiveStatus.PRESENT_CURRENT
        )
        present = tuple(
            state
            for state in ordered_states
            if state.status == PrimitiveStatus.PRESENT_CURRENT
        )
        return (*missing, *score_gap_states, *present)
    return _primitive_states_from_score_gaps(score_gaps)


def _ordered_agentic_primitive_states(
    states: Sequence[PrimitiveStateV2],
    *,
    archetype_id: str | None = None,
) -> tuple[PrimitiveStateV2, ...]:
    priorities = _agentic_contract_primitive_priorities(archetype_id)
    indexed = tuple(enumerate(states))
    return tuple(
        state
        for _index, state in sorted(
            indexed,
            key=lambda item: (
                item[1].status == PrimitiveStatus.PRESENT_CURRENT,
                priorities.get(item[1].primitive_id, 10_000),
                item[0],
            ),
        )
    )


def _agentic_contract_primitive_priorities(archetype_id: str | None) -> Mapping[str, int]:
    clean = str(archetype_id or "").strip()
    if not clean:
        return {}
    try:
        contract = load_evidence_contracts_v2().get(clean)
    except Exception:
        return {}
    if contract is None:
        return {}
    priorities: dict[str, int] = {}
    for index, primitive_id in enumerate(contract.green_gate.primitive_ids()):
        priorities.setdefault(primitive_id, index)
    offset = 1_000
    for index, primitive_id in enumerate(contract.required_primitives):
        priorities.setdefault(primitive_id, offset + index)
    offset = 2_000
    for index, primitive_id in enumerate(contract.alternative_primitives):
        priorities.setdefault(primitive_id, offset + index)
    return priorities


def _tasks_with_contract_source_quorum(
    tasks: Sequence[SourceAcquisitionTask],
    *,
    archetype_id: str | None,
    as_of_date: date | None = None,
) -> tuple[SourceAcquisitionTask, ...]:
    material_gap_enriched = tuple(_task_with_material_gap_source_preferences(task) for task in tasks)
    clean = str(archetype_id or "").strip()
    if not clean:
        return material_gap_enriched
    try:
        contract = load_evidence_contracts_v2().get(clean)
    except Exception:
        return material_gap_enriched
    if contract is None:
        return material_gap_enriched
    enriched: list[SourceAcquisitionTask] = []
    for task in material_gap_enriched:
        updated_task = task
        if not (task.source_quorum_min_official > 0 or task.source_quorum_min_independent_tier2 > 0):
            rule_id = _source_quorum_rule_id_for_task(contract, task)
            rule = contract.source_quorum.get(rule_id) if rule_id else None
            if rule is not None:
                updated_task = replace(
                    updated_task,
                    source_quorum_rule_id=rule_id,
                    source_quorum_min_official=rule.min_official,
                    source_quorum_min_independent_tier2=rule.min_independent_tier2,
                )
        enriched.append(
            _task_with_contract_primitive_aliases(
                _task_with_contract_freshness(
                    updated_task,
                    contract=contract,
                    as_of_date=as_of_date,
                ),
                contract=contract,
            ),
        )
    return tuple(enriched)


def _task_with_contract_primitive_aliases(
    task: SourceAcquisitionTask,
    *,
    contract: EvidenceContractV2,
) -> SourceAcquisitionTask:
    aliases = contract.primitive_aliases.get(task.primitive_gap)
    if not aliases:
        return task
    return replace(task, primitive_aliases=aliases)


def _task_with_material_gap_source_preferences(task: SourceAcquisitionTask) -> SourceAcquisitionTask:
    preferred = _material_gap_preferred_source_classes(task.primitive_gap)
    if not preferred:
        return task
    return replace(task, preferred_source_classes=preferred)


def _material_gap_preferred_source_classes(primitive_gap: str) -> tuple[str, ...]:
    marker = str(primitive_gap or "").casefold()
    if any(
        token in marker
        for token in (
            "emerging_theme",
            "theme_to_revenue",
            "green_unlock",
            "backlog_margin_bridge",
            "non_price_bridge",
            "theme_overheat",
        )
    ):
        return ("IR", "RESEARCH_REPORT", "FILING", "XBRL", "NEWS")
    if "cash_or_revision_conversion" not in marker and any(
        token in marker
        for token in ("selected_eps_source_missing", "selected_revision_source_missing", "consensus", "revision")
    ):
        return ("RESEARCH_REPORT", "API", "IR", "FILING")
    if any(token in marker for token in ("selected_fcf_source_missing", "cash_or_revision_conversion", "fcf", "cash")):
        return ("FILING", "XBRL", "IR", "RESEARCH_REPORT")
    if any(token in marker for token in ("selected_operating_profit_source_missing", "operating_profit", "op_source")):
        return ("FILING", "XBRL", "IR", "RESEARCH_REPORT")
    if any(token in marker for token in ("memory_price_increase_mentioned", "memory_price", "average_selling_price", "asp", "price_increase")):
        return ("IR", "RESEARCH_REPORT", "NEWS", "FILING")
    if any(token in marker for token in ("qualification_status", "customer_preorder_or_allocation", "hbm_capacity_pre_sold", "hbm_capacity_constraint")):
        return ("IR", "RESEARCH_REPORT", "NEWS", "FILING")
    return ()


def _source_quorum_rule_id_for_task(
    contract: EvidenceContractV2,
    task: SourceAcquisitionTask,
) -> str | None:
    marker = " ".join(
        (
            task.primitive_gap,
            task.required_source_tier or "",
            task.stop_condition,
            task.fallback_policy,
        )
    ).casefold()
    if any(token in marker for token in ("hard_break", "trust", "accounting", "risk", "guard", "red_team", "thesis_break")):
        if "hard_break" in contract.source_quorum:
            return "hard_break"
    if task.primitive_gap in contract.green_gate.primitive_ids() and "green_gate" in contract.source_quorum:
        return "green_gate"
    if "score_contribution" in contract.source_quorum:
        return "score_contribution"
    if "green_gate" in contract.source_quorum:
        return "green_gate"
    if "hard_break" in contract.source_quorum:
        return "hard_break"
    return None


def _task_with_contract_freshness(
    task: SourceAcquisitionTask,
    *,
    contract: EvidenceContractV2,
    as_of_date: date | None,
) -> SourceAcquisitionTask:
    if as_of_date is None:
        return task
    policy = contract.freshness.get(task.primitive_gap)
    if policy is None or policy.max_age_days is None:
        return task
    freshness_start = as_of_date - timedelta(days=policy.max_age_days)
    current_start, current_end = task.date_window or (None, None)
    start = max(item for item in (current_start, freshness_start) if item is not None)
    end = current_end if current_end is not None else as_of_date
    if end > as_of_date:
        end = as_of_date
    return replace(task, date_window=(start, end))


def _route_archetype_for_follow_up(theme_route: ThemeRouteOutput | None) -> str | None:
    if theme_route is None:
        return None
    return str(theme_route.canonical_archetype_id or "").strip() or None


def _follow_up_archetype_id(
    theme_route: ThemeRouteOutput | None,
    *,
    source_fields: Mapping[str, Any] | None = None,
    inputs: FreeWebResearchInput | None = None,
) -> str | None:
    route_archetype = _route_archetype_for_follow_up(theme_route)
    if route_archetype:
        return route_archetype
    fields = source_fields or {}
    for key in (
        "canonical_archetype_id",
        "evidence_contract_canonical_archetype_id",
        "evidence_contract_archetype_id",
    ):
        clean = str(fields.get(key) or "").strip()
        if clean:
            return clean
    if inputs is not None and inputs.base_feature_input is not None:
        clean = str(inputs.base_feature_input.canonical_archetype_id or "").strip()
        if clean:
            return clean
    return None


def _follow_up_material_state(
    state: PrimitiveStateV2,
    *,
    archetype_id: str | None = None,
) -> PrimitiveStateV2:
    materiality = _agentic_primitive_materiality_remaining(
        state.primitive_id,
        archetype_id=archetype_id,
        existing_materiality=state.materiality_remaining_points,
    )
    if materiality == state.materiality_remaining_points:
        return state
    return replace(state, materiality_remaining_points=materiality)


def _agentic_primitive_materiality_remaining(
    primitive_id: str,
    *,
    archetype_id: str | None = None,
    existing_materiality: float = 0.0,
) -> float:
    try:
        current = float(existing_materiality or 0.0)
    except (TypeError, ValueError):
        current = 0.0
    if current > 0.0:
        return current
    clean_archetype = str(archetype_id or "").strip()
    if not clean_archetype:
        return 5.0
    try:
        contract = load_evidence_contracts_v2().get(clean_archetype)
    except Exception:
        return 5.0
    if contract is None:
        return 5.0
    material_primitives = _contract_score_material_primitive_ids(contract)
    return 5.0 if primitive_id in material_primitives else 0.0


def _contract_score_material_primitive_ids(contract: EvidenceContractV2) -> set[str]:
    material = set(contract.required_primitives)
    material.update(contract.green_gate.primitive_ids())
    for primitives in contract.score_rubric.values():
        material.update(primitives)
    return material


def _primitive_states_from_score_gaps(score_gaps: Sequence[str]) -> tuple[PrimitiveStateV2, ...]:
    states: list[PrimitiveStateV2] = []
    for index, gap in enumerate(score_gaps):
        states.append(
            PrimitiveStateV2(
                primitive_id=_primitive_id_from_score_gap(gap, index),
                status=PrimitiveStatus.UNKNOWN,
                materiality_remaining_points=5.0,
            )
        )
    return tuple(states)


def _score_gap_follow_up_states(
    score_gaps: Sequence[str],
    *,
    existing_primitive_ids: Sequence[str],
) -> tuple[PrimitiveStateV2, ...]:
    existing = {str(item).strip() for item in existing_primitive_ids if str(item).strip()}
    states: list[PrimitiveStateV2] = []
    for index, gap in enumerate(_material_score_gaps(score_gaps)):
        primitive_id = _primitive_id_from_score_gap(gap, index)
        if primitive_id in existing:
            continue
        existing.add(primitive_id)
        materiality = _agentic_gap_materiality_value(str(gap))
        states.append(
            PrimitiveStateV2(
                primitive_id=primitive_id,
                status=PrimitiveStatus.UNKNOWN,
                materiality_remaining_points=materiality if materiality is not None and materiality > 0.0 else 5.0,
            )
        )
    return tuple(states)


def _primitive_id_from_score_gap(gap: str, index: int) -> str:
    text = str(gap)
    agentic_match = re.search(r"agentic\s+primitive\s+gap\s*:\s*([A-Za-z0-9_]+)", text, re.IGNORECASE)
    if agentic_match:
        return agentic_match.group(1).strip()
    lowered = text.casefold()
    if "emerging theme requires completed deep research" in lowered:
        return "emerging_theme_revenue_eps_fcf_rpo_backlog_margin_bridge"
    if "emerging theme green unlock evidence" in lowered:
        return "emerging_theme_green_unlock_revenue_fcf_contract_capacity_pricing_valuation"
    if "price-only blowoff guard" in lowered:
        return "price_only_blowoff_non_price_earnings_fcf_orders_backlog_bridge"
    if "theme overheat guard" in lowered:
        return "theme_overheat_revenue_eps_fcf_valuation_bridge"
    if "stage2 non-price bridge" in lowered:
        return "stage2_non_price_financial_disclosure_report_consensus_news_bridge"
    if "snippet-only" in lowered:
        return "snippet_only_full_source_document"
    if "date-unverified" in lowered:
        return "date_verified_full_source_document"
    head = text.split(";", 1)[0]
    head = re.sub(r"^score_gap:", "", head).strip().lower()
    clean = re.sub(r"[^a-z0-9_]+", "_", head).strip("_")
    return clean[:80] or f"score_gap_{index}"


def _agentic_follow_up_max_queries(inputs: FreeWebResearchInput) -> int:
    if inputs.post_parse_gap_expansion_max_queries is None:
        return 10
    return max(1, min(inputs.post_parse_gap_expansion_max_queries, 10))


def _agentic_follow_up_target_names(inputs: FreeWebResearchInput) -> tuple[str, ...]:
    names = (
        inputs.company_name,
        inputs.symbol,
        *inputs.company_aliases,
    )
    return tuple(dict.fromkeys(str(item).strip() for item in names if str(item).strip()))


def _default_agentic_follow_up_task(
    inputs: FreeWebResearchInput,
    planning_input: FollowUpPlanningInput,
) -> SourceAcquisitionTask:
    primitive_gap = planning_input.primitive_states[0].primitive_id if planning_input.primitive_states else "score_gap"
    return SourceAcquisitionTask(
        task_id=f"agentic-follow-up-{inputs.symbol}",
        target_entity_id=planning_input.target_entity_id,
        primitive_gap=primitive_gap,
        preferred_source_classes=("FILING", "IR", "RESEARCH_REPORT", "NEWS"),
        date_window=(None, inputs.as_of_date),
        required_source_tier=None,
        max_queries=planning_input.max_queries,
        max_candidates=planning_input.max_candidates,
        max_fetches=planning_input.max_fetches,
        stop_condition="bounded_source_router_selected_candidates",
        fallback_policy="official_first_then_independent_web",
        target_aliases=planning_input.target_names,
    )


def _route_agentic_follow_up_results(
    *,
    task: SourceAcquisitionTask,
    results: Sequence[SearchResult],
) -> tuple[SearchResult, ...]:
    return _search_results_for_route_plan(
        results,
        _route_agentic_follow_up_plan(task=task, results=results),
    )


def _route_agentic_follow_up_plan(
    *,
    task: SourceAcquisitionTask,
    results: Sequence[SearchResult],
) -> SourceRoutePlan:
    if not results:
        return build_source_route_plan(task=task, candidates=())
    candidates = tuple(
        _source_candidate_from_search_result(result, index=index)
        for index, result in enumerate(results)
    )
    return build_source_route_plan(task=task, candidates=candidates)


def _search_results_for_route_plan(
    results: Sequence[SearchResult],
    plan: SourceRoutePlan,
) -> tuple[SearchResult, ...]:
    selected_ids = {candidate.candidate_id for candidate in plan.selected_candidates}
    return tuple(
        result
        for index, result in enumerate(results)
        if _source_candidate_id(result, index) in selected_ids
    )


def _agentic_follow_up_route_plan_summary(
    *,
    task: SourceAcquisitionTask,
    query: str,
    plan: SourceRoutePlan,
) -> Mapping[str, object]:
    return {
        "task_id": task.task_id,
        "primitive_gap": task.primitive_gap,
        "query": query,
        "query_origin": "llm_follow_up_planner_suggested_query",
        "deterministic_fallback_query_used": False,
        "selected_candidate_ids": tuple(candidate.candidate_id for candidate in plan.selected_candidates),
        "selected_source_family_ids": tuple(candidate.source_family_id for candidate in plan.selected_candidates),
        "selected_candidate_titles": tuple(candidate.title for candidate in plan.selected_candidates),
        "selected_candidate_snippets": tuple(candidate.snippet for candidate in plan.selected_candidates),
        "selected_candidate_urls": tuple(candidate.url for candidate in plan.selected_candidates),
        "selected_candidate_source_types": tuple(candidate.source_type.value for candidate in plan.selected_candidates),
        "selected_candidate_tiers": tuple(candidate.tier for candidate in plan.selected_candidates),
        "selected_candidate_official": tuple(candidate.official for candidate in plan.selected_candidates),
        "selected_candidate_independent": tuple(candidate.independent for candidate in plan.selected_candidates),
        "selected_candidate_target_alias_counts": tuple(
            candidate_target_alias_count(task, candidate)
            for candidate in plan.selected_candidates
        ),
        "selected_candidate_target_alias_present": tuple(
            candidate_target_alias_present(task, candidate)
            for candidate in plan.selected_candidates
        ),
        "selected_candidate_cash_bridge_signal_counts": tuple(
            _source_candidate_cash_bridge_signal_count(candidate)
            for candidate in plan.selected_candidates
        ),
        "selected_candidate_cash_bridge_signal_present": tuple(
            _source_candidate_cash_bridge_signal_count(candidate) > 0
            for candidate in plan.selected_candidates
        ),
        "selected_candidate_target_scoped_cash_bridge_signal_counts": tuple(
            _source_candidate_target_scoped_cash_bridge_signal_count(task, candidate)
            for candidate in plan.selected_candidates
        ),
        "selected_candidate_target_scoped_cash_bridge_signal_present": tuple(
            _source_candidate_target_scoped_cash_bridge_signal_count(task, candidate) > 0
            for candidate in plan.selected_candidates
        ),
        "selected_candidate_primitive_operating_signal_counts": tuple(
            _source_candidate_primitive_operating_signal_count(task, candidate)
            for candidate in plan.selected_candidates
        ),
        "selected_candidate_primitive_operating_signal_present": tuple(
            _source_candidate_primitive_operating_signal_count(task, candidate) > 0
            for candidate in plan.selected_candidates
        ),
        "selected_candidate_published_dates": tuple(
            candidate.published_at.isoformat() if candidate.published_at is not None else None
            for candidate in plan.selected_candidates
        ),
        "selected_candidate_date_verified": tuple(candidate.date_verified for candidate in plan.selected_candidates),
        "skipped_candidate_ids": tuple(plan.skipped_candidate_ids),
        "skipped_candidate_reasons": dict(plan.skipped_candidate_reasons),
        "skipped_candidate_audit_rows": tuple(
            _source_candidate_audit_row(
                task=task,
                candidate=candidate,
                reason=plan.skipped_candidate_reasons.get(candidate.candidate_id, "not_selected"),
            )
            for candidate in plan.skipped_candidates
        ),
        "skipped_candidate_reason_counts": _source_route_skip_reason_counts(plan),
        "stop_condition_satisfied": plan.stop_condition_satisfied,
        "stop_reason": plan.stop_reason,
        "max_candidates": task.max_candidates,
        "max_fetches": task.max_fetches,
        "date_window": _source_task_date_window_summary(task),
        "preferred_source_classes": tuple(task.preferred_source_classes),
        "target_aliases": tuple(task.target_aliases),
        "primitive_aliases": tuple(task.primitive_aliases),
        "required_source_tier": task.required_source_tier,
        "stop_condition": task.stop_condition,
        "fallback_policy": task.fallback_policy,
        "source_quorum_rule_id": task.source_quorum_rule_id,
        "source_quorum_min_official": task.source_quorum_min_official,
        "source_quorum_min_independent_tier2": task.source_quorum_min_independent_tier2,
    }


def _source_candidate_cash_bridge_signal_count(candidate: SourceCandidate) -> int:
    text = f"{candidate.title} {candidate.snippet} {candidate.url or ''}"
    return cash_bridge_signal_count(text)


def _source_candidate_target_scoped_cash_bridge_signal_count(
    task: SourceAcquisitionTask,
    candidate: SourceCandidate,
) -> int:
    text = f"{candidate.title} {candidate.snippet} {candidate.url or ''}"
    if _source_candidate_cash_bridge_signal_count(candidate) <= 0:
        return 0
    if not candidate_target_alias_present(task, candidate):
        return 0
    aliases = _target_alias_terms_for_route_summary(task)
    if not aliases:
        return cash_bridge_signal_count(text)
    if candidate.official or candidate.source_type in {SourceType.FILING, SourceType.XBRL, SourceType.API}:
        return cash_bridge_signal_count(text)
    return sum(
        cash_bridge_signal_count(segment)
        for segment in _source_candidate_local_text_segments(candidate)
        if _route_summary_text_has_any_target_alias(segment, aliases)
    )


def _target_alias_terms_for_route_summary(task: SourceAcquisitionTask) -> tuple[str, ...]:
    if not task.target_aliases:
        return ()
    raw_aliases = [*task.target_aliases]
    target = str(task.target_entity_id or "").strip()
    if target:
        raw_aliases.append(target)
        tail = re.split(r"[:|/]", target)[-1].strip()
        if tail and tail != target:
            raw_aliases.append(tail)
    terms: list[str] = []
    seen: set[str] = set()
    for item in raw_aliases:
        term = str(item or "").casefold().strip()
        compact = _route_summary_compact_text(term)
        if len(compact) < 3:
            continue
        if term not in seen:
            seen.add(term)
            terms.append(term)
    return tuple(terms)


def _source_candidate_local_text_segments(candidate: SourceCandidate) -> tuple[str, ...]:
    segments: list[str] = []
    for part in (candidate.title, candidate.snippet, candidate.url or ""):
        text = str(part or "").strip()
        if not text:
            continue
        pieces = re.split(r"[\n\r]|(?<=[.!?。！？])\s+", text)
        segments.extend(piece.strip() for piece in pieces if piece.strip())
    return tuple(segments)


def _route_summary_text_has_any_target_alias(text: str, aliases: Sequence[str]) -> bool:
    marker = str(text or "").casefold()
    compact_marker = _route_summary_compact_text(marker)
    return any(alias in marker or _route_summary_compact_text(alias) in compact_marker for alias in aliases)


def _route_summary_compact_text(text: str) -> str:
    return re.sub(r"[\s\-_/.,:;()]+", "", str(text or "").casefold())


def _source_candidate_primitive_operating_signal_count(
    task: SourceAcquisitionTask,
    candidate: SourceCandidate,
) -> int:
    text = f"{candidate.title} {candidate.snippet} {candidate.url or ''}"
    return task_primitive_operating_signal_count(task, text)


def _source_candidate_audit_row(
    *,
    task: SourceAcquisitionTask,
    candidate: SourceCandidate,
    reason: str,
) -> Mapping[str, object]:
    return {
        "candidate_id": candidate.candidate_id,
        "source_family_id": candidate.source_family_id,
        "reason": reason,
        "title": candidate.title,
        "snippet": candidate.snippet,
        "url": candidate.url,
        "source_type": candidate.source_type.value,
        "tier": candidate.tier,
        "official": candidate.official,
        "independent": candidate.independent,
        "published_at": candidate.published_at.isoformat() if candidate.published_at is not None else None,
        "date_verified": candidate.date_verified,
        "target_alias_count": candidate_target_alias_count(task, candidate),
        "target_alias_present": candidate_target_alias_present(task, candidate),
        "cash_bridge_signal_count": _source_candidate_cash_bridge_signal_count(candidate),
        "target_scoped_cash_bridge_signal_count": _source_candidate_target_scoped_cash_bridge_signal_count(
            task,
            candidate,
        ),
        "primitive_operating_signal_count": _source_candidate_primitive_operating_signal_count(task, candidate),
    }


def _source_route_skip_reason_counts(plan: SourceRoutePlan) -> Mapping[str, int]:
    counts: dict[str, int] = {}
    for reason in plan.skipped_candidate_reasons.values():
        counts[reason] = counts.get(reason, 0) + 1
    return counts


def _source_task_date_window_summary(task: SourceAcquisitionTask) -> tuple[str | None, str | None] | None:
    if task.date_window is None:
        return None
    start, end = task.date_window
    return (
        start.isoformat() if start is not None else None,
        end.isoformat() if end is not None else None,
    )


def _search_optional_provider(
    *,
    provider: SearchProvider | None,
    query: str,
    as_of_date: date,
    max_results: int,
    provider_errors: list[str],
    error_prefix: str,
) -> tuple[SearchResult, ...]:
    if provider is None:
        return ()
    try:
        return tuple(provider.search(query, as_of_date, max_results))
    except Exception as exc:
        provider_errors.append(f"{error_prefix}:{type(exc).__name__}:{str(exc)[:160]}")
        return ()


def _agentic_task_can_stop_after_official(
    task: SourceAcquisitionTask,
    results: Sequence[SearchResult],
) -> bool:
    if not any(_source_candidate_from_search_result(result, index=index).official for index, result in enumerate(results)):
        return False
    marker = f"{task.stop_condition} {task.fallback_policy}".lower()
    return "official" in marker and ("stop" in marker or "first_official" in marker)


def _provider_fixture_text_by_url(provider: SearchProvider | None) -> Mapping[str, str | Path]:
    if provider is None or not hasattr(provider, "fixture_text_by_url"):
        return {}
    value = getattr(provider, "fixture_text_by_url")
    if not callable(value):
        return {}
    try:
        mapping = value()
    except Exception:
        return {}
    if not isinstance(mapping, Mapping):
        return {}
    return {
        str(url): text
        for url, text in mapping.items()
        if str(url).strip() and isinstance(text, (str, Path))
    }


def _source_candidate_from_search_result(result: SearchResult, *, index: int) -> SourceCandidate:
    source_type = _agentic_source_type(result)
    official = source_type in {SourceType.FILING, SourceType.XBRL, SourceType.API, SourceType.IR}
    tier = 1 if official else (2 if result.is_report_domain or result.is_news else 3)
    published = (
        result.published_at.date()
        if result.published_at
        else _agentic_infer_document_published_at(result)
    )
    date_verified = bool(result.date_verified or published is not None or (official and published is not None))
    green_allowed_by_date = bool(result.green_allowed_by_date or (official and published is not None))
    return SourceCandidate(
        candidate_id=_source_candidate_id(result, index),
        source_family_id=_search_result_source_family_id(result),
        source_type=source_type,
        tier=tier,
        url=result.url,
        title=result.title,
        snippet=result.snippet or "",
        published_at=published,
        date_verified=date_verified,
        green_allowed_by_date=green_allowed_by_date,
        official=official,
        detail_document=_agentic_source_is_detail_document(result),
        independent=not official,
        underlying_event_id=_search_result_underlying_event_id(result),
    )


def _agentic_source_is_detail_document(result: SearchResult) -> bool:
    url = str(result.url or "").strip().lower()
    source = str(result.source or "").strip().lower()
    return url.startswith("opendart-detail://") or "detail" in source


def _source_candidate_id(result: SearchResult, index: int) -> str:
    digest = hashlib.sha256(f"{result.url}\n{result.title}\n{index}".encode("utf-8")).hexdigest()
    return f"SRC-{digest[:20]}"


def _search_result_source_family_id(result: SearchResult) -> str:
    title_key = re.sub(r"\s+", " ", result.title.strip().lower())[:120]
    source_key = re.sub(r"\s+", "-", (result.source or "web").strip().lower())
    if result.is_disclosure or result.is_report_domain:
        return result.url
    if result.is_news:
        return f"news-event:{_search_result_underlying_event_id(result)}"
    return f"{source_key}:{title_key or result.url}"


def _search_result_underlying_event_id(result: SearchResult) -> str:
    published = result.published_at.date().isoformat() if result.published_at else "undated"
    title_key = re.sub(r"\s+", " ", result.title.strip().lower())[:120]
    return f"{published}:{title_key or result.url}"


def _apply_agentic_provider_bundle(inputs: FreeWebResearchInput, bundle: AgenticEvidenceProviderBundle) -> None:
    if inputs.agentic_claim_extractor_provider is None:
        object.__setattr__(inputs, "agentic_claim_extractor_provider", bundle.extractor)
    if inputs.agentic_claim_adjudicator_provider is None:
        object.__setattr__(inputs, "agentic_claim_adjudicator_provider", bundle.adjudicator)
    if inputs.agentic_primitive_mapper_provider is None:
        object.__setattr__(inputs, "agentic_primitive_mapper_provider", bundle.mapper)
    if inputs.agentic_follow_up_planner_provider is None:
        object.__setattr__(inputs, "agentic_follow_up_planner_provider", bundle.follow_up_planner)


def _apply_agentic_provider_timeout(inputs: FreeWebResearchInput) -> None:
    timeout_seconds = inputs.agentic_provider_timeout_seconds
    if timeout_seconds is None:
        return
    for attr in (
        "agentic_claim_extractor_provider",
        "agentic_claim_adjudicator_provider",
        "agentic_primitive_mapper_provider",
        "agentic_follow_up_planner_provider",
    ):
        provider = getattr(inputs, attr)
        if provider is None:
            continue
        object.__setattr__(inputs, attr, _provider_for_timeout(provider, timeout_seconds=timeout_seconds))


def _provider_for_timeout(provider: Any, *, timeout_seconds: float | None) -> Any:
    if timeout_seconds is None:
        return provider
    current_timeout = getattr(provider, "timeout_seconds", None)
    if current_timeout is None:
        return provider
    try:
        current = float(current_timeout)
        requested = float(timeout_seconds)
    except (TypeError, ValueError):
        return provider
    effective_timeout = min(current, requested)
    if effective_timeout == current:
        return provider
    try:
        return replace(provider, timeout_seconds=effective_timeout)
    except TypeError:
        return provider


def _agentic_evidence_archetype_for_workflow(
    *,
    inputs: FreeWebResearchInput,
    theme_route: ThemeRouteOutput | None,
    web_result: WebResearchResult | None = None,
) -> tuple[str, str | None]:
    route_canonical = str(theme_route.canonical_archetype_id or "").strip() if theme_route else ""
    if route_canonical:
        return route_canonical, "theme_route_canonical"
    if inputs.base_feature_input is not None:
        base_canonical = str(inputs.base_feature_input.canonical_archetype_id or "").strip()
        if base_canonical:
            return base_canonical, "base_feature_input"
    hint_archetype = _theme_route_archetype_hint(theme_route)
    if hint_archetype:
        return hint_archetype, "theme_route_hint"
    context_archetype = _context_contract_relevance_archetype_hint(
        inputs=inputs,
        theme_route=theme_route,
        web_result=web_result,
    )
    if context_archetype:
        return context_archetype, "context_contract_relevance"
    return "", None


def _context_contract_relevance_archetype_hint(
    *,
    inputs: FreeWebResearchInput,
    theme_route: ThemeRouteOutput | None,
    web_result: WebResearchResult | None,
) -> str | None:
    context_tokens = _agentic_text_tokens(
        _agentic_archetype_context_text(inputs=inputs, theme_route=theme_route, web_result=web_result)
    )
    if not context_tokens:
        return None
    try:
        contracts = load_evidence_contracts_v2()
    except Exception:
        return None
    scored: list[tuple[float, str]] = []
    for archetype_id, contract in sorted(contracts.items()):
        weights = dict(_agentic_contract_relevance_tokens(contract))
        for values in contract.route_hints.values():
            for value in values:
                for token in _agentic_text_tokens(value):
                    weights[token] = max(weights.get(token, 0.0), 4.0)
        score = sum(weight for token, weight in weights.items() if token in context_tokens)
        if score:
            scored.append((score, archetype_id))
    if not scored:
        return None
    scored.sort(reverse=True)
    top_score, top_archetype = scored[0]
    runner_up_score = scored[1][0] if len(scored) > 1 else 0.0
    if top_score < 25.0:
        return None
    if top_score - runner_up_score < 8.0:
        return None
    return top_archetype


def _agentic_archetype_context_text(
    *,
    inputs: FreeWebResearchInput,
    theme_route: ThemeRouteOutput | None,
    web_result: WebResearchResult | None,
) -> str:
    parts: list[str] = [
        inputs.company_name,
        inputs.symbol,
        inputs.sector or "",
        inputs.stage_context or "",
        " ".join(inputs.candidate_reason_codes),
    ]
    if theme_route is not None:
        parts.extend(
            (
                theme_route.emerging_theme_id or "",
                theme_route.primary_route_id or "",
                " ".join(theme_route.secondary_archetype_ids),
                " ".join(theme_route.missing_information),
                " ".join(theme_route.suggested_queries),
            )
    )
    if web_result is not None:
        for ranked in web_result.ranked_results[:40]:
            result = ranked.result
            parts.extend(
                (
                    result.title,
                    result.snippet or "",
                    result.query or "",
                    result.source,
                    result.url,
                )
            )
    return " ".join(part for part in parts if part).strip()


def _theme_route_archetype_hint(theme_route: ThemeRouteOutput | None) -> str | None:
    if theme_route is None:
        return None
    emerging_theme_id = _normalise_route_hint_value(theme_route.emerging_theme_id)
    if not emerging_theme_id:
        return None
    primary_route_id = _normalise_route_hint_value(theme_route.primary_route_id)
    try:
        contracts = load_evidence_contracts_v2()
    except Exception:
        return None
    matches: list[str] = []
    for archetype_id, contract in sorted(contracts.items()):
        emerging_hints = {
            _normalise_route_hint_value(item)
            for item in contract.route_hints.get("emerging_theme_ids", ())
        }
        if emerging_theme_id not in emerging_hints:
            continue
        primary_hints = {
            _normalise_route_hint_value(item)
            for item in contract.route_hints.get("primary_route_ids", ())
        }
        if primary_route_id and primary_hints and primary_route_id not in primary_hints:
            continue
        matches.append(archetype_id)
    if len(matches) != 1:
        return None
    return matches[0]


def _normalise_route_hint_value(value: object) -> str:
    return re.sub(r"\s+", "_", str(value or "").strip()).upper()


def _run_agentic_evidence_dual_run(
    *,
    inputs: FreeWebResearchInput,
    web_result: WebResearchResult,
    theme_route: ThemeRouteOutput | None,
    skip_document_ids: Sequence[str] = (),
    include_official_documents: bool = True,
) -> tuple[AgenticEvidenceRuntimeTrace, Mapping[str, object]]:
    if not inputs.agentic_evidence_enabled:
        trace = AgenticEvidenceRuntimeTrace(status="disabled")
        _emit_phase_event(inputs, "agentic_evidence_complete", status=trace.status)
        return trace, _agentic_evidence_diagnostics(trace, inputs=inputs)
    if not _has_agentic_evidence_providers(inputs):
        trace = AgenticEvidenceRuntimeTrace(status="disabled_no_provider")
        _emit_phase_event(inputs, "agentic_evidence_complete", status=trace.status)
        return trace, _agentic_evidence_diagnostics(trace, inputs=inputs)
    archetype_id, archetype_source = _agentic_evidence_archetype_for_workflow(
        inputs=inputs,
        theme_route=theme_route,
        web_result=web_result,
    )
    if not archetype_id:
        trace = AgenticEvidenceRuntimeTrace(status="skipped_no_archetype")
        _emit_phase_event(
            inputs,
            "agentic_evidence_complete",
            status=trace.status,
            fetched_document_count=len(web_result.fetched_documents),
        )
        return trace, _agentic_evidence_diagnostics(trace, inputs=inputs)
    try:
        contract = load_evidence_contracts_v2().get(archetype_id)
    except Exception as exc:  # pragma: no cover - config failures are surfaced as diagnostics.
        trace = AgenticEvidenceRuntimeTrace(
            status="contract_load_error",
            archetype_id=archetype_id,
            archetype_source=archetype_source,
            error_count=1,
            errors=(f"{type(exc).__name__}:{str(exc)[:180]}",),
        )
        _emit_phase_event(
            inputs,
            "agentic_evidence_complete",
            status=trace.status,
            archetype_id=archetype_id,
            archetype_source=archetype_source,
            error_count=trace.error_count,
        )
        return trace, _agentic_evidence_diagnostics(trace, inputs=inputs)
    if contract is None:
        trace = AgenticEvidenceRuntimeTrace(
            status="contract_missing",
            archetype_id=archetype_id,
            archetype_source=archetype_source,
        )
        _emit_phase_event(
            inputs,
            "agentic_evidence_complete",
            status=trace.status,
            archetype_id=archetype_id,
            archetype_source=archetype_source,
        )
        return trace, _agentic_evidence_diagnostics(trace, inputs=inputs)

    raw_document_inputs = _agentic_document_inputs(
        inputs=inputs,
        web_result=web_result,
        contract=contract,
        include_official_documents=include_official_documents,
    )
    document_inputs, skipped_existing_document_count = _filter_agentic_document_inputs_for_append_only(
        raw_document_inputs,
        skip_document_ids=skip_document_ids,
    )
    document_inputs = _limit_agentic_document_inputs(
        document_inputs,
        contract=contract,
        target_names=_agentic_follow_up_target_names(inputs),
        as_of_date=inputs.as_of_date,
        document_limit=inputs.agentic_evidence_document_limit,
    )
    _emit_phase_event(
        inputs,
        "agentic_evidence_start",
        archetype_id=archetype_id,
        archetype_source=archetype_source,
        fetched_document_count=len(web_result.fetched_documents),
        document_input_count=len(document_inputs),
        document_limit=inputs.agentic_evidence_document_limit,
        skipped_existing_document_count=skipped_existing_document_count,
        raw_assertion_budget_limit=inputs.agentic_max_raw_assertions_per_run,
        mapper_self_consistency_rounds=inputs.agentic_mapper_self_consistency_rounds,
        mapper_self_consistency_min_agreement=inputs.agentic_mapper_self_consistency_min_agreement,
        mapper_self_consistency_use_batch=inputs.agentic_mapper_self_consistency_use_batch,
        mapper_batch_max_tasks=inputs.agentic_mapper_batch_max_tasks,
    )
    if not document_inputs:
        status = "no_new_documents" if skipped_existing_document_count else "no_fetched_documents"
        trace = AgenticEvidenceRuntimeTrace(
            status=status,
            archetype_id=archetype_id,
            archetype_source=archetype_source,
            skipped_existing_document_count=skipped_existing_document_count,
        )
        _emit_phase_event(
            inputs,
            "agentic_evidence_complete",
            status=trace.status,
            archetype_id=archetype_id,
            archetype_source=archetype_source,
            document_count=trace.document_count,
        )
        return trace, _agentic_evidence_diagnostics(trace, inputs=inputs)

    target_entity_id = _agentic_target_entity_id(inputs)
    registry = EntityRegistry(
        {
            target_entity_id: EntityRecord(
                entity_id=target_entity_id,
                legal_name=inputs.company_name,
                aliases=tuple(dict.fromkeys((inputs.symbol, *inputs.company_aliases))),
                ticker=inputs.symbol,
                exchange=inputs.market.value,
            )
        }
    )
    def _agentic_workflow_event_sink(event: Mapping[str, Any]) -> None:
        phase = str(event.get("phase") or "agentic_evidence_workflow_event")
        payload = {key: value for key, value in event.items() if key != "phase"}
        context_document_id = workflow_event_context.get("document_id")
        if context_document_id and not payload.get("document_id"):
            payload["document_id"] = context_document_id
        _record_agentic_workflow_metrics(
            phase,
            payload,
            metrics=workflow_event_metrics,
        )
        _emit_phase_event(
            inputs,
            phase,
            archetype_id=archetype_id,
            archetype_source=archetype_source,
            **payload,
        )

    orchestrator = EvidenceWorkflowOrchestrator(
        extractor=inputs.agentic_claim_extractor_provider,
        adjudicator=inputs.agentic_claim_adjudicator_provider,
        mapper=inputs.agentic_primitive_mapper_provider,
        mapper_self_consistency_rounds=inputs.agentic_mapper_self_consistency_rounds,
        mapper_self_consistency_min_agreement=inputs.agentic_mapper_self_consistency_min_agreement,
        mapper_self_consistency_use_batch=inputs.agentic_mapper_self_consistency_use_batch,
        mapper_batch_max_tasks=inputs.agentic_mapper_batch_max_tasks,
        event_sink=_agentic_workflow_event_sink,
    )
    canonical_primitive_ids = _contract_canonical_primitive_ids(contract)
    document_count = 0
    raw_count = 0
    claim_count = 0
    accepted_mapping_count = 0
    rejected_mapping_count = 0
    claim_ids: list[str] = []
    mapping_ids: list[str] = []
    rejected_mapping_ids: list[str] = []
    rejected_mapping_summaries: list[str] = []
    eligibility_rejection_summaries: list[str] = []
    document_selection_summaries: list[str] = []
    document_ids: list[str] = []
    errors: list[str] = []
    workflow_event_context: dict[str, str | None] = {"document_id": None}
    workflow_event_metrics: dict[str, Any] = {
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
    combined_ledger = AppendOnlyEvidenceLedger()
    raw_budget_limit = inputs.agentic_max_raw_assertions_per_run
    raw_budget_limited = False
    for index, (document, text, anchors) in enumerate(document_inputs):
        max_raw_assertions = _agentic_document_raw_assertion_limit(
            raw_budget_limit=raw_budget_limit,
            raw_count=raw_count,
            document_index=index,
            document_count=len(document_inputs),
        )
        if max_raw_assertions == 0:
            raw_budget_limited = True
            _emit_phase_event(
                inputs,
                "agentic_evidence_document_skipped_budget",
                archetype_id=archetype_id,
                document_index=index,
                document_count=len(document_inputs),
                document_id=document.document_id,
                raw_assertion_count=raw_count,
                raw_assertion_budget_limit=raw_budget_limit,
            )
            break
        _emit_phase_event(
            inputs,
            "agentic_evidence_document_start",
            archetype_id=archetype_id,
            document_index=index,
            document_count=len(document_inputs),
            document_id=document.document_id,
            source_type=document.source_type.value,
            max_raw_assertions=max_raw_assertions,
            raw_assertion_count_before=raw_count,
        )
        try:
            workflow_event_context["document_id"] = document.document_id
            result = orchestrator.compile(
                EvidenceCompilationInput(
                    target_entity_id=target_entity_id,
                    target_names=tuple(dict.fromkeys((inputs.company_name, inputs.symbol, *inputs.company_aliases))),
                    as_of_date=inputs.as_of_date,
                    document=document,
                    document_text=text,
                    anchors=anchors,
                    entity_registry=registry,
                    contract=contract,
                    canonical_primitive_ids=canonical_primitive_ids,
                    max_raw_assertions=max_raw_assertions,
                )
            )
        except Exception as exc:
            errors.append(f"{document.document_id}:{type(exc).__name__}:{str(exc)[:160]}")
            _emit_phase_event(
                inputs,
                "agentic_evidence_document_error",
                archetype_id=archetype_id,
                document_index=index,
                document_count=len(document_inputs),
                document_id=document.document_id,
                error_type=type(exc).__name__,
                error=str(exc)[:160],
            )
            continue
        finally:
            workflow_event_context["document_id"] = None
        if result.raw_assertion_budget_truncated:
            raw_budget_limited = True
        document_count += 1
        document_ids.append(document.document_id)
        document_selection_summaries.append(
            _agentic_document_selection_summary(
                document,
                text,
                contract=contract,
                target_names=_agentic_follow_up_target_names(inputs),
                as_of_date=inputs.as_of_date,
            )
        )
        raw_count += len(result.raw_assertions)
        claim_count += len(result.adjudicated_claims)
        accepted_mapping_count += len(result.accepted_mappings)
        rejected_mapping_count += result.rejected_mapping_count
        claim_ids.extend(claim.claim_id for claim in result.adjudicated_claims)
        mapping_ids.extend(mapping.mapping_id for mapping in result.accepted_mappings)
        rejected_mapping_ids.extend(mapping.mapping_id for mapping in result.rejected_mappings)
        rejected_mapping_summaries.extend(
            _agentic_rejected_mapping_summary(mapping)
            for mapping in result.rejected_mappings
            if mapping.mapping_status != MappingStatus.ACCEPTED
        )
        eligibility_rejection_summaries.extend(result.eligibility_rejection_summaries)
        for claim in result.adjudicated_claims:
            combined_ledger.append_claim(claim)
        for mapping in result.accepted_mappings:
            combined_ledger.append_mapping(mapping)
        _emit_phase_event(
            inputs,
            "agentic_evidence_document_complete",
            archetype_id=archetype_id,
            document_index=index,
            document_count=len(document_inputs),
            document_id=document.document_id,
            raw_assertion_count=len(result.raw_assertions),
            claim_count=len(result.adjudicated_claims),
            accepted_mapping_count=len(result.accepted_mappings),
            rejected_mapping_count=result.rejected_mapping_count,
            raw_assertion_budget_truncated=result.raw_assertion_budget_truncated,
            cumulative_raw_assertion_count=raw_count,
            cumulative_accepted_mapping_count=accepted_mapping_count,
        )
        if raw_budget_limit is not None and raw_count >= raw_budget_limit and index < len(document_inputs) - 1:
            raw_budget_limited = True
            break
    status = "completed" if not errors else ("partial_error" if document_count else "provider_error")
    if raw_budget_limited and status == "completed":
        status = "completed_budget_limited"
    elif raw_budget_limited and status == "partial_error":
        status = "partial_error_budget_limited"
    primitive_states = tuple(
        aggregate_primitive_states(
            ledger=combined_ledger,
            contract=contract,
            as_of_date=inputs.as_of_date,
            extra_primitive_ids=canonical_primitive_ids,
        ).values()
    )
    trace = AgenticEvidenceRuntimeTrace(
        status=status,
        archetype_id=archetype_id,
        archetype_source=archetype_source,
        raw_assertion_budget_limited=raw_budget_limited,
        raw_assertion_budget_limit=raw_budget_limit,
        document_count=document_count,
        raw_assertion_count=raw_count,
        adjudicated_claim_count=claim_count,
        accepted_mapping_count=accepted_mapping_count,
        rejected_mapping_count=rejected_mapping_count,
        mapping_prefilter_original_task_count=int(
            workflow_event_metrics.get("mapping_prefilter_original_task_count") or 0
        ),
        mapping_prefilter_filtered_task_count=int(
            workflow_event_metrics.get("mapping_prefilter_filtered_task_count") or 0
        ),
        mapping_prefilter_skipped_input_count=int(
            workflow_event_metrics.get("mapping_prefilter_skipped_input_count") or 0
        ),
        mapping_prefilter_fallback_full_map_count=int(
            workflow_event_metrics.get("mapping_prefilter_fallback_full_map_count") or 0
        ),
        mapping_empty_output_count=int(workflow_event_metrics.get("mapping_empty_output_count") or 0),
        mapping_empty_output_retry_count=int(
            workflow_event_metrics.get("mapping_empty_output_retry_count") or 0
        ),
        mapping_empty_output_recovered_count=int(
            workflow_event_metrics.get("mapping_empty_output_recovered_count") or 0
        ),
        mapping_empty_output_summaries=tuple(
            dict.fromkeys(workflow_event_metrics.get("mapping_empty_output_summaries") or ())
        )[:20],
        mapping_empty_output_retry_summaries=tuple(
            dict.fromkeys(workflow_event_metrics.get("mapping_empty_output_retry_summaries") or ())
        )[:20],
        mapping_prefilter_fallback_full_map_summaries=tuple(
            dict.fromkeys(workflow_event_metrics.get("mapping_prefilter_fallback_full_map_summaries") or ())
        )[:20],
        claim_ids=tuple(dict.fromkeys(claim_ids)),
        mapping_ids=tuple(dict.fromkeys(mapping_ids)),
        rejected_mapping_ids=tuple(dict.fromkeys(rejected_mapping_ids)),
        rejected_mapping_summaries=tuple(dict.fromkeys(rejected_mapping_summaries))[:20],
        eligibility_rejection_summaries=tuple(dict.fromkeys(eligibility_rejection_summaries))[:20],
        document_selection_summaries=tuple(document_selection_summaries[:20]),
        document_ids=tuple(dict.fromkeys(document_ids)),
        skipped_existing_document_count=skipped_existing_document_count,
        primitive_states=primitive_states,
        error_count=len(errors),
        errors=tuple(errors[:20]),
    )
    _emit_phase_event(
        inputs,
        "agentic_evidence_complete",
        status=trace.status,
        archetype_id=archetype_id,
        archetype_source=archetype_source,
        document_count=trace.document_count,
        raw_assertion_count=trace.raw_assertion_count,
        claim_count=trace.adjudicated_claim_count,
        accepted_mapping_count=trace.accepted_mapping_count,
        mapping_prefilter_original_task_count=trace.mapping_prefilter_original_task_count,
        mapping_prefilter_filtered_task_count=trace.mapping_prefilter_filtered_task_count,
        mapping_prefilter_fallback_full_map_count=trace.mapping_prefilter_fallback_full_map_count,
        mapping_empty_output_count=trace.mapping_empty_output_count,
        mapping_empty_output_retry_count=trace.mapping_empty_output_retry_count,
        mapping_empty_output_recovered_count=trace.mapping_empty_output_recovered_count,
        raw_assertion_budget_limited=trace.raw_assertion_budget_limited,
        error_count=trace.error_count,
    )
    return trace, _agentic_evidence_diagnostics(trace, inputs=inputs)


def _agentic_document_raw_assertion_limit(
    *,
    raw_budget_limit: int | None,
    raw_count: int,
    document_index: int,
    document_count: int,
) -> int | None:
    if raw_budget_limit is None:
        return None
    remaining_budget = raw_budget_limit - raw_count
    if remaining_budget <= 0:
        return 0
    remaining_documents = max(0, document_count - document_index - 1)
    if remaining_documents == 0:
        return remaining_budget
    remaining_slots = remaining_documents + 1
    return max(1, remaining_budget // remaining_slots)


def _agentic_evidence_diagnostics(
    trace: AgenticEvidenceRuntimeTrace,
    *,
    inputs: FreeWebResearchInput | None = None,
) -> Mapping[str, object]:
    present = tuple(
        state.primitive_id
        for state in trace.primitive_states
        if state.status == PrimitiveStatus.PRESENT_CURRENT and (state.support_claim_ids or state.counter_claim_ids)
    )
    contradicted = tuple(
        state.primitive_id
        for state in trace.primitive_states
        if state.status == PrimitiveStatus.CONTRADICTED
    )
    diagnostics = {
        "agentic_evidence_status": trace.status,
        "agentic_evidence_archetype_id": trace.archetype_id,
        "agentic_evidence_archetype_source": trace.archetype_source,
        "agentic_evidence_raw_assertion_budget_limited": trace.raw_assertion_budget_limited,
        "agentic_evidence_raw_assertion_budget_limit": trace.raw_assertion_budget_limit,
        "agentic_evidence_document_count": trace.document_count,
        "agentic_evidence_raw_assertion_count": trace.raw_assertion_count,
        "agentic_evidence_claim_count": trace.adjudicated_claim_count,
        "agentic_evidence_accepted_mapping_count": trace.accepted_mapping_count,
        "agentic_evidence_rejected_mapping_count": trace.rejected_mapping_count,
        "agentic_evidence_mapping_prefilter_original_task_count": trace.mapping_prefilter_original_task_count,
        "agentic_evidence_mapping_prefilter_filtered_task_count": trace.mapping_prefilter_filtered_task_count,
        "agentic_evidence_mapping_prefilter_skipped_input_count": trace.mapping_prefilter_skipped_input_count,
        "agentic_evidence_mapping_prefilter_fallback_full_map_count": (
            trace.mapping_prefilter_fallback_full_map_count
        ),
        "agentic_evidence_mapping_prefilter_fallback_full_map_summaries": (
            trace.mapping_prefilter_fallback_full_map_summaries
        ),
        "agentic_evidence_mapping_empty_output_count": trace.mapping_empty_output_count,
        "agentic_evidence_mapping_empty_output_retry_count": trace.mapping_empty_output_retry_count,
        "agentic_evidence_mapping_empty_output_recovered_count": trace.mapping_empty_output_recovered_count,
        "agentic_evidence_mapping_empty_output_summaries": trace.mapping_empty_output_summaries,
        "agentic_evidence_mapping_empty_output_retry_summaries": trace.mapping_empty_output_retry_summaries,
        "agentic_evidence_error_count": trace.error_count,
        "agentic_evidence_claim_ids": trace.claim_ids,
        "agentic_evidence_mapping_ids": trace.mapping_ids,
        "agentic_evidence_rejected_mapping_ids": trace.rejected_mapping_ids,
        "agentic_evidence_rejected_mapping_summaries": trace.rejected_mapping_summaries,
        "agentic_evidence_eligibility_rejection_summaries": trace.eligibility_rejection_summaries,
        "agentic_evidence_document_selection_summaries": trace.document_selection_summaries,
        "agentic_evidence_document_ids": _agentic_trace_document_ids(trace),
        "agentic_evidence_skipped_existing_document_count": trace.skipped_existing_document_count,
        "agentic_evidence_errors": trace.errors,
        "agentic_evidence_primitive_state_count": len(trace.primitive_states),
        "agentic_evidence_present_primitives": present,
        "agentic_evidence_contradicted_primitives": contradicted,
        "agentic_evidence_primitive_statuses": tuple(
            f"{state.primitive_id}:{state.status.value}" for state in trace.primitive_states
        ),
    }
    if inputs is not None:
        diagnostics.update(
            {
                "agentic_evidence_enabled": bool(inputs.agentic_evidence_enabled),
                "agentic_evidence_required_for_scoring": bool(inputs.agentic_evidence_enabled),
                "agentic_evidence_provider_configured": _has_agentic_evidence_providers(inputs),
                "agentic_evidence_mapper_self_consistency_rounds": inputs.agentic_mapper_self_consistency_rounds,
                "agentic_evidence_mapper_self_consistency_min_agreement": (
                    inputs.agentic_mapper_self_consistency_min_agreement
                ),
                "agentic_evidence_mapper_self_consistency_use_batch": (
                    inputs.agentic_mapper_self_consistency_use_batch
                ),
                "agentic_evidence_mapper_batch_max_tasks": inputs.agentic_mapper_batch_max_tasks,
                "agentic_evidence_document_limit": inputs.agentic_evidence_document_limit,
                "agentic_evidence_max_raw_assertions_per_run": inputs.agentic_max_raw_assertions_per_run,
                "agentic_evidence_provider_timeout_seconds": inputs.agentic_provider_timeout_seconds,
            }
        )
    return diagnostics


def _merge_agentic_evidence_runtime_traces(
    previous: AgenticEvidenceRuntimeTrace,
    current: AgenticEvidenceRuntimeTrace,
) -> AgenticEvidenceRuntimeTrace:
    if previous.status == "disabled" and not previous.primitive_states:
        return current
    if current.status == "disabled" and not current.primitive_states:
        return previous
    if current.status == "no_new_documents" and not current.primitive_states:
        return AgenticEvidenceRuntimeTrace(
            status=previous.status,
            archetype_id=previous.archetype_id,
            archetype_source=previous.archetype_source,
            raw_assertion_budget_limited=previous.raw_assertion_budget_limited,
            raw_assertion_budget_limit=previous.raw_assertion_budget_limit,
            document_count=previous.document_count,
            raw_assertion_count=previous.raw_assertion_count,
            adjudicated_claim_count=previous.adjudicated_claim_count,
            accepted_mapping_count=previous.accepted_mapping_count,
            rejected_mapping_count=previous.rejected_mapping_count,
            mapping_prefilter_original_task_count=previous.mapping_prefilter_original_task_count,
            mapping_prefilter_filtered_task_count=previous.mapping_prefilter_filtered_task_count,
            mapping_prefilter_skipped_input_count=previous.mapping_prefilter_skipped_input_count,
            mapping_prefilter_fallback_full_map_count=previous.mapping_prefilter_fallback_full_map_count,
            mapping_empty_output_count=previous.mapping_empty_output_count,
            mapping_empty_output_retry_count=previous.mapping_empty_output_retry_count,
            mapping_empty_output_recovered_count=previous.mapping_empty_output_recovered_count,
            mapping_empty_output_summaries=previous.mapping_empty_output_summaries,
            mapping_empty_output_retry_summaries=previous.mapping_empty_output_retry_summaries,
            mapping_prefilter_fallback_full_map_summaries=(
                previous.mapping_prefilter_fallback_full_map_summaries
            ),
            claim_ids=previous.claim_ids,
            mapping_ids=previous.mapping_ids,
            rejected_mapping_ids=previous.rejected_mapping_ids,
            rejected_mapping_summaries=previous.rejected_mapping_summaries,
            eligibility_rejection_summaries=previous.eligibility_rejection_summaries,
            document_selection_summaries=previous.document_selection_summaries,
            document_ids=_agentic_trace_document_ids(previous),
            skipped_existing_document_count=(
                previous.skipped_existing_document_count + current.skipped_existing_document_count
            ),
            primitive_states=previous.primitive_states,
            error_count=previous.error_count,
            errors=previous.errors,
        )
    previous_states = {state.primitive_id: state for state in previous.primitive_states}
    current_states = {state.primitive_id: state for state in current.primitive_states}
    merged_states = tuple(
        _merge_primitive_state(previous_states.get(primitive_id), current_states.get(primitive_id))
        for primitive_id in sorted({*previous_states, *current_states})
    )
    claim_ids = tuple(dict.fromkeys((*previous.claim_ids, *current.claim_ids)))
    mapping_ids = tuple(dict.fromkeys((*previous.mapping_ids, *current.mapping_ids)))
    rejected_mapping_ids = tuple(dict.fromkeys((*previous.rejected_mapping_ids, *current.rejected_mapping_ids)))
    rejected_mapping_summaries = tuple(
        dict.fromkeys((*previous.rejected_mapping_summaries, *current.rejected_mapping_summaries))
    )[:20]
    eligibility_rejection_summaries = tuple(
        dict.fromkeys((*previous.eligibility_rejection_summaries, *current.eligibility_rejection_summaries))
    )[:20]
    document_selection_summaries = tuple(
        dict.fromkeys((*previous.document_selection_summaries, *current.document_selection_summaries))
    )[:20]
    document_ids = tuple(dict.fromkeys((*_agentic_trace_document_ids(previous), *_agentic_trace_document_ids(current))))
    errors = tuple(dict.fromkeys((*previous.errors, *current.errors)))[:20]
    mapping_empty_output_summaries = tuple(
        dict.fromkeys((*previous.mapping_empty_output_summaries, *current.mapping_empty_output_summaries))
    )[:20]
    mapping_empty_output_retry_summaries = tuple(
        dict.fromkeys(
            (*previous.mapping_empty_output_retry_summaries, *current.mapping_empty_output_retry_summaries)
        )
    )[:20]
    mapping_prefilter_fallback_full_map_summaries = tuple(
        dict.fromkeys(
            (
                *previous.mapping_prefilter_fallback_full_map_summaries,
                *current.mapping_prefilter_fallback_full_map_summaries,
            )
        )
    )[:20]
    return AgenticEvidenceRuntimeTrace(
        status=_merged_agentic_trace_status(previous.status, current.status),
        archetype_id=current.archetype_id or previous.archetype_id,
        archetype_source=current.archetype_source or previous.archetype_source,
        raw_assertion_budget_limited=previous.raw_assertion_budget_limited or current.raw_assertion_budget_limited,
        raw_assertion_budget_limit=current.raw_assertion_budget_limit or previous.raw_assertion_budget_limit,
        document_count=len(document_ids) if document_ids else max(previous.document_count, current.document_count),
        raw_assertion_count=max(previous.raw_assertion_count, current.raw_assertion_count),
        adjudicated_claim_count=len(claim_ids) if claim_ids else max(previous.adjudicated_claim_count, current.adjudicated_claim_count),
        accepted_mapping_count=len(mapping_ids) if mapping_ids else max(previous.accepted_mapping_count, current.accepted_mapping_count),
        rejected_mapping_count=max(previous.rejected_mapping_count, current.rejected_mapping_count),
        mapping_prefilter_original_task_count=(
            previous.mapping_prefilter_original_task_count + current.mapping_prefilter_original_task_count
        ),
        mapping_prefilter_filtered_task_count=(
            previous.mapping_prefilter_filtered_task_count + current.mapping_prefilter_filtered_task_count
        ),
        mapping_prefilter_skipped_input_count=(
            previous.mapping_prefilter_skipped_input_count + current.mapping_prefilter_skipped_input_count
        ),
        mapping_prefilter_fallback_full_map_count=(
            previous.mapping_prefilter_fallback_full_map_count + current.mapping_prefilter_fallback_full_map_count
        ),
        mapping_empty_output_count=previous.mapping_empty_output_count + current.mapping_empty_output_count,
        mapping_empty_output_retry_count=(
            previous.mapping_empty_output_retry_count + current.mapping_empty_output_retry_count
        ),
        mapping_empty_output_recovered_count=(
            previous.mapping_empty_output_recovered_count + current.mapping_empty_output_recovered_count
        ),
        mapping_empty_output_summaries=mapping_empty_output_summaries,
        mapping_empty_output_retry_summaries=mapping_empty_output_retry_summaries,
        mapping_prefilter_fallback_full_map_summaries=mapping_prefilter_fallback_full_map_summaries,
        claim_ids=claim_ids,
        mapping_ids=mapping_ids,
        rejected_mapping_ids=rejected_mapping_ids,
        rejected_mapping_summaries=rejected_mapping_summaries,
        eligibility_rejection_summaries=eligibility_rejection_summaries,
        document_selection_summaries=document_selection_summaries,
        document_ids=document_ids,
        skipped_existing_document_count=(
            previous.skipped_existing_document_count + current.skipped_existing_document_count
        ),
        primitive_states=merged_states,
        error_count=len(errors),
        errors=errors,
    )


def _agentic_trace_document_ids(trace: AgenticEvidenceRuntimeTrace | None) -> tuple[str, ...]:
    if trace is None:
        return ()
    explicit_ids = tuple(str(item).strip() for item in getattr(trace, "document_ids", ()) if str(item).strip())
    if explicit_ids:
        return tuple(dict.fromkeys(explicit_ids))
    parsed: list[str] = []
    for summary in getattr(trace, "document_selection_summaries", ()) or ():
        document_id = str(summary).split("|", 1)[0].strip()
        if document_id:
            parsed.append(document_id)
    return tuple(dict.fromkeys(parsed))


def _score_gap_progress_diagnostics(
    *,
    previous_trace: AgenticEvidenceRuntimeTrace | None,
    current_trace: AgenticEvidenceRuntimeTrace | None,
    merged_trace: AgenticEvidenceRuntimeTrace | None = None,
    archetype_id: str | None = None,
    previous_signature: Sequence[str],
    current_signature: Sequence[str],
    previous_score_contributions: Sequence[ScoreContributionV2] = (),
    current_score_contributions: Sequence[ScoreContributionV2] = (),
) -> Mapping[str, object]:
    previous_document_ids = set(_agentic_trace_document_ids(previous_trace))
    current_document_ids = _agentic_trace_document_ids(current_trace)
    reprocessed_document_ids = tuple(
        document_id for document_id in current_document_ids if document_id in previous_document_ids
    )
    new_document_ids = tuple(document_id for document_id in current_document_ids if document_id not in previous_document_ids)
    previous_claim_ids = set(getattr(previous_trace, "claim_ids", ()) or ())
    current_claim_ids = tuple(getattr(current_trace, "claim_ids", ()) or ())
    new_claim_ids = tuple(claim_id for claim_id in current_claim_ids if claim_id not in previous_claim_ids)
    previous_mapping_ids = set(getattr(previous_trace, "mapping_ids", ()) or ())
    current_mapping_ids = tuple(getattr(current_trace, "mapping_ids", ()) or ())
    new_mapping_ids = tuple(mapping_id for mapping_id in current_mapping_ids if mapping_id not in previous_mapping_ids)
    previous_rejected_mapping_ids = set(getattr(previous_trace, "rejected_mapping_ids", ()) or ())
    current_rejected_mapping_ids = tuple(getattr(current_trace, "rejected_mapping_ids", ()) or ())
    new_rejected_mapping_ids = tuple(
        mapping_id for mapping_id in current_rejected_mapping_ids if mapping_id not in previous_rejected_mapping_ids
    )
    new_rejected_mapping_summaries = _summaries_for_mapping_ids(
        getattr(current_trace, "rejected_mapping_summaries", ()) or (),
        new_rejected_mapping_ids,
    )
    previous_eligibility_rejection_summaries = set(
        getattr(previous_trace, "eligibility_rejection_summaries", ()) or ()
    )
    current_eligibility_rejection_summaries = tuple(
        getattr(current_trace, "eligibility_rejection_summaries", ()) or ()
    )
    new_eligibility_rejection_summaries = tuple(
        summary
        for summary in current_eligibility_rejection_summaries
        if summary not in previous_eligibility_rejection_summaries
    )[:20]
    new_trace_errors = tuple(getattr(current_trace, "errors", ()) or ())
    signature_changed = tuple(previous_signature) != tuple(current_signature)
    current_status = str(getattr(current_trace, "status", "") or "")
    primitive_comparison_trace = merged_trace if merged_trace is not None else current_trace
    primitive_delta_summaries = _primitive_state_delta_summaries(previous_trace, primitive_comparison_trace)
    unchanged_gap_primitive_summaries = _unchanged_gap_primitive_summaries(
        previous_trace,
        primitive_comparison_trace,
        archetype_id=archetype_id,
    )
    contribution_delta_summaries = _score_contribution_delta_summaries(
        previous_score_contributions,
        current_score_contributions,
    )
    evidence_progress_without_score_change = bool(
        not signature_changed
        and (
            primitive_delta_summaries
            or contribution_delta_summaries
        )
    )
    if reprocessed_document_ids:
        reason = "score_gap_reprocessed_existing_documents"
    elif signature_changed:
        reason = "score_gap_changed_score_state"
    elif evidence_progress_without_score_change:
        reason = "score_gap_evidence_progress_without_score_state_change"
    elif not new_document_ids:
        reason = "score_gap_no_new_documents"
    elif not new_claim_ids:
        reason = "score_gap_new_documents_without_claims"
    elif not new_mapping_ids:
        reason = "score_gap_new_claims_without_accepted_mappings"
    else:
        reason = "score_gap_new_accepted_mappings_without_score_state_change"
    return {
        "post_score_gap_progress_reason": reason,
        "post_score_gap_score_state_changed": signature_changed,
        "post_score_gap_append_only_violation": bool(reprocessed_document_ids),
        "post_score_gap_reprocessed_document_count": len(reprocessed_document_ids),
        "post_score_gap_reprocessed_document_ids": reprocessed_document_ids,
        "post_score_gap_new_document_count": len(new_document_ids),
        "post_score_gap_new_document_ids": new_document_ids,
        "post_score_gap_new_claim_count": len(new_claim_ids),
        "post_score_gap_new_claim_ids": new_claim_ids,
        "post_score_gap_new_accepted_mapping_count": len(new_mapping_ids),
        "post_score_gap_new_accepted_mapping_ids": new_mapping_ids,
        "post_score_gap_new_rejected_mapping_count": len(new_rejected_mapping_ids),
        "post_score_gap_new_rejected_mapping_ids": new_rejected_mapping_ids,
        "post_score_gap_new_rejected_mapping_summaries": new_rejected_mapping_summaries,
        "post_score_gap_new_eligibility_rejection_summaries": new_eligibility_rejection_summaries,
        "post_score_gap_new_trace_status": current_status,
        "post_score_gap_new_trace_skipped_existing_document_count": int(
            getattr(current_trace, "skipped_existing_document_count", 0) or 0
        ),
        "post_score_gap_new_trace_mapping_prefilter_original_task_count": int(
            getattr(current_trace, "mapping_prefilter_original_task_count", 0) or 0
        ),
        "post_score_gap_new_trace_mapping_prefilter_filtered_task_count": int(
            getattr(current_trace, "mapping_prefilter_filtered_task_count", 0) or 0
        ),
        "post_score_gap_new_trace_mapping_prefilter_skipped_input_count": int(
            getattr(current_trace, "mapping_prefilter_skipped_input_count", 0) or 0
        ),
        "post_score_gap_new_trace_mapping_prefilter_fallback_full_map_count": int(
            getattr(current_trace, "mapping_prefilter_fallback_full_map_count", 0) or 0
        ),
        "post_score_gap_new_trace_mapping_prefilter_fallback_full_map_summaries": tuple(
            getattr(current_trace, "mapping_prefilter_fallback_full_map_summaries", ()) or ()
        ),
        "post_score_gap_new_trace_mapping_empty_output_count": int(
            getattr(current_trace, "mapping_empty_output_count", 0) or 0
        ),
        "post_score_gap_new_trace_mapping_empty_output_retry_count": int(
            getattr(current_trace, "mapping_empty_output_retry_count", 0) or 0
        ),
        "post_score_gap_new_trace_mapping_empty_output_recovered_count": int(
            getattr(current_trace, "mapping_empty_output_recovered_count", 0) or 0
        ),
        "post_score_gap_new_trace_mapping_empty_output_summaries": tuple(
            getattr(current_trace, "mapping_empty_output_summaries", ()) or ()
        ),
        "post_score_gap_new_trace_mapping_empty_output_retry_summaries": tuple(
            getattr(current_trace, "mapping_empty_output_retry_summaries", ()) or ()
        ),
        "post_score_gap_new_trace_error_count": int(getattr(current_trace, "error_count", 0) or 0),
        "post_score_gap_new_trace_errors": new_trace_errors,
        "post_score_gap_primitive_state_changed": bool(primitive_delta_summaries),
        "post_score_gap_primitive_delta_summaries": primitive_delta_summaries,
        "post_score_gap_unchanged_gap_primitive_summaries": unchanged_gap_primitive_summaries,
        "post_score_gap_score_contribution_changed": bool(contribution_delta_summaries),
        "post_score_gap_score_contribution_delta_summaries": contribution_delta_summaries,
    }


def _score_gap_state_repeated_rejection_reasons(
    progress_diagnostics: Mapping[str, object],
) -> tuple[str, ...]:
    reason = str(progress_diagnostics.get("post_score_gap_progress_reason") or "").strip()
    if not reason:
        return ("score_gap_state_repeated",)
    return tuple(dict.fromkeys(("score_gap_state_repeated", reason)))


def _summaries_for_mapping_ids(
    summaries: Sequence[str],
    mapping_ids: Sequence[str],
) -> tuple[str, ...]:
    wanted = {str(mapping_id).strip() for mapping_id in mapping_ids if str(mapping_id).strip()}
    if not wanted:
        return ()
    matched: list[str] = []
    for summary in summaries:
        text = str(summary)
        mapping_id = text.split("|", 1)[0].strip()
        if mapping_id in wanted:
            matched.append(text)
    return tuple(dict.fromkeys(matched))[:20]


def _score_gap_audit_event(
    *,
    inputs: FreeWebResearchInput,
    round_index: int,
    expansion: _ScoreGapExpansionResult,
    progress_diagnostics: Mapping[str, object],
    previous_signature: Sequence[str],
    current_signature: Sequence[str],
) -> Mapping[str, object]:
    payload = {
        "symbol": inputs.symbol,
        "company_name": inputs.company_name,
        "as_of_date": inputs.as_of_date.isoformat(),
        "round_index": round_index,
        "expansion_status": expansion.status,
        "queries_run": tuple(expansion.queries_run),
        "unresolved_gaps": tuple(expansion.unresolved_gaps),
        "progress_reason": progress_diagnostics.get("post_score_gap_progress_reason"),
        "score_state_changed": progress_diagnostics.get("post_score_gap_score_state_changed"),
        "new_document_ids": tuple(progress_diagnostics.get("post_score_gap_new_document_ids", ()) or ()),
        "append_only_violation": progress_diagnostics.get("post_score_gap_append_only_violation"),
        "reprocessed_document_ids": tuple(
            progress_diagnostics.get("post_score_gap_reprocessed_document_ids", ()) or ()
        ),
        "new_claim_ids": tuple(progress_diagnostics.get("post_score_gap_new_claim_ids", ()) or ()),
        "new_accepted_mapping_ids": tuple(
            progress_diagnostics.get("post_score_gap_new_accepted_mapping_ids", ()) or ()
        ),
        "new_rejected_mapping_ids": tuple(
            progress_diagnostics.get("post_score_gap_new_rejected_mapping_ids", ()) or ()
        ),
        "new_rejected_mapping_summaries": tuple(
            progress_diagnostics.get("post_score_gap_new_rejected_mapping_summaries", ()) or ()
        ),
        "new_eligibility_rejection_summaries": tuple(
            progress_diagnostics.get("post_score_gap_new_eligibility_rejection_summaries", ()) or ()
        ),
        "new_trace_status": progress_diagnostics.get("post_score_gap_new_trace_status"),
        "new_trace_mapping_prefilter_fallback_full_map_count": progress_diagnostics.get(
            "post_score_gap_new_trace_mapping_prefilter_fallback_full_map_count",
            0,
        ),
        "new_trace_mapping_prefilter_fallback_full_map_summaries": tuple(
            progress_diagnostics.get(
                "post_score_gap_new_trace_mapping_prefilter_fallback_full_map_summaries",
                (),
            )
            or ()
        ),
        "new_trace_mapping_empty_output_count": progress_diagnostics.get(
            "post_score_gap_new_trace_mapping_empty_output_count",
            0,
        ),
        "new_trace_mapping_empty_output_retry_count": progress_diagnostics.get(
            "post_score_gap_new_trace_mapping_empty_output_retry_count",
            0,
        ),
        "new_trace_mapping_empty_output_recovered_count": progress_diagnostics.get(
            "post_score_gap_new_trace_mapping_empty_output_recovered_count",
            0,
        ),
        "new_trace_mapping_empty_output_summaries": tuple(
            progress_diagnostics.get("post_score_gap_new_trace_mapping_empty_output_summaries", ()) or ()
        ),
        "new_trace_mapping_empty_output_retry_summaries": tuple(
            progress_diagnostics.get("post_score_gap_new_trace_mapping_empty_output_retry_summaries", ()) or ()
        ),
        "new_trace_error_count": progress_diagnostics.get("post_score_gap_new_trace_error_count"),
        "new_trace_errors": tuple(progress_diagnostics.get("post_score_gap_new_trace_errors", ()) or ()),
        "primitive_state_changed": progress_diagnostics.get("post_score_gap_primitive_state_changed"),
        "primitive_delta_summaries": tuple(
            progress_diagnostics.get("post_score_gap_primitive_delta_summaries", ()) or ()
        ),
        "unchanged_gap_primitive_summaries": tuple(
            progress_diagnostics.get("post_score_gap_unchanged_gap_primitive_summaries", ()) or ()
        ),
        "score_contribution_changed": progress_diagnostics.get(
            "post_score_gap_score_contribution_changed"
        ),
        "score_contribution_delta_summaries": tuple(
            progress_diagnostics.get("post_score_gap_score_contribution_delta_summaries", ()) or ()
        ),
        "previous_score_gap_signature_hash": _score_gap_signature_hash(previous_signature),
        "current_score_gap_signature_hash": _score_gap_signature_hash(current_signature),
    }
    event_id_material = "|".join(
        (
            str(payload["symbol"]),
            str(payload["as_of_date"]),
            str(payload["round_index"]),
            str(payload["progress_reason"]),
            str(payload["previous_score_gap_signature_hash"]),
            str(payload["current_score_gap_signature_hash"]),
            ",".join(payload["new_claim_ids"]),  # type: ignore[arg-type]
            ",".join(payload["new_accepted_mapping_ids"]),  # type: ignore[arg-type]
        )
    )
    return {"event_id": f"SGAUD-{hashlib.sha1(event_id_material.encode('utf-8')).hexdigest()[:20]}", **payload}


def _score_gap_signature_hash(signature: Sequence[str]) -> str:
    material = "\n".join(str(item) for item in signature)
    return hashlib.sha1(material.encode("utf-8")).hexdigest()[:20]


def _score_contribution_delta_summaries(
    previous: Sequence[ScoreContributionV2],
    current: Sequence[ScoreContributionV2],
) -> tuple[str, ...]:
    previous_by_key = _score_contributions_by_key(previous)
    current_by_key = _score_contributions_by_key(current)
    summaries: list[str] = []
    for key in sorted(set(previous_by_key) | set(current_by_key)):
        before = previous_by_key.get(key)
        after = current_by_key.get(key)
        if _score_contribution_delta_key(before) == _score_contribution_delta_key(after):
            continue
        summaries.append(_score_contribution_delta_summary(key, before, after))
    return tuple(summaries[:20])


def _score_contributions_by_key(
    contributions: Sequence[ScoreContributionV2],
) -> Mapping[tuple[str, str], tuple[ScoreContributionV2, ...]]:
    grouped: dict[tuple[str, str], list[ScoreContributionV2]] = {}
    for item in contributions:
        grouped.setdefault((item.component_key, item.criterion_id), []).append(item)
    return {key: tuple(value) for key, value in grouped.items()}


def _score_contribution_delta_key(rows: Sequence[ScoreContributionV2] | None) -> tuple[object, ...]:
    if not rows:
        return ("missing",)
    raw_points = round(sum(float(item.raw_points) for item in rows), 4)
    support_claim_ids = tuple(
        dict.fromkeys(claim_id for item in rows for claim_id in item.support_claim_ids)
    )
    counter_claim_ids = tuple(
        dict.fromkeys(claim_id for item in rows for claim_id in item.counter_claim_ids)
    )
    cap_reasons = tuple(dict.fromkeys(str(item.cap_reason) for item in rows if item.cap_reason))
    return (raw_points, support_claim_ids, counter_claim_ids, cap_reasons)


def _score_contribution_delta_summary(
    key: tuple[str, str],
    before: Sequence[ScoreContributionV2] | None,
    after: Sequence[ScoreContributionV2] | None,
) -> str:
    component_key, criterion_id = key
    before_raw, before_support, before_counter, before_caps = _score_contribution_summary_parts(before)
    after_raw, after_support, after_counter, after_caps = _score_contribution_summary_parts(after)
    support_added = tuple(sorted(set(after_support) - set(before_support)))
    support_removed = tuple(sorted(set(before_support) - set(after_support)))
    counter_added = tuple(sorted(set(after_counter) - set(before_counter)))
    counter_removed = tuple(sorted(set(before_counter) - set(after_counter)))
    parts = [f"{component_key}/{criterion_id}:raw={before_raw}->{after_raw}"]
    if support_added:
        parts.append(f"support+={','.join(support_added[:4])}")
    if support_removed:
        parts.append(f"support-={','.join(support_removed[:4])}")
    if counter_added:
        parts.append(f"counter+={','.join(counter_added[:4])}")
    if counter_removed:
        parts.append(f"counter-={','.join(counter_removed[:4])}")
    if before_caps != after_caps:
        parts.append(f"cap={_compact_reason_tuple(before_caps)}->{_compact_reason_tuple(after_caps)}")
    return "; ".join(parts)


def _score_contribution_summary_parts(
    rows: Sequence[ScoreContributionV2] | None,
) -> tuple[float, tuple[str, ...], tuple[str, ...], tuple[str, ...]]:
    if not rows:
        return 0.0, (), (), ()
    raw_points = round(sum(float(item.raw_points) for item in rows), 4)
    support_claim_ids = tuple(
        dict.fromkeys(claim_id for item in rows for claim_id in item.support_claim_ids)
    )
    counter_claim_ids = tuple(
        dict.fromkeys(claim_id for item in rows for claim_id in item.counter_claim_ids)
    )
    cap_reasons = tuple(dict.fromkeys(str(item.cap_reason) for item in rows if item.cap_reason))
    return raw_points, support_claim_ids, counter_claim_ids, cap_reasons


def _compact_reason_tuple(values: Sequence[str]) -> str:
    if not values:
        return "none"
    return "|".join(str(item) for item in values[:4])


def _primitive_state_delta_summaries(
    previous_trace: AgenticEvidenceRuntimeTrace | None,
    current_trace: AgenticEvidenceRuntimeTrace | None,
) -> tuple[str, ...]:
    previous_states = _primitive_states_by_id(previous_trace)
    current_states = _primitive_states_by_id(current_trace)
    summaries: list[str] = []
    for primitive_id in sorted(set(previous_states) | set(current_states)):
        previous = previous_states.get(primitive_id)
        current = current_states.get(primitive_id)
        if _primitive_state_delta_key(previous) == _primitive_state_delta_key(current):
            continue
        summaries.append(_primitive_state_delta_summary(primitive_id, previous, current))
    return tuple(summaries[:20])


def _unchanged_gap_primitive_summaries(
    previous_trace: AgenticEvidenceRuntimeTrace | None,
    current_trace: AgenticEvidenceRuntimeTrace | None,
    *,
    archetype_id: str | None = None,
) -> tuple[str, ...]:
    previous_states = _primitive_states_by_id(previous_trace)
    current_states = _primitive_states_by_id(current_trace)
    summaries: list[str] = []
    gap_statuses = {
        PrimitiveStatus.UNKNOWN,
        PrimitiveStatus.NOT_OBSERVED,
        PrimitiveStatus.CONTRADICTED,
        PrimitiveStatus.HISTORICAL,
        PrimitiveStatus.RESOLVED,
    }
    for primitive_id in sorted(set(previous_states) & set(current_states)):
        previous = previous_states[primitive_id]
        current = current_states[primitive_id]
        if previous.status != current.status or current.status not in gap_statuses:
            continue
        materiality = _agentic_primitive_materiality_remaining(
            primitive_id,
            archetype_id=archetype_id,
            existing_materiality=current.materiality_remaining_points,
        )
        summaries.append(
            f"{primitive_id}:{current.status.value}; "
            f"support={len(current.support_claim_ids)}; counter={len(current.counter_claim_ids)}; "
            f"materiality={round(float(materiality), 4)}"
        )
    return tuple(summaries[:20])


def _primitive_states_by_id(
    trace: AgenticEvidenceRuntimeTrace | None,
) -> Mapping[str, PrimitiveStateV2]:
    if trace is None:
        return {}
    states = getattr(trace, "primitive_states", ()) or ()
    return {
        str(state.primitive_id): state
        for state in states
        if isinstance(state, PrimitiveStateV2) and str(state.primitive_id).strip()
    }


def _primitive_state_delta_key(state: PrimitiveStateV2 | None) -> tuple[object, ...]:
    if state is None:
        return ("missing",)
    return (
        state.status.value,
        tuple(state.support_claim_ids),
        tuple(state.counter_claim_ids),
        tuple(state.support_mapping_ids),
        tuple(state.counter_mapping_ids),
        tuple(state.support_source_family_ids),
        tuple(state.counter_source_family_ids),
        round(float(state.materiality_remaining_points or 0.0), 4),
    )


def _primitive_state_delta_summary(
    primitive_id: str,
    previous: PrimitiveStateV2 | None,
    current: PrimitiveStateV2 | None,
) -> str:
    previous_status = previous.status.value if previous is not None else "MISSING"
    current_status = current.status.value if current is not None else "MISSING"
    previous_support = set(previous.support_claim_ids if previous is not None else ())
    current_support = set(current.support_claim_ids if current is not None else ())
    previous_counter = set(previous.counter_claim_ids if previous is not None else ())
    current_counter = set(current.counter_claim_ids if current is not None else ())
    support_added = tuple(sorted(current_support - previous_support))
    support_removed = tuple(sorted(previous_support - current_support))
    counter_added = tuple(sorted(current_counter - previous_counter))
    counter_removed = tuple(sorted(previous_counter - current_counter))
    previous_materiality = round(float(previous.materiality_remaining_points or 0.0), 4) if previous else 0.0
    current_materiality = round(float(current.materiality_remaining_points or 0.0), 4) if current else 0.0
    parts = [f"{primitive_id}:{previous_status}->{current_status}"]
    if support_added:
        parts.append(f"support+={','.join(support_added[:4])}")
    if support_removed:
        parts.append(f"support-={','.join(support_removed[:4])}")
    if counter_added:
        parts.append(f"counter+={','.join(counter_added[:4])}")
    if counter_removed:
        parts.append(f"counter-={','.join(counter_removed[:4])}")
    if previous_materiality != current_materiality:
        parts.append(f"materiality={previous_materiality}->{current_materiality}")
    return "; ".join(parts)


def _agentic_rejected_mapping_summary(mapping) -> str:
    rationale = re.sub(r"\s+", " ", str(mapping.rationale or "")).strip()
    if len(rationale) > 120:
        rationale = f"{rationale[:117]}..."
    return (
        f"{mapping.mapping_id}|claim={mapping.claim_id}|primitive={mapping.primitive_id}|"
        f"status={mapping.mapping_status.value}|direction={mapping.support_direction.value}|"
        f"reason={rationale}"
    )


def _merge_primitive_state(
    previous: PrimitiveStateV2 | None,
    current: PrimitiveStateV2 | None,
) -> PrimitiveStateV2:
    if previous is None:
        return current  # type: ignore[return-value]
    if current is None:
        return previous
    chosen = current if _primitive_status_rank(current.status) >= _primitive_status_rank(previous.status) else previous
    support_claim_ids = tuple(dict.fromkeys((*previous.support_claim_ids, *current.support_claim_ids)))
    counter_claim_ids = tuple(dict.fromkeys((*previous.counter_claim_ids, *current.counter_claim_ids)))
    support_mapping_ids = tuple(dict.fromkeys((*previous.support_mapping_ids, *current.support_mapping_ids)))
    counter_mapping_ids = tuple(dict.fromkeys((*previous.counter_mapping_ids, *current.counter_mapping_ids)))
    support_source_family_ids = tuple(
        dict.fromkeys((*previous.support_source_family_ids, *current.support_source_family_ids))
    )
    counter_source_family_ids = tuple(
        dict.fromkeys((*previous.counter_source_family_ids, *current.counter_source_family_ids))
    )
    confidence = max(previous.confidence_for_review, current.confidence_for_review)
    freshness_candidates = [item for item in (previous.freshness_days, current.freshness_days) if item is not None]
    return PrimitiveStateV2(
        primitive_id=chosen.primitive_id,
        status=chosen.status,
        normalized_value=chosen.normalized_value,
        support_claim_ids=support_claim_ids,
        counter_claim_ids=counter_claim_ids,
        support_source_family_ids=support_source_family_ids,
        counter_source_family_ids=counter_source_family_ids,
        confidence_for_review=confidence,
        freshness_days=min(freshness_candidates) if freshness_candidates else None,
        materiality_remaining_points=max(previous.materiality_remaining_points, current.materiality_remaining_points),
        support_mapping_ids=support_mapping_ids,
        counter_mapping_ids=counter_mapping_ids,
    )


def _primitive_status_rank(status: PrimitiveStatus) -> int:
    order = {
        PrimitiveStatus.CONTRADICTED: 6,
        PrimitiveStatus.PRESENT_CURRENT: 5,
        PrimitiveStatus.ABSENT_EXPLICITLY_CONFIRMED: 4,
        PrimitiveStatus.RESOLVED: 3,
        PrimitiveStatus.HISTORICAL: 3,
        PrimitiveStatus.NOT_OBSERVED: 2,
        PrimitiveStatus.UNKNOWN: 1,
    }
    return order.get(status, 0)


def _merged_agentic_trace_status(previous: str, current: str) -> str:
    if previous == current:
        return previous
    if "budget_limited" in previous or "budget_limited" in current:
        if (
            "provider_error" in {previous, current}
            or "partial_error" in {previous, current}
            or previous == "partial_error_budget_limited"
            or current == "partial_error_budget_limited"
        ):
            return "partial_error_budget_limited"
        return "completed_budget_limited"
    if "provider_error" in {previous, current}:
        return "partial_error"
    if "partial_error" in {previous, current}:
        return "partial_error"
    if "completed" in {previous, current}:
        return "completed"
    return current or previous


def _agentic_document_inputs(
    *,
    inputs: FreeWebResearchInput,
    web_result: WebResearchResult,
    contract: EvidenceContractV2 | None = None,
    include_official_documents: bool = True,
) -> tuple[tuple[EvidenceDocument, str, tuple[EvidenceAnchor, ...]], ...]:
    rows: list[tuple[EvidenceDocument, str, tuple[EvidenceAnchor, ...]]] = []
    primitive_tokens = _agentic_contract_relevance_tokens(contract)
    for ranked_result, fetch in zip(web_result.selected_results, web_result.fetched_documents):
        if not fetch.ok or not fetch.text or not fetch.text.strip():
            continue
        search_result = ranked_result.result
        document_text = _agentic_fetched_document_text(search_result, fetch.text)
        published_at = search_result.published_at or _agentic_infer_document_published_at(
            search_result,
            as_of_date=inputs.as_of_date,
            document_text=document_text,
        )
        document = EvidenceDocument.from_text(
            text=document_text,
            canonical_url=fetch.url,
            source_type=_agentic_source_type(search_result),
            source_name=search_result.source or "web",
            published_at=published_at,
            available_at=published_at,
            fetched_at=fetch.fetched_at,
            parser_version="web_research_runner:v2_dual_run",
            source_lineage_id=_agentic_source_lineage_id(search_result),
        )
        chunks = _agentic_document_prompt_chunks(document_text, relevance_terms=primitive_tokens)
        if not chunks:
            continue
        for chunk_index, chunk_text in enumerate(chunks):
            locator = (
                "document:full_text_excerpt"
                if len(chunks) == 1
                else f"document:prompt_chunk:{chunk_index}"
            )
            anchor = EvidenceAnchor.text_span(
                document=document,
                document_text=document_text,
                exact_text=chunk_text,
                locator=locator,
            )
            rows.append((document, chunk_text, (anchor,)))
    if include_official_documents:
        rows.extend(_agentic_official_document_inputs(inputs))
    deduped: dict[str, tuple[EvidenceDocument, str, tuple[EvidenceAnchor, ...]]] = {}
    for row in rows:
        anchor_key = row[2][0].anchor_id if row[2] else ""
        deduped.setdefault(f"{row[0].document_id}:{anchor_key}", row)
    return tuple(deduped.values())


def _filter_agentic_document_inputs_for_append_only(
    rows: Sequence[tuple[EvidenceDocument, str, tuple[EvidenceAnchor, ...]]],
    *,
    skip_document_ids: Sequence[str] = (),
) -> tuple[tuple[tuple[EvidenceDocument, str, tuple[EvidenceAnchor, ...]], ...], int]:
    """Drop already-compiled documents before a score-gap Evidence OS pass.

    Gap rounds should append new evidence. Re-sending the same document to an
    LLM mapper can produce a different accepted-mapping set for identical
    source material, which makes score deltas hard to audit.
    """

    skipped_ids = {str(item).strip() for item in skip_document_ids if str(item).strip()}
    if not skipped_ids:
        return tuple(rows), 0
    kept: list[tuple[EvidenceDocument, str, tuple[EvidenceAnchor, ...]]] = []
    skipped_documents: set[str] = set()
    for row in rows:
        document_id = row[0].document_id
        if document_id in skipped_ids:
            skipped_documents.add(document_id)
            continue
        kept.append(row)
    return tuple(kept), len(skipped_documents)


def _agentic_fetched_document_text(search_result: SearchResult, fetched_text: str) -> str:
    parts = [str(search_result.title or "").strip()]
    snippet = str(search_result.snippet or "").strip()
    if snippet:
        parts.append(snippet)
    parts.append(str(fetched_text or "").strip())
    return "\n".join(item for item in parts if item).strip()


def _agentic_infer_document_published_at(
    search_result: SearchResult,
    *,
    as_of_date: date | None = None,
    document_text: str | None = None,
) -> date | None:
    """Infer a report/news source date from auditable metadata.

    This does not use arbitrary body facts as the source date. It accepts
    URL/title/snippet/source date patterns such as ``/2026/06/04/`` or
    ``Daily_260608.pdf`` and, for fetched pages, article metadata labels such
    as ``입력 2026.06.26`` / ``Published: 2026-06-26``. Future inferred dates
    are intentionally preserved so the eligibility gate can reject them as
    ``future_source``.
    """

    if search_result.published_at is not None:
        return search_result.published_at.date()
    metadata_text = " ".join(
        item
        for item in (
            unquote(str(search_result.url or "")),
            str(search_result.title or ""),
            str(search_result.snippet or ""),
            str(search_result.source or ""),
        )
        if item
    )
    candidates = _agentic_date_candidates_from_metadata(metadata_text, as_of_date=as_of_date)
    if document_text:
        candidates = (
            *candidates,
            *_agentic_publication_date_candidates_from_labeled_text(
                document_text,
                as_of_date=as_of_date,
            ),
        )
    if not candidates:
        return None
    return max(candidates)


def _agentic_date_candidates_from_metadata(text: str, *, as_of_date: date | None = None) -> tuple[date, ...]:
    candidates: list[date] = []
    for match in re.finditer(r"(?<!\d)(20\d{2})[./_-]([01]\d)[./_-]([0-3]\d)(?!\d)", text):
        candidate = _agentic_valid_date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
        if candidate is not None:
            candidates.append(candidate)
    for match in re.finditer(r"(?<!\d)(20\d{2})([01]\d)([0-3]\d)(?!\d)", text):
        candidate = _agentic_valid_date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
        if candidate is not None:
            candidates.append(candidate)
    for match in re.finditer(
        r"(?i)(?:[/_-]|(?:article|view|news|data|html|ecn)[^0-9]{0,12})"
        r"(20\d{2})([01]\d)([0-3]\d)(?=\d{2,18}(?:\D|$))",
        text,
    ):
        candidate = _agentic_valid_date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
        if candidate is not None:
            candidates.append(candidate)
    yy_upper_bound = (as_of_date.year + 1) % 100 if as_of_date is not None else 35
    for match in re.finditer(r"(?<!\d)(\d{2})([01]\d)([0-3]\d)(?!\d)", text):
        yy = int(match.group(1))
        if yy > yy_upper_bound:
            continue
        candidate = _agentic_valid_date(2000 + yy, int(match.group(2)), int(match.group(3)))
        if candidate is not None:
            candidates.append(candidate)
    return tuple(dict.fromkeys(candidates))


def _agentic_publication_date_candidates_from_labeled_text(
    text: str,
    *,
    as_of_date: date | None = None,
) -> tuple[date, ...]:
    """Return publication dates only from explicit article metadata labels."""

    candidates: list[date] = []
    for raw_line in str(text or "").splitlines()[:500]:
        line = raw_line.strip()
        if not line or not _agentic_has_publication_date_label(line):
            continue
        candidates.extend(_agentic_date_candidates_from_metadata(line, as_of_date=as_of_date))
        for match in re.finditer(r"(?<!\d)(20\d{2})([01]\d)([0-3]\d)(?=\d{2,6}(?:\D|$))", line):
            candidate = _agentic_valid_date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
            if candidate is not None:
                candidates.append(candidate)
    return tuple(dict.fromkeys(candidates))


def _agentic_has_publication_date_label(line: str) -> bool:
    normalized = re.sub(r"\s+", " ", str(line or "").strip()).lower()
    if not normalized:
        return False
    korean_labels = (
        "입력",
        "등록",
        "승인",
        "발행",
        "게시",
        "보도",
        "작성",
        "최종수정",
        "최종 수정",
        "수정",
        "기사입력",
        "기사 입력",
        "기사등록",
        "기사 등록",
    )
    prefix = normalized[:32]
    if any(label in prefix for label in korean_labels):
        return True
    return bool(
        re.search(
            r"(?i)^(?:published|posted|updated|publication\s+date|release\s+date|article\s+date|date)\b",
            normalized,
        )
    )


def _agentic_valid_date(year: int, month: int, day: int) -> date | None:
    try:
        return date(year, month, day)
    except ValueError:
        return None


def _limit_agentic_document_inputs(
    rows: Sequence[tuple[EvidenceDocument, str, tuple[EvidenceAnchor, ...]]],
    *,
    contract: EvidenceContractV2 | None = None,
    target_names: Sequence[str] = (),
    as_of_date: date | None = None,
    document_limit: int = _AGENTIC_EVIDENCE_DOCUMENT_LIMIT,
) -> tuple[tuple[EvidenceDocument, str, tuple[EvidenceAnchor, ...]], ...]:
    if document_limit <= 0:
        raise ValueError("document_limit must be positive")
    ranked_rows = _rank_agentic_document_inputs(
        rows,
        contract=contract,
        target_names=target_names,
        as_of_date=as_of_date,
    )
    primitive_tokens = _agentic_contract_relevance_tokens(contract)
    selected: list[tuple[EvidenceDocument, str, tuple[EvidenceAnchor, ...]]] = []
    selected_documents: set[str] = set()
    selected_rows: set[tuple[str, tuple[str, ...], str]] = set()
    chunks_by_document: dict[str, int] = {}

    def select(row: tuple[EvidenceDocument, str, tuple[EvidenceAnchor, ...]]) -> bool:
        document, text, anchors = row
        if _agentic_document_time_bucket(document, as_of_date=as_of_date) >= 3:
            return False
        document_id = document.document_id
        row_key = (document_id, tuple(anchor.anchor_id for anchor in anchors), hashlib.sha1(text.encode("utf-8")).hexdigest())
        if row_key in selected_rows:
            return False
        if document_id not in selected_documents and len(selected_documents) >= document_limit:
            return False
        if chunks_by_document.get(document_id, 0) >= _AGENTIC_EVIDENCE_CHUNK_LIMIT_PER_DOCUMENT:
            return False
        selected_documents.add(document_id)
        selected_rows.add(row_key)
        chunks_by_document[document_id] = chunks_by_document.get(document_id, 0) + 1
        selected.append(row)
        return True

    for row in ranked_rows:
        if _agentic_should_reserve_official_document(
            row,
            primitive_tokens=primitive_tokens,
            as_of_date=as_of_date,
        ) and select(row):
            break
    for row in ranked_rows:
        select(row)
    return _merge_agentic_document_input_chunks(selected)


def _merge_agentic_document_input_chunks(
    rows: Sequence[tuple[EvidenceDocument, str, tuple[EvidenceAnchor, ...]]],
) -> tuple[tuple[EvidenceDocument, str, tuple[EvidenceAnchor, ...]], ...]:
    merged: list[tuple[EvidenceDocument, str, tuple[EvidenceAnchor, ...]]] = []
    index_by_document: dict[str, int] = {}
    text_hashes_by_document: dict[str, set[str]] = {}
    anchor_ids_by_document: dict[str, set[str]] = {}
    for document, text, anchors in rows:
        document_id = document.document_id
        text_hash = hashlib.sha1(text.encode("utf-8")).hexdigest()
        if document_id not in index_by_document:
            index_by_document[document_id] = len(merged)
            text_hashes_by_document[document_id] = {text_hash}
            anchor_ids_by_document[document_id] = {anchor.anchor_id for anchor in anchors}
            merged.append((document, text, tuple(anchors)))
            continue

        text_hashes = text_hashes_by_document[document_id]
        anchor_ids = anchor_ids_by_document[document_id]
        existing_index = index_by_document[document_id]
        existing_document, existing_text, existing_anchors = merged[existing_index]
        next_text = existing_text
        if text_hash not in text_hashes:
            next_text = f"{existing_text}\n\n--- evidence chunk ---\n\n{text}".strip()
            text_hashes.add(text_hash)
        next_anchors = list(existing_anchors)
        for anchor in anchors:
            if anchor.anchor_id in anchor_ids:
                continue
            next_anchors.append(anchor)
            anchor_ids.add(anchor.anchor_id)
        merged[existing_index] = (existing_document, next_text, tuple(next_anchors))
    return tuple(merged)


def _rank_agentic_document_inputs(
    rows: Sequence[tuple[EvidenceDocument, str, tuple[EvidenceAnchor, ...]]],
    *,
    contract: EvidenceContractV2 | None = None,
    target_names: Sequence[str] = (),
    as_of_date: date | None = None,
) -> tuple[tuple[EvidenceDocument, str, tuple[EvidenceAnchor, ...]], ...]:
    if not rows:
        return ()
    primitive_tokens = _agentic_contract_relevance_tokens(contract)
    ranked = sorted(
        enumerate(rows),
        key=lambda item: (
            _agentic_document_priority_bucket(
                item[1],
                primitive_tokens=primitive_tokens,
                target_names=target_names,
                as_of_date=as_of_date,
            ),
            _agentic_document_time_bucket(item[1][0], as_of_date=as_of_date),
            -_agentic_document_relevance_score(
                item[1],
                primitive_tokens=primitive_tokens,
                target_names=target_names,
                as_of_date=as_of_date,
            ),
            item[0],
        ),
    )
    return tuple(row for _, row in ranked)


def _agentic_document_priority_bucket(
    row: tuple[EvidenceDocument, str, tuple[EvidenceAnchor, ...]],
    *,
    primitive_tokens: Mapping[str, float],
    target_names: Sequence[str] = (),
    as_of_date: date | None = None,
) -> int:
    if not primitive_tokens:
        return 1
    document = row[0]
    time_bucket = _agentic_document_time_bucket(document, as_of_date=as_of_date)
    if time_bucket >= 3:
        return 6
    overlap_score = _agentic_document_overlap_score(row, primitive_tokens=primitive_tokens)
    relevant = overlap_score > 0
    high_trust = _agentic_is_high_trust_document_type(document.source_type)
    target_direct_signal = _agentic_document_target_direct_signal_score(
        row,
        primitive_tokens=primitive_tokens,
        target_names=target_names,
    )
    date_penalty = 1 if time_bucket == 1 else 0
    if relevant and target_direct_signal > 0 and _agentic_source_quality_adjustment(document) >= 0:
        return 0 + date_penalty
    if relevant and high_trust:
        return 1 + date_penalty
    if relevant:
        return 2 + date_penalty
    if high_trust:
        return 3 + date_penalty
    if _agentic_source_quality_adjustment(document) < 0:
        return 5
    return 4 + date_penalty


def _agentic_should_reserve_official_document(
    row: tuple[EvidenceDocument, str, tuple[EvidenceAnchor, ...]],
    *,
    primitive_tokens: Mapping[str, float],
    as_of_date: date | None = None,
) -> bool:
    document = row[0]
    if _agentic_document_time_bucket(document, as_of_date=as_of_date) >= 3:
        return False
    if document.source_type not in {SourceType.FILING, SourceType.IR, SourceType.XBRL, SourceType.API}:
        return False
    if _agentic_source_quality_adjustment(document) < 0:
        return False
    return _agentic_document_overlap_score(row, primitive_tokens=primitive_tokens) > 0


def _agentic_document_relevance_score(
    row: tuple[EvidenceDocument, str, tuple[EvidenceAnchor, ...]],
    *,
    primitive_tokens: Mapping[str, float],
    target_names: Sequence[str] = (),
    as_of_date: date | None = None,
) -> float:
    document = row[0]
    overlap_score = _agentic_document_overlap_score(row, primitive_tokens=primitive_tokens)
    target_direct_signal = _agentic_document_target_direct_signal_score(
        row,
        primitive_tokens=primitive_tokens,
        target_names=target_names,
    )
    return (
        overlap_score
        + target_direct_signal
        + _agentic_source_type_priority(document.source_type)
        + _agentic_source_quality_adjustment(document)
        + _agentic_document_time_adjustment(document, as_of_date=as_of_date)
    )


def _agentic_document_time_bucket(
    document: EvidenceDocument,
    *,
    as_of_date: date | None = None,
) -> int:
    """Rank source-date usability before spending bounded LLM document slots."""

    if as_of_date is None:
        return 0
    published = document.published_date()
    available = document.available_date()
    if (published is not None and published > as_of_date) or (
        available is not None and available > as_of_date
    ):
        return 3
    if published is None and available is None:
        return 1
    return 0


def _agentic_document_time_adjustment(
    document: EvidenceDocument,
    *,
    as_of_date: date | None = None,
) -> float:
    time_bucket = _agentic_document_time_bucket(document, as_of_date=as_of_date)
    if time_bucket >= 3:
        return -100.0
    if time_bucket == 1:
        return -10.0
    return 4.0


def _agentic_document_overlap_score(
    row: tuple[EvidenceDocument, str, tuple[EvidenceAnchor, ...]],
    *,
    primitive_tokens: Mapping[str, float],
) -> float:
    document, text, anchors = row
    haystack = " ".join(
        item
        for item in (
            document.source_name,
            document.canonical_url or "",
            document.source_type.value,
            text,
            " ".join(anchor.locator for anchor in anchors),
        )
        if item
    )
    haystack_tokens = _agentic_text_tokens(haystack)
    return sum(weight for token, weight in primitive_tokens.items() if token in haystack_tokens)


def _agentic_document_target_direct_signal_score(
    row: tuple[EvidenceDocument, str, tuple[EvidenceAnchor, ...]],
    *,
    primitive_tokens: Mapping[str, float],
    target_names: Sequence[str] = (),
) -> float:
    """Boost source routing when target and operating fact appear together.

    This is not score evidence.  It only decides which bounded documents/chunks
    the contract-blind extractor reads first.  The claim still needs entity,
    temporal, mapping, eligibility, and source-quorum validation before scoring.
    """

    if not primitive_tokens or not target_names:
        return 0.0
    document, text, _anchors = row
    haystack = "\n".join(
        item
        for item in (
            document.source_name,
            document.canonical_url or "",
            text,
        )
        if item
    )
    best = 0.0
    for segment in _agentic_relevance_segments(haystack):
        if not _agentic_segment_has_target_name(segment, target_names=target_names):
            continue
        segment_tokens = _agentic_text_tokens(segment)
        segment_score = sum(weight for token, weight in primitive_tokens.items() if token in segment_tokens)
        if segment_score <= 0:
            continue
        best = max(best, segment_score)
    if best <= 0:
        return 0.0
    return min(48.0, 18.0 + best)


def _agentic_relevance_segments(text: str) -> tuple[str, ...]:
    segments = [item.strip() for item in re.split(r"[\n\r。.!?;；]+", str(text or "")) if item.strip()]
    return tuple(segment[:700] for segment in segments)


def _agentic_segment_has_target_name(segment: str, *, target_names: Sequence[str]) -> bool:
    segment_text = str(segment or "")
    if not segment_text:
        return False
    segment_casefold = segment_text.casefold()
    segment_compact = re.sub(r"[^0-9a-z가-힣]+", "", segment_casefold)
    segment_tokens = _agentic_text_tokens(segment_text)
    for name in target_names:
        raw_name = str(name or "").strip()
        if not raw_name:
            continue
        name_casefold = raw_name.casefold()
        if name_casefold and name_casefold in segment_casefold:
            return True
        name_compact = re.sub(r"[^0-9a-z가-힣]+", "", name_casefold)
        if len(name_compact) >= 3 and name_compact in segment_compact:
            return True
        name_tokens = _agentic_text_tokens(raw_name)
        if name_tokens and name_tokens.issubset(segment_tokens):
            return True
    return False


def _agentic_document_selection_summary(
    document: EvidenceDocument,
    text: str,
    *,
    contract: EvidenceContractV2 | None = None,
    target_names: Sequence[str] = (),
    as_of_date: date | None = None,
) -> str:
    primitive_tokens = _agentic_contract_relevance_tokens(contract)
    haystack_tokens = _agentic_text_tokens(
        " ".join(
            item
            for item in (
                document.source_name,
                document.canonical_url or "",
                document.source_type.value,
                text,
            )
            if item
        )
    )
    matched = tuple(token for token in primitive_tokens if token in haystack_tokens)[:12]
    target_direct_signal = _agentic_document_target_direct_signal_score(
        (document, text, ()),
        primitive_tokens=primitive_tokens,
        target_names=target_names,
    )
    score = _agentic_document_relevance_score(
        (document, text, ()),
        primitive_tokens=primitive_tokens,
        target_names=target_names,
        as_of_date=as_of_date,
    )
    quality_adjustment = _agentic_source_quality_adjustment(document)
    time_bucket = _agentic_document_time_bucket(document, as_of_date=as_of_date)
    url = document.canonical_url or document.document_id
    if len(url) > 96:
        url = f"{url[:93]}..."
    published = document.published_date().isoformat() if document.published_date() else "-"
    available = document.available_date().isoformat() if document.available_date() else "-"
    return (
        f"{document.document_id}|source={document.source_type.value}|score={score:.2f}|"
        f"published_at={published}|available_at={available}|"
        f"time_bucket={time_bucket}|"
        f"quality_adjustment={quality_adjustment:.2f}|"
        f"target_direct_signal={target_direct_signal:.2f}|"
        f"matched={','.join(matched) if matched else '-'}|url={url}"
    )


def _agentic_contract_relevance_tokens(contract: EvidenceContractV2 | None) -> Mapping[str, float]:
    if contract is None:
        return {}
    weighted: dict[str, float] = {}
    green_primitives = set(contract.green_gate.primitive_ids())
    required_primitives = set(contract.required_primitives)
    alternative_primitives = set(contract.alternative_primitives) | {
        item for values in contract.alternative_primitives.values() for item in values
    }
    for primitive_id in sorted(green_primitives | required_primitives | alternative_primitives):
        weight = 2.0
        if primitive_id in required_primitives:
            weight += 1.0
        if primitive_id in green_primitives:
            weight += 2.0
        for token in _agentic_text_tokens(primitive_id):
            weighted[token] = max(weighted.get(token, 0.0), weight)
        for alias in contract.primitive_aliases.get(primitive_id, ()):
            for token in _agentic_text_tokens(alias):
                weighted[token] = max(weighted.get(token, 0.0), weight)
    for primitives in contract.score_rubric.values():
        for primitive_id in primitives:
            for token in _agentic_text_tokens(primitive_id):
                weighted[token] = max(weighted.get(token, 0.0), 1.0)
            for alias in contract.primitive_aliases.get(primitive_id, ()):
                for token in _agentic_text_tokens(alias):
                    weighted[token] = max(weighted.get(token, 0.0), 1.0)
    canonical_primitive_ids = set(_contract_canonical_primitive_ids(contract))
    for primitive_id, aliases in _AGENTIC_GENERIC_BRIDGE_PRIMITIVE_ALIASES.items():
        if primitive_id not in canonical_primitive_ids:
            continue
        for token in _agentic_text_tokens(primitive_id):
            weighted[token] = max(weighted.get(token, 0.0), 2.0)
        for alias in aliases:
            for token in _agentic_text_tokens(alias):
                weighted[token] = max(weighted.get(token, 0.0), 2.0)
    return weighted


def _agentic_text_tokens(text: str) -> set[str]:
    tokens: set[str] = set()
    for raw in re.split(r"[^0-9A-Za-z가-힣]+", str(text or "").lower()):
        token = raw.strip()
        has_hangul = bool(re.search(r"[가-힣]", token))
        min_length = 2 if has_hangul else 3
        if len(token) < min_length:
            continue
        tokens.add(token)
    return tokens


def _agentic_source_type_priority(source_type: SourceType) -> float:
    if source_type in {SourceType.FILING, SourceType.IR, SourceType.XBRL}:
        return 12.0
    if source_type == SourceType.RESEARCH_REPORT:
        return 8.0
    if source_type == SourceType.API:
        return 4.0
    if source_type == SourceType.NEWS:
        return 0.0
    return -1.0


def _agentic_is_high_trust_document_type(source_type: SourceType) -> bool:
    return source_type in {
        SourceType.FILING,
        SourceType.IR,
        SourceType.XBRL,
        SourceType.API,
        SourceType.RESEARCH_REPORT,
    }


def _agentic_source_quality_adjustment(document: EvidenceDocument) -> float:
    """Prefer auditable primary/report sources before social mirrors.

    This is a source-routing adjustment only.  A low-quality source can still be
    used when it is the best available candidate, but it should not consume the
    first bounded claim-extraction slots ahead of official documents or reports.
    """

    haystack = f"{document.source_name} {document.canonical_url or ''}".lower()
    if re.search(r"(^|[/:.])t\.me([/:?#]|$)", haystack) or "telegram" in haystack:
        return -8.0
    low_trust_markers = (
        "discord",
        "reddit",
        "dcinside",
        "theqoo",
        "fmkorea",
        "blog.",
        "blog/",
        "blogspot.",
        "brunch.co.kr",
        "medium.com",
        "tistory.",
        "tistory.com",
        "wordpress.",
        "wordpress.com",
        "cafe.",
        "cafe/",
        "community",
    )
    if any(marker in haystack for marker in low_trust_markers):
        return -5.0
    return 0.0


def _agentic_official_document_inputs(
    inputs: FreeWebResearchInput,
) -> tuple[tuple[EvidenceDocument, str, tuple[EvidenceAnchor, ...]], ...]:
    base = inputs.base_feature_input
    if base is None:
        return ()
    evidence_items = evidence_from_feature_domains(
        market=inputs.market,
        fallback_symbol=inputs.symbol,
        financial_actuals=base.financial_actuals,
        consensus=base.consensus,
        consensus_revisions=base.consensus_revisions,
        disclosures=base.disclosures,
        research_reports=base.research_reports,
        news_items=base.news_items,
    )
    rows: list[tuple[EvidenceDocument, str, tuple[EvidenceAnchor, ...]]] = []
    for evidence in evidence_items:
        row = _agentic_document_input_from_evidence(evidence)
        if row is not None:
            rows.append(row)
    return tuple(rows)


def _agentic_document_input_from_evidence(
    evidence,
) -> tuple[EvidenceDocument, str, tuple[EvidenceAnchor, ...]] | None:
    document_text = _agentic_evidence_document_text(evidence)
    if not document_text:
        return None
    source_type = _agentic_source_type_from_evidence(evidence.source_type)
    document = EvidenceDocument.from_text(
        text=document_text,
        canonical_url=evidence.url_or_identifier,
        source_type=source_type,
        source_name=evidence.source_name,
        published_at=evidence.published_at,
        available_at=evidence.available_at,
        fetched_at=evidence.observed_at,
        revision_id=evidence.evidence_id,
        parser_version="feature_domain_evidence:v2_dual_run",
        source_lineage_id=f"{evidence.source_type}:{evidence.source_name}",
    )
    anchors: list[EvidenceAnchor] = [
        EvidenceAnchor.text_span(
            document=document,
            document_text=document_text,
            exact_text=_agentic_anchor_text(document_text),
            locator="evidence:document_text",
        )
    ]
    structured_fields = _agentic_structured_evidence_fields(evidence.parsed_fields)
    if structured_fields:
        anchors.append(
            EvidenceAnchor.structured(
                document=document,
                anchor_type=_agentic_anchor_type_for_evidence(evidence.source_type),
                locator="evidence:parsed_fields",
                normalized_value=structured_fields,
                exact_text="",
                anchor_verified=True,
            )
        )
    return document, document_text, tuple(anchors)


def _agentic_evidence_document_text(evidence) -> str:
    parts = [str(evidence.title or "").strip()]
    excerpt = evidence.excerpt_or_value
    if excerpt not in (None, ""):
        parts.append(str(excerpt).strip())
    if evidence.source_type in {"financial_actual", "consensus", "consensus_revision", "exchange_risk"}:
        structured_fields = _agentic_structured_evidence_fields(evidence.parsed_fields)
        if structured_fields:
            parts.append(
                "\n".join(f"{key}: {structured_fields[key]}" for key in sorted(structured_fields))
            )
    return "\n".join(item for item in parts if item).strip()


def _agentic_structured_evidence_fields(parsed_fields: Mapping[str, Any]) -> dict[str, Any]:
    fields: dict[str, Any] = {}
    for key, value in sorted((parsed_fields or {}).items()):
        field_name = str(key).strip()
        if not field_name or not _agentic_evidence_field_allowed(field_name, value):
            continue
        fields[field_name] = value
    return fields


def _agentic_evidence_field_allowed(field_name: str, value: Any) -> bool:
    if value in (None, ""):
        return False
    if field_name in {
        "agent_extracted_field_source",
        "claim_ledger_version",
        "compiled_claim_ids",
        "compiled_claim_ids_by_primitive",
        "compiled_primitive_states",
        "evidence_os_v2_score_eligible_claim_ids_by_primitive",
    }:
        return False
    if field_name.startswith("claim_") or field_name.startswith("compiled_"):
        return False
    if isinstance(value, (Mapping, list, tuple, set)):
        return False
    return True


def _agentic_source_type_from_evidence(source_type: str) -> SourceType:
    if source_type == "disclosure":
        return SourceType.FILING
    if source_type == "financial_actual":
        return SourceType.XBRL
    if source_type in {"consensus", "consensus_revision", "exchange_risk"}:
        return SourceType.API
    if source_type == "research_report":
        return SourceType.RESEARCH_REPORT
    if source_type == "news":
        return SourceType.NEWS
    return SourceType.OTHER


def _agentic_anchor_type_for_evidence(source_type: str) -> AnchorType:
    if source_type == "financial_actual":
        return AnchorType.XBRL_FACT
    if source_type == "disclosure":
        return AnchorType.TABLE_CELL
    return AnchorType.API_RECORD


def _agentic_source_type(result: SearchResult) -> SourceType:
    structured_type = _agentic_structured_source_type(result)
    if structured_type is not None:
        return structured_type
    if result.is_disclosure and _agentic_is_official_disclosure_result(result):
        return SourceType.FILING
    if result.is_report_domain or result.is_pdf:
        return SourceType.RESEARCH_REPORT
    if result.is_news:
        return SourceType.NEWS
    return SourceType.OTHER


def _agentic_structured_source_type(result: SearchResult) -> SourceType | None:
    feature_type = _agentic_feature_source_type(result)
    if feature_type is not None:
        return feature_type
    url = str(result.url or "").strip().lower()
    if url.startswith("opendart://") and "/financial_actual/" in url:
        return SourceType.XBRL
    return None


def _agentic_feature_source_type(result: SearchResult) -> SourceType | None:
    url = str(result.url or "").strip().lower()
    if not url.startswith("feature://"):
        return None
    if "/financial_actual/" in url:
        return SourceType.XBRL
    if "/consensus/" in url or "/consensus_revision/" in url or "/exchange_risk/" in url:
        return SourceType.API
    if "/disclosure/" in url:
        return SourceType.FILING
    if "/research_report/" in url:
        return SourceType.RESEARCH_REPORT
    if "/news/" in url:
        return SourceType.NEWS
    return SourceType.API


def _agentic_is_official_disclosure_result(result: SearchResult) -> bool:
    haystack = f"{result.source} {result.url}".lower()
    official_markers = (
        "dart.fss.or.kr",
        "opendart.fss.or.kr",
        "dart.example.com",
        "opendart://",
        "opendart-detail://",
        "kind.krx.co.kr",
        "kind.krx",
        "feature://",
    )
    return any(marker in haystack for marker in official_markers)


def _agentic_anchor_text(text: str, *, max_chars: int = 4_000) -> str:
    clean = text.strip()
    if not clean:
        return ""
    return clean[:max_chars]


def _agentic_document_prompt_text(text: str) -> str:
    return _agentic_anchor_text(text, max_chars=_AGENTIC_EVIDENCE_DOCUMENT_TEXT_LIMIT)


def _agentic_document_prompt_chunks(
    text: str,
    *,
    relevance_terms: Mapping[str, float] | None = None,
) -> tuple[str, ...]:
    clean = text.strip()
    if not clean:
        return ()
    if relevance_terms:
        relevance_chunks = _agentic_relevance_prompt_chunks(clean, relevance_terms=relevance_terms)
        if relevance_chunks:
            return relevance_chunks
    chunks: list[str] = []
    start = 0
    limit = _AGENTIC_EVIDENCE_DOCUMENT_TEXT_LIMIT
    while start < len(clean) and len(chunks) < _AGENTIC_EVIDENCE_CHUNK_LIMIT_PER_DOCUMENT:
        end = min(len(clean), start + limit)
        if end < len(clean):
            newline = clean.rfind("\n", start + max(limit // 2, 1), end)
            if newline > start:
                end = newline
        chunk = clean[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start = end
        while start < len(clean) and clean[start].isspace():
            start += 1
    return tuple(chunks)


def _agentic_relevance_prompt_chunks(
    text: str,
    *,
    relevance_terms: Mapping[str, float],
) -> tuple[str, ...]:
    limit = _AGENTIC_EVIDENCE_DOCUMENT_TEXT_LIMIT
    first = _agentic_prompt_chunk_at(text, start=0, limit=limit)
    chunks: list[str] = []
    if first:
        chunks.append(first)
    windows: list[tuple[float, int, str]] = []
    haystack = text.lower()
    for term, weight in relevance_terms.items():
        token = str(term or "").strip().lower()
        if len(token) < 3:
            continue
        start = 0
        while True:
            pos = haystack.find(token, start)
            if pos < 0:
                break
            window_start = max(0, pos - limit // 3)
            window = _agentic_prompt_chunk_at(text, start=window_start, limit=limit)
            if window:
                score = _agentic_prompt_chunk_relevance_score(window, relevance_terms=relevance_terms)
                windows.append((score + float(weight), window_start, window))
            start = pos + len(token)
    for _, _, window in sorted(windows, key=lambda item: (-item[0], item[1])):
        if len(chunks) >= _AGENTIC_EVIDENCE_CHUNK_LIMIT_PER_DOCUMENT:
            break
        if _agentic_chunk_duplicate_or_overlapping(window, chunks):
            continue
        chunks.append(window)
    return tuple(chunks[:_AGENTIC_EVIDENCE_CHUNK_LIMIT_PER_DOCUMENT])


def _agentic_prompt_chunk_at(text: str, *, start: int, limit: int) -> str:
    clean = text.strip()
    if not clean or start >= len(clean):
        return ""
    start = max(0, start)
    end = min(len(clean), start + limit)
    if end < len(clean):
        newline = clean.rfind("\n", start + max(limit // 2, 1), end)
        if newline > start:
            end = newline
    return clean[start:end].strip()


def _agentic_prompt_chunk_relevance_score(
    chunk: str,
    *,
    relevance_terms: Mapping[str, float],
) -> float:
    haystack = chunk.lower()
    return sum(float(weight) for term, weight in relevance_terms.items() if str(term).lower() in haystack)


def _agentic_chunk_duplicate_or_overlapping(candidate: str, chunks: Sequence[str]) -> bool:
    if not candidate:
        return True
    for chunk in chunks:
        if candidate == chunk:
            return True
    return False


def _agentic_target_entity_id(inputs: FreeWebResearchInput) -> str:
    return f"{inputs.market.value}:{inputs.symbol}"


def _agentic_source_lineage_id(result: SearchResult) -> str:
    source = re.sub(r"\s+", "-", (result.source or "web").strip().lower())
    query = re.sub(r"\s+", "-", (result.query or "").strip().lower())[:80]
    return f"{source}:{query}" if query else source


def _contract_canonical_primitive_ids(contract) -> tuple[str, ...]:
    ids: list[str] = []
    ids.extend(contract.required_primitives)
    ids.extend(contract.green_gate.primitive_ids())
    ids.extend(contract.guard_modes.keys())
    for key, alternatives in contract.alternative_primitives.items():
        ids.append(key)
        ids.extend(alternatives)
    return tuple(dict.fromkeys(item for item in ids if str(item).strip()))


class _FixedQueryPlanner:
    """Adapter so WebResearchRunner uses the already budgeted query plan."""

    def __init__(self, query_plan: QueryPlan) -> None:
        self._query_plan = query_plan

    def plan(self, **kwargs) -> QueryPlan:
        return self._query_plan


def _emit_phase_event(inputs: FreeWebResearchInput, phase: str, **payload: Any) -> None:
    sink = inputs.phase_event_sink
    if sink is None:
        return
    event = {
        "symbol": inputs.symbol,
        "company_name": inputs.company_name,
        "as_of_date": inputs.as_of_date.isoformat(),
        "phase": phase,
        **payload,
    }
    sink(event)


def _emit_web_result_phase(inputs: FreeWebResearchInput, phase: str, web_result: WebResearchResult) -> None:
    _emit_phase_event(
        inputs,
        phase,
        query_count=len(web_result.queries_run),
        search_result_count=len(web_result.search_results),
        ranked_result_count=len(web_result.ranked_results),
        selected_result_count=len(web_result.selected_results),
        fetched_document_count=len(web_result.fetched_documents),
        parsed_report_count=len(web_result.parsed_reports),
        parsed_news_count=len(web_result.parsed_news),
        parsed_disclosure_count=len(web_result.parsed_disclosures),
        evidence_count=len(web_result.evidence),
    )


def _record_agentic_workflow_metrics(
    phase: str,
    payload: Mapping[str, Any],
    *,
    metrics: dict[str, Any],
) -> None:
    if phase == "agentic_evidence_mapping_prefilter_complete":
        metrics["mapping_prefilter_original_task_count"] = int(
            metrics.get("mapping_prefilter_original_task_count") or 0
        ) + int(payload.get("mapping_prefilter_original_task_count") or 0)
        metrics["mapping_prefilter_filtered_task_count"] = int(
            metrics.get("mapping_prefilter_filtered_task_count") or 0
        ) + int(payload.get("mapping_prefilter_filtered_task_count") or 0)
        metrics["mapping_prefilter_skipped_input_count"] = int(
            metrics.get("mapping_prefilter_skipped_input_count") or 0
        ) + int(payload.get("mapping_prefilter_skipped_input_count") or 0)
        metrics["mapping_prefilter_fallback_full_map_count"] = int(
            metrics.get("mapping_prefilter_fallback_full_map_count") or 0
        ) + int(payload.get("mapping_prefilter_fallback_full_map_count") or 0)
        summaries = metrics.setdefault("mapping_prefilter_fallback_full_map_summaries", [])
        if isinstance(summaries, list):
            document_id = str(payload.get("document_id") or "").strip()
            for row in payload.get("mapping_prefilter_reason_by_claim") or ():
                if not isinstance(row, Mapping) or not row.get("fallback_full_map"):
                    continue
                summaries.append(
                    "fallback_full_map"
                    f"|document={document_id or 'unknown'}"
                    f"|claim={row.get('claim_id')}"
                    f"|raw_assertion={row.get('raw_assertion_id')}"
                    f"|reason={row.get('reason')}"
                    f"|original_candidates={row.get('original_candidate_count')}"
                )
                if len(summaries) >= 20:
                    break
        return

    if phase not in {
        "agentic_evidence_mapping_chunk_complete",
        "agentic_evidence_mapping_single_complete",
        "agentic_evidence_mapping_chunk_empty_retry_start",
        "agentic_evidence_mapping_single_empty_retry_start",
        "agentic_evidence_mapping_chunk_empty_retry_recovered",
        "agentic_evidence_mapping_single_empty_retry_recovered",
    }:
        return
    if phase in {
        "agentic_evidence_mapping_chunk_empty_retry_start",
        "agentic_evidence_mapping_single_empty_retry_start",
    }:
        metrics["mapping_empty_output_retry_count"] = int(
            metrics.get("mapping_empty_output_retry_count") or 0
        ) + 1
        summaries = metrics.setdefault("mapping_empty_output_retry_summaries", [])
        if isinstance(summaries, list) and len(summaries) < 20:
            summaries.append(_agentic_mapping_retry_summary(phase, payload))
        return
    if phase in {
        "agentic_evidence_mapping_chunk_empty_retry_recovered",
        "agentic_evidence_mapping_single_empty_retry_recovered",
    }:
        metrics["mapping_empty_output_recovered_count"] = int(
            metrics.get("mapping_empty_output_recovered_count") or 0
        ) + 1
        summaries = metrics.setdefault("mapping_empty_output_retry_summaries", [])
        if isinstance(summaries, list) and len(summaries) < 20:
            summaries.append(_agentic_mapping_retry_summary(phase, payload))
        return
    mapping_input_count = int(payload.get("mapping_input_count") or 0)
    mapping_output_count = int(payload.get("mapping_output_count") or 0)
    if mapping_input_count <= 0 or mapping_output_count != 0:
        return
    metrics["mapping_empty_output_count"] = int(metrics.get("mapping_empty_output_count") or 0) + 1
    summaries = metrics.setdefault("mapping_empty_output_summaries", [])
    if isinstance(summaries, list) and len(summaries) < 20:
        summaries.append(
            _agentic_mapping_empty_output_summary(
                phase,
                payload,
                mapping_input_count=mapping_input_count,
            )
        )


def _agentic_mapping_retry_summary(phase: str, payload: Mapping[str, Any]) -> str:
    return (
        "empty_mapper_retry"
        f"|phase={phase}"
        f"|document={payload.get('document_id') or 'unknown'}"
        f"|round={payload.get('round_index')}"
        f"|retry={payload.get('retry_index')}"
        f"|chunk={payload.get('chunk_index')}"
        f"|item={payload.get('item_index')}"
        f"|mapping_input_count={payload.get('mapping_input_count')}"
        f"|mapping_output_count={payload.get('mapping_output_count')}"
    )


def _agentic_mapping_empty_output_summary(
    phase: str,
    payload: Mapping[str, Any],
    *,
    mapping_input_count: int,
) -> str:
    return (
        "empty_mapper_output"
        f"|phase={phase}"
        f"|document={payload.get('document_id') or 'unknown'}"
        f"|round={payload.get('round_index')}"
        f"|chunk={payload.get('chunk_index')}"
        f"|item={payload.get('item_index')}"
        f"|mapping_input_count={mapping_input_count}"
    )


def _theme_route_search_results_from_ranked(
    inputs: FreeWebResearchInput,
    ranked: Sequence[RankedSearchResult],
) -> tuple[ThemeRouteSearchResult, ...]:
    return tuple(
        ThemeRouteSearchResult.from_search_result(item.result)
        for item in _select_ranked_for_llm(ranked, inputs.theme_route_search_result_limit)
    )


def _select_ranked_for_llm(
    ranked: Sequence[RankedSearchResult],
    limit: int | None,
) -> tuple[RankedSearchResult, ...]:
    eligible = tuple(
        item
        for item in ranked
        if item.score > 0
        and "duplicate_url" not in item.negative_reasons
        and "future_result" not in item.negative_reasons
    )
    if limit is None:
        return eligible
    if limit <= 0:
        return ()
    selected: list[RankedSearchResult] = []
    selected_urls: set[str] = set()
    covered_queries: set[str] = set()
    for item in eligible:
        query = (item.result.query or "").strip()
        if not query or query in covered_queries:
            continue
        selected.append(item)
        selected_urls.add(item.result.url)
        covered_queries.add(query)
        if len(selected) >= limit:
            return tuple(selected)
    for item in eligible:
        if item.result.url in selected_urls:
            continue
        selected.append(item)
        selected_urls.add(item.result.url)
        if len(selected) >= limit:
            break
    return tuple(selected)


_POST_PARSE_GAP_ROUTE_STATUSES = {
    "transition_detected",
    "mixed_route",
    "needs_more_evidence",
    "more_evidence_needed",
}


def _post_parse_gap_expansion_allowed(inputs: FreeWebResearchInput, route: ThemeRouteOutput | None) -> bool:
    return bool(
        inputs.post_parse_gap_expansion_enabled
        and (inputs.post_parse_gap_expansion_max_queries is None or inputs.post_parse_gap_expansion_max_queries > 0)
        and inputs.theme_evidence_review_enabled
        and inputs.theme_rebalance_enabled
        and inputs.theme_route_provider is not None
        and route is not None
        and route.status in _POST_PARSE_GAP_ROUTE_STATUSES
    )


def _post_score_gap_expansion_allowed(inputs: FreeWebResearchInput, score: ScoreSnapshot) -> bool:
    return bool(
        inputs.post_parse_gap_expansion_enabled
        and (inputs.post_parse_gap_expansion_max_queries is None or inputs.post_parse_gap_expansion_max_queries > 0)
        and inputs.theme_evidence_review_enabled
        and inputs.theme_rebalance_enabled
    )


def _post_parse_gap_queries(
    *,
    inputs: FreeWebResearchInput,
    route: ThemeRouteOutput | None,
) -> tuple[str, ...]:
    if route is None:
        return ()

    normalized: list[str] = []
    for query in route.suggested_queries:
        clean = re.sub(r"\s+", " ", str(query)).strip()
        if not clean:
            continue
        normalized.append(clean)
        if _query_limit_reached(normalized, inputs.post_parse_gap_expansion_max_queries):
            break
    unique = tuple(dict.fromkeys(normalized))
    if inputs.post_parse_gap_expansion_max_queries is None:
        return unique
    return unique[: inputs.post_parse_gap_expansion_max_queries]


def _post_parse_gap_retry_route(
    *,
    inputs: FreeWebResearchInput,
    web_result: WebResearchResult,
    existing_route: ThemeRouteOutput | None,
    retry_index: int,
    previous_rejections: Sequence[str],
) -> ThemeRouteOutput:
    if inputs.theme_route_provider is None:
        return ThemeRouteOutput(status="disabled_no_provider", blocked_reason="post_parse_gap_retry_without_provider")
    agent = LLMThemeRebalanceAgent(
        _theme_route_provider_for_timeout(
            inputs.theme_route_provider,
            timeout_seconds=inputs.theme_evidence_review_timeout_seconds,
        )
    )
    search_results = _theme_route_search_results_from_ranked(inputs, web_result.ranked_results)
    documents = _theme_route_documents(
        web_result,
        limit=inputs.theme_route_document_limit,
        excerpt_chars=inputs.theme_route_document_excerpt_chars,
    )
    _emit_phase_event(
        inputs,
        "post_parse_gap_retry_route_start",
        retry_index=retry_index,
        raw_ranked_result_count=len(web_result.ranked_results),
        llm_search_result_count=len(search_results),
        raw_document_count=len(web_result.fetched_documents),
        llm_document_count=len(documents),
        timeout_seconds=inputs.theme_evidence_review_timeout_seconds,
    )
    return agent.route(
        ThemeRouteInput(
            company_name=inputs.company_name,
            symbol=inputs.symbol,
            sector=inputs.sector,
            market=inputs.market.value,
            as_of_date=inputs.as_of_date,
            stage_context=inputs.stage_context,
            candidate_reason_codes=inputs.candidate_reason_codes,
            current_large_sector_id=existing_route.large_sector_id if existing_route else None,
            current_canonical_archetype_id=existing_route.canonical_archetype_id if existing_route else None,
            search_results=search_results,
            documents=documents,
            score_gap_context=_llm_query_retry_context(
                phase="post_parse_gap",
                retry_index=retry_index,
                previous_rejections=previous_rejections,
                missing_information=tuple(
                    dict.fromkeys(
                        (
                            *(existing_route.missing_information if existing_route else ()),
                            *_theme_route_contract_gap_context(existing_route),
                        )
                    )
                ),
            ),
        )
    )


def _score_gap_route(
    *,
    inputs: FreeWebResearchInput,
    score: ScoreSnapshot,
    score_gaps: Sequence[str],
    web_result: WebResearchResult,
    theme_route: ThemeRouteOutput | None,
    source_fields: Mapping[str, Any],
) -> ThemeRouteOutput:
    if inputs.theme_route_provider is None:
        return ThemeRouteOutput(status="disabled_no_provider", blocked_reason="score_gap_expansion_without_provider")
    agent = LLMThemeRebalanceAgent(
        _theme_route_provider_for_timeout(
            inputs.theme_route_provider,
            timeout_seconds=inputs.theme_evidence_review_timeout_seconds,
        )
    )
    search_results = _theme_route_search_results_from_ranked(inputs, web_result.ranked_results)
    documents = _theme_route_documents(
        web_result,
        limit=inputs.theme_route_document_limit,
        excerpt_chars=inputs.theme_route_document_excerpt_chars,
    )
    _emit_phase_event(
        inputs,
        "score_gap_route_start",
        raw_ranked_result_count=len(web_result.ranked_results),
        llm_search_result_count=len(search_results),
        raw_document_count=len(web_result.fetched_documents),
        llm_document_count=len(documents),
        score_gap_count=len(score_gaps),
        timeout_seconds=inputs.theme_evidence_review_timeout_seconds,
    )
    return agent.route(
        ThemeRouteInput(
            company_name=inputs.company_name,
            symbol=inputs.symbol,
            sector=inputs.sector,
            market=inputs.market.value,
            as_of_date=inputs.as_of_date,
            stage_context=inputs.stage_context,
            candidate_reason_codes=tuple(dict.fromkeys((*inputs.candidate_reason_codes, *_score_gap_reason_codes(score, score_gaps)))),
            current_large_sector_id=theme_route.large_sector_id if theme_route else None,
            current_canonical_archetype_id=theme_route.canonical_archetype_id if theme_route else None,
            search_results=search_results,
            documents=documents,
            score_gap_context=tuple(
                dict.fromkeys(
                    (
                        *score_gaps,
                        *_source_field_contract_gap_context(source_fields),
                        *_theme_route_contract_gap_context(theme_route),
                    )
                )
            ),
        )
    )


def _score_gap_reason_codes(score: ScoreSnapshot, gaps: Sequence[str]) -> tuple[str, ...]:
    codes = [f"SCORE_GAP:{item}" for item in gaps]
    codes.append(f"RAW_SCORE_TOTAL_BEFORE_GAP:{round(float(score.total_score), 4)}")
    return tuple(codes)


def _source_field_contract_gap_context(source_fields: Mapping[str, Any]) -> tuple[str, ...]:
    canonical = str(source_fields.get("canonical_archetype_id") or "").strip()
    missing = str(source_fields.get("evidence_contract_missing_primitives") or "").strip()
    required = str(source_fields.get("evidence_contract_required_primitives") or "").strip()
    axes = str(source_fields.get("evidence_contract_required_bridge_axes") or "").strip()
    bridge_group = str(source_fields.get("evidence_contract_runtime_bridge_group") or "").strip()
    positive_missing = str(source_fields.get("evidence_contract_positive_missing_primitives") or "").strip()
    positive_required = str(source_fields.get("evidence_contract_positive_primitives") or "").strip()
    green_gate_missing = str(source_fields.get("evidence_contract_green_gate_missing_primitives") or "").strip()
    green_gate_required = str(source_fields.get("evidence_contract_green_gate_primitives") or "").strip()
    guard_required = str(source_fields.get("evidence_contract_guard_primitives") or "").strip()
    guard_present = str(source_fields.get("evidence_contract_guard_present_primitives") or "").strip()
    guard_missing = str(source_fields.get("evidence_contract_guard_missing_primitives") or "").strip()
    if not canonical or not required:
        return ()
    if positive_required:
        missing_text = positive_missing or "none"
    elif "evidence_contract_positive_primitives" in source_fields:
        missing_text = "none"
    else:
        missing_text = missing or "none"
    return (
        (
            f"archetype_evidence_contract:{canonical}; "
            f"bridge_group={bridge_group or 'unknown'}; "
            f"required_primitives={required}; "
            f"missing_required_primitives={missing or 'none'}; "
            f"positive_primitives={positive_required or 'none'}; "
            f"missing_positive_primitives={missing_text}; "
            f"green_gate_primitives={green_gate_required or 'none'}; "
            f"missing_green_gate_primitives={green_gate_missing or 'none'}; "
            f"guard_primitives_to_check={guard_required or 'none'}; "
            f"present_guard_primitives={guard_present or 'none'}; "
            f"missing_guard_primitives={guard_missing or 'none'}; "
            f"required_bridge_axes={axes or 'unknown'}; "
            "expand source-backed issuer-scoped claims for missing positive primitives where applicable and verify guard primitives before score/stage finalisation"
        ),
    )


def _llm_query_retry_context(
    *,
    phase: str,
    retry_index: int,
    previous_rejections: Sequence[str],
    missing_information: Sequence[str] = (),
) -> tuple[str, ...]:
    if retry_index <= 0 and not previous_rejections:
        return ()
    rejection_text = ""
    if previous_rejections:
        rejection_text = f" Previous suggested queries were not executable because: {', '.join(previous_rejections)}."
    missing_text = ""
    if missing_information:
        missing_text = f" Missing information still unresolved: {', '.join(str(item) for item in missing_information)}."
    return (
        (
            f"{phase}_retry_{retry_index}: previous LLM suggested_queries did not produce new executable searches."
            f"{rejection_text}{missing_text} Produce different concrete company-scoped queries for the unresolved evidence gaps."
        ),
    )


def _score_gap_context_for_retry(
    gaps: Sequence[str],
    retry_index: int,
    previous_rejections: Sequence[str] = (),
) -> tuple[str, ...]:
    if retry_index <= 0 and not previous_rejections:
        return tuple(gaps)
    rejection_text = ""
    if previous_rejections:
        rejection_text = f" Previous suggested queries were not executable because: {', '.join(previous_rejections)}."
    retry_reason = "previous score-gap route did not produce new executable searches"
    if "query_task_alignment_rejected" in set(previous_rejections):
        retry_reason = "previous score-gap route rejected suggested_queries because query/task primitive alignment failed"
    elif {"llm_returned_no_suggested_queries", "agentic_follow_up_no_suggested_queries"} & set(previous_rejections):
        retry_reason = "previous score-gap route returned no suggested_queries and did not produce new executable searches"
    return tuple(
        dict.fromkeys(
            (
                *gaps,
                (
                    f"retry_{retry_index}: {retry_reason}."
                    f"{rejection_text} Produce different concrete company-scoped queries for the unresolved score gaps."
                ),
            )
        )
    )


def _only_budget_rejections(rejections: Sequence[str]) -> bool:
    budget_reasons = {
        "budget_denied",
        "daily_query_budget_exhausted",
        "symbol_query_budget_exhausted",
        "deep_research_symbol_budget_exhausted",
        "active_monitoring_symbol_budget_exhausted",
    }
    return bool(rejections) and all(item in budget_reasons for item in rejections)


def _retry_should_stop(
    *,
    retry_index: int,
    max_retries: int | None,
    previous_rejections: Sequence[str],
    seen_failures: set[tuple[str, ...]],
) -> bool:
    if max_retries is not None:
        return retry_index >= max_retries
    signature = tuple(dict.fromkeys(previous_rejections)) or ("no_executable_searches",)
    if signature in seen_failures:
        return True
    seen_failures.add(signature)
    return False


def _score_gap_missing_information(score: ScoreSnapshot) -> tuple[str, ...]:
    gaps: list[str] = []
    diagnostics = score.diagnostic_scores
    if _diagnostic_value(diagnostics, "estimate_missing_eps_source") > 0.0:
        gaps.append("score_gap:selected_eps_source_missing; evidence_need: source-backed EPS estimate, consensus, guidance, or report bridge")
    if _diagnostic_value(diagnostics, "estimate_missing_revision_source") > 0.0:
        gaps.append("score_gap:selected_revision_source_missing; evidence_need: source-backed estimate/revision bridge for EPS OP FCF target-price or analyst-consensus changes")
    if _diagnostic_value(diagnostics, "estimate_missing_fcf_source") > 0.0:
        gaps.append("score_gap:selected_fcf_source_missing; evidence_need: source-backed FCF, operating-cash-flow, conversion, guidance, or consensus bridge")
    if _diagnostic_value(diagnostics, "estimate_missing_op_source") > 0.0:
        gaps.append("score_gap:selected_operating_profit_source_missing; evidence_need: source-backed operating-profit estimate, consensus, guidance, or report bridge")
    if _diagnostic_value(diagnostics, "revision_score") < 80.0:
        gaps.append("revision estimate consensus target price EPS OP FCF")
    if score.eps_fcf_explosion_score < 12.0:
        gaps.append("earnings profit sales FCF margin actual forecast visibility")
    if score.earnings_visibility_score < 14.0 or _diagnostic_value(diagnostics, "structural_visibility_quality") < 60.0:
        gaps.append("visibility earnings profit revenue FCF margin guidance backlog RPO")
    if score.bottleneck_pricing_score < 14.0:
        gaps.append("pricing bottleneck shortage capacity CAPA ASP supply")
    if _diagnostic_value(diagnostics, "contract_required_for_green") >= 1.0 and _diagnostic_value(diagnostics, "contract_quality") < 45.0:
        gaps.append("contract backlog RPO prepayment order allocation")
    if _diagnostic_value(diagnostics, "backlog_rpo_visibility") < 45.0:
        gaps.append("backlog RPO order allocation revenue visibility contract")
    if _diagnostic_value(diagnostics, "capa_constraint") < 45.0:
        gaps.append("capacity CAPA utilization lead time allocation bottleneck")
    if _diagnostic_value(diagnostics, "asp_pricing_power") < 45.0:
        gaps.append("ASP pricing power price increase premium mix")
    if score.market_mispricing_score < 9.0:
        gaps.append("mispricing valuation revision target price consensus")
    if score.valuation_rerating_score < 9.0:
        gaps.append("valuation rerating multiple PER PBR target price")
    if _diagnostic_value(diagnostics, "valuation_score") < 45.0:
        gaps.append("valuation PER PBR EV EBITDA market cap earnings target multiple")
    if score.capital_allocation_score < 2.5:
        gaps.append("capital CAPEX investment buyback dividend shareholder")
    if score.information_confidence_score < 4.0:
        gaps.append("report disclosure news consensus source confidence")
    if _diagnostic_value(diagnostics, "fcf_quality_score") < 50.0:
        gaps.append("FCF conversion operating cash flow free cash flow net income cashflow quality")
    if _diagnostic_value(diagnostics, "actual_profit_conversion_score") < 50.0:
        gaps.append("actual sales growth OPM change FCF operating profit margin inventory receivables working capital")
    if _diagnostic_value(diagnostics, "domain_specific_evidence_score") < 35.0:
        gaps.append("domain-specific operating KPI revenue conversion customer demand unit economics product mix")
    if _diagnostic_value(diagnostics, "recurring_demand_visibility") < 35.0:
        gaps.append("recurring demand repeat purchase retention channel sell-through customer renewal")
    if _diagnostic_value(diagnostics, "export_channel_visibility") < 35.0:
        gaps.append("export mix export growth regional sales overseas channel US Europe customer")
    if _diagnostic_value(diagnostics, "medium_term_revision_visibility") < 50.0:
        gaps.append("medium-term guidance FY1 FY2 revenue OP EPS FCF estimate visibility")
    if _diagnostic_value(diagnostics, "sector_visibility_score") < 45.0:
        gaps.append("sector visibility customer demand orders sell-through backlog guidance")
    if _diagnostic_value(diagnostics, "sector_bottleneck_score") < 45.0:
        gaps.append("sector bottleneck capacity utilization lead time pricing shortage supply")
    if _diagnostic_value(diagnostics, "price_only_blowoff_score") >= 60.0:
        gaps.append("price-only blowoff guard: expand non-price evidence for earnings, FCF, orders, backlog, disclosures, reports, and company catalyst confirmation")
    if _diagnostic_value(diagnostics, "theme_overheat_score") >= 60.0:
        gaps.append("theme overheat guard: expand source-backed revenue EPS FCF valuation bridge and contradiction evidence before treating price/theme momentum as rerating")
    if _diagnostic_value(diagnostics, "snippet_only_green_block") > 0.0:
        gaps.append("snippet-only Green block: expand full article report disclosure or primary-source document with date-verified evidence")
    if _diagnostic_value(diagnostics, "emerging_theme_active") > 0.0 and _diagnostic_value(diagnostics, "llm_deep_research_completed") < 100.0:
        gaps.append("emerging theme requires completed deep research: expand company-specific theme-to-revenue EPS FCF RPO backlog margin bridge")
    if _diagnostic_value(diagnostics, "emerging_theme_active") > 0.0 and _diagnostic_value(diagnostics, "green_unlock_evidence_score") < 60.0:
        gaps.append("emerging theme Green unlock evidence: expand source-backed company revenue bridge, FCF bridge, customer contract, capacity, pricing, and valuation runway")
    if _diagnostic_value(diagnostics, "date_unverified_snippet_news_count_capped") > 0.0:
        gaps.append("date-unverified snippet evidence: expand date-verified full news report disclosure or filing visible by as_of_date")
    if _diagnostic_value(diagnostics, "date_unverified_document_count_capped") > 0.0:
        gaps.append("date-unverified document evidence: expand date-verified report disclosure news filing or primary-source document visible by as_of_date")
    if _diagnostic_value(diagnostics, "report_date_confidence") < 1.0:
        gaps.append("date-unverified document evidence: expand date-verified full report disclosure news filing or primary-source document visible by as_of_date")
    if _diagnostic_value(diagnostics, "v12_scope_stage2_required_bridge_match") > 0.0 and _diagnostic_value(diagnostics, "cross_evidence_family_count") < 3.0:
        gaps.append("stage2 non-price bridge: expand financial actual disclosure research report consensus revision and full news evidence beyond price-only signal")
    if _diagnostic_value(diagnostics, "evidence_family_price") <= 0.0:
        gaps.append("price history market cap close shares valuation price path")
    if _diagnostic_value(diagnostics, "evidence_family_financial_actual") <= 0.0:
        gaps.append("financial actual quarterly sales operating profit net income FCF OPM inventory receivables")
    if _diagnostic_value(diagnostics, "evidence_family_disclosure") <= 0.0:
        gaps.append("filing disclosure contract investment order capacity customer allocation")
    if _diagnostic_value(diagnostics, "evidence_family_research_report") <= 0.0:
        gaps.append("research report analyst report target price earnings estimate thesis")
    if _diagnostic_value(diagnostics, "evidence_family_consensus") <= 0.0:
        gaps.append("consensus FY1 FY2 estimates PER PBR target price analyst count")
    if _diagnostic_value(diagnostics, "evidence_family_consensus_revision") <= 0.0:
        gaps.append("consensus revision EPS OP FCF target price change estimate upgrade downgrade")
    if _diagnostic_value(diagnostics, "evidence_family_news") <= 0.0 and _diagnostic_value(diagnostics, "evidence_family_search_snippet_news") <= 0.0:
        gaps.append("news catalyst company event order customer demand margin change")
    if _diagnostic_value(diagnostics, "one_off_shortage_risk") >= 60.0:
        gaps.append("risk slowdown decline inventory receivable demand normalization")
    return tuple(dict.fromkeys(gaps))


def _score_gap_state_signature(
    score: ScoreSnapshot,
    red_team: RedTeamAssessment,
    source_fields: Mapping[str, Any] | None = None,
) -> tuple[str, ...]:
    gaps = tuple(dict.fromkeys((*_score_gap_missing_information(score), *_stage_gate_missing_information(score, red_team))))
    components = (
        f"total={round(float(score.total_score), 4)}",
        f"eps={round(float(score.eps_fcf_explosion_score), 4)}",
        f"visibility={round(float(score.earnings_visibility_score), 4)}",
        f"bottleneck={round(float(score.bottleneck_pricing_score), 4)}",
        f"mispricing={round(float(score.market_mispricing_score), 4)}",
        f"valuation={round(float(score.valuation_rerating_score), 4)}",
        f"capital={round(float(score.capital_allocation_score), 4)}",
        f"info={round(float(score.information_confidence_score), 4)}",
        f"risk={round(float(score.risk_penalty), 4)}",
    )
    return tuple((*components, *_source_field_contract_state_signature(source_fields or {}), *gaps))


def _source_field_contract_state_signature(source_fields: Mapping[str, Any]) -> tuple[str, ...]:
    keys = (
        "canonical_archetype_id",
        "evidence_contract_required_primitives",
        "evidence_contract_missing_primitives",
        "evidence_contract_positive_missing_primitives",
        "evidence_contract_green_gate_missing_primitives",
        "evidence_contract_guard_present_primitives",
        "evidence_contract_guard_missing_primitives",
    )
    parts: list[str] = []
    for key in keys:
        value = str(source_fields.get(key) or "").strip()
        if value:
            parts.append(f"{key}={value}")
    return tuple(parts)


_STAGE_GATE_GAP_CONTEXT = {
    "failed_stage2_total_score": "stage2 total score gate failed; expand source-backed company evidence for actual earnings, FCF, valuation, and catalyst conversion",
    "failed_stage2_eps_fcf": "stage2 EPS/FCF gate failed; expand actual and forward EPS, OP, FCF, cashflow, and margin evidence",
    "failed_stage2_valuation": "stage2 valuation gate failed; expand valuation, PER, PBR, EV EBITDA, market cap, target price, and earnings estimate evidence",
    "failed_stage2_information_confidence": "stage2 information-confidence gate failed; expand independent report, disclosure, news, consensus, and source confidence evidence",
    "failed_stage2_red_team": "stage2 red-team gate failed; expand source-backed thesis-break, accounting, legal, slowdown, cancellation, and risk-reversal evidence",
    "failed_stage2_non_price_bridge": "stage2 non-price bridge gate failed; expand financial actual, disclosure, research report, consensus revision, and full news evidence beyond price-only movement",
    "failed_stage3_total_score": "stage3 Green total score gate failed; expand the weakest source-backed score components before final stage classification",
    "failed_stage3_eps_fcf": "stage3 Green EPS/FCF gate failed; expand EPS, OP, FCF, sales growth, OPM, conversion, and forward estimate evidence",
    "failed_stage3_visibility": "stage3 Green earnings visibility gate failed; expand guidance, backlog, RPO, contract duration, customer demand, and revenue visibility evidence",
    "failed_stage3_bottleneck": "stage3 Green bottleneck/pricing gate failed; expand shortage, capacity, utilization, lead time, ASP, pricing power, allocation, and supply evidence",
    "failed_stage3_market_mispricing": "stage3 Green mispricing gate failed; expand consensus revision, target price, valuation runway, market expectation, and estimate-change evidence",
    "failed_stage3_valuation": "stage3 Green valuation gate failed; expand PER, PBR, EV EBITDA, market cap, target multiple, earnings, and rerating runway evidence",
    "failed_stage3_revision": "stage3 Green revision gate failed; expand EPS, OP, FCF, target price, consensus revision, analyst upgrade, and estimate-change evidence",
    "failed_stage3_contract_quality": "stage3 Green contract-quality gate failed; expand source-backed contract amount, duration, customer, cancellation terms, prepayment, backlog, and RPO evidence",
    "failed_structural_visibility_quality": "stage3 Green structural visibility gate failed; expand source-backed recurring demand, backlog, RPO, guidance, contract, utilization, and multi-quarter visibility evidence",
    "failed_sector_visibility": "stage3 sector visibility gate failed; expand source-backed sector demand, customer orders, sell-through, backlog, and guidance evidence",
    "failed_sector_bottleneck": "stage3 sector bottleneck gate failed; expand source-backed sector capacity, utilization, lead time, price increase, shortage, and supply evidence",
    "failed_green_cross_evidence": "stage3 Green cross-evidence gate failed; expand missing independent evidence families rather than relying on one source type",
    "failed_report_date_confidence": "stage3 Green report-date confidence gate failed; expand date-verified report, disclosure, news, or filing evidence visible by as_of_date",
    "failed_date_unverified_green_evidence": "stage3 Green date-unverified evidence gate failed; replace undated snippets or documents with date-verified full news, reports, disclosures, filings, or primary-source evidence visible by as_of_date",
    "failed_domain_specific_evidence": "stage3 domain-specific evidence gate failed; expand operating KPI, customer demand, unit economics, product mix, paid conversion, and revenue conversion evidence",
    "failed_stage3_one_off_shortage_risk": "stage3 Green one-off shortage risk gate failed; expand evidence distinguishing structural demand from one-off cost, temporary shortage, inventory, receivables, and demand normalization",
    "failed_stage3_red_team": "stage3 Green red-team gate failed; expand source-backed accounting, legal, customer cancellation, slowdown, valuation crowding, thesis-break, and risk mitigation evidence",
    "failed_stage3_yellow_calibrated_total": "stage3 Yellow total gate failed; expand source-backed evidence for candidate promotion before final stage classification",
    "failed_positive_stage_price_only_blowoff": "positive-stage price-only blowoff guard failed; expand non-price evidence that ties price movement to target-company earnings, FCF, orders, backlog, disclosures, reports, or durable catalyst conversion",
    "failed_snippet_only_green_block": "snippet-only Green guard failed; expand full-text date-verified news, report, disclosure, filing, or primary-source evidence before Green promotion",
    "failed_emerging_theme_deep_research": "emerging-theme deep research gate failed; expand company-specific theme-to-revenue, EPS, FCF, RPO, backlog, margin, customer, capacity, and valuation evidence",
    "failed_emerging_theme_green_unlock_evidence": "emerging-theme Green unlock gate failed; expand source-backed revenue bridge, FCF bridge, contract/customer bridge, capacity/pricing bridge, and valuation runway evidence",
    "failed_emerging_theme_date_verified_evidence": "emerging-theme date verification gate failed; expand date-verified documents visible by as_of_date rather than undated snippets",
    "failed_theme_overheat_risk": "theme-overheat guard failed; expand source-backed fundamental bridge and contradiction evidence so theme momentum is not treated as unsupported rerating",
    "failed_evidence_contract_positive_coverage": "evidence contract Green gate primitive coverage failed; expand source-backed issuer-scoped claims for missing archetype positive and Green-gate primitives before final score/stage classification",
    "failed_evidence_contract_guard_present": "evidence contract guard primitive is present; expand source-backed contradiction, mitigation, cancellation, slowdown, thesis-break, and guard verification evidence before Green promotion",
    "failed_evidence_contract_guard_unverified": "evidence contract guard primitive is missing or unverified; expand source-backed issuer-scoped claims that verify or refute the configured guard primitives before Green promotion",
    "failed_claim_backed_green_score": "claim-backed Green score gate failed; expand source-backed claim evidence and component-to-claim mapping for every nonzero score contribution before final score/stage classification",
}


def _stage_gate_missing_information(score: ScoreSnapshot, red_team: RedTeamAssessment) -> tuple[str, ...]:
    diagnostics = diagnose_stage_gates(score, red_team)
    gaps: list[str] = []
    for gate_name in diagnostics.failed_gate_names:
        context = _STAGE_GATE_GAP_CONTEXT.get(gate_name)
        if context:
            value = diagnostics.values_vs_thresholds.get(gate_name, {}).get("value")
            threshold = diagnostics.values_vs_thresholds.get(gate_name, {}).get("threshold")
            gaps.append(f"{context}; gate={gate_name}; value={value}; threshold={threshold}")
    if diagnostics.missing_evidence_families:
        gaps.append(
            "missing independent evidence families for stage gate: "
            + ", ".join(diagnostics.missing_evidence_families)
            + "; expand source-backed evidence for these families"
        )
    return tuple(dict.fromkeys(gaps))


def _with_stage_gate_diagnostics(
    diagnostics: Mapping[str, object],
    score: ScoreSnapshot,
    red_team: RedTeamAssessment,
) -> Mapping[str, object]:
    stage_gates = diagnose_stage_gates(score, red_team)
    payload = {
        "stage2_gate_passed": stage_gates.stage2_gate_passed,
        "stage3_green_gate_passed": stage_gates.stage3_green_gate_passed,
        "stage4a_continuation_gate_passed": stage_gates.stage4a_continuation_gate_passed,
        "stage4b_overlay_gate_passed": stage_gates.stage4b_overlay_gate_passed,
        "stage4c_thesis_break_gate_passed": stage_gates.stage4c_thesis_break_gate_passed,
        "failed_gate_names": tuple(stage_gates.failed_gate_names),
        "values_vs_thresholds": {
            name: dict(values)
            for name, values in stage_gates.values_vs_thresholds.items()
        },
        "sector_profile": stage_gates.sector_profile,
        "structural_visibility_quality": stage_gates.structural_visibility_quality,
        "sector_visibility_score": stage_gates.sector_visibility_score,
        "sector_bottleneck_score": stage_gates.sector_bottleneck_score,
        "cross_evidence_families_present": tuple(stage_gates.cross_evidence_families_present),
        "missing_evidence_families": tuple(stage_gates.missing_evidence_families),
        "promotion_band": stage_gates.promotion_band,
    }
    green_gate_names = {
        "failed_structural_visibility_quality",
        "failed_sector_visibility",
        "failed_sector_bottleneck",
        "failed_green_cross_evidence",
        "failed_report_date_confidence",
        "failed_date_unverified_green_evidence",
        "failed_domain_specific_evidence",
        "failed_evidence_contract_positive_coverage",
        "failed_evidence_contract_guard_present",
        "failed_evidence_contract_guard_unverified",
        "failed_claim_backed_green_score",
        "failed_positive_stage_price_only_blowoff",
        "failed_snippet_only_green_block",
        "failed_emerging_theme_deep_research",
        "failed_emerging_theme_green_unlock_evidence",
        "failed_emerging_theme_date_verified_evidence",
        "failed_theme_overheat_risk",
    }
    failed_green_gates = tuple(
        name
        for name in stage_gates.failed_gate_names
        if name.startswith("failed_stage3") or name in green_gate_names
    )
    return {
        **dict(diagnostics),
        "stage_gate_diagnostics": payload,
        "failed_green_gates": failed_green_gates,
    }


def _diagnostic_value(diagnostics: Mapping[str, Any], key: str) -> float:
    return diagnostic_value(diagnostics.get(key, 0.0))


def _query_limit_reached(queries: Sequence[str], limit: int | None) -> bool:
    return limit is not None and len(tuple(dict.fromkeys(queries))) >= limit


def _post_parse_gap_query_spec(
    *,
    query: str,
    inputs: FreeWebResearchInput,
    query_index: int,
) -> QuerySpec:
    return QuerySpec(
        group="post_parse_gap",
        query=query.strip(),
        priority=130 + query_index,
        company_name=inputs.company_name,
        symbol=inputs.symbol,
        sector=inputs.sector,
        market=inputs.market,
        as_of_date=inputs.as_of_date,
    )


def _post_score_gap_query_spec(
    *,
    query: str,
    inputs: FreeWebResearchInput,
    query_index: int,
) -> QuerySpec:
    return QuerySpec(
        group="post_score_gap",
        query=query.strip(),
        priority=170 + query_index,
        company_name=inputs.company_name,
        symbol=inputs.symbol,
        sector=inputs.sector,
        market=inputs.market,
        as_of_date=inputs.as_of_date,
    )


def _post_gap_top_results(inputs: FreeWebResearchInput, gap_specs: Sequence[QuerySpec]) -> int | None:
    query_count = len(tuple(dict.fromkeys(spec.query for spec in gap_specs)))
    if query_count <= 0:
        return 0
    return max(inputs.post_gap_fetch_min_results, query_count * inputs.post_gap_fetch_results_per_query)


def _merge_web_research_results(
    *,
    base: WebResearchResult,
    incremental: WebResearchResult,
    combined_query_plan: QueryPlan,
) -> WebResearchResult:
    selected_results, fetched_documents = _merge_selected_fetch_pairs(base, incremental)
    evidence_by_id = {item.evidence_id: item for item in (*base.evidence, *incremental.evidence)}
    return replace(
        base,
        query_plan=combined_query_plan,
        queries_run=tuple(dict.fromkeys((*base.queries_run, *incremental.queries_run))),
        search_results=_dedupe_search_results_by_url((*incremental.search_results, *base.search_results)),
        ranked_results=_dedupe_ranked_results_by_url((*incremental.ranked_results, *base.ranked_results)),
        selected_results=selected_results,
        fetched_documents=fetched_documents,
        parsed_reports=_dedupe_reports((*base.parsed_reports, *incremental.parsed_reports)),
        parsed_news=_dedupe_news((*base.parsed_news, *incremental.parsed_news)),
        parsed_disclosures=_dedupe_disclosures((*base.parsed_disclosures, *incremental.parsed_disclosures)),
        evidence=tuple(evidence_by_id.values()),
        red_team_findings=_dedupe_red_team_findings((*base.red_team_findings, *incremental.red_team_findings)),
        dropped_results=_dedupe_dropped_results((*base.dropped_results, *incremental.dropped_results)),
    )


def _web_research_result_for_queries(
    web_result: WebResearchResult,
    *,
    queries: Sequence[str],
) -> WebResearchResult:
    query_set = {str(query).strip() for query in queries if str(query).strip()}
    if not query_set:
        return replace(
            web_result,
            query_plan=replace(web_result.query_plan, queries=()),
            queries_run=(),
            search_results=(),
            ranked_results=(),
            selected_results=(),
            fetched_documents=(),
            parsed_reports=(),
            parsed_news=(),
            parsed_disclosures=(),
            evidence=(),
            red_team_findings=(),
            dropped_results=(),
        )

    selected_pairs = tuple(
        (ranked, fetched)
        for ranked, fetched in zip(web_result.selected_results, web_result.fetched_documents)
        if ranked.result.query in query_set
    )
    selected_urls = {ranked.result.url for ranked, _fetched in selected_pairs}
    query_specs = tuple(spec for spec in web_result.query_plan.queries if spec.query in query_set)
    return replace(
        web_result,
        query_plan=replace(web_result.query_plan, queries=query_specs),
        queries_run=tuple(query for query in web_result.queries_run if query in query_set),
        search_results=tuple(result for result in web_result.search_results if result.query in query_set),
        ranked_results=tuple(result for result in web_result.ranked_results if result.result.query in query_set),
        selected_results=tuple(ranked for ranked, _fetched in selected_pairs),
        fetched_documents=tuple(fetched for _ranked, fetched in selected_pairs),
        parsed_reports=tuple(
            report
            for report in web_result.parsed_reports
            if _parsed_item_source_url(report) in selected_urls
        ),
        parsed_news=tuple(
            news
            for news in web_result.parsed_news
            if _parsed_item_source_url(news) in selected_urls
        ),
        parsed_disclosures=tuple(
            disclosure
            for disclosure in web_result.parsed_disclosures
            if _parsed_item_source_url(disclosure) in selected_urls
        ),
        evidence=tuple(
            evidence
            for evidence in web_result.evidence
            if any(url in selected_urls for url in _evidence_url_keys(evidence))
        ),
        red_team_findings=(),
        dropped_results=tuple(
            item for item in web_result.dropped_results if getattr(getattr(item, "result", None), "query", None) in query_set
        ),
    )


def _parsed_item_source_url(item: Any) -> str | None:
    parsed_fields = getattr(item, "parsed_fields", None)
    if isinstance(parsed_fields, Mapping):
        for key in ("source_url", "url"):
            value = parsed_fields.get(key)
            if value:
                return str(value)
    url = getattr(item, "url", None)
    if url:
        return str(url)
    return None


def _merge_selected_fetch_pairs(
    base: WebResearchResult,
    incremental: WebResearchResult,
) -> tuple[tuple[RankedSearchResult, ...], tuple[Any, ...]]:
    pairs: list[tuple[RankedSearchResult, Any]] = []
    seen_urls: set[str] = set()
    for web_result in (incremental, base):
        for ranked, fetched in zip(web_result.selected_results, web_result.fetched_documents):
            url = ranked.result.url
            if url in seen_urls:
                continue
            pairs.append((ranked, fetched))
            seen_urls.add(url)
    return tuple(item[0] for item in pairs), tuple(item[1] for item in pairs)


def _dedupe_search_results_by_url(items: Sequence[SearchResult]) -> tuple[SearchResult, ...]:
    by_url: dict[str, SearchResult] = {}
    for item in items:
        by_url.setdefault(item.url, item)
    return tuple(by_url.values())


def _dedupe_ranked_results_by_url(items: Sequence[RankedSearchResult]) -> tuple[RankedSearchResult, ...]:
    by_url: dict[str, RankedSearchResult] = {}
    for item in items:
        by_url.setdefault(item.result.url, item)
    return tuple(by_url.values())


def _dedupe_red_team_findings(items: Sequence[RedTeamFinding]) -> tuple[RedTeamFinding, ...]:
    by_key = {
        (item.risk_type, item.description, item.is_hard_break, tuple(item.evidence_ids)): item
        for item in items
    }
    return tuple(by_key.values())


def _dedupe_dropped_results(items: Sequence[Any]) -> tuple[Any, ...]:
    by_key: dict[tuple[str, str], Any] = {}
    for item in items:
        result = getattr(item, "result", None)
        url = getattr(result, "url", None)
        reason = getattr(item, "reason", None)
        if not url:
            continue
        by_key.setdefault((str(url), str(reason or "")), item)
    return tuple(by_key.values())


def _merge_feature_input(
    *,
    inputs: FreeWebResearchInput,
    web_result: WebResearchResult,
    proxy: Any,
    route_large_sector_id: str | None,
    route_canonical_archetype_id: str | None,
    agent_extracted_fields: Mapping[str, bool | float | str],
) -> FeatureEngineeringInput:
    base = inputs.base_feature_input
    if base is not None:
        if base.symbol != inputs.symbol:
            raise ValueError("base_feature_input symbol must match research input symbol")
        if base.as_of_date != inputs.as_of_date:
            raise ValueError("base_feature_input as_of_date must match research input as_of_date")

    merged_agent_fields = dict(base.agent_extracted_fields) if base is not None else {}
    merged_agent_fields.update(agent_extracted_fields)
    return FeatureEngineeringInput(
        symbol=inputs.symbol,
        as_of_date=inputs.as_of_date,
        company_name=inputs.company_name or (base.company_name if base is not None else None),
        sector_context=inputs.sector or (base.sector_context if base is not None else None),
        large_sector_id=route_large_sector_id or (base.large_sector_id if base is not None else None),
        canonical_archetype_id=route_canonical_archetype_id or (base.canonical_archetype_id if base is not None else None),
        price_bars=base.price_bars if base is not None else (),
        financial_actuals=base.financial_actuals if base is not None else (),
        consensus=_dedupe_consensus((base.consensus if base is not None else ()) + tuple(proxy.consensus)),
        consensus_revisions=_dedupe_revisions(
            (base.consensus_revisions if base is not None else ()) + tuple(proxy.consensus_revisions)
        ),
        disclosures=_dedupe_disclosures((base.disclosures if base is not None else ()) + tuple(web_result.parsed_disclosures)),
        research_reports=_dedupe_reports((base.research_reports if base is not None else ()) + tuple(proxy.reports)),
        news_items=_dedupe_news((base.news_items if base is not None else ()) + tuple(web_result.parsed_news)),
        agent_extracted_fields=merged_agent_fields,
    )


def _with_report_consensus_proxy_evidence(
    *,
    inputs: FreeWebResearchInput,
    web_result: WebResearchResult,
    proxy: Any,
) -> WebResearchResult:
    proxy_evidence = evidence_from_feature_domains(
        market=inputs.market,
        fallback_symbol=inputs.symbol,
        consensus=proxy.consensus,
        consensus_revisions=proxy.consensus_revisions,
    )
    if not proxy_evidence:
        return web_result
    marked_proxy_evidence = []
    for item in proxy_evidence:
        parsed_fields = dict(item.parsed_fields)
        parsed_fields["consensus_proxy_created"] = True
        parsed_fields["consensus_proxy_source"] = "research_report"
        parsed_fields["derived_from_source_type"] = "research_report"
        marked_proxy_evidence.append(replace(item, parsed_fields=parsed_fields))
    by_id = {item.evidence_id: item for item in tuple(web_result.evidence) + tuple(marked_proxy_evidence)}
    return replace(web_result, evidence=tuple(by_id.values()))


def _dedupe_consensus(items):
    by_key = {(item.symbol, item.date, item.fiscal_year, item.source): item for item in items}
    return tuple(sorted(by_key.values(), key=lambda item: (item.date, item.fiscal_year, item.source)))


def _dedupe_revisions(items):
    by_key = {(item.symbol, item.date, item.fiscal_year, item.source): item for item in items}
    return tuple(sorted(by_key.values(), key=lambda item: (item.date, item.fiscal_year, item.source)))


def _dedupe_disclosures(items):
    by_key = {
        (item.symbol, item.rcept_no or item.title, item.published_at, item.source): item
        for item in items
    }
    return tuple(sorted(by_key.values(), key=lambda item: (item.published_at, item.rcept_no or item.title)))


def _dedupe_reports(items):
    by_key = {(item.symbol, item.publish_date, item.broker, item.title): item for item in items}
    return tuple(sorted(by_key.values(), key=lambda item: (item.publish_date, item.broker, item.title)))


def _dedupe_news(items):
    by_key = {
        (
            item.symbol,
            item.published_at,
            item.source,
            item.parsed_fields.get("source_url") or item.parsed_fields.get("url") or item.title,
        ): item
        for item in items
    }
    return tuple(sorted(by_key.values(), key=lambda item: (item.published_at, item.source, item.title)))


def _theme_route_documents(
    web_result: WebResearchResult,
    *,
    limit: int | None = None,
    excerpt_chars: int = 2_400,
) -> tuple[ThemeRouteDocument, ...]:
    evidence_by_url = _evidence_by_url(web_result)
    documents: list[ThemeRouteDocument] = []
    for ranked_result, fetch in zip(web_result.selected_results, web_result.fetched_documents):
        if limit is not None and len(documents) >= limit:
            break
        result = ranked_result.result
        evidence_items = evidence_by_url.get(result.url, ())
        parsed_fields: dict[str, bool | float | str] = {}
        evidence_ids: list[str] = []
        for item in evidence_items:
            evidence_ids.append(item.evidence_id)
            parsed_fields.update(_safe_theme_parsed_fields(item.parsed_fields))
        document_ref = _theme_route_document_ref(result, fetch)
        if document_ref:
            evidence_ids.append(document_ref)
        documents.append(
            ThemeRouteDocument(
                title=result.title,
                url=result.url,
                source=result.source,
                published_at=result.published_at.isoformat() if result.published_at else None,
                query=result.query,
                fetch_ok=fetch.ok,
                fetch_reason=fetch.reason,
                text_excerpt=_theme_text_excerpt(fetch.text, limit=excerpt_chars),
                evidence_ids=tuple(dict.fromkeys(evidence_ids)),
                parsed_fields=parsed_fields,
            )
        )
    return tuple(documents)


def _theme_route_document_refs(web_result: WebResearchResult) -> tuple[str, ...]:
    refs = []
    for ranked_result, fetch in zip(web_result.selected_results, web_result.fetched_documents):
        ref = _theme_route_document_ref(ranked_result.result, fetch)
        if ref:
            refs.append(ref)
    return tuple(dict.fromkeys(refs))


def _theme_route_document_ref(result: SearchResult, fetch: Any) -> str | None:
    if not getattr(fetch, "ok", False) or not getattr(fetch, "text", None):
        return None
    content_key = hashlib.sha1(str(fetch.text).encode("utf-8", errors="ignore")).hexdigest()[:16]
    url_key = hashlib.sha1(str(result.url).encode("utf-8", errors="ignore")).hexdigest()[:16]
    return f"document_anchor:{url_key}:{content_key}"


def _is_theme_document_ref(ref: object) -> bool:
    return str(ref).startswith("document_anchor:")


def _evidence_by_url(web_result: WebResearchResult) -> dict[str, tuple[Any, ...]]:
    by_url: dict[str, list[Any]] = {}
    for evidence in web_result.evidence:
        for key in _evidence_url_keys(evidence):
            by_url.setdefault(key, []).append(evidence)
    return {key: tuple(value) for key, value in by_url.items()}


def _evidence_url_keys(evidence: Any) -> tuple[str, ...]:
    fields = getattr(evidence, "parsed_fields", {}) or {}
    keys = (
        getattr(evidence, "url_or_identifier", None),
        fields.get("source_url") if isinstance(fields, Mapping) else None,
        fields.get("url") if isinstance(fields, Mapping) else None,
    )
    return tuple(dict.fromkeys(str(item).strip() for item in keys if item and str(item).strip()))


def _safe_theme_parsed_fields(fields: Mapping[str, Any]) -> dict[str, bool | float | str]:
    clean: dict[str, bool | float | str] = {}
    for key, value in fields.items():
        key_text = str(key).strip()
        if not key_text or key_text in {"raw_text", "body", "document_text", "full_text"}:
            continue
        if isinstance(value, bool):
            clean[key_text] = value
        elif isinstance(value, (int, float)) and not isinstance(value, bool):
            clean[key_text] = float(value)
        elif isinstance(value, str):
            text = value.strip()
            if text and len(text) <= 300:
                clean[key_text] = text
    return clean


def _theme_text_excerpt(text: str | None, *, limit: int = 2_400) -> str | None:
    if not text:
        return None
    clean = re.sub(r"\s+", " ", text).strip()
    return clean[:limit] if clean else None


def _merge_theme_routes(existing: ThemeRouteOutput | None, review: ThemeRouteOutput) -> ThemeRouteOutput:
    if existing is None:
        return review
    if review.status in {"provider_error", "invalid_provider_output", "disabled_no_provider"}:
        return existing
    status = existing.status if review.status == "no_transition" else review.status
    return replace(
        existing,
        status=status,
        transition_detected=existing.transition_detected or review.transition_detected,
        route_confidence=max(existing.route_confidence, review.route_confidence),
        emerging_theme_id=review.emerging_theme_id or existing.emerging_theme_id,
        primary_route_id=review.primary_route_id or existing.primary_route_id,
        large_sector_id=review.large_sector_id or existing.large_sector_id,
        canonical_archetype_id=review.canonical_archetype_id or existing.canonical_archetype_id,
        secondary_archetype_ids=tuple(dict.fromkeys((*existing.secondary_archetype_ids, *review.secondary_archetype_ids))),
        normalized_parsed_fields={**existing.normalized_parsed_fields, **review.normalized_parsed_fields},
        diagnostic_scores={**existing.diagnostic_scores, **review.diagnostic_scores},
        evidence_slots=review.evidence_slots or existing.evidence_slots,
        missing_information=review.missing_information or existing.missing_information,
        suggested_queries=tuple(dict.fromkeys((*existing.suggested_queries, *review.suggested_queries))),
        blocked_reason=review.blocked_reason or existing.blocked_reason,
    )


def _gate_theme_route_to_web_evidence(
    *,
    route: ThemeRouteOutput | None,
    diagnostics: Mapping[str, object],
    web_result: WebResearchResult,
) -> tuple[ThemeRouteOutput | None, Mapping[str, object]]:
    if route is None:
        return None, diagnostics
    document_refs = _theme_route_document_refs(web_result)
    available = {item.evidence_id for item in web_result.evidence}
    available.update(document_refs)
    gated_slots: list[Any] = []
    matched_refs: list[str] = []
    unmatched_refs: list[str] = []
    for slot in route.evidence_slots:
        refs = tuple(ref for ref in slot.evidence_refs if ref in available)
        matched_refs.extend(refs)
        unmatched_refs.extend(ref for ref in slot.evidence_refs if ref not in available)
        if slot.status == "present" and not refs:
            gated_slots.append(
                replace(
                    slot,
                    status="unknown",
                    evidence_refs=(),
                    missing_reason=slot.missing_reason or "evidence_ref_not_found_in_web_result",
                )
            )
        else:
            gated_slots.append(replace(slot, evidence_refs=refs))
    gated = replace(route, evidence_slots=tuple(gated_slots))
    updated = dict(diagnostics)
    updated["theme_evidence_ref_match_count"] = len(tuple(dict.fromkeys(matched_refs)))
    updated["theme_evidence_ref_unmatched_count"] = len(tuple(dict.fromkeys(unmatched_refs)))
    updated["theme_document_ref_available_count"] = len(document_refs)
    source_backed = _has_source_backed_theme_slot(gated)
    if route.evidence_slots:
        updated["theme_evidence_gate_status"] = "source_backed" if source_backed else "no_matching_evidence_refs"
    else:
        updated["theme_evidence_gate_status"] = "no_evidence_slots"
    if not source_backed and route.status in {"transition_detected", "mixed_route"}:
        gated = _downgrade_unbacked_theme_route(gated)
        updated["theme_route_status"] = gated.status
        updated["large_sector_id"] = gated.large_sector_id
        updated["canonical_archetype_id"] = gated.canonical_archetype_id
        updated["blocked_reason"] = gated.blocked_reason
    return gated, updated


def _downgrade_unbacked_theme_route(route: ThemeRouteOutput) -> ThemeRouteOutput:
    missing = tuple(dict.fromkeys((*route.missing_information, "source_backed_evidence_refs_missing")))
    return replace(
        route,
        status="needs_more_evidence",
        transition_detected=False,
        large_sector_id=None,
        canonical_archetype_id=None,
        normalized_parsed_fields={},
        diagnostic_scores={},
        missing_information=missing,
        blocked_reason=route.blocked_reason or "theme_route_lacked_matching_source_backed_evidence_refs",
    )


def _initial_query_limit(inputs: FreeWebResearchInput) -> int | None:
    if not inputs.theme_rebalance_enabled or inputs.theme_route_provider is None:
        return None
    max_queries = inputs.budget.max_queries_per_symbol
    if max_queries is None:
        return None
    if max_queries <= 0:
        return 0
    reserve = min(max(0, inputs.theme_expansion_reserve_queries), max_queries)
    return max(1, max_queries - reserve)


def _theme_query_spec(
    *,
    query: str,
    inputs: FreeWebResearchInput,
    round_index: int,
    query_index: int,
) -> QuerySpec:
    return QuerySpec(
        group="deep_research",
        query=query.strip(),
        priority=90 + round_index * 10 + query_index,
        company_name=inputs.company_name,
        symbol=inputs.symbol,
        sector=inputs.sector,
        market=inputs.market,
        as_of_date=inputs.as_of_date,
    )


def _flatten_results(results_by_query: Mapping[str, Sequence[SearchResult]]) -> tuple[SearchResult, ...]:
    unique: dict[str, SearchResult] = {}
    for results in results_by_query.values():
        for item in results:
            unique.setdefault(item.url, item)
    return tuple(unique.values())


def _asof_safe_theme_query(query: str, as_of_date: date) -> str | None:
    clean = re.sub(r"\s+", " ", query).strip()
    if not clean:
        return None
    for match in re.finditer(r"\b(?:after|since|from):\s*(20\d{2}-\d{2}-\d{2})\b", clean, flags=re.IGNORECASE):
        try:
            if date.fromisoformat(match.group(1)) > as_of_date:
                return None
        except ValueError:
            return None
    return clean


def _company_scoped_query(query: str, inputs: FreeWebResearchInput) -> str:
    lowered = query.lower()
    aliases = tuple(
        dict.fromkeys(
            item.strip().lower()
            for item in (inputs.company_name, inputs.symbol, *inputs.company_aliases)
            if item and item.strip()
        )
    )
    if any(alias in lowered for alias in aliases):
        return query
    return f"{inputs.company_name} {query}".strip()


def _theme_route_run_diagnostics(
    route: ThemeRouteOutput,
    expansion_queries_run: Sequence[str],
    status: str,
) -> Mapping[str, object]:
    return {
        "theme_rebalance_status": status,
        "theme_route_status": route.status,
        "theme_route_confidence": route.route_confidence,
        "emerging_theme_id": route.emerging_theme_id,
        "primary_route_id": route.primary_route_id,
        "large_sector_id": route.large_sector_id,
        "canonical_archetype_id": route.canonical_archetype_id,
        "missing_information": route.missing_information,
        "evidence_contract_gap_context": _theme_route_contract_gap_context(route),
        "suggested_queries": route.suggested_queries,
        "expansion_queries_run": tuple(expansion_queries_run),
        "expansion_query_count": len(expansion_queries_run),
        "blocked_reason": route.blocked_reason,
    }


def _theme_route_scoring_ids(route: ThemeRouteOutput | None) -> tuple[str | None, str | None]:
    if route is None:
        return None, None
    if route.status not in {"transition_detected", "mixed_route"}:
        return None, None
    if route.route_confidence < 0.55:
        return None, None
    if not route.canonical_archetype_id:
        return None, None
    if not _has_source_backed_theme_slot(route):
        return None, None
    return route.large_sector_id, route.canonical_archetype_id


def _theme_route_can_contribute_fields(route: ThemeRouteOutput | None) -> bool:
    if route is None:
        return False
    if route.status not in {"transition_detected", "mixed_route"}:
        return False
    if route.route_confidence < 0.55:
        return False
    return _has_source_backed_theme_slot(route)


def _theme_route_contract_gap_context(route: ThemeRouteOutput | None) -> tuple[str, ...]:
    if route is None or not route.canonical_archetype_id:
        return ()
    present_primitives = tuple(_theme_route_agent_extracted_fields(route))
    return evidence_contract_gap_context(
        route.canonical_archetype_id,
        present_primitives=present_primitives,
    )


_UNSAFE_AGENT_FIELD_KEYS = {
    "stage",
    "deterministic_stage",
    "stage_override",
    "attempted_stage_override",
    "large_sector_id",
    "canonical_archetype_id",
}


def _theme_route_agent_extracted_fields(route: ThemeRouteOutput | None) -> dict[str, bool | float | str]:
    if not _theme_route_can_contribute_fields(route):
        return {}
    fields: dict[str, bool | float | str] = {}
    source_backed_slots = _source_backed_theme_slot_names(route, include_document_refs=False)
    for key, value in route.normalized_parsed_fields.items():
        key_text = str(key).strip()
        if not key_text or key_text in _UNSAFE_AGENT_FIELD_KEYS:
            continue
        if not _field_matches_source_backed_slot(key_text, source_backed_slots):
            continue
        if isinstance(value, bool):
            if value:
                fields[key_text] = True
        elif isinstance(value, (int, float)) and not isinstance(value, bool):
            fields[key_text] = float(value)
        elif isinstance(value, str):
            text = value.strip()
            if text and len(text) <= 300:
                fields[key_text] = text
    if route.transition_detected:
        fields.setdefault("theme_transition_detected", True)
    if route.emerging_theme_id:
        fields.setdefault("emerging_theme_active", True)
        fields.setdefault("emerging_theme_id", route.emerging_theme_id)
    return fields


_SYNTHETIC_AGENT_FIELD_KEYS = {
    "theme_transition_detected",
    "emerging_theme_active",
    "emerging_theme_id",
}


def _theme_route_agent_field_claim_diagnostics(
    *,
    route: ThemeRouteOutput | None,
    inputs: FreeWebResearchInput,
    agent_extracted_fields: Mapping[str, bool | float | str],
) -> Mapping[str, object]:
    if route is None or not agent_extracted_fields:
        return {}
    evidence_refs_by_field = _agent_field_evidence_refs_by_field(route, agent_extracted_fields)
    claims = []
    for field_key, refs in evidence_refs_by_field.items():
        for evidence_ref in refs:
            claims.extend(
                compile_claims_from_primitives(
                    evidence_id=evidence_ref,
                    symbol=inputs.symbol,
                    as_of_date=inputs.as_of_date,
                    primitive_ids=(field_key,),
                    archetype_id=route.canonical_archetype_id,
                    subject=inputs.company_name,
                    quote_text=f"LLM route normalized field: {field_key}",
                    confidence=route.route_confidence,
                    verified=True,
                )
            )
    if not claims:
        return {}
    metadata = dict(claim_metadata_from_claims(tuple(claims), as_of_date=inputs.as_of_date))
    return {
        "agent_field_claim_ledger_version": metadata["claim_ledger_version"],
        "agent_field_claim_count": metadata["compiled_claim_count"],
        "agent_field_claim_ids_by_primitive": metadata["compiled_claim_ids_by_primitive"],
        "agent_field_primitive_states": metadata["compiled_primitive_states"],
        "agent_field_evidence_refs_by_field": evidence_refs_by_field,
    }


def _claim_backed_theme_route_agent_fields(
    *,
    route: ThemeRouteOutput | None,
    inputs: FreeWebResearchInput,
    agent_extracted_fields: Mapping[str, bool | float | str],
) -> tuple[dict[str, Any], Mapping[str, object]]:
    fields = dict(agent_extracted_fields)
    diagnostics = _theme_route_agent_field_claim_diagnostics(
        route=route,
        inputs=inputs,
        agent_extracted_fields=agent_extracted_fields,
    )
    claim_ids_by_primitive = diagnostics.get("agent_field_claim_ids_by_primitive")
    if not isinstance(claim_ids_by_primitive, Mapping):
        return fields, diagnostics
    compiled_claim_ids = tuple(
        dict.fromkeys(
            str(claim_id).strip()
            for claim_ids in claim_ids_by_primitive.values()
            for claim_id in (claim_ids if isinstance(claim_ids, (list, tuple)) else (claim_ids,))
            if str(claim_id).strip()
        )
    )
    if not compiled_claim_ids:
        return fields, diagnostics
    fields.update(
        {
            "claim_ledger_version": diagnostics.get("agent_field_claim_ledger_version"),
            "compiled_claim_count": diagnostics.get("agent_field_claim_count"),
            "compiled_claim_ids": list(compiled_claim_ids),
            "compiled_claim_ids_by_primitive": {
                str(primitive): list(claim_ids if isinstance(claim_ids, (list, tuple)) else (claim_ids,))
                for primitive, claim_ids in claim_ids_by_primitive.items()
            },
            "compiled_primitive_states": diagnostics.get("agent_field_primitive_states"),
        }
    )
    return fields, diagnostics


def _agent_field_evidence_refs_by_field(
    route: ThemeRouteOutput,
    agent_extracted_fields: Mapping[str, bool | float | str],
) -> Mapping[str, tuple[str, ...]]:
    refs_by_field: dict[str, tuple[str, ...]] = {}
    for field_key in agent_extracted_fields:
        if field_key in _SYNTHETIC_AGENT_FIELD_KEYS:
            continue
        refs: list[str] = []
        for slot in route.evidence_slots:
            if slot.status != "present" or not slot.evidence_refs:
                continue
            if _field_matches_source_backed_slot(field_key, (slot.slot,)):
                refs.extend(ref for ref in slot.evidence_refs if not _is_theme_document_ref(ref))
        if refs:
            refs_by_field[field_key] = tuple(dict.fromkeys(refs))
    return refs_by_field


def _has_source_backed_theme_slot(route: ThemeRouteOutput) -> bool:
    return any(slot.status == "present" and slot.evidence_refs for slot in route.evidence_slots)


def _source_backed_theme_slot_names(
    route: ThemeRouteOutput,
    *,
    include_document_refs: bool = True,
) -> tuple[str, ...]:
    return tuple(
        str(slot.slot).strip()
        for slot in route.evidence_slots
        if slot.status == "present"
        and str(slot.slot).strip()
        and (
            bool(slot.evidence_refs)
            if include_document_refs
            else any(not _is_theme_document_ref(ref) for ref in slot.evidence_refs)
        )
    )


def _field_matches_source_backed_slot(field_key: str, source_backed_slots: Sequence[str]) -> bool:
    field_tokens = _evidence_slot_tokens(field_key)
    if not field_tokens:
        return False
    for slot in source_backed_slots:
        slot_tokens = _evidence_slot_tokens(slot)
        if not slot_tokens:
            continue
        if _ordered_tokens_contain(field_tokens, slot_tokens):
            return True
    return False


def _ordered_tokens_contain(container_tokens: Sequence[str], target_tokens: Sequence[str]) -> bool:
    if not container_tokens or not target_tokens:
        return False
    target_index = 0
    for token in container_tokens:
        if token == target_tokens[target_index]:
            target_index += 1
            if target_index == len(target_tokens):
                return True
    return False


def _evidence_slot_tokens(value: str) -> tuple[str, ...]:
    stop_words = {
        "and",
        "or",
        "the",
        "a",
        "an",
        "visible",
        "visibility",
        "confirmed",
        "confirm",
        "mentioned",
        "score",
        "pct",
        "percent",
        "growth",
        "route",
        "bridge",
        "evidence",
        "slot",
    }
    return tuple(
        token
        for token in re.split(r"[^A-Za-z0-9]+", str(value).lower())
        if token and token not in stop_words and len(token) > 1
    )


_THEME_STATUS_CODES = {
    "completed": 100.0,
    "no_transition": 10.0,
    "disabled_no_provider": 20.0,
    "needs_more_evidence": 25.0,
    "more_evidence_needed": 25.0,
    "provider_error": 30.0,
    "invalid_provider_output": 40.0,
    "budget_denied": 50.0,
    "captcha_or_block_detected": 60.0,
    "daily_query_budget_exhausted": 70.0,
    "symbol_query_budget_exhausted": 80.0,
    "deep_research_symbol_budget_exhausted": 90.0,
}

_THEME_ROUTE_SCORE_BLOCK_REASON_CODES = {
    "theme_route_missing": 10.0,
    "theme_route_provider_error": 20.0,
    "theme_route_invalid_provider_output": 25.0,
    "theme_route_disabled_no_provider": 30.0,
    "theme_route_needs_more_evidence": 40.0,
    "theme_route_budget_denied": 50.0,
    "theme_route_search_blocked": 60.0,
    "theme_route_low_confidence": 70.0,
    "theme_route_missing_canonical_archetype_id": 80.0,
    "theme_route_not_source_backed": 90.0,
    "theme_route_unapplied_to_scoring": 95.0,
}

_SCORE_GAP_BLOCK_REASON_CODES = {
    "score_gap_provider_error": 10.0,
    "score_gap_invalid_provider_output": 20.0,
    "score_gap_disabled_no_provider": 30.0,
    "score_gap_llm_no_suggested_queries": 40.0,
    "score_gap_no_executable_searches": 50.0,
    "score_gap_budget_blocked": 60.0,
    "score_gap_search_blocked": 70.0,
    "score_gap_unresolved": 80.0,
    "score_gap_round_limit": 85.0,
    "score_gap_no_progress": 90.0,
}

_AGENTIC_EVIDENCE_BLOCK_REASON_CODES = {
    "agentic_evidence_provider_error": 5.0,
    "agentic_evidence_missing_archetype": 7.0,
    "agentic_evidence_no_fetched_documents": 8.0,
    "agentic_evidence_no_accepted_mappings": 9.0,
    "agentic_evidence_missing_v2_score_contributions": 10.0,
    "agentic_evidence_claim_budget_limited": 11.0,
}

_AGENTIC_EVIDENCE_SCORE_BLOCK_STATUSES = {
    "disabled_no_provider": "agentic_evidence_provider_error",
    "provider_error": "agentic_evidence_provider_error",
    "contract_load_error": "agentic_evidence_provider_error",
    "contract_missing": "agentic_evidence_provider_error",
    "skipped_no_archetype": "agentic_evidence_missing_archetype",
    "no_fetched_documents": "agentic_evidence_no_fetched_documents",
    "completed_budget_limited": "agentic_evidence_claim_budget_limited",
    "partial_error_budget_limited": "agentic_evidence_claim_budget_limited",
}

_SCORE_GAP_FAILURE_STATUSES = {
    "provider_error",
    "invalid_provider_output",
    "disabled_no_provider",
    "llm_no_suggested_queries",
    "no_executable_searches",
    "budget_blocked",
    "round_limit_reached",
    "no_progress",
    "daily_query_budget_exhausted",
    "symbol_query_budget_exhausted",
    "deep_research_symbol_budget_exhausted",
    "active_monitoring_symbol_budget_exhausted",
    "captcha_or_block_detected",
    "stopped",
}

_SCORE_GAP_STAGE_COURT_DEFERRABLE_REASONS = {
    "score_gap_material_gaps_pending",
    "score_gap_no_progress",
    "score_gap_round_limit",
    "score_gap_unresolved",
}

_MATERIAL_SCORE_GAP_MARKERS = (
    "selected_eps_source_missing",
    "selected_revision_source_missing",
    "selected_fcf_source_missing",
    "selected_operating_profit_source_missing",
    "missing independent evidence families",
    "stage2 non-price bridge",
    "stage3 green cross-evidence gate failed",
    "price-only blowoff guard",
    "theme overheat guard",
    "date-unverified",
    "snippet-only",
    "emerging theme requires completed deep research",
    "emerging theme Green unlock evidence",
    "evidence contract Green gate",
    "evidence contract guard primitive",
    "claim-backed Green score",
    "agentic primitive gap",
)


def _theme_route_score_block_reason(
    *,
    inputs: FreeWebResearchInput,
    route: ThemeRouteOutput | None,
    diagnostics: Mapping[str, object],
    route_large_sector_id: str | None,
    route_canonical_archetype_id: str | None,
) -> str | None:
    if not inputs.require_valid_theme_route_for_scoring:
        return None
    if not inputs.theme_rebalance_enabled or inputs.theme_route_provider is None:
        return None
    if route_canonical_archetype_id:
        return None
    base = inputs.base_feature_input
    if base is not None and base.large_sector_id and base.canonical_archetype_id:
        return None
    if route is None:
        return "theme_route_missing"
    status = str(diagnostics.get("theme_rebalance_status") or route.status or "").strip()
    if status == "provider_error" or route.status == "provider_error":
        return "theme_route_provider_error"
    if status == "invalid_provider_output" or route.status == "invalid_provider_output":
        return "theme_route_invalid_provider_output"
    if status == "disabled_no_provider" or route.status == "disabled_no_provider":
        return "theme_route_disabled_no_provider"
    if status in {"budget_denied", "daily_query_budget_exhausted", "symbol_query_budget_exhausted", "deep_research_symbol_budget_exhausted"}:
        return "theme_route_budget_denied"
    if status == "captcha_or_block_detected":
        return "theme_route_search_blocked"
    if route.status in {"needs_more_evidence", "more_evidence_needed"}:
        return "theme_route_needs_more_evidence"
    if route.status in {"transition_detected", "mixed_route"}:
        if route.route_confidence < 0.55:
            return "theme_route_low_confidence"
        if not route.canonical_archetype_id:
            return "theme_route_missing_canonical_archetype_id"
        if not _has_source_backed_theme_slot(route):
            return "theme_route_not_source_backed"
        if not route_large_sector_id:
            return "theme_route_missing_canonical_archetype_id"
        return "theme_route_unapplied_to_scoring"
    return None


def _with_score_gap_expansion_diagnostics(
    diagnostics: Mapping[str, object],
    expansion: _ScoreGapExpansionResult,
    queries_run_so_far: Sequence[str],
) -> Mapping[str, object]:
    updated = dict(diagnostics)
    updated["post_score_gap_expansion_count"] = len(tuple(queries_run_so_far))
    updated["post_score_gap_expansion_queries"] = tuple(queries_run_so_far)
    updated["post_score_gap_expansion_status"] = expansion.status
    updated["post_score_gap_unresolved_gaps"] = tuple(expansion.unresolved_gaps)
    updated["material_score_gap_unresolved_gaps"] = _material_score_gaps(expansion.unresolved_gaps)
    updated["post_score_gap_rejection_reasons"] = tuple(expansion.rejection_reasons)
    updated.update(expansion.diagnostic_details)
    _apply_score_gap_route_plan_query_origin_diagnostics(updated)
    if expansion.blocked_reason:
        updated["post_score_gap_blocked_reason"] = expansion.blocked_reason
    return updated


def _source_route_plan_diagnostics(expansion: _ScoreGapExpansionResult) -> tuple[Mapping[str, object], ...]:
    raw = expansion.diagnostic_details.get("post_score_gap_source_route_plans", ())
    if not isinstance(raw, (list, tuple)):
        return ()
    return tuple(item for item in raw if isinstance(item, Mapping))


def _apply_score_gap_route_plan_query_origin_diagnostics(diagnostics: dict[str, object]) -> None:
    raw = diagnostics.get("post_score_gap_source_route_plans", ())
    route_plans = tuple(item for item in raw if isinstance(item, Mapping)) if isinstance(raw, (list, tuple)) else ()
    diagnostics["post_score_gap_query_origins"] = tuple(
        str(plan.get("query_origin") or "unknown")
        for plan in route_plans
    )
    diagnostics["post_score_gap_deterministic_fallback_query_used"] = any(
        bool(plan.get("deterministic_fallback_query_used"))
        for plan in route_plans
    )


def _with_agentic_score_contributions(
    feature_result: FeatureEngineeringResult,
    trace: AgenticEvidenceRuntimeTrace,
) -> FeatureEngineeringResult:
    rubric_archetype_id = _agentic_score_contribution_archetype_id(
        feature_result.payload.canonical_archetype_id,
        trace,
    )
    contributions = _agentic_score_contributions_from_trace(
        components=feature_result.payload.components,
        canonical_archetype_id=rubric_archetype_id,
        trace=trace,
    )
    if not contributions:
        return feature_result
    diagnostics = dict(feature_result.payload.diagnostic_scores)
    diagnostics["require_v2_score_contributions"] = 100.0
    diagnostics["agentic_score_contribution_v2_runtime_input"] = 100.0
    diagnostics["agentic_score_contribution_v2_rubric_source"] = 100.0
    _quarantine_legacy_parser_score_diagnostics_for_v2(diagnostics)
    if rubric_archetype_id and rubric_archetype_id == str(trace.archetype_id or "").strip():
        diagnostics["agentic_score_contribution_v2_trace_archetype_used"] = 100.0
    feature_source_fields = dict(feature_result.source_fields)
    _quarantine_legacy_parser_score_source_fields_for_v2(feature_source_fields)
    if rubric_archetype_id:
        feature_source_fields["agentic_score_contribution_v2_archetype_id"] = rubric_archetype_id
    feature_archetype_id = str(feature_result.payload.canonical_archetype_id or "").strip()
    trace_archetype_id = str(trace.archetype_id or "").strip()
    if feature_archetype_id and trace_archetype_id and feature_archetype_id != trace_archetype_id:
        diagnostics["agentic_score_contribution_v2_archetype_mismatch_overrode"] = 100.0
        feature_source_fields["agentic_score_contribution_v2_archetype_mismatch"] = (
            f"{feature_archetype_id}->{trace_archetype_id}"
        )
    payload = replace(
        feature_result.payload,
        diagnostic_scores=diagnostics,
        score_contributions_v2=contributions,
    )
    return replace(feature_result, payload=payload, source_fields=feature_source_fields)


def _quarantine_legacy_parser_score_diagnostics_for_v2(diagnostics: dict[str, float]) -> None:
    raw_count = diagnostics.get("legacy_parser_score_claim_without_v2_count_capped")
    if raw_count is None or float(raw_count) <= 0.0:
        return
    diagnostics["legacy_parser_score_claim_without_v2_quarantined_count_capped"] = min(float(raw_count), 100.0)
    diagnostics["legacy_parser_score_claim_without_v2_count_capped"] = 0.0
    diagnostics["legacy_parser_score_quarantined_by_v2_score_contributions"] = 100.0


def _quarantine_legacy_parser_score_source_fields_for_v2(source_fields: dict[str, object]) -> None:
    raw_fields = str(source_fields.get("legacy_parser_score_claim_fields_without_v2") or "").strip()
    if not raw_fields:
        return
    source_fields["legacy_parser_score_claim_fields_quarantined_by_v2"] = raw_fields
    source_fields["legacy_parser_score_claim_fields_without_v2"] = ""


def _agentic_score_contribution_archetype_id(
    feature_archetype_id: str | None,
    trace: AgenticEvidenceRuntimeTrace,
) -> str | None:
    """Use the Evidence OS contract id for claim-backed score contributions."""

    trace_archetype_id = str(trace.archetype_id or "").strip()
    if trace_archetype_id:
        return trace_archetype_id
    clean_feature_id = str(feature_archetype_id or "").strip()
    return clean_feature_id or None


def _agentic_score_contribution_diagnostics(
    contributions: Sequence[ScoreContributionV2],
) -> Mapping[str, object]:
    if not contributions:
        return {
            "agentic_score_contribution_v2_count": 0,
            "agentic_score_contribution_v2_nonzero_count": 0,
            "agentic_score_contribution_v2_cap_summaries": (),
            "agentic_score_contribution_v2_support_summaries": (),
        }
    cap_summaries: list[str] = []
    support_summaries: list[str] = []
    for item in contributions:
        if item.raw_points > 0.0 and item.support_claim_ids:
            support_summaries.append(
                f"{item.component_key}/{item.criterion_id}:raw={round(float(item.raw_points), 4)}; "
                f"claims={','.join(item.support_claim_ids[:4])}"
            )
            continue
        if item.cap_reason:
            cap_summaries.append(
                f"{item.component_key}/{item.criterion_id}:raw={round(float(item.raw_points), 4)}; "
                f"cap={item.cap_reason}"
            )
    return {
        "agentic_score_contribution_v2_count": len(contributions),
        "agentic_score_contribution_v2_nonzero_count": sum(1 for item in contributions if item.raw_points > 0.0),
        "agentic_score_contribution_v2_cap_summaries": tuple(cap_summaries[:20]),
        "agentic_score_contribution_v2_support_summaries": tuple(support_summaries[:20]),
    }


def _agentic_score_contributions_from_trace(
    *,
    components: Mapping[str, float],
    canonical_archetype_id: str | None,
    trace: AgenticEvidenceRuntimeTrace,
) -> tuple[ScoreContributionV2, ...]:
    if not trace.primitive_states or not canonical_archetype_id:
        return ()
    contract = load_evidence_contracts_v2().get(canonical_archetype_id)
    if contract is None or not contract.score_rubric:
        return ()
    primitive_states = {state.primitive_id: state for state in trace.primitive_states}
    return build_component_score_contributions_from_rubric(
        components=components,
        primitive_states=primitive_states,
        score_rubric=contract.score_rubric,
    )


def _agentic_stage_court_output(
    *,
    diagnostics: Mapping[str, object],
    trace: AgenticEvidenceRuntimeTrace,
    score: ScoreSnapshot,
    inputs: FreeWebResearchInput,
    theme_route: ThemeRouteOutput | None,
) -> StageCourtOutput | None:
    if not trace.primitive_states:
        return None
    archetype_id = str(theme_route.canonical_archetype_id or "").strip() if theme_route else ""
    if not archetype_id and inputs.base_feature_input is not None:
        archetype_id = str(inputs.base_feature_input.canonical_archetype_id or "").strip()
    if not archetype_id:
        archetype_id = str(trace.archetype_id or "").strip()
    if not archetype_id:
        return None
    try:
        contract = load_evidence_contracts_v2().get(archetype_id)
    except Exception:
        return None
    if contract is None:
        return None
    primitive_states = {state.primitive_id: state for state in trace.primitive_states}
    materiality_remaining = sum(
        max(
            float(
                _agentic_primitive_materiality_remaining(
                    state.primitive_id,
                    archetype_id=archetype_id,
                    existing_materiality=state.materiality_remaining_points,
                )
            ),
            0.0,
        )
        for state in trace.primitive_states
        if state.status == PrimitiveStatus.UNKNOWN
    )
    verified_score = _agentic_stage_court_verified_score(score=score, diagnostics=diagnostics)
    return decide_stage_court(
        StageCourtInput(
            score_interval=ScoreInterval(
                verified_score=verified_score,
                potential_score_upper_bound=min(100.0, verified_score + materiality_remaining),
                invalid_evidence=_score_validity_invalidates_stage_court(
                    score=score,
                    diagnostics=diagnostics,
                ),
                provider_failed=trace.status in {"provider_error", "disabled_no_provider"},
            ),
            primitive_states=primitive_states,
            contract=contract,
            current_hard_break_claim_ids=(),
            has_prior_live_thesis=inputs.previous_stage not in (None, Stage.STAGE_0),
        )
    )


def _agentic_stage_court_verified_score(
    *,
    score: ScoreSnapshot,
    diagnostics: Mapping[str, object],
) -> float:
    reason = str(diagnostics.get("score_blocked_reason") or "").strip()
    if reason.startswith("score_gap_"):
        for key in (
            "raw_score_total_before_score_gap_block",
            "raw_score_before_block",
        ):
            value = diagnostics.get(key)
            if value is None:
                value = score.diagnostic_scores.get(key)
            try:
                number = float(value)
            except (TypeError, ValueError):
                continue
            if number >= 0.0:
                return min(100.0, number)
    return float(score.total_score)


def _score_validity_invalidates_stage_court(
    *,
    score: ScoreSnapshot,
    diagnostics: Mapping[str, object],
) -> bool:
    reason = str(diagnostics.get("score_blocked_reason") or "").strip()
    if reason in _SCORE_GAP_STAGE_COURT_DEFERRABLE_REASONS:
        return False
    return score.diagnostic_scores.get("score_valid") == 0.0 or diagnostics.get("score_valid") is False


def _score_gap_block_should_defer_to_stage_court(
    *,
    reason: str | None,
    trace: AgenticEvidenceRuntimeTrace | None,
) -> bool:
    if reason not in _SCORE_GAP_STAGE_COURT_DEFERRABLE_REASONS:
        return False
    if trace is None or not trace.primitive_states:
        return False
    if trace.status in {"provider_error", "disabled_no_provider"}:
        return False
    return True


def _with_agentic_stage_court_diagnostics(
    *,
    diagnostics: Mapping[str, object],
    stage_output: StageCourtOutput,
) -> Mapping[str, object]:
    updated = dict(diagnostics)
    updated.update(
        {
            "agentic_stage_court_runtime_stage": stage_output.decision.canonical_stage(),
            "agentic_stage_court_runtime_base_stage": stage_output.decision.base_stage.value,
            "agentic_stage_court_runtime_investigation_status": stage_output.decision.investigation_status.value,
            "agentic_stage_court_runtime_transition_overlay": stage_output.decision.transition_overlay.value,
            "agentic_stage_court_runtime_score_status": stage_output.score_status.value,
            "agentic_stage_court_verified_score": round(float(stage_output.score_interval.verified_score), 4),
            "agentic_stage_court_potential_score_upper_bound": round(
                float(stage_output.score_interval.potential_score_upper_bound),
                4,
            ),
            "agentic_stage_court_unresolved_material_gap_points": round(
                float(stage_output.unresolved_material_gap_points),
                4,
            ),
            "agentic_stage_court_score_interval_width": round(
                max(
                    0.0,
                    float(stage_output.score_interval.potential_score_upper_bound)
                    - float(stage_output.score_interval.verified_score),
                ),
                4,
            ),
            "agentic_stage_court_material_stage_boundaries_crossed": tuple(
                round(float(boundary), 4)
                for boundary in stage_output.material_stage_boundaries_crossed
            ),
            "agentic_stage_court_material_stage_boundary_crossed_count": len(
                stage_output.material_stage_boundaries_crossed
            ),
            "agentic_stage_court_base_stage_preview": stage_output.decision.base_stage.value,
            "agentic_stage_court_investigation_status_preview": stage_output.decision.investigation_status.value,
            "agentic_stage_court_transition_overlay_preview": stage_output.decision.transition_overlay.value,
            "agentic_stage_court_canonical_stage_preview": stage_output.decision.canonical_stage(),
            "agentic_stage_court_score_status_preview": stage_output.score_status.value,
            "agentic_stage_court_present_green_primitives": stage_output.present_green_primitives,
            "agentic_stage_court_missing_green_primitives": stage_output.missing_green_primitives,
            "agentic_stage_court_reasons": stage_output.reasons,
        }
    )
    return updated


def _stage_snapshot_from_agentic_stage_court(
    *,
    stage_output: StageCourtOutput,
    legacy_stage: StageSnapshot,
    score: ScoreSnapshot,
    inputs: FreeWebResearchInput,
) -> StageSnapshot:
    stage = Stage(stage_output.decision.canonical_stage())
    return StageSnapshot(
        symbol=score.symbol,
        as_of_date=score.as_of_date,
        stage=stage,
        previous_stage=inputs.previous_stage,
        stage_changed=inputs.previous_stage is not None and inputs.previous_stage != stage,
        grade=_agentic_stage_grade(stage_output),
        stage_reason=tuple(
            dict.fromkeys(
                (
                    "agentic_stage_court_runtime_output",
                    *stage_output.reasons,
                    f"base_stage:{stage_output.decision.base_stage.value}",
                    f"investigation_status:{stage_output.decision.investigation_status.value}",
                    f"score_status:{stage_output.score_status.value}",
                    f"legacy_stage:{legacy_stage.stage.value}",
                )
            )
        ),
        red_team_status=legacy_stage.red_team_status,
        evidence_ids=legacy_stage.evidence_ids,
        classifier_version=f"e2r-agentic-stage-court-v2:{legacy_stage.classifier_version}",
    )


def _agentic_stage_grade(stage_output: StageCourtOutput) -> str:
    parts = [
        stage_output.decision.base_stage.value,
        stage_output.decision.investigation_status.value.lower(),
        stage_output.score_status.value.lower(),
    ]
    if stage_output.decision.transition_overlay.value != "NONE":
        parts.append(stage_output.decision.transition_overlay.value)
    return "agentic-" + "-".join(parts)


def _score_gap_score_block_reason(
    *,
    inputs: FreeWebResearchInput,
    expansion: _ScoreGapExpansionResult,
    queries_run_count: int = 0,
) -> str | None:
    if not inputs.require_resolved_score_gaps_for_scoring:
        return None
    if not _material_score_gaps(expansion.unresolved_gaps):
        return None
    status = _normalized_score_gap_expansion_status(expansion.status)
    if status == "no_gaps" or status == "executed":
        return None
    if status == "provider_error":
        return "score_gap_provider_error"
    if status == "invalid_provider_output":
        return "score_gap_invalid_provider_output"
    if status == "disabled_no_provider":
        return "score_gap_disabled_no_provider"
    if status == "llm_no_suggested_queries":
        return "score_gap_llm_no_suggested_queries"
    if status == "no_executable_searches":
        return "score_gap_no_executable_searches"
    if status == "budget_blocked":
        return "score_gap_budget_blocked"
    if status == "round_limit_reached":
        return "score_gap_round_limit"
    if status == "no_progress":
        if _score_gap_expansion_has_evidence_progress(expansion):
            return "score_gap_material_gaps_pending"
        return "score_gap_no_progress"
    if status in {"captcha_or_block_detected", "daily_query_budget_exhausted", "symbol_query_budget_exhausted", "deep_research_symbol_budget_exhausted", "active_monitoring_symbol_budget_exhausted"}:
        return "score_gap_search_blocked"
    if status in _SCORE_GAP_FAILURE_STATUSES:
        return "score_gap_unresolved"
    return None


def _score_gap_expansion_has_evidence_progress(expansion: _ScoreGapExpansionResult) -> bool:
    details = expansion.diagnostic_details
    if details.get("post_score_gap_score_state_changed"):
        return False
    if details.get("post_score_gap_primitive_state_changed"):
        return True
    if details.get("post_score_gap_score_contribution_changed"):
        return True
    reason = str(details.get("post_score_gap_progress_reason") or "").strip()
    return reason == "score_gap_evidence_progress_without_score_state_change"


def _score_gap_warning_reason(
    *,
    inputs: FreeWebResearchInput,
    expansion: _ScoreGapExpansionResult,
    queries_run_count: int,
) -> str | None:
    if not inputs.require_resolved_score_gaps_for_scoring:
        return None
    if not _material_score_gaps(expansion.unresolved_gaps):
        return None
    status = _normalized_score_gap_expansion_status(expansion.status)
    if status == "provider_error":
        return "score_gap_provider_error"
    if status == "invalid_provider_output":
        return "score_gap_invalid_provider_output"
    if status == "llm_no_suggested_queries":
        return "score_gap_llm_no_suggested_queries"
    if status == "no_executable_searches":
        return "score_gap_no_executable_searches"
    if queries_run_count <= 0:
        return None
    if status == "round_limit_reached":
        return "score_gap_round_limit"
    return None


def _normalized_score_gap_expansion_status(status: str) -> str:
    agentic_status_map = {
        "agentic_follow_up_provider_error": "provider_error",
        "agentic_follow_up_no_suggested_queries": "llm_no_suggested_queries",
        "agentic_follow_up_no_executable_searches": "no_executable_searches",
        "agentic_follow_up_executed": "executed",
    }
    return agentic_status_map.get(status, status)


def _material_score_gaps(gaps: Sequence[str]) -> tuple[str, ...]:
    material: list[str] = []
    for gap in gaps:
        text = str(gap)
        lowered = text.lower()
        if "agentic primitive gap:" in lowered:
            materiality = _agentic_gap_materiality_value(text)
            if materiality is not None:
                if materiality > 0.0:
                    material.append(text)
                continue
        if any(marker.lower() in lowered for marker in _MATERIAL_SCORE_GAP_MARKERS):
            material.append(text)
    return tuple(dict.fromkeys(material))


def _agentic_gap_materiality_value(gap: str) -> float | None:
    match = re.search(r"\bmateriality\s*[:=]\s*(-?\d+(?:\.\d+)?)", str(gap), re.IGNORECASE)
    if not match:
        return None
    try:
        return float(match.group(1))
    except ValueError:
        return None


def _mark_score_valid_for_theme_route(
    *,
    inputs: FreeWebResearchInput,
    score: ScoreSnapshot,
    diagnostics: Mapping[str, object],
) -> tuple[ScoreSnapshot, Mapping[str, object]]:
    if not inputs.require_valid_theme_route_for_scoring:
        return score, diagnostics
    numeric = dict(score.diagnostic_scores)
    numeric.setdefault("score_valid", 100.0)
    numeric.setdefault("score_blocked_by_theme_route", 0.0)
    numeric.setdefault("theme_route_required_for_scoring", 100.0)
    updated = dict(diagnostics)
    updated.setdefault("score_valid", True)
    updated.setdefault("score_blocked_by_theme_route", False)
    return replace(score, diagnostic_scores=numeric), updated


def _agentic_evidence_score_block_reason(
    *,
    inputs: FreeWebResearchInput,
    score: ScoreSnapshot,
    trace: AgenticEvidenceRuntimeTrace,
) -> str | None:
    if not inputs.agentic_evidence_enabled:
        return None
    if trace.status in _AGENTIC_EVIDENCE_SCORE_BLOCK_STATUSES:
        return _AGENTIC_EVIDENCE_SCORE_BLOCK_STATUSES[trace.status]
    if trace.status in {"completed", "partial_error"} and trace.accepted_mapping_count <= 0:
        return "agentic_evidence_no_accepted_mappings"
    if diagnostic_value(score.diagnostic_scores.get("agentic_score_contribution_v2_runtime_input")) > 0.0:
        return None
    if trace.status == "disabled":
        return None
    return "agentic_evidence_missing_v2_score_contributions"


def _invalidate_score_for_agentic_evidence(
    *,
    score: ScoreSnapshot,
    diagnostics: Mapping[str, object],
    reason: str,
) -> tuple[ScoreSnapshot, Mapping[str, object]]:
    raw_components = {
        "raw_eps_fcf_before_agentic_evidence_block": score.eps_fcf_explosion_score,
        "raw_earnings_visibility_before_agentic_evidence_block": score.earnings_visibility_score,
        "raw_bottleneck_pricing_before_agentic_evidence_block": score.bottleneck_pricing_score,
        "raw_market_mispricing_before_agentic_evidence_block": score.market_mispricing_score,
        "raw_valuation_rerating_before_agentic_evidence_block": score.valuation_rerating_score,
        "raw_capital_allocation_before_agentic_evidence_block": score.capital_allocation_score,
        "raw_information_confidence_before_agentic_evidence_block": score.information_confidence_score,
        "raw_score_total_before_agentic_evidence_block": score.total_score,
        "raw_risk_penalty_before_agentic_evidence_block": min(100.0, score.risk_penalty),
    }
    numeric = dict(score.diagnostic_scores)
    numeric.update(raw_components)
    numeric["score_valid"] = 0.0
    numeric["score_blocked_by_agentic_evidence"] = 100.0
    numeric["agentic_evidence_required_for_scoring"] = 100.0
    numeric["agentic_evidence_block_reason_code"] = _AGENTIC_EVIDENCE_BLOCK_REASON_CODES.get(reason, 99.0)
    updated = dict(diagnostics)
    updated["score_valid"] = False
    updated["score_blocked_by_agentic_evidence"] = True
    updated["score_blocked_reason"] = reason
    updated["raw_score_total_before_agentic_evidence_block"] = score.total_score
    return (
        replace(
            score,
            eps_fcf_explosion_score=0.0,
            earnings_visibility_score=0.0,
            bottleneck_pricing_score=0.0,
            market_mispricing_score=0.0,
            valuation_rerating_score=0.0,
            capital_allocation_score=0.0,
            information_confidence_score=0.0,
            risk_penalty=0.0,
            total_score=0.0,
            diagnostic_scores=numeric,
            scoring_version=f"{score.scoring_version}:agentic-evidence-block",
        ),
        updated,
    )


def _blocked_stage_for_agentic_evidence(
    *,
    inputs: FreeWebResearchInput,
    score: ScoreSnapshot,
    red_team: RedTeamAssessment,
    web_result: WebResearchResult,
    reason: str,
) -> StageSnapshot:
    evidence_ids = tuple(
        dict.fromkeys(
            score.evidence_ids
            + red_team.evidence_ids
            + tuple(item.evidence_id for item in web_result.evidence)
        )
    )
    return StageSnapshot(
        symbol=score.symbol,
        as_of_date=score.as_of_date,
        stage=Stage.STAGE_0,
        previous_stage=inputs.previous_stage,
        stage_changed=inputs.previous_stage is not None and inputs.previous_stage != Stage.STAGE_0,
        grade="Watch",
        stage_reason=(f"agentic evidence ledger incomplete; scoring blocked before stage classification: {reason}",),
        red_team_status=red_team.risk_level.value,
        evidence_ids=evidence_ids,
        classifier_version=f"{StageClassifier.version}:agentic-evidence-block",
    )


def _mark_score_gap_warning_if_any(
    *,
    inputs: FreeWebResearchInput,
    score: ScoreSnapshot,
    diagnostics: Mapping[str, object],
    expansion: _ScoreGapExpansionResult,
    queries_run_count: int,
) -> tuple[ScoreSnapshot, Mapping[str, object]]:
    reason = _score_gap_warning_reason(
        inputs=inputs,
        expansion=expansion,
        queries_run_count=queries_run_count,
    )
    if reason is None:
        return score, diagnostics
    numeric = dict(score.diagnostic_scores)
    numeric.setdefault("score_gap_required_for_scoring", 100.0)
    numeric["score_blocked_by_score_gap"] = 0.0
    numeric["score_gap_unresolved_warning"] = 100.0
    numeric["score_gap_warning_reason_code"] = _SCORE_GAP_BLOCK_REASON_CODES.get(reason, 99.0)
    existing_queries = diagnostics.get("post_score_gap_expansion_queries", ())
    if isinstance(existing_queries, str):
        existing_query_tuple: tuple[str, ...] = (existing_queries,)
    else:
        existing_query_tuple = tuple(str(item) for item in existing_queries) if isinstance(existing_queries, Sequence) else ()
    updated = dict(_with_score_gap_expansion_diagnostics(diagnostics, expansion, existing_query_tuple))
    updated["score_gap_unresolved_warning"] = True
    updated["post_score_gap_warning_reason"] = reason
    updated["material_score_gap_unresolved_gaps"] = _material_score_gaps(expansion.unresolved_gaps)
    return replace(score, diagnostic_scores=numeric), updated


def _invalidate_score_for_theme_route(
    *,
    score: ScoreSnapshot,
    diagnostics: Mapping[str, object],
    reason: str,
) -> tuple[ScoreSnapshot, Mapping[str, object]]:
    raw_components = {
        "raw_eps_fcf_before_theme_route_block": score.eps_fcf_explosion_score,
        "raw_earnings_visibility_before_theme_route_block": score.earnings_visibility_score,
        "raw_bottleneck_pricing_before_theme_route_block": score.bottleneck_pricing_score,
        "raw_market_mispricing_before_theme_route_block": score.market_mispricing_score,
        "raw_valuation_rerating_before_theme_route_block": score.valuation_rerating_score,
        "raw_capital_allocation_before_theme_route_block": score.capital_allocation_score,
        "raw_information_confidence_before_theme_route_block": score.information_confidence_score,
        "raw_score_total_before_theme_route_block": score.total_score,
        "raw_risk_penalty_before_theme_route_block": min(100.0, score.risk_penalty),
    }
    numeric = dict(score.diagnostic_scores)
    numeric.update(raw_components)
    numeric["score_valid"] = 0.0
    numeric["score_blocked_by_theme_route"] = 100.0
    numeric["theme_route_required_for_scoring"] = 100.0
    numeric["theme_route_block_reason_code"] = _THEME_ROUTE_SCORE_BLOCK_REASON_CODES.get(reason, 100.0)
    updated = dict(diagnostics)
    updated["score_valid"] = False
    updated["score_blocked_by_theme_route"] = True
    updated["score_blocked_reason"] = reason
    updated["raw_score_total_before_theme_route_block"] = score.total_score
    return (
        replace(
            score,
            eps_fcf_explosion_score=0.0,
            earnings_visibility_score=0.0,
            bottleneck_pricing_score=0.0,
            market_mispricing_score=0.0,
            valuation_rerating_score=0.0,
            capital_allocation_score=0.0,
            information_confidence_score=0.0,
            risk_penalty=0.0,
            total_score=0.0,
            diagnostic_scores=numeric,
            scoring_version=f"{score.scoring_version}:theme-route-block",
        ),
        updated,
    )


def _invalidate_score_for_score_gap(
    *,
    score: ScoreSnapshot,
    diagnostics: Mapping[str, object],
    reason: str,
    expansion: _ScoreGapExpansionResult,
) -> tuple[ScoreSnapshot, Mapping[str, object]]:
    raw_components = {
        "raw_eps_fcf_before_score_gap_block": score.eps_fcf_explosion_score,
        "raw_earnings_visibility_before_score_gap_block": score.earnings_visibility_score,
        "raw_bottleneck_pricing_before_score_gap_block": score.bottleneck_pricing_score,
        "raw_market_mispricing_before_score_gap_block": score.market_mispricing_score,
        "raw_valuation_rerating_before_score_gap_block": score.valuation_rerating_score,
        "raw_capital_allocation_before_score_gap_block": score.capital_allocation_score,
        "raw_information_confidence_before_score_gap_block": score.information_confidence_score,
        "raw_score_total_before_score_gap_block": score.total_score,
        "raw_risk_penalty_before_score_gap_block": min(100.0, score.risk_penalty),
    }
    numeric = dict(score.diagnostic_scores)
    numeric.update(raw_components)
    numeric["score_valid"] = 0.0
    numeric["score_blocked_by_score_gap"] = 100.0
    numeric["score_gap_required_for_scoring"] = 100.0
    numeric["score_gap_block_reason_code"] = _SCORE_GAP_BLOCK_REASON_CODES.get(reason, 99.0)
    existing_queries = diagnostics.get("post_score_gap_expansion_queries", ())
    if isinstance(existing_queries, str):
        existing_query_tuple: tuple[str, ...] = (existing_queries,)
    else:
        existing_query_tuple = tuple(str(item) for item in existing_queries) if isinstance(existing_queries, Sequence) else ()
    updated = _with_score_gap_expansion_diagnostics(diagnostics, expansion, existing_query_tuple)
    updated = dict(updated)
    updated["score_valid"] = False
    updated["score_blocked_by_score_gap"] = True
    updated["score_blocked_reason"] = reason
    updated["raw_score_total_before_score_gap_block"] = score.total_score
    updated["material_score_gap_unresolved_gaps"] = _material_score_gaps(expansion.unresolved_gaps)
    return (
        replace(
            score,
            eps_fcf_explosion_score=0.0,
            earnings_visibility_score=0.0,
            bottleneck_pricing_score=0.0,
            market_mispricing_score=0.0,
            valuation_rerating_score=0.0,
            capital_allocation_score=0.0,
            information_confidence_score=0.0,
            risk_penalty=0.0,
            total_score=0.0,
            diagnostic_scores=numeric,
            scoring_version=f"{score.scoring_version}:score-gap-block",
        ),
        updated,
    )


def _clear_unconfirmed_theme_route_classification(feature_result: FeatureEngineeringResult) -> FeatureEngineeringResult:
    payload = replace(
        feature_result.payload,
        large_sector_id=None,
        canonical_archetype_id=None,
    )
    return replace(feature_result, payload=payload)


def _blocked_stage_for_theme_route(
    *,
    inputs: FreeWebResearchInput,
    score: ScoreSnapshot,
    red_team: RedTeamAssessment,
    web_result: WebResearchResult,
    reason: str,
) -> StageSnapshot:
    evidence_ids = tuple(
        dict.fromkeys(
            score.evidence_ids
            + red_team.evidence_ids
            + tuple(item.evidence_id for item in web_result.evidence)
        )
    )
    return StageSnapshot(
        symbol=score.symbol,
        as_of_date=score.as_of_date,
        stage=Stage.STAGE_0,
        previous_stage=inputs.previous_stage,
        stage_changed=inputs.previous_stage is not None and inputs.previous_stage != Stage.STAGE_0,
        grade="Watch",
        stage_reason=(f"theme route unresolved; scoring blocked before stage classification: {reason}",),
        red_team_status=red_team.risk_level.value,
        evidence_ids=evidence_ids,
        classifier_version=f"{StageClassifier.version}:theme-route-block",
    )


def _blocked_stage_for_score_gap(
    *,
    inputs: FreeWebResearchInput,
    score: ScoreSnapshot,
    red_team: RedTeamAssessment,
    web_result: WebResearchResult,
    reason: str,
) -> StageSnapshot:
    evidence_ids = tuple(
        dict.fromkeys(
            score.evidence_ids
            + red_team.evidence_ids
            + tuple(item.evidence_id for item in web_result.evidence)
        )
    )
    return StageSnapshot(
        symbol=score.symbol,
        as_of_date=score.as_of_date,
        stage=Stage.STAGE_0,
        previous_stage=inputs.previous_stage,
        stage_changed=inputs.previous_stage is not None and inputs.previous_stage != Stage.STAGE_0,
        grade="Watch",
        stage_reason=(f"score-gap expansion unresolved; scoring blocked before stage classification: {reason}",),
        red_team_status=red_team.risk_level.value,
        evidence_ids=evidence_ids,
        classifier_version=f"{StageClassifier.version}:score-gap-block",
    )


def _with_theme_route_diagnostics(
    feature_result: FeatureEngineeringResult,
    route: ThemeRouteOutput | None,
    diagnostics: Mapping[str, object],
) -> FeatureEngineeringResult:
    if route is None:
        return feature_result
    numeric = route_diagnostics(route)
    status = str(diagnostics.get("theme_rebalance_status") or route.status)
    numeric["theme_rebalance_enabled"] = 100.0
    numeric["llm_deep_research_completed"] = 100.0 if status == "completed" else 0.0
    numeric["theme_route_status_code"] = _THEME_STATUS_CODES.get(status, _THEME_STATUS_CODES.get(route.status, 0.0))
    numeric["theme_route_applied_to_scoring"] = 100.0 if _theme_route_scoring_ids(route)[1] else 0.0
    merged = dict(feature_result.payload.diagnostic_scores)
    merged.update(numeric)
    payload = replace(feature_result.payload, diagnostic_scores=merged)
    return replace(feature_result, payload=payload)


def _full_news_items(web_result: WebResearchResult) -> tuple:
    return tuple(item for item in web_result.parsed_news if not item.parsed_fields.get("search_snippet_only"))


def _theme_regime_score(web_result: WebResearchResult, feature_input: FeatureEngineeringInput) -> float:
    if web_result.parsed_news or web_result.parsed_reports:
        return 80.0
    if feature_input.agent_extracted_fields.get("emerging_theme_active") or feature_input.agent_extracted_fields.get("theme_transition_detected"):
        return 80.0
    return 0.0


def _company_event_score(web_result: WebResearchResult, feature_input: FeatureEngineeringInput) -> float:
    if web_result.parsed_disclosures or web_result.parsed_reports or _full_news_items(web_result):
        return 80.0
    if feature_input.disclosures or feature_input.research_reports or feature_input.financial_actuals:
        return 80.0
    return 0.0


def _high_quality_company_event(web_result: WebResearchResult, feature_input: FeatureEngineeringInput) -> bool:
    return bool(
        web_result.parsed_disclosures
        or web_result.parsed_reports
        or feature_input.disclosures
        or feature_input.research_reports
        or feature_input.financial_actuals
    )


def _layer_for_query(query_spec: QuerySpec, stage_context: str | None) -> ResearchLayer:
    if query_spec.group == "event_search":
        return ResearchLayer.EVENT_SEARCH
    if query_spec.group == "deep_research":
        return ResearchLayer.DEEP_RESEARCH
    if query_spec.group == "discovery":
        return ResearchLayer.EVENT_SEARCH
    if query_spec.group == "monitoring" and stage_context:
        return ResearchLayer.ACTIVE_MONITORING
    if query_spec.group in {"confirmation", "monitoring"}:
        return ResearchLayer.DEEP_RESEARCH
    return ResearchLayer.EVENT_SEARCH


def _provider_blocked(provider: object) -> bool:
    return bool(getattr(provider, "blocked", False))


def _provider_errors(provider: object) -> list[str]:
    errors = getattr(provider, "errors", None)
    return list(errors) if errors else []


__all__ = [
    "FreeWebResearchInput",
    "FreeWebResearchRunner",
    "SkippedQuery",
    "WebResearchPipelineResult",
]
