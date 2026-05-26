"""Stage-transition summaries for v12 residual calibration rows."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any
import json


STAGE_ORDER = {
    "Stage2": 2,
    "Stage2-Actionable": 2,
    "Stage3-Yellow": 3,
    "Stage3-Green": 4,
    "Stage4B": 5,
    "Stage4C": 6,
}


def _num(value: Any) -> float | None:
    if isinstance(value, (int, float)):
        return float(value)
    try:
        return float(str(value).replace(",", "").replace("%", ""))
    except (TypeError, ValueError):
        return None


def _return_pct(from_price: Any, to_price: Any) -> float | None:
    start = _num(from_price)
    end = _num(to_price)
    if start is None or end is None or start <= 0:
        return None
    return round((end / start - 1.0) * 100.0, 4)


def _best_row(rows: list[dict[str, Any]], stage_types: set[str]) -> dict[str, Any] | None:
    candidates = [row for row in rows if row.get("trigger_type") in stage_types]
    if not candidates:
        return None
    return sorted(candidates, key=lambda row: (str(row.get("entry_date") or ""), -(_num(row.get("MFE_90D_pct")) or -999)))[0]


def _peak_price(rows: list[dict[str, Any]]) -> tuple[Any, Any]:
    best_price = None
    best_date = None
    for row in rows:
        entry = _num(row.get("entry_price"))
        mfe180 = _num(row.get("MFE_180D_pct"))
        mfe90 = _num(row.get("MFE_90D_pct"))
        mfe = mfe180 if mfe180 is not None else mfe90
        if entry is None or mfe is None:
            continue
        price = entry * (1 + mfe / 100.0)
        if best_price is None or price > best_price:
            best_price = round(price, 4)
            best_date = row.get("entry_date")
    return best_price, best_date


def _transition_verdict(stage2: dict[str, Any] | None, green: dict[str, Any] | None, four_b: dict[str, Any] | None, four_c: dict[str, Any] | None) -> str:
    if four_c and str(four_c.get("v12_4c_quality")) == "late_4c":
        return "4c_too_late"
    if four_b:
        if four_b.get("v12_4b_quality") == "good_4b_timing":
            return "4b_good_peak_capture"
        if four_b.get("v12_4b_quality") == "too_early_4b":
            return "4b_too_early"
    if green:
        if green.get("current_profile_false_positive"):
            return "green_false_positive"
        if green.get("current_profile_too_late"):
            return "green_too_late"
        return "green_good_but_late"
    if stage2:
        return "stage2_actionable_best_entry" if stage2.get("trigger_type") == "Stage2-Actionable" else "stage2_captured_most_upside"
    return "no_valid_stage_transition"


def build_stage_transition_summary(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[Any, ...], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        key = (
            row.get("case_id") or row.get("symbol"),
            row.get("symbol"),
            row.get("large_sector_id"),
            row.get("canonical_archetype_id"),
        )
        grouped[key].append(row)

    summaries: list[dict[str, Any]] = []
    for (case_id, symbol, large_sector_id, canonical_archetype_id), members in sorted(grouped.items(), key=lambda item: str(item[0])):
        stage2 = _best_row(members, {"Stage2", "Stage2-Actionable"})
        yellow = _best_row(members, {"Stage3-Yellow"})
        green = _best_row(members, {"Stage3-Green"})
        four_b = _best_row(members, {"Stage4B"})
        four_c = _best_row(members, {"Stage4C"})
        peak_price, peak_date = _peak_price(members)
        stage2_price = stage2.get("entry_price") if stage2 else None
        green_price = green.get("entry_price") if green else None
        four_b_price = four_b.get("entry_price") if four_b else None
        summary = {
            "case_id": case_id,
            "symbol": symbol,
            "company_name": next((row.get("company_name") for row in members if row.get("company_name")), None),
            "large_sector_id": large_sector_id,
            "canonical_archetype_id": canonical_archetype_id,
            "stage2_trigger_id": stage2.get("trigger_id") if stage2 else None,
            "stage2_entry_date": stage2.get("entry_date") if stage2 else None,
            "stage2_entry_price": stage2_price,
            "stage3_yellow_trigger_id": yellow.get("trigger_id") if yellow else None,
            "stage3_green_trigger_id": green.get("trigger_id") if green else None,
            "stage3_green_entry_date": green.get("entry_date") if green else None,
            "stage3_green_entry_price": green_price,
            "stage4b_trigger_id": four_b.get("trigger_id") if four_b else None,
            "stage4b_entry_date": four_b.get("entry_date") if four_b else None,
            "stage4b_entry_price": four_b_price,
            "stage4c_trigger_id": four_c.get("trigger_id") if four_c else None,
            "stage4c_entry_date": four_c.get("entry_date") if four_c else None,
            "peak_price": peak_price,
            "peak_date": peak_date,
            "stage2_to_green_return_pct": _return_pct(stage2_price, green_price),
            "stage2_to_4b_return_pct": _return_pct(stage2_price, four_b_price),
            "stage2_to_peak_return_pct": _return_pct(stage2_price, peak_price),
            "green_to_peak_remaining_upside_pct": _return_pct(green_price, peak_price),
            "stage4b_peak_capture_pct": _return_pct(stage2_price, four_b_price),
            "peak_to_4c_drawdown_pct": _return_pct(peak_price, four_c.get("entry_price") if four_c else None),
            "transition_verdict": _transition_verdict(stage2, green, four_b, four_c),
        }
        summaries.append(summary)
    return summaries


def write_stage_transition_outputs(
    rows: list[dict[str, Any]],
    *,
    data_directory: str | Path,
    report_directory: str | Path,
) -> dict[str, Path]:
    data_dir = Path(data_directory)
    report_dir = Path(report_directory)
    by_arch_dir = report_dir / "by_archetype_stage_transition"
    data_dir.mkdir(parents=True, exist_ok=True)
    report_dir.mkdir(parents=True, exist_ok=True)
    by_arch_dir.mkdir(parents=True, exist_ok=True)
    summaries = build_stage_transition_summary(rows)
    summary_path = data_dir / "stage_transition_summary.jsonl"
    with summary_path.open("w", encoding="utf-8") as handle:
        for row in summaries:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True, allow_nan=False) + "\n")
    report_path = report_dir / "stage_transition_report.md"
    report_path.write_text(render_stage_transition_report(summaries), encoding="utf-8")
    paths = {"stage_transition_summary": summary_path, "stage_transition_report": report_path}
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in summaries:
        grouped[str(row.get("canonical_archetype_id") or "unknown")].append(row)
    for archetype, members in grouped.items():
        path = by_arch_dir / f"{archetype}.md"
        path.write_text(render_stage_transition_report(members, title=f"{archetype} Stage Transition Report"), encoding="utf-8")
        paths[f"by_archetype_{archetype}"] = path
    return paths


def render_stage_transition_report(rows: list[dict[str, Any]], title: str = "V12 Stage Transition Report") -> str:
    lines = [
        f"# {title}",
        "",
        f"- stage_transition_summary_rows: `{len(rows)}`",
        "",
        "| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | verdict |",
        "|---|---|---|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            "| {case_id} | {symbol} | {arch} | {s2} | {green} | {b4} | {peak} | {verdict} |".format(
                case_id=row.get("case_id"),
                symbol=row.get("symbol"),
                arch=row.get("canonical_archetype_id"),
                s2=row.get("stage2_entry_price"),
                green=row.get("stage3_green_entry_price"),
                b4=row.get("stage4b_entry_price"),
                peak=row.get("stage2_to_peak_return_pct"),
                verdict=row.get("transition_verdict"),
            )
        )
    return "\n".join(lines) + "\n"
