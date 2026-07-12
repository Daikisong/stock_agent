"""Deterministic, lineage-preserving aggregation of independent judge memos.

This module never asks an LLM for a total and never emits Stage.  Provider
failure or material judge disagreement returns RESEARCH_REQUIRED instead of a
low component score.
"""

from __future__ import annotations

import hashlib
import json
import statistics
from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from .schemas import (
    CANONICAL_COMPONENT_ORDER,
    ComponentJudgeDecision,
    ComponentJudgeRole,
    ComponentResearchMemo,
    FinalComponentDecision,
)


AGGREGATOR_CONFIG: Mapping[str, Any] = {
    "version": "e2r_v5_component_consensus_v1",
    "required_roles": [value.value for value in ComponentJudgeRole],
    "material_disagreement_fraction": 0.20,
    "material_disagreement_absolute_floor": 2.0,
    "source_confidence_affects_points": False,
    "stage_authority": False,
}


@dataclass(frozen=True)
class ComponentAggregationResult:
    status: str
    decision: FinalComponentDecision | None
    pending_reasons: tuple[str, ...]

    def __post_init__(self) -> None:
        if self.status not in {"COMPLETE", "RESEARCH_REQUIRED"}:
            raise ValueError("unknown component aggregation status")
        if self.status == "COMPLETE" and self.decision is None:
            raise ValueError("complete aggregation requires a decision")
        if self.status == "RESEARCH_REQUIRED" and not self.pending_reasons:
            raise ValueError("research-required aggregation needs reasons")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "status": self.status,
            "decision": self.decision.to_dict() if self.decision else None,
            "pending_reasons": list(self.pending_reasons),
        }


@dataclass(frozen=True)
class DeterministicTotalScore:
    total_points: float
    max_points: float
    component_points: Mapping[str, float]
    component_decision_ids: Mapping[str, str]
    confidence: float
    score_valid: bool
    config_hash: str
    schema_version: str = "e2r_v5_deterministic_total_score_v1"

    def __post_init__(self) -> None:
        if set(self.component_points) != set(CANONICAL_COMPONENT_ORDER):
            raise ValueError("total score requires exactly seven components")
        if set(self.component_decision_ids) != set(CANONICAL_COMPONENT_ORDER):
            raise ValueError("total score lineage requires seven decisions")
        if not 0 <= self.total_points <= self.max_points:
            raise ValueError("total score is outside maximum")
        if not 0 <= self.confidence <= 1:
            raise ValueError("total confidence is invalid")
        if not self.score_valid:
            raise ValueError("DeterministicTotalScore cannot represent pending score")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "total_points": self.total_points,
            "max_points": self.max_points,
            "component_points": dict(self.component_points),
            "component_decision_ids": dict(self.component_decision_ids),
            "confidence": self.confidence,
            "score_valid": self.score_valid,
            "config_hash": self.config_hash,
            "stage_authority": False,
        }


@dataclass(frozen=True)
class TotalAggregationResult:
    status: str
    score: DeterministicTotalScore | None
    pending_reasons: tuple[str, ...]

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "status": self.status,
            "score": self.score.to_dict() if self.score else None,
            "pending_reasons": list(self.pending_reasons),
        }


class DeterministicScoreAggregator:
    def __init__(self, *, config: Mapping[str, Any] = AGGREGATOR_CONFIG) -> None:
        self.config = dict(config)
        self.config_hash = hashlib.sha256(
            json.dumps(self.config, sort_keys=True).encode("utf-8")
        ).hexdigest()

    def aggregate_component(
        self,
        *,
        memo: ComponentResearchMemo,
        judge_decisions: Sequence[ComponentJudgeDecision],
        prompt_hashes: Sequence[str] = (),
    ) -> ComponentAggregationResult:
        if not memo.research_complete:
            return _component_pending("COMPONENT_RESEARCH_INCOMPLETE")
        valid = [row for row in judge_decisions if row.memo_id == memo.memo_id]
        roles = [row.role for row in valid]
        required_roles = set(self.config["required_roles"])
        if len(roles) != len(set(roles)):
            return _component_pending("DUPLICATE_JUDGE_ROLE")
        if set(roles) != required_roles:
            return _component_pending("THREE_JUDGE_CONSENSUS_MISSING")
        for row in valid:
            lower, upper = row.allowed_range
            if not 0 <= lower <= row.proposed_points <= upper <= memo.component_max_points:
                return _component_pending(f"INVALID_JUDGE_RANGE:{row.judge_id}")
            if set(row.support_fact_ids) - set(memo.positive_fact_ids):
                return _component_pending(f"INVALID_SUPPORT_LINEAGE:{row.judge_id}")
            if set(row.counter_fact_ids) - set(memo.counter_fact_ids):
                return _component_pending(f"INVALID_COUNTER_LINEAGE:{row.judge_id}")
            if set(row.nearest_anchor_ids) - set(memo.historical_anchor_ids):
                return _component_pending(f"INVALID_ANCHOR_LINEAGE:{row.judge_id}")
        lower_consensus = max(row.allowed_range[0] for row in valid)
        upper_consensus = min(row.allowed_range[1] for row in valid)
        proposals = [row.proposed_points for row in valid]
        spread = max(proposals) - min(proposals)
        material_limit = max(
            float(self.config["material_disagreement_absolute_floor"]),
            memo.component_max_points
            * float(self.config["material_disagreement_fraction"]),
        )
        if lower_consensus > upper_consensus or spread > material_limit:
            return _component_pending(
                "UNRESOLVED_MATERIAL_JUDGE_DISAGREEMENT"
            )
        by_role = {row.role: row for row in valid}
        analyst = by_role[ComponentJudgeRole.ANALYST.value].proposed_points
        calibration = by_role[
            ComponentJudgeRole.CALIBRATION_JUDGE.value
        ].proposed_points
        skeptic = by_role[ComponentJudgeRole.SKEPTIC.value].proposed_points
        support_points = min(
            memo.component_max_points,
            statistics.median((analyst, calibration)),
        )
        if lower_consensus > support_points:
            return _component_pending(
                "CONSENSUS_RANGE_EXCEEDS_SUPPORTED_ECONOMIC_POINTS"
            )
        consensus_mid = statistics.median(proposals)
        # Skeptic can reduce but cannot create economic support.  Confidence is
        # separate, so source quality is never multiplied into points here.
        final_points = min(support_points, skeptic, consensus_mid)
        final_points = min(upper_consensus, max(lower_consensus, final_points))
        final_points = min(support_points, final_points)
        counter_effect = max(0.0, support_points - final_points)
        confidence = max(
            0.0,
            min(1.0, memo.confidence * (1.0 - spread / memo.component_max_points)),
        )
        support_fact_ids = tuple(
            dict.fromkeys(
                fact_id for row in valid for fact_id in row.support_fact_ids
            )
        )
        counter_fact_ids = tuple(
            dict.fromkeys(
                fact_id for row in valid for fact_id in row.counter_fact_ids
            )
        )
        anchor_ids = tuple(
            dict.fromkeys(
                anchor_id for row in valid for anchor_id in row.nearest_anchor_ids
            )
        )
        decision = FinalComponentDecision(
            component_id=memo.component_id,
            support_points=round(support_points, 6),
            counter_effect=round(counter_effect, 6),
            final_points=round(final_points, 6),
            max_points=memo.component_max_points,
            fact_ids=support_fact_ids,
            counter_fact_ids=counter_fact_ids,
            anchor_ids=anchor_ids,
            judge_ids=tuple(row.judge_id for row in valid),
            research_complete=True,
            confidence=round(confidence, 6),
            decision_trace=(
                "validated three-judge lineage; median consensus; skeptic counter effect; component max clamp"
            ),
            config_hash=self.config_hash,
            prompt_hashes=tuple(dict.fromkeys(prompt_hashes)),
        )
        return ComponentAggregationResult(
            status="COMPLETE", decision=decision, pending_reasons=()
        )

    def aggregate_total(
        self, decisions: Sequence[FinalComponentDecision]
    ) -> TotalAggregationResult:
        by_component = {row.component_id: row for row in decisions}
        if len(by_component) != len(decisions):
            return TotalAggregationResult(
                status="RESEARCH_REQUIRED",
                score=None,
                pending_reasons=("DUPLICATE_COMPONENT_DECISION",),
            )
        missing = set(CANONICAL_COMPONENT_ORDER) - set(by_component)
        if missing:
            return TotalAggregationResult(
                status="RESEARCH_REQUIRED",
                score=None,
                pending_reasons=(
                    "SEVEN_COMPONENT_DECISIONS_MISSING:" + ",".join(sorted(missing)),
                ),
            )
        if any(not row.research_complete for row in by_component.values()):
            return TotalAggregationResult(
                status="RESEARCH_REQUIRED",
                score=None,
                pending_reasons=("COMPONENT_RESEARCH_INCOMPLETE",),
            )
        component_points = {
            component_id: by_component[component_id].final_points
            for component_id in CANONICAL_COMPONENT_ORDER
        }
        maximum = sum(
            by_component[component_id].max_points
            for component_id in CANONICAL_COMPONENT_ORDER
        )
        score = DeterministicTotalScore(
            total_points=round(sum(component_points.values()), 6),
            max_points=round(maximum, 6),
            component_points=component_points,
            component_decision_ids={
                component_id: _decision_id(by_component[component_id])
                for component_id in CANONICAL_COMPONENT_ORDER
            },
            confidence=round(
                statistics.mean(row.confidence for row in by_component.values()), 6
            ),
            score_valid=True,
            config_hash=self.config_hash,
        )
        return TotalAggregationResult(
            status="COMPLETE", score=score, pending_reasons=()
        )


def _component_pending(reason: str) -> ComponentAggregationResult:
    return ComponentAggregationResult(
        status="RESEARCH_REQUIRED", decision=None, pending_reasons=(reason,)
    )


def _decision_id(decision: FinalComponentDecision) -> str:
    return "FCDEC-" + hashlib.sha256(
        json.dumps(decision.to_dict(), sort_keys=True).encode("utf-8")
    ).hexdigest()[:24]


__all__ = [
    "AGGREGATOR_CONFIG",
    "ComponentAggregationResult",
    "DeterministicScoreAggregator",
    "DeterministicTotalScore",
    "TotalAggregationResult",
]
