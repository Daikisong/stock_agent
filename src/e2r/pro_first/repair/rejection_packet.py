"""Compile deterministic verifier failures into source-backed repair packets."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..ids import canonical_hash, stable_id
from .models import VerifierRejectionPacket


_STATUS_CATEGORY = {
    "REJECTED_QUOTE_MISMATCH": "QUOTE_MISMATCH",
    "REJECTED_WRONG_SUBJECT": "WRONG_SUBJECT",
    "REJECTED_WRONG_TARGET": "WRONG_TARGET",
    "REJECTED_WRONG_SEGMENT": "WRONG_SEGMENT",
    "REJECTED_WRONG_PRODUCT": "WRONG_PRODUCT",
    "REJECTED_FUTURE": "FUTURE_SOURCE",
    "REJECTED_SNIPPET_ONLY": "SNIPPET_ONLY",
    "REJECTED_SOURCE_UNAVAILABLE": "SOURCE_UNAVAILABLE",
    "REJECTED_DUPLICATE_LINEAGE": "DUPLICATE_LINEAGE",
    "REJECTED_UNSUPPORTED_DERIVATION": "UNSUPPORTED_DERIVATION",
}


def compile_rejection_packets(
    *,
    dossier: Mapping[str, Any],
    verification_rows: Sequence[Mapping[str, Any]],
    fact_compilation_rejection_rows: Sequence[Mapping[str, Any]] = (),
    job_root: str | Path,
    conversation_id: str,
    maximum_excerpt_chars: int = 12_000,
) -> tuple[VerifierRejectionPacket, ...]:
    if dossier.get("schema_version") != "e2r_pro_research_dossier_v2":
        raise ValueError("verifier repair requires ResearchDossierV2")
    if maximum_excerpt_chars < 512:
        raise ValueError("repair source excerpt bound is too small")
    root = Path(job_root).resolve()
    facts = {
        str(row.get("dossier_fact_id") or ""): row
        for collection in ("material_facts", "counterfacts", "resolution_facts")
        for row in dossier.get(collection) or ()
    }
    question_ids_by_fact: dict[str, list[str]] = {}
    for row in dossier.get("question_family_results") or ():
        question_id = str(row.get("question_family_id") or "")
        for key in ("support_fact_ids", "counter_fact_ids", "resolution_fact_ids"):
            for fact_id in row.get(key) or ():
                question_ids_by_fact.setdefault(str(fact_id), []).append(question_id)
    effective_verification_rows = _attach_fact_compilation_rejections(
        verification_rows=verification_rows,
        fact_compilation_rejection_rows=fact_compilation_rejection_rows,
    )
    packets: list[VerifierRejectionPacket] = []
    seen_candidates: set[str] = set()
    for verification in effective_verification_rows:
        status = str(verification.get("status") or "")
        category = _rejection_category(status, str(verification.get("reason") or ""))
        if category is None:
            continue
        candidate_id = str(verification.get("dossier_fact_id") or "")
        if candidate_id in seen_candidates:
            raise ValueError("one rejected candidate has multiple verifier terminal rows")
        seen_candidates.add(candidate_id)
        candidate = facts.get(candidate_id)
        if candidate is None:
            raise ValueError("verifier rejection references an unknown dossier fact")
        question_ids = tuple(
            dict.fromkeys(
                str(value)
                for value in (
                    *(candidate.get("question_family_ids") or ()),
                    *(question_ids_by_fact.get(candidate_id) or ()),
                )
                if str(value).strip()
            )
        )
        document_path = str(verification.get("document_path") or "") or None
        content_hash = str(verification.get("content_hash") or "") or None
        source_excerpt = _load_hash_verified_excerpt(
            root=root,
            document_path=document_path,
            expected_hash=content_hash,
            maximum_chars=maximum_excerpt_chars,
        )
        original_hash = canonical_hash(candidate)
        packet_id = stable_id(
            "PROREPAIRPACKET",
            {
                "job_id": dossier.get("job_id"),
                "conversation_id": conversation_id,
                "candidate_id": candidate_id,
                "original_candidate_hash": original_hash,
                "rejection_category": category,
                "content_hash": content_hash,
            },
        )
        packets.append(
            VerifierRejectionPacket(
                packet_id=packet_id,
                job_id=str(dossier.get("job_id") or ""),
                conversation_id=conversation_id,
                candidate_id=candidate_id,
                question_family_ids=question_ids,
                rejection_category=category,
                verifier_status=status,
                verifier_reason=str(verification.get("reason") or ""),
                source_url=str(verification.get("source_url") or ""),
                source_id=str(verification.get("source_id") or ""),
                content_hash=content_hash,
                document_path=document_path,
                fetched_source_excerpt=source_excerpt,
                fetched_source_excerpt_hash=(
                    canonical_hash({"excerpt": source_excerpt})
                    if source_excerpt
                    else None
                ),
                original_candidate=dict(candidate),
                original_candidate_hash=original_hash,
            )
        )
    return tuple(packets)


def load_verification_rows(job_root: str | Path) -> tuple[Mapping[str, Any], ...]:
    path = Path(job_root).resolve() / "verification/source_verifications.jsonl"
    return tuple(
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )


def load_fact_compilation_rejection_rows(
    job_root: str | Path,
) -> tuple[Mapping[str, Any], ...]:
    path = (
        Path(job_root).resolve()
        / "verification/fact_compilation_rejections.jsonl"
    )
    if not path.is_file():
        return ()
    return tuple(
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )


def _attach_fact_compilation_rejections(
    *,
    verification_rows: Sequence[Mapping[str, Any]],
    fact_compilation_rejection_rows: Sequence[Mapping[str, Any]],
) -> tuple[Mapping[str, Any], ...]:
    source_rows = tuple(dict(row) for row in verification_rows)
    if not fact_compilation_rejection_rows:
        return source_rows
    by_claim = {
        str(row.get("compiled_claim_id") or ""): row
        for row in source_rows
        if str(row.get("compiled_claim_id") or "")
    }
    rejected_candidate_ids = {
        str(row.get("dossier_fact_id") or "")
        for row in source_rows
        if _rejection_category(
            str(row.get("status") or ""), str(row.get("reason") or "")
        )
        is not None
    }
    synthesized: list[Mapping[str, Any]] = []
    for rejection in fact_compilation_rejection_rows:
        claim_id = str(rejection.get("claim_id") or "")
        source = by_claim.get(claim_id)
        if source is None:
            raise ValueError(
                "fact compilation rejection lacks source-verifier candidate lineage"
            )
        candidate_id = str(source.get("dossier_fact_id") or "")
        if candidate_id in rejected_candidate_ids:
            continue
        reason = str(rejection.get("reason") or "")
        duplicate = any(
            marker in reason.upper()
            for marker in ("DUPLICATE", "CYCLIC", "LINEAGE")
        )
        synthesized.append(
            {
                **source,
                "status": (
                    "REJECTED_DUPLICATE_LINEAGE"
                    if duplicate
                    else "REJECTED_UNSUPPORTED_DERIVATION"
                ),
                "reason": reason,
            }
        )
    source_without_synthesized = tuple(
        row
        for row in source_rows
        if str(row.get("dossier_fact_id") or "")
        not in {
            str(value.get("dossier_fact_id") or "") for value in synthesized
        }
    )
    return (*source_without_synthesized, *synthesized)


def _rejection_category(status: str, reason: str) -> str | None:
    if status in _STATUS_CATEGORY:
        return _STATUS_CATEGORY[status]
    if status == "UNVERIFIED_PENDING":
        normalized = reason.upper()
        if "DATE" in normalized or "PUBLISHED" in normalized:
            return "DATE_UNRESOLVED"
        return "UNSUPPORTED_DERIVATION"
    return None


def _load_hash_verified_excerpt(
    *,
    root: Path,
    document_path: str | None,
    expected_hash: str | None,
    maximum_chars: int,
) -> str:
    if not document_path or not expected_hash:
        return ""
    path = (root / document_path).resolve()
    try:
        path.relative_to(root)
    except ValueError as error:
        raise ValueError("repair source document escapes the job root") from error
    payload = path.read_bytes()
    if hashlib.sha256(payload).hexdigest() != expected_hash:
        raise ValueError("repair source document hash differs from verifier receipt")
    text = payload.decode("utf-8")
    if len(text) <= maximum_chars:
        return text
    half = maximum_chars // 2
    return text[:half].rstrip() + "\n[...SOURCE_EXCERPT_BOUND...]\n" + text[-half:].lstrip()


__all__ = [
    "compile_rejection_packets",
    "load_fact_compilation_rejection_rows",
    "load_verification_rows",
]
