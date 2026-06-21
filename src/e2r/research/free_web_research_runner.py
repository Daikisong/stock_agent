"""Free search-first E2R web research runner."""

from __future__ import annotations

import re
from dataclasses import dataclass, field, replace
from datetime import date
from pathlib import Path
from time import sleep
from typing import Any, Callable, Mapping, Protocol, Sequence

from e2r.agentic import claim_metadata_from_claims, compile_claims_from_primitives, evidence_contract_gap_context
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
from e2r.research.report_consensus_proxy import build_report_consensus_proxy
from e2r.research.search_budget import ResearchLayer, SearchBudget, SearchBudgetTracker
from e2r.research.search_provider import FixtureSearchProvider, SearchProvider, SearchResult
from e2r.research.search_result_ranker import RankedSearchResult, SearchResultRanker
from e2r.research.web_research_runner import WebResearchInput, WebResearchResult, WebResearchRunner
from e2r.stage_gate_diagnostics import diagnose_stage_gates
from e2r.staging import StageClassificationInput, StageClassifier


_SCORE_GAP_QUERY_RETRY_MAX: int | None = None
_LLM_QUERY_RETRY_MAX: int | None = None


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
    top_results: int | None = None
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
    post_parse_gap_expansion_enabled: bool = True
    post_parse_gap_expansion_max_queries: int | None = 10
    post_gap_fetch_results_per_query: int = 5
    post_gap_fetch_min_results: int = 20
    llm_query_retry_max: int | None = _LLM_QUERY_RETRY_MAX
    score_gap_query_retry_max: int | None = _SCORE_GAP_QUERY_RETRY_MAX
    require_valid_theme_route_for_scoring: bool | None = None
    require_resolved_score_gaps_for_scoring: bool | None = None
    base_feature_input: FeatureEngineeringInput | None = None
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
        if self.theme_route_search_result_limit is not None and self.theme_route_search_result_limit < 0:
            raise ValueError("theme_route_search_result_limit must be non-negative")
        if self.theme_route_document_limit is not None and self.theme_route_document_limit < 0:
            raise ValueError("theme_route_document_limit must be non-negative")
        if self.theme_route_document_excerpt_chars <= 0:
            raise ValueError("theme_route_document_excerpt_chars must be positive")
        if self.theme_expansion_reserve_queries < 0:
            raise ValueError("theme_expansion_reserve_queries must be non-negative")
        if self.post_parse_gap_expansion_max_queries is not None and self.post_parse_gap_expansion_max_queries < 0:
            raise ValueError("post_parse_gap_expansion_max_queries must be non-negative")
        if self.post_gap_fetch_results_per_query <= 0:
            raise ValueError("post_gap_fetch_results_per_query must be positive")
        if self.post_gap_fetch_min_results < 0:
            raise ValueError("post_gap_fetch_min_results must be non-negative")
        if self.llm_query_retry_max is not None and self.llm_query_retry_max < 0:
            raise ValueError("llm_query_retry_max must be non-negative")
        if self.score_gap_query_retry_max is not None and self.score_gap_query_retry_max < 0:
            raise ValueError("score_gap_query_retry_max must be non-negative")


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


@dataclass(frozen=True)
class _ScoreGapExpansionResult:
    specs: tuple[QuerySpec, ...] = ()
    queries_run: tuple[str, ...] = ()
    status: str = "not_attempted"
    unresolved_gaps: tuple[str, ...] = ()
    rejection_reasons: tuple[str, ...] = ()
    blocked_reason: str | None = None


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
        score = feature_result.score()
        red_team = RedTeamEngine().assess(feature_result.red_team_signals)
        score_gap_queries: tuple[str, ...] = ()
        score_gap_expansion_result = _ScoreGapExpansionResult(status="not_attempted")
        score_gap_round_index = 0
        seen_score_gap_signatures: set[tuple[str, ...]] = set()
        theme_route_diagnostics = dict(theme_route_diagnostics)
        theme_route_diagnostics["post_score_gap_expansion_count"] = 0
        theme_route_diagnostics["post_score_gap_expansion_queries"] = ()
        theme_route_diagnostics["post_score_gap_expansion_status"] = "not_attempted"
        theme_route_diagnostics["post_score_gap_unresolved_gaps"] = ()
        theme_route_diagnostics["post_score_gap_rejection_reasons"] = ()
        while True:
            gap_signature = _score_gap_state_signature(score, red_team, feature_result.source_fields)
            if gap_signature in seen_score_gap_signatures:
                score_gap_expansion_result = _ScoreGapExpansionResult(
                    status="no_progress",
                    unresolved_gaps=tuple(dict.fromkeys((*_score_gap_missing_information(score), *_stage_gate_missing_information(score, red_team)))),
                    rejection_reasons=("score_gap_state_repeated",),
                )
                theme_route_diagnostics = _with_score_gap_expansion_diagnostics(
                    theme_route_diagnostics,
                    score_gap_expansion_result,
                    score_gap_queries,
                )
                _emit_phase_event(
                    inputs,
                    "post_score_gap_stop_no_progress",
                    round_index=score_gap_round_index,
                    score_gap_query_count=len(score_gap_queries),
                    unresolved_gap_count=len(score_gap_expansion_result.unresolved_gaps),
                )
                break
            if (
                inputs.max_score_gap_expansion_rounds is not None
                and score_gap_round_index >= inputs.max_score_gap_expansion_rounds
            ):
                score_gap_expansion_result = _ScoreGapExpansionResult(
                    status="round_limit_reached",
                    unresolved_gaps=tuple(dict.fromkeys((*_score_gap_missing_information(score), *_stage_gate_missing_information(score, red_team)))),
                    rejection_reasons=("max_score_gap_expansion_rounds_reached",),
                )
                theme_route_diagnostics = _with_score_gap_expansion_diagnostics(
                    theme_route_diagnostics,
                    score_gap_expansion_result,
                    score_gap_queries,
                )
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
            )
            theme_route_diagnostics = _with_score_gap_expansion_diagnostics(
                theme_route_diagnostics,
                score_gap_expansion_result,
                score_gap_queries,
            )
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
            score = feature_result.score()
            red_team = RedTeamEngine().assess(feature_result.red_team_signals)
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

        agent = LLMThemeRebalanceAgent(inputs.theme_route_provider)
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
        return route, _theme_route_run_diagnostics(route, tuple(expansion_queries_run), status), tuple(expansion_specs), tuple(expansion_queries_run)

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

        agent = LLMThemeRebalanceAgent(inputs.theme_route_provider)
        route_search_results = self._theme_route_search_results_from_web_result(inputs, web_result)
        _emit_phase_event(
            inputs,
            "theme_evidence_review_start",
            raw_ranked_result_count=len(web_result.ranked_results),
            llm_search_result_count=len(route_search_results),
            raw_document_count=len(web_result.fetched_documents),
            llm_document_count=len(documents),
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
        if review.status in {"provider_error", "invalid_provider_output", "disabled_no_provider"} and existing_route is not None:
            diagnostics["theme_evidence_review_status"] = review.status
            diagnostics["theme_evidence_review_blocked_reason"] = review.blocked_reason
            diagnostics["theme_evidence_document_count"] = len(documents)
            return existing_route, diagnostics

        merged = _merge_theme_routes(existing_route, review)
        diagnostics = dict(_theme_route_run_diagnostics(merged, expansion_queries_run, str(existing_diagnostics.get("theme_rebalance_status") or "completed")))
        diagnostics["theme_evidence_review_status"] = "completed"
        diagnostics["theme_evidence_document_count"] = len(documents)
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
    ) -> _ScoreGapExpansionResult:
        if not _post_score_gap_expansion_allowed(inputs, score):
            return _ScoreGapExpansionResult(status="disabled")
        score_gaps = tuple(dict.fromkeys((*_score_gap_missing_information(score), *_stage_gate_missing_information(score, red_team))))
        if not score_gaps:
            return _ScoreGapExpansionResult(status="no_gaps")
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
    agent = LLMThemeRebalanceAgent(inputs.theme_route_provider)
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
    agent = LLMThemeRebalanceAgent(inputs.theme_route_provider)
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
    if "llm_returned_no_suggested_queries" in set(previous_rejections):
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
    if (
        _diagnostic_value(diagnostics, "evidence_family_consensus") <= 0.0
        and _diagnostic_value(diagnostics, "evidence_family_consensus_proxy") <= 0.0
    ):
        gaps.append("consensus FY1 FY2 estimates PER PBR target price analyst count")
    if (
        _diagnostic_value(diagnostics, "evidence_family_consensus_revision") <= 0.0
        and _diagnostic_value(diagnostics, "evidence_family_consensus_revision_proxy") <= 0.0
    ):
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
    available = {item.evidence_id for item in web_result.evidence}
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
    years = [int(match.group(0)) for match in re.finditer(r"\b20\d{2}\b", clean)]
    if any(year > as_of_date.year for year in years):
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
    source_backed_slots = _source_backed_theme_slot_names(route)
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
                refs.extend(slot.evidence_refs)
        if refs:
            refs_by_field[field_key] = tuple(dict.fromkeys(refs))
    return refs_by_field


def _has_source_backed_theme_slot(route: ThemeRouteOutput) -> bool:
    return any(slot.status == "present" and slot.evidence_refs for slot in route.evidence_slots)


def _source_backed_theme_slot_names(route: ThemeRouteOutput) -> tuple[str, ...]:
    return tuple(
        str(slot.slot).strip()
        for slot in route.evidence_slots
        if slot.status == "present" and slot.evidence_refs and str(slot.slot).strip()
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
    updated["post_score_gap_rejection_reasons"] = tuple(expansion.rejection_reasons)
    if expansion.blocked_reason:
        updated["post_score_gap_blocked_reason"] = expansion.blocked_reason
    return updated


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
    status = expansion.status
    if status == "no_gaps" or status == "executed":
        return None
    if status == "provider_error":
        if _score_gap_warning_reason(inputs=inputs, expansion=expansion, queries_run_count=queries_run_count):
            return None
        return "score_gap_provider_error"
    if status == "invalid_provider_output":
        if _score_gap_warning_reason(inputs=inputs, expansion=expansion, queries_run_count=queries_run_count):
            return None
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
        if _score_gap_warning_reason(inputs=inputs, expansion=expansion, queries_run_count=queries_run_count):
            return None
        return "score_gap_round_limit"
    if status == "no_progress":
        return "score_gap_no_progress"
    if status in {"captcha_or_block_detected", "daily_query_budget_exhausted", "symbol_query_budget_exhausted", "deep_research_symbol_budget_exhausted", "active_monitoring_symbol_budget_exhausted"}:
        return "score_gap_search_blocked"
    if status in _SCORE_GAP_FAILURE_STATUSES:
        return "score_gap_unresolved"
    return None


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
    if expansion.status == "provider_error":
        return "score_gap_provider_error"
    if expansion.status == "invalid_provider_output":
        return "score_gap_invalid_provider_output"
    if queries_run_count <= 0:
        return None
    if expansion.status == "round_limit_reached":
        return "score_gap_round_limit"
    return None


def _material_score_gaps(gaps: Sequence[str]) -> tuple[str, ...]:
    material: list[str] = []
    for gap in gaps:
        text = str(gap)
        lowered = text.lower()
        if any(marker.lower() in lowered for marker in _MATERIAL_SCORE_GAP_MARKERS):
            material.append(text)
    return tuple(dict.fromkeys(material))


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
