"""Historical universe replay for E2R Layer-1 and stage lifecycle analysis."""

from __future__ import annotations

import json
from dataclasses import dataclass, fields, is_dataclass, replace
from datetime import date, datetime, timedelta
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.backtest.layer1_recall import (
    LAYER_DEEP_RESEARCH,
    LAYER_EVENT_SEARCH,
    LAYER_NONE,
    LAYER_STAGE2_OR_HIGHER,
    Layer1RecallCase,
    Layer1RecallResult,
    evaluate_layer1_recall_case,
)
from e2r.backtest.stage_lifecycle_backtest import (
    StageLifecycleBacktest,
    StageLifecycleInput,
    StageLifecycleResult,
    write_stage_lifecycle_outputs,
)
from e2r.features import DeterministicFeatureEngineer, FeatureEngineeringInput
from e2r.historical_cases import HistoricalCase, load_historical_cases
from e2r.models import Evidence, Market, PriceBar, Stage
from e2r.red_team import RedTeamEngine
from e2r.staging import StageClassificationInput, StageClassifier


DEFAULT_HISTORICAL_REPLAY_OUTPUT_DIR = Path("output/backtests/historical_replay")


class HistoricalReplayMode(str, Enum):
    """Historical source modes with explicit report/news availability boundaries."""

    OFFICIAL_ONLY = "official_only"
    CASE_FIXTURE = "case_fixture"
    HYBRID = "hybrid"


class ReplayFrequency(str, Enum):
    """Replay date cadence."""

    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"


@dataclass(frozen=True)
class HistoricalReplayConfig:
    """Configuration for fixture-backed historical universe replay."""

    start_date: date
    end_date: date
    replay_frequency: ReplayFrequency | str = ReplayFrequency.MONTHLY
    mode: HistoricalReplayMode | str = HistoricalReplayMode.CASE_FIXTURE
    market: Market | str = Market.KR
    universe_limit: int | None = None
    max_candidates_per_date: int = 50
    max_report_radar_queries_per_date: int = 0
    require_point_in_time: bool = True
    output_directory: str | Path = DEFAULT_HISTORICAL_REPLAY_OUTPUT_DIR
    case_root: str | Path = "data/historical_cases"

    def __post_init__(self) -> None:
        if not isinstance(self.mode, HistoricalReplayMode):
            object.__setattr__(self, "mode", HistoricalReplayMode(str(self.mode)))
        if not isinstance(self.replay_frequency, ReplayFrequency):
            object.__setattr__(self, "replay_frequency", ReplayFrequency(str(self.replay_frequency)))
        if not isinstance(self.market, Market):
            object.__setattr__(self, "market", Market(str(self.market)))
        if self.end_date < self.start_date:
            raise ValueError("end_date cannot be before start_date")
        if self.universe_limit is not None and self.universe_limit <= 0:
            raise ValueError("universe_limit must be positive")
        if self.max_candidates_per_date <= 0:
            raise ValueError("max_candidates_per_date must be positive")
        if self.max_report_radar_queries_per_date < 0:
            raise ValueError("max_report_radar_queries_per_date must be non-negative")


@dataclass(frozen=True)
class HistoricalReplayCandidate:
    """One symbol discovered by historical Layer-1 replay."""

    case_id: str
    symbol: str
    company_name: str
    as_of_date: date
    stage: Stage
    total_score: float
    layer1_result: str
    layer1_score: float
    candidate_source_path: str
    reason_codes: tuple[str, ...]
    evidence_types_seen: tuple[str, ...]
    missing_evidence_warnings: tuple[str, ...] = ()


@dataclass(frozen=True)
class HistoricalReplayDroppedCandidate:
    """One instrument scanned but not promoted to a historical replay candidate."""

    case_id: str
    symbol: str
    company_name: str
    as_of_date: date
    dropped_reason: str
    evidence_types_seen: tuple[str, ...]
    stage: Stage
    total_score: float


@dataclass(frozen=True)
class HistoricalReplayStageRecord:
    """Compact stage snapshot stored inside replay output."""

    case_id: str
    symbol: str
    company_name: str
    as_of_date: date
    stage: Stage
    total_score: float
    red_team_status: str
    evidence_ids: tuple[str, ...]


@dataclass(frozen=True)
class HistoricalReplaySnapshot:
    """Replay result for one historical date."""

    as_of_date: date
    instruments_scanned: int
    candidates: tuple[HistoricalReplayCandidate, ...]
    dropped_candidates: tuple[HistoricalReplayDroppedCandidate, ...]
    stage_snapshots: tuple[HistoricalReplayStageRecord, ...]
    evidence_counts: Mapping[str, int]
    reason_code_distribution: Mapping[str, int]
    missing_evidence_warnings: tuple[str, ...]
    source_coverage_summary: Mapping[str, Any]


@dataclass(frozen=True)
class KnownCaseValidation:
    """Known-case validation row for structural and boom-bust fixtures."""

    case_id: str
    symbol: str
    company_name: str
    expected_group: str
    status: str
    final_stage: Stage | None
    layer1_result: str | None
    failure_reason: str | None = None


@dataclass(frozen=True)
class HistoricalUniverseReplayResult:
    """Complete historical replay output and report paths."""

    config: HistoricalReplayConfig
    snapshots: tuple[HistoricalReplaySnapshot, ...]
    lifecycle_results: tuple[StageLifecycleResult, ...]
    known_case_validations: tuple[KnownCaseValidation, ...]
    summary_json_path: Path | None = None
    summary_md_path: Path | None = None
    lifecycle_json_path: Path | None = None
    lifecycle_csv_path: Path | None = None
    top_stage3_path: Path | None = None
    false_positive_path: Path | None = None
    missed_winner_path: Path | None = None


class HistoricalUniverseReplay:
    """Replay historical fixture universe without using future evidence."""

    def run(self, config: HistoricalReplayConfig, *, write_outputs: bool = True) -> HistoricalUniverseReplayResult:
        cases = _filtered_cases(config)
        replay_dates = tuple(_replay_dates(config.start_date, config.end_date, config.replay_frequency))
        snapshots = tuple(self._snapshot_for_date(config, cases, replay_date) for replay_date in replay_dates)
        lifecycle_results = self._lifecycle_results(config, cases, snapshots)
        validations = _known_case_validations(config, cases, snapshots)
        result = HistoricalUniverseReplayResult(
            config=config,
            snapshots=snapshots,
            lifecycle_results=lifecycle_results,
            known_case_validations=validations,
        )
        if not write_outputs:
            return result
        return _write_outputs(result)

    def _snapshot_for_date(
        self,
        config: HistoricalReplayConfig,
        cases: Sequence[HistoricalCase],
        replay_date: date,
    ) -> HistoricalReplaySnapshot:
        candidates: list[HistoricalReplayCandidate] = []
        dropped: list[HistoricalReplayDroppedCandidate] = []
        stages: list[HistoricalReplayStageRecord] = []
        evidence_counts: dict[str, int] = {}
        reason_counts: dict[str, int] = {}
        warnings: list[str] = []
        scanned = 0

        for case in cases:
            scanned += 1
            view = _case_view(case, replay_date, config.mode)
            replayed = _score_view(view, replay_date)
            for evidence_type in _evidence_counts(view):
                evidence_counts[evidence_type] = evidence_counts.get(evidence_type, 0) + 1
            missing = _missing_evidence_warnings(case, view, config.mode)
            warnings.extend(f"{case.case_id}:{item}" for item in missing)
            layer1 = _layer1_result(view, replay_date, case.expected_stage)
            reason_codes = _reason_codes(layer1, replayed.stage, missing, config.mode)
            for code in reason_codes:
                reason_counts[code] = reason_counts.get(code, 0) + 1

            stages.append(
                HistoricalReplayStageRecord(
                    case_id=case.case_id,
                    symbol=case.symbol,
                    company_name=case.company_name,
                    as_of_date=replay_date,
                    stage=replayed.stage,
                    total_score=replayed.total_score,
                    red_team_status=replayed.red_team_status,
                    evidence_ids=replayed.evidence_ids,
                )
            )

            if _is_candidate(layer1, replayed.stage):
                candidates.append(
                    HistoricalReplayCandidate(
                        case_id=case.case_id,
                        symbol=case.symbol,
                        company_name=case.company_name,
                        as_of_date=replay_date,
                        stage=replayed.stage,
                        total_score=replayed.total_score,
                        layer1_result=layer1.actual_layer1_result,
                        layer1_score=layer1.layer1_score,
                        candidate_source_path=_candidate_source_path(config.mode, layer1),
                        reason_codes=reason_codes,
                        evidence_types_seen=layer1.evidence_types_seen,
                        missing_evidence_warnings=missing,
                    )
                )
            else:
                dropped.append(
                    HistoricalReplayDroppedCandidate(
                        case_id=case.case_id,
                        symbol=case.symbol,
                        company_name=case.company_name,
                        as_of_date=replay_date,
                        dropped_reason=layer1.false_none_reason or _drop_reason(layer1, replayed.stage, missing),
                        evidence_types_seen=layer1.evidence_types_seen,
                        stage=replayed.stage,
                        total_score=replayed.total_score,
                    )
                )

        ranked_candidates = tuple(
            sorted(candidates, key=lambda item: (-item.layer1_score, -item.total_score, item.case_id))[
                : config.max_candidates_per_date
            ]
        )
        coverage = {
            "mode": config.mode.value,
            "report_news_available": config.mode in {HistoricalReplayMode.CASE_FIXTURE, HistoricalReplayMode.HYBRID},
            "report_radar_queries_allowed": config.max_report_radar_queries_per_date,
            "official_only_report_news_excluded": config.mode == HistoricalReplayMode.OFFICIAL_ONLY,
            "case_fixture_count": len(cases),
        }
        return HistoricalReplaySnapshot(
            as_of_date=replay_date,
            instruments_scanned=scanned,
            candidates=ranked_candidates,
            dropped_candidates=tuple(dropped),
            stage_snapshots=tuple(stages),
            evidence_counts=dict(sorted(evidence_counts.items())),
            reason_code_distribution=dict(sorted(reason_counts.items())),
            missing_evidence_warnings=tuple(dict.fromkeys(warnings)),
            source_coverage_summary=coverage,
        )

    def _lifecycle_results(
        self,
        config: HistoricalReplayConfig,
        cases: Sequence[HistoricalCase],
        snapshots: Sequence[HistoricalReplaySnapshot],
    ) -> tuple[StageLifecycleResult, ...]:
        events: dict[str, StageLifecycleInput] = {}
        case_by_id = {case.case_id: case for case in cases}
        for snapshot in snapshots:
            for candidate in snapshot.candidates:
                if candidate.stage not in _LIFECYCLE_STAGES or candidate.case_id in events:
                    continue
                case = case_by_id[candidate.case_id]
                stage_date = case.stage3_date if case.stage3_date >= config.start_date else candidate.as_of_date
                stage_bar = _bar_on_date(case.price_bars, stage_date)
                stage_price = case.stage3_price if stage_date == case.stage3_date else (stage_bar.close if stage_bar else None)
                if stage_price is None:
                    continue
                evidence_coverage_insufficient = bool(candidate.missing_evidence_warnings)
                events[candidate.case_id] = StageLifecycleInput(
                    symbol=case.symbol,
                    company_name=case.company_name,
                    stage=candidate.stage,
                    stage_date=stage_date,
                    stage_price=stage_price,
                    price_bars=case.price_bars,
                    stage_snapshots=case.stage_snapshots,
                    evidence_coverage_insufficient=evidence_coverage_insufficient,
                    source_mode=config.mode.value,
                )
        return StageLifecycleBacktest().evaluate_many(tuple(events.values()))


@dataclass(frozen=True)
class _ScoredView:
    stage: Stage
    total_score: float
    red_team_status: str
    evidence_ids: tuple[str, ...]


_LIFECYCLE_STAGES = {
    Stage.STAGE_2,
    Stage.STAGE_3_GREEN,
    Stage.STAGE_3_YELLOW,
    Stage.STAGE_3_RED,
}


def render_historical_replay_summary(result: HistoricalUniverseReplayResult) -> str:
    """Render the operator-facing summary report."""

    candidates = [candidate for snapshot in result.snapshots for candidate in snapshot.candidates]
    lifecycle = tuple(item for item in result.lifecycle_results if item.failure_reason is None)
    stage_counts: dict[str, int] = {}
    for candidate in candidates:
        stage_counts[candidate.stage.value] = stage_counts.get(candidate.stage.value, 0) + 1
    below_entry_count = sum(1 for item in lifecycle if item.below_entry_flag)
    lines = [
        "# Checkpoint 21 Historical Universe Replay",
        "",
        f"- mode: {result.config.mode.value}",
        f"- period: {result.config.start_date.isoformat()} to {result.config.end_date.isoformat()}",
        f"- replay_frequency: {result.config.replay_frequency.value}",
        f"- replay_dates: {len(result.snapshots)}",
        f"- stocks_scanned: {sum(snapshot.instruments_scanned for snapshot in result.snapshots)}",
        f"- event_search_or_higher: {sum(1 for item in candidates if item.layer1_result in {LAYER_EVENT_SEARCH, LAYER_DEEP_RESEARCH, LAYER_STAGE2_OR_HIGHER})}",
        f"- deep_research: {sum(1 for item in candidates if item.layer1_result == LAYER_DEEP_RESEARCH)}",
        f"- Stage 2: {stage_counts.get(Stage.STAGE_2.value, 0)}",
        f"- Stage 3-Green: {stage_counts.get(Stage.STAGE_3_GREEN.value, 0)}",
        f"- Stage 3-Yellow: {stage_counts.get(Stage.STAGE_3_YELLOW.value, 0)}",
        f"- Stage 3-Red: {stage_counts.get(Stage.STAGE_3_RED.value, 0)}",
        f"- below_entry_after_stage: {below_entry_count}",
        f"- average_time_to_50pct: {_avg(item.time_to_50pct for item in lifecycle)}",
        f"- average_time_to_100pct: {_avg(item.time_to_100pct for item in lifecycle)}",
        f"- average_time_to_200pct: {_avg(item.time_to_200pct for item in lifecycle)}",
        f"- reached_4B: {sum(1 for item in lifecycle if item.stage4b_date is not None)}",
        f"- reached_4C: {sum(1 for item in lifecycle if item.stage4c_date is not None)}",
        f"- still_active: {sum(1 for item in lifecycle if item.still_active_flag)}",
        "",
        "## Known Cases",
        "",
        "| case | group | status | stage | layer1 | reason |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in result.known_case_validations:
        lines.append(
            f"| {item.case_id} | {item.expected_group} | {item.status} | "
            f"{item.final_stage.value if item.final_stage else 'n/a'} | {item.layer1_result or 'n/a'} | "
            f"{item.failure_reason or ''} |"
        )
    return "\n".join(lines).rstrip() + "\n"


def render_top_stage3_candidates(result: HistoricalUniverseReplayResult) -> str:
    candidates = [
        candidate
        for snapshot in result.snapshots
        for candidate in snapshot.candidates
        if candidate.stage in {Stage.STAGE_3_GREEN, Stage.STAGE_3_YELLOW, Stage.STAGE_3_RED}
    ]
    lines = [
        "# Top Stage 3 Candidates",
        "",
        "| date | case | company | stage | score | layer1 | evidence |",
        "| --- | --- | --- | --- | ---: | --- | --- |",
    ]
    for item in sorted(candidates, key=lambda candidate: (candidate.as_of_date, -candidate.total_score))[:20]:
        lines.append(
            f"| {item.as_of_date.isoformat()} | {item.case_id} | {item.company_name} | {item.stage.value} | "
            f"{item.total_score:.1f} | {item.layer1_result} | {', '.join(item.evidence_types_seen)} |"
        )
    if len(lines) == 4:
        lines.append("| n/a | n/a | n/a | n/a | 0.0 | n/a | n/a |")
    return "\n".join(lines).rstrip() + "\n"


def render_false_positive_cases(result: HistoricalUniverseReplayResult) -> str:
    rows = [
        item
        for item in result.known_case_validations
        if item.expected_group == "warning_or_boom_bust" or item.status == "detected_but_yellow_red"
    ]
    lines = ["# False Positive And Warning Cases", ""]
    if not rows:
        lines.append("No warning fixtures were promoted to Stage 3-Green.")
        return "\n".join(lines).rstrip() + "\n"
    lines.extend(["| case | status | stage | reason |", "| --- | --- | --- | --- |"])
    for item in rows:
        lines.append(
            f"| {item.case_id} | {item.status} | {item.final_stage.value if item.final_stage else 'n/a'} | "
            f"{item.failure_reason or ''} |"
        )
    return "\n".join(lines).rstrip() + "\n"


def render_missed_winner_cases(result: HistoricalUniverseReplayResult) -> str:
    rows = [item for item in result.known_case_validations if item.status in {"missed", "skipped_missing_historical_report_news_data"}]
    lines = ["# Missed Winner Cases", ""]
    if not rows:
        lines.append("No structural winner misses were found in this fixture replay.")
        return "\n".join(lines).rstrip() + "\n"
    lines.extend(["| case | status | stage | layer1 | reason |", "| --- | --- | --- | --- | --- |"])
    for item in rows:
        lines.append(
            f"| {item.case_id} | {item.status} | {item.final_stage.value if item.final_stage else 'n/a'} | "
            f"{item.layer1_result or 'n/a'} | {item.failure_reason or ''} |"
        )
    return "\n".join(lines).rstrip() + "\n"


def _filtered_cases(config: HistoricalReplayConfig) -> tuple[HistoricalCase, ...]:
    cases = [
        case
        for case in load_historical_cases(config.case_root)
        if case.market == config.market and case.stage3_date <= config.end_date
    ]
    cases = sorted(cases, key=lambda item: (item.stage3_date, item.case_id))
    if config.universe_limit is not None:
        cases = cases[: config.universe_limit]
    return tuple(cases)


def _case_view(case: HistoricalCase, as_of_date: date, mode: HistoricalReplayMode) -> HistoricalCase:
    reports = tuple(item for item in case.research_reports if item.as_of_date <= as_of_date)
    news = tuple(item for item in case.news_items if item.as_of_date <= as_of_date)
    consensus = tuple(item for item in case.consensus if item.as_of_date <= as_of_date)
    revisions = tuple(item for item in case.consensus_revisions if item.as_of_date <= as_of_date)
    if mode == HistoricalReplayMode.OFFICIAL_ONLY:
        reports = ()
        news = ()
        consensus = ()
        revisions = ()
    evidence = tuple(_visible_evidence(case.evidence, as_of_date, mode))
    return replace(
        case,
        stage3_date=as_of_date,
        financial_actuals=tuple(item for item in case.financial_actuals if item.as_of_date <= as_of_date),
        consensus=consensus,
        consensus_revisions=revisions,
        disclosures=tuple(item for item in case.disclosures if item.available_at.date() <= as_of_date),
        research_reports=reports,
        news_items=news,
        evidence=evidence,
        price_bars=tuple(item for item in case.price_bars if item.as_of_date <= as_of_date),
    )


def _visible_evidence(evidence: Sequence[Evidence], as_of_date: date, mode: HistoricalReplayMode) -> tuple[Evidence, ...]:
    official_types = {"disclosure", "financial_actual"}
    rows = []
    for item in evidence:
        if item.available_at.date() > as_of_date or item.as_of_date > as_of_date:
            continue
        if mode == HistoricalReplayMode.OFFICIAL_ONLY and item.source_type not in official_types:
            continue
        rows.append(item)
    return tuple(rows)


def _score_view(case: HistoricalCase, replay_date: date) -> _ScoredView:
    feature_input = FeatureEngineeringInput(
        symbol=case.symbol,
        as_of_date=replay_date,
        price_bars=case.price_bars,
        financial_actuals=case.financial_actuals,
        consensus=case.consensus,
        consensus_revisions=case.consensus_revisions,
        disclosures=case.disclosures,
        research_reports=case.research_reports,
        news_items=case.news_items,
    )
    feature_result = DeterministicFeatureEngineer().engineer(feature_input)
    score = feature_result.score()
    red_team = RedTeamEngine().assess(feature_result.red_team_signals)
    stage = StageClassifier().classify(
        StageClassificationInput(
            score=score,
            red_team=red_team,
            theme_regime_score=80.0 if case.evidence else 0.0,
            company_event_score=80.0 if case.evidence else 0.0,
            evidence_ids=tuple(item.evidence_id for item in case.evidence),
        )
    )
    return _ScoredView(
        stage=stage.stage,
        total_score=score.total_score,
        red_team_status=red_team.risk_level.value,
        evidence_ids=stage.evidence_ids,
    )


def _layer1_result(case: HistoricalCase, replay_date: date, expected_stage: Stage | None) -> Layer1RecallResult:
    expected = Layer1RecallCase(
        case_id=case.case_id,
        symbol=case.symbol,
        company_name=case.company_name,
        as_of_date=replay_date,
        expected_trigger_date=replay_date,
        expected_layer1_min_result=LAYER_EVENT_SEARCH,
        expected_final_stage=expected_stage,
    )
    return evaluate_layer1_recall_case(case, expected)


def _is_candidate(layer1: Layer1RecallResult, stage: Stage) -> bool:
    return layer1.actual_layer1_result != LAYER_NONE or _stage_rank(stage) >= 1


def _reason_codes(
    layer1: Layer1RecallResult,
    stage: Stage,
    missing: Sequence[str],
    mode: HistoricalReplayMode,
) -> tuple[str, ...]:
    codes: list[str] = []
    for evidence_type in layer1.evidence_types_seen:
        codes.append(f"EVIDENCE_{evidence_type.upper()}")
    if layer1.actual_layer1_result == LAYER_DEEP_RESEARCH:
        codes.append("REACHED_DEEP_RESEARCH")
    elif layer1.actual_layer1_result == LAYER_EVENT_SEARCH:
        codes.append("REACHED_EVENT_SEARCH")
    if _stage_rank(stage) >= 2:
        codes.append("REACHED_STAGE2_OR_HIGHER")
    if mode == HistoricalReplayMode.OFFICIAL_ONLY:
        codes.append("OFFICIAL_ONLY")
    for item in missing:
        codes.append(item.upper())
    return tuple(dict.fromkeys(codes))


def _drop_reason(layer1: Layer1RecallResult, stage: Stage, missing: Sequence[str]) -> str:
    if missing:
        return missing[0]
    if not layer1.evidence_types_seen:
        return "source_missing"
    if _stage_rank(stage) < 1:
        return "below_stage1"
    return "below_candidate_threshold"


def _candidate_source_path(mode: HistoricalReplayMode, layer1: Layer1RecallResult) -> str:
    if mode == HistoricalReplayMode.OFFICIAL_ONLY:
        return "official_only"
    if "research_report" in layer1.evidence_types_seen:
        return "report_fixture"
    if mode == HistoricalReplayMode.HYBRID:
        return "hybrid_official"
    return "case_fixture"


def _missing_evidence_warnings(
    original: HistoricalCase,
    view: HistoricalCase,
    mode: HistoricalReplayMode,
) -> tuple[str, ...]:
    warnings: list[str] = []
    if mode == HistoricalReplayMode.OFFICIAL_ONLY:
        if original.research_reports:
            warnings.append("evidence_missing:research_report_excluded_in_official_only")
        if original.news_items:
            warnings.append("evidence_missing:news_excluded_in_official_only")
        if original.consensus or original.consensus_revisions:
            warnings.append("evidence_missing:consensus_excluded_in_official_only")
    elif original.research_reports and not view.research_reports:
        warnings.append("search_snapshot_unavailable")
    if not view.price_bars:
        warnings.append("evidence_missing:price_path")
    return tuple(dict.fromkeys(warnings))


def _evidence_counts(case: HistoricalCase) -> tuple[str, ...]:
    types: list[str] = []
    if case.research_reports:
        types.append("research_report")
    if case.disclosures:
        types.append("disclosure")
    if case.news_items:
        types.append("news")
    if case.financial_actuals:
        types.append("financial_actual")
    if case.consensus:
        types.append("consensus")
    if case.consensus_revisions:
        types.append("consensus_revision")
    if case.price_bars:
        types.append("price")
    return tuple(types)


def _known_case_validations(
    config: HistoricalReplayConfig,
    cases: Sequence[HistoricalCase],
    snapshots: Sequence[HistoricalReplaySnapshot],
) -> tuple[KnownCaseValidation, ...]:
    candidates_by_case: dict[str, HistoricalReplayCandidate] = {}
    dropped_by_case: dict[str, HistoricalReplayDroppedCandidate] = {}
    for snapshot in snapshots:
        for candidate in snapshot.candidates:
            previous = candidates_by_case.get(candidate.case_id)
            if previous is None or _candidate_rank_tuple(candidate) > _candidate_rank_tuple(previous):
                candidates_by_case[candidate.case_id] = candidate
        for item in snapshot.dropped_candidates:
            dropped_by_case.setdefault(item.case_id, item)
    rows: list[KnownCaseValidation] = []
    for case in cases:
        expected_group = _expected_group(case)
        candidate = candidates_by_case.get(case.case_id)
        dropped = dropped_by_case.get(case.case_id)
        if candidate is None:
            if config.mode == HistoricalReplayMode.OFFICIAL_ONLY and (case.research_reports or case.news_items):
                status = "skipped_missing_historical_report_news_data"
            else:
                status = "missed"
            rows.append(
                KnownCaseValidation(
                    case_id=case.case_id,
                    symbol=case.symbol,
                    company_name=case.company_name,
                    expected_group=expected_group,
                    status=status,
                    final_stage=dropped.stage if dropped else None,
                    layer1_result=None,
                    failure_reason=dropped.dropped_reason if dropped else "not_in_replay_window",
                )
            )
            continue

        status = _known_case_status(case, candidate, config.mode)
        failure_reason = None
        if status in {"missed", "skipped_missing_historical_report_news_data"}:
            failure_reason = ",".join(candidate.missing_evidence_warnings) or "below_expected_stage"
        rows.append(
            KnownCaseValidation(
                case_id=case.case_id,
                symbol=case.symbol,
                company_name=case.company_name,
                expected_group=expected_group,
                status=status,
                final_stage=candidate.stage,
                layer1_result=candidate.layer1_result,
                failure_reason=failure_reason,
            )
        )
    return tuple(rows)


def _candidate_rank_tuple(candidate: HistoricalReplayCandidate) -> tuple[int, float, float, int]:
    layer_rank = {
        LAYER_NONE: 0,
        LAYER_EVENT_SEARCH: 2,
        LAYER_DEEP_RESEARCH: 3,
        LAYER_STAGE2_OR_HIGHER: 4,
    }.get(candidate.layer1_result, 0)
    return (_stage_rank(candidate.stage), candidate.layer1_score, candidate.total_score, -candidate.as_of_date.toordinal())


def _known_case_status(case: HistoricalCase, candidate: HistoricalReplayCandidate, mode: HistoricalReplayMode) -> str:
    if mode == HistoricalReplayMode.OFFICIAL_ONLY and candidate.missing_evidence_warnings:
        return "skipped_missing_historical_report_news_data"
    if _expected_group(case) == "warning_or_boom_bust":
        if candidate.stage == Stage.STAGE_3_GREEN:
            return "missed"
        if candidate.stage in {Stage.STAGE_3_YELLOW, Stage.STAGE_3_RED}:
            return "detected_but_yellow_red"
        return "detected"
    if candidate.stage in {Stage.STAGE_3_YELLOW, Stage.STAGE_3_RED}:
        return "detected_but_yellow_red"
    if candidate.stage in {Stage.STAGE_2, Stage.STAGE_3_GREEN}:
        return "detected"
    if candidate.layer1_result in {LAYER_EVENT_SEARCH, LAYER_DEEP_RESEARCH, LAYER_STAGE2_OR_HIGHER}:
        return "detected_late" if candidate.as_of_date > case.stage3_date else "detected"
    return "missed"


def _expected_group(case: HistoricalCase) -> str:
    lowered = f"{case.case_id} {case.company_name}".lower()
    if any(token in lowered for token in ("zoom", "seegene", "씨젠", "smci", "ecopro", "hmm", "daehan", "대한전선")):
        return "warning_or_boom_bust"
    return "structural_success"


def _write_outputs(result: HistoricalUniverseReplayResult) -> HistoricalUniverseReplayResult:
    output_root = Path(result.config.output_directory)
    output_root.mkdir(parents=True, exist_ok=True)
    stem = result.config.end_date.isoformat()
    summary_json = output_root / f"{stem}_summary.json"
    summary_md = output_root / f"{stem}_summary.md"
    lifecycle_json = output_root / "stage_lifecycle_results.json"
    lifecycle_csv = output_root / "stage_lifecycle_results.csv"
    top_stage3 = output_root / "top_stage3_candidates.md"
    false_positive = output_root / "false_positive_cases.md"
    missed = output_root / "missed_winner_cases.md"

    summary_json.write_text(json.dumps(_jsonable(result), ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    summary_md.write_text(render_historical_replay_summary(result), encoding="utf-8")
    write_stage_lifecycle_outputs(result.lifecycle_results, json_path=lifecycle_json, csv_path=lifecycle_csv)
    top_stage3.write_text(render_top_stage3_candidates(result), encoding="utf-8")
    false_positive.write_text(render_false_positive_cases(result), encoding="utf-8")
    missed.write_text(render_missed_winner_cases(result), encoding="utf-8")

    return HistoricalUniverseReplayResult(
        config=result.config,
        snapshots=result.snapshots,
        lifecycle_results=result.lifecycle_results,
        known_case_validations=result.known_case_validations,
        summary_json_path=summary_json,
        summary_md_path=summary_md,
        lifecycle_json_path=lifecycle_json,
        lifecycle_csv_path=lifecycle_csv,
        top_stage3_path=top_stage3,
        false_positive_path=false_positive,
        missed_winner_path=missed,
    )


def _replay_dates(start: date, end: date, frequency: ReplayFrequency) -> tuple[date, ...]:
    values: list[date] = []
    current = start
    while current <= end:
        values.append(current)
        if frequency == ReplayFrequency.DAILY:
            current += timedelta(days=1)
        elif frequency == ReplayFrequency.WEEKLY:
            current += timedelta(days=7)
        else:
            current = _next_month(current)
    if values[-1] != end:
        values.append(end)
    return tuple(dict.fromkeys(values))


def _next_month(value: date) -> date:
    year = value.year + (1 if value.month == 12 else 0)
    month = 1 if value.month == 12 else value.month + 1
    days_in_month = [31, 29 if _is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = min(value.day, days_in_month[month - 1])
    return date(year, month, day)


def _is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def _bar_on_date(price_bars: Sequence[PriceBar], target: date) -> PriceBar | None:
    for item in price_bars:
        if item.date == target:
            return item
    return None


def _stage_rank(stage: Stage) -> int:
    order = {
        Stage.STAGE_0: 0,
        Stage.STAGE_1: 1,
        Stage.STAGE_2: 2,
        Stage.STAGE_3_RED: 3,
        Stage.STAGE_3_YELLOW: 3,
        Stage.STAGE_3_GREEN: 3,
        Stage.STAGE_4A: 4,
        Stage.STAGE_4B: 4,
        Stage.STAGE_4C: 4,
        Stage.STAGE_5: 5,
    }
    return order[stage]


def _avg(values: Sequence[int | None]) -> str:
    clean = [item for item in values if item is not None]
    if not clean:
        return "n/a"
    return f"{sum(clean) / len(clean):.1f}"


def _jsonable(value: Any) -> Any:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Path):
        return str(value)
    if is_dataclass(value):
        return {field.name: _jsonable(getattr(value, field.name)) for field in fields(value)}
    if isinstance(value, Mapping):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set, frozenset)):
        return [_jsonable(item) for item in value]
    return value


__all__ = [
    "DEFAULT_HISTORICAL_REPLAY_OUTPUT_DIR",
    "HistoricalReplayCandidate",
    "HistoricalReplayConfig",
    "HistoricalReplayDroppedCandidate",
    "HistoricalReplayMode",
    "HistoricalReplaySnapshot",
    "HistoricalReplayStageRecord",
    "HistoricalUniverseReplay",
    "HistoricalUniverseReplayResult",
    "KnownCaseValidation",
    "ReplayFrequency",
    "render_false_positive_cases",
    "render_historical_replay_summary",
    "render_missed_winner_cases",
    "render_top_stage3_candidates",
]
