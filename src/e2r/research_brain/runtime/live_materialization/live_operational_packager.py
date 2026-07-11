"""Package live materialization and pure evaluator leaves into Phase 32 outputs."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping
from urllib.parse import urlsplit

from e2r.production.metadata import stable_hash, write_json, write_jsonl, write_text
from e2r.research_brain.runtime.current_operation_runner import CurrentOperationRunnerResult

from .authorization import LiveRunMode
from .schemas import LiveOperationalRunEnvelope


def package_live_current_operation(
    *,
    result: CurrentOperationRunnerResult,
    live_root: str | Path,
    input_manifest: str | Path,
    output_root: str | Path,
    run_mode: str,
) -> Mapping[str, Path]:
    live = Path(live_root)
    root = Path(output_root)
    # These are extraction/acquisition leaves which the pure evaluator does not
    # carry.  They remain copied from the live materialization root.
    live_leaf_mappings = {
        "planner_runs": (live / "planner_runs.jsonl", root / "planner_runs.jsonl"),
        "source_task_executions": (live / "source_task_satisfaction.jsonl", root / "source_task_executions.jsonl"),
        "evidence_documents": (live / "evidence_documents.jsonl", root / "evidence_documents.jsonl"),
        "evidence_anchors": (live / "evidence_anchors.jsonl", root / "evidence_anchors.jsonl"),
        "raw_assertions": (live / "raw_assertions.jsonl", root / "raw_assertions.jsonl"),
        "adjudicated_claims": (live / "adjudicated_claims.jsonl", root / "adjudicated_claims.jsonl"),
    }
    paths: dict[str, Path] = {}
    for name, (source, destination) in live_leaf_mappings.items():
        write_jsonl(destination, _read_jsonl(source))
        paths[name] = destination

    # Canonical evaluator leaves must win over an older low-level live root.
    # A common repair flow recompiles an accepted claim after acquisition; in
    # that case copying accepted_current_claims.jsonl from the older root would
    # silently erase the claim that the evaluator actually used.
    canonical_rows = {
        "universe": tuple(item.to_dict() for item in result.universe),
        "baseline_lanes": tuple(item.to_dict() for item in result.baseline_lanes),
        "trigger_signals": tuple(item.to_dict() for item in result.triggers),
        "source_tasks": tuple(item.to_dict() for item in result.source_tasks),
        "accepted_claims": tuple(item.to_dict() for item in result.claims),
        "claim_provenance": tuple(
            item.to_dict() for item in result.claim_provenance
        ),
        "primitive_states": _primitive_state_rows(result),
        "atomic_decisions": tuple(
            item.to_dict() for item in result.atomic_decisions
        ),
    }
    for name, rows in canonical_rows.items():
        destination = root / {
            "universe": "universe.jsonl",
            "baseline_lanes": "baseline_lanes.jsonl",
            "trigger_signals": "trigger_signals.jsonl",
            "source_tasks": "source_tasks.jsonl",
            "accepted_claims": "accepted_claims.jsonl",
            "claim_provenance": "claim_provenance.jsonl",
            "primitive_states": "primitive_states.jsonl",
            "atomic_decisions": "atomic_decisions.jsonl",
        }[name]
        write_jsonl(destination, rows)
        paths[name] = destination

    contribution_rows = tuple(
        {
            "target_id": decision.target_id,
            "decision_id": decision.decision_id,
            **contribution.to_dict(),
        }
        for decision in result.atomic_decisions
        for contribution in decision.contributions
    )
    contributions = root / "score_contributions.jsonl"
    write_jsonl(contributions, contribution_rows)
    paths["score_contributions"] = contributions

    claim_chain = _canonical_claim_chain(
        result=result,
        live_root=live,
        base_rows={
            name: _read_jsonl(path)
            for name, path in (
                ("evidence_documents", paths["evidence_documents"]),
                ("evidence_anchors", paths["evidence_anchors"]),
                ("raw_assertions", paths["raw_assertions"]),
                ("adjudicated_claims", paths["adjudicated_claims"]),
                ("source_task_executions", paths["source_task_executions"]),
            )
        },
    )
    for name in (
        "evidence_documents",
        "evidence_anchors",
        "raw_assertions",
        "adjudicated_claims",
        "source_task_executions",
    ):
        write_jsonl(paths[name], claim_chain["rows"][name])

    deep = root / "deep_executions.jsonl"
    write_jsonl(deep, (item.to_dict() for item in result.deep_executions))
    paths["deep_executions"] = deep
    manifest = root / "current_operation_input_manifest.json"
    write_json(manifest, json.loads(Path(input_manifest).read_text(encoding="utf-8")))
    paths["current_operation_input_manifest"] = manifest
    statuses = root / "current_stage_status.jsonl"
    write_jsonl(statuses, (item.to_dict() for item in result.stage_statuses))
    paths["current_stage_status"] = statuses
    watchlist = root / "current_watchlist.json"
    write_json(
        watchlist,
        {
            "schema_version": "e2r_live_current_watchlist_v1",
            "as_of_date": result.as_of_date,
            "rows": [item.to_dict() for item in result.watchlist],
        },
    )
    paths["current_watchlist"] = watchlist

    provider_rows = _read_jsonl(live / "provider_fetch_results.jsonl")
    documents = tuple(claim_chain["rows"]["evidence_documents"])
    accepted_rows = canonical_rows["accepted_claims"]
    provenance_rows = canonical_rows["claim_provenance"]
    live_provenance_rows = tuple(
        row for row in provenance_rows if _is_actual_live_provenance(row)
    )
    provider_failures = tuple(
        dict.fromkeys(
            str(item.get("provider_name") or "") + ":" + str(item.get("provider_error") or "")
            for item in provider_rows
            if item.get("acquisition_class") in {"PROVIDER_FAILED", "AUTH_FAILED", "RATE_LIMITED"}
            and item.get("cache_hit") is False
        )
    )
    actual_source_ids = {
        str(item.get("document_id") or item.get("content_hash") or "")
        for item in provider_rows
        if item.get("acquisition_class") == "REAL_PROVIDER_FETCH"
        and str(item.get("document_id") or item.get("content_hash") or "")
    }
    actual_source_ids.update(
        str(item.get("document_id") or item.get("content_sha256") or "")
        for item in live_provenance_rows
    )
    fresh_cache_ids = {
        str(item.get("document_id") or item.get("content_hash") or "")
        for item in provider_rows
        if item.get("acquisition_class") == "FRESH_PROVIDER_CACHE"
        and str(item.get("document_id") or item.get("content_hash") or "")
    }

    claim_ids = {str(item.get("claim_id") or "") for item in accepted_rows}
    provenance_claim_ids = {
        str(item.get("claim_id") or "") for item in provenance_rows
    }
    live_provenance_claim_ids = {
        str(item.get("claim_id") or "") for item in live_provenance_rows
    }
    supported_claim_ids = {
        str(claim_id)
        for item in contribution_rows
        for claim_id in item.get("support_claim_ids") or ()
    }
    operational_critical = {
        **dict(result.audit["critical_counts"]),
        **dict(claim_chain["critical_counts"]),
        "accepted_claim_without_provenance_count": len(
            claim_ids - provenance_claim_ids
        ),
        "accepted_claim_without_actual_live_provenance_count": len(
            claim_ids - live_provenance_claim_ids
        ),
        "orphan_claim_provenance_count": len(provenance_claim_ids - claim_ids),
        "score_contribution_without_result_claim_count": len(
            supported_claim_ids - claim_ids
        ),
    }
    readiness_blockers: list[str] = []
    if not accepted_rows:
        readiness_blockers.append("NO_ACCEPTED_CURRENT_CLAIM")
    if accepted_rows and claim_ids - live_provenance_claim_ids:
        readiness_blockers.append("ACCEPTED_CLAIM_PROVENANCE_INCOMPLETE")
    if not actual_source_ids:
        readiness_blockers.append("NO_ACTUAL_LIVE_SOURCE")
    if not result.atomic_decisions:
        readiness_blockers.append("NO_ATOMIC_DECISION")
    if accepted_rows and not contribution_rows:
        readiness_blockers.append("NO_SCORE_CONTRIBUTION")
    if sum(int(value) for value in operational_critical.values()):
        readiness_blockers.append("OPERATIONAL_CRITICAL_PRESENT")
    if result.config.test_mode or run_mode == LiveRunMode.TEST_FIXTURE.value:
        readiness_blockers.append("TEST_MODE_NOT_PRODUCTION_READY")
    # Provider failures remain visible diagnostics.  They become final blockers
    # only when no real source/provenance path resolved the run.
    if provider_failures and not actual_source_ids:
        readiness_blockers.extend(provider_failures)
    provider_blockers = tuple(dict.fromkeys(readiness_blockers))
    production_runtime_ready = not provider_blockers
    envelope = LiveOperationalRunEnvelope(
        materialization_run_id="LIVEMAT-" + stable_hash(
            {
                "as_of_date": result.as_of_date,
                "source_ids": sorted(actual_source_ids),
                "claim_ids": sorted(claim_ids),
            }
        )[:24],
        evaluator_run_id=result.run_id,
        as_of_date=result.as_of_date,
        run_mode=run_mode,
        source_corpus_hash=stable_hash(
            {
                "evidence_documents": documents,
                "claim_provenance": provenance_rows,
            }
        ),
        input_manifest_hash=_sha256_file(Path(input_manifest)),
        evaluator_leaf_hash=str(result.manifest["leaf_hash"]),
        actual_live_source_count=len(actual_source_ids),
        fresh_provider_cache_count=len(fresh_cache_ids),
        accepted_current_claim_count=len(accepted_rows),
        current_atomic_decision_count=len(result.atomic_decisions),
        provider_blockers=provider_blockers,
        critical_counts=operational_critical,
        production_runtime_ready=production_runtime_ready,
    )
    envelope_path = root / "live_operational_envelope.json"
    write_json(envelope_path, envelope.to_dict())
    paths["live_operational_envelope"] = envelope_path
    audit_summary = root / "audit_summary.json"
    if production_runtime_ready:
        status = "LIVE_OPERATIONAL_BRAIN_READY"
    elif not accepted_rows:
        status = "LIVE_OPERATION_EXECUTED_PENDING_ACCEPTED_CURRENT_CLAIM"
    elif sum(int(value) for value in operational_critical.values()):
        status = "LIVE_OPERATION_EXECUTED_PENDING_INTEGRITY_REPAIR"
    else:
        status = "LIVE_OPERATION_EXECUTED_PENDING_SOURCE_OR_PROVENANCE"
    write_json(
        audit_summary,
        {
            "schema_version": "e2r_live_operational_audit_summary_v1",
            "status": status,
            "as_of_date": result.as_of_date,
            "full_universe_count": len(result.universe),
            "watchlist_count": len(result.watchlist),
            "deep_execution_count": len(result.deep_executions),
            "actual_live_source_count": envelope.actual_live_source_count,
            "fresh_provider_cache_count": envelope.fresh_provider_cache_count,
            "accepted_current_claim_count": len(accepted_rows),
            "claim_provenance_count": len(provenance_rows),
            "actual_live_claim_provenance_count": len(live_provenance_rows),
            "atomic_decision_count": len(result.atomic_decisions),
            "score_contribution_count": len(contribution_rows),
            "provider_failure_count": len(provider_failures),
            "provider_failure_diagnostics": list(provider_failures),
            "promotion_manifest_applied": claim_chain[
                "promotion_manifest_applied"
            ],
            "promotion_manifest_hash": claim_chain["promotion_manifest_hash"],
            "canonical_claim_chain_counts": dict(claim_chain["counts"]),
            "operational_blockers": list(provider_blockers),
            "evaluator_critical_count_sum": result.audit["critical_count_sum"],
            "operational_critical_count_sum": sum(
                int(value) for value in operational_critical.values()
            ),
            "production_runtime_ready": production_runtime_ready,
        },
    )
    paths["audit_summary"] = audit_summary
    digest = root / "operator_digest.md"
    write_text(
        digest,
        "\n".join(
            (
                "# E2R Live Current Operator Digest",
                "",
                f"- as_of_date: {result.as_of_date}",
                f"- full universe: {len(result.universe)}",
                f"- current watchlist: {len(result.watchlist)}",
                f"- deep executions: {len(result.deep_executions)}",
                f"- actual live documents: {envelope.actual_live_source_count}",
                f"- accepted current claims: {len(accepted_rows)}",
                f"- claim provenance: {len(provenance_rows)}",
                f"- atomic decisions: {len(result.atomic_decisions)}",
                f"- score contributions: {len(contribution_rows)}",
                f"- provider failure diagnostics: {len(provider_failures)}",
                f"- critical count: {sum(int(value) for value in operational_critical.values())}",
                f"- status: {'Operational Runtime Ready' if production_runtime_ready else 'Provider/Source Pending'}",
                "- direct investment recommendation: none",
                "",
            )
        ),
    )
    paths["operator_digest"] = digest
    return paths


def _canonical_claim_chain(
    *,
    result: CurrentOperationRunnerResult,
    live_root: Path,
    base_rows: Mapping[str, tuple[Mapping[str, Any], ...]],
) -> Mapping[str, Any]:
    accepted_claim_ids = {
        str(claim_id)
        for decision in result.atomic_decisions
        for claim_id in decision.accepted_claim_ids
    }
    claims_by_id = {item.claim_id: item for item in result.claims}
    provenance_by_claim = {
        item.claim_id: item for item in result.claim_provenance
    }
    task_ids = {
        value
        for item in result.source_tasks
        for value in (item.task_id, item.question_task_id)
        if value
    }
    tasks_by_target: dict[str, list[Any]] = {}
    for item in result.source_tasks:
        tasks_by_target.setdefault(item.target_id, []).append(item)
    for values in tasks_by_target.values():
        values.sort(key=lambda item: (item.question_task_id, item.task_id))

    projected: dict[str, list[Mapping[str, Any]]] = {
        "evidence_documents": [],
        "evidence_anchors": [],
        "raw_assertions": [],
        "adjudicated_claims": [],
        "source_task_executions": [],
    }
    for claim_id in sorted(accepted_claim_ids):
        claim = claims_by_id.get(claim_id)
        provenance = provenance_by_claim.get(claim_id)
        if claim is None or provenance is None:
            continue
        document_text = provenance.document_text
        quote = provenance.exact_quote
        quote_start = document_text.find(quote)
        projected["evidence_documents"].append(
            {
                "schema_version": "e2r_live_source_acquisition_v1",
                "acquisition_class": "REAL_PROVIDER_FETCH",
                "document_id": provenance.document_id,
                "target_id": provenance.target_id,
                "canonical_url": provenance.source_url,
                "published_at": provenance.published_date,
                "available_at": provenance.available_date,
                "content_hash": provenance.content_sha256,
                "content_text": document_text,
                "current_score_eligible": True,
                "snippet_only": False,
                "source_lineage_ids": list(provenance.source_ids),
                "projection_kind": "RESULT_PROVENANCE_CANONICAL",
            }
        )
        raw_id = "RESULT-RAW-" + stable_hash(
            {"claim_id": claim_id, "document_id": provenance.document_id}
        )[:20]
        for anchor_id in provenance.anchor_ids:
            projected["evidence_anchors"].append(
                {
                    "anchor_id": anchor_id,
                    "anchor_type": "TEXT_SPAN",
                    "anchor_verified": True,
                    "content_hash": provenance.content_sha256,
                    "document_id": provenance.document_id,
                    "exact_text": quote,
                    "locator": (
                        f"char:{quote_start}:{quote_start + len(quote)}"
                        if quote_start >= 0
                        else "exact_quote"
                    ),
                    "source_task_ids": [],
                    "target_id": provenance.target_id,
                    "projection_kind": "RESULT_PROVENANCE_CANONICAL",
                }
            )
        primary_anchor = provenance.anchor_ids[0]
        projected["raw_assertions"].append(
            {
                "raw_assertion_id": raw_id,
                "document_id": provenance.document_id,
                "anchor_id": primary_anchor,
                "target_id": claim.target_id,
                "subject_text": claim.target_id,
                "predicate": claim.primitive_id,
                "object_text": quote,
                "exact_quote": quote,
                "extraction_provider_kind": provenance.extraction_provider_kind,
                "extractor_contract_blind": True,
                "projection_kind": "RESULT_PROVENANCE_CANONICAL",
            }
        )
        projected["adjudicated_claims"].append(
            {
                "claim_id": claim_id,
                "target_id": claim.target_id,
                "target_entity_id": claim.target_id,
                "subject_entity_id": claim.target_id,
                "document_id": provenance.document_id,
                "source_document_id": provenance.document_id,
                "source_anchor_id": primary_anchor,
                "raw_assertion_id": raw_id,
                "directness": "DIRECT",
                "target_scope_status": "DIRECT",
                "temporal_status": "CURRENT",
                "semantic_status": "PASS",
                "verification_status": "SEMANTIC_VERIFIED",
                "adjudication_provider_kind": provenance.mapping_provider_kind,
                "projection_kind": "RESULT_PROVENANCE_CANONICAL",
            }
        )
        target_tasks = tasks_by_target.get(claim.target_id, [])
        if target_tasks:
            task = target_tasks[0]
            projected["source_task_executions"].append(
                {
                    "schema_version": "e2r_live_current_claim_v1",
                    "source_task_id": task.question_task_id,
                    "daily_source_task_id": task.task_id,
                    "target_id": claim.target_id,
                    "primitive_id": claim.primitive_id,
                    "status": "DIRECT_TASK_SATISFIED",
                    "original_gap_open": False,
                    "accepted_claim_ids": [claim_id],
                    "accepted_mapping_ids": list(claim.mapping_ids),
                    "document_ids": [provenance.document_id],
                    "raw_assertion_ids": [raw_id],
                    "projection_kind": "RESULT_PROVENANCE_CANONICAL",
                }
            )

    promotion = _load_promotion_claim_rows(
        live_root=live_root,
        as_of_date=result.as_of_date,
        accepted_claim_ids=accepted_claim_ids,
        document_ids={
            item.document_id
            for claim_id, item in provenance_by_claim.items()
            if claim_id in accepted_claim_ids
        },
        anchor_ids={
            anchor_id
            for claim_id, item in provenance_by_claim.items()
            if claim_id in accepted_claim_ids
            for anchor_id in item.anchor_ids
        },
        source_task_ids=task_ids,
    )
    keys = {
        "evidence_documents": lambda row: str(
            row.get("document_id") or row.get("content_hash") or ""
        ),
        "evidence_anchors": lambda row: str(row.get("anchor_id") or ""),
        "raw_assertions": lambda row: str(row.get("raw_assertion_id") or ""),
        "adjudicated_claims": lambda row: str(row.get("claim_id") or ""),
        "source_task_executions": lambda row: stable_hash(
            {
                "source_task_id": row.get("source_task_id"),
                "primitive_id": row.get("primitive_id"),
                "accepted_claim_ids": row.get("accepted_claim_ids") or (),
                "status": row.get("status"),
            }
        ),
    }
    rows = {
        name: _merge_rows(
            base_rows.get(name, ()),
            projected[name],
            promotion["rows"][name],
            key=keys[name],
        )
        for name in keys
    }
    critical = _audit_canonical_claim_chain(
        accepted_claim_ids=accepted_claim_ids,
        provenance_by_claim=provenance_by_claim,
        result_source_task_ids=task_ids,
        rows=rows,
    )
    critical["promotion_manifest_invalid_count"] = int(
        promotion["manifest_present"] and not promotion["manifest_valid"]
    )
    return {
        "rows": rows,
        "critical_counts": critical,
        "promotion_manifest_applied": promotion["manifest_valid"],
        "promotion_manifest_hash": promotion["manifest_hash"],
        "counts": {name: len(values) for name, values in rows.items()},
    }


def _load_promotion_claim_rows(
    *,
    live_root: Path,
    as_of_date: str,
    accepted_claim_ids: set[str],
    document_ids: set[str],
    anchor_ids: set[str],
    source_task_ids: set[str],
) -> Mapping[str, Any]:
    empty_rows: dict[str, tuple[Mapping[str, Any], ...]] = {
        "evidence_documents": (),
        "evidence_anchors": (),
        "raw_assertions": (),
        "adjudicated_claims": (),
        "source_task_executions": (),
    }
    manifest_path = live_root / "live_acceptance_promotion.json"
    if not manifest_path.is_file():
        return {
            "rows": empty_rows,
            "manifest_present": False,
            "manifest_valid": False,
            "manifest_hash": None,
        }
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        source_roots = tuple(manifest.get("source_roots") or ())
        manifest_valid = bool(
            manifest.get("schema_version") == "e2r_live_acceptance_promotion_v1"
            and manifest.get("status") == "FULL_LIVE_ACCEPTANCE_PROMOTED"
            and manifest.get("as_of_date") == as_of_date
            and set(manifest.get("accepted_claim_ids") or ())
            == accepted_claim_ids
            and source_roots
        )
        resolved_roots: list[Path] = []
        for row in source_roots:
            path = Path(str(row.get("path") or ""))
            if not path.is_absolute():
                path = Path.cwd() / path
            if not path.exists() or _tree_hash(path) != row.get("tree_hash"):
                manifest_valid = False
            resolved_roots.append(path)
        if not manifest_valid:
            raise ValueError("promotion manifest/source hash mismatch")

        loaded: dict[str, list[Mapping[str, Any]]] = {
            name: [] for name in empty_rows
        }
        file_names = {
            "evidence_documents": ("evidence_documents.jsonl", "evidence_document.json"),
            "evidence_anchors": ("evidence_anchors.jsonl",),
            "raw_assertions": ("raw_assertions.jsonl",),
            "adjudicated_claims": ("adjudicated_claims.jsonl",),
            "source_task_executions": ("source_task_satisfaction.jsonl",),
        }
        for root in resolved_roots:
            wanted_names = sorted(
                {value for values in file_names.values() for value in values}
            )
            candidates = (
                (root,)
                if root.is_file()
                else tuple(
                    sorted(
                        {
                            item
                            for name in wanted_names
                            for item in root.rglob(name)
                        },
                        key=str,
                    )
                )
            )
            for path in candidates:
                for output_name, names in file_names.items():
                    if path.name not in names:
                        continue
                    loaded[output_name].extend(_read_json_rows(path))
        filtered = {
            "evidence_documents": tuple(
                row
                for row in loaded["evidence_documents"]
                if str(row.get("document_id") or "") in document_ids
            ),
            "evidence_anchors": tuple(
                row
                for row in loaded["evidence_anchors"]
                if str(row.get("anchor_id") or "") in anchor_ids
                or str(row.get("document_id") or "") in document_ids
            ),
            "raw_assertions": tuple(
                row
                for row in loaded["raw_assertions"]
                if str(row.get("anchor_id") or "") in anchor_ids
                or str(row.get("document_id") or "") in document_ids
            ),
            "adjudicated_claims": tuple(
                row
                for row in loaded["adjudicated_claims"]
                if str(row.get("claim_id") or "") in accepted_claim_ids
            ),
            "source_task_executions": tuple(
                row
                for row in loaded["source_task_executions"]
                if accepted_claim_ids
                & {str(value) for value in row.get("accepted_claim_ids") or ()}
                or str(row.get("source_task_id") or "") in source_task_ids
            ),
        }
        return {
            "rows": filtered,
            "manifest_present": True,
            "manifest_valid": True,
            "manifest_hash": _sha256_file(manifest_path),
        }
    except (OSError, TypeError, ValueError, json.JSONDecodeError):
        return {
            "rows": empty_rows,
            "manifest_present": True,
            "manifest_valid": False,
            "manifest_hash": _sha256_file(manifest_path),
        }


def _audit_canonical_claim_chain(
    *,
    accepted_claim_ids: set[str],
    provenance_by_claim: Mapping[str, Any],
    result_source_task_ids: set[str],
    rows: Mapping[str, tuple[Mapping[str, Any], ...]],
) -> dict[str, int]:
    documents = {
        str(row.get("document_id") or ""): row
        for row in rows["evidence_documents"]
    }
    anchors = {
        str(row.get("anchor_id") or ""): row
        for row in rows["evidence_anchors"]
    }
    raw_assertions = {
        str(row.get("raw_assertion_id") or ""): row
        for row in rows["raw_assertions"]
    }
    adjudicated = {
        str(row.get("claim_id") or ""): row
        for row in rows["adjudicated_claims"]
    }
    satisfaction = tuple(rows["source_task_executions"])
    missing_document = 0
    hash_or_text_mismatch = 0
    missing_anchor = 0
    missing_raw_or_adjudicated = 0
    missing_source_task_lineage = 0
    for claim_id in accepted_claim_ids:
        provenance = provenance_by_claim.get(claim_id)
        if provenance is None:
            continue
        document = documents.get(provenance.document_id)
        missing_document += int(document is None)
        if document is not None:
            text = str(
                document.get("content_text")
                or document.get("document_text")
                or ""
            )
            digest = str(
                document.get("content_hash")
                or document.get("content_sha256")
                or ""
            )
            hash_or_text_mismatch += int(
                digest != provenance.content_sha256
                or hashlib.sha256(text.encode("utf-8")).hexdigest()
                != provenance.content_sha256
                or provenance.exact_quote not in text
            )
        missing_anchor += sum(
            anchor_id not in anchors
            or str(anchors[anchor_id].get("document_id") or "")
            != provenance.document_id
            or str(
                anchors[anchor_id].get("content_hash")
                or anchors[anchor_id].get("content_sha256")
                or ""
            )
            != provenance.content_sha256
            for anchor_id in provenance.anchor_ids
        )
        adjudication = adjudicated.get(claim_id)
        raw_id = str((adjudication or {}).get("raw_assertion_id") or "")
        missing_raw_or_adjudicated += int(
            adjudication is None
            or str(adjudication.get("source_document_id") or "")
            != provenance.document_id
            or str(adjudication.get("source_anchor_id") or "")
            not in provenance.anchor_ids
            or not raw_id
            or raw_id not in raw_assertions
        )
        matching_satisfaction = tuple(
            row
            for row in satisfaction
            if claim_id
            in {str(value) for value in row.get("accepted_claim_ids") or ()}
        )
        missing_source_task_lineage += int(
            not matching_satisfaction
            or not any(
                str(row.get("source_task_id") or "")
                in result_source_task_ids
                or str(row.get("daily_source_task_id") or "")
                in result_source_task_ids
                for row in matching_satisfaction
            )
        )
    return {
        "accepted_claim_document_join_failure_count": missing_document,
        "accepted_claim_document_hash_or_quote_failure_count": hash_or_text_mismatch,
        "accepted_claim_anchor_join_failure_count": missing_anchor,
        "accepted_claim_raw_adjudication_join_failure_count": missing_raw_or_adjudicated,
        "accepted_claim_source_task_lineage_failure_count": missing_source_task_lineage,
    }


def _merge_rows(
    *groups: Any,
    key: Any,
) -> tuple[Mapping[str, Any], ...]:
    merged: dict[str, Mapping[str, Any]] = {}
    anonymous: list[Mapping[str, Any]] = []
    for group in groups:
        for row in group:
            identity = str(key(row) or "")
            if identity:
                merged[identity] = row
            else:
                anonymous.append(row)
    return tuple(
        [merged[value] for value in sorted(merged)]
        + sorted(anonymous, key=stable_hash)
    )


def _read_json_rows(path: Path) -> tuple[Mapping[str, Any], ...]:
    if path.suffix == ".jsonl":
        return _read_jsonl(path)
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, Mapping):
        raise ValueError(f"JSON object required: {path}")
    return (value,)


def _tree_hash(path: Path) -> str:
    if path.is_file():
        return _sha256_file(path)
    return stable_hash(
        [
            {
                "path": str(item.relative_to(path)),
                "sha256": _sha256_file(item),
            }
            for item in sorted(path.rglob("*"))
            if item.is_file()
        ]
    )


def _primitive_state_rows(
    result: CurrentOperationRunnerResult,
) -> tuple[Mapping[str, Any], ...]:
    state_by_status = {
        "SATISFIED": "PRESENT_CURRENT",
        "MISSING": "UNKNOWN",
        "CONTRADICTED": "CONTRADICTED",
        "NOT_APPLICABLE": "ABSENT_CURRENT",
    }
    return tuple(
        {
            "target_id": decision.target_id,
            "primitive_id": assessment.primitive_id,
            "state": state_by_status[assessment.status],
            "support_claim_ids": list(assessment.support_claim_ids),
            "counter_claim_ids": list(assessment.counter_claim_ids),
            "material_gap_open": assessment.primitive_id
            in decision.material_gap_ids,
            "reason": (
                "canonical evaluator decision contains direct current support"
                if assessment.status == "SATISFIED"
                else "canonical evaluator decision keeps the primitive unresolved"
            ),
            "decision_id": decision.decision_id,
        }
        for decision in result.atomic_decisions
        for assessment in decision.primitive_assessments
    )


def _is_actual_live_provenance(row: Mapping[str, Any]) -> bool:
    parsed = urlsplit(str(row.get("source_url") or ""))
    return bool(
        row.get("fetched") is True
        and row.get("anchor_verified") is True
        and row.get("source_proxy_only") is False
        and row.get("test_only") is False
        and parsed.scheme == "https"
        and parsed.netloc
        and str(row.get("document_id") or "")
        and str(row.get("content_sha256") or "")
    )


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    with path.open(encoding="utf-8") as handle:
        return tuple(json.loads(line) for line in handle if line.strip())


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


__all__ = ["package_live_current_operation"]
