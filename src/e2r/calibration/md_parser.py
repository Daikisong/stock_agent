"""Parsers for generated Stock-Web historical calibration Markdown files."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv
import io
import json
import re
from typing import Any

from .evidence_flags import normalise_evidence_quality_flags, text_has_evidence_url_pending
from .md_discovery import MarkdownDocument
from .taxonomy import normalise_canonical_archetype_id, normalise_large_sector_id


COLUMN_ALIASES = {
    "MFE30": "MFE_30D_pct",
    "MFE_30D": "MFE_30D_pct",
    "MFE_30D_pct": "MFE_30D_pct",
    "MFE90": "MFE_90D_pct",
    "MFE_90D": "MFE_90D_pct",
    "MFE_90D_pct": "MFE_90D_pct",
    "MFE180": "MFE_180D_pct",
    "MFE_180D": "MFE_180D_pct",
    "MFE_180D_pct": "MFE_180D_pct",
    "mfe_30_pct": "MFE_30D_pct",
    "mfe_30d_pct": "MFE_30D_pct",
    "mfe_90_pct": "MFE_90D_pct",
    "mfe_90d_pct": "MFE_90D_pct",
    "mfe_180_pct": "MFE_180D_pct",
    "mfe_180d_pct": "MFE_180D_pct",
    "mfe_pct": "MFE_180D_pct",
    "MAE30": "MAE_30D_pct",
    "MAE_30D": "MAE_30D_pct",
    "MAE_30D_pct": "MAE_30D_pct",
    "MAE90": "MAE_90D_pct",
    "MAE_90D": "MAE_90D_pct",
    "MAE_90D_pct": "MAE_90D_pct",
    "MAE180": "MAE_180D_pct",
    "MAE_180D": "MAE_180D_pct",
    "MAE_180D_pct": "MAE_180D_pct",
    "mae_30_pct": "MAE_30D_pct",
    "mae_30d_pct": "MAE_30D_pct",
    "mae_90_pct": "MAE_90D_pct",
    "mae_90d_pct": "MAE_90D_pct",
    "mae_180_pct": "MAE_180D_pct",
    "mae_180d_pct": "MAE_180D_pct",
    "mae_pct": "MAE_180D_pct",
    "type": "trigger_type",
    "trigger": "trigger_id",
    "entry": "entry_date",
    "price": "entry_price",
    "entry_close": "entry_price",
    "entry close": "entry_price",
    "entry_close_price": "entry_price",
    "ticker": "symbol",
    "name": "company_name",
    "review_id": "trigger_id",
    "research_id": "trigger_id",
    "original_trigger_type": "trigger_family",
    "current": "current_profile_verdict",
    "outcome": "trigger_outcome_label",
    "verdict": "trigger_outcome_label",
    "role": "case_type",
    "fine": "fine_archetype_id",
    "evidence family": "evidence_family",
    "validation status": "validation_status",
    "positive / counterexample": "positive_or_counterexample",
    "positive_or_counterexample": "positive_or_counterexample",
    "4b_case_count": "4B_case_count",
    "4c_case_count": "4C_case_count",
    "dedupe": "dedupe_for_aggregate",
    "dedupe_for_aggregate": "dedupe_for_aggregate",
    "agg_role": "aggregate_group_role",
    "aggregate_role": "aggregate_group_role",
    "group_role": "aggregate_group_role",
    "selected_round": "round",
    "tradable_shard_path": "price_shard_path",
}

ROW_TYPES = {
    "price_source_validation",
    "case",
    "trigger",
    "score_simulation",
    "profile_comparison",
    "shadow_weight",
    "optimization_decision",
    "aggregate_metric",
    "narrative_only",
    "residual_contribution",
    "stage_transition_summary",
    "coverage_matrix",
    "sector_rule_candidate",
    "canonical_archetype_rule_candidate",
}

ROW_TYPE_ALIASES = {
    "aggregate": "aggregate_metric",
    "r13_cross_case": "trigger",
    "r13_review_trigger": "trigger",
    "cross_review_trigger": "trigger",
    "review_case": "trigger",
    "trigger_case": "trigger",
    "r13_cross_summary": "residual_contribution",
    "r13_cross_archetype_rule_candidate": "canonical_archetype_rule_candidate",
    "r13_guardrail_candidate": "shadow_weight",
    "shadow_rule_candidate": "shadow_weight",
}

FENCE_RE = re.compile(r"```(?P<lang>[A-Za-z0-9_-]*)\n(?P<body>.*?)```", re.DOTALL)


@dataclass(frozen=True)
class ParsedMarkdown:
    registry_row: dict[str, Any]
    rows_by_type: dict[str, list[dict[str, Any]]]
    failed: bool = False
    failure_reason: str | None = None


def _normalise_key(key: str) -> str:
    stripped = key.strip().strip("`")
    if stripped in COLUMN_ALIASES:
        return COLUMN_ALIASES[stripped]
    for alias_key, alias_value in COLUMN_ALIASES.items():
        if stripped.lower() == alias_key.lower():
            return alias_value
    lowered = re.sub(r"[^0-9A-Za-z가-힣_]+", "_", stripped.strip().lower()).strip("_")
    return COLUMN_ALIASES.get(lowered, lowered or stripped)


def _normalise_row_type(value: Any) -> str:
    row_type = str(value or "").strip()
    return ROW_TYPE_ALIASES.get(row_type, ROW_TYPE_ALIASES.get(row_type.lower(), row_type))


def _normalise_value(value: Any) -> Any:
    if isinstance(value, str):
        stripped = value.strip()
        if stripped.lower() in {"true", "false"}:
            return stripped.lower() == "true"
        return stripped
    return value


def _text_has_any(text: str, terms: tuple[str, ...]) -> bool:
    return any(term in text for term in terms)


def _canonical_stage_trigger_type(value: Any) -> str | None:
    text = str(value or "").strip()
    if not text:
        return None
    if text.startswith("Stage2-Actionable") or text == "S2A":
        return "Stage2-Actionable"
    if text.startswith("Stage3-Yellow"):
        return "Stage3-Yellow"
    if text.startswith("Stage3-Green"):
        return "Stage3-Green"
    if text.startswith("Stage4B") or text.startswith("4B"):
        return "Stage4B"
    if text.startswith("Stage4C") or text.startswith("4C"):
        return "Stage4C"
    if text.startswith("Stage2"):
        return "Stage2"
    return None


def _derive_v12_compact_semantics(normalised: dict[str, Any]) -> None:
    """Preserve compact v12 research rows as stage-aware trigger rows.

    Some recent research files emitted calibration rows as ``case`` /
    ``trigger_case`` / ``review_case`` instead of canonical ``trigger`` rows.
    These rows still carry entry date, price path and classification. We map
    only the stage bucket needed for calibration and keep the original label in
    ``trigger_family`` so runtime scoring never depends on stock names.
    """

    if normalised.get("row_type") != "trigger":
        return
    source_row_type = str(normalised.get("source_row_type") or "").strip()
    v12_source_types = {
        "v12_compact_case",
        "trigger_case",
        "cross_review_trigger",
        "review_case",
        "r13_cross_case",
        "r13_review_trigger",
    }
    label_fields = (
        "classification",
        "path_label",
        "r13_route",
        "polarity",
        "bridge_status",
        "r13_verdict",
        "stage_judgment",
        "score_alignment",
        "trigger_outcome_label",
        "current_profile_verdict",
        "trigger_type",
        "trigger_family",
    )
    label_text = " ".join(str(normalised.get(key) or "") for key in label_fields).lower()
    if source_row_type not in v12_source_types and not any(
        normalised.get(key) not in (None, "") for key in ("classification", "path_label", "r13_route", "polarity")
    ):
        return

    original_trigger = normalised.get("trigger_type") or normalised.get("trigger_family")
    if original_trigger and not normalised.get("trigger_family"):
        normalised["trigger_family"] = original_trigger

    if not normalised.get("trigger_id"):
        trigger_parts = [
            normalised.get("case_id"),
            normalised.get("symbol"),
            normalised.get("entry_date"),
            normalised.get("trigger_family") or normalised.get("classification") or normalised.get("r13_route"),
        ]
        suffix = "_".join(str(part).strip().replace(" ", "_") for part in trigger_parts if part not in (None, ""))
        normalised["trigger_id"] = f"V12_COMPACT_{suffix}" if suffix else "V12_COMPACT_TRIGGER"
    if not normalised.get("trigger_date") and normalised.get("entry_date"):
        normalised["trigger_date"] = normalised.get("entry_date")
    if not normalised.get("evidence_source"):
        normalised["evidence_source"] = (
            normalised.get("evidence_summary")
            or normalised.get("evidence_family")
            or normalised.get("classification")
            or normalised.get("r13_route")
            or normalised.get("trigger_family")
        )
    if not normalised.get("trigger_outcome_label"):
        normalised["trigger_outcome_label"] = (
            normalised.get("classification")
            or normalised.get("path_label")
            or normalised.get("r13_route")
            or normalised.get("polarity")
        )

    hard_4c = _text_has_any(label_text, ("hard_4c", "4c_candidate", "route_to_4c", "thesis_break"))
    negative = hard_4c or _text_has_any(
        label_text,
        (
            "counterexample",
            "false_positive",
            "failed",
            "failure",
            "high_mae",
            "weak_bridge",
            "bridge_missing",
            "without_",
            "without ",
            "no_bridge",
            "blocked",
            "not_green",
            "green_blocked",
        ),
    )
    positive = (
        str(normalised.get("polarity") or "").lower() in {"positive", "positive_control"}
        or _text_has_any(label_text, ("positive_with", "local_positive", "positive_control", "approved", "bridge_present"))
    ) and not negative

    if not normalised.get("positive_or_counterexample"):
        normalised["positive_or_counterexample"] = "counterexample" if negative else "positive" if positive else "counterexample"
    if not normalised.get("case_type"):
        if hard_4c:
            normalised["case_type"] = "4c_thesis_break"
        elif normalised["positive_or_counterexample"] == "positive":
            normalised["case_type"] = "structural_success"
        else:
            normalised["case_type"] = "failed_rerating"
    if not normalised.get("current_profile_verdict"):
        normalised["current_profile_verdict"] = (
            "current_profile_correct" if normalised["positive_or_counterexample"] == "positive" else "current_profile_false_positive"
        )

    canonical_stage = _canonical_stage_trigger_type(normalised.get("trigger_type"))
    if canonical_stage is None:
        if hard_4c:
            canonical_stage = "Stage4C"
        elif normalised["positive_or_counterexample"] == "positive":
            canonical_stage = "Stage2-Actionable"
        else:
            canonical_stage = "Stage2"
    normalised["trigger_type"] = canonical_stage


def _normalise_row(row: dict[str, Any]) -> dict[str, Any]:
    normalised: dict[str, Any] = {}
    for key, value in row.items():
        if key is None:
            continue
        if isinstance(value, str) and key.startswith("_"):
            normalised[key] = value
            continue
        normalised[_normalise_key(str(key))] = _normalise_value(value)
    original_row_type = str(normalised.get("row_type") or "").strip()
    row_type = _normalise_row_type(original_row_type)
    if row_type:
        normalised["row_type"] = row_type
    if original_row_type and row_type != original_row_type:
        normalised["source_row_type"] = original_row_type
    if original_row_type in {"r13_cross_case", "r13_review_trigger", "cross_review_trigger", "review_case", "trigger_case"}:
        if not normalised.get("round") and normalised.get("source_round"):
            normalised["round"] = normalised.get("source_round")
        if not normalised.get("loop") and normalised.get("source_loop"):
            normalised["loop"] = normalised.get("source_loop")
        if not normalised.get("round") and normalised.get("scheduled_round"):
            normalised["round"] = normalised.get("scheduled_round")
        if not normalised.get("loop") and normalised.get("scheduled_loop"):
            normalised["loop"] = normalised.get("scheduled_loop")
        if not normalised.get("large_sector_id") and normalised.get("original_large_sector_id"):
            normalised["large_sector_id"] = normalised.get("original_large_sector_id")
        if not normalised.get("canonical_archetype_id") and normalised.get("original_canonical_archetype_id"):
            normalised["canonical_archetype_id"] = normalised.get("original_canonical_archetype_id")
        if not normalised.get("trigger_id"):
            if normalised.get("source_trigger_id"):
                normalised["trigger_id"] = normalised.get("source_trigger_id")
            else:
                trigger_parts = [
                    normalised.get("case_id"),
                    normalised.get("symbol"),
                    normalised.get("entry_date"),
                    normalised.get("trigger_type"),
                ]
                trigger_suffix = "_".join(str(part).strip().replace(" ", "_") for part in trigger_parts if part not in (None, ""))
                normalised["trigger_id"] = f"R13_CROSS_{trigger_suffix}" if trigger_suffix else "R13_REVIEW_TRIGGER"
        if original_row_type in {"r13_cross_case", "r13_review_trigger", "cross_review_trigger", "review_case"}:
            normalised["do_not_count_as_new_case"] = True
            normalised.setdefault("independent_evidence_weight", 0)
    _derive_v12_compact_semantics(normalised)
    if normalised.get("large_sector_id"):
        normalised["large_sector_id"] = normalise_large_sector_id(normalised.get("large_sector_id"))
    if normalised.get("canonical_archetype_id"):
        normalised["canonical_archetype_id"] = normalise_canonical_archetype_id(normalised.get("canonical_archetype_id"))
    return normalised


def _append_row(
    rows_by_type: dict[str, list[dict[str, Any]]],
    row: dict[str, Any],
    *,
    document: MarkdownDocument,
    method: str,
    line_number: int | None,
    raw_snippet: str,
) -> None:
    normalised = _normalise_row(row)
    row_type = str(normalised.get("row_type", "")).strip()
    if row_type not in ROW_TYPES:
        return
    normalised.setdefault("round", document.round)
    normalised.setdefault("loop", document.loop)
    normalised.setdefault("schema_family", document.schema_family)
    normalised.setdefault("large_sector_id", document.large_sector_id)
    normalised.setdefault("canonical_archetype_id", document.canonical_archetype_id)
    normalised.setdefault("fine_archetype_id", document.fine_archetype_id)
    if document.schema_family == "v12_sector_archetype_residual":
        normalised.setdefault("price_data_source", "Songdaiki/stock-web")
        normalised.setdefault("price_source", "Songdaiki/stock-web")
        normalised.setdefault("source", "Songdaiki/stock-web")
        normalised.setdefault("price_basis", "tradable_raw")
        normalised.setdefault("price_adjustment_status", "raw_unadjusted_marcap")
    normalised["source_file"] = str(document.path)
    normalised["source_sha256"] = document.sha256
    normalised["source_line_range"] = f"{line_number}" if line_number else None
    normalised["raw_source_snippet"] = raw_snippet[:1000]
    normalised["parse_method"] = method
    rows_by_type.setdefault(row_type, []).append(normalised)


def _parse_metadata(text: str) -> dict[str, str]:
    metadata: dict[str, str] = {}
    for match in FENCE_RE.finditer(text[:16000]):
        if match.group("lang").strip().lower() not in {"text", ""}:
            continue
        for raw_line in match.group("body").splitlines():
            line = raw_line.strip()
            if "=" not in line:
                continue
            key, value = [part.strip() for part in line.split("=", 1)]
            if key:
                metadata[_normalise_key(key)] = value.strip().strip("`")
    for raw_line in text[:24000].splitlines():
        line = raw_line.strip()
        if line.startswith("- "):
            line = line[2:].strip()
        if ":" not in line:
            continue
        key, value = [part.strip() for part in line.split(":", 1)]
        normalised_key = _normalise_key(key)
        if not normalised_key or normalised_key in metadata:
            continue
        cleaned = value.strip().strip("`").strip()
        if cleaned:
            metadata[normalised_key] = cleaned
    if "Songdaiki/stock-web" in text[:24000] and "price_source" not in metadata:
        metadata["price_source"] = "Songdaiki/stock-web"
    if metadata.get("large_sector_id"):
        normalised_large = normalise_large_sector_id(metadata.get("large_sector_id"))
        if normalised_large:
            metadata["large_sector_id"] = normalised_large
    if metadata.get("canonical_archetype_id"):
        normalised_canonical = normalise_canonical_archetype_id(metadata.get("canonical_archetype_id"))
        if normalised_canonical:
            metadata["canonical_archetype_id"] = normalised_canonical
    return metadata


def _line_number_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _v12_document_flags(text: str) -> dict[str, bool]:
    lower = text.lower()
    return {
        "evidence_url_pending": text_has_evidence_url_pending(lower),
        "source_proxy_only": "source-name-level" in lower
        or "historical public-event proxies" in lower
        or "event proxies" in lower,
    }


def _parse_json_lines(text: str, rows_by_type: dict[str, list[dict[str, Any]]], document: MarkdownDocument) -> None:
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if not (line.startswith("{") and line.endswith("}")):
            continue
        try:
            payload = json.loads(line)
        except json.JSONDecodeError:
            continue
        if "row_type" not in payload and _looks_like_no_repeat_trigger_row(payload):
            payload = {"row_type": "trigger", **payload}
        elif "row_type" not in payload and payload.get("source") == "Songdaiki/stock-web":
            payload = {"row_type": "price_source_validation", **payload}
        _append_row(
            rows_by_type,
            payload,
            document=document,
            method="jsonl",
            line_number=line_number,
            raw_snippet=raw_line,
        )


def _looks_like_no_repeat_trigger_row(payload: dict[str, Any]) -> bool:
    schema_version = str(payload.get("schema_version") or "")
    if schema_version.startswith("v12_no_repeat_standalone_trigger_row"):
        return True
    normalised_keys = {_normalise_key(str(key)) for key in payload}
    required = {"trigger_type", "entry_date", "entry_price"}
    price_path = {"MFE_30D_pct", "MFE_90D_pct", "MFE_180D_pct", "MAE_30D_pct", "MAE_90D_pct", "MAE_180D_pct"}
    return required.issubset(normalised_keys) and len(price_path.intersection(normalised_keys)) >= 2


def _parse_csv_fences(text: str, rows_by_type: dict[str, list[dict[str, Any]]], document: MarkdownDocument) -> None:
    for match in FENCE_RE.finditer(text):
        lang = match.group("lang").strip().lower()
        body = match.group("body").strip("\n")
        if lang not in {"csv", "tsv"}:
            continue
        if "row_type" not in body.splitlines()[0]:
            continue
        delimiter = "\t" if lang == "tsv" else ","
        reader = csv.DictReader(io.StringIO(body), delimiter=delimiter)
        start_line = _line_number_for_offset(text, match.start("body"))
        for offset, row in enumerate(reader, start=1):
            _append_row(
                rows_by_type,
                dict(row),
                document=document,
                method=f"{lang}_fence",
                line_number=start_line + offset,
                raw_snippet=",".join(str(value) for value in row.values()),
            )


def _split_markdown_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _parse_markdown_tables(text: str, rows_by_type: dict[str, list[dict[str, Any]]], document: MarkdownDocument) -> None:
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        if not lines[index].lstrip().startswith("|"):
            index += 1
            continue
        start = index
        block: list[str] = []
        while index < len(lines) and lines[index].lstrip().startswith("|"):
            block.append(lines[index])
            index += 1
        if len(block) < 2:
            continue
        headers = [_normalise_key(cell) for cell in _split_markdown_row(block[0])]
        separator = _split_markdown_row(block[1])
        if not all(set(cell.replace(":", "").strip()) <= {"-"} for cell in separator if cell):
            continue
        data_lines = block[2:]
        has_row_type = "row_type" in headers
        looks_like_trigger = {"trigger_id", "entry_date", "entry_price"}.issubset(set(headers))
        looks_like_case = {"case_id", "symbol"}.issubset(set(headers)) and (
            "company_name" in headers or "positive_or_counterexample" in headers or "case_type" in headers
        )
        looks_like_coverage = {"large_sector_id", "canonical_archetype_id"}.issubset(set(headers)) and (
            "calibration_usable_trigger_count" in headers or "representative_trigger_count" in headers
        )
        looks_like_rule_candidate = "rule_scope" in headers or (
            "sector_rule_candidate" in headers or "canonical_rule_candidate" in headers
        )
        looks_like_price_source = headers == ["field", "value"]
        if not (has_row_type or looks_like_trigger or looks_like_case or looks_like_coverage or looks_like_rule_candidate or looks_like_price_source):
            continue
        if looks_like_price_source:
            values = {}
            for line in data_lines:
                cells = _split_markdown_row(line)
                if len(cells) >= 2:
                    values[cells[0]] = cells[1]
            if values.get("source") == "Songdaiki/stock-web" or values.get("price_basis") == "tradable_raw":
                _append_row(
                    rows_by_type,
                    {"row_type": "price_source_validation", **values},
                    document=document,
                    method="markdown_table",
                    line_number=start + 1,
                    raw_snippet="\n".join(block[: min(8, len(block))]),
                )
            continue
        for line in data_lines:
            cells = _split_markdown_row(line)
            if len(cells) != len(headers):
                continue
            row = dict(zip(headers, cells))
            if looks_like_trigger and "row_type" not in row:
                row["row_type"] = "trigger"
            elif looks_like_case and "row_type" not in row:
                row["row_type"] = "case"
            elif looks_like_coverage and "row_type" not in row:
                row["row_type"] = "coverage_matrix"
            elif looks_like_rule_candidate and "row_type" not in row:
                row["row_type"] = "sector_rule_candidate"
            _append_row(
                rows_by_type,
                row,
                document=document,
                method="markdown_table",
                line_number=start + 1,
                raw_snippet=line,
            )


def _enrich_trigger_rows_by_trigger_id(rows_by_type: dict[str, list[dict[str, Any]]]) -> None:
    """Merge trigger-grid metadata into OHLC trigger rows with the same id.

    Several v12 research files separate the trigger grid from the price-path
    table. The OHLC table is the row usable for validation because it has
    MFE/MAE, but it may omit ``trigger_type`` and case verdict fields. Treating
    that omission as a valid blank trigger silently weakens stage transition
    aggregation, so we copy non-price metadata from the trigger-grid row.
    """

    trigger_rows = rows_by_type.get("trigger", [])
    metadata_by_trigger_id: dict[str, dict[str, Any]] = {}
    metadata_keys = (
        "case_id",
        "trigger_type",
        "trigger_date",
        "trigger_outcome_label",
        "current_profile_verdict",
        "aggregate_group_role",
        "case_type",
        "positive_or_counterexample",
        "dedupe_for_aggregate",
        "calibration_usable",
        "evidence_source",
        "evidence_available_at_that_date",
    )
    for row in trigger_rows:
        trigger_id = str(row.get("trigger_id") or "").strip()
        if not trigger_id:
            continue
        if not row.get("trigger_type") and not row.get("case_id"):
            continue
        metadata = metadata_by_trigger_id.setdefault(trigger_id, {})
        for key in metadata_keys:
            value = row.get(key)
            if value not in (None, "") and key not in metadata:
                metadata[key] = value
    for row in trigger_rows:
        trigger_id = str(row.get("trigger_id") or "").strip()
        if not trigger_id:
            continue
        metadata = metadata_by_trigger_id.get(trigger_id)
        if not metadata:
            continue
        for key, value in metadata.items():
            if row.get(key) in (None, ""):
                row[key] = value


def _has_price_path_fragment(row: dict[str, Any]) -> bool:
    return any(
        row.get(key) not in (None, "")
        for key in (
            "MFE_30D_pct",
            "MFE_90D_pct",
            "MFE_180D_pct",
            "MAE_30D_pct",
            "MAE_90D_pct",
            "MAE_180D_pct",
            "mfe_pct",
            "mae_pct",
        )
    )


def _looks_like_compact_v12_case_trigger(row: dict[str, Any]) -> bool:
    if row.get("row_type") != "case":
        return False
    if not (row.get("case_id") and row.get("symbol") and row.get("entry_date") and row.get("entry_price")):
        return False
    has_label = any(
        row.get(key) not in (None, "")
        for key in ("trigger_type", "classification", "path_label", "stage_judgment", "evidence_summary")
    )
    return has_label and _has_price_path_fragment(row)


def _synthesise_v12_case_triggers(rows_by_type: dict[str, list[dict[str, Any]]], document: MarkdownDocument) -> None:
    """Create trigger rows from compact v12 case rows.

    Newer research output sometimes wrote the calibration datum as a case row:
    symbol, entry date, entry price, price path and classification are present,
    but ``row_type`` is still ``case``. Without this synthesis the document is
    parsed but contributes zero trigger rows.
    """

    if document.schema_family != "v12_sector_archetype_residual":
        return
    existing_case_ids = {row.get("case_id") for row in rows_by_type.get("trigger", []) if row.get("case_id")}
    for case_row in list(rows_by_type.get("case", [])):
        if not _looks_like_compact_v12_case_trigger(case_row):
            continue
        if case_row.get("case_id") in existing_case_ids:
            continue
        trigger_row = dict(case_row)
        trigger_row["row_type"] = "trigger"
        trigger_row["source_row_type"] = "v12_compact_case"
        trigger_row.setdefault("trigger_id", f"{case_row.get('case_id')}_TRIGGER")
        trigger_row.setdefault("trigger_date", case_row.get("trigger_date") or case_row.get("entry_date"))
        _append_row(
            rows_by_type,
            trigger_row,
            document=document,
            method="compact_case_synthesis",
            line_number=None,
            raw_snippet=str(case_row.get("raw_source_snippet") or case_row)[:1000],
        )
        existing_case_ids.add(case_row.get("case_id"))


def _synthesise_v12_review_only_audit_trigger(rows_by_type: dict[str, list[dict[str, Any]]], document: MarkdownDocument) -> None:
    """Keep review-only v12 files visible in the trigger rejection ledger.

    A few R13 red-team files intentionally contain only aggregate, coverage or
    shadow-weight rows. They should not become valid calibration cases, but a
    zero-trigger document makes preflight look like parser loss. We add one
    audit-only trigger row that validation will reject for missing price path.
    """

    if document.schema_family != "v12_sector_archetype_residual":
        return
    if rows_by_type.get("trigger"):
        return
    support_row_types = (
        "aggregate_metric",
        "coverage_matrix",
        "shadow_weight",
        "residual_contribution",
        "narrative_only",
        "profile_comparison",
        "score_simulation",
    )
    if not any(rows_by_type.get(row_type) for row_type in support_row_types):
        return
    trigger_id = "V12_REVIEW_ONLY_{round}_{loop}_{arch}".format(
        round=document.round or "unknown_round",
        loop=document.loop or "unknown_loop",
        arch=document.canonical_archetype_id or "unknown_archetype",
    )
    audit_row = {
        "row_type": "trigger",
        "source_row_type": "v12_review_only_audit",
        "trigger_id": trigger_id,
        "case_id": trigger_id,
        "trigger_type": "review_only_no_price_path",
        "calibration_usable": False,
        "dedupe_for_aggregate": False,
        "aggregate_group_role": "audit_only",
        "do_not_count_as_new_case": True,
        "independent_evidence_weight": 0,
        "calibration_block_reasons": ["review_only_document_without_symbol_entry_price_path"],
        "positive_or_counterexample": "counterexample",
        "case_type": "review_only",
        "current_profile_verdict": "review_only_not_calibration_case",
    }
    _append_row(
        rows_by_type,
        audit_row,
        document=document,
        method="review_only_audit_synthesis",
        line_number=None,
        raw_snippet=json.dumps(audit_row, ensure_ascii=False),
    )


def parse_markdown_document(document: MarkdownDocument) -> ParsedMarkdown:
    text = document.path.read_text(encoding="utf-8", errors="replace")
    metadata = _parse_metadata(text)
    if document.round is None and metadata.get("round"):
        round_value = str(metadata.get("round")).strip().upper()
        if round_value and not round_value.startswith("R") and round_value.isdigit():
            round_value = f"R{int(round_value)}"
        object.__setattr__(document, "round", round_value)
    if document.loop is None and metadata.get("loop"):
        loop_value = str(metadata.get("loop")).strip()
        object.__setattr__(document, "loop", str(int(loop_value)) if loop_value.isdigit() else loop_value)
    if document.large_sector_id is not None:
        object.__setattr__(document, "large_sector_id", normalise_large_sector_id(document.large_sector_id))
    if document.large_sector_id is None and metadata.get("large_sector_id"):
        object.__setattr__(document, "large_sector_id", metadata.get("large_sector_id"))
    if document.canonical_archetype_id is not None:
        object.__setattr__(document, "canonical_archetype_id", normalise_canonical_archetype_id(document.canonical_archetype_id))
    if document.canonical_archetype_id is None and metadata.get("canonical_archetype_id"):
        object.__setattr__(document, "canonical_archetype_id", metadata.get("canonical_archetype_id"))
    if document.fine_archetype_id is None and metadata.get("fine_archetype_id"):
        object.__setattr__(document, "fine_archetype_id", metadata.get("fine_archetype_id"))
    rows_by_type: dict[str, list[dict[str, Any]]] = {row_type: [] for row_type in ROW_TYPES}

    try:
        _parse_json_lines(text, rows_by_type, document)
        _parse_csv_fences(text, rows_by_type, document)
        _parse_markdown_tables(text, rows_by_type, document)
        _synthesise_v12_case_triggers(rows_by_type, document)
        _synthesise_v12_review_only_audit_trigger(rows_by_type, document)
        _enrich_trigger_rows_by_trigger_id(rows_by_type)
        if not rows_by_type["price_source_validation"]:
            candidate = {
                "row_type": "price_source_validation",
                "source": metadata.get("price_source"),
                "price_data_source": metadata.get("price_source"),
                "price_basis": metadata.get("price_basis", "tradable_raw" if document.schema_family == "v12_sector_archetype_residual" else None),
                "price_adjustment_status": metadata.get(
                    "price_adjustment_status",
                    "raw_unadjusted_marcap" if document.schema_family == "v12_sector_archetype_residual" else None,
                ),
                "validation_status": "metadata_fallback",
            }
            if candidate["source"]:
                _append_row(
                    rows_by_type,
                    candidate,
                    document=document,
                    method="metadata_fallback",
                    line_number=None,
                    raw_snippet=json.dumps(candidate, ensure_ascii=False),
                )
        if document.schema_family == "v12_sector_archetype_residual":
            doc_flags = _v12_document_flags(text)
            residual_row = {
                "row_type": "residual_contribution",
                "research_session": metadata.get("research_session"),
                "mode": metadata.get("mode"),
                "round": document.round or metadata.get("round"),
                "loop": document.loop or metadata.get("loop"),
                "large_sector_id": document.large_sector_id or metadata.get("large_sector_id"),
                "canonical_archetype_id": document.canonical_archetype_id or metadata.get("canonical_archetype_id"),
                "fine_archetype_id": document.fine_archetype_id or metadata.get("fine_archetype_id"),
                "loop_objective": metadata.get("loop_objective"),
                "current_default_profile_proxy": metadata.get("current_default_profile_proxy") or metadata.get("current_default_proxy"),
                "previous_baseline_reference": metadata.get("previous_baseline_reference"),
                "new_independent_case_count": metadata.get("new_independent_case_count"),
                "reused_case_count": metadata.get("reused_case_count"),
                "new_symbol_count": metadata.get("new_symbol_count"),
                "same_archetype_new_symbol_count": metadata.get("same_archetype_new_symbol_count"),
                "same_archetype_new_trigger_family_count": metadata.get("same_archetype_new_trigger_family_count"),
                "positive_case_count": metadata.get("positive_case_count"),
                "counterexample_count": metadata.get("counterexample_count"),
                "4B_case_count": metadata.get("4B_case_count"),
                "4C_case_count": metadata.get("4C_case_count"),
                "loop_contribution_label": metadata.get("loop_contribution_label"),
                "do_not_propose_new_weight_delta": metadata.get("do_not_propose_new_weight_delta"),
                "auto_selected_coverage_gap": metadata.get("auto_selected_coverage_gap"),
                **doc_flags,
            }
            _append_row(
                rows_by_type,
                residual_row,
                document=document,
                method="metadata_residual_summary",
                line_number=None,
                raw_snippet=json.dumps(residual_row, ensure_ascii=False),
            )
            _synthesise_v12_review_only_audit_trigger(rows_by_type, document)
            for typed_rows in rows_by_type.values():
                for index, row in enumerate(typed_rows):
                    if doc_flags["evidence_url_pending"]:
                        row["evidence_url_pending"] = True
                    if doc_flags["source_proxy_only"]:
                        row["source_proxy_only"] = True
                    typed_rows[index] = normalise_evidence_quality_flags(row)
    except Exception as exc:  # pragma: no cover - defensive registry path
        return ParsedMarkdown(
            registry_row=_registry_row(document, metadata, rows_by_type, "failed", str(exc)),
            rows_by_type=rows_by_type,
            failed=True,
            failure_reason=str(exc),
        )

    status = "parsed" if any(rows_by_type[row_type] for row_type in ROW_TYPES) else "metadata_only"
    return ParsedMarkdown(
        registry_row=_registry_row(document, metadata, rows_by_type, status, None),
        rows_by_type=rows_by_type,
    )


def _registry_row(
    document: MarkdownDocument,
    metadata: dict[str, str],
    rows_by_type: dict[str, list[dict[str, Any]]],
    status: str,
    failure_reason: str | None,
) -> dict[str, Any]:
    trigger_count = len(rows_by_type.get("trigger", []))
    rejected_count = 0
    return {
        "file_path": str(document.path),
        "sha256": document.sha256,
        "filename": document.filename or document.path.name,
        "schema_family": document.schema_family,
        "round": document.round or metadata.get("round"),
        "loop": document.loop or metadata.get("loop"),
        "sector": metadata.get("sector"),
        "large_sector_id": document.large_sector_id or metadata.get("large_sector_id"),
        "canonical_archetype_id": document.canonical_archetype_id or metadata.get("canonical_archetype_id"),
        "fine_archetype_id": document.fine_archetype_id or metadata.get("fine_archetype_id"),
        "loop_objective": metadata.get("loop_objective"),
        "loop_contribution_label": metadata.get("loop_contribution_label"),
        "extraction_status": status,
        "parsed_trigger_row_count": trigger_count,
        "rejected_row_count": rejected_count,
        "failure_reason": failure_reason,
        "row_type_counts": {row_type: len(rows) for row_type, rows in sorted(rows_by_type.items()) if rows},
    }
