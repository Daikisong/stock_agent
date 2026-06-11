"""Free search-first E2R web research runner."""

from __future__ import annotations

import re
from dataclasses import dataclass, field, replace
from datetime import date
from pathlib import Path
from time import sleep
from typing import Any, Mapping, Protocol, Sequence

from e2r.features import DeterministicFeatureEngineer, FeatureEngineeringInput, FeatureEngineeringResult
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
from e2r.research.search_result_ranker import SearchResultRanker
from e2r.research.web_research_runner import WebResearchInput, WebResearchResult, WebResearchRunner
from e2r.staging import StageClassificationInput, StageClassifier


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
    max_results_per_query: int = 5
    top_results: int = 8
    fixture_text_by_url: Mapping[str, str | Path] = field(default_factory=dict)
    include_manual_sources: bool = True
    live_page_fetch_enabled: bool = False
    page_fetch_timeout_seconds: float = 10.0
    page_fetch_cache_directory: str | Path | None = None
    theme_rebalance_enabled: bool | None = None
    theme_route_provider: ThemeRouteProvider | None = None
    max_theme_expansion_rounds: int = 3
    theme_expansion_reserve_queries: int = 10
    theme_evidence_review_enabled: bool = False
    post_parse_gap_expansion_enabled: bool = True
    post_parse_gap_expansion_max_queries: int = 12
    base_feature_input: FeatureEngineeringInput | None = None

    def __post_init__(self) -> None:
        if self.theme_rebalance_enabled is None:
            object.__setattr__(self, "theme_rebalance_enabled", self.theme_route_provider is not None)
        if self.max_theme_expansion_rounds < 0:
            raise ValueError("max_theme_expansion_rounds must be non-negative")
        if self.theme_expansion_reserve_queries < 0:
            raise ValueError("theme_expansion_reserve_queries must be non-negative")
        if self.post_parse_gap_expansion_max_queries < 0:
            raise ValueError("post_parse_gap_expansion_max_queries must be non-negative")


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

        web_result = self._run_web_research(
            inputs=inputs,
            query_plan=final_query_plan,
            results_by_query=results_by_query,
            text_mapping=text_mapping,
        )
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
            web_result = self._run_web_research(
                inputs=inputs,
                query_plan=final_query_plan,
                results_by_query=results_by_query,
                text_mapping=text_mapping,
                top_results_override=_post_gap_top_results(inputs, gap_specs),
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
        theme_route, theme_route_diagnostics = _gate_theme_route_to_web_evidence(
            route=theme_route,
            diagnostics=theme_route_diagnostics,
            web_result=web_result,
        )
        route_large_sector_id, route_canonical_archetype_id = _theme_route_scoring_ids(theme_route)
        agent_extracted_fields = _theme_route_agent_extracted_fields(theme_route)
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
                top_results=top_results_override or inputs.top_results,
            )
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
        rounds = max(1, inputs.max_theme_expansion_rounds)

        for round_index in range(rounds):
            route = agent.route(
                ThemeRouteInput(
                    company_name=inputs.company_name,
                    symbol=inputs.symbol,
                    sector=inputs.sector,
                    market=inputs.market.value,
                    as_of_date=inputs.as_of_date,
                    stage_context=inputs.stage_context,
                    candidate_reason_codes=inputs.candidate_reason_codes,
                    search_results=tuple(ThemeRouteSearchResult.from_search_result(item) for item in _flatten_results(results_by_query)),
                )
            )
            if route.status in {"provider_error", "invalid_provider_output", "disabled_no_provider"}:
                status = route.status
                break
            if inputs.max_theme_expansion_rounds <= 0:
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
            for spec in query_specs:
                safe_query = _asof_safe_theme_query(spec.query, inputs.as_of_date)
                if safe_query is None:
                    skipped.append(SkippedQuery(query=spec.query, layer=ResearchLayer.DEEP_RESEARCH, reason="future_query_rejected"))
                    continue
                safe_query = _company_scoped_query(safe_query, inputs)
                if safe_query in planned_queries:
                    continue
                planned_queries.add(safe_query)
                runnable_specs.append(replace(spec, query=safe_query))

            ran_this_round = 0
            for spec in runnable_specs:
                decision = tracker.can_run(inputs.symbol, ResearchLayer.DEEP_RESEARCH)
                if not decision.allowed:
                    skipped.append(SkippedQuery(query=spec.query, layer=ResearchLayer.DEEP_RESEARCH, reason=decision.reason or "budget_denied"))
                    status = decision.reason or "budget_denied"
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
                break

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
        documents = _theme_route_documents(web_result)
        diagnostics = dict(existing_diagnostics)
        if not documents:
            diagnostics["theme_evidence_review_status"] = "no_fetched_documents"
            return existing_route, diagnostics

        agent = LLMThemeRebalanceAgent(inputs.theme_route_provider)
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
                search_results=tuple(ThemeRouteSearchResult.from_search_result(item.result) for item in web_result.ranked_results),
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
        query_texts = _post_parse_gap_queries(
            inputs=inputs,
            route=theme_route,
        )
        if not query_texts:
            return (), ()

        seen_queries = set(results_by_query)
        specs: list[QuerySpec] = []
        queries_run: list[str] = []
        for query_index, query in enumerate(query_texts):
            safe_query = _asof_safe_theme_query(query, inputs.as_of_date)
            if safe_query is None:
                skipped.append(SkippedQuery(query=query, layer=ResearchLayer.DEEP_RESEARCH, reason="future_query_rejected"))
                continue
            safe_query = _company_scoped_query(safe_query, inputs)
            if safe_query in seen_queries:
                continue
            decision = tracker.can_run(inputs.symbol, ResearchLayer.DEEP_RESEARCH)
            if not decision.allowed:
                skipped.append(SkippedQuery(query=safe_query, layer=ResearchLayer.DEEP_RESEARCH, reason=decision.reason or "budget_denied"))
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
        return tuple(specs), tuple(queries_run)


class _FixedQueryPlanner:
    """Adapter so WebResearchRunner uses the already budgeted query plan."""

    def __init__(self, query_plan: QueryPlan) -> None:
        self._query_plan = query_plan

    def plan(self, **kwargs) -> QueryPlan:
        return self._query_plan


_POST_PARSE_GAP_ROUTE_STATUSES = {
    "transition_detected",
    "mixed_route",
    "needs_more_evidence",
    "more_evidence_needed",
}


def _post_parse_gap_expansion_allowed(inputs: FreeWebResearchInput, route: ThemeRouteOutput | None) -> bool:
    return bool(
        inputs.post_parse_gap_expansion_enabled
        and inputs.post_parse_gap_expansion_max_queries > 0
        and inputs.theme_evidence_review_enabled
        and inputs.theme_rebalance_enabled
        and inputs.theme_route_provider is not None
        and route is not None
        and route.status in _POST_PARSE_GAP_ROUTE_STATUSES
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
        if len(tuple(dict.fromkeys(normalized))) >= inputs.post_parse_gap_expansion_max_queries:
            break
    return tuple(dict.fromkeys(normalized))[: inputs.post_parse_gap_expansion_max_queries]


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


def _post_gap_top_results(inputs: FreeWebResearchInput, gap_specs: Sequence[QuerySpec]) -> int:
    return min(40, max(inputs.top_results, inputs.top_results + min(len(gap_specs), inputs.post_parse_gap_expansion_max_queries)))


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


def _theme_route_documents(web_result: WebResearchResult) -> tuple[ThemeRouteDocument, ...]:
    evidence_by_url = _evidence_by_url(web_result)
    documents: list[ThemeRouteDocument] = []
    for ranked_result, fetch in zip(web_result.selected_results, web_result.fetched_documents):
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
                text_excerpt=_theme_text_excerpt(fetch.text),
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
    for key, value in route.normalized_parsed_fields.items():
        key_text = str(key).strip()
        if not key_text or key_text in _UNSAFE_AGENT_FIELD_KEYS:
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


def _has_source_backed_theme_slot(route: ThemeRouteOutput) -> bool:
    return any(slot.status == "present" and slot.evidence_refs for slot in route.evidence_slots)


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
