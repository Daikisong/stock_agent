"""Package live materialization and pure evaluator leaves into Phase 32 outputs."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping

from e2r.production.metadata import stable_hash, write_json, write_jsonl, write_text
from e2r.research_brain.runtime.current_operation_runner import CurrentOperationRunnerResult

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
    mappings = {
        "universe": (live / "universe_eligible.jsonl", root / "universe.jsonl"),
        "baseline_lanes": (live / "baseline_lanes.jsonl", root / "baseline_lanes.jsonl"),
        "trigger_signals": (live / "trigger_signals.jsonl", root / "trigger_signals.jsonl"),
        "planner_runs": (live / "planner_runs.jsonl", root / "planner_runs.jsonl"),
        "source_tasks": (live / "source_tasks.jsonl", root / "source_tasks.jsonl"),
        "source_task_executions": (live / "source_task_satisfaction.jsonl", root / "source_task_executions.jsonl"),
        "evidence_documents": (live / "evidence_documents.jsonl", root / "evidence_documents.jsonl"),
        "evidence_anchors": (live / "evidence_anchors.jsonl", root / "evidence_anchors.jsonl"),
        "raw_assertions": (live / "raw_assertions.jsonl", root / "raw_assertions.jsonl"),
        "adjudicated_claims": (live / "adjudicated_claims.jsonl", root / "adjudicated_claims.jsonl"),
        "accepted_claims": (live / "accepted_current_claims.jsonl", root / "accepted_claims.jsonl"),
        "claim_provenance": (live / "daily_claim_provenance.jsonl", root / "claim_provenance.jsonl"),
        "primitive_states": (live / "primitive_states.jsonl", root / "primitive_states.jsonl"),
        "atomic_decisions": (live / "atomic_stage_decisions.jsonl", root / "atomic_decisions.jsonl"),
    }
    paths: dict[str, Path] = {}
    for name, (source, destination) in mappings.items():
        write_jsonl(destination, _read_jsonl(source))
        paths[name] = destination
    contributions = root / "score_contributions.jsonl"
    write_jsonl(contributions, ())
    paths["score_contributions"] = contributions
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
    documents = _read_jsonl(live / "evidence_documents.jsonl")
    accepted = _read_jsonl(live / "accepted_current_claims.jsonl")
    provider_blockers = tuple(
        dict.fromkeys(
            str(item.get("provider_name") or "") + ":" + str(item.get("provider_error") or "")
            for item in provider_rows
            if item.get("acquisition_class") in {"PROVIDER_FAILED", "AUTH_FAILED", "RATE_LIMITED"}
            and item.get("cache_hit") is False
        )
    )
    if not accepted:
        provider_blockers = (*provider_blockers, "NO_ACCEPTED_CURRENT_CLAIM")
    envelope = LiveOperationalRunEnvelope(
        materialization_run_id="LIVEMAT-" + stable_hash(
            {"as_of_date": result.as_of_date, "document_count": len(documents)}
        )[:24],
        evaluator_run_id=result.run_id,
        as_of_date=result.as_of_date,
        run_mode=run_mode,
        source_corpus_hash=stable_hash(documents),
        input_manifest_hash=_sha256_file(Path(input_manifest)),
        evaluator_leaf_hash=str(result.manifest["leaf_hash"]),
        actual_live_source_count=sum(
            item.get("acquisition_class") == "REAL_PROVIDER_FETCH" for item in provider_rows
        ),
        fresh_provider_cache_count=sum(
            item.get("acquisition_class") == "FRESH_PROVIDER_CACHE" for item in provider_rows
        ),
        accepted_current_claim_count=len(accepted),
        current_atomic_decision_count=len(result.atomic_decisions),
        provider_blockers=provider_blockers,
        critical_counts=dict(result.audit["critical_counts"]),
        production_runtime_ready=False,
    )
    envelope_path = root / "live_operational_envelope.json"
    write_json(envelope_path, envelope.to_dict())
    paths["live_operational_envelope"] = envelope_path
    audit_summary = root / "audit_summary.json"
    write_json(
        audit_summary,
        {
            "schema_version": "e2r_live_operational_audit_summary_v1",
            "status": "LIVE_OPERATION_EXECUTED_PENDING_ACCEPTED_CURRENT_CLAIM",
            "as_of_date": result.as_of_date,
            "full_universe_count": len(result.universe),
            "watchlist_count": len(result.watchlist),
            "deep_execution_count": len(result.deep_executions),
            "actual_live_source_count": envelope.actual_live_source_count,
            "accepted_current_claim_count": 0,
            "atomic_decision_count": len(result.atomic_decisions),
            "evaluator_critical_count_sum": result.audit["critical_count_sum"],
            "production_runtime_ready": False,
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
                "- accepted current claims: 0",
                "- status: Provider/Source Pending",
                "- direct investment recommendation: none",
                "",
            )
        ),
    )
    paths["operator_digest"] = digest
    return paths


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
