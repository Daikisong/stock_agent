"""Use the existing calibrated scorer after seven memos and 21 judges."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from e2r.research_brain.researcher_mode.schemas import (
    CANONICAL_COMPONENT_ORDER,
    ComponentJudgeDecision,
    ComponentResearchMemo,
)
from e2r.research_brain.runtime.scoring_contracts import (
    load_archetype_scoring_contract,
)
from e2r.research_brain.scoring import (
    ComponentAssessment,
    ComponentAssessmentBuilder,
    CreditValidatedImpact,
    FullScoreValidityEvidenceV2,
    ResearchCalibratedComponentScorer,
    ResearchCalibratedScoreResult,
)

from .judge_bridge import JudgeBridgeResult


@dataclass(frozen=True)
class CalibratedScoreBridgeResult:
    status: str
    score: ResearchCalibratedScoreResult | None
    assessments: tuple[ComponentAssessment, ...]
    impacts: tuple[CreditValidatedImpact, ...]
    pending_reasons: tuple[str, ...]
    impact_fact_lineage: Mapping[str, tuple[str, ...]]
    ignored_proposed_score_ranges_hash: str | None
    ignored_proposed_stage: str | None

    @property
    def score_valid(self) -> bool:
        return bool(self.score is not None and self.score.full_score_valid)

    @property
    def receipt_payload(self) -> Mapping[str, Any]:
        return {
            "schema_version": "e2r_pro_calibrated_score_bridge_receipt_v1",
            "status": self.status,
            "score": self.score.to_dict() if self.score else None,
            "component_assessments": [row.to_dict() for row in self.assessments],
            "validated_impacts": [row.to_dict() for row in self.impacts],
            "pending_reasons": list(self.pending_reasons),
            "impact_fact_lineage": {
                claim_id: list(fact_ids)
                for claim_id, fact_ids in sorted(self.impact_fact_lineage.items())
            },
            "score_valid": self.score_valid,
            "scorer_class": "ResearchCalibratedComponentScorer",
            "ignored_proposed_score_ranges_hash": (
                self.ignored_proposed_score_ranges_hash
            ),
            "ignored_proposed_stage": self.ignored_proposed_stage,
            "pro_score_ignored": True,
            "pro_stage_ignored": True,
            "new_score_engine_count": 0,
            "production_score_authority": True,
            "production_stage_authority": False,
        }


class ProCalibratedScorerBridge:
    def score(
        self,
        *,
        selected_archetype_id: str,
        memos: Sequence[ComponentResearchMemo],
        judge_result: JudgeBridgeResult,
        validated_impacts: Sequence[CreditValidatedImpact],
        terminal_evidence: Mapping[str, Mapping[str, Any]],
        validity_evidence: FullScoreValidityEvidenceV2,
        accepted_claim_ids: Sequence[str],
        accepted_claim_fact_ids: Mapping[str, Sequence[str]],
        proposed_score_ranges_hash: str | None = None,
        proposed_stage: str | None = None,
    ) -> CalibratedScoreBridgeResult:
        if judge_result.status != "JUDGING_COMPLETE" or len(judge_result.decisions) != 21:
            return CalibratedScoreBridgeResult(
                status="JUDGING_PROVIDER_PENDING",
                score=None,
                assessments=(),
                impacts=tuple(validated_impacts),
                pending_reasons=judge_result.pending_reasons
                or ("TWENTY_ONE_JUDGE_COVERAGE_MISSING",),
                impact_fact_lineage={},
                ignored_proposed_score_ranges_hash=proposed_score_ranges_hash,
                ignored_proposed_stage=proposed_stage,
            )
        _validate_rosters(memos=memos, judges=judge_result.decisions)
        contract = load_archetype_scoring_contract(selected_archetype_id)
        impacts = tuple(validated_impacts)
        memo_targets = {row.target_id for row in memos}
        if len(memo_targets) != 1:
            raise ValueError("component memos must describe one target")
        target_id = next(iter(memo_targets))
        if any(
            impact.target_id != target_id
            or impact.archetype_id != selected_archetype_id
            for impact in impacts
        ):
            raise ValueError(
                "validated impact target/archetype differs from the component dossier"
            )
        accepted = {str(value) for value in accepted_claim_ids}
        if any(impact.claim_id not in accepted for impact in impacts):
            raise ValueError("validated impact is not linked to an accepted claim")
        memo_facts_by_component = {
            memo.component_id: {
                *memo.positive_fact_ids,
                *memo.counter_fact_ids,
                *memo.resolution_fact_ids,
                *memo.context_fact_ids,
            }
            for memo in memos
        }
        claim_fact_lineage = {
            str(claim_id): tuple(
                dict.fromkeys(str(fact_id) for fact_id in fact_ids)
            )
            for claim_id, fact_ids in accepted_claim_fact_ids.items()
        }
        for impact in impacts:
            if not set(claim_fact_lineage.get(impact.claim_id, ())) & set(
                memo_facts_by_component.get(impact.component_id, ())
            ):
                raise ValueError(
                    "validated impact lacks fact lineage in its component memo"
                )
        assessment_result = ComponentAssessmentBuilder().build(
            contract=contract,
            impacts=impacts,
            terminal_evidence=terminal_evidence,
        )
        assessments = assessment_result.assessments
        score = ResearchCalibratedComponentScorer().score(
            contract=contract,
            impacts=impacts,
            assessments=assessments,
            validity_evidence=validity_evidence,
        )
        by_component = {row.component_id: row for row in assessments}
        for component_id, points in score.component_score_vector.items():
            assessment = by_component[component_id]
            if float(points) > 0 and not assessment.support_impact_ids:
                raise ValueError("nonzero calibrated component lacks impact lineage")
        return CalibratedScoreBridgeResult(
            status=(
                "DETERMINISTIC_SCORE_COMPLETE"
                if score.full_score_valid
                else "DETERMINISTIC_SCORE_PENDING"
            ),
            score=score,
            assessments=tuple(assessments),
            impacts=impacts,
            pending_reasons=tuple(score.material_nonterminal_components),
            impact_fact_lineage={
                impact.claim_id: claim_fact_lineage[impact.claim_id]
                for impact in impacts
            },
            ignored_proposed_score_ranges_hash=proposed_score_ranges_hash,
            ignored_proposed_stage=proposed_stage,
        )


def _validate_rosters(
    *,
    memos: Sequence[ComponentResearchMemo],
    judges: Sequence[ComponentJudgeDecision],
) -> None:
    memo_by_component = {row.component_id: row for row in memos}
    if set(memo_by_component) != set(CANONICAL_COMPONENT_ORDER) or len(memos) != 7:
        raise ValueError("calibrated scoring requires seven component memos")
    roles_by_component: dict[str, set[str]] = {
        component_id: set() for component_id in CANONICAL_COMPONENT_ORDER
    }
    for judge in judges:
        memo = memo_by_component.get(judge.component_id)
        if memo is None or judge.memo_id != memo.memo_id:
            raise ValueError("judge decision is detached from its component memo")
        roles_by_component[judge.component_id].add(judge.role)
    expected_roles = {"ANALYST", "SKEPTIC", "CALIBRATION_JUDGE"}
    if len(judges) != 21 or any(
        roles != expected_roles for roles in roles_by_component.values()
    ):
        raise ValueError("calibrated scoring requires three judge roles per component")


__all__ = ["CalibratedScoreBridgeResult", "ProCalibratedScorerBridge"]
