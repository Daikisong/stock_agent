"""Claim-backed scoring and StageCourt connection for Research Brain v3."""

from __future__ import annotations

from collections import Counter
from datetime import date
from typing import Any, Mapping, Sequence

from e2r.agentic.evidence_os import EvidenceContractV2, ScoreInterval
from e2r.agentic.primitive_aggregator import aggregate_primitive_states
from e2r.agentic.score_contribution_ledger import (
    DEFAULT_SCORE_COMPONENT_MAX_POINTS,
    build_component_score_contributions_from_rubric,
)
from e2r.agentic.stage_court import StageCourtInput, decide_stage_court
from e2r.calibration.taxonomy import large_sector_for_archetype
from e2r.scoring import CANONICAL_SCORE_COMPONENTS, DeterministicScorer, ScoringPayload
from e2r.research_brain.schemas import SourceTask
from e2r.research_brain.v2_schemas import ArchetypeMemoryCard, CandidateEventV2
from e2r.research_brain.v3_evidence_os_execution_bridge import EvidenceOSExecutionBundleV3
from e2r.research_brain.v3_schemas import DailyWatchlistItemV3, ScoreValidStatusV3


def build_claim_backed_watchlist_item_v3(
    *,
    event: CandidateEventV2,
    primary_archetype: str | None,
    secondary_archetypes: Sequence[str],
    card: ArchetypeMemoryCard | None,
    contract: EvidenceContractV2 | None,
    tasks: Sequence[SourceTask],
    bundle: EvidenceOSExecutionBundleV3 | None,
    as_of_date: date,
    planner_failed: bool = False,
    provider_error: str | None = None,
) -> DailyWatchlistItemV3:
    accepted_claim_ids = tuple(
        dict.fromkeys(
            claim_id
            for execution in (bundle.executions if bundle else ())
            for claim_id in execution.accepted_claim_ids
        )
    )
    status_summary = Counter(execution.status for execution in (bundle.executions if bundle else ()))
    trigger_priority = _float_or_none(event.price_context.get("cheap_scan_total_score"))
    if planner_failed:
        return _pending_item(
            event=event,
            primary_archetype=primary_archetype,
            secondary_archetypes=secondary_archetypes,
            card=card,
            tasks=tasks,
            status_summary=status_summary,
            trigger_priority=trigger_priority,
            score_valid_status=ScoreValidStatusV3.PROVIDER_FAILED.value,
            note=provider_error or "planner provider failed",
        )
    if not contract or not bundle or not accepted_claim_ids:
        return _pending_item(
            event=event,
            primary_archetype=primary_archetype,
            secondary_archetypes=secondary_archetypes,
            card=card,
            tasks=tasks,
            status_summary=status_summary,
            trigger_priority=trigger_priority,
            score_valid_status=ScoreValidStatusV3.PENDING_EVIDENCE_OS_CLAIMS.value,
            note="no Evidence OS accepted claim",
        )

    primitive_states = aggregate_primitive_states(ledger=bundle.ledger, contract=contract, as_of_date=as_of_date)
    contributions = build_component_score_contributions_from_rubric(
        components={component.key: component.max_points for component in CANONICAL_SCORE_COMPONENTS},
        primitive_states=primitive_states,
        score_rubric=contract.score_rubric,
        component_max_points=DEFAULT_SCORE_COMPONENT_MAX_POINTS,
    )
    positive_contributions = tuple(item for item in contributions if item.raw_points > 0)
    if not positive_contributions:
        return _pending_item(
            event=event,
            primary_archetype=primary_archetype,
            secondary_archetypes=secondary_archetypes,
            card=card,
            tasks=tasks,
            status_summary=status_summary,
            trigger_priority=trigger_priority,
            score_valid_status=ScoreValidStatusV3.PENDING_EVIDENCE_OS_CLAIMS.value,
            note="accepted claims did not map to score rubric",
        )
    payload = ScoringPayload(
        symbol=event.symbol,
        as_of_date=as_of_date,
        components={component.key: 0.0 for component in CANONICAL_SCORE_COMPONENTS},
        diagnostic_scores={
            "require_v2_score_contributions": 100.0,
            "agentic_evidence_required_for_scoring": 100.0,
            "claim_backed_claim_count_capped": min(float(len(accepted_claim_ids)), 100.0),
        },
        evidence_ids=accepted_claim_ids,
        score_contributions_v2=contributions,
        large_sector_id=large_sector_for_archetype(primary_archetype or "") if primary_archetype else None,
        canonical_archetype_id=primary_archetype,
        scoring_version="research-brain-v3-shadow",
    )
    snapshot = DeterministicScorer().score(payload)
    interval = ScoreInterval(verified_score=snapshot.total_score, potential_score_upper_bound=snapshot.total_score)
    stage = decide_stage_court(
        StageCourtInput(
            score_interval=interval,
            primitive_states=primitive_states,
            contract=contract,
            current_hard_break_claim_ids=(),
            has_prior_live_thesis=False,
        )
    )
    score_status = _score_valid_status(stage.score_status.value)
    return DailyWatchlistItemV3(
        symbol=event.symbol,
        company_name=event.company_name,
        candidate_event_id=event.candidate_event_id,
        event_type=event.event_type,
        event_summary=event.event_summary,
        primary_archetype=primary_archetype,
        secondary_archetypes=tuple(secondary_archetypes),
        research_memory_cards_used=(card.archetype_id,) if card else (),
        trigger_priority_score=trigger_priority,
        verified_score=snapshot.total_score,
        provisional_score=None,
        score_interval_lower=interval.verified_score,
        score_interval_upper=interval.potential_score_upper_bound,
        score_valid_status=score_status,
        base_stage=stage.decision.base_stage.value,
        investigation_status=stage.decision.investigation_status.value,
        transition_overlay=stage.decision.transition_overlay.value,
        accepted_claim_ids=accepted_claim_ids,
        score_contribution_ids=tuple(item.contribution_id for item in positive_contributions),
        failed_stage_gates=tuple(stage.reasons),
        green_blockers=tuple(stage.missing_green_primitives or (card.green_blockers if card else ())),
        red_team_checks=tuple(card.false_positive_patterns[:5] if card else ()),
        source_task_status_summary=dict(status_summary),
        follow_up_tasks=tuple(task.to_dict() for task in tasks if not accepted_claim_ids),
        do_not_promote_reasons=tuple(card.do_not_promote_rules[:5] if card else ()),
        stage_court_trace={
            "score_status": stage.score_status.value,
            "present_green_primitives": list(stage.present_green_primitives),
            "missing_green_primitives": list(stage.missing_green_primitives),
            "material_stage_boundaries_crossed": list(stage.material_stage_boundaries_crossed),
        },
        operator_notes="Research Brain v3 shadow item; 투자 권고가 아니다.",
    )


def _pending_item(
    *,
    event: CandidateEventV2,
    primary_archetype: str | None,
    secondary_archetypes: Sequence[str],
    card: ArchetypeMemoryCard | None,
    tasks: Sequence[SourceTask],
    status_summary: Counter,
    trigger_priority: float | None,
    score_valid_status: str,
    note: str,
) -> DailyWatchlistItemV3:
    return DailyWatchlistItemV3(
        symbol=event.symbol,
        company_name=event.company_name,
        candidate_event_id=event.candidate_event_id,
        event_type=event.event_type,
        event_summary=event.event_summary,
        primary_archetype=primary_archetype,
        secondary_archetypes=tuple(secondary_archetypes),
        research_memory_cards_used=(card.archetype_id,) if card else (),
        trigger_priority_score=trigger_priority,
        verified_score=None,
        provisional_score=None,
        score_interval_lower=None,
        score_interval_upper=None,
        score_valid_status=score_valid_status,
        base_stage="0",
        investigation_status="PENDING" if score_valid_status != ScoreValidStatusV3.PROVIDER_FAILED.value else "FAILED",
        transition_overlay="NONE",
        accepted_claim_ids=(),
        score_contribution_ids=(),
        green_blockers=tuple(card.green_blockers[:5] if card else ()),
        red_team_checks=tuple(card.false_positive_patterns[:5] if card else ()),
        source_task_status_summary=dict(status_summary),
        follow_up_tasks=tuple(task.to_dict() for task in tasks),
        do_not_promote_reasons=tuple(card.do_not_promote_rules[:5] if card else ("planner pending",)),
        stage_court_trace={},
        operator_notes=note,
    )


def _score_valid_status(value: str) -> str:
    if value in {item.value for item in ScoreValidStatusV3}:
        return value
    if value == "PROVIDER_FAILURE":
        return ScoreValidStatusV3.PROVIDER_FAILED.value
    return ScoreValidStatusV3.FINAL.value


def _float_or_none(value: Any) -> float | None:
    try:
        if value is None:
            return None
        return float(value)
    except (TypeError, ValueError):
        return None


__all__ = ["build_claim_backed_watchlist_item_v3"]
