"""Helpers for separating valid scores from blocked diagnostic snapshots."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum
from typing import Any, Mapping, Sequence

from e2r.diagnostic_values import diagnostic_value
from e2r.models import ScoreSnapshot


_BLOCK_FLAG_KEYS = (
    "score_blocked_by_theme_route",
    "score_blocked_by_score_gap",
    "score_blocked_by_asof_web",
)

_RAW_BLOCK_SCORE_KEYS = (
    "raw_score_total_before_theme_route_block",
    "raw_score_total_before_score_gap_block",
    "raw_score_total_before_asof_web_block",
)

_BLOCK_REASON_BY_RAW_KEY = {
    "raw_score_total_before_theme_route_block": "theme_route_unresolved",
    "raw_score_total_before_score_gap_block": "score_gap_unresolved",
    "raw_score_total_before_asof_web_block": "asof_web_score_unresolved",
}

_VISIBLE_SCORE_ALIAS_KEYS = ("visible_score", "current_score", "merged_score")
_COMPAT_SCORE_KEYS = ("score", "score_total", "total_score")
_COMPONENT_SCORE_FIELD_KEYS = {
    "eps_fcf_explosion_score": "eps_fcf_explosion",
    "earnings_visibility_score": "earnings_visibility",
    "bottleneck_pricing_score": "bottleneck_pricing",
    "market_mispricing_score": "market_mispricing",
    "valuation_rerating_score": "valuation_rerating",
    "capital_allocation_score": "capital_allocation",
    "information_confidence_score": "information_confidence",
}


@dataclass(frozen=True)
class ScoreStateComparison:
    """Classify why a visible score changed between two run outputs."""

    status: str
    visible_score_before: float | None
    visible_score_after: float | None
    visible_score_delta: float | None
    score_valid_before: bool | None
    score_valid_after: bool | None
    score_fingerprint_before: str | None
    score_fingerprint_after: str | None
    research_input_fingerprint_before: str | None
    research_input_fingerprint_after: str | None
    component_deltas: Mapping[str, float]
    drivers: tuple[str, ...]


@dataclass(frozen=True)
class ScoreStateRowChange:
    """One keyed row-level score-state comparison."""

    key: str
    before: Mapping[str, object] | object | None
    after: Mapping[str, object] | object | None
    comparison: ScoreStateComparison


@dataclass(frozen=True)
class ScoreStateContractFinding:
    """One serialized output path that violates the score-state contract."""

    path: str
    violation: str


def is_score_valid(score: ScoreSnapshot | None) -> bool:
    if score is None:
        return False
    diagnostics = score.diagnostic_scores
    if any(_diagnostic_value(diagnostics.get(key)) > 0.0 for key in _BLOCK_FLAG_KEYS):
        return False
    if any(key in diagnostics for key in _RAW_BLOCK_SCORE_KEYS):
        return False
    return _diagnostic_value(diagnostics.get("score_valid")) > 0.0


def score_block_reason(score: ScoreSnapshot | None) -> str | None:
    if score is None:
        return None
    if _diagnostic_value(score.diagnostic_scores.get("score_blocked_by_theme_route", 0.0)) > 0.0:
        return "theme_route_unresolved"
    if _diagnostic_value(score.diagnostic_scores.get("score_blocked_by_score_gap", 0.0)) > 0.0:
        return "score_gap_unresolved"
    if _diagnostic_value(score.diagnostic_scores.get("score_blocked_by_asof_web", 0.0)) > 0.0:
        return "asof_web_score_unresolved"
    for key, reason in _BLOCK_REASON_BY_RAW_KEY.items():
        if key in score.diagnostic_scores:
            return reason
    if is_score_valid(score):
        return None
    return "score_invalid"


def raw_score_total_before_block(score: ScoreSnapshot | None) -> float | None:
    if score is None:
        return None
    diagnostics = score.diagnostic_scores
    for key in _RAW_BLOCK_SCORE_KEYS:
        value = diagnostics.get(key)
        if value is not None:
            try:
                return float(value)
            except (TypeError, ValueError):
                return None
    return None


def visible_score_total(score: ScoreSnapshot | None) -> float | None:
    if not is_score_valid(score):
        return None
    return score.total_score if score is not None else None


def compare_score_states(
    before: Mapping[str, object] | object | None,
    after: Mapping[str, object] | object | None,
    *,
    materiality: float = 0.01,
) -> ScoreStateComparison:
    """Compare two serialized score states without mixing raw/cheap scores."""

    before_visible, before_source = _state_visible_score(before)
    after_visible, after_source = _state_visible_score(after)
    before_valid = serialized_score_valid(before)
    after_valid = serialized_score_valid(after)
    before_fp = _state_text(before, "score_fingerprint")
    after_fp = _state_text(after, "score_fingerprint")
    before_input_fp = _state_text(before, "research_input_fingerprint")
    after_input_fp = _state_text(after, "research_input_fingerprint")
    before_reason = serialized_score_block_reason(before)
    after_reason = serialized_score_block_reason(after)
    before_components = _state_component_scores(before)
    after_components = _state_component_scores(after)
    component_deltas = _component_score_deltas(before_components, after_components, materiality=materiality)
    delta = None
    if before_visible is not None and after_visible is not None:
        delta = after_visible - before_visible

    drivers: list[str] = []
    if before is None:
        drivers.append("state_missing:before")
    if after is None:
        drivers.append("state_missing:after")
    _append_visible_score_source_driver(drivers, "before", before_source)
    _append_visible_score_source_driver(drivers, "after", after_source)
    _append_contract_violation_drivers(drivers, "before", before)
    _append_contract_violation_drivers(drivers, "after", after)
    if before_valid != after_valid:
        drivers.append(f"score_valid_changed:{before_valid}->{after_valid}")
    if before_reason != after_reason:
        drivers.append(f"score_blocked_reason_changed:{before_reason or 'none'}->{after_reason or 'none'}")
    if delta is not None and abs(delta) >= materiality:
        drivers.append(f"visible_score_delta:{delta:g}")
    if before_components or after_components:
        if not before_components:
            drivers.append("component_scores_missing:before")
        if not after_components:
            drivers.append("component_scores_missing:after")
    for key, value in component_deltas.items():
        drivers.append(f"component_delta:{key}={value:g}")
    _append_variability_driver_changes(drivers, before, after)
    if before_fp and after_fp:
        drivers.append("score_fingerprint_same" if before_fp == after_fp else "score_fingerprint_changed")
    else:
        drivers.append("score_fingerprint_missing")
    if before_input_fp and after_input_fp:
        drivers.append("research_input_fingerprint_same" if before_input_fp == after_input_fp else "research_input_fingerprint_changed")
    else:
        drivers.append("research_input_fingerprint_missing")

    return ScoreStateComparison(
        status=_score_state_comparison_status(
            before=before,
            after=after,
            before_visible=before_visible,
            after_visible=after_visible,
            delta=delta,
            materiality=materiality,
            score_fingerprint_before=before_fp,
            score_fingerprint_after=after_fp,
            research_input_fingerprint_before=before_input_fp,
            research_input_fingerprint_after=after_input_fp,
            score_valid_before=before_valid,
            score_valid_after=after_valid,
        ),
        visible_score_before=before_visible,
        visible_score_after=after_visible,
        visible_score_delta=delta,
        score_valid_before=before_valid,
        score_valid_after=after_valid,
        score_fingerprint_before=before_fp,
        score_fingerprint_after=after_fp,
        research_input_fingerprint_before=before_input_fp,
        research_input_fingerprint_after=after_input_fp,
        component_deltas=component_deltas,
        drivers=tuple(dict.fromkeys(drivers)),
    )


def compare_score_state_rows(
    before_rows: Sequence[Mapping[str, object] | object],
    after_rows: Sequence[Mapping[str, object] | object],
    *,
    key_fields: Sequence[str] = ("symbol", "case_id", "company", "name"),
    materiality: float = 0.01,
) -> tuple[ScoreStateRowChange, ...]:
    """Compare score-state rows by stable keys without dropping missing rows."""

    before_by_key = _score_state_rows_by_key(before_rows, key_fields=key_fields)
    after_by_key = _score_state_rows_by_key(after_rows, key_fields=key_fields)
    changes: list[ScoreStateRowChange] = []
    for key in sorted(before_by_key.keys() | after_by_key.keys()):
        before = before_by_key.get(key)
        after = after_by_key.get(key)
        changes.append(
            ScoreStateRowChange(
                key=key,
                before=before,
                after=after,
                comparison=compare_score_states(before, after, materiality=materiality),
            )
        )
    return tuple(changes)


def serialized_visible_score(state: Mapping[str, object] | object | None) -> float | None:
    """Return only the score that is safe to display as visible score."""

    value, _ = _state_visible_score(state)
    return value


def serialized_score_valid(state: Mapping[str, object] | object | None) -> bool | None:
    """Return the effective serialized score validity used for display."""

    if state is None:
        return None
    if _state_invalid_score_marker(state):
        return False
    if _score_alias_conflict_marker(state):
        return False
    raw_valid = _state_bool(state, "score_valid")
    if raw_valid is True:
        return serialized_visible_score(state) is not None
    return raw_valid


def serialized_score_block_reason(state: Mapping[str, object] | object | None) -> str | None:
    """Return the effective serialized block reason used for display."""

    if state is None:
        return None
    explicit_reason = _state_text(state, "score_blocked_reason")
    marker = _state_invalid_score_marker(state)
    if marker:
        return explicit_reason or marker
    conflict = _score_alias_conflict_marker(state)
    if conflict:
        return explicit_reason or conflict
    if _state_bool(state, "score_valid") is True and serialized_visible_score(state) is None:
        return explicit_reason or "visible_score_missing"
    return explicit_reason


def normalized_score_state_payload(state: Mapping[str, object]) -> dict[str, object]:
    """Normalize serialized score-state fields before JSON/CSV exposure."""

    payload = dict(state)
    marker = _state_invalid_score_marker(payload)
    if marker:
        return _normalized_blocked_score_payload(payload, marker)
    conflict = _score_alias_conflict_marker(payload)
    if conflict:
        return _normalized_blocked_score_payload(payload, conflict, force_invalid=True)
    visible = serialized_visible_score(payload)
    if any(key in payload for key in (*_VISIBLE_SCORE_ALIAS_KEYS, *_COMPAT_SCORE_KEYS)):
        if visible is None:
            return _normalized_blocked_score_payload(payload, "visible_score_missing", force_invalid=True)
        payload["visible_score"] = visible
        for key in (*_VISIBLE_SCORE_ALIAS_KEYS, *_COMPAT_SCORE_KEYS):
            if key in payload:
                payload[key] = visible
    return payload


def normalized_score_state_mapping_if_present(state: Mapping[str, object]) -> dict[str, object]:
    """Normalize a plain mapping only when it carries score-state fields."""

    payload = dict(state)
    if not _state_has_any_score_state_marker(payload):
        return payload
    if not any(key in payload for key in (*_VISIBLE_SCORE_ALIAS_KEYS, *_COMPAT_SCORE_KEYS)):
        return payload
    return normalized_score_state_payload(payload)


def normalized_score_alias_value(
    value: object,
    *,
    score_valid: object,
    score_blocked_reason: object = None,
) -> object | None:
    """Normalize a secondary score column with the same visible-score contract."""

    payload = normalized_score_state_payload(
        {
            "score": value,
            "score_valid": score_valid,
            "score_blocked_reason": score_blocked_reason,
        }
    )
    return payload.get("score")


def score_state_contract_violations(state: Mapping[str, object] | object | None) -> tuple[str, ...]:
    """Return score-state output contract violations for serialized rows."""

    if state is None:
        return ("state_missing",)
    violations: list[str] = []
    valid = _state_bool(state, "score_valid")
    marker = _state_invalid_score_marker(state)
    visible_value = _state_primary_visible_score(state)
    if marker:
        if valid is True:
            if _state_text(state, "score_blocked_reason"):
                violations.append("valid_block_reason_present")
            for key in (*_RAW_BLOCK_SCORE_KEYS, "raw_score_before_block"):
                if _state_value(state, key) not in (None, ""):
                    violations.append(f"valid_raw_block_marker_present:{key}")
        for key in (*_VISIBLE_SCORE_ALIAS_KEYS, *_COMPAT_SCORE_KEYS):
            if _state_value(state, key) not in (None, ""):
                if key == "visible_score":
                    violations.append("invalid_visible_score_present")
                elif key in _VISIBLE_SCORE_ALIAS_KEYS:
                    violations.append(f"invalid_visible_score_alias_present:{key}")
                else:
                    violations.append(f"invalid_compat_score_present:{key}")
    elif valid is True:
        conflict = _score_alias_conflict_marker(state)
        visible_not_numeric = visible_value not in (None, "") and _score_numeric_value(visible_value) is None
        if conflict and not (conflict == "score_alias_not_numeric" and visible_not_numeric):
            violations.append(conflict)
        if visible_value in (None, ""):
            violations.append("valid_visible_score_missing")
        else:
            visible_numeric = _score_numeric_value(visible_value)
            if visible_numeric is None:
                violations.append("valid_visible_score_not_numeric")
            else:
                for key in (*_VISIBLE_SCORE_ALIAS_KEYS, *_COMPAT_SCORE_KEYS):
                    value = _state_value(state, key)
                    if value in (None, ""):
                        continue
                    numeric = _score_numeric_value(value)
                    if numeric is None:
                        violations.append(f"valid_score_alias_not_numeric:{key}")
                    elif abs(numeric - visible_numeric) > 1e-9:
                        violations.append(f"valid_score_alias_mismatch:{key}")
        for key in (*_RAW_BLOCK_SCORE_KEYS, "raw_score_before_block"):
            if _state_value(state, key) not in (None, ""):
                violations.append(f"valid_raw_block_marker_present:{key}")
        if _valid_high_confidence_row_has_claim_backed_gap(state):
            violations.append("valid_high_confidence_claim_backed_gap")
        if _valid_high_confidence_row_missing_score_contribution_claim_ids(state):
            violations.append("valid_high_confidence_score_contribution_claim_ids_missing")
        if _valid_high_confidence_row_missing_score_contribution_ledger(state):
            violations.append("valid_high_confidence_score_contribution_ledger_missing")
        if _valid_high_confidence_row_missing_claim_ledger_ids(state):
            violations.append("valid_high_confidence_claim_ledger_ids_missing")
        if _valid_high_confidence_row_has_unknown_score_contribution_claim_ids(state):
            violations.append("valid_high_confidence_score_contribution_claim_ids_unknown")
        if _valid_stage3_green_has_present_guard_primitives(state):
            violations.append("valid_stage3_green_guard_primitives_present")
        if _valid_stage3_green_has_unverified_guard_primitives(state):
            violations.append("valid_stage3_green_guard_primitives_unverified")
    return tuple(violations)


def score_state_output_contract_violations(state: Mapping[str, object] | object | None) -> tuple[str, ...]:
    """Return score-state violations for user-facing output rows."""

    violations = list(score_state_contract_violations(state))
    if isinstance(state, Mapping) and _output_row_missing_visible_score_field(state):
        violations.append("visible_score_field_missing")
    return tuple(violations)


def find_score_state_contract_violations(
    value: object,
    *,
    path: str = "$",
    include_score_only: bool = False,
    require_visible_score_field: bool = False,
    max_findings: int = 100,
) -> tuple[ScoreStateContractFinding, ...]:
    """Recursively find score-state contract violations in serialized output."""

    findings: list[ScoreStateContractFinding] = []
    _collect_score_state_contract_violations(
        value,
        path=path,
        include_score_only=include_score_only,
        require_visible_score_field=require_visible_score_field,
        max_findings=max_findings,
        findings=findings,
    )
    return tuple(findings)


def _normalized_blocked_score_payload(
    payload: dict[str, object],
    reason: str,
    *,
    force_invalid: bool = False,
) -> dict[str, object]:
    payload["visible_score"] = None
    for key in (*_VISIBLE_SCORE_ALIAS_KEYS, *_COMPAT_SCORE_KEYS):
        if key in payload:
            payload[key] = None
    if force_invalid or "score_valid" in payload or reason != "score_valid_missing":
        payload["score_valid"] = False
    if reason and not _state_text(payload, "score_blocked_reason"):
        payload["score_blocked_reason"] = reason
    return payload


def score_fingerprint(score: ScoreSnapshot | None) -> str | None:
    if score is None:
        return None
    payload = {
        "symbol": score.symbol,
        "as_of_date": score.as_of_date.isoformat(),
        "scoring_version": score.scoring_version,
        "evidence_ids": tuple(sorted(score.evidence_ids)),
        "diagnostic_scores": {key: score.diagnostic_scores[key] for key in sorted(score.diagnostic_scores)},
        "component_scores": {
            "eps_fcf_explosion": score.eps_fcf_explosion_score,
            "earnings_visibility": score.earnings_visibility_score,
            "bottleneck_pricing": score.bottleneck_pricing_score,
            "market_mispricing": score.market_mispricing_score,
            "valuation_rerating": score.valuation_rerating_score,
            "capital_allocation": score.capital_allocation_score,
            "information_confidence": score.information_confidence_score,
            "risk_penalty": score.risk_penalty,
            "total_score": score.total_score,
        },
    }
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.blake2s(encoded, digest_size=12).hexdigest()


def research_input_fingerprint(
    *,
    score: ScoreSnapshot | None = None,
    evidence: Sequence[Any] = (),
    queries: Sequence[str] = (),
    route_diagnostics: Mapping[str, object] | None = None,
    input_counts: Mapping[str, int] | None = None,
    source_fields: Mapping[str, object] | None = None,
    extra: Mapping[str, object] | None = None,
) -> str:
    """Fingerprint the input bundle that can make the same symbol score differently."""

    payload = {
        "score_symbol": score.symbol if score is not None else None,
        "score_as_of_date": score.as_of_date.isoformat() if score is not None else None,
        "score_evidence_ids": tuple(sorted(score.evidence_ids)) if score is not None else (),
        "evidence": tuple(sorted((_evidence_fingerprint_row(item) for item in evidence), key=lambda row: row["sort_key"])),
        "queries": tuple(str(item) for item in queries),
        "route_diagnostics": _stable_json_value(route_diagnostics or {}),
        "input_counts": _stable_json_value(input_counts or {}),
        "source_fields": _stable_json_value(source_fields or {}),
        "extra": _stable_json_value(extra or {}),
    }
    return _stable_digest(payload)


def score_variability_drivers(
    score: ScoreSnapshot | None,
    *,
    score_valid: bool | None = None,
    blocked_reason: str | None = None,
    route_diagnostics: Mapping[str, object] | None = None,
    input_counts: Mapping[str, int] | None = None,
    evidence_count: int | None = None,
    expansion_query_count: int | None = None,
    scoring_canonical_archetype_id: str | None = None,
    input_fingerprint: str | None = None,
) -> tuple[str, ...]:
    """Explain why a visible score can differ across otherwise similar runs."""

    valid = is_score_valid(score) if score_valid is None else score_valid
    reason = blocked_reason or score_block_reason(score)
    diagnostics = dict(score.diagnostic_scores) if score is not None else {}
    route = dict(route_diagnostics or {})
    drivers: list[str] = []
    if not valid:
        drivers.append(f"score_invalid:{reason or 'score_invalid'}")
    raw_total = raw_score_total_before_block(score)
    if raw_total is not None:
        drivers.append(f"raw_score_before_block:{raw_total:g}")
    _append_component_state_driver(drivers, score)
    _append_route_drivers(
        drivers,
        route,
        blocked_reason=reason,
        scoring_canonical_archetype_id=scoring_canonical_archetype_id,
    )
    _append_estimate_drivers(drivers, diagnostics)
    _append_input_count_drivers(drivers, input_counts or {})
    if evidence_count is not None:
        drivers.append(f"evidence_count:{evidence_count}")
        if evidence_count <= 0:
            drivers.append("input_missing:evidence")
    if score is not None and not score.evidence_ids:
        drivers.append("score_evidence_missing")
    if score is not None:
        drivers.append(f"score_evidence_count:{len(score.evidence_ids)}")
    _append_claim_contribution_drivers(drivers, diagnostics)
    if expansion_query_count is not None:
        drivers.append(f"llm_expansion_query_count:{expansion_query_count}")
        if expansion_query_count <= 0:
            drivers.append("llm_expansion_query_count:0")
    if input_fingerprint:
        drivers.append(f"research_input_fingerprint:{input_fingerprint}")
    post_gap_count = _route_num(route.get("post_score_gap_expansion_count"))
    post_gap_status = str(route.get("post_score_gap_expansion_status") or "").strip()
    if post_gap_status and post_gap_count <= 0.0 and post_gap_status not in {"disabled", "no_gaps"}:
        drivers.append(f"score_gap_expansion_status:{post_gap_status}")
    return tuple(dict.fromkeys(drivers))


def _append_claim_contribution_drivers(drivers: list[str], diagnostics: Mapping[str, object]) -> None:
    for diagnostic_key, label in (
        ("claim_backed_claim_count_capped", "claim_backed_claim_count"),
        ("claim_backed_primitive_count_capped", "claim_backed_primitive_count"),
        ("score_claim_backed_component_count_capped", "score_claim_backed_component_count"),
        ("orphan_score_component_count_capped", "orphan_score_component_count"),
        ("score_claim_backed_component_ratio", "score_claim_backed_component_ratio"),
    ):
        value = _route_num(diagnostics.get(diagnostic_key))
        if value > 0.0 or diagnostic_key in diagnostics:
            drivers.append(f"{label}:{value:g}")


def _evidence_fingerprint_row(item: Any) -> Mapping[str, object]:
    evidence_id = str(getattr(item, "evidence_id", "") or "")
    source_type = str(getattr(item, "source_type", "") or "")
    source_name = str(getattr(item, "source_name", "") or "")
    symbol = str(getattr(item, "symbol", "") or "")
    title = str(getattr(item, "title", "") or "")
    url = str(getattr(item, "url_or_identifier", "") or "")
    published_at = getattr(item, "published_at", None)
    available_at = getattr(item, "available_at", None)
    excerpt = getattr(item, "excerpt_or_value", None)
    parsed_fields = getattr(item, "parsed_fields", {})
    sort_key = "|".join((evidence_id, source_type, symbol, url, title))
    return {
        "sort_key": sort_key,
        "evidence_id": evidence_id,
        "source_type": source_type,
        "source_name": source_name,
        "symbol": symbol,
        "title": title,
        "url": url,
        "published_at": _stable_json_value(published_at),
        "available_at": _stable_json_value(available_at),
        "excerpt_digest": _stable_digest(_stable_json_value(excerpt)) if excerpt is not None else None,
        "parsed_fields": _stable_json_value(parsed_fields),
    }


def _stable_digest(payload: object) -> str:
    encoded = json.dumps(_stable_json_value(payload), ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.blake2s(encoded, digest_size=12).hexdigest()


def _stable_json_value(value: object) -> object:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Mapping):
        return {str(key): _stable_json_value(item) for key, item in sorted(value.items(), key=lambda pair: str(pair[0]))}
    if isinstance(value, (list, tuple)):
        return [_stable_json_value(item) for item in value]
    if isinstance(value, (set, frozenset)):
        return [_stable_json_value(item) for item in sorted(value, key=lambda item: str(item))]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return str(value)


def _score_state_comparison_status(
    *,
    before: Mapping[str, object] | object | None,
    after: Mapping[str, object] | object | None,
    before_visible: float | None,
    after_visible: float | None,
    delta: float | None,
    materiality: float,
    score_fingerprint_before: str | None,
    score_fingerprint_after: str | None,
    research_input_fingerprint_before: str | None,
    research_input_fingerprint_after: str | None,
    score_valid_before: bool | None,
    score_valid_after: bool | None,
) -> str:
    if before is None:
        return "missing_before_state"
    if after is None:
        return "missing_after_state"
    if score_valid_before is not True and score_valid_after is True:
        return "score_became_valid"
    if score_valid_before is True and score_valid_after is not True:
        return "score_became_invalid"
    if score_valid_before is True and score_valid_after is True and before_visible is None and after_visible is not None:
        return "visible_score_missing_before"
    if score_valid_before is True and score_valid_after is True and before_visible is not None and after_visible is None:
        return "visible_score_missing_after"
    if score_valid_before is True and score_valid_after is True and before_visible is None and after_visible is None:
        return "visible_score_missing_both"
    changed = delta is not None and abs(delta) >= materiality
    if score_fingerprint_before and score_fingerprint_after and score_fingerprint_before == score_fingerprint_after:
        return "same_score_snapshot" if not changed else "inconsistent_output_same_score_fingerprint"
    if not changed and score_valid_before == score_valid_after:
        return "same_visible_score"
    if research_input_fingerprint_before and research_input_fingerprint_after:
        if research_input_fingerprint_before != research_input_fingerprint_after:
            return "input_changed"
        if score_fingerprint_before and score_fingerprint_after and score_fingerprint_before != score_fingerprint_after:
            return "scoring_changed_same_input"
        return "same_input_unclassified_score_change"
    return "fingerprint_missing"


def _state_visible_score(state: Mapping[str, object] | object | None) -> tuple[float | None, str | None]:
    invalid_marker = _state_invalid_score_marker(state)
    if invalid_marker:
        if _state_value(state, "visible_score") not in (None, ""):
            return None, f"visible_score_ignored_{invalid_marker}"
        return None, f"{invalid_marker}_without_visible_score"
    conflict_marker = _score_alias_conflict_marker(state)
    if conflict_marker:
        if _state_value(state, "visible_score") not in (None, ""):
            return None, f"visible_score_ignored_{conflict_marker}"
        return None, f"{conflict_marker}_without_visible_score"
    for key in _VISIBLE_SCORE_ALIAS_KEYS:
        value = _state_value(state, key)
        if value in (None, ""):
            continue
        try:
            return float(value), key
        except (TypeError, ValueError):
            return None, key
    if any(_state_value(state, key) not in (None, "") for key in _COMPAT_SCORE_KEYS):
        return None, "compat_score_without_visible_score"
    return None, None


def _state_primary_visible_score(state: Mapping[str, object] | object | None) -> object | None:
    for key in _VISIBLE_SCORE_ALIAS_KEYS:
        value = _state_value(state, key)
        if value not in (None, ""):
            return value
    return None


def _append_visible_score_source_driver(drivers: list[str], side: str, source: str | None) -> None:
    if not source or source == "visible_score":
        return
    if "ignored" in source or source.endswith("_without_visible_score"):
        drivers.append(f"{side}_visible_score_ignored:{source}")
        return
    drivers.append(f"{side}_visible_score_alias:{source}")


def _append_contract_violation_drivers(
    drivers: list[str],
    side: str,
    state: Mapping[str, object] | object | None,
) -> None:
    if state is None:
        return
    for violation in score_state_contract_violations(state)[:5]:
        drivers.append(f"{side}_score_state_contract:{violation}")


def _collect_score_state_contract_violations(
    value: object,
    *,
    path: str,
    include_score_only: bool,
    require_visible_score_field: bool,
    max_findings: int,
    findings: list[ScoreStateContractFinding],
) -> None:
    if len(findings) >= max_findings:
        return
    if isinstance(value, Mapping):
        if _should_audit_score_state_mapping(value, include_score_only=include_score_only):
            violations = list(score_state_contract_violations(value))
            if require_visible_score_field and _output_row_missing_visible_score_field(value):
                violations.append("visible_score_field_missing")
            for violation in violations:
                findings.append(ScoreStateContractFinding(path=path, violation=violation))
                if len(findings) >= max_findings:
                    return
        for key, item in value.items():
            _collect_score_state_contract_violations(
                item,
                path=f"{path}.{_path_key(key)}",
                include_score_only=include_score_only,
                require_visible_score_field=require_visible_score_field,
                max_findings=max_findings,
                findings=findings,
            )
            if len(findings) >= max_findings:
                return
        return
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        for index, item in enumerate(value):
            _collect_score_state_contract_violations(
                item,
                path=f"{path}[{index}]",
                include_score_only=include_score_only,
                require_visible_score_field=require_visible_score_field,
                max_findings=max_findings,
                findings=findings,
            )
            if len(findings) >= max_findings:
                return


def _should_audit_score_state_mapping(state: Mapping[str, object], *, include_score_only: bool) -> bool:
    score_keys_present = any(key in state for key in (*_VISIBLE_SCORE_ALIAS_KEYS, *_COMPAT_SCORE_KEYS))
    if not score_keys_present:
        return include_score_only and _state_has_any_score_state_marker(state) and _has_score_output_context(state)
    visible_keys_present = any(key in state for key in _VISIBLE_SCORE_ALIAS_KEYS)
    if visible_keys_present:
        return True
    if _state_has_any_score_state_marker(state):
        return True
    return include_score_only and _has_score_output_context(state)


def _has_score_output_context(state: Mapping[str, object]) -> bool:
    return any(
        key in state
        for key in (
            "symbol",
            "company",
            "company_name",
            "case_id",
            "as_of_date",
            "stage",
            "rank",
            "layer",
        )
    )


def _output_row_missing_visible_score_field(state: Mapping[str, object]) -> bool:
    if "visible_score" in state:
        return False
    if not _has_score_output_context(state):
        return False
    if _state_has_any_score_state_marker(state):
        return True
    return _state_has_any_score_value(state)


def _path_key(key: object) -> str:
    text = str(key).strip()
    if text.replace("_", "").replace("-", "").isalnum():
        return text
    return json.dumps(text, ensure_ascii=False)


def _state_invalid_score_marker(state: Mapping[str, object] | object | None) -> str | None:
    valid = _state_bool(state, "score_valid")
    reason = _state_text(state, "score_blocked_reason")
    if valid is True:
        if reason and reason.strip().lower() not in {"valid", "none"}:
            return "score_blocked_reason"
        for key in (*_RAW_BLOCK_SCORE_KEYS, "raw_score_before_block"):
            if _state_value(state, key) not in (None, ""):
                return _BLOCK_REASON_BY_RAW_KEY.get(key, "raw_score_before_block")
        return None
    if valid is False:
        return "score_valid_false"
    if reason and reason.strip().lower() not in {"valid", "none"}:
        return "score_blocked_reason"
    for key in (*_RAW_BLOCK_SCORE_KEYS, "raw_score_before_block"):
        if _state_value(state, key) not in (None, ""):
            return _BLOCK_REASON_BY_RAW_KEY.get(key, "raw_score_before_block")
    if _state_has_any_score_value(state):
        return "score_valid_missing"
    return None


def _score_alias_conflict_marker(state: Mapping[str, object] | object | None) -> str | None:
    if not _state_has_any_score_value(state):
        return None
    if _state_bool(state, "score_valid") is not True:
        return None
    visible_score = _state_value(state, "visible_score")
    if visible_score not in (None, ""):
        if _score_numeric_value(visible_score) is None:
            return "score_alias_not_numeric"
        return None
    visible_aliases = _present_score_alias_keys(state, _VISIBLE_SCORE_ALIAS_KEYS)
    compat_aliases = _present_score_alias_keys(state, _COMPAT_SCORE_KEYS)
    aliases_to_check = visible_aliases or compat_aliases
    if not aliases_to_check:
        return None
    if any(_score_numeric_value(_state_value(state, key)) is None for key in aliases_to_check):
        return "score_alias_not_numeric"
    if len(aliases_to_check) >= 2 and _numeric_alias_values_conflict(state, aliases_to_check):
        return "score_alias_conflict"
    return None


def _present_score_alias_keys(state: Mapping[str, object] | object | None, keys: Sequence[str]) -> tuple[str, ...]:
    return tuple(key for key in keys if _state_value(state, key) not in (None, ""))


def _numeric_alias_values_conflict(state: Mapping[str, object] | object | None, keys: Sequence[str]) -> bool:
    values = tuple(_score_numeric_value(_state_value(state, key)) for key in keys)
    numeric_values = tuple(value for value in values if value is not None)
    if not numeric_values:
        return False
    baseline = numeric_values[0]
    return any(abs(value - baseline) > 1e-9 for value in numeric_values[1:])


def _state_has_any_score_state_marker(state: Mapping[str, object] | object | None) -> bool:
    if _state_value(state, "score_valid") not in (None, ""):
        return True
    if _state_text(state, "score_blocked_reason"):
        return True
    for key in (*_RAW_BLOCK_SCORE_KEYS, "raw_score_before_block"):
        if _state_value(state, key) not in (None, ""):
            return True
    return False


def _state_has_any_score_value(state: Mapping[str, object] | object | None) -> bool:
    for key in (*_VISIBLE_SCORE_ALIAS_KEYS, *_COMPAT_SCORE_KEYS):
        if _state_value(state, key) not in (None, ""):
            return True
    return False


def _valid_high_confidence_row_has_claim_backed_gap(state: Mapping[str, object] | object | None) -> bool:
    if _state_bool(state, "score_valid") is not True:
        return False
    if not _state_requires_claim_backed_high_confidence_score(state):
        return False
    if not _state_is_high_confidence_candidate_score(state):
        return False
    claim_count = _score_numeric_value(_state_value(state, "claim_backed_claim_count"))
    if claim_count is None:
        claim_count = _score_numeric_value(_state_value(state, "claim_backed_claim_count_capped"))
    ratio = _score_numeric_value(_state_value(state, "score_claim_backed_component_ratio"))
    orphan_count = _score_numeric_value(_state_value(state, "orphan_score_component_count"))
    if orphan_count is None:
        orphan_count = _score_numeric_value(_state_value(state, "orphan_score_component_count_capped"))
    return (claim_count is not None and claim_count <= 0.0) or (ratio is not None and ratio < 100.0) or (
        orphan_count is not None and orphan_count > 0.0
    )


def _valid_high_confidence_row_missing_score_contribution_claim_ids(
    state: Mapping[str, object] | object | None,
) -> bool:
    if _state_bool(state, "score_valid") is not True:
        return False
    if not _state_requires_claim_backed_high_confidence_score(state):
        return False
    if not _state_is_high_confidence_candidate_score(state):
        return False
    contribution_claims = _state_score_contribution_claim_ids(state)
    if not contribution_claims:
        return True
    nonzero_components = tuple(
        component
        for component, value in _state_component_scores(state).items()
        if value > 0.0
    )
    if not nonzero_components:
        return False
    return any(component not in contribution_claims for component in nonzero_components)


def _valid_high_confidence_row_missing_score_contribution_ledger(
    state: Mapping[str, object] | object | None,
) -> bool:
    if _state_bool(state, "score_valid") is not True:
        return False
    if not _state_requires_claim_backed_high_confidence_score(state):
        return False
    if not _state_is_high_confidence_candidate_score(state):
        return False
    ledger = _state_score_contribution_ledger(state)
    if not ledger:
        return True
    nonzero_components = tuple(
        component
        for component, value in _state_component_scores(state).items()
        if value > 0.0
    )
    if not nonzero_components:
        return False
    return any(component not in ledger or not ledger[component] for component in nonzero_components)


def _valid_high_confidence_row_missing_claim_ledger_ids(
    state: Mapping[str, object] | object | None,
) -> bool:
    if _state_bool(state, "score_valid") is not True:
        return False
    if not _state_requires_claim_backed_high_confidence_score(state):
        return False
    if not _state_is_high_confidence_candidate_score(state):
        return False
    return not _state_claim_ledger_claim_ids(state)


def _valid_high_confidence_row_has_unknown_score_contribution_claim_ids(
    state: Mapping[str, object] | object | None,
) -> bool:
    if _state_bool(state, "score_valid") is not True:
        return False
    if not _state_requires_claim_backed_high_confidence_score(state):
        return False
    if not _state_is_high_confidence_candidate_score(state):
        return False
    known_claim_ids = set(_state_claim_ledger_claim_ids(state))
    if not known_claim_ids:
        return False
    referenced_claim_ids: set[str] = set()
    for claim_ids in _state_score_contribution_claim_ids(state).values():
        referenced_claim_ids.update(claim_ids)
    for claim_ids in _state_score_contribution_ledger(state).values():
        referenced_claim_ids.update(claim_ids)
    return bool(referenced_claim_ids - known_claim_ids)


def _valid_stage3_green_has_unverified_guard_primitives(state: Mapping[str, object] | object | None) -> bool:
    if _state_bool(state, "score_valid") is not True:
        return False
    stage = str(_state_value(state, "stage") or _state_value(state, "merged_stage") or "").strip()
    if stage != "3-Green":
        return False
    guard_missing = _score_numeric_value(_state_value(state, "evidence_contract_guard_missing_primitive_count"))
    if guard_missing is None:
        guard_missing = _score_numeric_value(
            _state_value(state, "evidence_contract_guard_missing_primitive_count_capped")
        )
    return guard_missing is not None and guard_missing > 0.0


def _valid_stage3_green_has_present_guard_primitives(state: Mapping[str, object] | object | None) -> bool:
    if _state_bool(state, "score_valid") is not True:
        return False
    stage = str(_state_value(state, "stage") or _state_value(state, "merged_stage") or "").strip()
    if stage != "3-Green":
        return False
    guard_present = _score_numeric_value(_state_value(state, "evidence_contract_guard_present_primitive_count"))
    if guard_present is None:
        guard_present = _score_numeric_value(
            _state_value(state, "evidence_contract_guard_present_primitive_count_capped")
        )
    return guard_present is not None and guard_present > 0.0


def _state_requires_claim_backed_high_confidence_score(state: Mapping[str, object] | object | None) -> bool:
    return any(
        (_score_numeric_value(_state_value(state, key)) or 0.0) > 0.0
        for key in (
            "score_claim_backed_required",
            "source_backed_green_bridge_raw",
            "source_backed_deep_research_completed",
            "evidence_contract_required_primitive_count",
            "evidence_contract_required_primitive_count_capped",
            "evidence_contract_green_gate_required_primitive_count",
            "evidence_contract_green_gate_required_primitive_count_capped",
        )
    )


def _state_is_high_confidence_candidate_score(state: Mapping[str, object] | object | None) -> bool:
    stage = str(_state_value(state, "stage") or _state_value(state, "merged_stage") or "").strip()
    if stage in {"3-Green", "3-Yellow"}:
        return True
    visible = serialized_visible_score(state)
    return visible is not None and visible >= 65.0


def _score_numeric_value(value: object) -> float | None:
    if value in (None, ""):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _score_state_rows_by_key(
    rows: Sequence[Mapping[str, object] | object],
    *,
    key_fields: Sequence[str],
) -> Mapping[str, Mapping[str, object] | object]:
    keyed: dict[str, Mapping[str, object] | object] = {}
    seen: dict[str, int] = {}
    for index, row in enumerate(rows):
        base_key = _score_state_row_key(row, index=index, key_fields=key_fields)
        count = seen.get(base_key, 0) + 1
        seen[base_key] = count
        key = base_key if count == 1 else f"{base_key}#{count}"
        keyed[key] = row
    return keyed


def _score_state_row_key(
    row: Mapping[str, object] | object,
    *,
    index: int,
    key_fields: Sequence[str],
) -> str:
    for field in key_fields:
        value = _state_value(row, field)
        if value in (None, ""):
            continue
        text = str(value).strip()
        if text:
            return text
    return f"row:{index}"


def _state_component_scores(state: Mapping[str, object] | object | None) -> Mapping[str, float]:
    for key in ("component_scores", "score_components"):
        value = _state_value(state, key)
        if not isinstance(value, Mapping):
            continue
        row: dict[str, float] = {}
        for item_key, item_value in value.items():
            if item_value in (None, ""):
                continue
            try:
                row[_component_key(item_key)] = float(item_value)
            except (TypeError, ValueError):
                continue
        return row
    row = {}
    for field_key, component_key in _COMPONENT_SCORE_FIELD_KEYS.items():
        value = _state_value(state, field_key)
        if value in (None, ""):
            continue
        try:
            row[component_key] = float(value)
        except (TypeError, ValueError):
            continue
    if row:
        return row
    return {}


def _state_score_contribution_claim_ids(state: Mapping[str, object] | object | None) -> Mapping[str, tuple[str, ...]]:
    value = _state_value(state, "score_contribution_claim_ids")
    if isinstance(value, str):
        text = value.strip()
        if not text:
            return {}
        try:
            value = json.loads(text)
        except json.JSONDecodeError:
            return {}
    if not isinstance(value, Mapping):
        return {}
    row: dict[str, tuple[str, ...]] = {}
    for key, raw_ids in value.items():
        component = _component_key(key)
        if not component:
            continue
        if isinstance(raw_ids, str):
            claim_ids = (raw_ids,)
        elif isinstance(raw_ids, Sequence):
            claim_ids = tuple(str(item) for item in raw_ids)
        else:
            claim_ids = ()
        clean = tuple(dict.fromkeys(item.strip() for item in claim_ids if item.strip()))
        if clean:
            row[component] = clean
    return row


def _state_score_contribution_ledger(state: Mapping[str, object] | object | None) -> Mapping[str, tuple[str, ...]]:
    value = _state_value(state, "score_contribution_ledger")
    if isinstance(value, str):
        text = value.strip()
        if not text:
            return {}
        try:
            value = json.loads(text)
        except json.JSONDecodeError:
            return {}
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes, bytearray)):
        return {}
    row: dict[str, tuple[str, ...]] = {}
    for item in value:
        if not isinstance(item, Mapping):
            continue
        component = _component_key(item.get("component_key") or item.get("criterion_id") or "")
        if not component:
            continue
        raw_points = _score_numeric_value(item.get("raw_points"))
        if raw_points is not None and raw_points <= 0.0:
            continue
        raw_claims = item.get("support_claim_ids")
        if isinstance(raw_claims, str):
            claim_ids = (raw_claims,)
        elif isinstance(raw_claims, Sequence):
            claim_ids = tuple(str(claim) for claim in raw_claims)
        else:
            claim_ids = ()
        clean = tuple(dict.fromkeys(claim.strip() for claim in claim_ids if claim.strip()))
        if clean:
            row[component] = clean
    return row


def _state_claim_ledger_claim_ids(state: Mapping[str, object] | object | None) -> tuple[str, ...]:
    claim_ids: list[str] = []
    for key in ("claim_ledger_claim_ids", "claim_ledger_score_eligible_claim_ids", "compiled_claim_ids"):
        claim_ids.extend(_claim_id_values(_state_value(state, key)))
    for key in ("claim_ledger_claim_ids_by_primitive", "compiled_claim_ids_by_primitive"):
        value = _json_state_value(_state_value(state, key))
        if not isinstance(value, Mapping):
            continue
        for raw_claims in value.values():
            claim_ids.extend(_claim_id_values(raw_claims))
    compiled_claims = _json_state_value(_state_value(state, "compiled_claims"))
    if isinstance(compiled_claims, list):
        for item in compiled_claims:
            if isinstance(item, Mapping):
                claim_ids.extend(_claim_id_values(item.get("claim_id")))
    return tuple(dict.fromkeys(claim_id for claim_id in claim_ids if claim_id))


def _claim_id_values(value: object) -> tuple[str, ...]:
    if value in (None, ""):
        return ()
    parsed = _json_state_value(value)
    if parsed in (None, ""):
        return ()
    if isinstance(parsed, Mapping):
        return ()
    if isinstance(parsed, str):
        raw_values = parsed.split(",")
    elif isinstance(parsed, (list, tuple)):
        raw_values = parsed
    else:
        raw_values = (parsed,)
    return tuple(dict.fromkeys(str(item).strip() for item in raw_values if str(item).strip()))


def _json_state_value(value: object) -> object:
    if not isinstance(value, str):
        return value
    text = value.strip()
    if not text or not text.startswith(("[", "{")):
        return value
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return value


def _component_score_deltas(
    before: Mapping[str, float],
    after: Mapping[str, float],
    *,
    materiality: float,
) -> Mapping[str, float]:
    deltas: dict[str, float] = {}
    for key in sorted(before.keys() & after.keys()):
        delta = after[key] - before[key]
        if abs(delta) >= materiality:
            deltas[key] = delta
    return deltas


def _component_key(key: object) -> str:
    text = str(key).strip()
    return text.removesuffix("_score")


def _append_variability_driver_changes(
    drivers: list[str],
    before: Mapping[str, object] | object | None,
    after: Mapping[str, object] | object | None,
) -> None:
    before_values = set(_state_variability_drivers(before))
    after_values = set(_state_variability_drivers(after))
    for item in sorted(after_values - before_values)[:5]:
        drivers.append(f"variability_driver_added:{_short_driver_text(item)}")
    for item in sorted(before_values - after_values)[:5]:
        drivers.append(f"variability_driver_removed:{_short_driver_text(item)}")


def _state_variability_drivers(state: Mapping[str, object] | object | None) -> tuple[str, ...]:
    value = _state_value(state, "score_variability_drivers")
    if value in (None, ""):
        return ()
    if isinstance(value, str):
        if "|" in value:
            return tuple(item.strip() for item in value.split("|") if item.strip())
        return (value,)
    if isinstance(value, Sequence) and not isinstance(value, (bytes, bytearray)):
        return tuple(str(item) for item in value if str(item))
    return (str(value),)


def _state_bool(state: Mapping[str, object] | object | None, key: str) -> bool | None:
    value = _state_value(state, key)
    if value is None or value == "":
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return float(value) > 0.0
    text = str(value).strip().lower()
    if text in {"true", "1", "yes", "y"}:
        return True
    if text in {"false", "0", "no", "n"}:
        return False
    try:
        return float(text) > 0.0
    except ValueError:
        return None


def _state_text(state: Mapping[str, object] | object | None, key: str) -> str | None:
    value = _state_value(state, key)
    if value in (None, ""):
        return None
    return str(value)


def _state_value(state: Mapping[str, object] | object | None, key: str) -> object | None:
    if state is None:
        return None
    if isinstance(state, Mapping):
        return state.get(key)
    return getattr(state, key, None)


def _append_component_state_driver(drivers: list[str], score: ScoreSnapshot | None) -> None:
    if score is None or not is_score_valid(score):
        return
    drivers.append(
        "score_components:"
        f"eps_fcf={score.eps_fcf_explosion_score:g},"
        f"visibility={score.earnings_visibility_score:g},"
        f"bottleneck={score.bottleneck_pricing_score:g},"
        f"mispricing={score.market_mispricing_score:g},"
        f"valuation={score.valuation_rerating_score:g},"
        f"capital={score.capital_allocation_score:g},"
        f"confidence={score.information_confidence_score:g},"
        f"risk={score.risk_penalty:g},"
        f"total={score.total_score:g}"
    )


def _append_route_drivers(
    drivers: list[str],
    route: Mapping[str, object],
    *,
    blocked_reason: str | None,
    scoring_canonical_archetype_id: str | None,
) -> None:
    _append_route_state_driver(
        drivers,
        route,
        scoring_canonical_archetype_id=scoring_canonical_archetype_id,
    )
    if blocked_reason and str(blocked_reason).startswith("score_gap"):
        drivers.append(f"score_gap_blocked:{blocked_reason}")
    theme_rebalance_status = str(route.get("theme_rebalance_status") or "").strip()
    if theme_rebalance_status and theme_rebalance_status != "completed":
        drivers.append(f"theme_rebalance_status:{theme_rebalance_status}")
    theme_route_status = str(route.get("theme_route_status") or "").strip()
    if theme_route_status and theme_route_status not in {"transition_detected", "mixed_route", "no_transition"}:
        drivers.append(f"theme_route_status:{theme_route_status}")
    gate_status = str(route.get("theme_evidence_gate_status") or "").strip()
    if gate_status and gate_status != "source_backed":
        drivers.append(f"theme_evidence_gate_status:{gate_status}")
    theme_route = route.get("canonical_archetype_id")
    if theme_route and scoring_canonical_archetype_id and str(theme_route) != scoring_canonical_archetype_id:
        drivers.append("route_mismatch:theme_vs_scoring_archetype")
    if route.get("post_score_gap_blocked_reason"):
        drivers.append(f"score_gap_blocked:{route.get('post_score_gap_blocked_reason')}")
    if route.get("post_score_gap_warning_reason"):
        drivers.append(f"score_gap_warning:{route.get('post_score_gap_warning_reason')}")
    unresolved_gaps = route.get("post_score_gap_unresolved_gaps") or ()
    if isinstance(unresolved_gaps, (str, bytes)):
        unresolved_gaps = (unresolved_gaps,)
    for gap in tuple(unresolved_gaps)[:5]:
        drivers.append(f"score_gap_unresolved:{_short_driver_text(gap)}")


def _append_route_state_driver(
    drivers: list[str],
    route: Mapping[str, object],
    *,
    scoring_canonical_archetype_id: str | None,
) -> None:
    route_parts: list[str] = []
    for key, label in (
        ("theme_rebalance_status", "rebalance"),
        ("theme_route_status", "route"),
        ("theme_evidence_gate_status", "gate"),
        ("large_sector_id", "sector"),
        ("canonical_archetype_id", "route_archetype"),
    ):
        value = str(route.get(key) or "").strip()
        if value:
            route_parts.append(f"{label}={_short_driver_text(value)}")
    if scoring_canonical_archetype_id:
        route_parts.append(f"scoring_archetype={_short_driver_text(scoring_canonical_archetype_id)}")
    if route_parts:
        drivers.append(f"route_state:{'|'.join(route_parts)}")


def _append_estimate_drivers(drivers: list[str], diagnostics: Mapping[str, object]) -> None:
    for key, label in (
        ("estimate_missing_eps_source", "eps"),
        ("estimate_missing_fcf_source", "fcf"),
        ("estimate_missing_revision_source", "revision"),
        ("estimate_missing_op_source", "op"),
    ):
        if _diagnostic_value(diagnostics.get(key)) > 0.0:
            drivers.append(f"estimate_source_missing:{label}")
    for key in ("estimate_conflict_count_capped", "estimate_proxy_quarantined_count_capped", "estimate_revision_outlier_count_capped"):
        value = _diagnostic_value(diagnostics.get(key))
        if value > 0.0:
            drivers.append(f"estimate_quality:{key}={value:g}")


def _append_input_count_drivers(drivers: list[str], input_counts: Mapping[str, int]) -> None:
    for key, label in (
        ("price_bars", "price_bar"),
        ("financial_actuals", "financial_actual"),
        ("research_reports", "research_report"),
        ("news_items", "news_item"),
        ("consensus", "consensus"),
        ("consensus_revisions", "consensus_revision"),
        ("agent_extracted_fields", "agent_extracted_field"),
    ):
        if key not in input_counts:
            continue
        count = int(input_counts.get(key, 0) or 0)
        drivers.append(f"input_count:{label}={count}")
        if count <= 0:
            drivers.append(f"input_missing:{label}")


def _short_driver_text(value: object) -> str:
    text = str(value).strip().replace("\n", " ")
    if len(text) <= 120:
        return text
    return f"{text[:117]}..."


def _route_num(value: object) -> float:
    if value in (None, ""):
        return 0.0
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def _diagnostic_value(value: object) -> float:
    return diagnostic_value(value)


__all__ = [
    "ScoreStateComparison",
    "ScoreStateContractFinding",
    "ScoreStateRowChange",
    "compare_score_state_rows",
    "compare_score_states",
    "find_score_state_contract_violations",
    "is_score_valid",
    "normalized_score_alias_value",
    "normalized_score_state_mapping_if_present",
    "normalized_score_state_payload",
    "raw_score_total_before_block",
    "score_block_reason",
    "score_fingerprint",
    "score_state_contract_violations",
    "score_state_output_contract_violations",
    "score_variability_drivers",
    "serialized_score_block_reason",
    "serialized_score_valid",
    "serialized_visible_score",
    "visible_score_total",
]
