"""Retrospective as-of research replay for E2R_STANDARD.

This is the current practical historical backtest flow: start from official
historical universe/data, then reconstruct old public research with strict
document-date filtering. It is not strict forward-archive proof.
"""

from __future__ import annotations

import csv
import json
from collections import Counter
from dataclasses import dataclass, field, fields, is_dataclass
from datetime import date, datetime, timedelta
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.backtest.benchmark_labels import BenchmarkLabel, labels_for_market, load_benchmark_labels
from e2r.backtest.asof_evidence_bundle import (
    AsOfEvidenceBundleScore,
    build_asof_evidence_bundle,
    score_asof_evidence_bundle,
)
from e2r.backtest.historical_official_store import (
    DEFAULT_HISTORICAL_OFFICIAL_ROOT,
    HistoricalOfficialSources,
    HistoricalOfficialStore,
)
from e2r.backtest.historical_universe_replay import ReplayFrequency
from e2r.backtest.runtime_fixture_evidence import RuntimeFixtureEvidenceStore
from e2r.cheap_scan import KoreaCheapScanConfig, KoreaCheapScanner
from e2r.cheap_scan.models import CheapScanCandidate, RecommendedNextLayer
from e2r.llm import build_default_codex_theme_route_provider, build_theme_route_provider_from_env
from e2r.llm.theme_provider import ThemeRouteProvider
from e2r.models import Instrument, Market, ScoreContribution, Stage
from e2r.research.asof_web_research import (
    AsOfDateFilteredSearchProvider,
    AsOfWebResearchConfig,
    AsOfWebResearchResult,
    AsOfWebResearchRunner,
    RetrospectiveSnapshotSearchProvider,
    fixture_text_by_url_for_candidate,
)
from e2r.research.report_radar import ReportRadar
from e2r.research.report_snapshot_store import ReportSnapshotStore
from e2r.research.search_budget import SearchBudget
from e2r.research.search_provider import EmptySearchProvider, SearchProvider
from e2r.research.search_snapshot_store import SearchSnapshotStore
from e2r.score_validity import (
    is_score_valid,
    normalized_score_state_mapping_if_present,
    normalized_score_state_payload,
    research_input_fingerprint,
    score_block_reason,
    score_fingerprint,
    score_variability_drivers,
    visible_score_total,
)
from e2r.stage_gate_diagnostics import promotion_band


DEFAULT_ASOF_REPLAY_OUTPUT_DIR = Path("output/backtests/asof_research_replay")


@dataclass(frozen=True)
class AsOfResearchReplayConfig:
    """Configuration for retrospective as-of research replay."""

    start_date: date
    end_date: date
    frequency: ReplayFrequency | str = ReplayFrequency.MONTHLY
    market: Market | str = Market.KR
    output_directory: str | Path = DEFAULT_ASOF_REPLAY_OUTPUT_DIR
    official_root: str | Path = DEFAULT_HISTORICAL_OFFICIAL_ROOT
    benchmark_label_path: str | Path = "data/benchmark_labels/e2r_known_winners.json"
    search_snapshot_root: str | Path = "data/search_snapshots"
    report_snapshot_root: str | Path = "data/report_snapshots"
    universe_limit: int | None = None
    max_candidates_per_date: int | None = None
    max_web_research_candidates_per_date: int | None = None
    max_queries_per_candidate: int | None = None
    max_results_per_query: int = 100
    require_date_verified_for_green: bool = True
    allow_undated_docs_for_yellow_only: bool = True
    save_reconstructed_snapshots: bool = False
    dry_run: bool = False
    live_search: bool = False
    fixture_search: bool = True
    allow_snapshot_derived_universe: bool = False
    allow_live_historical_official_fetch: bool = False
    save_official_history_cache: bool = False
    theme_rebalance_enabled: bool | None = None
    theme_route_provider: ThemeRouteProvider | None = None
    max_theme_expansion_rounds: int | None = None
    theme_evidence_review_enabled: bool = True
    extra_replay_dates: Sequence[date | str] = ()
    runtime_fixture_spec_paths: Sequence[str | Path] = ()

    def __post_init__(self) -> None:
        if not isinstance(self.frequency, ReplayFrequency):
            object.__setattr__(self, "frequency", ReplayFrequency(str(self.frequency)))
        if not isinstance(self.market, Market):
            object.__setattr__(self, "market", Market(str(self.market)))
        if self.end_date < self.start_date:
            raise ValueError("end_date cannot be before start_date")
        extra_replay_dates = tuple(_normalise_extra_replay_date(item) for item in self.extra_replay_dates)
        out_of_range = [item for item in extra_replay_dates if item < self.start_date or item > self.end_date]
        if out_of_range:
            raise ValueError("extra_replay_dates must be within start_date and end_date")
        object.__setattr__(self, "extra_replay_dates", extra_replay_dates)
        object.__setattr__(self, "runtime_fixture_spec_paths", tuple(self.runtime_fixture_spec_paths or ()))
        if self.max_candidates_per_date is not None and self.max_candidates_per_date <= 0:
            raise ValueError("max_candidates_per_date must be positive")
        if self.max_web_research_candidates_per_date is not None and self.max_web_research_candidates_per_date < 0:
            raise ValueError("max_web_research_candidates_per_date cannot be negative")
        if self.max_queries_per_candidate is not None and self.max_queries_per_candidate < 0:
            raise ValueError("max_queries_per_candidate cannot be negative")
        if self.max_theme_expansion_rounds is not None and self.max_theme_expansion_rounds < 0:
            raise ValueError("max_theme_expansion_rounds must be non-negative")


@dataclass(frozen=True)
class FlowTraceStep:
    """One ordered step in the as-of replay trace."""

    name: str
    reached: bool
    detail: str | None = None


@dataclass(frozen=True)
class FlowTrace:
    """Replay trace for a symbol or benchmark label."""

    symbol: str
    company_name: str
    as_of_date: date
    steps: tuple[FlowTraceStep, ...]
    failure_stage: str | None = None

    def reached(self, name: str) -> bool:
        return any(item.name == name and item.reached for item in self.steps)


@dataclass(frozen=True)
class AsOfReplayCandidate:
    """Candidate produced by the as-of research replay."""

    symbol: str
    company_name: str
    as_of_date: date
    layer: str
    stage: Stage
    rank: int
    score: float | None
    evidence_types_seen: tuple[str, ...]
    reason_codes: tuple[str, ...]
    candidate_source_path: str
    large_sector_id: str | None = None
    canonical_archetype_id: str | None = None
    date_verified_documents: int = 0
    date_unverified_documents: int = 0
    rejected_future_documents: int = 0
    web_only_stage: Stage | None = None
    merged_stage: Stage | None = None
    web_only_score: float | None = None
    merged_score: float | None = None
    score_valid: bool | None = None
    score_blocked_reason: str | None = None
    score_fingerprint: str | None = None
    research_input_fingerprint: str | None = None
    score_variability_drivers: tuple[str, ...] = field(default_factory=tuple)
    web_only_score_valid: bool | None = None
    web_only_score_blocked_reason: str | None = None
    web_only_score_fingerprint: str | None = None
    web_only_research_input_fingerprint: str | None = None
    web_only_score_variability_drivers: tuple[str, ...] = field(default_factory=tuple)
    promotion_delta: str = "none"
    promotion_band: str = "Stage 1"
    score_source_mode: str = "operational_merged"
    runtime_fixture_injected: bool = False
    runtime_fixture_evidence_count: int = 0
    merged_evidence_count: int = 0
    eps_fcf_explosion_score: float | None = None
    earnings_visibility_score: float | None = None
    bottleneck_pricing_score: float | None = None
    market_mispricing_score: float | None = None
    valuation_rerating_score: float | None = None
    capital_allocation_score: float | None = None
    information_confidence_score: float | None = None
    risk_penalty: float | None = None
    claim_backed_claim_count: float | None = None
    claim_backed_primitive_count: float | None = None
    score_claim_backed_component_count: float | None = None
    orphan_score_component_count: float | None = None
    score_claim_backed_component_ratio: float | None = None
    claim_ledger_claim_ids: tuple[str, ...] = field(default_factory=tuple)
    claim_ledger_claim_ids_by_primitive: Mapping[str, tuple[str, ...]] = field(default_factory=dict)
    score_contribution_claim_ids: Mapping[str, tuple[str, ...]] = field(default_factory=dict)
    score_contribution_ledger: tuple[ScoreContribution, ...] = field(default_factory=tuple)
    source_backed_green_bridge_raw: float | None = None
    evidence_contract_required_primitive_count: float | None = None
    evidence_contract_present_primitive_count: float | None = None
    evidence_contract_missing_primitive_count: float | None = None
    evidence_contract_coverage_pct: float | None = None
    evidence_contract_positive_coverage_pct: float | None = None
    evidence_contract_positive_missing_primitive_count: float | None = None
    evidence_contract_green_gate_coverage_pct: float | None = None
    evidence_contract_green_gate_missing_primitive_count: float | None = None
    evidence_contract_guard_present_primitive_count: float | None = None
    evidence_contract_guard_cleared_primitive_count: float | None = None
    evidence_contract_guard_missing_primitive_count: float | None = None
    evidence_contract_missing_primitives: str | None = None
    evidence_contract_positive_missing_primitives: str | None = None
    evidence_contract_green_gate_primitives: str | None = None
    evidence_contract_green_gate_missing_primitives: str | None = None
    evidence_contract_guard_primitives: str | None = None
    evidence_contract_guard_present_primitives: str | None = None
    evidence_contract_guard_cleared_primitives: str | None = None
    evidence_contract_guard_missing_primitives: str | None = None
    evidence_contract_required_primitives: str | None = None
    evidence_contract_required_bridge_axes: str | None = None


@dataclass(frozen=True)
class BenchmarkAsOfRecallRow:
    """Benchmark evaluation row, applied only after replay output exists."""

    label_id: str
    symbol: str
    company_name: str
    expected_group: str
    appeared_in_candidates: bool
    first_detected_date: date | None
    first_layer: str | None
    first_stage: Stage | None
    detection_lag_days: int | None
    evidence_types_seen: tuple[str, ...]
    failure_stage: str | None = None


@dataclass(frozen=True)
class AsOfResearchReplaySnapshot:
    """One replay date output."""

    as_of_date: date
    universe_count: int
    layer1_candidates: tuple[CheapScanCandidate, ...]
    candidates: tuple[AsOfReplayCandidate, ...]
    web_research_results: tuple[AsOfWebResearchResult, ...]
    flow_traces: tuple[FlowTrace, ...]
    limitations: tuple[str, ...] = field(default_factory=tuple)
    documents_rejected_after_asof: int = 0
    documents_date_verified: int = 0
    documents_date_unverified: int = 0


@dataclass(frozen=True)
class AsOfResearchReplayResult:
    """Complete as-of research replay output."""

    config: AsOfResearchReplayConfig
    snapshots: tuple[AsOfResearchReplaySnapshot, ...]
    discovered_candidates: tuple[AsOfReplayCandidate, ...]
    benchmark_recall: tuple[BenchmarkAsOfRecallRow, ...]
    output_root: Path | None = None
    report_paths: Mapping[str, Path] = field(default_factory=dict)


class AsOfResearchReplay:
    """Run official-first retrospective as-of research replay."""

    def run(self, config: AsOfResearchReplayConfig, *, write_outputs: bool = True) -> AsOfResearchReplayResult:
        store = HistoricalOfficialStore(config.official_root)
        sources = HistoricalOfficialSources(store)
        search_store = SearchSnapshotStore(config.search_snapshot_root)
        report_store = ReportSnapshotStore(config.report_snapshot_root)
        fixture_store = RuntimeFixtureEvidenceStore(config.runtime_fixture_spec_paths)
        snapshots: list[AsOfResearchReplaySnapshot] = []
        for replay_date in _scheduled_replay_dates(
            config.start_date,
            config.end_date,
            config.frequency,
            config.extra_replay_dates,
        ):
            snapshots.append(self._run_one_date(config, replay_date, store, sources, search_store, report_store, fixture_store))
        discovered = tuple(item for snapshot in snapshots for item in snapshot.candidates)
        # Benchmark labels are loaded only after candidate generation finishes.
        labels = labels_for_market(load_benchmark_labels(config.benchmark_label_path), config.market)
        recall = _evaluate_benchmarks(labels, discovered, snapshots, store, config)
        result = AsOfResearchReplayResult(
            config=config,
            snapshots=tuple(snapshots),
            discovered_candidates=discovered,
            benchmark_recall=recall,
        )
        if not write_outputs:
            return result
        return _write_outputs(result)

    def _run_one_date(
        self,
        config: AsOfResearchReplayConfig,
        replay_date: date,
        store: HistoricalOfficialStore,
        sources: HistoricalOfficialSources,
        search_store: SearchSnapshotStore,
        report_store: ReportSnapshotStore,
        fixture_store: RuntimeFixtureEvidenceStore,
    ) -> AsOfResearchReplaySnapshot:
        official_universe = sources.list_instruments(config.market, replay_date)
        fixture_universe = fixture_store.instruments(market=config.market, as_of_date=replay_date)
        snapshot_universe = (
            _snapshot_derived_universe(search_store, report_store, config.market, replay_date)
            if config.allow_snapshot_derived_universe
            else ()
        )
        universe = _merge_universe(official_universe, snapshot_universe, fixture_universe)
        if config.universe_limit is not None:
            universe = universe[: config.universe_limit]
        limitations = list(store.coverage(replay_date, config.market).limitations())
        if snapshot_universe:
            limitations.append("snapshot_derived_universe")
        if not universe:
            limitations.append("insufficient official historical data: universe missing")
            return AsOfResearchReplaySnapshot(
                as_of_date=replay_date,
                universe_count=0,
                layer1_candidates=(),
                candidates=(),
                web_research_results=(),
                flow_traces=(),
                limitations=tuple(dict.fromkeys(limitations)),
            )

        cheap_scan = KoreaCheapScanner(sources).run(
            KoreaCheapScanConfig(
                as_of_date=replay_date,
                markets=(config.market,),
                sources=sources,
                universe_limit=config.universe_limit,
                lookback_days=370,
                disclosure_lookback_days=45,
                top_n=config.max_candidates_per_date,
                report_radar_enabled=False,
            )
        )
        replay_universe_symbols = {item.symbol for item in universe}
        radar_candidates = _snapshot_report_radar_candidates(
            config=config,
            replay_date=replay_date,
            search_store=search_store,
            instruments=tuple(item for item in snapshot_universe if item.symbol in replay_universe_symbols),
        )
        active_replay_symbols = {item.symbol for item in (*cheap_scan.candidates, *radar_candidates)}
        fixture_candidates = fixture_store.candidates(
            market=config.market,
            as_of_date=replay_date,
            carry_forward_symbols=tuple(active_replay_symbols),
        )
        layer1 = tuple(
            item
            for item in _merge_candidates(cheap_scan.candidates, radar_candidates, fixture_candidates)
            if item.recommended_next_layer in {RecommendedNextLayer.EVENT_SEARCH, RecommendedNextLayer.DEEP_RESEARCH}
        )
        web_results: list[AsOfWebResearchResult] = []
        traces: list[FlowTrace] = []
        candidate_rows: list[AsOfReplayCandidate] = []
        web_research_slice = layer1 if config.max_web_research_candidates_per_date is None else layer1[: config.max_web_research_candidates_per_date]
        theme_route_provider = _theme_route_provider_for_config(config)
        for rank, candidate in enumerate(layer1, start=1):
            should_research = candidate in web_research_slice and not config.dry_run
            web_result: AsOfWebResearchResult | None = None
            if should_research:
                provider = _provider_for_candidate(config, search_store, candidate)
                fixture_text = fixture_text_by_url_for_candidate(
                    store=report_store,
                    symbol=candidate.symbol,
                    company_name=candidate.company_name,
                )
                base_feature_input = build_asof_evidence_bundle(candidate=candidate, store=store).feature_input()
                web_result = AsOfWebResearchRunner().run(
                    candidate=candidate,
                    search_provider=provider,
                    fixture_text_by_url=fixture_text,
                    base_feature_input=base_feature_input,
                    config=AsOfWebResearchConfig(
                        as_of_date=replay_date,
                        max_queries_per_candidate=config.max_queries_per_candidate,
                        max_results_per_query=config.max_results_per_query,
                        require_date_verified_for_green=config.require_date_verified_for_green,
                        allow_undated_docs_for_yellow_only=config.allow_undated_docs_for_yellow_only,
                        save_reconstructed_snapshots=config.save_reconstructed_snapshots,
                        theme_rebalance_enabled=config.theme_rebalance_enabled,
                        theme_route_provider=theme_route_provider,
                        max_theme_expansion_rounds=config.max_theme_expansion_rounds,
                        theme_evidence_review_enabled=config.theme_evidence_review_enabled,
                    ),
                )
                web_results.append(web_result)
            extra_reports = fixture_store.reports_for_candidate(candidate)
            extra_evidence = fixture_store.evidence_for_candidate(candidate)
            bundle = build_asof_evidence_bundle(
                candidate=candidate,
                store=store,
                web_result=web_result,
                extra_reports=extra_reports,
                extra_evidence=extra_evidence,
            )
            merged_scoring = score_asof_evidence_bundle(bundle, candidate=candidate, web_result=web_result)
            row = _candidate_row(candidate, rank, web_result, merged_scoring)
            candidate_rows.append(row)
            traces.append(_trace_for_candidate(candidate, row, web_result, should_research))
        return AsOfResearchReplaySnapshot(
            as_of_date=replay_date,
            universe_count=len(universe),
            layer1_candidates=layer1,
            candidates=tuple(candidate_rows),
            web_research_results=tuple(web_results),
            flow_traces=tuple(traces),
            limitations=tuple(dict.fromkeys(limitations)),
            documents_rejected_after_asof=sum(item.rejected_future_count for item in web_results),
            documents_date_verified=sum(item.date_verified_count for item in web_results),
            documents_date_unverified=sum(item.date_unverified_count for item in web_results),
        )


def _provider_for_candidate(
    config: AsOfResearchReplayConfig,
    search_store: SearchSnapshotStore,
    candidate: CheapScanCandidate,
) -> SearchProvider:
    if config.fixture_search:
        return RetrospectiveSnapshotSearchProvider(
            store=search_store,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
        )
    if config.live_search:
        # Live search providers are intentionally not wired here. The CLI flag
        # marks intent, while tests and default replay remain offline-safe.
        return EmptySearchProvider()
    return EmptySearchProvider()


def _theme_route_provider_for_config(config: AsOfResearchReplayConfig) -> ThemeRouteProvider | None:
    if config.theme_rebalance_enabled is False:
        return None
    if config.theme_route_provider is not None:
        return config.theme_route_provider
    if config.theme_rebalance_enabled:
        provider = build_theme_route_provider_from_env(working_directory=Path.cwd())
        if provider is not None:
            return provider
        return build_default_codex_theme_route_provider(working_directory=Path.cwd())
    return None


def _snapshot_derived_universe(
    search_store: SearchSnapshotStore,
    report_store: ReportSnapshotStore,
    market: Market,
    as_of_date: date,
) -> tuple[Instrument, ...]:
    by_symbol: dict[str, Instrument] = {}
    for item in search_store.load_snapshots():
        if item.published_at is not None and item.published_at.date() > as_of_date:
            continue
        _add_snapshot_instrument(by_symbol, item.symbol, item.company_name, market)
    for item in report_store.load_snapshots(as_of_date=as_of_date):
        _add_snapshot_instrument(by_symbol, item.symbol, item.company_name, market)
    return tuple(sorted(by_symbol.values(), key=lambda item: item.symbol))


def _add_snapshot_instrument(
    by_symbol: dict[str, Instrument],
    symbol: str | None,
    company_name: str | None,
    market: Market,
) -> None:
    if not symbol or not company_name:
        return
    by_symbol.setdefault(
        symbol,
        Instrument(
            symbol=symbol,
            name=company_name,
            market=market,
            exchange="KRX" if market == Market.KR else market.value,
            currency="KRW" if market == Market.KR else "USD",
        ),
    )


def _merge_universe(*groups: Sequence[Instrument]) -> tuple[Instrument, ...]:
    by_symbol: dict[str, Instrument] = {}
    for group in groups:
        for item in group:
            by_symbol.setdefault(item.symbol, item)
    return tuple(by_symbol.values())


def _snapshot_report_radar_candidates(
    *,
    config: AsOfResearchReplayConfig,
    replay_date: date,
    search_store: SearchSnapshotStore,
    instruments: Sequence[Instrument],
) -> tuple[CheapScanCandidate, ...]:
    if not config.allow_snapshot_derived_universe or not instruments:
        return ()
    candidates: list[CheapScanCandidate] = []
    for instrument in instruments:
        provider = AsOfDateFilteredSearchProvider(
            RetrospectiveSnapshotSearchProvider(
                store=search_store,
                symbol=instrument.symbol,
                company_name=instrument.name,
            ),
            replay_date,
        )
        budget = SearchBudget(
            max_total_queries_per_day=None,
            max_queries_per_symbol=config.max_queries_per_candidate,
        )
        radar_rows = ReportRadar(provider, max_results_per_query=config.max_results_per_query).run(
            instruments=(instrument,),
            as_of_date=replay_date,
            budget=budget,
            max_symbols=1,
        )
        candidates.extend(item.to_cheap_scan_candidate() for item in radar_rows)
    return _merge_candidates(candidates)


def _merge_candidates(*groups: Sequence[CheapScanCandidate]) -> tuple[CheapScanCandidate, ...]:
    by_symbol: dict[tuple[object, ...], CheapScanCandidate] = {}
    for group in groups:
        for item in group:
            key = _candidate_merge_key(item)
            existing = by_symbol.get(key)
            if existing is None or _candidate_rank(item) > _candidate_rank(existing):
                by_symbol[key] = item
    return tuple(by_symbol.values())


def _candidate_merge_key(candidate: CheapScanCandidate) -> tuple[object, ...]:
    if candidate.candidate_source_path == "runtime_fixture_spec":
        return (
            candidate.candidate_source_path,
            candidate.symbol,
            candidate.as_of_date,
            candidate.reason_codes,
            candidate.evidence_ids,
        )
    return ("symbol", candidate.symbol)


def _candidate_rank(candidate: CheapScanCandidate) -> tuple[int, float, int]:
    layer_rank = {
        RecommendedNextLayer.NONE: 0,
        RecommendedNextLayer.EVENT_SEARCH: 1,
        RecommendedNextLayer.DEEP_RESEARCH: 2,
    }.get(candidate.recommended_next_layer, 0)
    source_rank = {
        "official_cheap_scan": 0,
        "top_trading_value_probe": 0,
        "targeted_smoke": 1,
        "report_radar": 2,
    }.get(candidate.candidate_source_path, 0)
    return (layer_rank, float(candidate.cheap_scan_total_score), source_rank)


def _candidate_row(
    candidate: CheapScanCandidate,
    rank: int,
    web_result: AsOfWebResearchResult | None,
    merged_scoring: AsOfEvidenceBundleScore,
) -> AsOfReplayCandidate:
    pipeline = web_result.pipeline_result if web_result is not None else None
    web_only_stage = pipeline.stage.stage if pipeline is not None else None
    web_only_score = visible_score_total(pipeline.score) if pipeline is not None else None
    evidence_types = merged_scoring.bundle.source_types or ("official_cheap_scan",)
    merged_stage = merged_scoring.stage.stage
    merged_score = visible_score_total(merged_scoring.score)
    web_score = pipeline.score if pipeline is not None else None
    merged_input_counts = merged_scoring.bundle.coverage()
    merged_input_fingerprint = research_input_fingerprint(
        score=merged_scoring.score,
        evidence=merged_scoring.bundle.evidence,
        queries=pipeline.web_result.queries_run if pipeline is not None else (),
        route_diagnostics=pipeline.theme_route_diagnostics if pipeline is not None else None,
        input_counts=_normalized_bundle_counts(merged_input_counts),
        source_fields=merged_scoring.feature_result.source_fields,
        extra={"expansion_queries": tuple(pipeline.expansion_queries_run) if pipeline is not None else ()},
    )
    web_only_input_fingerprint = (
        research_input_fingerprint(
            score=web_score,
            evidence=pipeline.web_result.evidence,
            queries=pipeline.web_result.queries_run,
            route_diagnostics=pipeline.theme_route_diagnostics,
            input_counts=_feature_input_count_row(pipeline.feature_input),
            source_fields=pipeline.feature_result.source_fields,
            extra={"expansion_queries": tuple(pipeline.expansion_queries_run)},
        )
        if pipeline is not None
        else None
    )
    runtime_fixture_evidence_count = _runtime_fixture_evidence_count(merged_scoring.bundle.evidence)
    runtime_fixture_injected = (
        candidate.candidate_source_path == "runtime_fixture_spec"
        or runtime_fixture_evidence_count > 0
        or any(_runtime_fixture_report(report) for report in merged_scoring.bundle.research_reports)
    )
    return AsOfReplayCandidate(
        symbol=candidate.symbol,
        company_name=candidate.company_name,
        as_of_date=candidate.as_of_date,
        large_sector_id=merged_scoring.feature_result.payload.large_sector_id,
        canonical_archetype_id=merged_scoring.feature_result.payload.canonical_archetype_id,
        layer=candidate.recommended_next_layer.value,
        stage=merged_stage,
        rank=rank,
        score=merged_score,
        evidence_types_seen=evidence_types,
        reason_codes=candidate.reason_codes,
        candidate_source_path=candidate.candidate_source_path,
        date_verified_documents=web_result.date_verified_count if web_result is not None else 0,
        date_unverified_documents=web_result.date_unverified_count if web_result is not None else 0,
        rejected_future_documents=web_result.rejected_future_count if web_result is not None else 0,
        web_only_stage=web_only_stage,
        merged_stage=merged_stage,
        web_only_score=web_only_score,
        merged_score=merged_score,
        score_valid=is_score_valid(merged_scoring.score),
        score_blocked_reason=score_block_reason(merged_scoring.score),
        score_fingerprint=score_fingerprint(merged_scoring.score),
        research_input_fingerprint=merged_input_fingerprint,
        score_variability_drivers=score_variability_drivers(
            merged_scoring.score,
            input_counts=_normalized_bundle_counts(merged_input_counts),
            evidence_count=len(merged_scoring.bundle.evidence),
            input_fingerprint=merged_input_fingerprint,
        ),
        web_only_score_valid=is_score_valid(web_score) if web_score is not None else None,
        web_only_score_blocked_reason=score_block_reason(web_score) if web_score is not None else None,
        web_only_score_fingerprint=score_fingerprint(web_score) if web_score is not None else None,
        web_only_research_input_fingerprint=web_only_input_fingerprint,
        web_only_score_variability_drivers=score_variability_drivers(
            web_score,
            route_diagnostics=pipeline.theme_route_diagnostics if pipeline is not None else None,
            evidence_count=len(pipeline.web_result.evidence) if pipeline is not None else None,
            expansion_query_count=len(pipeline.expansion_queries_run) if pipeline is not None else None,
            scoring_canonical_archetype_id=pipeline.feature_result.payload.canonical_archetype_id if pipeline is not None else None,
            input_fingerprint=web_only_input_fingerprint,
        )
        if web_score is not None
        else (),
        promotion_delta=_promotion_delta(web_only_stage, merged_stage),
        promotion_band=promotion_band(merged_scoring.score, merged_stage),
        score_source_mode="runtime_fixture_injected" if runtime_fixture_injected else "operational_merged",
        runtime_fixture_injected=runtime_fixture_injected,
        runtime_fixture_evidence_count=runtime_fixture_evidence_count,
        merged_evidence_count=len(merged_scoring.bundle.evidence),
        eps_fcf_explosion_score=merged_scoring.score.eps_fcf_explosion_score,
        earnings_visibility_score=merged_scoring.score.earnings_visibility_score,
        bottleneck_pricing_score=merged_scoring.score.bottleneck_pricing_score,
        market_mispricing_score=merged_scoring.score.market_mispricing_score,
        valuation_rerating_score=merged_scoring.score.valuation_rerating_score,
        capital_allocation_score=merged_scoring.score.capital_allocation_score,
        information_confidence_score=merged_scoring.score.information_confidence_score,
        risk_penalty=merged_scoring.score.risk_penalty,
        claim_backed_claim_count=_diagnostic_score(merged_scoring.score, "claim_backed_claim_count_capped"),
        claim_backed_primitive_count=_diagnostic_score(merged_scoring.score, "claim_backed_primitive_count_capped"),
        score_claim_backed_component_count=_diagnostic_score(
            merged_scoring.score,
            "score_claim_backed_component_count_capped",
        ),
        orphan_score_component_count=_diagnostic_score(merged_scoring.score, "orphan_score_component_count_capped"),
        score_claim_backed_component_ratio=_diagnostic_score(
            merged_scoring.score,
            "score_claim_backed_component_ratio",
        ),
        claim_ledger_claim_ids=_source_field_claim_ids(merged_scoring.feature_result, "claim_ledger_score_eligible_claim_ids"),
        claim_ledger_claim_ids_by_primitive=_source_field_claim_ids_by_primitive(
            merged_scoring.feature_result,
            "claim_ledger_claim_ids_by_primitive",
        ),
        score_contribution_claim_ids=merged_scoring.score.score_contribution_claim_ids,
        score_contribution_ledger=merged_scoring.score.score_contribution_ledger,
        source_backed_green_bridge_raw=_diagnostic_score(merged_scoring.score, "source_backed_green_bridge_raw"),
        evidence_contract_required_primitive_count=_diagnostic_score(
            merged_scoring.score,
            "evidence_contract_required_primitive_count_capped",
        ),
        evidence_contract_present_primitive_count=_diagnostic_score(
            merged_scoring.score,
            "evidence_contract_present_primitive_count_capped",
        ),
        evidence_contract_missing_primitive_count=_diagnostic_score(
            merged_scoring.score,
            "evidence_contract_missing_primitive_count_capped",
        ),
        evidence_contract_coverage_pct=_diagnostic_score(merged_scoring.score, "evidence_contract_coverage_pct"),
        evidence_contract_positive_coverage_pct=_diagnostic_score(
            merged_scoring.score,
            "evidence_contract_positive_coverage_pct",
        ),
        evidence_contract_positive_missing_primitive_count=_diagnostic_score(
            merged_scoring.score,
            "evidence_contract_positive_missing_primitive_count_capped",
        ),
        evidence_contract_green_gate_coverage_pct=_diagnostic_score(
            merged_scoring.score,
            "evidence_contract_green_gate_coverage_pct",
        ),
        evidence_contract_green_gate_missing_primitive_count=_diagnostic_score(
            merged_scoring.score,
            "evidence_contract_green_gate_missing_primitive_count_capped",
        ),
        evidence_contract_guard_present_primitive_count=_diagnostic_score(
            merged_scoring.score,
            "evidence_contract_guard_present_primitive_count_capped",
        ),
        evidence_contract_guard_cleared_primitive_count=_diagnostic_score(
            merged_scoring.score,
            "evidence_contract_guard_cleared_primitive_count_capped",
        ),
        evidence_contract_guard_missing_primitive_count=_diagnostic_score(
            merged_scoring.score,
            "evidence_contract_guard_missing_primitive_count_capped",
        ),
        evidence_contract_missing_primitives=_source_field_text(
            merged_scoring.feature_result,
            "evidence_contract_missing_primitives",
        ),
        evidence_contract_positive_missing_primitives=_source_field_text(
            merged_scoring.feature_result,
            "evidence_contract_positive_missing_primitives",
        ),
        evidence_contract_green_gate_primitives=_source_field_text(
            merged_scoring.feature_result,
            "evidence_contract_green_gate_primitives",
        ),
        evidence_contract_green_gate_missing_primitives=_source_field_text(
            merged_scoring.feature_result,
            "evidence_contract_green_gate_missing_primitives",
        ),
        evidence_contract_guard_primitives=_source_field_text(
            merged_scoring.feature_result,
            "evidence_contract_guard_primitives",
        ),
        evidence_contract_guard_present_primitives=_source_field_text(
            merged_scoring.feature_result,
            "evidence_contract_guard_present_primitives",
        ),
        evidence_contract_guard_cleared_primitives=_source_field_text(
            merged_scoring.feature_result,
            "evidence_contract_guard_cleared_primitives",
        ),
        evidence_contract_guard_missing_primitives=_source_field_text(
            merged_scoring.feature_result,
            "evidence_contract_guard_missing_primitives",
        ),
        evidence_contract_required_primitives=_source_field_text(
            merged_scoring.feature_result,
            "evidence_contract_required_primitives",
        ),
        evidence_contract_required_bridge_axes=_source_field_text(
            merged_scoring.feature_result,
            "evidence_contract_required_bridge_axes",
        ),
    )


def _diagnostic_score(score: Any, key: str) -> float | None:
    diagnostics = getattr(score, "diagnostic_scores", None)
    if not isinstance(diagnostics, Mapping) or key not in diagnostics:
        return None
    try:
        return float(diagnostics[key])
    except (TypeError, ValueError):
        return None


def _source_field_text(feature_result: Any, key: str) -> str | None:
    source_fields = getattr(feature_result, "source_fields", None)
    if not isinstance(source_fields, Mapping):
        return None
    value = source_fields.get(key)
    if value in (None, ""):
        return None
    return str(value)


def _source_field_claim_ids(feature_result: Any, key: str) -> tuple[str, ...]:
    value = _source_field_text(feature_result, key)
    if not value:
        return ()
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError:
        parsed = None
    if isinstance(parsed, list):
        values = parsed
    else:
        values = value.split(",")
    return tuple(dict.fromkeys(str(item).strip() for item in values if str(item).strip()))


def _source_field_claim_ids_by_primitive(feature_result: Any, key: str) -> Mapping[str, tuple[str, ...]]:
    value = _source_field_text(feature_result, key)
    if not value:
        return {}
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError:
        return {}
    if not isinstance(parsed, Mapping):
        return {}
    result: dict[str, tuple[str, ...]] = {}
    for primitive, raw_claims in parsed.items():
        primitive_id = str(primitive).strip()
        if not primitive_id:
            continue
        values = raw_claims if isinstance(raw_claims, (list, tuple)) else (raw_claims,)
        claims = tuple(dict.fromkeys(str(item).strip() for item in values if str(item).strip()))
        if claims:
            result[primitive_id] = claims
    return result


def _runtime_fixture_evidence_count(evidence: Sequence[Any]) -> int:
    return sum(1 for item in evidence if _runtime_fixture_fields(getattr(item, "parsed_fields", {})))


def _runtime_fixture_report(report: Any) -> bool:
    return _runtime_fixture_fields(getattr(report, "parsed_fields", {}))


def _runtime_fixture_fields(fields: Any) -> bool:
    return isinstance(fields, Mapping) and bool(fields.get("runtime_fixture_source_backed"))


def _normalized_bundle_counts(counts: Mapping[str, int]) -> Mapping[str, int]:
    return {
        "price_bars": int(counts.get("price_bars_count", 0)),
        "financial_actuals": int(counts.get("financial_actuals_count", 0)),
        "disclosures": int(counts.get("disclosures_count", 0)),
        "research_reports": int(counts.get("research_reports_count", 0)),
        "news_items": int(counts.get("news_items_count", 0)),
        "consensus": int(counts.get("consensus_count", 0)),
        "consensus_revisions": int(counts.get("consensus_revisions_count", 0)),
    }


def _feature_input_count_row(feature_input: Any) -> Mapping[str, int]:
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


def _promotion_delta(web_only_stage: Stage | None, merged_stage: Stage) -> str:
    if web_only_stage is None:
        return f"official_only_to_{merged_stage.value}"
    if web_only_stage == merged_stage:
        return "unchanged"
    return f"{web_only_stage.value}_to_{merged_stage.value}"


def _trace_for_candidate(
    candidate: CheapScanCandidate,
    row: AsOfReplayCandidate,
    web_result: AsOfWebResearchResult | None,
    web_research_executed: bool,
) -> FlowTrace:
    search_results = web_result.pipeline_result.web_result.search_results if web_result and web_result.pipeline_result else ()
    fetched = web_result.pipeline_result.web_result.fetched_documents if web_result and web_result.pipeline_result else ()
    evidence = web_result.pipeline_result.web_result.evidence if web_result and web_result.pipeline_result else ()
    from_report_radar = candidate.candidate_source_path == "report_radar"
    steps = (
        FlowTraceStep("entered_universe", True),
        FlowTraceStep("passed_official_cheap_scan", not from_report_radar),
        FlowTraceStep("watch_disclosure_found", bool(set(candidate.reason_codes) & {"DISC_SUPPLY_CONTRACT", "DISC_FACILITY_INVESTMENT", "DISC_EARNINGS_PREANNOUNCE"})),
        FlowTraceStep("opendart_detail_fetched", False, "detail fetch is represented by historical official fixtures when present"),
        FlowTraceStep(
            "report_radar_candidate",
            from_report_radar,
            "candidate came from explicit snapshot-derived report radar",
        ),
        FlowTraceStep("free_web_research_executed", web_research_executed),
        FlowTraceStep("search_results_found", bool(search_results)),
        FlowTraceStep("documents_fetched", any(item.ok for item in fetched)),
        FlowTraceStep("documents_date_verified", bool(web_result and web_result.date_verified_count > 0)),
        FlowTraceStep("evidence_created", bool(evidence)),
        FlowTraceStep("feature_score_created", web_result is not None and web_result.pipeline_result is not None),
        FlowTraceStep("stage_created", True),
        FlowTraceStep("red_team_blocked", row.stage == Stage.STAGE_4C),
        FlowTraceStep("audit_blocked", False),
        FlowTraceStep("benchmark_detected", False, "benchmark evaluation happens after output"),
    )
    failure_stage = None
    if not web_research_executed:
        failure_stage = "free_web_research_not_executed"
    elif not search_results:
        failure_stage = "free_web_research_no_results"
    elif not any(item.ok for item in fetched):
        failure_stage = "documents_not_fetched"
    elif not evidence:
        failure_stage = "evidence_not_created"
    return FlowTrace(
        symbol=candidate.symbol,
        company_name=candidate.company_name,
        as_of_date=candidate.as_of_date,
        steps=steps,
        failure_stage=failure_stage,
    )


def _evaluate_benchmarks(
    labels: Sequence[BenchmarkLabel],
    discovered: Sequence[AsOfReplayCandidate],
    snapshots: Sequence[AsOfResearchReplaySnapshot],
    store: HistoricalOfficialStore,
    config: AsOfResearchReplayConfig,
) -> tuple[BenchmarkAsOfRecallRow, ...]:
    rows: list[BenchmarkAsOfRecallRow] = []
    for label in labels:
        matches = [
            item
            for item in discovered
            if item.symbol == label.symbol and label.expected_window_start <= item.as_of_date <= label.expected_window_end
        ]
        if matches:
            first = sorted(matches, key=lambda item: (item.as_of_date, item.rank))[0]
            rows.append(
                BenchmarkAsOfRecallRow(
                    label_id=label.label_id,
                    symbol=label.symbol,
                    company_name=label.company_name,
                    expected_group=label.expected_group.value,
                    appeared_in_candidates=True,
                    first_detected_date=first.as_of_date,
                    first_layer=first.layer,
                    first_stage=first.stage,
                    detection_lag_days=(first.as_of_date - label.expected_window_start).days,
                    evidence_types_seen=first.evidence_types_seen,
                )
            )
            continue
        rows.append(
            BenchmarkAsOfRecallRow(
                label_id=label.label_id,
                symbol=label.symbol,
                company_name=label.company_name,
                expected_group=label.expected_group.value,
                appeared_in_candidates=False,
                first_detected_date=None,
                first_layer=None,
                first_stage=None,
                detection_lag_days=None,
                evidence_types_seen=(),
                failure_stage=_failure_stage(label, snapshots, store, config),
            )
        )
    return tuple(rows)


def _failure_stage(
    label: BenchmarkLabel,
    snapshots: Sequence[AsOfResearchReplaySnapshot],
    store: HistoricalOfficialStore,
    config: AsOfResearchReplayConfig,
) -> str:
    dates = [item.as_of_date for item in snapshots if label.expected_window_start <= item.as_of_date <= label.expected_window_end]
    if not dates:
        return "outside_expected_window"
    if not any(any(item.symbol == label.symbol for item in store.load_universe(replay_date, config.market)) for replay_date in dates):
        return "not_in_universe"
    traces = [trace for snapshot in snapshots for trace in snapshot.flow_traces if trace.symbol == label.symbol]
    if not traces:
        return "failed_official_cheap_scan"
    if not any(trace.reached("free_web_research_executed") for trace in traces):
        return "free_web_research_not_executed"
    if not any(trace.reached("search_results_found") for trace in traces):
        return "free_web_research_no_results"
    if any(snapshot.documents_rejected_after_asof for snapshot in snapshots if label.expected_window_start <= snapshot.as_of_date <= label.expected_window_end):
        return "documents_after_asof_date"
    if not any(trace.reached("documents_date_verified") for trace in traces):
        return "documents_date_unverified"
    if not any(trace.reached("evidence_created") for trace in traces):
        return "evidence_not_created"
    return "stage_not_high_enough"


def render_asof_replay_summary(result: AsOfResearchReplayResult) -> str:
    stage_counts = Counter(item.stage.value for item in result.discovered_candidates)
    band_counts = Counter(item.promotion_band for item in result.discovered_candidates)
    if result.config.allow_snapshot_derived_universe:
        candidate_generation_note = (
            "This replay starts from official historical universe data and explicitly enabled "
            "snapshot-derived report-radar candidates."
        )
    else:
        candidate_generation_note = "This replay starts from official historical universe data."
    lines = [
        "# As-Of Research Replay Summary",
        "",
        "- replay_type: asof_research_replay",
        "- strict_forward_archive_proof: false",
        "- benchmark_labels_used_before_candidate_generation: no",
        f"- period: {result.config.start_date.isoformat()} to {result.config.end_date.isoformat()}",
        f"- frequency: {result.config.frequency.value}",
        f"- market: {result.config.market.value}",
        f"- replay_dates: {len(result.snapshots)}",
        f"- total_universe_rows_scanned: {sum(item.universe_count for item in result.snapshots)}",
        f"- layer1_candidates: {sum(len(item.layer1_candidates) for item in result.snapshots)}",
        f"- web_researched_candidates: {sum(len(item.web_research_results) for item in result.snapshots)}",
        f"- documents_rejected_after_asof: {sum(item.documents_rejected_after_asof for item in result.snapshots)}",
        f"- documents_date_verified: {sum(item.documents_date_verified for item in result.snapshots)}",
        f"- documents_date_unverified: {sum(item.documents_date_unverified for item in result.snapshots)}",
        f"- discovered_candidates: {len(result.discovered_candidates)}",
        f"- Stage 2 count: {stage_counts.get(Stage.STAGE_2.value, 0)}",
        f"- Stage 3-Green count: {stage_counts.get(Stage.STAGE_3_GREEN.value, 0)}",
        f"- Stage 3-Yellow count: {stage_counts.get(Stage.STAGE_3_YELLOW.value, 0)}",
        f"- Stage 3-Red count: {stage_counts.get(Stage.STAGE_3_RED.value, 0)}",
        f"- Stage 2-High band count: {band_counts.get('Stage 2-High', 0)}",
        f"- Stage 3-Watch band count: {band_counts.get('Stage 3-Watch', 0)}",
        f"- merged scoring used: yes",
        "",
        candidate_generation_note,
        "Web research is executed only after Layer-1 candidate generation.",
        "It uses reconstructed public-document research and rejects documents published after the replay date.",
    ]
    limitations = tuple(dict.fromkeys(item for snapshot in result.snapshots for item in snapshot.limitations))
    if limitations:
        lines.extend(["", "Limitations:"])
        lines.extend(f"- {item}" for item in limitations)
    return "\n".join(lines).rstrip() + "\n"


def render_benchmark_recall_report(result: AsOfResearchReplayResult) -> str:
    lines = [
        "# As-Of Benchmark Recall Report",
        "",
        "| label | company | group | appeared | first date | layer | stage | lag days | evidence | failure stage |",
        "| --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- |",
    ]
    for item in result.benchmark_recall:
        lines.append(
            f"| {item.label_id} | {item.company_name} | {item.expected_group} | {'yes' if item.appeared_in_candidates else 'no'} | "
            f"{item.first_detected_date.isoformat() if item.first_detected_date else 'n/a'} | {item.first_layer or 'n/a'} | "
            f"{item.first_stage.value if item.first_stage else 'n/a'} | {item.detection_lag_days if item.detection_lag_days is not None else 'n/a'} | "
            f"{', '.join(item.evidence_types_seen) or 'none'} | {item.failure_stage or ''} |"
        )
    return "\n".join(lines).rstrip() + "\n"


def render_missed_benchmark_labels(result: AsOfResearchReplayResult) -> str:
    missed = [item for item in result.benchmark_recall if not item.appeared_in_candidates]
    lines = ["# Missed Benchmark Labels", ""]
    if not missed:
        lines.append("No benchmark labels were missed in this as-of replay.")
        return "\n".join(lines).rstrip() + "\n"
    lines.extend(["| label | company | failure stage |", "| --- | --- | --- |"])
    for item in missed:
        lines.append(f"| {item.label_id} | {item.company_name} | {item.failure_stage} |")
    return "\n".join(lines).rstrip() + "\n"


def render_failure_stage_report(result: AsOfResearchReplayResult) -> str:
    counts = Counter(item.failure_stage or "detected" for item in result.benchmark_recall)
    lines = ["# Failure Stage Report", "", "| stage | count |", "| --- | ---: |"]
    for key, value in sorted(counts.items()):
        lines.append(f"| {key} | {value} |")
    lines.append("")
    lines.append("This answers where each benchmark failed in the official-first replay flow.")
    return "\n".join(lines).rstrip() + "\n"


def render_evidence_coverage_report(result: AsOfResearchReplayResult) -> str:
    counts = Counter()
    for candidate in result.discovered_candidates:
        counts.update(candidate.evidence_types_seen)
    lines = ["# Evidence Coverage Report", "", "| evidence type | count |", "| --- | ---: |"]
    if counts:
        for key, value in sorted(counts.items()):
            lines.append(f"| {key} | {value} |")
    else:
        lines.append("| none | 0 |")
    lines.extend(
        [
            "",
            f"- date_verified_documents: {sum(item.documents_date_verified for item in result.snapshots)}",
            f"- date_unverified_documents: {sum(item.documents_date_unverified for item in result.snapshots)}",
            f"- documents_rejected_after_asof: {sum(item.documents_rejected_after_asof for item in result.snapshots)}",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def render_reconstructed_snapshot_report(result: AsOfResearchReplayResult) -> str:
    paths = sorted({str(path) for snapshot in result.snapshots for web in snapshot.web_research_results for path in web.reconstructed_snapshot_paths})
    lines = [
        "# Reconstructed Snapshot Report",
        "",
        "- point_in_time_status: retrospective_reconstructed",
        "- strict_pit_proof: false",
        "- documents after as_of_date are rejected",
        "- undated documents cannot create Stage 3-Green alone when configured",
        "",
        "| path |",
        "| --- |",
    ]
    lines.extend(f"| {path} |" for path in paths) if paths else lines.append("| none |")
    return "\n".join(lines).rstrip() + "\n"


def render_false_positive_report(result: AsOfResearchReplayResult) -> str:
    rows = [
        item
        for item in result.benchmark_recall
        if item.expected_group in {"one_off", "boom_bust", "valuation_overheat"}
    ]
    lines = ["# False Positive Report", "", "| label | group | appeared | stage | interpretation |", "| --- | --- | --- | --- | --- |"]
    for item in rows:
        unsafe = item.first_stage == Stage.STAGE_3_GREEN
        lines.append(
            f"| {item.label_id} | {item.expected_group} | {'yes' if item.appeared_in_candidates else 'no'} | "
            f"{item.first_stage.value if item.first_stage else 'n/a'} | {'unsafe Green' if unsafe else 'contained or not detected'} |"
        )
    return "\n".join(lines).rstrip() + "\n"


def render_stage_lifecycle_report(result: AsOfResearchReplayResult) -> str:
    lines = ["# Stage Lifecycle Report", "", "| symbol | company | date | stage | note |", "| --- | --- | --- | --- | --- |"]
    rows = [item for item in result.discovered_candidates if item.stage in {Stage.STAGE_3_GREEN, Stage.STAGE_3_YELLOW, Stage.STAGE_3_RED, Stage.STAGE_4A, Stage.STAGE_4B, Stage.STAGE_4C}]
    if not rows:
        lines.append("| n/a | n/a | n/a | n/a | no Stage 3 lifecycle candidates |")
    for item in rows:
        lines.append(f"| {item.symbol} | {item.company_name} | {item.as_of_date.isoformat()} | {item.stage.value} | lifecycle detector not run in as-of layer yet |")
    return "\n".join(lines).rstrip() + "\n"


def render_limitations(result: AsOfResearchReplayResult) -> str:
    lines = [
        "# As-Of Research Replay Limitations",
        "",
        "- This is retrospective as-of research, not strict forward-archive proof.",
        "- It uses current/fixture search to reconstruct older public evidence.",
        "- Documents published after replay date are rejected.",
        "- Undated documents are date_unverified and cannot create Stage 3-Green alone when configured.",
        "- Benchmark labels are evaluation-only and loaded after candidate output.",
    ]
    if result.config.allow_snapshot_derived_universe:
        lines.append("- Search/report snapshots can add report-radar candidates only because the explicit option was enabled.")
    else:
        lines.append("- Search/report snapshots do not define the universe.")
    for item in tuple(dict.fromkeys(value for snapshot in result.snapshots for value in snapshot.limitations)):
        lines.append(f"- {item}")
    return "\n".join(lines).rstrip() + "\n"


def _write_outputs(result: AsOfResearchReplayResult) -> AsOfResearchReplayResult:
    output_root = Path(result.config.output_directory) / f"{result.config.start_date.isoformat()}_to_{result.config.end_date.isoformat()}"
    output_root.mkdir(parents=True, exist_ok=True)
    paths = {
        "summary_md": output_root / "asof_replay_summary.md",
        "summary_json": output_root / "asof_replay_summary.json",
        "candidates_csv": output_root / "discovered_candidates.csv",
        "candidates_json": output_root / "discovered_candidates.json",
        "recall_md": output_root / "benchmark_recall_report.md",
        "recall_json": output_root / "benchmark_recall_report.json",
        "missed_md": output_root / "missed_benchmark_labels.md",
        "failure_stage_md": output_root / "failure_stage_report.md",
        "lifecycle_md": output_root / "stage_lifecycle_report.md",
        "evidence_md": output_root / "evidence_coverage_report.md",
        "reconstructed_md": output_root / "reconstructed_snapshot_report.md",
        "false_positive_md": output_root / "false_positive_report.md",
        "limitations_md": output_root / "limitations.md",
    }
    paths["summary_md"].write_text(render_asof_replay_summary(result), encoding="utf-8")
    paths["summary_json"].write_text(json.dumps(_jsonable(result), ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    _write_candidates(paths["candidates_csv"], paths["candidates_json"], result.discovered_candidates)
    paths["recall_md"].write_text(render_benchmark_recall_report(result), encoding="utf-8")
    paths["recall_json"].write_text(json.dumps(_jsonable(result.benchmark_recall), ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    paths["missed_md"].write_text(render_missed_benchmark_labels(result), encoding="utf-8")
    paths["failure_stage_md"].write_text(render_failure_stage_report(result), encoding="utf-8")
    paths["lifecycle_md"].write_text(render_stage_lifecycle_report(result), encoding="utf-8")
    paths["evidence_md"].write_text(render_evidence_coverage_report(result), encoding="utf-8")
    paths["reconstructed_md"].write_text(render_reconstructed_snapshot_report(result), encoding="utf-8")
    paths["false_positive_md"].write_text(render_false_positive_report(result), encoding="utf-8")
    paths["limitations_md"].write_text(render_limitations(result), encoding="utf-8")
    return AsOfResearchReplayResult(
        config=result.config,
        snapshots=result.snapshots,
        discovered_candidates=result.discovered_candidates,
        benchmark_recall=result.benchmark_recall,
        output_root=output_root,
        report_paths=paths,
    )


def _write_candidates(csv_path: Path, json_path: Path, rows: Sequence[AsOfReplayCandidate]) -> None:
    json_path.write_text(json.dumps(_jsonable(rows), ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=(
                "symbol",
                "company_name",
                "as_of_date",
                "large_sector_id",
                "canonical_archetype_id",
                "layer",
                "stage",
                "rank",
                "reason_codes",
                "score",
                "visible_score",
                "candidate_source_path",
                "date_verified_documents",
                "date_unverified_documents",
                "rejected_future_documents",
                "web_only_stage",
                "merged_stage",
                "web_only_score",
                "merged_score",
                "score_valid",
                "score_blocked_reason",
                "score_fingerprint",
                "research_input_fingerprint",
                "score_variability_drivers",
                "web_only_score_valid",
                "web_only_score_blocked_reason",
                "web_only_score_fingerprint",
                "web_only_research_input_fingerprint",
                "web_only_score_variability_drivers",
                "promotion_delta",
                "promotion_band",
                "score_source_mode",
                "runtime_fixture_injected",
                "runtime_fixture_evidence_count",
                "merged_evidence_count",
                "eps_fcf_explosion_score",
                "earnings_visibility_score",
                "bottleneck_pricing_score",
                "market_mispricing_score",
                "valuation_rerating_score",
                "capital_allocation_score",
                "information_confidence_score",
                "risk_penalty",
                "claim_backed_claim_count",
                "claim_backed_primitive_count",
                "score_claim_backed_component_count",
                "orphan_score_component_count",
                "score_claim_backed_component_ratio",
                "claim_ledger_claim_ids",
                "claim_ledger_claim_ids_by_primitive",
                "score_contribution_claim_ids",
                "score_contribution_ledger",
                "source_backed_green_bridge_raw",
                "evidence_contract_required_primitive_count",
                "evidence_contract_present_primitive_count",
                "evidence_contract_missing_primitive_count",
                "evidence_contract_coverage_pct",
                "evidence_contract_positive_coverage_pct",
                "evidence_contract_positive_missing_primitive_count",
                "evidence_contract_green_gate_coverage_pct",
                "evidence_contract_green_gate_missing_primitive_count",
                "evidence_contract_guard_present_primitive_count",
                "evidence_contract_guard_cleared_primitive_count",
                "evidence_contract_guard_missing_primitive_count",
                "evidence_contract_missing_primitives",
                "evidence_contract_positive_missing_primitives",
                "evidence_contract_green_gate_primitives",
                "evidence_contract_green_gate_missing_primitives",
                "evidence_contract_guard_primitives",
                "evidence_contract_guard_present_primitives",
                "evidence_contract_guard_cleared_primitives",
                "evidence_contract_guard_missing_primitives",
                "evidence_contract_required_primitives",
                "evidence_contract_required_bridge_axes",
            ),
        )
        writer.writeheader()
        for item in rows:
            score_payload = normalized_score_state_payload(
                {
                    "score": item.score,
                    "merged_score": item.merged_score,
                    "score_valid": item.score_valid,
                    "score_blocked_reason": item.score_blocked_reason,
                }
            )
            score = score_payload.get("score")
            visible_score = score_payload.get("visible_score")
            merged_score = score_payload.get("merged_score")
            web_only_payload = (
                normalized_score_state_payload(
                    {
                        "score": item.web_only_score,
                        "score_valid": item.web_only_score_valid,
                        "score_blocked_reason": item.web_only_score_blocked_reason,
                    }
                )
                if item.web_only_score is not None or item.web_only_score_valid is not None or item.web_only_score_blocked_reason
                else {}
            )
            web_only_score = web_only_payload.get("score")
            writer.writerow(
                {
                    "symbol": item.symbol,
                    "company_name": item.company_name,
                    "as_of_date": item.as_of_date.isoformat(),
                    "large_sector_id": item.large_sector_id or "",
                    "canonical_archetype_id": item.canonical_archetype_id or "",
                    "layer": item.layer,
                    "stage": item.stage.value,
                    "rank": item.rank,
                    "reason_codes": "|".join(item.reason_codes),
                    "score": score if score is not None else "",
                    "visible_score": visible_score if visible_score is not None else "",
                    "candidate_source_path": item.candidate_source_path,
                    "date_verified_documents": item.date_verified_documents,
                    "date_unverified_documents": item.date_unverified_documents,
                    "rejected_future_documents": item.rejected_future_documents,
                    "web_only_stage": item.web_only_stage.value if item.web_only_stage else "",
                    "merged_stage": item.merged_stage.value if item.merged_stage else "",
                    "web_only_score": web_only_score if web_only_score is not None else "",
                    "merged_score": merged_score if merged_score is not None else "",
                    "score_valid": score_payload.get("score_valid") if score_payload.get("score_valid") is not None else "",
                    "score_blocked_reason": score_payload.get("score_blocked_reason") or "",
                    "score_fingerprint": item.score_fingerprint or "",
                    "research_input_fingerprint": item.research_input_fingerprint or "",
                    "score_variability_drivers": "|".join(item.score_variability_drivers),
                    "web_only_score_valid": web_only_payload.get("score_valid") if web_only_payload.get("score_valid") is not None else "",
                    "web_only_score_blocked_reason": web_only_payload.get("score_blocked_reason") or "",
                    "web_only_score_fingerprint": item.web_only_score_fingerprint or "",
                    "web_only_research_input_fingerprint": item.web_only_research_input_fingerprint or "",
                    "web_only_score_variability_drivers": "|".join(item.web_only_score_variability_drivers),
                    "promotion_delta": item.promotion_delta,
                    "promotion_band": item.promotion_band,
                    "score_source_mode": item.score_source_mode,
                    "runtime_fixture_injected": item.runtime_fixture_injected,
                    "runtime_fixture_evidence_count": item.runtime_fixture_evidence_count,
                    "merged_evidence_count": item.merged_evidence_count,
                    "eps_fcf_explosion_score": item.eps_fcf_explosion_score if item.eps_fcf_explosion_score is not None else "",
                    "earnings_visibility_score": item.earnings_visibility_score if item.earnings_visibility_score is not None else "",
                    "bottleneck_pricing_score": item.bottleneck_pricing_score if item.bottleneck_pricing_score is not None else "",
                    "market_mispricing_score": item.market_mispricing_score if item.market_mispricing_score is not None else "",
                    "valuation_rerating_score": item.valuation_rerating_score if item.valuation_rerating_score is not None else "",
                    "capital_allocation_score": item.capital_allocation_score if item.capital_allocation_score is not None else "",
                    "information_confidence_score": item.information_confidence_score if item.information_confidence_score is not None else "",
                    "risk_penalty": item.risk_penalty if item.risk_penalty is not None else "",
                    "claim_backed_claim_count": item.claim_backed_claim_count if item.claim_backed_claim_count is not None else "",
                    "claim_backed_primitive_count": item.claim_backed_primitive_count if item.claim_backed_primitive_count is not None else "",
                    "score_claim_backed_component_count": item.score_claim_backed_component_count if item.score_claim_backed_component_count is not None else "",
                    "orphan_score_component_count": item.orphan_score_component_count if item.orphan_score_component_count is not None else "",
                    "score_claim_backed_component_ratio": item.score_claim_backed_component_ratio if item.score_claim_backed_component_ratio is not None else "",
                    "claim_ledger_claim_ids": json.dumps(_jsonable(item.claim_ledger_claim_ids), ensure_ascii=False, sort_keys=True),
                    "claim_ledger_claim_ids_by_primitive": json.dumps(_jsonable(item.claim_ledger_claim_ids_by_primitive), ensure_ascii=False, sort_keys=True),
                    "score_contribution_claim_ids": json.dumps(_jsonable(item.score_contribution_claim_ids), ensure_ascii=False, sort_keys=True),
                    "score_contribution_ledger": json.dumps(_jsonable(item.score_contribution_ledger), ensure_ascii=False, sort_keys=True),
                    "source_backed_green_bridge_raw": item.source_backed_green_bridge_raw if item.source_backed_green_bridge_raw is not None else "",
                    "evidence_contract_required_primitive_count": item.evidence_contract_required_primitive_count if item.evidence_contract_required_primitive_count is not None else "",
                    "evidence_contract_present_primitive_count": item.evidence_contract_present_primitive_count if item.evidence_contract_present_primitive_count is not None else "",
                    "evidence_contract_missing_primitive_count": item.evidence_contract_missing_primitive_count if item.evidence_contract_missing_primitive_count is not None else "",
                    "evidence_contract_coverage_pct": item.evidence_contract_coverage_pct if item.evidence_contract_coverage_pct is not None else "",
                    "evidence_contract_positive_coverage_pct": item.evidence_contract_positive_coverage_pct if item.evidence_contract_positive_coverage_pct is not None else "",
                    "evidence_contract_positive_missing_primitive_count": item.evidence_contract_positive_missing_primitive_count if item.evidence_contract_positive_missing_primitive_count is not None else "",
                    "evidence_contract_green_gate_coverage_pct": item.evidence_contract_green_gate_coverage_pct if item.evidence_contract_green_gate_coverage_pct is not None else "",
                    "evidence_contract_green_gate_missing_primitive_count": item.evidence_contract_green_gate_missing_primitive_count if item.evidence_contract_green_gate_missing_primitive_count is not None else "",
                    "evidence_contract_guard_present_primitive_count": item.evidence_contract_guard_present_primitive_count if item.evidence_contract_guard_present_primitive_count is not None else "",
                    "evidence_contract_guard_cleared_primitive_count": item.evidence_contract_guard_cleared_primitive_count if item.evidence_contract_guard_cleared_primitive_count is not None else "",
                    "evidence_contract_guard_missing_primitive_count": item.evidence_contract_guard_missing_primitive_count if item.evidence_contract_guard_missing_primitive_count is not None else "",
                    "evidence_contract_missing_primitives": item.evidence_contract_missing_primitives or "",
                    "evidence_contract_positive_missing_primitives": item.evidence_contract_positive_missing_primitives or "",
                    "evidence_contract_green_gate_primitives": item.evidence_contract_green_gate_primitives or "",
                    "evidence_contract_green_gate_missing_primitives": item.evidence_contract_green_gate_missing_primitives or "",
                    "evidence_contract_guard_primitives": item.evidence_contract_guard_primitives or "",
                    "evidence_contract_guard_present_primitives": item.evidence_contract_guard_present_primitives or "",
                    "evidence_contract_guard_cleared_primitives": item.evidence_contract_guard_cleared_primitives or "",
                    "evidence_contract_guard_missing_primitives": item.evidence_contract_guard_missing_primitives or "",
                    "evidence_contract_required_primitives": item.evidence_contract_required_primitives or "",
                    "evidence_contract_required_bridge_axes": item.evidence_contract_required_bridge_axes or "",
                }
            )


def _replay_dates(start: date, end: date, frequency: ReplayFrequency) -> tuple[date, ...]:
    values: list[date] = []
    cursor = start
    while cursor <= end:
        values.append(cursor)
        if frequency == ReplayFrequency.DAILY:
            cursor += timedelta(days=1)
        elif frequency == ReplayFrequency.WEEKLY:
            cursor += timedelta(days=7)
        else:
            year = cursor.year + (1 if cursor.month == 12 else 0)
            month = 1 if cursor.month == 12 else cursor.month + 1
            cursor = date(year, month, 1)
    return tuple(values)


def _normalise_extra_replay_date(value: date | str) -> date:
    if isinstance(value, date):
        return value
    return date.fromisoformat(str(value))


def _scheduled_replay_dates(
    start: date,
    end: date,
    frequency: ReplayFrequency,
    extra_replay_dates: Sequence[date | str] = (),
) -> tuple[date, ...]:
    base_dates = set(_replay_dates(start, end, frequency))
    for item in extra_replay_dates:
        extra_date = _normalise_extra_replay_date(item)
        if start <= extra_date <= end:
            base_dates.add(extra_date)
    return tuple(sorted(base_dates))


def _jsonable(value: Any) -> Any:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Path):
        return str(value)
    if is_dataclass(value):
        payload = {field.name: _jsonable(getattr(value, field.name)) for field in fields(value)}
        if "score" in payload and "score_valid" in payload:
            payload = normalized_score_state_payload(payload)
        if "web_only_score" in payload and "web_only_score_valid" in payload:
            web_only_payload = (
                normalized_score_state_payload(
                    {
                        "score": payload.get("web_only_score"),
                        "score_valid": payload.get("web_only_score_valid"),
                        "score_blocked_reason": payload.get("web_only_score_blocked_reason"),
                    }
                )
                if payload.get("web_only_score") is not None
                or payload.get("web_only_score_valid") is not None
                or payload.get("web_only_score_blocked_reason")
                else {}
            )
            if web_only_payload:
                payload["web_only_score"] = web_only_payload.get("score")
                payload["web_only_score_valid"] = web_only_payload.get("score_valid")
                payload["web_only_score_blocked_reason"] = web_only_payload.get("score_blocked_reason")
        return payload
    if isinstance(value, Mapping):
        return normalized_score_state_mapping_if_present({str(key): _jsonable(item) for key, item in value.items()})
    if isinstance(value, (list, tuple, set, frozenset)):
        return [_jsonable(item) for item in value]
    return value


__all__ = [
    "AsOfReplayCandidate",
    "AsOfResearchReplay",
    "AsOfResearchReplayConfig",
    "AsOfResearchReplayResult",
    "AsOfResearchReplaySnapshot",
    "BenchmarkAsOfRecallRow",
    "FlowTrace",
    "FlowTraceStep",
    "render_asof_replay_summary",
]
