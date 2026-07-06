"""Primitive mapping is deliberately separate from raw extraction."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Mapping, Sequence

from .contract_blind_extractor import RawAssertionRecord
from .entity_temporal_adjudicator import AdjudicationResult


@dataclass(frozen=True)
class PrimitiveMappingDecision:
    primitive_id: str | None
    mapping_status: str
    support_direction: str
    rationale: str

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def map_claim_to_primitive(
    assertion: RawAssertionRecord,
    adjudication: AdjudicationResult,
    *,
    allowed_primitives: Sequence[str],
    predicate_to_primitives: Mapping[str, Sequence[str]] | None = None,
) -> PrimitiveMappingDecision:
    if adjudication.semantic_status != "PASS":
        return PrimitiveMappingDecision(None, "REJECTED", "NEUTRAL", "adjudication_not_passed")
    mapping = predicate_to_primitives or {
        "official_document_fact": ("information_confidence",),
        "contract_or_order_claim": ("contract_quality", "revenue_visibility_contract", "order_to_revenue_bridge"),
        "capital_event_claim": ("capital_allocation_event",),
        "capacity_investment_claim": ("capacity_expansion", "capacity_precommitted"),
        "revision_claim": ("medium_term_revision_visibility",),
        "audit_or_accounting_claim": ("accounting_trust_break",),
        "profitability_or_cash_claim": ("fcf_quality_score", "margin_bridge_visible"),
        "material_pricing_power_claim": ("pricing_power_confirmed",),
        "material_spread_expansion_claim": ("spread_expansion",),
        "material_profitability_bridge_claim": ("fcf_quality_score", "opm_expansion_pctp", "margin_bridge_visible"),
        "utilization_or_volume_claim": ("utilization_rate", "capa_utilization_pct"),
        "inventory_cycle_claim": ("inventory_cycle",),
        "bio_trial_quality_claim": ("trial_quality_visible",),
        "bio_binary_event_risk_claim": ("binary_event_unresolved",),
        "bio_approval_not_confirmed_claim": ("approval_not_confirmed",),
        "bio_safety_signal_claim": ("safety_signal",),
        "cash_runway_risk_claim": ("cash_runway_risk",),
        "software_arr_growth_claim": ("arr_growth_visible",),
        "software_net_retention_claim": ("nrr",),
        "software_renewal_or_churn_claim": ("retention_or_renewal",),
        "software_rpo_or_deferred_revenue_claim": ("rpo_to_sales",),
        "software_recurring_margin_claim": ("recurring_margin_leverage",),
        "semiconductor_test_profile_claim": ("socket_or_test_demand_visible",),
        "customer_diversification_claim": ("named_customer_quality",),
        "customer_quality_or_qualification_claim": ("named_customer_quality", "qualification_confirmed"),
        "customer_allocation_or_qualification_claim": (
            "customer_preorder_or_allocation",
            "qualification_status",
            "revenue_visibility_contract",
        ),
        "capacity_allocation_claim": (
            "hbm_capacity_pre_sold",
            "hbm_capacity_constraint",
            "capacity_precommitted",
        ),
    }
    if assertion.predicate == "audit_or_accounting_claim" and adjudication.polarity != "NEGATIVE":
        return PrimitiveMappingDecision(None, "REJECTED", "NEUTRAL", "normal_or_positive_audit_is_not_trust_break")
    if assertion.predicate == "capacity_investment_claim":
        guard = _capacity_investment_guard(assertion, adjudication)
        if guard is not None:
            return guard
    if assertion.predicate == "customer_allocation_or_qualification_claim":
        return _customer_allocation_or_qualification_mapping(
            assertion,
            adjudication,
            allowed_primitives=allowed_primitives,
        )
    for primitive in mapping.get(assertion.predicate, ()):
        if primitive in allowed_primitives:
            direction = "COUNTER" if adjudication.polarity == "NEGATIVE" else "SUPPORT"
            return PrimitiveMappingDecision(primitive, "ACCEPTED", direction, f"predicate:{assertion.predicate}")
    return PrimitiveMappingDecision(None, "REJECTED", "NEUTRAL", "no_allowed_primitive_for_predicate")


def _capacity_investment_guard(
    assertion: RawAssertionRecord,
    adjudication: AdjudicationResult,
) -> PrimitiveMappingDecision | None:
    text = " ".join(
        str(value)
        for value in (
            assertion.exact_quote,
            assertion.object_text,
            assertion.predicate,
        )
        if value
    ).lower()
    if _has_any(text, ("기재정정", "정정신고", "정정사유", "정정전", "정정후", "correction", "amendment")):
        return PrimitiveMappingDecision(
            None,
            "REJECTED",
            "NEUTRAL",
            "facility_investment_correction_requires_followup_not_positive_capacity",
        )
    if _has_any(text, ("종료일 연장", "연장", "지연", "연기", "delay", "delayed", "postpone")):
        return PrimitiveMappingDecision(
            None,
            "REJECTED",
            "NEUTRAL",
            "facility_investment_schedule_delay_not_positive_capacity",
        )
    if _has_any(text, ("취소", "철회", "중단", "해지", "cancel", "withdraw", "terminated")):
        return PrimitiveMappingDecision(
            None,
            "REJECTED",
            "NEUTRAL",
            "facility_investment_cancelled_not_positive_capacity",
        )
    if adjudication.polarity == "NEGATIVE":
        return PrimitiveMappingDecision(
            None,
            "REJECTED",
            "NEUTRAL",
            "negative_facility_investment_not_positive_capacity",
        )
    return None


def _customer_allocation_or_qualification_mapping(
    assertion: RawAssertionRecord,
    adjudication: AdjudicationResult,
    *,
    allowed_primitives: Sequence[str],
) -> PrimitiveMappingDecision:
    text = " ".join(
        str(value)
        for value in (
            assertion.exact_quote,
            assertion.object_text,
        )
        if value
    ).lower()
    direction = "COUNTER" if adjudication.polarity == "NEGATIVE" else "SUPPORT"
    if "customer_preorder_or_allocation" in allowed_primitives and _has_customer_allocation_signal(text):
        return PrimitiveMappingDecision(
            "customer_preorder_or_allocation",
            "ACCEPTED",
            direction,
            "predicate:customer_allocation_or_qualification_claim:explicit_customer_allocation",
        )
    if "qualification_status" in allowed_primitives and _has_customer_qualification_signal(text):
        return PrimitiveMappingDecision(
            "qualification_status",
            "ACCEPTED",
            direction,
            "predicate:customer_allocation_or_qualification_claim:explicit_customer_qualification",
        )
    if "revenue_visibility_contract" in allowed_primitives and _has_customer_allocation_signal(text):
        return PrimitiveMappingDecision(
            "revenue_visibility_contract",
            "ACCEPTED",
            direction,
            "predicate:customer_allocation_or_qualification_claim:allocation_supports_revenue_visibility",
        )
    return PrimitiveMappingDecision(
        None,
        "REJECTED",
        "NEUTRAL",
        "customer_allocation_or_qualification_requires_explicit_customer_allocation_or_qualification",
    )


def _has_customer_allocation_signal(text: str) -> bool:
    if _has_any(
        text,
        (
            "customer allocation",
            "customer preorder",
            "customer pre-order",
            "preorder",
            "pre-order",
            "pre sold",
            "pre-sold",
            "allocated capacity",
            "capacity allocation",
            "allocation confirmed",
            "booked capacity",
            "secured capacity",
            "고객 물량 배정",
            "고객사 물량 배정",
            "고객 배정",
            "고객사 배정",
            "고객 allocation",
            "고객사 allocation",
            "고객사 확정 물량",
            "확정 물량",
            "물량 배정",
            "선주문",
            "선수주",
            "선점",
        ),
    ):
        return True
    return (
        ("customer" in text and "allocation" in text)
        or ("고객" in text and "allocation" in text)
        or ("고객" in text and "배정" in text)
    )


def _has_customer_qualification_signal(text: str) -> bool:
    if _has_any(
        text,
        (
            "customer qualification",
            "customer approval",
            "customer validation",
            "nvidia qualification",
            "nvidia approval",
            "qualification",
            "qualified",
            "approved",
            "고객 인증",
            "고객 승인",
            "고객 검증",
            "고객사 qualification",
            "엔비디아 인증",
            "엔비디아 승인",
            "퀄",
            "퀄리피케이션",
            "인증",
            "승인",
            "검증",
        ),
    ):
        return True
    return ("고객" in text and ("인증" in text or "승인" in text or "검증" in text))


def _has_any(text: str, needles: tuple[str, ...]) -> bool:
    return any(needle.lower() in text for needle in needles)


__all__ = ["PrimitiveMappingDecision", "map_claim_to_primitive"]
