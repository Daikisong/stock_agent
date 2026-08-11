"""Compile fetched current documents into provenance-backed Evidence OS claims."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass, replace
from datetime import date
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic import (
    AgenticEvidenceProviderBundle,
    EntityRecord,
    EntityRegistry,
    EvidenceAnchor,
    EvidenceCompilationInput,
    EvidenceDocument,
    EvidenceExtractionPass,
    EvidenceWorkflowOrchestrator,
    SourceType,
    build_default_codex_agentic_evidence_provider_bundle,
)
from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
from e2r.production.metadata import stable_hash, write_json, write_jsonl
from e2r.research_brain.runtime.current_operation_runner import (
    DailyClaimProvenance,
    DailyProviderKind,
)


LIVE_CURRENT_CLAIM_SCHEMA_VERSION = "e2r_live_current_claim_v1"


@dataclass(frozen=True)
class CurrentClaimCompilerConfig:
    as_of_date: str
    max_documents: int
    max_raw_assertions_per_document: int = 12
    max_extraction_passes_per_document: int = 16
    mapper_self_consistency_rounds: int = 2
    test_mode: bool = False
    additional_primitive_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        if not 1 <= self.max_documents <= 100:
            raise ValueError("current claim compiler document budget must be bounded by 100")
        if not 1 <= self.max_raw_assertions_per_document <= 48:
            raise ValueError("raw assertion budget must be bounded by 48")
        if not 1 <= self.max_extraction_passes_per_document <= 16:
            raise ValueError("extraction pass budget must be bounded by 16")
        if not 1 <= self.mapper_self_consistency_rounds <= 3:
            raise ValueError("mapper self-consistency rounds must be bounded by 3")
        if len(self.additional_primitive_ids) != len(set(self.additional_primitive_ids)):
            raise ValueError("additional primitive ids must be unique")
        if any(not str(value).strip() for value in self.additional_primitive_ids):
            raise ValueError("additional primitive ids must be non-empty")


@dataclass(frozen=True)
class SourceTaskSatisfactionRecord:
    source_task_id: str
    target_id: str
    recipe_id: str
    primitive_id: str
    status: str
    document_ids: tuple[str, ...]
    raw_assertion_ids: tuple[str, ...]
    accepted_claim_ids: tuple[str, ...]
    accepted_mapping_ids: tuple[str, ...]
    rerouted_mapping_ids: tuple[str, ...]
    original_gap_open: bool
    reason: str
    schema_version: str = LIVE_CURRENT_CLAIM_SCHEMA_VERSION

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class CurrentClaimCompilationResult:
    as_of_date: str
    status: str
    evidence_anchors: tuple[Mapping[str, Any], ...]
    raw_assertions: tuple[Mapping[str, Any], ...]
    adjudicated_claims: tuple[Mapping[str, Any], ...]
    primitive_mappings: tuple[Mapping[str, Any], ...]
    accepted_current_claims: tuple[Mapping[str, Any], ...]
    daily_claim_provenance: tuple[DailyClaimProvenance, ...]
    source_task_satisfaction: tuple[SourceTaskSatisfactionRecord, ...]
    compilation_pending: tuple[Mapping[str, Any], ...]
    audit: Mapping[str, Any]


class CurrentClaimCompiler:
    def compile(
        self,
        config: CurrentClaimCompilerConfig,
        *,
        evidence_documents: Sequence[Mapping[str, Any]],
        question_source_tasks: Sequence[Mapping[str, Any]],
        provider_fetch_results: Sequence[Mapping[str, Any]] = (),
        provider_bundle: AgenticEvidenceProviderBundle | None = None,
    ) -> CurrentClaimCompilationResult:
        if len(evidence_documents) > config.max_documents:
            raise ValueError("claim compiler document count exceeds bounded budget")
        question_by_id = _unique_mapping(
            question_source_tasks,
            key="task_id",
            context="question source tasks",
        )
        effective_bundle = provider_bundle
        if effective_bundle is None and not config.test_mode:
            effective_bundle = build_default_codex_agentic_evidence_provider_bundle(
                working_directory=Path.cwd()
            )
        if effective_bundle is None:
            raise ValueError("current claim compiler provider bundle is not configured")
        provider_kind = (
            DailyProviderKind.FIXTURE.value
            if config.test_mode
            else DailyProviderKind.CODEX.value
        )
        contracts = load_evidence_contracts_v2(require_all_archetypes=True)
        documents_by_task: dict[str, list[Mapping[str, Any]]] = {}
        compile_jobs: dict[tuple[str, str], dict[str, Any]] = {}
        for document in evidence_documents:
            for task_id in document.get("source_task_ids") or ():
                task = question_by_id.get(str(task_id))
                if task is None:
                    raise ValueError("evidence document references unknown QuestionSourceTask")
                documents_by_task.setdefault(str(task_id), []).append(document)
                key = (str(document.get("document_id") or ""), str(task.get("archetype_id") or ""))
                job = compile_jobs.setdefault(
                    key,
                    {
                        "document": document,
                        "task": task,
                        "retrieval_focus_terms": [],
                        "retrieval_focus_term_sets": [],
                    },
                )
                task_focus_terms = _retrieval_focus_terms(task)
                job["retrieval_focus_terms"] = list(
                    dict.fromkeys(
                        (
                            *job["retrieval_focus_terms"],
                            *task_focus_terms,
                        )
                    )
                )
                if task_focus_terms and task_focus_terms not in job["retrieval_focus_term_sets"]:
                    job["retrieval_focus_term_sets"].append(task_focus_terms)

        anchors: list[Mapping[str, Any]] = []
        raw_rows: list[Mapping[str, Any]] = []
        claim_rows: list[Mapping[str, Any]] = []
        mapping_rows: list[Mapping[str, Any]] = []
        pending: list[Mapping[str, Any]] = []
        extraction_pass_count = 0
        extracted_raw_assertion_count = 0
        deduplicated_raw_assertion_count = 0
        raw_assertion_budget_truncated_document_count = 0
        result_by_job: dict[tuple[str, str], Mapping[str, Any]] = {}
        orchestrator = EvidenceWorkflowOrchestrator(
            extractor=effective_bundle.extractor,
            adjudicator=effective_bundle.adjudicator,
            mapper=effective_bundle.mapper,
            mapper_self_consistency_rounds=config.mapper_self_consistency_rounds,
            mapper_self_consistency_min_agreement=1,
        )
        for key, job in compile_jobs.items():
            document_row = job["document"]
            task = job["task"]
            archetype_id = str(task.get("archetype_id") or "")
            contract = contracts.get(archetype_id)
            if contract is None:
                raise ValueError(f"QuestionSourceTask archetype lacks EvidenceContract: {archetype_id}")
            allowed_optional = set(contract.alternative_primitives)
            allowed_optional.update(
                value
                for values in contract.alternative_primitives.values()
                for value in values
            )
            unknown_additional = set(config.additional_primitive_ids) - (
                set(contract.required_primitives) | allowed_optional
            )
            if unknown_additional:
                raise ValueError(
                    "additional dossier primitive is outside EvidenceContract: "
                    f"{sorted(unknown_additional)}"
                )
            canonical_primitive_ids = tuple(
                dict.fromkeys(
                    (*contract.required_primitives, *config.additional_primitive_ids)
                )
            )
            document, text = _evidence_document(document_row)
            extraction_passes = _bounded_extraction_passes(
                document=document,
                document_text=text,
                focus_term_sets=tuple(job["retrieval_focus_term_sets"]),
                fallback_focus_terms=tuple(job["retrieval_focus_terms"]),
                max_passes=config.max_extraction_passes_per_document,
            )
            retrieval_anchors = tuple(
                {
                    anchor.anchor_id: anchor
                    for extraction_pass in extraction_passes
                    for anchor in extraction_pass.anchors
                }.values()
            )
            anchor = retrieval_anchors[0]
            anchors.extend(
                {
                    **_json_safe(asdict(item)),
                    "target_id": str(task.get("target_id") or ""),
                    "source_task_ids": list(document_row.get("source_task_ids") or ()),
                }
                for item in retrieval_anchors
            )
            target_id = str(task.get("target_id") or "")
            target_name = str(task.get("company_name") or "")
            registry = EntityRegistry(
                entities={
                    target_id: EntityRecord(
                        entity_id=target_id,
                        legal_name=target_name,
                        aliases=(),
                        ticker=target_id,
                    )
                }
            )
            try:
                compiled = orchestrator.compile(
                    EvidenceCompilationInput(
                        target_entity_id=target_id,
                        target_names=(target_name, target_id),
                        as_of_date=date.fromisoformat(config.as_of_date),
                        document=document,
                        document_text=text,
                        anchors=retrieval_anchors,
                        entity_registry=registry,
                        contract=contract,
                        canonical_primitive_ids=canonical_primitive_ids,
                        max_raw_assertions=config.max_raw_assertions_per_document,
                        retrieval_focus_terms=tuple(job["retrieval_focus_terms"]),
                        extraction_passes=extraction_passes,
                    )
                )
            except Exception as exc:
                pending_row = {
                    "schema_version": LIVE_CURRENT_CLAIM_SCHEMA_VERSION,
                    "document_id": document.document_id,
                    "target_id": target_id,
                    "archetype_id": archetype_id,
                    "reason_code": "CLAIM_COMPILER_PROVIDER_OR_OUTPUT_ERROR",
                    "reason_detail": f"{type(exc).__name__}: {exc}",
                    "score_created": False,
                }
                pending.append(pending_row)
                result_by_job[key] = {"pending": pending_row}
                continue
            raw_by_id = {item.raw_assertion_id: item for item in compiled.raw_assertions}
            extraction_pass_count += compiled.extraction_pass_count
            extracted_raw_assertion_count += compiled.extracted_raw_assertion_count
            deduplicated_raw_assertion_count += compiled.deduplicated_raw_assertion_count
            raw_assertion_budget_truncated_document_count += int(
                compiled.raw_assertion_budget_truncated
            )
            claims_by_id = {item.claim_id: item for item in compiled.adjudicated_claims}
            raw_rows.extend(
                {
                    **_json_safe(asdict(item)),
                    "document_id": document.document_id,
                    "target_id": target_id,
                    "extractor_contract_blind": True,
                    "extraction_provider_kind": provider_kind,
                }
                for item in compiled.raw_assertions
            )
            claim_rows.extend(
                {
                    **_json_safe(asdict(item)),
                    "document_id": document.document_id,
                    "target_id": target_id,
                    "adjudication_provider_kind": provider_kind,
                }
                for item in compiled.adjudicated_claims
            )
            mapping_rows.extend(
                {
                    **_json_safe(asdict(item)),
                    "document_id": document.document_id,
                    "target_id": target_id,
                    "mapping_provider_kind": provider_kind,
                    "accepted_by_evidence_os": item in compiled.accepted_mappings,
                }
                for item in (*compiled.accepted_mappings, *compiled.rejected_mappings)
            )
            result_by_job[key] = {
                "document": document,
                "document_row": document_row,
                "anchor": anchor,
                "anchors_by_id": {
                    item.anchor_id: item for item in retrieval_anchors
                },
                "raw_by_id": raw_by_id,
                "claims_by_id": claims_by_id,
                "accepted_mappings": tuple(compiled.accepted_mappings),
                "raw_assertion_ids": tuple(raw_by_id),
            }

        accepted_claims: dict[str, Mapping[str, Any]] = {}
        provenance_by_claim_mapping: dict[tuple[str, str], DailyClaimProvenance] = {}
        satisfaction: list[SourceTaskSatisfactionRecord] = []
        fetch_by_task: dict[str, list[Mapping[str, Any]]] = {}
        for row in provider_fetch_results:
            fetch_by_task.setdefault(str(row.get("source_task_id") or ""), []).append(row)
        for task_id, task in question_by_id.items():
            target_id = str(task.get("target_id") or "")
            task_documents = tuple(documents_by_task.get(task_id, ()))
            task_raw_ids: list[str] = []
            direct: list[Any] = []
            rerouted: list[Any] = []
            accepted_ids: list[str] = []
            task_pending = False
            primitive_id = str(task.get("primitive_id") or "")
            for document_row in task_documents:
                key = (
                    str(document_row.get("document_id") or ""),
                    str(task.get("archetype_id") or ""),
                )
                compiled = result_by_job.get(key) or {}
                if compiled.get("pending"):
                    task_pending = True
                    continue
                task_raw_ids.extend(compiled.get("raw_assertion_ids") or ())
                for mapping in compiled.get("accepted_mappings") or ():
                    claim = compiled["claims_by_id"].get(mapping.claim_id)
                    raw = compiled["raw_by_id"].get(claim.raw_assertion_id) if claim else None
                    if claim is None or raw is None or not str(raw.exact_quote or "").strip():
                        continue
                    if raw.exact_quote not in str(document_row.get("content_text") or ""):
                        continue
                    accepted_ids.append(claim.claim_id)
                    (direct if mapping.primitive_id == primitive_id else rerouted).append(mapping)
                    accepted_row = {
                        **_json_safe(asdict(claim)),
                        "target_id": target_id,
                        "raw_assertion": _json_safe(asdict(raw)),
                        "mapping_ids": [mapping.mapping_id],
                        "document_id": compiled["document"].document_id,
                        "accepted": True,
                        "current_score_eligible": False,
                    }
                    previous = accepted_claims.get(claim.claim_id)
                    if previous is not None:
                        previous_without_mappings = {
                            key: value for key, value in previous.items()
                            if key != "mapping_ids"
                        }
                        current_without_mappings = {
                            key: value for key, value in accepted_row.items()
                            if key != "mapping_ids"
                        }
                        if previous_without_mappings != current_without_mappings:
                            raise ValueError("same claim id has conflicting accepted payloads")
                        accepted_row["mapping_ids"] = list(dict.fromkeys((
                            *(previous.get("mapping_ids") or ()),
                            mapping.mapping_id,
                        )))
                    accepted_claims[claim.claim_id] = accepted_row
                    provenance = _daily_provenance(
                        task=task,
                        document_row=document_row,
                        anchor=compiled["anchors_by_id"].get(
                            raw.anchor_id,
                            compiled["anchor"],
                        ),
                        claim=claim,
                        raw=raw,
                        mapping=mapping,
                        provider_kind=provider_kind,
                        test_mode=config.test_mode,
                    )
                    provenance_by_claim_mapping[(claim.claim_id, mapping.mapping_id)] = provenance
            if direct:
                status = "DIRECT_TASK_SATISFIED"
                reason = "accepted current mapping matches the task primitive"
                original_gap_open = False
            elif rerouted:
                status = "REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN"
                reason = "a current claim mapped elsewhere; the requested primitive remains open"
                original_gap_open = True
            elif task_pending:
                status = "PROVIDER_FAILED"
                reason = "claim extractor, adjudicator, or mapper failed without fallback"
                original_gap_open = True
            elif task_documents:
                status = "NO_RELEVANT_CLAIM"
                reason = "fetched official documents did not satisfy the task predicate"
                original_gap_open = True
            else:
                fetch_rows = fetch_by_task.get(task_id, ())
                provider_failed = any(
                    str(row.get("acquisition_class") or "")
                    in {"PROVIDER_FAILED", "AUTH_FAILED", "RATE_LIMITED"}
                    for row in fetch_rows
                )
                status = "PROVIDER_FAILED" if provider_failed else "SOURCE_EXHAUSTED"
                reason = (
                    "official provider failed and no document was available"
                    if provider_failed
                    else "official source route produced no usable document"
                )
                original_gap_open = True
            satisfaction.append(
                SourceTaskSatisfactionRecord(
                    source_task_id=task_id,
                    target_id=str(task.get("target_id") or ""),
                    recipe_id=str(task.get("recipe_id") or ""),
                    primitive_id=primitive_id,
                    status=status,
                    document_ids=tuple(
                        dict.fromkeys(str(item.get("document_id") or "") for item in task_documents)
                    ),
                    raw_assertion_ids=tuple(dict.fromkeys(task_raw_ids)),
                    accepted_claim_ids=tuple(dict.fromkeys(accepted_ids)),
                    accepted_mapping_ids=tuple(item.mapping_id for item in direct),
                    rerouted_mapping_ids=tuple(item.mapping_id for item in rerouted),
                    original_gap_open=original_gap_open,
                    reason=reason,
                )
            )
        provenance = _merge_claim_provenance(
            tuple(provenance_by_claim_mapping.values())
        )
        audit = _audit_claim_compilation(
            as_of_date=config.as_of_date,
            raw_assertions=raw_rows,
            adjudicated_claims=claim_rows,
            accepted_claims=tuple(accepted_claims.values()),
            provenance=provenance,
            satisfaction=satisfaction,
            pending=pending,
            extraction_pass_count=extraction_pass_count,
            extracted_raw_assertion_count=extracted_raw_assertion_count,
            deduplicated_raw_assertion_count=deduplicated_raw_assertion_count,
            raw_assertion_budget_truncated_document_count=(
                raw_assertion_budget_truncated_document_count
            ),
        )
        return CurrentClaimCompilationResult(
            as_of_date=config.as_of_date,
            status=(
                "CURRENT_CLAIM_COMPILER_PASS"
                if audit["hard_acceptance_pass"]
                else "CURRENT_CLAIM_COMPILER_FAIL"
            ),
            evidence_anchors=tuple(anchors),
            raw_assertions=tuple(raw_rows),
            adjudicated_claims=tuple(claim_rows),
            primitive_mappings=tuple(mapping_rows),
            accepted_current_claims=tuple(accepted_claims.values()),
            daily_claim_provenance=provenance,
            source_task_satisfaction=tuple(satisfaction),
            compilation_pending=tuple(pending),
            audit=audit,
        )


def write_current_claim_compilation(
    result: CurrentClaimCompilationResult,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root)
    paths = {
        "anchors": root / "evidence_anchors.jsonl",
        "raw_assertions": root / "raw_assertions.jsonl",
        "claims": root / "adjudicated_claims.jsonl",
        "mappings": root / "primitive_mappings.jsonl",
        "accepted": root / "accepted_current_claims.jsonl",
        "provenance": root / "daily_claim_provenance.jsonl",
        "satisfaction": root / "source_task_satisfaction.jsonl",
        "pending": root / "claim_compilation_pending.jsonl",
        "audit": root / "claim_compiler_audit.json",
    }
    write_jsonl(paths["anchors"], result.evidence_anchors)
    write_jsonl(paths["raw_assertions"], result.raw_assertions)
    write_jsonl(paths["claims"], result.adjudicated_claims)
    write_jsonl(paths["mappings"], result.primitive_mappings)
    write_jsonl(paths["accepted"], result.accepted_current_claims)
    write_jsonl(paths["provenance"], (item.to_dict() for item in result.daily_claim_provenance))
    write_jsonl(paths["satisfaction"], (item.to_dict() for item in result.source_task_satisfaction))
    write_jsonl(paths["pending"], result.compilation_pending)
    write_json(paths["audit"], {**dict(result.audit), "status": result.status})
    return paths


def _evidence_document(row: Mapping[str, Any]) -> tuple[EvidenceDocument, str]:
    text = str(row.get("content_text") or "")
    if hashlib.sha256(text.encode("utf-8")).hexdigest() != str(row.get("content_hash") or ""):
        raise ValueError("evidence document content hash mismatch")
    source_class = str(row.get("source_class") or "")
    source_type = (
        SourceType.FILING
        if source_class in {"DART", "KIND"}
        else SourceType.IR
        if "IR" in source_class
        else SourceType.RESEARCH_REPORT
        if source_class == "CompanyGuide"
        else SourceType.API
    )
    document = EvidenceDocument.from_text(
        text=text,
        canonical_url=str(row.get("canonical_url") or ""),
        source_type=source_type,
        source_name=str(row.get("provider_name") or ""),
        published_at=date.fromisoformat(str(row.get("published_at") or "")),
        available_at=date.fromisoformat(str(row.get("available_at") or "")),
        fetched_at=date.fromisoformat(str(row.get("fetched_at") or "")[:10]),
        revision_id=str(row.get("content_hash") or ""),
        parser_version="e2r_live_current_claim_v1",
        source_lineage_id=str(row.get("source_lineage_id") or ""),
        source_proxy_only=False,
    )
    if document.document_id != str(row.get("document_id") or ""):
        raise ValueError("evidence document stable identity mismatch")
    return document, text


def _retrieval_focus_terms(task: Mapping[str, Any]) -> tuple[str, ...]:
    """Tokenize only LLM-authored query/question text for document retrieval."""

    query_intent = task.get("query_intent") or {}
    texts = (
        *(str(item) for item in query_intent.get("literal_queries") or ()),
        str(task.get("question_to_answer") or ""),
    )
    blocked = {
        re.sub(r"[^0-9a-z가-힣]", "", str(value).casefold())
        for value in (
            task.get("target_id"),
            task.get("symbol"),
            task.get("company_name"),
        )
        if str(value or "").strip()
    }
    generic = {
        "official",
        "source",
        "document",
        "current",
        "latest",
        "does",
        "and",
        "what",
        "exactly",
        "exist",
        "equivalent",
        "commercial",
        "target",
        "defined",
        "product",
        "period",
        "currently",
        "remains",
        "only",
        "site",
        "com",
        "before",
        "after",
        "원문",
        "공식",
        "최근",
        "현재",
        "확인",
        "관련",
        "이전",
        "이후",
        "발표",
    }
    result: list[str] = []
    for text in texts:
        for token in re.findall(r"[a-z][a-z0-9_-]{2,}|[가-힣]{2,}", text.casefold()):
            normalized = re.sub(r"[^0-9a-z가-힣]", "", token)
            if normalized in blocked or normalized in generic or normalized.isdigit():
                continue
            if token not in result:
                result.append(token)
            if len(result) >= 96:
                return tuple(result)
    return tuple(result)


def _bounded_extraction_passes(
    *,
    document: EvidenceDocument,
    document_text: str,
    focus_term_sets: Sequence[Sequence[str]],
    fallback_focus_terms: Sequence[str],
    max_passes: int,
) -> tuple[EvidenceExtractionPass, ...]:
    """Keep LLM-authored question focuses separate under an explicit pass budget."""

    unique_term_sets = list(
        dict.fromkeys(
            tuple(dict.fromkeys(str(term) for term in terms if str(term).strip()))
            for terms in focus_term_sets
            if any(str(term).strip() for term in terms)
        )
    )
    if not unique_term_sets:
        unique_term_sets = [tuple(fallback_focus_terms)]
    if len(unique_term_sets) > max_passes:
        retained = unique_term_sets[: max_passes - 1]
        overflow = tuple(
            dict.fromkeys(
                term
                for term_set in unique_term_sets[max_passes - 1 :]
                for term in term_set
            )
        )
        unique_term_sets = [*retained, overflow]
    return tuple(
        EvidenceExtractionPass(
            anchors=_retrieval_anchors(
                document=document,
                document_text=document_text,
                focus_terms=term_set,
            ),
            retrieval_focus_terms=term_set,
        )
        for term_set in unique_term_sets
    )


def _retrieval_anchors(
    *,
    document: EvidenceDocument,
    document_text: str,
    focus_terms: Sequence[str],
    max_anchors: int = 8,
) -> tuple[EvidenceAnchor, ...]:
    lower = document_text.casefold()
    ranked = sorted(
        (
            (lower.count(term.casefold()), -len(term), index, term.casefold())
            for index, term in enumerate(focus_terms)
            if term and lower.count(term.casefold()) > 0
        ),
        key=lambda item: item[:3],
    )
    spans: list[tuple[int, int]] = []
    for _count, _negative_length, _index, term in ranked:
        position = lower.find(term)
        if position < 0:
            continue
        start = max(0, position - 700)
        end = min(len(document_text), position + len(term) + 1_300)
        if any(start < prior_end and end > prior_start for prior_start, prior_end in spans):
            continue
        spans.append((start, end))
        if len(spans) >= max_anchors:
            break
    if not spans:
        spans.append((0, min(len(document_text), 4_000)))
    return tuple(
        EvidenceAnchor.text_span(
            document=document,
            document_text=document_text,
            exact_text=document_text[start:end],
            locator=f"char:{start}:{end}",
        )
        for start, end in spans
        if end > start
    )


def _daily_provenance(
    *,
    task: Mapping[str, Any],
    document_row: Mapping[str, Any],
    anchor: EvidenceAnchor,
    claim: Any,
    raw: Any,
    mapping: Any,
    provider_kind: str,
    test_mode: bool,
) -> DailyClaimProvenance:
    source_ids = tuple(
        dict.fromkeys(
            (
                str(document_row.get("source_lineage_id") or ""),
                str(document_row.get("official_document_id") or ""),
            )
        )
    )
    return DailyClaimProvenance(
        provenance_id="CLMPROV-" + stable_hash(
            {"claim_id": claim.claim_id, "mapping_id": mapping.mapping_id}
        )[:24],
        claim_id=claim.claim_id,
        target_id=str(task.get("target_id") or ""),
        document_id=str(document_row.get("document_id") or ""),
        source_url=str(document_row.get("canonical_url") or ""),
        published_date=str(document_row.get("published_at") or ""),
        available_date=str(document_row.get("available_at") or ""),
        content_sha256=str(document_row.get("content_hash") or ""),
        document_text=str(document_row.get("content_text") or ""),
        exact_quote=str(raw.exact_quote),
        source_ids=source_ids,
        anchor_ids=(anchor.anchor_id,),
        mapping_ids=(mapping.mapping_id,),
        extraction_provider_kind=provider_kind,
        mapping_provider_kind=provider_kind,
        decision_use="SCORE",
        directness="DIRECT",
        temporal_status="CURRENT",
        mapping_status="ACCEPTED",
        fetched=True,
        anchor_verified=True,
        source_proxy_only=False,
        test_only=test_mode,
    )


def _merge_claim_provenance(
    rows: Sequence[DailyClaimProvenance],
) -> tuple[DailyClaimProvenance, ...]:
    """Preserve every mapping while keeping one canonical provenance per claim."""

    grouped: dict[str, list[DailyClaimProvenance]] = {}
    for row in rows:
        grouped.setdefault(row.claim_id, []).append(row)
    merged: list[DailyClaimProvenance] = []
    for claim_id, claim_rows in sorted(grouped.items()):
        first = claim_rows[0]
        comparable = asdict(first)
        for key in ("provenance_id", "mapping_ids"):
            comparable.pop(key, None)
        mapping_ids: list[str] = []
        for row in claim_rows:
            other = asdict(row)
            for key in ("provenance_id", "mapping_ids"):
                other.pop(key, None)
            if other != comparable:
                raise ValueError("same claim id has conflicting provenance payloads")
            mapping_ids.extend(row.mapping_ids)
        unique_mapping_ids = tuple(dict.fromkeys(mapping_ids))
        merged.append(replace(
            first,
            provenance_id="CLMPROV-" + stable_hash({
                "claim_id": claim_id,
                "mapping_ids": list(unique_mapping_ids),
            })[:24],
            mapping_ids=unique_mapping_ids,
        ))
    return tuple(merged)


def _audit_claim_compilation(
    *,
    as_of_date: str,
    raw_assertions: Sequence[Mapping[str, Any]],
    adjudicated_claims: Sequence[Mapping[str, Any]],
    accepted_claims: Sequence[Mapping[str, Any]],
    provenance: Sequence[DailyClaimProvenance],
    satisfaction: Sequence[SourceTaskSatisfactionRecord],
    pending: Sequence[Mapping[str, Any]],
    extraction_pass_count: int,
    extracted_raw_assertion_count: int,
    deduplicated_raw_assertion_count: int,
    raw_assertion_budget_truncated_document_count: int,
) -> Mapping[str, Any]:
    provenance_claim_ids = {item.claim_id for item in provenance}
    critical = {
        "accepted_claim_without_provenance": sum(
            str(item.get("claim_id") or "") not in provenance_claim_ids
            for item in accepted_claims
        ),
        "accepted_claim_without_exact_quote": sum(
            not str((item.get("raw_assertion") or {}).get("exact_quote") or "").strip()
            for item in accepted_claims
        ),
        "accepted_claim_without_content_hash": sum(
            not item.content_sha256 for item in provenance
        ),
        "wrong_subject_score": 0,
        "source_proxy_current_claim": sum(item.source_proxy_only for item in provenance),
        "rerouted_claim_closed_original_gap": sum(
            item.status == "REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN"
            and not item.original_gap_open
            for item in satisfaction
        ),
        "old_unknown_risk_penalty": 0,
        "unstructured_rule_fallback_score": 0,
    }
    status_counts: dict[str, int] = {}
    for item in satisfaction:
        status_counts[item.status] = status_counts.get(item.status, 0) + 1
    return {
        "schema_version": "e2r_live_current_claim_audit_v1",
        "as_of_date": as_of_date,
        "anchor_count": len({item.get("anchor_id") for item in raw_assertions}),
        "raw_assertion_count": len(raw_assertions),
        "extraction_pass_count": extraction_pass_count,
        "extracted_raw_assertion_count": extracted_raw_assertion_count,
        "deduplicated_raw_assertion_count": deduplicated_raw_assertion_count,
        "raw_assertion_budget_truncated_document_count": (
            raw_assertion_budget_truncated_document_count
        ),
        "adjudicated_claim_count": len(adjudicated_claims),
        "accepted_current_claim_count": len(accepted_claims),
        "daily_claim_provenance_count": len(provenance),
        "source_task_satisfaction_count": len(satisfaction),
        "source_task_satisfaction_counts": dict(sorted(status_counts.items())),
        "claim_compilation_pending_count": len(pending),
        "extractor_contract_blind_count": sum(
            item.get("extractor_contract_blind") is True for item in raw_assertions
        ),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "hard_acceptance_pass": sum(critical.values()) == 0,
        "production_runtime_ready": False,
    }


def _unique_mapping(
    rows: Sequence[Mapping[str, Any]],
    *,
    key: str,
    context: str,
) -> Mapping[str, Mapping[str, Any]]:
    result: dict[str, Mapping[str, Any]] = {}
    for row in rows:
        identity = str(row.get(key) or "")
        if not identity or identity in result:
            raise ValueError(f"duplicate or empty identity in {context}")
        result[identity] = row
    return result


def _json_safe(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, Mapping):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (tuple, list, set, frozenset)):
        return [_json_safe(item) for item in value]
    return value


__all__ = [
    "LIVE_CURRENT_CLAIM_SCHEMA_VERSION",
    "CurrentClaimCompilationResult",
    "CurrentClaimCompiler",
    "CurrentClaimCompilerConfig",
    "SourceTaskSatisfactionRecord",
    "write_current_claim_compilation",
]
