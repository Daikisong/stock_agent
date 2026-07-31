"""Phase 95 deterministic StageCourt for the v5 Researcher Mode.

The LLM has one narrow job here: map current source-backed EvidenceFact rows to
configured Evidence Contract primitive ids and explicitly dispose every row.
It never sees or returns a score or Stage. Deterministic code resolves each row
through fact/claim/source lineage, validates currentness, scope, freshness and
quorum, builds the canonical score snapshot, and is the sole Stage authority.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import date
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
from e2r.agentic.evidence_os import (
    EvidenceContractV2,
    SourceFamilyEvidence,
    SourceQuorumRule,
    SourceType,
)
from e2r.calibration.archetype_weight_profile import (
    CANONICAL_COMPONENT_MAX_POINTS,
)
from e2r.models import ScoreSnapshot, Stage
from e2r.production.metadata import write_json, write_jsonl
from e2r.red_team import (
    RedTeamAssessment,
    RedTeamRiskLevel,
    Soft4BStatus,
)
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderRejected,
    StructuredProviderUnavailable,
)
from e2r.staging import ACTIVE_RERATING_STAGES, StageClassificationInput, StageClassifier

from .component_researcher import (
    STAGE_GATE_FACT_MAPPING_SCHEMA,
    StructuredResearchProvider,
)
from .prompt_projection import (
    citable_fact_id_by_row_index,
    project_claim_fact_link_profile,
    project_research_source_claim_profile,
    project_research_source_document_profile,
    project_stage_gate_citable_facts,
    resolve_citable_fact_row_indices,
)
from .schemas import (
    CANONICAL_COMPONENT_ORDER,
    assert_blind_research_output,
    scrub_blind_research_payload,
)
from .score_aggregator import DeterministicScoreAggregationRun


STAGECOURT_OUTPUT_FILES: Mapping[str, str] = {
    "mappings": "stage_gate_mappings.jsonl",
    "decision": "atomic_stage_decision.json",
    "trace": "stagecourt_trace.json",
    "audit": "stagecourt_audit.json",
}

_FINAL_STATUS = "FINAL"
_PENDING_STATUSES = {
    "RESEARCH_IN_PROGRESS",
    "PROVIDER_PENDING",
    "STAGE_GATE_MAPPING_PENDING",
}
_ACTIVE_LIFECYCLES = {"CURRENT", "OPEN"}
_OFFICIAL_SOURCE_TIERS = {
    "REGULATORY_OFFICIAL",
    "ISSUER_OFFICIAL",
    "CUSTOMER_OFFICIAL",
}
_TRUSTED_SOURCE_TIERS = _OFFICIAL_SOURCE_TIERS | {
    "FINANCIAL_REVISION",
    "TRUSTED_INDEPENDENT",
}


@dataclass(frozen=True)
class StageTransitionContext:
    """Optional deterministic transition state, kept separate from daily events."""

    previous_stage: str | None = None
    thesis_ongoing: bool = False
    soft_4b_score: float = 0.0
    soft_4b_status: str = Soft4BStatus.NONE.value
    thesis_break_score: float = 0.0
    risk_claim_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.previous_stage is not None:
            Stage(self.previous_stage)
        for value, label in (
            (self.soft_4b_score, "soft_4b_score"),
            (self.thesis_break_score, "thesis_break_score"),
        ):
            if isinstance(value, bool) or not math.isfinite(float(value)) or not 0 <= value <= 100:
                raise ValueError(f"{label} must be between 0 and 100")
        Soft4BStatus(self.soft_4b_status)
        object.__setattr__(
            self,
            "risk_claim_ids",
            _unique_text(self.risk_claim_ids),
        )


@dataclass(frozen=True)
class ResearcherEventOverlay:
    """Daily event signal that cannot alter the full-thesis canonical Stage."""

    status: str = "NO_EVENT_OVERLAY"
    event_claim_ids: tuple[str, ...] = ()
    event_type: str = ""
    rationale: str = ""
    source_evidence_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.status not in {"NO_EVENT_OVERLAY", "EVENT_OVERLAY_ACTIVE"}:
            raise ValueError("unknown event overlay status")
        object.__setattr__(self, "event_claim_ids", _unique_text(self.event_claim_ids))
        object.__setattr__(
            self,
            "source_evidence_ids",
            _unique_text(self.source_evidence_ids),
        )
        if self.status == "EVENT_OVERLAY_ACTIVE" and not self.event_claim_ids:
            raise ValueError("active event overlay requires source-backed claim ids")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class StagePrimitiveMapping:
    mapping_id: str
    primitive_id: str
    direction: str
    claim_ids: tuple[str, ...]
    fact_ids: tuple[str, ...]
    source_document_ids: tuple[str, ...]
    semantic_rationale: str
    current_eligible_claim_ids: tuple[str, ...]
    source_quorum_satisfied: bool
    prompt_hash: str
    response_hash: str
    schema_version: str = "e2r_v5_stage_primitive_mapping_v1"

    def __post_init__(self) -> None:
        if self.direction not in {"SUPPORT", "COUNTER"}:
            raise ValueError("unknown Stage primitive mapping direction")
        for value, label in (
            (self.mapping_id, "mapping_id"),
            (self.primitive_id, "primitive_id"),
            (self.semantic_rationale, "semantic_rationale"),
            (self.prompt_hash, "prompt_hash"),
            (self.response_hash, "response_hash"),
        ):
            if not str(value).strip():
                raise ValueError(f"{label} is required")
        for values, label, allow_empty in (
            (self.claim_ids, "claim_ids", False),
            (self.fact_ids, "fact_ids", False),
            (self.source_document_ids, "source_document_ids", False),
            (self.current_eligible_claim_ids, "current_eligible_claim_ids", True),
        ):
            if tuple(values) != _unique_text(values) or (not allow_empty and not values):
                raise ValueError(f"{label} must contain unique source lineage")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ResearcherStageCourtDecision:
    decision_id: str
    trace_id: str
    target_id: str
    archetype_id: str
    as_of_date: str
    status: str
    canonical_stage: str | None
    score_valid: bool
    research_complete: bool
    counter_thesis_complete: bool
    stage_gates_complete: bool
    total_points: float | None
    component_vector: Mapping[str, float]
    present_positive_primitives: tuple[str, ...]
    current_guard_primitives: tuple[str, ...]
    hard_break_claim_ids: tuple[str, ...]
    score_fact_ids: tuple[str, ...]
    stage_claim_ids: tuple[str, ...]
    mapping_ids: tuple[str, ...]
    structured_record_ids: tuple[str, ...]
    event_overlay: Mapping[str, Any]
    stage_reasons: tuple[str, ...]
    pending_reasons: tuple[str, ...]
    classifier_version: str | None
    llm_stage_authority: bool = False
    schema_version: str = "e2r_v5_researcher_stagecourt_decision_v1"

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        if self.status not in {_FINAL_STATUS, *_PENDING_STATUSES}:
            raise ValueError("unknown Researcher StageCourt status")
        final = self.status == _FINAL_STATUS
        if final != bool(self.canonical_stage):
            raise ValueError("only FINAL StageCourt decisions may contain canonical Stage")
        if self.canonical_stage is not None:
            Stage(self.canonical_stage)
        if final and (
            not self.score_valid
            or not self.research_complete
            or not self.counter_thesis_complete
            or not self.stage_gates_complete
            or self.total_points is None
            or self.pending_reasons
        ):
            raise ValueError("FINAL StageCourt contradicts research completeness")
        if not final and not self.pending_reasons:
            raise ValueError("pending StageCourt requires exact blocker reasons")
        if self.llm_stage_authority:
            raise ValueError("LLM cannot be Stage authority")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ResearcherStageCourtRun:
    decision: ResearcherStageCourtDecision
    mappings: tuple[StagePrimitiveMapping, ...]
    mapping_rejections: tuple[Mapping[str, Any], ...]
    prompt_hash: str | None
    response_hash: str | None
    audit: Mapping[str, Any]
    schema_version: str = "e2r_v5_researcher_stagecourt_run_v1"

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "decision": self.decision.to_dict(),
            "mappings": [row.to_dict() for row in self.mappings],
            "mapping_rejections": [dict(row) for row in self.mapping_rejections],
            "prompt_hash": self.prompt_hash,
            "response_hash": self.response_hash,
            "audit": dict(self.audit),
            "llm_stage_authority": False,
        }


class ResearcherStageCourt:
    """Map semantic primitives, then deterministically decide canonical Stage."""

    def __init__(
        self,
        *,
        provider: StructuredResearchProvider,
        contracts: Mapping[str, EvidenceContractV2] | None = None,
    ) -> None:
        self.provider = provider
        self.contracts = dict(
            contracts
            if contracts is not None
            else load_evidence_contracts_v2(require_all_archetypes=True)
        )

    def decide(
        self,
        *,
        target_id: str,
        archetype_id: str,
        as_of_date: str,
        score_aggregation: DeterministicScoreAggregationRun,
        evidence_facts: Sequence[Any | Mapping[str, Any]],
        material_claims: Sequence[Mapping[str, Any]],
        claim_fact_links: Sequence[Mapping[str, Any]],
        source_documents: Sequence[Mapping[str, Any]],
        structured_records: Sequence[Any | Mapping[str, Any]],
        research_complete: bool,
        counter_thesis_complete: bool,
        transition: StageTransitionContext | None = None,
        event_overlay: ResearcherEventOverlay | None = None,
    ) -> ResearcherStageCourtRun:
        cutoff = date.fromisoformat(as_of_date)
        if archetype_id not in self.contracts:
            raise ValueError("StageCourt archetype lacks Evidence Contract v2")
        contract = self.contracts[archetype_id]
        transition = transition or StageTransitionContext()
        event = event_overlay or ResearcherEventOverlay()
        readiness_reasons = _readiness_reasons(
            score_aggregation=score_aggregation,
            research_complete=research_complete,
            counter_thesis_complete=counter_thesis_complete,
        )
        if readiness_reasons:
            return _pending_run(
                target_id=target_id,
                archetype_id=archetype_id,
                as_of_date=as_of_date,
                status="RESEARCH_IN_PROGRESS",
                reasons=readiness_reasons,
                score_aggregation=score_aggregation,
                research_complete=research_complete,
                counter_thesis_complete=counter_thesis_complete,
                event=event,
                structured_record_ids=_raw_structured_record_ids(
                    structured_records
                ),
            )
        claims = _validated_claims(
            material_claims,
            target_id=target_id,
            as_of_date=as_of_date,
            cutoff=cutoff,
        )
        documents = _validated_documents(
            source_documents,
            target_id=target_id,
            cutoff=cutoff,
        )
        links = _validated_claim_fact_links(
            claim_fact_links,
            claim_ids=set(claims),
        )
        facts = _validated_evidence_facts(
            evidence_facts,
            target_id=target_id,
            as_of_date=as_of_date,
        )
        fact_claim_ids = _validated_fact_claim_lineage(
            facts=facts,
            claims=claims,
            links=links,
        )
        records = _structured_rows(
            structured_records,
            target_id=target_id,
            as_of_date=as_of_date,
            cutoff=cutoff,
        )
        _validate_event(event, claims=claims, documents=documents)
        _validate_transition(transition, claims=claims)

        allowed_primitives = _contract_primitive_ids(contract)
        fact_projection = project_stage_gate_citable_facts(
            tuple(facts.values())
        )
        fact_id_by_row_index = citable_fact_id_by_row_index(
            fact_projection
        )
        provider_fact_projection = {
            key: value
            for key, value in fact_projection.items()
            if key not in {"facts", "fact_id_by_row_index"}
        }
        stage_link_rows = tuple(
            dict(row)
            for row in claim_fact_links
            if str(row.get("claim_id") or "") in claims
        )
        payload = scrub_blind_research_payload(
            {
                "researcher_role": "STAGE_GATE_FACT_MAPPER",
                "target_id": target_id,
                "archetype_id": archetype_id,
                "as_of_date": as_of_date,
                "evidence_contract": {
                    "allowed_primitive_ids": list(allowed_primitives),
                    "green_gate_primitive_ids": list(
                        contract.green_gate.primitive_ids()
                    ),
                    "guard_modes": dict(contract.guard_modes),
                    "primitive_aliases": {
                        key: list(value)
                        for key, value in contract.primitive_aliases.items()
                    },
                    "aggregation_rules": list(contract.aggregation_rules),
                },
                "current_evidence_fact_graph": fact_projection["facts"],
                "current_evidence_fact_projection": (
                    provider_fact_projection
                ),
                "source_claims": project_research_source_claim_profile(
                    tuple(claims.values())
                ),
                "source_documents": (
                    project_research_source_document_profile(
                        tuple(documents.values())
                    )
                ),
                "claim_fact_links": project_claim_fact_link_profile(
                    stage_link_rows
                ),
                "instructions": (
                    "Map only semantically matching CURRENT/OPEN POSITIVE or COUNTER "
                    "EvidenceFact rows to exact allowed primitive ids. Return canonical "
                    "fact_row_indices, never ids. SUPPORT is positive evidence and COUNTER "
                    "is thesis risk. Review every supplied row and return it exactly once "
                    "in fact_dispositions as MAPPED, NO_MATCH, or UNRESOLVED. Do not "
                    "calculate or mention score, Stage, investment action, expected "
                    "outcome, or future data."
                ),
            }
        )
        prompt_hash = _hash(payload)
        try:
            response = self.provider.complete(
                pass_name="STAGE_GATE_FACT_MAPPING",
                payload=payload,
            )
            assert_blind_research_output(response)
        except (
            StructuredProviderUnavailable,
            StructuredProviderRejected,
            TimeoutError,
            OSError,
            RuntimeError,
            KeyError,
            TypeError,
            ValueError,
        ) as exc:
            return _pending_run(
                target_id=target_id,
                archetype_id=archetype_id,
                as_of_date=as_of_date,
                status="PROVIDER_PENDING",
                reasons=(
                    "STAGE_GATE_MAPPING_PROVIDER_OR_OUTPUT_ERROR:"
                    f"{type(exc).__name__}:{_clean_error(exc)}",
                ),
                score_aggregation=score_aggregation,
                research_complete=research_complete,
                counter_thesis_complete=counter_thesis_complete,
                event=event,
                structured_record_ids=tuple(row["record_id"] for row in records),
                prompt_hash=prompt_hash,
            )

        response_hash = _hash(scrub_blind_research_payload(response))
        mappings, rejections = _validate_mapping_response(
            response,
            contract=contract,
            claims=claims,
            links=links,
            facts=facts,
            fact_claim_ids=fact_claim_ids,
            fact_id_by_row_index=fact_id_by_row_index,
            documents=documents,
            cutoff=cutoff,
            prompt_hash=prompt_hash,
            response_hash=response_hash,
        )
        unresolved = _strings(response.get("unresolved_material_questions"))
        mapping_complete = response.get("mapping_complete") is True
        mapping_reasons = tuple(
            dict.fromkeys(
                (
                    *(f"STAGE_GATE_MAPPING_REJECTED:{row['reason']}" for row in rejections),
                    *(f"STAGE_GATE_UNRESOLVED:{value}" for value in unresolved),
                    *(() if mapping_complete else ("STAGE_GATE_MAPPING_NOT_COMPLETE",)),
                )
            )
        )
        if mapping_reasons:
            return _pending_run(
                target_id=target_id,
                archetype_id=archetype_id,
                as_of_date=as_of_date,
                status="STAGE_GATE_MAPPING_PENDING",
                reasons=mapping_reasons,
                score_aggregation=score_aggregation,
                research_complete=research_complete,
                counter_thesis_complete=counter_thesis_complete,
                event=event,
                structured_record_ids=tuple(row["record_id"] for row in records),
                mappings=mappings,
                mapping_rejections=rejections,
                prompt_hash=prompt_hash,
                response_hash=response_hash,
            )

        score = score_aggregation.total_result.score
        if score is None:
            raise ValueError("ready StageCourt requires deterministic total score")
        positive_primitives = _present_positive_primitives(mappings)
        current_guards = _current_guard_primitives(mappings, contract=contract)
        hard_break_claim_ids = _hard_break_claim_ids(
            mappings,
            contract=contract,
            claims=claims,
            documents=documents,
            cutoff=cutoff,
        )
        green_gate_satisfied = contract.green_gate_satisfied(positive_primitives)
        blocking_green_guards = tuple(
            primitive
            for primitive in current_guards
            if contract.guard_modes.get(primitive)
            in {"block_if_current", "block_green_if_current"}
        )
        revision_score = _revision_score(records)
        snapshot = _score_snapshot(
            target_id=target_id,
            as_of_date=as_of_date,
            score_aggregation=score_aggregation,
            claims=claims,
            mappings=mappings,
            contract=contract,
            green_gate_satisfied=green_gate_satisfied,
            blocking_green_guards=blocking_green_guards,
            revision_score=revision_score,
        )
        red_team = _red_team_assessment(
            target_id=target_id,
            as_of_date=as_of_date,
            transition=transition,
            current_guards=current_guards,
            hard_break_claim_ids=hard_break_claim_ids,
            mapping_claim_ids=tuple(
                claim_id
                for row in mappings
                if row.direction == "COUNTER"
                for claim_id in row.current_eligible_claim_ids
            ),
        )
        previous_stage = (
            Stage(transition.previous_stage)
            if transition.previous_stage is not None
            else None
        )
        staged = StageClassifier().classify(
            StageClassificationInput(
                score=snapshot,
                red_team=red_team,
                previous_stage=previous_stage,
                thesis_ongoing=(
                    transition.thesis_ongoing
                    and previous_stage in ACTIVE_RERATING_STAGES
                ),
                # Daily events are deliberately not fed to canonical Stage.
                company_event_score=0.0,
                high_quality_company_event=False,
                evidence_ids=tuple(hard_break_claim_ids),
            )
        )
        stage_claim_ids = _unique_text(
            claim_id
            for row in mappings
            for claim_id in row.current_eligible_claim_ids
        )
        mapping_ids = tuple(row.mapping_id for row in mappings)
        decision_payload = {
            "target_id": target_id,
            "archetype_id": archetype_id,
            "as_of_date": as_of_date,
            "canonical_stage": staged.stage.value,
            "total_points": score.total_points,
            "component_vector": dict(score.component_points),
            "mapping_ids": list(mapping_ids),
            "hard_break_claim_ids": list(hard_break_claim_ids),
            "event_overlay": event.to_dict(),
        }
        trace_id = "STAGECOURT-" + _hash(decision_payload)[:24]
        decision = ResearcherStageCourtDecision(
            decision_id="ADEC5-" + _hash({**decision_payload, "trace_id": trace_id})[:24],
            trace_id=trace_id,
            target_id=target_id,
            archetype_id=archetype_id,
            as_of_date=as_of_date,
            status=_FINAL_STATUS,
            canonical_stage=staged.stage.value,
            score_valid=True,
            research_complete=True,
            counter_thesis_complete=True,
            stage_gates_complete=True,
            total_points=score.total_points,
            component_vector=dict(score.component_points),
            present_positive_primitives=positive_primitives,
            current_guard_primitives=current_guards,
            hard_break_claim_ids=hard_break_claim_ids,
            score_fact_ids=score.fact_ids,
            stage_claim_ids=stage_claim_ids,
            mapping_ids=mapping_ids,
            structured_record_ids=tuple(row["record_id"] for row in records),
            event_overlay={
                **event.to_dict(),
                "canonical_stage_effect": "NONE",
            },
            stage_reasons=tuple(staged.stage_reason),
            pending_reasons=(),
            classifier_version=staged.classifier_version,
        )
        audit = _audit(
            decision=decision,
            mappings=mappings,
            mapping_rejections=(),
            contract=contract,
            green_gate_satisfied=green_gate_satisfied,
            blocking_green_guards=blocking_green_guards,
            revision_score=revision_score,
        )
        return ResearcherStageCourtRun(
            decision=decision,
            mappings=mappings,
            mapping_rejections=(),
            prompt_hash=prompt_hash,
            response_hash=response_hash,
            audit=audit,
        )


def write_researcher_stagecourt_run(
    run: ResearcherStageCourtRun,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root)
    paths = {
        key: root / filename for key, filename in STAGECOURT_OUTPUT_FILES.items()
    }
    write_jsonl(paths["mappings"], (row.to_dict() for row in run.mappings))
    write_json(paths["decision"], run.decision.to_dict())
    write_json(paths["trace"], run.to_dict())
    write_json(paths["audit"], run.audit)
    return paths


def _validated_claims(
    rows: Sequence[Mapping[str, Any]],
    *,
    target_id: str,
    as_of_date: str,
    cutoff: date,
) -> Mapping[str, Mapping[str, Any]]:
    claims: dict[str, Mapping[str, Any]] = {}
    for raw in rows:
        row = dict(raw)
        claim_id = str(row.get("claim_id") or "").strip()
        if not claim_id or claim_id in claims:
            raise ValueError("StageCourt claims require unique ids")
        if str(row.get("target_id") or "") != target_id:
            raise ValueError("StageCourt claim crosses target scope")
        if str(row.get("as_of_date") or "") != as_of_date:
            raise ValueError("StageCourt claim as_of_date mismatch")
        for key in ("published_at", "available_at"):
            value = str(row.get(key) or "")[:10]
            if not value or date.fromisoformat(value) > cutoff:
                raise ValueError("StageCourt claim leaks future evidence")
        if row.get("accepted") is not True or row.get("material") is not True:
            continue
        if row.get("accepted_by_evidence_os") is not True:
            raise ValueError("StageCourt material claim bypassed Evidence OS")
        if row.get("llm_score_authority") or row.get("llm_stage_authority"):
            raise ValueError("StageCourt claim grants forbidden LLM authority")
        claims[claim_id] = row
    return claims


def _validated_documents(
    rows: Sequence[Mapping[str, Any]],
    *,
    target_id: str,
    cutoff: date,
) -> Mapping[str, Mapping[str, Any]]:
    documents: dict[str, Mapping[str, Any]] = {}
    for raw in rows:
        row = dict(raw)
        document_id = str(row.get("document_id") or "").strip()
        if not document_id or document_id in documents:
            raise ValueError("StageCourt source documents require unique ids")
        row_target = str(row.get("target_id") or target_id)
        if row_target != target_id:
            raise ValueError("StageCourt source document crosses target scope")
        published = str(row.get("published_at") or "")[:10]
        available = str(row.get("available_at") or published)[:10]
        if not published or not available:
            raise ValueError("StageCourt source document lacks point-in-time dates")
        if date.fromisoformat(published) > cutoff or date.fromisoformat(available) > cutoff:
            raise ValueError("StageCourt source document leaks future evidence")
        if row.get("snippet_only") is True or row.get("evidence_eligible") is False:
            continue
        documents[document_id] = row
    return documents


def _validated_claim_fact_links(
    rows: Sequence[Mapping[str, Any]],
    *,
    claim_ids: set[str],
) -> Mapping[str, tuple[str, ...]]:
    links: dict[str, list[str]] = {claim_id: [] for claim_id in claim_ids}
    for raw in rows:
        claim_id = str(raw.get("claim_id") or "")
        fact_id = str(raw.get("fact_id") or "")
        if claim_id not in links:
            continue
        if not fact_id:
            raise ValueError("StageCourt claim/fact link lacks fact id")
        links[claim_id].append(fact_id)
    missing = sorted(claim_id for claim_id, fact_ids in links.items() if not fact_ids)
    if missing:
        raise ValueError(f"StageCourt material claims lack fact lineage: {missing[:5]}")
    return {key: _unique_text(value) for key, value in links.items()}


def _validated_evidence_facts(
    rows: Sequence[Any | Mapping[str, Any]],
    *,
    target_id: str,
    as_of_date: str,
) -> Mapping[str, Mapping[str, Any]]:
    facts: dict[str, Mapping[str, Any]] = {}
    for raw in rows:
        row = dict(raw) if isinstance(raw, Mapping) else dict(raw.to_dict())
        fact_id = str(row.get("fact_id") or "").strip()
        if not fact_id or fact_id in facts:
            raise ValueError("StageCourt EvidenceFacts require unique ids")
        if str(row.get("target_id") or "") != target_id:
            raise ValueError("StageCourt EvidenceFact crosses target scope")
        if str(row.get("as_of_date") or "") != as_of_date:
            raise ValueError("StageCourt EvidenceFact as_of_date mismatch")
        if str(row.get("direction") or "") not in {
            "POSITIVE",
            "COUNTER",
            "NEUTRAL",
            "RESOLUTION",
        }:
            raise ValueError("StageCourt EvidenceFact direction is invalid")
        if str(row.get("current_lifecycle") or "") not in {
            "CURRENT",
            "OPEN",
            "RESOLVED",
            "SUPERSEDED",
        }:
            raise ValueError("StageCourt EvidenceFact lifecycle is invalid")
        facts[fact_id] = row
    return facts


def _validated_fact_claim_lineage(
    *,
    facts: Mapping[str, Mapping[str, Any]],
    claims: Mapping[str, Mapping[str, Any]],
    links: Mapping[str, tuple[str, ...]],
) -> Mapping[str, tuple[str, ...]]:
    fact_claim_ids: dict[str, list[str]] = {
        fact_id: [] for fact_id in facts
    }
    for claim_id, fact_ids in links.items():
        for fact_id in fact_ids:
            if fact_id not in facts:
                raise ValueError(
                    "StageCourt claim/fact link references unknown fact"
                )
            fact_claim_ids[fact_id].append(claim_id)
    unlinked = sorted(
        fact_id
        for fact_id, claim_ids in fact_claim_ids.items()
        if not claim_ids
    )
    if unlinked:
        raise ValueError(
            f"StageCourt EvidenceFacts lack claim lineage: {unlinked[:5]}"
        )

    result: dict[str, tuple[str, ...]] = {}
    for fact_id, linked_claim_ids in fact_claim_ids.items():
        canonical_claim_ids = _unique_text(linked_claim_ids)
        fact = facts[fact_id]
        embedded_claim_ids = _unique_text(
            _strings(fact.get("claim_ids"))
        )
        if embedded_claim_ids and set(embedded_claim_ids) != set(
            canonical_claim_ids
        ):
            raise ValueError(
                "StageCourt EvidenceFact embedded claim lineage mismatch"
            )
        fact_direction = str(fact.get("direction") or "")
        fact_lifecycle = str(fact.get("current_lifecycle") or "")
        fact_source_ids = set(_strings(fact.get("source_ids")))
        for claim_id in canonical_claim_ids:
            claim = claims[claim_id]
            if str(claim.get("direction") or "") != fact_direction:
                raise ValueError(
                    "StageCourt EvidenceFact/claim direction mismatch"
                )
            if (
                str(claim.get("current_lifecycle") or "")
                != fact_lifecycle
            ):
                raise ValueError(
                    "StageCourt EvidenceFact/claim lifecycle mismatch"
                )
            if not set(_strings(claim.get("source_ids"))).issubset(
                fact_source_ids
            ):
                raise ValueError(
                    "StageCourt EvidenceFact source lineage mismatch"
                )
        result[fact_id] = canonical_claim_ids
    return result


def _raw_structured_record_ids(
    rows: Sequence[Any | Mapping[str, Any]],
) -> tuple[str, ...]:
    values: list[str] = []
    for raw in rows:
        row = raw if isinstance(raw, Mapping) else raw.to_dict()
        value = str(row.get("record_id") or "").strip()
        if value:
            values.append(value)
    return _unique_text(values)


def _structured_rows(
    rows: Sequence[Any | Mapping[str, Any]],
    *,
    target_id: str,
    as_of_date: str,
    cutoff: date,
) -> tuple[Mapping[str, Any], ...]:
    result: list[Mapping[str, Any]] = []
    seen: set[str] = set()
    for raw in rows:
        row = dict(raw) if isinstance(raw, Mapping) else dict(raw.to_dict())
        record_id = str(row.get("record_id") or "").strip()
        if not record_id or record_id in seen:
            raise ValueError("StageCourt structured records require unique ids")
        if str(row.get("target_id") or row.get("symbol") or target_id) != target_id:
            raise ValueError("StageCourt structured record crosses target scope")
        if str(row.get("as_of_date") or "") != as_of_date:
            raise ValueError("StageCourt structured record as_of_date mismatch")
        observed = str(row.get("observed_at") or row.get("period_end") or as_of_date)[:10]
        if date.fromisoformat(observed) > cutoff:
            raise ValueError("StageCourt structured record leaks future data")
        seen.add(record_id)
        result.append(row)
    return tuple(result)


def _validate_event(
    event: ResearcherEventOverlay,
    *,
    claims: Mapping[str, Mapping[str, Any]],
    documents: Mapping[str, Mapping[str, Any]],
) -> None:
    if not set(event.event_claim_ids) <= set(claims):
        raise ValueError("event overlay references unknown material claims")
    if event.status == "EVENT_OVERLAY_ACTIVE" and any(
        not _claim_source_backed(claims[claim_id], documents)
        for claim_id in event.event_claim_ids
    ):
        raise ValueError("event overlay requires source-backed claims")


def _validate_transition(
    transition: StageTransitionContext,
    *,
    claims: Mapping[str, Mapping[str, Any]],
) -> None:
    if not set(transition.risk_claim_ids) <= set(claims):
        raise ValueError("transition context references unknown material claims")


def _readiness_reasons(
    *,
    score_aggregation: DeterministicScoreAggregationRun,
    research_complete: bool,
    counter_thesis_complete: bool,
) -> tuple[str, ...]:
    reasons: list[str] = []
    if not research_complete:
        reasons.append("RESEARCHER_MODE_NOT_COMPLETE")
    if not counter_thesis_complete:
        reasons.append("COUNTER_THESIS_NOT_COMPLETE")
    if not score_aggregation.score_valid or not score_aggregation.ready_for_stagecourt:
        reasons.append("DETERMINISTIC_SCORE_NOT_READY")
    if score_aggregation.total_result.score is None:
        reasons.append("DETERMINISTIC_TOTAL_SCORE_MISSING")
    return tuple(dict.fromkeys(reasons))


def _contract_primitive_ids(contract: EvidenceContractV2) -> tuple[str, ...]:
    values = list(contract.required_primitives)
    values.extend(contract.green_gate.primitive_ids())
    values.extend(contract.alternative_primitives)
    values.extend(
        primitive
        for alternatives in contract.alternative_primitives.values()
        for primitive in alternatives
    )
    values.extend(contract.guard_modes)
    return _unique_text(values)


def _claim_prompt_row(row: Mapping[str, Any]) -> Mapping[str, Any]:
    return {
        key: row.get(key)
        for key in (
            "claim_id",
            "direction",
            "current_lifecycle",
            "materiality",
            "subject",
            "predicate",
            "predicate_family",
            "normalized_object",
            "economic_mechanism",
            "exact_quote",
            "period",
            "value",
            "unit",
            "scope_business_segment",
            "scope_product_family",
            "scope_technology_family",
            "scope_transaction_type",
            "scope_economic_mechanism",
            "mechanism_scope_id",
            "source_family",
            "source_tier",
            "published_at",
            "available_at",
        )
    }


def _validate_mapping_response(
    response: Mapping[str, Any],
    *,
    contract: EvidenceContractV2,
    claims: Mapping[str, Mapping[str, Any]],
    links: Mapping[str, tuple[str, ...]],
    facts: Mapping[str, Mapping[str, Any]],
    fact_claim_ids: Mapping[str, tuple[str, ...]],
    fact_id_by_row_index: Mapping[int, str],
    documents: Mapping[str, Mapping[str, Any]],
    cutoff: date,
    prompt_hash: str,
    response_hash: str,
) -> tuple[tuple[StagePrimitiveMapping, ...], tuple[Mapping[str, Any], ...]]:
    del links
    raw_rows = response.get("mappings")
    if not isinstance(raw_rows, list):
        return (), ({"proposal_index": -1, "reason": "MAPPINGS_NOT_ARRAY"},)
    allowed = set(_contract_primitive_ids(contract))
    mappings: list[StagePrimitiveMapping] = []
    rejections: list[Mapping[str, Any]] = list(
        _stage_fact_accounting_rejections(
            response=response,
            fact_id_by_row_index=fact_id_by_row_index,
            facts=facts,
        )
    )
    keys: set[tuple[str, str]] = set()
    for index, raw in enumerate(raw_rows):
        if not isinstance(raw, Mapping):
            rejections.append({"proposal_index": index, "reason": "MAPPING_NOT_OBJECT"})
            continue
        primitive_id = str(raw.get("primitive_id") or "").strip()
        direction = str(raw.get("direction") or "").strip()
        raw_fact_row_indices = raw.get("fact_row_indices")
        fact_row_indices = _non_negative_integers(
            raw_fact_row_indices
        )
        rationale = str(raw.get("semantic_rationale") or "").strip()
        reason = None
        if primitive_id not in allowed:
            reason = "UNKNOWN_PRIMITIVE_ID"
        elif direction not in {"SUPPORT", "COUNTER"}:
            reason = "UNKNOWN_MAPPING_DIRECTION"
        elif (
            not fact_row_indices
            or len(fact_row_indices) != len(set(fact_row_indices))
        ):
            reason = "FACT_ROW_INDICES_EMPTY_OR_DUPLICATED"
        elif any(
            row_index not in fact_id_by_row_index
            for row_index in fact_row_indices
        ):
            reason = "UNKNOWN_FACT_ROW_INDEX"
        elif not rationale:
            reason = "SEMANTIC_RATIONALE_MISSING"
        elif (primitive_id, direction) in keys:
            reason = "DUPLICATE_PRIMITIVE_DIRECTION"
        elif any(
            str(
                facts[fact_id_by_row_index[row_index]].get("direction")
                or ""
            )
            not in ({"POSITIVE"} if direction == "SUPPORT" else {"COUNTER"})
            for row_index in fact_row_indices
        ):
            reason = "FACT_DIRECTION_MISMATCH"
        fact_ids = (
            resolve_citable_fact_row_indices(
                fact_row_indices,
                fact_id_by_row_index=fact_id_by_row_index,
                label="fact_row_indices",
            )
            if reason is None
            else ()
        )
        claim_ids = _unique_text(
            claim_id
            for fact_id in fact_ids
            for claim_id in fact_claim_ids[fact_id]
        )
        if reason is None and (
            not claim_ids
            or any(claim_id not in claims for claim_id in claim_ids)
        ):
            reason = "FACT_CLAIM_LINEAGE_MISSING"
        elif any(
            not _claim_source_backed(claims[claim_id], documents)
            for claim_id in claim_ids
        ):
            reason = "CLAIM_NOT_SOURCE_BACKED"
        if reason:
            rejections.append(
                {
                    "proposal_index": index,
                    "primitive_id": primitive_id,
                    "direction": direction,
                    "fact_row_indices": list(fact_row_indices),
                    "fact_ids": list(fact_ids),
                    "claim_ids": list(claim_ids),
                    "reason": reason,
                }
            )
            continue
        keys.add((primitive_id, direction))
        current_ids = tuple(
            claim_id
            for claim_id in claim_ids
            if _claim_current_for_primitive(
                claims[claim_id],
                primitive_id=primitive_id,
                contract=contract,
                cutoff=cutoff,
            )
        )
        document_ids = _unique_text(
            str(claims[claim_id].get("document_id") or "")
            for claim_id in claim_ids
        )
        eligible_claims = [claims[claim_id] for claim_id in current_ids]
        quorum = _source_quorum_satisfied(
            primitive_id=primitive_id,
            claims=eligible_claims,
            contract=contract,
            scope="green_gate" if direction == "SUPPORT" else "hard_break",
        )
        mapping_payload = {
            "primitive_id": primitive_id,
            "direction": direction,
            "claim_ids": list(claim_ids),
            "fact_ids": list(fact_ids),
            "prompt_hash": prompt_hash,
            "response_hash": response_hash,
        }
        mappings.append(
            StagePrimitiveMapping(
                mapping_id="STGMAP-" + _hash(mapping_payload)[:24],
                primitive_id=primitive_id,
                direction=direction,
                claim_ids=claim_ids,
                fact_ids=fact_ids,
                source_document_ids=document_ids,
                semantic_rationale=rationale,
                current_eligible_claim_ids=current_ids,
                source_quorum_satisfied=quorum,
                prompt_hash=prompt_hash,
                response_hash=response_hash,
            )
        )
    return tuple(mappings), tuple(rejections)


def _stage_fact_accounting_rejections(
    *,
    response: Mapping[str, Any],
    fact_id_by_row_index: Mapping[int, str],
    facts: Mapping[str, Mapping[str, Any]],
) -> tuple[Mapping[str, Any], ...]:
    """Reject omission, duplication, tamper, and incomplete row disposition."""

    raw_mappings = response.get("mappings")
    mapped: set[int] = set()
    if isinstance(raw_mappings, list):
        for raw in raw_mappings:
            if not isinstance(raw, Mapping):
                continue
            values = _non_negative_integers(raw.get("fact_row_indices"))
            mapped.update(
                row_index
                for row_index in values
                if row_index in fact_id_by_row_index
            )

    raw_dispositions = response.get("fact_dispositions")
    if not isinstance(raw_dispositions, list):
        return (
            {
                "proposal_index": -1,
                "reason": "FACT_DISPOSITIONS_NOT_ARRAY",
            },
        )
    seen: dict[int, str] = {}
    rejections: list[Mapping[str, Any]] = []
    allowed = set(fact_id_by_row_index)
    for index, raw in enumerate(raw_dispositions):
        if not isinstance(raw, Mapping):
            rejections.append(
                {
                    "proposal_index": index,
                    "reason": "FACT_DISPOSITION_NOT_OBJECT",
                }
            )
            continue
        row_index = raw.get("fact_row_index")
        status = str(raw.get("status") or "")
        rationale = str(raw.get("rationale") or "").strip()
        reason = None
        if (
            isinstance(row_index, bool)
            or not isinstance(row_index, int)
            or row_index < 0
            or row_index not in allowed
        ):
            reason = "FACT_DISPOSITION_UNKNOWN_ROW"
        elif row_index in seen:
            reason = "FACT_DISPOSITION_DUPLICATE_ROW"
        elif status not in {"MAPPED", "NO_MATCH", "UNRESOLVED"}:
            reason = "FACT_DISPOSITION_UNKNOWN_STATUS"
        elif not rationale:
            reason = "FACT_DISPOSITION_RATIONALE_MISSING"
        elif (status == "MAPPED") != (row_index in mapped):
            reason = "FACT_DISPOSITION_MAPPING_MISMATCH"
        if reason:
            rejections.append(
                {
                    "proposal_index": index,
                    "fact_row_index": row_index,
                    "reason": reason,
                }
            )
            continue
        seen[row_index] = status
        if status == "UNRESOLVED":
            rejections.append(
                {
                    "proposal_index": index,
                    "fact_row_index": row_index,
                    "fact_id": fact_id_by_row_index[row_index],
                    "reason": "FACT_DISPOSITION_UNRESOLVED",
                }
            )
    if set(seen) != allowed:
        rejections.append(
            {
                "proposal_index": -1,
                "reason": "FACT_DISPOSITION_ROSTER_MISMATCH",
                "missing_fact_row_indices": sorted(allowed - set(seen)),
                "extra_fact_row_indices": sorted(set(seen) - allowed),
            }
        )
    for row_index in mapped & allowed:
        expected = str(
            facts[fact_id_by_row_index[row_index]].get("direction") or ""
        )
        if expected not in {"POSITIVE", "COUNTER"}:
            rejections.append(
                {
                    "proposal_index": -1,
                    "fact_row_index": row_index,
                    "reason": "MAPPED_FACT_DIRECTION_NOT_ELIGIBLE",
                }
            )
    return tuple(rejections)


def _non_negative_integers(value: Any) -> tuple[int, ...]:
    if isinstance(value, (str, bytes)) or not isinstance(value, Sequence):
        return ()
    result = []
    for item in value:
        if isinstance(item, bool) or not isinstance(item, int) or item < 0:
            return ()
        result.append(item)
    return tuple(result)


def _claim_source_backed(
    claim: Mapping[str, Any],
    documents: Mapping[str, Mapping[str, Any]],
) -> bool:
    document_id = str(claim.get("document_id") or "")
    source_ids = set(_strings(claim.get("source_ids")))
    exact_quote = str(claim.get("exact_quote") or "")
    if not document_id or document_id not in documents or document_id not in source_ids:
        return False
    if not exact_quote:
        return False
    content = str(documents[document_id].get("content_text") or "")
    return not content or exact_quote in content


def _claim_current_for_primitive(
    claim: Mapping[str, Any],
    *,
    primitive_id: str,
    contract: EvidenceContractV2,
    cutoff: date,
) -> bool:
    if str(claim.get("current_lifecycle") or "") not in _ACTIVE_LIFECYCLES:
        return False
    policy = contract.freshness.get(primitive_id)
    if policy is None or policy.max_age_days is None:
        return True
    available = date.fromisoformat(str(claim.get("available_at") or "")[:10])
    return (cutoff - available).days <= policy.max_age_days


def _source_quorum_satisfied(
    *,
    primitive_id: str,
    claims: Sequence[Mapping[str, Any]],
    contract: EvidenceContractV2,
    scope: str,
) -> bool:
    if not claims:
        return False
    rule = contract.source_quorum.get(primitive_id) or contract.source_quorum.get(scope)
    if rule is None:
        rule = SourceQuorumRule()
    return rule.satisfied(tuple(_source_family(row) for row in claims))


def _source_family(claim: Mapping[str, Any]) -> SourceFamilyEvidence:
    tier_name = str(claim.get("source_tier") or "GENERAL_WEB")
    official = tier_name in _OFFICIAL_SOURCE_TIERS
    trusted = tier_name in _TRUSTED_SOURCE_TIERS
    if official:
        source_type = SourceType.FILING
        tier = 1
    elif tier_name == "FINANCIAL_REVISION":
        source_type = SourceType.RESEARCH_REPORT
        tier = 2
    elif trusted:
        source_type = SourceType.RESEARCH_REPORT
        tier = 2
    else:
        source_type = SourceType.NEWS
        tier = 3
    return SourceFamilyEvidence(
        source_family_id=str(
            claim.get("source_independence_group")
            or claim.get("source_family")
            or claim.get("document_id")
        ),
        document_id=str(claim.get("document_id") or ""),
        source_type=source_type,
        tier=tier,
        official=official,
        independent=tier_name != "ISSUER_OFFICIAL",
    )


def _present_positive_primitives(
    mappings: Sequence[StagePrimitiveMapping],
) -> tuple[str, ...]:
    return _unique_text(
        row.primitive_id
        for row in mappings
        if row.direction == "SUPPORT"
        and row.current_eligible_claim_ids
        and row.source_quorum_satisfied
    )


def _current_guard_primitives(
    mappings: Sequence[StagePrimitiveMapping],
    *,
    contract: EvidenceContractV2,
) -> tuple[str, ...]:
    return _unique_text(
        row.primitive_id
        for row in mappings
        if row.direction == "COUNTER"
        and row.primitive_id in contract.guard_modes
        and row.current_eligible_claim_ids
    )


def _hard_break_claim_ids(
    mappings: Sequence[StagePrimitiveMapping],
    *,
    contract: EvidenceContractV2,
    claims: Mapping[str, Mapping[str, Any]],
    documents: Mapping[str, Mapping[str, Any]],
    cutoff: date,
) -> tuple[str, ...]:
    result: list[str] = []
    for mapping in mappings:
        if (
            mapping.direction != "COUNTER"
            or contract.guard_modes.get(mapping.primitive_id)
            != "hard_break_if_current_and_quorum"
            or not mapping.source_quorum_satisfied
        ):
            continue
        for claim_id in mapping.current_eligible_claim_ids:
            claim = claims[claim_id]
            if _hard_break_claim_eligible(
                claim,
                documents=documents,
                cutoff=cutoff,
            ):
                result.append(claim_id)
    return _unique_text(result)


def _hard_break_claim_eligible(
    claim: Mapping[str, Any],
    *,
    documents: Mapping[str, Mapping[str, Any]],
    cutoff: date,
) -> bool:
    if str(claim.get("direction") or "") != "COUNTER":
        return False
    if str(claim.get("current_lifecycle") or "") != "OPEN":
        return False
    if claim.get("material") is not True or claim.get("accepted_by_evidence_os") is not True:
        return False
    if not _claim_source_backed(claim, documents):
        return False
    if date.fromisoformat(str(claim.get("available_at") or "")[:10]) > cutoff:
        return False
    if not str(claim.get("mechanism_scope_id") or "").strip():
        return False
    try:
        scope_confidence = float(claim.get("scope_confidence") or 0.0)
    except (TypeError, ValueError):
        return False
    if scope_confidence < 0.5:
        return False
    generic_transaction = str(claim.get("scope_transaction_type") or "") in {
        "",
        "GENERIC_INFORMATION",
    }
    generic_mechanism = str(claim.get("scope_economic_mechanism") or "") in {
        "",
        "INFORMATION_ONLY",
    }
    return not (generic_transaction and generic_mechanism)


def _revision_score(records: Sequence[Mapping[str, Any]]) -> float:
    numeric: list[float] = []
    directions: list[str] = []
    for row in records:
        metadata = row.get("metadata") or {}
        if not isinstance(metadata, Mapping):
            metadata = {}
        family = str(metadata.get("revision_family") or "")
        target_only = bool(metadata.get("target_price_only"))
        metric_id = str(row.get("metric_id") or "").casefold()
        if target_only or (family and family != "EARNINGS"):
            continue
        if "revision" not in metric_id:
            continue
        value = row.get("value")
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            number = float(value)
            if math.isfinite(number) and abs(number) <= 300:
                numeric.append(number)
        elif str(value) in {"UP", "DOWN", "UNCHANGED"}:
            directions.append(str(value))
    if numeric:
        return round(max(0.0, min(100.0, max(numeric) / 30.0 * 100.0)), 4)
    if directions:
        up = sum(value == "UP" for value in directions)
        down = sum(value == "DOWN" for value in directions)
        directional = up + down
        return round(up / directional * 100.0, 4) if directional else 50.0
    return 0.0


def _score_snapshot(
    *,
    target_id: str,
    as_of_date: str,
    score_aggregation: DeterministicScoreAggregationRun,
    claims: Mapping[str, Mapping[str, Any]],
    mappings: Sequence[StagePrimitiveMapping],
    contract: EvidenceContractV2,
    green_gate_satisfied: bool,
    blocking_green_guards: Sequence[str],
    revision_score: float,
) -> ScoreSnapshot:
    score = score_aggregation.total_result.score
    if score is None:
        raise ValueError("StageCourt score snapshot requires complete total")
    raw: dict[str, float] = {}
    diagnostics: dict[str, float] = {
        "score_valid": 1.0,
        "archetype_weight_profile_applied": 1.0,
        "claim_backed_claim_count_capped": min(100.0, float(bool(claims))),
        "score_claim_backed_component_ratio": 100.0,
        "orphan_score_component_count_capped": 0.0,
        "score_claim_backed_required": 100.0,
        "source_backed_deep_research_completed": 100.0,
        "llm_deep_research_completed": 100.0,
        "report_date_confidence": 100.0,
        "date_unverified_snippet_news_count_capped": 0.0,
        "date_unverified_document_count_capped": 0.0,
        "snippet_only_green_block": 0.0,
        "emerging_theme_active": 0.0,
        "archetype_green_restricted_by_profile": 0.0,
        "revision_score": revision_score,
        "structural_visibility_quality": 100.0 if green_gate_satisfied else 0.0,
        "contract_quality": 100.0 if green_gate_satisfied else 0.0,
        "one_off_shortage_risk": 0.0 if green_gate_satisfied else 100.0,
        "price_only_blowoff_score": 0.0,
        "theme_overheat_score": 0.0,
        "evidence_contract_required_primitive_count_capped": min(
            100.0, float(len(contract.required_primitives))
        ),
        "evidence_contract_green_gate_required_primitive_count_capped": min(
            100.0, float(len(contract.green_gate.primitive_ids()))
        ),
        "evidence_contract_green_gate_coverage_pct": (
            100.0 if green_gate_satisfied else 0.0
        ),
        "evidence_contract_green_gate_missing_primitive_count_capped": (
            0.0 if green_gate_satisfied else 1.0
        ),
        "evidence_contract_guard_present_primitive_count_capped": min(
            100.0, float(len(blocking_green_guards))
        ),
        "evidence_contract_guard_missing_primitive_count_capped": 0.0,
        "cross_evidence_family_count": min(
            100.0,
            float(
                len(
                    {
                        str(claim.get("source_family") or "")
                        for claim in claims.values()
                        if claim.get("source_family")
                    }
                )
            ),
        ),
    }
    for component_id in CANONICAL_COMPONENT_ORDER:
        points = float(score.component_points[component_id])
        maximum = float(score.component_max_points[component_id])
        canonical_max = float(CANONICAL_COMPONENT_MAX_POINTS[component_id])
        raw[component_id] = (
            round(points / maximum * canonical_max, 6) if maximum else 0.0
        )
        diagnostics[f"archetype_weight_{component_id}"] = maximum
        diagnostics[f"archetype_component_{component_id}"] = points
    mapped_claim_ids = _unique_text(
        claim_id for row in mappings for claim_id in row.current_eligible_claim_ids
    )
    return ScoreSnapshot(
        symbol=target_id,
        as_of_date=date.fromisoformat(as_of_date),
        eps_fcf_explosion_score=raw["eps_fcf_explosion"],
        earnings_visibility_score=raw["earnings_visibility"],
        bottleneck_pricing_score=raw["bottleneck_pricing"],
        market_mispricing_score=raw["market_mispricing"],
        valuation_rerating_score=raw["valuation_rerating"],
        capital_allocation_score=raw["capital_allocation"],
        information_confidence_score=raw["information_confidence"],
        risk_penalty=0.0,
        total_score=float(score.total_points),
        diagnostic_scores=diagnostics,
        evidence_ids=tuple(score.fact_ids) + mapped_claim_ids,
        scoring_version="e2r-v5-researcher-stagecourt",
    )


def _red_team_assessment(
    *,
    target_id: str,
    as_of_date: str,
    transition: StageTransitionContext,
    current_guards: Sequence[str],
    hard_break_claim_ids: Sequence[str],
    mapping_claim_ids: Sequence[str],
) -> RedTeamAssessment:
    if hard_break_claim_ids:
        risk_level = RedTeamRiskLevel.HARD_BREAK
    elif current_guards or transition.thesis_break_score >= 40.0:
        risk_level = RedTeamRiskLevel.HIGH
    elif transition.thesis_break_score >= 20.0:
        risk_level = RedTeamRiskLevel.MODERATE
    else:
        risk_level = RedTeamRiskLevel.LOW
    return RedTeamAssessment(
        symbol=target_id,
        as_of_date=date.fromisoformat(as_of_date),
        soft_4b_score=transition.soft_4b_score,
        soft_4b_status=Soft4BStatus(transition.soft_4b_status),
        thesis_break_score=max(
            transition.thesis_break_score,
            100.0 if hard_break_claim_ids else 40.0 if current_guards else 0.0,
        ),
        risk_level=risk_level,
        has_hard_break=bool(hard_break_claim_ids),
        evidence_ids=_unique_text(
            (*transition.risk_claim_ids, *mapping_claim_ids, *hard_break_claim_ids)
        ),
        version="e2r-v5-researcher-stagecourt",
    )


def _pending_run(
    *,
    target_id: str,
    archetype_id: str,
    as_of_date: str,
    status: str,
    reasons: Sequence[str],
    score_aggregation: DeterministicScoreAggregationRun,
    research_complete: bool,
    counter_thesis_complete: bool,
    event: ResearcherEventOverlay,
    structured_record_ids: tuple[str, ...],
    mappings: tuple[StagePrimitiveMapping, ...] = (),
    mapping_rejections: tuple[Mapping[str, Any], ...] = (),
    prompt_hash: str | None = None,
    response_hash: str | None = None,
) -> ResearcherStageCourtRun:
    score = score_aggregation.total_result.score
    pending = tuple(dict.fromkeys(str(value) for value in reasons if str(value).strip()))
    payload = {
        "target_id": target_id,
        "archetype_id": archetype_id,
        "as_of_date": as_of_date,
        "status": status,
        "pending_reasons": list(pending),
        "mapping_ids": [row.mapping_id for row in mappings],
    }
    trace_id = "STAGECOURT-" + _hash(payload)[:24]
    decision = ResearcherStageCourtDecision(
        decision_id="ADEC5-" + _hash({**payload, "trace_id": trace_id})[:24],
        trace_id=trace_id,
        target_id=target_id,
        archetype_id=archetype_id,
        as_of_date=as_of_date,
        status=status,
        canonical_stage=None,
        score_valid=bool(score_aggregation.score_valid),
        research_complete=research_complete,
        counter_thesis_complete=counter_thesis_complete,
        stage_gates_complete=False,
        total_points=float(score.total_points) if score is not None else None,
        component_vector=dict(score.component_points) if score is not None else {},
        present_positive_primitives=(),
        current_guard_primitives=(),
        hard_break_claim_ids=(),
        score_fact_ids=score.fact_ids if score is not None else (),
        stage_claim_ids=(),
        mapping_ids=tuple(row.mapping_id for row in mappings),
        structured_record_ids=structured_record_ids,
        event_overlay={**event.to_dict(), "canonical_stage_effect": "NONE"},
        stage_reasons=(),
        pending_reasons=pending,
        classifier_version=None,
    )
    audit = _audit(
        decision=decision,
        mappings=mappings,
        mapping_rejections=mapping_rejections,
        contract=None,
        green_gate_satisfied=False,
        blocking_green_guards=(),
        revision_score=0.0,
    )
    return ResearcherStageCourtRun(
        decision=decision,
        mappings=mappings,
        mapping_rejections=mapping_rejections,
        prompt_hash=prompt_hash,
        response_hash=response_hash,
        audit=audit,
    )


def _audit(
    *,
    decision: ResearcherStageCourtDecision,
    mappings: Sequence[StagePrimitiveMapping],
    mapping_rejections: Sequence[Mapping[str, Any]],
    contract: EvidenceContractV2 | None,
    green_gate_satisfied: bool,
    blocking_green_guards: Sequence[str],
    revision_score: float,
) -> Mapping[str, Any]:
    critical_counts = {
        "research_incomplete_count": int(not decision.research_complete),
        "score_invalid_count": int(not decision.score_valid),
        "counter_thesis_incomplete_count": int(not decision.counter_thesis_complete),
        "stage_gate_incomplete_count": int(not decision.stage_gates_complete),
        "mapping_rejection_count": len(mapping_rejections),
        "llm_stage_authority_count": int(decision.llm_stage_authority),
        "final_without_stage_count": int(
            decision.status == _FINAL_STATUS and decision.canonical_stage is None
        ),
        "pending_disguised_as_stage0_count": int(
            decision.status != _FINAL_STATUS and decision.canonical_stage == "0"
        ),
        "hard_break_without_claim_lineage_count": int(
            decision.canonical_stage == "4C" and not decision.hard_break_claim_ids
        ),
        "event_changed_canonical_stage_count": int(
            decision.event_overlay.get("canonical_stage_effect") != "NONE"
        ),
    }
    critical_sum = sum(critical_counts.values())
    return {
        "schema_version": "e2r_v5_stagecourt_audit_v1",
        "status": (
            "STAGECOURT_AUDIT_PASS"
            if decision.status == _FINAL_STATUS and critical_sum == 0
            else "STAGECOURT_AUDIT_PENDING"
        ),
        "target_id": decision.target_id,
        "archetype_id": decision.archetype_id,
        "as_of_date": decision.as_of_date,
        "decision_status": decision.status,
        "canonical_stage": decision.canonical_stage,
        "mapping_count": len(mappings),
        "green_gate_primitive_count": (
            len(contract.green_gate.primitive_ids()) if contract is not None else 0
        ),
        "green_gate_satisfied": green_gate_satisfied,
        "blocking_green_guard_primitives": list(blocking_green_guards),
        "revision_score": revision_score,
        "daily_event_overlay_separate": True,
        "accepted_claim_count_stage_boost": False,
        "llm_score_authority": False,
        "llm_stage_authority": False,
        "critical_counts": critical_counts,
        "critical_count_sum": critical_sum,
    }


def _strings(value: Any) -> tuple[str, ...]:
    if not isinstance(value, (list, tuple)) or isinstance(value, (str, bytes)):
        return ()
    return _unique_text(str(item) for item in value if str(item).strip())


def _unique_text(values: Sequence[str] | Any) -> tuple[str, ...]:
    return tuple(dict.fromkeys(str(value) for value in values if str(value).strip()))


def _hash(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            default=str,
        ).encode()
    ).hexdigest()


def _clean_error(error: Exception) -> str:
    value = " ".join(str(error).split())
    if "usage limit" in value.casefold():
        return "PROVIDER_USAGE_LIMIT"
    return value[-800:] or type(error).__name__


__all__ = [
    "ResearcherEventOverlay",
    "ResearcherStageCourt",
    "ResearcherStageCourtDecision",
    "ResearcherStageCourtRun",
    "STAGECOURT_OUTPUT_FILES",
    "STAGE_GATE_FACT_MAPPING_SCHEMA",
    "StagePrimitiveMapping",
    "StageTransitionContext",
    "write_researcher_stagecourt_run",
]
