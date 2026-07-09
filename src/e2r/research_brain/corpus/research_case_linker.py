"""Link structured historical rows without collapsing cases."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Any, Iterable, Mapping

from e2r.research_brain.intelligence_schema import (
    LinkageError,
    ParsedResearchArtifact,
    ParsedResearchRow,
    QuarantineReason,
    QuarantineRecord,
    stable_intelligence_id,
)


CASE_ROW_TYPES = {
    "case",
    "case_header",
    "case_row",
    "case_summary",
}
TRIGGER_ROW_TYPES = {
    "trigger",
    "trigger_case",
    "trigger_result",
    "trigger_row",
    "trigger_row_representative",
    "v12_trigger",
    "v12_trigger_case",
    "cross_review_trigger",
    "positive_contrast_review",
    "redteam_review",
    "review_case",
    "r13_4b4c_redteam_trigger",
    "r13_4b_4c_redteam_trigger",
    "r13_accounting_trust_price_validation_trigger",
    "r13_cross_case",
    "r13_cross_holdout_trigger",
    "r13_high_mae_guardrail_trigger",
    "r13_loop92_cross_case",
    "r13_loop92_review_trigger",
    "r13_review_trigger",
    "r13_stage2_false_positive_trigger",
}
SCORE_ROW_TYPES = {"score_simulation", "score_simulation_row"}
OUTCOME_ROW_TYPES = TRIGGER_ROW_TYPES | SCORE_ROW_TYPES | {
    "stage_transition",
    "stage_transition_summary",
}
RULE_ROW_TYPES = {
    "shadow_weight",
    "shadow_weight_audit",
    "shadow_weight_candidate",
    "shadow_weight_change_candidate",
    "shadow_weight_delta",
    "shadow_weight_proposal",
    "shadow_weight_recommendation",
    "shadow_weight_rule_candidate",
    "shadow_rule",
    "shadow_rule_candidate",
    "shadow_guardrail",
    "guardrail_delta",
    "r13_guardrail_candidate",
    "r13_guardrail_rule_candidate",
    "residual_rule_candidate",
    "sector_rule_candidate",
    "canonical_archetype_rule_candidate",
    "v12_shadow_weight_proposal",
    "residual_contribution",
    "residual_contribution_summary",
    "v12_aggregate_residual_contribution",
    "stage_transition_summary",
    "stage_transition",
    "rule_candidate",
}
ARTIFACT_METADATA_ROW_TYPES = {
    "price_source_validation",
    "atlas_validation",
    "price_atlas_manifest",
    "profile_validation",
    "symbol_profile_validation",
    "symbol_profile_check",
    "validation_scope",
    "aggregate",
    "aggregate_metric",
    "aggregate_metrics",
    "aggregate_profile",
    "aggregate_profile_comparison",
    "aggregate_row",
    "aggregate_shadow_weight",
    "aggregate_summary",
    "batch_aggregate",
    "coverage_matrix",
    "coverage",
    "profile_aggregate",
    "profile_aggregate_comparison",
    "profile_comparison",
    "profile_check",
    "profile_simulation",
    "profile_summary",
    "score_profile_aggregate",
    "score_profile_summary",
    "selected_price_row",
    "v12_aggregate",
    "v12_aggregate_metrics_candidate",
    "v12_batch_aggregate",
    "research_metadata",
    "research_state",
    "next_research_state",
    "completed_state",
    "narrative_only",
    "narrative_only_audit",
    "narrative_only_blocked",
    "narrative_only_blocked_price_row",
    "narrative_only_future_todo",
    "narrative_only_future_trigger_todo",
    "narrative_only_price_blocked",
}
SOURCE_ROW_TYPES = {"source_map", "evidence_source", "source", "evidence_map"}


@dataclass(frozen=True)
class LinkedCaseRows:
    case_id: str
    case_row: ParsedResearchRow | None
    trigger_rows: tuple[ParsedResearchRow, ...]
    score_simulation_rows: tuple[ParsedResearchRow, ...]
    shadow_rule_rows: tuple[ParsedResearchRow, ...]
    transition_rows: tuple[ParsedResearchRow, ...]
    source_rows: tuple[ParsedResearchRow, ...]

    @property
    def all_rows(self) -> tuple[ParsedResearchRow, ...]:
        rows: list[ParsedResearchRow] = []
        if self.case_row:
            rows.append(self.case_row)
        rows.extend(self.trigger_rows)
        rows.extend(self.score_simulation_rows)
        rows.extend(self.shadow_rule_rows)
        rows.extend(self.transition_rows)
        rows.extend(self.source_rows)
        return _unique_rows(rows)


@dataclass(frozen=True)
class ResearchCaseLinkage:
    artifact: ParsedResearchArtifact
    cases: tuple[LinkedCaseRows, ...]
    rule_rows: tuple[ParsedResearchRow, ...]
    metadata_rows: tuple[ParsedResearchRow, ...]
    unlinked_rows: tuple[ParsedResearchRow, ...]
    linkage_errors: tuple[LinkageError, ...]
    quarantine: tuple[QuarantineRecord, ...]


def link_research_rows(parsed: ParsedResearchArtifact) -> ResearchCaseLinkage:
    explicit_rows = [row for row in parsed.rows if row.structured and row_type_of(row)]
    by_case_id: dict[str, list[ParsedResearchRow]] = {}
    triggers_by_case: dict[str, list[ParsedResearchRow]] = {}
    trigger_to_case: dict[str, str] = {}
    scores_by_case: dict[str, list[ParsedResearchRow]] = {}
    shadow_by_case: dict[str, list[ParsedResearchRow]] = {}
    transitions_by_case: dict[str, list[ParsedResearchRow]] = {}
    sources_by_case: dict[str, list[ParsedResearchRow]] = {}
    trigger_rows: list[ParsedResearchRow] = []
    rule_rows: list[ParsedResearchRow] = []
    metadata_rows: list[ParsedResearchRow] = []
    unlinked_rows: list[ParsedResearchRow] = []
    errors: list[LinkageError] = []
    quarantine: list[QuarantineRecord] = list(parsed.quarantine)
    resolved_case_rows: dict[str, str] = {}
    resolved_trigger_cases: dict[str, str] = {}
    case_hints_by_trigger: dict[str, set[str]] = {}
    case_hints_by_identity: dict[tuple[str, str], set[str]] = {}
    case_hints_by_symbol: dict[str, set[str]] = {}

    for row in explicit_rows:
        if row_type_of(row) not in CASE_ROW_TYPES:
            continue
        case_id = _explicit_case_id(row) or _synthetic_case_id(row)
        resolved_case_rows[row.row_id] = case_id
        for key in ("best_trigger", "trigger_id", "representative_trigger_id", "source_trigger_id"):
            trigger_reference = _text(row.data.get(key))
            if trigger_reference:
                case_hints_by_trigger.setdefault(trigger_reference, set()).add(case_id)
        identity = _symbol_date_identity(row)
        if identity:
            case_hints_by_identity.setdefault(identity, set()).add(case_id)
        symbol = normalize_symbol(row.data.get("symbol") or row.data.get("ticker"))
        if symbol:
            case_hints_by_symbol.setdefault(symbol, set()).add(case_id)

    # Resolve trigger identities before dependent rows.  Historical files do not
    # guarantee that score/source rows appear after their trigger row.
    for row in explicit_rows:
        if row_type_of(row) not in TRIGGER_ROW_TYPES:
            continue
        case_id = _explicit_case_id(row)
        trigger_id = _trigger_id_of(row)
        if not case_id and trigger_id:
            case_id = _resolve_case_hint(trigger_id, case_hints_by_trigger)
        if not case_id:
            identity = _symbol_date_identity(row)
            hinted = case_hints_by_identity.get(identity or ("", ""), set())
            if len(hinted) == 1:
                case_id = next(iter(hinted))
        if not case_id:
            case_id = _synthetic_case_id(row)
        resolved_trigger_cases[row.row_id] = case_id
        symbol = normalize_symbol(row.data.get("symbol") or row.data.get("ticker"))
        if symbol:
            case_hints_by_symbol.setdefault(symbol, set()).add(case_id)
        if not trigger_id:
            continue
        existing = trigger_to_case.get(trigger_id)
        if existing and existing != case_id:
            errors.append(
                _link_error(
                    row,
                    "trigger_to_case",
                    trigger_id,
                    {"existing_case_id": existing, "new_case_id": case_id},
                )
            )
            quarantine.append(
                _quarantine(
                    row,
                    QuarantineReason.CONFLICTING_DUPLICATE,
                    {"trigger_id": trigger_id, "case_ids": [existing, case_id]},
                )
            )
        else:
            trigger_to_case[trigger_id] = case_id

    for row in explicit_rows:
        row_type = row_type_of(row)
        if row_type in CASE_ROW_TYPES:
            case_id = resolved_case_rows[row.row_id]
            by_case_id.setdefault(case_id, []).append(row)
        elif row_type in TRIGGER_ROW_TYPES:
            trigger_rows.append(row)
            case_id = resolved_trigger_cases[row.row_id]
            trigger_id = _trigger_id_of(row)
            triggers_by_case.setdefault(case_id, []).append(row)
        elif row_type in SCORE_ROW_TYPES:
            case_id = _case_id_from_row(row, trigger_to_case, case_hints_by_symbol)
            if case_id:
                scores_by_case.setdefault(case_id, []).append(row)
            else:
                unlinked_rows.append(row)
        elif row_type in RULE_ROW_TYPES:
            rule_rows.append(row)
        elif row_type in ARTIFACT_METADATA_ROW_TYPES:
            metadata_rows.append(row)
        elif row_type in SOURCE_ROW_TYPES:
            case_id = _case_id_from_row(row, trigger_to_case, case_hints_by_symbol)
            if case_id:
                sources_by_case.setdefault(case_id, []).append(row)
            else:
                unlinked_rows.append(row)
        else:
            unlinked_rows.append(row)

    selected_case_rows: dict[str, ParsedResearchRow] = {}
    for case_id, candidates in by_case_id.items():
        selected, conflicts = _select_case_row(case_id, candidates)
        selected_case_rows[case_id] = selected
        for conflict in conflicts:
            errors.append(
                _link_error(
                    conflict,
                    "case_duplicate",
                    case_id,
                    {"selected_row_id": selected.row_id, "conflicting_row_id": conflict.row_id},
                )
            )
            quarantine.append(
                _quarantine(
                    conflict,
                    QuarantineReason.CONFLICTING_DUPLICATE,
                    {"case_id": case_id, "selected_row_id": selected.row_id},
                )
            )

    for row in rule_rows:
        row_type = row_type_of(row)
        trigger_ids = _listish(row.data.get("trigger_ids") or row.data.get("evidence_trigger_ids"))
        case_ids = _listish(row.data.get("case_ids") or row.data.get("evidence_case_ids"))
        for trigger_id in trigger_ids:
            case_id = _resolve_trigger_case(trigger_id, trigger_to_case)
            if case_id:
                shadow_by_case.setdefault(case_id, []).append(row)
            else:
                errors.append(_link_error(row, f"{row_type}_to_trigger", trigger_id, {}))
        for case_id in case_ids:
            shadow_by_case.setdefault(case_id, []).append(row)
        direct_case = _explicit_case_id(row)
        if direct_case:
            shadow_by_case.setdefault(direct_case, []).append(row)

    for row in rule_rows:
        if row_type_of(row) not in {"stage_transition", "stage_transition_summary"}:
            continue
        direct_case = _explicit_case_id(row)
        if direct_case:
            transitions_by_case.setdefault(direct_case, []).append(row)
            continue
        symbol = normalize_symbol(row.data.get("symbol") or row.data.get("ticker"))
        entry_date = _text(row.data.get("entry_date") or row.data.get("trigger_date"))
        identity_rows = [*trigger_rows, *selected_case_rows.values()]
        matching_case_ids = {
            (
                resolved_trigger_cases.get(identity_row.row_id)
                or resolved_case_rows.get(identity_row.row_id)
                or _explicit_case_id(identity_row)
            )
            for identity_row in identity_rows
            if normalize_symbol(
                identity_row.data.get("symbol") or identity_row.data.get("ticker")
            )
            == symbol
            and _text(
                identity_row.data.get("entry_date")
                or identity_row.data.get("trigger_date")
            )
            == entry_date
            and (
                resolved_trigger_cases.get(identity_row.row_id)
                or resolved_case_rows.get(identity_row.row_id)
                or _explicit_case_id(identity_row)
            )
        }
        if len(matching_case_ids) == 1:
            case_id = next(iter(matching_case_ids))
            transitions_by_case.setdefault(case_id, []).append(row)
        elif symbol or entry_date:
            errors.append(
                _link_error(
                    row,
                    "stage_transition_symbol_entry_date",
                    f"{symbol or '?'}:{entry_date or '?'}",
                    {"match_count": len(matching_case_ids)},
                )
            )

    all_case_ids = set(selected_case_rows) | set(triggers_by_case)
    cases: list[LinkedCaseRows] = []
    for case_id in sorted(all_case_ids):
        cases.append(
            LinkedCaseRows(
                case_id=case_id,
                case_row=selected_case_rows.get(case_id),
                trigger_rows=tuple(triggers_by_case.get(case_id, ())),
                score_simulation_rows=tuple(scores_by_case.get(case_id, ())),
                shadow_rule_rows=_unique_rows(shadow_by_case.get(case_id, ())),
                transition_rows=_unique_rows(transitions_by_case.get(case_id, ())),
                source_rows=_unique_rows(sources_by_case.get(case_id, ())),
            )
        )

    linked_ids = {row.row_id for case in cases for row in case.all_rows}
    linked_ids.update(row.row_id for row in rule_rows)
    linked_ids.update(row.row_id for row in metadata_rows)
    for row in explicit_rows:
        if row.row_id not in linked_ids and row not in unlinked_rows:
            unlinked_rows.append(row)
    for row in unlinked_rows:
        if not any(item.row_id == row.row_id for item in quarantine):
            reason = (
                QuarantineReason.OUTCOME_ONLY
                if row_type_of(row) in OUTCOME_ROW_TYPES
                else (
                    QuarantineReason.URL_CASE_ASSOCIATION_AMBIGUOUS
                    if row_type_of(row) in SOURCE_ROW_TYPES
                    else QuarantineReason.UNLINKED_ROW
                )
            )
            quarantine.append(
                _quarantine(
                    row,
                    reason,
                    {"row_type": row_type_of(row)},
                )
            )

    return ResearchCaseLinkage(
        artifact=parsed,
        cases=tuple(cases),
        rule_rows=tuple(rule_rows),
        metadata_rows=tuple(metadata_rows),
        unlinked_rows=_unique_rows(unlinked_rows),
        linkage_errors=tuple(errors),
        quarantine=tuple(quarantine),
    )


def row_type_of(row: ParsedResearchRow) -> str | None:
    for key in ("row_type", "type", "record_type"):
        value = _text(row.data.get(key))
        if value:
            return value.lower().replace("-", "_").replace(" ", "_")
    return None


def normalize_symbol(value: Any) -> str | None:
    match = re.search(r"(?<!\d)(\d{6})(?!\d)", str(value or ""))
    return match.group(1) if match else None


def company_from_symbol_field(value: Any) -> str | None:
    text = str(value or "").strip()
    match = re.match(r"^\d{6}\s+(.+)$", text)
    return match.group(1).strip() if match else None


def _select_case_row(
    case_id: str,
    rows: Iterable[ParsedResearchRow],
) -> tuple[ParsedResearchRow, tuple[ParsedResearchRow, ...]]:
    ordered = sorted(rows, key=lambda row: (row.precedence, row.source_line_range.start, row.row_id))
    selected = ordered[0]
    selected_payload = _semantic_payload(selected.data)
    conflicts = tuple(
        row for row in ordered[1:] if _semantic_payload(row.data) != selected_payload
    )
    return selected, conflicts


def _semantic_payload(data: Mapping[str, Any]) -> str:
    ignored = {"source_file", "source_line_range", "raw_source_snippet", "parse_method"}
    payload = {key: value for key, value in data.items() if key not in ignored}
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, default=str)


def _case_id_from_row(
    row: ParsedResearchRow,
    trigger_to_case: Mapping[str, str],
    cases_by_symbol: Mapping[str, set[str]],
) -> str | None:
    case_id = _explicit_case_id(row)
    if case_id:
        return case_id
    trigger_id = _trigger_id_of(row)
    from_trigger = _resolve_trigger_case(trigger_id or "", trigger_to_case)
    if from_trigger:
        return from_trigger
    symbol = normalize_symbol(row.data.get("symbol") or row.data.get("ticker"))
    matched = cases_by_symbol.get(symbol or "", set())
    return next(iter(matched)) if len(matched) == 1 else None


def _resolve_trigger_case(
    trigger_reference: str,
    trigger_to_case: Mapping[str, str],
) -> str | None:
    direct = trigger_to_case.get(trigger_reference)
    if direct:
        return direct
    matched_cases = {
        case_id
        for trigger_id, case_id in trigger_to_case.items()
        if trigger_id.startswith(f"{trigger_reference}_")
    }
    return next(iter(matched_cases)) if len(matched_cases) == 1 else None


def _resolve_case_hint(
    trigger_reference: str,
    hints: Mapping[str, set[str]],
) -> str | None:
    direct = hints.get(trigger_reference, set())
    if len(direct) == 1:
        return next(iter(direct))
    matched = {
        case_id
        for known_trigger, case_ids in hints.items()
        if known_trigger.startswith(f"{trigger_reference}_")
        or trigger_reference.startswith(f"{known_trigger}_")
        for case_id in case_ids
    }
    return next(iter(matched)) if len(matched) == 1 else None


def _symbol_date_identity(row: ParsedResearchRow) -> tuple[str, str] | None:
    symbol = normalize_symbol(row.data.get("symbol") or row.data.get("ticker"))
    date = _text(row.data.get("entry_date") or row.data.get("trigger_date"))
    return (symbol, date) if symbol and date else None


def _synthetic_case_id(row: ParsedResearchRow) -> str:
    return stable_intelligence_id(
        "HCASE",
        {
            "trigger_id": _trigger_id_of(row),
            "symbol": normalize_symbol(row.data.get("symbol") or row.data.get("ticker")),
            "date": _text(row.data.get("entry_date") or row.data.get("trigger_date")),
            "canonical_archetype_id": _text(
                row.data.get("canonical_archetype_id") or row.data.get("archetype_id")
            ),
            "trigger_type": _text(row.data.get("trigger_type")),
            "trigger_family": _text(row.data.get("trigger_family")),
        },
    )


def _explicit_case_id(row: ParsedResearchRow) -> str | None:
    return _text(row.data.get("case_id") or row.data.get("review_id"))


def _trigger_id_of(row: ParsedResearchRow) -> str | None:
    return _text(
        row.data.get("trigger_id")
        or row.data.get("source_trigger_id")
        or row.data.get("representative_trigger_id")
        or row.data.get("review_id")
    )


def _listish(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, (list, tuple, set)):
        return [str(item).strip() for item in value if str(item).strip()]
    return [
        part.strip()
        for part in re.split(r"[|,;]", str(value))
        if part.strip()
    ]


def _text(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _unique_rows(rows: Iterable[ParsedResearchRow]) -> tuple[ParsedResearchRow, ...]:
    seen: set[str] = set()
    result: list[ParsedResearchRow] = []
    for row in rows:
        if row.row_id in seen:
            continue
        seen.add(row.row_id)
        result.append(row)
    return tuple(result)


def _link_error(
    row: ParsedResearchRow,
    relation: str,
    missing_or_conflicting_id: str,
    details: Mapping[str, Any],
) -> LinkageError:
    return LinkageError(
        linkage_error_id=stable_intelligence_id(
            "HLINK",
            {
                "row_id": row.row_id,
                "relation": relation,
                "identity": missing_or_conflicting_id,
                "details": details,
            },
        ),
        artifact_id=row.artifact_id,
        source_file=row.source_file,
        source_row_id=row.row_id,
        source_line_range=row.source_line_range,
        relation=relation,
        missing_or_conflicting_id=missing_or_conflicting_id,
        details=dict(details),
    )


def _quarantine(
    row: ParsedResearchRow,
    reason: QuarantineReason,
    details: Mapping[str, Any],
) -> QuarantineRecord:
    return QuarantineRecord(
        quarantine_id=stable_intelligence_id(
            "HQUAR",
            {"row_id": row.row_id, "reason": reason.value, "details": details},
        ),
        artifact_id=row.artifact_id,
        source_file=row.source_file,
        source_line_range=row.source_line_range,
        reason=reason.value,
        row_id=row.row_id,
        details=dict(details),
        raw_text=row.raw_text,
    )


__all__ = [
    "ARTIFACT_METADATA_ROW_TYPES",
    "CASE_ROW_TYPES",
    "LinkedCaseRows",
    "OUTCOME_ROW_TYPES",
    "RULE_ROW_TYPES",
    "SCORE_ROW_TYPES",
    "SOURCE_ROW_TYPES",
    "ResearchCaseLinkage",
    "TRIGGER_ROW_TYPES",
    "company_from_symbol_field",
    "link_research_rows",
    "normalize_symbol",
    "row_type_of",
]
