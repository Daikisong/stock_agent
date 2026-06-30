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
    }
    if assertion.predicate == "audit_or_accounting_claim" and adjudication.polarity != "NEGATIVE":
        return PrimitiveMappingDecision(None, "REJECTED", "NEUTRAL", "normal_or_positive_audit_is_not_trust_break")
    for primitive in mapping.get(assertion.predicate, ()):
        if primitive in allowed_primitives:
            direction = "COUNTER" if adjudication.polarity == "NEGATIVE" else "SUPPORT"
            return PrimitiveMappingDecision(primitive, "ACCEPTED", direction, f"predicate:{assertion.predicate}")
    return PrimitiveMappingDecision(None, "REJECTED", "no_allowed_primitive_for_predicate")


__all__ = ["PrimitiveMappingDecision", "map_claim_to_primitive"]
