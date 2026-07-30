"""Phase 97 selective-deep daily Census and persistent dossier integration.

The daily Census remains a cheap full-universe operation.  Researcher Mode is
opened only for selected candidates, while an already researched target keeps
one versioned dossier.  A material event does not erase that dossier: facts
with explicit component lineage reopen only the affected component memos and
the downstream red-team/synthesis/score path.

This module plans and audits that state transition.  It never generates a
literal search query, scores evidence, or decides a Stage.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date
from enum import Enum
import json
import math
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json, write_jsonl
from e2r.research_brain.runtime.atomic_score_stage import CanonicalStage
from e2r.research_brain.runtime.current_operation import CurrentDeepOutcome
from e2r.research_brain.runtime.current_operation_runner import (
    CensusDepthLevel,
    CurrentOperationRunnerResult,
    DailyTerminalStatus,
)

from .schemas import CANONICAL_COMPONENT_ORDER, EvidenceLifecycle
from .saturation import (
    GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY,
    SATURATION_REVIEW_ROLES,
)


DAILY_CENSUS_INTEGRATION_SCHEMA_VERSION = (
    "e2r_v5_daily_census_researcher_integration_v1"
)
DAILY_CENSUS_INTEGRATION_PASS = (
    "V5_PHASE97_DAILY_CENSUS_RESEARCHER_INTEGRATION_PASS"
)
DAILY_CENSUS_INTEGRATION_FAIL = (
    "V5_PHASE97_DAILY_CENSUS_RESEARCHER_INTEGRATION_FAIL"
)
DEFAULT_DAILY_CENSUS_INTEGRATION_OUTPUT_PATH = (
    "docs/operational/e2r_v5_daily_census_integration.json"
)


class DossierResearchStatus(str, Enum):
    FULL_THESIS_ACTIVE = "FULL_THESIS_ACTIVE"
    RESEARCH_PENDING = "RESEARCH_PENDING"
    SOURCE_PENDING = "SOURCE_PENDING"
    PROVIDER_PENDING = "PROVIDER_PENDING"
    DISPROVED = "DISPROVED"


class DossierComponentStatus(str, Enum):
    CURRENT = "CURRENT"
    REOPEN_REQUIRED = "REOPEN_REQUIRED"
    RESEARCH_PENDING = "RESEARCH_PENDING"


class FullThesisStatus(str, Enum):
    NOT_OPEN = "NOT_OPEN"
    FULL_RESEARCH_REQUIRED = "FULL_RESEARCH_REQUIRED"
    DELTA_RESEARCH_REQUIRED = "DELTA_RESEARCH_REQUIRED"
    FACT_IMPACT_MAPPING_PENDING = "FACT_IMPACT_MAPPING_PENDING"
    SOURCE_PENDING = "SOURCE_PENDING"
    PROVIDER_PENDING = "PROVIDER_PENDING"
    BUDGET_CHECKPOINT_PENDING = "BUDGET_CHECKPOINT_PENDING"
    FULL_THESIS_CURRENT = "FULL_THESIS_CURRENT"
    FULL_THESIS_REUSED = "FULL_THESIS_REUSED"
    DISPROVED = "DISPROVED"


class ScoreDisplayStatus(str, Enum):
    NO_CURRENT_SCORE = "NO_CURRENT_SCORE"
    CURRENT_DETERMINISTIC = "CURRENT_DETERMINISTIC"
    LAST_EFFECTIVE = "LAST_EFFECTIVE"
    LAST_EFFECTIVE_PENDING_DELTA = "LAST_EFFECTIVE_PENDING_DELTA"
    RAW_REFERENCE_ONLY = "RAW_REFERENCE_ONLY"


_PENDING_TERMINALS = {
    DailyTerminalStatus.SOURCE_PENDING.value,
    DailyTerminalStatus.PROVIDER_PENDING.value,
    DailyTerminalStatus.BUDGET_PENDING.value,
}
_DEEP_DEPTHS = {
    CensusDepthLevel.L3_RESEARCH_BRAIN.value,
    CensusDepthLevel.L4_ACQUISITION.value,
    CensusDepthLevel.L5_FULL_THESIS.value,
}


@dataclass(frozen=True)
class DossierFactLineage:
    fact_id: str
    target_id: str
    available_date: str
    source_ids: tuple[str, ...]
    allowed_component_ids: tuple[str, ...]
    current_lifecycle: str = EvidenceLifecycle.CURRENT.value

    def __post_init__(self) -> None:
        object.__setattr__(self, "source_ids", tuple(self.source_ids))
        object.__setattr__(
            self, "allowed_component_ids", tuple(self.allowed_component_ids)
        )
        if not self.fact_id.strip() or not self.target_id.strip():
            raise ValueError("dossier fact identity is required")
        date.fromisoformat(self.available_date)
        EvidenceLifecycle(self.current_lifecycle)
        _unique_text(self.source_ids, "dossier fact source ids", required=True)
        _unique_text(
            self.allowed_component_ids,
            "dossier fact component ids",
            required=False,
        )
        if set(self.allowed_component_ids) - set(CANONICAL_COMPONENT_ORDER):
            raise ValueError("dossier fact contains an unknown component")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class DossierComponentState:
    component_id: str
    status: str
    memo_id: str | None
    memo_hash: str | None
    decision_id: str | None
    fact_ids: tuple[str, ...]
    final_points: float | None
    reviewed_event_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "fact_ids", tuple(self.fact_ids))
        object.__setattr__(
            self, "reviewed_event_ids", tuple(self.reviewed_event_ids)
        )
        if self.component_id not in CANONICAL_COMPONENT_ORDER:
            raise ValueError("dossier component id is not canonical")
        status = DossierComponentStatus(self.status)
        _unique_text(self.fact_ids, "dossier component fact ids", required=False)
        _unique_text(
            self.reviewed_event_ids,
            "dossier component reviewed events",
            required=False,
        )
        if status == DossierComponentStatus.CURRENT:
            if not all(
                isinstance(value, str) and value.strip()
                for value in (self.memo_id, self.memo_hash, self.decision_id)
            ):
                raise ValueError("current dossier component needs memo/decision lineage")
            if len(str(self.memo_hash)) != 64:
                raise ValueError("dossier component memo hash must be sha256")
            try:
                int(str(self.memo_hash), 16)
            except ValueError as exc:
                raise ValueError("dossier component memo hash must be hexadecimal") from exc
            if (
                self.final_points is None
                or isinstance(self.final_points, bool)
                or not math.isfinite(float(self.final_points))
                or not 0.0 <= float(self.final_points) <= 100.0
            ):
                raise ValueError("current component requires finite points")
        elif any(
            value is not None
            for value in (self.memo_id, self.memo_hash, self.decision_id, self.final_points)
        ):
            raise ValueError("reopened/pending component cannot masquerade as current")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class PersistedResearchDossier:
    dossier_id: str
    target_id: str
    target_name: str
    archetype_id: str
    as_of_date: str
    version: int
    previous_dossier_id: str | None
    status: str
    research_epoch_checkpoint_id: str | None
    semantic_saturation_certified: bool
    facts: tuple[DossierFactLineage, ...]
    components: tuple[DossierComponentState, ...]
    business_model_memo_hash: str | None
    red_team_memo_hash: str | None
    synthesis_memo_hash: str | None
    score_decision_id: str | None
    score_value: float | None
    canonical_stage: str | None
    score_valid: bool
    applied_event_ids: tuple[str, ...] = ()
    pending_reasons: tuple[str, ...] = ()
    score_authority: str = "DETERMINISTIC_SCORE_AGGREGATOR"
    stage_authority: str = "DETERMINISTIC_STAGECOURT"
    schema_version: str = "e2r_v5_persisted_research_dossier_v1"

    def __post_init__(self) -> None:
        object.__setattr__(self, "facts", tuple(self.facts))
        object.__setattr__(self, "components", tuple(self.components))
        object.__setattr__(self, "applied_event_ids", tuple(self.applied_event_ids))
        object.__setattr__(self, "pending_reasons", tuple(self.pending_reasons))
        selected_status = DossierResearchStatus(self.status)
        if not all(
            isinstance(value, str) and value.strip()
            for value in (
                self.dossier_id,
                self.target_id,
                self.target_name,
                self.archetype_id,
            )
        ):
            raise ValueError("persisted dossier identity is required")
        date.fromisoformat(self.as_of_date)
        if isinstance(self.version, bool) or self.version <= 0:
            raise ValueError("dossier version must be positive")
        if self.version == 1 and self.previous_dossier_id is not None:
            raise ValueError("initial dossier cannot have prior lineage")
        if self.version > 1 and not str(self.previous_dossier_id or "").strip():
            raise ValueError("versioned dossier requires prior lineage")
        for name in ("semantic_saturation_certified", "score_valid"):
            if not isinstance(getattr(self, name), bool):
                raise ValueError(f"dossier {name} must be boolean")
        _unique_text(self.applied_event_ids, "dossier applied events", required=False)
        _unique_text(self.pending_reasons, "dossier pending reasons", required=False)
        fact_ids = tuple(row.fact_id for row in self.facts)
        _unique_text(fact_ids, "dossier fact ids", required=False)
        if any(row.target_id != self.target_id for row in self.facts):
            raise ValueError("dossier contains a fact for another target")
        if any(
            date.fromisoformat(row.available_date)
            > date.fromisoformat(self.as_of_date)
            for row in self.facts
        ):
            raise ValueError("future fact entered persisted dossier")
        component_ids = tuple(row.component_id for row in self.components)
        _unique_text(component_ids, "dossier component ids", required=False)
        if any(
            set(row.fact_ids) - set(fact_ids)
            for row in self.components
        ):
            raise ValueError("dossier component references an unknown fact")
        if self.score_authority != "DETERMINISTIC_SCORE_AGGREGATOR":
            raise ValueError("dossier score authority must remain deterministic")
        if self.stage_authority != "DETERMINISTIC_STAGECOURT":
            raise ValueError("dossier Stage authority must remain deterministic")
        if self.canonical_stage is not None:
            CanonicalStage(self.canonical_stage)
        complete = selected_status in {
            DossierResearchStatus.FULL_THESIS_ACTIVE,
            DossierResearchStatus.DISPROVED,
        }
        if complete:
            component_total = sum(
                float(row.final_points or 0.0) for row in self.components
            )
            if (
                not self.semantic_saturation_certified
                or not self.score_valid
                or self.score_value is None
                or not math.isfinite(float(self.score_value))
                or not 0.0 <= float(self.score_value) <= 100.0
                or self.canonical_stage is None
                or not self.score_decision_id
                or not self.research_epoch_checkpoint_id
                or self.pending_reasons
                or tuple(component_ids) != tuple(CANONICAL_COMPONENT_ORDER)
                or any(
                    row.status != DossierComponentStatus.CURRENT.value
                    for row in self.components
                )
                or abs(component_total - float(self.score_value or 0.0)) > 1e-9
                or not all(
                    _sha256(value)
                    for value in (
                        self.business_model_memo_hash,
                        self.red_team_memo_hash,
                        self.synthesis_memo_hash,
                    )
                )
            ):
                raise ValueError("complete dossier lacks full semantic/score lineage")
        else:
            if not self.pending_reasons:
                raise ValueError("pending dossier needs exact reasons")
            if self.score_valid or self.score_value is not None or self.canonical_stage is not None:
                raise ValueError("pending dossier cannot publish a current score or Stage")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            **asdict(self),
            "facts": [row.to_dict() for row in self.facts],
            "components": [row.to_dict() for row in self.components],
        }


@dataclass(frozen=True)
class DailyDossierEvent:
    event_id: str
    target_id: str
    event_date: str
    available_date: str
    source_document_ids: tuple[str, ...]
    new_facts: tuple[DossierFactLineage, ...] = ()
    revised_fact_ids: tuple[str, ...] = ()
    retired_fact_ids: tuple[str, ...] = ()
    impact_mapping_ids: tuple[str, ...] = ()
    global_business_model_impact: bool = False
    material: bool = True

    def __post_init__(self) -> None:
        for name in (
            "source_document_ids",
            "new_facts",
            "revised_fact_ids",
            "retired_fact_ids",
            "impact_mapping_ids",
        ):
            object.__setattr__(self, name, tuple(getattr(self, name)))
        if not self.event_id.strip() or not self.target_id.strip():
            raise ValueError("daily dossier event identity is required")
        event_day = date.fromisoformat(self.event_date)
        available = date.fromisoformat(self.available_date)
        if available < event_day:
            raise ValueError("event cannot be available before it happened")
        for name in ("global_business_model_impact", "material"):
            if not isinstance(getattr(self, name), bool):
                raise ValueError(f"event {name} must be boolean")
        _unique_text(
            self.source_document_ids,
            "daily event source documents",
            required=True,
        )
        _unique_text(self.revised_fact_ids, "revised fact ids", required=False)
        _unique_text(self.retired_fact_ids, "retired fact ids", required=False)
        _unique_text(self.impact_mapping_ids, "impact mapping ids", required=False)
        new_ids = tuple(row.fact_id for row in self.new_facts)
        _unique_text(new_ids, "new event fact ids", required=False)
        if any(row.target_id != self.target_id for row in self.new_facts):
            raise ValueError("event fact target mismatch")
        if any(date.fromisoformat(row.available_date) > available for row in self.new_facts):
            raise ValueError("event contains a fact unavailable at event time")
        changed = set(new_ids) | set(self.revised_fact_ids) | set(self.retired_fact_ids)
        if set(self.revised_fact_ids) & set(self.retired_fact_ids):
            raise ValueError("one event cannot revise and retire the same fact")
        if self.global_business_model_impact and not self.impact_mapping_ids:
            raise ValueError("global business-model impact requires mapping lineage")
        if (self.material or self.global_business_model_impact) and changed:
            if not self.impact_mapping_ids:
                raise ValueError("material fact delta requires impact mapping lineage")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            **asdict(self),
            "new_facts": [row.to_dict() for row in self.new_facts],
        }


@dataclass(frozen=True)
class DossierDeltaPlan:
    delta_id: str
    target_id: str
    as_of_date: str
    prior_dossier_id: str
    event_ids: tuple[str, ...]
    status: str
    changed_fact_ids: tuple[str, ...]
    retired_fact_ids: tuple[str, ...]
    reopened_component_ids: tuple[str, ...]
    reused_component_ids: tuple[str, ...]
    source_refresh_objectives: tuple[Mapping[str, Any], ...]
    component_rejudge_ids: tuple[str, ...]
    red_team_reopen: bool
    synthesis_reopen: bool
    deterministic_rescore_required: bool
    prior_score_value: float | None
    prior_canonical_stage: str | None
    new_score_value: float | None
    new_canonical_stage: str | None
    score_delta: float | None
    pending_reasons: tuple[str, ...]
    query_generation_authority: str = "LLM_RESEARCH_SUPERVISOR"
    deterministic_query_synthesis: bool = False
    llm_score_authority: bool = False
    llm_stage_authority: bool = False

    def __post_init__(self) -> None:
        for name in (
            "event_ids",
            "changed_fact_ids",
            "retired_fact_ids",
            "reopened_component_ids",
            "reused_component_ids",
            "source_refresh_objectives",
            "component_rejudge_ids",
            "pending_reasons",
        ):
            object.__setattr__(self, name, tuple(getattr(self, name)))
        if self.status not in {
            "DELTA_RESEARCH_REQUIRED",
            "FACT_IMPACT_MAPPING_PENDING",
            "DELTA_APPLIED",
        }:
            raise ValueError("unknown dossier delta status")
        if not self.delta_id.strip() or not self.prior_dossier_id.strip():
            raise ValueError("dossier delta identity is required")
        date.fromisoformat(self.as_of_date)
        for values, label, required in (
            (self.event_ids, "delta event ids", True),
            (self.changed_fact_ids, "delta changed facts", False),
            (self.retired_fact_ids, "delta retired facts", False),
            (self.reopened_component_ids, "delta reopened components", False),
            (self.reused_component_ids, "delta reused components", False),
            (self.component_rejudge_ids, "delta rejudge components", False),
            (self.pending_reasons, "delta pending reasons", False),
        ):
            _unique_text(values, label, required=required)
        all_components = set(CANONICAL_COMPONENT_ORDER)
        reopened = set(self.reopened_component_ids)
        reused = set(self.reused_component_ids)
        if reopened & reused or reopened | reused != all_components:
            raise ValueError("delta must partition all canonical components")
        if tuple(self.component_rejudge_ids) != tuple(self.reopened_component_ids):
            raise ValueError("only reopened components may be re-judged")
        if len(self.source_refresh_objectives) != len(reopened):
            raise ValueError("each reopened component requires one source objective")
        for objective in self.source_refresh_objectives:
            if (
                objective.get("component_id") not in reopened
                or objective.get("query_generation_authority")
                != "LLM_RESEARCH_SUPERVISOR"
                or objective.get("literal_query") is not None
                or objective.get("official_first") is not True
                or objective.get("general_web_requires_official_gap") is not True
            ):
                raise ValueError("delta source objective violates LLM/official-first policy")
        mapped = self.status != "FACT_IMPACT_MAPPING_PENDING"
        if mapped != bool(reopened):
            raise ValueError("mapped delta and reopened component state disagree")
        if mapped and not (
            self.red_team_reopen
            and self.synthesis_reopen
            and self.deterministic_rescore_required
        ):
            raise ValueError("component delta must reopen all downstream judgments")
        if self.status == "DELTA_APPLIED":
            if (
                self.pending_reasons
                or self.new_score_value is None
                or self.new_canonical_stage is None
                or self.score_delta is None
            ):
                raise ValueError("applied delta needs deterministic score/Stage result")
            CanonicalStage(self.new_canonical_stage)
        elif (
            self.new_score_value is not None
            or self.new_canonical_stage is not None
            or self.score_delta is not None
            or not self.pending_reasons
        ):
            raise ValueError("pending delta cannot manufacture a score delta")
        if self.query_generation_authority != "LLM_RESEARCH_SUPERVISOR":
            raise ValueError("delta query generation must remain LLM-owned")
        if (
            self.deterministic_query_synthesis
            or self.llm_score_authority
            or self.llm_stage_authority
        ):
            raise ValueError("delta cannot grant deterministic-query or LLM score authority")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            **asdict(self),
            "source_refresh_objectives": [
                dict(row) for row in self.source_refresh_objectives
            ],
        }


@dataclass(frozen=True)
class DailyResearcherCensusRow:
    assessment_id: str
    target_id: str
    target_name: str
    as_of_date: str
    maximum_depth: str
    daily_assessment_event_ids: tuple[str, ...]
    researcher_candidate: bool
    researcher_candidate_id: str | None
    dossier_id: str | None
    dossier_version: int | None
    current_score: float | None
    raw_reference_score: float | None
    current_stage: str | None
    score_display_status: str
    full_thesis_status: str
    pending_reasons: tuple[str, ...]
    next_action: str
    direct_investment_recommendation: bool = False

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "daily_assessment_event_ids",
            tuple(self.daily_assessment_event_ids),
        )
        object.__setattr__(self, "pending_reasons", tuple(self.pending_reasons))
        CensusDepthLevel(self.maximum_depth)
        ScoreDisplayStatus(self.score_display_status)
        FullThesisStatus(self.full_thesis_status)
        date.fromisoformat(self.as_of_date)
        if not self.assessment_id.strip() or not self.target_id.strip():
            raise ValueError("daily Researcher Census identity is required")
        _unique_text(
            self.daily_assessment_event_ids,
            "daily assessment event ids",
            required=False,
        )
        _unique_text(self.pending_reasons, "daily pending reasons", required=False)
        if self.researcher_candidate != bool(self.researcher_candidate_id):
            raise ValueError("Researcher candidate id/flag mismatch")
        if self.current_stage is not None:
            CanonicalStage(self.current_stage)
        if self.current_score is not None and (
            isinstance(self.current_score, bool)
            or not math.isfinite(float(self.current_score))
            or not 0.0 <= float(self.current_score) <= 100.0
        ):
            raise ValueError("daily current score is invalid")
        if self.full_thesis_status in {
            FullThesisStatus.SOURCE_PENDING.value,
            FullThesisStatus.PROVIDER_PENDING.value,
            FullThesisStatus.BUDGET_CHECKPOINT_PENDING.value,
            FullThesisStatus.FACT_IMPACT_MAPPING_PENDING.value,
        } and not self.pending_reasons:
            raise ValueError("pending daily row requires exact reasons")
        if self.direct_investment_recommendation:
            raise ValueError("daily output cannot contain an investment instruction")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class DailyCensusResearcherIntegrationResult:
    integration_id: str
    as_of_date: str
    daily_run_id: str
    rows: tuple[DailyResearcherCensusRow, ...]
    delta_plans: tuple[DossierDeltaPlan, ...]
    dossiers: tuple[PersistedResearchDossier, ...]
    audit: Mapping[str, Any]
    status: str
    schema_version: str = DAILY_CENSUS_INTEGRATION_SCHEMA_VERSION

    def __post_init__(self) -> None:
        object.__setattr__(self, "rows", tuple(self.rows))
        object.__setattr__(self, "delta_plans", tuple(self.delta_plans))
        object.__setattr__(self, "dossiers", tuple(self.dossiers))
        date.fromisoformat(self.as_of_date)
        if self.status not in {
            DAILY_CENSUS_INTEGRATION_PASS,
            DAILY_CENSUS_INTEGRATION_FAIL,
        }:
            raise ValueError("daily integration status is invalid")
        expected_audit = audit_daily_census_integration(self.to_leaf_dict())
        if dict(self.audit) != dict(expected_audit):
            raise ValueError("daily integration audit does not reconcile")
        expected_status = (
            DAILY_CENSUS_INTEGRATION_PASS
            if expected_audit["critical_count_sum"] == 0
            else DAILY_CENSUS_INTEGRATION_FAIL
        )
        if self.status != expected_status:
            raise ValueError("daily integration status contradicts audit")

    def to_leaf_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "integration_id": self.integration_id,
            "as_of_date": self.as_of_date,
            "daily_run_id": self.daily_run_id,
            "rows": [row.to_dict() for row in self.rows],
            "delta_plans": [row.to_dict() for row in self.delta_plans],
            "dossiers": [row.to_dict() for row in self.dossiers],
        }

    def to_dict(self) -> Mapping[str, Any]:
        return {
            **self.to_leaf_dict(),
            "status": self.status,
            "audit": dict(self.audit),
        }


def integrate_daily_census_researcher_mode(
    daily_census: CurrentOperationRunnerResult | Mapping[str, Any],
    *,
    persisted_dossiers: Sequence[PersistedResearchDossier | Mapping[str, Any]] = (),
    new_events: Sequence[DailyDossierEvent | Mapping[str, Any]] = (),
    completed_dossier_updates: Sequence[
        PersistedResearchDossier | Mapping[str, Any]
    ] = (),
) -> DailyCensusResearcherIntegrationResult:
    """Join one daily Census with stored dossiers and source-backed deltas."""

    daily = (
        daily_census.to_dict()
        if isinstance(daily_census, CurrentOperationRunnerResult)
        else _json_safe(daily_census)
    )
    as_of_date = str(daily.get("as_of_date") or "")
    cutoff = date.fromisoformat(as_of_date)
    daily_run_id = str(daily.get("run_id") or daily.get("integration_fixture_id") or "")
    if not daily_run_id:
        raise ValueError("daily Census run id is required")
    universe = tuple(_mapping_rows(daily.get("universe")))
    statuses = tuple(_mapping_rows(daily.get("stage_statuses")))
    depths = tuple(_mapping_rows(daily.get("depth_decisions")))
    if not universe or len(statuses) != len(universe) or len(depths) != len(universe):
        raise ValueError("daily integration requires one status/depth per universe row")
    _unique_text(
        tuple(str(row.get("target_id") or "") for row in universe),
        "daily integration universe ids",
        required=True,
    )
    status_by_target = _unique_mapping(statuses, "target_id", "daily status")
    depth_by_target = _unique_mapping(depths, "target_id", "daily depth")
    _validate_daily_depth_rows(
        universe=universe,
        statuses=status_by_target,
        depths=depth_by_target,
    )

    prior = tuple(_coerce_dossier(row) for row in persisted_dossiers)
    updates = tuple(_coerce_dossier(row) for row in completed_dossier_updates)
    events = tuple(_coerce_event(row) for row in new_events)
    _unique_objects(events, "event_id", "daily dossier event")
    if any(
        date.fromisoformat(row.as_of_date) > cutoff for row in (*prior, *updates)
    ):
        raise ValueError("future dossier entered daily integration")
    prior_by_target = _unique_objects(prior, "target_id", "persisted dossier")
    update_by_target = _unique_objects(updates, "target_id", "completed dossier")
    if set(update_by_target) - set(prior_by_target):
        raise ValueError("completed delta update requires a prior dossier")
    events_by_target: dict[str, list[DailyDossierEvent]] = {}
    for event in events:
        if date.fromisoformat(event.available_date) > cutoff:
            raise ValueError("future event entered daily dossier integration")
        if event.target_id not in status_by_target:
            raise ValueError("daily event target is outside the Census universe")
        events_by_target.setdefault(event.target_id, []).append(event)

    material_event_targets = {
        target_id
        for target_id, target_events in events_by_target.items()
        if any(row.material or row.global_business_model_impact for row in target_events)
    }
    if set(update_by_target) - material_event_targets:
        raise ValueError("completed dossier update requires a material daily event")

    delta_plans: list[DossierDeltaPlan] = []
    for target_id in sorted(events_by_target):
        stored = prior_by_target.get(target_id)
        if stored is None:
            continue
        material_events = tuple(
            row
            for row in sorted(events_by_target[target_id], key=lambda row: row.event_id)
            if row.material or row.global_business_model_impact
        )
        if not material_events:
            continue
        plan = _build_delta_plan(
            as_of_date=as_of_date,
            prior=stored,
            events=material_events,
            completed_update=update_by_target.get(target_id),
        )
        if update_by_target.get(target_id) is not None and plan.status != "DELTA_APPLIED":
            raise ValueError("completed dossier update did not close its material delta")
        delta_plans.append(plan)
    delta_by_target = {row.target_id: row for row in delta_plans}

    rows: list[DailyResearcherCensusRow] = []
    for member in universe:
        target_id = str(member.get("target_id") or "")
        target_name = str(member.get("target_name") or target_id)
        status = status_by_target[target_id]
        depth = depth_by_target[target_id]
        maximum_depth = str(depth.get("maximum_depth") or "")
        CensusDepthLevel(maximum_depth)
        selected = bool(depth.get("selected_for_deep"))
        candidate = selected or maximum_depth in _DEEP_DEPTHS
        event_rows = tuple(
            sorted(events_by_target.get(target_id, ()), key=lambda row: row.event_id)
        )
        stored = prior_by_target.get(target_id)
        completed = update_by_target.get(target_id)
        plan = delta_by_target.get(target_id)
        row = _build_census_row(
            member=member,
            status=status,
            depth=depth,
            as_of_date=as_of_date,
            candidate=candidate,
            events=event_rows,
            stored=stored,
            completed=completed,
            delta_plan=plan,
        )
        rows.append(row)

    result_payload = {
        "as_of_date": as_of_date,
        "daily_run_id": daily_run_id,
        "row_ids": [row.assessment_id for row in rows],
        "delta_ids": [row.delta_id for row in delta_plans],
        "dossier_ids": [row.dossier_id for row in (*prior, *updates)],
    }
    integration_id = "DCI-" + stable_hash(result_payload)[:24]
    dossiers = tuple(sorted((*prior, *updates), key=lambda row: (row.target_id, row.version)))
    leaf = {
        "schema_version": DAILY_CENSUS_INTEGRATION_SCHEMA_VERSION,
        "integration_id": integration_id,
        "as_of_date": as_of_date,
        "daily_run_id": daily_run_id,
        "rows": [row.to_dict() for row in rows],
        "delta_plans": [row.to_dict() for row in delta_plans],
        "dossiers": [row.to_dict() for row in dossiers],
        "daily_source_tasks": list(_mapping_rows(daily.get("source_tasks"))),
        "daily_deep_executions": list(_mapping_rows(daily.get("deep_executions"))),
    }
    audit = audit_daily_census_integration(leaf)
    status_value = (
        DAILY_CENSUS_INTEGRATION_PASS
        if audit["critical_count_sum"] == 0
        else DAILY_CENSUS_INTEGRATION_FAIL
    )
    # Result validation intentionally audits only persisted leaves.  Runtime
    # SourceTask checks were already included above and must pass before return.
    if audit["critical_count_sum"]:
        raise ValueError(f"daily Census integration audit failed: {audit['critical_counts']}")
    compact_leaf = {key: value for key, value in leaf.items() if not key.startswith("daily_") or key == "daily_run_id"}
    compact_audit = audit_daily_census_integration(compact_leaf)
    return DailyCensusResearcherIntegrationResult(
        integration_id=integration_id,
        as_of_date=as_of_date,
        daily_run_id=daily_run_id,
        rows=tuple(rows),
        delta_plans=tuple(delta_plans),
        dossiers=dossiers,
        audit=compact_audit,
        status=status_value,
    )


def build_persisted_research_dossier(
    *,
    target_name: str,
    research_dossier: Any | Mapping[str, Any],
    research_epoch_checkpoint: Any | Mapping[str, Any],
    score_aggregation: Any | Mapping[str, Any],
    stagecourt_run: Any | Mapping[str, Any],
    evidence_facts: Sequence[Any | Mapping[str, Any]],
    prior_dossier: PersistedResearchDossier | Mapping[str, Any] | None = None,
    applied_event_ids: Sequence[str] = (),
    reopened_component_ids: Sequence[str] = (),
    research_status: str = DossierResearchStatus.FULL_THESIS_ACTIVE.value,
) -> PersistedResearchDossier:
    """Materialize one L5 dossier from the canonical Phase 84--95 leaves.

    This is an adapter, not a scoring shortcut.  It accepts only a completed
    Researcher dossier, certified research epoch, complete deterministic score,
    and FINAL StageCourt result whose identities and component vectors agree.
    """

    research = _object_mapping(research_dossier, "research dossier")
    epoch = _object_mapping(research_epoch_checkpoint, "research epoch checkpoint")
    score = _object_mapping(score_aggregation, "deterministic score aggregation")
    court = _object_mapping(stagecourt_run, "StageCourt run")
    facts = tuple(
        _object_mapping(row, "EvidenceFact") for row in evidence_facts
    )
    prior = _coerce_dossier(prior_dossier) if prior_dossier is not None else None
    applied = tuple(applied_event_ids)
    reopened = tuple(reopened_component_ids)
    _unique_text(applied, "dossier materialization applied events", required=False)
    _unique_text(reopened, "dossier materialization reopened components", required=False)
    if set(reopened) - set(CANONICAL_COMPONENT_ORDER):
        raise ValueError("dossier materialization contains unknown reopened component")

    target_id = str(research.get("target_id") or "")
    archetype_id = str(research.get("archetype_id") or "")
    as_of_date = str(research.get("as_of_date") or "")
    cutoff = date.fromisoformat(as_of_date)
    if not target_id or not archetype_id or not str(target_name).strip():
        raise ValueError("dossier materialization identity is required")
    if research.get("status") != "RESEARCH_MEMOS_COMPLETE" or research.get(
        "pending_reasons"
    ):
        raise ValueError("L5 dossier requires complete Researcher Mode memos")
    if (
        research.get("production_score_authority") is not False
        or research.get("final_stage_authority") is not False
    ):
        raise ValueError("Researcher memo layer cannot own score or Stage")

    business_result = _required_mapping(
        research.get("business_model_result"), "business-model result"
    )
    business_memo = _required_mapping(
        business_result.get("memo"), "business-model memo"
    )
    component_results = tuple(
        _mapping_rows(research.get("component_results"))
    )
    component_result_by_id = _unique_mapping(
        component_results, "component_id", "research component result"
    )
    if tuple(component_result_by_id) != tuple(CANONICAL_COMPONENT_ORDER):
        raise ValueError("research dossier lacks canonical seven-component order")
    component_memo_by_id: dict[str, Mapping[str, Any]] = {}
    for component_id in CANONICAL_COMPONENT_ORDER:
        result = component_result_by_id[component_id]
        memo = _required_mapping(result.get("memo"), "component research memo")
        if (
            result.get("status") != "COMPLETE"
            or result.get("pending_reasons")
            or memo.get("component_id") != component_id
            or memo.get("target_id") != target_id
            or memo.get("archetype_id") != archetype_id
            or memo.get("research_complete") is not True
        ):
            raise ValueError("component research memo is incomplete or out of scope")
        component_memo_by_id[component_id] = memo
    red_result = _required_mapping(research.get("red_team_result"), "red-team result")
    red_memo = _required_mapping(red_result.get("memo"), "red-team memo")
    synthesis_result = _required_mapping(
        research.get("synthesis_result"), "synthesis result"
    )
    synthesis_memo = _required_mapping(
        synthesis_result.get("memo"), "synthesis memo"
    )
    if (
        business_result.get("status") != "COMPLETE"
        or business_memo.get("research_complete") is not True
        or business_memo.get("target_id") != target_id
        or business_memo.get("archetype_id") != archetype_id
        or business_memo.get("as_of_date") != as_of_date
        or red_result.get("status") != "COMPLETE"
        or red_memo.get("review_complete") is not True
        or red_memo.get("target_id") != target_id
        or red_memo.get("archetype_id") != archetype_id
        or tuple(red_memo.get("reviewed_component_ids") or ())
        != tuple(CANONICAL_COMPONENT_ORDER)
        or synthesis_result.get("status") != "COMPLETE"
        or synthesis_memo.get("synthesis_complete") is not True
        or synthesis_memo.get("target_id") != target_id
        or synthesis_memo.get("archetype_id") != archetype_id
        or set(synthesis_memo.get("component_memo_ids") or ())
        != {
            str(component_memo_by_id[component_id].get("memo_id") or "")
            for component_id in CANONICAL_COMPONENT_ORDER
        }
        or synthesis_memo.get("unresolved_material_questions")
    ):
        raise ValueError("business/red-team/synthesis research is not L5-complete")

    certificate = _required_mapping(
        epoch.get("saturation_certificate"), "semantic saturation certificate"
    )
    saturation_rows = tuple(_mapping_rows(epoch.get("saturation_reviews")))
    saturation_roles = tuple(
        str(row.get("reviewer_role") or "") for row in saturation_rows
    )
    review_payloads = tuple(
        _required_mapping(row.get("review"), "semantic saturation review")
        for row in saturation_rows
    )
    review_ids = tuple(str(row.get("review_id") or "") for row in review_payloads)
    prompt_hashes = tuple(
        str(row.get("prompt_hash") or "") for row in review_payloads
    )
    if any(
        epoch.get(key) is not False
        for key in (
            "completion_based_on_fixed_rounds",
            "zero_search_result_treated_as_saturation",
            "transport_budget_treated_as_completion",
            "production_score_authority",
        )
    ) or (
        epoch.get("target_id") != target_id
        or epoch.get("as_of_date") != as_of_date
        or epoch.get("schema_version")
        != "e2r_research_epoch_checkpoint_v3"
        or epoch.get("status") != "SEMANTIC_SATURATION_CERTIFIED"
        or epoch.get("semantic_saturation_certified") is not True
        or epoch.get("gold_evaluation_status")
        != GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY
        or epoch.get("gold_critical_fact_miss_count") is not None
        or not str(epoch.get("checkpoint_id") or "").strip()
        or certificate.get("schema_version")
        != "e2r_semantic_saturation_certificate_v3"
        or certificate.get("status") != "CERTIFIED"
        or certificate.get("semantic_saturation_certified") is not True
        or certificate.get("checkpoint_id") != epoch.get("checkpoint_id")
        or certificate.get("provider_backed_reviews_required") is not True
        or certificate.get("gold_evaluation_status")
        != GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY
        or certificate.get("gold_critical_fact_miss_count") is not None
        or len(saturation_rows) != len(SATURATION_REVIEW_ROLES)
        or set(saturation_roles) != set(SATURATION_REVIEW_ROLES)
        or any(row.get("status") != "COMPLETE" for row in saturation_rows)
        or any(
            review.get("schema_version")
            != "e2r_semantic_saturation_review_v3"
            or review.get("approve") is not True
            or review.get("provider_backed") is not True
            or review.get("checkpoint_id") != epoch.get("checkpoint_id")
            or review.get("reviewer_role") != saturation_roles[index]
            or review.get("gold_evaluation_status")
            != GOLD_EVALUATION_NOT_RUN_POST_RUN_ONLY
            or review.get("gold_critical_fact_miss_count") is not None
            for index, review in enumerate(review_payloads)
        )
        or any(not value for value in review_ids)
        or any(not _sha256(value) for value in prompt_hashes)
        or len(set(review_ids)) != len(SATURATION_REVIEW_ROLES)
        or len(set(prompt_hashes)) != len(SATURATION_REVIEW_ROLES)
        or set(review_ids) != set(certificate.get("review_ids") or ())
        or set(prompt_hashes)
        != set(certificate.get("provider_prompt_hashes") or ())
    ):
        raise ValueError("L5 dossier requires a valid semantic saturation checkpoint")

    if (
        score.get("target_id") != target_id
        or score.get("archetype_id") != archetype_id
        or score.get("as_of_date") != as_of_date
        or score.get("status") != "DETERMINISTIC_SCORE_COMPLETE"
        or score.get("score_valid") is not True
        or score.get("ready_for_stagecourt") is not True
        or score.get("production_stage_authority") is not False
        or score.get("pending_reasons")
        or int(_required_mapping(score.get("audit"), "score aggregation audit").get(
            "critical_count_sum"
        ) or 0)
        != 0
    ):
        raise ValueError("L5 dossier requires complete deterministic score aggregation")
    total_result = _required_mapping(score.get("total_result"), "total score result")
    total_score = _required_mapping(total_result.get("score"), "deterministic total score")
    if total_result.get("status") != "COMPLETE" or total_result.get("pending_reasons"):
        raise ValueError("deterministic total score is pending")
    component_points = _required_mapping(
        total_score.get("component_points"), "component score vector"
    )
    component_decision_ids = _required_mapping(
        total_score.get("component_decision_ids"), "component decision ids"
    )
    if (
        set(component_points) != set(CANONICAL_COMPONENT_ORDER)
        or set(component_decision_ids) != set(CANONICAL_COMPONENT_ORDER)
        or total_score.get("score_valid") is not True
        or total_score.get("production_stage_authority") is not False
    ):
        raise ValueError("deterministic score lacks the canonical component vector")
    score_component_results = tuple(_mapping_rows(score.get("component_results")))
    score_result_by_id = _unique_mapping(
        score_component_results, "component_id", "score component result"
    )
    if set(score_result_by_id) != set(CANONICAL_COMPONENT_ORDER):
        raise ValueError("deterministic score lacks seven component decisions")

    decision = _required_mapping(court.get("decision"), "StageCourt decision")
    court_audit = _required_mapping(court.get("audit"), "StageCourt audit")
    if (
        decision.get("target_id") != target_id
        or decision.get("archetype_id") != archetype_id
        or decision.get("as_of_date") != as_of_date
        or decision.get("status") != "FINAL"
        or decision.get("score_valid") is not True
        or decision.get("research_complete") is not True
        or decision.get("counter_thesis_complete") is not True
        or decision.get("stage_gates_complete") is not True
        or decision.get("llm_stage_authority") is not False
        or decision.get("pending_reasons")
        or court.get("llm_stage_authority") is not False
        or int(court_audit.get("critical_count_sum") or 0) != 0
    ):
        raise ValueError("L5 dossier requires one final deterministic StageCourt result")
    total_points = float(total_score.get("total_points"))
    if (
        abs(float(decision.get("total_points")) - total_points) > 1e-9
        or dict(decision.get("component_vector") or {})
        != {key: float(value) for key, value in component_points.items()}
    ):
        raise ValueError("StageCourt and deterministic score vector disagree")
    canonical_stage = str(decision.get("canonical_stage") or "")
    CanonicalStage(canonical_stage)

    fact_by_id = _unique_mapping(facts, "fact_id", "dossier EvidenceFact")
    current_fact_ids = tuple(str(value) for value in epoch.get("current_fact_ids") or ())
    _unique_text(current_fact_ids, "epoch current fact ids", required=True)
    if set(current_fact_ids) != set(fact_by_id):
        raise ValueError("semantic checkpoint and current EvidenceFact roster disagree")
    dossier_facts: list[DossierFactLineage] = []
    for fact_id in current_fact_ids:
        fact = fact_by_id[fact_id]
        if (
            fact.get("target_id") != target_id
            or fact.get("as_of_date") != as_of_date
            or date.fromisoformat(str(fact.get("as_of_date"))) > cutoff
        ):
            raise ValueError("dossier EvidenceFact target/as_of scope mismatch")
        dossier_facts.append(
            DossierFactLineage(
                fact_id=fact_id,
                target_id=target_id,
                available_date=str(fact.get("as_of_date")),
                source_ids=tuple(str(value) for value in fact.get("source_ids") or ()),
                allowed_component_ids=tuple(
                    str(value) for value in fact.get("allowed_component_ids") or ()
                ),
                current_lifecycle=str(fact.get("current_lifecycle") or ""),
            )
        )

    score_fact_ids = set(str(value) for value in total_score.get("fact_ids") or ())
    score_fact_ids.update(
        str(value) for value in total_score.get("counter_fact_ids") or ()
    )
    score_fact_ids.update(
        str(value) for value in decision.get("score_fact_ids") or ()
    )
    if not score_fact_ids.issubset(fact_by_id):
        raise ValueError("deterministic score references a fact outside the dossier")
    prior_components = (
        {row.component_id: row for row in prior.components} if prior else {}
    )
    if prior is None and (applied or reopened):
        raise ValueError("initial dossier cannot claim delta event lineage")
    if prior is not None and (
        prior.target_id != target_id
        or prior.archetype_id != archetype_id
        or not applied
        or not reopened
    ):
        raise ValueError("dossier update requires prior scope and reopened event lineage")
    components: list[DossierComponentState] = []
    for component_id in CANONICAL_COMPONENT_ORDER:
        score_result = score_result_by_id.get(component_id)
        if score_result is None:
            raise ValueError("deterministic score component result is missing")
        score_decision = _required_mapping(
            score_result.get("decision"), "component score decision"
        )
        if (
            score_result.get("status") != "COMPLETE"
            or score_result.get("pending_reasons")
            or score_decision.get("component_id") != component_id
            or score_decision.get("research_complete") is not True
            or score_decision.get("production_stage_authority") is not False
            or abs(
                float(score_decision.get("final_points"))
                - float(component_points[component_id])
            )
            > 1e-9
        ):
            raise ValueError("deterministic component decision is incomplete or mismatched")
        memo = component_memo_by_id[component_id]
        memo_fact_ids = tuple(
            dict.fromkeys(
                str(value)
                for key in (
                    "positive_fact_ids",
                    "counter_fact_ids",
                    "resolution_fact_ids",
                    "context_fact_ids",
                )
                for value in memo.get(key) or ()
            )
        )
        component_fact_ids = tuple(
            dict.fromkeys(
                (
                    *memo_fact_ids,
                    *(str(value) for value in score_decision.get("fact_ids") or ()),
                    *(
                        str(value)
                        for value in score_decision.get("counter_fact_ids") or ()
                    ),
                )
            )
        )
        if not set(component_fact_ids).issubset(fact_by_id):
            raise ValueError("component memo/decision references an unknown fact")
        fresh = DossierComponentState(
            component_id=component_id,
            status=DossierComponentStatus.CURRENT.value,
            memo_id=str(memo.get("memo_id") or ""),
            memo_hash=stable_hash(memo),
            decision_id=str(component_decision_ids[component_id]),
            fact_ids=component_fact_ids,
            final_points=float(component_points[component_id]),
            reviewed_event_ids=applied if component_id in reopened else (),
        )
        if prior is not None and component_id not in reopened:
            old = prior_components.get(component_id)
            if old is None or (
                old.decision_id != fresh.decision_id
                or old.final_points != fresh.final_points
            ):
                raise ValueError("unreopened component score changed in canonical outputs")
            components.append(old)
        else:
            components.append(fresh)

    version = 1 if prior is None else prior.version + 1
    identity = {
        "target_id": target_id,
        "archetype_id": archetype_id,
        "as_of_date": as_of_date,
        "version": version,
        "previous_dossier_id": prior.dossier_id if prior else None,
        "checkpoint_id": epoch["checkpoint_id"],
        "score_decision_id": decision.get("decision_id"),
        "applied_event_ids": list(applied),
    }
    return PersistedResearchDossier(
        dossier_id="DOSSIER-" + stable_hash(identity)[:24],
        target_id=target_id,
        target_name=str(target_name),
        archetype_id=archetype_id,
        as_of_date=as_of_date,
        version=version,
        previous_dossier_id=prior.dossier_id if prior else None,
        status=research_status,
        research_epoch_checkpoint_id=str(epoch["checkpoint_id"]),
        semantic_saturation_certified=True,
        facts=tuple(dossier_facts),
        components=tuple(components),
        business_model_memo_hash=stable_hash(business_memo),
        red_team_memo_hash=stable_hash(red_memo),
        synthesis_memo_hash=stable_hash(synthesis_memo),
        score_decision_id=str(decision.get("decision_id") or ""),
        score_value=total_points,
        canonical_stage=canonical_stage,
        score_valid=True,
        applied_event_ids=applied,
    )


def _build_delta_plan(
    *,
    as_of_date: str,
    prior: PersistedResearchDossier,
    events: tuple[DailyDossierEvent, ...],
    completed_update: PersistedResearchDossier | None,
) -> DossierDeltaPlan:
    prior_fact_by_id = {row.fact_id: row for row in prior.facts}
    component_by_fact: dict[str, set[str]] = {}
    for component in prior.components:
        for fact_id in component.fact_ids:
            component_by_fact.setdefault(fact_id, set()).add(component.component_id)
    new_fact_by_id: dict[str, DossierFactLineage] = {}
    revised_ids: set[str] = set()
    retired_ids: set[str] = set()
    global_impact = False
    event_ids = tuple(row.event_id for row in events)
    pending: list[str] = []
    for event in events:
        global_impact = global_impact or event.global_business_model_impact
        for fact in event.new_facts:
            if fact.fact_id in prior_fact_by_id or fact.fact_id in new_fact_by_id:
                pending.append(f"DUPLICATE_NEW_FACT:{fact.fact_id}")
            new_fact_by_id[fact.fact_id] = fact
        revised_ids.update(event.revised_fact_ids)
        retired_ids.update(event.retired_fact_ids)
    for fact_id in sorted(revised_ids | retired_ids):
        if fact_id not in prior_fact_by_id:
            pending.append(f"UNKNOWN_PRIOR_FACT:{fact_id}")
    changed_ids = set(new_fact_by_id) | revised_ids | retired_ids
    impacted: set[str] = set(CANONICAL_COMPONENT_ORDER) if global_impact else set()
    unmapped: list[str] = []
    if not global_impact:
        for fact_id in sorted(changed_ids):
            fact = new_fact_by_id.get(fact_id) or prior_fact_by_id.get(fact_id)
            linked = set(component_by_fact.get(fact_id, ()))
            if fact is not None:
                linked.update(fact.allowed_component_ids)
            if not linked:
                unmapped.append(fact_id)
            impacted.update(linked)
    if not changed_ids and not global_impact:
        pending.append("EVENT_FACT_EXTRACTION_REQUIRED")
    pending.extend(f"FACT_COMPONENT_IMPACT_MAPPING_REQUIRED:{value}" for value in unmapped)
    impacted &= set(CANONICAL_COMPONENT_ORDER)
    status = (
        "FACT_IMPACT_MAPPING_PENDING"
        if pending or not impacted
        else "DELTA_RESEARCH_REQUIRED"
    )
    if status == "FACT_IMPACT_MAPPING_PENDING":
        impacted = set()
    reopened = tuple(
        component_id
        for component_id in CANONICAL_COMPONENT_ORDER
        if component_id in impacted
    )
    reused = tuple(
        component_id
        for component_id in CANONICAL_COMPONENT_ORDER
        if component_id not in impacted
    )
    objectives = tuple(
        {
            "component_id": component_id,
            "reason_fact_ids": sorted(
                fact_id
                for fact_id in changed_ids
                if component_id
                in (
                    set(component_by_fact.get(fact_id, ()))
                    | set(
                        (
                            new_fact_by_id.get(fact_id)
                            or prior_fact_by_id.get(fact_id)
                        ).allowed_component_ids
                        if (new_fact_by_id.get(fact_id) or prior_fact_by_id.get(fact_id))
                        else ()
                    )
                )
            ),
            "reason_event_ids": list(event_ids),
            "query_generation_authority": "LLM_RESEARCH_SUPERVISOR",
            "literal_query": None,
            "official_first": True,
            "general_web_requires_official_gap": True,
            "checkpoint_bounded": True,
            "transport_budget_is_completion": False,
        }
        for component_id in reopened
    )
    new_score = None
    new_stage = None
    score_delta = None
    if completed_update is not None and status == "DELTA_RESEARCH_REQUIRED":
        _validate_completed_delta(
            prior=prior,
            update=completed_update,
            events=events,
            event_ids=event_ids,
            reopened_component_ids=reopened,
            reused_component_ids=reused,
        )
        status = "DELTA_APPLIED"
        pending = []
        new_score = completed_update.score_value
        new_stage = completed_update.canonical_stage
        if prior.score_value is not None and new_score is not None:
            score_delta = round(float(new_score) - float(prior.score_value), 10)
    elif status == "DELTA_RESEARCH_REQUIRED":
        pending.append("REOPENED_COMPONENT_RESEARCH_AND_JUDGMENT_REQUIRED")
        pending.append("DETERMINISTIC_RESCORE_AND_STAGECOURT_REQUIRED")
    payload = {
        "target_id": prior.target_id,
        "as_of_date": as_of_date,
        "prior_dossier_id": prior.dossier_id,
        "event_ids": list(event_ids),
        "changed_fact_ids": sorted(changed_ids),
        "reopened_component_ids": list(reopened),
    }
    return DossierDeltaPlan(
        delta_id="DDELTA-" + stable_hash(payload)[:24],
        target_id=prior.target_id,
        as_of_date=as_of_date,
        prior_dossier_id=prior.dossier_id,
        event_ids=event_ids,
        status=status,
        changed_fact_ids=tuple(sorted(changed_ids)),
        retired_fact_ids=tuple(sorted(retired_ids)),
        reopened_component_ids=reopened,
        reused_component_ids=reused,
        source_refresh_objectives=objectives,
        component_rejudge_ids=reopened,
        red_team_reopen=bool(reopened),
        synthesis_reopen=bool(reopened),
        deterministic_rescore_required=bool(reopened),
        prior_score_value=prior.score_value if prior.score_valid else None,
        prior_canonical_stage=prior.canonical_stage if prior.score_valid else None,
        new_score_value=new_score,
        new_canonical_stage=new_stage,
        score_delta=score_delta,
        pending_reasons=tuple(dict.fromkeys(pending)),
    )


def _validate_completed_delta(
    *,
    prior: PersistedResearchDossier,
    update: PersistedResearchDossier,
    events: tuple[DailyDossierEvent, ...],
    event_ids: tuple[str, ...],
    reopened_component_ids: tuple[str, ...],
    reused_component_ids: tuple[str, ...],
) -> None:
    if (
        update.target_id != prior.target_id
        or update.version != prior.version + 1
        or update.previous_dossier_id != prior.dossier_id
        or update.status != DossierResearchStatus.FULL_THESIS_ACTIVE.value
        or not set(event_ids).issubset(update.applied_event_ids)
    ):
        raise ValueError("completed dossier delta has invalid version/event lineage")
    if date.fromisoformat(update.as_of_date) < max(
        date.fromisoformat(row.available_date) for row in events
    ):
        raise ValueError("completed dossier predates its applied event")
    updated_fact_by_id = {row.fact_id: row for row in update.facts}
    new_fact_ids = {
        fact.fact_id for event in events for fact in event.new_facts
    }
    revised_fact_ids = {
        fact_id for event in events for fact_id in event.revised_fact_ids
    }
    retired_fact_ids = {
        fact_id for event in events for fact_id in event.retired_fact_ids
    }
    if not (new_fact_ids | revised_fact_ids).issubset(updated_fact_by_id):
        raise ValueError("completed dossier omitted a new or revised fact")
    if any(
        updated_fact_by_id[fact_id].current_lifecycle
        not in {EvidenceLifecycle.CURRENT.value, EvidenceLifecycle.OPEN.value}
        for fact_id in new_fact_ids | revised_fact_ids
    ):
        raise ValueError("new or revised delta fact is not current")
    if any(
        fact_id in updated_fact_by_id
        and updated_fact_by_id[fact_id].current_lifecycle
        != EvidenceLifecycle.SUPERSEDED.value
        for fact_id in retired_fact_ids
    ):
        raise ValueError("retired delta fact remains current in completed dossier")
    prior_components = {row.component_id: row for row in prior.components}
    updated_components = {row.component_id: row for row in update.components}
    for component_id in reused_component_ids:
        before = prior_components.get(component_id)
        after = updated_components.get(component_id)
        if before is None or after is None or (
            before.memo_id,
            before.memo_hash,
            before.decision_id,
            before.final_points,
        ) != (
            after.memo_id,
            after.memo_hash,
            after.decision_id,
            after.final_points,
        ):
            raise ValueError("unaffected component changed during delta update")
    for component_id in reopened_component_ids:
        after = updated_components.get(component_id)
        if after is None or not set(event_ids).issubset(after.reviewed_event_ids):
            raise ValueError("reopened component lacks event review lineage")
        if set(after.fact_ids) & retired_fact_ids:
            raise ValueError("reopened component still uses a retired fact")


def _build_census_row(
    *,
    member: Mapping[str, Any],
    status: Mapping[str, Any],
    depth: Mapping[str, Any],
    as_of_date: str,
    candidate: bool,
    events: tuple[DailyDossierEvent, ...],
    stored: PersistedResearchDossier | None,
    completed: PersistedResearchDossier | None,
    delta_plan: DossierDeltaPlan | None,
) -> DailyResearcherCensusRow:
    target_id = str(member.get("target_id") or "")
    target_name = str(member.get("target_name") or target_id)
    maximum_depth = str(depth.get("maximum_depth") or "")
    terminal = str(status.get("terminal_status") or "")
    pending = [str(value) for value in status.get("provider_gaps") or ()]
    pending.extend(str(value) for value in status.get("source_gaps") or ())
    pending.extend(str(value) for value in status.get("missing_conditions") or ())
    effective = completed or stored
    dossier_id = effective.dossier_id if effective else None
    dossier_version = effective.version if effective else None
    current_score = None
    current_stage = None
    raw_reference = _optional_float(status.get("raw_reference_score"))
    score_display = ScoreDisplayStatus.NO_CURRENT_SCORE

    if completed is not None and completed.score_valid:
        current_score = completed.score_value
        current_stage = completed.canonical_stage
        score_display = ScoreDisplayStatus.CURRENT_DETERMINISTIC
    elif delta_plan is not None and stored is not None and stored.score_valid:
        current_score = stored.score_value
        current_stage = stored.canonical_stage
        score_display = ScoreDisplayStatus.LAST_EFFECTIVE_PENDING_DELTA
    elif status.get("score_valid") is True and status.get("score_finalization_allowed") is True:
        current_score = _optional_float(status.get("score_value"))
        current_stage = str(status.get("canonical_stage") or "") or None
        score_display = ScoreDisplayStatus.CURRENT_DETERMINISTIC
    elif stored is not None and stored.score_valid:
        current_score = stored.score_value
        current_stage = stored.canonical_stage
        score_display = ScoreDisplayStatus.LAST_EFFECTIVE
    elif raw_reference is not None:
        score_display = ScoreDisplayStatus.RAW_REFERENCE_ONLY
        if str(status.get("canonical_stage") or "") == CanonicalStage.STAGE_1.value:
            current_stage = CanonicalStage.STAGE_1.value
    elif str(status.get("canonical_stage") or "") == CanonicalStage.STAGE_1.value:
        current_stage = CanonicalStage.STAGE_1.value

    if delta_plan is not None:
        if delta_plan.status == "FACT_IMPACT_MAPPING_PENDING":
            thesis = FullThesisStatus.FACT_IMPACT_MAPPING_PENDING
        elif delta_plan.status == "DELTA_APPLIED":
            thesis = FullThesisStatus.FULL_THESIS_CURRENT
        else:
            thesis = FullThesisStatus.DELTA_RESEARCH_REQUIRED
        pending.extend(delta_plan.pending_reasons)
    elif terminal == DailyTerminalStatus.PROVIDER_PENDING.value:
        thesis = FullThesisStatus.PROVIDER_PENDING
    elif terminal == DailyTerminalStatus.SOURCE_PENDING.value:
        thesis = FullThesisStatus.SOURCE_PENDING
    elif terminal == DailyTerminalStatus.BUDGET_PENDING.value:
        thesis = FullThesisStatus.BUDGET_CHECKPOINT_PENDING
    elif effective is not None and effective.status == DossierResearchStatus.FULL_THESIS_ACTIVE.value:
        thesis = (
            FullThesisStatus.FULL_THESIS_CURRENT
            if completed is not None
            else FullThesisStatus.FULL_THESIS_REUSED
        )
    elif effective is not None and effective.status == DossierResearchStatus.DISPROVED.value:
        thesis = FullThesisStatus.DISPROVED
    elif terminal == DailyTerminalStatus.FULL_THESIS.value:
        # A daily label alone is insufficient: a persisted semantically saturated
        # dossier is the L5 proof.
        thesis = FullThesisStatus.FULL_RESEARCH_REQUIRED
        pending.append("PERSISTED_SEMANTIC_DOSSIER_REQUIRED")
    elif candidate or any(
        row.material or row.global_business_model_impact for row in events
    ):
        thesis = FullThesisStatus.FULL_RESEARCH_REQUIRED
        pending.append("RESEARCHER_MODE_DOSSIER_REQUIRED")
    else:
        thesis = FullThesisStatus.NOT_OPEN

    if thesis in {
        FullThesisStatus.PROVIDER_PENDING,
        FullThesisStatus.SOURCE_PENDING,
        FullThesisStatus.BUDGET_CHECKPOINT_PENDING,
    } and not pending:
        pending.append(f"{terminal}:EXACT_RUNTIME_REASON_REQUIRED")
    event_ids = tuple(row.event_id for row in events)
    candidate_id = (
        "RCAND-"
        + stable_hash(
            {
                "target_id": target_id,
                "as_of_date": as_of_date,
                "maximum_depth": maximum_depth,
            }
        )[:24]
        if candidate
        else None
    )
    next_action = _next_action(thesis)
    identity = {
        "target_id": target_id,
        "as_of_date": as_of_date,
        "maximum_depth": maximum_depth,
        "event_ids": list(event_ids),
        "dossier_id": dossier_id,
        "full_thesis_status": thesis.value,
    }
    return DailyResearcherCensusRow(
        assessment_id="DASSESS-" + stable_hash(identity)[:24],
        target_id=target_id,
        target_name=target_name,
        as_of_date=as_of_date,
        maximum_depth=maximum_depth,
        daily_assessment_event_ids=event_ids,
        researcher_candidate=candidate,
        researcher_candidate_id=candidate_id,
        dossier_id=dossier_id,
        dossier_version=dossier_version,
        current_score=current_score,
        raw_reference_score=raw_reference,
        current_stage=current_stage,
        score_display_status=score_display.value,
        full_thesis_status=thesis.value,
        pending_reasons=tuple(dict.fromkeys(value for value in pending if value)),
        next_action=next_action,
    )


def _next_action(status: FullThesisStatus) -> str:
    return {
        FullThesisStatus.NOT_OPEN: "OBSERVE_DAILY_ASSESSMENT",
        FullThesisStatus.FULL_RESEARCH_REQUIRED: "OPEN_RESEARCHER_MODE",
        FullThesisStatus.DELTA_RESEARCH_REQUIRED: "REFRESH_AFFECTED_COMPONENTS",
        FullThesisStatus.FACT_IMPACT_MAPPING_PENDING: "COMPLETE_FACT_IMPACT_MAPPING",
        FullThesisStatus.SOURCE_PENDING: "RETRY_OFFICIAL_SOURCE",
        FullThesisStatus.PROVIDER_PENDING: "RETRY_RESEARCH_PROVIDER",
        FullThesisStatus.BUDGET_CHECKPOINT_PENDING: "RESUME_NEXT_BOUNDED_CHECKPOINT",
        FullThesisStatus.FULL_THESIS_CURRENT: "MONITOR_NEXT_EARNINGS_AND_BACKLOG",
        FullThesisStatus.FULL_THESIS_REUSED: "MONITOR_FOR_MATERIAL_DELTA",
        FullThesisStatus.DISPROVED: "MONITOR_COUNTER_THESIS",
    }[status]


def audit_daily_census_integration(payload: Mapping[str, Any]) -> Mapping[str, Any]:
    rows = tuple(_mapping_rows(payload.get("rows")))
    deltas = tuple(_mapping_rows(payload.get("delta_plans")))
    dossiers = tuple(_mapping_rows(payload.get("dossiers")))
    source_tasks = tuple(_mapping_rows(payload.get("daily_source_tasks")))
    executions = tuple(_mapping_rows(payload.get("daily_deep_executions")))
    row_targets = [str(row.get("target_id") or "") for row in rows]
    dossier_by_id = {
        str(row.get("dossier_id") or ""): row
        for row in dossiers
        if row.get("dossier_id")
    }
    pending_labels = {
        FullThesisStatus.SOURCE_PENDING.value,
        FullThesisStatus.PROVIDER_PENDING.value,
        FullThesisStatus.BUDGET_CHECKPOINT_PENDING.value,
        FullThesisStatus.FACT_IMPACT_MAPPING_PENDING.value,
    }
    critical_counts = {
        "duplicate_or_empty_census_target_count": (
            len(row_targets) - len(set(row_targets)) + sum(not value for value in row_targets)
        ),
        "deep_without_researcher_candidate_count": sum(
            str(row.get("maximum_depth") or "") in _DEEP_DEPTHS
            and row.get("researcher_candidate") is not True
            for row in rows
        ),
        "candidate_without_id_count": sum(
            bool(row.get("researcher_candidate")) != bool(row.get("researcher_candidate_id"))
            for row in rows
        ),
        "pending_without_reason_count": sum(
            row.get("full_thesis_status") in pending_labels
            and not row.get("pending_reasons")
            for row in rows
        ),
        "pending_fabricated_stage0_count": sum(
            row.get("full_thesis_status") in pending_labels
            and row.get("current_stage") == CanonicalStage.STAGE_0.value
            and row.get("score_display_status")
            != ScoreDisplayStatus.LAST_EFFECTIVE_PENDING_DELTA.value
            for row in rows
        ),
        "l5_without_semantic_dossier_count": sum(
            row.get("full_thesis_status")
            in {
                FullThesisStatus.FULL_THESIS_CURRENT.value,
                FullThesisStatus.FULL_THESIS_REUSED.value,
            }
            and (
                not row.get("dossier_id")
                or not dossier_by_id.get(str(row.get("dossier_id")))
                or dossier_by_id[str(row.get("dossier_id"))].get(
                    "semantic_saturation_certified"
                )
                is not True
            )
            for row in rows
        ),
        "budget_treated_as_full_thesis_count": sum(
            execution.get("outcome") == CurrentDeepOutcome.BUDGET_PENDING.value
            and any(
                row.get("target_id") == execution.get("target_id")
                and row.get("full_thesis_status")
                in {
                    FullThesisStatus.FULL_THESIS_CURRENT.value,
                    FullThesisStatus.FULL_THESIS_REUSED.value,
                }
                for row in rows
            )
            for execution in executions
        ),
        "source_task_unbounded_or_no_stop_count": sum(
            any(
                isinstance(task.get(key), bool)
                or not isinstance(task.get(key), int)
                or int(task.get(key)) <= 0
                for key in ("max_queries", "max_candidates", "max_fetches")
            )
            or task.get("stop_condition") != "stop_on_resolution"
            for task in source_tasks
        ),
        "general_web_without_official_gap_count": sum(
            task.get("allows_general_web") is True
            and (
                task.get("official_first_attempted") is not True
                or not task.get("official_gap_reasons")
            )
            for task in source_tasks
        ),
        "delta_component_partition_mismatch_count": sum(
            bool(
                set(delta.get("reopened_component_ids") or ())
                & set(delta.get("reused_component_ids") or ())
            )
            or (
                set(delta.get("reopened_component_ids") or ())
                | set(delta.get("reused_component_ids") or ())
                != set(CANONICAL_COMPONENT_ORDER)
            )
            for delta in deltas
        ),
        "delta_query_or_llm_authority_count": sum(
            delta.get("query_generation_authority")
            != "LLM_RESEARCH_SUPERVISOR"
            or delta.get("deterministic_query_synthesis") is not False
            or delta.get("llm_score_authority") is not False
            or delta.get("llm_stage_authority") is not False
            or any(
                objective.get("literal_query") is not None
                for objective in _mapping_rows(delta.get("source_refresh_objectives"))
            )
            for delta in deltas
        ),
        "pending_delta_with_score_count": sum(
            delta.get("status") != "DELTA_APPLIED"
            and any(
                delta.get(key) is not None
                for key in ("new_score_value", "new_canonical_stage", "score_delta")
            )
            for delta in deltas
        ),
        "dossier_nondeterministic_authority_count": sum(
            dossier.get("score_authority") != "DETERMINISTIC_SCORE_AGGREGATOR"
            or dossier.get("stage_authority") != "DETERMINISTIC_STAGECOURT"
            for dossier in dossiers
        ),
        "direct_investment_recommendation_count": sum(
            row.get("direct_investment_recommendation") is not False for row in rows
        ),
    }
    critical_sum = sum(int(value) for value in critical_counts.values())
    return _json_safe({
        "schema_version": "e2r_v5_daily_census_integration_audit_v1",
        "status": (
            "DAILY_CENSUS_INTEGRATION_AUDIT_PASS"
            if critical_sum == 0
            else "DAILY_CENSUS_INTEGRATION_AUDIT_FAIL"
        ),
        "as_of_date": payload.get("as_of_date"),
        "daily_run_id": payload.get("daily_run_id"),
        "full_universe_assessment_count": len(rows),
        "researcher_candidate_count": sum(
            row.get("researcher_candidate") is True for row in rows
        ),
        "persisted_dossier_count": len(dossiers),
        "delta_plan_count": len(deltas),
        "selective_deep": True,
        "dossier_persistence": True,
        "delta_component_reopen": True,
        "transport_budget_is_semantic_completion": False,
        "query_generation_authority": "LLM_RESEARCH_SUPERVISOR",
        "score_authority": "DETERMINISTIC_SCORE_AGGREGATOR",
        "stage_authority": "DETERMINISTIC_STAGECOURT",
        "critical_counts": critical_counts,
        "critical_count_sum": critical_sum,
    })


class ResearchDossierStore:
    """Small versioned filesystem store for production dossier snapshots."""

    def __init__(self, root: str | Path) -> None:
        self.root = Path(root)

    def save(self, dossier: PersistedResearchDossier) -> Mapping[str, Path]:
        target_key = stable_hash({"target_id": dossier.target_id})[:24]
        target_root = self.root / "targets" / target_key
        latest_path = target_root / "latest.json"
        existing = self.load_latest(dossier.target_id)
        if existing is None:
            if dossier.version != 1 or dossier.previous_dossier_id is not None:
                raise ValueError("new dossier store lineage must start at version 1")
        elif dossier.dossier_id == existing.dossier_id:
            return {
                "version": target_root / "versions" / f"{dossier.version:06d}-{dossier.dossier_id}.json",
                "latest": latest_path,
            }
        elif (
            dossier.version != existing.version + 1
            or dossier.previous_dossier_id != existing.dossier_id
        ):
            raise ValueError("dossier store rejects a non-contiguous update")
        version_path = (
            target_root
            / "versions"
            / f"{dossier.version:06d}-{dossier.dossier_id}.json"
        )
        write_json(version_path, dossier.to_dict())
        write_json(
            latest_path,
            {
                "schema_version": "e2r_v5_dossier_latest_pointer_v1",
                "target_id": dossier.target_id,
                "dossier_id": dossier.dossier_id,
                "version": dossier.version,
                "version_path": str(version_path.relative_to(self.root)),
            },
        )
        return {"version": version_path, "latest": latest_path}

    def load_latest(self, target_id: str) -> PersistedResearchDossier | None:
        target_key = stable_hash({"target_id": target_id})[:24]
        pointer_path = self.root / "targets" / target_key / "latest.json"
        if not pointer_path.is_file():
            return None
        pointer = json.loads(pointer_path.read_text(encoding="utf-8"))
        if pointer.get("target_id") != target_id:
            raise ValueError("dossier latest pointer target mismatch")
        version_path = self.root / str(pointer.get("version_path") or "")
        if not version_path.is_file():
            raise ValueError("dossier latest pointer references a missing version")
        dossier = _coerce_dossier(json.loads(version_path.read_text(encoding="utf-8")))
        if dossier.dossier_id != pointer.get("dossier_id"):
            raise ValueError("dossier latest pointer identity mismatch")
        return dossier


def write_daily_census_researcher_integration(
    result: DailyCensusResearcherIntegrationResult,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root)
    paths = {
        "manifest": root / "daily_census_researcher_integration.json",
        "rows": root / "daily_researcher_census.jsonl",
        "deltas": root / "dossier_delta_plans.jsonl",
        "dossiers": root / "dossier_snapshots.jsonl",
        "audit": root / "daily_census_researcher_integration_audit.json",
    }
    write_json(paths["manifest"], result.to_dict())
    write_jsonl(paths["rows"], (row.to_dict() for row in result.rows))
    write_jsonl(paths["deltas"], (row.to_dict() for row in result.delta_plans))
    write_jsonl(paths["dossiers"], (row.to_dict() for row in result.dossiers))
    write_json(paths["audit"], result.audit)
    return paths


def compile_phase97_daily_census_integration_audit() -> Mapping[str, Any]:
    """Build a deterministic structural proof for the Phase 97 contract."""

    as_of_date = "2026-07-13"
    prior = _audit_fixture_dossier(as_of_date="2026-07-12")
    event_fact = DossierFactLineage(
        fact_id="FACT-DELTA-CONTRACT",
        target_id=prior.target_id,
        available_date=as_of_date,
        source_ids=("DOC-DELTA-CONTRACT",),
        allowed_component_ids=("earnings_visibility",),
    )
    event = DailyDossierEvent(
        event_id="EVENT-DELTA-CONTRACT",
        target_id=prior.target_id,
        event_date=as_of_date,
        available_date=as_of_date,
        source_document_ids=("DOC-DELTA-CONTRACT",),
        new_facts=(event_fact,),
        impact_mapping_ids=("MAP-DELTA-CONTRACT",),
    )
    daily = _audit_fixture_daily(as_of_date=as_of_date, target_id=prior.target_id)
    result = integrate_daily_census_researcher_mode(
        daily,
        persisted_dossiers=(prior,),
        new_events=(event,),
    )
    delta = result.delta_plans[0]
    phase_critical = {
        "full_universe_row_mismatch_count": int(len(result.rows) != 3),
        "selective_deep_mismatch_count": int(
            sum(row.researcher_candidate for row in result.rows) != 2
            or sum(row.researcher_candidate for row in result.rows)
            >= len(result.rows)
        ),
        "delta_reopen_scope_mismatch_count": int(
            delta.reopened_component_ids != ("earnings_visibility",)
            or len(delta.reused_component_ids) != 6
        ),
        "transport_cap_completed_l5_count": int(
            result.rows[2].full_thesis_status
            != FullThesisStatus.BUDGET_CHECKPOINT_PENDING.value
        ),
        "query_authority_mismatch_count": int(
            delta.query_generation_authority != "LLM_RESEARCH_SUPERVISOR"
            or any(row.get("literal_query") is not None for row in delta.source_refresh_objectives)
        ),
        "score_or_stage_authority_leak_count": int(
            delta.new_score_value is not None
            or delta.new_canonical_stage is not None
            or delta.score_delta is not None
        ),
        "integration_audit_critical_count": int(result.audit["critical_count_sum"]),
    }
    phase_sum = sum(phase_critical.values())
    return _json_safe({
        "schema_version": "e2r_v5_phase97_daily_census_integration_audit_v1",
        "status": (
            DAILY_CENSUS_INTEGRATION_PASS
            if phase_sum == 0
            else DAILY_CENSUS_INTEGRATION_FAIL
        ),
        "as_of_date": as_of_date,
        "operational_model": {
            "L0": "full universe membership",
            "L1": "full universe cheap baseline",
            "L2": "bounded official light",
            "L3": "selected Researcher Mode planning",
            "L4": "bounded official-first Source Graph acquisition checkpoint",
            "L5": "semantic-saturation-certified full research dossier",
        },
        "daily_census_rows": [row.to_dict() for row in result.rows],
        "delta_example": delta.to_dict(),
        "dossier_persistence_contract": {
            "versioned": True,
            "contiguous_previous_dossier_lineage_required": True,
            "unchanged_component_memos_reused": True,
            "affected_component_memos_reopened": True,
            "score_delta_after_deterministic_rescore_only": True,
        },
        "canonical_l5_materialization_contract": {
            "required_leaves": [
                "RESEARCH_MEMOS_COMPLETE",
                "SEMANTIC_SATURATION_CERTIFIED_WITH_THREE_PROVIDER_REVIEWS",
                "DETERMINISTIC_SCORE_COMPLETE",
                "FINAL_DETERMINISTIC_STAGECOURT",
            ],
            "target_archetype_as_of_must_match": True,
            "seven_component_vector_must_reconcile": True,
            "current_fact_roster_must_match_checkpoint": True,
            "fixed_round_zero_result_or_transport_completion_allowed": False,
        },
        "production_safety": {
            "official_first": True,
            "general_web_requires_recorded_official_gap": True,
            "source_tasks_bounded_per_checkpoint": True,
            "arbitrary_cap_can_complete_l5": False,
            "provider_or_source_failure_becomes_low_score": False,
            "literal_query_generation_authority": "LLM_RESEARCH_SUPERVISOR",
            "score_authority": "DETERMINISTIC_SCORE_AGGREGATOR",
            "stage_authority": "DETERMINISTIC_STAGECOURT",
        },
        "critical_counts": phase_critical,
        "critical_count_sum": phase_sum,
    })


def write_phase97_daily_census_integration_audit(
    payload: Mapping[str, Any],
    output_path: str | Path = DEFAULT_DAILY_CENSUS_INTEGRATION_OUTPUT_PATH,
) -> Path:
    path = Path(output_path)
    write_json(path, payload)
    return path


def _audit_fixture_dossier(*, as_of_date: str) -> PersistedResearchDossier:
    target_id = "PHASE97-TARGET-A"
    facts = tuple(
        DossierFactLineage(
            fact_id=f"FACT-{component_id}",
            target_id=target_id,
            available_date=as_of_date,
            source_ids=(f"DOC-{component_id}",),
            allowed_component_ids=(component_id,),
        )
        for component_id in CANONICAL_COMPONENT_ORDER
    )
    components = tuple(
        DossierComponentState(
            component_id=component_id,
            status=DossierComponentStatus.CURRENT.value,
            memo_id=f"MEMO-{component_id}",
            memo_hash=stable_hash({"component_id": component_id}),
            decision_id=f"DECISION-{component_id}",
            fact_ids=(f"FACT-{component_id}",),
            final_points=10.0,
        )
        for component_id in CANONICAL_COMPONENT_ORDER
    )
    identity = {"target_id": target_id, "as_of_date": as_of_date, "version": 1}
    return PersistedResearchDossier(
        dossier_id="DOSSIER-" + stable_hash(identity)[:24],
        target_id=target_id,
        target_name="Phase 97 Target A",
        archetype_id="GENERIC_ARCHETYPE_CONTRACT",
        as_of_date=as_of_date,
        version=1,
        previous_dossier_id=None,
        status=DossierResearchStatus.FULL_THESIS_ACTIVE.value,
        research_epoch_checkpoint_id="REPOCH-PHASE97-A",
        semantic_saturation_certified=True,
        facts=facts,
        components=components,
        business_model_memo_hash=stable_hash("business"),
        red_team_memo_hash=stable_hash("red-team"),
        synthesis_memo_hash=stable_hash("synthesis"),
        score_decision_id="SCORE-PHASE97-A",
        score_value=70.0,
        canonical_stage=CanonicalStage.STAGE_2.value,
        score_valid=True,
    )


def _audit_fixture_daily(*, as_of_date: str, target_id: str) -> Mapping[str, Any]:
    targets = (target_id, "PHASE97-TARGET-B", "PHASE97-TARGET-C")
    maximums = (
        CensusDepthLevel.L3_RESEARCH_BRAIN.value,
        CensusDepthLevel.L1_BASELINE.value,
        CensusDepthLevel.L4_ACQUISITION.value,
    )
    terminals = (
        DailyTerminalStatus.OFFICIAL_LIGHT.value,
        DailyTerminalStatus.BASELINE_ONLY.value,
        DailyTerminalStatus.BUDGET_PENDING.value,
    )
    universe = [
        {
            "target_id": value,
            "target_name": f"Target {index}",
            "market": "KOSPI",
            "as_of_date": as_of_date,
            "eligible": True,
        }
        for index, value in enumerate(targets)
    ]
    depths = [
        {
            "target_id": value,
            "maximum_depth": maximums[index],
            "completed_depths": list(tuple(CensusDepthLevel)[: tuple(CensusDepthLevel).index(CensusDepthLevel(maximums[index])) + 1]),
            "selected_for_deep": index in {0, 2},
        }
        for index, value in enumerate(targets)
    ]
    # Enum values above must be serialized, not Enum objects.
    for row in depths:
        row["completed_depths"] = [value.value for value in row["completed_depths"]]
    statuses = [
        {
            "target_id": value,
            "target_name": f"Target {index}",
            "as_of_date": as_of_date,
            "maximum_depth": maximums[index],
            "terminal_status": terminals[index],
            "canonical_stage": CanonicalStage.STAGE_0.value,
            "score_valid": False,
            "score_finalization_allowed": False,
            "score_value": None,
            "raw_reference_score": None,
            "provider_gaps": [],
            "source_gaps": [],
            "missing_conditions": (
                ["bounded_checkpoint_exhausted"] if index == 2 else []
            ),
        }
        for index, value in enumerate(targets)
    ]
    return {
        "schema_version": "phase97_fixture_daily_v1",
        "integration_fixture_id": "PHASE97-FIXTURE-DAILY",
        "as_of_date": as_of_date,
        "universe": universe,
        "depth_decisions": depths,
        "stage_statuses": statuses,
        "source_tasks": [],
        "deep_executions": [
            {
                "target_id": targets[2],
                "outcome": CurrentDeepOutcome.BUDGET_PENDING.value,
            }
        ],
    }


def _coerce_dossier(
    value: PersistedResearchDossier | Mapping[str, Any],
) -> PersistedResearchDossier:
    if isinstance(value, PersistedResearchDossier):
        return value
    payload = dict(value)
    payload["facts"] = tuple(
        row if isinstance(row, DossierFactLineage) else DossierFactLineage(**row)
        for row in _mapping_rows(payload.get("facts"))
    )
    payload["components"] = tuple(
        row if isinstance(row, DossierComponentState) else DossierComponentState(**row)
        for row in _mapping_rows(payload.get("components"))
    )
    for key in ("applied_event_ids", "pending_reasons"):
        payload[key] = tuple(payload.get(key) or ())
    return PersistedResearchDossier(**{
        key: payload[key]
        for key in PersistedResearchDossier.__dataclass_fields__
        if key in payload
    })


def _coerce_event(value: DailyDossierEvent | Mapping[str, Any]) -> DailyDossierEvent:
    if isinstance(value, DailyDossierEvent):
        return value
    payload = dict(value)
    payload["new_facts"] = tuple(
        row if isinstance(row, DossierFactLineage) else DossierFactLineage(**row)
        for row in _mapping_rows(payload.get("new_facts"))
    )
    for key in (
        "source_document_ids",
        "revised_fact_ids",
        "retired_fact_ids",
        "impact_mapping_ids",
    ):
        payload[key] = tuple(payload.get(key) or ())
    return DailyDossierEvent(**{
        key: payload[key]
        for key in DailyDossierEvent.__dataclass_fields__
        if key in payload
    })


def _validate_daily_depth_rows(
    *,
    universe: Sequence[Mapping[str, Any]],
    statuses: Mapping[str, Mapping[str, Any]],
    depths: Mapping[str, Mapping[str, Any]],
) -> None:
    universe_ids = {str(row.get("target_id") or "") for row in universe}
    if set(statuses) != universe_ids or set(depths) != universe_ids:
        raise ValueError("daily status/depth target roster differs from universe")
    ordered = tuple(CensusDepthLevel)
    for target_id in sorted(universe_ids):
        depth = depths[target_id]
        status = statuses[target_id]
        maximum = CensusDepthLevel(str(depth.get("maximum_depth") or ""))
        completed = tuple(
            CensusDepthLevel(str(value))
            for value in (depth.get("completed_depths") or ())
        )
        if (
            not completed
            or completed[-1] != maximum
            or len(completed) != len(set(completed))
            or tuple(ordered.index(value) for value in completed)
            != tuple(sorted(ordered.index(value) for value in completed))
        ):
            raise ValueError("daily completed depth path is invalid")
        selected = depth.get("selected_for_deep") is True
        deep = maximum.value in _DEEP_DEPTHS
        if selected != deep:
            raise ValueError("daily deep selection and maximum depth disagree")
        if str(status.get("maximum_depth") or "") != maximum.value:
            raise ValueError("daily status and depth maximum disagree")
        if (
            status.get("terminal_status") == DailyTerminalStatus.FULL_THESIS.value
            and maximum != CensusDepthLevel.L5_FULL_THESIS
        ):
            raise ValueError("daily FULL_THESIS requires L5 depth")


def _mapping_rows(value: Any) -> tuple[Mapping[str, Any], ...]:
    return tuple(row for row in (value or ()) if isinstance(row, Mapping))


def _object_mapping(value: Any, label: str) -> Mapping[str, Any]:
    if isinstance(value, Mapping):
        return _json_safe(value)
    to_dict = getattr(value, "to_dict", None)
    if callable(to_dict):
        payload = to_dict()
        if isinstance(payload, Mapping):
            return _json_safe(payload)
    raise ValueError(f"{label} must be a mapping or canonical to_dict object")


def _required_mapping(value: Any, label: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping) or not value:
        raise ValueError(f"{label} is required")
    return value


def _unique_mapping(
    rows: Sequence[Mapping[str, Any]], key: str, label: str
) -> Mapping[str, Mapping[str, Any]]:
    output: dict[str, Mapping[str, Any]] = {}
    for row in rows:
        value = str(row.get(key) or "")
        if not value or value in output:
            raise ValueError(f"{label} {key} must be unique and non-empty")
        output[value] = row
    return output


def _unique_objects(rows: Sequence[Any], key: str, label: str) -> Mapping[str, Any]:
    output: dict[str, Any] = {}
    for row in rows:
        value = str(getattr(row, key))
        if not value or value in output:
            raise ValueError(f"{label} {key} must be unique and non-empty")
        output[value] = row
    return output


def _unique_text(values: Sequence[str], label: str, *, required: bool) -> None:
    if any(not isinstance(value, str) or not value.strip() for value in values):
        raise ValueError(f"{label} must contain non-empty strings")
    if len(values) != len(set(values)):
        raise ValueError(f"{label} must be unique")
    if required and not values:
        raise ValueError(f"{label} is required")


def _optional_float(value: Any) -> float | None:
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    parsed = float(value)
    return parsed if math.isfinite(parsed) else None


def _sha256(value: Any) -> bool:
    if not isinstance(value, str) or len(value) != 64:
        return False
    try:
        int(value, 16)
    except ValueError:
        return False
    return True


def _json_safe(value: Any) -> Any:
    return json.loads(json.dumps(value, ensure_ascii=False, sort_keys=True, default=str))


__all__ = [
    "DAILY_CENSUS_INTEGRATION_FAIL",
    "DAILY_CENSUS_INTEGRATION_PASS",
    "DAILY_CENSUS_INTEGRATION_SCHEMA_VERSION",
    "DEFAULT_DAILY_CENSUS_INTEGRATION_OUTPUT_PATH",
    "DailyCensusResearcherIntegrationResult",
    "DailyDossierEvent",
    "DailyResearcherCensusRow",
    "DossierComponentState",
    "DossierComponentStatus",
    "DossierDeltaPlan",
    "DossierFactLineage",
    "DossierResearchStatus",
    "FullThesisStatus",
    "PersistedResearchDossier",
    "ResearchDossierStore",
    "ScoreDisplayStatus",
    "audit_daily_census_integration",
    "build_persisted_research_dossier",
    "compile_phase97_daily_census_integration_audit",
    "integrate_daily_census_researcher_mode",
    "write_daily_census_researcher_integration",
    "write_phase97_daily_census_integration_audit",
]
