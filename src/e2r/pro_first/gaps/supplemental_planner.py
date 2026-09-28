"""Bounded material-gap-only SourceTask planning; never a full restart."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from e2r.research_brain.schemas import SourceTask, SourceTaskType

from ..ids import stable_id
from ..models import ProResearchJob
from .adjudicator import GapAdjudicationResult, ProGapDecision
from .source_family_policy import source_family_requires_general_web


GENERAL_WEB_FAMILIES = frozenset(
    {"GENERAL_WEB_DISCOVERY", "NAVER_DISCOVERY", "TRUSTED_BUSINESS_MEDIA"}
)
OFFICIAL_SOURCE_PRIORITY = (
    "OPENDART",
    "KIND_KRX",
    "ISSUER_EARNINGS_RELEASE",
    "ISSUER_PRESENTATION",
    "FINANCIAL_STATEMENTS",
    "SEGMENT_DATA",
    "CASH_FLOW",
    "CUSTOMER_OFFICIAL",
    "ISSUER_NEWSROOM",
    "MARKET_CAP_PRICE",
    "CONSENSUS_REVISION",
    "VALUATION_MULTIPLES",
)


@dataclass(frozen=True)
class SupplementalTaskBinding:
    decision: ProGapDecision
    source_task: SourceTask
    official_first_attempted: bool
    official_gap_reasons: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.decision.supplemental_allowed:
            raise ValueError("prohibited gap cannot receive a supplemental SourceTask")
        if self.source_task.max_queries > 3:
            raise ValueError("supplemental max_queries exceeds material-gap budget")
        if self.source_task.max_candidates > 20:
            raise ValueError("supplemental max_candidates exceeds material-gap budget")
        if self.source_task.max_fetches > 6:
            raise ValueError("supplemental max_fetches exceeds material-gap budget")
        if self.source_task.general_search_allowed and not self.official_gap_reasons:
            raise ValueError("general web supplemental requires an official-source gap")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": "e2r_pro_supplemental_task_binding_v1",
            "evidence_gap_key": self.decision.key.gap_key,
            "semantic_gap_id": self.decision.key.semantic_gap_id,
            "dossier_gap_id": self.decision.dossier_gap_id,
            "planner_label": self.decision.planner_label,
            "source_task": self.source_task.to_dict(),
            "official_first_attempted": self.official_first_attempted,
            "official_gap_reasons": list(self.official_gap_reasons),
            "llm_owns_literal_queries": True,
            "full_research_restart": False,
            "production_score_authority": False,
            "production_stage_authority": False,
        }


@dataclass(frozen=True)
class SupplementalPlan:
    tasks: tuple[SupplementalTaskBinding, ...]
    decision_count: int

    @property
    def receipt_payload(self) -> Mapping[str, Any]:
        return {
            "schema_version": "e2r_pro_supplemental_plan_receipt_v1",
            "status": "SUPPLEMENTAL_PLAN_COMPLETE",
            "decision_count": self.decision_count,
            "supplemental_task_count": len(self.tasks),
            "max_queries_per_gap": 3,
            "max_candidates_per_gap": 20,
            "max_fetches_per_gap": 6,
            "full_research_restart_count": 0,
            "prohibited_gap_task_count": sum(
                binding.decision.planner_label
                in {"CORROBORATION_CAP", "MONITORING_GAP"}
                for binding in self.tasks
            ),
            "deterministic_query_template_count": 0,
            "llm_query_generation_required": True,
            "pro_score_authority": False,
            "pro_stage_authority": False,
        }


class MaterialGapSupplementalPlanner:
    def plan(
        self,
        *,
        adjudication: GapAdjudicationResult,
        job: ProResearchJob,
    ) -> SupplementalPlan:
        tasks = tuple(
            self._task_for_decision(decision, job=job)
            for decision in adjudication.decisions
            if decision.supplemental_allowed
        )
        plan = SupplementalPlan(tasks=tasks, decision_count=len(adjudication.decisions))
        if plan.receipt_payload["prohibited_gap_task_count"] != 0:
            raise ValueError("supplemental planner opened a prohibited gap")
        return plan

    def _task_for_decision(
        self,
        decision: ProGapDecision,
        *,
        job: ProResearchJob,
    ) -> SupplementalTaskBinding:
        families = _source_families(decision.key.required_source_family)
        general_web = any(source_family_requires_general_web(row) for row in families)
        context = decision.deterministic_context
        if general_web and not context.official_gap_reasons:
            raise ValueError("general web route lacks official-first gap lineage")
        preferred = tuple(
            sorted(
                families,
                key=lambda family: (
                    OFFICIAL_SOURCE_PRIORITY.index(family)
                    if family in OFFICIAL_SOURCE_PRIORITY
                    else len(OFFICIAL_SOURCE_PRIORITY),
                    family,
                ),
            )
        )
        task_type = {
            "HARD_BREAK_GAP": SourceTaskType.CONTRADICTION_RESOLUTION.value,
            "STAGE_BOUNDARY_GAP": SourceTaskType.GREEN_CLOSURE.value,
            "CORE_SCORE_BLOCKER": (
                SourceTaskType.SOURCE_REPAIR.value
                if context.provider_or_parser_failure
                else SourceTaskType.POSITIVE_VERIFY.value
            ),
        }[decision.planner_label]
        task = SourceTask(
            task_id=stable_id(
                "PROSUPTASK",
                {
                    "job_id": job.job_id,
                    "evidence_gap_key": decision.key.gap_key,
                    "planner_label": decision.planner_label,
                },
            ),
            candidate_event_id=job.candidate_id,
            symbol=job.symbol,
            company_name=job.company_name,
            archetype_id=decision.key.archetype_id,
            primitive_gap=decision.key.predicate_or_fact_need_id,
            task_type=task_type,
            preferred_source_classes=preferred,
            fallback_source_classes=(),
            forbidden_source_classes=("unbounded_general_search",),
            date_window={"end": job.as_of_date},
            max_queries=3,
            max_candidates=20,
            max_fetches=6,
            stop_condition={
                "gap_key": decision.key.gap_key,
                "stop_on_resolution": True,
                "counter_supersession_check_done": True,
            },
            query_intents=(decision.key.objective_identity,),
            llm_query_allowed=True,
            general_search_allowed=general_web,
            reason_from_memory=f"material-gap:{decision.key.gap_key}",
            memory_record_ids=(),
        )
        return SupplementalTaskBinding(
            decision=decision,
            source_task=task,
            official_first_attempted=context.official_first_attempted,
            official_gap_reasons=context.official_gap_reasons,
        )


def _source_families(requirement: str) -> tuple[str, ...]:
    prefix = "SOURCE_FAMILY_SET["
    if requirement.startswith(prefix) and requirement.endswith("]"):
        values = requirement[len(prefix) : -1].split(",")
    else:
        values = [requirement]
    families = tuple(
        dict.fromkeys(value.strip().upper() for value in values if value.strip())
    )
    if not families:
        raise ValueError("supplemental task requires a source family")
    return families


__all__ = [
    "MaterialGapSupplementalPlanner",
    "SupplementalPlan",
    "SupplementalTaskBinding",
]
