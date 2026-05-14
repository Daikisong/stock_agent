"""Historical E2R_STANDARD replay without hidden benchmark inputs."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field, fields, is_dataclass
from datetime import date, datetime, timedelta
from enum import Enum
from pathlib import Path
from typing import Any, Mapping

from e2r.backtest.historical_source_adapter import (
    HistoricalPointInTimeSourceAdapter,
    HistoricalSourceCoverage,
)
from e2r.backtest.historical_universe_replay import (
    HistoricalReplayConfig,
    HistoricalReplayMode,
    HistoricalUniverseReplay,
    ReplayFrequency,
)
from e2r.backtest.stage_lifecycle_detector import (
    StageLifecycleDetection,
    StageLifecycleDetectionInput,
    StageLifecycleDetector,
)
from e2r.models import Market, Stage
from e2r.pipeline.e2r_standard_flow import E2R_STANDARD, E2RStandardConfig, E2RStandardFlow
from e2r.research.search_budget import SearchBudget


@dataclass(frozen=True)
class E2RStandardReplayConfig:
    """Configuration for true E2R_STANDARD historical replay."""

    start_date: date
    end_date: date
    replay_frequency: ReplayFrequency | str = ReplayFrequency.MONTHLY
    market: Market | str = Market.KR
    output_directory: str | Path = "output/backtests/blind_discovery"
    universe_limit: int | None = None
    max_candidates_per_date: int = 50
    case_root: str | Path = "data/historical_cases"
    search_snapshot_root: str | Path = "data/search_snapshots"
    report_snapshot_root: str | Path = "data/report_snapshots"
    use_search_snapshots: bool = True
    use_report_snapshots: bool = True
    allow_fixture_source_proxy: bool = False
    llm_enabled: bool = False

    def __post_init__(self) -> None:
        if not isinstance(self.replay_frequency, ReplayFrequency):
            object.__setattr__(self, "replay_frequency", ReplayFrequency(str(self.replay_frequency)))
        if not isinstance(self.market, Market):
            object.__setattr__(self, "market", Market(str(self.market)))
        if self.end_date < self.start_date:
            raise ValueError("end_date cannot be before start_date")
        if self.max_candidates_per_date <= 0:
            raise ValueError("max_candidates_per_date must be positive")


@dataclass(frozen=True)
class E2RStandardReplayCandidate:
    """One candidate discovered by true E2R_STANDARD replay."""

    symbol: str
    company_name: str
    as_of_date: date
    layer: str
    stage: Stage
    rank: int
    score: float
    evidence_types_seen: tuple[str, ...]
    reason_codes: tuple[str, ...]
    candidate_source_path: str
    lifecycle_status: str = "unknown_insufficient_evidence"
    lifecycle_stage: Stage | None = None
    missing_evidence_warnings: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        object.__setattr__(self, "evidence_types_seen", tuple(dict.fromkeys(self.evidence_types_seen)))
        object.__setattr__(self, "reason_codes", tuple(dict.fromkeys(self.reason_codes)))
        object.__setattr__(self, "missing_evidence_warnings", tuple(dict.fromkeys(self.missing_evidence_warnings)))


@dataclass(frozen=True)
class E2RStandardReplaySnapshot:
    """One replay date result."""

    as_of_date: date
    candidates: tuple[E2RStandardReplayCandidate, ...]
    source_coverage: HistoricalSourceCoverage
    true_standard_flow_used: bool = True
    fixture_proxy_used: bool = False
    limitations: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class E2RStandardReplayResult:
    """Complete E2R_STANDARD replay output."""

    config: E2RStandardReplayConfig
    snapshots: tuple[E2RStandardReplaySnapshot, ...]
    candidates: tuple[E2RStandardReplayCandidate, ...]
    source_coverage_summary: Mapping[str, Any]
    true_standard_flow_used: bool = True
    fixture_proxy_used: bool = False
    benchmark_labels_used_before_candidate_generation: bool = False
    limitations: tuple[str, ...] = field(default_factory=tuple)


class E2RStandardReplay:
    """Replay canonical E2R_STANDARD over point-in-time historical snapshots."""

    def run(self, config: E2RStandardReplayConfig) -> E2RStandardReplayResult:
        if config.allow_fixture_source_proxy:
            return _run_fixture_proxy(config)
        adapter = HistoricalPointInTimeSourceAdapter(
            search_snapshot_root=config.search_snapshot_root,
            report_snapshot_root=config.report_snapshot_root,
        )
        snapshots: list[E2RStandardReplaySnapshot] = []
        for replay_date in _replay_dates(config.start_date, config.end_date, config.replay_frequency):
            bundle = adapter.build(
                as_of_date=replay_date,
                market=config.market,
                use_search_snapshots=config.use_search_snapshots,
                use_report_snapshots=config.use_report_snapshots,
            )
            if not bundle.coverage.universe_available:
                snapshots.append(
                    E2RStandardReplaySnapshot(
                        as_of_date=replay_date,
                        candidates=(),
                        source_coverage=bundle.coverage,
                        limitations=bundle.coverage.limitations(),
                    )
                )
                continue
            flow_result = E2RStandardFlow().run(
                E2RStandardConfig(
                    as_of_date=replay_date,
                    market=config.market,
                    sources=bundle.sources,
                    universe_limit=config.universe_limit,
                    top_candidates=config.max_candidates_per_date,
                    fixture_mode=True,
                    report_radar_enabled=True,
                    report_radar_universe_limit=config.max_candidates_per_date,
                    search_budget=SearchBudget(
                        max_total_queries_per_day=max(200, config.max_candidates_per_date * 20),
                        max_queries_per_symbol=40,
                        max_deep_research_symbols=config.max_candidates_per_date,
                    ),
                    browser_provider=bundle.search_provider,
                    free_search_provider=bundle.search_provider,
                    fixture_text_by_url=bundle.fixture_text_by_url,
                    llm_enabled=config.llm_enabled,
                )
            )
            rows = _candidate_rows(flow_result, bundle.coverage)
            snapshots.append(
                E2RStandardReplaySnapshot(
                    as_of_date=replay_date,
                    candidates=tuple(rows[: config.max_candidates_per_date]),
                    source_coverage=bundle.coverage,
                    limitations=bundle.coverage.limitations(),
                )
            )
        candidates = tuple(item for snapshot in snapshots for item in snapshot.candidates)
        return E2RStandardReplayResult(
            config=config,
            snapshots=tuple(snapshots),
            candidates=candidates,
            source_coverage_summary=_source_coverage_summary(snapshots),
            limitations=_aggregate_limitations(snapshots),
        )


def _run_fixture_proxy(config: E2RStandardReplayConfig) -> E2RStandardReplayResult:
    """Explicit diagnostic fallback using curated case fixtures.

    This path is not proof of blind discovery. It is intentionally available
    only when ``allow_fixture_source_proxy=True``.
    """

    proxy_config = HistoricalReplayConfig(
        start_date=config.start_date,
        end_date=config.end_date,
        replay_frequency=config.replay_frequency,
        mode=HistoricalReplayMode.HYBRID,
        market=config.market,
        universe_limit=config.universe_limit,
        max_candidates_per_date=config.max_candidates_per_date,
        output_directory=Path(config.output_directory) / "_fixture_proxy_internal",
        case_root=config.case_root,
    )
    proxy = HistoricalUniverseReplay().run(proxy_config, write_outputs=False)
    coverage = HistoricalSourceCoverage(
        universe_available=True,
        price_available=True,
        disclosure_available=True,
        financial_available=True,
        search_snapshot_available=False,
        report_snapshot_available=False,
        coverage_notes=("fixture_proxy_mode_not_proof_of_live_discovery",),
    )
    snapshots: list[E2RStandardReplaySnapshot] = []
    for proxy_snapshot in proxy.snapshots:
        candidates: list[E2RStandardReplayCandidate] = []
        ranked = sorted(proxy_snapshot.candidates, key=lambda item: (-item.layer1_score, -item.total_score, item.symbol))
        for rank, item in enumerate(ranked, start=1):
            candidates.append(
                E2RStandardReplayCandidate(
                    symbol=item.symbol,
                    company_name=item.company_name,
                    as_of_date=item.as_of_date,
                    layer=item.layer1_result,
                    stage=item.stage,
                    rank=rank,
                    score=item.total_score,
                    evidence_types_seen=tuple(item.evidence_types_seen),
                    reason_codes=tuple(item.reason_codes),
                    candidate_source_path=item.candidate_source_path,
                    missing_evidence_warnings=("fixture_proxy_mode",) + tuple(item.missing_evidence_warnings),
                )
            )
        snapshots.append(
            E2RStandardReplaySnapshot(
                as_of_date=proxy_snapshot.as_of_date,
                candidates=tuple(candidates),
                source_coverage=coverage,
                true_standard_flow_used=False,
                fixture_proxy_used=True,
                limitations=("fixture proxy mode; not proof of live discovery",),
            )
        )
    candidates = tuple(item for snapshot in snapshots for item in snapshot.candidates)
    return E2RStandardReplayResult(
        config=config,
        snapshots=tuple(snapshots),
        candidates=candidates,
        source_coverage_summary=_source_coverage_summary(snapshots),
        true_standard_flow_used=False,
        fixture_proxy_used=True,
        limitations=("fixture proxy mode; not proof of live discovery",),
    )


def _candidate_rows(flow_result, coverage: HistoricalSourceCoverage) -> tuple[E2RStandardReplayCandidate, ...]:
    scores_by_symbol = {item.symbol: item for item in flow_result.scores}
    stages_by_symbol = {item.symbol: item for item in flow_result.stages}
    evidence_by_symbol: dict[str, set[str]] = {}
    for item in flow_result.evidence:
        evidence_by_symbol.setdefault(item.symbol, set()).add(item.source_type)
    rows: list[E2RStandardReplayCandidate] = []
    ranked = sorted(flow_result.candidates, key=lambda item: (-item.cheap_scan_total_score, item.symbol))
    for rank, candidate in enumerate(ranked, start=1):
        stage_snapshot = stages_by_symbol.get(candidate.symbol)
        score = scores_by_symbol.get(candidate.symbol)
        stage = stage_snapshot.stage if stage_snapshot is not None else Stage.STAGE_1
        lifecycle = _detect_lifecycle(candidate.symbol, candidate.as_of_date, stage, score)
        rows.append(
            E2RStandardReplayCandidate(
                symbol=candidate.symbol,
                company_name=candidate.company_name,
                as_of_date=candidate.as_of_date,
                layer=candidate.recommended_next_layer.value,
                stage=stage,
                rank=rank,
                score=score.total_score if score is not None else candidate.cheap_scan_total_score,
                evidence_types_seen=tuple(sorted(evidence_by_symbol.get(candidate.symbol, ()))) or ("search_snapshot",),
                reason_codes=tuple(candidate.reason_codes),
                candidate_source_path=candidate.candidate_source_path,
                lifecycle_status=lifecycle.status,
                lifecycle_stage=lifecycle.lifecycle_stage,
                missing_evidence_warnings=coverage.limitations(),
            )
        )
    return tuple(rows)


def _detect_lifecycle(symbol: str, as_of_date: date, stage: Stage, score) -> StageLifecycleDetection:
    if stage not in {Stage.STAGE_3_GREEN, Stage.STAGE_3_YELLOW, Stage.STAGE_3_RED, Stage.STAGE_4A, Stage.STAGE_4B}:
        return StageLifecycleDetector().detect(
            StageLifecycleDetectionInput(
                symbol=symbol,
                as_of_date=as_of_date,
                previous_stage=stage,
                stage3_evidence_intact=False,
                eps_fcf_visibility_strong=False,
            )
        )
    return StageLifecycleDetector().detect(
        StageLifecycleDetectionInput(
            symbol=symbol,
            as_of_date=as_of_date,
            previous_stage=stage,
            valuation_rerating_score=getattr(score, "valuation_rerating_score", None),
            stage3_evidence_intact=True,
            eps_fcf_visibility_strong=True,
        )
    )


def _replay_dates(start: date, end: date, frequency: ReplayFrequency) -> tuple[date, ...]:
    dates: list[date] = []
    cursor = start
    while cursor <= end:
        dates.append(cursor)
        if frequency == ReplayFrequency.DAILY:
            cursor += timedelta(days=1)
        elif frequency == ReplayFrequency.WEEKLY:
            cursor += timedelta(days=7)
        else:
            year = cursor.year + (1 if cursor.month == 12 else 0)
            month = 1 if cursor.month == 12 else cursor.month + 1
            cursor = date(year, month, 1)
    return tuple(dates)


def _source_coverage_summary(snapshots: list[E2RStandardReplaySnapshot] | tuple[E2RStandardReplaySnapshot, ...]) -> Mapping[str, Any]:
    total = len(snapshots)
    if total == 0:
        return {"replay_dates": 0}
    counters = Counter()
    notes = Counter()
    for snapshot in snapshots:
        coverage = snapshot.source_coverage
        for key in (
            "universe_available",
            "price_available",
            "disclosure_available",
            "financial_available",
            "search_snapshot_available",
            "report_snapshot_available",
            "llm_available",
        ):
            if getattr(coverage, key):
                counters[key] += 1
        for note in coverage.limitations():
            notes[note] += 1
    return {
        "replay_dates": total,
        **{key: counters[key] for key in counters},
        "limitations": dict(notes),
    }


def _aggregate_limitations(snapshots: list[E2RStandardReplaySnapshot] | tuple[E2RStandardReplaySnapshot, ...]) -> tuple[str, ...]:
    values: list[str] = []
    for snapshot in snapshots:
        values.extend(snapshot.limitations)
    if not values:
        values.append("no_limitations_recorded")
    return tuple(dict.fromkeys(values))


def jsonable(value: Any) -> Any:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Path):
        return str(value)
    if is_dataclass(value):
        return {field.name: jsonable(getattr(value, field.name)) for field in fields(value)}
    if isinstance(value, Mapping):
        return {str(key): jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set, frozenset)):
        return [jsonable(item) for item in value]
    return value


__all__ = [
    "E2RStandardReplay",
    "E2RStandardReplayCandidate",
    "E2RStandardReplayConfig",
    "E2RStandardReplayResult",
    "E2RStandardReplaySnapshot",
    "jsonable",
]
