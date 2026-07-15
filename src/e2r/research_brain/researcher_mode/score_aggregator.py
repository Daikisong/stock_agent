"""Deterministic aggregation of independent component-scoring memos.

The LLM judges stop at component proposals.  This module independently checks
their evidence, anchor, prompt, and call lineage; removes invalid proposals;
resolves non-material consensus deterministically; and sums exactly seven
final component decisions.  It never asks an LLM for a total and never emits a
Stage.  Material disagreement or weak source finalization becomes a structured
research request instead of a deceptively low score.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
import hashlib
import json
import math
from pathlib import Path
import statistics
from typing import Any, Iterable, Mapping, Sequence

from e2r.production.metadata import write_json, write_jsonl
from e2r.research_brain.intelligence_schema import stable_intelligence_id

from .component_judge import JUDGE_PASS_BY_ROLE
from .component_scoring_memos import ComponentScoringMemoRun
from .schemas import (
    AnchorConfidence,
    CANONICAL_COMPONENT_ORDER,
    ComponentAnchor,
    ComponentJudgeDecision,
    ComponentJudgeRole,
    ComponentResearchMemo,
    EvidenceDirection,
    EvidenceFact,
    EvidenceLifecycle,
    FinalComponentDecision,
)


AGGREGATOR_CONFIG: Mapping[str, Any] = {
    "version": "e2r_v5_component_consensus_v2",
    "required_roles": [value.value for value in ComponentJudgeRole],
    "invalid_proposal_policy": "REMOVE_AND_RECORD",
    "consensus_method": "MEDIAN_WITH_ALLOWED_RANGE_INTERSECTION",
    "counter_application": "SKEPTIC_CANNOT_CREATE_SUPPORT",
    "material_disagreement_fraction": 0.20,
    "material_disagreement_absolute_floor": 2.0,
    "minimum_finalization_confidence": 0.40,
    "source_confidence_affects_points": False,
    "independent_corroboration_affects_points": False,
    "tiny_impact_cap_multiplication": False,
    "material_disagreement_policy": "RESEARCH_REQUIRED",
    "stage_authority": False,
}

SCORE_AGGREGATION_OUTPUT_FILES: Mapping[str, str] = {
    "component_results": "deterministic_component_aggregation_results.jsonl",
    "proposal_validations": "judge_proposal_validations.jsonl",
    "research_requests": "component_score_research_requests.jsonl",
    "total_score": "deterministic_total_score.json",
    "run": "deterministic_score_aggregation_run.json",
    "audit": "deterministic_score_aggregation_audit.json",
}


@dataclass(frozen=True)
class JudgeProposalValidation:
    proposal_index: int
    judge_id: str
    memo_id: str
    component_id: str
    role: str
    valid: bool
    reason_codes: tuple[str, ...]
    support_fact_ids: tuple[str, ...]
    counter_fact_ids: tuple[str, ...]
    anchor_ids: tuple[str, ...]
    prompt_hash: str
    response_hash: str
    judge_call_id: str
    schema_version: str = "e2r_judge_proposal_validation_v1"

    def __post_init__(self) -> None:
        if self.proposal_index < 0:
            raise ValueError("proposal_index must be nonnegative")
        for value, label in (
            (self.judge_id, "judge_id"),
            (self.memo_id, "memo_id"),
            (self.component_id, "component_id"),
            (self.role, "role"),
            (self.prompt_hash, "prompt_hash"),
            (self.response_hash, "response_hash"),
            (self.judge_call_id, "judge_call_id"),
        ):
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{label} is required")
        if self.valid == bool(self.reason_codes):
            raise ValueError("proposal validity and rejection reasons disagree")
        _unique_text(self.reason_codes, "reason_codes", allow_empty=self.valid)
        for values, label in (
            (self.support_fact_ids, "support_fact_ids"),
            (self.counter_fact_ids, "counter_fact_ids"),
            (self.anchor_ids, "anchor_ids"),
        ):
            _unique_text(values, label, allow_empty=True)

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "proposal_index": self.proposal_index,
            "judge_id": self.judge_id,
            "memo_id": self.memo_id,
            "component_id": self.component_id,
            "role": self.role,
            "valid": self.valid,
            "reason_codes": list(self.reason_codes),
            "support_fact_ids": list(self.support_fact_ids),
            "counter_fact_ids": list(self.counter_fact_ids),
            "anchor_ids": list(self.anchor_ids),
            "prompt_hash": self.prompt_hash,
            "response_hash": self.response_hash,
            "judge_call_id": self.judge_call_id,
        }


@dataclass(frozen=True)
class ComponentScoreResearchRequest:
    request_id: str
    component_id: str
    reason_codes: tuple[str, ...]
    judge_ids: tuple[str, ...]
    fact_ids: tuple[str, ...]
    counter_fact_ids: tuple[str, ...]
    anchor_ids: tuple[str, ...]
    proposal_points: Mapping[str, float]
    observed_proposal_span: tuple[float, float] | None
    consensus_band: tuple[float, float] | None
    query_generation_authority: str = "LLM_RESEARCH_SUPERVISOR"
    deterministic_query_synthesis: bool = False
    schema_version: str = "e2r_component_score_research_request_v1"

    def __post_init__(self) -> None:
        if self.component_id not in CANONICAL_COMPONENT_ORDER:
            raise ValueError("research request requires a canonical component")
        if not self.request_id.strip() or not self.reason_codes:
            raise ValueError("research request identity and reasons are required")
        _unique_text(self.reason_codes, "reason_codes", allow_empty=False)
        for values, label in (
            (self.judge_ids, "judge_ids"),
            (self.fact_ids, "fact_ids"),
            (self.counter_fact_ids, "counter_fact_ids"),
            (self.anchor_ids, "anchor_ids"),
        ):
            _unique_text(values, label, allow_empty=True)
        for role, points in self.proposal_points.items():
            if role not in JUDGE_PASS_BY_ROLE or not _is_finite_number(points):
                raise ValueError("research request proposal points are invalid")
        for value, label in (
            (self.observed_proposal_span, "observed_proposal_span"),
            (self.consensus_band, "consensus_band"),
        ):
            if value is not None and (
                len(value) != 2
                or not all(_is_finite_number(item) for item in value)
                or float(value[0]) > float(value[1])
            ):
                raise ValueError(f"{label} is invalid")
        if self.query_generation_authority != "LLM_RESEARCH_SUPERVISOR":
            raise ValueError("new research queries must remain LLM-owned")
        if self.deterministic_query_synthesis:
            raise ValueError("score aggregation cannot synthesize fallback queries")

    def to_score_gap_context(self) -> Mapping[str, Any]:
        return {
            "request_id": self.request_id,
            "component_id": self.component_id,
            "reason_codes": list(self.reason_codes),
            "judge_ids": list(self.judge_ids),
            "fact_ids": list(self.fact_ids),
            "counter_fact_ids": list(self.counter_fact_ids),
            "anchor_ids": list(self.anchor_ids),
            "proposal_points": dict(self.proposal_points),
            "observed_proposal_span": (
                list(self.observed_proposal_span)
                if self.observed_proposal_span is not None
                else None
            ),
            "consensus_band": (
                list(self.consensus_band) if self.consensus_band is not None else None
            ),
            "next_query_generation_authority": self.query_generation_authority,
            "deterministic_query_synthesis": False,
        }

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            **self.to_score_gap_context(),
            "query_generation_authority": self.query_generation_authority,
        }


@dataclass(frozen=True)
class ComponentAggregationResult:
    component_id: str
    status: str
    decision: FinalComponentDecision | None
    proposal_validations: tuple[JudgeProposalValidation, ...]
    consensus_band: tuple[float, float] | None
    proposal_median: float | None
    material_disagreement: bool
    research_request: ComponentScoreResearchRequest | None
    pending_reasons: tuple[str, ...]
    schema_version: str = "e2r_component_aggregation_result_v2"

    def __post_init__(self) -> None:
        if self.component_id not in CANONICAL_COMPONENT_ORDER:
            raise ValueError("component aggregation requires a canonical component")
        if self.status not in {"COMPLETE", "RESEARCH_REQUIRED"}:
            raise ValueError("unknown component aggregation status")
        valid_count = sum(row.valid for row in self.proposal_validations)
        if self.status == "COMPLETE":
            if (
                self.decision is None
                or self.pending_reasons
                or self.research_request is not None
                or self.material_disagreement
                or valid_count != 3
                or self.consensus_band is None
                or self.proposal_median is None
            ):
                raise ValueError("complete component aggregation is inconsistent")
        else:
            if self.decision is not None or not self.pending_reasons:
                raise ValueError("research-required aggregation needs reasons and no score")
            if self.research_request is None:
                raise ValueError("research-required aggregation needs a retry request")
        if self.decision and self.decision.component_id != self.component_id:
            raise ValueError("component result and decision scopes differ")
        if self.research_request and self.research_request.component_id != self.component_id:
            raise ValueError("component result and research request scopes differ")
        _unique_text(self.pending_reasons, "pending_reasons", allow_empty=self.status == "COMPLETE")

    @property
    def invalid_proposal_count(self) -> int:
        return sum(not row.valid for row in self.proposal_validations)

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "component_id": self.component_id,
            "status": self.status,
            "decision": self.decision.to_dict() if self.decision else None,
            "proposal_validations": [row.to_dict() for row in self.proposal_validations],
            "consensus_band": list(self.consensus_band) if self.consensus_band else None,
            "proposal_median": self.proposal_median,
            "material_disagreement": self.material_disagreement,
            "research_request": (
                self.research_request.to_dict() if self.research_request else None
            ),
            "pending_reasons": list(self.pending_reasons),
            "invalid_proposal_count": self.invalid_proposal_count,
            "source_confidence_affects_points": False,
            "production_stage_authority": False,
        }


@dataclass(frozen=True)
class DeterministicTotalScore:
    total_points: float
    max_points: float
    component_points: Mapping[str, float]
    component_max_points: Mapping[str, float]
    component_decision_ids: Mapping[str, str]
    fact_ids: tuple[str, ...]
    counter_fact_ids: tuple[str, ...]
    anchor_ids: tuple[str, ...]
    judge_ids: tuple[str, ...]
    prompt_hashes: tuple[str, ...]
    config_hash: str
    confidence: float
    confidence_interval: tuple[float, float]
    score_valid: bool
    source_confidence_affects_points: bool = False
    production_stage_authority: bool = False
    schema_version: str = "e2r_v5_deterministic_total_score_v2"

    def __post_init__(self) -> None:
        required = set(CANONICAL_COMPONENT_ORDER)
        for values, label in (
            (self.component_points, "component_points"),
            (self.component_max_points, "component_max_points"),
            (self.component_decision_ids, "component_decision_ids"),
        ):
            if set(values) != required:
                raise ValueError(f"total score {label} requires exactly seven components")
        if any(
            not _is_finite_number(self.component_points[key])
            or not _is_finite_number(self.component_max_points[key])
            or not 0 <= float(self.component_points[key]) <= float(self.component_max_points[key])
            for key in CANONICAL_COMPONENT_ORDER
        ):
            raise ValueError("total score component point range is invalid")
        if not _is_finite_number(self.total_points) or not _is_finite_number(self.max_points):
            raise ValueError("total score points must be finite")
        if abs(float(self.total_points) - sum(self.component_points.values())) > 1e-6:
            raise ValueError("total points do not reconcile with components")
        if abs(float(self.max_points) - sum(self.component_max_points.values())) > 1e-6:
            raise ValueError("total maximum does not reconcile with components")
        if not 0 <= self.total_points <= self.max_points:
            raise ValueError("total score is outside maximum")
        if not _is_finite_number(self.confidence) or not 0 <= self.confidence <= 1:
            raise ValueError("total confidence is invalid")
        if (
            len(self.confidence_interval) != 2
            or not all(_is_finite_number(value) for value in self.confidence_interval)
            or not 0 <= self.confidence_interval[0] <= self.total_points
            or not self.total_points <= self.confidence_interval[1] <= self.max_points
        ):
            raise ValueError("total confidence interval is invalid")
        for values, label, allow_empty in (
            (self.fact_ids, "fact_ids", self.total_points == 0),
            (self.counter_fact_ids, "counter_fact_ids", True),
            (self.anchor_ids, "anchor_ids", False),
            (self.judge_ids, "judge_ids", False),
            (self.prompt_hashes, "prompt_hashes", False),
        ):
            _unique_text(values, label, allow_empty=allow_empty)
        if len(self.judge_ids) != 21 or len(self.prompt_hashes) != 21:
            raise ValueError("total score requires twenty-one independent judge lineages")
        if any(len(value) != 64 for value in self.prompt_hashes):
            raise ValueError("total score prompt hashes must be sha256")
        try:
            for value in self.prompt_hashes:
                int(value, 16)
        except ValueError as exc:
            raise ValueError("total score prompt hashes must be hexadecimal") from exc
        decision_ids = tuple(self.component_decision_ids.values())
        if any(not value.strip() for value in decision_ids) or len(
            set(decision_ids)
        ) != len(CANONICAL_COMPONENT_ORDER):
            raise ValueError("total score component decision ids must be unique")
        if not self.score_valid:
            raise ValueError("DeterministicTotalScore cannot represent a pending score")
        if len(self.config_hash) != 64:
            raise ValueError("total config hash must be sha256")
        try:
            int(self.config_hash, 16)
        except ValueError as exc:
            raise ValueError("total config hash must be hexadecimal") from exc
        if self.source_confidence_affects_points:
            raise ValueError("source confidence cannot multiply total economic points")
        if self.production_stage_authority:
            raise ValueError("deterministic total score cannot decide Stage")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "total_points": self.total_points,
            "max_points": self.max_points,
            "component_points": dict(self.component_points),
            "component_max_points": dict(self.component_max_points),
            "component_decision_ids": dict(self.component_decision_ids),
            "fact_ids": list(self.fact_ids),
            "counter_fact_ids": list(self.counter_fact_ids),
            "anchor_ids": list(self.anchor_ids),
            "judge_ids": list(self.judge_ids),
            "prompt_hashes": list(self.prompt_hashes),
            "confidence": self.confidence,
            "confidence_interval": list(self.confidence_interval),
            "score_valid": self.score_valid,
            "config_hash": self.config_hash,
            "source_confidence_affects_points": False,
            "production_stage_authority": False,
        }


@dataclass(frozen=True)
class TotalAggregationResult:
    status: str
    score: DeterministicTotalScore | None
    pending_reasons: tuple[str, ...]
    schema_version: str = "e2r_total_aggregation_result_v2"

    def __post_init__(self) -> None:
        if self.status not in {"COMPLETE", "RESEARCH_REQUIRED"}:
            raise ValueError("unknown total aggregation status")
        if self.status == "COMPLETE" and (self.score is None or self.pending_reasons):
            raise ValueError("complete total aggregation requires one valid score")
        if self.status == "RESEARCH_REQUIRED" and (
            self.score is not None or not self.pending_reasons
        ):
            raise ValueError("pending total aggregation requires reasons and no score")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "status": self.status,
            "score": self.score.to_dict() if self.score else None,
            "pending_reasons": list(self.pending_reasons),
            "production_stage_authority": False,
        }


@dataclass(frozen=True)
class DeterministicScoreAggregationRun:
    target_id: str
    archetype_id: str
    as_of_date: str
    status: str
    component_results: tuple[ComponentAggregationResult, ...]
    total_result: TotalAggregationResult
    research_requests: tuple[ComponentScoreResearchRequest, ...]
    pending_reasons: tuple[str, ...]
    audit: Mapping[str, Any]
    config_hash: str
    score_valid: bool
    ready_for_stagecourt: bool
    production_stage_authority: bool = False
    schema_version: str = "e2r_deterministic_score_aggregation_run_v1"

    def __post_init__(self) -> None:
        if not self.target_id.strip() or not self.archetype_id.strip():
            raise ValueError("score aggregation run identity is incomplete")
        date.fromisoformat(self.as_of_date)
        if self.status not in {
            "DETERMINISTIC_SCORE_COMPLETE",
            "DETERMINISTIC_SCORE_RESEARCH_REQUIRED",
        }:
            raise ValueError("unknown deterministic score run status")
        if tuple(row.component_id for row in self.component_results) != tuple(
            CANONICAL_COMPONENT_ORDER
        ):
            raise ValueError("score aggregation run requires canonical component order")
        expected_requests = tuple(
            row.research_request
            for row in self.component_results
            if row.research_request is not None
        )
        if self.research_requests != expected_requests:
            raise ValueError("score aggregation research requests do not reconcile")
        critical = self.audit.get("critical_counts")
        if not isinstance(critical, Mapping) or any(
            isinstance(value, bool) or not isinstance(value, int) or value < 0
            for value in critical.values()
        ):
            raise ValueError("score aggregation audit critical counts are invalid")
        critical_sum = sum(critical.values())
        if critical_sum != self.audit.get("critical_count_sum"):
            raise ValueError("score aggregation audit counts do not reconcile")
        expected_audit_status = (
            "DETERMINISTIC_SCORE_AGGREGATION_AUDIT_PASS"
            if critical_sum == 0
            else "DETERMINISTIC_SCORE_AGGREGATION_AUDIT_FAIL"
        )
        if self.audit.get("status") != expected_audit_status:
            raise ValueError("score aggregation audit status is invalid")
        if (
            self.audit.get("component_count") != len(self.component_results)
            or self.audit.get("proposal_validation_count")
            != sum(len(row.proposal_validations) for row in self.component_results)
            or self.audit.get("research_request_count") != len(self.research_requests)
        ):
            raise ValueError("score aggregation audit leaves do not reconcile")
        complete = bool(
            critical_sum == 0
            and not self.pending_reasons
            and all(row.status == "COMPLETE" for row in self.component_results)
            and self.total_result.status == "COMPLETE"
            and self.total_result.score is not None
        )
        expected_status = (
            "DETERMINISTIC_SCORE_COMPLETE"
            if complete
            else "DETERMINISTIC_SCORE_RESEARCH_REQUIRED"
        )
        if self.status != expected_status:
            raise ValueError("score aggregation run status contradicts leaves")
        if self.score_valid != complete or self.ready_for_stagecourt != complete:
            raise ValueError("score validity/readiness contradicts aggregation state")
        if len(self.config_hash) != 64:
            raise ValueError("score aggregation run config hash must be sha256")
        try:
            int(self.config_hash, 16)
        except ValueError as exc:
            raise ValueError("score aggregation run config hash must be hexadecimal") from exc
        if complete and self.total_result.score.config_hash != self.config_hash:
            raise ValueError("run and total config lineage differ")
        if not complete and not (
            self.pending_reasons or self.research_requests or critical_sum
        ):
            raise ValueError("pending aggregation run requires a concrete blocker")
        if self.production_stage_authority:
            raise ValueError("score aggregation run cannot decide Stage")

    def to_score_gap_context(self) -> Mapping[str, Any]:
        return {
            "deterministic_score_aggregation_status": self.status,
            "score_valid": self.score_valid,
            "pending_reasons": list(self.pending_reasons),
            "component_research_requests": [
                row.to_score_gap_context() for row in self.research_requests
            ],
            "next_query_generation_authority": "LLM_RESEARCH_SUPERVISOR",
            "deterministic_query_synthesis": False,
        }

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "target_id": self.target_id,
            "archetype_id": self.archetype_id,
            "as_of_date": self.as_of_date,
            "status": self.status,
            "component_results": [row.to_dict() for row in self.component_results],
            "total_result": self.total_result.to_dict(),
            "research_requests": [row.to_dict() for row in self.research_requests],
            "pending_reasons": list(self.pending_reasons),
            "audit": dict(self.audit),
            "config_hash": self.config_hash,
            "score_valid": self.score_valid,
            "ready_for_stagecourt": self.ready_for_stagecourt,
            "source_confidence_affects_points": False,
            "production_stage_authority": False,
        }


class DeterministicScoreAggregator:
    """Validate, resolve, and sum component proposals without LLM authority."""

    def __init__(self, *, config: Mapping[str, Any] = AGGREGATOR_CONFIG) -> None:
        self.config = _validate_config(config)
        self.config_hash = _canonical_hash(self.config)

    def aggregate_component(
        self,
        *,
        memo: ComponentResearchMemo,
        judge_decisions: Sequence[ComponentJudgeDecision],
        evidence_facts: Sequence[EvidenceFact],
        historical_anchors: Sequence[ComponentAnchor | Mapping[str, Any]],
        expected_as_of_date: str | None = None,
        prompt_hashes: Sequence[str] = (),
    ) -> ComponentAggregationResult:
        if not memo.research_complete:
            return _component_pending(
                component_id=memo.component_id,
                reasons=("COMPONENT_RESEARCH_INCOMPLETE",),
                validations=(),
                decisions=(),
            )
        facts, fact_reasons = _validated_fact_inputs(
            memo=memo,
            evidence_facts=evidence_facts,
            expected_as_of_date=expected_as_of_date,
        )
        anchors, anchor_reasons = _validated_anchor_inputs(
            memo=memo,
            historical_anchors=historical_anchors,
        )
        base_reasons = tuple(dict.fromkeys((*fact_reasons, *anchor_reasons)))
        validations, valid = _validate_proposals(
            memo=memo,
            judge_decisions=judge_decisions,
            facts=facts,
            anchors=anchors,
            base_reasons=base_reasons,
        )
        required_roles = tuple(self.config["required_roles"])
        valid_roles = tuple(row.role for row in valid)
        roster_reasons: list[str] = []
        if set(valid_roles) != set(required_roles) or len(valid_roles) != len(required_roles):
            roster_reasons.append("THREE_VALID_JUDGE_CONSENSUS_MISSING")
        derived_prompt_hashes = tuple(row.prompt_hash for row in valid)
        if prompt_hashes and tuple(prompt_hashes) != derived_prompt_hashes:
            roster_reasons.append("CALLER_PROMPT_HASH_LINEAGE_MISMATCH")
        if roster_reasons:
            return _component_pending(
                component_id=memo.component_id,
                reasons=tuple(dict.fromkeys((*base_reasons, *roster_reasons))),
                validations=validations,
                decisions=valid,
            )

        by_role = {row.role: row for row in valid}
        ordered = tuple(by_role[role] for role in required_roles)
        proposals = tuple(float(row.proposed_points) for row in ordered)
        proposal_median = float(statistics.median(proposals))
        lower_consensus = max(float(row.allowed_range[0]) for row in ordered)
        upper_consensus = min(float(row.allowed_range[1]) for row in ordered)
        consensus_band = (lower_consensus, upper_consensus)
        spread = max(proposals) - min(proposals)
        material_limit = max(
            float(self.config["material_disagreement_absolute_floor"]),
            memo.component_max_points
            * float(self.config["material_disagreement_fraction"]),
        )
        if lower_consensus > upper_consensus or spread > material_limit:
            return _component_pending(
                component_id=memo.component_id,
                reasons=("UNRESOLVED_MATERIAL_JUDGE_DISAGREEMENT",),
                validations=validations,
                decisions=ordered,
                consensus_band=(
                    consensus_band if lower_consensus <= upper_consensus else None
                ),
                proposal_median=proposal_median,
                material_disagreement=True,
            )

        analyst = by_role[ComponentJudgeRole.ANALYST.value].proposed_points
        calibration = by_role[
            ComponentJudgeRole.CALIBRATION_JUDGE.value
        ].proposed_points
        skeptic = by_role[ComponentJudgeRole.SKEPTIC.value].proposed_points
        support_points = min(
            memo.component_max_points,
            float(statistics.median((analyst, calibration))),
        )
        if lower_consensus > support_points:
            return _component_pending(
                component_id=memo.component_id,
                reasons=("CONSENSUS_RANGE_EXCEEDS_SUPPORTED_ECONOMIC_POINTS",),
                validations=validations,
                decisions=ordered,
                consensus_band=consensus_band,
                proposal_median=proposal_median,
            )
        pre_counter = min(support_points, proposal_median)
        counter_adjusted = min(pre_counter, float(skeptic))
        final_points = min(upper_consensus, max(lower_consensus, counter_adjusted))
        if final_points > support_points + 1e-9:
            return _component_pending(
                component_id=memo.component_id,
                reasons=("COUNTER_APPLICATION_WOULD_CREATE_SUPPORT",),
                validations=validations,
                decisions=ordered,
                consensus_band=consensus_band,
                proposal_median=proposal_median,
            )

        support_fact_ids = _ordered_unique(
            fact_id for row in ordered for fact_id in row.support_fact_ids
        )
        counter_fact_ids = _ordered_unique(
            fact_id for row in ordered for fact_id in row.counter_fact_ids
        )
        anchor_ids = _ordered_unique(
            anchor_id for row in ordered for anchor_id in row.nearest_anchor_ids
        )
        source_confidence, corroboration_group_count = _source_confidence(
            fact_ids=(*support_fact_ids, *counter_fact_ids),
            anchor_ids=anchor_ids,
            facts=facts,
            anchors=anchors,
            proposal_spread=spread,
            component_max_points=memo.component_max_points,
        )
        if source_confidence < float(self.config["minimum_finalization_confidence"]):
            return _component_pending(
                component_id=memo.component_id,
                reasons=("SOURCE_CONFIDENCE_BELOW_FINALIZATION_THRESHOLD",),
                validations=validations,
                decisions=ordered,
                consensus_band=consensus_band,
                proposal_median=proposal_median,
            )

        support_points_rounded = round(support_points, 6)
        final_points_rounded = round(final_points, 6)
        counter_effect_rounded = round(
            support_points_rounded - final_points_rounded, 6
        )
        expansion = (1.0 - source_confidence) * memo.component_max_points * 0.15
        confidence_interval = (
            round(max(0.0, min(final_points_rounded, lower_consensus - expansion)), 6),
            round(
                min(
                    memo.component_max_points,
                    max(final_points_rounded, upper_consensus + expansion),
                ),
                6,
            ),
        )
        decision = FinalComponentDecision(
            component_id=memo.component_id,
            support_points=support_points_rounded,
            counter_effect=counter_effect_rounded,
            final_points=final_points_rounded,
            max_points=memo.component_max_points,
            fact_ids=support_fact_ids,
            counter_fact_ids=counter_fact_ids,
            anchor_ids=anchor_ids,
            judge_ids=tuple(row.judge_id for row in ordered),
            research_complete=True,
            confidence=round(source_confidence, 6),
            decision_trace=(
                "all proposal lineages validated; invalid proposals removed; "
                "median/allowed-range consensus resolved; skeptic counter effect "
                "applied once; component maximum clamped; source confidence kept "
                "outside economic points"
            ),
            proposal_median=round(proposal_median, 6),
            consensus_band=(round(lower_consensus, 6), round(upper_consensus, 6)),
            confidence_interval=confidence_interval,
            judge_proposals={
                role: round(float(by_role[role].proposed_points), 6)
                for role in required_roles
            },
            config_hash=self.config_hash,
            prompt_hashes=tuple(row.prompt_hash for row in ordered),
            response_hashes=tuple(row.response_hash for row in ordered),
            judge_call_ids=tuple(row.judge_call_id for row in ordered),
            corroboration_group_count=corroboration_group_count,
        )
        return ComponentAggregationResult(
            component_id=memo.component_id,
            status="COMPLETE",
            decision=decision,
            proposal_validations=validations,
            consensus_band=decision.consensus_band,
            proposal_median=decision.proposal_median,
            material_disagreement=False,
            research_request=None,
            pending_reasons=(),
        )

    def aggregate_total(
        self, decisions: Sequence[FinalComponentDecision]
    ) -> TotalAggregationResult:
        components = [row.component_id for row in decisions]
        if len(components) != len(set(components)):
            return _total_pending("DUPLICATE_COMPONENT_DECISION")
        required = set(CANONICAL_COMPONENT_ORDER)
        actual = set(components)
        if actual != required:
            missing = ",".join(sorted(required - actual)) or "NONE"
            extra = ",".join(sorted(actual - required)) or "NONE"
            return _total_pending(
                f"EXACT_SEVEN_COMPONENT_DECISIONS_REQUIRED:MISSING={missing}:EXTRA={extra}"
            )
        by_component = {row.component_id: row for row in decisions}
        ordered = tuple(by_component[key] for key in CANONICAL_COMPONENT_ORDER)
        if any(not row.research_complete for row in ordered):
            return _total_pending("COMPONENT_RESEARCH_INCOMPLETE")
        if any(row.config_hash != self.config_hash for row in ordered):
            return _total_pending("COMPONENT_CONFIG_HASH_MISMATCH")
        if any(
            len(row.judge_ids) != 3
            or len(row.prompt_hashes) != 3
            or len(row.judge_call_ids) != 3
            or not row.anchor_ids
            or (row.final_points > 0 and not row.fact_ids)
            for row in ordered
        ):
            return _total_pending("COMPONENT_REQUIRED_LINEAGE_MISSING")
        all_judge_ids = tuple(value for row in ordered for value in row.judge_ids)
        all_prompt_hashes = tuple(value for row in ordered for value in row.prompt_hashes)
        all_call_ids = tuple(value for row in ordered for value in row.judge_call_ids)
        if len(set(all_judge_ids)) != 21:
            return _total_pending("CROSS_COMPONENT_JUDGE_ID_REUSE")
        if len(set(all_prompt_hashes)) != 21:
            return _total_pending("CROSS_COMPONENT_PROMPT_HASH_REUSE")
        if len(set(all_call_ids)) != 21:
            return _total_pending("CROSS_COMPONENT_JUDGE_CALL_ID_REUSE")

        component_points = {
            row.component_id: row.final_points for row in ordered
        }
        component_max_points = {
            row.component_id: row.max_points for row in ordered
        }
        total_points = round(sum(component_points.values()), 6)
        maximum = round(sum(component_max_points.values()), 6)
        confidence_interval = (
            round(sum(row.confidence_interval[0] for row in ordered), 6),
            round(sum(row.confidence_interval[1] for row in ordered), 6),
        )
        score = DeterministicTotalScore(
            total_points=total_points,
            max_points=maximum,
            component_points=component_points,
            component_max_points=component_max_points,
            component_decision_ids={
                row.component_id: _decision_id(row) for row in ordered
            },
            fact_ids=_ordered_unique(
                fact_id for row in ordered for fact_id in row.fact_ids
            ),
            counter_fact_ids=_ordered_unique(
                fact_id for row in ordered for fact_id in row.counter_fact_ids
            ),
            anchor_ids=_ordered_unique(
                anchor_id for row in ordered for anchor_id in row.anchor_ids
            ),
            judge_ids=all_judge_ids,
            prompt_hashes=all_prompt_hashes,
            config_hash=self.config_hash,
            confidence=round(statistics.mean(row.confidence for row in ordered), 6),
            confidence_interval=confidence_interval,
            score_valid=True,
        )
        return TotalAggregationResult(
            status="COMPLETE", score=score, pending_reasons=()
        )

    def aggregate_run(
        self,
        *,
        scoring_memo_run: ComponentScoringMemoRun,
        component_research_memos: Sequence[ComponentResearchMemo],
        evidence_facts: Sequence[EvidenceFact],
        historical_anchors: Sequence[ComponentAnchor | Mapping[str, Any]],
    ) -> DeterministicScoreAggregationRun:
        date.fromisoformat(scoring_memo_run.as_of_date)
        global_reasons = list(
            _run_input_reasons(
                scoring_memo_run=scoring_memo_run,
                component_research_memos=component_research_memos,
                evidence_facts=evidence_facts,
                historical_anchors=historical_anchors,
            )
        )
        grouped: dict[str, list[ComponentResearchMemo]] = {}
        for memo in component_research_memos:
            if memo.component_id in CANONICAL_COMPONENT_ORDER:
                grouped.setdefault(memo.component_id, []).append(memo)
        scoring_by_component = {
            row.component_id: row for row in scoring_memo_run.component_memos
        }
        component_results: list[ComponentAggregationResult] = []
        for component_id in CANONICAL_COMPONENT_ORDER:
            candidates = grouped.get(component_id, [])
            scoring_memo = scoring_by_component[component_id]
            if len(candidates) != 1:
                reason = (
                    "COMPONENT_RESEARCH_MEMO_MISSING"
                    if not candidates
                    else "DUPLICATE_COMPONENT_RESEARCH_MEMO"
                )
                component_results.append(
                    _component_pending(
                        component_id=component_id,
                        reasons=(reason,),
                        validations=(),
                        decisions=(),
                    )
                )
                continue
            memo = candidates[0]
            scope_reasons = []
            if (
                memo.target_id != scoring_memo_run.target_id
                or memo.archetype_id != scoring_memo_run.archetype_id
            ):
                scope_reasons.append("COMPONENT_RESEARCH_MEMO_SCOPE_MISMATCH")
            if scoring_memo.status != "COMPLETE" or not scoring_memo.ready_for_deterministic_aggregation:
                scope_reasons.append("COMPONENT_SCORING_MEMO_NOT_READY")
                scope_reasons.extend(scoring_memo.pending_reasons)
            if scoring_memo.component_research_memo_id != memo.memo_id:
                scope_reasons.append("COMPONENT_SCORING_MEMO_ID_MISMATCH")
            if (
                scoring_memo.component_max_points is None
                or abs(scoring_memo.component_max_points - memo.component_max_points) > 1e-9
            ):
                scope_reasons.append("COMPONENT_SCORING_MAXIMUM_MISMATCH")
            if global_reasons:
                scope_reasons.extend(global_reasons)
            if scope_reasons:
                component_results.append(
                    _component_pending(
                        component_id=component_id,
                        reasons=tuple(dict.fromkeys(scope_reasons)),
                        validations=(),
                        decisions=scoring_memo.judge_decisions,
                    )
                )
                continue
            component_results.append(
                self.aggregate_component(
                    memo=memo,
                    judge_decisions=scoring_memo.judge_decisions,
                    evidence_facts=evidence_facts,
                    historical_anchors=historical_anchors,
                    expected_as_of_date=scoring_memo_run.as_of_date,
                    prompt_hashes=scoring_memo.prompt_hashes,
                )
            )

        results = tuple(component_results)
        decisions = tuple(
            row.decision for row in results if row.decision is not None
        )
        total_result = self.aggregate_total(decisions)
        if total_result.status != "COMPLETE":
            global_reasons.extend(total_result.pending_reasons)
        global_pending = tuple(dict.fromkeys(global_reasons))
        requests = tuple(
            row.research_request for row in results if row.research_request is not None
        )
        audit = _aggregation_audit(
            config=self.config,
            config_hash=self.config_hash,
            scoring_memo_run=scoring_memo_run,
            component_results=results,
            total_result=total_result,
            global_pending_reasons=global_pending,
        )
        complete = bool(
            audit["critical_count_sum"] == 0
            and not global_pending
            and all(row.status == "COMPLETE" for row in results)
            and total_result.status == "COMPLETE"
        )
        return DeterministicScoreAggregationRun(
            target_id=scoring_memo_run.target_id,
            archetype_id=scoring_memo_run.archetype_id,
            as_of_date=scoring_memo_run.as_of_date,
            status=(
                "DETERMINISTIC_SCORE_COMPLETE"
                if complete
                else "DETERMINISTIC_SCORE_RESEARCH_REQUIRED"
            ),
            component_results=results,
            total_result=total_result,
            research_requests=requests,
            pending_reasons=global_pending,
            audit=audit,
            config_hash=self.config_hash,
            score_valid=complete,
            ready_for_stagecourt=complete,
        )


def write_deterministic_score_aggregation_run(
    result: DeterministicScoreAggregationRun,
    output_directory: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_directory)
    paths = {
        key: root / filename for key, filename in SCORE_AGGREGATION_OUTPUT_FILES.items()
    }
    write_jsonl(
        paths["component_results"],
        (row.to_dict() for row in result.component_results),
    )
    write_jsonl(
        paths["proposal_validations"],
        (
            validation.to_dict()
            for row in result.component_results
            for validation in row.proposal_validations
        ),
    )
    write_jsonl(
        paths["research_requests"],
        (row.to_dict() for row in result.research_requests),
    )
    write_json(paths["total_score"], result.total_result.to_dict())
    write_json(paths["run"], result.to_dict())
    write_json(paths["audit"], result.audit)
    return paths


def _validate_config(config: Mapping[str, Any]) -> Mapping[str, Any]:
    value = dict(config)
    required_keys = set(AGGREGATOR_CONFIG)
    if set(value) != required_keys:
        missing = sorted(required_keys - set(value))
        extra = sorted(set(value) - required_keys)
        raise ValueError(f"aggregator config keys differ: missing={missing} extra={extra}")
    if tuple(value["required_roles"]) != tuple(
        role.value for role in ComponentJudgeRole
    ):
        raise ValueError("aggregator requires the canonical three judge roles")
    for key in (
        "material_disagreement_fraction",
        "material_disagreement_absolute_floor",
        "minimum_finalization_confidence",
    ):
        if not _is_finite_number(value[key]) or float(value[key]) < 0:
            raise ValueError(f"aggregator {key} is invalid")
    if not 0 <= float(value["material_disagreement_fraction"]) <= 1:
        raise ValueError("material disagreement fraction must be a probability")
    if not 0 <= float(value["minimum_finalization_confidence"]) <= 1:
        raise ValueError("minimum finalization confidence must be a probability")
    expected_text = {
        "invalid_proposal_policy": "REMOVE_AND_RECORD",
        "consensus_method": "MEDIAN_WITH_ALLOWED_RANGE_INTERSECTION",
        "counter_application": "SKEPTIC_CANNOT_CREATE_SUPPORT",
        "material_disagreement_policy": "RESEARCH_REQUIRED",
    }
    if any(value[key] != expected for key, expected in expected_text.items()):
        raise ValueError("aggregator policy cannot bypass deterministic safeguards")
    for key in (
        "source_confidence_affects_points",
        "independent_corroboration_affects_points",
        "tiny_impact_cap_multiplication",
        "stage_authority",
    ):
        if value[key] is not False:
            raise ValueError(f"aggregator safeguard {key} must remain false")
    if not isinstance(value["version"], str) or not value["version"].strip():
        raise ValueError("aggregator config version is required")
    return value


def _validated_fact_inputs(
    *,
    memo: ComponentResearchMemo,
    evidence_facts: Sequence[EvidenceFact],
    expected_as_of_date: str | None,
) -> tuple[Mapping[str, EvidenceFact], tuple[str, ...]]:
    reasons: list[str] = []
    ids = [row.fact_id for row in evidence_facts]
    if len(ids) != len(set(ids)):
        reasons.append("DUPLICATE_EVIDENCE_FACT_ID")
    facts = {row.fact_id: row for row in evidence_facts}
    referenced = {
        *memo.positive_fact_ids,
        *memo.counter_fact_ids,
        *memo.resolution_fact_ids,
    }
    for fact_id in sorted(referenced - set(facts)):
        reasons.append(f"UNAVAILABLE_EVIDENCE_FACT:{fact_id}")
    available = referenced & set(facts)
    if any(facts[fact_id].target_id != memo.target_id for fact_id in available):
        reasons.append("EVIDENCE_FACT_TARGET_MISMATCH")
    for fact_id in sorted(available):
        allowed = facts[fact_id].allowed_component_ids
        if allowed and memo.component_id not in allowed:
            reasons.append(f"EVIDENCE_FACT_COMPONENT_SCOPE_MISMATCH:{fact_id}")
    as_of_values = {facts[fact_id].as_of_date for fact_id in available}
    if len(as_of_values) > 1:
        reasons.append("EVIDENCE_FACT_AS_OF_SNAPSHOT_MIXED")
    if expected_as_of_date is not None:
        try:
            date.fromisoformat(expected_as_of_date)
        except ValueError:
            reasons.append("EXPECTED_AS_OF_DATE_INVALID")
        if any(value != expected_as_of_date for value in as_of_values):
            reasons.append("EVIDENCE_FACT_AS_OF_MISMATCH")
    for fact_id in memo.positive_fact_ids:
        fact = facts.get(fact_id)
        if fact and (
            fact.direction != EvidenceDirection.POSITIVE.value
            or fact.current_lifecycle
            in {EvidenceLifecycle.RESOLVED.value, EvidenceLifecycle.SUPERSEDED.value}
        ):
            reasons.append(f"INVALID_POSITIVE_FACT_DIRECTION_OR_LIFECYCLE:{fact_id}")
    for fact_id in memo.counter_fact_ids:
        fact = facts.get(fact_id)
        if fact and (
            fact.direction != EvidenceDirection.COUNTER.value
            or fact.current_lifecycle
            in {EvidenceLifecycle.RESOLVED.value, EvidenceLifecycle.SUPERSEDED.value}
        ):
            reasons.append(f"INVALID_COUNTER_FACT_DIRECTION_OR_LIFECYCLE:{fact_id}")
    for fact_id in memo.resolution_fact_ids:
        fact = facts.get(fact_id)
        if fact and not (
            fact.direction == EvidenceDirection.RESOLUTION.value
            or fact.current_lifecycle == EvidenceLifecycle.RESOLVED.value
        ):
            reasons.append(f"INVALID_RESOLUTION_FACT_DIRECTION_OR_LIFECYCLE:{fact_id}")
    return facts, tuple(dict.fromkeys(reasons))


def _validated_anchor_inputs(
    *,
    memo: ComponentResearchMemo,
    historical_anchors: Sequence[ComponentAnchor | Mapping[str, Any]],
) -> tuple[Mapping[str, Mapping[str, Any]], tuple[str, ...]]:
    reasons: list[str] = []
    rows = [_anchor_dict(row) for row in historical_anchors]
    ids = [str(row.get("anchor_id") or "").strip() for row in rows]
    if any(not value for value in ids) or len(ids) != len(set(ids)):
        reasons.append("DUPLICATE_OR_EMPTY_HISTORICAL_ANCHOR_ID")
    anchors = {anchor_id: row for anchor_id, row in zip(ids, rows) if anchor_id}
    for anchor_id in memo.historical_anchor_ids:
        row = anchors.get(anchor_id)
        if row is None:
            reasons.append(f"UNAVAILABLE_HISTORICAL_ANCHOR:{anchor_id}")
            continue
        if row.get("archetype_id") != memo.archetype_id:
            reasons.append(f"HISTORICAL_ANCHOR_ARCHETYPE_MISMATCH:{anchor_id}")
        if row.get("component_id") != memo.component_id:
            reasons.append(f"HISTORICAL_ANCHOR_COMPONENT_MISMATCH:{anchor_id}")
        if row.get("company_name_conditioned") or row.get("target_symbol_conditioned"):
            reasons.append(f"TARGET_CONDITIONED_HISTORICAL_ANCHOR:{anchor_id}")
        if type(row.get("usable_as_exact_anchor")) is not bool or type(
            row.get("usable_as_ordinal_anchor")
        ) is not bool:
            reasons.append(f"INVALID_HISTORICAL_ANCHOR_USABILITY_TYPE:{anchor_id}")
        if not (
            row.get("usable_as_exact_anchor") is True
            or row.get("usable_as_ordinal_anchor") is True
        ):
            reasons.append(f"UNUSABLE_HISTORICAL_ANCHOR:{anchor_id}")
        if row.get("confidence") not in {
            AnchorConfidence.HIGH.value,
            AnchorConfidence.MEDIUM.value,
            AnchorConfidence.LOW.value,
        }:
            reasons.append(f"INVALID_HISTORICAL_ANCHOR_CONFIDENCE:{anchor_id}")
        if row.get("usable_as_exact_anchor") is True and (
            row.get("confidence") != AnchorConfidence.HIGH.value
            or not row.get("source_backed_case_ids")
            or bool(row.get("source_proxy_guard_case_ids"))
        ):
            reasons.append(f"INVALID_EXACT_HISTORICAL_ANCHOR_LINEAGE:{anchor_id}")
        values = tuple(
            row.get(key)
            for key in ("points_lower", "points_mid", "points_upper", "max_points")
        )
        if not all(_is_finite_number(value) for value in values):
            reasons.append(f"INVALID_HISTORICAL_ANCHOR_RANGE:{anchor_id}")
            continue
        lower, mid, upper, maximum = (float(value) for value in values)
        if not 0 <= lower <= mid <= upper <= maximum:
            reasons.append(f"INVALID_HISTORICAL_ANCHOR_RANGE:{anchor_id}")
        if abs(maximum - memo.component_max_points) > 1e-9:
            reasons.append(f"HISTORICAL_ANCHOR_MAXIMUM_MISMATCH:{anchor_id}")
    if not memo.historical_anchor_ids:
        reasons.append("HISTORICAL_ANCHOR_LINEAGE_MISSING")
    return anchors, tuple(dict.fromkeys(reasons))


def _validate_proposals(
    *,
    memo: ComponentResearchMemo,
    judge_decisions: Sequence[ComponentJudgeDecision],
    facts: Mapping[str, EvidenceFact],
    anchors: Mapping[str, Mapping[str, Any]],
    base_reasons: Sequence[str],
) -> tuple[tuple[JudgeProposalValidation, ...], tuple[ComponentJudgeDecision, ...]]:
    reason_lists: list[list[str]] = []
    for row in judge_decisions:
        reasons = list(base_reasons)
        if row.memo_id != memo.memo_id:
            reasons.append("JUDGE_MEMO_ID_MISMATCH")
        if row.component_id != memo.component_id:
            reasons.append("JUDGE_COMPONENT_ID_MISMATCH")
        if abs(row.component_max_points - memo.component_max_points) > 1e-9:
            reasons.append("JUDGE_COMPONENT_MAXIMUM_MISMATCH")
        if row.role not in JUDGE_PASS_BY_ROLE:
            reasons.append("UNKNOWN_JUDGE_ROLE")
        elif row.pass_name != JUDGE_PASS_BY_ROLE[row.role]:
            reasons.append("JUDGE_ROLE_PASS_MISMATCH")
        if row.production_total_score_authority or row.production_stage_authority:
            reasons.append("LLM_SCORE_OR_STAGE_AUTHORITY_FORBIDDEN")
        lower, upper = row.allowed_range
        if not (
            _is_finite_number(lower)
            and _is_finite_number(row.proposed_points)
            and _is_finite_number(upper)
            and 0 <= lower <= row.proposed_points <= upper <= memo.component_max_points
        ):
            reasons.append("INVALID_JUDGE_POINT_RANGE")
        if set(row.support_fact_ids) - set(memo.positive_fact_ids):
            reasons.append("JUDGE_SUPPORT_OUTSIDE_COMPONENT_MEMO")
        if set(row.counter_fact_ids) - set(memo.counter_fact_ids):
            reasons.append("JUDGE_COUNTER_OUTSIDE_COMPONENT_MEMO")
        if set(row.nearest_anchor_ids) - set(memo.historical_anchor_ids):
            reasons.append("JUDGE_ANCHOR_OUTSIDE_COMPONENT_MEMO")
        if set((*row.support_fact_ids, *row.counter_fact_ids)) - set(facts):
            reasons.append("JUDGE_FACT_LINEAGE_UNAVAILABLE")
        if set(row.nearest_anchor_ids) - set(anchors):
            reasons.append("JUDGE_ANCHOR_LINEAGE_UNAVAILABLE")
        if row.role == ComponentJudgeRole.ANALYST.value and set(
            memo.positive_fact_ids
        ) - set(row.support_fact_ids):
            reasons.append("ANALYST_POSITIVE_FACT_COVERAGE_INCOMPLETE")
        if row.role == ComponentJudgeRole.SKEPTIC.value and set(
            memo.counter_fact_ids
        ) - set(row.counter_fact_ids):
            reasons.append("SKEPTIC_COUNTER_FACT_COVERAGE_INCOMPLETE")
        expected_call_id = stable_intelligence_id(
            "JUDGECALL",
            {
                "memo_id": memo.memo_id,
                "component_id": memo.component_id,
                "role": row.role,
                "pass_name": row.pass_name,
                "provider_name": row.provider_name,
                "prompt_hash": row.prompt_hash,
            },
        )
        if row.judge_call_id != expected_call_id:
            reasons.append("JUDGE_CALL_ID_LINEAGE_MISMATCH")
        reason_lists.append(list(dict.fromkeys(reasons)))

    for field_name, code in (
        ("role", "DUPLICATE_VALID_JUDGE_ROLE"),
        ("judge_id", "DUPLICATE_VALID_JUDGE_ID"),
        ("prompt_hash", "DUPLICATE_VALID_PROMPT_HASH"),
        ("response_hash", "DUPLICATE_VALID_RESPONSE_HASH"),
        ("judge_call_id", "DUPLICATE_VALID_JUDGE_CALL_ID"),
    ):
        groups: dict[str, list[int]] = {}
        for index, row in enumerate(judge_decisions):
            if not reason_lists[index]:
                groups.setdefault(str(getattr(row, field_name)), []).append(index)
        for indices in groups.values():
            if len(indices) > 1:
                for index in indices:
                    reason_lists[index].append(code)

    validations = tuple(
        JudgeProposalValidation(
            proposal_index=index,
            judge_id=row.judge_id,
            memo_id=row.memo_id,
            component_id=row.component_id,
            role=row.role,
            valid=not reason_lists[index],
            reason_codes=tuple(reason_lists[index]),
            support_fact_ids=row.support_fact_ids,
            counter_fact_ids=row.counter_fact_ids,
            anchor_ids=row.nearest_anchor_ids,
            prompt_hash=row.prompt_hash,
            response_hash=row.response_hash,
            judge_call_id=row.judge_call_id,
        )
        for index, row in enumerate(judge_decisions)
    )
    valid = tuple(
        row for row, validation in zip(judge_decisions, validations) if validation.valid
    )
    return validations, valid


def _source_confidence(
    *,
    fact_ids: Sequence[str],
    anchor_ids: Sequence[str],
    facts: Mapping[str, EvidenceFact],
    anchors: Mapping[str, Mapping[str, Any]],
    proposal_spread: float,
    component_max_points: float,
) -> tuple[float, int]:
    selected_facts = [facts[value] for value in _ordered_unique(fact_ids) if value in facts]
    fact_confidence = (
        statistics.mean(row.confidence for row in selected_facts)
        if selected_facts
        else 0.0
    )
    anchor_values = []
    for anchor_id in _ordered_unique(anchor_ids):
        confidence = str(anchors.get(anchor_id, {}).get("confidence") or "LOW")
        anchor_values.append(
            {
                AnchorConfidence.HIGH.value: 1.0,
                AnchorConfidence.MEDIUM.value: 0.75,
                AnchorConfidence.LOW.value: 0.5,
            }.get(confidence, 0.0)
        )
    anchor_confidence = statistics.mean(anchor_values) if anchor_values else 0.0
    agreement_confidence = max(
        0.0, min(1.0, 1.0 - proposal_spread / component_max_points)
    )
    independence_groups = {
        group
        for row in selected_facts
        for group in (
            row.source_independence_group,
            *row.corroborating_independence_groups,
        )
        if group
    }
    corroboration_bonus = min(0.10, max(0, len(independence_groups) - 1) * 0.025)
    confidence = min(
        1.0,
        max(
            0.0,
            0.50 * fact_confidence
            + 0.25 * anchor_confidence
            + 0.25 * agreement_confidence
            + corroboration_bonus,
        ),
    )
    return confidence, len(independence_groups)


def _component_pending(
    *,
    component_id: str,
    reasons: Sequence[str],
    validations: Sequence[JudgeProposalValidation],
    decisions: Sequence[ComponentJudgeDecision],
    consensus_band: tuple[float, float] | None = None,
    proposal_median: float | None = None,
    material_disagreement: bool = False,
) -> ComponentAggregationResult:
    normalized_reasons = tuple(dict.fromkeys(str(value) for value in reasons if value))
    if not normalized_reasons:
        normalized_reasons = ("DETERMINISTIC_COMPONENT_AGGREGATION_PENDING",)
    request = _research_request(
        component_id=component_id,
        reasons=normalized_reasons,
        decisions=decisions,
        consensus_band=consensus_band,
    )
    return ComponentAggregationResult(
        component_id=component_id,
        status="RESEARCH_REQUIRED",
        decision=None,
        proposal_validations=tuple(validations),
        consensus_band=consensus_band,
        proposal_median=proposal_median,
        material_disagreement=material_disagreement,
        research_request=request,
        pending_reasons=normalized_reasons,
    )


def _research_request(
    *,
    component_id: str,
    reasons: tuple[str, ...],
    decisions: Sequence[ComponentJudgeDecision],
    consensus_band: tuple[float, float] | None,
) -> ComponentScoreResearchRequest:
    proposal_points = {
        row.role: float(row.proposed_points)
        for row in decisions
        if row.role in JUDGE_PASS_BY_ROLE
    }
    span = (
        (min(proposal_points.values()), max(proposal_points.values()))
        if proposal_points
        else None
    )
    payload = {
        "component_id": component_id,
        "reason_codes": reasons,
        "judge_ids": [row.judge_id for row in decisions],
        "proposal_points": proposal_points,
        "consensus_band": consensus_band,
    }
    return ComponentScoreResearchRequest(
        request_id="SCORE-RESEARCH-" + _canonical_hash(payload)[:24],
        component_id=component_id,
        reason_codes=reasons,
        judge_ids=_ordered_unique(row.judge_id for row in decisions),
        fact_ids=_ordered_unique(
            value for row in decisions for value in row.support_fact_ids
        ),
        counter_fact_ids=_ordered_unique(
            value for row in decisions for value in row.counter_fact_ids
        ),
        anchor_ids=_ordered_unique(
            value for row in decisions for value in row.nearest_anchor_ids
        ),
        proposal_points=proposal_points,
        observed_proposal_span=span,
        consensus_band=consensus_band,
    )


def _total_pending(reason: str) -> TotalAggregationResult:
    return TotalAggregationResult(
        status="RESEARCH_REQUIRED", score=None, pending_reasons=(reason,)
    )


def _run_input_reasons(
    *,
    scoring_memo_run: ComponentScoringMemoRun,
    component_research_memos: Sequence[ComponentResearchMemo],
    evidence_facts: Sequence[EvidenceFact],
    historical_anchors: Sequence[ComponentAnchor | Mapping[str, Any]],
) -> tuple[str, ...]:
    reasons = []
    # Run-level readiness is the conjunction of all seven component memos.  It
    # must not be copied into every component: one pending memo would otherwise
    # erase six independently complete component decisions.  Each component's
    # readiness is checked in ``aggregate_run`` and the exact-seven total gate
    # still keeps the overall score pending.
    fact_ids = [row.fact_id for row in evidence_facts]
    if len(fact_ids) != len(set(fact_ids)):
        reasons.append("RUN_DUPLICATE_EVIDENCE_FACT_ID")
    if any(row.target_id != scoring_memo_run.target_id for row in evidence_facts):
        reasons.append("RUN_EVIDENCE_FACT_TARGET_MISMATCH")
    if any(row.as_of_date != scoring_memo_run.as_of_date for row in evidence_facts):
        reasons.append("RUN_EVIDENCE_FACT_AS_OF_MISMATCH")
    if any(
        row.target_id != scoring_memo_run.target_id
        or row.archetype_id != scoring_memo_run.archetype_id
        for row in component_research_memos
    ):
        reasons.append("RUN_COMPONENT_RESEARCH_SCOPE_MISMATCH")
    anchor_ids = [str(_anchor_dict(row).get("anchor_id") or "") for row in historical_anchors]
    if any(not value for value in anchor_ids) or len(anchor_ids) != len(set(anchor_ids)):
        reasons.append("RUN_DUPLICATE_OR_EMPTY_ANCHOR_ID")
    return tuple(dict.fromkeys(reasons))


def _aggregation_audit(
    *,
    config: Mapping[str, Any],
    config_hash: str,
    scoring_memo_run: ComponentScoringMemoRun,
    component_results: Sequence[ComponentAggregationResult],
    total_result: TotalAggregationResult,
    global_pending_reasons: Sequence[str],
) -> Mapping[str, Any]:
    decisions = [row.decision for row in component_results if row.decision is not None]
    validations = [
        validation for row in component_results for validation in row.proposal_validations
    ]
    score = total_result.score
    total_reconciliation_error = int(
        score is not None
        and abs(score.total_points - sum(score.component_points.values())) > 1e-6
    )
    required_lineage_missing = sum(
        not row.fact_ids
        or not row.anchor_ids
        or len(row.judge_ids) != 3
        or len(row.prompt_hashes) != 3
        or len(row.judge_call_ids) != 3
        or not row.config_hash
        for row in decisions
    )
    critical = {
        "component_roster_mismatch_count": int(
            tuple(row.component_id for row in component_results)
            != tuple(CANONICAL_COMPONENT_ORDER)
        ),
        "component_research_required_count": sum(
            row.status != "COMPLETE" for row in component_results
        ),
        "material_disagreement_count": sum(
            row.material_disagreement for row in component_results
        ),
        "total_aggregation_pending_count": int(total_result.status != "COMPLETE"),
        "global_pending_reason_count": len(global_pending_reasons),
        "required_component_lineage_missing_count": required_lineage_missing,
        "component_config_hash_mismatch_count": sum(
            row.config_hash != config_hash for row in decisions
        ),
        "component_max_violation_count": sum(
            row.final_points > row.max_points + 1e-9 for row in decisions
        ),
        "total_reconciliation_error_count": total_reconciliation_error,
        "source_confidence_points_multiplication_enabled_count": int(
            config["source_confidence_affects_points"] is not False
            or config["independent_corroboration_affects_points"] is not False
        ),
        "tiny_impact_cap_multiplication_enabled_count": int(
            config["tiny_impact_cap_multiplication"] is not False
        ),
        "production_stage_authority_count": int(
            config["stage_authority"] is not False
        )
        + sum(row.production_stage_authority for row in decisions),
    }
    critical_sum = sum(critical.values())
    return {
        "schema_version": "e2r_deterministic_score_aggregation_audit_v1",
        "status": (
            "DETERMINISTIC_SCORE_AGGREGATION_AUDIT_PASS"
            if critical_sum == 0
            else "DETERMINISTIC_SCORE_AGGREGATION_AUDIT_FAIL"
        ),
        "critical_counts": critical,
        "critical_count_sum": critical_sum,
        "diagnostic_counts": {
            "invalid_proposal_removed_count": sum(not row.valid for row in validations),
            "valid_proposal_count": sum(row.valid for row in validations),
            "counter_effect_applied_component_count": sum(
                row.counter_effect > 0 for row in decisions
            ),
            "independently_corroborated_component_count": sum(
                row.corroboration_group_count > 1 for row in decisions
            ),
        },
        "component_count": len(component_results),
        "complete_component_count": len(decisions),
        "proposal_validation_count": len(validations),
        "research_request_count": sum(
            row.research_request is not None for row in component_results
        ),
        "component_scoring_memo_run_status": scoring_memo_run.status,
        "aggregation_config_hash": config_hash,
        "aggregation_config": dict(config),
        "total_score_reconciled": total_reconciliation_error == 0,
        "source_confidence_affects_points": False,
        "independent_corroboration_affects_confidence_only": True,
        "tiny_impact_cap_multiplication_used": False,
        "production_stage_authority": False,
    }


def _anchor_dict(row: ComponentAnchor | Mapping[str, Any]) -> Mapping[str, Any]:
    return row.to_dict() if isinstance(row, ComponentAnchor) else dict(row)


def _decision_id(decision: FinalComponentDecision) -> str:
    return "FCDEC-" + _canonical_hash(decision.to_dict())[:24]


def _canonical_hash(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            default=str,
        ).encode("utf-8")
    ).hexdigest()


def _ordered_unique(values: Iterable[Any]) -> tuple[str, ...]:
    return tuple(dict.fromkeys(str(value) for value in values))


def _unique_text(values: Sequence[str], label: str, *, allow_empty: bool) -> None:
    if isinstance(values, str):
        raise ValueError(f"{label} must be a sequence")
    normalized = tuple(str(value).strip() for value in values)
    if not allow_empty and not normalized:
        raise ValueError(f"{label} cannot be empty")
    if any(not value for value in normalized) or len(normalized) != len(set(normalized)):
        raise ValueError(f"{label} must contain unique nonempty values")


def _is_finite_number(value: Any) -> bool:
    return (
        not isinstance(value, bool)
        and isinstance(value, (int, float))
        and math.isfinite(float(value))
    )


__all__ = [
    "AGGREGATOR_CONFIG",
    "SCORE_AGGREGATION_OUTPUT_FILES",
    "ComponentAggregationResult",
    "ComponentScoreResearchRequest",
    "DeterministicScoreAggregationRun",
    "DeterministicScoreAggregator",
    "DeterministicTotalScore",
    "JudgeProposalValidation",
    "TotalAggregationResult",
    "write_deterministic_score_aggregation_run",
]
