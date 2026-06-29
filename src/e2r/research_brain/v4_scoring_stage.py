"""Claim-backed scoring and daily watchlist construction for v4."""

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
from e2r.research_brain.schemas import SourceTask
from e2r.research_brain.v2_schemas import ArchetypeMemoryCard, CandidateEventV2
from e2r.research_brain.v4_evidence_extraction_bridge import EvidenceOSExecutionBundleV4
from e2r.research_brain.v4_schemas import DailyWatchlistItemV4, PlannerRunV4, ScoreValidStatusV4
from e2r.scoring import CANONICAL_SCORE_COMPONENTS, DeterministicScorer, ScoringPayload


def build_claim_backed_watchlist_item_v4(
    *,
    event: CandidateEventV2,
    planner_run: PlannerRunV4,
    primary_archetype: str | None,
    secondary_archetypes: Sequence[str],
    card: ArchetypeMemoryCard | None,
    contract: EvidenceContractV2 | None,
    tasks: Sequence[SourceTask],
    bundle: EvidenceOSExecutionBundleV4 | None,
    as_of_date: date,
) -> DailyWatchlistItemV4:
    accepted_claim_ids = tuple(
        dict.fromkeys(
            claim_id
            for execution in (bundle.executions if bundle else ())
            for claim_id in execution.accepted_claim_ids
        )
    )
    status_summary = Counter(execution.status for execution in (bundle.executions if bundle else ()))
    trigger_priority = _float_or_none(event.price_context.get("cheap_scan_total_score"))
    if planner_run.provider_failed:
        return _pending_item(
            event=event,
            planner_run=planner_run,
            primary_archetype=primary_archetype,
            secondary_archetypes=secondary_archetypes,
            card=card,
            tasks=tasks,
            bundle=bundle,
            status_summary=status_summary,
            trigger_priority=trigger_priority,
            score_valid_status=ScoreValidStatusV4.PROVIDER_FAILED.value,
            note=planner_run.provider_error or "planner provider failed",
        )
    if not contract or not bundle or not accepted_claim_ids:
        return _pending_item(
            event=event,
            planner_run=planner_run,
            primary_archetype=primary_archetype,
            secondary_archetypes=secondary_archetypes,
            card=card,
            tasks=tasks,
            bundle=bundle,
            status_summary=status_summary,
            trigger_priority=trigger_priority,
            score_valid_status=ScoreValidStatusV4.PENDING_EVIDENCE_OS_CLAIMS.value,
            note="no real Evidence OS accepted claim",
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
            planner_run=planner_run,
            primary_archetype=primary_archetype,
            secondary_archetypes=secondary_archetypes,
            card=card,
            tasks=tasks,
            bundle=bundle,
            status_summary=status_summary,
            trigger_priority=trigger_priority,
            score_valid_status=ScoreValidStatusV4.PENDING_EVIDENCE_OS_CLAIMS.value,
            note="accepted claims did not map to scoring rubric",
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
        scoring_version="research-brain-v4-production-shadow",
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
    return DailyWatchlistItemV4(
        symbol=event.symbol,
        company_name=event.company_name,
        candidate_event_id=event.candidate_event_id,
        event_type=event.event_type,
        event_summary=event.event_summary,
        event_source=f"{event.source_family}:{event.source_id}",
        primary_archetype=primary_archetype,
        secondary_archetypes=tuple(secondary_archetypes),
        planner_provider=planner_run.provider_name,
        planner_real_provider=planner_run.real_provider_success,
        research_memory_cards_used=(card.archetype_id,) if card else (),
        source_tasks=tuple(task.to_dict() for task in tasks),
        source_task_executions=tuple(execution.to_dict() for execution in bundle.executions),
        accepted_claim_ids=accepted_claim_ids,
        top_supporting_claims=accepted_claim_ids[:5],
        score_contribution_ids=tuple(item.contribution_id for item in positive_contributions),
        trigger_priority_score=trigger_priority,
        verified_score=snapshot.total_score,
        provisional_score=None,
        score_interval_lower=interval.verified_score,
        score_interval_upper=interval.potential_score_upper_bound,
        score_valid_status=_score_valid_status(stage.score_status.value),
        base_stage=stage.decision.base_stage.value,
        investigation_status=stage.decision.investigation_status.value,
        transition_overlay=stage.decision.transition_overlay.value,
        failed_stage_gates=tuple(stage.reasons),
        green_blockers=tuple(stage.missing_green_primitives or (card.green_blockers if card else ())),
        red_team_checks=tuple(card.false_positive_patterns[:5] if card else ()),
        do_not_promote_reasons=tuple(card.do_not_promote_rules[:5] if card else ()),
        follow_up_tasks=tuple(task.to_dict() for task in tasks if not accepted_claim_ids),
        operator_notes="Research Brain v4 production shadow state board; 투자 권고가 아니다.",
        stage_court_trace={
            "score_status": stage.score_status.value,
            "present_green_primitives": list(stage.present_green_primitives),
            "missing_green_primitives": list(stage.missing_green_primitives),
            "material_stage_boundaries_crossed": list(stage.material_stage_boundaries_crossed),
            "source_task_status_summary": dict(status_summary),
        },
    )


def _pending_item(
    *,
    event: CandidateEventV2,
    planner_run: PlannerRunV4,
    primary_archetype: str | None,
    secondary_archetypes: Sequence[str],
    card: ArchetypeMemoryCard | None,
    tasks: Sequence[SourceTask],
    bundle: EvidenceOSExecutionBundleV4 | None,
    status_summary: Counter,
    trigger_priority: float | None,
    score_valid_status: str,
    note: str,
) -> DailyWatchlistItemV4:
    return DailyWatchlistItemV4(
        symbol=event.symbol,
        company_name=event.company_name,
        candidate_event_id=event.candidate_event_id,
        event_type=event.event_type,
        event_summary=event.event_summary,
        event_source=f"{event.source_family}:{event.source_id}",
        primary_archetype=primary_archetype,
        secondary_archetypes=tuple(secondary_archetypes),
        planner_provider=planner_run.provider_name,
        planner_real_provider=planner_run.real_provider_success,
        research_memory_cards_used=(card.archetype_id,) if card else (),
        source_tasks=tuple(task.to_dict() for task in tasks),
        source_task_executions=tuple(execution.to_dict() for execution in (bundle.executions if bundle else ())),
        trigger_priority_score=trigger_priority,
        score_valid_status=score_valid_status,
        base_stage="0",
        investigation_status="FAILED" if score_valid_status == ScoreValidStatusV4.PROVIDER_FAILED.value else "PENDING",
        transition_overlay="NONE",
        green_blockers=tuple(card.green_blockers[:5] if card else ()),
        red_team_checks=tuple(card.false_positive_patterns[:5] if card else ()),
        do_not_promote_reasons=tuple(card.do_not_promote_rules[:5] if card else ("planner pending",)),
        follow_up_tasks=tuple(task.to_dict() for task in tasks),
        operator_notes=note,
        stage_court_trace={"source_task_status_summary": dict(status_summary)} if status_summary else {},
    )


def _score_valid_status(value: str) -> str:
    if value in {item.value for item in ScoreValidStatusV4}:
        return value
    if value == "PROVIDER_FAILURE":
        return ScoreValidStatusV4.PROVIDER_FAILED.value
    return ScoreValidStatusV4.FINAL.value


def _float_or_none(value: Any) -> float | None:
    try:
        if value is None:
            return None
        return float(value)
    except (TypeError, ValueError):
        return None


__all__ = ["build_claim_backed_watchlist_item_v4"]
