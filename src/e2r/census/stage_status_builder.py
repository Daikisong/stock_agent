"""Build CensusStageStatus from baseline, depth, claims, and score ledger."""

from __future__ import annotations

from typing import Any, Mapping, Sequence

from .schemas import (
    accepted_claim_id,
    AssessmentDepth,
    BaseStage,
    BaselineScanResult,
    CensusStageStatus,
    CensusStatus,
    DepthDecision,
    DepthLevel,
    InvestigationStatus,
    ScoreValidStatus,
    StageConfidence,
    TransitionOverlay,
    UniverseInstrument,
    score_contribution_claim_ids,
)


def build_stage_status(
    *,
    instrument: UniverseInstrument,
    as_of_date: str,
    scan: BaselineScanResult,
    depth_decision: DepthDecision,
    accepted_claims: Sequence[Mapping[str, Any]] = (),
    score_contributions: Sequence[Mapping[str, Any]] = (),
    missing_primitives: Sequence[str] = (),
    failed_stage_gates: Sequence[str] = (),
    provider_gaps: Sequence[str] = (),
    source_gaps: Sequence[str] = (),
) -> CensusStageStatus:
    accepted_ids = tuple(filter(None, (accepted_claim_id(claim) for claim in accepted_claims)))
    nonzero = tuple(row for row in score_contributions if float(row.get("raw_points") or row.get("points") or 0.0) > 0.0)
    orphan_score_count = _orphan_score_count(nonzero)
    score_total = round(sum(float(row.get("raw_points") or row.get("points") or 0.0) for row in nonzero), 4)
    claim_backed_ratio = 0.0 if not nonzero else round((len(nonzero) - orphan_score_count) / len(nonzero), 4)
    assessment_depth = _assessment_depth(depth_decision.recommended_depth)

    if not instrument.eligible_for_census:
        return _status(
            instrument=instrument,
            as_of_date=as_of_date,
            scan=scan,
            depth=assessment_depth,
            census_status=CensusStatus.SKIPPED_INELIGIBLE,
            base_stage=BaseStage.UNKNOWN,
            investigation_status=InvestigationStatus.COMPLETE,
            score_valid_status=ScoreValidStatus.NOT_SCORED,
            next_actions=("IGNORE",),
        )
    if scan.has_provider_failure or provider_gaps:
        return _status(
            instrument=instrument,
            as_of_date=as_of_date,
            scan=scan,
            depth=assessment_depth,
            census_status=CensusStatus.PENDING_PROVIDER,
            base_stage=BaseStage.UNKNOWN,
            investigation_status=InvestigationStatus.PROVIDER_FAILED,
            score_valid_status=ScoreValidStatus.PROVIDER_FAILED,
            stage_confidence=StageConfidence.INSUFFICIENT_EVIDENCE,
            provider_gaps=tuple(provider_gaps or scan.provider_errors),
            next_actions=("PROVIDER_WAIT", "RECHECK_SOURCE"),
        )
    if orphan_score_count:
        return _status(
            instrument=instrument,
            as_of_date=as_of_date,
            scan=scan,
            depth=assessment_depth,
            census_status=CensusStatus.FAILED,
            base_stage=BaseStage.UNKNOWN,
            investigation_status=InvestigationStatus.PENDING,
            score_valid_status=ScoreValidStatus.INVALID_EVIDENCE,
            orphan_score_count=orphan_score_count,
            accepted_claim_count=len(accepted_ids),
            score_contribution_count=len(nonzero),
            claim_backed_score_ratio=claim_backed_ratio,
            source_gaps=("orphan_score_contribution",),
            next_actions=("RECHECK_SOURCE",),
        )
    if nonzero and not accepted_ids:
        return _status(
            instrument=instrument,
            as_of_date=as_of_date,
            scan=scan,
            depth=assessment_depth,
            census_status=CensusStatus.FAILED,
            base_stage=BaseStage.UNKNOWN,
            investigation_status=InvestigationStatus.PENDING,
            score_valid_status=ScoreValidStatus.INVALID_EVIDENCE,
            accepted_claim_count=0,
            score_contribution_count=len(nonzero),
            claim_backed_score_ratio=0.0,
            orphan_score_count=len(nonzero),
            source_gaps=("claimless_nonzero_score",),
            next_actions=("RECHECK_SOURCE",),
        )
    if scan.market_only_signal and not nonzero:
        return _status(
            instrument=instrument,
            as_of_date=as_of_date,
            scan=scan,
            depth=assessment_depth,
            census_status=CensusStatus.LIGHT_ONLY,
            base_stage=BaseStage.STAGE1,
            investigation_status=InvestigationStatus.PENDING,
            score_valid_status=ScoreValidStatus.NOT_SCORED,
            stage_confidence=StageConfidence.LOW,
            source_gaps=tuple(source_gaps),
            next_actions=("INVESTIGATE",),
        )
    if not scan.has_current_event and not accepted_ids and not nonzero:
        return _status(
            instrument=instrument,
            as_of_date=as_of_date,
            scan=scan,
            depth=assessment_depth,
            census_status=CensusStatus.SCANNED,
            base_stage=BaseStage.STAGE0,
            investigation_status=InvestigationStatus.NO_CURRENT_CATALYST,
            score_valid_status=ScoreValidStatus.NO_CURRENT_EVENT,
            stage_confidence=StageConfidence.LOW,
            next_actions=("IGNORE",),
        )
    if accepted_ids and score_total > 0.0:
        base_stage = _score_to_stage(score_total, missing_primitives=missing_primitives, failed_stage_gates=failed_stage_gates)
        return _status(
            instrument=instrument,
            as_of_date=as_of_date,
            scan=scan,
            depth=AssessmentDepth.VERIFIED_STAGE,
            census_status=CensusStatus.DEEP_VERIFIED,
            base_stage=base_stage,
            investigation_status=InvestigationStatus.COMPLETE,
            score_valid_status=ScoreValidStatus.FINAL if not missing_primitives else ScoreValidStatus.FINAL_WITH_NONMATERIAL_GAPS,
            stage_confidence=StageConfidence.MEDIUM if missing_primitives else StageConfidence.HIGH,
            accepted_claim_count=len(accepted_ids),
            score_contribution_count=len(nonzero),
            claim_backed_score_ratio=claim_backed_ratio,
            verified_score=score_total,
            score_interval_lower=score_total,
            score_interval_upper=score_total + _gap_upside(missing_primitives),
            missing_primitives=tuple(missing_primitives),
            failed_stage_gates=tuple(failed_stage_gates),
            next_actions=("DAILY_TRIGGER_TRACK",) if base_stage != BaseStage.STAGE0 else ("WATCH",),
        )
    return _status(
        instrument=instrument,
        as_of_date=as_of_date,
        scan=scan,
        depth=assessment_depth,
        census_status=CensusStatus.LIGHT_ONLY,
        base_stage=BaseStage.STAGE1 if scan.has_current_event else BaseStage.STAGE0,
        investigation_status=InvestigationStatus.PENDING if scan.has_current_event else InvestigationStatus.NO_CURRENT_CATALYST,
        score_valid_status=ScoreValidStatus.NOT_SCORED if scan.has_current_event else ScoreValidStatus.NO_CURRENT_EVENT,
        stage_confidence=StageConfidence.INSUFFICIENT_EVIDENCE,
        accepted_claim_count=len(accepted_ids),
        missing_primitives=tuple(missing_primitives),
        source_gaps=tuple(source_gaps or ("accepted_claim_absent",)),
        next_actions=("RECHECK_SOURCE",) if scan.has_current_event else ("IGNORE",),
    )


def _assessment_depth(depth: DepthLevel) -> AssessmentDepth:
    mapping = {
        DepthLevel.L0_UNIVERSE_ONLY: AssessmentDepth.UNIVERSE_ONLY,
        DepthLevel.L1_CHEAP_BASELINE: AssessmentDepth.CHEAP_BASELINE,
        DepthLevel.L2_OFFICIAL_LIGHT: AssessmentDepth.OFFICIAL_LIGHT,
        DepthLevel.L3_RESEARCH_BRAIN_TRIAGE: AssessmentDepth.RESEARCH_BRAIN_TRIAGE,
        DepthLevel.L4_DEEP_DOSSIER: AssessmentDepth.DEEP_DOSSIER,
        DepthLevel.L5_VERIFIED_STAGE: AssessmentDepth.VERIFIED_STAGE,
    }
    return mapping[depth]


def _score_to_stage(score: float, *, missing_primitives: Sequence[str], failed_stage_gates: Sequence[str]) -> BaseStage:
    if score >= 85 and not missing_primitives and not failed_stage_gates:
        return BaseStage.STAGE3_GREEN
    if score >= 75:
        return BaseStage.STAGE3_YELLOW
    if score >= 45:
        return BaseStage.STAGE2_ACTIONABLE
    return BaseStage.STAGE2_WATCH


def _gap_upside(missing_primitives: Sequence[str]) -> float:
    return float(min(len(tuple(missing_primitives)) * 5, 20))


def _orphan_score_count(contributions: Sequence[Mapping[str, Any]]) -> int:
    return sum(1 for row in contributions if not score_contribution_claim_ids(row))


def _status(
    *,
    instrument: UniverseInstrument,
    as_of_date: str,
    scan: BaselineScanResult,
    depth: AssessmentDepth,
    census_status: CensusStatus,
    base_stage: BaseStage,
    investigation_status: InvestigationStatus,
    score_valid_status: ScoreValidStatus,
    transition_overlay: TransitionOverlay = TransitionOverlay.NONE,
    stage_confidence: StageConfidence = StageConfidence.INSUFFICIENT_EVIDENCE,
    trigger_priority_score: float | None = None,
    verified_score: float | None = None,
    provisional_score: float | None = None,
    score_interval_lower: float | None = None,
    score_interval_upper: float | None = None,
    accepted_claim_count: int = 0,
    score_contribution_count: int = 0,
    claim_backed_score_ratio: float = 0.0,
    orphan_score_count: int = 0,
    missing_primitives: Sequence[str] = (),
    failed_stage_gates: Sequence[str] = (),
    provider_gaps: Sequence[str] = (),
    source_gaps: Sequence[str] = (),
    next_actions: Sequence[str] = (),
) -> CensusStageStatus:
    return CensusStageStatus(
        symbol=instrument.symbol,
        company_name=instrument.company_name,
        as_of_date=as_of_date,
        census_status=census_status,
        assessment_depth=depth,
        base_stage=base_stage,
        investigation_status=investigation_status,
        transition_overlay=transition_overlay,
        stage_confidence=stage_confidence,
        score_valid_status=score_valid_status,
        trigger_priority_score=scan.trigger_priority_score if trigger_priority_score is None else trigger_priority_score,
        verified_score=verified_score,
        provisional_score=provisional_score,
        score_interval_lower=score_interval_lower,
        score_interval_upper=score_interval_upper,
        large_sector_id=instrument.large_sector_id,
        accepted_claim_count=accepted_claim_count,
        score_contribution_count=score_contribution_count,
        claim_backed_score_ratio=claim_backed_score_ratio,
        orphan_score_count=orphan_score_count,
        recent_event_count=int(scan.has_current_event),
        recent_official_event_count=scan.recent_disclosure_count
        + scan.recent_supply_contract_count
        + scan.recent_facility_investment_count
        + scan.recent_earnings_event_count
        + scan.recent_risk_event_count,
        market_anomaly_count=scan.price_anomaly_count,
        risk_event_count=scan.recent_risk_event_count,
        missing_primitives=tuple(missing_primitives),
        failed_stage_gates=tuple(failed_stage_gates),
        provider_gaps=tuple(provider_gaps),
        source_gaps=tuple(source_gaps),
        next_actions=tuple(next_actions),
    )


__all__ = ["build_stage_status"]
