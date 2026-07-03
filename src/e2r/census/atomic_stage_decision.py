"""Atomic stage decision builder for Census v4.

The central invariant is simple: a final CensusStageStatus row must not combine
stage from one StageCourt trace with score/status/claim IDs from another trace.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from e2r.evidence.primitive_semantic_guard import guard_score_contribution
from e2r.production.metadata import stable_hash


STAGE_NORMALIZATION = {
    "0": "Stage0",
    "1": "Stage1",
    "2": "Stage2-Watch",
    "3-Yellow": "Stage3-Yellow",
    "3-Green": "Stage3-Green",
    "3-Red": "Red",
    "Reject": "Reject",
    "Red": "Red",
    "Stage0": "Stage0",
    "Stage1": "Stage1",
    "Stage2-Watch": "Stage2-Watch",
    "Stage2-Actionable": "Stage2-Actionable",
    "Stage3-Yellow": "Stage3-Yellow",
    "Stage3-Green": "Stage3-Green",
}

CANONICAL_STAGE_BY_DISPLAY = {
    "Stage0": "0",
    "Stage1": "1",
    "Stage2-Watch": "2",
    "Stage2-Actionable": "2",
    "Stage3-Yellow": "3-Yellow",
    "Stage3-Green": "3-Green",
    "Stage3-Red": "3-Red",
    "Red": "3-Red",
    "Reject": "3-Red",
    "4A": "4A",
    "4B": "4B",
    "4C": "4C",
    "5": "5",
}


@dataclass(frozen=True)
class AtomicStageDecision:
    payload: Mapping[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return dict(self.payload)


def build_atomic_stage_decisions(
    *,
    symbol: str,
    company_name: str,
    as_of_date: str,
    stagecourt_traces: Sequence[Mapping[str, Any]],
    accepted_claims: Sequence[Mapping[str, Any]],
    score_contributions: Sequence[Mapping[str, Any]],
    primitive_states: Sequence[Mapping[str, Any]] = (),
    source_tasks: Sequence[Mapping[str, Any]] = (),
    source_task_executions: Sequence[Mapping[str, Any]] = (),
) -> list[dict[str, Any]]:
    claims_by_id = {str(row.get("claim_id")): row for row in accepted_claims}
    contributions_by_id = {str(row.get("score_contribution_id") or row.get("contribution_id")): row for row in score_contributions}
    primitive_ids_by_claim = _primitive_ids_by_claim(primitive_states)
    rows: list[dict[str, Any]] = []
    for trace in stagecourt_traces:
        trace_id = str(trace.get("stagecourt_trace_id") or trace.get("trace_id") or "")
        accepted_ids = _clean_ids(trace.get("accepted_claim_ids") or ())
        contribution_ids = _clean_ids(trace.get("score_contribution_ids") or ())
        trace_claims = [claims_by_id[item] for item in accepted_ids if item in claims_by_id]
        trace_contributions = [contributions_by_id[item] for item in contribution_ids if item in contributions_by_id]
        semantic = _semantic_guard(trace_contributions, claims_by_id)
        score_status = str(trace.get("score_status") or "NOT_SCORED")
        lower, upper = _score_interval(trace)
        score_allowed = semantic["score_allowed"]
        base_stage = normalize_stage(trace.get("base_stage"))
        if not score_allowed and base_stage not in {"Red", "Reject"}:
            base_stage = "Stage1"
        canonical_stage = canonical_stage_for_display(base_stage)
        event_score = lower if score_allowed and lower is not None else None
        decision_status = _stage_decision_status(base_stage=base_stage, score_status=score_status, score_allowed=score_allowed)
        stage_signal = _stage_signal(base_stage=base_stage, decision_status=decision_status, score_allowed=score_allowed)
        risk_signal = _risk_stage_signal(base_stage=base_stage)
        decision_id = "ATOMIC-" + stable_hash(
            {
                "symbol": symbol,
                "trace_id": trace_id,
                "accepted_claim_ids": accepted_ids,
                "score_contribution_ids": contribution_ids,
                "score_interval": trace.get("score_interval"),
                "semantic_guard": semantic,
            }
        )[:20]
        rows.append(
            {
                "schema_version": "e2r_census_v4_atomic_stage_decision_v1",
                "atomic_stage_decision_id": decision_id,
                "symbol": symbol,
                "company_name": company_name,
                "as_of_date": as_of_date,
                "candidate_event_id": trace.get("candidate_event_id"),
                "source_task_ids": _task_ids_for_event(source_tasks, trace.get("candidate_event_id")),
                "source_task_execution_ids": _task_ids_for_event(source_task_executions, trace.get("candidate_event_id")),
                "stagecourt_trace_id": trace_id,
                "base_stage": base_stage,
                "canonical_stage": canonical_stage,
                "stage_signal": stage_signal,
                "stage_scope": "CENSUS_EVENT_BOARD",
                "risk_stage_signal": risk_signal,
                "transition_overlay": "NONE",
                "stage_decision_status": decision_status,
                "score_scale": "EVENT_WEIGHTED_PARTIAL" if event_score is not None else "NO_SCORE",
                "score_scope": "EVENT_WEIGHTED_PARTIAL" if event_score is not None else "NO_SCORE",
                "score_source": "STAGECOURT_SCORE_INTERVAL" if event_score is not None else "NONE",
                "event_evidence_score": event_score,
                "full_e2r_verified_score": None,
                "raw_contribution_score": _raw_contribution_sum(trace_contributions) if score_allowed and trace_contributions else None,
                "score_interval_lower": lower if event_score is not None else None,
                "score_interval_upper": upper if event_score is not None else None,
                "score_valid_status": score_status if score_allowed else "INVALID_EVIDENCE",
                "accepted_claim_ids": accepted_ids if score_allowed else [],
                "blocked_claim_ids": accepted_ids if not score_allowed else [],
                "score_contribution_ids": contribution_ids if score_allowed else [],
                "blocked_score_contribution_ids": contribution_ids if not score_allowed else [],
                "primitive_state_ids": _primitive_state_ids_for_claims(accepted_ids, primitive_ids_by_claim) if score_allowed else [],
                "blocked_primitive_state_ids": _primitive_state_ids_for_claims(accepted_ids, primitive_ids_by_claim) if not score_allowed else [],
                "failed_stage_gates": [],
                "missing_primitives": list(trace.get("missing_green_primitives") or ()),
                "material_gap_ids": list(trace.get("missing_green_primitives") or ()) + list(trace.get("missing_yellow_primitives") or ()),
                "source_cutover_date": trace.get("source_cutover_date"),
                "is_representative": False,
                "additional_stage_decision_ids": [],
                "semantic_guard_status": semantic["semantic_guard_status"],
                "semantic_guard_class": semantic["semantic_guard_class"],
                "semantic_guard_reasons": semantic["semantic_guard_reasons"],
                "stage_decision_reason": trace.get("stage_decision_reason"),
            }
        )
    return rows


def _primitive_ids_by_claim(primitive_states: Sequence[Mapping[str, Any]]) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for state in primitive_states:
        primitive_state_id = str(state.get("primitive_state_id") or "")
        if not primitive_state_id:
            continue
        for key in ("support_claim_ids", "counter_claim_ids"):
            for claim_id in state.get(key) or ():
                claim_key = str(claim_id)
                if claim_key and primitive_state_id not in out.setdefault(claim_key, []):
                    out[claim_key].append(primitive_state_id)
    return out


def _primitive_state_ids_for_claims(claim_ids: Sequence[str], primitive_ids_by_claim: Mapping[str, Sequence[str]]) -> list[str]:
    out: list[str] = []
    for claim_id in claim_ids:
        for primitive_state_id in primitive_ids_by_claim.get(str(claim_id), ()):
            if primitive_state_id not in out:
                out.append(primitive_state_id)
    return out


def choose_representative_decision(decisions: Sequence[Mapping[str, Any]]) -> dict[str, Any] | None:
    if not decisions:
        return None
    ordered = sorted(decisions, key=_decision_sort_key, reverse=True)
    representative = dict(ordered[0])
    representative["is_representative"] = True
    representative["additional_stage_decision_ids"] = [
        str(row.get("atomic_stage_decision_id")) for row in ordered[1:] if row.get("atomic_stage_decision_id")
    ]
    return representative


def normalize_stage(value: Any) -> str:
    return STAGE_NORMALIZATION.get(str(value or ""), str(value or "Stage1"))


def canonical_stage_for_display(value: Any) -> str:
    display = normalize_stage(value)
    return CANONICAL_STAGE_BY_DISPLAY.get(display, str(value or "1"))


def _semantic_guard(
    contributions: Sequence[Mapping[str, Any]],
    claims_by_id: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    statuses: list[str] = []
    classes: list[str] = []
    reasons: list[str] = []
    allowed = True
    for contribution in contributions:
        support_claims = [claims_by_id[item] for item in _clean_ids(contribution.get("support_claim_ids") or ()) if item in claims_by_id]
        result = guard_score_contribution(contribution=contribution, support_claims=support_claims)
        statuses.append(str(result["semantic_guard_status"]))
        classes.append(str(result["semantic_guard_class"]))
        reasons.extend(str(item) for item in result.get("semantic_guard_reasons") or ())
        allowed = allowed and bool(result["score_allowed"])
    return {
        "semantic_guard_status": "PASS" if allowed else "BLOCKED",
        "semantic_guard_class": ",".join(dict.fromkeys(classes)) if classes else "no_score_contribution",
        "semantic_guard_reasons": list(dict.fromkeys(reasons)),
        "score_allowed": allowed,
        "contract_quality_semantic_guard_checked": bool(contributions),
    }


def _decision_sort_key(row: Mapping[str, Any]) -> tuple[int, int, float, str]:
    score_allowed = 1 if row.get("score_scale") != "NO_SCORE" else 0
    stage_rank = {
        "Red": 50,
        "Reject": 45,
        "Stage3-Green": 40,
        "Stage3-Yellow": 35,
        "Stage2-Actionable": 30,
        "Stage2-Watch": 25,
        "Stage1": 10,
        "Stage0": 0,
    }.get(str(row.get("base_stage")), 0)
    score = float(row.get("event_evidence_score") or row.get("full_e2r_verified_score") or 0.0)
    date_key = str(row.get("source_cutover_date") or "")
    return (score_allowed, stage_rank, score, date_key)


def _stage_decision_status(*, base_stage: str, score_status: str, score_allowed: bool) -> str:
    if not score_allowed:
        return "SOURCE_PENDING"
    if score_status == "PENDING_MATERIAL_GAPS":
        return "PENDING_MATERIAL_GAPS"
    if base_stage in {"Red", "Reject"}:
        return "RISK_REVIEW"
    return "FINAL"


def _stage_signal(*, base_stage: str, decision_status: str, score_allowed: bool) -> str:
    if not score_allowed:
        return "EVIDENCE_INSUFFICIENT"
    if decision_status == "PENDING_MATERIAL_GAPS":
        return "MATERIAL_CLAIM_WATCH"
    if base_stage in {"Red", "Reject"}:
        return "RISK_REVIEW"
    if base_stage == "Stage2-Watch":
        return "MATERIAL_CLAIM_WATCH"
    return "OFFICIAL_EVENT_WATCH"


def _risk_stage_signal(*, base_stage: str) -> str:
    if base_stage in {"Red", "Reject"}:
        return "CURRENT_DIRECT_RISK"
    return "NONE"


def _score_interval(trace: Mapping[str, Any]) -> tuple[float | None, float | None]:
    interval = trace.get("score_interval")
    if not isinstance(interval, Mapping):
        return None, None
    return _float_or_none(interval.get("lower")), _float_or_none(interval.get("upper"))


def _raw_contribution_sum(contributions: Sequence[Mapping[str, Any]]) -> float:
    return round(sum(float(item.get("raw_points") or 0.0) for item in contributions), 4)


def _float_or_none(value: Any) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _clean_ids(values: Sequence[Any]) -> list[str]:
    return [str(item) for item in values if str(item).strip()]


def _task_ids_for_event(rows: Sequence[Mapping[str, Any]], candidate_event_id: Any) -> list[str]:
    if not candidate_event_id:
        return []
    values: list[str] = []
    for row in rows:
        if row.get("candidate_event_id") == candidate_event_id or (isinstance(row.get("source_task"), Mapping) and row["source_task"].get("candidate_event_id") == candidate_event_id):
            task_id = row.get("task_id") or (row.get("source_task") or {}).get("task_id")
            if task_id:
                values.append(str(task_id))
    return list(dict.fromkeys(values))


__all__ = [
    "AtomicStageDecision",
    "build_atomic_stage_decisions",
    "canonical_stage_for_display",
    "choose_representative_decision",
    "normalize_stage",
]
