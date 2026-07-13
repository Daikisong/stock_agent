"""Provider-backed full-document extraction for current Researcher Mode.

The LLM proposes explicit economic facts.  Deterministic code verifies target,
as-of date, full-document eligibility, exact-quote lineage, document accounting,
and source identity before the existing EvidenceFactCompiler is allowed to
create canonical facts.  Search snippets and LLM-only assertions never enter
the fact graph.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import write_json, write_jsonl
from e2r.research_brain.intelligence_schema import stable_intelligence_id
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderRejected,
    StructuredProviderUnavailable,
)
from e2r.research_brain.scoring.business_mechanism_scope import (
    ArchetypeMechanismScopeContract,
    BusinessMechanismScope,
    MechanismScopeValidator,
    load_mechanism_scope_contracts,
)

from .component_researcher import StructuredResearchProvider
from .evidence_fact_compiler import EvidenceFactCompiler, FactCompilationResult
from .schemas import (
    CANONICAL_COMPONENT_ORDER,
    EvidenceDirection,
    EvidenceLifecycle,
    assert_blind_research_output,
    scrub_blind_research_payload,
)


FACT_EXTRACTION_OUTPUT_FILES: Mapping[str, str] = {
    "accepted_claims": "material_fact_claims.jsonl",
    "rejections": "fact_extraction_rejections.jsonl",
    "document_dispositions": "fact_document_dispositions.jsonl",
    "provider_calls": "fact_extraction_provider_calls.jsonl",
    "facts": "evidence_facts.jsonl",
    "claim_fact_links": "claim_fact_links.jsonl",
    "result": "fact_extraction_result.json",
    "audit": "fact_extraction_audit.json",
}


@dataclass(frozen=True)
class FactExtractionRejection:
    batch_id: str
    proposal_index: int
    document_id: str
    reason: str
    material_proposal: bool
    proposed_exact_quote: str | None = None
    schema_version: str = "e2r_v5_fact_extraction_rejection_v1"

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class FactExtractionProviderCall:
    batch_id: str
    status: str
    document_ids: tuple[str, ...]
    accepted_claim_ids: tuple[str, ...]
    rejected_proposal_count: int
    document_dispositions: tuple[Mapping[str, Any], ...]
    pending_reasons: tuple[str, ...]
    research_gap_feedback: tuple[str, ...]
    provider_name: str
    prompt_hash: str
    response_hash: str | None
    provider_attempt_count: int = 1
    validation_retry_used: bool = False
    schema_version: str = "e2r_v5_fact_extraction_provider_call_v1"

    def __post_init__(self) -> None:
        if self.status not in {"COMPLETE", "PENDING"}:
            raise ValueError("unknown fact extraction provider-call status")
        if self.status == "PENDING" and not self.pending_reasons:
            raise ValueError("pending fact extraction call requires reasons")
        if self.provider_attempt_count <= 0:
            raise ValueError("fact extraction provider attempt count must be positive")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            **asdict(self),
            "document_dispositions": [dict(row) for row in self.document_dispositions],
        }


@dataclass(frozen=True)
class ResearcherFactExtractionResult:
    target_id: str
    as_of_date: str
    status: str
    material_claims: tuple[Mapping[str, Any], ...]
    fact_compilation: FactCompilationResult
    provider_calls: tuple[FactExtractionProviderCall, ...]
    rejections: tuple[FactExtractionRejection, ...]
    document_dispositions: tuple[Mapping[str, Any], ...]
    pending_reasons: tuple[str, ...]
    research_gap_feedback: tuple[str, ...]
    audit: Mapping[str, Any]
    production_score_authority: bool = False
    schema_version: str = "e2r_v5_researcher_fact_extraction_v1"

    def __post_init__(self) -> None:
        if self.status not in {"FACT_EXTRACTION_COMPLETE", "FACT_EXTRACTION_PENDING"}:
            raise ValueError("unknown Researcher fact extraction status")
        if self.status == "FACT_EXTRACTION_PENDING" and not self.pending_reasons:
            raise ValueError("pending fact extraction requires reasons")
        if self.production_score_authority:
            raise ValueError("fact extraction cannot assign production score")

    @property
    def facts(self):
        return self.fact_compilation.facts

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "target_id": self.target_id,
            "as_of_date": self.as_of_date,
            "status": self.status,
            "material_claims": [dict(row) for row in self.material_claims],
            "fact_compilation": self.fact_compilation.to_dict(),
            "provider_calls": [row.to_dict() for row in self.provider_calls],
            "rejections": [row.to_dict() for row in self.rejections],
            "document_dispositions": [dict(row) for row in self.document_dispositions],
            "pending_reasons": list(self.pending_reasons),
            "research_gap_feedback": list(self.research_gap_feedback),
            "audit": dict(self.audit),
            "production_score_authority": False,
        }


class ResearcherEvidenceFactExtractor:
    """Extract and verify facts from every supplied full document.

    ``documents_per_call`` is only a prompt-transport chunk size.  Every input
    document is processed, so it cannot become a research-completion cap.
    """

    def __init__(
        self,
        *,
        provider: StructuredResearchProvider,
        documents_per_call: int = 3,
        max_document_chars_per_call: int = 220_000,
    ) -> None:
        if isinstance(documents_per_call, bool) or documents_per_call <= 0:
            raise ValueError("documents_per_call must be a positive transport chunk")
        if (
            isinstance(max_document_chars_per_call, bool)
            or max_document_chars_per_call < 10_000
        ):
            raise ValueError("fact extraction character transport bound is too small")
        self.provider = provider
        self.documents_per_call = documents_per_call
        self.max_document_chars_per_call = max_document_chars_per_call

    def extract(
        self,
        *,
        target_id: str,
        target_name: str,
        target_aliases: Sequence[str],
        archetype_id: str,
        as_of_date: str,
        documents: Sequence[Mapping[str, Any]],
        open_objectives: Sequence[Mapping[str, Any]],
        current_facts: Sequence[Mapping[str, Any]] = (),
        score_gap_context: Mapping[str, Any] | None = None,
        prior_material_claims: Sequence[Mapping[str, Any]] = (),
        prior_document_dispositions: Sequence[Mapping[str, Any]] = (),
        prior_provider_calls: Sequence[
            FactExtractionProviderCall | Mapping[str, Any]
        ] = (),
        prior_rejections: Sequence[
            FactExtractionRejection | Mapping[str, Any]
        ] = (),
    ) -> ResearcherFactExtractionResult:
        cutoff = date.fromisoformat(as_of_date)
        if not target_id.strip() or not target_name.strip() or not archetype_id.strip():
            raise ValueError("fact extraction target identity is incomplete")
        prepared = _validate_documents(
            documents,
            target_id=target_id,
            as_of_date=as_of_date,
            cutoff=cutoff,
        )
        scope_contract = load_mechanism_scope_contracts().get(archetype_id)
        if scope_contract is None:
            raise ValueError("fact extraction archetype lacks mechanism-scope contract")
        document_ids = {str(row["document_id"]) for row in prepared}
        dispositions: list[Mapping[str, Any]] = [
            dict(row) for row in prior_document_dispositions
        ]
        prior_disposition_ids = [
            str(row.get("document_id") or "") for row in dispositions
        ]
        if (
            any(not value or value not in document_ids for value in prior_disposition_ids)
            or len(prior_disposition_ids) != len(set(prior_disposition_ids))
        ):
            raise ValueError("prior fact dispositions are stale or duplicated")
        claims: list[Mapping[str, Any]] = [dict(row) for row in prior_material_claims]
        claim_ids = [str(row.get("claim_id") or "") for row in claims]
        if any(not value for value in claim_ids) or len(claim_ids) != len(set(claim_ids)):
            raise ValueError("prior material claims require unique ids")
        if any(
            str(row.get("document_id") or "") not in set(prior_disposition_ids)
            or str(row.get("target_id") or "") != target_id
            or str(row.get("as_of_date") or "") != as_of_date
            for row in claims
        ):
            raise ValueError("prior material claims are outside resumed document scope")
        rejections: list[FactExtractionRejection] = [
            _coerce_rejection(row) for row in prior_rejections
        ]
        calls: list[FactExtractionProviderCall] = [
            _coerce_provider_call(row) for row in prior_provider_calls
        ]
        if any(row.status != "COMPLETE" for row in calls):
            raise ValueError("only completed fact provider calls may be resumed")
        pending: list[str] = []
        research_gap_feedback: list[str] = [
            reason for row in calls for reason in row.research_gap_feedback
        ]
        provider_name = str(
            getattr(self.provider, "provider_name", type(self.provider).__name__)
        )
        remaining = tuple(
            row
            for row in prepared
            if str(row["document_id"]) not in set(prior_disposition_ids)
        )
        for batch in _document_batches(
            remaining,
            max_documents=self.documents_per_call,
            max_chars=self.max_document_chars_per_call,
        ):
            batch_id = stable_intelligence_id(
                "FACTBATCH",
                {
                    "target_id": target_id,
                    "as_of_date": as_of_date,
                    "document_ids": [str(row["document_id"]) for row in batch],
                },
            )
            payload = scrub_blind_research_payload(
                {
                    "target_id": target_id,
                    "target_name": target_name,
                    "target_aliases": list(target_aliases),
                    "archetype_hypothesis": archetype_id,
                    "as_of_date": as_of_date,
                    "open_research_objectives": [dict(row) for row in open_objectives],
                    "current_evidence_facts": [dict(row) for row in current_facts],
                    "score_gap_context": dict(score_gap_context or {}),
                    "normalization_contract": {
                        "question_family_id": "stable semantic research-question family, not a query string",
                        "subject_id": "stable target business/product/mechanism subject",
                        "predicate_family": "stable economic predicate family",
                        "normalized_object": "concise normalized economic object or state",
                        "mechanism_scope_id": "target-direct business mechanism, never industry or wrong-segment proxy",
                    },
                    "deterministic_mechanism_scope_contract": {
                        "allowed_business_segments": list(scope_contract.allowed_business_segments),
                        "allowed_product_families": list(scope_contract.allowed_product_families),
                        "allowed_technology_families": list(scope_contract.allowed_technology_families),
                        "allowed_transaction_types": list(scope_contract.allowed_transaction_types),
                        "allowed_economic_mechanisms": list(scope_contract.allowed_economic_mechanisms),
                        "generic_company_allowed_components": list(scope_contract.generic_company_allowed_components),
                        "forbidden_business_segments": list(scope_contract.forbidden_business_segments),
                        "forbidden_product_families": list(scope_contract.forbidden_product_families),
                        "issuer_wide_fact_encoding": {
                            "scope_business_segment": "CORPORATE_GENERIC",
                            "scope_product_family": "CORPORATE_GENERIC",
                            "scope_technology_family": "CORPORATE_GENERIC",
                            "scope_transaction_type": "GENERIC_INFORMATION",
                            "scope_economic_mechanism": "INFORMATION_ONLY",
                            "allowed_only_for_components": list(
                                scope_contract.generic_company_allowed_components
                            ),
                            "instruction": (
                                "Use these exact scope tokens for issuer-wide liquidity, "
                                "capital allocation, funding, governance, or information-quality "
                                "facts that are not attributable to the archetype business segment."
                            ),
                        },
                    },
                    "full_documents": [_document_prompt_row(row) for row in batch],
                }
            )
            attempt_payload = payload
            provider_attempt_count = 0
            validation_retry_used = False
            while True:
                prompt_hash = stable_intelligence_id(
                    "FACTPROMPT", attempt_payload
                )
                provider_attempt_count += 1
                try:
                    response = self.provider.complete(
                        pass_name="EVIDENCE_FACT_EXTRACTION",
                        payload=attempt_payload,
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
                    reason = (
                        "FACT_EXTRACTION_PROVIDER_OR_OUTPUT_ERROR:"
                        f"{type(exc).__name__}:{_clean_error(exc)}"
                    )
                    pending.append(reason)
                    calls.append(
                        FactExtractionProviderCall(
                            batch_id=batch_id,
                            status="PENDING",
                            document_ids=tuple(
                                str(row["document_id"]) for row in batch
                            ),
                            accepted_claim_ids=(),
                            rejected_proposal_count=0,
                            document_dispositions=(),
                            pending_reasons=(reason,),
                            research_gap_feedback=(),
                            provider_name=provider_name,
                            prompt_hash=prompt_hash,
                            response_hash=None,
                            provider_attempt_count=provider_attempt_count,
                            validation_retry_used=validation_retry_used,
                        )
                    )
                    break
                response_hash = stable_intelligence_id(
                    "FACTRESP", scrub_blind_research_payload(response)
                )
                (
                    batch_claims,
                    batch_rejections,
                    batch_dispositions,
                    batch_pending,
                    batch_feedback,
                ) = _validate_response(
                    response,
                    batch_id=batch_id,
                    documents=batch,
                    target_id=target_id,
                    as_of_date=as_of_date,
                    scope_contract=scope_contract,
                    provider_name=provider_name,
                    prompt_hash=prompt_hash,
                    response_hash=response_hash,
                )
                if batch_pending and not validation_retry_used:
                    validation_retry_used = True
                    attempt_payload = scrub_blind_research_payload(
                        {
                            **payload,
                            "fact_extraction_retry_context": {
                                "validation_errors": list(batch_pending),
                                "rejected_proposals": [
                                    {
                                        "proposal_index": row.proposal_index,
                                        "document_id": row.document_id,
                                        "reason": row.reason,
                                        "proposed_exact_quote": (
                                            row.proposed_exact_quote
                                        ),
                                    }
                                    for row in batch_rejections
                                    if row.material_proposal
                                    and not row.reason.startswith(
                                        "MECHANISM_SCOPE_REJECTED"
                                    )
                                ],
                                "required_document_ids": [
                                    str(row["document_id"]) for row in batch
                                ],
                                "instruction": (
                                    "Rewrite the complete batch. Every material "
                                    "exact_quote must be copied as one literal "
                                    "contiguous substring from that document's "
                                    "content_text. Delete any unsupported proposal; "
                                    "do not paraphrase or repair quotes in code."
                                ),
                            },
                        }
                    )
                    continue
                claims.extend(batch_claims)
                rejections.extend(batch_rejections)
                dispositions.extend(batch_dispositions)
                pending.extend(batch_pending)
                research_gap_feedback.extend(batch_feedback)
                calls.append(
                    FactExtractionProviderCall(
                        batch_id=batch_id,
                        status="PENDING" if batch_pending else "COMPLETE",
                        document_ids=tuple(
                            str(row["document_id"]) for row in batch
                        ),
                        accepted_claim_ids=tuple(
                            str(row["claim_id"]) for row in batch_claims
                        ),
                        rejected_proposal_count=len(batch_rejections),
                        document_dispositions=tuple(batch_dispositions),
                        pending_reasons=tuple(batch_pending),
                        research_gap_feedback=tuple(batch_feedback),
                        provider_name=provider_name,
                        prompt_hash=prompt_hash,
                        response_hash=response_hash,
                        provider_attempt_count=provider_attempt_count,
                        validation_retry_used=validation_retry_used,
                    )
                )
                break
        compilation = EvidenceFactCompiler().compile(
            target_id=target_id,
            as_of_date=as_of_date,
            accepted_claims=claims,
        )
        if compilation.status != "FACT_COMPILATION_COMPLETE":
            pending.append(compilation.status)
        pending = list(dict.fromkeys(pending))
        research_gap_feedback.extend(
            f"FACT_EXTRACTION_RETRY_CONTEXT:{reason}" for reason in pending
        )
        critical_counts = {
            "snippet_or_non_full_document_input_count": sum(
                bool(row.get("snippet_only"))
                or not bool(row.get("full_fetch_performed"))
                or not bool(row.get("evidence_eligible"))
                for row in prepared
            ),
            "unaccounted_document_count": max(0, len(prepared) - len(dispositions)),
            "duplicate_document_disposition_count": max(
                0,
                len(dispositions)
                - len({str(row.get("document_id") or "") for row in dispositions}),
            ),
            "material_proposal_rejection_count": sum(
                row.material_proposal
                and not row.reason.startswith("MECHANISM_SCOPE_REJECTED")
                for row in rejections
            ),
            "accepted_claim_without_fact_count": (
                compilation.accepted_claim_without_fact_count
            ),
            "provider_or_semantic_pending_count": len(pending),
            "future_source_count": sum(
                date.fromisoformat(str(row["published_at"])[:10]) > cutoff
                for row in prepared
            ),
        }
        critical_sum = sum(critical_counts.values())
        complete = critical_sum == 0 and all(
            row.status == "COMPLETE" for row in calls
        )
        audit = {
            "schema_version": "e2r_v5_fact_extraction_audit_v1",
            "status": "FACT_EXTRACTION_AUDIT_PASS" if complete else "FACT_EXTRACTION_AUDIT_PENDING",
            "target_id": target_id,
            "as_of_date": as_of_date,
            "input_document_count": len(prepared),
            "provider_call_count": len(calls),
            "provider_attempt_count": sum(
                row.provider_attempt_count for row in calls
            ),
            "validation_retry_call_count": sum(
                row.validation_retry_used for row in calls
            ),
            "transport_chunk_size": self.documents_per_call,
            "transport_character_bound": self.max_document_chars_per_call,
            "transport_chunk_is_completion_cap": False,
            "accepted_material_claim_count": len(claims),
            "compiled_fact_count": len(compilation.facts),
            "counterfact_count": sum(
                row.direction == EvidenceDirection.COUNTER.value
                for row in compilation.facts
            ),
            "research_gap_feedback_count": len(
                tuple(dict.fromkeys(research_gap_feedback))
            ),
            "wrong_mechanism_terminal_count": sum(
                row.reason.startswith("MECHANISM_SCOPE_REJECTED")
                for row in rejections
            ),
            "snippet_is_evidence": False,
            "llm_score_authority": False,
            "llm_stage_authority": False,
            "critical_counts": critical_counts,
            "critical_count_sum": critical_sum,
        }
        return ResearcherFactExtractionResult(
            target_id=target_id,
            as_of_date=as_of_date,
            status=(
                "FACT_EXTRACTION_COMPLETE"
                if complete
                else "FACT_EXTRACTION_PENDING"
            ),
            material_claims=tuple(claims),
            fact_compilation=compilation,
            provider_calls=tuple(calls),
            rejections=tuple(rejections),
            document_dispositions=tuple(dispositions),
            pending_reasons=tuple(pending),
            research_gap_feedback=tuple(dict.fromkeys(research_gap_feedback)),
            audit=audit,
        )


def write_researcher_fact_extraction_result(
    result: ResearcherFactExtractionResult,
    output_directory: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_directory)
    paths = {
        key: root / filename for key, filename in FACT_EXTRACTION_OUTPUT_FILES.items()
    }
    write_jsonl(paths["accepted_claims"], result.material_claims)
    write_jsonl(paths["rejections"], (row.to_dict() for row in result.rejections))
    write_jsonl(paths["document_dispositions"], result.document_dispositions)
    write_jsonl(paths["provider_calls"], (row.to_dict() for row in result.provider_calls))
    write_jsonl(paths["facts"], (row.to_dict() for row in result.facts))
    write_jsonl(
        paths["claim_fact_links"],
        (row.to_dict() for row in result.fact_compilation.claim_fact_links),
    )
    write_json(paths["result"], result.to_dict())
    write_json(paths["audit"], result.audit)
    return paths


def production_material_fact_rows(
    result: ResearcherFactExtractionResult,
) -> tuple[Mapping[str, Any], ...]:
    """Project verified claims into the isolated Phase 93 comparison contract."""

    claim_by_id = {
        str(row["claim_id"]): row for row in result.material_claims
    }
    output = []
    for fact in result.facts:
        primary = claim_by_id[str(fact.claim_ids[0])]
        output.append(
            {
                "schema_version": "e2r_v5_production_material_fact_v1",
                "fact_id": fact.fact_id,
                "target_id": fact.target_id,
                "question_family_id": primary["question_family_id"],
                "subject_id": primary["subject_id"],
                "predicate_family": primary["predicate_family"],
                "normalized_object": primary["normalized_object"],
                "period": fact.period,
                "mechanism_scope_id": primary["mechanism_scope_id"],
                "source_id": fact.source_ids[0],
                "source_ids": list(fact.source_ids),
                "source_tier": primary["source_tier"],
                "temporal_status": "CURRENT",
                "as_of_date": fact.as_of_date,
                "materiality": primary["materiality"],
                "fact_role": (
                    "SUPERSESSION"
                    if fact.current_lifecycle == EvidenceLifecycle.SUPERSEDED.value
                    else "COUNTER"
                    if fact.direction == EvidenceDirection.COUNTER.value
                    else "SUPPORT"
                ),
                "economic_mechanism": fact.economic_mechanism,
                "predicate": fact.predicate,
                "value": fact.value,
                "confidence": fact.confidence,
                "claim_ids": list(fact.claim_ids),
                "quote_ids": list(fact.quote_ids),
                "gold_visibility": False,
            }
        )
    return tuple(output)


def _document_batches(
    documents: Sequence[Mapping[str, Any]],
    *,
    max_documents: int,
    max_chars: int,
) -> tuple[tuple[Mapping[str, Any], ...], ...]:
    batches: list[tuple[Mapping[str, Any], ...]] = []
    current: list[Mapping[str, Any]] = []
    current_chars = 0
    for document in documents:
        chars = len(str(document.get("content_text") or ""))
        if current and (
            len(current) >= max_documents or current_chars + chars > max_chars
        ):
            batches.append(tuple(current))
            current = []
            current_chars = 0
        current.append(document)
        current_chars += chars
    if current:
        batches.append(tuple(current))
    return tuple(batches)


def _validate_documents(
    documents: Sequence[Mapping[str, Any]],
    *,
    target_id: str,
    as_of_date: str,
    cutoff: date,
) -> tuple[Mapping[str, Any], ...]:
    rows = tuple(dict(row) for row in documents)
    ids = [str(row.get("document_id") or "") for row in rows]
    if not rows:
        return ()
    if any(not value for value in ids) or len(ids) != len(set(ids)):
        raise ValueError("fact extraction documents require unique ids")
    for row in rows:
        if str(row.get("target_id") or "") != target_id:
            raise ValueError("fact extraction received a cross-target document")
        if str(row.get("as_of_date") or "") != as_of_date:
            raise ValueError("fact extraction document as_of_date mismatch")
        if (
            not row.get("full_fetch_performed")
            or row.get("snippet_only")
            or row.get("snippet_used_as_document")
            or not row.get("evidence_eligible")
        ):
            raise ValueError("fact extraction requires full evidence-eligible documents")
        published = date.fromisoformat(str(row.get("published_at") or "")[:10])
        available = date.fromisoformat(str(row.get("available_at") or "")[:10])
        if published > cutoff or available > cutoff:
            raise ValueError("future document cannot enter fact extraction")
        text = str(row.get("content_text") or "")
        if not text.strip() or hashlib.sha256(text.encode("utf-8")).hexdigest() != str(
            row.get("content_hash") or ""
        ):
            raise ValueError("fact extraction document content/hash mismatch")
    return rows


def _document_prompt_row(row: Mapping[str, Any]) -> Mapping[str, Any]:
    return {
        "document_id": row["document_id"],
        "canonical_url": row["canonical_url"],
        "title": row.get("title"),
        "source_family": row["source_family"],
        "published_at": row["published_at"],
        "available_at": row["available_at"],
        "source_independence_group": row["source_independence_group"],
        "objective_ids": list(row.get("objective_ids") or ()),
        "content_text": row["content_text"],
        "full_fetch_performed": True,
        "snippet_used_as_document": False,
    }


def _validate_response(
    response: Mapping[str, Any],
    *,
    batch_id: str,
    documents: Sequence[Mapping[str, Any]],
    target_id: str,
    as_of_date: str,
    scope_contract: ArchetypeMechanismScopeContract,
    provider_name: str,
    prompt_hash: str,
    response_hash: str,
) -> tuple[
    list[Mapping[str, Any]],
    list[FactExtractionRejection],
    list[Mapping[str, Any]],
    list[str],
    list[str],
]:
    document_by_id = {str(row["document_id"]): row for row in documents}
    raw_facts = response.get("facts")
    raw_dispositions = response.get("document_dispositions")
    unresolved = response.get("unresolved_document_ids")
    notes = response.get("unresolved_research_notes")
    if any(
        isinstance(value, (str, bytes)) or not isinstance(value, Sequence)
        for value in (raw_facts, raw_dispositions, unresolved, notes)
    ):
        raise TypeError("fact extraction arrays are malformed")
    claims: list[Mapping[str, Any]] = []
    rejections: list[FactExtractionRejection] = []
    pending: list[str] = []
    feedback: list[str] = []
    accepted_by_document: dict[str, int] = {}
    for index, proposal in enumerate(raw_facts):
        document_id = (
            str(proposal.get("document_id") or "")
            if isinstance(proposal, Mapping)
            else ""
        )
        material = bool(proposal.get("material")) if isinstance(proposal, Mapping) else False
        reason = _proposal_rejection_reason(
            proposal,
            document_by_id=document_by_id,
            target_id=target_id,
            scope_contract=scope_contract,
        )
        if reason:
            rejections.append(
                FactExtractionRejection(
                    batch_id=batch_id,
                    proposal_index=index,
                    document_id=document_id,
                    reason=reason,
                    material_proposal=material,
                    proposed_exact_quote=(
                        str(proposal.get("exact_quote") or "").strip() or None
                        if isinstance(proposal, Mapping)
                        else None
                    ),
                )
            )
            if material and not reason.startswith("MECHANISM_SCOPE_REJECTED"):
                pending.append(f"MATERIAL_FACT_PROPOSAL_REJECTED:{document_id}:{reason}")
            continue
        assert isinstance(proposal, Mapping)
        if not material:
            rejections.append(
                FactExtractionRejection(
                    batch_id=batch_id,
                    proposal_index=index,
                    document_id=document_id,
                    reason="IMMATERIAL_PROPOSAL_TERMINAL",
                    material_proposal=False,
                    proposed_exact_quote=(
                        str(proposal.get("exact_quote") or "").strip() or None
                    ),
                )
            )
            continue
        document = document_by_id[document_id]
        allowed_component_ids, _ = _allowed_components(
            proposal,
            target_id=target_id,
            scope_contract=scope_contract,
        )
        claim = _accepted_claim(
            proposal,
            document=document,
            target_id=target_id,
            as_of_date=as_of_date,
            provider_name=provider_name,
            prompt_hash=prompt_hash,
            response_hash=response_hash,
            allowed_component_ids=allowed_component_ids,
        )
        claims.append(claim)
        accepted_by_document[document_id] = accepted_by_document.get(document_id, 0) + 1
    dispositions: list[Mapping[str, Any]] = []
    disposition_ids: list[str] = []
    for raw in raw_dispositions:
        if not isinstance(raw, Mapping):
            pending.append("INVALID_DOCUMENT_DISPOSITION_OBJECT")
            continue
        document_id = str(raw.get("document_id") or "")
        status = str(raw.get("status") or "")
        rationale = str(raw.get("rationale") or "").strip()
        if document_id not in document_by_id:
            pending.append(f"UNKNOWN_DOCUMENT_DISPOSITION:{document_id}")
            continue
        if status not in {
            "FACTS_EXTRACTED",
            "NO_MATERIAL_FACT",
            "WRONG_TARGET_OR_SEGMENT",
            "UNREADABLE",
        } or not rationale:
            pending.append(f"INVALID_DOCUMENT_DISPOSITION:{document_id}")
            continue
        if status == "FACTS_EXTRACTED" and not accepted_by_document.get(document_id):
            pending.append(f"FACTS_EXTRACTED_WITHOUT_ACCEPTED_FACT:{document_id}")
        if status != "FACTS_EXTRACTED" and accepted_by_document.get(document_id):
            pending.append(f"ACCEPTED_FACT_DISPOSITION_MISMATCH:{document_id}")
        if status == "UNREADABLE":
            pending.append(f"UNREADABLE_FULL_DOCUMENT:{document_id}")
        dispositions.append(
            {
                "schema_version": "e2r_v5_fact_document_disposition_v1",
                "batch_id": batch_id,
                "document_id": document_id,
                "status": status,
                "rationale": rationale,
                "accepted_fact_count": accepted_by_document.get(document_id, 0),
                "source_absence_proven": False,
                "production_score_authority": False,
            }
        )
        disposition_ids.append(document_id)
    expected_ids = set(document_by_id)
    if set(disposition_ids) != expected_ids or len(disposition_ids) != len(expected_ids):
        pending.append("EVERY_DOCUMENT_REQUIRES_EXACTLY_ONE_DISPOSITION")
    unresolved_ids = tuple(str(value).strip() for value in unresolved if str(value).strip())
    if set(unresolved_ids) - expected_ids:
        pending.append("UNRESOLVED_DOCUMENT_ID_OUTSIDE_BATCH")
    if unresolved_ids:
        pending.extend(f"UNRESOLVED_DOCUMENT:{value}" for value in unresolved_ids)
    feedback.extend(
        f"UNRESOLVED_RESEARCH_NOTE:{str(value).strip()}"
        for value in notes
        if str(value).strip()
    )
    if response.get("extraction_complete") is not True:
        pending.append("LLM_DECLARED_FACT_EXTRACTION_INCOMPLETE")
    return (
        claims,
        rejections,
        dispositions,
        list(dict.fromkeys(pending)),
        list(dict.fromkeys(feedback)),
    )


def _proposal_rejection_reason(
    proposal: Any,
    *,
    document_by_id: Mapping[str, Mapping[str, Any]],
    target_id: str,
    scope_contract: ArchetypeMechanismScopeContract,
) -> str | None:
    if not isinstance(proposal, Mapping):
        return "FACT_PROPOSAL_NOT_OBJECT"
    document_id = str(proposal.get("document_id") or "")
    if document_id not in document_by_id:
        return "UNKNOWN_DOCUMENT_ID"
    required = (
        "question_family_id",
        "subject_id",
        "subject",
        "business_segment",
        "product_family",
        "scope_business_segment",
        "scope_product_family",
        "scope_technology_family",
        "scope_transaction_type",
        "scope_economic_mechanism",
        "economic_mechanism",
        "mechanism_scope_id",
        "predicate",
        "predicate_family",
        "value",
        "normalized_object",
        "period",
        "exact_quote",
        "materiality_rationale",
    )
    missing = [key for key in required if not str(proposal.get(key) or "").strip()]
    if missing:
        return "EXPLICIT_FACT_FIELDS_MISSING:" + ",".join(missing)
    try:
        EvidenceDirection(str(proposal.get("direction") or ""))
        EvidenceLifecycle(str(proposal.get("current_lifecycle") or ""))
        confidence = float(proposal.get("confidence"))
        if not math.isfinite(confidence) or not 0 <= confidence <= 1:
            raise ValueError("confidence")
    except (TypeError, ValueError):
        return "INVALID_FACT_ENUM_OR_CONFIDENCE"
    if str(proposal.get("materiality") or "") not in {"CRITICAL", "NONCRITICAL"}:
        return "INVALID_MATERIALITY"
    allowed_component_ids, scope_reasons = _allowed_components(
        proposal,
        target_id=target_id,
        scope_contract=scope_contract,
    )
    if not allowed_component_ids:
        return "MECHANISM_SCOPE_REJECTED:" + ",".join(scope_reasons)
    quote = str(proposal.get("exact_quote") or "").strip()
    if quote not in str(document_by_id[document_id].get("content_text") or ""):
        return "EXACT_QUOTE_NOT_IN_FULL_DOCUMENT"
    return None


def _accepted_claim(
    proposal: Mapping[str, Any],
    *,
    document: Mapping[str, Any],
    target_id: str,
    as_of_date: str,
    provider_name: str,
    prompt_hash: str,
    response_hash: str,
    allowed_component_ids: Sequence[str],
) -> Mapping[str, Any]:
    identity = {
        "target_id": target_id,
        "as_of_date": as_of_date,
        "document_id": document["document_id"],
        "question_family_id": proposal["question_family_id"],
        "subject_id": proposal["subject_id"],
        "predicate_family": proposal["predicate_family"],
        "normalized_object": proposal["normalized_object"],
        "period": proposal["period"],
        "mechanism_scope_id": proposal["mechanism_scope_id"],
        "exact_quote": proposal["exact_quote"],
    }
    claim_id = stable_intelligence_id("RFC", identity)
    source_family = str(document.get("source_family") or "")
    return {
        "schema_version": "e2r_v5_researcher_material_claim_v1",
        "claim_id": claim_id,
        "target_id": target_id,
        "as_of_date": as_of_date,
        "accepted": True,
        "accepted_by_evidence_os": True,
        "material": True,
        "materiality": proposal["materiality"],
        "question_family_id": str(proposal["question_family_id"]).strip(),
        "subject_id": str(proposal["subject_id"]).strip(),
        "subject": str(proposal["subject"]).strip(),
        "business_segment": str(proposal["business_segment"]).strip(),
        "product_family": str(proposal["product_family"]).strip(),
        "scope_business_segment": str(proposal["scope_business_segment"]).strip(),
        "scope_product_family": str(proposal["scope_product_family"]).strip(),
        "scope_technology_family": str(proposal["scope_technology_family"]).strip(),
        "scope_transaction_type": str(proposal["scope_transaction_type"]).strip(),
        "scope_economic_mechanism": str(proposal["scope_economic_mechanism"]).strip(),
        "scope_confidence": float(proposal["scope_confidence"]),
        "economic_mechanism": str(proposal["economic_mechanism"]).strip(),
        "mechanism_scope_id": str(proposal["mechanism_scope_id"]).strip(),
        "predicate": str(proposal["predicate"]).strip(),
        "predicate_family": str(proposal["predicate_family"]).strip(),
        "value": str(proposal["value"]).strip(),
        "normalized_object": str(proposal["normalized_object"]).strip(),
        "unit": str(proposal.get("unit") or "").strip() or None,
        "period": str(proposal["period"]).strip(),
        "direction": str(proposal["direction"]),
        "current_lifecycle": str(proposal["current_lifecycle"]),
        "source_ids": [str(document["document_id"])],
        "document_id": str(document["document_id"]),
        "canonical_url": str(document["canonical_url"]),
        "published_at": str(document["published_at"]),
        "available_at": str(document["available_at"]),
        "exact_quote": str(proposal["exact_quote"]).strip(),
        "source_independence_group": str(
            document["source_independence_group"]
        ),
        "source_family": source_family,
        "source_tier": _source_tier(source_family),
        "confidence": float(proposal["confidence"]),
        "question_family_tags": list(
            dict.fromkeys(
                (
                    str(proposal["question_family_id"]).strip(),
                    *(str(value).strip() for value in proposal.get("question_family_tags") or ()),
                )
            )
        ),
        "primitive_tags": list(
            dict.fromkeys(
                str(value).strip()
                for value in proposal.get("primitive_tags") or ()
                if str(value).strip()
            )
        ),
        "structured_evidence_roles": list(
            dict.fromkeys(
                str(value).strip()
                for value in proposal.get("structured_evidence_roles") or ()
                if str(value).strip()
            )
        ),
        "allowed_component_ids": list(allowed_component_ids),
        "materiality_rationale": str(proposal["materiality_rationale"]).strip(),
        "provider_name": provider_name,
        "provider_prompt_hash": prompt_hash,
        "provider_response_hash": response_hash,
        "llm_score_authority": False,
        "llm_stage_authority": False,
    }


def _allowed_components(
    proposal: Mapping[str, Any],
    *,
    target_id: str,
    scope_contract: ArchetypeMechanismScopeContract,
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    try:
        scope_confidence = float(proposal.get("scope_confidence"))
        if not math.isfinite(scope_confidence) or not 0 <= scope_confidence <= 1:
            raise ValueError("scope_confidence")
        scope = BusinessMechanismScope(
            issuer_id=target_id,
            business_segment=str(proposal.get("scope_business_segment") or ""),
            product_family=str(proposal.get("scope_product_family") or ""),
            technology_family=str(proposal.get("scope_technology_family") or ""),
            customer_or_counterparty="",
            transaction_type=str(proposal.get("scope_transaction_type") or ""),
            economic_mechanism=str(proposal.get("scope_economic_mechanism") or ""),
            geography="UNSPECIFIED",
            effective_period=str(proposal.get("period") or ""),
            scope_confidence=scope_confidence,
        )
    except (TypeError, ValueError):
        return (), ("INVALID_SCOPE_FIELDS",)
    validator = MechanismScopeValidator()
    validations = tuple(
        validator.validate(
            scope=scope,
            contract=scope_contract,
            component_id=component_id,
        )
        for component_id in CANONICAL_COMPONENT_ORDER
    )
    allowed = tuple(
        component_id
        for component_id, validation in zip(
            CANONICAL_COMPONENT_ORDER, validations
        )
        if validation.scope_match
    )
    reasons = tuple(
        dict.fromkeys(
            validation.reason_code
            for validation in validations
            if validation.reason_code
        )
    )
    return allowed, reasons


def _source_tier(source_family: str) -> str:
    if source_family in {"OPENDART", "KIND_KRX"}:
        return "REGULATORY_OFFICIAL"
    if source_family in {
        "ISSUER_EARNINGS_RELEASE",
        "ISSUER_PRESENTATION",
        "ISSUER_NEWSROOM",
        "FINANCIAL_STATEMENTS",
        "SEGMENT_DATA",
        "CASH_FLOW",
    }:
        return "ISSUER_OFFICIAL"
    if source_family == "CUSTOMER_OFFICIAL":
        return "CUSTOMER_OFFICIAL"
    if source_family in {"CONSENSUS_REVISION", "VALUATION_MULTIPLES"}:
        return "FINANCIAL_REVISION"
    if source_family in {
        "REUTERS",
        "TRUSTED_BUSINESS_MEDIA",
        "PUBLIC_BROKER_PDF",
        "INDUSTRY_REPORT",
    }:
        return "TRUSTED_INDEPENDENT"
    return "GENERAL_WEB"


def _clean_error(error: Exception) -> str:
    return " ".join(str(error).split())[-800:] or type(error).__name__


def _coerce_provider_call(
    row: FactExtractionProviderCall | Mapping[str, Any],
) -> FactExtractionProviderCall:
    if isinstance(row, FactExtractionProviderCall):
        return row
    return FactExtractionProviderCall(
        batch_id=str(row["batch_id"]),
        status=str(row["status"]),
        document_ids=tuple(row.get("document_ids") or ()),
        accepted_claim_ids=tuple(row.get("accepted_claim_ids") or ()),
        rejected_proposal_count=int(row.get("rejected_proposal_count") or 0),
        document_dispositions=tuple(
            dict(value) for value in row.get("document_dispositions") or ()
        ),
        pending_reasons=tuple(row.get("pending_reasons") or ()),
        research_gap_feedback=tuple(row.get("research_gap_feedback") or ()),
        provider_name=str(row["provider_name"]),
        prompt_hash=str(row["prompt_hash"]),
        response_hash=(
            str(row["response_hash"]) if row.get("response_hash") else None
        ),
        provider_attempt_count=int(row.get("provider_attempt_count") or 1),
        validation_retry_used=bool(row.get("validation_retry_used")),
    )


def _coerce_rejection(
    row: FactExtractionRejection | Mapping[str, Any],
) -> FactExtractionRejection:
    if isinstance(row, FactExtractionRejection):
        return row
    return FactExtractionRejection(
        batch_id=str(row["batch_id"]),
        proposal_index=int(row["proposal_index"]),
        document_id=str(row.get("document_id") or ""),
        reason=str(row["reason"]),
        material_proposal=bool(row.get("material_proposal")),
        proposed_exact_quote=(
            str(row["proposed_exact_quote"])
            if row.get("proposed_exact_quote")
            else None
        ),
    )


__all__ = [
    "FACT_EXTRACTION_OUTPUT_FILES",
    "FactExtractionProviderCall",
    "FactExtractionRejection",
    "ResearcherEvidenceFactExtractor",
    "ResearcherFactExtractionResult",
    "production_material_fact_rows",
    "write_researcher_fact_extraction_result",
]
