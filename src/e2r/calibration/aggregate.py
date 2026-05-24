"""Aggregate deduped calibration trigger rows."""

from __future__ import annotations

from collections import defaultdict
from statistics import mean, median
from typing import Any, Iterable

from .validation import FOUR_B_TYPES, FOUR_C_TYPES, POSITIVE_TRIGGER_TYPES


def _num(row: dict[str, Any], key: str) -> float | None:
    value = row.get(key)
    return value if isinstance(value, (int, float)) else None


def _mean(rows: Iterable[dict[str, Any]], key: str) -> float | None:
    values = [_num(row, key) for row in rows]
    filtered = [float(value) for value in values if value is not None]
    return round(mean(filtered), 4) if filtered else None


def _median(rows: Iterable[dict[str, Any]], key: str) -> float | None:
    values = [_num(row, key) for row in rows]
    filtered = [float(value) for value in values if value is not None]
    return round(median(filtered), 4) if filtered else None


def _rate(rows: list[dict[str, Any]], predicate) -> float | None:
    if not rows:
        return None
    return round(sum(1 for row in rows if predicate(row)) / len(rows), 4)


def _aggregate_rows(rows: list[dict[str, Any]], group_name: str, group_value: str) -> dict[str, Any]:
    positive_rows = [row for row in rows if row.get("trigger_type") in POSITIVE_TRIGGER_TYPES]
    four_b_rows = [row for row in rows if row.get("trigger_type") in FOUR_B_TYPES]
    four_c_rows = [row for row in rows if row.get("trigger_type") in FOUR_C_TYPES]
    return {
        "row_type": "aggregate_metric",
        "group_name": group_name,
        "group_value": group_value,
        "count": len(rows),
        "positive_entry_count": len(positive_rows),
        "four_b_count": len(four_b_rows),
        "four_c_count": len(four_c_rows),
        "unique_case_count": len({row.get("case_id") for row in rows if row.get("case_id")}),
        "unique_symbol_count": len({row.get("symbol") for row in rows if row.get("symbol")}),
        "unique_round_count": len({row.get("round") for row in rows if row.get("round")}),
        "avg_MFE_30D_pct": _mean(positive_rows, "MFE_30D_pct"),
        "avg_MFE_90D_pct": _mean(positive_rows, "MFE_90D_pct"),
        "avg_MFE_180D_pct": _mean(positive_rows, "MFE_180D_pct"),
        "median_MFE_90D_pct": _median(positive_rows, "MFE_90D_pct"),
        "median_MFE_180D_pct": _median(positive_rows, "MFE_180D_pct"),
        "avg_MAE_30D_pct": _mean(positive_rows, "MAE_30D_pct"),
        "avg_MAE_90D_pct": _mean(positive_rows, "MAE_90D_pct"),
        "avg_MAE_180D_pct": _mean(positive_rows, "MAE_180D_pct"),
        "median_MAE_90D_pct": _median(positive_rows, "MAE_90D_pct"),
        "median_MAE_180D_pct": _median(positive_rows, "MAE_180D_pct"),
        "hit_rate_MFE90_ge_20": _rate(positive_rows, lambda row: (row.get("MFE_90D_pct") or -999) >= 20),
        "hit_rate_MFE180_ge_30": _rate(positive_rows, lambda row: (row.get("MFE_180D_pct") or -999) >= 30),
        "drawdown_risk_rate_MAE90_le_minus_20": _rate(
            positive_rows, lambda row: (row.get("MAE_90D_pct") or 999) <= -20
        ),
        "drawdown_risk_rate_MAE180_le_minus_30": _rate(
            positive_rows, lambda row: (row.get("MAE_180D_pct") or 999) <= -30
        ),
        "positive_asymmetry_score": _positive_asymmetry_score(positive_rows),
        "avg_green_lateness_ratio": _mean(
            [row for row in positive_rows if row.get("trigger_type") == "Stage3-Green"],
            "green_lateness_ratio",
        ),
        "avg_four_b_local_peak_proximity": _mean(four_b_rows, "four_b_local_peak_proximity"),
        "avg_four_b_full_window_peak_proximity": _mean(four_b_rows, "four_b_full_window_peak_proximity"),
        "non_price_4B_count": sum(1 for row in four_b_rows if row.get("guardrail_class") == "non_price_4b"),
        "price_only_4B_count": sum(1 for row in four_b_rows if row.get("guardrail_class") == "price_only_4b_rejection"),
        "thesis_break_evidence_count": len(four_c_rows),
    }


def _positive_asymmetry_score(rows: list[dict[str, Any]]) -> float | None:
    if not rows:
        return None
    mfe = _mean(rows, "MFE_90D_pct") or 0.0
    mae = abs(_mean(rows, "MAE_90D_pct") or 0.0)
    return round(mfe - mae, 4)


def aggregate_validated_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    aggregates: list[dict[str, Any]] = [_aggregate_rows(rows, "global", "all")]
    for group_name in ("round", "sector", "sector_slug", "primary_archetype", "trigger_type", "case_type", "trigger_outcome_label"):
        grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for row in rows:
            value = row.get(group_name)
            if value:
                grouped[str(value)].append(row)
        for value, members in sorted(grouped.items()):
            aggregates.append(_aggregate_rows(members, group_name, value))
    return aggregates
