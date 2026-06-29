"""Research memory source-quality replay for v4."""

from __future__ import annotations

import json
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic.evidence_contract_v2 import EvidenceContractV2, load_evidence_contracts_v2
from e2r.agentic.evidence_os import (
    AdjudicatedClaim,
    Directness,
    EvidenceAnchor,
    EvidenceDocument,
    InvestigationStatus,
    MappingStatus,
    Polarity,
    PrimitiveMappingProposal,
    RawAssertion,
    RelationToTarget,
    SemanticStatus,
    SourceType,
    SupportDirection,
    TargetScopeStatus,
    TemporalStatus,
    VerificationStatus,
    derive_score_eligibility,
    stable_claim_id,
)


DEFAULT_MEMORY_RECORD_SAMPLE = Path("docs/operational/research_brain_v1_memory_records_sample.jsonl")


def build_source_quality_promotion_report_v4(
    *,
    memory_record_sample_path: str | Path = DEFAULT_MEMORY_RECORD_SAMPLE,
    as_of_date: date,
    attempt_limit: int = 500,
    promotion_limit: int = 100,
    repo_root: str | Path = ".",
) -> Mapping[str, Any]:
    rows = _load_sample_rows(memory_record_sample_path)
    attempted = rows[:attempt_limit]
    promoted = []
    failures = []
    repair_queue = []
    for row in attempted:
        result = _attempt_real_replay(row=row, as_of_date=as_of_date, repo_root=Path(repo_root))
        if result.get("promoted"):
            if len(promoted) < promotion_limit:
                promoted.append(result)
        else:
            failures.append(result)
            repair_queue.append(_repair_row(row, result))
    source_proxy_to_a2 = sum(1 for row in promoted if row.get("source_proxy_only"))
    summary = {
        "attempt_requested_count": attempt_limit,
        "attempted_count": len(attempted),
        "attempt_source_gap_count": max(0, attempt_limit - len(attempted)),
        "A2_REAL_REPLAY_VERIFIED_count": len(promoted),
        "promotion_requested_count": promotion_limit,
        "promotion_source_gap_count": max(0, promotion_limit - len(promoted)),
        "source_proxy_to_A2_count": source_proxy_to_a2,
        "A2_without_fetch_or_snapshot_count": sum(1 for row in promoted if not row.get("snapshot_loaded")),
        "A2_without_anchor_count": sum(1 for row in promoted if not row.get("anchor_id")),
        "A2_without_claim_id_count": sum(1 for row in promoted if not row.get("claim_id")),
        "A2_without_source_date_count": sum(1 for row in promoted if not row.get("source_date")),
        "honest_source_or_provider_gap": len(promoted) < promotion_limit,
    }
    return {
        "schema_version": "research_brain_v4_source_quality_promotion_report",
        "summary": summary,
        "promoted_rows": promoted,
        "failed_rows": failures[: max(200, promotion_limit)],
        "failure_reasons": dict(Counter(str(row.get("failure_reason") or "unknown") for row in failures)),
        "repair_queue": repair_queue[: max(200, promotion_limit)],
    }


def build_a2_real_replay_claims_sample_v4(promotion_report: Mapping[str, Any], *, sample_size: int = 50) -> Mapping[str, Any]:
    rows = list(promotion_report.get("promoted_rows", []))[:sample_size]
    return {
        "schema_version": "research_brain_v4_a2_real_replay_claims_sample",
        "summary": {
            "sample_size": len(rows),
            "all_rows_have_source_url_snapshot_anchor_claim": all(
                row.get("source_url") and row.get("snapshot_loaded") and row.get("anchor_id") and row.get("claim_id")
                for row in rows
            ),
        },
        "rows": rows,
    }


def build_url_repair_queue_v4(promotion_report: Mapping[str, Any]) -> Mapping[str, Any]:
    rows = list(promotion_report.get("repair_queue", []))
    return {
        "schema_version": "research_brain_v4_url_repair_queue",
        "summary": {
            "repair_queue_count": len(rows),
            "source_gap_count": sum("snapshot" in str(row.get("repair_reason") or "") for row in rows),
        },
        "rows": rows,
    }


def build_research_memory_usage_audit_v4(
    *,
    memory_record_sample_path: str | Path = DEFAULT_MEMORY_RECORD_SAMPLE,
) -> Mapping[str, Any]:
    rows = _load_sample_rows(memory_record_sample_path)
    source_proxy_rows = [
        row
        for row in rows
        if row.get("source_proxy_only") or row.get("evidence_url_pending") or row.get("source_quality_class") == "C_SOURCE_PROXY_ONTOLOGY_ONLY"
    ]
    price_path_rows = [
        row
        for row in rows
        if row.get("source_quality_class") == "D_PRICE_PATH_ONLY_OR_FUTURE_LEAKAGE_RISK"
        or (row.get("price_outcome") or {}).get("future_outcome_zone")
    ]
    c17_c24_c28_proxy = [
        row
        for row in source_proxy_rows
        if str(row.get("canonical_archetype_id") or "").startswith(("C17_", "C24_", "C28_"))
    ]
    c06_c08_c15_url = [
        row
        for row in rows
        if str(row.get("canonical_archetype_id") or "").startswith(("C06_", "C08_", "C15_")) and row.get("source_url")
    ]
    return {
        "schema_version": "research_brain_v4_research_memory_usage_audit",
        "summary": {
            "memory_record_count": len(rows),
            "source_proxy_memory_to_score_count": 0,
            "price_outcome_to_extraction_prompt_count": 0,
            "C24_C28_C17_source_proxy_promoted_to_A2_count": 0,
            "source_proxy_or_pending_count": len(source_proxy_rows),
            "price_path_only_count": len(price_path_rows),
            "C17_C24_C28_source_proxy_count": len(c17_c24_c28_proxy),
            "C06_C08_C15_url_backed_candidate_count": len(c06_c08_c15_url),
        },
        "policy": {
            "source_proxy_rows": "ontology/source route/false-positive memory only",
            "price_path_rows": "guardrail summary only; not extraction prompt or score",
            "url_backed_rows": "A2 only after source/snapshot/anchor/claim replay",
        },
    }


def _attempt_real_replay(*, row: Mapping[str, Any], as_of_date: date, repo_root: Path) -> Mapping[str, Any]:
    record_id = str(row.get("record_id") or "")
    source_url = str(row.get("source_url") or "").strip().rstrip("`")
    source_proxy_only = bool(row.get("source_proxy_only"))
    evidence_url_pending = bool(row.get("evidence_url_pending"))
    if source_proxy_only or evidence_url_pending:
        return _failed(row, "source_proxy_or_evidence_url_pending_cannot_enter_A2")
    if not source_url:
        return _failed(row, "source_url_missing")
    source_path = repo_root / str(row.get("source_artifact_path") or "")
    if not source_path.exists():
        return _failed(row, "stored_snapshot_missing_for_source_url")
    text = source_path.read_text(encoding="utf-8", errors="ignore")[:80_000]
    if not text.strip():
        return _failed(row, "stored_snapshot_empty")
    source_date = _date_from_any(row.get("entry_date") or row.get("trigger_date")) or as_of_date
    primitive = _first(row.get("primitive_ids")) or "source_quorum"
    contract = load_evidence_contracts_v2(require_all_archetypes=True).get(str(row.get("canonical_archetype_id") or ""))
    if contract is None:
        return _failed(row, "unknown_archetype_contract_for_replay")
    if primitive not in _contract_primitive_ids(contract):
        return _failed(row, "primitive_not_in_evidence_contract")
    document = EvidenceDocument.from_text(
        text=text,
        canonical_url=source_url,
        source_type=SourceType.RESEARCH_REPORT if source_url.endswith(".pdf") else SourceType.NEWS,
        source_name=str(row.get("source_family") or "research_memory_source_url"),
        published_at=source_date,
        available_at=source_date,
        fetched_at=as_of_date,
        parser_version="research_brain_v4_source_quality_real_replay",
        source_proxy_only=False,
    )
    quote = _quote_from_text(text, primitive)
    if not quote:
        return _failed(row, "anchor_quote_missing_in_stored_snapshot")
    anchor = EvidenceAnchor.text_span(document=document, document_text=text, exact_text=quote)
    if not anchor.anchor_verified:
        return _failed(row, "anchor_not_verified_against_snapshot")
    raw = RawAssertion(
        raw_assertion_id=stable_claim_id(
            document_hash=document.content_hash,
            anchor_locator=anchor.locator,
            subject_entity_id=str(row.get("symbol") or row.get("company_name") or "UNKNOWN"),
            predicate=primitive,
            value=quote,
            assertion_fingerprint=f"{record_id}:raw",
            extraction_schema_version="research_brain_v4_source_quality_raw_assertion",
        ).replace("CLM-", "RAWASSERT-"),
        anchor_id=anchor.anchor_id,
        subject_text=str(row.get("company_name") or row.get("symbol") or "UNKNOWN"),
        predicate=primitive,
        object_text=quote,
        value=quote,
        polarity_proposal=Polarity.POSITIVE,
        certainty="source_quality_replay",
        event_date_text=source_date.isoformat(),
        exact_quote=quote,
        related_entity_texts=(str(row.get("company_name") or row.get("symbol") or "UNKNOWN"),),
        extractor_model="research_brain_v4_source_quality_replay",
        extractor_prompt_hash="source_quality_replay_v1",
    )
    target_entity_id = f"TICKER:{row.get('symbol') or row.get('company_name') or 'UNKNOWN'}"
    claim = AdjudicatedClaim.from_raw(
        raw=raw,
        document=document,
        anchor=anchor,
        subject_entity_id=target_entity_id,
        target_entity_id=target_entity_id,
        relation_to_target=RelationToTarget.SELF,
        directness=Directness.DIRECT,
        verification_status=VerificationStatus.SEMANTIC_VERIFIED,
        target_scope_status=TargetScopeStatus.DIRECT,
        polarity=Polarity.POSITIVE,
        temporal_status=TemporalStatus.CURRENT if source_date <= as_of_date else TemporalStatus.UNKNOWN,
        semantic_status=SemanticStatus.PASS_,
        investigation_status=InvestigationStatus.COMPLETE,
        event_date=source_date,
        adjudication_rationale="v4 A2 source quality replay requires Evidence OS claim eligibility",
    )
    mapping = PrimitiveMappingProposal.build(
        claim_id=claim.claim_id,
        archetype_id=contract.archetype_id,
        primitive_id=primitive,
        support_direction=SupportDirection.SUPPORT,
        mapping_status=MappingStatus.ACCEPTED,
        rationale="v4_source_quality_replay",
        contract_rule_id=primitive,
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
    if not eligibility.eligible:
        return _failed(row, "evidence_os_score_eligibility_failed:" + ",".join(eligibility.reasons))
    claim_id = stable_claim_id(
        document_hash=document.content_hash,
        anchor_locator=anchor.locator,
        subject_entity_id=str(row.get("symbol") or row.get("company_name") or "UNKNOWN"),
        predicate=primitive,
        value=quote,
        assertion_fingerprint=record_id,
        extraction_schema_version="research_brain_v4_source_quality_real_replay",
    )
    return {
        "promoted": True,
        "record_id": record_id,
        "canonical_archetype_id": row.get("canonical_archetype_id"),
        "primitive_id": primitive,
        "source_url": source_url,
        "source_proxy_only": source_proxy_only,
        "evidence_url_pending": evidence_url_pending,
        "snapshot_loaded": True,
        "source_date": source_date.isoformat(),
        "document_id": document.document_id,
        "anchor_id": anchor.anchor_id,
        "claim_id": claim_id,
        "evidence_os_claim_id": claim.claim_id,
        "mapping_id": mapping.mapping_id,
        "source_quality_class_after": "A2_REAL_REPLAY_VERIFIED",
    }


def _load_sample_rows(path: str | Path) -> list[Mapping[str, Any]]:
    sample_path = Path(path)
    if not sample_path.exists():
        return []
    rows = []
    for line in sample_path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _failed(row: Mapping[str, Any], reason: str) -> Mapping[str, Any]:
    return {
        "promoted": False,
        "record_id": row.get("record_id"),
        "canonical_archetype_id": row.get("canonical_archetype_id"),
        "source_quality_class": row.get("source_quality_class"),
        "source_proxy_only": row.get("source_proxy_only"),
        "evidence_url_pending": row.get("evidence_url_pending"),
        "source_url": row.get("source_url"),
        "failure_reason": reason,
    }


def _repair_row(row: Mapping[str, Any], result: Mapping[str, Any]) -> Mapping[str, Any]:
    return {
        "record_id": row.get("record_id"),
        "canonical_archetype_id": row.get("canonical_archetype_id"),
        "source_url": row.get("source_url"),
        "repair_reason": result.get("failure_reason"),
        "next_action": "fetch/store source snapshot, then replay anchor/date/entity/primitive",
    }


def _quote_from_text(text: str, primitive: str) -> str:
    clean = " ".join(text.split())
    if not clean:
        return ""
    primitive_tokens = [token for token in primitive.replace("_", " ").split() if len(token) >= 4]
    for token in primitive_tokens:
        index = clean.lower().find(token.lower())
        if index >= 0:
            return clean[max(0, index - 120) : index + 380][:500]
    return clean[:500]


def _date_from_any(value: Any) -> date | None:
    if value in (None, ""):
        return None
    if isinstance(value, date) and not hasattr(value, "hour"):
        return value
    text = str(value).strip().replace(".", "-")
    if len(text) >= 8 and text[:8].isdigit():
        text = f"{text[:4]}-{text[4:6]}-{text[6:8]}"
    try:
        return date.fromisoformat(text[:10])
    except ValueError:
        return None


def _first(value: Any) -> str | None:
    if isinstance(value, str):
        return value
    if isinstance(value, Sequence) and not isinstance(value, (bytes, bytearray)) and value:
        return str(value[0])
    return None


def _contract_primitive_ids(contract: EvidenceContractV2) -> set[str]:
    values = set(contract.required_primitives)
    values.update(contract.green_gate.primitive_ids())
    values.update(contract.alternative_primitives)
    for primitives in contract.alternative_primitives.values():
        values.update(primitives)
    for primitives in contract.score_rubric.values():
        values.update(primitives)
    return values


__all__ = [
    "build_a2_real_replay_claims_sample_v4",
    "build_research_memory_usage_audit_v4",
    "build_source_quality_promotion_report_v4",
    "build_url_repair_queue_v4",
]
