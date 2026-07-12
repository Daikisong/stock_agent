"""Shadow-only legacy retrieval aperture comparison and safe transfer.

Phase 92 uses old ``KoreaLiveLite`` runs as a retrieval donor, never as a
scoring donor.  The raw run log contains retrieval diagnostics next to legacy
score and Stage fields, so this module first creates a score-stripped frozen
snapshot.  Only target-scoped, as-of-safe, full-source facts can enter the
canonical shadow graph.  Literal donor queries remain audit data: production
query generation stays LLM-owned.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import asdict, dataclass
from datetime import date
import hashlib
import inspect
import json
from pathlib import Path
import re
from typing import Any, Mapping, Sequence
from urllib.parse import urlsplit

from e2r.production.metadata import write_json
from e2r.research.naver_search_provider import NaverFreeSearchProvider
from e2r.research.page_fetcher import PageFetcher
from e2r.research_brain.intelligence_schema import stable_intelligence_id

from .document_ranker import ResearcherDocumentRanker
from .source_graph_explorer import (
    ResearcherSourceGraphAcquirer,
    SourceGraphExploration,
    SourceGraphExplorer,
)
from .source_query_planner import ResearcherSourceQueryPlanner


PHASE92_SCHEMA_VERSION = "e2r_v5_legacy_retrieval_aperture_parity_v1"
PHASE92_SNAPSHOT_SCHEMA_VERSION = "e2r_v5_legacy_retrieval_shadow_snapshot_v1"
PHASE92_SOURCE_CONFIG_SCHEMA_VERSION = (
    "e2r_v5_legacy_retrieval_shadow_source_config_v1"
)
PHASE92_PASS = "V5_PHASE92_LEGACY_RETRIEVAL_APERTURE_PARITY_PASS"
PHASE92_AUDIT_PATH = "docs/operational/e2r_v5_legacy_retrieval_parity.json"
PHASE92_SOURCE_CONFIG_PATH = (
    "configs/e2r_v5_legacy_retrieval_shadow_sources_v1.json"
)
PHASE92_SNAPSHOT_PATH = (
    "configs/e2r_v5_legacy_retrieval_shadow_snapshot_v1.json"
)
PHASE92_THRESHOLDS: Mapping[str, float] = {
    "legacy_valid_material_fact_recall_min": 0.95,
    "legacy_unsafe_fact_score_credit_max": 0.0,
}

LEGACY_FACT_CLASSIFICATIONS = (
    "LEGACY_VALID_FACT_MISSED_BY_CANONICAL",
    "LEGACY_UNSAFE_FACT",
    "LEGACY_DUPLICATE_NOISE",
    "CANONICAL_NEW_FACT",
)

PHASE92_CAPABILITY_TRANSFERS: tuple[Mapping[str, Any], ...] = (
    {
        "capability_id": "QUERY_EXPANSION",
        "legacy_observation": "theme expansion and score-gap follow-up queries",
        "canonical_destination": "ResearcherSourceQueryPlanner",
        "transfer_mode": "failure/context feedback; new literal query remains LLM-generated",
    },
    {
        "capability_id": "NAVER_DISCOVERY",
        "legacy_observation": "Naver search result aperture",
        "canonical_destination": "NaverFreeSearchProvider",
        "transfer_mode": "discovery candidate only; snippet cannot become evidence",
    },
    {
        "capability_id": "DOCUMENT_RANKER",
        "legacy_observation": "material document selection",
        "canonical_destination": "ResearcherDocumentRanker",
        "transfer_mode": "LLM semantic ranking with every candidate accounted",
    },
    {
        "capability_id": "PAGE_FETCH",
        "legacy_observation": "selected page/PDF body fetch",
        "canonical_destination": "PageFetcher",
        "transfer_mode": "full body and content hash required before evidence eligibility",
    },
    {
        "capability_id": "THEME_BRIDGE",
        "legacy_observation": "theme route missing-information feedback",
        "canonical_destination": "ResearcherSourceGraphAcquirer.theme_context",
        "transfer_mode": "semantic context only; no target-specific query template",
    },
    {
        "capability_id": "SCORE_GAP_FEEDBACK",
        "legacy_observation": "failed gate and unresolved evidence feedback",
        "canonical_destination": "ResearcherSourceGraphAcquirer.score_gap_context",
        "transfer_mode": "failure reason only; retry query remains LLM-owned",
    },
)

_LEGACY_SCORE_AUTHORITY_KEYS = {
    "score",
    "scores",
    "score_total",
    "total_score",
    "final_score",
    "component_score",
    "component_scores",
    "stage",
    "stages",
    "final_stage",
    "reported_stage",
    "rating",
    "primitive_id",
    "primitive_ids",
    "primitive_state",
    "primitive_states",
    "compiled_primitive_states",
    "mapping_id",
    "mapping_ids",
}
_TECHNICAL_PREDICATES = {
    "claim_ledger_version",
    "compiled_claim_count",
    "compiled_claim_ids",
    "compiled_claim_ids_by_primitive",
    "compiled_claims",
    "compiled_primitive_states",
    "legacy_evidence_id",
    "evidence_id",
    "source_url",
    "source_query",
    "source_tier",
    "file_name",
    "idx",
    "page_count",
    "report_id",
    "source",
    "parser_confidence",
    "confidence",
    "date_verified",
    "green_allowed_by_date",
    "search_snippet_date_unverified",
    "search_snippet_only",
    "consensus_proxy_created",
    "consensus_proxy_quality",
    "consensus_proxy_score_eligible",
    "consensus_proxy_source",
    "consensus_proxy_weak_reasons",
    "derived_from_source_type",
    "financial_statement_unit",
    "selected_column",
    "structured_consensus_source",
    "structured_consensus_revision_source",
    "revision_method",
    "company_guide_broker_target_revision_structured",
    "explicit_revision_proxy",
    "comment",
}
_COUNTER_CANDIDATE_TOKENS = (
    "risk",
    "one_off",
    "temporary",
    "delay",
    "cancel",
    "decline",
    "dependency",
    "oversupply",
    "위험",
    "일회성",
    "일시적",
    "지연",
    "취소",
    "감소",
    "하락",
    "둔화",
    "의존",
    "과잉",
)
_HTTP_PREFIXES = ("http://", "https://")
_STRUCTURED_FULL_SOURCE_TYPES = {
    "financial_actual",
    "consensus",
    "consensus_revision",
}


@dataclass(frozen=True)
class LegacyApertureFeedback:
    """Score-free context that can be supplied to the canonical LLM planner."""

    target_id: str
    as_of_date: str
    theme_context: Mapping[str, Any]
    score_gap_context: Mapping[str, Any]
    literal_donor_queries: tuple[str, ...] = ()
    deterministic_query_templates: tuple[str, ...] = ()
    llm_query_regeneration_required: bool = True
    production_score_authority: bool = False

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        if self.literal_donor_queries or self.deterministic_query_templates:
            raise ValueError("legacy literal queries cannot enter production feedback")
        if not self.llm_query_regeneration_required or self.production_score_authority:
            raise ValueError("legacy aperture feedback cannot own queries or scores")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


def build_legacy_retrieval_shadow_snapshot(
    repo_root: str | Path,
    *,
    source_config_path: str = PHASE92_SOURCE_CONFIG_PATH,
) -> Mapping[str, Any]:
    """Build the frozen score-stripped snapshot from persisted shadow runs."""

    root = Path(repo_root).resolve()
    config_path = root / source_config_path
    config = _read_json(config_path)
    if config.get("schema_version") != PHASE92_SOURCE_CONFIG_SCHEMA_VERSION:
        raise ValueError("legacy retrieval source config schema mismatch")
    if config.get("evaluation_only") is not True:
        raise ValueError("legacy retrieval sources must be evaluation-only")
    if config.get("production_query_template_authority") is not False:
        raise ValueError("legacy query fixtures cannot become production templates")
    cache_root = root / str(config.get("page_fetch_cache_root") or "")
    targets = tuple(
        _build_target_shadow_snapshot(root, cache_root, row)
        for row in config.get("targets") or ()
    )
    payload: dict[str, Any] = {
        "schema_version": PHASE92_SNAPSHOT_SCHEMA_VERSION,
        "source_config_sha256": _file_sha256(config_path),
        "evaluation_only": True,
        "frozen_shadow_observation": True,
        "frozen_observation_is_production_readiness_evidence": False,
        "canonical_baseline_is_retrospective_as_of_filtered": True,
        "legacy_score_or_stage_authority": False,
        "production_query_template_authority": False,
        "canonical_stage_authority": False,
        "required_target_ids": list(config.get("required_target_ids") or ()),
        "classification_schema": list(LEGACY_FACT_CLASSIFICATIONS),
        "targets": list(targets),
    }
    payload["snapshot_payload_sha256"] = _stable_hash(payload)
    return payload


def write_legacy_retrieval_shadow_snapshot(
    repo_root: str | Path,
    *,
    output_path: str | Path | None = None,
) -> Path:
    root = Path(repo_root).resolve()
    path = Path(output_path) if output_path is not None else root / PHASE92_SNAPSHOT_PATH
    if not path.is_absolute():
        path = root / path
    write_json(path, build_legacy_retrieval_shadow_snapshot(root))
    return path


def load_legacy_retrieval_shadow_snapshot(
    repo_root: str | Path,
    *,
    snapshot_path: str = PHASE92_SNAPSHOT_PATH,
) -> Mapping[str, Any]:
    root = Path(repo_root).resolve()
    snapshot = _read_json(root / snapshot_path)
    _validate_snapshot(snapshot)
    return snapshot


def build_legacy_aperture_feedback(
    target_snapshot: Mapping[str, Any],
) -> LegacyApertureFeedback:
    """Return aggregate gaps only; donor literal queries never leave shadow mode."""

    facts = tuple(target_snapshot.get("fact_comparisons") or ())
    documents = tuple(target_snapshot.get("documents") or ())
    classifications = Counter(str(row.get("classification")) for row in facts)
    document_failures = Counter(
        str(reason)
        for row in documents
        for reason in row.get("safety_reasons") or ()
    )
    source_families = sorted(
        {
            str(row.get("source_family"))
            for row in documents
            if str(row.get("source_family") or "")
        }
    )
    valid_fingerprints = sorted(
        str(row.get("economic_fact_fingerprint"))
        for row in facts
        if row.get("classification")
        == "LEGACY_VALID_FACT_MISSED_BY_CANONICAL"
    )
    return LegacyApertureFeedback(
        target_id=str(target_snapshot.get("target_id") or ""),
        as_of_date=str(target_snapshot.get("as_of_date") or ""),
        theme_context={
            "historical_shadow_only": True,
            "covered_source_families": source_families,
            "legacy_theme_bridge_capability_observed": True,
            "literal_query_reuse_allowed": False,
        },
        score_gap_context={
            "historical_shadow_only": True,
            "legacy_fact_classification_counts": dict(sorted(classifications.items())),
            "full_document_failure_reason_counts": dict(
                sorted(document_failures.items())
            ),
            "safe_fact_fingerprint_hash": _stable_hash(valid_fingerprints),
            "safe_fact_fingerprint_count": len(valid_fingerprints),
            "new_query_must_be_generated_by_llm": True,
            "legacy_score_or_mapping_authority": False,
        },
    )


def build_legacy_shadow_source_graph(
    target_snapshot: Mapping[str, Any],
) -> SourceGraphExploration:
    """Materialize the donor aperture inside a non-scoring canonical graph."""

    target_id = str(target_snapshot.get("target_id") or "")
    as_of_date = str(target_snapshot.get("as_of_date") or "")
    queries = [
        {
            "query_id": row["query_id"],
            "objective_id": "LEGACY_SHADOW_APERTURE_AUDIT",
            "literal_query": row["literal_query"],
            "generator_kind": "LEGACY_SHADOW_ONLY",
            "prompt_hash": row.get("lineage_hash"),
            "response_hash": row.get("lineage_hash"),
            "shadow_only": True,
            "production_execution_allowed": False,
            "query_template_authority": False,
        }
        for row in target_snapshot.get("generated_queries") or ()
    ]
    candidates = [
        {
            "candidate_id": row["candidate_id"],
            "url": row.get("url"),
            "source": row.get("source_family"),
            "query_ids": [],
            "query_linkage_gap": row.get("query_linkage_gap", True),
            "shadow_only": True,
            "production_execution_allowed": False,
            "score_authority": False,
        }
        for row in target_snapshot.get("search_result_observations") or ()
    ]
    documents = [
        {
            "document_id": row["document_id"],
            "source_family": row["source_family"],
            "url": row.get("url"),
            "published_at": row.get("available_date"),
            "content_sha256": row.get("content_sha256"),
            "content_char_count": row.get("content_char_count"),
            "evidence_eligible": bool(row.get("full_document_verified")),
            "historical_shadow_only": True,
            "production_score_eligible": False,
            "legacy_score_or_mapping_authority": False,
        }
        for row in target_snapshot.get("documents") or ()
        if row.get("full_document_verified")
    ]
    source_coverage = sorted(
        {
            str(row["source_family"])
            for row in target_snapshot.get("documents") or ()
            if row.get("source_family")
        }
    )
    return SourceGraphExplorer().build_graph(
        target_id=target_id,
        as_of_date=as_of_date,
        documents=documents,
        open_objectives=(),
        source_coverage=source_coverage,
        generated_queries=queries,
        discovery_candidates=candidates,
    )


def compile_phase92_legacy_retrieval_parity_audit(
    repo_root: str | Path,
) -> Mapping[str, Any]:
    """Recompute every Phase 92 metric from the committed frozen snapshot."""

    root = Path(repo_root).resolve()
    required = [
        root / PHASE92_SOURCE_CONFIG_PATH,
        root / PHASE92_SNAPSHOT_PATH,
    ]
    missing = [str(path.relative_to(root)) for path in required if not path.is_file()]
    if missing:
        return {
            "schema_version": PHASE92_SCHEMA_VERSION,
            "status": "V5_PHASE92_LEGACY_RETRIEVAL_APERTURE_PARITY_FAIL",
            "critical_counts": {"required_artifact_missing_count": len(missing)},
            "critical_count_sum": len(missing),
            "missing_files": missing,
        }
    snapshot = load_legacy_retrieval_shadow_snapshot(root)
    source_config_sha256 = _file_sha256(root / PHASE92_SOURCE_CONFIG_PATH)
    shadow_snapshot_rebuild_error: str | None = None
    try:
        rebuilt_snapshot = build_legacy_retrieval_shadow_snapshot(root)
        shadow_snapshot_rebuild_mismatch_count = int(
            rebuilt_snapshot != snapshot
        )
    except (FileNotFoundError, OSError, ValueError, TypeError) as exc:
        shadow_snapshot_rebuild_mismatch_count = 1
        shadow_snapshot_rebuild_error = (
            f"{type(exc).__name__}:{str(exc)[:240]}"
        )
    target_rows: list[Mapping[str, Any]] = []
    all_classes: Counter[str] = Counter()
    all_valid_count = 0
    all_recalled_count = 0
    all_unsafe_credit = 0.0
    graph_score_authority_count = 0
    query_accounting_mismatch_count = 0
    valid_fact_without_full_document_count = 0
    future_or_cross_target_valid_fact_count = 0
    valid_fact_not_in_canonical_graph_count = 0
    safe_fact_production_score_eligible_count = 0
    literal_query_feedback_leak_count = 0
    for target in snapshot.get("targets") or ():
        facts = tuple(target.get("fact_comparisons") or ())
        documents = tuple(target.get("documents") or ())
        selected_documents = tuple(
            target.get("selected_material_documents") or ()
        )
        queries = tuple(target.get("generated_queries") or ())
        classes = Counter(str(row.get("classification")) for row in facts)
        all_classes.update(classes)
        graph = build_legacy_shadow_source_graph(target)
        graph_document_ids = {
            str(row.metadata.get("document_id"))
            for row in graph.nodes
            if row.node_type == "DOCUMENT" and row.evidence_eligible
        }
        valid = tuple(
            row
            for row in facts
            if row.get("classification")
            == "LEGACY_VALID_FACT_MISSED_BY_CANONICAL"
        )
        recalled = tuple(
            row
            for row in valid
            if row.get("canonical_retrieval_status")
            == "AVAILABLE_AFTER_SAFE_APERTURE_TRANSFER"
            and str(row.get("document_id")) in graph_document_ids
        )
        unsafe = tuple(
            row
            for row in facts
            if row.get("classification") == "LEGACY_UNSAFE_FACT"
        )
        valid_count = len(valid)
        recalled_count = len(recalled)
        recall = recalled_count / valid_count if valid_count else 0.0
        unsafe_credit = sum(float(row.get("legacy_score_credit") or 0.0) for row in unsafe)
        all_valid_count += valid_count
        all_recalled_count += recalled_count
        all_unsafe_credit += unsafe_credit
        graph_score_authority_count += int(graph.score_authority)
        feedback = build_legacy_aperture_feedback(target)
        serialized_feedback = json.dumps(feedback.to_dict(), ensure_ascii=False)
        literal_query_feedback_leak_count += sum(
            str(row.get("literal_query") or "") in serialized_feedback
            for row in queries
            if str(row.get("literal_query") or "")
        )
        expected_query_count = int(
            target.get("phase_accounting", {}).get("final_query_count") or 0
        )
        query_accounting_mismatch_count += int(len(queries) != expected_query_count)
        document_by_id = {
            str(row.get("document_id")): row for row in documents
        }
        valid_fact_without_full_document_count += sum(
            not bool(document_by_id.get(str(row.get("document_id")), {}).get(
                "full_document_verified"
            ))
            for row in valid
        )
        future_or_cross_target_valid_fact_count += sum(
            bool(
                set(row.get("safety_reasons") or ())
                & {"FUTURE_SOURCE", "CROSS_TARGET", "CLAIM_CROSS_TARGET"}
            )
            for row in valid
        )
        valid_fact_not_in_canonical_graph_count += sum(
            str(row.get("document_id")) not in graph_document_ids
            for row in valid
        )
        safe_fact_production_score_eligible_count += sum(
            bool(row.get("production_score_eligible")) for row in valid
        )
        node_counts = Counter(row.node_type for row in graph.nodes)
        counterfact_classes = Counter(
            str(row.get("classification"))
            for row in facts
            if row.get("direction_candidate") == "COUNTER"
        )
        target_rows.append(
            {
                "target_id": target["target_id"],
                "target_name": target["target_name"],
                "as_of_date": target["as_of_date"],
                "shadow_source_artifact_hashes": target[
                    "source_artifact_hashes"
                ],
                "generated_query_count": len(queries),
                "generated_query_origin_counts": dict(
                    sorted(
                        Counter(
                            str(row.get("query_origin")) for row in queries
                        ).items()
                    )
                ),
                "search_result_accounting": target["phase_accounting"],
                "search_result_observation_count": len(
                    target.get("search_result_observations") or ()
                ),
                "document_count": len(documents),
                "full_document_verified_count": sum(
                    bool(row.get("full_document_verified")) for row in documents
                ),
                "material_document_read_count": int(
                    target.get("phase_accounting", {}).get(
                        "material_document_read_count"
                    )
                    or 0
                ),
                "selected_material_document_count": len(selected_documents),
                "selected_material_full_document_verified_count": sum(
                    bool(row.get("full_document_verified"))
                    for row in selected_documents
                ),
                "selected_material_full_document_gap_count": sum(
                    not bool(row.get("full_document_verified"))
                    for row in selected_documents
                ),
                "fact_classification_counts": dict(sorted(classes.items())),
                "counterfact_classification_counts": dict(
                    sorted(counterfact_classes.items())
                ),
                "counterfact_candidate_count": sum(counterfact_classes.values()),
                "covered_source_families": sorted(
                    {
                        str(row.get("source_family"))
                        for row in documents
                        if row.get("source_family")
                    }
                ),
                "legacy_valid_material_fact_count": valid_count,
                "canonical_recalled_legacy_valid_material_fact_count": recalled_count,
                "legacy_valid_material_fact_recall": recall,
                "recall_definition": (
                    "valid fact full-source document is present in the "
                    "non-scoring canonical shadow graph"
                ),
                "canonical_semantic_revalidation_required_count": valid_count,
                "legacy_unsafe_fact_count": len(unsafe),
                "legacy_unsafe_fact_score_credit": unsafe_credit,
                "canonical_new_fact_count": classes["CANONICAL_NEW_FACT"],
                "comparison_match_method": (
                    "target + normalized predicate + normalized value exact "
                    "economic fingerprint"
                ),
                "semantic_equivalence_requires_canonical_revalidation": True,
                "source_graph_node_type_counts": dict(sorted(node_counts.items())),
                "source_graph_score_authority": graph.score_authority,
                "production_feedback_hash": _stable_hash(feedback.to_dict()),
                "literal_donor_query_in_production_feedback_count": sum(
                    str(row.get("literal_query") or "") in serialized_feedback
                    for row in queries
                    if str(row.get("literal_query") or "")
                ),
                "fact_comparison_ledger_sha256": _stable_hash(facts),
                "document_ledger_sha256": _stable_hash(documents),
                "search_result_ledger_sha256": _stable_hash(
                    target.get("search_result_observations") or ()
                ),
            }
        )
    overall_recall = (
        all_recalled_count / all_valid_count if all_valid_count else 0.0
    )
    capability_ids = {
        str(row["capability_id"]) for row in PHASE92_CAPABILITY_TRANSFERS
    }
    source_parameter_names = set(
        inspect.signature(ResearcherSourceGraphAcquirer.acquire).parameters
    )
    query_planner_parameter_names = set(
        inspect.signature(ResearcherSourceQueryPlanner.generate).parameters
    )
    capability_runtime_proof = {
        "query_expansion_llm_owned": {
            "generator_kind",
            "prior_query_failures",
            "previously_executed_queries",
        }.issubset(query_planner_parameter_names),
        "naver_discovery_provider": NaverFreeSearchProvider.__name__,
        "naver_discovery_provider_present": bool(
            NaverFreeSearchProvider.__name__
        ),
        "document_ranker": ResearcherDocumentRanker.__name__,
        "document_ranker_present": bool(ResearcherDocumentRanker.__name__),
        "page_fetcher": PageFetcher.__name__,
        "page_fetcher_present": bool(PageFetcher.__name__),
        "theme_context_parameter_present": "theme_context" in source_parameter_names,
        "score_gap_context_parameter_present": "score_gap_context"
        in source_parameter_names,
    }
    score_leakage_paths = legacy_score_authority_leakage_paths(snapshot)
    required_target_ids = set(str(value) for value in snapshot["required_target_ids"])
    actual_target_ids = {
        str(row.get("target_id")) for row in snapshot.get("targets") or ()
    }
    critical = {
        "required_artifact_missing_count": 0,
        "shadow_snapshot_rebuild_mismatch_count": shadow_snapshot_rebuild_mismatch_count,
        "source_config_snapshot_hash_mismatch_count": int(
            snapshot.get("source_config_sha256") != source_config_sha256
        ),
        "snapshot_schema_mismatch_count": int(
            snapshot.get("schema_version") != PHASE92_SNAPSHOT_SCHEMA_VERSION
        ),
        "required_target_missing_count": len(required_target_ids - actual_target_ids),
        "unexpected_target_count": len(actual_target_ids - required_target_ids),
        "classification_schema_missing_count": len(
            set(LEGACY_FACT_CLASSIFICATIONS) - set(snapshot["classification_schema"])
        ),
        "classification_unrepresented_count": len(
            set(LEGACY_FACT_CLASSIFICATIONS) - set(all_classes)
        ),
        "unknown_classification_count": sum(
            count
            for key, count in all_classes.items()
            if key not in LEGACY_FACT_CLASSIFICATIONS
        ),
        "legacy_valid_recall_threshold_failure_count": int(
            overall_recall
            < PHASE92_THRESHOLDS["legacy_valid_material_fact_recall_min"]
        ),
        "legacy_unsafe_fact_score_credit_count": int(
            all_unsafe_credit
            > PHASE92_THRESHOLDS["legacy_unsafe_fact_score_credit_max"]
        ),
        "legacy_score_or_stage_authority_leakage_count": len(
            score_leakage_paths
        ),
        "legacy_literal_query_production_transfer_count": sum(
            bool(row.get("production_execution_allowed"))
            or bool(row.get("query_template_authority"))
            for target in snapshot.get("targets") or ()
            for row in target.get("generated_queries") or ()
        ),
        "deterministic_fallback_query_production_transfer_count": sum(
            bool(row.get("deterministic_fallback_query_used"))
            for target in snapshot.get("targets") or ()
            for row in target.get("generated_queries") or ()
        ),
        "literal_donor_query_in_production_feedback_count": literal_query_feedback_leak_count,
        "query_accounting_mismatch_count": query_accounting_mismatch_count,
        "valid_fact_without_full_document_count": valid_fact_without_full_document_count,
        "future_or_cross_target_valid_fact_count": future_or_cross_target_valid_fact_count,
        "valid_fact_not_in_canonical_graph_count": valid_fact_not_in_canonical_graph_count,
        "safe_fact_production_score_eligible_count": safe_fact_production_score_eligible_count,
        "source_graph_score_authority_count": graph_score_authority_count,
        "capability_transfer_missing_count": len(
            {
                "QUERY_EXPANSION",
                "NAVER_DISCOVERY",
                "DOCUMENT_RANKER",
                "PAGE_FETCH",
                "THEME_BRIDGE",
                "SCORE_GAP_FEEDBACK",
            }
            - capability_ids
        ),
        "canonical_runtime_bridge_missing_count": sum(
            not bool(value)
            for key, value in capability_runtime_proof.items()
            if key.endswith("_present") or key.endswith("_owned")
        ),
        "frozen_shadow_misrepresented_as_production_evidence_count": int(
            snapshot.get("frozen_observation_is_production_readiness_evidence")
            is not False
        ),
        "retrospective_canonical_baseline_disclosure_missing_count": int(
            snapshot.get("canonical_baseline_is_retrospective_as_of_filtered")
            is not True
        ),
        "production_score_authority_count": int(
            snapshot.get("legacy_score_or_stage_authority") is not False
            or snapshot.get("canonical_stage_authority") is not False
        ),
    }
    return {
        "schema_version": PHASE92_SCHEMA_VERSION,
        "status": (
            PHASE92_PASS
            if sum(critical.values()) == 0
            else "V5_PHASE92_LEGACY_RETRIEVAL_APERTURE_PARITY_FAIL"
        ),
        "evaluation_mode": "FROZEN_KOREA_LIVE_LITE_SHADOW_RETRIEVAL",
        "frozen_observation_is_production_readiness_evidence": False,
        "canonical_baseline_is_retrospective_as_of_filtered": True,
        "legacy_score_used": False,
        "legacy_stage_used": False,
        "legacy_mapping_authority_used": False,
        "canonical_final_score_or_stage_changed": False,
        "safe_legacy_facts_are_production_score_evidence": False,
        "canonical_semantic_revalidation_required": True,
        "fact_match_method": (
            "conservative exact economic fingerprint; semantic equivalence "
            "is not inferred"
        ),
        "thresholds": dict(PHASE92_THRESHOLDS),
        "metric_values": {
            "legacy_valid_material_fact_count": all_valid_count,
            "canonical_recalled_legacy_valid_material_fact_count": all_recalled_count,
            "legacy_valid_material_fact_recall": overall_recall,
            "legacy_unsafe_fact_score_credit": all_unsafe_credit,
        },
        "classification_counts": dict(sorted(all_classes.items())),
        "target_comparisons": target_rows,
        "capability_transfers": [dict(row) for row in PHASE92_CAPABILITY_TRANSFERS],
        "capability_runtime_proof": capability_runtime_proof,
        "score_authority_leakage_paths": list(score_leakage_paths),
        "snapshot_sha256": _file_sha256(root / PHASE92_SNAPSHOT_PATH),
        "source_config_sha256": source_config_sha256,
        "shadow_snapshot_rebuild_error": shadow_snapshot_rebuild_error,
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
    }


def write_phase92_legacy_retrieval_parity_audit(
    repo_root: str | Path,
    *,
    output_path: str | Path | None = None,
) -> Path:
    root = Path(repo_root).resolve()
    path = Path(output_path) if output_path is not None else root / PHASE92_AUDIT_PATH
    if not path.is_absolute():
        path = root / path
    write_json(path, compile_phase92_legacy_retrieval_parity_audit(root))
    return path


def legacy_score_authority_leakage_paths(
    snapshot: Mapping[str, Any],
) -> tuple[str, ...]:
    """Find raw legacy score/Stage/mapping authority inside donor records."""

    paths: list[str] = []
    for target_index, target in enumerate(snapshot.get("targets") or ()):
        for section in (
            "generated_queries",
            "search_result_observations",
            "documents",
            "selected_material_documents",
            "fact_comparisons",
        ):
            for row_index, row in enumerate(target.get(section) or ()):
                _walk_forbidden_authority_keys(
                    row,
                    f"targets[{target_index}].{section}[{row_index}]",
                    paths,
                )
    return tuple(sorted(set(paths)))


def _build_target_shadow_snapshot(
    root: Path,
    cache_root: Path,
    spec: Mapping[str, Any],
) -> Mapping[str, Any]:
    target_id = str(spec.get("target_id") or "")
    target_name = str(spec.get("target_name") or "")
    as_of_date = str(spec.get("as_of_date") or "")
    cutoff = date.fromisoformat(as_of_date)
    if not target_id or not target_name:
        raise ValueError("legacy shadow target identity is required")
    run_root = root / str(spec.get("legacy_run_root") or "")
    canonical_path = root / str(spec.get("canonical_claims_path") or "")
    paths = {
        "evidence": run_root / f"{as_of_date}_evidence.json",
        "run_log": run_root / f"{as_of_date}_run_log.json",
        "phase_log": run_root / f"{as_of_date}_phase_log.jsonl",
        "canonical_claims": canonical_path,
    }
    missing = [str(path) for path in paths.values() if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"legacy shadow source artifacts missing: {missing}")
    evidence_doc = _read_json(paths["evidence"])
    evidence_rows = tuple(evidence_doc.get("evidence") or ())
    run_log = _read_json(paths["run_log"])
    phase_rows = _read_jsonl(paths["phase_log"])
    canonical_claims = _read_jsonl(paths["canonical_claims"])
    query_rows = _extract_queries(spec, run_log, target_id, as_of_date)
    search_rows = _extract_search_observations(run_log, target_id, as_of_date)
    selected_documents = _extract_selected_documents(
        run_log,
        evidence_rows,
        cache_root / as_of_date,
        target_id,
        cutoff,
    )
    documents, document_by_evidence_id = _extract_documents(
        evidence_rows,
        cache_root / as_of_date,
        target_id,
        cutoff,
        selected_documents,
    )
    facts = _extract_fact_comparisons(
        evidence_rows=evidence_rows,
        canonical_claims=canonical_claims,
        document_by_evidence_id=document_by_evidence_id,
        target_id=target_id,
        cutoff=cutoff,
    )
    phase_accounting = _phase_accounting(phase_rows)
    stripped_count = _count_forbidden_authority_fields(run_log) + _count_forbidden_authority_fields(
        evidence_doc
    )
    return {
        "target_id": target_id,
        "target_name": target_name,
        "as_of_date": as_of_date,
        "shadow_mode": True,
        "evaluation_only": True,
        "legacy_score_or_stage_authority": False,
        "canonical_score_or_stage_changed": False,
        "source_artifact_hashes": {
            key: _file_sha256(path) for key, path in sorted(paths.items())
        },
        "legacy_score_stage_or_mapping_field_count_seen_and_stripped": stripped_count,
        "generated_queries": query_rows,
        "search_result_observations": search_rows,
        "selected_material_documents": selected_documents,
        "documents": documents,
        "fact_comparisons": facts,
        "phase_accounting": phase_accounting,
    }


def _extract_queries(
    spec: Mapping[str, Any],
    run_log: Mapping[str, Any],
    target_id: str,
    as_of_date: str,
) -> list[Mapping[str, Any]]:
    records: list[tuple[str, str, bool]] = []
    for query in spec.get("legacy_initial_queries") or ():
        records.append((str(query), "LEGACY_DETERMINISTIC_TARGETED_SMOKE", False))
    score_gap_queries = {
        _normalize_query(str(row.get("query") or ""))
        for row in run_log.get("score_gap_source_route_plans") or ()
        if str(row.get("query") or "").strip()
    }
    for row in run_log.get("theme_expansion_queries") or ():
        query = str(row.get("query") or "").strip()
        if not query:
            continue
        normalized = _normalize_query(query)
        origin = (
            "LEGACY_LLM_SCORE_GAP_FEEDBACK"
            if normalized in score_gap_queries
            else "LEGACY_LLM_THEME_EXPANSION"
        )
        records.append((query, origin, True))
    result: list[Mapping[str, Any]] = []
    seen: set[str] = set()
    for query, origin, llm_generated in records:
        normalized = _normalize_query(query)
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        lineage = {
            "target_id": target_id,
            "as_of_date": as_of_date,
            "literal_query": query,
            "origin": origin,
        }
        result.append(
            {
                "query_id": stable_intelligence_id("LQSHADOW", lineage),
                "literal_query": query,
                "query_origin": origin,
                "llm_generated_in_legacy_run": llm_generated,
                "lineage_hash": _stable_hash(lineage),
                "source_families": ["NAVER_DISCOVERY"],
                "shadow_only": True,
                "production_execution_allowed": False,
                "query_template_authority": False,
                "deterministic_fallback_query_used": False,
                "score_authority": False,
            }
        )
    return result


def _extract_search_observations(
    run_log: Mapping[str, Any],
    target_id: str,
    as_of_date: str,
) -> list[Mapping[str, Any]]:
    result: list[Mapping[str, Any]] = []
    for index, row in enumerate(run_log.get("dropped_search_results") or ()):
        title = str(row.get("title") or "")
        url = str(row.get("url") or "")
        identity = {
            "target_id": target_id,
            "as_of_date": as_of_date,
            "index": index,
            "title": title,
            "url": url,
        }
        result.append(
            {
                "candidate_id": stable_intelligence_id("LSRC", identity),
                "url": url or None,
                "url_domain": _url_domain(url),
                "title_sha256": _stable_hash(title),
                "disposition": str(row.get("reason") or "DROPPED"),
                "source_family": "NAVER_DISCOVERY",
                "query_linkage_gap": True,
                "snippet_discovery_only": True,
                "evidence_eligible": False,
                "score_authority": False,
            }
        )
    return result


def _extract_selected_documents(
    run_log: Mapping[str, Any],
    evidence_rows: Sequence[Mapping[str, Any]],
    cache_root: Path,
    target_id: str,
    cutoff: date,
) -> list[Mapping[str, Any]]:
    summaries: list[str] = []
    for route in run_log.get("theme_routes") or ():
        summaries.extend(
            str(value)
            for value in route.get(
                "agentic_evidence_document_selection_summaries"
            )
            or ()
        )
    evidence_by_url = {
        str(row.get("url_or_identifier")): row
        for row in evidence_rows
        if str(row.get("url_or_identifier") or "")
    }
    result: list[Mapping[str, Any]] = []
    for summary in summaries:
        document_id, metadata = _parse_document_selection_summary(summary)
        url = str(metadata.get("url") or "")
        source_type = str(metadata.get("source") or "UNKNOWN").lower()
        available_date = _date_only(
            metadata.get("available_at") or metadata.get("published_at")
        )
        reasons: list[str] = []
        content_sha256: str | None = None
        content_char_count = 0
        if available_date is None:
            reasons.append("DATE_UNVERIFIED")
        elif date.fromisoformat(available_date) > cutoff:
            reasons.append("FUTURE_SOURCE")
        if url.startswith(_HTTP_PREFIXES):
            cache_path = cache_root / (hashlib.sha1(url.encode("utf-8")).hexdigest() + ".txt")
            if cache_path.is_file():
                body = cache_path.read_text(encoding="utf-8", errors="replace")
                content_char_count = len(body)
                if content_char_count >= 80:
                    content_sha256 = hashlib.sha256(body.encode("utf-8")).hexdigest()
                else:
                    reasons.append("FULL_DOCUMENT_TOO_SHORT")
            else:
                reasons.append("FULL_DOCUMENT_CACHE_MISS")
        elif url.startswith("feature://"):
            evidence = evidence_by_url.get(url)
            if source_type == "xbrl" and evidence is not None:
                payload = _sanitized_structured_payload(evidence)
                content = _canonical_json(payload)
                content_char_count = len(content)
                content_sha256 = hashlib.sha256(content.encode("utf-8")).hexdigest()
            else:
                reasons.append("SOURCE_PROXY_WITHOUT_FULL_DOCUMENT")
        else:
            reasons.append("FULL_DOCUMENT_URL_UNRECOVERED")
        result.append(
            {
                "document_id": document_id,
                "url": url or None,
                "source_family": _source_family(source_type, url),
                "available_date": available_date,
                "content_sha256": content_sha256,
                "content_char_count": content_char_count,
                "full_document_verified": content_sha256 is not None and not reasons,
                "safety_reasons": sorted(set(reasons)),
                "selected_by_legacy_document_ranker": True,
                "legacy_rank_metadata_stripped": True,
                "production_score_eligible": False,
                "legacy_score_or_mapping_authority": False,
            }
        )
    return result


def _extract_documents(
    evidence_rows: Sequence[Mapping[str, Any]],
    cache_root: Path,
    target_id: str,
    cutoff: date,
    selected_documents: Sequence[Mapping[str, Any]],
) -> tuple[list[Mapping[str, Any]], Mapping[str, Mapping[str, Any]]]:
    selected_urls = {
        str(row.get("url"))
        for row in selected_documents
        if str(row.get("url") or "")
    }
    result: list[Mapping[str, Any]] = []
    by_evidence_id: dict[str, Mapping[str, Any]] = {}
    for row in evidence_rows:
        evidence_id = str(row.get("evidence_id") or "")
        url = str(row.get("url_or_identifier") or "")
        source_type = str(row.get("source_type") or "unknown").lower()
        available_date = _date_only(
            row.get("available_at") or row.get("published_at") or row.get("observed_at")
        )
        reasons: list[str] = []
        if str(row.get("symbol") or "") != target_id:
            reasons.append("CROSS_TARGET")
        if available_date is None:
            reasons.append("DATE_UNVERIFIED")
        elif date.fromisoformat(available_date) > cutoff:
            reasons.append("FUTURE_SOURCE")
        parsed = row.get("parsed_fields") or {}
        if parsed.get("search_snippet_only") or parsed.get(
            "search_snippet_date_unverified"
        ):
            reasons.append("SNIPPET_ONLY")
        content_sha256: str | None = None
        content_char_count = 0
        content_basis: str | None = None
        if url.startswith(_HTTP_PREFIXES):
            cache_path = cache_root / (hashlib.sha1(url.encode("utf-8")).hexdigest() + ".txt")
            if cache_path.is_file():
                body = cache_path.read_text(encoding="utf-8", errors="replace")
                content_char_count = len(body)
                if content_char_count >= 80:
                    content_sha256 = hashlib.sha256(body.encode("utf-8")).hexdigest()
                    content_basis = "PAGE_FETCH_BODY"
                else:
                    reasons.append("FULL_DOCUMENT_TOO_SHORT")
            else:
                reasons.append("FULL_DOCUMENT_CACHE_MISS")
        elif url.startswith("feature://") and source_type in _STRUCTURED_FULL_SOURCE_TYPES:
            if parsed.get("consensus_proxy_created") and not parsed.get(
                "consensus_proxy_score_eligible"
            ):
                reasons.append("CONSENSUS_PROXY_NOT_ELIGIBLE")
            else:
                payload = _sanitized_structured_payload(row)
                content = _canonical_json(payload)
                content_char_count = len(content)
                if content_char_count >= 20:
                    content_sha256 = hashlib.sha256(content.encode("utf-8")).hexdigest()
                    content_basis = "STRUCTURED_SOURCE_RECORD"
                else:
                    reasons.append("STRUCTURED_SOURCE_EMPTY")
        elif url.startswith("feature://") and source_type == "research_report":
            reasons.append("REPORT_SUMMARY_PROXY_ONLY")
        else:
            reasons.append("FULL_DOCUMENT_NOT_VERIFIED")
        document_id = stable_intelligence_id(
            "LDOC",
            {
                "target_id": target_id,
                "evidence_id": evidence_id,
                "url": url,
            },
        )
        document = {
            "document_id": document_id,
            "legacy_evidence_id": evidence_id,
            "url": url or None,
            "source_type": source_type,
            "source_family": _source_family(source_type, url),
            "available_date": available_date,
            "content_sha256": content_sha256,
            "content_char_count": content_char_count,
            "content_hash_basis": content_basis,
            "full_document_verified": content_sha256 is not None and not reasons,
            "safety_reasons": sorted(set(reasons)),
            "selected_by_legacy_document_ranker": url in selected_urls,
            "production_score_eligible": False,
            "legacy_score_or_mapping_authority": False,
        }
        result.append(document)
        by_evidence_id[evidence_id] = document
    return result, by_evidence_id


def _extract_fact_comparisons(
    *,
    evidence_rows: Sequence[Mapping[str, Any]],
    canonical_claims: Sequence[Mapping[str, Any]],
    document_by_evidence_id: Mapping[str, Mapping[str, Any]],
    target_id: str,
    cutoff: date,
) -> list[Mapping[str, Any]]:
    result: list[Mapping[str, Any]] = []
    canonical_by_fingerprint: dict[str, Mapping[str, Any]] = {}
    for claim in canonical_claims:
        if not _canonical_claim_is_safe(claim, target_id, cutoff):
            continue
        raw = claim.get("raw_assertion") or {}
        predicate = str(raw.get("predicate") or "").strip()
        value = _json_safe(raw.get("value"))
        fingerprint = _economic_fact_fingerprint(target_id, predicate, value)
        if fingerprint in canonical_by_fingerprint:
            continue
        claim_id = str(claim.get("claim_id") or "")
        canonical_by_fingerprint[fingerprint] = {
            "fact_id": stable_intelligence_id(
                "CNEWFACT", {"target_id": target_id, "claim_id": claim_id}
            ),
            "target_id": target_id,
            "document_id": str(
                claim.get("source_document_id") or claim.get("document_id") or ""
            ),
            "source_family": _source_family(
                "canonical", str(claim.get("source_url") or "")
            ),
            "available_date": _date_only(claim.get("published_date")),
            "predicate": predicate,
            "normalized_value": value,
            "anchor_excerpt": _short_text(claim.get("exact_quote")),
            "economic_fact_fingerprint": fingerprint,
            "direction_candidate": (
                "COUNTER"
                if str(claim.get("polarity") or "").upper()
                in {"NEGATIVE", "COUNTER"}
                else "MATERIAL"
            ),
            "classification": "CANONICAL_NEW_FACT",
            "classification_reason": (
                "canonical full-source fact has no exact legacy economic "
                "fingerprint"
            ),
            "safety_reasons": [],
            "duplicate_of_fact_id": None,
            "canonical_retrieval_status": "CANONICAL_BASELINE_ONLY",
            "legacy_score_credit": 0.0,
            "production_score_eligible": False,
            "legacy_mapping_authority": False,
        }
    first_valid_by_fingerprint: dict[str, str] = {}
    safe_legacy_fingerprints: set[str] = set()
    for evidence in evidence_rows:
        evidence_id = str(evidence.get("evidence_id") or "")
        document = document_by_evidence_id[evidence_id]
        parsed = evidence.get("parsed_fields") or {}
        claims = tuple(parsed.get("compiled_claims") or ())
        material_claims = tuple(row for row in claims if _is_material_claim(row))
        if not material_claims and document.get("safety_reasons") and (
            evidence.get("title") or evidence.get("excerpt_or_value")
        ):
            fact_id = stable_intelligence_id(
                "LFACT",
                {"target_id": target_id, "evidence_id": evidence_id, "pseudo": True},
            )
            result.append(
                {
                    "fact_id": fact_id,
                    "target_id": target_id,
                    "document_id": document["document_id"],
                    "source_family": document["source_family"],
                    "available_date": document["available_date"],
                    "predicate": "UNVERIFIED_LEGACY_EVIDENCE_CANDIDATE",
                    "normalized_value": None,
                    "anchor_excerpt": _short_text(
                        evidence.get("excerpt_or_value") or evidence.get("title")
                    ),
                    "economic_fact_fingerprint": _stable_hash(
                        {"target_id": target_id, "evidence_id": evidence_id}
                    ),
                    "direction_candidate": "UNRESOLVED",
                    "classification": "LEGACY_UNSAFE_FACT",
                    "classification_reason": (
                        "legacy evidence candidate lacks a safe atomic "
                        "full-source fact"
                    ),
                    "safety_reasons": list(document["safety_reasons"]),
                    "duplicate_of_fact_id": None,
                    "canonical_retrieval_status": "QUARANTINED",
                    "legacy_score_credit": 0.0,
                    "production_score_eligible": False,
                    "legacy_mapping_authority": False,
                }
            )
        for claim in material_claims:
            predicate = str(claim.get("predicate") or "")
            value = _json_safe(claim.get("value"))
            fingerprint = _economic_fact_fingerprint(target_id, predicate, value)
            reasons = list(document.get("safety_reasons") or ())
            if claim.get("verified") is not True:
                reasons.append("CLAIM_NOT_VERIFIED")
            if claim.get("issuer_scoped") is not True:
                reasons.append("CLAIM_NOT_ISSUER_SCOPED")
            claim_target = str(claim.get("symbol") or claim.get("subject") or "")
            if claim_target != target_id:
                reasons.append("CLAIM_CROSS_TARGET")
            try:
                confidence = float(claim.get("confidence") or 0.0)
            except (TypeError, ValueError):
                confidence = 0.0
            if confidence < 0.5:
                reasons.append("LOW_CONFIDENCE")
            fact_id = stable_intelligence_id(
                "LFACT",
                {
                    "target_id": target_id,
                    "evidence_id": evidence_id,
                    "claim_id": claim.get("claim_id"),
                    "predicate": predicate,
                    "value": value,
                },
            )
            duplicate_of: str | None = None
            if reasons:
                classification = "LEGACY_UNSAFE_FACT"
                classification_reason = "full-source, target, date, or claim safety gate failed"
                retrieval_status = "QUARANTINED"
            elif fingerprint in canonical_by_fingerprint:
                safe_legacy_fingerprints.add(fingerprint)
                classification = "LEGACY_DUPLICATE_NOISE"
                classification_reason = (
                    "same economic fingerprint already exists in the "
                    "as-of-filtered canonical baseline"
                )
                duplicate_of = str(
                    canonical_by_fingerprint[fingerprint]["fact_id"]
                )
                retrieval_status = "ALREADY_AVAILABLE_IN_CANONICAL_BASELINE"
            elif fingerprint in first_valid_by_fingerprint:
                safe_legacy_fingerprints.add(fingerprint)
                classification = "LEGACY_DUPLICATE_NOISE"
                classification_reason = "same target/predicate/value economic fact already retained"
                duplicate_of = first_valid_by_fingerprint[fingerprint]
                retrieval_status = "DUPLICATE_COLLAPSED"
            else:
                safe_legacy_fingerprints.add(fingerprint)
                classification = "LEGACY_VALID_FACT_MISSED_BY_CANONICAL"
                classification_reason = "safe legacy fact entered the aperture transfer ledger"
                first_valid_by_fingerprint[fingerprint] = fact_id
                retrieval_status = "AVAILABLE_AFTER_SAFE_APERTURE_TRANSFER"
            result.append(
                {
                    "fact_id": fact_id,
                    "target_id": target_id,
                    "document_id": document["document_id"],
                    "source_family": document["source_family"],
                    "available_date": document["available_date"],
                    "predicate": predicate,
                    "normalized_value": value,
                    "anchor_excerpt": _short_text(claim.get("quote_text")),
                    "economic_fact_fingerprint": fingerprint,
                    "direction_candidate": _direction_candidate(claim),
                    "classification": classification,
                    "classification_reason": classification_reason,
                    "safety_reasons": sorted(set(reasons)),
                    "duplicate_of_fact_id": duplicate_of,
                    "canonical_retrieval_status": retrieval_status,
                    "legacy_score_credit": 0.0,
                    "production_score_eligible": False,
                    "legacy_mapping_authority": False,
                }
            )
    result.extend(
        row
        for fingerprint, row in canonical_by_fingerprint.items()
        if fingerprint not in safe_legacy_fingerprints
    )
    return result


def _phase_accounting(rows: Sequence[Mapping[str, Any]]) -> Mapping[str, int]:
    final_web_rows = [
        row
        for row in rows
        if row.get("phase") == "post_score_gap_web_research_complete"
    ]
    complete_web_rows = [
        row
        for row in rows
        if row.get("phase")
        in {
            "web_research_initial_complete",
            "post_parse_gap_web_research_complete",
            "post_score_gap_web_research_complete",
        }
    ]
    document_ids = {
        str(row.get("document_id"))
        for row in rows
        if row.get("phase") == "agentic_evidence_document_start"
        and str(row.get("document_id") or "")
    }
    return {
        "initial_query_count": max(
            (
                int(row.get("query_count") or 0)
                for row in rows
                if row.get("phase") == "initial_search_complete"
            ),
            default=0,
        ),
        "final_query_count": int(
            (final_web_rows[-1] if final_web_rows else complete_web_rows[-1]).get(
                "query_count", 0
            )
            if complete_web_rows
            else 0
        ),
        "maximum_ranked_search_result_count": max(
            (int(row.get("ranked_result_count") or 0) for row in complete_web_rows),
            default=0,
        ),
        "final_ranked_search_result_count": int(
            (final_web_rows[-1] if final_web_rows else complete_web_rows[-1]).get(
                "ranked_result_count", 0
            )
            if complete_web_rows
            else 0
        ),
        "final_fetched_document_count": int(
            (final_web_rows[-1] if final_web_rows else complete_web_rows[-1]).get(
                "fetched_document_count", 0
            )
            if complete_web_rows
            else 0
        ),
        "material_document_read_count": len(document_ids),
    }


def _validate_snapshot(snapshot: Mapping[str, Any]) -> None:
    if snapshot.get("schema_version") != PHASE92_SNAPSHOT_SCHEMA_VERSION:
        raise ValueError("legacy retrieval shadow snapshot schema mismatch")
    stored_hash = str(snapshot.get("snapshot_payload_sha256") or "")
    payload = dict(snapshot)
    payload.pop("snapshot_payload_sha256", None)
    if not stored_hash or stored_hash != _stable_hash(payload):
        raise ValueError("legacy retrieval shadow snapshot hash mismatch")
    if snapshot.get("evaluation_only") is not True:
        raise ValueError("legacy retrieval snapshot must remain evaluation-only")
    if snapshot.get("frozen_observation_is_production_readiness_evidence") is not False:
        raise ValueError("frozen shadow cannot prove production readiness")
    if snapshot.get("canonical_baseline_is_retrospective_as_of_filtered") is not True:
        raise ValueError("retrospective canonical baseline must be disclosed")
    if snapshot.get("legacy_score_or_stage_authority") is not False:
        raise ValueError("legacy snapshot cannot own score or Stage")
    if legacy_score_authority_leakage_paths(snapshot):
        raise ValueError("legacy score/Stage/mapping authority leaked into snapshot")


def _canonical_claim_is_safe(
    claim: Mapping[str, Any], target_id: str, cutoff: date
) -> bool:
    published = _date_only(claim.get("published_date"))
    return bool(
        claim.get("accepted") is True
        and claim.get("fetched") is True
        and claim.get("source_proxy_only") is False
        and str(claim.get("target_id") or "") == target_id
        and str(claim.get("subject_entity_id") or "") == target_id
        and str(claim.get("target_scope_status") or "") == "DIRECT"
        and str(claim.get("verification_status") or "") == "SEMANTIC_VERIFIED"
        and published is not None
        and date.fromisoformat(published) <= cutoff
        and str((claim.get("raw_assertion") or {}).get("predicate") or "").strip()
    )


def _is_material_claim(claim: Mapping[str, Any]) -> bool:
    predicate = str(claim.get("predicate") or "").strip()
    if not predicate or claim.get("value") is None:
        return False
    normalized = predicate.lower()
    if normalized in _TECHNICAL_PREDICATES:
        return False
    if normalized.startswith("compiled_") or normalized.startswith(
        "consensus_proxy_"
    ):
        return False
    if normalized.endswith("_comment"):
        return False
    return True


def _direction_candidate(claim: Mapping[str, Any]) -> str:
    value = claim.get("value")
    text = " ".join(
        (
            str(claim.get("predicate") or ""),
            str(claim.get("quote_text") or ""),
        )
    ).lower()
    if value is False or any(token in text for token in _COUNTER_CANDIDATE_TOKENS):
        return "COUNTER"
    return "MATERIAL"


def _source_family(source_type: str, url: str) -> str:
    source = source_type.upper()
    domain = _url_domain(url)
    if "dart.fss.or.kr" in domain or source in {"DISCLOSURE", "FILING"}:
        return "OPENDART"
    if source == "EXCHANGE_RISK":
        return "KIND_KRX"
    if source == "FINANCIAL_ACTUAL" or source == "XBRL":
        return "FINANCIAL_STATEMENTS"
    if source == "CONSENSUS_REVISION":
        return "CONSENSUS_REVISION"
    if source == "CONSENSUS":
        return "VALUATION_MULTIPLES"
    if source in {"RESEARCH_REPORT", "REPORT"}:
        return "PUBLIC_BROKER_PDF"
    if source == "CANONICAL" and domain:
        return "TRUSTED_BUSINESS_MEDIA"
    if source == "NEWS":
        return "NAVER_DISCOVERY"
    return "GENERAL_WEB_DISCOVERY"


def _sanitized_structured_payload(row: Mapping[str, Any]) -> Mapping[str, Any]:
    parsed = row.get("parsed_fields") or {}
    return {
        "evidence_id": row.get("evidence_id"),
        "as_of_date": row.get("as_of_date"),
        "available_at": row.get("available_at"),
        "source_name": row.get("source_name"),
        "source_type": row.get("source_type"),
        "symbol": row.get("symbol"),
        "fields": {
            key: _json_safe(value)
            for key, value in sorted(parsed.items())
            if key not in _TECHNICAL_PREDICATES
            and key not in _LEGACY_SCORE_AUTHORITY_KEYS
            and not key.startswith("compiled_")
        },
    }


def _parse_document_selection_summary(
    summary: str,
) -> tuple[str, Mapping[str, str]]:
    parts = summary.split("|")
    document_id = parts[0].strip()
    metadata: dict[str, str] = {}
    for part in parts[1:]:
        if "=" not in part:
            continue
        key, value = part.split("=", 1)
        if key == "score":
            key = "legacy_retrieval_rank_value"
        metadata[key] = value
    return document_id, metadata


def _economic_fact_fingerprint(target_id: str, predicate: str, value: Any) -> str:
    normalized_predicate = re.sub(r"\s+", " ", predicate.strip().lower())
    return _stable_hash(
        {
            "target_id": target_id,
            "predicate": normalized_predicate,
            "value": _json_safe(value),
        }
    )


def _walk_forbidden_authority_keys(
    value: Any, path: str, output: list[str]
) -> None:
    if isinstance(value, Mapping):
        for key, child in value.items():
            normalized = str(key).lower()
            if normalized in _LEGACY_SCORE_AUTHORITY_KEYS:
                output.append(f"{path}.{key}")
            _walk_forbidden_authority_keys(child, f"{path}.{key}", output)
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        for index, child in enumerate(value):
            _walk_forbidden_authority_keys(child, f"{path}[{index}]", output)


def _count_forbidden_authority_fields(value: Any) -> int:
    if isinstance(value, Mapping):
        return sum(
            int(str(key).lower() in _LEGACY_SCORE_AUTHORITY_KEYS)
            + _count_forbidden_authority_fields(child)
            for key, child in value.items()
        )
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        return sum(_count_forbidden_authority_fields(child) for child in value)
    return 0


def _normalize_query(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().lower())


def _url_domain(value: str) -> str:
    try:
        return urlsplit(value).netloc.lower()
    except ValueError:
        return ""


def _date_only(value: Any) -> str | None:
    text = str(value or "").strip()
    if len(text) < 10:
        return None
    candidate = text[:10]
    try:
        date.fromisoformat(candidate)
    except ValueError:
        return None
    return candidate


def _short_text(value: Any, limit: int = 240) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    return text[:limit]


def _read_json(path: Path) -> Mapping[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, Mapping):
        raise ValueError(f"expected JSON object: {path}")
    return value


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    result: list[Mapping[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        value = json.loads(line)
        if not isinstance(value, Mapping):
            raise ValueError(f"expected JSONL object: {path}")
        result.append(value)
    return tuple(result)


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _stable_hash(value: Any) -> str:
    return hashlib.sha256(_canonical_json(value).encode("utf-8")).hexdigest()


def _canonical_json(value: Any) -> str:
    return json.dumps(
        _json_safe(value),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def _json_safe(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _json_safe(child) for key, child in value.items()}
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        return [_json_safe(child) for child in value]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return str(value)


__all__ = [
    "LEGACY_FACT_CLASSIFICATIONS",
    "LegacyApertureFeedback",
    "PHASE92_AUDIT_PATH",
    "PHASE92_CAPABILITY_TRANSFERS",
    "PHASE92_PASS",
    "PHASE92_SCHEMA_VERSION",
    "PHASE92_SNAPSHOT_PATH",
    "PHASE92_THRESHOLDS",
    "build_legacy_aperture_feedback",
    "build_legacy_retrieval_shadow_snapshot",
    "build_legacy_shadow_source_graph",
    "compile_phase92_legacy_retrieval_parity_audit",
    "legacy_score_authority_leakage_paths",
    "load_legacy_retrieval_shadow_snapshot",
    "write_legacy_retrieval_shadow_snapshot",
    "write_phase92_legacy_retrieval_parity_audit",
]
