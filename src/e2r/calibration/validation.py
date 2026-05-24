"""Validation rules for extracted calibration rows."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
import math
import re


POSITIVE_TRIGGER_TYPES = {"Stage2", "Stage2-Actionable", "Stage3-Yellow", "Stage3-Green"}
FOUR_B_TYPES = {"Stage4B", "4B", "4B-watch", "Stage4B-watch"}
FOUR_C_TYPES = {"Stage4C", "4C", "Stage4C-hard", "hard_4C"}

UNAVAILABLE_MARKERS = {
    "",
    "unavailable",
    "n/a",
    "na",
    "none",
    "null",
    "not_applicable",
    "unavailable_not_needed_for_delta",
    "insufficient_forward_window_in_stock_web",
    "contaminated_or_unavailable",
}


@dataclass(frozen=True)
class ValidationBundle:
    valid_rows: list[dict[str, Any]]
    rejected_rows: list[dict[str, Any]]


def parse_number(value: Any) -> float | None:
    if value is None:
        return None
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        if isinstance(value, float) and (math.isnan(value) or math.isinf(value)):
            return None
        return float(value)
    text = str(value).strip().strip('"').strip("'")
    if text.lower() in UNAVAILABLE_MARKERS:
        return None
    text = text.replace("%", "").replace(",", "")
    match = re.search(r"[-+]?\d+(?:\.\d+)?", text)
    if not match:
        return None
    try:
        return float(match.group(0))
    except ValueError:
        return None


def parse_bool(value: Any, default: bool | None = None) -> bool | None:
    if isinstance(value, bool):
        return value
    if value is None:
        return default
    text = str(value).strip().lower()
    if text in {"true", "yes", "y", "1", "pass"}:
        return True
    if text in {"false", "no", "n", "0", "fail"}:
        return False
    return default


def normalise_trigger_type(value: Any) -> str:
    text = str(value or "").strip()
    aliases = {
        "Stage1/weak watch": "Stage1",
        "4B / false-positive guardrail": "Stage4B",
        "Stage4B-watch": "Stage4B",
        "4B-watch": "Stage4B",
        "Stage4B": "Stage4B",
        "Stage4C": "Stage4C",
        "Stage3_Yellow": "Stage3-Yellow",
        "Stage3_Green": "Stage3-Green",
    }
    return aliases.get(text, text)


def _contains_any(row: dict[str, Any], terms: tuple[str, ...]) -> bool:
    haystack = " ".join(str(value) for value in row.values()).lower()
    return any(term in haystack for term in terms)


def _price_source_valid(row: dict[str, Any]) -> bool:
    source = row.get("price_data_source") or row.get("price_source") or row.get("source")
    return source == "Songdaiki/stock-web"


def _price_basis_valid(row: dict[str, Any]) -> bool:
    return row.get("price_basis") == "tradable_raw"


def _adjustment_valid(row: dict[str, Any]) -> bool:
    return row.get("price_adjustment_status") == "raw_unadjusted_marcap"


def _has_required_mfe_mae(row: dict[str, Any]) -> bool:
    return all(
        parse_number(row.get(key)) is not None
        for key in (
            "MFE_30D_pct",
            "MFE_90D_pct",
            "MFE_180D_pct",
            "MAE_30D_pct",
            "MAE_90D_pct",
            "MAE_180D_pct",
        )
    )


def _has_forward_window(row: dict[str, Any]) -> bool:
    value = parse_number(row.get("forward_window_trading_days"))
    return value is None or value >= 180


def _is_corporate_action_contaminated(row: dict[str, Any]) -> bool:
    text = " ".join(str(row.get(key, "")) for key in ("corporate_action_window_status", "calibration_block_reasons"))
    return "contaminated" in text.lower() and "no_overlap" not in text.lower() and "clean" not in text.lower()


def _non_price_evidence(row: dict[str, Any]) -> bool:
    if _contains_any(row, ("price_only_no_evidence", "price-only no evidence", "price_only_local", "price-only local")):
        return False
    evidence_source = str(row.get("evidence_source") or row.get("evidence_available_at_that_date") or "")
    if evidence_source and evidence_source.lower().strip() in {"price", "price_only", "relative strength only"}:
        return False
    return True


def validate_trigger_rows(trigger_rows: list[dict[str, Any]]) -> ValidationBundle:
    valid_rows: list[dict[str, Any]] = []
    rejected_rows: list[dict[str, Any]] = []
    for row in trigger_rows:
        validated = dict(row)
        reasons: list[str] = []
        trigger_type = normalise_trigger_type(validated.get("trigger_type"))
        validated["trigger_type"] = trigger_type

        if not _price_source_valid(validated):
            reasons.append("invalid_price_source")
        if not _price_basis_valid(validated):
            reasons.append("raw_all_basis" if validated.get("price_basis") else "missing_price_basis")
        if not _adjustment_valid(validated):
            reasons.append("invalid_price_adjustment_status")
        if parse_number(validated.get("entry_price")) is None or (parse_number(validated.get("entry_price")) or 0) <= 0:
            reasons.append("missing_entry_price")
        if not validated.get("entry_date"):
            reasons.append("missing_entry_date")
        if not _has_required_mfe_mae(validated):
            reasons.append("missing_required_mfe_mae")
        if not _has_forward_window(validated):
            reasons.append("insufficient_forward_window")
        if _is_corporate_action_contaminated(validated):
            reasons.append("corporate_action_contaminated")

        price_path_valid = not reasons
        calibration_usable = parse_bool(validated.get("calibration_usable"), True)
        representative = str(validated.get("aggregate_group_role") or "representative").lower() == "representative"
        dedupe_for_aggregate = parse_bool(validated.get("dedupe_for_aggregate"), True)
        is_positive = trigger_type in POSITIVE_TRIGGER_TYPES
        is_4b = trigger_type in FOUR_B_TYPES
        is_4c = trigger_type in FOUR_C_TYPES
        non_price = _non_price_evidence(validated)

        usable_for_weight = (
            price_path_valid
            and bool(calibration_usable)
            and bool(representative)
            and bool(dedupe_for_aggregate)
            and is_positive
            and non_price
            and not _contains_any(
                validated,
                (
                    "narrative_only",
                    "label_comparison_only",
                    "4b_overlay_only",
                    "4c_overlay_only",
                    "price_only_no_evidence_run",
                    "blocked_by_corporate_action",
                ),
            )
        )

        guardrail_usable = price_path_valid and bool(calibration_usable) and (is_4b or is_4c)
        if is_4b and not non_price:
            validated["guardrail_class"] = "price_only_4b_rejection"
        elif is_4b:
            validated["guardrail_class"] = "non_price_4b"
        elif is_4c:
            validated["guardrail_class"] = "hard_4c"

        if is_positive and not non_price:
            reasons.append("price_only_no_evidence")
        if is_positive and _contains_any(validated, ("false_positive_score",)):
            reasons.append("false_positive_not_positive_promotion")
        if not representative:
            reasons.append("not_representative_for_aggregate")
        if dedupe_for_aggregate is False:
            reasons.append("not_representative_for_aggregate")

        validated["price_path_valid"] = price_path_valid
        validated["usable_for_weight_calibration"] = usable_for_weight
        validated["guardrail_usable"] = guardrail_usable
        validated["validation_reasons"] = reasons

        for numeric_key in (
            "entry_price",
            "MFE_30D_pct",
            "MFE_90D_pct",
            "MFE_180D_pct",
            "MAE_30D_pct",
            "MAE_90D_pct",
            "MAE_180D_pct",
            "green_lateness_ratio",
            "four_b_peak_proximity",
            "four_b_local_peak_proximity",
            "four_b_full_window_peak_proximity",
        ):
            if numeric_key in validated:
                parsed = parse_number(validated.get(numeric_key))
                if parsed is not None:
                    validated[numeric_key] = parsed

        if price_path_valid:
            valid_rows.append(validated)
        else:
            rejected = dict(validated)
            rejected["rejection_reasons"] = reasons
            rejected_rows.append(rejected)

        if price_path_valid and not (usable_for_weight or guardrail_usable):
            rejected = dict(validated)
            rejected["rejection_reasons"] = reasons or ["not_usable_for_promotion"]
            rejected_rows.append(rejected)

    return ValidationBundle(valid_rows=valid_rows, rejected_rows=rejected_rows)
