"""Adaptive organic claim closure from a source-backed live research run."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import write_json, write_jsonl
from e2r.research_brain.runtime.live_materialization.current_claim_compiler import (
    CurrentClaimCompiler,
    CurrentClaimCompilerConfig,
)
from e2r.research_brain.runtime.scoring_contracts import (
    load_archetype_scoring_contract,
)
from e2r.research_brain.research_quality import (
    FAILURE_NEXT_ACTIONS,
    canonical_research_failure_class,
)

from .orchestrator import DossierTarget


ADAPTIVE_CLOSURE_SCHEMA_VERSION = "e2r_adaptive_organic_claim_closure_v1"
FAILURE_ACTIONS = dict(FAILURE_NEXT_ACTIONS)


@dataclass(frozen=True)
class OrganicClaimClosureResult:
    status: str
    target_id: str
    organic_claim_count: int
    accepted_mapping_count: int
    output_paths: Mapping[str, Path]
    audit: Mapping[str, Any]


def next_action_for_failure(failure_class: str) -> str:
    canonical = canonical_research_failure_class(failure_class)
    return FAILURE_ACTIONS[canonical]


def run_organic_claim_closure(
    *,
    target: DossierTarget,
    as_of_date: str,
    archetype_id: str,
    source_root: str | Path,
    output_root: str | Path,
    compiler: CurrentClaimCompiler | None = None,
    provider_bundle: Any | None = None,
    max_documents: int = 20,
) -> OrganicClaimClosureResult:
    source = Path(source_root)
    output = Path(output_root)
    documents = _select_source_documents(
        source_root=source,
        target_id=target.target_id,
        as_of_date=as_of_date,
        max_documents=max_documents,
    )
    referenced_task_ids = {
        str(task_id)
        for document in documents
        for task_id in document.get("source_task_ids") or ()
    }
    source_tasks = tuple(
        row
        for row in _read_jsonl(source / "question_source_tasks.jsonl")
        if str(row.get("task_id") or "") in referenced_task_ids
        and str(row.get("target_id") or "") == target.target_id
    )
    fetch_rows = tuple(
        row
        for row in _read_jsonl(source / "provider_fetch_results.jsonl")
        if str(row.get("target_id") or "") == target.target_id
    )
    if documents and not source_tasks:
        raise ValueError("organic source documents lack resolvable SourceTask lineage")
    effective_compiler = compiler or CurrentClaimCompiler()
    if documents:
        claim_result = effective_compiler.compile(
            CurrentClaimCompilerConfig(
                as_of_date=as_of_date,
                max_documents=max(1, len(documents)),
                test_mode=False,
                additional_primitive_ids=tuple(
                    load_archetype_scoring_contract(
                        archetype_id
                    ).primitive_to_component_allowed_edges
                ),
            ),
            evidence_documents=documents,
            question_source_tasks=source_tasks,
            provider_fetch_results=fetch_rows,
            provider_bundle=provider_bundle,
        )
    else:
        claim_result = None
    paths = _write_closure_leaves(
        output_root=output,
        source_root=source,
        target=target,
        as_of_date=as_of_date,
        archetype_id=archetype_id,
        documents=documents,
        source_tasks=source_tasks,
        fetch_rows=fetch_rows,
        claim_result=claim_result,
    )
    accepted = tuple(claim_result.accepted_current_claims) if claim_result else ()
    mappings = tuple(claim_result.primitive_mappings) if claim_result else ()
    accepted_mapping_count = sum(
        row.get("accepted_by_evidence_os") is True for row in mappings
    )
    failure_class = _failure_class(
        documents=documents,
        claim_result=claim_result,
        accepted=accepted,
        mappings=mappings,
    )
    critical = {
        "organic_document_missing": int(not documents),
        "organic_accepted_claim_missing": int(not accepted),
        "accepted_mapping_missing": int(accepted_mapping_count <= 0),
        "claim_compiler_critical_count": int(
            (claim_result.audit.get("critical_count_sum") if claim_result else 0) or 0
        ),
        "target_contamination_count": sum(
            str(row.get("target_id") or "") != target.target_id for row in accepted
        ),
        "probe_contamination_count": sum(
            row.get("evidence_origin") == "CONTROLLED_CLAIM_PROBE"
            for row in accepted
        ),
    }
    audit = {
        "schema_version": ADAPTIVE_CLOSURE_SCHEMA_VERSION,
        "status": (
            "ORGANIC_CLAIM_CLOSURE_PASS"
            if sum(critical.values()) == 0
            else "ORGANIC_CLAIM_CLOSURE_NOT_READY"
        ),
        "target_id": target.target_id,
        "company_name": target.company_name,
        "as_of_date": as_of_date,
        "archetype_id": archetype_id,
        "source_document_count": len(documents),
        "raw_assertion_count": len(claim_result.raw_assertions) if claim_result else 0,
        "adjudicated_claim_count": (
            len(claim_result.adjudicated_claims) if claim_result else 0
        ),
        "organic_accepted_claim_count": len(accepted),
        "accepted_mapping_count": accepted_mapping_count,
        "failure_class": failure_class,
        "next_action": next_action_for_failure(failure_class),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "readiness_eligible": False,
        "score_type": "NO_SCORE",
    }
    write_json(output / "audit_summary.json", audit)
    return OrganicClaimClosureResult(
        status=str(audit["status"]),
        target_id=target.target_id,
        organic_claim_count=len(accepted),
        accepted_mapping_count=accepted_mapping_count,
        output_paths=paths,
        audit=audit,
    )


def _select_source_documents(
    *,
    source_root: Path,
    target_id: str,
    as_of_date: str,
    max_documents: int,
) -> tuple[Mapping[str, Any], ...]:
    selected_path = source_root / "claim_selected_documents.jsonl"
    evidence_path = source_root / "evidence_documents.jsonl"
    path = selected_path if selected_path.is_file() else evidence_path
    if not path.is_file():
        return ()
    selected: list[Mapping[str, Any]] = []
    seen_hashes: set[str] = set()
    for row in _read_jsonl(path):
        if str(row.get("target_id") or "") != target_id:
            continue
        if str(row.get("published_at") or "") > as_of_date:
            continue
        text = str(row.get("content_text") or "")
        content_hash = str(row.get("content_hash") or "")
        if hashlib.sha256(text.encode("utf-8")).hexdigest() != content_hash:
            raise ValueError("organic source document content hash mismatch")
        if row.get("acquisition_class") not in {
            "ACTUAL_LIVE_FULL_DOCUMENT",
            "REAL_PROVIDER_FETCH",
            "FRESH_PROVIDER_CACHE",
        }:
            continue
        if not str(row.get("canonical_url") or "").startswith("https://"):
            continue
        if content_hash in seen_hashes:
            continue
        seen_hashes.add(content_hash)
        selected.append(row)
    selected.sort(
        key=lambda row: (
            str(row.get("published_at") or ""),
            str(row.get("document_id") or ""),
        ),
        reverse=True,
    )
    return tuple(selected[:max_documents])


def _write_closure_leaves(
    *,
    output_root: Path,
    source_root: Path,
    target: DossierTarget,
    as_of_date: str,
    archetype_id: str,
    documents: Sequence[Mapping[str, Any]],
    source_tasks: Sequence[Mapping[str, Any]],
    fetch_rows: Sequence[Mapping[str, Any]],
    claim_result: Any | None,
) -> Mapping[str, Path]:
    output_root.mkdir(parents=True, exist_ok=True)
    paths = {
        "source_timeline": output_root / "source_timeline.jsonl",
        "provider_fetch_results": output_root / "provider_fetch_results.jsonl",
        "evidence_documents": output_root / "evidence_documents.jsonl",
        "evidence_anchors": output_root / "evidence_anchors.jsonl",
        "raw_assertions": output_root / "raw_assertions.jsonl",
        "adjudicated_claims": output_root / "adjudicated_claims.jsonl",
        "accepted_current_claims": output_root / "accepted_current_claims.jsonl",
        "claim_provenance": output_root / "claim_provenance.jsonl",
        "primitive_mappings": output_root / "primitive_mappings.jsonl",
        "question_closure": output_root / "question_closure.jsonl",
        "query_change_log": output_root / "query_change_log.jsonl",
        "impact_change_log": output_root / "impact_change_log.jsonl",
        "component_delta_log": output_root / "component_delta_log.jsonl",
        "dossier_iterations": output_root / "dossier_iterations.jsonl",
    }
    timeline = tuple(
        {
            "target_id": target.target_id,
            "document_id": row.get("document_id"),
            "source_url": row.get("canonical_url"),
            "published_date": row.get("published_at"),
            "available_date": row.get("available_at"),
            "fetched_at": row.get("fetched_at"),
            "content_sha256": row.get("content_hash"),
            "evidence_origin": "ORGANIC_LIVE",
            "as_of_valid": str(row.get("published_at") or "") <= as_of_date,
            "source_proxy_only": False,
        }
        for row in documents
    )
    write_jsonl(paths["source_timeline"], timeline)
    write_jsonl(paths["provider_fetch_results"], fetch_rows)
    write_jsonl(paths["evidence_documents"], documents)
    anchors = tuple(claim_result.evidence_anchors) if claim_result else ()
    raw = tuple(claim_result.raw_assertions) if claim_result else ()
    adjudicated = tuple(claim_result.adjudicated_claims) if claim_result else ()
    mappings = tuple(claim_result.primitive_mappings) if claim_result else ()
    provenance = (
        tuple(item.to_dict() for item in claim_result.daily_claim_provenance)
        if claim_result
        else ()
    )
    provenance_by_claim = {
        str(row.get("claim_id") or ""): row for row in provenance
    }
    accepted = tuple(
        _organic_claim_row(row, provenance_by_claim=provenance_by_claim)
        for row in (claim_result.accepted_current_claims if claim_result else ())
    )
    write_jsonl(paths["evidence_anchors"], anchors)
    write_jsonl(paths["raw_assertions"], raw)
    write_jsonl(paths["adjudicated_claims"], adjudicated)
    write_jsonl(paths["accepted_current_claims"], accepted)
    write_jsonl(paths["claim_provenance"], provenance)
    write_jsonl(paths["primitive_mappings"], mappings)
    family_tasks = _read_jsonl(output_root / "question_source_tasks.jsonl")
    closures = _question_closures(
        target_id=target.target_id,
        tasks=family_tasks,
        accepted_claims=accepted,
        mappings=mappings,
    )
    write_jsonl(paths["question_closure"], closures)
    query_changes = _query_change_rows(
        source_root=source_root,
        target_id=target.target_id,
        source_tasks=source_tasks,
    )
    write_jsonl(paths["query_change_log"], query_changes)
    failure_class = _failure_class(
        documents=documents,
        claim_result=claim_result,
        accepted=accepted,
        mappings=mappings,
    )
    write_jsonl(
        paths["impact_change_log"],
        (
            {
                "iteration": 1,
                "target_id": target.target_id,
                "failure_class": "IMPACT_ADJUDICATION_REQUIRED",
                "accepted_claim_count": len(accepted),
                "validated_impact_count": 0,
                "next_action": next_action_for_failure(
                    "IMPACT_ADJUDICATION_REQUIRED"
                ),
            },
        ),
    )
    contract = load_archetype_scoring_contract(archetype_id)
    accepted_primitives = {
        str(row.get("primitive_id") or "")
        for row in mappings
        if row.get("accepted_by_evidence_os") is True
    }
    component_candidates = sorted(
        {
            component
            for primitive in accepted_primitives
            for component in contract.primitive_to_component_allowed_edges.get(
                primitive, ()
            )
        }
    )
    write_jsonl(
        paths["component_delta_log"],
        (
            {
                "iteration": 1,
                "target_id": target.target_id,
                "accepted_primitive_ids": sorted(accepted_primitives),
                "candidate_component_ids": component_candidates,
                "verified_component_points": 0.0,
                "note": "Candidate components require validated LLM claim impacts before points.",
            },
        ),
    )
    previous_iterations = _read_jsonl(paths["dossier_iterations"])
    iteration = {
        "iteration": 1,
        "target_id": target.target_id,
        "failure_class": failure_class,
        "root_cause": "source-backed claims require adaptive mapping and impact closure",
        "before_metrics": {
            "organic_accepted_claim_count": 0,
            "validated_impact_count": 0,
        },
        "patch": "expanded semantic primitive contract and recompiled current full sources",
        "after_metrics": {
            "organic_accepted_claim_count": len(accepted),
            "accepted_mapping_count": sum(
                row.get("accepted_by_evidence_os") is True for row in mappings
            ),
        },
        "next_action": next_action_for_failure(failure_class),
        "status": (
            "RESOLVED_TO_ORGANIC_CLAIM"
            if accepted
            else "UNRESOLVED"
        ),
    }
    write_jsonl(paths["dossier_iterations"], (*previous_iterations, iteration))
    return paths


def _organic_claim_row(
    row: Mapping[str, Any], *, provenance_by_claim: Mapping[str, Mapping[str, Any]]
) -> Mapping[str, Any]:
    claim_id = str(row.get("claim_id") or "")
    provenance = provenance_by_claim.get(claim_id)
    if provenance is None:
        raise ValueError("accepted organic claim lacks provenance")
    return {
        **dict(row),
        "evidence_origin": "ORGANIC_LIVE",
        "fetched": provenance.get("fetched") is True,
        "source_proxy_only": provenance.get("source_proxy_only") is True,
        "source_url": provenance.get("source_url"),
        "published_date": provenance.get("published_date"),
        "content_sha256": provenance.get("content_sha256"),
        "exact_quote": provenance.get("exact_quote"),
        "scoring_readiness_eligible": True,
    }


def _question_closures(
    *,
    target_id: str,
    tasks: Sequence[Mapping[str, Any]],
    accepted_claims: Sequence[Mapping[str, Any]],
    mappings: Sequence[Mapping[str, Any]],
) -> tuple[Mapping[str, Any], ...]:
    claims_by_mapping: dict[str, str] = {}
    for claim in accepted_claims:
        for mapping_id in claim.get("mapping_ids") or ():
            claims_by_mapping[str(mapping_id)] = str(claim.get("claim_id") or "")
    accepted_mappings = tuple(
        row
        for row in mappings
        if row.get("accepted_by_evidence_os") is True
        and str(row.get("mapping_id") or "") in claims_by_mapping
    )
    rows: list[Mapping[str, Any]] = []
    for task in tasks:
        if str(task.get("target_id") or "") != target_id:
            continue
        primitives = set(str(value) for value in task.get("primitive_ids") or ())
        matches = tuple(
            row
            for row in accepted_mappings
            if str(row.get("primitive_id") or "") in primitives
        )
        support = tuple(
            row for row in matches if row.get("support_direction") == "SUPPORT"
        )
        counter = tuple(
            row for row in matches if row.get("support_direction") == "COUNTER"
        )
        if support:
            status = "SUPPORTED" if len(support) >= len(primitives) else "PARTIALLY_SUPPORTED"
            failure_class = None
        elif counter:
            status = "COUNTERED"
            failure_class = "COUNTER_ONLY"
        else:
            status = "PROVIDER_PENDING"
            failure_class = "REROUTED_PRIMITIVE" if accepted_mappings else "IMPACT_MAPPING_REJECTED"
        rows.append(
            {
                "question_family_id": task.get("question_family_id"),
                "source_task_id": task.get("source_task_id"),
                "target_id": target_id,
                "status": status,
                "failure_class": failure_class,
                "supporting_claim_ids": sorted(
                    {
                        claims_by_mapping[str(row.get("mapping_id") or "")]
                        for row in support
                    }
                ),
                "counter_claim_ids": sorted(
                    {
                        claims_by_mapping[str(row.get("mapping_id") or "")]
                        for row in counter
                    }
                ),
                "search_exhaustion_proof": [],
                "next_action": (
                    next_action_for_failure(failure_class)
                    if failure_class
                    else "RUN_LLM_IMPACT_ADJUDICATION"
                ),
            }
        )
    return tuple(rows)


def _query_change_rows(
    *, source_root: Path, target_id: str, source_tasks: Sequence[Mapping[str, Any]]
) -> tuple[Mapping[str, Any], ...]:
    rows = _read_jsonl(source_root / "web_search_results.jsonl")
    seen: set[str] = set()
    result: list[Mapping[str, Any]] = []
    task_ids = {str(row.get("task_id") or "") for row in source_tasks}
    for row in rows:
        query = str(row.get("query") or "").strip()
        if (
            str(row.get("target_id") or "") != target_id
            or str(row.get("source_task_id") or "") not in task_ids
            or not query
            or query in seen
        ):
            continue
        seen.add(query)
        result.append(
            {
                "target_id": target_id,
                "query": query,
                "query_source": "RESEARCH_BRAIN_LLM_SOURCE_RUN",
                "duplicate": False,
                "change_reason": "ORGANIC_SOURCE_LINEAGE_REPLAY",
            }
        )
    return tuple(result)


def _failure_class(
    *,
    documents: Sequence[Mapping[str, Any]],
    claim_result: Any | None,
    accepted: Sequence[Mapping[str, Any]],
    mappings: Sequence[Mapping[str, Any]],
) -> str:
    if not documents:
        return "NO_DOCUMENT_FOUND"
    if claim_result and claim_result.compilation_pending:
        return "PROVIDER_FAILED"
    if accepted:
        return "IMPACT_MAPPING_FAILED"
    if mappings:
        return "IMPACT_MAPPING_FAILED"
    if claim_result and claim_result.adjudicated_claims:
        return "GENERIC_CONTEXT_ONLY"
    return "NO_DOCUMENT_FOUND"


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    if not path.is_file():
        return ()
    with path.open(encoding="utf-8") as handle:
        return tuple(json.loads(line) for line in handle if line.strip())


__all__ = [
    "ADAPTIVE_CLOSURE_SCHEMA_VERSION",
    "FAILURE_ACTIONS",
    "OrganicClaimClosureResult",
    "next_action_for_failure",
    "run_organic_claim_closure",
]
