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
        "Stage1/weak-watch": "Stage1",
        "4B / false-positive guardrail": "Stage4B",
        "4B_false_positive_guardrail": "Stage4B",
        "Stage4B-watch": "Stage4B",
        "Stage4B local overlay": "Stage4B",
        "Stage4B full-window overlay": "Stage4B",
        "price-only-local-4B-overlay": "Stage4B",
        "price-only local 4B overlay": "Stage4B",
        "4B-watch": "Stage4B",
        "Stage4B": "Stage4B",
        "Stage4C": "Stage4C",
        "Stage4C protection watch": "Stage4C",
        "Stage3_Yellow": "Stage3-Yellow",
        "Stage3_Green": "Stage3-Green",
        "Stage3-Green comparison": "Stage3-Green",
        "Stage3-Green compare": "Stage3-Green",
        "Stage2 policy-only stress": "Stage2",
        "price-only-theme-breakout": "price_only_theme_breakout_guardrail",
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


def _v12_bool_flag(row: dict[str, Any], key: str) -> bool:
    parsed = parse_bool(row.get(key), None)
    if parsed is not None:
        return parsed
    return _contains_any(row, (key.replace("_", " "), key))


def _v12_non_price_evidence(row: dict[str, Any]) -> bool:
    if not _non_price_evidence(row):
        return False
    trigger_text = str(row.get("trigger_type") or "").lower()
    if "price_only" in trigger_text or "price-only" in trigger_text:
        return False
    return True


def _classify_stage2_quality(row: dict[str, Any]) -> str | None:
    if row.get("trigger_type") not in {"Stage2", "Stage2-Actionable"}:
        return None
    mfe90 = parse_number(row.get("MFE_90D_pct"))
    mfe180 = parse_number(row.get("MFE_180D_pct"))
    mae90 = parse_number(row.get("MAE_90D_pct"))
    label = " ".join(str(row.get(key, "")) for key in ("trigger_outcome_label", "current_profile_verdict")).lower()
    non_price = _v12_non_price_evidence(row)
    if (
        ((mfe90 is not None and mfe90 >= 20) or (mfe180 is not None and mfe180 >= 30))
        and (mae90 is None or mae90 > -25 or "high_mae_success" in label)
        and non_price
    ):
        return "good_stage2"
    if (
        (mfe90 is not None and mfe90 < 10)
        or (mae90 is not None and mae90 <= -25)
        or any(term in label for term in ("failed", "false_positive", "watch_only", "high_mae", "evidence_good_but_price_failed"))
    ):
        return "bad_stage2"
    return "neutral_stage2"


def _classify_4b_quality(row: dict[str, Any]) -> str | None:
    if row.get("trigger_type") not in FOUR_B_TYPES:
        return None
    label = " ".join(str(row.get(key, "")) for key in ("trigger_outcome_label", "current_profile_verdict")).lower()
    local = parse_number(row.get("four_b_local_peak_proximity"))
    full = parse_number(row.get("four_b_full_window_peak_proximity"))
    proximity = full if full is not None else local
    if not _v12_non_price_evidence(row):
        return "price_only_4b"
    if (proximity is not None and 0.7 <= proximity <= 1.1) or any(
        term in label for term in ("good_4b_timing", "4b_overlay_success")
    ):
        return "good_4b_timing"
    if (proximity is not None and proximity < 0.5) or any(term in label for term in ("too_early", "price_only_local_4b_too_early")):
        return "too_early_4b"
    if "too_late" in label:
        return "too_late_4b"
    return "neutral_4b"


def _classify_4c_quality(row: dict[str, Any]) -> str | None:
    if row.get("trigger_type") not in FOUR_C_TYPES:
        return None
    label = " ".join(str(row.get(key, "")) for key in ("trigger_outcome_label", "current_profile_verdict")).lower()
    if "current_profile_4c_too_late" in label or "thesis_break_late" in label or "4c_late" in label:
        return "late_4c"
    if "hard_4c" in label or "4c_success" in label:
        return "hard_4c"
    return "watch_only_4c"


def validate_v12_trigger_rows(trigger_rows: list[dict[str, Any]]) -> ValidationBundle:
    """Validate v12 residual rows for shadow calibration, not default promotion."""

    base = validate_trigger_rows(trigger_rows)
    valid_rows: list[dict[str, Any]] = []
    rejected_rows: list[dict[str, Any]] = list(base.rejected_rows)

    for row in base.valid_rows:
        validated = dict(row)
        reasons = list(validated.get("validation_reasons", []))
        validated["schema_family"] = validated.get("schema_family") or "v12_sector_archetype_residual"
        large_sector_id = validated.get("large_sector_id")
        canonical_archetype_id = validated.get("canonical_archetype_id")
        if not large_sector_id:
            reasons.append("missing_large_sector_id")
        if not canonical_archetype_id:
            reasons.append("missing_canonical_archetype_id")

        evidence_url_pending = _v12_bool_flag(validated, "evidence_url_pending") or _contains_any(
            validated, ("evidence url pending", "url pending")
        )
        source_proxy_only = _v12_bool_flag(validated, "source_proxy_only") or _contains_any(
            validated, ("source-name-level", "event proxies", "public-event proxies")
        )
        duplicate_low_value = _contains_any(validated, ("duplicate_low_value_loop",))
        rematerialization = _contains_any(validated, ("schema_rematerialization_only",))
        do_not_count = parse_bool(validated.get("do_not_count_as_new_case"), False) is True
        independent_weight_zero = parse_number(validated.get("independent_evidence_weight")) == 0

        trigger_type = validated.get("trigger_type")
        is_positive = trigger_type in POSITIVE_TRIGGER_TYPES
        is_4b_or_4c = trigger_type in FOUR_B_TYPES or trigger_type in FOUR_C_TYPES
        is_price_only_theme_guard = trigger_type == "price_only_theme_breakout_guardrail"
        non_price = _v12_non_price_evidence(validated)

        validated["evidence_url_pending"] = evidence_url_pending
        validated["source_proxy_only"] = source_proxy_only
        validated["usable_for_global_promotion"] = False
        validated["usable_for_v12_shadow_calibration"] = bool(large_sector_id) and bool(canonical_archetype_id)
        validated["usable_for_sector_shadow"] = bool(large_sector_id) and not duplicate_low_value and not rematerialization
        validated["usable_for_archetype_shadow"] = bool(canonical_archetype_id) and not duplicate_low_value and not rematerialization
        validated["usable_for_new_weight_evidence"] = (
            validated["usable_for_v12_shadow_calibration"]
            and not duplicate_low_value
            and not rematerialization
            and not do_not_count
            and not independent_weight_zero
            and not is_4b_or_4c
            and not is_price_only_theme_guard
            and is_positive
            and non_price
        )
        validated["residual_counterexample"] = str(validated.get("positive_or_counterexample", "")).lower() == "counterexample"
        verdict_text = str(validated.get("current_profile_verdict") or "").lower()
        outcome_text = str(validated.get("trigger_outcome_label") or "").lower()
        combined_text = f"{verdict_text} {outcome_text}"
        validated["current_profile_error"] = "current_profile_" in combined_text and "correct" not in combined_text
        validated["current_profile_false_positive"] = "false_positive" in combined_text
        validated["current_profile_missed_structural"] = "missed_structural" in combined_text
        validated["current_profile_too_late"] = "too_late" in combined_text or "late_green" in combined_text
        validated["current_profile_4B_too_early"] = "4b_too_early" in combined_text
        validated["current_profile_4C_too_late"] = "4c_too_late" in combined_text
        validated["v12_stage2_quality"] = _classify_stage2_quality(validated)
        validated["v12_4b_quality"] = _classify_4b_quality(validated)
        validated["v12_4c_quality"] = _classify_4c_quality(validated)
        validated["validation_reasons"] = reasons

        for numeric_key in (
            "new_independent_case_count",
            "reused_case_count",
            "same_archetype_new_symbol_count",
            "same_archetype_new_trigger_family_count",
            "positive_case_count",
            "counterexample_count",
            "4B_case_count",
            "4C_case_count",
            "four_b_local_peak_proximity",
            "four_b_full_window_peak_proximity",
        ):
            if numeric_key in validated:
                parsed = parse_number(validated.get(numeric_key))
                if parsed is not None:
                    validated[numeric_key] = parsed

        if large_sector_id and canonical_archetype_id:
            valid_rows.append(validated)
        else:
            rejected = dict(validated)
            rejected["rejection_reasons"] = reasons or ["not_usable_for_v12_shadow_calibration"]
            rejected_rows.append(rejected)

    return ValidationBundle(valid_rows=valid_rows, rejected_rows=rejected_rows)
