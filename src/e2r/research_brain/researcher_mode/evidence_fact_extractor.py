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

from .component_researcher import (
    FACT_EXTRACTION_PAGE_FACT_LIMIT,
    StructuredResearchProvider,
)
from .prompt_projection import (
    project_fact_extraction_evidence_context,
    project_fact_extraction_score_gap_context,
)
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
    completion_flag_reconciled: bool = False
    transport_chunk_ids: tuple[str, ...] = ()
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
        documents_per_call: int = 1,
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
        transport_documents = tuple(
            chunk
            for document in remaining
            for chunk in _document_transport_chunks(
                document,
                max_chars=self.max_document_chars_per_call,
            )
        )
        split_chunk_ids_by_document = _split_chunk_ids_by_document(
            transport_documents
        )
        pending_transport_chunk_ids: set[str] = set()
        provider_circuit_breaker_open = False
        current_fact_prompt_context = project_fact_extraction_evidence_context(
            current_facts
        )
        current_fact_prompt_context_chars = _json_character_count(
            current_fact_prompt_context
        )
        score_gap_prompt_context = project_fact_extraction_score_gap_context(
            score_gap_context or {}
        )
        score_gap_prompt_context_chars = _json_character_count(
            score_gap_prompt_context
        )
        max_primary_payload_chars = 0
        max_attempt_payload_chars = 0
        max_full_document_chars = max(
            (len(str(row.get("content_text") or "")) for row in prepared),
            default=0,
        )
        max_transport_chunk_chars = 0
        pagination_continuation_call_count = 0
        maximum_pagination_page_count = 1
        for batch in _document_batches(
            transport_documents,
            max_documents=self.documents_per_call,
            max_chars=self.max_document_chars_per_call,
        ):
            batch_identity = {
                "target_id": target_id,
                "as_of_date": as_of_date,
                "document_ids": [str(row["document_id"]) for row in batch],
            }
            batch_transport_chunk_ids = _batch_transport_chunk_ids(batch)
            if any(
                int(row.get("transport_chunk_count") or 1) > 1
                for row in batch
            ):
                batch_identity["transport_chunk_ids"] = list(
                    batch_transport_chunk_ids
                )
            batch_id = stable_intelligence_id("FACTBATCH", batch_identity)
            payload = scrub_blind_research_payload(
                {
                    "target_id": target_id,
                    "target_name": target_name,
                    "target_aliases": list(target_aliases),
                    "archetype_hypothesis": archetype_id,
                    "as_of_date": as_of_date,
                    "open_research_objectives": [dict(row) for row in open_objectives],
                    "current_evidence_facts": current_fact_prompt_context,
                    "score_gap_context": score_gap_prompt_context,
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
            prompt_documents = tuple(payload.get("full_documents") or ())
            if len(prompt_documents) != len(batch) or any(
                str(prompt_row.get("content_text") or "")
                != str(source_row.get("content_text") or "")
                for source_row, prompt_row in zip(batch, prompt_documents)
            ):
                raise ValueError(
                    "fact extraction prompt must preserve every full document verbatim"
                )
            max_primary_payload_chars = max(
                max_primary_payload_chars,
                _json_character_count(payload),
            )
            max_transport_chunk_chars = max(
                max_transport_chunk_chars,
                *(len(str(row.get("content_text") or "")) for row in batch),
            )
            attempt_payload = payload
            provider_attempt_count = 0
            validation_retry_used = False
            validation_retry_count = 0
            pagination_page_number = 1
            previously_accepted_claims: dict[str, Mapping[str, Any]] = {}
            previously_rejected_material_quote_failures: dict[
                tuple[str, str], FactExtractionRejection
            ] = {}
            while True:
                max_attempt_payload_chars = max(
                    max_attempt_payload_chars,
                    _json_character_count(attempt_payload),
                )
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
                    pending_transport_chunk_ids.update(
                        batch_transport_chunk_ids
                    )
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
                            transport_chunk_ids=(
                                batch_transport_chunk_ids
                            ),
                        )
                    )
                    # Usage-limit / process-launch failures are transport-wide:
                    # retrying them once per remaining document only burns time
                    # and can make a no-progress checkpoint look active.  A CLI
                    # timeout is different.  It can be caused by one unusually
                    # large document, while the next document may complete
                    # normally.  Preserve that batch as pending, continue the
                    # queue, and let checkpoint/resume retry only the timed-out
                    # document later.
                    provider_circuit_breaker_open = (
                        _is_transport_wide_provider_failure(exc)
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
                    batch_completion_flag_reconciled,
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
                    previously_accepted_claim_counts={
                        document_id: sum(
                            1
                            for claim in previously_accepted_claims.values()
                            if str(claim.get("document_id") or "")
                            == document_id
                        )
                        for document_id in {
                            str(row["document_id"]) for row in batch
                        }
                    },
                    previously_accepted_exact_quotes={
                        document_id: tuple(
                            dict.fromkeys(
                                str(claim.get("exact_quote") or "")
                                for claim in previously_accepted_claims.values()
                                if str(claim.get("document_id") or "")
                                == document_id
                                and str(claim.get("exact_quote") or "")
                            )
                        )
                        for document_id in {
                            str(row["document_id"]) for row in batch
                        }
                    },
                    previously_rejected_material_quote_failure_counts={
                        document_id: sum(
                            1
                            for rejection in (
                                previously_rejected_material_quote_failures.values()
                            )
                            if rejection.document_id == document_id
                        )
                        for document_id in {
                            str(row["document_id"]) for row in batch
                        }
                    },
                )
                page_boundary_reached = (
                    len(tuple(response.get("facts") or ()))
                    >= FACT_EXTRACTION_PAGE_FACT_LIMIT
                )
                unresolved_page_ids = {
                    str(value).strip()
                    for value in response.get("unresolved_document_ids") or ()
                    if str(value).strip()
                }
                required_page_ids = {
                    str(row["document_id"]) for row in batch
                }
                pagination_only_pending = all(
                    reason == "LLM_DECLARED_FACT_EXTRACTION_INCOMPLETE"
                    or (
                        reason.startswith("UNRESOLVED_DOCUMENT:")
                        and reason.split(":", 1)[1] in required_page_ids
                    )
                    for reason in batch_pending
                )
                pagination_requested = (
                    bool(batch_claims)
                    and pagination_only_pending
                    and (
                        page_boundary_reached
                        or (
                            response.get("extraction_complete") is not True
                            and bool(unresolved_page_ids)
                            and unresolved_page_ids.issubset(
                                required_page_ids
                            )
                        )
                    )
                )
                if pagination_requested:
                    for claim in batch_claims:
                        previously_accepted_claims[
                            str(claim["claim_id"])
                        ] = claim
                    pagination_page_number += 1
                    pagination_continuation_call_count += 1
                    maximum_pagination_page_count = max(
                        maximum_pagination_page_count,
                        pagination_page_number,
                    )
                    attempt_payload = scrub_blind_research_payload(
                        {
                            **payload,
                            "fact_extraction_continuation_context": {
                                "page_number": pagination_page_number,
                                "page_fact_limit": (
                                    FACT_EXTRACTION_PAGE_FACT_LIMIT
                                ),
                                "required_document_ids": sorted(
                                    required_page_ids
                                ),
                                "previously_accepted_facts": [
                                    {
                                        "document_id": str(
                                            claim["document_id"]
                                        ),
                                        "question_family_id": str(
                                            claim["question_family_id"]
                                        ),
                                        "subject_id": str(
                                            claim["subject_id"]
                                        ),
                                        "predicate_family": str(
                                            claim["predicate_family"]
                                        ),
                                        "normalized_object": str(
                                            claim["normalized_object"]
                                        ),
                                        "period": str(claim["period"]),
                                        "direction": str(
                                            claim["direction"]
                                        ),
                                        "current_lifecycle": str(
                                            claim["current_lifecycle"]
                                        ),
                                        "exact_quote": str(
                                            claim["exact_quote"]
                                        ),
                                    }
                                    for claim in (
                                        previously_accepted_claims.values()
                                    )
                                ],
                                "instruction": (
                                    "Continue the same supplied batch without "
                                    "repeating any previously accepted fact or "
                                    "exact quote. Return the next distinct page "
                                    "of material facts. If more remain after "
                                    "this page, keep extraction_complete false "
                                    "and list the affected document ids. If no "
                                    "distinct facts remain, return an empty facts "
                                    "array, the accurate final disposition "
                                    "(FACTS_EXTRACTED when prior accepted facts "
                                    "exist), an empty unresolved_document_ids "
                                    "array, and extraction_complete true."
                                ),
                            },
                        }
                    )
                    continue
                if batch_pending and validation_retry_count < 2:
                    for claim in batch_claims:
                        previously_accepted_claims[str(claim["claim_id"])] = claim
                    validation_retry_count += 1
                    validation_retry_used = True
                    rejected_material_proposals = [
                        {
                            "proposal_index": row.proposal_index,
                            "document_id": row.document_id,
                            "reason": row.reason,
                            "proposed_exact_quote": row.proposed_exact_quote,
                        }
                        for row in batch_rejections
                        if row.material_proposal
                        and not row.reason.startswith("MECHANISM_SCOPE_REJECTED")
                    ]
                    for rejection in batch_rejections:
                        if (
                            rejection.material_proposal
                            and rejection.reason
                            == "EXACT_QUOTE_NOT_IN_FULL_DOCUMENT"
                            and rejection.proposed_exact_quote
                        ):
                            previously_rejected_material_quote_failures[
                                (
                                    rejection.document_id,
                                    rejection.proposed_exact_quote,
                                )
                            ] = rejection
                    retry_rejected_proposals = {
                        (
                            str(row["document_id"]),
                            str(row["proposed_exact_quote"] or ""),
                            str(row["reason"]),
                        ): row
                        for row in (
                            *rejected_material_proposals,
                            *(
                                {
                                    "proposal_index": row.proposal_index,
                                    "document_id": row.document_id,
                                    "reason": row.reason,
                                    "proposed_exact_quote": (
                                        row.proposed_exact_quote
                                    ),
                                }
                                for row in (
                                    previously_rejected_material_quote_failures.values()
                                )
                            ),
                        )
                    }
                    attempt_payload = scrub_blind_research_payload(
                        {
                            **payload,
                            "fact_extraction_retry_context": {
                                "rewrite_attempt": validation_retry_count,
                                "maximum_rewrite_attempts": 2,
                                "validation_errors": list(batch_pending),
                                "rejected_proposals": list(
                                    retry_rejected_proposals.values()
                                ),
                                "prior_material_quote_failures": [
                                    {
                                        "document_id": row.document_id,
                                        "reason": row.reason,
                                        "proposed_exact_quote": (
                                            row.proposed_exact_quote
                                        ),
                                    }
                                    for row in (
                                        previously_rejected_material_quote_failures.values()
                                    )
                                ],
                                "must_not_repeat_rejected_proposals": True,
                                "previously_accepted_facts": [
                                    {
                                        "document_id": str(
                                            claim["document_id"]
                                        ),
                                        "question_family_id": str(
                                            claim["question_family_id"]
                                        ),
                                        "subject_id": str(claim["subject_id"]),
                                        "predicate_family": str(
                                            claim["predicate_family"]
                                        ),
                                        "normalized_object": str(
                                            claim["normalized_object"]
                                        ),
                                        "period": str(claim["period"]),
                                        "direction": str(claim["direction"]),
                                        "current_lifecycle": str(
                                            claim["current_lifecycle"]
                                        ),
                                        "exact_quote": str(
                                            claim["exact_quote"]
                                        ),
                                    }
                                    for claim in previously_accepted_claims.values()
                                ],
                                "prohibited_exact_quote_reuse": [
                                    {
                                        "document_id": row["document_id"],
                                        "exact_quote": row["proposed_exact_quote"],
                                    }
                                    for row in rejected_material_proposals
                                    if row["reason"]
                                    == "EXACT_QUOTE_NOT_IN_FULL_DOCUMENT"
                                    and row["proposed_exact_quote"]
                                ],
                                "required_document_ids": [
                                    str(row["document_id"]) for row in batch
                                ],
                                "instruction": (
                                    "Rewrite the complete batch. Every listed rejected "
                                    "proposal was deterministically invalid and must not "
                                    "be repeated, paraphrased, whitespace-normalized, or "
                                    "reused. Facts listed in previously_accepted_facts have "
                                    "already passed deterministic validation: do not emit "
                                    "them again and do not downgrade their document to "
                                    "NO_MATERIAL_FACT. Use FACTS_EXTRACTED for every document "
                                    "that has a previously accepted fact. Omit a rejected "
                                    "proposal unless a different literal substring "
                                    "in the same document directly supports the fact. Every material "
                                    "exact_quote must be copied as one literal "
                                    "contiguous substring from that document's "
                                    "content_text. Delete any unsupported proposal; "
                                    "do not paraphrase or repair quotes in code. If the "
                                    "document contains semantically material content but "
                                    "parser fragmentation or noise prevents a literal "
                                    "quote, use UNREADABLE rather than NO_MATERIAL_FACT. "
                                    "A prior material quote failure cannot be closed as "
                                    "NO_MATERIAL_FACT merely because quote copying failed."
                                    " extraction_complete is local to this supplied batch, "
                                    "not to the broader thesis or future research. Set it "
                                    "to true when every required_document_id has exactly "
                                    "one valid disposition and unresolved_document_ids is "
                                    "empty, including when every disposition is "
                                    "NO_MATERIAL_FACT. Put broader evidence gaps only in "
                                    "unresolved_research_notes; those gaps alone must not "
                                    "make extraction_complete false."
                                ),
                            },
                        }
                    )
                    continue
                combined_batch_claims = {
                    **previously_accepted_claims,
                    **{
                        str(claim["claim_id"]): claim
                        for claim in batch_claims
                    },
                }
                claims.extend(combined_batch_claims.values())
                rejections.extend(batch_rejections)
                if batch_pending:
                    rejections.extend(
                        previously_rejected_material_quote_failures.values()
                    )
                dispositions.extend(batch_dispositions)
                pending.extend(batch_pending)
                if batch_pending:
                    pending_transport_chunk_ids.update(
                        batch_transport_chunk_ids
                    )
                research_gap_feedback.extend(batch_feedback)
                calls.append(
                    FactExtractionProviderCall(
                        batch_id=batch_id,
                        status="PENDING" if batch_pending else "COMPLETE",
                        document_ids=tuple(
                            str(row["document_id"]) for row in batch
                        ),
                        accepted_claim_ids=tuple(
                            combined_batch_claims
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
                        completion_flag_reconciled=(
                            batch_completion_flag_reconciled
                        ),
                        transport_chunk_ids=batch_transport_chunk_ids,
                    )
                )
                break
            if provider_circuit_breaker_open:
                break
        claims, dispositions, pending = _reconcile_transport_chunks(
            claims=claims,
            dispositions=dispositions,
            pending=pending,
            split_chunk_ids_by_document=split_chunk_ids_by_document,
            pending_transport_chunk_ids=pending_transport_chunk_ids,
            target_id=target_id,
            as_of_date=as_of_date,
        )
        rejections = list(
            {
                (
                    row.batch_id,
                    row.document_id,
                    row.reason,
                    row.proposed_exact_quote,
                ): row
                for row in rejections
            }.values()
        )
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
            "completion_flag_reconciled_count": (
                sum(row.completion_flag_reconciled for row in calls)
            ),
            "completion_flag_reconciliation_policy": (
                "BATCH_DISPOSITIONS_COMPLETE_AND_NO_UNRESOLVED_DOCUMENT_IDS"
            ),
            "fact_page_limit": FACT_EXTRACTION_PAGE_FACT_LIMIT,
            "fact_page_limit_is_total_fact_cap": False,
            "pagination_continuation_call_count": (
                pagination_continuation_call_count
            ),
            "maximum_pagination_page_count": (
                maximum_pagination_page_count
            ),
            "transport_chunk_size": self.documents_per_call,
            "transport_character_bound": self.max_document_chars_per_call,
            "transport_chunk_is_completion_cap": False,
            "prompt_transport_accounting": {
                "current_fact_projection_schema_version": (
                    current_fact_prompt_context["schema_version"]
                ),
                "current_fact_count": len(current_facts),
                "current_fact_projection_chars": (
                    current_fact_prompt_context_chars
                ),
                "score_gap_projection_schema_version": (
                    score_gap_prompt_context[
                        "fact_extraction_score_gap_projection_audit"
                    ]["schema_version"]
                ),
                "score_gap_projection_chars": score_gap_prompt_context_chars,
                "maximum_full_document_chars": max_full_document_chars,
                "maximum_transport_chunk_chars": max_transport_chunk_chars,
                "transport_character_bound_enforced": (
                    max_transport_chunk_chars
                    <= self.max_document_chars_per_call
                ),
                "split_document_count": len(split_chunk_ids_by_document),
                "transport_chunk_count": len(transport_documents),
                "every_full_document_covered_by_transport_chunks": True,
                "maximum_primary_payload_chars": max_primary_payload_chars,
                "maximum_attempt_payload_chars": max_attempt_payload_chars,
                "full_document_content_preserved_verbatim": True,
                "full_fact_records_persisted_outside_prompt": True,
                "fixed_top_n_used": False,
                "prompt_projection_is_research_cap": False,
                "score_authority": False,
            },
            "provider_circuit_breaker_open": provider_circuit_breaker_open,
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
        if int(document.get("transport_chunk_count") or 1) > 1:
            if current:
                batches.append(tuple(current))
                current = []
                current_chars = 0
            batches.append((document,))
            continue
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
    payload = {
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
    if int(row.get("transport_chunk_count") or 1) > 1:
        payload["transport_chunk"] = {
            "transport_chunk_id": row["transport_chunk_id"],
            "chunk_index": int(row["transport_chunk_index"]),
            "chunk_count": int(row["transport_chunk_count"]),
            "start_char": int(row["transport_chunk_start"]),
            "end_char": int(row["transport_chunk_end"]),
            "chunk_content_hash": row["transport_chunk_content_hash"],
            "full_document_content_hash": row["content_hash"],
            "full_document_text_chars": int(
                row["full_document_text_chars"]
            ),
            "all_chunks_required_before_document_completion": True,
            "instruction": (
                "Inspect and dispose only this literal transport chunk. "
                "NO_MATERIAL_FACT for one chunk does not prove that the "
                "canonical parent document lacks a fact; deterministic code "
                "aggregates the parent only after every chunk is complete."
            ),
        }
    return payload


def _document_transport_chunks(
    document: Mapping[str, Any],
    *,
    max_chars: int,
) -> tuple[Mapping[str, Any], ...]:
    """Split one canonical document into overlapping literal transport chunks."""

    text = str(document.get("content_text") or "")
    if len(text) <= max_chars:
        return (document,)
    overlap = min(4_000, max(1_000, max_chars // 50))
    ranges: list[tuple[int, int]] = []
    start = 0
    while start < len(text):
        hard_end = min(len(text), start + max_chars)
        end = hard_end
        if hard_end < len(text):
            minimum_boundary = start + int(max_chars * 0.80)
            newline = text.rfind("\n", minimum_boundary, hard_end)
            if newline >= minimum_boundary:
                end = newline + 1
        if end <= start:
            end = hard_end
        ranges.append((start, end))
        if end >= len(text):
            break
        next_start = max(start + 1, end - overlap)
        start = next_start
    chunks: list[Mapping[str, Any]] = []
    count = len(ranges)
    for index, (chunk_start, chunk_end) in enumerate(ranges):
        chunk_text = text[chunk_start:chunk_end]
        chunk_id = stable_intelligence_id(
            "FACTCHUNK",
            {
                "document_id": document["document_id"],
                "content_hash": document["content_hash"],
                "start": chunk_start,
                "end": chunk_end,
            },
        )
        chunks.append(
            {
                **dict(document),
                "content_text": chunk_text,
                "transport_chunk_id": chunk_id,
                "transport_chunk_index": index,
                "transport_chunk_count": count,
                "transport_chunk_start": chunk_start,
                "transport_chunk_end": chunk_end,
                "transport_chunk_content_hash": hashlib.sha256(
                    chunk_text.encode("utf-8")
                ).hexdigest(),
                "full_document_text_chars": len(text),
            }
        )
    if (
        not chunks
        or chunks[0]["transport_chunk_start"] != 0
        or chunks[-1]["transport_chunk_end"] != len(text)
        or any(len(str(row["content_text"])) > max_chars for row in chunks)
        or any(
            int(right["transport_chunk_start"])
            > int(left["transport_chunk_end"])
            for left, right in zip(chunks, chunks[1:])
        )
    ):
        raise ValueError("fact transport chunks do not cover the full document")
    return tuple(chunks)


def _split_chunk_ids_by_document(
    documents: Sequence[Mapping[str, Any]],
) -> Mapping[str, tuple[str, ...]]:
    output: dict[str, list[str]] = {}
    for row in documents:
        if int(row.get("transport_chunk_count") or 1) <= 1:
            continue
        output.setdefault(str(row["document_id"]), []).append(
            str(row["transport_chunk_id"])
        )
    return {key: tuple(values) for key, values in output.items()}


def _batch_transport_chunk_ids(
    batch: Sequence[Mapping[str, Any]],
) -> tuple[str, ...]:
    return tuple(
        str(row["transport_chunk_id"])
        for row in batch
        if row.get("transport_chunk_id")
    )


def _reconcile_transport_chunks(
    *,
    claims: Sequence[Mapping[str, Any]],
    dispositions: Sequence[Mapping[str, Any]],
    pending: Sequence[str],
    split_chunk_ids_by_document: Mapping[str, tuple[str, ...]],
    pending_transport_chunk_ids: set[str],
    target_id: str,
    as_of_date: str,
) -> tuple[list[Mapping[str, Any]], list[Mapping[str, Any]], list[str]]:
    deduped_claims = list(
        {
            str(row.get("claim_id") or stable_intelligence_id("CLAIM", row)): row
            for row in claims
        }.values()
    )
    if not split_chunk_ids_by_document:
        return deduped_claims, list(dispositions), list(pending)
    by_document: dict[str, list[Mapping[str, Any]]] = {}
    for row in dispositions:
        document_id = str(row.get("document_id") or "")
        if document_id in split_chunk_ids_by_document:
            by_document.setdefault(document_id, []).append(row)
    output_dispositions = [
        row
        for row in dispositions
        if str(row.get("document_id") or "")
        not in split_chunk_ids_by_document
    ]
    output_pending = list(pending)
    incomplete_document_ids: set[str] = set()
    for document_id, expected_chunk_ids in split_chunk_ids_by_document.items():
        rows = by_document.get(document_id, [])
        completed_chunk_ids = {
            str(row.get("transport_chunk_id") or "")
            for row in rows
            if str(row.get("transport_chunk_id") or "")
        }
        expected = set(expected_chunk_ids)
        incomplete = (
            completed_chunk_ids != expected
            or bool(expected & pending_transport_chunk_ids)
        )
        if incomplete:
            incomplete_document_ids.add(document_id)
            output_pending.append(
                "INCOMPLETE_DOCUMENT_TRANSPORT_CHUNKS:"
                f"{document_id}:{len(completed_chunk_ids)}/{len(expected)}"
            )
            continue
        document_claims = [
            row
            for row in deduped_claims
            if str(row.get("document_id") or "") == document_id
        ]
        statuses = [str(row.get("status") or "") for row in rows]
        status = (
            "FACTS_EXTRACTED"
            if document_claims
            else "WRONG_TARGET_OR_SEGMENT"
            if statuses and all(value == "WRONG_TARGET_OR_SEGMENT" for value in statuses)
            else "NO_MATERIAL_FACT"
        )
        rationales = tuple(
            dict.fromkeys(
                str(row.get("rationale") or "").strip()
                for row in rows
                if str(row.get("rationale") or "").strip()
            )
        )
        output_dispositions.append(
            {
                "schema_version": "e2r_v5_fact_document_disposition_v1",
                "batch_id": stable_intelligence_id(
                    "FACTDOCAGG",
                    {
                        "target_id": target_id,
                        "as_of_date": as_of_date,
                        "document_id": document_id,
                        "transport_chunk_ids": list(expected_chunk_ids),
                    },
                ),
                "document_id": document_id,
                "status": status,
                "rationale": " | ".join(rationales),
                "accepted_fact_count": len(document_claims),
                "source_absence_proven": False,
                "production_score_authority": False,
                "transport_chunk_count": len(expected_chunk_ids),
                "completed_transport_chunk_count": len(completed_chunk_ids),
                "transport_chunk_ids": list(expected_chunk_ids),
                "all_transport_chunks_complete": True,
            }
        )
    if incomplete_document_ids:
        deduped_claims = [
            row
            for row in deduped_claims
            if str(row.get("document_id") or "")
            not in incomplete_document_ids
        ]
    return deduped_claims, output_dispositions, output_pending


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
    previously_accepted_claim_counts: Mapping[str, int] | None = None,
    previously_accepted_exact_quotes: (
        Mapping[str, Sequence[str]] | None
    ) = None,
    previously_rejected_material_quote_failure_counts: (
        Mapping[str, int] | None
    ) = None,
) -> tuple[
    list[Mapping[str, Any]],
    list[FactExtractionRejection],
    list[Mapping[str, Any]],
    list[str],
    list[str],
    bool,
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
    accepted_by_document: dict[str, int] = {
        str(document_id): int(count)
        for document_id, count in (
            previously_accepted_claim_counts or {}
        ).items()
        if str(document_id) in document_by_id and int(count) > 0
    }
    accepted_quotes_by_document = {
        str(document_id): frozenset(
            _literal_quote_whitespace_identity(value)
            for value in values
            if str(value).strip()
        )
        for document_id, values in (
            previously_accepted_exact_quotes or {}
        ).items()
        if str(document_id) in document_by_id
    }
    for index, raw_proposal in enumerate(raw_facts):
        proposal = _normalize_transport_fact_proposal(
            raw_proposal,
            document_by_id=document_by_id,
        )
        document_id = (
            str(proposal.get("document_id") or "")
            if isinstance(proposal, Mapping)
            else ""
        )
        material = bool(proposal.get("material")) if isinstance(proposal, Mapping) else False
        proposed_exact_quote = (
            str(proposal.get("exact_quote") or "").strip()
            if isinstance(proposal, Mapping)
            else ""
        )
        if (
            material
            and proposed_exact_quote
            and _literal_quote_whitespace_identity(proposed_exact_quote)
            in accepted_quotes_by_document.get(document_id, frozenset())
        ):
            rejections.append(
                FactExtractionRejection(
                    batch_id=batch_id,
                    proposal_index=index,
                    document_id=document_id,
                    reason="PREVIOUSLY_ACCEPTED_EXACT_QUOTE_REPEATED",
                    material_proposal=False,
                    proposed_exact_quote=proposed_exact_quote,
                )
            )
            continue
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
        document = document_by_id[document_id]
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
        if (
            status == "NO_MATERIAL_FACT"
            and int(
                (previously_rejected_material_quote_failure_counts or {}).get(
                    document_id,
                    0,
                )
            )
            > 0
            and not accepted_by_document.get(document_id)
        ):
            pending.append(
                "NO_MATERIAL_FACT_CANNOT_CLOSE_PRIOR_MATERIAL_"
                f"QUOTE_FAILURE:{document_id}"
            )
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
                **(
                    {
                        "transport_chunk_id": str(
                            document.get("transport_chunk_id")
                        ),
                        "transport_chunk_index": int(
                            document.get("transport_chunk_index") or 0
                        ),
                        "transport_chunk_count": int(
                            document.get("transport_chunk_count") or 1
                        ),
                        "transport_chunk_start": int(
                            document.get("transport_chunk_start") or 0
                        ),
                        "transport_chunk_end": int(
                            document.get("transport_chunk_end") or 0
                        ),
                    }
                    if int(document.get("transport_chunk_count") or 1) > 1
                    else {}
                ),
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
    batch_document_accounting_complete = (
        set(disposition_ids) == expected_ids
        and len(disposition_ids) == len(expected_ids)
        and not unresolved_ids
    )
    completion_flag_reconciled = (
        response.get("extraction_complete") is not True
        and batch_document_accounting_complete
    )
    if (
        response.get("extraction_complete") is not True
        and not completion_flag_reconciled
    ):
        pending.append("LLM_DECLARED_FACT_EXTRACTION_INCOMPLETE")
    return (
        claims,
        rejections,
        dispositions,
        list(dict.fromkeys(pending)),
        list(dict.fromkeys(feedback)),
        completion_flag_reconciled,
    )


def _literal_quote_whitespace_identity(value: Any) -> str:
    """Identify the same literal quote despite transport/OCR spacing only."""

    return "".join(str(value).split()).casefold()


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
        "deterministic_field_normalizations": list(
            dict.fromkeys(
                str(value).strip()
                for value in proposal.get(
                    "deterministic_field_normalizations", ()
                )
                if str(value).strip()
            )
        ),
        "provider_name": provider_name,
        "provider_prompt_hash": prompt_hash,
        "provider_response_hash": response_hash,
        "llm_score_authority": False,
        "llm_stage_authority": False,
    }


def _normalize_transport_fact_proposal(
    proposal: Any,
    *,
    document_by_id: Mapping[str, Mapping[str, Any]],
) -> Any:
    """Repair only representation noise that can be proven deterministically.

    The model occasionally wraps an otherwise literal source substring in one
    extra pair of quotation marks or emits a probability as a percentage.  We
    accept those forms only when stripping the wrapper produces an exact
    contiguous substring of the cited document, and only when a confidence
    value is within the conventional 0..100 percentage range.  No source text
    or economic assertion is rewritten.
    """

    if not isinstance(proposal, Mapping):
        return proposal
    normalized = dict(proposal)
    normalizations: list[str] = [
        str(value).strip()
        for value in proposal.get("deterministic_field_normalizations", ())
        if str(value).strip()
    ]
    document_id = str(normalized.get("document_id") or "")
    document = document_by_id.get(document_id)
    quote = str(normalized.get("exact_quote") or "").strip()
    content = str((document or {}).get("content_text") or "")
    if quote and content and quote not in content:
        quote_pairs = {
            '"': '"',
            "'": "'",
            "`": "`",
            "“": "”",
            "‘": "’",
        }
        expected_closer = quote_pairs.get(quote[0])
        if expected_closer is not None and quote.endswith(expected_closer):
            inner = quote[1:-1].strip()
            if inner and inner in content:
                normalized["exact_quote"] = inner
                normalizations.append("EXACT_QUOTE_OUTER_WRAPPER_STRIPPED")
    for field in ("confidence", "scope_confidence"):
        raw_value = normalized.get(field)
        try:
            numeric = float(raw_value)
        except (TypeError, ValueError):
            continue
        if math.isfinite(numeric) and 1 < numeric <= 100:
            normalized[field] = numeric / 100.0
            normalizations.append(f"{field.upper()}_PERCENT_TO_PROBABILITY")
    if normalizations:
        normalized["deterministic_field_normalizations"] = list(
            dict.fromkeys(normalizations)
        )
    return normalized


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


def _is_transport_wide_provider_failure(error: Exception) -> bool:
    """Return whether later document calls cannot reasonably make progress.

    The shared transport exposes both terminal provider failures and a
    per-request CLI timeout as ``StructuredProviderUnavailable``.  A timeout
    must leave only its own document pending because later, smaller documents
    can still succeed in the same checkpoint.
    """

    if not isinstance(error, StructuredProviderUnavailable):
        return False
    return "codex_cli_timeout" not in _clean_error(error).casefold()


def _json_character_count(value: Any) -> int:
    return len(
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            default=str,
        )
    )


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
        completion_flag_reconciled=bool(
            row.get("completion_flag_reconciled")
        ),
        transport_chunk_ids=tuple(row.get("transport_chunk_ids") or ()),
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
