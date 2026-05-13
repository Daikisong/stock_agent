"""Controlled Korea live-lite pilot runner."""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass, field, fields, is_dataclass, replace
from datetime import date, datetime, timedelta
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.briefing import MorningBrief, generate_morning_briefing
from e2r.cheap_scan import KoreaCheapScanConfig, KoreaCheapScanResult, KoreaCheapScanSources, KoreaCheapScanner
from e2r.cheap_scan.korea_sources import DataGoKrFSCConnector
from e2r.cheap_scan.models import CheapScanCandidate, RecommendedNextLayer
from e2r.cheap_scan.query_escalation import EscalationQueryPlanner, queries_for_candidate
from e2r.models import DisclosureEvent, Evidence, Instrument, Market, RedTeamFinding, ScoreSnapshot, Stage, StageSnapshot
from e2r.research.free_web_research_runner import FreeWebResearchInput, FreeWebResearchRunner, WebResearchPipelineResult
from e2r.research.naver_search_provider import NaverFreeSearchProvider
from e2r.research.search_budget import SearchBudget
from e2r.research.search_provider import EmptySearchProvider, SearchProvider, SearchResult
from e2r.sources import KINDConnector, KRXConnector, OpenDARTConnector
from e2r.sources.http_client import HttpClient, HttpClientStats
from e2r.sources.source_errors import SourceRequest, load_fixture_records


DEFAULT_FIXTURE_ROOT = Path("data/raw/korea_cheap_scan")


@dataclass(frozen=True)
class KoreaLiveLiteBudget:
    """Strict source and research caps for a Korea live-lite run."""

    max_opendart_calls_per_day: int = 1_000
    max_krx_calls_per_day: int = 500
    max_data_go_kr_calls_per_day: int = 500
    max_naver_search_calls_per_day: int = 2_000
    max_symbols_for_event_search: int = 200
    max_symbols_for_deep_research: int = 30

    def __post_init__(self) -> None:
        for field_name in (
            "max_opendart_calls_per_day",
            "max_krx_calls_per_day",
            "max_data_go_kr_calls_per_day",
            "max_naver_search_calls_per_day",
            "max_symbols_for_event_search",
            "max_symbols_for_deep_research",
        ):
            if getattr(self, field_name) < 0:
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
    top_candidates: int = 50
    disclosure_lookback_days: int = 1
    lookback_days: int = 370
    browser_provider: SearchProvider | None = None
    free_search_provider: SearchProvider | None = None
    fixture_text_by_url: Mapping[str, str | Path] = field(default_factory=dict)
    max_results_per_query: int = 5
    top_results: int = 8
    require_cross_evidence_for_stage3_green: bool = True
    http_client: HttpClient | None = None
    cache_directory: str | Path = "data/cache"

    def __post_init__(self) -> None:
        if type(self.as_of_date) is not date:
            raise ValueError("as_of_date must be a date")
        if self.universe_limit is not None and self.universe_limit <= 0:
            raise ValueError("universe_limit must be positive when set")
        if self.top_candidates <= 0:
            raise ValueError("top_candidates must be positive")
        if self.disclosure_lookback_days < 0:
            raise ValueError("disclosure_lookback_days must be non-negative")
        if self.lookback_days <= 0:
            raise ValueError("lookback_days must be positive")
        if self.max_results_per_query <= 0:
            raise ValueError("max_results_per_query must be positive")
        if self.top_results <= 0:
            raise ValueError("top_results must be positive")


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


class KoreaLiveLiteRunner:
    """Run Korea cheap scan plus budgeted free web research."""

    def __init__(self, sources: KoreaCheapScanSources | None = None) -> None:
        self._sources = sources or fixture_sources()

    def run(self, config: KoreaLiveLiteConfig) -> KoreaLiveLiteResult:
        missing_credentials = _missing_credentials(config)
        effective_fixture_mode = config.fixture_mode or (config.live_enabled and bool(missing_credentials))
        sources = config.sources or self._sources
        http_client = config.http_client or HttpClient()
        source_modes, fallback_reasons, request_only_sources = _initial_source_status(config, missing_credentials)
        start = config.as_of_date - timedelta(days=config.disclosure_lookback_days)
        built_requests: list[SourceRequest] = []
        source_call_counts: dict[str, int] = {
            "opendart_disclosure_date_range": 0,
            "opendart_symbol_disclosure_calls": 0,
            "krx_calls": 0,
            "data_go_kr_calls": 0,
            "naver_search_queries": 0,
        }

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
        scan_sources = _sources_with_date_disclosures(sources, date_disclosures)
        cheap_scan = KoreaCheapScanner(scan_sources).run(
            KoreaCheapScanConfig(
                as_of_date=config.as_of_date,
                markets=(Market.KR,),
                sources=scan_sources,
                universe_limit=config.universe_limit,
                lookback_days=config.lookback_days,
                disclosure_lookback_days=config.disclosure_lookback_days,
                top_n=config.top_candidates,
            )
        )
        _record_estimated_source_calls(source_call_counts, sources, cheap_scan.instruments_scanned)
        cheap_evidence = _cheap_scan_evidence_by_id(sources, date_disclosures, config.as_of_date)
        selected_candidates, skipped_candidate_items = _select_candidates_for_research(cheap_scan.candidates, config.budget)

        web_results: list[WebResearchPipelineResult] = []
        skipped_candidates = list(skipped_candidate_items)
        skipped_queries: list[Mapping[str, Any]] = []
        dropped_results: list[Mapping[str, Any]] = []
        free_search_provider = _free_search_provider(config, http_client, source_modes, fallback_reasons)
        for candidate in selected_candidates:
            remaining_queries = config.budget.max_naver_search_calls_per_day - source_call_counts["naver_search_queries"]
            if remaining_queries <= 0:
                skipped_candidates.append(_skip(candidate, "naver_search_budget_exhausted"))
                continue
            runner = FreeWebResearchRunner(
                browser_provider=config.browser_provider or EmptySearchProvider(),
                free_search_provider=free_search_provider,
                query_planner=EscalationQueryPlanner(candidate),
            )
            result = runner.run(
                FreeWebResearchInput(
                    company_name=candidate.company_name,
                    symbol=candidate.symbol,
                    sector=None,
                    market=candidate.market,
                    as_of_date=candidate.as_of_date,
                    budget=_search_budget(config.budget, remaining_queries),
                    max_results_per_query=config.max_results_per_query,
                    top_results=config.top_results,
                    fixture_text_by_url=config.fixture_text_by_url,
                )
            )
            source_call_counts["naver_search_queries"] += result.budget_tracker.total_queries_used
            combined_evidence = tuple(cheap_evidence.get(evidence_id) for evidence_id in candidate.evidence_ids)
            combined_evidence = tuple(item for item in combined_evidence if item is not None) + tuple(result.web_result.evidence)
            result = _enforce_cross_evidence_stage3_green(result, combined_evidence, config)
            web_results.append(result)
            skipped_queries.extend(_skipped_query_rows(candidate, result))
            dropped_results.extend(_dropped_result_rows(candidate, result))

        evidence = _dedupe_evidence(
            tuple(cheap_evidence.values()) + tuple(item for result in web_results for item in result.web_result.evidence)
        )
        scores = tuple(result.score for result in web_results)
        stages = tuple(result.stage for result in web_results)
        findings = tuple(finding for result in web_results for finding in result.red_team_findings)
        instruments = _instruments_from_scan_sources(scan_sources, config.as_of_date, config.universe_limit)
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
            request_only_sources=tuple(dict.fromkeys(request_only_sources)),
            notes=_run_notes(config, effective_fixture_mode),
        )
        candidates_path, evidence_path, brief_path, run_log_path = _write_outputs(
            config=config,
            cheap_scan=cheap_scan,
            evidence=evidence,
            morning_brief=morning_brief,
            run_log=run_log,
        )
        return KoreaLiveLiteResult(
            as_of_date=config.as_of_date,
            cheap_scan=cheap_scan,
            candidates=cheap_scan.candidates,
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
            run_log=run_log,
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
    max_pages = max(1, config.budget.max_opendart_calls_per_day)
    disclosures: list[DisclosureEvent] = []
    page_no = 1
    while page_no <= max_pages:
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
) -> None:
    if sources.krx is not None:
        source_call_counts["krx_calls"] = 1 + instruments_scanned
    if sources.fsc is not None:
        source_call_counts["data_go_kr_calls"] = 1 + instruments_scanned


def _select_candidates_for_research(
    candidates: Sequence[CheapScanCandidate],
    budget: KoreaLiveLiteBudget,
) -> tuple[tuple[CheapScanCandidate, ...], tuple[SkippedCandidate, ...]]:
    selected: list[CheapScanCandidate] = []
    skipped: list[SkippedCandidate] = []
    event_symbols = 0
    deep_symbols = 0
    for candidate in candidates:
        if candidate.recommended_next_layer == RecommendedNextLayer.NONE:
            skipped.append(_skip(candidate, "next_layer_none_or_hard_risk"))
            continue
        if not queries_for_candidate(candidate).queries:
            skipped.append(_skip(candidate, "no_escalation_queries"))
            continue
        if candidate.recommended_next_layer == RecommendedNextLayer.DEEP_RESEARCH:
            if deep_symbols >= budget.max_symbols_for_deep_research:
                skipped.append(_skip(candidate, "deep_research_symbol_budget_exhausted"))
                continue
            deep_symbols += 1
            selected.append(candidate)
            continue
        if event_symbols >= budget.max_symbols_for_event_search:
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

    def search(self, query: str, as_of_date: date, max_results: int = 10) -> tuple[SearchResult, ...]:
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


def _search_budget(budget: KoreaLiveLiteBudget, remaining_queries: int) -> SearchBudget:
    return SearchBudget(
        max_total_queries_per_day=max(0, remaining_queries),
        max_queries_per_symbol=40,
        max_deep_research_symbols=budget.max_symbols_for_deep_research,
        max_active_monitoring_symbols=0,
        sleep_seconds_between_queries=0.0,
        stop_on_captcha_or_block=True,
    )


def _enforce_cross_evidence_stage3_green(
    result: WebResearchPipelineResult,
    evidence: Sequence[Evidence],
    config: KoreaLiveLiteConfig,
) -> WebResearchPipelineResult:
    if not config.require_cross_evidence_for_stage3_green:
        return result
    if result.stage.stage != Stage.STAGE_3_GREEN:
        return result
    evidence_types = _independent_evidence_types(evidence)
    if len(evidence_types) >= 2:
        return result
    new_stage = replace(
        result.stage,
        stage=Stage.STAGE_3_YELLOW,
        grade="cross-evidence-required",
        stage_reason=tuple(result.stage.stage_reason)
        + ("live-lite Stage 3-Green requires at least two independent evidence types",),
        evidence_ids=tuple(dict.fromkeys(result.stage.evidence_ids + tuple(item.evidence_id for item in evidence))),
    )
    return replace(result, stage=new_stage)


def _independent_evidence_types(evidence: Sequence[Evidence]) -> tuple[str, ...]:
    accepted = {"disclosure", "research_report", "news", "financial_actual", "consensus", "consensus_revision"}
    return tuple(sorted({item.source_type for item in evidence if item.source_type in accepted}))


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
    sources = ("opendart", "krx", "data_go_kr", "naver_search")
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
        },
        {},
        ("krx", "data_go_kr"),
    )


def _run_notes(config: KoreaLiveLiteConfig, effective_fixture_mode: bool) -> tuple[str, ...]:
    notes = ["live calls are optional and fixture mode is the default"]
    if effective_fixture_mode:
        notes.append("running in fixture/fallback mode")
    if config.require_cross_evidence_for_stage3_green:
        notes.append("Stage 3-Green requires at least two independent evidence types")
    return tuple(notes)


def _safe_filename(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9가-힣._-]+", "_", value).strip("_")[:80] or "query"


def _write_outputs(
    *,
    config: KoreaLiveLiteConfig,
    cheap_scan: KoreaCheapScanResult,
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
        json.dumps(_jsonable({"as_of_date": config.as_of_date, "candidates": cheap_scan.candidates}), ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    evidence_path.write_text(
        json.dumps(_jsonable({"as_of_date": config.as_of_date, "evidence": tuple(evidence)}), ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    brief_path.write_text(morning_brief.text, encoding="utf-8")
    run_log_path.write_text(json.dumps(_jsonable(run_log), ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    return candidates_path, evidence_path, brief_path, run_log_path


def _dedupe_evidence(items: Sequence[Evidence]) -> tuple[Evidence, ...]:
    unique: dict[str, Evidence] = {}
    for item in items:
        unique.setdefault(item.evidence_id, item)
    return tuple(unique.values())


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
        return {str(key): _jsonable(item) for key, item in value.items()}
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
]
