"""Primitive mapping guardrails for Evidence OS/Census outputs."""

from __future__ import annotations

from typing import Any, Mapping, Sequence

from .contract_semantic_classifier import classify_contract_event


def guard_score_contribution(
    *,
    contribution: Mapping[str, Any],
    support_claims: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    """Return score eligibility metadata for a score contribution.

    The guard is conservative: customer/revenue contract quality must be
    supported by a revenue-facing contract class. Financial/admin disclosures can
    still be useful events, but they must not unlock earnings visibility as if
    they were customer demand.
    """

    criterion = str(contribution.get("criterion_id") or "")
    component = str(contribution.get("component_key") or "")
    primitive_ids = {str(claim.get("primitive_id") or "") for claim in support_claims}
    needs_capacity_guard = (
        "capacity_expansion" in criterion
        or "capacity_precommitted" in criterion
        or "capacity_expansion" in primitive_ids
        or "capacity_precommitted" in primitive_ids
        or (component == "bottleneck_pricing" and bool(primitive_ids & {"capacity_expansion", "capacity_precommitted"}))
    )
    if needs_capacity_guard:
        capacity = _classify_capacity_event(support_claims)
        if not capacity["score_allowed"]:
            return capacity
    needs_contract_guard = (
        "contract_quality" in criterion
        or "contract_quality" in primitive_ids
        or (component == "earnings_visibility" and "contract_quality" in primitive_ids)
    )
    if not needs_contract_guard:
        return {
            "semantic_guard_status": "PASS",
            "semantic_guard_class": "not_contract_quality",
            "score_allowed": True,
            "semantic_guard_reasons": [],
        }

    classifications = [classify_contract_event(claim) for claim in support_claims]
    allowed = any(item.allowed_for_contract_quality for item in classifications)
    return {
        "semantic_guard_status": "PASS" if allowed else "BLOCKED",
        "semantic_guard_class": ",".join(item.event_class for item in classifications) or "unknown",
        "score_allowed": allowed,
        "semantic_guard_reasons": [reason for item in classifications for reason in item.reasons],
    }


def _classify_capacity_event(support_claims: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    text = " ".join(_claim_text(claim) for claim in support_claims).lower()
    if not text:
        return {
            "semantic_guard_status": "BLOCKED",
            "semantic_guard_class": "capacity_claim_without_text",
            "score_allowed": False,
            "semantic_guard_reasons": ["capacity score requires a readable source-backed claim"],
        }
    if _has_any(text, ("기재정정", "정정신고", "정정사유", "정정전", "정정후", "correction", "amendment")):
        return {
            "semantic_guard_status": "BLOCKED",
            "semantic_guard_class": "facility_investment_correction_followup_required",
            "score_allowed": False,
            "semantic_guard_reasons": ["facility investment correction is a follow-up trigger, not positive capacity score by itself"],
        }
    if _has_any(text, ("종료일 연장", "연장", "지연", "연기", "delay", "delayed", "postpone")):
        return {
            "semantic_guard_status": "BLOCKED",
            "semantic_guard_class": "facility_investment_schedule_delay",
            "score_allowed": False,
            "semantic_guard_reasons": ["facility investment schedule delay cannot support positive capacity expansion score"],
        }
    if _has_any(text, ("취소", "철회", "중단", "해지", "cancel", "withdraw", "terminated")):
        return {
            "semantic_guard_status": "BLOCKED",
            "semantic_guard_class": "facility_investment_cancelled",
            "score_allowed": False,
            "semantic_guard_reasons": ["cancelled or withdrawn facility investment cannot support positive capacity expansion score"],
        }
    return {
        "semantic_guard_status": "PASS",
        "semantic_guard_class": "capacity_event_no_adverse_revision_detected",
        "score_allowed": True,
        "semantic_guard_reasons": [],
    }


def _claim_text(claim: Mapping[str, Any]) -> str:
    parts: list[str] = []
    for key in (
        "quote_text",
        "event_title",
        "event_summary",
        "event_type",
        "report_nm",
        "title",
        "summary",
        "primitive_id",
    ):
        value = claim.get(key)
        if value is not None:
            parts.append(str(value))
    mapping = claim.get("mapping")
    if isinstance(mapping, Mapping):
        for key in ("primitive_id", "rationale"):
            value = mapping.get(key)
            if value is not None:
                parts.append(str(value))
    return " ".join(parts)


def _has_any(text: str, needles: tuple[str, ...]) -> bool:
    return any(needle.lower() in text for needle in needles)


__all__ = ["guard_score_contribution"]
