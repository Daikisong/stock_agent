"""Research-calibrated component aggregation and full-score validity gate."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Mapping, Sequence

from e2r.research_brain.runtime.scoring_contracts import (
    ArchetypeScoringContract,
)

from .component_assessment import (
    ComponentAssessment,
    TERMINAL_FULL_SCORE_STATUSES,
)
from .component_scoring_model import (
    load_component_scoring_model,
    score_component_subcriteria,
)
from .full_score_validity import (
    FullScoreValidityEvidenceV2,
    evaluate_full_score_validity_v2,
)
from .impact_validator import CreditValidatedImpact


@dataclass(frozen=True)
class ResearchCalibratedScoreResult:
    profile_id: str
    profile_version: str
    contract_hash: str
    component_score_vector: Mapping[str, float]
    verified_supported_score: float
    provisional_score_lower: float
    provisional_score_upper: float
    full_e2r_score: float | None
    full_score_valid: bool
    score_type: str
    score_confidence: float
    material_nonterminal_components: tuple[str, ...]
    audit: Mapping[str, Any]

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


class ResearchCalibratedComponentScorer:
    def score(
        self,
        *,
        contract: ArchetypeScoringContract,
        impacts: Sequence[CreditValidatedImpact],
        assessments: Sequence[ComponentAssessment],
        validity_evidence: FullScoreValidityEvidenceV2 | None = None,
    ) -> ResearchCalibratedScoreResult:
        by_component = {row.component_id: row for row in assessments}
        if set(by_component) != set(contract.component_weights):
            raise ValueError(
                "component assessment coverage differs from calibrated profile"
            )
        model = load_component_scoring_model(contract.archetype_id)
        calibrated = (
            score_component_subcriteria(model=model, impacts=impacts)
            if model is not None
            else None
        )
        for component_id, assessment in by_component.items():
            if (
                abs(
                    assessment.max_points
                    - contract.component_max_points[component_id]
                )
                > 1e-6
            ):
                raise ValueError(
                    "component max points differ from calibrated profile"
                )
            expected = (
                calibrated.component_points[component_id]
                if calibrated is not None
                else round(
                    assessment.max_points
                    * min(
                        1.0,
                        sum(
                            impact.support_credit_fraction
                            for impact in impacts
                            if impact.component_id == component_id
                        ),
                    ),
                    6,
                )
            )
            if (
                assessment.support_impact_ids
                and abs(assessment.verified_points - expected) > 1e-6
            ):
                raise ValueError(
                    "component points differ from validated impacts"
                )
        vector = {
            key: round(by_component[key].verified_points, 6)
            for key in contract.component_weights
        }
        verified = round(sum(vector.values()), 6)
        lower = round(
            sum(row.lower_bound_points for row in assessments), 6
        )
        upper = round(
            sum(row.upper_bound_points for row in assessments), 6
        )
        validity = evaluate_full_score_validity_v2(
            assessments=assessments,
            evidence=validity_evidence,
        )
        full_valid = validity.full_score_valid
        full = verified if full_valid else None
        nonterminal = tuple(
            row.component_id
            for row in assessments
            if row.status not in TERMINAL_FULL_SCORE_STATUSES
        )
        confidence = round(
            sum(row.confidence * row.max_points for row in assessments)
            / 100.0,
            6,
        )
        critical = {
            "balanced_point_score_count": int(
                len(set(vector.values())) == 1
                and len(vector) > 1
                and verified > 0
            ),
            "calibrated_profile_not_used_count": 0,
            "supported_component_lost_count": sum(
                bool(row.support_impact_ids)
                and not row.counter_impact_ids
                and row.verified_points <= 0
                for row in assessments
            ),
            "full_score_with_nonterminal_component_count": int(
                full is not None and bool(nonterminal)
            ),
            "component_sum_total_mismatch_count": int(
                full is not None and abs(sum(vector.values()) - full) > 1e-6
            ),
            "full_score_validity_v2_critical_count": (
                validity.critical_count_sum
            ),
        }
        critical_sum = sum(critical.values())
        return ResearchCalibratedScoreResult(
            profile_id=contract.profile_id,
            profile_version=contract.profile_version,
            contract_hash=contract.config_hash,
            component_score_vector=vector,
            verified_supported_score=verified,
            provisional_score_lower=lower,
            provisional_score_upper=upper,
            full_e2r_score=full,
            full_score_valid=full_valid,
            score_type=(
                "FULL_E2R_100"
                if full_valid
                else "VERIFIED_COMPONENT_PARTIAL"
            ),
            score_confidence=confidence,
            material_nonterminal_components=nonterminal,
            audit={
                "schema_version": "e2r_research_calibrated_score_audit_v2",
                "status": (
                    "RESEARCH_CALIBRATED_COMPONENT_SCORING_PASS"
                    if critical_sum == 0
                    else "RESEARCH_CALIBRATED_COMPONENT_SCORING_FAIL"
                ),
                "full_score_validity": validity.to_dict(),
                "critical_counts": critical,
                "critical_count_sum": critical_sum,
            },
        )


__all__ = [
    "ResearchCalibratedComponentScorer",
    "ResearchCalibratedScoreResult",
]
