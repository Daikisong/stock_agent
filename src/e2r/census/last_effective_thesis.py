"""Last effective thesis state for Census v2."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence

from .baseline_input_collector import CensusBaselineBundle
from .lifecycle_refresh import adjudicate_lifecycle, load_lifecycle_policy
from .source_timeline import SourceTimeline


@dataclass(frozen=True)
class LastEffectiveThesisState:
    symbol: str
    company_name: str
    as_of_date: str
    thesis_status: str
    base_stage_hint: str
    last_effective_event_id: str | None = None
    accepted_claim_count: int = 0
    score_contribution_count: int = 0
    source_task_count: int = 0
    current_score_eligible_claim_count: int = 0
    followup_required: bool = False
    reason_codes: tuple[str, ...] = ()
    lifecycle_notes: tuple[Mapping[str, Any], ...] = field(default_factory=tuple)

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": "e2r_census_v2_last_effective_thesis_state_v1",
            "symbol": self.symbol,
            "company_name": self.company_name,
            "as_of_date": self.as_of_date,
            "thesis_status": self.thesis_status,
            "base_stage_hint": self.base_stage_hint,
            "last_effective_event_id": self.last_effective_event_id,
            "accepted_claim_count": self.accepted_claim_count,
            "score_contribution_count": self.score_contribution_count,
            "source_task_count": self.source_task_count,
            "current_score_eligible_claim_count": self.current_score_eligible_claim_count,
            "followup_required": self.followup_required,
            "reason_codes": list(self.reason_codes),
            "lifecycle_notes": [dict(item) for item in self.lifecycle_notes],
        }


def build_last_effective_thesis_states(
    *,
    timelines: Sequence[SourceTimeline],
    bundle: CensusBaselineBundle,
    as_of_date: str,
    lifecycle_policy_path: str = "configs/e2r_census_lifecycle_policy_v1.json",
) -> tuple[LastEffectiveThesisState, ...]:
    policy = load_lifecycle_policy(lifecycle_policy_path)
    task_count_by_symbol: dict[str, int] = {}
    for task in bundle.source_tasks:
        symbol = str(task.get("symbol") or "").zfill(6)
        task_count_by_symbol[symbol] = task_count_by_symbol.get(symbol, 0) + 1
    states: list[LastEffectiveThesisState] = []
    for timeline in timelines:
        accepted = tuple(bundle.existing_ledger.accepted_claims_by_symbol.get(timeline.symbol, ()))
        score_contribs = tuple(bundle.existing_ledger.score_contributions_by_symbol.get(timeline.symbol, ()))
        lifecycle_notes = tuple(
            {
                "event_id": event.event_id,
                **adjudicate_lifecycle(event={**event.metadata, **event.to_dict()}, as_of_date=as_of_date, policy=policy).to_dict(),
            }
            for event in timeline.events
            if event.event_type != "CensusAssessmentEvent"
        )
        if accepted and score_contribs:
            stage_hint = _stage_hint(bundle.existing_ledger.existing_stage_by_symbol.get(timeline.symbol))
            states.append(
                LastEffectiveThesisState(
                    symbol=timeline.symbol,
                    company_name=timeline.company_name,
                    as_of_date=as_of_date,
                    thesis_status="ACTIVE_THESIS",
                    base_stage_hint=stage_hint,
                    last_effective_event_id=_last_event_id(timeline),
                    accepted_claim_count=len(accepted),
                    score_contribution_count=len(score_contribs),
                    source_task_count=task_count_by_symbol.get(timeline.symbol, 0),
                    current_score_eligible_claim_count=len(accepted),
                    followup_required=False,
                    reason_codes=("accepted_current_claims_present",),
                    lifecycle_notes=lifecycle_notes,
                )
            )
            continue
        if task_count_by_symbol.get(timeline.symbol, 0) or any(event.candidate_event_eligible for event in timeline.events if event.event_type != "CensusAssessmentEvent"):
            events = tuple(event for event in timeline.events if event.event_type != "CensusAssessmentEvent")
            only_market = bool(events) and all(event.event_type == "MarketAnomaly" for event in events)
            states.append(
                LastEffectiveThesisState(
                    symbol=timeline.symbol,
                    company_name=timeline.company_name,
                    as_of_date=as_of_date,
                    thesis_status="NEEDS_REFRESH" if only_market else "SOURCE_PENDING",
                    base_stage_hint="Stage1" if events else "Stage0",
                    last_effective_event_id=_last_event_id(timeline),
                    source_task_count=task_count_by_symbol.get(timeline.symbol, 0),
                    followup_required=True,
                    reason_codes=("market_anomaly_investigation_only",) if only_market else ("candidate_event_without_accepted_current_claim",),
                    lifecycle_notes=lifecycle_notes,
                )
            )
            continue
        states.append(
            LastEffectiveThesisState(
                symbol=timeline.symbol,
                company_name=timeline.company_name,
                as_of_date=as_of_date,
                thesis_status="NO_KNOWN_THESIS",
                base_stage_hint="Stage0",
                last_effective_event_id=None,
                reason_codes=("no_current_catalyst_after_baseline_sources",),
                lifecycle_notes=lifecycle_notes,
            )
        )
    return tuple(states)


def _last_event_id(timeline: SourceTimeline) -> str | None:
    for event in reversed(timeline.events):
        if event.event_type != "CensusAssessmentEvent":
            return event.event_id
    return None


def _stage_hint(value: str | None) -> str:
    if value == "3-Red":
        return "Red"
    if value == "2":
        return "Stage2-Watch"
    if value == "1":
        return "Stage1"
    return "Stage1"


__all__ = ["LastEffectiveThesisState", "build_last_effective_thesis_states"]
