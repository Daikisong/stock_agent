"""Strict impact validation, policy totality, and fact/document credit dedupe."""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Any, Mapping, Sequence
from urllib.parse import urlsplit, urlunsplit

from e2r.production.metadata import stable_hash
from e2r.research_brain.runtime.scoring_contracts import (
    load_archetype_scoring_contract,
)
from e2r.research_brain.runtime.scoring_contracts.scoring_policy_v2 import (
    ScoringContractIncompleteError,
    load_scoring_policy_v2,
    require_scoring_key,
)

from .business_mechanism_scope import load_mechanism_scope_contracts
from .claim_impact_ledger import ValidatedClaimImpact


@dataclass(frozen=True)
class EconomicFactCluster:
    fact_cluster_id: str
    normalized_subject: str
    normalized_predicate: str
    normalized_object_value: str
    period: str
    business_mechanism: str
    claim_ids: tuple[str, ...]
    document_cluster_ids: tuple[str, ...]
    impact_ids: tuple[str, ...]
    primary_impact_id: str
    corroborating_impact_ids: tuple[str, ...]
    corroborating_document_count: int
    corroborating_source_count: int
    evidence_confidence: float

    def to_dict(self) -> Mapping[str, Any]:
        return json.loads(json.dumps(asdict(self), ensure_ascii=False))


@dataclass(frozen=True)
class DocumentCluster:
    document_cluster_id: str
    content_identity: str
    document_ids: tuple[str, ...]
    source_urls: tuple[str, ...]
    claim_ids: tuple[str, ...]
    impact_ids: tuple[str, ...]

    def to_dict(self) -> Mapping[str, Any]:
        return json.loads(json.dumps(asdict(self), ensure_ascii=False))


@dataclass(frozen=True)
class CreditValidatedImpact:
    impact_id: str
    claim_id: str
    mapping_id: str
    target_id: str
    archetype_id: str
    primitive_id: str
    component_id: str
    direction: str
    support_type: str
    source_family: str
    source_independence_key: str
    evidence_family_id: str
    question_family_id: str
    component_subcriterion_id: str
    raw_credit_fraction: float
    validated_credit_fraction: float
    support_credit_fraction: float
    counter_effect_fraction: float
    resolution_effect: float
    strength_fraction: float
    completeness_fraction: float
    causal_cap: float
    source_cap: float
    temporal_cap: float
    support_type_cap: float
    evidence_confidence: float
    scope_validation: Mapping[str, Any]
    fact_cluster_id: str
    document_cluster_id: str
    claim_budget_scaled: bool
    fact_budget_scaled: bool
    document_budget_scaled: bool
    evidence_family_budget_scaled: bool
    correlation_scaled: bool
    information_diversity_scaled: bool
    corroboration_only: bool
    duplicate_reason: str | None
    counter_claim_ids: tuple[str, ...] = ()
    lineage_mapping_ids: tuple[str, ...] = ()
    eligibility_decision_id: str = ""
    validation_status: str = "CREDIT_VALIDATED_V2"

    def to_dict(self) -> Mapping[str, Any]:
        return json.loads(json.dumps(asdict(self), ensure_ascii=False))


@dataclass(frozen=True)
class ImpactValidationResult:
    status: str
    impacts: tuple[CreditValidatedImpact, ...]
    rejected: tuple[Mapping[str, Any], ...]
    economic_fact_clusters: tuple[EconomicFactCluster, ...]
    document_clusters: tuple[DocumentCluster, ...]
    audit: Mapping[str, Any]


class ImpactValidator:
    def validate(
        self,
        *,
        impacts: Sequence[ValidatedClaimImpact],
        claim_provenance: Sequence[Mapping[str, Any]],
        claim_eligibility_decisions: Sequence[Mapping[str, Any]] = (),
        accepted_current_claims: Sequence[Mapping[str, Any]] = (),
    ) -> ImpactValidationResult:
        from e2r.research_brain.compiler.evidence_impact_rubric_compiler import (
            compile_evidence_impact_rubrics,
        )

        scoring_policy = load_scoring_policy_v2()
        provenance = {
            str(row.get("claim_id") or ""): row for row in claim_provenance
        }
        claims = {
            str(row.get("claim_id") or ""): row
            for row in accepted_current_claims
        }
        eligibility = {
            str(row.get("eligibility_decision_id") or ""): row
            for row in claim_eligibility_decisions
        }
        mechanism_contracts = load_mechanism_scope_contracts()
        accepted: list[CreditValidatedImpact] = []
        rejected: list[Mapping[str, Any]] = []
        group_by_primitive: dict[tuple[str, str], str] = {}
        fact_dimensions: dict[str, Mapping[str, str]] = {}
        document_dimensions: dict[str, Mapping[str, str]] = {}

        for impact in impacts:
            proposal = impact.proposal
            contract = load_archetype_scoring_contract(proposal.archetype_id)
            catalog = compile_evidence_impact_rubrics(proposal.archetype_id)
            rubric = catalog.by_primitive().get(proposal.primitive_id)
            prov = provenance.get(proposal.claim_id)
            reason = _lineage_rejection_reason(
                impact=impact,
                rubric=rubric,
                provenance=prov,
                eligibility=eligibility,
            )
            if not reason:
                reason = _scope_rejection_reason(
                    impact=impact,
                    mechanism_contract_configured=(
                        proposal.archetype_id in mechanism_contracts
                    ),
                )
            if reason:
                rejected.append(
                    {
                        "impact_id": proposal.impact_id,
                        "claim_id": proposal.claim_id,
                        "mapping_id": proposal.mapping_id,
                        "component_id": proposal.component_id,
                        "question_family_id": proposal.question_family_id,
                        "component_subcriterion_id": (
                            proposal.component_subcriterion_id
                        ),
                        "reason": reason,
                        "scope_validation": dict(impact.scope_validation),
                    }
                )
                continue

            strength = float(
                _required_policy(
                    rubric.strength_bands,
                    proposal.strength_band,
                    policy_name="strength_bands",
                    error_code="MISSING_STRENGTH_POLICY",
                )
            )
            completeness = float(
                _required_policy(
                    rubric.completeness_bands,
                    proposal.completeness_band,
                    policy_name="completeness_bands",
                    error_code="MISSING_COMPLETENESS_POLICY",
                )
            )
            causal = float(
                _required_policy(
                    rubric.causal_distance_caps,
                    proposal.causal_distance,
                    policy_name="causal_distance_caps",
                    error_code="MISSING_CAUSAL_DISTANCE_POLICY",
                )
            )
            source = float(
                _required_policy(
                    rubric.source_family_caps,
                    proposal.source_family,
                    policy_name="source_family_caps",
                    error_code="MISSING_SOURCE_FAMILY_POLICY",
                )
            )
            temporal = float(
                _required_policy(
                    contract.freshness_caps,
                    proposal.temporal_scope,
                    policy_name="temporal_scope_caps",
                    error_code="MISSING_TEMPORAL_POLICY",
                )
            )
            support_cap = _directional_support_cap(
                scoring_policy=scoring_policy,
                support_type=proposal.support_type,
                direction=proposal.direction,
            )
            raw = round(strength * completeness, 6)
            effect = round(
                min(raw, causal, source, temporal, support_cap),
                6,
            )
            fact_cluster_id, fact_dimension = _fact_cluster(
                proposal=proposal,
                impact=impact,
                claim=claims.get(proposal.claim_id),
                provenance=prov or {},
            )
            document_cluster_id, document_dimension = _document_cluster(
                proposal=proposal,
                provenance=prov or {},
            )
            fact_dimensions.setdefault(fact_cluster_id, fact_dimension)
            document_dimensions.setdefault(
                document_cluster_id, document_dimension
            )
            support_credit, counter_effect, resolution_effect = _effect_planes(
                direction=proposal.direction,
                effect=effect,
            )
            accepted.append(
                CreditValidatedImpact(
                    impact_id=proposal.impact_id,
                    claim_id=proposal.claim_id,
                    mapping_id=proposal.mapping_id,
                    target_id=proposal.target_id,
                    archetype_id=proposal.archetype_id,
                    primitive_id=proposal.primitive_id,
                    component_id=proposal.component_id,
                    direction=proposal.direction,
                    support_type=proposal.support_type,
                    source_family=proposal.source_family,
                    source_independence_key=_source_independence_key(
                        proposal=proposal,
                        provenance=prov or {},
                    ),
                    evidence_family_id=proposal.evidence_family_id,
                    question_family_id=proposal.question_family_id,
                    component_subcriterion_id=(
                        proposal.component_subcriterion_id
                    ),
                    raw_credit_fraction=raw,
                    validated_credit_fraction=effect,
                    support_credit_fraction=support_credit,
                    counter_effect_fraction=counter_effect,
                    resolution_effect=resolution_effect,
                    strength_fraction=strength,
                    completeness_fraction=completeness,
                    causal_cap=causal,
                    source_cap=source,
                    temporal_cap=temporal,
                    support_type_cap=support_cap,
                    evidence_confidence=proposal.confidence,
                    scope_validation=dict(impact.scope_validation),
                    fact_cluster_id=fact_cluster_id,
                    document_cluster_id=document_cluster_id,
                    claim_budget_scaled=False,
                    fact_budget_scaled=False,
                    document_budget_scaled=False,
                    evidence_family_budget_scaled=False,
                    correlation_scaled=False,
                    information_diversity_scaled=False,
                    corroboration_only=False,
                    duplicate_reason=None,
                    counter_claim_ids=proposal.counter_claim_ids,
                    lineage_mapping_ids=proposal.lineage_mapping_ids,
                    eligibility_decision_id=impact.eligibility_decision_id,
                )
            )
            for group, primitives in contract.correlation_groups.items():
                if proposal.primitive_id in primitives:
                    group_by_primitive[
                        (proposal.archetype_id, proposal.primitive_id)
                    ] = group

        suppressed_same_fact = 0
        suppressed_same_document = 0
        accepted, suppressed_same_fact = _suppress_duplicate_groups(
            accepted,
            key=lambda item: (
                item.fact_cluster_id,
                item.component_id,
                item.direction,
            ),
            duplicate_reason="SAME_ECONOMIC_FACT_CORROBORATION_ONLY",
        )
        accepted, suppressed_same_document = _suppress_duplicate_groups(
            accepted,
            key=lambda item: (
                item.document_cluster_id,
                item.component_id,
                item.direction,
            )
            if item.component_id == "information_confidence"
            else ("UNIQUE", item.impact_id),
            duplicate_reason="SAME_DOCUMENT_INFORMATION_CORROBORATION_ONLY",
        )
        budget = scoring_policy.credit_budget_policy
        accepted = _scale_group_budget(
            accepted,
            keys=lambda item: (item.fact_cluster_id, item.component_id),
            cap=budget.fact_cluster_component_fraction_cap,
            flag="fact_budget_scaled",
        )
        accepted = _scale_group_budget(
            accepted,
            keys=lambda item: (item.document_cluster_id, item.component_id),
            cap=budget.document_cluster_component_fraction_cap,
            flag="document_budget_scaled",
        )
        accepted = _scale_group_budget(
            accepted,
            keys=lambda item: (item.evidence_family_id, item.component_id),
            cap=budget.evidence_family_component_fraction_cap,
            flag="evidence_family_budget_scaled",
        )
        accepted = _apply_information_confidence_diversity(
            accepted,
            diversity_cap=(
                budget.information_confidence_diversity_increment_cap
            ),
            max_families=(
                budget.information_confidence_max_independent_families
            ),
        )
        accepted = _scale_group_budget(
            accepted,
            keys=lambda item: (item.claim_id,),
            cap=budget.claim_total_fraction_cap,
            flag="claim_budget_scaled",
        )
        accepted = _scale_correlation_groups(
            accepted,
            groups=group_by_primitive,
            cap=budget.component_correlation_fraction_cap,
        )

        economic_clusters = _economic_clusters(
            impacts=accepted,
            dimensions=fact_dimensions,
        )
        document_clusters = _document_clusters(
            impacts=accepted,
            dimensions=document_dimensions,
            provenance=provenance,
        )
        critical = {
            "unvalidated_impact_to_score_count": sum(
                row["reason"] == "UNVALIDATED_LEDGER_IMPACT"
                for row in rejected
            ),
            "rubric_edge_violation_count": sum(
                row["reason"] == "RUBRIC_EDGE_VIOLATION"
                for row in rejected
            ),
            "source_cap_violation_count": sum(
                item.validated_credit_fraction > item.source_cap + 1e-9
                for item in accepted
            ),
            "claim_credit_budget_violation_count": _budget_violation_count(
                accepted,
                keys=lambda item: (item.claim_id,),
                cap=budget.claim_total_fraction_cap,
            ),
            "correlated_double_count_count": _correlation_violation_count(
                accepted,
                groups=group_by_primitive,
                cap=budget.component_correlation_fraction_cap,
            ),
            "component_score_without_eligibility_decision_count": sum(
                row["reason"] == "ELIGIBILITY_DECISION_MISSING"
                for row in rejected
            ),
            "positive_impact_zeroed_by_missing_cap_count": 0,
            "counter_impact_zeroed_by_missing_cap_count": 0,
            "cross_mechanism_impact_count": sum(
                item.scope_validation.get("scope_match") is not True
                for item in accepted
                if item.archetype_id in mechanism_contracts
            ),
            "same_fact_duplicate_credit_count": _duplicate_credit_count(
                accepted,
                key=lambda item: (
                    item.fact_cluster_id,
                    item.component_id,
                    item.direction,
                ),
            ),
            "same_document_duplicate_credit_count": _duplicate_credit_count(
                (
                    item
                    for item in accepted
                    if item.component_id == "information_confidence"
                ),
                key=lambda item: (
                    item.document_cluster_id,
                    item.component_id,
                    item.direction,
                ),
            ),
            "fact_cluster_missing_count": sum(
                not item.fact_cluster_id for item in accepted
            ),
            "document_cluster_missing_count": sum(
                not item.document_cluster_id for item in accepted
            ),
        }
        critical_sum = sum(critical.values())
        audit = {
            "schema_version": "e2r_impact_validator_v2_audit_v1",
            "status": (
                "STRICT_IMPACT_VALIDATOR_V2_PASS"
                if not rejected and critical_sum == 0
                else "STRICT_IMPACT_VALIDATOR_V2_FAIL"
            ),
            "validated_impact_count": len(accepted),
            "credited_impact_count": sum(
                item.validated_credit_fraction > 0 for item in accepted
            ),
            "rejected_impact_count": len(rejected),
            "economic_fact_cluster_count": len(economic_clusters),
            "document_cluster_count": len(document_clusters),
            "suppressed_same_fact_duplicate_count": suppressed_same_fact,
            "suppressed_same_document_duplicate_count": (
                suppressed_same_document
            ),
            "claim_budget_scaled_count": sum(
                item.claim_budget_scaled for item in accepted
            ),
            "fact_budget_scaled_count": sum(
                item.fact_budget_scaled for item in accepted
            ),
            "document_budget_scaled_count": sum(
                item.document_budget_scaled for item in accepted
            ),
            "evidence_family_budget_scaled_count": sum(
                item.evidence_family_budget_scaled for item in accepted
            ),
            "correlation_scaled_count": sum(
                item.correlation_scaled for item in accepted
            ),
            "information_diversity_scaled_count": sum(
                item.information_diversity_scaled for item in accepted
            ),
            "critical_counts": critical,
            "critical_count_sum": critical_sum,
        }
        return ImpactValidationResult(
            status=(
                "IMPACT_CREDIT_CAP_PASS"
                if not rejected and critical_sum == 0
                else "IMPACT_CREDIT_CAP_FAIL"
            ),
            impacts=tuple(accepted),
            rejected=tuple(rejected),
            economic_fact_clusters=economic_clusters,
            document_clusters=document_clusters,
            audit=audit,
        )


def _lineage_rejection_reason(
    *,
    impact: ValidatedClaimImpact,
    rubric: Any,
    provenance: Mapping[str, Any] | None,
    eligibility: Mapping[str, Mapping[str, Any]],
) -> str:
    proposal = impact.proposal
    if impact.validation_status != "LINEAGE_AND_EDGE_VALIDATED":
        return "UNVALIDATED_LEDGER_IMPACT"
    if rubric is None or proposal.component_id not in rubric.allowed_component_ids:
        return "RUBRIC_EDGE_VIOLATION"
    if (
        provenance is None
        or provenance.get("source_proxy_only") is not False
        or provenance.get("directness") != "DIRECT"
        or provenance.get("temporal_status") != "CURRENT"
    ):
        return "PROVENANCE_NOT_CURRENT_DIRECT"
    mapping_ids = {str(value) for value in provenance.get("mapping_ids") or ()}
    if proposal.mapping_id not in mapping_ids or any(
        mapping_id not in mapping_ids
        for mapping_id in proposal.lineage_mapping_ids
    ):
        return "PROVENANCE_MAPPING_MISSING"
    if (
        not impact.eligibility_decision_id
        or impact.eligibility_decision_id not in eligibility
    ):
        return "ELIGIBILITY_DECISION_MISSING"
    if eligibility[impact.eligibility_decision_id].get(
        "component_scoring_eligibility"
    ) is not True:
        return "CLAIM_COMPONENT_INELIGIBLE"
    return ""


def _scope_rejection_reason(
    *,
    impact: ValidatedClaimImpact,
    mechanism_contract_configured: bool,
) -> str:
    if not mechanism_contract_configured:
        return ""
    validation = impact.scope_validation
    if not validation:
        return "MECHANISM_SCOPE_MISSING"
    if validation.get("scope_match") is not True:
        return "CROSS_MECHANISM_IMPACT"
    scope = validation.get("scope")
    if not isinstance(scope, Mapping):
        return "MECHANISM_SCOPE_MISSING"
    required = (
        "issuer_id",
        "business_segment",
        "product_family",
        "economic_mechanism",
    )
    if any(not str(scope.get(field) or "") for field in required):
        return "MECHANISM_SCOPE_INCOMPLETE"
    if str(scope.get("issuer_id") or "") != impact.proposal.target_id:
        return "MECHANISM_SCOPE_ISSUER_MISMATCH"
    return ""


def _required_policy(
    mapping: Mapping[str, Any],
    key: str,
    *,
    policy_name: str,
    error_code: str,
) -> Any:
    if key not in mapping:
        raise ScoringContractIncompleteError(
            f"{error_code}:SCORING_CONTRACT_INCOMPLETE:{policy_name}:{key}"
        )
    return mapping[key]


def _directional_support_cap(
    *, scoring_policy: Any, support_type: str, direction: str
) -> float:
    if support_type not in scoring_policy.support_type_policies:
        raise ScoringContractIncompleteError(
            "MISSING_SUPPORT_TYPE_POLICY:"
            f"SCORING_CONTRACT_INCOMPLETE:support_type_policies:{support_type}"
        )
    if direction not in scoring_policy.direction_policy_fields:
        raise ScoringContractIncompleteError(
            "MISSING_COUNTER_EFFECT_POLICY:"
            f"SCORING_CONTRACT_INCOMPLETE:direction_policy_fields:{direction}"
        )
    policy = require_scoring_key(
        scoring_policy.support_type_policies,
        support_type,
        policy_name="support_type_policies",
    )
    field = require_scoring_key(
        scoring_policy.direction_policy_fields,
        direction,
        policy_name="direction_policy_fields",
    )
    if not hasattr(policy, field):
        raise ScoringContractIncompleteError(
            "MISSING_COUNTER_EFFECT_POLICY:"
            f"SCORING_CONTRACT_INCOMPLETE:{support_type}:{field}"
        )
    return float(getattr(policy, field))


def _effect_planes(*, direction: str, effect: float) -> tuple[float, float, float]:
    if direction in {"SUPPORT", "NEUTRAL"}:
        return effect, 0.0, 0.0
    if direction == "COUNTER":
        return 0.0, effect, 0.0
    if direction == "RESOLUTION":
        return 0.0, 0.0, effect
    raise ScoringContractIncompleteError(
        f"MISSING_COUNTER_EFFECT_POLICY:UNKNOWN_DIRECTION:{direction}"
    )


def _fact_cluster(
    *,
    proposal: Any,
    impact: ValidatedClaimImpact,
    claim: Mapping[str, Any] | None,
    provenance: Mapping[str, Any],
) -> tuple[str, Mapping[str, str]]:
    claim = claim or {}
    raw = claim.get("raw_assertion") or {}
    scope = impact.scope_validation.get("scope") or {}
    subject = _normalize_text(
        str(raw.get("subject") or " ".join(
            str(scope.get(field) or "")
            for field in ("issuer_id", "business_segment", "product_family")
        ))
    )
    predicate = _normalize_text(
        str(raw.get("predicate") or proposal.primitive_id)
    )
    object_value = _normalize_text(
        str(
            raw.get("object_text")
            or claim.get("exact_quote")
            or provenance.get("exact_quote")
            or proposal.rationale
        )
    )
    period = _normalize_text(
        "/".join(
            str(value)
            for value in (
                claim.get("effective_start"),
                claim.get("effective_end"),
                claim.get("event_date"),
                claim.get("reporting_period"),
            )
            if value
        )
        or str(provenance.get("effective_period") or "CURRENT")
    )
    mechanism = _normalize_text(str(scope.get("economic_mechanism") or ""))
    explicit = str(
        claim.get("economic_fact_key")
        or claim.get("semantic_fact_key")
        or ""
    )
    payload = {
        "normalized_subject": subject,
        "normalized_predicate": predicate,
        "normalized_object_value": object_value,
        "period": period,
        "business_mechanism": mechanism,
        "explicit_semantic_key": explicit,
    }
    identity_payload = (
        {
            "target_id": proposal.target_id,
            "explicit_semantic_key": explicit,
            "business_mechanism": mechanism,
            "period": period,
        }
        if explicit
        else payload
    )
    return "FACT-" + stable_hash(identity_payload)[:24], payload


def _document_cluster(
    *, proposal: Any, provenance: Mapping[str, Any]
) -> tuple[str, Mapping[str, str]]:
    source_url = _canonical_url(str(provenance.get("source_url") or ""))
    content_identity = str(
        provenance.get("document_cluster_id")
        or provenance.get("content_sha256")
        or provenance.get("content_hash")
        or provenance.get("document_id")
        or source_url
        or proposal.evidence_family_id
    )
    payload = {
        "content_identity": content_identity,
        "document_id": str(provenance.get("document_id") or ""),
        "source_url": source_url,
    }
    return "DOC_CLUSTER-" + stable_hash(content_identity)[:24], payload


def _suppress_duplicate_groups(
    items: Sequence[CreditValidatedImpact],
    *,
    key: Any,
    duplicate_reason: str,
) -> tuple[list[CreditValidatedImpact], int]:
    result = list(items)
    groups: dict[Any, list[int]] = {}
    for index, item in enumerate(result):
        groups.setdefault(key(item), []).append(index)
    suppressed = 0
    for indexes in groups.values():
        credited = [
            index
            for index in indexes
            if result[index].validated_credit_fraction > 0
        ]
        if len(credited) <= 1:
            continue
        credited.sort(
            key=lambda index: (
                result[index].validated_credit_fraction,
                result[index].source_cap,
                result[index].evidence_confidence,
                result[index].impact_id,
            ),
            reverse=True,
        )
        for index in credited[1:]:
            result[index] = _set_effect(
                result[index],
                0.0,
                corroboration_only=True,
                duplicate_reason=duplicate_reason,
            )
            suppressed += 1
    return result, suppressed


def _scale_group_budget(
    items: Sequence[CreditValidatedImpact],
    *,
    keys: Any,
    cap: float,
    flag: str,
) -> list[CreditValidatedImpact]:
    result = list(items)
    groups: dict[Any, list[int]] = {}
    for index, item in enumerate(result):
        groups.setdefault(keys(item), []).append(index)
    for indexes in groups.values():
        total = sum(result[index].validated_credit_fraction for index in indexes)
        if total <= cap + 1e-12 or total <= 0:
            continue
        scale = cap / total
        for index in indexes:
            current = result[index]
            updates = {flag: True}
            result[index] = _set_effect(
                current,
                round(current.validated_credit_fraction * scale, 6),
                **updates,
            )
    return result


def _scale_correlation_groups(
    items: Sequence[CreditValidatedImpact],
    *,
    groups: Mapping[tuple[str, str], str],
    cap: float,
) -> list[CreditValidatedImpact]:
    return _scale_group_budget(
        items,
        keys=lambda item: (
            item.claim_id,
            groups.get((item.archetype_id, item.primitive_id), item.impact_id),
        ),
        cap=cap,
        flag="correlation_scaled",
    )


def _apply_information_confidence_diversity(
    items: Sequence[CreditValidatedImpact],
    *,
    diversity_cap: float,
    max_families: int,
) -> list[CreditValidatedImpact]:
    result = list(items)
    target_groups: dict[str, list[int]] = {}
    for index, item in enumerate(result):
        if (
            item.component_id == "information_confidence"
            and item.direction == "SUPPORT"
            and item.validated_credit_fraction > 0
        ):
            target_groups.setdefault(item.target_id, []).append(index)
    for indexes in target_groups.values():
        indexes.sort(
            key=lambda index: (
                result[index].source_cap,
                result[index].validated_credit_fraction,
                result[index].impact_id,
            ),
            reverse=True,
        )
        seen_families: set[str] = set()
        family_rank = 0
        for index in indexes:
            item = result[index]
            if item.source_independence_key in seen_families:
                result[index] = _set_effect(
                    item,
                    0.0,
                    corroboration_only=True,
                    duplicate_reason="SAME_SOURCE_FAMILY_CONFIDENCE_ONLY",
                    information_diversity_scaled=True,
                )
                continue
            seen_families.add(item.source_independence_key)
            family_rank += 1
            if family_rank == 1:
                continue
            if family_rank > max_families:
                result[index] = _set_effect(
                    item,
                    0.0,
                    corroboration_only=True,
                    duplicate_reason="INDEPENDENT_SOURCE_FAMILY_LIMIT",
                    information_diversity_scaled=True,
                )
                continue
            bounded = min(item.validated_credit_fraction, diversity_cap)
            result[index] = _set_effect(
                item,
                round(bounded, 6),
                information_diversity_scaled=(
                    bounded < item.validated_credit_fraction
                ),
            )
    return result


def _set_effect(
    item: CreditValidatedImpact,
    value: float,
    **updates: Any,
) -> CreditValidatedImpact:
    support, counter, resolution = _effect_planes(
        direction=item.direction,
        effect=value,
    )
    return replace(
        item,
        validated_credit_fraction=value,
        support_credit_fraction=support,
        counter_effect_fraction=counter,
        resolution_effect=resolution,
        **updates,
    )


def _economic_clusters(
    *,
    impacts: Sequence[CreditValidatedImpact],
    dimensions: Mapping[str, Mapping[str, str]],
) -> tuple[EconomicFactCluster, ...]:
    groups: dict[str, list[CreditValidatedImpact]] = {}
    for impact in impacts:
        groups.setdefault(impact.fact_cluster_id, []).append(impact)
    result = []
    for cluster_id, rows in sorted(groups.items()):
        primary = max(
            rows,
            key=lambda item: (
                item.validated_credit_fraction,
                item.source_cap,
                item.impact_id,
            ),
        )
        dimension = dimensions[cluster_id]
        result.append(
            EconomicFactCluster(
                fact_cluster_id=cluster_id,
                normalized_subject=dimension["normalized_subject"],
                normalized_predicate=dimension["normalized_predicate"],
                normalized_object_value=dimension[
                    "normalized_object_value"
                ],
                period=dimension["period"],
                business_mechanism=dimension["business_mechanism"],
                claim_ids=tuple(
                    sorted({item.claim_id for item in rows})
                ),
                document_cluster_ids=tuple(
                    sorted({item.document_cluster_id for item in rows})
                ),
                impact_ids=tuple(sorted(item.impact_id for item in rows)),
                primary_impact_id=primary.impact_id,
                corroborating_impact_ids=tuple(
                    sorted(
                        item.impact_id
                        for item in rows
                        if item.impact_id != primary.impact_id
                    )
                ),
                corroborating_document_count=max(
                    len({item.document_cluster_id for item in rows}) - 1,
                    0,
                ),
                corroborating_source_count=max(
                    len({item.source_independence_key for item in rows}) - 1,
                    0,
                ),
                evidence_confidence=round(
                    min(
                        0.99,
                        max(item.evidence_confidence for item in rows)
                        + 0.03
                        * max(
                            len(
                                {
                                    item.source_independence_key
                                    for item in rows
                                }
                            )
                            - 1,
                            0,
                        ),
                    ),
                    6,
                ),
            )
        )
    return tuple(result)


def _document_clusters(
    *,
    impacts: Sequence[CreditValidatedImpact],
    dimensions: Mapping[str, Mapping[str, str]],
    provenance: Mapping[str, Mapping[str, Any]],
) -> tuple[DocumentCluster, ...]:
    groups: dict[str, list[CreditValidatedImpact]] = {}
    for impact in impacts:
        groups.setdefault(impact.document_cluster_id, []).append(impact)
    result = []
    for cluster_id, rows in sorted(groups.items()):
        dimension = dimensions[cluster_id]
        result.append(
            DocumentCluster(
                document_cluster_id=cluster_id,
                content_identity=dimension["content_identity"],
                document_ids=tuple(
                    sorted(
                        {
                            str(provenance.get(item.claim_id, {}).get("document_id") or "")
                            for item in rows
                            if provenance.get(item.claim_id, {}).get("document_id")
                        }
                    )
                ),
                source_urls=tuple(
                    sorted(
                        {
                            _canonical_url(
                                str(
                                    provenance.get(item.claim_id, {}).get(
                                        "source_url"
                                    )
                                    or ""
                                )
                            )
                            for item in rows
                            if provenance.get(item.claim_id, {}).get("source_url")
                        }
                    )
                ),
                claim_ids=tuple(sorted({item.claim_id for item in rows})),
                impact_ids=tuple(sorted(item.impact_id for item in rows)),
            )
        )
    return tuple(result)


def _budget_violation_count(
    items: Sequence[CreditValidatedImpact],
    *,
    keys: Any,
    cap: float,
) -> int:
    groups: dict[Any, float] = {}
    for item in items:
        identity = keys(item)
        groups[identity] = groups.setdefault(identity, 0.0) + item.validated_credit_fraction
    return sum(total > cap + 1e-6 for total in groups.values())


def _correlation_violation_count(
    items: Sequence[CreditValidatedImpact],
    *,
    groups: Mapping[tuple[str, str], str],
    cap: float,
) -> int:
    return _budget_violation_count(
        items,
        keys=lambda item: (
            item.claim_id,
            groups.get((item.archetype_id, item.primitive_id), item.impact_id),
        ),
        cap=cap,
    )


def _duplicate_credit_count(
    items: Sequence[CreditValidatedImpact], *, key: Any
) -> int:
    groups: dict[Any, int] = {}
    for item in items:
        if item.validated_credit_fraction <= 0:
            continue
        identity = key(item)
        groups[identity] = groups.setdefault(identity, 0) + 1
    return sum(max(count - 1, 0) for count in groups.values())


def _normalize_text(value: str) -> str:
    normalized = re.sub(r"[^0-9a-zA-Z가-힣.%+-]+", " ", value.casefold())
    return " ".join(normalized.split())


def _canonical_url(value: str) -> str:
    if not value:
        return ""
    parsed = urlsplit(value)
    return urlunsplit(
        (
            parsed.scheme.casefold(),
            parsed.netloc.casefold(),
            parsed.path.rstrip("/"),
            "",
            "",
        )
    )


def _source_independence_key(
    *, proposal: Any, provenance: Mapping[str, Any]
) -> str:
    if proposal.source_family in {"ISSUER_OFFICIAL", "OFFICIAL_FILING"}:
        return f"ISSUER:{proposal.target_id}"
    source_url = str(provenance.get("source_url") or "")
    domain = urlsplit(source_url).netloc.casefold()
    return domain or f"{proposal.source_family}:{proposal.evidence_family_id}"


def audit_impact_validator_v2(
    *, repo_root: str | Path = "."
) -> Mapping[str, Any]:
    """Frozen Phase-58 corpus를 새 validator로 재생한다."""

    from .claim_eligibility import compile_claim_eligibility_decisions
    from .claim_impact_ledger import (
        ClaimImpactLedgerBuilder,
        ClaimImpactProposal,
    )

    root = Path(repo_root).resolve()
    target_rows = {}
    aggregate_critical: dict[str, int] = {}
    for target_id in ("005930", "000660"):
        dossier = (
            root / "output/evidence_to_score/c06/2026-07-11" / target_id
        )
        claims = _jsonl(dossier / "accepted_current_claims.jsonl")
        provenance = _jsonl(dossier / "claim_provenance.jsonl")
        proposals = []
        for raw in _jsonl(dossier / "claim_impacts_proposed.jsonl"):
            row = dict(raw)
            row["unsupported_aspects"] = tuple(
                row.get("unsupported_aspects") or ()
            )
            row["counter_claim_ids"] = tuple(
                row.get("counter_claim_ids") or ()
            )
            row["lineage_mapping_ids"] = tuple(
                row.get("lineage_mapping_ids") or ()
            )
            proposals.append(ClaimImpactProposal(**row))
        decisions = tuple(
            decision.to_dict()
            for decision in compile_claim_eligibility_decisions(
                claims=claims,
                claim_provenance=provenance,
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            )
        )
        ledger = ClaimImpactLedgerBuilder().build(
            proposals=proposals,
            accepted_current_claims=claims,
            claim_provenance=provenance,
            source_task_satisfaction=(),
            claim_eligibility_decisions=decisions,
        )
        validation = ImpactValidator().validate(
            impacts=ledger.validated_impacts,
            claim_provenance=provenance,
            claim_eligibility_decisions=decisions,
            accepted_current_claims=claims,
        )
        target_rows[target_id] = {
            "proposal_count": len(proposals),
            "ledger_validated_count": len(ledger.validated_impacts),
            "ledger_scope_rejected_count": sum(
                row.get("reason")
                in {"REROUTED_TO_OTHER_MECHANISM", "MECHANISM_SCOPE_REJECTED"}
                for row in ledger.rejected_impacts
            ),
            "validator_audit": validation.audit,
            "economic_fact_clusters": [
                row.to_dict() for row in validation.economic_fact_clusters
            ],
            "document_clusters": [
                row.to_dict() for row in validation.document_clusters
            ],
        }
        for name, value in validation.audit["critical_counts"].items():
            aggregate_critical[name] = aggregate_critical.setdefault(name, 0) + int(
                value
            )
    critical_sum = sum(aggregate_critical.values())
    return {
        "schema_version": "e2r_impact_validator_v2_frozen_audit_v1",
        "status": (
            "STRICT_IMPACT_VALIDATOR_V2_PASS"
            if critical_sum == 0
            else "STRICT_IMPACT_VALIDATOR_V2_FAIL"
        ),
        "frozen_source_commit": "52f09f3",
        "targets": target_rows,
        "critical_counts": dict(sorted(aggregate_critical.items())),
        "critical_count_sum": critical_sum,
    }


def compile_fact_document_dedupe_audit(
    impact_audit: Mapping[str, Any]
) -> Mapping[str, Any]:
    targets = impact_audit["targets"]
    critical = {
        "same_fact_duplicate_credit_count": sum(
            int(row["validator_audit"]["critical_counts"][
                "same_fact_duplicate_credit_count"
            ])
            for row in targets.values()
        ),
        "same_document_duplicate_credit_count": sum(
            int(row["validator_audit"]["critical_counts"][
                "same_document_duplicate_credit_count"
            ])
            for row in targets.values()
        ),
    }
    critical_sum = sum(critical.values())
    return {
        "schema_version": "e2r_fact_document_dedupe_audit_v1",
        "status": (
            "FACT_DOCUMENT_DEDUPE_PASS"
            if critical_sum == 0
            else "FACT_DOCUMENT_DEDUPE_FAIL"
        ),
        "targets": {
            target_id: {
                "economic_fact_cluster_count": len(
                    row["economic_fact_clusters"]
                ),
                "document_cluster_count": len(row["document_clusters"]),
                "suppressed_same_fact_duplicate_count": row[
                    "validator_audit"
                ]["suppressed_same_fact_duplicate_count"],
                "suppressed_same_document_duplicate_count": row[
                    "validator_audit"
                ]["suppressed_same_document_duplicate_count"],
            }
            for target_id, row in targets.items()
        },
        "critical_counts": critical,
        "critical_count_sum": critical_sum,
    }


def _jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    return tuple(
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )


__all__ = [
    "CreditValidatedImpact",
    "DocumentCluster",
    "EconomicFactCluster",
    "ImpactValidationResult",
    "ImpactValidator",
    "audit_impact_validator_v2",
    "compile_fact_document_dedupe_audit",
]
