"""Independent semantic-research saturation contract."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Mapping, Sequence

from e2r.research_brain.intelligence_schema import stable_intelligence_id


SATURATION_REVIEW_ROLES = (
    "RESEARCH_SUPERVISOR_A",
    "RESEARCH_SUPERVISOR_B",
    "INDEPENDENT_COMPLETENESS_REVIEWER",
)


@dataclass(frozen=True)
class SaturationReview:
    review_id: str
    reviewer_role: str
    approve: bool
    seven_component_memos_complete: bool
    material_positive_routes_reviewed: bool
    counter_and_supersession_routes_checked: bool
    structured_data_complete: bool
    new_source_family_directions_reviewed: bool
    unresolved_material_questions: tuple[str, ...]
    gold_critical_fact_miss_count: int
    rationale: str

    def __post_init__(self) -> None:
        if self.reviewer_role not in SATURATION_REVIEW_ROLES:
            raise ValueError("unknown saturation reviewer role")
        if self.gold_critical_fact_miss_count < 0:
            raise ValueError("critical fact miss count cannot be negative")
        if not self.rationale.strip():
            raise ValueError("saturation review rationale is required")
        criteria = (
            self.seven_component_memos_complete,
            self.material_positive_routes_reviewed,
            self.counter_and_supersession_routes_checked,
            self.structured_data_complete,
            self.new_source_family_directions_reviewed,
            not self.unresolved_material_questions,
            self.gold_critical_fact_miss_count == 0,
        )
        if self.approve and not all(criteria):
            raise ValueError("saturation approval requires every semantic criterion")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class SemanticSaturationCertificate:
    certificate_id: str
    status: str
    review_ids: tuple[str, ...]
    pending_reasons: tuple[str, ...]
    semantic_saturation_certified: bool
    fixed_round_completion_used: bool = False
    zero_search_result_treated_as_saturation: bool = False

    def __post_init__(self) -> None:
        if self.status not in {"CERTIFIED", "PENDING"}:
            raise ValueError("unknown saturation certificate status")
        if self.fixed_round_completion_used or self.zero_search_result_treated_as_saturation:
            raise ValueError("transport outcomes cannot certify semantic saturation")
        if self.status == "CERTIFIED" and (
            not self.semantic_saturation_certified or self.pending_reasons
        ):
            raise ValueError("certified saturation cannot have pending reasons")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


class SemanticSaturationCertifier:
    def certify(
        self, reviews: Sequence[SaturationReview]
    ) -> SemanticSaturationCertificate:
        roles = [row.reviewer_role for row in reviews]
        reasons = []
        if len(roles) != len(set(roles)):
            reasons.append("DUPLICATE_SATURATION_REVIEW_ROLE")
        missing = set(SATURATION_REVIEW_ROLES) - set(roles)
        if missing:
            reasons.append("MISSING_REVIEW_ROLES:" + ",".join(sorted(missing)))
        for row in reviews:
            if not row.approve:
                reasons.append(f"{row.reviewer_role}:NOT_APPROVED")
            reasons.extend(
                f"{row.reviewer_role}:{question}"
                for question in row.unresolved_material_questions
            )
            if row.gold_critical_fact_miss_count:
                reasons.append(
                    f"{row.reviewer_role}:GOLD_CRITICAL_FACT_MISS={row.gold_critical_fact_miss_count}"
                )
        certified = not reasons and set(roles) == set(SATURATION_REVIEW_ROLES)
        payload = {
            "review_ids": sorted(row.review_id for row in reviews),
            "certified": certified,
            "pending_reasons": reasons,
        }
        return SemanticSaturationCertificate(
            certificate_id=stable_intelligence_id("SATCERT", payload),
            status="CERTIFIED" if certified else "PENDING",
            review_ids=tuple(sorted(row.review_id for row in reviews)),
            pending_reasons=tuple(dict.fromkeys(reasons)),
            semantic_saturation_certified=certified,
        )


__all__ = [
    "SATURATION_REVIEW_ROLES",
    "SaturationReview",
    "SemanticSaturationCertificate",
    "SemanticSaturationCertifier",
]
