"""Deterministic question-closure and full-thesis saturation records."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from math import isfinite
from typing import Any, Mapping

from ..ids import canonical_hash


TERMINAL_QUESTION_STATUSES = frozenset(
    {
        "SUPPORTED_SCORING",
        "PARTIALLY_SUPPORTED_SCORING",
        "SUPPORTED_NON_SCORING",
        "COUNTER_SUPPORTED",
        "EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH",
        "LIKELY_NONPUBLIC",
        "FUTURE_EVENT_ONLY",
        "NOT_APPLICABLE_WITH_REASON",
    }
)
NONTERMINAL_QUESTION_STATUSES = frozenset(
    {
        "PUBLIC_SEARCHABLE",
        "UNKNOWN_ROUTE_NOT_YET_TESTED",
        "CONTRADICTED_UNRESOLVED",
        "SOURCE_PENDING",
        "PROVIDER_PENDING",
        "PARSER_PENDING",
        "VERIFIER_REPAIR_REQUIRED",
    }
)
MATERIALITY_LEVELS = frozenset(
    {
        "NON_MATERIAL",
        "MONITORING",
        "CORE_SCORE",
        "SCORE_BOUNDARY",
        "STAGE_BOUNDARY",
        "HARD_BREAK",
    }
)


@dataclass(frozen=True)
class DeterministicQuestionBound:
    question_family_id: str
    materiality: str
    component_lower_delta: Mapping[str, float]
    component_upper_delta: Mapping[str, float]
    deterministic_lower_stage: str | None = None
    deterministic_upper_stage: str | None = None
    hard_break_polarity_resolved: bool = True
    missing_predicate_is_new_core: bool = True

    def __post_init__(self) -> None:
        if self.materiality not in MATERIALITY_LEVELS:
            raise ValueError(f"unsupported question materiality: {self.materiality}")
        if (self.deterministic_lower_stage is None) != (
            self.deterministic_upper_stage is None
        ):
            raise ValueError("question Stage bounds must be paired")

    @property
    def score_stage_range_bounded(self) -> bool:
        components = set(self.component_lower_delta) | set(self.component_upper_delta)
        deltas_are_finite = all(
            isinstance(value, (int, float)) and isfinite(float(value))
            for component in components
            for value in (
                self.component_lower_delta.get(component, 0.0),
                self.component_upper_delta.get(component, 0.0),
            )
        )
        return bool(
            deltas_are_finite
            and self.deterministic_lower_stage is not None
            and self.deterministic_upper_stage is not None
        )


@dataclass(frozen=True)
class RouteAdequacyDecision:
    question_family_id: str
    adequate: bool
    official_route_attempted: bool
    distinct_route_count: int
    independent_no_new_route_confirmation_count: int
    provider_parser_normal: bool
    accepted_fact_delta_zero: bool
    semantic_fixpoint: bool
    linked_route_receipt_ids: tuple[str, ...]
    failure_codes: tuple[str, ...]


@dataclass(frozen=True)
class AvailabilityDecision:
    question_family_id: str
    availability_class: str
    terminal: bool
    known_evidence_preserved: bool
    information_confidence_cap_allowed: bool
    component_upper_bound_allowed: bool
    stage_ceiling_allowed: bool
    component_zeroing_allowed: bool
    whole_score_invalidation_allowed: bool
    monitoring_only: bool
    failure_codes: tuple[str, ...]


@dataclass(frozen=True)
class QuestionClosureDecision:
    archetype_id: str
    question_family_id: str
    mandatory: bool
    status: str
    deterministic_status: str
    terminal: bool
    materiality: str
    gap_class: str
    component_ids: tuple[str, ...]
    required_source_roles: tuple[str, ...]
    verified_source_roles: tuple[str, ...]
    missing_core_source_roles: tuple[str, ...]
    missing_corroboration_source_roles: tuple[str, ...]
    linked_fact_ids: tuple[str, ...]
    verified_linked_fact_ids: tuple[str, ...]
    linked_source_lineage_ids: tuple[str, ...]
    question_to_source_linkage_complete: bool
    route_adequacy: RouteAdequacyDecision
    availability: AvailabilityDecision
    pro_materiality_proposal: Mapping[str, bool]
    deterministic_materiality_diverged: bool
    failure_codes: tuple[str, ...]

    @property
    def ready(self) -> bool:
        return bool(
            self.terminal
            and self.question_to_source_linkage_complete
            and not self.failure_codes
            and self.gap_class not in {
                "CORE_SCORE_BLOCKER",
                "STAGE_BOUNDARY_GAP",
                "HARD_BREAK_GAP",
            }
        )

    def to_dict(self) -> Mapping[str, Any]:
        payload = asdict(self)
        payload["ready"] = self.ready
        return payload


@dataclass(frozen=True)
class ResearchSaturationReceipt:
    job_id: str
    run_id: str
    target_id: str
    as_of_date: str
    conversation_id: str
    selected_archetype_ids: tuple[str, ...]
    selected_contract_ids: tuple[str, ...]
    question_decisions: tuple[QuestionClosureDecision, ...]
    expected_mandatory_question_ids: tuple[str, ...]
    missing_mandatory_question_ids: tuple[str, ...]
    nonterminal_mandatory_question_ids: tuple[str, ...]
    public_material_gap_question_ids: tuple[str, ...]
    verifier_repair_pending_ids: tuple[str, ...]
    provider_parser_core_pending_question_ids: tuple[str, ...]
    lifecycle_hard_break_pending_ids: tuple[str, ...]
    source_linkage_incomplete_question_ids: tuple[str, ...]
    likely_nonpublic_question_ids: tuple[str, ...]
    deterministic_research_status: str
    pro_claimed_research_status: str
    pro_status_diverged: bool
    fact_snapshot_hash: str
    accepted_lineage_roster_hash: str
    research_saturation_valid: bool
    component_entry_allowed: bool
    score_authority: bool = False
    stage_authority: bool = False

    def __post_init__(self) -> None:
        if self.research_saturation_valid != self.component_entry_allowed:
            raise ValueError("component entry must exactly follow research saturation")
        if self.score_authority or self.stage_authority:
            raise ValueError("saturation receipt cannot own score or Stage authority")

    @property
    def receipt_hash(self) -> str:
        return canonical_hash(self.to_dict(include_hash=False))

    def to_dict(self, *, include_hash: bool = True) -> Mapping[str, Any]:
        payload: dict[str, Any] = {
            "schema_version": "e2r_pro_research_saturation_receipt_v2",
            "status": (
                "FULL_THESIS_READY"
                if self.research_saturation_valid
                else "RESEARCH_SATURATION_PENDING"
            ),
            "job_id": self.job_id,
            "run_id": self.run_id,
            "target_id": self.target_id,
            "as_of_date": self.as_of_date,
            "conversation_id": self.conversation_id,
            "selected_archetype_ids": list(self.selected_archetype_ids),
            "selected_contract_ids": list(self.selected_contract_ids),
            "question_decisions": [row.to_dict() for row in self.question_decisions],
            "expected_mandatory_question_ids": list(
                self.expected_mandatory_question_ids
            ),
            "missing_mandatory_question_ids": list(self.missing_mandatory_question_ids),
            "nonterminal_mandatory_question_ids": list(
                self.nonterminal_mandatory_question_ids
            ),
            "public_material_gap_question_ids": list(
                self.public_material_gap_question_ids
            ),
            "verifier_repair_pending_ids": list(self.verifier_repair_pending_ids),
            "provider_parser_core_pending_question_ids": list(
                self.provider_parser_core_pending_question_ids
            ),
            "lifecycle_hard_break_pending_ids": list(
                self.lifecycle_hard_break_pending_ids
            ),
            "source_linkage_incomplete_question_ids": list(
                self.source_linkage_incomplete_question_ids
            ),
            "likely_nonpublic_question_ids": list(
                self.likely_nonpublic_question_ids
            ),
            "deterministic_research_status": self.deterministic_research_status,
            "pro_claimed_research_status": self.pro_claimed_research_status,
            "pro_status_diverged": self.pro_status_diverged,
            "fact_snapshot_hash": self.fact_snapshot_hash,
            "accepted_lineage_roster_hash": self.accepted_lineage_roster_hash,
            "research_saturation_valid": self.research_saturation_valid,
            "component_entry_allowed": self.component_entry_allowed,
            "score_authority": False,
            "stage_authority": False,
        }
        if include_hash:
            payload["receipt_hash"] = canonical_hash(payload)
        return payload


__all__ = [
    "AvailabilityDecision",
    "DeterministicQuestionBound",
    "MATERIALITY_LEVELS",
    "NONTERMINAL_QUESTION_STATUSES",
    "QuestionClosureDecision",
    "ResearchSaturationReceipt",
    "RouteAdequacyDecision",
    "TERMINAL_QUESTION_STATUSES",
]
