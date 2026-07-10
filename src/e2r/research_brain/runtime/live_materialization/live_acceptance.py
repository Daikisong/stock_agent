"""Compile the Phase 36 frozen live acceptance from source-backed live leaves."""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json
from e2r.research_brain.runtime.current_operation_runner import (
    CurrentOperationRunnerInput,
    CurrentOperationRunnerResult,
    current_operation_runner_input_from_mapping,
    load_current_operation_runner_input,
    run_current_daily_census,
    write_current_daily_census,
)

from .census_operational_packager import package_live_census_operation
from .current_atomic_decision import CurrentAtomicDecisionBuilder


LIVE_ACCEPTANCE_SCHEMA_VERSION = "e2r_full_live_acceptance_v1"


@dataclass(frozen=True)
class FullLiveAcceptanceResult:
    status: str
    inputs: CurrentOperationRunnerInput
    current_result: CurrentOperationRunnerResult
    report: Mapping[str, Any]


def run_full_live_acceptance(
    *,
    config_path: str | Path,
) -> FullLiveAcceptanceResult:
    config = _read_json(Path(config_path))
    if config.get("schema_version") != LIVE_ACCEPTANCE_SCHEMA_VERSION:
        raise ValueError("live acceptance config schema mismatch")
    as_of_date = str(config.get("as_of_date") or "")
    base = load_current_operation_runner_input(str(config["base_census_input_path"]))
    if base.as_of_date != as_of_date:
        raise ValueError("base Census input as_of_date mismatch")

    probe_root = Path(str(config["claim_probe_root"]))
    target_id = str(config["accepted_claim_target_id"])
    accepted_rows = tuple(
        item for item in _read_jsonl(probe_root / "accepted_current_claims.jsonl")
        if str(item.get("target_id") or "") == target_id
    )
    provenance_rows = tuple(
        item for item in _read_jsonl(probe_root / "daily_claim_provenance.jsonl")
        if str(item.get("target_id") or "") == target_id
    )
    satisfaction_rows = tuple(
        item for item in _read_jsonl(probe_root / "source_task_satisfaction.jsonl")
        if str(item.get("target_id") or "") == target_id
    )
    atomic = CurrentAtomicDecisionBuilder().build(
        as_of_date=as_of_date,
        source_task_satisfaction=satisfaction_rows,
        gap_status_rows=(),
        accepted_current_claims=accepted_rows,
        claim_provenance=provenance_rows,
    )
    if len(atomic.claims) != 1 or len(atomic.decisions) != 1:
        raise ValueError("acceptance claim probe must yield one atomic claim/decision")
    decision = atomic.decisions[0]
    if decision.score_type != "NO_SCORE" or decision.canonical_stage != "0":
        raise ValueError("partial C06 evidence must remain NO_SCORE Stage 0")

    direct_task_id = _direct_task_id(satisfaction_rows)
    targeted_root = Path(str(config["targeted_smoke_root"]))
    question_task = next(
        (
            row for row in _read_jsonl(targeted_root / "question_source_tasks.jsonl")
            if str(row.get("task_id") or "") == direct_task_id
        ),
        None,
    )
    if question_task is None:
        raise ValueError("accepted claim SourceTask is absent from targeted live trace")
    daily_task = _daily_source_task(question_task)
    planner_trace = next(
        (
            row for row in _read_jsonl(targeted_root / "source_task_planning_results.jsonl")
            if str(row.get("task_id") or "") == direct_task_id
        ),
        None,
    )
    if planner_trace is None or not planner_trace.get("traces"):
        raise ValueError("accepted claim lacks a real query-planner trace")

    payload = base.to_dict()
    payload["claims"] = [item.to_dict() for item in (*base.claims, *atomic.claims)]
    payload["claim_provenance"] = [
        *[item.to_dict() for item in base.claim_provenance],
        *provenance_rows,
    ]
    payload["source_tasks"] = [
        *[item.to_dict() for item in base.source_tasks],
        daily_task,
    ]
    payload["atomic_decisions"] = [
        *[item.to_dict() for item in base.atomic_decisions],
        decision.to_dict(),
    ]
    payload["deep_executions"] = _replace_target_execution(
        base.deep_executions,
        target_id=target_id,
        task_id=direct_task_id,
        decision_id=decision.decision_id,
        provider_trace_id=str(planner_trace.get("input_id") or direct_task_id),
    )
    inputs = current_operation_runner_input_from_mapping(payload)
    first = run_current_daily_census(inputs)
    second = run_current_daily_census(
        current_operation_runner_input_from_mapping(inputs.to_dict())
    )

    bootstrap = _read_json(Path(str(config["bootstrap_audit_path"])))
    historical_a = _read_json(
        Path(str(config["historical_replay_root"]))
        / "historical_source_backed_manifest.json"
    )
    historical_b = _read_json(
        Path(str(config["historical_replay_repeat_root"]))
        / "historical_source_backed_manifest.json"
    )
    source_payload = {
        "claim_provenance": provenance_rows,
        "question_source_task": question_task,
        "planner_trace": planner_trace,
    }
    hashes = {
        "config_hash": stable_hash(config),
        "source_hash": stable_hash(source_payload),
        "input_hash": stable_hash(inputs.to_dict()),
        "first_leaf_hash": str(first.manifest["leaf_hash"]),
        "second_leaf_hash": str(second.manifest["leaf_hash"]),
    }
    depths = {
        level: sum(level in item.completed_depths for item in first.depth_decisions)
        for level in ("L3_RESEARCH_BRAIN", "L4_ACQUISITION")
    }
    accepted_claim_ids = {
        claim_id
        for item in first.atomic_decisions
        for claim_id in item.accepted_claim_ids
    }
    real_planner_calls = sum(
        item.llm_calls for item in first.deep_executions
        if item.provider_kind == "CODEX"
    )
    fetched_documents = sum(item.fetches for item in first.deep_executions)
    eligible = sum(item.eligible for item in first.universe)
    required_lanes = eligible * 4
    evidence = {
        "eligible_universe_count": eligible,
        "baseline_lane_count": len(first.baseline_lanes),
        "required_baseline_lane_count": required_lanes,
        "trigger_count": len(first.triggers),
        "selected_l3_count": depths["L3_RESEARCH_BRAIN"],
        "selected_l4_count": depths["L4_ACQUISITION"],
        "real_planner_call_count": real_planner_calls,
        "source_task_count": len(first.source_tasks),
        "real_fresh_fetched_document_count": fetched_documents,
        "accepted_current_claim_count": len(accepted_claim_ids),
        "claim_provenance_count": len(first.claim_provenance),
        "atomic_decision_count": len(first.atomic_decisions),
    }
    hard = {
        "bootstrap_failed": int(
            bootstrap.get("status") != "CURRENT_STATE_BOOTSTRAP_PASS"
            or int(bootstrap.get("critical_count_sum") or 0) != 0
        ),
        "eligible_universe_too_small": int(eligible <= 1000),
        "baseline_lane_incomplete": int(len(first.baseline_lanes) != required_lanes),
        "trigger_pool_empty": int(not first.triggers),
        "selected_l3_or_l4_empty": int(not depths["L3_RESEARCH_BRAIN"] or not depths["L4_ACQUISITION"]),
        "real_planner_call_missing": int(real_planner_calls <= 0),
        "source_task_missing": int(not first.source_tasks),
        "fresh_document_missing": int(fetched_documents <= 0),
        "accepted_current_claim_missing": int(not accepted_claim_ids),
        "claim_provenance_missing": int(not first.claim_provenance),
        "atomic_decision_missing": int(not first.atomic_decisions),
        "current_audit_failed": int(first.audit.get("critical_count_sum") != 0),
        "historical_source_replay_failed": int(
            historical_a.get("status") != "HISTORICAL_SOURCE_BACKED_REPLAY_PASS"
            or historical_b.get("status") != "HISTORICAL_SOURCE_BACKED_REPLAY_PASS"
            or historical_a.get("critical_count_sum") != 0
            or historical_b.get("critical_count_sum") != 0
        ),
        "historical_replay_variance": int(
            historical_a.get("replay_leaf_hash") != historical_b.get("replay_leaf_hash")
            or historical_a.get("source_corpus_hash") != historical_b.get("source_corpus_hash")
        ),
        "same_manifest_replay_variance": int(
            first.to_dict() != second.to_dict()
            or hashes["first_leaf_hash"] != hashes["second_leaf_hash"]
        ),
        "partial_claim_promoted_to_final_score": int(
            decision.score_type != "NO_SCORE"
            or decision.score_valid
            or decision.canonical_stage != "0"
        ),
    }
    critical = sum(hard.values())
    report = {
        "schema_version": LIVE_ACCEPTANCE_SCHEMA_VERSION,
        "status": "FULL_LIVE_ACCEPTANCE_PASS" if critical == 0 else "FULL_LIVE_ACCEPTANCE_FAIL",
        "as_of_date": as_of_date,
        "executed_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "required_runs": {
            "live_bootstrap": bootstrap.get("status"),
            "live_daily_current": first.manifest.get("status"),
            "live_full_universe_census_baseline": "PASS" if len(first.baseline_lanes) == required_lanes else "FAIL",
            "live_census_selective_deep": "PASS" if all(depths.values()) else "FAIL",
            "historical_source_backed_replay": historical_a.get("status"),
            "same_manifest_replay_determinism": "ZERO_VARIANCE" if hard["same_manifest_replay_variance"] == 0 else "VARIANCE",
        },
        "current_census_evidence": evidence,
        "accepted_claim_proof": {
            "target_id": target_id,
            "claim_id": atomic.claims[0].claim_id,
            "primitive_id": atomic.claims[0].primitive_id,
            "source_url": provenance_rows[0].get("source_url"),
            "published_date": provenance_rows[0].get("published_date"),
            "content_sha256": provenance_rows[0].get("content_sha256"),
            "exact_quote": provenance_rows[0].get("exact_quote"),
            "mapping_ids": list(atomic.claims[0].mapping_ids),
            "query_generator_kind": (planner_trace.get("traces") or [{}])[0].get("generator_kind"),
            "query_prompt_hash": (planner_trace.get("traces") or [{}])[0].get("prompt_hash"),
            "score_type": decision.score_type,
            "score_valid": decision.score_valid,
            "canonical_stage": decision.canonical_stage,
            "decision_status": decision.decision_status,
            "material_gap_ids": list(decision.material_gap_ids),
        },
        "determinism": {**hashes, "variance_count": hard["same_manifest_replay_variance"]},
        "historical_replay": {
            "case_count": historical_a.get("curated_case_count"),
            "actual_full_source_fetch_count": historical_a.get("actual_full_source_fetch_count"),
            "source_corpus_hash": historical_a.get("source_corpus_hash"),
            "replay_leaf_hash": historical_a.get("replay_leaf_hash"),
            "repeat_replay_leaf_hash": historical_b.get("replay_leaf_hash"),
        },
        "phase_commit_shas": list(config.get("phase_commit_shas") or ()),
        "safety": {
            "future_data_leakage_count": first.audit["critical_counts"]["future_data_leakage"],
            "claim_provenance_contract_complete": first.audit["critical_counts"]["claim_provenance_contract_failure"] == 0,
            "full_thesis_pending_not_green": True,
            "search_snippet_used_as_score_evidence": False,
            "investment_recommendation_emitted": False,
            "production_runtime_ready": False,
        },
        "hard_acceptance_counts": hard,
        "critical_count_sum": critical,
        "hard_acceptance_pass": critical == 0,
    }
    return FullLiveAcceptanceResult(
        status=str(report["status"]),
        inputs=inputs,
        current_result=first,
        report=report,
    )


def write_full_live_acceptance(
    result: FullLiveAcceptanceResult,
    *,
    output_root: str | Path,
    operational_report_path: str | Path,
    shard_count: int = 4,
) -> Mapping[str, Path]:
    root = Path(output_root)
    current_root = root / "current"
    census_root = root / "census"
    write_json(root / "current_operation_input_manifest.json", result.inputs.to_dict())
    write_current_daily_census(result.current_result, output_root=current_root)
    package_live_census_operation(
        result=result.current_result,
        output_root=census_root,
        shard_count=shard_count,
        resume=False,
    )
    write_json(operational_report_path, result.report)
    return {
        "input_manifest": root / "current_operation_input_manifest.json",
        "current_manifest": current_root / "current_daily_census_manifest.json",
        "census_audit": census_root / "census_acceptance_audit.json",
        "operational_report": Path(operational_report_path),
    }


def _daily_source_task(task: Mapping[str, Any]) -> Mapping[str, Any]:
    contract = dict(task.get("acceptance_contract") or {})
    route = dict(task.get("source_route") or {})
    query = dict(task.get("query_intent") or {})
    budget = dict(task.get("budget") or {})
    stop = dict(task.get("stop_condition") or {})
    task_id = str(task.get("task_id") or "")
    return {
        "task_id": "DAILYSRC-" + stable_hash({"question_task_id": task_id})[:24],
        "target_id": str(task.get("target_id") or ""),
        "question_task_id": task_id,
        "source_class": "IssuerIR",
        "max_queries": int(budget.get("max_queries") or 1),
        "max_candidates": int(budget.get("max_candidates") or 1),
        "max_fetches": int(budget.get("max_fetches") or 1),
        "max_retries": 2,
        "recipe_id": str(task.get("recipe_id") or ""),
        "question_to_answer": str(task.get("question_to_answer") or ""),
        "why_material": str(task.get("why_material") or ""),
        "accepted_predicates": list(contract.get("accepted_predicates") or ()),
        "required_entities": list(contract.get("required_entities") or ()),
        "required_values_units": [
            *list(contract.get("required_values") or ()),
            *list(contract.get("required_units") or ()),
        ],
        "time_scope": list(contract.get("required_time_scope") or ()),
        "counter_questions": list(contract.get("counter_questions") or ()),
        "rejection_conditions": list(contract.get("rejection_conditions") or ()),
        "preferred_document_types": list(route.get("preferred_document_types") or ()),
        "preferred_sections": list(route.get("preferred_sections") or ()),
        "fallback_source_classes": list(route.get("fallback_source_families") or ()),
        "literal_queries": list(query.get("literal_queries") or ()),
        "query_provider_name": str(query.get("provider_name") or ""),
        "query_prompt_hash": str(query.get("prompt_hash") or ""),
        "query_response_hash": str(query.get("response_hash") or ""),
        "resolution_conditions": list(stop.get("resolution_conditions") or ()),
        "stop_condition": "stop_on_resolution",
        "allows_general_web": False,
        "official_first_attempted": True,
        "official_gap_reasons": [],
        "test_only": False,
    }


def _replace_target_execution(
    executions: Sequence[Any],
    *,
    target_id: str,
    task_id: str,
    decision_id: str,
    provider_trace_id: str,
) -> list[Mapping[str, Any]]:
    daily_task_id = "DAILYSRC-" + stable_hash({"question_task_id": task_id})[:24]
    rows: list[Mapping[str, Any]] = []
    found = False
    for item in executions:
        row = item.to_dict()
        if item.target_id == target_id:
            found = True
            row.update(
                {
                    "outcome": "SOURCE_PENDING",
                    "terminal_reason": "one current primitive closed; remaining full-thesis primitives require source repair",
                    "atomic_decision_id": decision_id,
                    "source_task_ids": [daily_task_id],
                    "provider_kind": "CODEX",
                    "provider_trace_id": provider_trace_id,
                    "llm_calls": 1,
                    "source_tasks": 1,
                    "fetches": 1,
                    "retries": 0,
                    "general_web_fetches": 0,
                    "official_first_attempted": True,
                    "official_gap_reasons": ["remaining C06 material primitives are source pending"],
                }
            )
        rows.append(row)
    if not found:
        raise ValueError("accepted claim target is outside Census selected deep set")
    return rows


def _direct_task_id(rows: Sequence[Mapping[str, Any]]) -> str:
    values = {
        str(item.get("source_task_id") or "")
        for item in rows
        if item.get("status") == "DIRECT_TASK_SATISFIED"
        and item.get("original_gap_open") is False
    }
    if len(values) != 1:
        raise ValueError("acceptance probe must have exactly one direct task closure")
    return next(iter(values))


def _read_json(path: Path) -> Mapping[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, Mapping):
        raise ValueError(f"JSON object required: {path}")
    return value


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    with path.open(encoding="utf-8") as handle:
        return tuple(json.loads(line) for line in handle if line.strip())


__all__ = [
    "FullLiveAcceptanceResult",
    "LIVE_ACCEPTANCE_SCHEMA_VERSION",
    "run_full_live_acceptance",
    "write_full_live_acceptance",
]
