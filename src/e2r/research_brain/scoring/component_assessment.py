from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any, Mapping, Sequence

from e2r.research_brain.runtime.scoring_contracts import ArchetypeScoringContract

from .component_scoring_model import (
    ComponentSubcriterionScore,
    load_component_scoring_model,
    score_component_subcriteria,
)
from .impact_validator import CreditValidatedImpact


class ComponentAssessmentStatus(str, Enum):
    VERIFIED_STRONG_SUPPORT = "VERIFIED_STRONG_SUPPORT"
    VERIFIED_PARTIAL_SUPPORT = "VERIFIED_PARTIAL_SUPPORT"
    VERIFIED_WEAK_SUPPORT = "VERIFIED_WEAK_SUPPORT"
    VERIFIED_ABSENT_AFTER_SEARCH = "VERIFIED_ABSENT_AFTER_SEARCH"
    VERIFIED_COUNTER = "VERIFIED_COUNTER"
    CONTRADICTED_OPEN = "CONTRADICTED_OPEN"
    HISTORICAL_ONLY = "HISTORICAL_ONLY"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    UNKNOWN_UNINVESTIGATED = "UNKNOWN_UNINVESTIGATED"
    SOURCE_PENDING = "SOURCE_PENDING"
    PROVIDER_PENDING = "PROVIDER_PENDING"
    BUDGET_PENDING = "BUDGET_PENDING"


TERMINAL_FULL_SCORE_STATUSES = {
    ComponentAssessmentStatus.VERIFIED_STRONG_SUPPORT.value,
    ComponentAssessmentStatus.VERIFIED_PARTIAL_SUPPORT.value,
    ComponentAssessmentStatus.VERIFIED_WEAK_SUPPORT.value,
    ComponentAssessmentStatus.VERIFIED_ABSENT_AFTER_SEARCH.value,
    ComponentAssessmentStatus.VERIFIED_COUNTER.value,
    ComponentAssessmentStatus.NOT_APPLICABLE.value,
}


@dataclass(frozen=True)
class ComponentAssessment:
    assessment_id: str
    component_id: str
    max_points: float
    status: str
    support_impact_ids: tuple[str, ...]
    counter_impact_ids: tuple[str, ...]
    verified_points: float
    lower_bound_points: float
    upper_bound_points: float
    missing_questions: tuple[str, ...]
    search_exhaustion_proof: tuple[str, ...]
    confidence: float
    scoring_model_hash: str
    aggregation_mode: str
    subcriterion_score_ids: tuple[str, ...]
    subcriterion_points: Mapping[str, float]

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ComponentAssessmentResult:
    status: str
    assessments: tuple[ComponentAssessment, ...]
    subcriterion_scores: tuple[ComponentSubcriterionScore, ...]
    material_nonterminal_components: tuple[str, ...]
    audit: Mapping[str, Any]


class ComponentAssessmentBuilder:
    def build(
        self,
        *,
        contract: ArchetypeScoringContract,
        impacts: Sequence[CreditValidatedImpact],
        terminal_evidence: Mapping[str, Mapping[str, Any]] | None = None,
    ) -> ComponentAssessmentResult:
        terminal_evidence = terminal_evidence or {}
        model = load_component_scoring_model(contract.archetype_id)
        subcriteria_result = (
            score_component_subcriteria(model=model, impacts=impacts)
            if model is not None
            else None
        )
        subcriteria_by_component: dict[
            str, tuple[ComponentSubcriterionScore, ...]
        ] = {}
        if subcriteria_result is not None:
            for component_id in contract.component_max_points:
                subcriteria_by_component[component_id] = tuple(
                    row
                    for row in subcriteria_result.scores
                    if row.component_id == component_id
                )
        assessments = []
        model_by_component = model.by_component() if model is not None else {}
        for component_id, max_points in contract.component_max_points.items():
            support = tuple(
                item
                for item in impacts
                if item.component_id == component_id
                and item.support_credit_fraction > 0
            )
            counter = tuple(
                item
                for item in impacts
                if item.component_id == component_id
                and item.counter_effect_fraction > 0
            )
            explicit = dict(terminal_evidence.get(component_id) or {})
            component_subcriteria = subcriteria_by_component.get(
                component_id, ()
            )
            if subcriteria_result is not None:
                verified = float(
                    subcriteria_result.component_points[component_id]
                )
                fraction = (
                    verified / float(max_points) if max_points else 0.0
                )
            else:
                fraction = min(
                    1.0,
                    sum(item.support_credit_fraction for item in support),
                )
                verified = round(float(max_points) * fraction, 6)
            proof = tuple(
                str(value)
                for value in explicit.get("search_exhaustion_proof") or ()
            )
            missing = tuple(
                str(value)
                for value in explicit.get("missing_questions") or ()
            )
            if support and counter:
                state = ComponentAssessmentStatus.CONTRADICTED_OPEN.value
            elif support:
                state = (
                    ComponentAssessmentStatus.VERIFIED_STRONG_SUPPORT.value
                    if fraction >= 0.75
                    else ComponentAssessmentStatus.VERIFIED_PARTIAL_SUPPORT.value
                    if fraction >= 0.4
                    else ComponentAssessmentStatus.VERIFIED_WEAK_SUPPORT.value
                )
            elif counter:
                state = ComponentAssessmentStatus.VERIFIED_COUNTER.value
            else:
                state = str(
                    explicit.get("status")
                    or ComponentAssessmentStatus.UNKNOWN_UNINVESTIGATED.value
                )
            if state not in {value.value for value in ComponentAssessmentStatus}:
                raise ValueError("unknown component assessment state")
            if (
                state
                == ComponentAssessmentStatus.VERIFIED_ABSENT_AFTER_SEARCH.value
                and not proof
            ):
                raise ValueError("evaluated absence requires search exhaustion proof")
            if state in {
                ComponentAssessmentStatus.VERIFIED_ABSENT_AFTER_SEARCH.value,
                ComponentAssessmentStatus.VERIFIED_COUNTER.value,
                ComponentAssessmentStatus.NOT_APPLICABLE.value,
            }:
                verified = 0.0
            terminal = state in TERMINAL_FULL_SCORE_STATUSES
            upper = verified if terminal else float(max_points)
            confidence = max(
                (
                    item.validated_credit_fraction
                    for item in (*support, *counter)
                ),
                default=float(explicit.get("confidence") or 0.0),
            )
            component_model = model_by_component.get(component_id)
            assessment_id = (
                f"COMP-{contract.config_hash[:8]}-{component_id}"
            )
            assessments.append(
                ComponentAssessment(
                    assessment_id=assessment_id,
                    component_id=component_id,
                    max_points=float(max_points),
                    status=state,
                    support_impact_ids=tuple(
                        item.impact_id for item in support
                    ),
                    counter_impact_ids=tuple(
                        item.impact_id for item in counter
                    ),
                    verified_points=round(verified, 6),
                    lower_bound_points=round(verified, 6),
                    upper_bound_points=round(upper, 6),
                    missing_questions=missing,
                    search_exhaustion_proof=proof,
                    confidence=round(confidence, 6),
                    scoring_model_hash=(model.config_hash if model else "LEGACY"),
                    aggregation_mode=(
                        component_model.aggregation_mode
                        if component_model is not None
                        else "LEGACY_COMPONENT_FRACTION"
                    ),
                    subcriterion_score_ids=tuple(
                        row.score_id for row in component_subcriteria
                    ),
                    subcriterion_points={
                        row.subcriterion_id: row.points
                        for row in component_subcriteria
                    },
                )
            )
        nonterminal = tuple(
            row.component_id
            for row in assessments
            if row.status not in TERMINAL_FULL_SCORE_STATUSES
        )
        critical = {
            "evaluated_absent_blocks_full_score_count": 0,
            "unknown_uninvestigated_allows_full_score_count": 0,
            "provider_pending_allows_full_score_count": 0,
            "supported_component_erased_by_other_gap_count": sum(
                bool(row.support_impact_ids) and row.verified_points <= 0
                for row in assessments
            ),
            "subcriterion_scoring_critical_count": int(
                (subcriteria_result.audit["critical_count_sum"] if subcriteria_result else 0)
            ),
            "component_subcriterion_sum_mismatch_count": sum(
                bool(row.subcriterion_points)
                and abs(sum(row.subcriterion_points.values()) - row.verified_points)
                > 1e-6
                and row.aggregation_mode != "CAP_BY_MISSING_BRIDGE"
                for row in assessments
            ),
        }
        critical_sum = sum(critical.values())
        return ComponentAssessmentResult(
            status=(
                "COMPONENT_ASSESSMENT_STATE_PASS"
                if critical_sum == 0
                else "COMPONENT_ASSESSMENT_STATE_FAIL"
            ),
            assessments=tuple(assessments),
            subcriterion_scores=(
                subcriteria_result.scores if subcriteria_result else ()
            ),
            material_nonterminal_components=nonterminal,
            audit={
                "schema_version": "e2r_component_assessment_audit_v2",
                "component_count": len(assessments),
                "subcriterion_count": sum(
                    len(row.subcriterion_score_ids) for row in assessments
                ),
                "terminal_component_count": len(assessments) - len(nonterminal),
                "nonterminal_component_count": len(nonterminal),
                "verified_supported_points": round(
                    sum(row.verified_points for row in assessments), 6
                ),
                "critical_counts": critical,
                "critical_count_sum": critical_sum,
            },
        )


__all__ = [
    "ComponentAssessment",
    "ComponentAssessmentBuilder",
    "ComponentAssessmentResult",
    "ComponentAssessmentStatus",
    "TERMINAL_FULL_SCORE_STATUSES",
]
