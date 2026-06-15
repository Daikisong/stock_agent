"""Blind discovery replay using E2R_STANDARD outputs before benchmark scoring."""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass, fields, is_dataclass
from datetime import date, datetime
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.backtest.benchmark_labels import BenchmarkGroup, BenchmarkLabel, labels_for_market, load_benchmark_labels
from e2r.backtest.e2r_standard_replay import E2RStandardReplay, E2RStandardReplayConfig, E2RStandardReplayResult
from e2r.backtest.historical_universe_replay import ReplayFrequency
from e2r.models import Market, Stage
from e2r.pipeline.e2r_standard_flow import E2R_STANDARD
from e2r.score_validity import normalized_score_state_mapping_if_present, normalized_score_state_payload


DEFAULT_BLIND_DISCOVERY_OUTPUT_DIR = Path("output/backtests/blind_discovery")


@dataclass(frozen=True)
class BlindDiscoveryConfig:
    start_date: date
    end_date: date
    frequency: ReplayFrequency | str = ReplayFrequency.MONTHLY
    market: Market | str = Market.KR
    flow: str = E2R_STANDARD
    output_directory: str | Path = DEFAULT_BLIND_DISCOVERY_OUTPUT_DIR
    universe_limit: int | None = None
    max_candidates_per_date: int | None = None
    case_root: str | Path = "data/historical_cases"
    benchmark_label_path: str | Path = "data/benchmark_labels/e2r_known_winners.json"
    search_snapshot_root: str | Path = "data/search_snapshots"
    report_snapshot_root: str | Path = "data/report_snapshots"
    use_search_snapshots: bool = True
    use_report_snapshots: bool = True
    allow_fixture_source_proxy: bool = False
    llm_enabled: bool = False

    def __post_init__(self) -> None:
        if self.flow != E2R_STANDARD:
            raise ValueError("blind discovery replay must use E2R_STANDARD")
        if not isinstance(self.frequency, ReplayFrequency):
            object.__setattr__(self, "frequency", ReplayFrequency(str(self.frequency)))
        if not isinstance(self.market, Market):
            object.__setattr__(self, "market", Market(str(self.market)))


@dataclass(frozen=True)
class DiscoveredCandidate:
    symbol: str
    company_name: str
    as_of_date: date
    layer: str
    stage: Stage
    rank: int
    score: float | None
    evidence_types_seen: tuple[str, ...]
    reason_codes: tuple[str, ...]
    score_valid: bool | None = None
    score_blocked_reason: str | None = None
    score_fingerprint: str | None = None
    research_input_fingerprint: str | None = None
    score_variability_drivers: tuple[str, ...] = ()


@dataclass(frozen=True)
class BenchmarkRecallRow:
    label_id: str
    symbol: str
    company_name: str
    expected_group: str
    appeared_in_candidates: bool
    first_detected_date: date | None
    first_layer: str | None
    first_stage: Stage | None
    detection_lag_days: int | None
    top_n_rank_at_detection: int | None
    evidence_types_seen: tuple[str, ...]
    miss_reason: str | None = None


@dataclass(frozen=True)
class BlindDiscoveryResult:
    config: BlindDiscoveryConfig
    replay_result: E2RStandardReplayResult
    discovered_candidates: tuple[DiscoveredCandidate, ...]
    benchmark_recall: tuple[BenchmarkRecallRow, ...]
    output_root: Path | None = None
    report_paths: Mapping[str, Path] = None


class BlindDiscoveryReplay:
    """Run discovery first, then apply hidden labels for evaluation."""

    def run(self, config: BlindDiscoveryConfig, *, write_outputs: bool = True) -> BlindDiscoveryResult:
        replay_result = _generate_standard_replay_outputs(config)
        discovered = _discovered_candidates(replay_result)
        # Benchmark labels are loaded only after discovery output exists.
        labels = labels_for_market(load_benchmark_labels(config.benchmark_label_path), config.market)
        recall = _evaluate_labels(labels, discovered, replay_result)
        result = BlindDiscoveryResult(
            config=config,
            replay_result=replay_result,
            discovered_candidates=discovered,
            benchmark_recall=recall,
        )
        if not write_outputs:
            return result
        return _write_outputs(result)


def _generate_standard_replay_outputs(config: BlindDiscoveryConfig) -> E2RStandardReplayResult:
    """Generate candidates with E2R_STANDARD before benchmark labels are loaded."""

    replay_config = E2RStandardReplayConfig(
        start_date=config.start_date,
        end_date=config.end_date,
        replay_frequency=config.frequency,
        market=config.market,
        output_directory=Path(config.output_directory) / "_standard_replay_internal",
        universe_limit=config.universe_limit,
        max_candidates_per_date=config.max_candidates_per_date,
        case_root=config.case_root,
        search_snapshot_root=config.search_snapshot_root,
        report_snapshot_root=config.report_snapshot_root,
        use_search_snapshots=config.use_search_snapshots,
        use_report_snapshots=config.use_report_snapshots,
        allow_fixture_source_proxy=config.allow_fixture_source_proxy,
        llm_enabled=config.llm_enabled,
    )
    return E2RStandardReplay().run(replay_config)


def _discovered_candidates(result: E2RStandardReplayResult) -> tuple[DiscoveredCandidate, ...]:
    rows: list[DiscoveredCandidate] = []
    for snapshot in result.snapshots:
        ranked = sorted(snapshot.candidates, key=lambda item: (-_score_sort_value(item.score), item.symbol))
        for rank, candidate in enumerate(ranked, start=1):
            rows.append(_candidate_row(candidate, rank))
    return tuple(rows)


def _score_sort_value(score: float | None) -> float:
    return float(score) if score is not None else -1.0


def _candidate_row(candidate, rank: int) -> DiscoveredCandidate:
    return DiscoveredCandidate(
        symbol=candidate.symbol,
        company_name=candidate.company_name,
        as_of_date=candidate.as_of_date,
        layer=candidate.layer,
        stage=candidate.stage,
        rank=rank,
        score=candidate.score,
        evidence_types_seen=tuple(candidate.evidence_types_seen),
        reason_codes=tuple(candidate.reason_codes),
        score_valid=getattr(candidate, "score_valid", None),
        score_blocked_reason=getattr(candidate, "score_blocked_reason", None),
        score_fingerprint=getattr(candidate, "score_fingerprint", None),
        research_input_fingerprint=getattr(candidate, "research_input_fingerprint", None),
        score_variability_drivers=tuple(getattr(candidate, "score_variability_drivers", ())),
    )


def _evaluate_labels(
    labels: Sequence[BenchmarkLabel],
    discovered: Sequence[DiscoveredCandidate],
    replay_result: E2RStandardReplayResult,
) -> tuple[BenchmarkRecallRow, ...]:
    rows: list[BenchmarkRecallRow] = []
    for label in labels:
        matches = [
            item
            for item in discovered
            if item.symbol == label.symbol
            and label.expected_window_start <= item.as_of_date <= label.expected_window_end
        ]
        if matches:
            first = sorted(matches, key=lambda item: (item.as_of_date, item.rank))[0]
            rows.append(
                BenchmarkRecallRow(
                    label_id=label.label_id,
                    symbol=label.symbol,
                    company_name=label.company_name,
                    expected_group=label.expected_group.value,
                    appeared_in_candidates=True,
                    first_detected_date=first.as_of_date,
                    first_layer=first.layer,
                    first_stage=first.stage,
                    detection_lag_days=(first.as_of_date - label.expected_window_start).days,
                    top_n_rank_at_detection=first.rank,
                    evidence_types_seen=first.evidence_types_seen,
                )
            )
            continue
        rows.append(
            BenchmarkRecallRow(
                label_id=label.label_id,
                symbol=label.symbol,
                company_name=label.company_name,
                expected_group=label.expected_group.value,
                appeared_in_candidates=False,
                first_detected_date=None,
                first_layer=None,
                first_stage=None,
                detection_lag_days=None,
                top_n_rank_at_detection=None,
                evidence_types_seen=(),
                miss_reason=_miss_reason(label, discovered, replay_result),
            )
        )
    return tuple(rows)


def _miss_reason(label: BenchmarkLabel, discovered: Sequence[DiscoveredCandidate], replay_result: E2RStandardReplayResult) -> str:
    if not any(item.symbol == label.symbol for item in discovered):
        limitations = set(replay_result.limitations)
        if "search_snapshot_unavailable" in limitations:
            return "search_snapshot_unavailable"
        if "report_snapshot_unavailable" in limitations:
            return "report_snapshot_unavailable"
        if "official_data_unavailable" in limitations or "insufficient_historical_source_coverage" in limitations:
            return "source_missing_or_not_in_universe"
        if label.expected_group in {BenchmarkGroup.STRUCTURAL, BenchmarkGroup.CYCLICAL}:
            return "source_missing_or_not_in_universe"
        return "not_in_universe"
    if label.expected_group in {BenchmarkGroup.STRUCTURAL, BenchmarkGroup.CYCLICAL}:
        return "no_report_snapshot"
    return "unknown"


def render_blind_discovery_summary(result: BlindDiscoveryResult) -> str:
    appeared = sum(1 for item in result.benchmark_recall if item.appeared_in_candidates)
    unsafe_green = [
        item
        for item in result.benchmark_recall
        if item.expected_group in {"one_off", "boom_bust", "valuation_overheat"}
        and item.first_stage == Stage.STAGE_3_GREEN
    ]
    lines = [
        "# Blind Discovery Replay",
        "",
        f"- flow: {result.config.flow}",
        f"- true_standard_flow_used: {'yes' if result.replay_result.true_standard_flow_used else 'no'}",
        f"- fixture_proxy_used: {'yes' if result.replay_result.fixture_proxy_used else 'no'}",
        "- benchmark_labels_used_before_candidate_generation: no",
        f"- llm_enabled: {'true' if result.config.llm_enabled else 'false'}",
        f"- period: {result.config.start_date.isoformat()} to {result.config.end_date.isoformat()}",
        f"- frequency: {result.config.frequency.value}",
        f"- market: {result.config.market.value}",
        f"- discovered_candidates: {len(result.discovered_candidates)}",
        f"- benchmark_labels_appeared: {appeared}/{len(result.benchmark_recall)}",
        f"- unsafe_warning_green_count: {len(unsafe_green)}",
        f"- Stage 3-Green count: {sum(1 for item in result.discovered_candidates if item.stage == Stage.STAGE_3_GREEN)}",
        f"- Stage 3-Yellow count: {sum(1 for item in result.discovered_candidates if item.stage == Stage.STAGE_3_YELLOW)}",
        f"- Stage 3-Red count: {sum(1 for item in result.discovered_candidates if item.stage == Stage.STAGE_3_RED)}",
        f"- 4B count: {sum(1 for item in result.discovered_candidates if item.stage == Stage.STAGE_4B)}",
        f"- 4C count: {sum(1 for item in result.discovered_candidates if item.stage == Stage.STAGE_4C)}",
        "",
        "Benchmark labels were applied only after candidate generation.",
        "Search/report snapshots are required for a true point-in-time report-driven replay.",
    ]
    if result.replay_result.fixture_proxy_used:
        lines.append("fixture proxy mode; not proof of live discovery")
    if result.replay_result.limitations:
        lines.extend(["", "Limitations:"])
        lines.extend(f"- {item}" for item in result.replay_result.limitations)
    return "\n".join(lines).rstrip() + "\n"


def render_benchmark_recall_report(result: BlindDiscoveryResult) -> str:
    lines = [
        "# Benchmark Recall Report",
        "",
        "| label | company | group | appeared | first date | layer | stage | lag days | rank | evidence | miss reason |",
        "| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | --- | --- |",
    ]
    for item in result.benchmark_recall:
        lines.append(
            f"| {item.label_id} | {item.company_name} | {item.expected_group} | {'yes' if item.appeared_in_candidates else 'no'} | "
            f"{item.first_detected_date.isoformat() if item.first_detected_date else 'n/a'} | {item.first_layer or 'n/a'} | "
            f"{item.first_stage.value if item.first_stage else 'n/a'} | {item.detection_lag_days if item.detection_lag_days is not None else 'n/a'} | "
            f"{item.top_n_rank_at_detection if item.top_n_rank_at_detection is not None else 'n/a'} | "
            f"{', '.join(item.evidence_types_seen) or 'none'} | {item.miss_reason or ''} |"
        )
    return "\n".join(lines).rstrip() + "\n"


def render_missed_benchmark_labels(result: BlindDiscoveryResult) -> str:
    rows = [item for item in result.benchmark_recall if not item.appeared_in_candidates]
    lines = ["# Missed Benchmark Labels", ""]
    if not rows:
        lines.append("No benchmark labels were missed in the evaluated market/window.")
        return "\n".join(lines).rstrip() + "\n"
    lines.extend(["| label | company | reason | required data |", "| --- | --- | --- | --- |"])
    for item in rows:
        lines.append(f"| {item.label_id} | {item.company_name} | {item.miss_reason} | {_required_data(item.miss_reason)} |")
    return "\n".join(lines).rstrip() + "\n"


def render_false_positive_report(result: BlindDiscoveryResult) -> str:
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
            f"{item.first_stage.value if item.first_stage else 'n/a'} | {'unsafe Green' if unsafe else 'contained or missing evidence'} |"
        )
    return "\n".join(lines).rstrip() + "\n"


def render_source_coverage_report(result: BlindDiscoveryResult) -> str:
    summary = result.replay_result.source_coverage_summary
    lines = [
        "# Source Coverage Report",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in sorted(summary.items()):
        lines.append(f"| {key} | {json.dumps(_jsonable(value), ensure_ascii=False)} |")
    lines.extend(
        [
            "",
            "Missing search/report snapshots mean the replay can still run, but it cannot prove that old web reports were discoverable at the replay date.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def render_benchmark_leakage_audit(result: BlindDiscoveryResult) -> str:
    return (
        "# Benchmark Leakage Audit\n\n"
        f"- true_standard_flow_used: {'yes' if result.replay_result.true_standard_flow_used else 'no'}\n"
        f"- benchmark_labels_used_before_candidate_generation: {'yes' if result.replay_result.benchmark_labels_used_before_candidate_generation else 'no'}\n"
        "- benchmark_labels_loaded_after_discovery: yes\n"
        "- benchmark_labels_as_input_evidence: no\n"
    )


def render_evidence_coverage_report(result: BlindDiscoveryResult) -> str:
    counts: dict[str, int] = {}
    for item in result.discovered_candidates:
        for evidence_type in item.evidence_types_seen:
            counts[evidence_type] = counts.get(evidence_type, 0) + 1
    lines = ["# Evidence Coverage Report", "", "| evidence type | count |", "| --- | ---: |"]
    for key, value in sorted(counts.items()):
        lines.append(f"| {key} | {value} |")
    if not counts:
        lines.append("| none | 0 |")
    lines.extend(
        [
            "",
            f"- search_snapshot_available_dates: {result.replay_result.source_coverage_summary.get('search_snapshot_available', 0)}",
            f"- report_snapshot_available_dates: {result.replay_result.source_coverage_summary.get('report_snapshot_available', 0)}",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def render_stage_lifecycle_report(result: BlindDiscoveryResult) -> str:
    rows = []
    for snapshot in result.replay_result.snapshots:
        rows.extend(snapshot.candidates)
    lines = [
        "# Stage Lifecycle Report",
        "",
        "| symbol | company | date | stage | lifecycle status | source path |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in rows:
        lines.append(
            f"| {item.symbol} | {item.company_name} | {item.as_of_date.isoformat()} | {item.stage.value} | "
            f"{item.lifecycle_status} | {item.candidate_source_path} |"
        )
    if not rows:
        lines.append("| n/a | n/a | n/a | n/a | unknown_insufficient_evidence | n/a |")
    return "\n".join(lines).rstrip() + "\n"


def render_limitations(result: BlindDiscoveryResult) -> str:
    lines = [
        "# Blind Discovery Limitations",
        "",
        "- Historical search/report snapshots are point-in-time evidence; benchmark labels are not evidence.",
        "- If snapshots are unavailable, the replay marks misses instead of pretending success.",
        "- Benchmark labels are evaluation-only and are not used by E2R_STANDARD candidate generation.",
        "- Stage 3-Green thresholds are not loosened for recall.",
    ]
    if result.replay_result.fixture_proxy_used:
        lines.append("- fixture proxy mode was enabled explicitly; this is regression only, not blind discovery proof.")
    lines.extend(f"- {item}" for item in result.replay_result.limitations)
    return "\n".join(lines).rstrip() + "\n"


def _write_outputs(result: BlindDiscoveryResult) -> BlindDiscoveryResult:
    output_root = Path(result.config.output_directory) / f"{result.config.start_date.isoformat()}_to_{result.config.end_date.isoformat()}"
    output_root.mkdir(parents=True, exist_ok=True)
    paths = {
        "summary_md": output_root / "blind_discovery_summary.md",
        "summary_json": output_root / "blind_discovery_summary.json",
        "candidates_csv": output_root / "discovered_candidates.csv",
        "candidates_json": output_root / "discovered_candidates.json",
        "recall_md": output_root / "benchmark_recall_report.md",
        "recall_json": output_root / "benchmark_recall_report.json",
        "missed_md": output_root / "missed_benchmark_labels.md",
        "false_positive_md": output_root / "false_positive_report.md",
        "lifecycle_md": output_root / "stage_lifecycle_report.md",
        "evidence_md": output_root / "evidence_coverage_report.md",
        "limitations_md": output_root / "limitations.md",
        "source_coverage_md": output_root / "source_coverage_report.md",
        "leakage_audit_md": output_root / "benchmark_leakage_audit.md",
        "llm_review_json": output_root / "llm_review.json",
        "llm_review_md": output_root / "llm_review.md",
    }
    paths["summary_md"].write_text(render_blind_discovery_summary(result), encoding="utf-8")
    paths["summary_json"].write_text(json.dumps(_jsonable(result), ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    paths["recall_md"].write_text(render_benchmark_recall_report(result), encoding="utf-8")
    paths["recall_json"].write_text(json.dumps(_jsonable(result.benchmark_recall), ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    paths["missed_md"].write_text(render_missed_benchmark_labels(result), encoding="utf-8")
    paths["false_positive_md"].write_text(render_false_positive_report(result), encoding="utf-8")
    paths["limitations_md"].write_text(render_limitations(result), encoding="utf-8")
    paths["lifecycle_md"].write_text(render_stage_lifecycle_report(result), encoding="utf-8")
    paths["evidence_md"].write_text(render_evidence_coverage_report(result), encoding="utf-8")
    paths["source_coverage_md"].write_text(render_source_coverage_report(result), encoding="utf-8")
    paths["leakage_audit_md"].write_text(render_benchmark_leakage_audit(result), encoding="utf-8")
    paths["llm_review_json"].write_text(
        json.dumps({"llm_enabled": result.config.llm_enabled, "outputs": []}, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    paths["llm_review_md"].write_text(
        "# LLM Review\n\nLLM is disabled by default for blind replay unless explicitly configured.\n",
        encoding="utf-8",
    )
    _write_candidates(paths["candidates_csv"], paths["candidates_json"], result.discovered_candidates)
    return BlindDiscoveryResult(
        config=result.config,
        replay_result=result.replay_result,
        discovered_candidates=result.discovered_candidates,
        benchmark_recall=result.benchmark_recall,
        output_root=output_root,
        report_paths=paths,
    )


def _write_candidates(csv_path: Path, json_path: Path, rows: Sequence[DiscoveredCandidate]) -> None:
    json_path.write_text(json.dumps(_jsonable(rows), ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=(
                "symbol",
                "company_name",
                "as_of_date",
                "layer",
                "stage",
                "rank",
                "score",
                "visible_score",
                "score_valid",
                "score_blocked_reason",
                "score_fingerprint",
                "research_input_fingerprint",
                "score_variability_drivers",
            ),
        )
        writer.writeheader()
        for item in rows:
            score_payload = normalized_score_state_payload(
                {
                    "score": item.score,
                    "score_valid": item.score_valid,
                    "score_blocked_reason": item.score_blocked_reason,
                }
            )
            score = score_payload.get("score")
            visible_score = score_payload.get("visible_score")
            writer.writerow(
                {
                    "symbol": item.symbol,
                    "company_name": item.company_name,
                    "as_of_date": item.as_of_date.isoformat(),
                    "layer": item.layer,
                    "stage": item.stage.value,
                    "rank": item.rank,
                    "score": score if score is not None else "",
                    "visible_score": visible_score if visible_score is not None else "",
                    "score_valid": score_payload.get("score_valid") if score_payload.get("score_valid") is not None else "",
                    "score_blocked_reason": score_payload.get("score_blocked_reason") or "",
                    "score_fingerprint": item.score_fingerprint or "",
                    "research_input_fingerprint": item.research_input_fingerprint or "",
                    "score_variability_drivers": "|".join(item.score_variability_drivers),
                }
            )


def _required_data(reason: str | None) -> str:
    if reason == "no_report_snapshot":
        return "archived search/report snapshots"
    if reason == "search_snapshot_unavailable":
        return "historical search snapshots"
    if reason == "report_snapshot_unavailable":
        return "historical report text snapshots"
    if reason == "source_missing_or_not_in_universe":
        return "historical universe, official evidence, and search snapshots"
    if reason == "not_in_universe":
        return "market fixture or universe membership"
    return "manual review"


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
        return payload
    if isinstance(value, Mapping):
        return normalized_score_state_mapping_if_present({str(key): _jsonable(item) for key, item in value.items()})
    if isinstance(value, (list, tuple, set, frozenset)):
        return [_jsonable(item) for item in value]
    return value


__all__ = [
    "BlindDiscoveryConfig",
    "BlindDiscoveryReplay",
    "BlindDiscoveryResult",
    "BenchmarkRecallRow",
    "DiscoveredCandidate",
    "render_benchmark_recall_report",
    "render_blind_discovery_summary",
]
