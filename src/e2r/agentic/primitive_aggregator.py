"""Primitive aggregation from append-only Evidence OS v2 ledgers."""

from __future__ import annotations

from datetime import date
from typing import Iterable, Mapping

from .evidence_os import (
    AdjudicatedClaim,
    AppendOnlyEvidenceLedger,
    Directness,
    EvidenceContractV2,
    FreshnessPolicy,
    LedgerEventType,
    MappingStatus,
    PrimitiveStateV2,
    PrimitiveStatus,
    SemanticStatus,
    SupportDirection,
    TargetScopeStatus,
    TemporalStatus,
    VerificationStatus,
    stable_source_evidence_id,
)


def aggregate_primitive_states(
    *,
    ledger: AppendOnlyEvidenceLedger,
    contract: EvidenceContractV2,
    as_of_date: date,
    extra_primitive_ids: Iterable[str] = (),
) -> Mapping[str, PrimitiveStateV2]:
    """Aggregate accepted mappings into primitive states.

    Rejected mappings and invalidated claims are ignored. Missing primitives
    remain UNKNOWN, not ABSENT.
    """

    primitive_ids = tuple(
        dict.fromkeys(
            (
                *contract.required_primitives,
                *contract.green_gate.primitive_ids(),
                *extra_primitive_ids,
                *(mapping.primitive_id for mapping in ledger.mappings.values()),
            )
        )
    )
    support: dict[str, list[str]] = {primitive_id: [] for primitive_id in primitive_ids}
    counter: dict[str, list[str]] = {primitive_id: [] for primitive_id in primitive_ids}
    support_mappings: dict[str, list[str]] = {primitive_id: [] for primitive_id in primitive_ids}
    counter_mappings: dict[str, list[str]] = {primitive_id: [] for primitive_id in primitive_ids}
    support_sources: dict[str, list[str]] = {primitive_id: [] for primitive_id in primitive_ids}
    counter_sources: dict[str, list[str]] = {primitive_id: [] for primitive_id in primitive_ids}
    freshness: dict[str, list[int]] = {primitive_id: [] for primitive_id in primitive_ids}
    lifecycle: dict[str, list[TemporalStatus]] = {primitive_id: [] for primitive_id in primitive_ids}
    implicit_closures = _implicit_lifecycle_closure_statuses(ledger, as_of_date=as_of_date)
    for mapping in ledger.mappings.values():
        if mapping.mapping_status != MappingStatus.ACCEPTED:
            continue
        if ledger.claim_is_invalidated(mapping.claim_id):
            continue
        claim = ledger.claims.get(mapping.claim_id)
        if claim is None:
            continue
        primitive_id = mapping.primitive_id
        support.setdefault(primitive_id, [])
        counter.setdefault(primitive_id, [])
        support_mappings.setdefault(primitive_id, [])
        counter_mappings.setdefault(primitive_id, [])
        support_sources.setdefault(primitive_id, [])
        counter_sources.setdefault(primitive_id, [])
        freshness.setdefault(primitive_id, [])
        lifecycle.setdefault(primitive_id, [])
        freshness_policy = contract.freshness.get(primitive_id)
        closed_status = _append_only_lifecycle_status(ledger, claim) or implicit_closures.get(claim.claim_id)
        if closed_status is not None:
            lifecycle[primitive_id].append(closed_status)
            continue
        if not _claim_can_contribute_current_primitive(
            claim,
            as_of_date=as_of_date,
            freshness_policy=freshness_policy,
        ):
            lifecycle[primitive_id].append(
                _non_current_lifecycle_status(
                    claim,
                    as_of_date=as_of_date,
                    freshness_policy=freshness_policy,
                )
            )
            continue
        if mapping.support_direction == SupportDirection.COUNTER:
            counter[primitive_id].append(mapping.claim_id)
            counter_mappings[primitive_id].append(mapping.mapping_id)
            counter_sources[primitive_id].append(_source_evidence_id_for_mapping(mapping, claim))
        elif mapping.support_direction == SupportDirection.SUPPORT:
            support[primitive_id].append(mapping.claim_id)
            support_mappings[primitive_id].append(mapping.mapping_id)
            support_sources[primitive_id].append(_source_evidence_id_for_mapping(mapping, claim))
        if claim.event_date is not None:
            freshness[primitive_id].append(max((as_of_date - claim.event_date).days, 0))

    return {
        primitive_id: PrimitiveStateV2(
            primitive_id=primitive_id,
            status=_primitive_status(
                support.get(primitive_id, ()),
                counter.get(primitive_id, ()),
                lifecycle.get(primitive_id, ()),
            ),
            support_claim_ids=tuple(dict.fromkeys(support.get(primitive_id, ()))),
            counter_claim_ids=tuple(dict.fromkeys(counter.get(primitive_id, ()))),
            support_source_family_ids=tuple(dict.fromkeys(support_sources.get(primitive_id, ()))),
            counter_source_family_ids=tuple(dict.fromkeys(counter_sources.get(primitive_id, ()))),
            freshness_days=min(freshness[primitive_id]) if freshness.get(primitive_id) else None,
            support_mapping_ids=tuple(dict.fromkeys(support_mappings.get(primitive_id, ()))),
            counter_mapping_ids=tuple(dict.fromkeys(counter_mappings.get(primitive_id, ()))),
        )
        for primitive_id in sorted(set(primitive_ids) | set(support) | set(counter))
    }


def _source_evidence_id_for_mapping(mapping, claim: AdjudicatedClaim) -> str:
    source_anchor_id = claim.source_anchor_id or claim.claim_id
    return stable_source_evidence_id(
        archetype_id=mapping.archetype_id,
        primitive_id=mapping.primitive_id,
        support_direction=mapping.support_direction,
        subject_entity_id=claim.subject_entity_id,
        target_entity_id=claim.target_entity_id,
        source_anchor_id=source_anchor_id,
    )


def _append_only_lifecycle_status(
    ledger: AppendOnlyEvidenceLedger,
    claim: AdjudicatedClaim,
) -> TemporalStatus | None:
    if claim.superseded_by_claim_ids:
        return TemporalStatus.SUPERSEDED
    if any(
        event.event_type == LedgerEventType.SUPERSEDES and event.to_id == claim.claim_id
        for event in ledger.events
    ):
        return TemporalStatus.SUPERSEDED
    if any(
        event.event_type == LedgerEventType.RESOLVES and event.to_id == claim.claim_id
        for event in ledger.events
    ):
        return TemporalStatus.RESOLVED
    return None


_LIFECYCLE_CLOSING_STATUSES = {
    TemporalStatus.RESOLVED,
    TemporalStatus.EXPIRED,
    TemporalStatus.SUPERSEDED,
}
_LIFECYCLE_STATUS_PRIORITY = {
    TemporalStatus.EXPIRED: 1,
    TemporalStatus.SUPERSEDED: 2,
    TemporalStatus.RESOLVED: 3,
}


def _implicit_lifecycle_closure_statuses(
    ledger: AppendOnlyEvidenceLedger,
    *,
    as_of_date: date,
) -> Mapping[str, TemporalStatus]:
    accepted_by_primitive: dict[str, list[tuple[AdjudicatedClaim, TemporalStatus | None]]] = {}
    for mapping in ledger.mappings.values():
        if mapping.mapping_status != MappingStatus.ACCEPTED:
            continue
        if ledger.claim_is_invalidated(mapping.claim_id):
            continue
        claim = ledger.claims.get(mapping.claim_id)
        if claim is None or claim.event_date is None or claim.event_date > as_of_date:
            continue
        if not _claim_has_valid_lifecycle_scope(claim):
            continue
        closing_status = claim.temporal_status if claim.temporal_status in _LIFECYCLE_CLOSING_STATUSES else None
        accepted_by_primitive.setdefault(mapping.primitive_id, []).append((claim, closing_status))

    closures: dict[str, TemporalStatus] = {}
    for claim_rows in accepted_by_primitive.values():
        closing_claims = tuple((claim, status) for claim, status in claim_rows if status is not None)
        if not closing_claims:
            continue
        for claim, _status in claim_rows:
            if claim.temporal_status in _LIFECYCLE_CLOSING_STATUSES:
                continue
            closure_status = _newest_lifecycle_closure_for_claim(claim, closing_claims)
            if closure_status is not None:
                closures[claim.claim_id] = closure_status
    return closures


def _claim_has_valid_lifecycle_scope(claim: AdjudicatedClaim) -> bool:
    return (
        claim.verification_status == VerificationStatus.SEMANTIC_VERIFIED
        and claim.semantic_status == SemanticStatus.PASS_
        and claim.target_scope_status == TargetScopeStatus.DIRECT
        and claim.directness == Directness.DIRECT
    )


def _newest_lifecycle_closure_for_claim(
    claim: AdjudicatedClaim,
    closing_claims: Iterable[tuple[AdjudicatedClaim, TemporalStatus]],
) -> TemporalStatus | None:
    if claim.event_date is None:
        return None
    selected: TemporalStatus | None = None
    selected_date: date | None = None
    for closing_claim, status in closing_claims:
        if closing_claim.claim_id == claim.claim_id or closing_claim.event_date is None:
            continue
        if closing_claim.event_date < claim.event_date:
            continue
        if selected is None or closing_claim.event_date > (selected_date or date.min):
            selected = status
            selected_date = closing_claim.event_date
            continue
        if closing_claim.event_date == selected_date and _lifecycle_priority(status) > _lifecycle_priority(selected):
            selected = status
    return selected


def _lifecycle_priority(status: TemporalStatus | None) -> int:
    if status is None:
        return 0
    return _LIFECYCLE_STATUS_PRIORITY.get(status, 0)


def _claim_can_contribute_current_primitive(
    claim: AdjudicatedClaim,
    *,
    as_of_date: date,
    freshness_policy: FreshnessPolicy | None = None,
) -> bool:
    return (
        claim.verification_status == VerificationStatus.SEMANTIC_VERIFIED
        and claim.semantic_status == SemanticStatus.PASS_
        and claim.target_scope_status == TargetScopeStatus.DIRECT
        and claim.directness == Directness.DIRECT
        and claim.temporal_status == TemporalStatus.CURRENT
        and (claim.event_date is None or claim.event_date <= as_of_date)
        and not _claim_exceeds_freshness_policy(
            claim,
            as_of_date=as_of_date,
            freshness_policy=freshness_policy,
        )
    )


def _non_current_lifecycle_status(
    claim: AdjudicatedClaim,
    *,
    as_of_date: date,
    freshness_policy: FreshnessPolicy | None,
) -> TemporalStatus:
    if _claim_exceeds_freshness_policy(
        claim,
        as_of_date=as_of_date,
        freshness_policy=freshness_policy,
    ):
        return TemporalStatus.HISTORICAL
    return claim.temporal_status


def _claim_exceeds_freshness_policy(
    claim: AdjudicatedClaim,
    *,
    as_of_date: date,
    freshness_policy: FreshnessPolicy | None,
) -> bool:
    if freshness_policy is None or freshness_policy.max_age_days is None or claim.event_date is None:
        return False
    age_days = (as_of_date - claim.event_date).days
    return age_days > freshness_policy.max_age_days


def _primitive_status(
    support_claim_ids: Iterable[str],
    counter_claim_ids: Iterable[str],
    lifecycle_statuses: Iterable[TemporalStatus] = (),
) -> PrimitiveStatus:
    has_support = any(True for _ in support_claim_ids)
    has_counter = any(True for _ in counter_claim_ids)
    if has_support and has_counter:
        return PrimitiveStatus.CONTRADICTED
    if has_support:
        return PrimitiveStatus.PRESENT_CURRENT
    if has_counter:
        return PrimitiveStatus.ABSENT_EXPLICITLY_CONFIRMED
    lifecycle = set(lifecycle_statuses)
    if TemporalStatus.RESOLVED in lifecycle:
        return PrimitiveStatus.RESOLVED
    if lifecycle & {TemporalStatus.HISTORICAL, TemporalStatus.EXPIRED, TemporalStatus.SUPERSEDED}:
        return PrimitiveStatus.HISTORICAL
    return PrimitiveStatus.UNKNOWN


__all__ = ["aggregate_primitive_states"]
