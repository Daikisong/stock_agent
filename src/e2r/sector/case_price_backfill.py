"""Price-path backfill for E2R case-library records."""

from __future__ import annotations

import csv
from dataclasses import replace
from datetime import date, timedelta
from pathlib import Path
from typing import Iterable

from e2r.sector.case_library import E2RCaseRecord, PriceValidation, load_case_library, write_case_library
from e2r.sources.source_errors import date_value, float_or_none, load_fixture_records


def backfill_case_price_paths(
    records: Iterable[E2RCaseRecord],
    *,
    price_root: str | Path = "data/historical_official/prices",
) -> tuple[E2RCaseRecord, ...]:
    """Fill price-validation fields from historical official price rows."""

    bars_by_symbol = _load_bars(price_root)
    filled: list[E2RCaseRecord] = []
    for record in records:
        bars = bars_by_symbol.get(record.symbol, ())
        filled.append(_fill_record(record, bars))
    return tuple(filled)


def backfill_case_price_file(
    *,
    cases_path: str | Path,
    price_root: str | Path,
    output_path: str | Path,
) -> Path:
    records = load_case_library(cases_path)
    filled = backfill_case_price_paths(records, price_root=price_root)
    return write_case_library(filled, output_path)


def _fill_record(record: E2RCaseRecord, bars: tuple[dict[str, float | date], ...]) -> E2RCaseRecord:
    if not bars:
        return replace(
            record,
            price_validation=replace(record.price_validation, price_validation_status="missing_price_data"),
        )

    stage1_price = _price_on_or_before(bars, record.stage1_date)
    stage2_price = _price_on_or_before(bars, record.stage2_date)
    stage3_price = _price_on_or_before(bars, record.stage3_date)
    stage4b_price = _price_on_or_before(bars, record.stage4b_date)
    stage4c_price = _price_on_or_before(bars, record.stage4c_date)
    anchor_date = record.stage3_date or record.stage2_date or record.stage1_date
    anchor_price = stage3_price or stage2_price or stage1_price
    if anchor_date is None or anchor_price is None:
        return replace(
            record,
            price_validation=PriceValidation(
                stage1_price=stage1_price,
                stage2_price=stage2_price,
                stage3_price=stage3_price,
                stage4b_price=stage4b_price,
                stage4c_price=stage4c_price,
                price_validation_status="needs_stage_dates",
            ),
        )

    peak_price = _peak_price_after(bars, anchor_date)
    mfe_30d, mae_30d = _mfe_mae(bars, anchor_date, anchor_price, 30)
    mfe_90d, mae_90d = _mfe_mae(bars, anchor_date, anchor_price, 90)
    mfe_180d, mae_180d = _mfe_mae(bars, anchor_date, anchor_price, 180)
    mfe_1y, mae_1y = _mfe_mae(bars, anchor_date, anchor_price, 365)
    mfe_2y, mae_2y = _mfe_mae(bars, anchor_date, anchor_price, 730)
    below_flag = _below_anchor_after(bars, anchor_date, anchor_price)
    drawdown = _drawdown_after_peak(bars, anchor_date, peak_price)
    peak_return_from_stage3 = _return_from_anchor(peak_price, stage3_price) if stage3_price else None
    time_to_50pct = _time_to_return(bars, record.stage3_date, stage3_price, 50.0)
    time_to_100pct = _time_to_return(bars, record.stage3_date, stage3_price, 100.0)
    time_to_200pct = _time_to_return(bars, record.stage3_date, stage3_price, 200.0)
    return replace(
        record,
        price_validation=PriceValidation(
            stage1_price=stage1_price,
            stage2_price=stage2_price,
            stage3_price=stage3_price,
            stage4b_price=stage4b_price,
            stage4c_price=stage4c_price,
            peak_price=peak_price,
            peak_return_from_stage3=peak_return_from_stage3,
            mfe_30d=mfe_30d,
            mfe_90d=mfe_90d,
            mfe_180d=mfe_180d,
            mfe_1y=mfe_1y,
            mfe_2y=mfe_2y,
            mae_30d=mae_30d,
            mae_90d=mae_90d,
            mae_180d=mae_180d,
            mae_1y=mae_1y,
            mae_2y=mae_2y,
            drawdown_after_peak=drawdown,
            below_stage3_price_flag=below_flag,
            time_to_50pct=time_to_50pct,
            time_to_100pct=time_to_100pct,
            time_to_200pct=time_to_200pct,
            price_validation_status="price_filled",
        ),
    )


def _load_bars(price_root: str | Path) -> dict[str, tuple[dict[str, float | date], ...]]:
    grouped: dict[str, list[dict[str, float | date]]] = {}
    for row in load_fixture_records(price_root, "prices"):
        symbol = str(row.get("symbol") or row.get("srtnCd") or "")
        if not symbol:
            continue
        bar = {
            "date": date_value(row.get("date") or row.get("basDt")),
            "close": float_or_none(row.get("close") or row.get("clpr")) or 0.0,
            "high": float_or_none(row.get("high") or row.get("hipr")) or float_or_none(row.get("close") or row.get("clpr")) or 0.0,
            "low": float_or_none(row.get("low") or row.get("lopr")) or float_or_none(row.get("close") or row.get("clpr")) or 0.0,
        }
        grouped.setdefault(symbol, []).append(bar)
    return {symbol: tuple(sorted(bars, key=lambda item: item["date"])) for symbol, bars in grouped.items()}


def _price_on_or_before(bars: tuple[dict[str, float | date], ...], stage_date: date | None) -> float | None:
    if stage_date is None:
        return None
    candidates = [bar for bar in bars if bar["date"] <= stage_date]
    if not candidates:
        return None
    return float(candidates[-1]["close"])


def _bars_after(bars: tuple[dict[str, float | date], ...], start: date, days: int | None = None) -> tuple[dict[str, float | date], ...]:
    end = start + timedelta(days=days) if days is not None else None
    return tuple(bar for bar in bars if bar["date"] >= start and (end is None or bar["date"] <= end))


def _peak_price_after(bars: tuple[dict[str, float | date], ...], start: date) -> float | None:
    future = _bars_after(bars, start)
    if not future:
        return None
    return max(float(bar["high"]) for bar in future)


def _mfe_mae(bars: tuple[dict[str, float | date], ...], start: date, anchor_price: float, days: int) -> tuple[float | None, float | None]:
    future = _bars_after(bars, start, days)
    if not future or anchor_price <= 0:
        return None, None
    high = max(float(bar["high"]) for bar in future)
    low = min(float(bar["low"]) for bar in future)
    return round((high / anchor_price - 1.0) * 100.0, 3), round((low / anchor_price - 1.0) * 100.0, 3)


def _below_anchor_after(bars: tuple[dict[str, float | date], ...], start: date, anchor_price: float) -> bool:
    return any(float(bar["low"]) < anchor_price for bar in _bars_after(bars, start))


def _return_from_anchor(price: float | None, anchor_price: float | None) -> float | None:
    if price is None or anchor_price is None or anchor_price <= 0:
        return None
    return round((price / anchor_price - 1.0) * 100.0, 3)


def _time_to_return(
    bars: tuple[dict[str, float | date], ...],
    start: date | None,
    anchor_price: float | None,
    target_pct: float,
) -> int | None:
    if start is None or anchor_price is None or anchor_price <= 0:
        return None
    target_price = anchor_price * (1.0 + target_pct / 100.0)
    for bar in _bars_after(bars, start):
        if float(bar["high"]) >= target_price:
            return (bar["date"] - start).days  # type: ignore[operator]
    return None


def _drawdown_after_peak(bars: tuple[dict[str, float | date], ...], start: date, peak_price: float | None) -> float | None:
    if peak_price is None or peak_price <= 0:
        return None
    future = _bars_after(bars, start)
    if not future:
        return None
    peak_seen = False
    lows_after_peak: list[float] = []
    for bar in future:
        if float(bar["high"]) >= peak_price:
            peak_seen = True
        if peak_seen:
            lows_after_peak.append(float(bar["low"]))
    if not lows_after_peak:
        return None
    return round((min(lows_after_peak) / peak_price - 1.0) * 100.0, 3)


def write_price_backfill_status_csv(records: Iterable[E2RCaseRecord], path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=("case_id", "symbol", "price_validation_status"))
        writer.writeheader()
        for record in records:
            writer.writerow(
                {
                    "case_id": record.case_id,
                    "symbol": record.symbol,
                    "price_validation_status": record.price_validation.price_validation_status,
                }
            )
    return target


__all__ = [
    "backfill_case_price_file",
    "backfill_case_price_paths",
    "write_price_backfill_status_csv",
]
