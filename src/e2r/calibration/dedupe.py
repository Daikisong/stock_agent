"""Deduplication for repeated historical calibration loops."""

from __future__ import annotations

from collections import defaultdict
from typing import Any


def _rounded_price(value: Any) -> str:
    try:
        return str(round(float(value), 2))
    except (TypeError, ValueError):
        return str(value or "")


def _hashable_key_value(value: Any) -> Any:
    if isinstance(value, list):
        items = tuple(_hashable_key_value(item) for item in value)
        return tuple(sorted(items, key=repr))
    if isinstance(value, dict):
        return tuple((key, _hashable_key_value(item)) for key, item in sorted(value.items()))
    return value


def _dedupe_key(row: dict[str, Any]) -> tuple[Any, ...]:
    same_entry_group_id = row.get("same_entry_group_id")
    if same_entry_group_id:
        return ("same_entry_group_id", same_entry_group_id)
    return (
        "fallback",
        row.get("round"),
        row.get("sector_slug") or row.get("sector"),
        row.get("symbol"),
        row.get("primary_archetype"),
        row.get("trigger_type"),
        row.get("trigger_date"),
        row.get("entry_date"),
        _rounded_price(row.get("entry_price")),
        str(row.get("company_name") or row.get("company") or "").strip().lower(),
    )


def _completeness_score(row: dict[str, Any]) -> int:
    keys = (
        "MFE_30D_pct",
        "MFE_90D_pct",
        "MFE_180D_pct",
        "MAE_30D_pct",
        "MAE_90D_pct",
        "MAE_180D_pct",
        "raw_component_scores_before",
        "raw_component_scores_after",
        "same_entry_group_id",
    )
    return sum(1 for key in keys if row.get(key) not in (None, "", "unavailable", "not_applicable"))


def _parse_loop(row: dict[str, Any]) -> int:
    try:
        return int(str(row.get("loop") or "0").strip())
    except ValueError:
        return 0


def _representative_sort_key(row: dict[str, Any]) -> tuple[int, int, int, int]:
    method_score = 3 if row.get("parse_method") == "jsonl" else 2 if "fence" in str(row.get("parse_method")) else 1
    explicit_dedupe = 1 if row.get("dedupe_for_aggregate") is True else 0
    return (method_score, explicit_dedupe, _completeness_score(row), _parse_loop(row))


def dedupe_trigger_rows(rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    grouped: dict[tuple[Any, ...], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[_dedupe_key(row)].append(row)

    representatives: list[dict[str, Any]] = []
    dedupe_map: list[dict[str, Any]] = []
    for key, members in sorted(grouped.items(), key=lambda item: str(item[0])):
        representative = sorted(members, key=_representative_sort_key, reverse=True)[0]
        representative = dict(representative)
        representative["dedupe_key"] = "|".join(str(part) for part in key)
        representative["dedupe_member_count"] = len(members)
        representative["is_aggregate_representative"] = True
        representatives.append(representative)
        rep_id = representative.get("trigger_id")
        for member in members:
            dedupe_map.append(
                {
                    "dedupe_key": representative["dedupe_key"],
                    "trigger_id": member.get("trigger_id"),
                    "source_file": member.get("source_file"),
                    "selected_representative_trigger_id": rep_id,
                    "duplicate_reason": "same_entry_group_id" if key[0] == "same_entry_group_id" else "fallback_trigger_key",
                    "is_representative": member is representative or member.get("trigger_id") == rep_id,
                }
            )
    return representatives, dedupe_map


def _v12_dedupe_key(row: dict[str, Any]) -> tuple[Any, ...]:
    evidence_family = row.get("evidence_family") or row.get("trigger_family") or row.get("fine_archetype_id")
    return (
        "v12_strict",
        row.get("symbol"),
        row.get("canonical_archetype_id"),
        row.get("trigger_type"),
        row.get("trigger_date"),
        row.get("entry_date"),
        _rounded_price(row.get("entry_price")),
        _hashable_key_value(evidence_family),
    )


def dedupe_v12_trigger_rows(rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Dedupe v12 rows without collapsing new symbols inside the same archetype.

    v12 is meant to add more symbols to the same canonical archetype. Therefore
    the strict key includes the symbol; only same-symbol/same-entry repeats are
    collapsed.
    """

    grouped: dict[tuple[Any, ...], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[_v12_dedupe_key(row)].append(row)

    representatives: list[dict[str, Any]] = []
    dedupe_map: list[dict[str, Any]] = []
    for key, members in sorted(grouped.items(), key=lambda item: str(item[0])):
        representative = sorted(members, key=_representative_sort_key, reverse=True)[0]
        representative = dict(representative)
        representative["dedupe_key"] = "|".join(str(part) for part in key)
        representative["dedupe_member_count"] = len(members)
        representative["is_aggregate_representative"] = True
        representatives.append(representative)
        rep_id = representative.get("trigger_id")
        for member in members:
            same_symbol_reuse = (
                member.get("symbol") == representative.get("symbol")
                and member.get("canonical_archetype_id") == representative.get("canonical_archetype_id")
            )
            dedupe_map.append(
                {
                    "dedupe_key": representative["dedupe_key"],
                    "trigger_id": member.get("trigger_id"),
                    "source_file": member.get("source_file"),
                    "selected_representative_trigger_id": rep_id,
                    "duplicate_reason": "same_symbol_same_trigger_entry" if same_symbol_reuse else "v12_independent_symbol",
                    "is_representative": member.get("trigger_id") == rep_id,
                }
            )
    return representatives, dedupe_map
