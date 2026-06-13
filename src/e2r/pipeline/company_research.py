"""Single-company research pipeline for the daily scan runner."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Callable, Sequence

from e2r.backtesting import BacktestEngine, Stage3BacktestInput
from e2r.features import DeterministicFeatureEngineer, FeatureEngineeringInput, FeatureEngineeringResult
from e2r.historical_cases import HistoricalCase
from e2r.llm.codex_theme_provider import build_default_codex_theme_route_provider, build_theme_route_provider_from_env
from e2r.llm.theme_provider import ThemeRouteProvider
from e2r.models import (
    BacktestResult,
    DisclosureEvent,
    Evidence,
    FinancialActual,
    Instrument,
    Market,
    NewsItem,
    PriceBar,
    RedTeamFinding,
    ResearchReport,
    ScoreSnapshot,
    StageSnapshot,
)
from e2r.pipeline.evidence_builder import evidence_from_feature_domains
from e2r.pipeline.stage_update import StageUpdateEngine, StageUpdateInput
from e2r.red_team import RedTeamAssessment, RedTeamEngine
from e2r.research.free_web_research_runner import FreeWebResearchInput, FreeWebResearchRunner
from e2r.research.report_parser import parse_research_report_text
from e2r.research.search_budget import SearchBudget
from e2r.research.search_provider import EmptySearchProvider, SearchProvider, SearchResult
from e2r.score_validity import is_score_valid
from e2r.sources import (
    ConsensusCSVConnector,
    KINDConnector,
    KRXConnector,
    NaverNewsConnector,
    NaverWebDocConnector,
    OpenDARTConnector,
    ReportSearchConnector,
    ReportSearchResult,
    SECEdgarConnector,
)
from e2r.sources.source_errors import SourceConnectorError


@dataclass(frozen=True)
class ConnectorBundle:
    """Source connectors used by the local daily scan runner."""

    krx: KRXConnector | None = None
    opendart: OpenDARTConnector | None = None
    kind: KINDConnector | None = None
    naver_news: NaverNewsConnector | None = None
    naver_webdoc: NaverWebDocConnector | None = None
    report_search: ReportSearchConnector | None = None
    consensus: ConsensusCSVConnector | None = None
    sec_edgar: SECEdgarConnector | None = None

    @classmethod
    def local_defaults(cls) -> "ConnectorBundle":
        return cls(
            krx=KRXConnector(),
            opendart=OpenDARTConnector(),
            kind=KINDConnector(),
            naver_news=NaverNewsConnector(),
            naver_webdoc=NaverWebDocConnector(),
            report_search=ReportSearchConnector(),
            consensus=ConsensusCSVConnector(),
            sec_edgar=SECEdgarConnector(),
        )


@dataclass(frozen=True)
class CompanyResearchInput:
    instrument: Instrument
    as_of_date: date
    connectors: ConnectorBundle = field(default_factory=ConnectorBundle)
    lookback_days: int = 756
    previous_stage: Any = None
    stage3_date: date | None = None
    stage3_price: float | None = None
    backtest_price_bars: Sequence[PriceBar] = field(default_factory=tuple)
    historical_evidence: Sequence[Evidence] = field(default_factory=tuple)
    fixture_mode: bool = True
    theme_rebalance_enabled: bool | None = None
    theme_route_provider: ThemeRouteProvider | None = None
    theme_evidence_review_enabled: bool = True
    max_theme_expansion_rounds: int | None = None
    free_search_provider: SearchProvider | None = None


@dataclass(frozen=True)
class CompanyResearchResult:
    instrument: Instrument
    as_of_date: date
    feature_input: FeatureEngineeringInput
    feature_result: FeatureEngineeringResult
    score: ScoreSnapshot
    red_team: RedTeamAssessment
    stage: StageSnapshot
    evidence: tuple[Evidence, ...] = field(default_factory=tuple)
    red_team_findings: tuple[RedTeamFinding, ...] = field(default_factory=tuple)
    backtest: BacktestResult | None = None
    report_search_results: tuple[ReportSearchResult, ...] = field(default_factory=tuple)
    errors: tuple[str, ...] = field(default_factory=tuple)


class CompanyResearchPipeline:
    """Collect local source data and classify one company."""

    def __init__(self, engineer: DeterministicFeatureEngineer | None = None) -> None:
        self._engineer = engineer or DeterministicFeatureEngineer()
        self._stage_engine = StageUpdateEngine()

    def run(self, inputs: CompanyResearchInput) -> CompanyResearchResult:
        instrument = inputs.instrument
        as_of_date = inputs.as_of_date
        start = as_of_date - timedelta(days=inputs.lookback_days)
        errors: list[str] = []

        price_bars = _safe_tuple(errors, "krx.get_price_bars", lambda: (
            inputs.connectors.krx.get_price_bars(instrument.symbol, start, as_of_date, as_of_date)
            if inputs.connectors.krx is not None
            else ()
        ))
        financial_actuals = self._financial_actuals(inputs, errors)
        consensus = _safe_tuple(errors, "consensus.get_consensus", lambda: (
            inputs.connectors.consensus.get_consensus(instrument.symbol, as_of_date)
            if inputs.connectors.consensus is not None
            else ()
        ))
        revisions = _safe_tuple(errors, "consensus.get_consensus_revisions", lambda: (
            inputs.connectors.consensus.get_consensus_revisions(instrument.symbol, as_of_date)
            if inputs.connectors.consensus is not None
            else ()
        ))
        disclosures = self._disclosures(inputs, start, errors)
        news_items = self._news(inputs, start, errors)
        report_results = self._report_search_results(instrument, as_of_date, inputs.connectors, errors)
        parsed_reports = self._parse_report_results(instrument, report_results, as_of_date, errors)
        source_findings = self._source_findings(inputs, news_items, errors)

        feature_input = FeatureEngineeringInput(
            symbol=instrument.symbol,
            as_of_date=as_of_date,
            company_name=instrument.name,
            sector_context=" ".join(part for part in (instrument.sector_custom, instrument.sector_exchange) if part) or None,
            price_bars=price_bars,
            financial_actuals=financial_actuals,
            consensus=consensus,
            consensus_revisions=revisions,
            disclosures=disclosures,
            research_reports=parsed_reports,
            news_items=news_items,
        )
        feature_result = self._engineer.engineer(feature_input)
        score = feature_result.score()
        red_team = RedTeamEngine().assess(feature_result.red_team_signals)
        evidence = _dedupe_evidence(
            tuple(inputs.historical_evidence)
            + evidence_from_feature_domains(
                market=instrument.market,
                fallback_symbol=instrument.symbol,
                financial_actuals=financial_actuals,
                consensus=consensus,
                consensus_revisions=revisions,
                disclosures=disclosures,
                research_reports=parsed_reports,
                news_items=news_items,
            )
        )
        expanded = self._expanded_web_research(
            inputs=inputs,
            base_feature_input=feature_input,
            base_evidence=evidence,
            report_results=report_results,
            errors=errors,
        )
        if expanded is not None:
            feature_input = expanded.feature_input
            feature_result = expanded.feature_result
            score = expanded.score
            red_team = expanded.red_team
            evidence = _dedupe_evidence(tuple(evidence) + tuple(expanded.web_result.evidence))
        if expanded is not None and not is_score_valid(score):
            stage = expanded.stage
        else:
            stage = self._stage_engine.classify(
                StageUpdateInput(
                    score=score,
                    red_team=red_team,
                    previous_stage=inputs.previous_stage,
                    theme_regime_score=80.0 if self._has_regime_context(feature_input) else 0.0,
                    company_event_score=80.0 if self._has_company_event(feature_input) else 0.0,
                    high_quality_company_event=bool(feature_input.disclosures or feature_input.research_reports),
                    evidence_ids=tuple(item.evidence_id for item in evidence if item.as_of_date <= as_of_date),
                )
            )
        backtest = self._backtest(inputs, stage, price_bars, errors)
        findings = tuple(red_team.findings) + tuple(source_findings)
        if expanded is not None:
            findings = _dedupe_findings(tuple(expanded.red_team_findings) + findings)
        return CompanyResearchResult(
            instrument=instrument,
            as_of_date=as_of_date,
            feature_input=feature_input,
            feature_result=feature_result,
            score=score,
            red_team=red_team,
            stage=stage,
            evidence=evidence,
            red_team_findings=findings,
            backtest=backtest,
            report_search_results=report_results,
            errors=tuple(errors),
        )

    def _expanded_web_research(
        self,
        *,
        inputs: CompanyResearchInput,
        base_feature_input: FeatureEngineeringInput,
        base_evidence: Sequence[Evidence],
        report_results: Sequence[ReportSearchResult],
        errors: list[str],
    ):
        theme_provider = _effective_theme_route_provider(inputs)
        if theme_provider is None:
            return None
        searchable_reports = _dedupe_report_results(
            tuple(report_results)
            + self._report_search_results(
                inputs.instrument,
                inputs.as_of_date,
                inputs.connectors,
                errors,
            )
        )
        search_provider = inputs.free_search_provider or _StaticReportSearchProvider(searchable_reports)
        fixture_text_by_url = _report_text_by_url(searchable_reports)
        result = FreeWebResearchRunner(
            browser_provider=EmptySearchProvider(),
            free_search_provider=search_provider,
        ).run(
            FreeWebResearchInput(
                company_name=inputs.instrument.name,
                symbol=inputs.instrument.symbol,
                sector=" ".join(part for part in (inputs.instrument.sector_custom, inputs.instrument.sector_exchange) if part) or None,
                market=inputs.instrument.market,
                as_of_date=inputs.as_of_date,
                previous_stage=inputs.previous_stage,
                company_aliases=(inputs.instrument.name, inputs.instrument.symbol),
                budget=SearchBudget(),
                fixture_text_by_url=fixture_text_by_url,
                theme_rebalance_enabled=True,
                theme_route_provider=theme_provider,
                max_theme_expansion_rounds=inputs.max_theme_expansion_rounds,
                theme_evidence_review_enabled=inputs.theme_evidence_review_enabled,
                base_feature_input=base_feature_input,
            )
        )
        return result

    def run_historical_case(self, case: HistoricalCase) -> CompanyResearchResult:
        instrument = case.instrument or Instrument(
            symbol=case.symbol,
            name=case.company_name,
            market=case.market,
            exchange="KRX" if case.market == Market.KR else "US",
            sector_custom="historical_case",
        )
        feature_input = case.feature_input()
        feature_result = self._engineer.engineer(feature_input)
        score = feature_result.score()
        red_team = RedTeamEngine().assess(feature_result.red_team_signals)
        evidence = _dedupe_evidence(
            tuple(case.evidence)
            + evidence_from_feature_domains(
                market=case.market,
                fallback_symbol=case.symbol,
                financial_actuals=feature_input.financial_actuals,
                consensus=feature_input.consensus,
                consensus_revisions=feature_input.consensus_revisions,
                disclosures=feature_input.disclosures,
                research_reports=feature_input.research_reports,
                news_items=feature_input.news_items,
            )
        )
        stage = self._stage_engine.classify(
            StageUpdateInput(
                score=score,
                red_team=red_team,
                theme_regime_score=80.0,
                company_event_score=80.0,
                high_quality_company_event=True,
                evidence_ids=tuple(item.evidence_id for item in evidence if item.as_of_date <= case.stage3_date),
            )
        )
        backtest = None
        try:
            backtest = case.backtest()
        except ValueError:
            backtest = None
        return CompanyResearchResult(
            instrument=instrument,
            as_of_date=case.stage3_date,
            feature_input=feature_input,
            feature_result=feature_result,
            score=score,
            red_team=red_team,
            stage=stage,
            evidence=evidence,
            red_team_findings=tuple(red_team.findings),
            backtest=backtest,
        )

    def _financial_actuals(self, inputs: CompanyResearchInput, errors: list[str]) -> tuple[FinancialActual, ...]:
        symbol = inputs.instrument.symbol
        as_of_date = inputs.as_of_date
        items: list[FinancialActual] = []
        if inputs.instrument.market == Market.KR:
            items.extend(_safe_tuple(errors, "opendart.get_financial_actuals", lambda: (
                inputs.connectors.opendart.get_financial_actuals(symbol, as_of_date)
                if inputs.connectors.opendart is not None
                else ()
            )))
        if inputs.instrument.market == Market.US:
            items.extend(_safe_tuple(errors, "sec_edgar.get_financial_actuals", lambda: (
                inputs.connectors.sec_edgar.get_financial_actuals(symbol, as_of_date)
                if inputs.connectors.sec_edgar is not None
                else ()
            )))
        return tuple(sorted(items, key=lambda item: (item.period_end, item.reported_at)))

    def _disclosures(self, inputs: CompanyResearchInput, start: date, errors: list[str]) -> tuple[DisclosureEvent, ...]:
        symbol = inputs.instrument.symbol
        as_of_date = inputs.as_of_date
        items: list[DisclosureEvent] = []
        if inputs.instrument.market == Market.KR:
            items.extend(_safe_tuple(errors, "opendart.get_disclosures", lambda: (
                inputs.connectors.opendart.get_disclosures(symbol, start, as_of_date, as_of_date)
                if inputs.connectors.opendart is not None
                else ()
            )))
        if inputs.instrument.market == Market.US:
            items.extend(_safe_tuple(errors, "sec_edgar.get_disclosures", lambda: (
                inputs.connectors.sec_edgar.get_disclosures(symbol, start, as_of_date, as_of_date)
                if inputs.connectors.sec_edgar is not None
                else ()
            )))
        return tuple(sorted(items, key=lambda item: item.published_at))

    def _news(self, inputs: CompanyResearchInput, start: date, errors: list[str]) -> tuple[NewsItem, ...]:
        symbol = inputs.instrument.symbol
        as_of_date = inputs.as_of_date
        items: list[NewsItem] = []
        items.extend(_safe_tuple(errors, "naver_news.get_news", lambda: (
            inputs.connectors.naver_news.get_news(symbol, start, as_of_date, as_of_date)
            if inputs.connectors.naver_news is not None
            else ()
        )))
        if inputs.instrument.market == Market.US:
            items.extend(_safe_tuple(errors, "sec_edgar.get_news", lambda: (
                inputs.connectors.sec_edgar.get_news(symbol, start, as_of_date, as_of_date)
                if inputs.connectors.sec_edgar is not None
                else ()
            )))
        return tuple(sorted(items, key=lambda item: item.published_at))

    @staticmethod
    def _report_search_results(
        instrument: Instrument,
        as_of_date: date,
        connectors: ConnectorBundle,
        errors: list[str],
    ) -> tuple[ReportSearchResult, ...]:
        results: list[ReportSearchResult] = []
        company = instrument.name
        results.extend(_safe_tuple(errors, "report_search.search_reports", lambda: (
            connectors.report_search.search_reports(company, as_of_date)
            if connectors.report_search is not None
            else ()
        )))
        results.extend(_safe_tuple(errors, "naver_webdoc.search_reports", lambda: (
            connectors.naver_webdoc.search_reports(company, as_of_date)
            if connectors.naver_webdoc is not None
            else ()
        )))
        unique: dict[str, ReportSearchResult] = {}
        for item in results:
            unique.setdefault(item.url, item)
        return tuple(unique.values())

    @staticmethod
    def _parse_report_results(
        instrument: Instrument,
        report_results: Sequence[ReportSearchResult],
        as_of_date: date,
        errors: list[str],
    ) -> tuple[ResearchReport, ...]:
        reports: list[ResearchReport] = []
        for result in report_results:
            text = result.parsed_fields.get("extracted_text")
            if not text:
                continue
            try:
                parsed = parse_research_report_text(
                    symbol=instrument.symbol,
                    market=instrument.market,
                    text=str(text),
                    metadata={
                        "title": result.title,
                        "broker": result.source,
                        "publish_date": result.publish_date or as_of_date,
                        "as_of_date": result.publish_date or as_of_date,
                        "url": result.url,
                    },
                )
                reports.append(parsed.report)
            except (ValueError, TypeError) as exc:
                errors.append(f"report_parser:{instrument.symbol}:{type(exc).__name__}:{exc}")
        return tuple(reports)

    @staticmethod
    def _source_findings(
        inputs: CompanyResearchInput,
        news_items: Sequence[NewsItem],
        errors: list[str],
    ) -> tuple[RedTeamFinding, ...]:
        findings: list[RedTeamFinding] = []
        findings.extend(_safe_tuple(errors, "kind.get_red_team_candidates", lambda: (
            inputs.connectors.kind.get_red_team_candidates(inputs.instrument.symbol, inputs.as_of_date)
            if inputs.connectors.kind is not None
            else ()
        )))
        if inputs.connectors.naver_news is not None:
            for item in news_items:
                finding = inputs.connectors.naver_news.to_red_team_finding(item)
                if finding is not None:
                    findings.append(finding)
        return tuple(findings)

    @staticmethod
    def _backtest(
        inputs: CompanyResearchInput,
        stage: StageSnapshot,
        price_bars: Sequence[PriceBar],
        errors: list[str],
    ) -> BacktestResult | None:
        stage3_date = inputs.stage3_date
        if stage3_date is None:
            return None
        bars = tuple(inputs.backtest_price_bars or price_bars)
        if not bars:
            return None
        try:
            return BacktestEngine().evaluate_stage3(
                Stage3BacktestInput(
                    symbol=inputs.instrument.symbol,
                    stage3_date=stage3_date,
                    price_bars=bars,
                    stage_snapshots=(stage,),
                    stage3_price=inputs.stage3_price,
                )
            )
        except ValueError as exc:
            errors.append(f"backtest:{inputs.instrument.symbol}:{exc}")
            return None

    @staticmethod
    def _has_company_event(feature_input: FeatureEngineeringInput) -> bool:
        return bool(feature_input.disclosures or feature_input.research_reports or feature_input.news_items)

    @staticmethod
    def _has_regime_context(feature_input: FeatureEngineeringInput) -> bool:
        return bool(feature_input.news_items or feature_input.research_reports)


def _safe_tuple(errors: list[str], label: str, loader: Callable[[], Sequence[Any]]) -> tuple[Any, ...]:
    try:
        return tuple(loader())
    except (AttributeError, FileNotFoundError, SourceConnectorError, ValueError, TypeError) as exc:
        errors.append(f"{label}:{type(exc).__name__}:{exc}")
        return ()


def _effective_theme_route_provider(inputs: CompanyResearchInput) -> ThemeRouteProvider | None:
    if inputs.theme_rebalance_enabled is False:
        return None
    if inputs.theme_route_provider is not None:
        return inputs.theme_route_provider
    if os.environ.get("E2R_THEME_ROUTE_PROVIDER"):
        return build_theme_route_provider_from_env(working_directory=Path.cwd())
    if inputs.theme_rebalance_enabled or not inputs.fixture_mode:
        return build_default_codex_theme_route_provider(working_directory=Path.cwd())
    return None


@dataclass(frozen=True)
class _StaticReportSearchProvider:
    """Expose connector report results through the FreeWebResearch search API."""

    report_results: Sequence[ReportSearchResult]

    def search(self, query: str, as_of_date: date, max_results: int = 100) -> tuple[SearchResult, ...]:
        rows: list[SearchResult] = []
        for rank, item in enumerate(self.report_results, start=1):
            if item.publish_date is not None and item.publish_date > as_of_date:
                continue
            if not _report_result_matches_query(item, query):
                continue
            rows.append(
                SearchResult(
                    title=item.title,
                    url=item.url,
                    snippet=item.snippet,
                    source=item.source,
                    published_at=datetime(item.publish_date.year, item.publish_date.month, item.publish_date.day, 8, 0)
                    if item.publish_date
                    else None,
                    query=query,
                    rank=rank,
                    is_pdf=item.is_pdf,
                    is_report_domain=item.is_recognized_report_domain,
                    confidence=0.9 if item.is_recognized_report_domain or item.is_pdf else 0.7,
                )
            )
        return tuple(rows[:max_results])


def _report_result_matches_query(item: ReportSearchResult, query: str) -> bool:
    if item.query:
        return _clean_query(item.query) == _clean_query(query)
    query_tokens = _query_tokens(query)
    if not query_tokens:
        return False
    haystack = _clean_query(" ".join(part for part in (item.title, item.snippet or "") if part))
    return all(token in haystack for token in query_tokens[:3])


def _query_tokens(query: str) -> tuple[str, ...]:
    return tuple(token for token in _clean_query(query).split() if len(token) >= 2)


def _clean_query(value: str) -> str:
    return " ".join(str(value or "").lower().split())


def _report_text_by_url(results: Sequence[ReportSearchResult]) -> dict[str, str]:
    text_by_url: dict[str, str] = {}
    for item in results:
        text = item.parsed_fields.get("extracted_text")
        if text:
            text_by_url[item.url] = str(text)
    return text_by_url


def _dedupe_report_results(items: Sequence[ReportSearchResult]) -> tuple[ReportSearchResult, ...]:
    by_url: dict[str, ReportSearchResult] = {}
    for item in items:
        by_url.setdefault(item.url, item)
    return tuple(by_url.values())


def _dedupe_evidence(items: Sequence[Evidence]) -> tuple[Evidence, ...]:
    unique: dict[str, Evidence] = {}
    for item in items:
        unique.setdefault(item.evidence_id, item)
    return tuple(unique.values())


def _dedupe_findings(items: Sequence[RedTeamFinding]) -> tuple[RedTeamFinding, ...]:
    unique: dict[tuple[str, str, tuple[str, ...]], RedTeamFinding] = {}
    for item in items:
        unique.setdefault((item.symbol, item.risk_type, item.evidence_ids), item)
    return tuple(unique.values())
