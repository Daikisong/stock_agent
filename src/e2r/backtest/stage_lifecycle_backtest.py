"""Stage lifecycle replay metrics for historical E2R candidates."""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass, fields, is_dataclass
from datetime import date, datetime
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.backtesting import BacktestEngine, Stage3BacktestInput
from e2r.models import PriceBar, Stage, StageSnapshot


STAGE4B_DETECTED = "detected"
STAGE4B_NOT_DETECTED = "not_detected"
STAGE4B_UNKNOWN_INSUFFICIENT_EVIDENCE = "unknown_insufficient_evidence"


@dataclass(frozen=True)
class StageLifecycleInput:
    """One historical stage event and the price path visible for backtesting."""

    symbol: str
    company_name: str
    stage: Stage
    stage_date: date
    stage_price: float
    price_bars: Sequence[PriceBar]
    stage_snapshots: Sequence[StageSnapshot] = ()
    evidence_coverage_insufficient: bool = False
    source_mode: str = "case_fixture"

    def __post_init__(self) -> None:
        object.__setattr__(self, "price_bars", tuple(self.price_bars))
        object.__setattr__(self, "stage_snapshots", tuple(self.stage_snapshots))


@dataclass(frozen=True)
class StageLifecycleResult:
    """Price-path and Stage 4 diagnostics after an E2R stage event."""

    symbol: str
    company_name: str
    stage: Stage
    stage_date: date
    stage_price: float
    pre_runup_252d: float | None
    pre_runup_3y: float | None
    mfe_30d: float | None
    mfe_90d: float | None
    mfe_180d: float | None
    mfe_1y: float | None
    mfe_2y: float | None
    mae_30d: float | None
    mae_90d: float | None
    mae_180d: float | None
    mae_1y: float | None
    below_entry_flag: bool | None
    time_to_50pct: int | None
    time_to_100pct: int | None
    time_to_200pct: int | None
    peak_date: date | None
    peak_price: float | None
    peak_return_from_stage: float | None
    stage4b_date: date | None
    stage4b_price: float | None
    stage4b_return_from_stage: float | None
    stage4b_status: str
    stage4c_date: date | None
    stage4c_price: float | None
    drawdown_after_peak: float | None
    still_active_flag: bool
    source_mode: str
    failure_reason: str | None = None


class StageLifecycleBacktest:
    """Compute post-stage price metrics without inventing missing 4B/4C evidence."""

    def evaluate(self, event: StageLifecycleInput) -> StageLifecycleResult:
        try:
            backtest = BacktestEngine().evaluate_stage3(
                Stage3BacktestInput(
                    symbol=event.symbol,
                    stage3_date=event.stage_date,
                    price_bars=event.price_bars,
                    stage_snapshots=event.stage_snapshots,
                    stage3_price=event.stage_price,
                )
            )
        except ValueError as exc:
            return _failed_result(event, str(exc))

        if backtest.stage4b_date is not None:
            stage4b_status = STAGE4B_DETECTED
        elif event.evidence_coverage_insufficient:
            stage4b_status = STAGE4B_UNKNOWN_INSUFFICIENT_EVIDENCE
        else:
            stage4b_status = STAGE4B_NOT_DETECTED

        return StageLifecycleResult(
            symbol=event.symbol,
            company_name=event.company_name,
            stage=event.stage,
            stage_date=backtest.stage3_date,
            stage_price=backtest.stage3_price,
            pre_runup_252d=backtest.pre_runup_252d,
            pre_runup_3y=backtest.pre_runup_3y,
            mfe_30d=backtest.mfe_30d,
            mfe_90d=backtest.mfe_90d,
            mfe_180d=backtest.mfe_180d,
            mfe_1y=backtest.mfe_1y,
            mfe_2y=backtest.mfe_2y,
            mae_30d=backtest.mae_30d,
            mae_90d=backtest.mae_90d,
            mae_180d=backtest.mae_180d,
            mae_1y=backtest.mae_1y,
            below_entry_flag=backtest.below_entry_flag,
            time_to_50pct=backtest.time_to_50pct,
            time_to_100pct=backtest.time_to_100pct,
            time_to_200pct=backtest.time_to_200pct,
            peak_date=backtest.peak_date,
            peak_price=backtest.peak_price,
            peak_return_from_stage=backtest.peak_return_from_stage3,
            stage4b_date=backtest.stage4b_date,
            stage4b_price=backtest.stage4b_price,
            stage4b_return_from_stage=backtest.stage4b_return_from_stage3,
            stage4b_status=stage4b_status,
            stage4c_date=backtest.stage4c_date,
            stage4c_price=backtest.stage4c_price,
            drawdown_after_peak=backtest.drawdown_after_peak,
            still_active_flag=backtest.stage4c_date is None,
            source_mode=event.source_mode,
        )

    def evaluate_many(self, events: Sequence[StageLifecycleInput]) -> tuple[StageLifecycleResult, ...]:
        return tuple(self.evaluate(event) for event in events)


def write_stage_lifecycle_outputs(
    results: Sequence[StageLifecycleResult],
    *,
    json_path: str | Path,
    csv_path: str | Path,
) -> None:
    """Write lifecycle results in machine-readable JSON and spreadsheet CSV."""

    json_target = Path(json_path)
    csv_target = Path(csv_path)
    json_target.parent.mkdir(parents=True, exist_ok=True)
    csv_target.parent.mkdir(parents=True, exist_ok=True)
    json_target.write_text(json.dumps(_jsonable(tuple(results)), ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    field_names = [field.name for field in fields(StageLifecycleResult)]
    with csv_target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=field_names)
        writer.writeheader()
        for item in results:
            writer.writerow({name: _csv_value(getattr(item, name)) for name in field_names})


def _failed_result(event: StageLifecycleInput, reason: str) -> StageLifecycleResult:
    if event.evidence_coverage_insufficient:
        stage4b_status = STAGE4B_UNKNOWN_INSUFFICIENT_EVIDENCE
    else:
        stage4b_status = STAGE4B_NOT_DETECTED
    return StageLifecycleResult(
        symbol=event.symbol,
        company_name=event.company_name,
        stage=event.stage,
        stage_date=event.stage_date,
        stage_price=event.stage_price,
        pre_runup_252d=None,
        pre_runup_3y=None,
        mfe_30d=None,
        mfe_90d=None,
        mfe_180d=None,
        mfe_1y=None,
        mfe_2y=None,
        mae_30d=None,
        mae_90d=None,
        mae_180d=None,
        mae_1y=None,
        below_entry_flag=None,
        time_to_50pct=None,
        time_to_100pct=None,
        time_to_200pct=None,
        peak_date=None,
        peak_price=None,
        peak_return_from_stage=None,
        stage4b_date=None,
        stage4b_price=None,
        stage4b_return_from_stage=None,
        stage4b_status=stage4b_status,
        stage4c_date=None,
        stage4c_price=None,
        drawdown_after_peak=None,
        still_active_flag=False,
        source_mode=event.source_mode,
        failure_reason=reason,
    )


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


def _csv_value(value: Any) -> Any:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, Enum):
        return value.value
    return value


__all__ = [
    "STAGE4B_DETECTED",
    "STAGE4B_NOT_DETECTED",
    "STAGE4B_UNKNOWN_INSUFFICIENT_EVIDENCE",
    "StageLifecycleBacktest",
    "StageLifecycleInput",
    "StageLifecycleResult",
    "write_stage_lifecycle_outputs",
]
