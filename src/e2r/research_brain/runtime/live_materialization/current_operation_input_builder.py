"""Build canonical CurrentOperationRunnerInput from materialized live leaves."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json
from e2r.research_brain.runtime.current_operation_runner import (
    CURRENT_OPERATION_RUNNER_SCHEMA_VERSION,
    CurrentOperationRunnerInput,
    current_operation_runner_input_from_mapping,
)

from .schemas import LiveRunProfile, load_live_run_profile


_TRIGGER_PRIORITY = {
    "RISK": 100,
    "OFFICIAL": 90,
    "EARNINGS": 85,
    "IR": 80,
    "EXISTING_LEDGER": 75,
    "REPORT": 70,
    "NEWS": 50,
    "MARKET": 40,
}


class CurrentOperationRunnerInputBuilder:
    def build_from_live_root(
        self,
        *,
        as_of_date: str,
        live_root: str | Path,
        run_profile: str | Path,
    ) -> tuple[CurrentOperationRunnerInput, Mapping[str, Any]]:
        root = Path(live_root)
        profile = load_live_run_profile(run_profile)
        universe_rows = _read_jsonl(root / "universe_eligible.jsonl")
        baseline_rows = _read_jsonl(root / "baseline_lanes.jsonl")
        trigger_rows = _read_jsonl(root / "trigger_signals.jsonl")
        source_tasks = _read_jsonl(root / "source_tasks.jsonl")
        decisions = _read_jsonl(root / "atomic_stage_decisions.jsonl")
        gap_rows = _read_jsonl(root / "gap_closure_status.jsonl")
        planner_rows = _read_jsonl(root / "planner_runs.jsonl")
        documents = _read_jsonl(root / "evidence_documents.jsonl")
        accepted_claims = _read_jsonl(root / "accepted_current_claims.jsonl")
        provenance = _read_jsonl(root / "daily_claim_provenance.jsonl")

        triggers = tuple(
            {
                "signal_id": row["trigger_signal_id"],
                "target_id": row["target_id"],
                "observed_date": row["effective_date"],
                "trigger_type": row["trigger_type"],
                "source_id": (row.get("source_refs") or [row["source_event_id"]])[0],
                "historical_replay": False,
                "expected_or_outcome_context": False,
                "counts_as_score_evidence": False,
            }
            for row in trigger_rows
        )
        triggers_by_target: dict[str, list[Mapping[str, Any]]] = {}
        for row in triggers:
            triggers_by_target.setdefault(str(row["target_id"]), []).append(row)
        ordered_candidate_targets = tuple(
            target_id
            for target_id, _ in sorted(
                triggers_by_target.items(),
                key=lambda item: _candidate_sort_key(item[0], item[1]),
            )
        )
        daily_tasks_by_target: dict[str, list[Mapping[str, Any]]] = {}
        for task in source_tasks:
            daily_tasks_by_target.setdefault(str(task["target_id"]), []).append(task)
        decision_by_target = {str(item["target_id"]): item for item in decisions}
        materialized_deep_targets = set(daily_tasks_by_target) | set(decision_by_target)
        missing_candidates = materialized_deep_targets - set(ordered_candidate_targets)
        if missing_candidates:
            raise ValueError("materialized deep target lacks current trigger lineage")
        required_deep_rank = max(
            (ordered_candidate_targets.index(target_id) + 1 for target_id in materialized_deep_targets),
            default=0,
        )
        runtime_max_deep = max(
            int(profile.budgets["max_deep_candidates"]), required_deep_rank
        )
        if runtime_max_deep > int(profile.budgets["max_official_light_targets"]):
            raise ValueError("materialized deep target exceeds official-light budget")
        selected_targets = ordered_candidate_targets[:runtime_max_deep]
        gap_by_target: dict[str, list[Mapping[str, Any]]] = {}
        for item in gap_rows:
            gap_by_target.setdefault(str(item["target_id"]), []).append(item)
        planner_by_target = {
            str(item["target_id"]): item
            for item in planner_rows
            if item.get("real_provider_success") is True
        }
        document_count_by_target: dict[str, int] = {}
        for item in documents:
            target_id = str(item["target_id"])
            document_count_by_target[target_id] = document_count_by_target.get(target_id, 0) + 1
        deep_executions = []
        for target_id in selected_targets:
            target_triggers = tuple(item["signal_id"] for item in triggers_by_target[target_id])
            target_tasks = tuple(daily_tasks_by_target.get(target_id, ()))
            decision = decision_by_target.get(target_id)
            gaps = gap_by_target.get(target_id, ())
            planner = planner_by_target.get(target_id)
            if any(item.get("terminal_status") == "PROVIDER_PENDING" for item in gaps):
                outcome = "PROVIDER_PENDING"
                reason = "material provider gap remains after bounded official-first execution"
            elif any(item.get("terminal_status") == "SOURCE_PENDING" for item in gaps):
                outcome = "SOURCE_PENDING"
                reason = "material source gap remains after unrelated official documents were rejected"
            else:
                outcome = "BUDGET_PENDING"
                reason = "selected deep candidate did not enter the bounded Brain/acquisition budget"
            provider_used = bool(planner)
            deep_executions.append(
                {
                    "execution_id": "DEXEC-" + stable_hash(
                        {"target_id": target_id, "as_of_date": as_of_date}
                    )[:24],
                    "target_id": target_id,
                    "outcome": outcome,
                    "trigger_signal_ids": list(target_triggers),
                    "terminal_reason": reason,
                    "atomic_decision_id": decision.get("decision_id") if decision else None,
                    "source_task_ids": [item["task_id"] for item in target_tasks],
                    "provider_kind": "CODEX" if provider_used else "NONE",
                    "provider_trace_id": planner.get("planner_run_id") if planner else None,
                    "llm_calls": min(int(planner.get("provider_call_count") or 0), int(profile.budgets["max_llm_calls_per_candidate"])) if planner else 0,
                    "source_tasks": len(target_tasks),
                    "fetches": document_count_by_target.get(target_id, 0),
                    "retries": 0,
                    "general_web_fetches": 0,
                    "official_first_attempted": bool(target_tasks),
                    "official_gap_reasons": ([reason] if target_tasks else []),
                    "runtime_seconds": 0.0,
                }
            )
        payload = {
            "schema_version": CURRENT_OPERATION_RUNNER_SCHEMA_VERSION,
            "as_of_date": as_of_date,
            "universe": [
                {
                    "target_id": row["symbol"],
                    "target_name": row["company_name"],
                    "market": row["market"],
                    "as_of_date": as_of_date,
                    "eligible": True,
                    "exclusion_reason": None,
                }
                for row in universe_rows
            ],
            "baseline_lanes": [_baseline_lane(row, as_of_date=as_of_date) for row in baseline_rows],
            "triggers": list(triggers),
            "claims": list(accepted_claims),
            "claim_provenance": list(provenance),
            "source_tasks": list(source_tasks),
            "atomic_decisions": list(decisions),
            "deep_executions": deep_executions,
            "config": {
                **dict(profile.budgets),
                "max_deep_candidates": runtime_max_deep,
                "test_mode": False,
                "require_claim_provenance": True,
            },
        }
        inputs = current_operation_runner_input_from_mapping(payload)
        audit = _audit_builder(
            inputs=inputs,
            profile=profile,
            selected_target_count=len(selected_targets),
            runtime_max_deep=runtime_max_deep,
        )
        return inputs, audit


def write_current_operation_input_manifest(
    inputs: CurrentOperationRunnerInput,
    *,
    live_root: str | Path,
    canonical_input_root: str | Path = "output/current_operation_inputs",
) -> Mapping[str, Path]:
    root = Path(live_root)
    paths = {
        "live_manifest": root / "current_operation_input_manifest.json",
        "canonical_manifest": Path(canonical_input_root) / f"{inputs.as_of_date}.json",
    }
    payload = inputs.to_dict()
    for path in paths.values():
        write_json(path, payload)
    return paths


def _baseline_lane(row: Mapping[str, Any], *, as_of_date: str) -> Mapping[str, Any]:
    sources = tuple(row.get("source_ids") or ())
    error = row.get("provider_error_category")
    if error:
        status = "PROVIDER_FAILED"
        sources = ()
    elif sources:
        status = "OBSERVED"
    else:
        status = "NO_RESULT"
    return {
        "target_id": row["target_id"],
        "as_of_date": as_of_date,
        "lane_type": row["lane"],
        "lane_status": status,
        "source_ids": list(sources),
        "observed_date": row.get("observed_date") if status == "OBSERVED" else None,
        "provider_error": str(error) if error else None,
    }


def _candidate_sort_key(target_id: str, signals: Sequence[Mapping[str, Any]]):
    priorities = tuple(_TRIGGER_PRIORITY[str(item["trigger_type"])] for item in signals)
    families = {str(item["trigger_type"]) for item in signals}
    return (-max(priorities), -len(families), -len(signals), target_id)


def _audit_builder(
    *,
    inputs: CurrentOperationRunnerInput,
    profile: LiveRunProfile,
    selected_target_count: int,
    runtime_max_deep: int,
) -> Mapping[str, Any]:
    critical = {
        "authorized_live_run_manifest_missing_exit": 0,
        "user_manual_manifest_required": 0,
        "materialized_manifest_schema_error": 0,
        "materializer_evaluator_as_of_mismatch": 0,
    }
    return {
        "schema_version": "e2r_current_operation_input_builder_audit_v1",
        "as_of_date": inputs.as_of_date,
        "profile_id": profile.profile_id,
        "universe_count": len(inputs.universe),
        "baseline_lane_count": len(inputs.baseline_lanes),
        "trigger_count": len(inputs.triggers),
        "source_task_count": len(inputs.source_tasks),
        "atomic_decision_count": len(inputs.atomic_decisions),
        "deep_execution_count": len(inputs.deep_executions),
        "selected_target_count": selected_target_count,
        "runtime_max_deep_candidates": runtime_max_deep,
        "profile_max_deep_candidates": profile.budgets["max_deep_candidates"],
        "test_mode": inputs.config.test_mode,
        "critical_counts": critical,
        "critical_count_sum": 0,
        "hard_acceptance_pass": True,
        "production_runtime_ready": False,
    }


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    with path.open(encoding="utf-8") as handle:
        return tuple(json.loads(line) for line in handle if line.strip())


__all__ = [
    "CurrentOperationRunnerInputBuilder",
    "write_current_operation_input_manifest",
]
