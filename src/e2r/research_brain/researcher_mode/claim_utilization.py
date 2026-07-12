"""Terminal claim utilization and many-to-many component credit accounting."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import math
import re
from typing import Any, Mapping, Sequence

from e2r.research_brain.intelligence_schema import stable_intelligence_id

from .evidence_fact_compiler import FactCompilationResult
from .schemas import CANONICAL_COMPONENT_ORDER, EvidenceFact


CLAIM_UTILIZATION_STATUSES = (
    "SCORED_SUPPORT",
    "SCORED_COUNTER",
    "CONFIDENCE_ONLY",
    "PROFILE_ONLY",
    "WRONG_MECHANISM",
    "DUPLICATE_FACT",
    "SUPERSEDED",
    "REJECTED_WITH_REASON",
)

COMPONENT_MECHANISM_IDS_BY_COMPONENT: Mapping[str, tuple[str, ...]] = {
    "eps_fcf_explosion": (
        "EARNINGS_CONVERSION",
        "FREE_CASH_FLOW_CONVERSION",
        "GROWTH_MAGNITUDE",
    ),
    "earnings_visibility": (
        "REVENUE_VISIBILITY",
        "CONTRACT_DURABILITY",
        "BACKLOG_OR_CAPACITY_VISIBILITY",
    ),
    "bottleneck_pricing": (
        "STRUCTURAL_SCARCITY",
        "PRICING_POWER",
        "CAPACITY_LOCK_OR_SHORTAGE",
    ),
    "market_mispricing": (
        "EXPECTATION_GAP",
        "EARNINGS_REVISION",
        "SURPRISE_OR_RELATIVE_REACTION",
    ),
    "valuation_rerating": (
        "VALUATION_MULTIPLE",
        "DURATION_RERATING",
        "FORWARD_CASH_YIELD",
    ),
    "capital_allocation": (
        "CAPITAL_ALLOCATION",
        "BALANCE_SHEET_CHANGE",
        "CAPEX_RETURN_DISCIPLINE",
    ),
    "information_confidence": (
        "SOURCE_DIRECTNESS",
        "INDEPENDENT_CORROBORATION",
        "DISCLOSURE_QUALITY",
    ),
}

_IMPACT_DIRECTIONS = {"SUPPORT", "COUNTER"}
_EXPLICIT_NON_SCORING_STATUSES = {
    "PROFILE_ONLY",
    "WRONG_MECHANISM",
    "REJECTED_WITH_REASON",
}


@dataclass(frozen=True)
class ClaimComponentImpactProposal:
    impact_id: str
    claim_id: str
    fact_id: str
    component_id: str
    direction: str
    component_mechanism_id: str
    fact_economic_mechanism: str
    proposed_credit_units: float
    rationale: str
    production_points_authority: bool = False
    schema_version: str = "e2r_claim_component_impact_proposal_v1"

    def __post_init__(self) -> None:
        if not all(
            str(value).strip()
            for value in (
                self.impact_id,
                self.claim_id,
                self.fact_id,
                self.component_id,
                self.direction,
                self.component_mechanism_id,
                self.fact_economic_mechanism,
                self.rationale,
            )
        ):
            raise ValueError("claim component impact proposal is incomplete")
        if self.direction not in _IMPACT_DIRECTIONS:
            raise ValueError("claim component impact direction is invalid")
        if (
            isinstance(self.proposed_credit_units, bool)
            or not math.isfinite(float(self.proposed_credit_units))
            or not 0 < float(self.proposed_credit_units) <= 1
        ):
            raise ValueError("proposed credit units must be in (0, 1]")
        if self.production_points_authority:
            raise ValueError("claim impact proposals cannot assign production points")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ClaimTerminalDisposition:
    disposition_id: str
    claim_id: str
    fact_id: str | None
    status: str
    rationale: str
    component_ids: tuple[str, ...] = ()
    production_score_authority: bool = False
    schema_version: str = "e2r_claim_terminal_disposition_v1"

    def __post_init__(self) -> None:
        if self.status not in _EXPLICIT_NON_SCORING_STATUSES:
            raise ValueError("explicit disposition must be a non-scoring status")
        if not all(
            str(value).strip()
            for value in (self.disposition_id, self.claim_id, self.rationale)
        ):
            raise ValueError("claim terminal disposition is incomplete")
        if len(self.component_ids) != len(set(self.component_ids)) or any(
            value not in CANONICAL_COMPONENT_ORDER for value in self.component_ids
        ):
            raise ValueError("claim disposition component ids are invalid")
        if self.production_score_authority:
            raise ValueError("non-scoring dispositions cannot assign score")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ValidatedClaimComponentImpact:
    impact_id: str
    claim_id: str
    fact_id: str
    component_id: str
    direction: str
    component_mechanism_id: str
    fact_economic_mechanism: str
    proposed_credit_units: float
    validated_credit_units: float
    credit_once_key: str
    mechanism_validation_id: str
    claim_cap_scaled: bool
    fact_cap_scaled: bool
    component_fact_cap_scaled: bool
    rationale: str
    production_points_authority: bool = False
    schema_version: str = "e2r_validated_claim_component_impact_v1"

    def __post_init__(self) -> None:
        if self.component_id not in CANONICAL_COMPONENT_ORDER:
            raise ValueError("validated impact component is invalid")
        if self.direction not in _IMPACT_DIRECTIONS:
            raise ValueError("validated impact direction is invalid")
        if not 0 < self.validated_credit_units <= self.proposed_credit_units <= 1:
            raise ValueError("validated impact credit units are invalid")
        if not self.credit_once_key or not self.mechanism_validation_id:
            raise ValueError("validated impact requires credit and mechanism lineage")
        if self.production_points_authority:
            raise ValueError("validated claim impacts cannot assign production points")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ClaimImpactRejection:
    impact_id: str
    claim_id: str
    fact_id: str
    reason: str

    def __post_init__(self) -> None:
        if not all(
            str(value).strip()
            for value in (self.impact_id, self.claim_id, self.fact_id, self.reason)
        ):
            raise ValueError("claim impact rejection is incomplete")

    def to_dict(self) -> Mapping[str, str]:
        return asdict(self)


@dataclass(frozen=True)
class ClaimUtilizationDecision:
    utilization_id: str
    claim_id: str
    fact_id: str | None
    status: str
    component_ids: tuple[str, ...]
    impact_ids: tuple[str, ...]
    rationale: str
    material_claim: bool
    terminal: bool = True
    production_score_authority: bool = False
    schema_version: str = "e2r_claim_utilization_decision_v1"

    def __post_init__(self) -> None:
        if self.status not in CLAIM_UTILIZATION_STATUSES:
            raise ValueError("unknown claim utilization status")
        if not all(
            str(value).strip()
            for value in (self.utilization_id, self.claim_id, self.rationale)
        ):
            raise ValueError("claim utilization decision is incomplete")
        if not self.terminal:
            raise ValueError("claim utilization rows must be terminal")
        if len(self.component_ids) != len(set(self.component_ids)) or any(
            value not in CANONICAL_COMPONENT_ORDER for value in self.component_ids
        ):
            raise ValueError("claim utilization components are invalid")
        if len(self.impact_ids) != len(set(self.impact_ids)):
            raise ValueError("claim utilization impact ids must be unique")
        scored = self.status in {"SCORED_SUPPORT", "SCORED_COUNTER"}
        if scored != bool(self.impact_ids):
            raise ValueError("scored utilization requires impacts and only scored rows may cite them")
        if self.production_score_authority:
            raise ValueError("claim utilization cannot assign production score")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ClaimUtilizationLedgerResult:
    status: str
    validated_impacts: tuple[ValidatedClaimComponentImpact, ...]
    rejected_impacts: tuple[ClaimImpactRejection, ...]
    utilization_decisions: tuple[ClaimUtilizationDecision, ...]
    audit: Mapping[str, Any]
    ready_for_component_scoring_memos: bool
    production_score_authority: bool = False
    schema_version: str = "e2r_claim_utilization_ledger_v1"

    def __post_init__(self) -> None:
        if self.status not in {
            "CLAIM_UTILIZATION_COMPLETE",
            "CLAIM_UTILIZATION_PENDING",
        }:
            raise ValueError("unknown claim utilization ledger status")
        if self.ready_for_component_scoring_memos != (
            self.status == "CLAIM_UTILIZATION_COMPLETE"
            and int(self.audit.get("critical_count_sum") or 0) == 0
        ):
            raise ValueError("claim utilization ready flag disagrees with audit")
        if self.production_score_authority:
            raise ValueError("claim utilization ledger cannot assign production score")
        impact_ids = [row.impact_id for row in self.validated_impacts]
        if len(impact_ids) != len(set(impact_ids)):
            raise ValueError("validated impact ids must be unique")
        utilization_ids = [row.utilization_id for row in self.utilization_decisions]
        if len(utilization_ids) != len(set(utilization_ids)):
            raise ValueError("claim utilization ids must be unique")
        cited_impacts = {
            impact_id
            for row in self.utilization_decisions
            for impact_id in row.impact_ids
        }
        if cited_impacts != set(impact_ids):
            raise ValueError("validated impacts and utilization lineage do not reconcile")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "status": self.status,
            "validated_impacts": [row.to_dict() for row in self.validated_impacts],
            "rejected_impacts": [row.to_dict() for row in self.rejected_impacts],
            "utilization_decisions": [
                row.to_dict() for row in self.utilization_decisions
            ],
            "audit": dict(self.audit),
            "ready_for_component_scoring_memos": (
                self.ready_for_component_scoring_memos
            ),
            "production_score_authority": False,
        }


class ClaimUtilizationLedgerBuilder:
    """Validate claim→fact→component use without calculating component points."""

    def build(
        self,
        *,
        fact_compilation: FactCompilationResult,
        impact_proposals: Sequence[ClaimComponentImpactProposal],
        explicit_dispositions: Sequence[ClaimTerminalDisposition] = (),
        claim_total_credit_cap: float = 1.0,
        fact_total_credit_cap: float = 1.0,
        component_fact_credit_cap: float = 1.0,
    ) -> ClaimUtilizationLedgerResult:
        caps = (
            float(claim_total_credit_cap),
            float(fact_total_credit_cap),
            float(component_fact_credit_cap),
        )
        if any(not math.isfinite(value) or not 0 < value <= 1 for value in caps):
            raise ValueError("claim/fact credit caps must be in (0, 1]")
        fact_by_id = {row.fact_id: row for row in fact_compilation.facts}
        link_by_claim = {
            row.claim_id: row for row in fact_compilation.claim_fact_links
        }
        proposals = tuple(impact_proposals)
        proposal_ids = [row.impact_id for row in proposals]
        duplicate_proposal_ids = {
            value for value in proposal_ids if proposal_ids.count(value) > 1
        }
        candidates: list[ClaimComponentImpactProposal] = []
        rejections: list[ClaimImpactRejection] = []
        credit_keys: set[tuple[str, str, str, str]] = set()
        for proposal in proposals:
            reason = ""
            link = link_by_claim.get(proposal.claim_id)
            fact = fact_by_id.get(proposal.fact_id)
            if proposal.impact_id in duplicate_proposal_ids:
                reason = "DUPLICATE_IMPACT_ID"
            elif link is None:
                reason = "CLAIM_FACT_LINK_MISSING"
            elif link.fact_id != proposal.fact_id or fact is None:
                reason = "CLAIM_FACT_LINEAGE_MISMATCH"
            elif link.link_role != "PRIMARY_FACT_CLAIM":
                reason = "CORROBORATION_OR_DUPLICATE_CANNOT_SCORE_AGAIN"
            elif fact.current_lifecycle in {"RESOLVED", "SUPERSEDED"}:
                reason = "FACT_NOT_CURRENT_FOR_SCORING"
            elif proposal.component_id not in CANONICAL_COMPONENT_ORDER:
                reason = "UNKNOWN_COMPONENT"
            elif proposal.component_mechanism_id not in set(
                COMPONENT_MECHANISM_IDS_BY_COMPONENT.get(
                    proposal.component_id, ()
                )
            ):
                reason = "WRONG_COMPONENT_MECHANISM"
            elif _normalize_text(proposal.fact_economic_mechanism) != _normalize_text(
                fact.economic_mechanism
            ):
                reason = "FACT_ECONOMIC_MECHANISM_MISMATCH"
            key = (
                proposal.fact_id,
                proposal.component_id,
                proposal.direction,
                proposal.component_mechanism_id,
            )
            if not reason and key in credit_keys:
                reason = "DUPLICATE_FACT_COMPONENT_CREDIT"
            if reason:
                rejections.append(
                    ClaimImpactRejection(
                        impact_id=proposal.impact_id,
                        claim_id=proposal.claim_id,
                        fact_id=proposal.fact_id,
                        reason=reason,
                    )
                )
                continue
            credit_keys.add(key)
            candidates.append(proposal)

        credit = {
            row.impact_id: float(row.proposed_credit_units) for row in candidates
        }
        claim_scaled = _scale_credit_groups(
            candidates,
            credit,
            key=lambda row: row.claim_id,
            cap=caps[0],
        )
        fact_scaled = _scale_credit_groups(
            candidates,
            credit,
            key=lambda row: row.fact_id,
            cap=caps[1],
        )
        component_fact_scaled = _scale_credit_groups(
            candidates,
            credit,
            key=lambda row: (row.fact_id, row.component_id),
            cap=caps[2],
        )
        validated = tuple(
            ValidatedClaimComponentImpact(
                impact_id=row.impact_id,
                claim_id=row.claim_id,
                fact_id=row.fact_id,
                component_id=row.component_id,
                direction=row.direction,
                component_mechanism_id=row.component_mechanism_id,
                fact_economic_mechanism=row.fact_economic_mechanism,
                proposed_credit_units=float(row.proposed_credit_units),
                validated_credit_units=round(credit[row.impact_id], 12),
                credit_once_key=stable_intelligence_id(
                    "CREDITONCE",
                    {
                        "fact_id": row.fact_id,
                        "component_id": row.component_id,
                        "direction": row.direction,
                        "component_mechanism_id": row.component_mechanism_id,
                    },
                ),
                mechanism_validation_id=stable_intelligence_id(
                    "MECHVAL",
                    {
                        "fact_id": row.fact_id,
                        "fact_economic_mechanism": _normalize_text(
                            row.fact_economic_mechanism
                        ),
                        "component_id": row.component_id,
                        "component_mechanism_id": row.component_mechanism_id,
                    },
                ),
                claim_cap_scaled=row.impact_id in claim_scaled,
                fact_cap_scaled=row.impact_id in fact_scaled,
                component_fact_cap_scaled=(
                    row.impact_id in component_fact_scaled
                ),
                rationale=row.rationale,
            )
            for row in sorted(candidates, key=lambda value: value.impact_id)
        )
        decisions, disposition_errors, missing_material = _utilization_decisions(
            fact_compilation=fact_compilation,
            validated_impacts=validated,
            rejected_impacts=tuple(rejections),
            explicit_dispositions=explicit_dispositions,
        )
        claim_sums = _credit_sums(validated, key=lambda row: row.claim_id)
        fact_sums = _credit_sums(validated, key=lambda row: row.fact_id)
        component_fact_sums = _credit_sums(
            validated,
            key=lambda row: (row.fact_id, row.component_id),
        )
        duplicate_scored = sum(
            row.status in {"SCORED_SUPPORT", "SCORED_COUNTER"}
            and link_by_claim.get(row.claim_id)
            and link_by_claim[row.claim_id].link_role != "PRIMARY_FACT_CLAIM"
            for row in decisions
        )
        critical = {
            "accepted_claim_without_fact_count": (
                fact_compilation.accepted_claim_without_fact_count
            ),
            "material_claim_without_terminal_utilization_count": missing_material,
            "invalid_explicit_disposition_count": len(disposition_errors),
            "duplicate_or_corroboration_scored_again_count": duplicate_scored,
            "claim_credit_cap_violation_count": sum(
                value > caps[0] + 1e-9 for value in claim_sums.values()
            ),
            "fact_credit_cap_violation_count": sum(
                value > caps[1] + 1e-9 for value in fact_sums.values()
            ),
            "component_fact_credit_cap_violation_count": sum(
                value > caps[2] + 1e-9
                for value in component_fact_sums.values()
            ),
            "duplicate_credit_once_key_count": len(validated)
            - len({row.credit_once_key for row in validated}),
            "mechanism_validation_missing_count": sum(
                not row.mechanism_validation_id for row in validated
            ),
            "question_or_primitive_tag_score_gateway_count": 0,
            "production_points_authority_count": sum(
                row.production_points_authority for row in validated
            ),
        }
        critical_sum = sum(critical.values())
        audit = {
            "schema_version": "e2r_claim_utilization_audit_v1",
            "critical_counts": critical,
            "critical_count_sum": critical_sum,
            "input_claim_count": fact_compilation.input_claim_count,
            "fact_count": len(fact_compilation.facts),
            "claim_fact_link_count": len(fact_compilation.claim_fact_links),
            "validated_impact_count": len(validated),
            "rejected_impact_count": len(rejections),
            "utilization_decision_count": len(decisions),
            "utilization_status_counts": {
                status: sum(row.status == status for row in decisions)
                for status in CLAIM_UTILIZATION_STATUSES
            },
            "claim_credit_cap": caps[0],
            "fact_credit_cap": caps[1],
            "component_fact_credit_cap": caps[2],
            "claim_cap_scaled_impact_count": len(claim_scaled),
            "fact_cap_scaled_impact_count": len(fact_scaled),
            "component_fact_cap_scaled_impact_count": len(
                component_fact_scaled
            ),
            "independent_corroboration_improves_confidence": True,
            "same_fact_points_once": True,
            "question_family_score_gateway": False,
            "primitive_score_gateway": False,
            "production_score_authority": False,
            "disposition_errors": disposition_errors,
        }
        status = (
            "CLAIM_UTILIZATION_COMPLETE"
            if critical_sum == 0
            else "CLAIM_UTILIZATION_PENDING"
        )
        return ClaimUtilizationLedgerResult(
            status=status,
            validated_impacts=validated,
            rejected_impacts=tuple(
                sorted(rejections, key=lambda row: (row.claim_id, row.impact_id))
            ),
            utilization_decisions=decisions,
            audit=audit,
            ready_for_component_scoring_memos=critical_sum == 0,
        )


def _utilization_decisions(
    *,
    fact_compilation: FactCompilationResult,
    validated_impacts: Sequence[ValidatedClaimComponentImpact],
    rejected_impacts: Sequence[ClaimImpactRejection],
    explicit_dispositions: Sequence[ClaimTerminalDisposition],
) -> tuple[tuple[ClaimUtilizationDecision, ...], tuple[Mapping[str, Any], ...], int]:
    fact_by_id = {row.fact_id: row for row in fact_compilation.facts}
    impacts_by_claim: dict[str, list[ValidatedClaimComponentImpact]] = {}
    rejected_by_claim: dict[str, list[ClaimImpactRejection]] = {}
    for row in validated_impacts:
        impacts_by_claim.setdefault(row.claim_id, []).append(row)
    for row in rejected_impacts:
        rejected_by_claim.setdefault(row.claim_id, []).append(row)
    explicit_by_claim: dict[str, ClaimTerminalDisposition] = {}
    errors: list[Mapping[str, Any]] = []
    for row in explicit_dispositions:
        if row.claim_id in explicit_by_claim:
            errors.append(
                {
                    "disposition_id": row.disposition_id,
                    "claim_id": row.claim_id,
                    "reason": "DUPLICATE_EXPLICIT_DISPOSITION",
                }
            )
        else:
            explicit_by_claim[row.claim_id] = row

    decisions: list[ClaimUtilizationDecision] = []
    for rejection in fact_compilation.rejected_claims:
        decisions.append(
            _decision(
                claim_id=rejection.claim_id,
                fact_id=None,
                status="REJECTED_WITH_REASON",
                component_ids=(),
                impact_ids=(),
                rationale=rejection.reason,
                material_claim=rejection.material_claim,
                discriminator=f"REJECTION:{rejection.input_index}",
            )
        )
    missing_material = 0
    known_claim_ids = {
        row.claim_id for row in fact_compilation.claim_fact_links
    } | {row.claim_id for row in fact_compilation.rejected_claims}
    for claim_id, disposition in explicit_by_claim.items():
        link = next(
            (
                row
                for row in fact_compilation.claim_fact_links
                if row.claim_id == claim_id
            ),
            None,
        )
        if claim_id not in known_claim_ids:
            errors.append(
                {
                    "disposition_id": disposition.disposition_id,
                    "claim_id": claim_id,
                    "reason": "EXPLICIT_DISPOSITION_UNKNOWN_CLAIM",
                }
            )
        elif link is None or link.link_role != "PRIMARY_FACT_CLAIM":
            errors.append(
                {
                    "disposition_id": disposition.disposition_id,
                    "claim_id": claim_id,
                    "reason": "EXPLICIT_DISPOSITION_NOT_PRIMARY_FACT_CLAIM",
                }
            )
        elif disposition.fact_id not in {None, link.fact_id}:
            errors.append(
                {
                    "disposition_id": disposition.disposition_id,
                    "claim_id": claim_id,
                    "reason": "EXPLICIT_DISPOSITION_FACT_MISMATCH",
                }
            )
        elif impacts_by_claim.get(claim_id):
            errors.append(
                {
                    "disposition_id": disposition.disposition_id,
                    "claim_id": claim_id,
                    "reason": "EXPLICIT_NONSCORING_DISPOSITION_CONFLICTS_WITH_IMPACT",
                }
            )
    for link in fact_compilation.claim_fact_links:
        fact = fact_by_id[link.fact_id]
        if fact.current_lifecycle in {"RESOLVED", "SUPERSEDED"}:
            decisions.append(
                _decision(
                    claim_id=link.claim_id,
                    fact_id=link.fact_id,
                    status="SUPERSEDED",
                    component_ids=(),
                    impact_ids=(),
                    rationale=f"fact lifecycle is {fact.current_lifecycle}",
                    material_claim=link.material_claim,
                )
            )
            continue
        if link.link_role == "INDEPENDENT_CORROBORATION":
            decisions.append(
                _decision(
                    claim_id=link.claim_id,
                    fact_id=link.fact_id,
                    status="CONFIDENCE_ONLY",
                    component_ids=(),
                    impact_ids=(),
                    rationale="independent source corroborates an already unique economic fact",
                    material_claim=link.material_claim,
                )
            )
            continue
        if link.link_role == "SAME_GROUP_DUPLICATE":
            decisions.append(
                _decision(
                    claim_id=link.claim_id,
                    fact_id=link.fact_id,
                    status="DUPLICATE_FACT",
                    component_ids=(),
                    impact_ids=(),
                    rationale="same independence group repeats the same economic fact",
                    material_claim=link.material_claim,
                )
            )
            continue
        impacts = impacts_by_claim.get(link.claim_id, [])
        for direction, status in (
            ("SUPPORT", "SCORED_SUPPORT"),
            ("COUNTER", "SCORED_COUNTER"),
        ):
            selected = [row for row in impacts if row.direction == direction]
            if selected:
                decisions.append(
                    _decision(
                        claim_id=link.claim_id,
                        fact_id=link.fact_id,
                        status=status,
                        component_ids=tuple(
                            sorted({row.component_id for row in selected})
                        ),
                        impact_ids=tuple(sorted(row.impact_id for row in selected)),
                        rationale=(
                            "validated component-specific economic mechanism and bounded credit"
                        ),
                        material_claim=link.material_claim,
                    )
                )
        if impacts:
            continue
        disposition = explicit_by_claim.get(link.claim_id)
        disposition_error = any(
            row["claim_id"] == link.claim_id for row in errors
        )
        if disposition and not disposition_error:
            decisions.append(
                _decision(
                    claim_id=link.claim_id,
                    fact_id=link.fact_id,
                    status=disposition.status,
                    component_ids=disposition.component_ids,
                    impact_ids=(),
                    rationale=disposition.rationale,
                    material_claim=link.material_claim,
                )
            )
            continue
        rejected = rejected_by_claim.get(link.claim_id, [])
        wrong_mechanism = any(
            row.reason
            in {"WRONG_COMPONENT_MECHANISM", "FACT_ECONOMIC_MECHANISM_MISMATCH"}
            for row in rejected
        )
        reason = (
            ";".join(sorted({row.reason for row in rejected}))
            if rejected
            else "MATERIAL_CLAIM_UTILIZATION_MISSING"
        )
        status = "WRONG_MECHANISM" if wrong_mechanism else "REJECTED_WITH_REASON"
        decisions.append(
            _decision(
                claim_id=link.claim_id,
                fact_id=link.fact_id,
                status=status,
                component_ids=(),
                impact_ids=(),
                rationale=reason,
                material_claim=link.material_claim,
            )
        )
        if link.material_claim and not rejected and not disposition:
            missing_material += 1
    return (
        tuple(sorted(decisions, key=lambda row: row.utilization_id)),
        tuple(errors),
        missing_material,
    )


def _decision(
    *,
    claim_id: str,
    fact_id: str | None,
    status: str,
    component_ids: tuple[str, ...],
    impact_ids: tuple[str, ...],
    rationale: str,
    material_claim: bool,
    discriminator: str = "",
) -> ClaimUtilizationDecision:
    identity = {
        "claim_id": claim_id,
        "fact_id": fact_id,
        "status": status,
        "component_ids": component_ids,
        "impact_ids": impact_ids,
        "discriminator": discriminator,
    }
    return ClaimUtilizationDecision(
        utilization_id=stable_intelligence_id("CUTIL", identity),
        claim_id=claim_id,
        fact_id=fact_id,
        status=status,
        component_ids=component_ids,
        impact_ids=impact_ids,
        rationale=rationale,
        material_claim=material_claim,
    )


def _scale_credit_groups(
    rows: Sequence[ClaimComponentImpactProposal],
    credit: dict[str, float],
    *,
    key,
    cap: float,
) -> set[str]:
    groups: dict[Any, list[ClaimComponentImpactProposal]] = {}
    for row in rows:
        groups.setdefault(key(row), []).append(row)
    scaled: set[str] = set()
    for members in groups.values():
        total = sum(credit[row.impact_id] for row in members)
        if total <= cap + 1e-12:
            continue
        ratio = cap / total
        for row in members:
            credit[row.impact_id] *= ratio
            scaled.add(row.impact_id)
    return scaled


def _credit_sums(rows: Sequence[ValidatedClaimComponentImpact], *, key) -> Mapping[Any, float]:
    result: dict[Any, float] = {}
    for row in rows:
        group = key(row)
        result[group] = result.get(group, 0.0) + row.validated_credit_units
    return result


def _normalize_text(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "").strip()).casefold()


__all__ = [
    "CLAIM_UTILIZATION_STATUSES",
    "COMPONENT_MECHANISM_IDS_BY_COMPONENT",
    "ClaimComponentImpactProposal",
    "ClaimImpactRejection",
    "ClaimTerminalDisposition",
    "ClaimUtilizationDecision",
    "ClaimUtilizationLedgerBuilder",
    "ClaimUtilizationLedgerResult",
    "ValidatedClaimComponentImpact",
]
