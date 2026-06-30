"""Research Brain triage facade for Census Mode."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from .schemas import BaselineScanResult, DepthDecision, DepthLevel


FORBIDDEN_RESEARCH_BRAIN_OUTPUT_KEYS = frozenset(
    {"score", "stage", "hard_break", "current_score_eligible", "verified_score", "base_stage"}
)


@dataclass(frozen=True)
class ResearchBrainPlan:
    symbol: str
    status: str
    top_k_archetype_hypotheses: tuple[str, ...]
    positive_thesis: str | None
    counter_thesis: str | None
    must_verify_primitives: tuple[str, ...]
    red_team_checks: tuple[str, ...]
    source_task_drafts: tuple[Mapping[str, Any], ...]
    do_not_promote_reasons: tuple[str, ...]
    confidence: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "symbol": self.symbol,
            "status": self.status,
            "top_k_archetype_hypotheses": list(self.top_k_archetype_hypotheses),
            "positive_thesis": self.positive_thesis,
            "counter_thesis": self.counter_thesis,
            "must_verify_primitives": list(self.must_verify_primitives),
            "red_team_checks": list(self.red_team_checks),
            "source_task_drafts": [dict(row) for row in self.source_task_drafts],
            "do_not_promote_reasons": list(self.do_not_promote_reasons),
            "confidence": self.confidence,
        }


def plan_research_brain(
    *,
    scan: BaselineScanResult,
    depth_decision: DepthDecision,
    primary_archetype: str | None = None,
) -> ResearchBrainPlan | None:
    if depth_decision.recommended_depth not in {
        DepthLevel.L3_RESEARCH_BRAIN_TRIAGE,
        DepthLevel.L4_DEEP_DOSSIER,
        DepthLevel.L5_VERIFIED_STAGE,
    }:
        return None
    if not scan.has_current_event and scan.price_anomaly_count == 0 and scan.existing_claim_count == 0:
        return ResearchBrainPlan(
            symbol=scan.symbol,
            status="NO_CURRENT_THESIS",
            top_k_archetype_hypotheses=(),
            positive_thesis=None,
            counter_thesis=None,
            must_verify_primitives=(),
            red_team_checks=(),
            source_task_drafts=(),
            do_not_promote_reasons=("No current E2R thesis; keep Stage0.",),
            confidence="LOW",
        )
    primitives = _primitive_gaps(scan)
    return ResearchBrainPlan(
        symbol=scan.symbol,
        status="TRIAGE_PLANNED",
        top_k_archetype_hypotheses=tuple(filter(None, (primary_archetype,))),
        positive_thesis="Current event requires source-backed primitive verification.",
        counter_thesis="Market or headline signal may not bridge to issuer-level score.",
        must_verify_primitives=primitives,
        red_team_checks=("wrong_subject", "historical_only", "market_anomaly_only"),
        source_task_drafts=tuple(
            {
                "primitive_gap": primitive,
                "source_class": "official_structured_first",
                "budget_required": True,
            }
            for primitive in primitives
        ),
        do_not_promote_reasons=("No score/stage output from Research Brain.",),
        confidence="MEDIUM" if primitives else "LOW",
    )


def research_brain_output_forbidden_key_count(plan: ResearchBrainPlan | Mapping[str, Any]) -> int:
    payload = plan.to_dict() if isinstance(plan, ResearchBrainPlan) else dict(plan)
    return sum(1 for key in payload if key in FORBIDDEN_RESEARCH_BRAIN_OUTPUT_KEYS)


def _primitive_gaps(scan: BaselineScanResult) -> tuple[str, ...]:
    gaps: list[str] = []
    if scan.recent_supply_contract_count:
        gaps.append("contract_quality_bridge")
    if scan.recent_facility_investment_count:
        gaps.append("capa_conversion_bridge")
    if scan.recent_earnings_event_count or scan.revision_signal_count:
        gaps.append("cash_or_revision_conversion")
    if scan.recent_risk_event_count:
        gaps.append("current_direct_risk_lifecycle")
    if scan.price_anomaly_count and not gaps:
        gaps.append("market_anomaly_explanation")
    return tuple(gaps)


__all__ = [
    "FORBIDDEN_RESEARCH_BRAIN_OUTPUT_KEYS",
    "ResearchBrainPlan",
    "plan_research_brain",
    "research_brain_output_forbidden_key_count",
]
