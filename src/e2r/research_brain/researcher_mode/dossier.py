"""Canonical Phase 84 orchestration for independent Researcher Mode memos."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from .business_model_researcher import (
    BusinessMechanismResearcher,
    BusinessModelResearchResult,
)
from .component_judge import SynthesisJudge, SynthesisResult
from .component_research_planner import ComponentResearchPlanner
from .component_researcher import (
    ComponentResearchResult,
    StructuredResearchProvider,
    build_component_researchers,
)
from .red_team_researcher import RedTeamResearchResult, RedTeamResearcher
from .research_question_seed_catalog import (
    ResearchQuestionSeed,
    load_research_question_seed_catalog,
)
from .schemas import (
    CANONICAL_COMPONENT_ORDER,
    ComponentAnchor,
    ComponentResearchMemo,
    ComponentResearchPlan,
    EvidenceFact,
)
from .structured_financial_engine import StructuredEngineResult


@dataclass(frozen=True)
class ResearcherModeDossier:
    target_id: str
    archetype_id: str
    as_of_date: str
    status: str
    business_model_result: BusinessModelResearchResult
    research_plans: tuple[ComponentResearchPlan, ...]
    component_results: tuple[ComponentResearchResult, ...]
    red_team_result: RedTeamResearchResult | None
    synthesis_result: SynthesisResult | None
    pending_reasons: tuple[str, ...]
    semantic_saturation_certified: bool = False
    production_score_authority: bool = False
    final_stage_authority: bool = False
    schema_version: str = "e2r_v5_researcher_mode_dossier_v1"

    def __post_init__(self) -> None:
        if self.status not in {"RESEARCH_MEMOS_COMPLETE", "RESEARCH_PENDING"}:
            raise ValueError("unknown Researcher Mode dossier status")
        if self.production_score_authority or self.final_stage_authority:
            raise ValueError("Phase 84 dossier is not final score or Stage authority")
        if self.semantic_saturation_certified:
            raise ValueError("Phase 84 memo orchestration cannot certify saturation")
        if self.status == "RESEARCH_PENDING" and not self.pending_reasons:
            raise ValueError("pending dossier requires reasons")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "target_id": self.target_id,
            "archetype_id": self.archetype_id,
            "as_of_date": self.as_of_date,
            "status": self.status,
            "business_model_result": self.business_model_result.to_dict(),
            "research_plans": [row.to_dict() for row in self.research_plans],
            "component_results": [row.to_dict() for row in self.component_results],
            "red_team_result": (
                self.red_team_result.to_dict() if self.red_team_result else None
            ),
            "synthesis_result": (
                self.synthesis_result.to_dict() if self.synthesis_result else None
            ),
            "pending_reasons": list(self.pending_reasons),
            "semantic_saturation_certified": self.semantic_saturation_certified,
            "production_score_authority": self.production_score_authority,
            "final_stage_authority": self.final_stage_authority,
        }


class CanonicalResearchDossierBuilder:
    """Runs business model, seven component researchers, red team, synthesis."""

    def __init__(
        self,
        *,
        provider: StructuredResearchProvider,
        planner: ComponentResearchPlanner | None = None,
        research_seeds: Sequence[ResearchQuestionSeed] | None = None,
    ) -> None:
        self.provider = provider
        self.planner = planner or ComponentResearchPlanner()
        self.research_seeds = (
            tuple(research_seeds)
            if research_seeds is not None
            else load_research_question_seed_catalog().seeds
        )

    def build(
        self,
        *,
        target_id: str,
        archetype_id: str,
        as_of_date: str,
        evidence_facts: Sequence[EvidenceFact | Mapping[str, Any]],
        historical_anchors: Sequence[ComponentAnchor | Mapping[str, Any]],
        source_claims: Sequence[Mapping[str, Any]],
        source_documents: Sequence[Mapping[str, Any]],
        source_coverage: Sequence[str | Mapping[str, Any]],
        structured_metrics_by_component: Mapping[str, Mapping[str, Any]] | None = None,
        structured_engine_result: StructuredEngineResult | None = None,
        component_max_points: Mapping[str, float] | None = None,
        structured_metric_requirements: Mapping[str, Sequence[str]] | None = None,
        prior_component_memos_by_component: Mapping[
            str, ComponentResearchMemo | Mapping[str, Any]
        ] | None = None,
    ) -> ResearcherModeDossier:
        if structured_metrics_by_component is not None and structured_engine_result is not None:
            raise ValueError(
                "provide structured metrics or structured engine result, not both"
            )
        if structured_engine_result is not None and (
            structured_engine_result.target_id != target_id
            or structured_engine_result.as_of_date != as_of_date
        ):
            raise ValueError("structured engine result target/as_of mismatch")
        facts = tuple(_coerce_fact(row) for row in evidence_facts)
        plans = self.planner.plan(
            target_id=target_id,
            archetype_id=archetype_id,
            evidence_facts=facts,
            historical_anchors=historical_anchors,
            research_seeds=self.research_seeds,
            component_max_points=component_max_points,
            structured_metric_requirements=structured_metric_requirements,
        )
        business_result = BusinessMechanismResearcher(
            provider=self.provider
        ).research(
            target_id=target_id,
            archetype_id=archetype_id,
            as_of_date=as_of_date,
            evidence_facts=facts,
            source_claims=source_claims,
            source_documents=source_documents,
            source_coverage=source_coverage,
        )
        if business_result.status != "COMPLETE" or business_result.memo is None:
            return ResearcherModeDossier(
                target_id=target_id,
                archetype_id=archetype_id,
                as_of_date=as_of_date,
                status="RESEARCH_PENDING",
                business_model_result=business_result,
                research_plans=plans,
                component_results=(),
                red_team_result=None,
                synthesis_result=None,
                pending_reasons=business_result.pending_reasons,
            )
        if structured_engine_result is not None:
            plan_requirements = {
                row.component_id: row.structured_metric_requirements for row in plans
            }
            metrics = structured_engine_result.to_component_structured_metrics(
                plan_requirements
            )
        else:
            metrics = structured_metrics_by_component or {}
        plan_by_component = {row.component_id: row for row in plans}
        prior_component_memos = prior_component_memos_by_component or {}
        unknown_prior_components = set(prior_component_memos) - set(
            CANONICAL_COMPONENT_ORDER
        )
        if unknown_prior_components:
            raise ValueError(
                "prior component memos contain unknown components: "
                f"{sorted(unknown_prior_components)}"
            )
        component_results = tuple(
            researcher.research(
                plan=plan_by_component[researcher.component_id],
                business_model=business_result.memo,
                evidence_facts=facts,
                historical_anchors=historical_anchors,
                source_coverage=source_coverage,
                source_claims=source_claims,
                source_documents=source_documents,
                structured_metrics=metrics.get(researcher.component_id, {}),
                prior_memo=prior_component_memos.get(researcher.component_id),
            )
            for researcher in build_component_researchers(self.provider)
        )
        pending = [
            f"{row.component_id}:{reason}"
            for row in component_results
            for reason in row.pending_reasons
        ]
        complete_memos = tuple(
            row.memo
            for row in component_results
            if row.status == "COMPLETE" and row.memo is not None
        )
        red_team_result = None
        synthesis_result = None
        if len(complete_memos) == len(CANONICAL_COMPONENT_ORDER):
            red_team_result = RedTeamResearcher(provider=self.provider).research(
                business_model=business_result.memo,
                component_memos=complete_memos,
                evidence_facts=facts,
                historical_anchors=historical_anchors,
                source_coverage=source_coverage,
                source_claims=source_claims,
                source_documents=source_documents,
            )
            pending.extend(red_team_result.pending_reasons)
            if red_team_result.status == "COMPLETE" and red_team_result.memo:
                synthesis_result = SynthesisJudge(provider=self.provider).synthesize(
                    target_id=target_id,
                    archetype_id=archetype_id,
                    component_memos=complete_memos,
                    red_team_memo=red_team_result.memo,
                )
                pending.extend(synthesis_result.pending_reasons)
                if synthesis_result.memo:
                    pending.extend(
                        "SYNTHESIS_UNRESOLVED:" + value
                        for value in synthesis_result.memo.unresolved_material_questions
                    )
        else:
            pending.append("SEVEN_COMPONENT_MEMOS_INCOMPLETE")
        complete = bool(
            not pending
            and len(complete_memos) == len(CANONICAL_COMPONENT_ORDER)
            and red_team_result
            and red_team_result.status == "COMPLETE"
            and synthesis_result
            and synthesis_result.status == "COMPLETE"
        )
        return ResearcherModeDossier(
            target_id=target_id,
            archetype_id=archetype_id,
            as_of_date=as_of_date,
            status=(
                "RESEARCH_MEMOS_COMPLETE" if complete else "RESEARCH_PENDING"
            ),
            business_model_result=business_result,
            research_plans=plans,
            component_results=component_results,
            red_team_result=red_team_result,
            synthesis_result=synthesis_result,
            pending_reasons=tuple(dict.fromkeys(pending)),
        )


def _coerce_fact(row: EvidenceFact | Mapping[str, Any]) -> EvidenceFact:
    if isinstance(row, EvidenceFact):
        return row
    payload = {
        key: row[key]
        for key in EvidenceFact.__dataclass_fields__
        if key in row
    }
    for key in (
        "source_ids",
        "claim_ids",
        "quote_ids",
        "corroborating_independence_groups",
        "question_family_tags",
        "primitive_tags",
        "allowed_component_ids",
        "structured_evidence_roles",
    ):
        if key in payload:
            payload[key] = tuple(payload[key] or ())
    return EvidenceFact(**payload)


__all__ = ["CanonicalResearchDossierBuilder", "ResearcherModeDossier"]
