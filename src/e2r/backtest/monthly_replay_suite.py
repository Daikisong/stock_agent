"""Monthly replay suite and operator-grade reports for Checkpoint 22."""

from __future__ import annotations

import json
from dataclasses import dataclass, fields, is_dataclass
from datetime import date, datetime
from enum import Enum
from pathlib import Path
from statistics import median
from typing import Any, Iterable, Mapping, Sequence

from e2r.backtest.historical_universe_replay import (
    HistoricalReplayCandidate,
    HistoricalReplayConfig,
    HistoricalReplayMode,
    HistoricalUniverseReplay,
    HistoricalUniverseReplayResult,
    ReplayFrequency,
)
from e2r.backtest.stage_lifecycle_backtest import (
    STAGE4B_UNKNOWN_INSUFFICIENT_EVIDENCE,
    StageLifecycleResult,
    write_stage_lifecycle_outputs,
)
from e2r.models import Market, Stage
from e2r.score_validity import (
    normalized_score_state_mapping_if_present,
    normalized_score_state_payload,
    serialized_score_block_reason,
    serialized_score_valid,
)


DEFAULT_MONTHLY_SUITE_OUTPUT_DIR = Path("output/backtests/monthly_replay_suite")


@dataclass(frozen=True)
class MonthlyReplaySuiteConfig:
    """Config for running all monthly historical replay modes as one suite."""

    start_date: date
    end_date: date
    output_directory: str | Path = DEFAULT_MONTHLY_SUITE_OUTPUT_DIR
    modes: tuple[HistoricalReplayMode, ...] = (
        HistoricalReplayMode.CASE_FIXTURE,
        HistoricalReplayMode.OFFICIAL_ONLY,
        HistoricalReplayMode.HYBRID,
    )
    frequency: ReplayFrequency | str = ReplayFrequency.MONTHLY
    market: Market | str = Market.KR
    universe_limit: int | None = None
    max_candidates_per_date: int | None = None
    strict: bool = False
    write_json: bool = True
    write_md: bool = True
    write_csv: bool = True
    case_root: str | Path = "data/historical_cases"

    def __post_init__(self) -> None:
        if self.end_date < self.start_date:
            raise ValueError("end_date cannot be before start_date")
        normalized_modes = tuple(mode if isinstance(mode, HistoricalReplayMode) else HistoricalReplayMode(str(mode)) for mode in self.modes)
        if not normalized_modes:
            raise ValueError("at least one replay mode is required")
        object.__setattr__(self, "modes", normalized_modes)
        if not isinstance(self.frequency, ReplayFrequency):
            object.__setattr__(self, "frequency", ReplayFrequency(str(self.frequency)))
        if not isinstance(self.market, Market):
            object.__setattr__(self, "market", Market(str(self.market)))


@dataclass(frozen=True)
class MonthlyReplaySuiteResult:
    """Complete suite output and report paths."""

    config: MonthlyReplaySuiteConfig
    output_root: Path
    mode_results: Mapping[str, HistoricalUniverseReplayResult]
    suite_summary: Mapping[str, Any]
    mode_comparison: Mapping[str, Any]
    lifecycle_aggregates: Mapping[str, Any]
    known_case_validation: tuple[Mapping[str, Any], ...]
    missed_winners: tuple[Mapping[str, Any], ...]
    false_positives: tuple[Mapping[str, Any], ...]
    evidence_coverage: Mapping[str, Any]
    readiness_assessment: Mapping[str, Any]
    limitations: tuple[str, ...]
    report_paths: Mapping[str, Path]


class MonthlyReplaySuiteRunner:
    """Run monthly replay modes and write operator-grade reports."""

    def run(self, config: MonthlyReplaySuiteConfig) -> MonthlyReplaySuiteResult:
        output_root = _suite_output_root(config)
        output_root.mkdir(parents=True, exist_ok=True)
        mode_results: dict[str, HistoricalUniverseReplayResult] = {}
        for mode in config.modes:
            mode_dir = output_root / mode.value
            replay_config = HistoricalReplayConfig(
                start_date=config.start_date,
                end_date=config.end_date,
                replay_frequency=config.frequency,
                mode=mode,
                market=config.market,
                universe_limit=config.universe_limit,
                max_candidates_per_date=config.max_candidates_per_date,
                output_directory=mode_dir,
                case_root=config.case_root,
            )
            mode_results[mode.value] = HistoricalUniverseReplay().run(replay_config, write_outputs=True)

        suite_summary = _suite_summary(config, mode_results)
        mode_comparison = _mode_comparison(mode_results)
        lifecycle_aggregates = _lifecycle_aggregates(mode_results)
        known_cases = _known_case_validation(mode_results)
        missed = _missed_winner_rows(known_cases)
        false_positives = _false_positive_rows(mode_results, known_cases)
        evidence_coverage = _evidence_coverage(mode_results)
        readiness = _readiness_assessment(mode_comparison, lifecycle_aggregates, missed, false_positives, evidence_coverage)
        limitations = _limitations(evidence_coverage)
        report_paths = _write_suite_reports(
            config=config,
            output_root=output_root,
            mode_results=mode_results,
            suite_summary=suite_summary,
            mode_comparison=mode_comparison,
            lifecycle_aggregates=lifecycle_aggregates,
            known_cases=known_cases,
            missed=missed,
            false_positives=false_positives,
            evidence_coverage=evidence_coverage,
            readiness=readiness,
            limitations=limitations,
        )
        return MonthlyReplaySuiteResult(
            config=config,
            output_root=output_root,
            mode_results=mode_results,
            suite_summary=suite_summary,
            mode_comparison=mode_comparison,
            lifecycle_aggregates=lifecycle_aggregates,
            known_case_validation=known_cases,
            missed_winners=missed,
            false_positives=false_positives,
            evidence_coverage=evidence_coverage,
            readiness_assessment=readiness,
            limitations=limitations,
            report_paths=report_paths,
        )


def render_suite_summary(result: MonthlyReplaySuiteResult) -> str:
    summary = result.suite_summary
    lines = [
        "# Monthly Historical Replay Suite",
        "",
        f"- replay_period: {summary['config']['start_date']} to {summary['config']['end_date']}",
        f"- modes_run: {', '.join(summary['modes'])}",
        f"- replay_dates: {summary['aggregate_counts']['replay_dates']}",
        f"- total_scanned_instruments_cases: {summary['aggregate_counts']['scanned_instruments']}",
        f"- total_candidates: {summary['aggregate_counts']['candidates']}",
        f"- event_search_or_higher: {summary['aggregate_counts']['event_search_or_higher']}",
        f"- deep_research: {summary['aggregate_counts']['deep_research']}",
        f"- Stage 2 count: {summary['stage_distribution'].get(Stage.STAGE_2.value, 0)}",
        f"- Stage 3-Green count: {summary['stage_distribution'].get(Stage.STAGE_3_GREEN.value, 0)}",
        f"- Stage 3-Yellow count: {summary['stage_distribution'].get(Stage.STAGE_3_YELLOW.value, 0)}",
        f"- Stage 3-Red count: {summary['stage_distribution'].get(Stage.STAGE_3_RED.value, 0)}",
        f"- Stage 4B count: {summary['aggregate_counts']['stage4b']}",
        f"- Stage 4C count: {summary['aggregate_counts']['stage4c']}",
        f"- still_active count: {summary['aggregate_counts']['still_active']}",
        f"- missed known winners: {summary['aggregate_counts']['missed_known_winners']}",
        f"- false_positive_or_boom_bust cases: {summary['aggregate_counts']['false_positive_or_boom_bust']}",
        "",
        "## Evidence Coverage",
        "",
    ]
    for key, value in result.evidence_coverage["aggregate_counts_by_source_type"].items():
        lines.append(f"- {key}: {value}")
    lines.extend(
        [
            f"- missing_report_news_snapshot_count: {result.evidence_coverage['missing_report_news_snapshot_count']}",
            f"- stage4b_unknown_count: {result.evidence_coverage['stage4b_unknown_count']}",
            "",
            "## Major Limitations",
            "",
        ]
    )
    for item in result.limitations:
        lines.append(f"- {item}")
    lines.extend(["", "## Readiness", "", result.readiness_assessment["summary"]])
    return "\n".join(lines).rstrip() + "\n"


def render_mode_comparison(result: MonthlyReplaySuiteResult) -> str:
    lines = [
        "# Mode Comparison",
        "",
        "| mode | candidates | Green | Yellow | Red | missed winners | false positives | 4B unknown | evidence_missing | report/news unavailable | official evidence |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for mode, row in result.mode_comparison.items():
        lines.append(
            f"| {mode} | {row['candidates']} | {row['stage3_green']} | {row['stage3_yellow']} | {row['stage3_red']} | "
            f"{row['missed_winners']} | {row['false_positives']} | {row['stage4b_unknown']} | "
            f"{row['evidence_missing']} | {row['report_news_unavailable']} | {row['official_evidence_coverage']} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- official_only is intentionally weaker when the historical winner was report/news-driven because those snapshots are excluded.",
            "- case_fixture is strong for regression testing, but curated fixtures do not prove live discovery.",
            "- hybrid is the closest practical approximation when report/news fixtures exist alongside official evidence.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def render_stage3_lifecycle_summary(result: MonthlyReplaySuiteResult) -> str:
    lines = ["# Stage 3 Lifecycle Summary", ""]
    for stage in (Stage.STAGE_3_GREEN, Stage.STAGE_3_YELLOW, Stage.STAGE_3_RED):
        row = result.lifecycle_aggregates["by_stage"].get(stage.value, _empty_lifecycle_row())
        interpretation = "warning / boom-bust protection" if stage == Stage.STAGE_3_RED else "candidate outcome diagnostics"
        lines.extend(
            [
                f"## {stage.value}",
                "",
                f"- count: {row['count']}",
                f"- average MFE 30D / 90D / 180D / 1Y / 2Y: {row['avg_mfe_30d']}, {row['avg_mfe_90d']}, {row['avg_mfe_180d']}, {row['avg_mfe_1y']}, {row['avg_mfe_2y']}",
                f"- average MAE 30D / 90D / 180D / 1Y: {row['avg_mae_30d']}, {row['avg_mae_90d']}, {row['avg_mae_180d']}, {row['avg_mae_1y']}",
                f"- below_entry_rate: {row['below_entry_rate']}",
                f"- average time_to_50pct / 100pct / 200pct: {row['avg_time_to_50pct']}, {row['avg_time_to_100pct']}, {row['avg_time_to_200pct']}",
                f"- median peak_return_from_stage: {row['median_peak_return_from_stage']}",
                f"- worst drawdown_after_peak: {row['worst_drawdown_after_peak']}",
                f"- interpretation: {interpretation}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def render_known_case_validation(result: MonthlyReplaySuiteResult) -> str:
    lines = [
        "# Known Case Validation",
        "",
        "| case_id | company | expected_group | expected_stage | actual_stage_by_mode | layer1_result_by_mode | status_by_mode | evidence_types_seen | missing_evidence_warnings | future_data_used | interpretation |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in result.known_case_validation:
        lines.append(
            f"| {row['case_id']} | {row['company_name']} | {row['expected_group']} | {row['expected_stage']} | "
            f"{_mapping_inline(row['actual_stage_by_mode'])} | {_mapping_inline(row['layer1_result_by_mode'])} | "
            f"{_mapping_inline(row['status_by_mode'])} | {_mapping_inline(row['evidence_types_seen'])} | "
            f"{_mapping_inline(row['missing_evidence_warnings'])} | {row['future_data_used']} | {row['interpretation']} |"
        )
    return "\n".join(lines).rstrip() + "\n"


def render_missed_winners(result: MonthlyReplaySuiteResult) -> str:
    lines = [
        "# Missed Winners",
        "",
        "| case | mode | reason | acceptable? | recommended fix |",
        "| --- | --- | --- | --- | --- |",
    ]
    rows = result.missed_winners
    if not rows:
        lines.append("| none | n/a | n/a | yes | keep monitoring larger replay |")
    for row in rows:
        reason = row["primary_failure_reason"]
        lines.append(
            f"| {row['case_id']} | {row['mode']} | {reason} | {_miss_acceptability(reason)} | {_recommended_fix(reason)} |"
        )
    return "\n".join(lines).rstrip() + "\n"


def render_false_positives(result: MonthlyReplaySuiteResult) -> str:
    lines = [
        "# False Positives And Contained Warnings",
        "",
        "| case | mode | stage | category | red_team_or_reason | 4B/4C | interpretation |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    rows = result.false_positives
    if not rows:
        lines.append("| none | n/a | n/a | n/a | n/a | n/a | no warning fixture became unsafe Green |")
    for row in rows:
        lines.append(
            f"| {row['case_id']} | {row['mode']} | {row['stage']} | {row['category']} | {row['reason']} | "
            f"{row['stage4b_4c']} | {row['interpretation']} |"
        )
    return "\n".join(lines).rstrip() + "\n"


def render_stage4b_4c_review(result: MonthlyReplaySuiteResult) -> str:
    lines = [
        "# Stage 4B / 4C Review",
        "",
        "| mode | symbol | company | Stage 3 date | Stage 3 price | peak date | peak return | 4B date | 4B return | 4B before peak | 4C date | drawdown after peak | status | interpretation |",
        "| --- | --- | --- | --- | ---: | --- | ---: | --- | ---: | --- | --- | ---: | --- | --- |",
    ]
    rows = []
    for mode, mode_result in result.mode_results.items():
        for item in mode_result.lifecycle_results:
            rows.append((mode, item))
    if not rows:
        lines.append("| n/a | n/a | n/a | n/a | 0 | n/a | 0 | n/a | 0 | unknown | n/a | 0 | unknown_insufficient_evidence | no lifecycle rows |")
    for mode, item in rows:
        status = _stage4b_status_against_peak(item)
        lines.append(
            f"| {mode} | {item.symbol} | {item.company_name} | {item.stage_date.isoformat()} | {item.stage_price:.2f} | "
            f"{item.peak_date.isoformat() if item.peak_date else 'n/a'} | {_fmt(item.peak_return_from_stage)} | "
            f"{item.stage4b_date.isoformat() if item.stage4b_date else 'n/a'} | {_fmt(item.stage4b_return_from_stage)} | "
            f"{_stage4b_before_peak(item)} | {item.stage4c_date.isoformat() if item.stage4c_date else 'n/a'} | "
            f"{_fmt(item.drawdown_after_peak)} | {status} | {_stage4b_interpretation(status)} |"
        )
    return "\n".join(lines).rstrip() + "\n"


def render_evidence_coverage(result: MonthlyReplaySuiteResult) -> str:
    coverage = result.evidence_coverage
    lines = ["# Evidence Coverage", "", "## Counts By Source Type", ""]
    for key, value in coverage["aggregate_counts_by_source_type"].items():
        lines.append(f"- {key}: {value}")
    lines.extend(
        [
            "",
            f"- missing_report_news_snapshot_count: {coverage['missing_report_news_snapshot_count']}",
            f"- official_only_limitations: {coverage['official_only_limitations']}",
            f"- stage3_or_4b_unknown_due_to_missing_evidence: {coverage['stage4b_unknown_count']}",
            "",
            "## Recommended Evidence Fixtures To Add Next",
            "",
        ]
    )
    for item in coverage["recommended_next_fixtures"]:
        lines.append(f"- {item}")
    return "\n".join(lines).rstrip() + "\n"


def render_next_backtest_readiness(result: MonthlyReplaySuiteResult) -> str:
    readiness = result.readiness_assessment
    lines = [
        "# Next Backtest Readiness",
        "",
        f"- ready_for_larger_backtest: {readiness['ready_for_larger_backtest']}",
        f"- preferred_mode: {readiness['preferred_mode']}",
        f"- threshold_read: {readiness['threshold_read']}",
        f"- weak_evidence_sources: {', '.join(readiness['weak_evidence_sources']) or 'none'}",
        f"- must_fix_before_weekly_daily: {', '.join(readiness['must_fix_before_weekly_daily']) or 'none'}",
        f"- recommended_next_step: {readiness['recommended_next_step']}",
        "",
        readiness["summary"],
    ]
    return "\n".join(lines).rstrip() + "\n"


def render_top_stage3_candidate_cards(result: MonthlyReplaySuiteResult) -> str:
    lines = ["# Top Stage 3 Candidate Cards", ""]
    rows = _top_stage3_candidates(result.mode_results)
    if not rows:
        lines.append("No Stage 3 candidates were produced by the suite.")
        return "\n".join(lines).rstrip() + "\n"
    lifecycle_by_key = {
        (mode, item.symbol, item.stage.value): item
        for mode, mode_result in result.mode_results.items()
        for item in mode_result.lifecycle_results
    }
    for mode, candidate in rows[:20]:
        lifecycle = lifecycle_by_key.get((mode, candidate.symbol, candidate.stage.value))
        lines.extend(
            [
                f"## {candidate.company_name} ({candidate.symbol})",
                "",
                f"- mode: {mode}",
                f"- first_stage3_date: {candidate.as_of_date.isoformat()}",
                f"- first_stage3_stage: {candidate.stage.value}",
                f"- stage3_price: {_fmt(lifecycle.stage_price if lifecycle else None)}",
                f"- pre_runup_252d: {_fmt(lifecycle.pre_runup_252d if lifecycle else None)}",
                f"- pre_runup_3y: {_fmt(lifecycle.pre_runup_3y if lifecycle else None)}",
                f"- evidence summary: {', '.join(candidate.evidence_types_seen) or 'none'}",
                f"- reason codes: {', '.join(candidate.reason_codes) or 'none'}",
                f"- score_state: {_candidate_score_state(candidate)}",
                "",
                "| score component | value |",
                "| --- | ---: |",
            ]
        )
        for key in (
            "eps_fcf_explosion",
            "contract_quality",
            "backlog_rpo_visibility",
            "capa_constraint",
            "asp_pricing_power",
            "market_mispricing",
            "valuation_rerating",
            "risk_penalty",
        ):
            value = None if candidate.total_score is None else candidate.score_components.get(key, candidate.diagnostic_scores.get(key))
            lines.append(f"| {key} | {_fmt(value)} |")
        lines.extend(
            [
                "",
                "| path metric | value |",
                "| --- | ---: |",
                f"| MFE 30D / 90D / 180D / 1Y / 2Y | {_joined_metrics(lifecycle, ('mfe_30d', 'mfe_90d', 'mfe_180d', 'mfe_1y', 'mfe_2y'))} |",
                f"| MAE 30D / 90D / 180D / 1Y | {_joined_metrics(lifecycle, ('mae_30d', 'mae_90d', 'mae_180d', 'mae_1y'))} |",
                f"| below_entry_flag | {lifecycle.below_entry_flag if lifecycle else 'n/a'} |",
                f"| time_to_50pct / 100pct / 200pct | {_joined_metrics(lifecycle, ('time_to_50pct', 'time_to_100pct', 'time_to_200pct'))} |",
                f"| peak date / return | {(lifecycle.peak_date.isoformat() if lifecycle and lifecycle.peak_date else 'n/a')} / {_fmt(lifecycle.peak_return_from_stage if lifecycle else None)} |",
                f"| 4B / 4C status | {(lifecycle.stage4b_status if lifecycle else 'n/a')} / {(lifecycle.stage4c_date.isoformat() if lifecycle and lifecycle.stage4c_date else 'n/a')} |",
                "",
                f"Interpretation: {_candidate_interpretation(candidate, lifecycle)}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def _candidate_score_state(candidate: HistoricalReplayCandidate) -> str:
    valid = serialized_score_valid(candidate)
    if valid is None:
        valid = "unknown"
    reason = serialized_score_block_reason(candidate) or "none"
    fingerprint = candidate.score_fingerprint or "none"
    input_fingerprint = candidate.research_input_fingerprint or "none"
    drivers = "|".join(candidate.score_variability_drivers) if candidate.score_variability_drivers else "none"
    total = _fmt(candidate.total_score)
    return f"total={total}; valid={valid}; reason={reason}; fingerprint={fingerprint}; input_fingerprint={input_fingerprint}; drivers={drivers}"


def _write_suite_reports(
    *,
    config: MonthlyReplaySuiteConfig,
    output_root: Path,
    mode_results: Mapping[str, HistoricalUniverseReplayResult],
    suite_summary: Mapping[str, Any],
    mode_comparison: Mapping[str, Any],
    lifecycle_aggregates: Mapping[str, Any],
    known_cases: Sequence[Mapping[str, Any]],
    missed: Sequence[Mapping[str, Any]],
    false_positives: Sequence[Mapping[str, Any]],
    evidence_coverage: Mapping[str, Any],
    readiness: Mapping[str, Any],
    limitations: Sequence[str],
) -> Mapping[str, Path]:
    result = MonthlyReplaySuiteResult(
        config=config,
        output_root=output_root,
        mode_results=mode_results,
        suite_summary=suite_summary,
        mode_comparison=mode_comparison,
        lifecycle_aggregates=lifecycle_aggregates,
        known_case_validation=tuple(known_cases),
        missed_winners=tuple(missed),
        false_positives=tuple(false_positives),
        evidence_coverage=evidence_coverage,
        readiness_assessment=readiness,
        limitations=tuple(limitations),
        report_paths={},
    )
    paths = {
        "suite_summary_md": output_root / "suite_summary.md",
        "suite_summary_json": output_root / "suite_summary.json",
        "mode_comparison_md": output_root / "mode_comparison.md",
        "mode_comparison_json": output_root / "mode_comparison.json",
        "stage3_lifecycle_summary_md": output_root / "stage3_lifecycle_summary.md",
        "stage3_lifecycle_results_csv": output_root / "stage3_lifecycle_results.csv",
        "stage3_lifecycle_results_json": output_root / "stage3_lifecycle_results.json",
        "known_case_validation_md": output_root / "known_case_validation.md",
        "missed_winners_md": output_root / "missed_winners.md",
        "false_positives_md": output_root / "false_positives.md",
        "stage4b_4c_review_md": output_root / "stage4b_4c_review.md",
        "evidence_coverage_md": output_root / "evidence_coverage.md",
        "next_backtest_readiness_md": output_root / "next_backtest_readiness.md",
        "top_stage3_candidate_cards_md": output_root / "top_stage3_candidate_cards.md",
    }
    if config.write_md:
        paths["suite_summary_md"].write_text(render_suite_summary(result), encoding="utf-8")
        paths["mode_comparison_md"].write_text(render_mode_comparison(result), encoding="utf-8")
        paths["stage3_lifecycle_summary_md"].write_text(render_stage3_lifecycle_summary(result), encoding="utf-8")
        paths["known_case_validation_md"].write_text(render_known_case_validation(result), encoding="utf-8")
        paths["missed_winners_md"].write_text(render_missed_winners(result), encoding="utf-8")
        paths["false_positives_md"].write_text(render_false_positives(result), encoding="utf-8")
        paths["stage4b_4c_review_md"].write_text(render_stage4b_4c_review(result), encoding="utf-8")
        paths["evidence_coverage_md"].write_text(render_evidence_coverage(result), encoding="utf-8")
        paths["next_backtest_readiness_md"].write_text(render_next_backtest_readiness(result), encoding="utf-8")
        paths["top_stage3_candidate_cards_md"].write_text(render_top_stage3_candidate_cards(result), encoding="utf-8")
    if config.write_json:
        schema = _suite_json_schema(result)
        paths["suite_summary_json"].write_text(json.dumps(schema, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
        paths["mode_comparison_json"].write_text(json.dumps(_jsonable(mode_comparison), ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    if config.write_csv or config.write_json:
        all_lifecycle = tuple(item for mode_result in mode_results.values() for item in mode_result.lifecycle_results)
        write_stage_lifecycle_outputs(
            all_lifecycle,
            json_path=paths["stage3_lifecycle_results_json"],
            csv_path=paths["stage3_lifecycle_results_csv"],
        )
    return paths


def _suite_json_schema(result: MonthlyReplaySuiteResult) -> Mapping[str, Any]:
    return {
        "config": _config_json(result.config),
        "modes": tuple(result.mode_results.keys()),
        "aggregate_counts": result.suite_summary["aggregate_counts"],
        "stage_distribution": result.suite_summary["stage_distribution"],
        "lifecycle_aggregates": result.lifecycle_aggregates,
        "known_case_validation": result.known_case_validation,
        "missed_winners": result.missed_winners,
        "false_positives": result.false_positives,
        "evidence_coverage": result.evidence_coverage,
        "readiness_assessment": result.readiness_assessment,
        "limitations": result.limitations,
    }


def _suite_summary(
    config: MonthlyReplaySuiteConfig,
    mode_results: Mapping[str, HistoricalUniverseReplayResult],
) -> Mapping[str, Any]:
    aggregate = _aggregate_counts(mode_results)
    stage_distribution = _stage_distribution(mode_results)
    known = _known_case_validation(mode_results)
    missed = len(_missed_winner_rows(known))
    false_positive = len(_false_positive_rows(mode_results, _known_case_validation(mode_results)))
    aggregate = dict(aggregate)
    aggregate["missed_known_winners"] = missed
    aggregate["false_positive_or_boom_bust"] = false_positive
    return {
        "config": _config_json(config),
        "modes": tuple(mode_results.keys()),
        "aggregate_counts": aggregate,
        "stage_distribution": stage_distribution,
    }


def _mode_comparison(mode_results: Mapping[str, HistoricalUniverseReplayResult]) -> Mapping[str, Any]:
    rows: dict[str, Any] = {}
    known_rows = _known_case_validation(mode_results)
    for mode, result in mode_results.items():
        candidates = _all_candidates(result)
        lifecycle = result.lifecycle_results
        mode_known = [row for row in known_rows if mode in row["status_by_mode"]]
        rows[mode] = {
            "candidates": len(candidates),
            "stage3_green": sum(1 for item in candidates if item.stage == Stage.STAGE_3_GREEN),
            "stage3_yellow": sum(1 for item in candidates if item.stage == Stage.STAGE_3_YELLOW),
            "stage3_red": sum(1 for item in candidates if item.stage == Stage.STAGE_3_RED),
            "missed_winners": sum(1 for item in mode_known if item["status_by_mode"].get(mode) in {"missed", "skipped_missing_historical_report_news_data"}),
            "false_positives": sum(1 for item in mode_known if item["expected_group"] != "structural" and item["actual_stage_by_mode"].get(mode) == Stage.STAGE_3_GREEN.value),
            "stage4b_unknown": sum(1 for item in lifecycle if item.stage4b_status == STAGE4B_UNKNOWN_INSUFFICIENT_EVIDENCE),
            "evidence_missing": sum(len(item.missing_evidence_warnings) for item in candidates),
            "report_news_unavailable": _missing_report_news_count(result),
            "official_evidence_coverage": _official_evidence_coverage(result),
        }
    return rows


def _lifecycle_aggregates(mode_results: Mapping[str, HistoricalUniverseReplayResult]) -> Mapping[str, Any]:
    rows = tuple(item for mode_result in mode_results.values() for item in mode_result.lifecycle_results if item.failure_reason is None)
    by_stage = {stage.value: _lifecycle_row(tuple(item for item in rows if item.stage == stage)) for stage in (Stage.STAGE_3_GREEN, Stage.STAGE_3_YELLOW, Stage.STAGE_3_RED)}
    return {
        "by_stage": by_stage,
        "total_lifecycle_rows": len(rows),
        "stage4b_count": sum(1 for item in rows if item.stage4b_date is not None),
        "stage4c_count": sum(1 for item in rows if item.stage4c_date is not None),
        "stage4b_unknown_count": sum(1 for item in rows if item.stage4b_status == STAGE4B_UNKNOWN_INSUFFICIENT_EVIDENCE),
    }


def _known_case_validation(mode_results: Mapping[str, HistoricalUniverseReplayResult]) -> tuple[Mapping[str, Any], ...]:
    case_ids = sorted({item.case_id for result in mode_results.values() for item in result.known_case_validations})
    rows: list[Mapping[str, Any]] = []
    for case_id in case_ids:
        validations = {
            mode: next((item for item in result.known_case_validations if item.case_id == case_id), None)
            for mode, result in mode_results.items()
        }
        first = next(item for item in validations.values() if item is not None)
        candidates = {
            mode: _best_candidate_for_case(result, case_id)
            for mode, result in mode_results.items()
        }
        expected_group = _expected_group_label(case_id, first.company_name)
        actual_stage = {mode: (item.final_stage.value if item and item.final_stage else "n/a") for mode, item in validations.items()}
        layer1 = {mode: (item.layer1_result if item else "n/a") for mode, item in validations.items()}
        status = {mode: (item.status if item else "not_in_mode") for mode, item in validations.items()}
        evidence_types = {mode: tuple(candidate.evidence_types_seen) if candidate else () for mode, candidate in candidates.items()}
        missing = {mode: tuple(candidate.missing_evidence_warnings) if candidate else () for mode, candidate in candidates.items()}
        rows.append(
            {
                "case_id": case_id,
                "company_name": first.company_name,
                "expected_group": expected_group,
                "expected_stage": _expected_stage_text(first.case_id, first.company_name),
                "actual_stage_by_mode": actual_stage,
                "layer1_result_by_mode": layer1,
                "status_by_mode": status,
                "evidence_types_seen": evidence_types,
                "missing_evidence_warnings": missing,
                "future_data_used": False,
                "interpretation": _known_case_interpretation(expected_group, status, actual_stage),
                "primary_failure_reason_by_mode": {mode: (item.failure_reason if item else None) for mode, item in validations.items()},
            }
        )
    return tuple(rows)


def _false_positive_rows(
    mode_results: Mapping[str, HistoricalUniverseReplayResult],
    known_cases: Sequence[Mapping[str, Any]],
) -> tuple[Mapping[str, Any], ...]:
    rows: list[Mapping[str, Any]] = []
    lifecycle_by_mode_symbol = {
        (mode, item.symbol): item
        for mode, result in mode_results.items()
        for item in result.lifecycle_results
    }
    for row in known_cases:
        if row["expected_group"] == "structural":
            continue
        for mode, stage in row["actual_stage_by_mode"].items():
            if stage == "n/a":
                continue
            candidate = _best_candidate_for_case(mode_results[mode], row["case_id"])
            lifecycle = lifecycle_by_mode_symbol.get((mode, candidate.symbol if candidate else ""))
            if stage == Stage.STAGE_3_GREEN.value:
                interpretation = "unsafe_green_false_positive"
            elif stage in {Stage.STAGE_3_YELLOW.value, Stage.STAGE_3_RED.value}:
                interpretation = "correctly_contained_as_warning"
            else:
                interpretation = "not_stage3_green"
            rows.append(
                {
                    "case_id": row["case_id"],
                    "mode": mode,
                    "stage": stage,
                    "category": row["expected_group"],
                    "reason": _mapping_inline(row["status_by_mode"]),
                    "stage4b_4c": _stage4b_4c_text(lifecycle),
                    "interpretation": interpretation,
                }
            )
    return tuple(rows)


def _missed_winner_rows(known_cases: Sequence[Mapping[str, Any]]) -> tuple[Mapping[str, Any], ...]:
    rows: list[Mapping[str, Any]] = []
    for row in known_cases:
        if row["expected_group"] != "structural":
            continue
        for mode, status in row["status_by_mode"].items():
            if status not in {"missed", "skipped_missing_historical_report_news_data"}:
                continue
            reason = row["primary_failure_reason_by_mode"].get(mode)
            if not reason:
                missing = row["missing_evidence_warnings"].get(mode, ())
                reason = ",".join(missing) if missing else status
            rows.append(
                {
                    "case_id": row["case_id"],
                    "company_name": row["company_name"],
                    "mode": mode,
                    "status": status,
                    "primary_failure_reason": _normalize_failure_reason(reason),
                    "raw_reason": reason,
                }
            )
    return tuple(rows)


def _evidence_coverage(mode_results: Mapping[str, HistoricalUniverseReplayResult]) -> Mapping[str, Any]:
    counts: dict[str, int] = {
        "disclosure": 0,
        "research_report": 0,
        "news": 0,
        "financial_actual": 0,
        "consensus": 0,
        "consensus_revision": 0,
        "price": 0,
    }
    missing_report_news = 0
    for result in mode_results.values():
        for snapshot in result.snapshots:
            for key, value in snapshot.evidence_counts.items():
                counts[key] = counts.get(key, 0) + int(value)
            missing_report_news += sum(
                1
                for item in snapshot.missing_evidence_warnings
                if "research_report" in item or "news" in item or "search_snapshot" in item
            )
    stage4b_unknown = sum(
        1
        for result in mode_results.values()
        for item in result.lifecycle_results
        if item.stage4b_status == STAGE4B_UNKNOWN_INSUFFICIENT_EVIDENCE
    )
    return {
        "aggregate_counts_by_source_type": dict(sorted(counts.items())),
        "missing_report_news_snapshot_count": missing_report_news,
        "official_only_limitations": "official_only excludes report/news/consensus fixtures by design",
        "stage4b_unknown_count": stage4b_unknown,
        "recommended_next_fixtures": (
            "add historical report/news snapshots for structural winners that are report-driven",
            "add more 4B evidence fixtures such as revision slowdown, backlog slowdown, and blow-off pattern records",
            "expand official historical disclosures and financial actuals before broad official_only replay",
        ),
    }


def _readiness_assessment(
    mode_comparison: Mapping[str, Any],
    lifecycle: Mapping[str, Any],
    missed: Sequence[Mapping[str, Any]],
    false_positives: Sequence[Mapping[str, Any]],
    coverage: Mapping[str, Any],
) -> Mapping[str, Any]:
    unsafe_green = [row for row in false_positives if row["interpretation"] == "unsafe_green_false_positive"]
    weak_sources = []
    if coverage["missing_report_news_snapshot_count"] > 0:
        weak_sources.append("historical_report_news_snapshots")
    if coverage["stage4b_unknown_count"] > 0:
        weak_sources.append("4B_evidence_coverage")
    ready = not unsafe_green
    must_fix = []
    if unsafe_green:
        must_fix.append("block one-off or boom-bust Stage 3-Green")
    if mode_comparison.get(HistoricalReplayMode.CASE_FIXTURE.value, {}).get("candidates", 0) == 0:
        must_fix.append("case_fixture candidate generation")
    preferred = HistoricalReplayMode.HYBRID.value if HistoricalReplayMode.HYBRID.value in mode_comparison else next(iter(mode_comparison))
    return {
        "ready_for_larger_backtest": ready,
        "preferred_mode": preferred,
        "threshold_read": "no broad threshold loosening recommended; investigate misses by evidence source first",
        "weak_evidence_sources": tuple(weak_sources),
        "must_fix_before_weekly_daily": tuple(must_fix),
        "recommended_next_step": "run hybrid weekly after adding missing report/news snapshots" if weak_sources else "run hybrid weekly",
        "summary": (
            "Monthly replay is structurally sane for a larger fixture backtest, but conclusions remain limited by missing "
            "historical report/news snapshots and sparse 4B evidence."
            if ready
            else "Monthly replay is not ready for a larger backtest because an unsafe Green false positive was detected."
        ),
    }


def _limitations(coverage: Mapping[str, Any]) -> tuple[str, ...]:
    items = [
        "Layer 1 recall is not Stage 3 conviction.",
        "case_fixture success is curated fixture replay, not proof of live discovery.",
        "official_only misses report-driven winners when old report/news snapshots are unavailable.",
        "4B is not fabricated; unknown_insufficient_evidence is a valid result.",
    ]
    if coverage["missing_report_news_snapshot_count"]:
        items.append("Missing report/news snapshots limit historical discovery claims.")
    return tuple(items)


def _aggregate_counts(mode_results: Mapping[str, HistoricalUniverseReplayResult]) -> Mapping[str, int]:
    candidates = [candidate for result in mode_results.values() for candidate in _all_candidates(result)]
    lifecycle = [item for result in mode_results.values() for item in result.lifecycle_results]
    return {
        "replay_dates": sum(len(result.snapshots) for result in mode_results.values()),
        "scanned_instruments": sum(snapshot.instruments_scanned for result in mode_results.values() for snapshot in result.snapshots),
        "candidates": len(candidates),
        "event_search_or_higher": sum(1 for item in candidates if item.layer1_result in {"event_search", "deep_research", "stage2_or_higher"}),
        "deep_research": sum(1 for item in candidates if item.layer1_result == "deep_research"),
        "stage4b": sum(1 for item in lifecycle if item.stage4b_date is not None),
        "stage4c": sum(1 for item in lifecycle if item.stage4c_date is not None),
        "still_active": sum(1 for item in lifecycle if item.still_active_flag),
    }


def _stage_distribution(mode_results: Mapping[str, HistoricalUniverseReplayResult]) -> Mapping[str, int]:
    counts: dict[str, int] = {}
    for result in mode_results.values():
        for candidate in _all_candidates(result):
            counts[candidate.stage.value] = counts.get(candidate.stage.value, 0) + 1
    return dict(sorted(counts.items()))


def _lifecycle_row(rows: Sequence[StageLifecycleResult]) -> Mapping[str, Any]:
    if not rows:
        return _empty_lifecycle_row()
    return {
        "count": len(rows),
        "avg_mfe_30d": _avg_float(item.mfe_30d for item in rows),
        "avg_mfe_90d": _avg_float(item.mfe_90d for item in rows),
        "avg_mfe_180d": _avg_float(item.mfe_180d for item in rows),
        "avg_mfe_1y": _avg_float(item.mfe_1y for item in rows),
        "avg_mfe_2y": _avg_float(item.mfe_2y for item in rows),
        "avg_mae_30d": _avg_float(item.mae_30d for item in rows),
        "avg_mae_90d": _avg_float(item.mae_90d for item in rows),
        "avg_mae_180d": _avg_float(item.mae_180d for item in rows),
        "avg_mae_1y": _avg_float(item.mae_1y for item in rows),
        "below_entry_rate": _avg_float((1.0 if item.below_entry_flag else 0.0) for item in rows),
        "avg_time_to_50pct": _avg_float(item.time_to_50pct for item in rows),
        "avg_time_to_100pct": _avg_float(item.time_to_100pct for item in rows),
        "avg_time_to_200pct": _avg_float(item.time_to_200pct for item in rows),
        "median_peak_return_from_stage": _median_float(item.peak_return_from_stage for item in rows),
        "worst_drawdown_after_peak": _min_float(item.drawdown_after_peak for item in rows),
    }


def _empty_lifecycle_row() -> Mapping[str, Any]:
    return {
        "count": 0,
        "avg_mfe_30d": None,
        "avg_mfe_90d": None,
        "avg_mfe_180d": None,
        "avg_mfe_1y": None,
        "avg_mfe_2y": None,
        "avg_mae_30d": None,
        "avg_mae_90d": None,
        "avg_mae_180d": None,
        "avg_mae_1y": None,
        "below_entry_rate": None,
        "avg_time_to_50pct": None,
        "avg_time_to_100pct": None,
        "avg_time_to_200pct": None,
        "median_peak_return_from_stage": None,
        "worst_drawdown_after_peak": None,
    }


def _top_stage3_candidates(mode_results: Mapping[str, HistoricalUniverseReplayResult]) -> tuple[tuple[str, HistoricalReplayCandidate], ...]:
    rows = [
        (mode, candidate)
        for mode, result in mode_results.items()
        for candidate in _all_candidates(result)
        if candidate.stage in {Stage.STAGE_3_GREEN, Stage.STAGE_3_YELLOW, Stage.STAGE_3_RED}
    ]
    return tuple(sorted(rows, key=lambda item: (-_score_sort_value(item[1].total_score), item[0], item[1].case_id)))


def _all_candidates(result: HistoricalUniverseReplayResult) -> tuple[HistoricalReplayCandidate, ...]:
    return tuple(candidate for snapshot in result.snapshots for candidate in snapshot.candidates)


def _best_candidate_for_case(result: HistoricalUniverseReplayResult, case_id: str) -> HistoricalReplayCandidate | None:
    candidates = [candidate for candidate in _all_candidates(result) if candidate.case_id == case_id]
    if not candidates:
        return None
    return sorted(candidates, key=lambda item: (_stage_rank(item.stage), item.layer1_score, _score_sort_value(item.total_score)), reverse=True)[0]


def _score_sort_value(score: float | None) -> float:
    return float(score) if score is not None else -1.0


def _missing_report_news_count(result: HistoricalUniverseReplayResult) -> int:
    return sum(
        1
        for snapshot in result.snapshots
        for warning in snapshot.missing_evidence_warnings
        if "research_report" in warning or "news" in warning or "search_snapshot" in warning
    )


def _official_evidence_coverage(result: HistoricalUniverseReplayResult) -> int:
    return sum(snapshot.evidence_counts.get("disclosure", 0) + snapshot.evidence_counts.get("financial_actual", 0) for snapshot in result.snapshots)


def _expected_group_label(case_id: str, company_name: str) -> str:
    lowered = f"{case_id} {company_name}".lower()
    if "zoom" in lowered or "seegene" in lowered or "씨젠" in lowered:
        return "one_off"
    if "smci" in lowered:
        return "boom_bust"
    if "daehan" in lowered or "대한전선" in lowered or "ecopro" in lowered or "hmm" in lowered:
        return "valuation_overheat"
    return "structural"


def _expected_stage_text(case_id: str, company_name: str) -> str:
    group = _expected_group_label(case_id, company_name)
    if group == "structural":
        return "Stage 2 or Stage 3-Green/Yellow depending evidence"
    if group == "one_off":
        return "Stage 3-Red or lower"
    if group == "boom_bust":
        return "4B before 4C if evidence exists"
    return "not S-grade Green"


def _known_case_interpretation(expected_group: str, statuses: Mapping[str, str], stages: Mapping[str, str]) -> str:
    if expected_group != "structural" and any(stage == Stage.STAGE_3_GREEN.value for stage in stages.values()):
        return "unsafe: warning fixture became Green"
    if any(status == "skipped_missing_historical_report_news_data" for status in statuses.values()):
        return "limited by missing report/news snapshot, especially official_only"
    if expected_group == "structural" and any(status in {"detected", "detected_late"} for status in statuses.values()):
        return "structural fixture reached Layer 1 or higher"
    return "contained or insufficient evidence"


def _miss_acceptability(reason: str) -> str:
    if "official_only" in reason or "research_report" in reason or "news" in reason:
        return "acceptable for official_only, not enough for live-discovery proof"
    return "needs review"


def _recommended_fix(reason: str) -> str:
    if "official_only" in reason or "research_report" in reason or "news" in reason:
        return "add historical report/news snapshots or run hybrid"
    if "price" in reason:
        return "add historical price bars"
    if "disclosure" in reason:
        return "add historical disclosure detail fixtures"
    if "threshold" in reason:
        return "review threshold only after evidence audit"
    return "inspect parser/source coverage"


def _normalize_failure_reason(reason: str) -> str:
    if "research_report_excluded" in reason or "news_excluded" in reason or "consensus_excluded" in reason:
        return "official_only_excluded_report_news"
    if "search_snapshot" in reason or "research_report" in reason or "news" in reason:
        return "no_report_radar_path"
    if "price" in reason:
        return "no_price_signal"
    if "disclosure" in reason:
        return "no_disclosure_signal"
    if "source_missing" in reason:
        return "source_missing"
    if "not_in_universe" in reason:
        return "not_in_universe"
    if "parser" in reason:
        return "parser_failure"
    if "threshold" in reason or "below" in reason:
        return "threshold_too_high"
    return "unknown"


def _stage4b_4c_text(item: StageLifecycleResult | None) -> str:
    if item is None:
        return "no lifecycle row"
    return f"4B={item.stage4b_date.isoformat() if item.stage4b_date else item.stage4b_status}, 4C={item.stage4c_date.isoformat() if item.stage4c_date else 'none'}"


def _stage4b_status_against_peak(item: StageLifecycleResult) -> str:
    if item.stage4b_status == STAGE4B_UNKNOWN_INSUFFICIENT_EVIDENCE:
        return "unknown_insufficient_evidence"
    if item.stage4b_date is None or item.peak_date is None:
        return "unknown_insufficient_evidence"
    delta = (item.stage4b_date - item.peak_date).days
    if delta < -30:
        return "detected_before_peak"
    if abs(delta) <= 30:
        return "detected_near_peak"
    return "detected_after_peak"


def _stage4b_before_peak(item: StageLifecycleResult) -> str:
    if item.stage4b_date is None or item.peak_date is None:
        return "unknown"
    return "yes" if item.stage4b_date <= item.peak_date else "no"


def _stage4b_interpretation(status: str) -> str:
    if status == "detected_before_peak":
        return "4B warning arrived before the final peak"
    if status == "detected_near_peak":
        return "4B warning arrived near the peak"
    if status == "detected_after_peak":
        return "4B was late versus the price peak"
    return "4B evidence is insufficient, so no date was invented"


def _candidate_interpretation(candidate: HistoricalReplayCandidate, lifecycle: StageLifecycleResult | None) -> str:
    if candidate.stage == Stage.STAGE_3_GREEN:
        return "true E2R-like only if structural evidence and cross-evidence remain valid; this is not a recommendation"
    if candidate.stage == Stage.STAGE_3_YELLOW:
        return "candidate has meaningful evidence, but Green confirmation is incomplete"
    if candidate.stage == Stage.STAGE_3_RED:
        return "rerating-like evidence exists, but Red Team or one-off/quality risk contains it"
    if lifecycle and lifecycle.stage4b_status == STAGE4B_UNKNOWN_INSUFFICIENT_EVIDENCE:
        return "outcome metrics exist, but Stage 4B evidence is incomplete"
    return "insufficient Stage 3 evidence"


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
    return order.get(stage, 0)


def _suite_output_root(config: MonthlyReplaySuiteConfig) -> Path:
    return Path(config.output_directory) / f"{config.start_date.isoformat()}_to_{config.end_date.isoformat()}"


def _config_json(config: MonthlyReplaySuiteConfig | HistoricalReplayConfig) -> Mapping[str, Any]:
    return {
        "start_date": config.start_date.isoformat(),
        "end_date": config.end_date.isoformat(),
        "output_directory": str(config.output_directory),
        "modes": tuple(mode.value for mode in getattr(config, "modes", (getattr(config, "mode", ""),)) if mode),
        "frequency": getattr(config, "frequency", getattr(config, "replay_frequency", "")).value,
        "market": getattr(config, "market", Market.KR).value,
        "universe_limit": getattr(config, "universe_limit", None),
        "max_candidates_per_date": getattr(config, "max_candidates_per_date", None),
    }


def _avg_float(values: Iterable[float | int | None]) -> float | None:
    clean = [float(item) for item in values if item is not None]
    if not clean:
        return None
    return round(sum(clean) / len(clean), 6)


def _median_float(values: Iterable[float | None]) -> float | None:
    clean = [float(item) for item in values if item is not None]
    if not clean:
        return None
    return round(float(median(clean)), 6)


def _min_float(values: Iterable[float | None]) -> float | None:
    clean = [float(item) for item in values if item is not None]
    if not clean:
        return None
    return round(min(clean), 6)


def _fmt(value: float | int | None) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, int):
        return str(value)
    return f"{value:.4f}"


def _joined_metrics(item: StageLifecycleResult | None, names: Sequence[str]) -> str:
    if item is None:
        return "n/a"
    return " / ".join(_fmt(getattr(item, name)) for name in names)


def _mapping_inline(value: Mapping[str, Any]) -> str:
    parts = []
    for key, item in value.items():
        if isinstance(item, (tuple, list)):
            text = ",".join(str(part) for part in item) or "none"
        else:
            text = str(item)
        parts.append(f"{key}:{text}")
    return "; ".join(parts) if parts else "none"


def _jsonable(value: Any) -> Any:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Path):
        return str(value)
    if is_dataclass(value):
        payload = {field.name: _jsonable(getattr(value, field.name)) for field in fields(value)}
        if "total_score" in payload and "score_valid" in payload:
            payload = normalized_score_state_payload(payload)
        return payload
    if isinstance(value, Mapping):
        return normalized_score_state_mapping_if_present({str(key): _jsonable(item) for key, item in value.items()})
    if isinstance(value, (list, tuple, set, frozenset)):
        return [_jsonable(item) for item in value]
    return value


__all__ = [
    "DEFAULT_MONTHLY_SUITE_OUTPUT_DIR",
    "MonthlyReplaySuiteConfig",
    "MonthlyReplaySuiteResult",
    "MonthlyReplaySuiteRunner",
    "render_evidence_coverage",
    "render_false_positives",
    "render_known_case_validation",
    "render_missed_winners",
    "render_mode_comparison",
    "render_next_backtest_readiness",
    "render_stage3_lifecycle_summary",
    "render_stage4b_4c_review",
    "render_suite_summary",
    "render_top_stage3_candidate_cards",
]
