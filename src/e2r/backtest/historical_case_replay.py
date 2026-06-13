"""Full historical fixture replay beyond Layer-1 recall."""

from __future__ import annotations

import json
from dataclasses import dataclass, fields, is_dataclass
from datetime import date, datetime
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.backtest.layer1_recall import Layer1RecallResult, evaluate_layer1_recall_case
from e2r.historical_cases import HistoricalCase, load_historical_cases, run_historical_case_pipeline
from e2r.models import BacktestResult, Stage
from e2r.score_validity import (
    is_score_valid,
    normalized_score_state_mapping_if_present,
    normalized_score_state_payload,
    research_input_fingerprint,
    serialized_score_block_reason,
    serialized_score_valid,
    score_block_reason,
    score_fingerprint,
    score_variability_drivers,
    visible_score_total,
)


DEFAULT_REPLAY_OUTPUT_DIR = Path("output/backtests/historical_case_replay")


@dataclass(frozen=True)
class HistoricalCaseReplayResult:
    """One full historical case replay row."""

    case_id: str
    symbol: str
    company_name: str
    market: str
    as_of_date: date
    expected_stage: Stage | None
    final_stage: Stage
    total_score: float | None
    score_valid: bool | None
    score_blocked_reason: str | None
    score_fingerprint: str | None
    research_input_fingerprint: str | None
    score_variability_drivers: tuple[str, ...]
    shortage_type: str
    red_team_status: str
    layer1_result: Layer1RecallResult
    backtest: BacktestResult
    passed_expected_behavior: bool
    failure_reason: str | None = None


@dataclass(frozen=True)
class HistoricalCaseReplaySummary:
    """Aggregated full historical replay output."""

    as_of_date: date
    results: tuple[HistoricalCaseReplayResult, ...]
    total_cases: int
    passed_cases: int
    failed_cases: int
    stage_distribution: Mapping[str, int]
    one_off_green_violations: tuple[str, ...]
    structural_misses: tuple[str, ...]
    smci_4b_before_4c: bool | None
    output_json_path: Path | None = None
    output_md_path: Path | None = None


class HistoricalCaseReplayRunner:
    """Replay fixture cases through features, stage, red team, and backtest."""

    def run(
        self,
        *,
        as_of_date: date,
        case_root: str | Path = "data/historical_cases",
        output_directory: str | Path = DEFAULT_REPLAY_OUTPUT_DIR,
        write_outputs: bool = True,
    ) -> HistoricalCaseReplaySummary:
        cases = tuple(load_historical_cases(case_root))
        results = tuple(_replay_case(case) for case in cases)
        summary = _summary(as_of_date, results)
        if not write_outputs:
            return summary
        output_root = Path(output_directory)
        output_root.mkdir(parents=True, exist_ok=True)
        stem = as_of_date.isoformat()
        json_path = output_root / f"{stem}_results.json"
        md_path = output_root / f"{stem}_summary.md"
        json_path.write_text(json.dumps(_jsonable(summary), ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
        md_path.write_text(render_historical_case_replay_summary(summary), encoding="utf-8")
        return HistoricalCaseReplaySummary(
            as_of_date=summary.as_of_date,
            results=summary.results,
            total_cases=summary.total_cases,
            passed_cases=summary.passed_cases,
            failed_cases=summary.failed_cases,
            stage_distribution=summary.stage_distribution,
            one_off_green_violations=summary.one_off_green_violations,
            structural_misses=summary.structural_misses,
            smci_4b_before_4c=summary.smci_4b_before_4c,
            output_json_path=json_path,
            output_md_path=md_path,
        )


def render_historical_case_replay_summary(summary: HistoricalCaseReplaySummary) -> str:
    """Render a compact markdown summary for operator review."""

    lines = [
        "# Historical Case Replay",
        "",
        f"- as_of_date: {summary.as_of_date.isoformat()}",
        f"- total_cases: {summary.total_cases}",
        f"- passed_cases: {summary.passed_cases}",
        f"- failed_cases: {summary.failed_cases}",
        f"- stage_distribution: {_mapping_text(summary.stage_distribution)}",
        f"- one_off_green_violations: {', '.join(summary.one_off_green_violations) if summary.one_off_green_violations else 'none'}",
        f"- structural_misses: {', '.join(summary.structural_misses) if summary.structural_misses else 'none'}",
        f"- smci_4b_before_4c: {summary.smci_4b_before_4c}",
        "",
        "| case | stage | layer1 | visible_score | score state | MFE 1Y | MAE 1Y | 4B | 4C | pass |",
        "| --- | --- | --- | ---: | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for item in summary.results:
        lines.append(
            "| "
            + " | ".join(
                (
                    item.case_id,
                    item.final_stage.value,
                    item.layer1_result.actual_layer1_result,
                    _fmt_score(item.total_score),
                    _score_state_text(item),
                    _fmt(item.backtest.mfe_1y),
                    _fmt(item.backtest.mae_1y),
                    str(item.backtest.time_to_4b),
                    str(item.backtest.time_to_4c),
                    "yes" if item.passed_expected_behavior else f"no: {item.failure_reason}",
                )
            )
            + " |"
        )
    return "\n".join(lines).rstrip() + "\n"


def _score_state_text(item: HistoricalCaseReplayResult) -> str:
    valid = serialized_score_valid(item)
    if valid is None:
        valid = "unknown"
    reason = serialized_score_block_reason(item) or "none"
    fingerprint = item.score_fingerprint or "none"
    return f"valid={valid}; reason={reason}; fp={fingerprint}"


def _replay_case(case: HistoricalCase) -> HistoricalCaseReplayResult:
    pipeline = run_historical_case_pipeline(case)
    layer1 = evaluate_layer1_recall_case(case)
    passed, reason = _expected_behavior(case, pipeline.stage.stage, pipeline.backtest, layer1)
    input_fingerprint = research_input_fingerprint(
        score=pipeline.score,
        evidence=case.evidence,
        input_counts=_feature_input_count_row(pipeline.feature_input),
        source_fields=pipeline.feature_result.source_fields,
        extra={"case_id": case.case_id},
    )
    return HistoricalCaseReplayResult(
        case_id=case.case_id,
        symbol=case.symbol,
        company_name=case.company_name,
        market=case.market.value,
        as_of_date=case.stage3_date,
        expected_stage=case.expected_stage,
        final_stage=pipeline.stage.stage,
        total_score=visible_score_total(pipeline.score),
        score_valid=is_score_valid(pipeline.score),
        score_blocked_reason=score_block_reason(pipeline.score),
        score_fingerprint=score_fingerprint(pipeline.score),
        research_input_fingerprint=input_fingerprint,
        score_variability_drivers=score_variability_drivers(
            pipeline.score,
            input_counts=_feature_input_count_row(pipeline.feature_input),
            evidence_count=len(pipeline.stage.evidence_ids),
            input_fingerprint=input_fingerprint,
        ),
        shortage_type=pipeline.feature_result.shortage_type.value,
        red_team_status=pipeline.red_team.risk_level.value,
        layer1_result=layer1,
        backtest=pipeline.backtest,
        passed_expected_behavior=passed,
        failure_reason=reason,
    )


def _expected_behavior(
    case: HistoricalCase,
    stage: Stage,
    backtest: BacktestResult,
    layer1: Layer1RecallResult,
) -> tuple[bool, str | None]:
    if not layer1.passed_minimum:
        return False, layer1.false_none_reason or "layer1_miss"
    lowered = f"{case.case_id} {case.company_name}".lower()
    if any(token in lowered for token in ("zoom", "seegene", "씨젠")) and stage == Stage.STAGE_3_GREEN:
        return False, "one_off_case_became_green"
    if "smci" in lowered:
        if backtest.time_to_4b is None or backtest.time_to_4c is None:
            return False, "smci_missing_4b_4c"
        if backtest.time_to_4b >= backtest.time_to_4c:
            return False, "smci_4b_not_before_4c"
    if "daehan" in lowered or "대한전선" in case.company_name:
        if stage == Stage.STAGE_3_GREEN:
            return False, "daehan_like_case_became_green"
    if _is_structural_success(case):
        allowed = {Stage.STAGE_2, Stage.STAGE_3_GREEN, Stage.STAGE_3_YELLOW}
        if stage not in allowed:
            return False, "structural_case_below_stage2"
    return True, None


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


def _summary(as_of_date: date, results: Sequence[HistoricalCaseReplayResult]) -> HistoricalCaseReplaySummary:
    stage_counts: dict[str, int] = {}
    for item in results:
        stage_counts[item.final_stage.value] = stage_counts.get(item.final_stage.value, 0) + 1
    one_off_violations = tuple(item.case_id for item in results if item.failure_reason == "one_off_case_became_green")
    structural_misses = tuple(item.case_id for item in results if item.failure_reason == "structural_case_below_stage2")
    smci = next((item for item in results if "smci" in item.case_id.lower()), None)
    smci_ok = None
    if smci is not None and smci.backtest.time_to_4b is not None and smci.backtest.time_to_4c is not None:
        smci_ok = smci.backtest.time_to_4b < smci.backtest.time_to_4c
    passed = sum(1 for item in results if item.passed_expected_behavior)
    return HistoricalCaseReplaySummary(
        as_of_date=as_of_date,
        results=tuple(sorted(results, key=lambda item: item.case_id)),
        total_cases=len(results),
        passed_cases=passed,
        failed_cases=len(results) - passed,
        stage_distribution=dict(sorted(stage_counts.items())),
        one_off_green_violations=one_off_violations,
        structural_misses=structural_misses,
        smci_4b_before_4c=smci_ok,
    )


def _is_structural_success(case: HistoricalCase) -> bool:
    lowered = case.case_id.lower()
    return any(
        token in lowered
        for token in (
            "hd_hyundai",
            "hyosung",
            "iljin",
            "sanil",
            "samyang",
            "hanwha",
            "nvidia",
        )
    )


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


def _mapping_text(value: Mapping[str, Any]) -> str:
    return ", ".join(f"{key}={item}" for key, item in value.items()) if value else "none"


def _fmt(value: float | None) -> str:
    return "n/a" if value is None else f"{value:.3f}"


def _fmt_score(value: float | None) -> str:
    return "" if value is None else f"{value:.1f}"


__all__ = [
    "DEFAULT_REPLAY_OUTPUT_DIR",
    "HistoricalCaseReplayResult",
    "HistoricalCaseReplayRunner",
    "HistoricalCaseReplaySummary",
    "render_historical_case_replay_summary",
]
