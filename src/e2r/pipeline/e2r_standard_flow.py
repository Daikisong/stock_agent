"""Canonical E2R_STANDARD production flow."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Mapping, Sequence

from e2r.audit import AuditFinding, audit_parser_outputs
from e2r.cheap_scan import KoreaCheapScanConfig, KoreaCheapScanResult, KoreaCheapScanSources, KoreaCheapScanner
from e2r.cheap_scan.models import CheapScanCandidate, RecommendedNextLayer
from e2r.llm import LLMAnalystInput, LLMAnalystOutput, LLMProvider, LLMResearchAnalyst, build_theme_route_provider_from_env
from e2r.llm.theme_provider import ThemeRouteProvider
from e2r.models import Evidence, Market, RedTeamFinding, ScoreSnapshot, StageSnapshot
from e2r.research.free_web_research_runner import FreeWebResearchInput, FreeWebResearchRunner, WebResearchPipelineResult
from e2r.research.report_radar import ReportRadar, ReportRadarCandidate
from e2r.research.search_budget import SearchBudget
from e2r.research.search_provider import EmptySearchProvider, SearchProvider


E2R_STANDARD = "E2R_STANDARD"
DIAGNOSTIC_REPLAY_MODES = ("official_only", "case_fixture", "hybrid")


@dataclass(frozen=True)
class E2RStandardConfig:
    """Configuration for the canonical E2R standard flow."""

    as_of_date: date
    market: Market = Market.KR
    sources: KoreaCheapScanSources | None = None
    universe_limit: int | None = None
    top_candidates: int = 50
    output_directory: str | Path = "output/e2r_standard"
    fixture_mode: bool = True
    cheap_scan_lookback_days: int = 370
    disclosure_lookback_days: int = 3
    report_radar_enabled: bool = True
    report_radar_universe_limit: int = 20
    search_budget: SearchBudget = field(default_factory=SearchBudget)
    browser_provider: SearchProvider | None = None
    free_search_provider: SearchProvider | None = None
    fixture_text_by_url: Mapping[str, str | Path] = field(default_factory=dict)
    live_page_fetch_enabled: bool = False
    page_fetch_timeout_seconds: float = 10.0
    page_fetch_cache_directory: str | Path | None = None
    llm_enabled: bool = False
    llm_provider: LLMProvider | None = None
    theme_rebalance_enabled: bool | None = None
    theme_route_provider: ThemeRouteProvider | None = None
    max_theme_expansion_rounds: int = 3
    theme_evidence_review_enabled: bool = False

    def __post_init__(self) -> None:
        if type(self.as_of_date) is not date:
            raise ValueError("as_of_date must be a date")
        if not isinstance(self.market, Market):
            object.__setattr__(self, "market", Market(self.market))
        if self.page_fetch_timeout_seconds <= 0:
            raise ValueError("page_fetch_timeout_seconds must be positive")
        if self.theme_rebalance_enabled is None:
            object.__setattr__(self, "theme_rebalance_enabled", _default_theme_rebalance_enabled(self))
        if self.max_theme_expansion_rounds < 0:
            raise ValueError("max_theme_expansion_rounds must be non-negative")


@dataclass(frozen=True)
class E2RStandardResult:
    """Output of one canonical E2R_STANDARD run."""

    flow_name: str
    as_of_date: date
    market: Market
    cheap_scan: KoreaCheapScanResult
    candidates: tuple[CheapScanCandidate, ...]
    report_radar_candidates: tuple[ReportRadarCandidate, ...]
    web_results: tuple[WebResearchPipelineResult, ...]
    evidence: tuple[Evidence, ...]
    scores: tuple[ScoreSnapshot, ...]
    stages: tuple[StageSnapshot, ...]
    red_team_findings: tuple[RedTeamFinding, ...]
    audit_findings: tuple[AuditFinding, ...]
    llm_outputs: tuple[LLMAnalystOutput, ...] = field(default_factory=tuple)
    notes: tuple[str, ...] = field(default_factory=tuple)


class E2RStandardFlow:
    """Canonical free-web plus official-data E2R flow.

    Diagnostic replay modes are deliberately not accepted here. They remain in
    backtest modules for coverage diagnosis and regression tests.
    """

    flow_name = E2R_STANDARD

    def run(self, config: E2RStandardConfig) -> E2RStandardResult:
        sources = config.sources or KoreaCheapScanSources.local_defaults()
        cheap_scan = KoreaCheapScanner(sources).run(
            KoreaCheapScanConfig(
                as_of_date=config.as_of_date,
                markets=(config.market,),
                sources=sources,
                universe_limit=config.universe_limit,
                lookback_days=config.cheap_scan_lookback_days,
                disclosure_lookback_days=config.disclosure_lookback_days,
                top_n=config.top_candidates,
                report_radar_enabled=config.report_radar_enabled,
            )
        )
        radar_candidates = self._run_report_radar(config, sources)
        candidates = _merge_candidates(cheap_scan.candidates, tuple(item.to_cheap_scan_candidate() for item in radar_candidates))
        web_results = self._run_web_research(config, candidates)
        evidence = tuple(item for result in web_results for item in result.web_result.evidence)
        scores = tuple(result.score for result in web_results)
        stages = tuple(result.stage for result in web_results)
        red_team_findings = _dedupe_red_team_findings(
            finding
            for result in web_results
            for finding in result.red_team_findings
        )
        audit_findings = audit_parser_outputs(evidence=evidence, scores=scores, stages=stages)
        llm_outputs = self._run_llm(config, web_results)
        return E2RStandardResult(
            flow_name=E2R_STANDARD,
            as_of_date=config.as_of_date,
            market=config.market,
            cheap_scan=cheap_scan,
            candidates=candidates,
            report_radar_candidates=radar_candidates,
            web_results=web_results,
            evidence=evidence,
            scores=scores,
            stages=stages,
            red_team_findings=red_team_findings,
            audit_findings=audit_findings,
            llm_outputs=llm_outputs,
            notes=(
                "E2R_STANDARD is the production flow",
                "official_only/case_fixture/hybrid are diagnostic replay modes only",
            ),
        )

    def _run_report_radar(
        self,
        config: E2RStandardConfig,
        sources: KoreaCheapScanSources,
    ) -> tuple[ReportRadarCandidate, ...]:
        if not config.report_radar_enabled:
            return ()
        provider = config.free_search_provider or EmptySearchProvider()
        instruments = sources.list_instruments(config.market, config.as_of_date)
        return ReportRadar(provider).run(
            instruments=instruments,
            as_of_date=config.as_of_date,
            budget=config.search_budget,
            max_symbols=config.report_radar_universe_limit,
        )

    def _run_web_research(
        self,
        config: E2RStandardConfig,
        candidates: Sequence[CheapScanCandidate],
    ) -> tuple[WebResearchPipelineResult, ...]:
        runner = FreeWebResearchRunner(
            browser_provider=config.browser_provider or EmptySearchProvider(),
            free_search_provider=config.free_search_provider or EmptySearchProvider(),
        )
        theme_route_provider = config.theme_route_provider
        if theme_route_provider is None and config.theme_rebalance_enabled:
            theme_route_provider = build_theme_route_provider_from_env(working_directory=Path.cwd())
        if theme_route_provider is None and _should_default_to_codex_theme_provider(config):
            theme_route_provider = build_theme_route_provider_from_env(
                {"E2R_THEME_ROUTE_PROVIDER": "codex"},
                working_directory=Path.cwd(),
            )
        results: list[WebResearchPipelineResult] = []
        for candidate in candidates:
            if candidate.recommended_next_layer not in {RecommendedNextLayer.EVENT_SEARCH, RecommendedNextLayer.DEEP_RESEARCH}:
                continue
            results.append(
                runner.run(
                    FreeWebResearchInput(
                        company_name=candidate.company_name,
                        symbol=candidate.symbol,
                        sector=None,
                        market=candidate.market,
                        as_of_date=candidate.as_of_date,
                        company_aliases=(candidate.company_name, candidate.symbol),
                        candidate_reason_codes=candidate.reason_codes,
                        budget=config.search_budget,
                        fixture_text_by_url=config.fixture_text_by_url,
                        live_page_fetch_enabled=config.live_page_fetch_enabled,
                        page_fetch_timeout_seconds=config.page_fetch_timeout_seconds,
                        page_fetch_cache_directory=config.page_fetch_cache_directory,
                        theme_rebalance_enabled=config.theme_rebalance_enabled,
                        theme_route_provider=theme_route_provider,
                        max_theme_expansion_rounds=config.max_theme_expansion_rounds,
                        theme_evidence_review_enabled=config.theme_evidence_review_enabled,
                    )
                )
            )
        return tuple(results)

    @staticmethod
    def _run_llm(
        config: E2RStandardConfig,
        web_results: Sequence[WebResearchPipelineResult],
    ) -> tuple[LLMAnalystOutput, ...]:
        if not config.llm_enabled or config.llm_provider is None:
            return ()
        analyst = LLMResearchAnalyst(config.llm_provider)
        outputs: list[LLMAnalystOutput] = []
        for result in web_results:
            outputs.append(
                analyst.analyze(
                    LLMAnalystInput(
                        symbol=result.stage.symbol,
                        company_name=result.web_result.company_name,
                        as_of_date=result.stage.as_of_date,
                        deterministic_stage=result.stage.stage,
                        evidence_ids=result.stage.evidence_ids,
                        document_text="\n".join(item.text or "" for item in result.web_result.fetched_documents),
                    )
                )
            )
        return tuple(outputs)


def _merge_candidates(
    official: Sequence[CheapScanCandidate],
    radar: Sequence[CheapScanCandidate],
) -> tuple[CheapScanCandidate, ...]:
    by_key: dict[tuple[str, str], CheapScanCandidate] = {}
    for item in tuple(official) + tuple(radar):
        key = (item.symbol, item.candidate_source_path)
        existing = by_key.get(key)
        if existing is None or item.cheap_scan_total_score > existing.cheap_scan_total_score:
            by_key[key] = item
    return tuple(sorted(by_key.values(), key=lambda item: (-item.cheap_scan_total_score, item.symbol)))


def _default_theme_rebalance_enabled(config: E2RStandardConfig) -> bool:
    return bool(
        config.theme_route_provider is not None
        or os.environ.get("E2R_THEME_ROUTE_PROVIDER")
        or not config.fixture_mode
    )


def _should_default_to_codex_theme_provider(config: E2RStandardConfig) -> bool:
    return bool(config.theme_rebalance_enabled and not config.fixture_mode)


def _dedupe_red_team_findings(findings) -> tuple[RedTeamFinding, ...]:
    unique: dict[tuple[str, str, str, tuple[str, ...]], RedTeamFinding] = {}
    for finding in findings:
        key = (finding.symbol, finding.as_of_date.isoformat(), finding.risk_type, tuple(finding.evidence_ids))
        unique.setdefault(key, finding)
    return tuple(unique.values())


__all__ = [
    "DIAGNOSTIC_REPLAY_MODES",
    "E2R_STANDARD",
    "E2RStandardConfig",
    "E2RStandardFlow",
    "E2RStandardResult",
]
