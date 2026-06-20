"""Controlled Korea live-lite pilot runner."""

from __future__ import annotations

import json
import os
import re
from collections import Counter
from dataclasses import dataclass, field, fields, is_dataclass, replace
from datetime import date, datetime, timedelta
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

from e2r.audit import AuditFinding, audit_parser_outputs
from e2r.briefing import MorningBrief, generate_morning_briefing
from e2r.calibration.scoring_profile import get_active_scoring_profile
from e2r.cheap_scan import KoreaCheapScanConfig, KoreaCheapScanResult, KoreaCheapScanSources, KoreaCheapScanner
from e2r.cheap_scan.korea_sources import DataGoKrFSCConnector
from e2r.cheap_scan.models import CheapScanCandidate, RecommendedNextLayer
from e2r.cheap_scan.query_escalation import EscalationQueryPlanner, queries_for_candidate
from e2r.env import load_project_env
from e2r.features import FeatureEngineeringInput
from e2r.llm.codex_theme_provider import build_default_codex_theme_route_provider, build_theme_route_provider_from_env
from e2r.llm.theme_provider import ThemeRouteProvider
from e2r.models import (
    ConsensusRevision,
    ConsensusSnapshot,
    DisclosureEvent,
    Evidence,
    FinancialActual,
    Instrument,
    Market,
    PriceBar,
    RedTeamFinding,
    ResearchReport,
    ScoreSnapshot,
    Stage,
    StageSnapshot,
)
from e2r.pipeline.evidence_builder import evidence_from_feature_domains
from e2r.research.free_web_research_runner import FreeWebResearchInput, FreeWebResearchRunner, WebResearchPipelineResult
from e2r.research.naver_search_provider import NaverFreeSearchProvider
from e2r.research.report_radar import REPORT_RADAR_PHRASES, ReportRadar, ReportRadarCandidate
from e2r.research.query_planner import QueryPlan, QuerySpec
from e2r.research.search_budget import SearchBudget
from e2r.research.search_provider import EmptySearchProvider, SearchProvider, SearchResult
from e2r.score_validity import (
    find_score_state_contract_violations,
    is_score_valid,
    normalized_score_state_mapping_if_present,
    raw_score_total_before_block,
    research_input_fingerprint,
    score_block_reason,
    score_fingerprint,
    score_variability_drivers as build_score_variability_drivers,
    visible_score_total,
)
from e2r.sources import DEFAULT_SOURCE_LICENSE_METADATA, BrokerTargetRow, CompanyGuideConnector, KINDConnector, KRXConnector, OpenDARTConnector, SourceLicenseMetadata
from e2r.sources.http_client import HttpClient, HttpClientStats
from e2r.sources.opendart import extract_document_text, normalize_disclosure_detail
from e2r.sources.rate_limit import RateLimiter, SourceRateLimit
from e2r.sources.source_errors import SourceRequest, load_fixture_records


DEFAULT_FIXTURE_ROOT = Path("data/raw/korea_cheap_scan")
_CROSS_EVIDENCE_STAGE3_GREEN_REASON = "live-lite Stage 3-Green requires at least two independent evidence types"


@dataclass(frozen=True)
class KoreaLiveLiteBudget:
    """Source and research accounting for a Korea live-lite run.

    ``None`` on accounting caps means the run is not stopped by search/API cap
    checks. Tests may still pass explicit small numbers to verify skip logs, but
    operational presets should not cap evidence collection by default.
    """

    max_opendart_calls_per_day: int | None = None
    max_krx_calls_per_day: int | None = None
    max_data_go_kr_calls_per_day: int | None = None
    max_naver_search_calls_per_day: int | None = None
    max_company_guide_calls_per_day: int | None = None
    max_symbols_for_event_search: int | None = None
    max_symbols_for_deep_research: int | None = None
    max_opendart_detail_fetches_per_run: int | None = None

    def __post_init__(self) -> None:
        nullable_fields = {
            "max_opendart_calls_per_day",
            "max_krx_calls_per_day",
            "max_data_go_kr_calls_per_day",
            "max_naver_search_calls_per_day",
            "max_company_guide_calls_per_day",
            "max_symbols_for_event_search",
            "max_symbols_for_deep_research",
            "max_opendart_detail_fetches_per_run",
        }
        for field_name in (
            "max_opendart_calls_per_day",
            "max_krx_calls_per_day",
            "max_data_go_kr_calls_per_day",
            "max_naver_search_calls_per_day",
            "max_company_guide_calls_per_day",
            "max_symbols_for_event_search",
            "max_symbols_for_deep_research",
            "max_opendart_detail_fetches_per_run",
        ):
            value = getattr(self, field_name)
            if value is None:
                if field_name not in nullable_fields:
                    raise ValueError(f"{field_name} must be non-negative")
                continue
            if value < 0:
                raise ValueError(f"{field_name} must be non-negative")


@dataclass(frozen=True)
class KoreaLiveLiteConfig:
    """Configuration for one Korea live-lite pilot run."""

    as_of_date: date
    output_directory: str | Path = "output"
    fixture_mode: bool = True
    live_enabled: bool = False
    sources: KoreaCheapScanSources | None = None
    budget: KoreaLiveLiteBudget = field(default_factory=KoreaLiveLiteBudget)
    universe_limit: int | None = None
    top_candidates: int | None = None
    disclosure_lookback_days: int = 1
    lookback_days: int = 370
    browser_provider: SearchProvider | None = None
    free_search_provider: SearchProvider | None = None
    fixture_text_by_url: Mapping[str, str | Path] = field(default_factory=dict)
    max_results_per_query: int = 100
    top_results: int | None = 60
    require_cross_evidence_for_stage3_green: bool = True
    http_client: HttpClient | None = None
    cache_directory: str | Path = "data/cache"
    env_file: str | Path | None = ".env"
    allow_parallel_live_requests: bool = False
    max_global_live_workers: int = 1
    live_page_fetch_enabled: bool = False
    page_fetch_timeout_seconds: float = 10.0
    page_fetch_cache_directory: str | Path | None = None
    live_smoke_preset_used: str | None = None
    enable_stock_issuance_source: bool = False
    enable_krx_openapi_source: bool = False
    event_search_min_score: float = 25.0
    deep_research_min_score: float = 45.0
    price_only_event_allowed: bool = True
    report_radar_enabled: bool = False
    report_radar_universe_limit: int | None = None
    active_watchlist_symbols: tuple[str, ...] = field(default_factory=tuple)
    targeted_smoke_enabled: bool = False
    targeted_smoke_only: bool = False
    targeted_smoke_symbol: str | None = None
    targeted_smoke_company: str | None = None
    targeted_smoke_queries: tuple[str, ...] = field(default_factory=tuple)
    top_trading_value_probe_enabled: bool = False
    top_trading_value_probe_count: int = 5
    top_trading_value_probe_queries: tuple[str, ...] = field(default_factory=tuple)
    theme_rebalance_enabled: bool | None = None
    theme_route_provider: ThemeRouteProvider | None = None
    max_theme_expansion_rounds: int | None = 2
    max_score_gap_expansion_rounds: int | None = 2
    theme_route_search_result_limit: int | None = 80
    theme_route_document_limit: int | None = 32
    theme_route_document_excerpt_chars: int = 1_200
    post_parse_gap_expansion_max_queries: int | None = 10
    score_gap_query_retry_max: int | None = None
    theme_evidence_review_enabled: bool = True
    phase_log_enabled: bool = True
    company_guide_enabled: bool = True
    company_guide_connector: CompanyGuideConnector | None = None
    company_guide_recent_reports_per_page: int = 20

    def __post_init__(self) -> None:
        if type(self.as_of_date) is not date:
            raise ValueError("as_of_date must be a date")
        if self.universe_limit is not None and self.universe_limit <= 0:
            raise ValueError("universe_limit must be positive when set")
        if self.top_candidates is not None and self.top_candidates <= 0:
            raise ValueError("top_candidates must be positive")
        if self.disclosure_lookback_days < 0:
            raise ValueError("disclosure_lookback_days must be non-negative")
        if self.lookback_days <= 0:
            raise ValueError("lookback_days must be positive")
        if self.max_results_per_query <= 0:
            raise ValueError("max_results_per_query must be positive")
        if self.top_results is not None and self.top_results <= 0:
            raise ValueError("top_results must be positive")
        if self.max_global_live_workers <= 0:
            raise ValueError("max_global_live_workers must be positive")
        if not self.allow_parallel_live_requests and self.max_global_live_workers != 1:
            raise ValueError("max_global_live_workers must be 1 unless allow_parallel_live_requests is true")
        if self.page_fetch_timeout_seconds <= 0:
            raise ValueError("page_fetch_timeout_seconds must be positive")
        if self.event_search_min_score < 0 or self.deep_research_min_score < 0:
            raise ValueError("cheap-scan score thresholds must be non-negative")
        if self.report_radar_universe_limit is not None and self.report_radar_universe_limit <= 0:
            raise ValueError("report_radar_universe_limit must be positive")
        object.__setattr__(self, "active_watchlist_symbols", tuple(self.active_watchlist_symbols))
        object.__setattr__(self, "targeted_smoke_queries", tuple(self.targeted_smoke_queries))
        object.__setattr__(self, "top_trading_value_probe_queries", tuple(self.top_trading_value_probe_queries))
        if self.theme_rebalance_enabled is None:
            object.__setattr__(self, "theme_rebalance_enabled", _default_theme_rebalance_enabled(self))
        if self.top_trading_value_probe_count <= 0:
            raise ValueError("top_trading_value_probe_count must be positive")
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
        if self.post_parse_gap_expansion_max_queries is not None and self.post_parse_gap_expansion_max_queries < 0:
            raise ValueError("post_parse_gap_expansion_max_queries must be non-negative")
        if self.score_gap_query_retry_max is not None and self.score_gap_query_retry_max < 0:
            raise ValueError("score_gap_query_retry_max must be non-negative")
        if self.company_guide_recent_reports_per_page <= 0:
            raise ValueError("company_guide_recent_reports_per_page must be positive")

    @classmethod
    def smoke_preset(
        cls,
        preset: str,
        *,
        as_of_date: date,
        **overrides,
    ) -> "KoreaLiveLiteConfig":
        """Build a safe live-lite preset for smoke or shadow runs."""

        if preset == "tiny":
            values = {
                "as_of_date": as_of_date,
                "universe_limit": 50,
                "budget": KoreaLiveLiteBudget(),
                "live_smoke_preset_used": "tiny",
            }
        elif preset == "small":
            values = {
                "as_of_date": as_of_date,
                "universe_limit": 300,
                "budget": KoreaLiveLiteBudget(),
                "live_smoke_preset_used": "small",
            }
        elif preset == "standard_shadow":
            values = {
                "as_of_date": as_of_date,
                "universe_limit": None,
                "budget": KoreaLiveLiteBudget(),
                "live_smoke_preset_used": "standard_shadow",
            }
        else:
            raise ValueError("preset must be tiny, small, or standard_shadow")
        values.update(overrides)
        return cls(**values)


@dataclass(frozen=True)
class SkippedCandidate:
    """Candidate not escalated to web research."""

    symbol: str
    company_name: str
    recommended_next_layer: RecommendedNextLayer
    reason: str


@dataclass(frozen=True)
class KoreaLiveLiteRunLog:
    """Machine-readable audit log for a live-lite run."""

    as_of_date: date
    fixture_mode: bool
    live_enabled: bool
    effective_fixture_mode: bool
    missing_credentials: tuple[str, ...] = field(default_factory=tuple)
    source_call_counts: Mapping[str, int] = field(default_factory=dict)
    built_requests: tuple[SourceRequest, ...] = field(default_factory=tuple)
    skipped_candidates: tuple[SkippedCandidate, ...] = field(default_factory=tuple)
    skipped_queries: tuple[Mapping[str, Any], ...] = field(default_factory=tuple)
    dropped_search_results: tuple[Mapping[str, Any], ...] = field(default_factory=tuple)
    source_modes: Mapping[str, str] = field(default_factory=dict)
    live_requests_executed: int = 0
    live_requests_failed: int = 0
    cache_hits: int = 0
    cache_writes: int = 0
    fallback_reasons: Mapping[str, str] = field(default_factory=dict)
    request_only_sources: tuple[str, ...] = field(default_factory=tuple)
    audit_findings: tuple[AuditFinding, ...] = field(default_factory=tuple)
    planned_opendart_detail_requests: tuple[SourceRequest, ...] = field(default_factory=tuple)
    executed_opendart_detail_requests: tuple[SourceRequest, ...] = field(default_factory=tuple)
    opendart_detail_evidence_ids: tuple[str, ...] = field(default_factory=tuple)
    report_radar_candidates: tuple[Mapping[str, Any], ...] = field(default_factory=tuple)
    targeted_smoke_results: tuple[Mapping[str, Any], ...] = field(default_factory=tuple)
    top_trading_value_probe_candidates: tuple[Mapping[str, Any], ...] = field(default_factory=tuple)
    theme_routes: tuple[Mapping[str, Any], ...] = field(default_factory=tuple)
    theme_expansion_queries: tuple[Mapping[str, Any], ...] = field(default_factory=tuple)
    theme_missing_slots: tuple[Mapping[str, Any], ...] = field(default_factory=tuple)
    theme_route_status_counts: Mapping[str, int] = field(default_factory=dict)
    audit_summary: Mapping[str, Any] = field(default_factory=dict)
    score_state_contract_findings: tuple[str, ...] = field(default_factory=tuple)
    rate_limit_waits: int = 0
    rate_limit_skips: int = 0
    actual_http_requests_by_source: Mapping[str, int] = field(default_factory=dict)
    logical_queries_by_source: Mapping[str, int] = field(default_factory=dict)
    max_concurrency_used_by_source: Mapping[str, int] = field(default_factory=dict)
    live_smoke_preset_used: str | None = None
    source_license_metadata: tuple[SourceLicenseMetadata, ...] = field(default_factory=tuple)
    phase_log_path: str | None = None
    notes: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class KoreaLiveLiteResult:
    """Output bundle for the Korea live-lite pilot."""

    as_of_date: date
    cheap_scan: KoreaCheapScanResult
    candidates: tuple[CheapScanCandidate, ...]
    web_results: tuple[WebResearchPipelineResult, ...]
    scores: tuple[ScoreSnapshot, ...]
    stages: tuple[StageSnapshot, ...]
    evidence: tuple[Evidence, ...]
    red_team_findings: tuple[RedTeamFinding, ...]
    morning_brief: MorningBrief
    candidates_path: Path
    evidence_path: Path
    brief_path: Path
    run_log_path: Path
    run_log: KoreaLiveLiteRunLog
    calibration_json_path: Path | None = None
    calibration_md_path: Path | None = None
    phase_log_path: Path | None = None


@dataclass(frozen=True)
class _CompanyGuideFeatureData:
    consensus: tuple[ConsensusSnapshot, ...] = field(default_factory=tuple)
    consensus_revisions: tuple[ConsensusRevision, ...] = field(default_factory=tuple)
    research_reports: tuple[ResearchReport, ...] = field(default_factory=tuple)


_EMPTY_COMPANY_GUIDE_FEATURE_DATA = _CompanyGuideFeatureData()


class KoreaLiveLiteRunner:
    """Run Korea cheap scan plus budgeted free web research."""

    def __init__(self, sources: KoreaCheapScanSources | None = None) -> None:
        self._sources = sources or fixture_sources()

    def run(self, config: KoreaLiveLiteConfig) -> KoreaLiveLiteResult:
        if config.live_enabled or not config.fixture_mode:
            load_project_env(config.env_file)
        missing_credentials = _missing_credentials(config)
        effective_fixture_mode = config.fixture_mode or (config.live_enabled and bool(missing_credentials))
        sources = config.sources or self._sources
        sources = _sources_with_stock_issuance_setting(sources, config.enable_stock_issuance_source)
        http_client = config.http_client or HttpClient(rate_limiter=_rate_limiter_for_config(config))
        source_modes, fallback_reasons, _request_only_sources = _initial_source_status(config, missing_credentials)
        source_modes["stock_issuance"] = _stock_issuance_source_mode(config)
        source_modes["krx_openapi"] = _krx_openapi_source_mode(config)
        source_modes["page_fetch"] = "live" if _live_page_fetch_enabled(config) else "fixture"
        if source_modes["krx_openapi"] == "fallback":
            fallback_reasons["krx_openapi"] = "missing_KRX_OPENAPI_KEY"
        if source_modes["krx_openapi"] == "request_only":
            _request_only_sources = tuple(dict.fromkeys((*_request_only_sources, "krx_openapi")))
        start = config.as_of_date - timedelta(days=config.disclosure_lookback_days)
        built_requests: list[SourceRequest] = []
        source_call_counts: dict[str, int] = {
            "opendart_disclosure_date_range": 0,
            "opendart_detail_fetches": 0,
            "opendart_symbol_disclosure_calls": 0,
            "opendart_company_code_calls": 0,
            "opendart_financial_statement_calls": 0,
            "krx_calls": 0,
            "data_go_kr_calls": 0,
            "data_go_kr_financial_actual_calls": 0,
            "naver_search_queries": 0,
            "company_guide_snapshot_calls": 0,
            "company_guide_recent_report_calls": 0,
        }

        targeted_only_research = _targeted_only_research_mode(config)
        smoke_candidates = _targeted_smoke_candidates(config)
        if targeted_only_research:
            sources = _sources_with_targeted_live_data_go_kr(
                sources=sources,
                config=config,
                candidates=smoke_candidates,
                http_client=http_client,
                built_requests=built_requests,
                source_call_counts=source_call_counts,
                source_modes=source_modes,
                fallback_reasons=fallback_reasons,
            )
        else:
            sources = _sources_with_live_data_go_kr(
                sources=sources,
                config=config,
                http_client=http_client,
                built_requests=built_requests,
                source_call_counts=source_call_counts,
                source_modes=source_modes,
                fallback_reasons=fallback_reasons,
            )
        date_disclosures = _collect_opendart_disclosures_by_date(
            sources=sources,
            start=start,
            end=config.as_of_date,
            as_of_date=config.as_of_date,
            config=config,
            http_client=http_client,
            built_requests=built_requests,
            source_call_counts=source_call_counts,
            source_modes=source_modes,
            fallback_reasons=fallback_reasons,
        )
        planned_opendart_detail_requests = plan_opendart_detail_fetches(date_disclosures, config.as_of_date)
        detail_disclosures, executed_opendart_detail_requests = _execute_opendart_detail_fetches(
            base_disclosures=date_disclosures,
            planned_requests=planned_opendart_detail_requests,
            as_of_date=config.as_of_date,
            config=config,
            http_client=http_client,
            built_requests=built_requests,
            source_call_counts=source_call_counts,
        )
        all_date_disclosures = _merge_detail_disclosures(date_disclosures, detail_disclosures)
        scan_sources = _sources_with_date_disclosures(sources, all_date_disclosures)
        if targeted_only_research:
            cheap_scan = _targeted_only_empty_cheap_scan(config)
        else:
            cheap_scan = KoreaCheapScanner(scan_sources).run(
                KoreaCheapScanConfig(
                    as_of_date=config.as_of_date,
                    markets=(Market.KR,),
                    sources=scan_sources,
                    universe_limit=config.universe_limit,
                    lookback_days=config.lookback_days,
                    disclosure_lookback_days=config.disclosure_lookback_days,
                    top_n=config.top_candidates,
                    event_search_min_score=config.event_search_min_score,
                    deep_research_min_score=config.deep_research_min_score,
                    price_only_event_allowed=config.price_only_event_allowed,
                    report_radar_enabled=config.report_radar_enabled,
                )
            )
            _record_estimated_source_calls(source_call_counts, sources, cheap_scan.instruments_scanned, source_modes)
        cheap_evidence = _cheap_scan_evidence_by_id(sources, all_date_disclosures, config.as_of_date)
        instruments = _instruments_from_scan_sources(scan_sources, config.as_of_date, config.universe_limit)
        free_search_provider = _free_search_provider(config, http_client, source_modes, fallback_reasons)
        radar_candidates = (
            ()
            if targeted_only_research
            else _run_report_radar(
                config=config,
                instruments=instruments,
                free_search_provider=free_search_provider,
                remaining_queries=_remaining_naver_queries(config, source_call_counts["naver_search_queries"]),
            )
        )
        if not targeted_only_research:
            source_call_counts["naver_search_queries"] += _estimate_radar_queries(config, instruments, radar_candidates)
        top_trading_value_probe_rows = () if targeted_only_research else _top_trading_value_probe_rows(config, scan_sources, instruments)
        top_trading_value_probe_candidates = _top_trading_value_probe_candidates(config, top_trading_value_probe_rows)
        merged_candidates = _merge_candidates(
            cheap_scan.candidates,
            tuple(item.to_cheap_scan_candidate() for item in radar_candidates),
            smoke_candidates,
            top_trading_value_probe_candidates,
        )
        production_candidates = tuple(candidate for candidate in merged_candidates if candidate.production_candidate)
        selected_candidates, skipped_candidate_items = _select_candidates_for_research(
            merged_candidates,
            config.budget,
            targeted_smoke_only=config.targeted_smoke_only,
        )
        selected_opendart_corp_codes = _opendart_corp_codes_for_candidates(
            candidates=selected_candidates,
            sources=sources,
            existing_disclosures=all_date_disclosures,
            config=config,
            http_client=http_client,
            built_requests=built_requests,
            source_call_counts=source_call_counts,
        )
        selected_symbol_disclosures = _execute_opendart_disclosures_for_candidates(
            candidates=selected_candidates,
            sources=sources,
            corp_codes=selected_opendart_corp_codes,
            config=config,
            http_client=http_client,
            built_requests=built_requests,
            source_call_counts=source_call_counts,
        )
        if selected_symbol_disclosures:
            all_date_disclosures = _merge_detail_disclosures(all_date_disclosures, selected_symbol_disclosures)
            scan_sources = _sources_with_date_disclosures(sources, all_date_disclosures)
            cheap_evidence.update(_cheap_scan_evidence_by_id(sources, selected_symbol_disclosures, config.as_of_date))
        live_financial_actuals = _execute_data_go_kr_financial_actuals_for_candidates(
            candidates=selected_candidates,
            sources=scan_sources,
            instruments=instruments,
            config=config,
            http_client=http_client,
            built_requests=built_requests,
            source_call_counts=source_call_counts,
        )
        opendart_financial_actuals = _execute_opendart_single_account_actuals_for_candidates(
            candidates=selected_candidates,
            sources=sources,
            date_disclosures=all_date_disclosures,
            candidate_corp_codes=selected_opendart_corp_codes,
            config=config,
            http_client=http_client,
            built_requests=built_requests,
            source_call_counts=source_call_counts,
        )
        company_guide_data = _execute_company_guide_for_candidates(
            candidates=selected_candidates,
            config=config,
            effective_fixture_mode=effective_fixture_mode,
            http_client=http_client,
            built_requests=built_requests,
            source_call_counts=source_call_counts,
            source_modes=source_modes,
            fallback_reasons=fallback_reasons,
        )
        base_feature_inputs = {
            candidate.symbol: base_input
            for candidate in selected_candidates
            if (
                base_input := _base_feature_input_for_candidate(
                    candidate=candidate,
                    sources=scan_sources,
                    instruments=instruments,
                    config=config,
                    extra_financial_actuals=_dedupe_financial_actuals(
                        tuple(live_financial_actuals.get(candidate.symbol, ()))
                        + tuple(opendart_financial_actuals.get(candidate.symbol, ()))
                    ),
                    extra_consensus=company_guide_data.get(candidate.symbol, _EMPTY_COMPANY_GUIDE_FEATURE_DATA).consensus,
                    extra_consensus_revisions=company_guide_data.get(
                        candidate.symbol, _EMPTY_COMPANY_GUIDE_FEATURE_DATA
                    ).consensus_revisions,
                    extra_research_reports=company_guide_data.get(candidate.symbol, _EMPTY_COMPANY_GUIDE_FEATURE_DATA).research_reports,
                )
            )
            is not None
        }
        base_evidence_by_symbol = {
            symbol: evidence_from_feature_domains(
                market=Market.KR,
                fallback_symbol=symbol,
                financial_actuals=base_input.financial_actuals,
                consensus=base_input.consensus,
                consensus_revisions=base_input.consensus_revisions,
                disclosures=base_input.disclosures,
                research_reports=base_input.research_reports,
                news_items=base_input.news_items,
            )
            for symbol, base_input in base_feature_inputs.items()
        }

        web_results: list[WebResearchPipelineResult] = []
        production_web_results: list[WebResearchPipelineResult] = []
        targeted_smoke_results: list[Mapping[str, Any]] = []
        skipped_candidates = list(skipped_candidate_items)
        skipped_queries: list[Mapping[str, Any]] = []
        dropped_results: list[Mapping[str, Any]] = []
        theme_routes: list[Mapping[str, Any]] = []
        theme_expansion_queries: list[Mapping[str, Any]] = []
        theme_missing_slots: list[Mapping[str, Any]] = []
        theme_route_status_counts: Counter[str] = Counter()
        theme_route_provider = config.theme_route_provider
        if theme_route_provider is None and config.theme_rebalance_enabled:
            theme_route_provider = build_theme_route_provider_from_env(working_directory=Path.cwd())
        if theme_route_provider is None and _should_default_to_codex_theme_provider(config, effective_fixture_mode=effective_fixture_mode):
            theme_route_provider = build_default_codex_theme_route_provider(working_directory=Path.cwd())
        phase_log_path = _prepare_phase_log(config)
        phase_event_sink = _phase_event_sink(phase_log_path)
        for candidate in selected_candidates:
            remaining_queries = _remaining_naver_queries(config, source_call_counts["naver_search_queries"])
            if remaining_queries is not None and remaining_queries <= 0:
                skipped_candidates.append(_skip(candidate, "naver_search_budget_exhausted"))
                continue
            runner = FreeWebResearchRunner(
                browser_provider=config.browser_provider or EmptySearchProvider(),
                free_search_provider=free_search_provider,
                query_planner=_query_planner_for_candidate(candidate, config),
            )
            result = runner.run(
                FreeWebResearchInput(
                    company_name=candidate.company_name,
                    symbol=candidate.symbol,
                    sector=None,
                    market=candidate.market,
                    as_of_date=candidate.as_of_date,
                    company_aliases=(candidate.company_name, candidate.symbol),
                    candidate_reason_codes=candidate.reason_codes,
                    budget=_search_budget(
                        config.budget,
                        remaining_queries,
                    ),
                    max_results_per_query=config.max_results_per_query,
                    top_results=config.top_results,
                    fixture_text_by_url=config.fixture_text_by_url,
                    live_page_fetch_enabled=_live_page_fetch_enabled(config),
                    page_fetch_timeout_seconds=config.page_fetch_timeout_seconds,
                    page_fetch_cache_directory=_page_fetch_cache_directory(config),
                    theme_rebalance_enabled=config.theme_rebalance_enabled,
                    theme_route_provider=theme_route_provider,
                    max_theme_expansion_rounds=config.max_theme_expansion_rounds,
                    max_score_gap_expansion_rounds=config.max_score_gap_expansion_rounds,
                    theme_route_search_result_limit=config.theme_route_search_result_limit,
                    theme_route_document_limit=config.theme_route_document_limit,
                    theme_route_document_excerpt_chars=config.theme_route_document_excerpt_chars,
                    post_parse_gap_expansion_max_queries=config.post_parse_gap_expansion_max_queries,
                    score_gap_query_retry_max=config.score_gap_query_retry_max,
                    theme_evidence_review_enabled=config.theme_evidence_review_enabled,
                    base_feature_input=base_feature_inputs.get(candidate.symbol),
                    phase_event_sink=phase_event_sink,
                )
            )
            source_call_counts["naver_search_queries"] += result.budget_tracker.total_queries_used
            combined_evidence = tuple(cheap_evidence.get(evidence_id) for evidence_id in candidate.evidence_ids)
            combined_evidence = (
                tuple(item for item in combined_evidence if item is not None)
                + tuple(base_evidence_by_symbol.get(candidate.symbol, ()))
                + tuple(result.web_result.evidence)
            )
            result = _enforce_cross_evidence_stage3_green(result, combined_evidence, config)
            web_results.append(result)
            if candidate.production_candidate:
                production_web_results.append(result)
            else:
                targeted_smoke_results.append(_targeted_smoke_result_row(candidate, result, combined_evidence))
            skipped_queries.extend(_skipped_query_rows(candidate, result))
            dropped_results.extend(_dropped_result_rows(candidate, result))
            theme_routes.append(_theme_route_row(candidate, result))
            theme_expansion_queries.extend(_theme_expansion_query_rows(candidate, result))
            theme_missing_slots.extend(_theme_missing_slot_rows(candidate, result))
            theme_route_status_counts.update([str(result.theme_route_diagnostics.get("theme_rebalance_status") or "disabled")])

        evidence = _dedupe_evidence(
            tuple(cheap_evidence.values())
            + tuple(item for items in base_evidence_by_symbol.values() for item in items)
            + tuple(item for result in web_results for item in result.web_result.evidence)
        )
        audit_findings = audit_parser_outputs(
            evidence=evidence,
            scores=tuple(result.score for result in production_web_results),
            stages=tuple(result.stage for result in production_web_results),
        )
        web_results = [_enforce_parser_audit_stage3_green(result, audit_findings) for result in web_results]
        production_web_results = [result for candidate, result in zip(selected_candidates, web_results) if candidate.production_candidate]
        scores = tuple(result.score for result in production_web_results)
        stages = tuple(result.stage for result in production_web_results)
        findings = tuple(finding for result in production_web_results for finding in result.red_team_findings)
        morning_brief = generate_morning_briefing(
            as_of_date=config.as_of_date,
            instruments=instruments,
            scores=scores,
            stages=stages,
            red_team_findings=findings,
            evidence=evidence,
        )
        run_log = KoreaLiveLiteRunLog(
            as_of_date=config.as_of_date,
            fixture_mode=config.fixture_mode,
            live_enabled=config.live_enabled,
            effective_fixture_mode=effective_fixture_mode,
            missing_credentials=missing_credentials,
            source_call_counts=dict(source_call_counts),
            built_requests=tuple(built_requests),
            skipped_candidates=tuple(skipped_candidates),
            skipped_queries=tuple(skipped_queries),
            dropped_search_results=tuple(dropped_results),
            source_modes=dict(source_modes),
            live_requests_executed=http_client.stats.live_requests_executed,
            live_requests_failed=http_client.stats.live_requests_failed,
            cache_hits=http_client.stats.cache_hits,
            cache_writes=http_client.stats.cache_writes,
            fallback_reasons=dict(fallback_reasons),
            request_only_sources=tuple(source for source, mode in source_modes.items() if mode == "request_only"),
            audit_findings=tuple(audit_findings),
            planned_opendart_detail_requests=tuple(planned_opendart_detail_requests),
            executed_opendart_detail_requests=tuple(executed_opendart_detail_requests),
            opendart_detail_evidence_ids=tuple(OpenDARTConnector.to_evidence(item, Market.KR).evidence_id for item in detail_disclosures),
            report_radar_candidates=tuple(_report_radar_row(item) for item in radar_candidates),
            targeted_smoke_results=tuple(targeted_smoke_results),
            top_trading_value_probe_candidates=tuple(top_trading_value_probe_rows),
            theme_routes=tuple(theme_routes),
            theme_expansion_queries=tuple(theme_expansion_queries),
            theme_missing_slots=tuple(theme_missing_slots),
            theme_route_status_counts=dict(theme_route_status_counts),
            audit_summary=_audit_summary(audit_findings, evidence),
            score_state_contract_findings=_score_state_contract_findings_for_outputs(
                as_of_date=config.as_of_date,
                candidates=production_candidates,
                targeted_smoke_results=targeted_smoke_results,
            ),
            rate_limit_waits=http_client.stats.rate_limit_waits,
            rate_limit_skips=http_client.stats.rate_limit_skips,
            actual_http_requests_by_source=dict(http_client.stats.actual_http_requests_by_source),
            logical_queries_by_source=_logical_queries_by_source(source_call_counts, http_client.stats),
            max_concurrency_used_by_source=dict(http_client.stats.max_concurrency_used_by_source),
            live_smoke_preset_used=config.live_smoke_preset_used,
            source_license_metadata=DEFAULT_SOURCE_LICENSE_METADATA,
            phase_log_path=str(phase_log_path) if phase_log_path is not None else None,
            notes=_run_notes(config, effective_fixture_mode) + _audit_notes(audit_findings),
        )
        candidates_path, evidence_path, brief_path, run_log_path = _write_outputs(
            config=config,
            cheap_scan=cheap_scan,
            candidates=production_candidates,
            evidence=evidence,
            morning_brief=morning_brief,
            run_log=run_log,
        )
        calibration_json_path, calibration_md_path = _write_calibration_outputs(config, cheap_scan)
        return KoreaLiveLiteResult(
            as_of_date=config.as_of_date,
            cheap_scan=cheap_scan,
            candidates=production_candidates,
            web_results=tuple(web_results),
            scores=scores,
            stages=stages,
            evidence=evidence,
            red_team_findings=findings,
            morning_brief=morning_brief,
            candidates_path=candidates_path,
            evidence_path=evidence_path,
            brief_path=brief_path,
            run_log_path=run_log_path,
            calibration_json_path=calibration_json_path,
            calibration_md_path=calibration_md_path,
            run_log=run_log,
            phase_log_path=phase_log_path,
        )


def fixture_sources(root: str | Path = DEFAULT_FIXTURE_ROOT) -> KoreaCheapScanSources:
    """Return Korea cheap-scan sources pointed at Checkpoint 13 fixtures."""

    root_path = Path(root)
    return KoreaCheapScanSources(
        krx=KRXConnector(fixture_root=root_path / "krx"),
        opendart=OpenDARTConnector(fixture_root=root_path / "opendart"),
        kind=KINDConnector(fixture_root=root_path / "kind"),
        fsc=DataGoKrFSCConnector(fixture_root=root_path / "data_go_kr_fsc"),
    )


def _sources_with_stock_issuance_setting(
    sources: KoreaCheapScanSources,
    enabled: bool,
) -> KoreaCheapScanSources:
    if sources.fsc is None:
        return sources
    return KoreaCheapScanSources(
        krx=sources.krx,
        opendart=sources.opendart,
        kind=sources.kind,
        fsc=replace(sources.fsc, enable_stock_issuance_source=enabled),
    )


def _stock_issuance_source_mode(config: KoreaLiveLiteConfig) -> str:
    return "not_configured" if config.enable_stock_issuance_source else "disabled_optional"


def _default_theme_rebalance_enabled(config: KoreaLiveLiteConfig) -> bool:
    return bool(
        config.theme_route_provider is not None
        or os.environ.get("E2R_THEME_ROUTE_PROVIDER")
        or (config.live_enabled and not config.fixture_mode)
    )


def _should_default_to_codex_theme_provider(config: KoreaLiveLiteConfig, *, effective_fixture_mode: bool) -> bool:
    return bool(config.theme_rebalance_enabled and config.live_enabled and not effective_fixture_mode)


def _krx_openapi_source_mode(config: KoreaLiveLiteConfig) -> str:
    if not config.enable_krx_openapi_source:
        return "disabled_optional"
    if config.fixture_mode or not config.live_enabled:
        return "fixture"
    if not os.environ.get("KRX_OPENAPI_KEY"):
        return "fallback"
    return "request_only"


def _rate_limiter_for_config(config: KoreaLiveLiteConfig) -> RateLimiter:
    return RateLimiter(
        (
            SourceRateLimit(
                source_name="opendart",
                max_requests_per_day=config.budget.max_opendart_calls_per_day,
                max_requests_per_second=5.0,
                min_interval_seconds=0.2,
                max_concurrency=1,
            ),
            SourceRateLimit(
                source_name="naver_search",
                max_requests_per_day=config.budget.max_naver_search_calls_per_day,
                max_requests_per_second=3.0,
                min_interval_seconds=0.3,
                max_concurrency=1,
            ),
            SourceRateLimit(
                source_name="company_guide",
                max_requests_per_day=config.budget.max_company_guide_calls_per_day,
                max_requests_per_second=1.0,
                min_interval_seconds=1.0,
                max_concurrency=1,
            ),
            SourceRateLimit(
                source_name="data_go_kr",
                max_requests_per_day=config.budget.max_data_go_kr_calls_per_day,
                max_requests_per_second=5.0,
                min_interval_seconds=0.2,
                max_concurrency=1,
            ),
            SourceRateLimit(
                source_name="krx",
                max_requests_per_day=config.budget.max_krx_calls_per_day,
                max_requests_per_second=5.0,
                min_interval_seconds=0.2,
                max_concurrency=1,
            ),
        )
    )


def _sources_with_live_data_go_kr(
    *,
    sources: KoreaCheapScanSources,
    config: KoreaLiveLiteConfig,
    http_client: HttpClient,
    built_requests: list[SourceRequest],
    source_call_counts: dict[str, int],
    source_modes: dict[str, str],
    fallback_reasons: dict[str, str],
) -> KoreaCheapScanSources:
    if not _can_execute_live_data_go_kr(config) or sources.fsc is None:
        return sources
    data_go_cap = config.budget.max_data_go_kr_calls_per_day
    if data_go_cap is not None and data_go_cap < 2:
        source_modes["data_go_kr"] = "fallback"
        fallback_reasons["data_go_kr"] = "data_go_kr_budget_too_low_for_universe_and_price"
        return sources

    financial_reserve = _data_go_kr_financial_actual_call_reserve(config)
    remaining_calls = _remaining_from_cap(data_go_cap, financial_reserve)
    if remaining_calls is not None and remaining_calls < 2:
        source_modes["data_go_kr"] = "fallback"
        fallback_reasons["data_go_kr"] = "data_go_kr_budget_too_low_after_financial_reserve"
        return sources
    instruments, remaining_calls, instruments_ok, instruments_reason = _execute_data_go_kr_listed_items_with_lookback(
        sources=sources,
        config=config,
        http_client=http_client,
        built_requests=built_requests,
        source_call_counts=source_call_counts,
        remaining_calls=remaining_calls,
    )
    if not instruments_ok:
        source_modes["data_go_kr"] = "fallback"
        fallback_reasons["data_go_kr"] = instruments_reason
        return sources

    price_start = config.as_of_date - timedelta(days=config.lookback_days)
    price_bars, remaining_calls, prices_ok = _execute_data_go_kr_pages(
        request_factory=lambda page_no, num_rows: sources.fsc.build_stock_price_page_request(price_start, config.as_of_date, config.as_of_date, page_no, num_rows),
        parser=lambda rows: tuple(sources.fsc.normalize_price_bar(row) for row in rows),
        cache_stem="stock_prices",
        as_of_date=config.as_of_date,
        config=config,
        http_client=http_client,
        built_requests=built_requests,
        source_call_counts=source_call_counts,
        remaining_calls=remaining_calls,
    )
    if not prices_ok:
        source_modes["data_go_kr"] = "fallback"
        fallback_reasons["data_go_kr"] = "data_go_kr_stock_prices_failed"
        return sources

    source_modes["data_go_kr"] = "live_executed"
    return KoreaCheapScanSources(
        # Once data.go.kr supplies both live universe and price rows, avoid
        # mixing KRX fixture prices into the same scan.
        krx=None,
        opendart=sources.opendart,
        kind=sources.kind,
        fsc=_LiveDataGoKrFSCConnector(
            base=sources.fsc,
            instruments=tuple(instruments),
            price_bars=tuple(price_bars),
        ),
    )


def _sources_with_targeted_live_data_go_kr(
    *,
    sources: KoreaCheapScanSources,
    config: KoreaLiveLiteConfig,
    candidates: Sequence[CheapScanCandidate],
    http_client: HttpClient,
    built_requests: list[SourceRequest],
    source_call_counts: dict[str, int],
    source_modes: dict[str, str],
    fallback_reasons: dict[str, str],
) -> KoreaCheapScanSources:
    if not candidates or not _can_execute_live_data_go_kr(config) or sources.fsc is None:
        return sources
    unique_candidates = _unique_candidates_by_symbol(candidates)
    financial_reserve = _data_go_kr_financial_actual_call_reserve(config)
    remaining_calls = _remaining_from_cap(config.budget.max_data_go_kr_calls_per_day, financial_reserve)
    if remaining_calls is not None and remaining_calls < len(unique_candidates):
        source_modes["data_go_kr"] = "fallback"
        fallback_reasons["data_go_kr"] = "data_go_kr_budget_too_low_for_targeted_prices"
        return sources

    price_start = config.as_of_date - timedelta(days=config.lookback_days)
    instruments: list[Instrument] = []
    price_bars: list[PriceBar] = []
    any_success = False
    last_error: str | None = None
    for candidate in unique_candidates:
        if not _has_remaining_calls(remaining_calls):
            break
        public_request = _data_go_public_request(
            _with_source_request_params(
                sources.fsc.build_stock_price_request(
                    candidate.symbol,
                    price_start,
                    config.as_of_date,
                    config.as_of_date,
                ),
                {"numOfRows": 1000},
            )
        )
        built_requests.append(public_request)
        live_request = _with_secret_param(public_request, "serviceKey", os.environ["DATA_GO_KR_SERVICE_KEY"])
        cache_path = (
            Path(config.cache_directory)
            / "data_go_kr"
            / config.as_of_date.isoformat()
            / f"targeted_stock_prices_{_safe_filename(candidate.symbol)}.json"
        )
        result = http_client.get_json(live_request, cache_path=cache_path)
        source_call_counts["data_go_kr_calls"] += 1
        remaining_calls = _consume_remaining_call(remaining_calls)
        if not result.ok or not isinstance(result.json_data, Mapping):
            last_error = result.error or "data_go_kr_targeted_stock_prices_failed"
            continue
        try:
            candidate_bars = tuple(sources.fsc.normalize_price_bar(row) for row in _data_go_kr_payload_items(result.json_data))
        except (KeyError, TypeError, ValueError) as exc:
            last_error = f"data_go_kr_targeted_stock_prices_parse_failed:{type(exc).__name__}"
            continue
        candidate_bars = tuple(item for item in candidate_bars if item.symbol == candidate.symbol)
        price_bars.extend(candidate_bars)
        instruments.append(_targeted_candidate_instrument(candidate))
        any_success = True

    if not any_success:
        source_modes["data_go_kr"] = "fallback"
        fallback_reasons["data_go_kr"] = last_error or "data_go_kr_targeted_stock_prices_empty"
        return sources
    source_modes["data_go_kr"] = "live_targeted"
    return KoreaCheapScanSources(
        krx=None,
        opendart=sources.opendart,
        kind=sources.kind,
        fsc=_LiveDataGoKrFSCConnector(
            base=sources.fsc,
            instruments=tuple(dict.fromkeys(instruments)),
            price_bars=tuple(price_bars),
        ),
    )


def _unique_candidates_by_symbol(candidates: Sequence[CheapScanCandidate]) -> tuple[CheapScanCandidate, ...]:
    unique: dict[str, CheapScanCandidate] = {}
    for candidate in candidates:
        unique.setdefault(candidate.symbol, candidate)
    return tuple(unique.values())


def _with_source_request_params(request: SourceRequest, params: Mapping[str, Any]) -> SourceRequest:
    merged = dict(request.params)
    merged.update(params)
    return SourceRequest(
        method=request.method,
        url=request.url,
        params=merged,
        headers=dict(request.headers),
        fixture_mode=request.fixture_mode,
        credential_name=request.credential_name,
    )


def _targeted_candidate_instrument(candidate: CheapScanCandidate) -> Instrument:
    return Instrument(
        symbol=candidate.symbol,
        name=candidate.company_name,
        market=candidate.market,
        exchange="KR",
    )


def _targeted_only_research_mode(config: KoreaLiveLiteConfig) -> bool:
    return bool(config.targeted_smoke_only and config.targeted_smoke_enabled)


def _targeted_only_empty_cheap_scan(config: KoreaLiveLiteConfig) -> KoreaCheapScanResult:
    return KoreaCheapScanResult(
        as_of_date=config.as_of_date,
        candidates=(),
        instruments_scanned=0,
        diagnostics=(),
        calibration=None,
    )


def _execute_data_go_kr_listed_items_with_lookback(
    *,
    sources: KoreaCheapScanSources,
    config: KoreaLiveLiteConfig,
    http_client: HttpClient,
    built_requests: list[SourceRequest],
    source_call_counts: dict[str, int],
    remaining_calls: int | None,
):
    """Fetch listed-item rows, retrying recent settled dates when today is empty."""

    if sources.fsc is None:
        return (), remaining_calls, False, "data_go_kr_fsc_not_configured"
    last_reason = "data_go_kr_listed_items_empty"
    max_lookback_days = 5 if remaining_calls is None else min(5, max(0, remaining_calls - 1))
    for days_back in range(max_lookback_days + 1):
        listed_date = config.as_of_date - timedelta(days=days_back)
        instruments, remaining_calls, ok = _execute_data_go_kr_pages(
            request_factory=lambda page_no, num_rows, listed_date=listed_date: sources.fsc.build_listed_items_page_request(Market.KR, listed_date, page_no, num_rows),
            parser=lambda rows: tuple(sources.fsc.normalize_instrument(row) for row in rows),
            cache_stem=f"listed_items_{listed_date.strftime('%Y%m%d')}",
            as_of_date=config.as_of_date,
            config=config,
            http_client=http_client,
            built_requests=built_requests,
            source_call_counts=source_call_counts,
            remaining_calls=remaining_calls,
        )
        if not ok:
            return (), remaining_calls, False, "data_go_kr_listed_items_failed"
        if instruments:
            return instruments, remaining_calls, True, ""
        last_reason = f"data_go_kr_listed_items_empty_{listed_date.strftime('%Y%m%d')}"
        if remaining_calls is not None and remaining_calls <= 1:
            break
    return (), remaining_calls, False, last_reason


def _can_execute_live_data_go_kr(config: KoreaLiveLiteConfig) -> bool:
    return bool(config.live_enabled and not config.fixture_mode and os.environ.get("DATA_GO_KR_SERVICE_KEY"))


def _remaining_from_cap(cap: int | None, used: int = 0) -> int | None:
    return None if cap is None else max(0, cap - used)


def _has_remaining_calls(remaining_calls: int | None) -> bool:
    return remaining_calls is None or remaining_calls > 0


def _consume_remaining_call(remaining_calls: int | None) -> int | None:
    return None if remaining_calls is None else max(0, remaining_calls - 1)


def _data_go_kr_financial_actual_call_reserve(config: KoreaLiveLiteConfig) -> int:
    years = len(_candidate_financial_years(config.as_of_date))
    if years <= 0:
        return 0
    selected_symbol_cap = _selected_candidate_symbol_cap(config)
    if selected_symbol_cap is not None:
        if config.targeted_smoke_enabled:
            selected_symbol_cap += 1
        if config.top_trading_value_probe_enabled:
            selected_symbol_cap += config.top_trading_value_probe_count
    if selected_symbol_cap is not None and selected_symbol_cap <= 0:
        return 0
    requested = years * min(selected_symbol_cap if selected_symbol_cap is not None else 30, 30)
    data_go_cap = config.budget.max_data_go_kr_calls_per_day
    return requested if data_go_cap is None else min(requested, max(0, data_go_cap - 2))


def _execute_data_go_kr_pages(
    *,
    request_factory,
    parser,
    cache_stem: str,
    as_of_date: date,
    config: KoreaLiveLiteConfig,
    http_client: HttpClient,
    built_requests: list[SourceRequest],
    source_call_counts: dict[str, int],
    remaining_calls: int | None,
):
    if not _has_remaining_calls(remaining_calls):
        return (), 0, False
    parsed_items: list[Any] = []
    page_no = 1
    num_rows = 1000
    while _has_remaining_calls(remaining_calls):
        public_request = _data_go_public_request(request_factory(page_no, num_rows))
        built_requests.append(public_request)
        live_request = _with_secret_param(public_request, "serviceKey", os.environ["DATA_GO_KR_SERVICE_KEY"])
        cache_path = Path(config.cache_directory) / "data_go_kr" / as_of_date.isoformat() / f"{cache_stem}_page_{page_no:04d}.json"
        result = http_client.get_json(live_request, cache_path=cache_path)
        source_call_counts["data_go_kr_calls"] += 1
        remaining_calls = _consume_remaining_call(remaining_calls)
        if not result.ok or not isinstance(result.json_data, Mapping):
            return (), remaining_calls, False
        payload = result.json_data
        rows = _data_go_kr_payload_items(payload)
        try:
            parsed_items.extend(parser(rows))
        except (KeyError, TypeError, ValueError):
            return (), remaining_calls, False
        total_pages = _data_go_kr_total_pages(payload, num_rows, page_no)
        if page_no >= total_pages:
            return tuple(parsed_items), remaining_calls, True
        page_no += 1
    return tuple(parsed_items), remaining_calls, True


def _data_go_public_request(request: SourceRequest) -> SourceRequest:
    params = {key: value for key, value in request.params.items() if key != "serviceKey"}
    return SourceRequest(
        method=request.method,
        url=request.url,
        params=params,
        headers=dict(request.headers),
        fixture_mode=False,
        credential_name="DATA_GO_KR_SERVICE_KEY",
    )


def _data_go_kr_payload_items(payload: Mapping[str, Any]) -> tuple[Mapping[str, Any], ...]:
    response = payload.get("response", payload)
    body = response.get("body", response) if isinstance(response, Mapping) else {}
    items = body.get("items", ()) if isinstance(body, Mapping) else ()
    if isinstance(items, Mapping):
        rows = items.get("item", ())
    else:
        rows = items
    if isinstance(rows, Mapping):
        rows = (rows,)
    if not isinstance(rows, Sequence) or isinstance(rows, (str, bytes)):
        return ()
    return tuple(row for row in rows if isinstance(row, Mapping))


def _data_go_kr_total_pages(payload: Mapping[str, Any], num_rows: int, default: int) -> int:
    response = payload.get("response", payload)
    body = response.get("body", response) if isinstance(response, Mapping) else {}
    if not isinstance(body, Mapping):
        return default
    total_count = _int_or_default(body.get("totalCount") or body.get("total_count"), 0)
    rows = _int_or_default(body.get("numOfRows") or body.get("num_of_rows"), num_rows)
    if total_count <= 0 or rows <= 0:
        return default
    return max(1, (total_count + rows - 1) // rows)


@dataclass(frozen=True)
class _LiveDataGoKrFSCConnector:
    base: DataGoKrFSCConnector
    instruments: tuple[Instrument, ...]
    price_bars: tuple[PriceBar, ...]
    _price_bars_by_symbol: Mapping[str, tuple[PriceBar, ...]] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        by_symbol: dict[str, list[PriceBar]] = {}
        for item in self.price_bars:
            by_symbol.setdefault(item.symbol, []).append(item)
        object.__setattr__(
            self,
            "_price_bars_by_symbol",
            {symbol: tuple(sorted(items, key=lambda row: row.date)) for symbol, items in by_symbol.items()},
        )

    def list_instruments(self, market: Market, as_of_date: date) -> tuple[Instrument, ...]:
        return tuple(
            sorted(
                (
                    item
                    for item in self.instruments
                    if item.market == market
                    and (item.listed_date is None or item.listed_date <= as_of_date)
                ),
                key=lambda item: item.symbol,
            )
        )

    def get_price_bars(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[PriceBar, ...]:
        bars = self._price_bars_by_symbol.get(symbol, ())
        return tuple(
            item
            for item in bars
            if start <= item.date <= end
            and item.date <= as_of_date
            and item.as_of_date <= as_of_date
        )

    def get_financial_actuals(self, symbol: str, as_of_date: date) -> tuple[FinancialActual, ...]:
        return self.base.get_financial_actuals(symbol, as_of_date)

    def get_disclosures(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[DisclosureEvent, ...]:
        return self.base.get_disclosures(symbol, start, end, as_of_date)

    def get_stock_issuance_records(self, symbol: str, as_of_date: date) -> tuple[dict[str, Any], ...]:
        return self.base.get_stock_issuance_records(symbol, as_of_date)


def _collect_opendart_disclosures_by_date(
    *,
    sources: KoreaCheapScanSources,
    start: date,
    end: date,
    as_of_date: date,
    config: KoreaLiveLiteConfig,
    http_client: HttpClient,
    built_requests: list[SourceRequest],
    source_call_counts: dict[str, int],
    source_modes: dict[str, str],
    fallback_reasons: dict[str, str],
) -> tuple[DisclosureEvent, ...]:
    """Preload OpenDART disclosures for the date window.

    This supports all-listed cheap scan without one OpenDART API call per
    symbol. The scanner still evaluates every listed instrument; per-symbol
    disclosure lookup later is only a local filter over this preloaded set.
    """

    if sources.opendart is None:
        return ()
    if _can_execute_live_opendart(config):
        live_disclosures = _execute_opendart_disclosure_pages(
            start=start,
            end=end,
            as_of_date=as_of_date,
            config=config,
            http_client=http_client,
            built_requests=built_requests,
            source_call_counts=source_call_counts,
            source_modes=source_modes,
            fallback_reasons=fallback_reasons,
        )
        if source_modes.get("opendart") == "live_executed":
            return live_disclosures
    else:
        requests = build_opendart_date_range_requests(start, end, as_of_date)
        built_requests.extend(requests)
        source_call_counts["opendart_disclosure_date_range"] += len(requests)
    rows = load_fixture_records(sources.opendart.fixture_root, "disclosures")
    disclosures = tuple(sources.opendart.normalize_disclosure(row) for row in rows)
    return tuple(
        sorted(
            (
                item
                for item in disclosures
                if start <= item.published_at.date() <= end
                and item.published_at.date() <= as_of_date
                and item.available_at.date() <= as_of_date
            ),
            key=lambda item: (item.symbol, item.published_at),
        )
    )


def _execute_opendart_disclosure_pages(
    *,
    start: date,
    end: date,
    as_of_date: date,
    config: KoreaLiveLiteConfig,
    http_client: HttpClient,
    built_requests: list[SourceRequest],
    source_call_counts: dict[str, int],
    source_modes: dict[str, str],
    fallback_reasons: dict[str, str],
) -> tuple[DisclosureEvent, ...]:
    page_count = 100
    max_pages = _opendart_disclosure_page_call_cap(config)
    disclosures: list[DisclosureEvent] = []
    page_no = 1
    while max_pages is None or page_no <= max_pages:
        public_request = _opendart_date_range_request(start, end, as_of_date, page_no=page_no, page_count=page_count, fixture_mode=False)
        built_requests.append(public_request)
        live_request = _with_secret_param(public_request, "crtfc_key", os.environ["OPENDART_API_KEY"])
        cache_path = Path(config.cache_directory) / "opendart" / as_of_date.isoformat() / f"list_page_{page_no:04d}.json"
        result = http_client.get_json(live_request, cache_path=cache_path)
        source_call_counts["opendart_disclosure_date_range"] += 1
        if not result.ok or not isinstance(result.json_data, Mapping):
            source_modes["opendart"] = "fallback"
            fallback_reasons["opendart"] = result.error or "opendart_live_request_failed"
            return ()
        payload = result.json_data
        source_modes["opendart"] = "live_executed"
        disclosures.extend(_opendart_payload_to_disclosures(payload, as_of_date))
        total_page = _int_or_default(payload.get("total_page") or payload.get("total_page_count"), page_no)
        if page_no >= total_page:
            break
        page_no += 1
    return tuple(
        sorted(
            (
                item
                for item in disclosures
                if start <= item.published_at.date() <= end
                and item.published_at.date() <= as_of_date
                and item.available_at.date() <= as_of_date
            ),
            key=lambda item: (item.symbol, item.published_at),
        )
    )


def _opendart_corp_codes_for_candidates(
    *,
    candidates: Sequence[CheapScanCandidate],
    sources: KoreaCheapScanSources,
    existing_disclosures: Sequence[DisclosureEvent],
    config: KoreaLiveLiteConfig,
    http_client: HttpClient,
    built_requests: list[SourceRequest],
    source_call_counts: dict[str, int],
) -> dict[str, str]:
    if not candidates or sources.opendart is None or not _can_execute_live_opendart(config):
        return {}
    corp_codes = _opendart_corp_codes_by_symbol(existing_disclosures)
    missing = tuple(
        candidate
        for candidate in _unique_candidates_by_symbol(candidates)
        if candidate.symbol not in corp_codes
    )
    if not missing:
        return dict(corp_codes)
    used_calls = (
        source_call_counts.get("opendart_disclosure_date_range", 0)
        + source_call_counts.get("opendart_detail_fetches", 0)
        + source_call_counts.get("opendart_symbol_disclosure_calls", 0)
        + source_call_counts.get("opendart_company_code_calls", 0)
        + source_call_counts.get("opendart_financial_statement_calls", 0)
    )
    remaining_calls = _remaining_from_cap(config.budget.max_opendart_calls_per_day, used_calls)
    corp_codes_from_map, _remaining_calls = _execute_opendart_company_code_lookup_for_candidates(
        candidates=missing,
        existing_corp_codes=corp_codes,
        sources=sources,
        config=config,
        http_client=http_client,
        built_requests=built_requests,
        source_call_counts=source_call_counts,
        remaining_calls=remaining_calls,
    )
    return {**corp_codes_from_map, **corp_codes}


def _execute_opendart_disclosures_for_candidates(
    *,
    candidates: Sequence[CheapScanCandidate],
    sources: KoreaCheapScanSources,
    corp_codes: Mapping[str, str],
    config: KoreaLiveLiteConfig,
    http_client: HttpClient,
    built_requests: list[SourceRequest],
    source_call_counts: dict[str, int],
) -> tuple[DisclosureEvent, ...]:
    """Fetch selected-candidate OpenDART list rows over the feature window.

    Date-range preloading is optimized for cheap-scan routing and may only
    cover a short market-wide window. Feature engineering needs the selected
    candidate's own recent filings, so this path uses the official corp code
    after candidate selection without adding symbol-specific scoring logic.
    """

    if not candidates or sources.opendart is None or not _can_execute_live_opendart(config):
        return ()
    if not hasattr(sources.opendart, "build_disclosure_search_request"):
        return ()
    used_calls = (
        source_call_counts.get("opendart_disclosure_date_range", 0)
        + source_call_counts.get("opendart_detail_fetches", 0)
        + source_call_counts.get("opendart_symbol_disclosure_calls", 0)
        + source_call_counts.get("opendart_company_code_calls", 0)
        + source_call_counts.get("opendart_financial_statement_calls", 0)
    )
    remaining_calls = _remaining_from_cap(config.budget.max_opendart_calls_per_day, used_calls)
    if not _has_remaining_calls(remaining_calls):
        return ()
    if (
        config.budget.max_opendart_calls_per_day is not None
        and remaining_calls <= _opendart_financial_statement_call_reserve(config)
    ):
        return ()
    if not corp_codes:
        return ()

    start = config.as_of_date - timedelta(days=max(config.disclosure_lookback_days, 30))
    fetched: list[DisclosureEvent] = []
    seen_symbols: set[str] = set()
    for candidate in candidates:
        if candidate.symbol in seen_symbols:
            continue
        seen_symbols.add(candidate.symbol)
        corp_code = corp_codes.get(candidate.symbol)
        if not corp_code or not _has_remaining_calls(remaining_calls):
            continue
        raw_request = sources.opendart.build_disclosure_search_request(
            corp_code,
            start,
            config.as_of_date,
            config.as_of_date,
        )
        public_request = SourceRequest(
            method=raw_request.method,
            url=raw_request.url,
            params={key: value for key, value in raw_request.params.items() if key != "crtfc_key"},
            headers=dict(raw_request.headers),
            fixture_mode=False,
            credential_name=raw_request.credential_name,
        )
        built_requests.append(public_request)
        live_request = _with_secret_param(public_request, "crtfc_key", os.environ["OPENDART_API_KEY"])
        cache_path = (
            Path(config.cache_directory)
            / "opendart_symbol_disclosures"
            / config.as_of_date.isoformat()
            / f"{_safe_filename(candidate.symbol)}_{_safe_filename(corp_code)}.json"
        )
        result = http_client.get_json(live_request, cache_path=cache_path)
        source_call_counts["opendart_symbol_disclosure_calls"] += 1
        remaining_calls = _consume_remaining_call(remaining_calls)
        if not result.ok or not isinstance(result.json_data, Mapping):
            continue
        for item in _opendart_payload_to_disclosures(result.json_data, config.as_of_date):
            if item.symbol not in {candidate.symbol, corp_code}:
                continue
            normalized = replace(item, symbol=candidate.symbol) if item.symbol != candidate.symbol else item
            if start <= normalized.published_at.date() <= config.as_of_date and normalized.available_at.date() <= config.as_of_date:
                fetched.append(normalized)
    return tuple(sorted(fetched, key=lambda item: (item.symbol, item.published_at, item.rcept_no or "")))


def _opendart_disclosure_page_call_cap(config: KoreaLiveLiteConfig) -> int | None:
    """Keep OpenDART budget for selected-candidate financial actuals.

    Date-range disclosure search can have hundreds of pages on active days.
    If it consumes the whole OpenDART budget first, selected candidates lose
    the official financial-statement evidence needed for EPS/FCF scoring.
    """

    if config.budget.max_opendart_calls_per_day is None:
        return None
    total_budget = max(1, config.budget.max_opendart_calls_per_day)
    detail_limit = config.budget.max_opendart_detail_fetches_per_run
    detail_reserve = min(
        max(0, detail_limit or 0),
        max(0, total_budget - 1),
    )
    financial_reserve = min(
        _opendart_financial_statement_call_reserve(config),
        max(0, total_budget - detail_reserve - 1),
    )
    return max(1, total_budget - detail_reserve - financial_reserve)


def _opendart_financial_statement_call_reserve(config: KoreaLiveLiteConfig) -> int:
    years = len(_opendart_financial_statement_periods(config.as_of_date))
    if years <= 0:
        return 0
    selected_symbol_cap = _selected_candidate_symbol_cap(config)
    if config.targeted_smoke_enabled:
        selected_symbol_cap += 1
    if config.top_trading_value_probe_enabled:
        selected_symbol_cap += config.top_trading_value_probe_count
    if selected_symbol_cap is not None and selected_symbol_cap <= 0:
        return 0
    # corpCode.xml은 선택 종목 전체가 공유하는 공식 식별자 조회다.
    # 재무 actual 경로가 최근 공시 존재 여부에 묶이지 않게 예약한다.
    return 1 + years * min(selected_symbol_cap if selected_symbol_cap is not None else 30, 30)


def _selected_candidate_symbol_cap(config: KoreaLiveLiteConfig) -> int | None:
    event_cap = config.budget.max_symbols_for_event_search
    deep_cap = config.budget.max_symbols_for_deep_research
    if event_cap is None or deep_cap is None:
        return config.top_candidates
    if config.top_candidates is None:
        return event_cap + deep_cap
    return min(config.top_candidates, event_cap + deep_cap)


def build_opendart_date_range_requests(
    start: date,
    end: date,
    as_of_date: date,
    page_count: int = 100,
    max_pages: int | None = None,
) -> tuple[SourceRequest, ...]:
    """Build paginated OpenDART date-range request metadata without network calls."""

    if page_count <= 0:
        raise ValueError("page_count must be positive")
    if max_pages is not None and max_pages <= 0:
        raise ValueError("max_pages must be positive when set")
    pages = range(1, (max_pages or 1) + 1)
    return tuple(_opendart_date_range_request(start, end, as_of_date, page_no=page_no, page_count=page_count) for page_no in pages)


OPENDART_DETAIL_WATCH_TYPES: tuple[str, ...] = (
    "단일판매·공급계약체결",
    "단일판매ㆍ공급계약체결",
    "신규시설투자",
    "잠정실적",
    "영업실적 전망",
    "유상증자",
    "전환사채",
    "신주인수권부사채",
    "감사의견",
    "거래정지",
    "계약 해지",
    "계약 취소",
    "계약 정정",
)


def plan_opendart_detail_fetches(
    disclosures: Sequence[DisclosureEvent],
    as_of_date: date,
) -> tuple[SourceRequest, ...]:
    """Plan detail fetch metadata for high-value OpenDART disclosures.

    The runner executes only a capped subset in live mode. All requests are
    still stored in ``run_log.json`` so operators can review exactly which
    receipt numbers were eligible for full-document parsing.
    """

    requests: dict[str, SourceRequest] = {}
    connector = OpenDARTConnector(api_key=None, fixture_mode=False)
    for disclosure in disclosures:
        if not disclosure.rcept_no or not _is_opendart_detail_watch(disclosure):
            continue
        request = connector.build_disclosure_detail_request(disclosure.rcept_no, as_of_date)
        params = dict(request.params)
        params["symbol"] = disclosure.symbol
        params["report_type"] = disclosure.report_type
        requests.setdefault(
            disclosure.rcept_no,
            SourceRequest(
                method=request.method,
                url=request.url,
                params=params,
                headers=dict(request.headers),
                fixture_mode=False,
                credential_name=request.credential_name,
            ),
        )
    return tuple(requests.values())


def _is_opendart_detail_watch(disclosure: DisclosureEvent) -> bool:
    watch_type = str(disclosure.parsed_fields.get("watch_type") or "")
    haystack = f"{disclosure.title} {disclosure.report_type} {watch_type}"
    return any(item in haystack for item in OPENDART_DETAIL_WATCH_TYPES)


def _opendart_date_range_request(
    start: date,
    end: date,
    as_of_date: date,
    *,
    page_no: int,
    page_count: int,
    fixture_mode: bool = True,
) -> SourceRequest:
    return SourceRequest(
        method="GET",
        url="https://opendart.fss.or.kr/api/list.json",
        params={
            "bgn_de": start.strftime("%Y%m%d"),
            "end_de": min(end, as_of_date).strftime("%Y%m%d"),
            "page_no": page_no,
            "page_count": page_count,
        },
        fixture_mode=fixture_mode,
        credential_name="OPENDART_API_KEY",
    )


def _can_execute_live_opendart(config: KoreaLiveLiteConfig) -> bool:
    return bool(config.live_enabled and not config.fixture_mode and os.environ.get("OPENDART_API_KEY"))


def _execute_opendart_detail_fetches(
    *,
    base_disclosures: Sequence[DisclosureEvent],
    planned_requests: Sequence[SourceRequest],
    as_of_date: date,
    config: KoreaLiveLiteConfig,
    http_client: HttpClient,
    built_requests: list[SourceRequest],
    source_call_counts: dict[str, int],
) -> tuple[tuple[DisclosureEvent, ...], tuple[SourceRequest, ...]]:
    """Execute capped OpenDART document.xml requests for watch disclosures."""

    cap = config.budget.max_opendart_detail_fetches_per_run
    if (cap is not None and cap <= 0) or not planned_requests:
        return (), ()
    if not _can_execute_live_opendart(config):
        return (), ()
    if not hasattr(http_client, "get_text"):
        return (), ()
    base_by_receipt = {item.rcept_no: item for item in base_disclosures if item.rcept_no}
    detail_events: list[DisclosureEvent] = []
    executed: list[SourceRequest] = []
    requests_to_run = planned_requests if cap is None else planned_requests[:cap]
    for request in requests_to_run:
        receipt_no = str(request.params.get("rcept_no") or "")
        base_event = base_by_receipt.get(receipt_no)
        if base_event is None:
            continue
        public_request = SourceRequest(
            method=request.method,
            url=request.url,
            params={key: value for key, value in request.params.items() if key != "crtfc_key"},
            headers=dict(request.headers),
            fixture_mode=False,
            credential_name=request.credential_name,
        )
        built_requests.append(public_request)
        live_request = _with_secret_param(public_request, "crtfc_key", os.environ["OPENDART_API_KEY"])
        cache_path = Path(config.cache_directory) / "opendart_detail" / as_of_date.isoformat() / f"{receipt_no}.xml"
        result = http_client.get_text(live_request, cache_path=cache_path)
        source_call_counts["opendart_detail_fetches"] += 1
        if not result.ok or result.text is None:
            continue
        text_cache_path = cache_path.with_suffix(".txt")
        text_cache_path.parent.mkdir(parents=True, exist_ok=True)
        text_cache_path.write_text(extract_document_text(result.text), encoding="utf-8")
        detail_events.append(normalize_disclosure_detail(base_event, result.text, as_of_date=as_of_date))
        executed.append(public_request)
    return tuple(detail_events), tuple(executed)


def _merge_detail_disclosures(
    list_disclosures: Sequence[DisclosureEvent],
    detail_disclosures: Sequence[DisclosureEvent],
) -> tuple[DisclosureEvent, ...]:
    by_key: dict[str, DisclosureEvent] = {}
    for item in list_disclosures:
        key = item.rcept_no or f"{item.symbol}:{item.published_at.isoformat()}:{item.title}"
        by_key[key] = item
    for item in detail_disclosures:
        key = item.rcept_no or f"{item.symbol}:{item.published_at.isoformat()}:{item.title}"
        by_key[key] = item
    return tuple(sorted(by_key.values(), key=lambda item: (item.symbol, item.published_at, item.rcept_no or "")))


def _with_secret_param(request: SourceRequest, key: str, value: str) -> SourceRequest:
    params = dict(request.params)
    params[key] = value
    return SourceRequest(
        method=request.method,
        url=request.url,
        params=params,
        headers=dict(request.headers),
        fixture_mode=request.fixture_mode,
        credential_name=request.credential_name,
    )


def _opendart_payload_to_disclosures(payload: Mapping[str, Any], as_of_date: date) -> tuple[DisclosureEvent, ...]:
    rows = payload.get("list") or payload.get("items") or payload.get("data") or ()
    disclosures: list[DisclosureEvent] = []
    if not isinstance(rows, Sequence) or isinstance(rows, (str, bytes)):
        return ()
    for row in rows:
        if not isinstance(row, Mapping):
            continue
        symbol = str(row.get("stock_code") or row.get("symbol") or row.get("corp_code") or "").strip()
        report_name = str(row.get("report_nm") or row.get("report_name") or row.get("title") or "OpenDART disclosure")
        receipt_date = row.get("rcept_dt") or row.get("published_at") or row.get("date") or as_of_date
        normalized = {
            "symbol": symbol,
            "source": "OpenDART",
            "report_type": report_name,
            "title": report_name,
            "published_at": receipt_date,
            "observed_at": receipt_date,
            "available_at": receipt_date,
            "as_of_date": as_of_date.isoformat(),
            "rcept_no": row.get("rcept_no"),
            "raw_text": row.get("raw_text") or row.get("rm") or "",
            "parsed_fields": {
                "opendart_corp_code": str(row.get("corp_code") or "").strip(),
                "opendart_corp_name": str(row.get("corp_name") or "").strip(),
                "opendart_corp_class": str(row.get("corp_cls") or "").strip(),
            },
        }
        if not symbol:
            continue
        disclosures.append(OpenDARTConnector.normalize_disclosure(normalized))
    return tuple(disclosures)


def _int_or_default(value: Any, default: int) -> int:
    try:
        return int(float(str(value)))
    except (TypeError, ValueError):
        return default


@dataclass(frozen=True)
class _DateBasedOpenDARTConnector:
    """OpenDART adapter that turns per-symbol calls into local filters.

    KoreaCheapScanner still scans all instruments. When it asks for one
    symbol's disclosures, this connector filters the already loaded date-range
    disclosures in memory, so ``opendart_symbol_disclosure_calls`` stays zero.
    """

    base: OpenDARTConnector
    date_disclosures: tuple[DisclosureEvent, ...]

    @property
    def fixture_root(self):
        return self.base.fixture_root

    def get_disclosures(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[DisclosureEvent, ...]:
        return tuple(
            item
            for item in self.date_disclosures
            if item.symbol == symbol
            and start <= item.published_at.date() <= end
            and item.available_at.date() <= as_of_date
        )

    def get_financial_actuals(self, symbol: str, as_of_date: date):
        return self.base.get_financial_actuals(symbol, as_of_date)


def _sources_with_date_disclosures(
    sources: KoreaCheapScanSources,
    date_disclosures: Sequence[DisclosureEvent],
) -> KoreaCheapScanSources:
    opendart = (
        _DateBasedOpenDARTConnector(sources.opendart, tuple(date_disclosures))
        if sources.opendart is not None
        else None
    )
    return KoreaCheapScanSources(
        krx=sources.krx,
        opendart=opendart,
        kind=sources.kind,
        fsc=sources.fsc,
    )


def _record_estimated_source_calls(
    source_call_counts: dict[str, int],
    sources: KoreaCheapScanSources,
    instruments_scanned: int,
    source_modes: Mapping[str, str],
) -> None:
    if sources.krx is not None and source_modes.get("krx") == "fixture":
        source_call_counts["krx_calls"] = 1 + instruments_scanned
    if sources.fsc is not None and source_modes.get("data_go_kr") == "fixture" and source_call_counts.get("data_go_kr_calls", 0) == 0:
        source_call_counts["data_go_kr_calls"] = 1 + instruments_scanned


def _remaining_naver_queries(config: KoreaLiveLiteConfig, used_queries: int) -> int | None:
    cap = config.budget.max_naver_search_calls_per_day
    if cap is None:
        return None
    return max(0, cap - used_queries)


def _logical_queries_by_source(
    source_call_counts: Mapping[str, int],
    http_stats: HttpClientStats,
) -> dict[str, int]:
    logical = {
        "opendart": int(source_call_counts.get("opendart_disclosure_date_range", 0))
        + int(source_call_counts.get("opendart_symbol_disclosure_calls", 0))
        + int(source_call_counts.get("opendart_detail_fetches", 0))
        + int(source_call_counts.get("opendart_company_code_calls", 0))
        + int(source_call_counts.get("opendart_financial_statement_calls", 0)),
        "krx": int(source_call_counts.get("krx_calls", 0)),
        "data_go_kr": int(source_call_counts.get("data_go_kr_calls", 0)),
        "naver_search": int(source_call_counts.get("naver_search_queries", 0)),
        "company_guide": int(source_call_counts.get("company_guide_snapshot_calls", 0))
        + int(source_call_counts.get("company_guide_recent_report_calls", 0)),
    }
    for source, count in http_stats.logical_queries_by_source.items():
        logical.setdefault(source, count)
    return {source: count for source, count in logical.items() if count}


def _select_candidates_for_research(
    candidates: Sequence[CheapScanCandidate],
    budget: KoreaLiveLiteBudget,
    *,
    targeted_smoke_only: bool = False,
) -> tuple[tuple[CheapScanCandidate, ...], tuple[SkippedCandidate, ...]]:
    selected: list[CheapScanCandidate] = []
    skipped: list[SkippedCandidate] = []
    event_symbols = 0
    deep_symbols = 0
    for candidate in candidates:
        if targeted_smoke_only and not candidate.test_injected:
            skipped.append(_skip(candidate, "targeted_smoke_only"))
            continue
        if candidate.recommended_next_layer == RecommendedNextLayer.NONE:
            skipped.append(_skip(candidate, "next_layer_none_or_hard_risk"))
            continue
        if not queries_for_candidate(candidate).queries:
            skipped.append(_skip(candidate, "no_escalation_queries"))
            continue
        if candidate.test_injected:
            selected.append(candidate)
            continue
        if candidate.recommended_next_layer == RecommendedNextLayer.DEEP_RESEARCH:
            if budget.max_symbols_for_deep_research is not None and deep_symbols >= budget.max_symbols_for_deep_research:
                skipped.append(_skip(candidate, "deep_research_symbol_budget_exhausted"))
                continue
            deep_symbols += 1
            selected.append(candidate)
            continue
        if budget.max_symbols_for_event_search is not None and event_symbols >= budget.max_symbols_for_event_search:
            skipped.append(_skip(candidate, "event_search_symbol_budget_exhausted"))
            continue
        event_symbols += 1
        selected.append(candidate)
    return tuple(selected), tuple(skipped)


def _skip(candidate: CheapScanCandidate, reason: str) -> SkippedCandidate:
    return SkippedCandidate(
        symbol=candidate.symbol,
        company_name=candidate.company_name,
        recommended_next_layer=candidate.recommended_next_layer,
        reason=reason,
    )


def _free_search_provider(
    config: KoreaLiveLiteConfig,
    http_client: HttpClient,
    source_modes: dict[str, str],
    fallback_reasons: dict[str, str],
) -> SearchProvider:
    if config.free_search_provider is not None:
        return config.free_search_provider
    if config.fixture_mode or not config.live_enabled:
        return EmptySearchProvider()
    if not os.environ.get("NAVER_CLIENT_ID") or not os.environ.get("NAVER_CLIENT_SECRET"):
        source_modes["naver_search"] = "fallback"
        fallback_reasons["naver_search"] = "missing_naver_credentials"
        return EmptySearchProvider()
    return _LiveNaverSearchProvider(
        client_id=os.environ["NAVER_CLIENT_ID"],
        client_secret=os.environ["NAVER_CLIENT_SECRET"],
        http_client=http_client,
        cache_directory=Path(config.cache_directory) / "naver" / config.as_of_date.isoformat(),
        source_modes=source_modes,
        fallback_reasons=fallback_reasons,
    )


def _live_page_fetch_enabled(config: KoreaLiveLiteConfig) -> bool:
    return bool(config.live_page_fetch_enabled or (config.live_enabled and not config.fixture_mode))


def _page_fetch_cache_directory(config: KoreaLiveLiteConfig) -> Path:
    if config.page_fetch_cache_directory is not None:
        return Path(config.page_fetch_cache_directory)
    return Path(config.cache_directory) / "page_fetch"


def _run_report_radar(
    *,
    config: KoreaLiveLiteConfig,
    instruments: Sequence[Instrument],
    free_search_provider: SearchProvider,
    remaining_queries: int | None,
) -> tuple[ReportRadarCandidate, ...]:
    if not config.report_radar_enabled or (remaining_queries is not None and remaining_queries <= 0):
        return ()
    budget = SearchBudget(
        max_total_queries_per_day=remaining_queries,
        max_queries_per_symbol=None,
        max_deep_research_symbols=config.budget.max_symbols_for_deep_research,
        max_active_monitoring_symbols=None,
    )
    return ReportRadar(free_search_provider, max_results_per_query=config.max_results_per_query).run(
        instruments=instruments,
        as_of_date=config.as_of_date,
        budget=budget,
        active_watchlist_symbols=config.active_watchlist_symbols,
        max_symbols=config.report_radar_universe_limit,
    )


def _estimate_radar_queries(
    config: KoreaLiveLiteConfig,
    instruments: Sequence[Instrument],
    radar_candidates: Sequence[ReportRadarCandidate],
) -> int:
    if not config.report_radar_enabled:
        return 0
    # The radar stops when its budget is exhausted. This conservative estimate
    # prevents later candidate research from assuming the full Naver budget is
    # still available after a radar pass.
    symbol_count = len(instruments) if config.report_radar_universe_limit is None else min(len(instruments), config.report_radar_universe_limit)
    estimated = symbol_count * len(REPORT_RADAR_PHRASES)
    cap = config.budget.max_naver_search_calls_per_day
    if not radar_candidates:
        return estimated if cap is None else min(cap, estimated)
    return estimated if cap is None else min(cap, estimated)


def _targeted_smoke_candidates(config: KoreaLiveLiteConfig) -> tuple[CheapScanCandidate, ...]:
    if not config.targeted_smoke_enabled:
        return ()
    company = (config.targeted_smoke_company or "").strip()
    symbol = (config.targeted_smoke_symbol or company or "TARGETED_SMOKE").strip()
    if not company:
        company = symbol
    return (
        CheapScanCandidate(
            symbol=symbol,
            company_name=company,
            market=Market.KR,
            as_of_date=config.as_of_date,
            reason_codes=("TARGETED_SMOKE",),
            cheap_scan_total_score=0.0,
            recommended_next_layer=RecommendedNextLayer.EVENT_SEARCH,
            candidate_source_path="targeted_smoke",
            test_injected=True,
            production_candidate=False,
        ),
    )


def _execute_opendart_single_account_actuals_for_candidates(
    *,
    candidates: Sequence[CheapScanCandidate],
    sources: KoreaCheapScanSources,
    date_disclosures: Sequence[DisclosureEvent],
    candidate_corp_codes: Mapping[str, str] | None = None,
    config: KoreaLiveLiteConfig,
    http_client: HttpClient,
    built_requests: list[SourceRequest],
    source_call_counts: dict[str, int],
) -> dict[str, tuple[FinancialActual, ...]]:
    if not candidates or sources.opendart is None or not _can_execute_live_opendart(config):
        return {}
    if not hasattr(sources.opendart, "build_single_account_request") or not hasattr(sources.opendart, "normalize_single_account_actuals"):
        return {}
    used_calls = (
        source_call_counts.get("opendart_disclosure_date_range", 0)
        + source_call_counts.get("opendart_detail_fetches", 0)
        + source_call_counts.get("opendart_symbol_disclosure_calls", 0)
        + source_call_counts.get("opendart_company_code_calls", 0)
        + source_call_counts.get("opendart_financial_statement_calls", 0)
    )
    remaining_calls = _remaining_from_cap(config.budget.max_opendart_calls_per_day, used_calls)
    if not _has_remaining_calls(remaining_calls):
        return {}
    corp_codes = {**(candidate_corp_codes or {}), **_opendart_corp_codes_by_symbol(date_disclosures)}
    if any(candidate.symbol not in corp_codes for candidate in _unique_candidates_by_symbol(candidates)):
        corp_codes_from_map, remaining_calls = _execute_opendart_company_code_lookup_for_candidates(
            candidates=candidates,
            existing_corp_codes=corp_codes,
            sources=sources,
            config=config,
            http_client=http_client,
            built_requests=built_requests,
            source_call_counts=source_call_counts,
            remaining_calls=remaining_calls,
        )
        corp_codes = {**corp_codes_from_map, **corp_codes}
    if not corp_codes:
        return {}

    fetched: dict[str, list[FinancialActual]] = {}
    seen_symbols: set[str] = set()
    for candidate in candidates:
        if candidate.symbol in seen_symbols:
            continue
        seen_symbols.add(candidate.symbol)
        corp_code = corp_codes.get(candidate.symbol)
        if not corp_code:
            continue
        for financial_period in _opendart_financial_statement_periods(config.as_of_date):
            if not _has_remaining_calls(remaining_calls):
                return {symbol: _dedupe_financial_actuals(items) for symbol, items in fetched.items()}
            public_request = sources.opendart.build_single_account_request(
                corp_code,
                financial_period["fiscal_year"],
                config.as_of_date,
                report_code=financial_period["report_code"],
                full_accounts=True,
                fs_div="CFS",
            )
            built_requests.append(public_request)
            live_request = _with_secret_param(public_request, "crtfc_key", os.environ["OPENDART_API_KEY"])
            cache_path = (
                Path(config.cache_directory)
                / "opendart_financial"
                / config.as_of_date.isoformat()
                / (
                    f"single_account_all_{_safe_filename(candidate.symbol)}_{_safe_filename(corp_code)}_"
                    f"{financial_period['fiscal_year']}_{financial_period['report_code']}_CFS.json"
                )
            )
            result = http_client.get_json(live_request, cache_path=cache_path)
            source_call_counts["opendart_financial_statement_calls"] += 1
            remaining_calls = _consume_remaining_call(remaining_calls)
            if not result.ok or not isinstance(result.json_data, Mapping):
                continue
            try:
                actuals = sources.opendart.normalize_single_account_actuals(
                    result.json_data,
                    symbol=candidate.symbol,
                    fiscal_year=financial_period["fiscal_year"],
                    as_of_date=config.as_of_date,
                    reported_at=financial_period["reported_at"],
                    fiscal_quarter=financial_period["fiscal_quarter"],
                    period_end=financial_period["period_end"],
                )
            except (TypeError, ValueError):
                continue
            fetched.setdefault(candidate.symbol, []).extend(actuals)
    return {symbol: _dedupe_financial_actuals(items) for symbol, items in fetched.items()}


def _execute_opendart_company_code_lookup_for_candidates(
    *,
    candidates: Sequence[CheapScanCandidate],
    existing_corp_codes: Mapping[str, str],
    sources: KoreaCheapScanSources,
    config: KoreaLiveLiteConfig,
    http_client: HttpClient,
    built_requests: list[SourceRequest],
    source_call_counts: dict[str, int],
    remaining_calls: int | None,
) -> tuple[dict[str, str], int | None]:
    missing_symbols = tuple(
        candidate.symbol
        for candidate in _unique_candidates_by_symbol(candidates)
        if candidate.symbol not in existing_corp_codes
    )
    if not missing_symbols or sources.opendart is None or not _has_remaining_calls(remaining_calls):
        return {}, remaining_calls
    if not hasattr(sources.opendart, "build_company_code_request") or not hasattr(sources.opendart, "company_codes_by_stock_code"):
        return {}, remaining_calls

    raw_request = sources.opendart.build_company_code_request()
    public_request = SourceRequest(
        method=raw_request.method,
        url=raw_request.url,
        params={key: value for key, value in raw_request.params.items() if key != "crtfc_key"},
        headers=dict(raw_request.headers),
        fixture_mode=False,
        credential_name=raw_request.credential_name,
    )
    built_requests.append(public_request)
    live_request = _with_secret_param(public_request, "crtfc_key", os.environ["OPENDART_API_KEY"])
    cache_path = Path(config.cache_directory) / "opendart_corp_code" / config.as_of_date.isoformat() / "corpCode.zip"
    if hasattr(http_client, "get_bytes"):
        result = http_client.get_bytes(live_request, cache_path=cache_path)
        payload: bytes | str | None = result.bytes_data
    else:
        result = http_client.get_text(live_request, cache_path=cache_path.with_suffix(".xml"))
        payload = result.text
    source_call_counts["opendart_company_code_calls"] += 1
    remaining_calls = _consume_remaining_call(remaining_calls)
    if not result.ok or payload in (None, b"", ""):
        return {}, remaining_calls
    try:
        all_codes = sources.opendart.company_codes_by_stock_code(payload)
    except Exception:
        return {}, remaining_calls
    wanted = set(missing_symbols)
    return {symbol: corp_code for symbol, corp_code in all_codes.items() if symbol in wanted}, remaining_calls


def _execute_company_guide_for_candidates(
    *,
    candidates: Sequence[CheapScanCandidate],
    config: KoreaLiveLiteConfig,
    effective_fixture_mode: bool,
    http_client: HttpClient,
    built_requests: list[SourceRequest],
    source_call_counts: dict[str, int],
    source_modes: dict[str, str],
    fallback_reasons: dict[str, str],
) -> dict[str, _CompanyGuideFeatureData]:
    if not config.company_guide_enabled:
        source_modes["company_guide"] = "disabled_optional"
        return {}
    if not candidates:
        source_modes["company_guide"] = "not_configured"
        return {}
    if effective_fixture_mode or not config.live_enabled or config.fixture_mode:
        source_modes["company_guide"] = "fixture"
        return {}
    if config.budget.max_company_guide_calls_per_day is not None and config.budget.max_company_guide_calls_per_day <= 0:
        source_modes["company_guide"] = "fallback"
        fallback_reasons["company_guide"] = "company_guide_budget_exhausted"
        return {}

    connector = config.company_guide_connector or CompanyGuideConnector(fixture_mode=False)
    remaining_calls = config.budget.max_company_guide_calls_per_day
    fetched: dict[str, _CompanyGuideFeatureData] = {}
    any_success = False
    last_error: str | None = None
    seen_symbols: set[str] = set()
    for candidate in candidates:
        if candidate.symbol in seen_symbols:
            continue
        seen_symbols.add(candidate.symbol)
        consensus: tuple[ConsensusSnapshot, ...] = ()
        revisions: tuple[ConsensusRevision, ...] = ()
        reports: tuple[ResearchReport, ...] = ()

        if _has_remaining_calls(remaining_calls):
            request = connector.build_snapshot_request(candidate.symbol, config.as_of_date)
            public_request = _company_guide_public_request(request)
            built_requests.append(public_request)
            cache_path = _company_guide_cache_path(config, candidate.symbol, "snapshot", "html")
            result = http_client.get_text(public_request, cache_path=cache_path)
            source_call_counts["company_guide_snapshot_calls"] += 1
            remaining_calls = _consume_remaining_call(remaining_calls)
            if result.ok and result.text:
                try:
                    parsed = connector.parse_consensus_snapshot_html(
                        result.text,
                        symbol=candidate.symbol,
                        as_of_date=config.as_of_date,
                    )
                    consensus = (parsed.consensus,)
                    revisions = _company_guide_revisions_from_broker_targets(
                        parsed.broker_targets,
                        symbol=candidate.symbol,
                        as_of_date=config.as_of_date,
                    )
                    any_success = True
                except (TypeError, ValueError) as exc:
                    last_error = f"company_guide_snapshot_parse_failed:{type(exc).__name__}"
            elif result.error:
                last_error = f"company_guide_snapshot_fetch_failed:{result.error}"

        if _has_remaining_calls(remaining_calls):
            request = connector.build_recent_reports_request(
                candidate.symbol,
                config.as_of_date,
                per_page=config.company_guide_recent_reports_per_page,
                cur_page=1,
            )
            public_request = _company_guide_public_request(request)
            built_requests.append(public_request)
            cache_path = _company_guide_cache_path(config, candidate.symbol, "recent_reports", "json")
            result = http_client.get_json(public_request, cache_path=cache_path)
            source_call_counts["company_guide_recent_report_calls"] += 1
            remaining_calls = _consume_remaining_call(remaining_calls)
            payload = result.json_data if isinstance(result.json_data, Mapping) else result.text
            if result.ok and payload is not None:
                try:
                    reports = connector.parse_recent_reports_payload(
                        payload,
                        symbol=candidate.symbol,
                        as_of_date=config.as_of_date,
                    )
                    any_success = True
                except (TypeError, ValueError) as exc:
                    last_error = f"company_guide_recent_report_parse_failed:{type(exc).__name__}"
            elif result.error:
                last_error = f"company_guide_recent_report_fetch_failed:{result.error}"

        if consensus or revisions or reports:
            fetched[candidate.symbol] = _CompanyGuideFeatureData(
                consensus=_dedupe_consensus_snapshots(consensus),
                consensus_revisions=_dedupe_consensus_revisions(revisions),
                research_reports=_dedupe_research_reports(reports),
            )
        if not _has_remaining_calls(remaining_calls):
            break

    source_modes["company_guide"] = "live_executed" if any_success else "fallback"
    if not any_success:
        fallback_reasons["company_guide"] = last_error or "company_guide_no_data"
    return fetched


def _company_guide_revisions_from_broker_targets(
    rows: Sequence[BrokerTargetRow],
    *,
    symbol: str,
    as_of_date: date,
) -> tuple[ConsensusRevision, ...]:
    usable = tuple(
        row
        for row in rows
        if row.symbol == symbol
        and row.date <= as_of_date
        and row.target_price_revision_pct is not None
    )
    if not usable:
        return ()
    values = tuple(float(row.target_price_revision_pct) for row in usable if row.target_price_revision_pct is not None)
    if not values:
        return ()
    latest_date = max(row.date for row in usable)
    average_revision = round(sum(values) / len(values), 4)
    return (
        ConsensusRevision(
            symbol=symbol,
            date=latest_date,
            fiscal_year=as_of_date.year,
            as_of_date=as_of_date,
            target_price_revision_1m=average_revision,
            analyst_count_change=len(values),
            source="company_guide_snapshot",
            parsed_fields={
                "source": "company_guide_snapshot",
                "company_guide_broker_target_revision_proxy": True,
                "revision_proxy_method": "average_broker_target_price_revision_pct",
                "broker_target_revision_count": len(values),
                "broker_target_revision_min": min(values),
                "broker_target_revision_max": max(values),
                "consensus_proxy_score_eligible": True,
            },
        ),
    )


def _company_guide_public_request(request: SourceRequest) -> SourceRequest:
    return SourceRequest(
        method=request.method,
        url=request.url,
        params=dict(request.params),
        headers=dict(request.headers),
        fixture_mode=False,
        credential_name="COMPANY_GUIDE",
    )


def _company_guide_cache_path(config: KoreaLiveLiteConfig, symbol: str, stem: str, suffix: str) -> Path:
    return (
        Path(config.cache_directory)
        / "company_guide"
        / config.as_of_date.isoformat()
        / f"{_safe_filename(symbol)}_{stem}.{suffix}"
    )


def _opendart_corp_codes_by_symbol(disclosures: Sequence[DisclosureEvent]) -> dict[str, str]:
    corp_codes: dict[str, str] = {}
    for item in disclosures:
        corp_code = str(item.parsed_fields.get("opendart_corp_code") or "").strip()
        if item.symbol and corp_code:
            corp_codes.setdefault(item.symbol, corp_code)
    return corp_codes


def _opendart_annual_financial_years(as_of_date: date) -> tuple[tuple[int, date], ...]:
    years: list[tuple[int, date]] = []
    for fiscal_year in (as_of_date.year - 1, as_of_date.year - 2, as_of_date.year - 3):
        reported_at = date(fiscal_year + 1, 4, 1)
        if reported_at <= as_of_date:
            years.append((fiscal_year, reported_at))
    return tuple(years)


def _opendart_financial_statement_periods(as_of_date: date) -> tuple[dict[str, Any], ...]:
    periods: list[dict[str, Any]] = []
    quarterly_candidates = (
        (as_of_date.year, 1, date(as_of_date.year, 3, 31), "11013", date(as_of_date.year, 5, 16)),
        (as_of_date.year, 2, date(as_of_date.year, 6, 30), "11012", date(as_of_date.year, 8, 16)),
        (as_of_date.year, 3, date(as_of_date.year, 9, 30), "11014", date(as_of_date.year, 11, 16)),
    )
    reported_quarters: list[tuple[int, int, date, str, date]] = []
    for fiscal_year, fiscal_quarter, period_end, report_code, reported_at in quarterly_candidates:
        if reported_at <= as_of_date:
            reported_quarters.append((fiscal_year, fiscal_quarter, period_end, report_code, reported_at))
            periods.append(
                {
                    "fiscal_year": fiscal_year,
                    "fiscal_quarter": fiscal_quarter,
                    "period_end": period_end,
                    "report_code": report_code,
                    "reported_at": reported_at,
                }
            )
    if reported_quarters:
        fiscal_year, fiscal_quarter, _, report_code, _ = reported_quarters[-1]
        prior_year = fiscal_year - 1
        prior_period_end = date(prior_year, fiscal_quarter * 3, _month_end_day(prior_year, fiscal_quarter * 3))
        prior_reported_at = date(prior_year, 5, 16) if fiscal_quarter == 1 else date(prior_year, 8, 16) if fiscal_quarter == 2 else date(prior_year, 11, 16)
        periods.append(
            {
                "fiscal_year": prior_year,
                "fiscal_quarter": fiscal_quarter,
                "period_end": prior_period_end,
                "report_code": report_code,
                "reported_at": prior_reported_at,
            }
        )
    for fiscal_year, reported_at in _opendart_annual_financial_years(as_of_date):
        periods.append(
            {
                "fiscal_year": fiscal_year,
                "fiscal_quarter": None,
                "period_end": date(fiscal_year, 12, 31),
                "report_code": "11011",
                "reported_at": reported_at,
            }
        )
    return tuple(periods)


def _month_end_day(year: int, month: int) -> int:
    if month == 2:
        return 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28
    return 30 if month in {4, 6, 9, 11} else 31


def _execute_data_go_kr_financial_actuals_for_candidates(
    *,
    candidates: Sequence[CheapScanCandidate],
    sources: KoreaCheapScanSources,
    instruments: Sequence[Instrument],
    config: KoreaLiveLiteConfig,
    http_client: HttpClient,
    built_requests: list[SourceRequest],
    source_call_counts: dict[str, int],
) -> dict[str, tuple[FinancialActual, ...]]:
    if not candidates or not _can_execute_live_data_go_kr(config):
        return {}
    connector = _data_go_kr_financial_connector(sources)
    if connector is None:
        return {}
    remaining_calls = _remaining_from_cap(config.budget.max_data_go_kr_calls_per_day, source_call_counts.get("data_go_kr_calls", 0))
    if not _has_remaining_calls(remaining_calls):
        return {}

    instruments_by_symbol = {item.symbol: item for item in instruments}
    fetched: dict[str, list[FinancialActual]] = {}
    seen_symbols: set[str] = set()
    for candidate in candidates:
        if candidate.symbol in seen_symbols:
            continue
        seen_symbols.add(candidate.symbol)
        instrument = instruments_by_symbol.get(candidate.symbol)
        company_name = instrument.name if instrument is not None else candidate.company_name
        corp_code = instrument.corp_code if instrument is not None else None
        financial_lookup_company_name = company_name if corp_code else None
        for fiscal_year in _candidate_financial_years(config.as_of_date):
            if not _has_remaining_calls(remaining_calls):
                return {symbol: _dedupe_financial_actuals(items) for symbol, items in fetched.items()}
            public_request = _data_go_public_request(
                connector.build_financial_info_request(
                    candidate.symbol,
                    config.as_of_date,
                    company_name=financial_lookup_company_name,
                    crno=corp_code,
                    fiscal_year=fiscal_year,
                )
            )
            built_requests.append(public_request)
            live_request = _with_secret_param(public_request, "serviceKey", os.environ["DATA_GO_KR_SERVICE_KEY"])
            request_key = corp_code or candidate.symbol
            cache_path = (
                Path(config.cache_directory)
                / "data_go_kr"
                / config.as_of_date.isoformat()
                / f"financial_actuals_{_safe_filename(candidate.symbol)}_{_safe_filename(request_key)}_{fiscal_year}.json"
            )
            result = http_client.get_json(live_request, cache_path=cache_path)
            source_call_counts["data_go_kr_calls"] += 1
            source_call_counts["data_go_kr_financial_actual_calls"] += 1
            remaining_calls = _consume_remaining_call(remaining_calls)
            if not result.ok or not isinstance(result.json_data, Mapping):
                continue
            for row in _data_go_kr_payload_items(result.json_data):
                if not _financial_row_matches_candidate(row, candidate, company_name, corp_code):
                    continue
                try:
                    actual = connector.normalize_financial_actual(
                        row,
                        as_of_date=config.as_of_date,
                        fallback_symbol=candidate.symbol,
                    )
                except (TypeError, ValueError):
                    continue
                if actual.symbol != candidate.symbol:
                    actual = replace(actual, symbol=candidate.symbol)
                fetched.setdefault(candidate.symbol, []).append(actual)
    return {symbol: _dedupe_financial_actuals(items) for symbol, items in fetched.items()}


def _data_go_kr_financial_connector(sources: KoreaCheapScanSources):
    fsc = sources.fsc
    if fsc is None:
        return None
    if hasattr(fsc, "build_financial_info_request") and hasattr(fsc, "normalize_financial_actual"):
        return fsc
    base = getattr(fsc, "base", None)
    if base is not None and hasattr(base, "build_financial_info_request") and hasattr(base, "normalize_financial_actual"):
        return base
    return None


def _candidate_financial_years(as_of_date: date) -> tuple[int, ...]:
    return (as_of_date.year, as_of_date.year - 1, as_of_date.year - 2)


def _financial_row_matches_candidate(
    row: Mapping[str, Any],
    candidate: CheapScanCandidate,
    company_name: str | None,
    corp_code: str | None,
) -> bool:
    row_symbol = str(row.get("symbol") or row.get("srtnCd") or row.get("isinCd") or "").strip()
    if row_symbol in {candidate.symbol, f"A{candidate.symbol}"}:
        return True
    row_crno = str(row.get("crno") or row.get("corp_code") or "").strip()
    if corp_code and row_crno == corp_code:
        return True
    if row_crno and not corp_code:
        return False
    haystack = " ".join(str(row.get(key) or "") for key in ("corpNm", "company_name", "itmsNm", "name"))
    names = tuple(
        item.strip()
        for item in (candidate.company_name, company_name)
        if item and item.strip()
    )
    return bool(haystack and any(name in haystack for name in names))


def _base_feature_input_for_candidate(
    *,
    candidate: CheapScanCandidate,
    sources: KoreaCheapScanSources,
    instruments: Sequence[Instrument],
    config: KoreaLiveLiteConfig,
    extra_financial_actuals: Sequence[FinancialActual] = (),
    extra_consensus: Sequence[ConsensusSnapshot] = (),
    extra_consensus_revisions: Sequence[ConsensusRevision] = (),
    extra_research_reports: Sequence[ResearchReport] = (),
) -> FeatureEngineeringInput | None:
    instrument = {item.symbol: item for item in instruments}.get(candidate.symbol)
    price_bars = sources.get_price_bars(candidate.symbol, config.as_of_date, config.lookback_days)
    disclosures = sources.get_disclosures(
        candidate.symbol,
        config.as_of_date,
        max(config.disclosure_lookback_days, 30),
    )
    financial_actuals = _dedupe_financial_actuals(
        tuple(sources.get_financial_actuals(candidate.symbol, config.as_of_date)) + tuple(extra_financial_actuals)
    )
    consensus = _dedupe_consensus_snapshots(tuple(extra_consensus))
    consensus_revisions = _dedupe_consensus_revisions(tuple(extra_consensus_revisions))
    research_reports = _dedupe_research_reports(tuple(extra_research_reports))
    if not price_bars and not disclosures and not financial_actuals and not consensus and not consensus_revisions and not research_reports:
        return None
    return FeatureEngineeringInput(
        symbol=candidate.symbol,
        as_of_date=config.as_of_date,
        company_name=instrument.name if instrument is not None else candidate.company_name,
        sector_context=_instrument_sector_context(instrument),
        price_bars=price_bars,
        financial_actuals=financial_actuals,
        consensus=consensus,
        consensus_revisions=consensus_revisions,
        disclosures=disclosures,
        research_reports=research_reports,
    )


def _instrument_sector_context(instrument: Instrument | None) -> str | None:
    if instrument is None:
        return None
    return " ".join(part for part in (instrument.sector_custom, instrument.sector_exchange) if part) or None


def _dedupe_financial_actuals(items: Sequence[FinancialActual]) -> tuple[FinancialActual, ...]:
    by_key: dict[tuple[str, int, int | None, date], FinancialActual] = {}
    for item in items:
        key = (item.symbol, item.fiscal_year, item.fiscal_quarter, item.period_end)
        existing = by_key.get(key)
        if existing is None or _financial_actual_field_count(item) > _financial_actual_field_count(existing):
            by_key[key] = item
    return tuple(sorted(by_key.values(), key=lambda item: (item.period_end, item.reported_at)))


def _financial_actual_field_count(item: FinancialActual) -> int:
    return sum(
        1
        for value in (
            item.sales,
            item.operating_profit,
            item.net_income,
            item.eps,
            item.bps,
            item.roe,
            item.opm,
            item.cashflow_from_operations,
            item.capex,
            item.fcf,
            item.receivables,
            item.inventory,
        )
        if value is not None
    )


def _dedupe_consensus_snapshots(items: Sequence[ConsensusSnapshot]) -> tuple[ConsensusSnapshot, ...]:
    by_key = {(item.symbol, item.date, item.fiscal_year, item.source): item for item in items}
    return tuple(sorted(by_key.values(), key=lambda item: (item.date, item.fiscal_year, item.source)))


def _dedupe_consensus_revisions(items: Sequence[ConsensusRevision]) -> tuple[ConsensusRevision, ...]:
    by_key = {(item.symbol, item.date, item.fiscal_year, item.source): item for item in items}
    return tuple(sorted(by_key.values(), key=lambda item: (item.date, item.fiscal_year, item.source)))


def _dedupe_research_reports(items: Sequence[ResearchReport]) -> tuple[ResearchReport, ...]:
    by_key = {(item.symbol, item.publish_date, item.broker, item.title): item for item in items}
    return tuple(sorted(by_key.values(), key=lambda item: (item.publish_date, item.broker, item.title)))


def _top_trading_value_probe_rows(
    config: KoreaLiveLiteConfig,
    sources: KoreaCheapScanSources,
    instruments: Sequence[Instrument],
) -> tuple[Mapping[str, Any], ...]:
    if not config.top_trading_value_probe_enabled:
        return ()
    ranked: list[Mapping[str, Any]] = []
    for instrument in instruments:
        bars = sources.get_price_bars(instrument.symbol, config.as_of_date, min(config.lookback_days, 14))
        if not bars:
            continue
        latest = max(bars, key=lambda item: item.date)
        if latest.trading_value <= 0:
            continue
        ranked.append(
            {
                "symbol": instrument.symbol,
                "company_name": instrument.name,
                "market": instrument.market,
                "price_date": latest.date,
                "close": latest.close,
                "volume": latest.volume,
                "trading_value": latest.trading_value,
                "source": latest.source,
            }
        )
    ranked.sort(key=lambda item: (-float(item["trading_value"]), -int(item["volume"]), str(item["symbol"])))
    rows = []
    for rank, row in enumerate(ranked[: config.top_trading_value_probe_count], start=1):
        item = dict(row)
        item["rank"] = rank
        item["candidate_source_path"] = "top_trading_value_probe"
        item["production_candidate"] = False
        item["test_injected"] = True
        rows.append(item)
    return tuple(rows)


def _top_trading_value_probe_candidates(
    config: KoreaLiveLiteConfig,
    rows: Sequence[Mapping[str, Any]],
) -> tuple[CheapScanCandidate, ...]:
    if not config.top_trading_value_probe_enabled:
        return ()
    return tuple(
        CheapScanCandidate(
            symbol=str(row["symbol"]),
            company_name=str(row["company_name"]),
            market=Market.KR,
            as_of_date=config.as_of_date,
            reason_codes=("TOP_TRADING_VALUE_PROBE",),
            cheap_scan_total_score=0.0,
            recommended_next_layer=RecommendedNextLayer.EVENT_SEARCH,
            candidate_source_path="top_trading_value_probe",
            test_injected=True,
            production_candidate=False,
        )
        for row in rows
    )


def _merge_candidates(*groups: Sequence[CheapScanCandidate]) -> tuple[CheapScanCandidate, ...]:
    merged: dict[tuple[str, str], CheapScanCandidate] = {}
    for group in groups:
        for candidate in group:
            key = (candidate.symbol, candidate.candidate_source_path)
            existing = merged.get(key)
            if existing is None or candidate.cheap_scan_total_score > existing.cheap_scan_total_score:
                merged[key] = candidate
    return tuple(sorted(merged.values(), key=lambda item: (not item.test_injected, not item.production_candidate, -item.cheap_scan_total_score, item.symbol)))


@dataclass
class _LiveNaverSearchProvider:
    client_id: str
    client_secret: str
    http_client: HttpClient
    cache_directory: Path
    source_modes: dict[str, str]
    fallback_reasons: dict[str, str]
    search_domains: tuple[str, ...] = ("news", "web", "doc")
    errors: list[str] = field(default_factory=list)

    def search(self, query: str, as_of_date: date, max_results: int = 100) -> tuple[SearchResult, ...]:
        request_builder = NaverFreeSearchProvider(
            client_id=self.client_id,
            client_secret=self.client_secret,
            search_domains=self.search_domains,
            fixture_mode=False,
            live_enabled=True,
        )
        results: list[SearchResult] = []
        for request in request_builder.build_search_requests(query, as_of_date, max_results):
            cache_path = self.cache_directory / f"{_safe_filename(query)}_{_safe_filename(Path(request.url).stem)}.json"
            result = self.http_client.get_json(request, cache_path=cache_path)
            if not result.ok or not isinstance(result.json_data, Mapping):
                self.errors.append(result.error or "naver_live_search_failed")
                self.source_modes["naver_search"] = "fallback"
                self.fallback_reasons["naver_search"] = result.error or "naver_live_search_failed"
                continue
            self.source_modes["naver_search"] = "live_executed"
            results.extend(
                NaverFreeSearchProvider.normalize_response(
                    result.json_data,
                    query=query,
                    as_of_date=as_of_date,
                    source=request.url,
                )
            )
        unique: dict[str, SearchResult] = {}
        for item in results:
            if item.published_at is not None and item.published_at.date() > as_of_date:
                continue
            unique.setdefault(item.url, item)
        return tuple(sorted(unique.values(), key=lambda item: item.rank or 9999)[:max_results])


def _search_budget(
    budget: KoreaLiveLiteBudget,
    remaining_queries: int | None,
) -> SearchBudget:
    return SearchBudget(
        max_total_queries_per_day=None if remaining_queries is None else max(0, remaining_queries),
        max_queries_per_symbol=None,
        max_deep_research_symbols=budget.max_symbols_for_deep_research,
        max_active_monitoring_symbols=None,
        sleep_seconds_between_queries=0.0,
        stop_on_captcha_or_block=True,
    )


def _query_planner_for_candidate(candidate: CheapScanCandidate, config: KoreaLiveLiteConfig):
    if candidate.candidate_source_path == "targeted_smoke" and config.targeted_smoke_queries:
        return _FixedCandidateQueryPlanner(candidate, config.targeted_smoke_queries)
    if candidate.candidate_source_path == "top_trading_value_probe" and config.top_trading_value_probe_queries:
        return _FixedCandidateQueryPlanner(candidate, _format_probe_queries(candidate, config.top_trading_value_probe_queries))
    return EscalationQueryPlanner(candidate)


def _format_probe_queries(candidate: CheapScanCandidate, queries: Sequence[str]) -> tuple[str, ...]:
    formatted: list[str] = []
    for query in queries:
        formatted.append(str(query).format(company=candidate.company_name, symbol=candidate.symbol))
    return tuple(dict.fromkeys(formatted))


class _FixedCandidateQueryPlanner:
    def __init__(self, candidate: CheapScanCandidate, queries: Sequence[str]) -> None:
        self._candidate = candidate
        self._queries = tuple(queries)

    def plan(self, **kwargs) -> QueryPlan:
        specs = tuple(
            QuerySpec(
                group="event_search",
                query=query,
                priority=10 + index,
                company_name=self._candidate.company_name,
                symbol=self._candidate.symbol,
                sector=None,
                market=self._candidate.market,
                as_of_date=self._candidate.as_of_date,
            )
            for index, query in enumerate(self._queries)
        )
        return QueryPlan(
            company_name=self._candidate.company_name,
            symbol=self._candidate.symbol,
            sector=None,
            market=self._candidate.market,
            as_of_date=self._candidate.as_of_date,
            queries=specs,
        )


def _targeted_smoke_result_row(
    candidate: CheapScanCandidate,
    result: WebResearchPipelineResult,
    combined_evidence: Sequence[Evidence] = (),
) -> Mapping[str, Any]:
    diagnostics = result.theme_route_diagnostics
    evidence_count = len(tuple(_dedupe_evidence(tuple(combined_evidence)))) if combined_evidence else len(result.web_result.evidence)
    score_valid_bool = _result_score_valid(result)
    blocked_reason = diagnostics.get("score_blocked_reason") or score_block_reason(result.score)
    raw_score_before_block = raw_score_total_before_block(result.score)
    visible_score = visible_score_total(result.score)
    input_fingerprint = _research_input_fingerprint(result, combined_evidence)
    variability_drivers = _score_variability_drivers(
        result,
        score_valid=score_valid_bool,
        blocked_reason=blocked_reason,
        evidence_count=evidence_count,
        input_fingerprint=input_fingerprint,
    )
    return {
        "symbol": candidate.symbol,
        "company_name": candidate.company_name,
        "candidate_source_path": candidate.candidate_source_path,
        "test_injected": candidate.test_injected,
        "production_candidate": candidate.production_candidate,
        "stage": result.stage.stage,
        "stage_reason": result.stage.stage_reason,
        "visible_score": visible_score,
        "score_total": visible_score,
        "score_valid": score_valid_bool,
        "score_blocked_reason": blocked_reason,
        "score_fingerprint": score_fingerprint(result.score),
        "research_input_fingerprint": input_fingerprint,
        "score_variability_drivers": variability_drivers,
        "raw_score_total_before_theme_route_block": diagnostics.get("raw_score_total_before_theme_route_block")
        or result.score.diagnostic_scores.get("raw_score_total_before_theme_route_block"),
        "raw_score_total_before_score_gap_block": diagnostics.get("raw_score_total_before_score_gap_block")
        or result.score.diagnostic_scores.get("raw_score_total_before_score_gap_block"),
        "raw_score_before_block": raw_score_before_block,
        "score_components": _score_component_row(result.score) if score_valid_bool else None,
        "raw_score_components_before_block": _raw_score_component_row(result.score) if not score_valid_bool else None,
        "estimate_quality": _estimate_quality_row(result),
        "feature_input_counts": _feature_input_count_row(result.feature_input),
        "evidence_count": evidence_count,
        "web_evidence_count": len(result.web_result.evidence),
        "score_evidence_count": len(result.score.evidence_ids),
        "score_evidence_ids": result.score.evidence_ids,
        "queries_run": result.web_result.queries_run,
        "theme_rebalance_status": diagnostics.get("theme_rebalance_status"),
        "theme_route_status": diagnostics.get("theme_route_status"),
        "theme_route_confidence": diagnostics.get("theme_route_confidence"),
        "theme_evidence_gate_status": diagnostics.get("theme_evidence_gate_status"),
        "theme_evidence_ref_match_count": diagnostics.get("theme_evidence_ref_match_count"),
        "theme_large_sector_id": diagnostics.get("large_sector_id"),
        "theme_canonical_archetype_id": diagnostics.get("canonical_archetype_id"),
        "scoring_large_sector_id": result.feature_result.payload.large_sector_id,
        "scoring_canonical_archetype_id": result.feature_result.payload.canonical_archetype_id,
        "theme_expansion_query_count": len(result.expansion_queries_run),
        "post_parse_gap_expansion_count": diagnostics.get("post_parse_gap_expansion_count", 0),
        "post_score_gap_expansion_count": diagnostics.get("post_score_gap_expansion_count", 0),
        "post_score_gap_expansion_status": diagnostics.get("post_score_gap_expansion_status", "not_attempted"),
        "post_score_gap_expansion_queries": diagnostics.get("post_score_gap_expansion_queries", ()),
        "post_score_gap_warning_reason": diagnostics.get("post_score_gap_warning_reason"),
        "material_score_gap_unresolved_gaps": diagnostics.get("material_score_gap_unresolved_gaps", ()),
        "failed_green_gates": diagnostics.get("failed_green_gates", ()),
        "stage_gate_diagnostics": diagnostics.get("stage_gate_diagnostics"),
        "status": (
            _score_blocked_status(blocked_reason)
            if not score_valid_bool
            else "evidence_pending_expansion"
            if evidence_count <= 0 and not result.score.evidence_ids
            else "evidence_found"
        ),
    }


def _result_score_valid(result: WebResearchPipelineResult) -> bool:
    base_valid = is_score_valid(result.score)
    value = result.theme_route_diagnostics.get("score_valid")
    if value is None:
        return base_valid
    if isinstance(value, bool):
        return base_valid and value
    if isinstance(value, (int, float)):
        return base_valid and float(value) > 0.0
    lowered = str(value).strip().lower()
    if lowered in {"false", "0", "no", "invalid", "blocked"}:
        return False
    if lowered in {"true", "1", "yes", "valid"}:
        return base_valid
    return base_valid


def _score_blocked_status(reason: str | None) -> str:
    if reason and str(reason).startswith("score_gap"):
        return "score_blocked_score_gap"
    if reason and str(reason).startswith("asof_web"):
        return "score_blocked_asof_web"
    return "score_blocked_theme_route"


def _score_variability_drivers(
    result: WebResearchPipelineResult,
    *,
    score_valid: bool,
    blocked_reason: str | None,
    evidence_count: int,
    input_fingerprint: str | None = None,
) -> tuple[str, ...]:
    return build_score_variability_drivers(
        result.score,
        score_valid=score_valid,
        blocked_reason=blocked_reason,
        route_diagnostics=result.theme_route_diagnostics,
        input_counts=_feature_input_count_row(result.feature_input),
        evidence_count=evidence_count,
        expansion_query_count=len(result.expansion_queries_run),
        scoring_canonical_archetype_id=result.feature_result.payload.canonical_archetype_id,
        input_fingerprint=input_fingerprint,
    )


def _research_input_fingerprint(result: WebResearchPipelineResult, combined_evidence: Sequence[Evidence] = ()) -> str:
    evidence = tuple(_dedupe_evidence(tuple(combined_evidence))) if combined_evidence else tuple(result.web_result.evidence)
    return research_input_fingerprint(
        score=result.score,
        evidence=evidence,
        queries=result.web_result.queries_run,
        route_diagnostics=result.theme_route_diagnostics,
        input_counts=_feature_input_count_row(result.feature_input),
        source_fields=result.feature_result.source_fields,
        extra={
            "expansion_queries": tuple(result.expansion_queries_run),
            "search_results": tuple(_search_result_fingerprint_row(item) for item in getattr(result.web_result, "search_results", ())),
            "scoring_large_sector_id": result.feature_result.payload.large_sector_id,
            "scoring_canonical_archetype_id": result.feature_result.payload.canonical_archetype_id,
        },
    )


def _search_result_fingerprint_row(item: SearchResult) -> Mapping[str, Any]:
    return {
        "query": item.query,
        "rank": item.rank,
        "title": item.title,
        "url": item.url,
        "source": item.source,
        "published_at": item.published_at.isoformat() if item.published_at is not None else None,
        "is_report_domain": item.is_report_domain,
        "is_news": item.is_news,
        "is_disclosure": item.is_disclosure,
        "date_verified": item.date_verified,
        "green_allowed_by_date": item.green_allowed_by_date,
    }


def _estimate_quality_row(result: WebResearchPipelineResult) -> Mapping[str, Any]:
    diagnostics = result.score.diagnostic_scores
    source_fields = result.feature_result.source_fields
    return {
        "selected_eps_source": source_fields.get("estimate_selected_eps_source"),
        "selected_op_source": source_fields.get("estimate_selected_op_source"),
        "selected_fcf_source": source_fields.get("estimate_selected_fcf_source"),
        "selected_target_price_source": source_fields.get("estimate_selected_target_price_source"),
        "selected_revision_source": source_fields.get("estimate_selected_revision_source"),
        "selected_eps_source_quality": diagnostics.get("estimate_selected_eps_source_quality"),
        "selected_revision_source_quality": diagnostics.get("estimate_selected_revision_source_quality"),
        "conflict_count_capped": diagnostics.get("estimate_conflict_count_capped", 0.0),
        "proxy_quarantined_count_capped": diagnostics.get("estimate_proxy_quarantined_count_capped", 0.0),
        "revision_outlier_count_capped": diagnostics.get("estimate_revision_outlier_count_capped", 0.0),
    }


def _feature_input_count_row(feature_input: FeatureEngineeringInput) -> Mapping[str, int]:
    return {
        "price_bars": len(feature_input.price_bars),
        "financial_actuals": len(feature_input.financial_actuals),
        "consensus": len(feature_input.consensus),
        "consensus_revisions": len(feature_input.consensus_revisions),
        "disclosures": len(feature_input.disclosures),
        "research_reports": len(feature_input.research_reports),
        "news_items": len(feature_input.news_items),
        "agent_extracted_fields": len(feature_input.agent_extracted_fields),
    }


def _score_component_row(score: ScoreSnapshot) -> Mapping[str, float]:
    return {
        "eps_fcf_explosion_score": score.eps_fcf_explosion_score,
        "earnings_visibility_score": score.earnings_visibility_score,
        "bottleneck_pricing_score": score.bottleneck_pricing_score,
        "market_mispricing_score": score.market_mispricing_score,
        "valuation_rerating_score": score.valuation_rerating_score,
        "capital_allocation_score": score.capital_allocation_score,
        "information_confidence_score": score.information_confidence_score,
        "risk_penalty": score.risk_penalty,
    }


def _raw_score_component_row(score: ScoreSnapshot) -> Mapping[str, float] | None:
    diagnostics = score.diagnostic_scores
    for suffix in ("theme_route_block", "score_gap_block", "asof_web_block"):
        total_key = f"raw_score_total_before_{suffix}"
        if total_key not in diagnostics:
            continue
        return {
            "eps_fcf_explosion_score": _diagnostic_float(diagnostics.get(f"raw_eps_fcf_before_{suffix}")),
            "earnings_visibility_score": _diagnostic_float(diagnostics.get(f"raw_earnings_visibility_before_{suffix}")),
            "bottleneck_pricing_score": _diagnostic_float(diagnostics.get(f"raw_bottleneck_pricing_before_{suffix}")),
            "market_mispricing_score": _diagnostic_float(diagnostics.get(f"raw_market_mispricing_before_{suffix}")),
            "valuation_rerating_score": _diagnostic_float(diagnostics.get(f"raw_valuation_rerating_before_{suffix}")),
            "capital_allocation_score": _diagnostic_float(diagnostics.get(f"raw_capital_allocation_before_{suffix}")),
            "information_confidence_score": _diagnostic_float(diagnostics.get(f"raw_information_confidence_before_{suffix}")),
            "risk_penalty": _diagnostic_float(diagnostics.get(f"raw_risk_penalty_before_{suffix}")),
        }
    return None


def _diagnostic_float(value: object) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def _theme_route_row(candidate: CheapScanCandidate, result: WebResearchPipelineResult) -> Mapping[str, Any]:
    diagnostics = result.theme_route_diagnostics
    route = result.theme_route
    return {
        "symbol": candidate.symbol,
        "company_name": candidate.company_name,
        "candidate_source_path": candidate.candidate_source_path,
        "theme_rebalance_status": diagnostics.get("theme_rebalance_status"),
        "theme_route_status": diagnostics.get("theme_route_status"),
        "theme_route_confidence": diagnostics.get("theme_route_confidence"),
        "emerging_theme_id": diagnostics.get("emerging_theme_id"),
        "primary_route_id": diagnostics.get("primary_route_id"),
        "expansion_query_count": diagnostics.get("expansion_query_count", 0),
        "post_parse_gap_expansion_count": diagnostics.get("post_parse_gap_expansion_count", 0),
        "missing_information": diagnostics.get("missing_information", ()),
        "blocked_reason": diagnostics.get("blocked_reason"),
        "evidence_slot_count": len(route.evidence_slots) if route is not None else 0,
    }


def _theme_expansion_query_rows(candidate: CheapScanCandidate, result: WebResearchPipelineResult) -> tuple[Mapping[str, Any], ...]:
    return tuple(
        {
            "symbol": candidate.symbol,
            "company_name": candidate.company_name,
            "query": query,
        }
        for query in result.expansion_queries_run
    )


def _theme_missing_slot_rows(candidate: CheapScanCandidate, result: WebResearchPipelineResult) -> tuple[Mapping[str, Any], ...]:
    if result.theme_route is None:
        return ()
    return tuple(
        {
            "symbol": candidate.symbol,
            "company_name": candidate.company_name,
            "slot": slot.slot,
            "status": slot.status,
            "missing_reason": slot.missing_reason,
        }
        for slot in result.theme_route.evidence_slots
        if slot.status in {"missing", "unknown", "contradicted"}
    )


def _report_radar_row(candidate: ReportRadarCandidate) -> Mapping[str, Any]:
    return {
        "company_name": candidate.company_name,
        "symbol": candidate.symbol,
        "trigger_query": candidate.trigger_query,
        "matched_title": candidate.matched_result.title,
        "matched_url": candidate.matched_result.url,
        "confidence": candidate.confidence,
        "reason_codes": candidate.reason_codes,
        "recommended_next_layer": candidate.recommended_next_layer,
    }


def _audit_summary(audit_findings: Sequence[AuditFinding], evidence: Sequence[Evidence]) -> Mapping[str, Any]:
    by_id = {item.evidence_id: item for item in evidence}
    by_source_type: Counter[str] = Counter()
    by_signal_class: Counter[str] = Counter()
    for finding in audit_findings:
        item = by_id.get(finding.evidence_id or "")
        by_source_type[item.source_type if item is not None else "unknown"] += 1
        signal_class = str((item.parsed_fields.get("signal_class") if item is not None else None) or "unknown")
        by_signal_class[signal_class] += 1
    return {
        "audit_findings_by_source_type": dict(by_source_type.most_common()),
        "audit_findings_by_signal_class": dict(by_signal_class.most_common()),
        "high_signal_audit_count": by_signal_class.get("high_signal", 0),
        "routine_audit_count": by_signal_class.get("routine", 0),
    }


def _enforce_cross_evidence_stage3_green(
    result: WebResearchPipelineResult,
    evidence: Sequence[Evidence],
    config: KoreaLiveLiteConfig,
) -> WebResearchPipelineResult:
    if not config.require_cross_evidence_for_stage3_green:
        return result
    evidence_types = _independent_evidence_types(evidence)
    if len(evidence_types) >= 2:
        return result
    if result.stage.stage not in {Stage.STAGE_3_GREEN, Stage.STAGE_3_YELLOW}:
        return result
    if (
        result.stage.stage == Stage.STAGE_3_YELLOW
        and result.score.total_score < get_active_scoring_profile().threshold("stage3_green_total_min", 85.0)
    ):
        return result
    reasons = tuple(result.stage.stage_reason)
    if _CROSS_EVIDENCE_STAGE3_GREEN_REASON in reasons:
        return result
    new_stage = replace(
        result.stage,
        stage=Stage.STAGE_3_YELLOW,
        grade="cross-evidence-required" if result.stage.stage == Stage.STAGE_3_GREEN else result.stage.grade,
        stage_reason=reasons + (_CROSS_EVIDENCE_STAGE3_GREEN_REASON,),
        evidence_ids=tuple(dict.fromkeys(result.stage.evidence_ids + tuple(item.evidence_id for item in evidence))),
    )
    return replace(result, stage=new_stage)


def _enforce_parser_audit_stage3_green(
    result: WebResearchPipelineResult,
    audit_findings: Sequence[AuditFinding],
) -> WebResearchPipelineResult:
    if result.stage.stage != Stage.STAGE_3_GREEN:
        return result
    blockers = tuple(
        finding
        for finding in audit_findings
        if finding.symbol == result.stage.symbol
        and (finding.severity == "hard" or finding.suggested_action == "block_green")
    )
    if not blockers:
        return result
    codes = ", ".join(finding.code for finding in blockers[:3])
    evidence_ids = tuple(finding.evidence_id for finding in blockers if finding.evidence_id)
    new_stage = replace(
        result.stage,
        stage=Stage.STAGE_3_YELLOW,
        grade="parser-audit-blocked",
        stage_reason=tuple(result.stage.stage_reason) + (f"parser audit blocked Stage 3-Green: {codes}",),
        evidence_ids=tuple(dict.fromkeys(result.stage.evidence_ids + evidence_ids)),
    )
    return replace(result, stage=new_stage)


def _independent_evidence_types(evidence: Sequence[Evidence]) -> tuple[str, ...]:
    accepted = {"disclosure", "research_report", "news", "financial_actual", "consensus", "consensus_revision"}
    return tuple(
        sorted(
            {
                _independent_evidence_type(item)
                for item in evidence
                if item.source_type in accepted
                and item.parsed_fields.get("signal_class") != "routine"
                and not item.parsed_fields.get("test_injected")
                and not item.parsed_fields.get("search_snippet_only")
                and not item.parsed_fields.get("search_snippet_date_unverified")
                and item.parsed_fields.get("green_allowed_by_date", True) is not False
            }
        )
    )


def _independent_evidence_type(item: Evidence) -> str:
    if item.parsed_fields.get("derived_from_source_type") == "research_report":
        return "research_report"
    return item.source_type


def _cheap_scan_evidence_by_id(
    sources: KoreaCheapScanSources,
    date_disclosures: Sequence[DisclosureEvent],
    as_of_date: date,
) -> dict[str, Evidence]:
    evidence: dict[str, Evidence] = {}
    for item in date_disclosures:
        ev = OpenDARTConnector.to_evidence(item, Market.KR)
        evidence[ev.evidence_id] = ev
    if sources.kind is not None:
        for record in sources.kind.get_risk_records(as_of_date=as_of_date):
            ev = KINDConnector.to_evidence(record)
            evidence[ev.evidence_id] = ev
    return evidence


def _skipped_query_rows(candidate: CheapScanCandidate, result: WebResearchPipelineResult) -> tuple[Mapping[str, Any], ...]:
    return tuple(
        {
            "symbol": candidate.symbol,
            "company_name": candidate.company_name,
            "query": item.query,
            "layer": item.layer.value,
            "reason": item.reason,
        }
        for item in result.skipped_queries
    )


def _dropped_result_rows(candidate: CheapScanCandidate, result: WebResearchPipelineResult) -> tuple[Mapping[str, Any], ...]:
    return tuple(
        {
            "symbol": candidate.symbol,
            "company_name": candidate.company_name,
            "title": item.result.title,
            "url": item.result.url,
            "reason": item.reason,
        }
        for item in result.web_result.dropped_results
    )


def _instruments_from_scan_sources(
    sources: KoreaCheapScanSources,
    as_of_date: date,
    universe_limit: int | None,
) -> tuple[Instrument, ...]:
    instruments = sources.list_instruments(Market.KR, as_of_date)
    if universe_limit is not None:
        instruments = instruments[:universe_limit]
    return instruments


def _missing_credentials(config: KoreaLiveLiteConfig) -> tuple[str, ...]:
    if not config.live_enabled:
        return ()
    missing: list[str] = []
    if not os.environ.get("OPENDART_API_KEY"):
        missing.append("OPENDART_API_KEY")
    if not (os.environ.get("KRX_OPENAPI_KEY") or os.environ.get("DATA_GO_KR_SERVICE_KEY")):
        missing.append("KRX_OPENAPI_KEY or DATA_GO_KR_SERVICE_KEY")
    if not os.environ.get("NAVER_CLIENT_ID"):
        missing.append("NAVER_CLIENT_ID")
    if not os.environ.get("NAVER_CLIENT_SECRET"):
        missing.append("NAVER_CLIENT_SECRET")
    return tuple(missing)


def _initial_source_status(config: KoreaLiveLiteConfig, missing_credentials: Sequence[str]) -> tuple[dict[str, str], dict[str, str], tuple[str, ...]]:
    sources = ("opendart", "krx", "data_go_kr", "naver_search", "company_guide")
    if config.fixture_mode or not config.live_enabled:
        return {source: "fixture" for source in sources}, {}, ()
    if missing_credentials:
        fallback_reasons = {source: "missing_credentials" for source in sources}
        return {source: "fallback" for source in sources}, fallback_reasons, ()
    return (
        {
            "opendart": "request_only",
            "krx": "request_only",
            "data_go_kr": "request_only",
            "naver_search": "request_only",
            "company_guide": "request_only",
        },
        {},
        ("krx", "data_go_kr"),
    )


def _run_notes(config: KoreaLiveLiteConfig, effective_fixture_mode: bool) -> tuple[str, ...]:
    notes = ["live calls are optional and fixture mode is the default"]
    if not config.allow_parallel_live_requests:
        notes.append("live HTTP execution defaults to serial source calls")
    if not config.enable_stock_issuance_source:
        notes.append("stock issuance API is disabled_optional; dilution risk uses OpenDART, FSC disclosure info, and Naver search fallback")
    if config.company_guide_enabled:
        notes.append("CompanyGuide/WiseReport enrichment is enabled for selected candidates; license metadata is operator-review only")
    if effective_fixture_mode:
        notes.append("running in fixture/fallback mode")
    if config.require_cross_evidence_for_stage3_green:
        notes.append("Stage 3-Green requires at least two independent evidence types")
    if config.theme_rebalance_enabled:
        notes.append("theme rebalance is enabled; LLM route can expand searches but deterministic rules still decide Stage")
    if _live_page_fetch_enabled(config):
        notes.append("live page fetch is enabled for selected search results")
    return tuple(notes)


def _audit_notes(audit_findings: Sequence[AuditFinding]) -> tuple[str, ...]:
    if not audit_findings:
        return ()
    notes = []
    if any(finding.severity == "hard" or finding.suggested_action == "block_green" for finding in audit_findings):
        notes.append("parser audit hard finding present; Stage 3-Green is blocked for affected symbols")
    if any(finding.suggested_action in {"manual_review", "downgrade_to_yellow", "block_green"} for finding in audit_findings):
        notes.append("manual_review_required: parser audit findings need review")
    return tuple(dict.fromkeys(notes))


def _safe_filename(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9가-힣._-]+", "_", value).strip("_")[:80] or "query"


def _score_state_contract_findings_for_outputs(
    *,
    as_of_date: date,
    candidates: Sequence[CheapScanCandidate],
    targeted_smoke_results: Sequence[Mapping[str, Any]],
) -> tuple[str, ...]:
    candidate_payload = _jsonable({"as_of_date": as_of_date, "candidates": tuple(candidates)})
    candidate_rows = candidate_payload.get("candidates", ()) if isinstance(candidate_payload, Mapping) else ()
    findings = (
        find_score_state_contract_violations(
            candidate_rows,
            path="candidates",
            include_score_only=True,
            require_visible_score_field=True,
        )
        + find_score_state_contract_violations(
            targeted_smoke_results,
            path="targeted_smoke_results",
            include_score_only=True,
            require_visible_score_field=True,
        )
    )
    return tuple(f"{finding.path}:{finding.violation}" for finding in findings)


def _write_outputs(
    *,
    config: KoreaLiveLiteConfig,
    cheap_scan: KoreaCheapScanResult,
    candidates: Sequence[CheapScanCandidate],
    evidence: Sequence[Evidence],
    morning_brief: MorningBrief,
    run_log: KoreaLiveLiteRunLog,
) -> tuple[Path, Path, Path, Path]:
    output_dir = Path(config.output_directory) / "korea_live_lite"
    output_dir.mkdir(parents=True, exist_ok=True)
    stem = config.as_of_date.isoformat()
    candidates_path = output_dir / f"{stem}_candidates.json"
    evidence_path = output_dir / f"{stem}_evidence.json"
    brief_path = output_dir / f"{stem}_brief.md"
    run_log_path = output_dir / f"{stem}_run_log.json"
    candidates_path.write_text(
        json.dumps(_jsonable({"as_of_date": config.as_of_date, "candidates": tuple(candidates)}), ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    evidence_path.write_text(
        json.dumps(_jsonable({"as_of_date": config.as_of_date, "evidence": tuple(evidence)}), ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    brief_path.write_text(morning_brief.text, encoding="utf-8")
    run_log_path.write_text(json.dumps(_jsonable(run_log), ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    return candidates_path, evidence_path, brief_path, run_log_path


def _prepare_phase_log(config: KoreaLiveLiteConfig) -> Path | None:
    if not config.phase_log_enabled:
        return None
    output_dir = Path(config.output_directory) / "korea_live_lite"
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{config.as_of_date.isoformat()}_phase_log.jsonl"
    path.write_text("", encoding="utf-8")
    return path


def _phase_event_sink(path: Path | None) -> Callable[[Mapping[str, Any]], None] | None:
    if path is None:
        return None

    def _append(event: Mapping[str, Any]) -> None:
        row = {
            "observed_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
            **dict(event),
        }
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(_jsonable(row), ensure_ascii=False, sort_keys=True) + "\n")

    return _append


def _write_calibration_outputs(
    config: KoreaLiveLiteConfig,
    cheap_scan: KoreaCheapScanResult,
) -> tuple[Path | None, Path | None]:
    if cheap_scan.calibration is None:
        return None, None
    output_dir = Path(config.output_directory) / "korea_live_lite"
    output_dir.mkdir(parents=True, exist_ok=True)
    stem = config.as_of_date.isoformat()
    json_path = output_dir / f"{stem}_cheap_scan_calibration.json"
    md_path = output_dir / f"{stem}_cheap_scan_calibration.md"
    json_path.write_text(json.dumps(_jsonable(cheap_scan.calibration), ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    md_path.write_text(_render_calibration_markdown(cheap_scan), encoding="utf-8")
    return json_path, md_path


def _render_calibration_markdown(cheap_scan: KoreaCheapScanResult) -> str:
    report = cheap_scan.calibration
    if report is None:
        return "# Korea Cheap Scan Calibration\n\n(no calibration report)\n"
    lines = [
        "# Korea Cheap Scan Calibration",
        "",
        f"- as_of_date: {report.as_of_date.isoformat()}",
        f"- instruments_scanned: {report.instruments_scanned}",
        f"- candidate_count: {report.candidate_count}",
        f"- event_search_count: {report.event_search_count}",
        f"- deep_research_count: {report.deep_research_count}",
        "",
        "## Reason Codes",
        "",
    ]
    lines.extend(f"- {key}: {value}" for key, value in report.reason_code_distribution.items())
    lines.extend(["", "## Diagnostic Reasons", ""])
    lines.extend(f"- {key}: {value}" for key, value in report.diagnostic_reason_distribution.items())
    lines.extend(["", "## Near Miss Top 50", "", "| symbol | company | cheap_scan_score | reasons |", "| --- | --- | ---: | --- |"])
    for item in report.near_miss_top_50:
        lines.append(f"| {item.symbol} | {item.company_name} | {item.cheap_scan_total_score:.2f} | {', '.join(item.diagnostic_reasons)} |")
    return "\n".join(lines).rstrip() + "\n"


def _dedupe_evidence(items: Sequence[Evidence]) -> tuple[Evidence, ...]:
    unique: dict[str, Evidence] = {}
    for item in items:
        unique.setdefault(_evidence_dedupe_key(item), item)
    return tuple(unique.values())


def _evidence_dedupe_key(item: Evidence) -> str:
    if item.source_type == "disclosure" and item.url_or_identifier:
        return f"disclosure:{item.symbol}:{item.url_or_identifier}"
    if item.source_type in {"news", "research_report"}:
        source_url = str(item.parsed_fields.get("source_url") or item.parsed_fields.get("url") or "").strip()
        if source_url:
            return f"{item.source_type}:{item.symbol}:{source_url}"
    return item.evidence_id


def _jsonable(value: Any) -> Any:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, SourceRequest):
        return {
            "method": value.method,
            "url": value.url,
            "params": _redacted_mapping(value.params),
            "headers": _redacted_mapping(value.headers),
            "fixture_mode": value.fixture_mode,
            "credential_name": value.credential_name,
        }
    if is_dataclass(value):
        return {field.name: _jsonable(getattr(value, field.name)) for field in fields(value)}
    if isinstance(value, Mapping):
        return normalized_score_state_mapping_if_present({str(key): _jsonable(item) for key, item in value.items()})
    if isinstance(value, (list, tuple, set, frozenset)):
        return [_jsonable(item) for item in value]
    return value


def _redacted_mapping(value: Mapping[str, Any]) -> dict[str, Any]:
    redacted: dict[str, Any] = {}
    for key, item in value.items():
        lowered = str(key).lower()
        if any(token in lowered for token in ("key", "secret", "token", "client-id", "client_secret", "crtfc")):
            redacted[str(key)] = "<redacted>"
        else:
            redacted[str(key)] = _jsonable(item)
    return redacted


__all__ = [
    "KoreaLiveLiteBudget",
    "KoreaLiveLiteConfig",
    "KoreaLiveLiteResult",
    "KoreaLiveLiteRunLog",
    "KoreaLiveLiteRunner",
    "SkippedCandidate",
    "build_opendart_date_range_requests",
    "fixture_sources",
    "plan_opendart_detail_fetches",
]
