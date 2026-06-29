"""Bridge SourceTask execution into Evidence OS v2 ledgers."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from typing import Mapping, Sequence

from e2r.agentic.evidence_os import (
    AdjudicatedClaim,
    AppendOnlyEvidenceLedger,
    Directness,
    EvidenceAnchor,
    EvidenceContractV2,
    EvidenceDocument,
    InvestigationStatus,
    MappingStatus,
    Polarity,
    PrimitiveMappingProposal,
    RawAssertion,
    RelationToTarget,
    SemanticStatus,
    SupportDirection,
    TargetScopeStatus,
    TemporalStatus,
    VerificationStatus,
    derive_score_eligibility,
)
from e2r.agentic.primitive_aggregator import aggregate_primitive_states
from e2r.research_brain.schemas import SourceTask, deterministic_id
from e2r.research_brain.v2_schemas import CandidateEventV2
from e2r.research_brain.v3_schemas import SourceTaskExecutionStatusV3, SourceTaskExecutionV3
from e2r.research_brain.v3_source_acquisition_runner import SourceAcquisitionRunnerV3


@dataclass(frozen=True)
class EvidenceOSExecutionBundleV3:
    ledger: AppendOnlyEvidenceLedger
    executions: tuple[SourceTaskExecutionV3, ...]
    documents: Mapping[str, EvidenceDocument]
    anchors: Mapping[str, EvidenceAnchor]
    document_text_by_id: Mapping[str, str]


def execute_source_tasks_with_evidence_os_v3(
    *,
    event: CandidateEventV2,
    tasks: Sequence[SourceTask],
    contract: EvidenceContractV2,
    as_of_date: date,
    source_runner: SourceAcquisitionRunnerV3 | None = None,
) -> EvidenceOSExecutionBundleV3:
    runner = source_runner or SourceAcquisitionRunnerV3(mode="snapshot")
    ledger = AppendOnlyEvidenceLedger()
    executions: list[SourceTaskExecutionV3] = []
    documents: dict[str, EvidenceDocument] = {}
    anchors: dict[str, EvidenceAnchor] = {}
    document_text_by_id: dict[str, str] = {}
    for task in tasks:
        result = runner.acquire(event=event, task=task, as_of_date=as_of_date)
        for document in result.documents:
            documents[document.document_id] = document
        for anchor in result.anchors:
            anchors[anchor.anchor_id] = anchor
        document_text_by_id.update(dict(result.document_text_by_id or {}))
        if result.status in {"REJECTED_BY_POLICY", "PROVIDER_FAILED", "NO_EVIDENCE_FOUND"}:
            executions.append(
                SourceTaskExecutionV3(
                    task_id=task.task_id,
                    source_task=task.to_dict(),
                    status=result.status,
                    fetched_document_ids=tuple(document.document_id for document in result.documents),
                    evidence_anchor_ids=tuple(anchor.anchor_id for anchor in result.anchors),
                    provider_errors=tuple(result.provider_errors),
                    not_eligible_reasons=tuple(result.not_eligible_reasons),
                    budget_used=dict(result.budget_used or {}),
                    stop_reason=result.stop_reason,
                )
            )
            continue
        execution = _append_claims_for_task(
            event=event,
            task=task,
            contract=contract,
            as_of_date=as_of_date,
            ledger=ledger,
            documents=tuple(result.documents),
            anchors_by_document={anchor.document_id: anchor for anchor in result.anchors},
            provider_errors=tuple(result.provider_errors),
            budget_used=dict(result.budget_used or {}),
            stop_reason=result.stop_reason,
        )
        executions.append(execution)
    return EvidenceOSExecutionBundleV3(
        ledger=ledger,
        executions=tuple(executions),
        documents=documents,
        anchors=anchors,
        document_text_by_id=document_text_by_id,
    )


def primitive_states_from_execution_bundle(
    *,
    bundle: EvidenceOSExecutionBundleV3,
    contract: EvidenceContractV2,
    as_of_date: date,
) -> Mapping[str, object]:
    return aggregate_primitive_states(ledger=bundle.ledger, contract=contract, as_of_date=as_of_date)


def _append_claims_for_task(
    *,
    event: CandidateEventV2,
    task: SourceTask,
    contract: EvidenceContractV2,
    as_of_date: date,
    ledger: AppendOnlyEvidenceLedger,
    documents: Sequence[EvidenceDocument],
    anchors_by_document: Mapping[str, EvidenceAnchor],
    provider_errors: Sequence[str],
    budget_used: Mapping[str, int],
    stop_reason: str,
) -> SourceTaskExecutionV3:
    accepted: list[str] = []
    rejected: list[str] = []
    assertion_ids: list[str] = []
    adjudicated_ids: list[str] = []
    anchor_ids: list[str] = []
    not_eligible: list[str] = []
    for document in documents:
        anchor = anchors_by_document.get(document.document_id)
        if anchor is None:
            continue
        anchor_ids.append(anchor.anchor_id)
        raw = _raw_assertion(event=event, task=task, anchor=anchor)
        assertion_ids.append(raw.raw_assertion_id)
        claim = _adjudicated_claim(event=event, task=task, document=document, anchor=anchor, raw=raw)
        adjudicated_ids.append(claim.claim_id)
        ledger.append_claim(claim)
        mapping_status = MappingStatus.ACCEPTED if task.primitive_gap in _contract_primitive_ids(contract) else MappingStatus.REJECTED
        mapping = PrimitiveMappingProposal.build(
            claim_id=claim.claim_id,
            archetype_id=contract.archetype_id,
            primitive_id=task.primitive_gap,
            support_direction=SupportDirection.SUPPORT,
            mapping_status=mapping_status,
            rationale=f"source_task:{task.task_id}",
            contract_rule_id=task.primitive_gap,
        )
        eligibility = derive_score_eligibility(
            document=document,
            anchor=anchor,
            claim=claim,
            mapping=mapping,
            as_of_date=as_of_date,
            allowed_target_scopes=contract.allowed_target_scopes,
            allowed_directness=contract.allowed_directness,
        )
        if eligibility.eligible and mapping.mapping_status == MappingStatus.ACCEPTED:
            ledger.append_mapping(mapping)
            accepted.append(claim.claim_id)
        else:
            rejected.append(claim.claim_id)
            not_eligible.extend(eligibility.reasons or ("mapping_rejected",))
            rejected_mapping = PrimitiveMappingProposal.build(
                claim_id=claim.claim_id,
                archetype_id=contract.archetype_id,
                primitive_id=task.primitive_gap,
                support_direction=SupportDirection.SUPPORT,
                mapping_status=MappingStatus.REJECTED,
                rationale=";".join(eligibility.reasons or ("mapping_rejected",)),
                contract_rule_id=task.primitive_gap,
            )
            ledger.append_mapping(rejected_mapping)
    status = (
        SourceTaskExecutionStatusV3.EVIDENCE_OS_ACCEPTED.value
        if accepted
        else SourceTaskExecutionStatusV3.NO_EVIDENCE_FOUND.value
    )
    return SourceTaskExecutionV3(
        task_id=task.task_id,
        source_task=task.to_dict(),
        status=status,
        fetched_document_ids=tuple(document.document_id for document in documents),
        evidence_anchor_ids=tuple(anchor_ids),
        raw_assertion_ids=tuple(assertion_ids),
        adjudicated_claim_ids=tuple(adjudicated_ids),
        accepted_claim_ids=tuple(dict.fromkeys(accepted)),
        rejected_claim_ids=tuple(dict.fromkeys(rejected)),
        not_eligible_reasons=tuple(dict.fromkeys(not_eligible)),
        provider_errors=tuple(provider_errors),
        budget_used=dict(budget_used),
        stop_reason=stop_reason if accepted else "no_score_eligible_claim",
    )


def _raw_assertion(*, event: CandidateEventV2, task: SourceTask, anchor: EvidenceAnchor) -> RawAssertion:
    quote = anchor.exact_text or f"{event.company_name} {task.primitive_gap} {event.event_summary}"
    return RawAssertion(
        raw_assertion_id=deterministic_id("RAWASSERTV3", (anchor.anchor_id, event.symbol, task.primitive_gap)),
        anchor_id=anchor.anchor_id,
        subject_text=event.company_name,
        predicate=task.primitive_gap,
        object_text=event.event_summary,
        value=event.event_summary,
        polarity_proposal=Polarity.POSITIVE,
        certainty="source_task_snapshot",
        event_date_text=event.event_date,
        exact_quote=quote,
        related_entity_texts=(event.company_name,),
        extractor_model="research_brain_v3_source_task_bridge",
        extractor_prompt_hash="deterministic_source_task_bridge",
    )


def _adjudicated_claim(
    *,
    event: CandidateEventV2,
    task: SourceTask,
    document: EvidenceDocument,
    anchor: EvidenceAnchor,
    raw: RawAssertion,
) -> AdjudicatedClaim:
    event_date = _date_from_text(event.event_date)
    target_entity_id = f"TICKER:{event.symbol}"
    return AdjudicatedClaim.from_raw(
        raw=raw,
        document=document,
        anchor=anchor,
        subject_entity_id=target_entity_id,
        target_entity_id=target_entity_id,
        relation_to_target=RelationToTarget.SELF,
        directness=Directness.DIRECT if event.issuer_directness == "DIRECT" else Directness.UNKNOWN,
        verification_status=VerificationStatus.SEMANTIC_VERIFIED if anchor.anchor_verified else VerificationStatus.UNVERIFIED,
        target_scope_status=TargetScopeStatus.DIRECT if event.issuer_directness == "DIRECT" else TargetScopeStatus.UNKNOWN,
        polarity=Polarity.POSITIVE,
        temporal_status=TemporalStatus.CURRENT,
        semantic_status=SemanticStatus.PASS_,
        investigation_status=InvestigationStatus.COMPLETE,
        event_date=event_date,
        adjudication_rationale=f"accepted from bounded SourceTask {task.task_id}",
    )


def _contract_primitive_ids(contract: EvidenceContractV2) -> set[str]:
    values = set(contract.required_primitives)
    values.update(contract.green_gate.primitive_ids())
    values.update(contract.alternative_primitives)
    for primitives in contract.alternative_primitives.values():
        values.update(primitives)
    for primitives in contract.score_rubric.values():
        values.update(primitives)
    return values


def _date_from_text(value: str) -> date | None:
    try:
        return datetime.fromisoformat(str(value)[:10]).date()
    except ValueError:
        return None


__all__ = [
    "EvidenceOSExecutionBundleV3",
    "execute_source_tasks_with_evidence_os_v3",
    "primitive_states_from_execution_bundle",
]
