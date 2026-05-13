"""Free search-first E2R web research runner."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from time import sleep
from typing import Mapping, Protocol, Sequence

from e2r.features import DeterministicFeatureEngineer, FeatureEngineeringInput, FeatureEngineeringResult
from e2r.models import Market, RedTeamFinding, ScoreSnapshot, Stage, StageSnapshot
from e2r.red_team import RedTeamAssessment, RedTeamEngine
from e2r.research.browser_search_provider import BrowserSearchProvider
from e2r.research.manual_source_provider import ManualSourceProvider
from e2r.research.naver_search_provider import NaverFreeSearchProvider
from e2r.research.page_fetcher import PageFetcher
from e2r.research.pdf_text_extractor import PDFTextExtractor
from e2r.research.query_planner import QueryPlan, QueryPlanner, QuerySpec
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
    budget: SearchBudget = field(default_factory=SearchBudget)
    max_results_per_query: int = 5
    top_results: int = 8
    fixture_text_by_url: Mapping[str, str | Path] = field(default_factory=dict)
    include_manual_sources: bool = True


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

        for query_spec in query_plan.queries:
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

        text_mapping: dict[str, str | Path] = dict(inputs.fixture_text_by_url)
        if inputs.include_manual_sources and self._manual_provider is not None:
            text_mapping.update(self._manual_provider.fixture_text_by_url())

        web_runner = WebResearchRunner(
            query_planner=_FixedQueryPlanner(query_plan),
            search_provider=FixtureSearchProvider(results_by_query=results_by_query),
            ranker=self._ranker,
            page_fetcher=PageFetcher(fixture_text_by_url=text_mapping),
            pdf_text_extractor=self._pdf_text_extractor,
        )
        web_result = web_runner.run(
            WebResearchInput(
                company_name=inputs.company_name,
                symbol=inputs.symbol,
                sector=inputs.sector,
                market=inputs.market,
                as_of_date=inputs.as_of_date,
                stage_context=inputs.stage_context,
                max_results_per_query=inputs.max_results_per_query,
                top_results=inputs.top_results,
            )
        )
        feature_input = FeatureEngineeringInput(
            symbol=inputs.symbol,
            as_of_date=inputs.as_of_date,
            disclosures=web_result.parsed_disclosures,
            research_reports=web_result.parsed_reports,
            news_items=web_result.parsed_news,
        )
        feature_result = self._engineer.engineer(feature_input)
        score = feature_result.score()
        red_team = RedTeamEngine().assess(feature_result.red_team_signals)
        stage = StageClassifier().classify(
            StageClassificationInput(
                score=score,
                red_team=red_team,
                previous_stage=inputs.previous_stage,
                theme_regime_score=80.0 if web_result.parsed_news or web_result.parsed_reports else 0.0,
                company_event_score=80.0 if web_result.parsed_disclosures or web_result.parsed_reports or web_result.parsed_news else 0.0,
                high_quality_company_event=bool(web_result.parsed_disclosures or web_result.parsed_reports),
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


class _FixedQueryPlanner:
    """Adapter so WebResearchRunner uses the already budgeted query plan."""

    def __init__(self, query_plan: QueryPlan) -> None:
        self._query_plan = query_plan

    def plan(self, **kwargs) -> QueryPlan:
        return self._query_plan


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
