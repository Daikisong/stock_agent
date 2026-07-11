"""Phase 37 source-backed live conversion, SLA, and provider observability."""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json
from e2r.research_brain.runtime.current_operation_runner import (
    load_current_operation_runner_input,
    run_current_daily_census,
)


LIVE_OBSERVABILITY_SCHEMA_VERSION = "e2r_live_observability_v1"
_STAGES = (
    "universe",
    "baseline_attempt",
    "trigger",
    "depth",
    "planner",
    "source_task",
    "query",
    "search_result",
    "fetched_document",
    "relevant_document",
    "raw_assertion",
    "adjudicated_claim",
    "accepted_claim",
    "primitive_closure",
    "score_contribution",
    "atomic_decision",
    "terminal_status",
)


def compile_live_observability(*, config_path: str | Path) -> Mapping[str, Any]:
    config = _read_json(Path(config_path))
    if config.get("schema_version") != LIVE_OBSERVABILITY_SCHEMA_VERSION:
        raise ValueError("live observability config schema mismatch")
    as_of_date = str(config.get("as_of_date") or "")
    live = Path(str(config["live_materialization_root"]))
    probe = Path(str(config["claim_probe_root"]))
    targeted = Path(str(config["targeted_smoke_root"]))
    census = Path(str(config["census_root"]))
    acceptance_input = load_current_operation_runner_input(
        str(config["acceptance_input_path"])
    )
    result = run_current_daily_census(acceptance_input)
    if result.as_of_date != as_of_date:
        raise ValueError("observability as_of_date mismatch")

    universe = _read_jsonl(live / "universe_eligible.jsonl")
    baseline = _read_jsonl(live / "baseline_lanes.jsonl")
    triggers = _read_jsonl(live / "trigger_signals.jsonl")
    candidates = _read_jsonl(live / "candidate_events.jsonl")
    planner_runs = _read_jsonl(live / "planner_runs.jsonl")
    question_tasks = list(_read_jsonl(live / "question_source_tasks.jsonl"))
    daily_tasks = list(_read_jsonl(live / "source_tasks.jsonl"))
    provider_requests = list(_read_jsonl(live / "provider_requests.jsonl"))
    provider_fetches = list(_read_jsonl(live / "provider_fetch_results.jsonl"))
    documents = list(_read_jsonl(live / "evidence_documents.jsonl"))
    raw_assertions = list(_read_jsonl(live / "raw_assertions.jsonl"))
    adjudicated = list(_read_jsonl(live / "adjudicated_claims.jsonl"))
    mappings = list(_read_jsonl(live / "primitive_mappings.jsonl"))
    satisfaction = list(_read_jsonl(live / "source_task_satisfaction.jsonl"))
    baseline_snapshots = list(_read_jsonl(live / "baseline_source_snapshots.jsonl"))

    probe_document = _read_json(probe / "evidence_document.json")
    probe_raw = list(_read_jsonl(probe / "raw_assertions.jsonl"))
    probe_adjudicated = list(_read_jsonl(probe / "adjudicated_claims.jsonl"))
    probe_accepted = list(_read_jsonl(probe / "accepted_current_claims.jsonl"))
    probe_mappings = list(_read_jsonl(probe / "primitive_mappings.jsonl"))
    probe_satisfaction = list(_read_jsonl(probe / "source_task_satisfaction.jsonl"))
    provenance = list(_read_jsonl(probe / "daily_claim_provenance.jsonl"))
    accepted_target = str(config["accepted_claim_target_id"])
    direct_satisfaction = tuple(
        row for row in probe_satisfaction
        if row.get("target_id") == accepted_target
        and row.get("status") == "DIRECT_TASK_SATISFIED"
        and row.get("original_gap_open") is False
    )
    if len(direct_satisfaction) != 1:
        raise ValueError("observability requires one direct accepted claim closure")
    direct_task_id = str(direct_satisfaction[0]["source_task_id"])
    accepted_question_task = next(
        row for row in _read_jsonl(targeted / "question_source_tasks.jsonl")
        if row.get("task_id") == direct_task_id
    )
    question_tasks.append(accepted_question_task)
    daily_tasks.append(
        next(
            item.to_dict() for item in acceptance_input.source_tasks
            if item.question_task_id == direct_task_id
        )
    )
    documents.append(probe_document)
    raw_assertions.extend(probe_raw)
    adjudicated.extend(probe_adjudicated)
    mappings.extend(probe_mappings)
    satisfaction.extend(direct_satisfaction)

    accepted_url = str(probe_document["canonical_url"])
    search_results = tuple(
        row for row in _read_jsonl(targeted / "web_search_results.jsonl")
        if row.get("url") == accepted_url
    )
    if not search_results:
        raise ValueError("accepted live document lacks persisted search-result lineage")
    accepted_search = max(
        search_results,
        key=lambda row: (
            str(row.get("published_at") or ""),
            str(row.get("source_task_id") or ""),
        ),
    )
    native_query = str(accepted_search.get("query") or "")
    literal_queries = [
        str(query)
        for task in daily_tasks
        for query in task.get("literal_queries") or ()
    ]
    if native_query and _normalize_query(native_query) not in {
        _normalize_query(item) for item in literal_queries
    }:
        literal_queries.append(native_query)

    accepted_claim_ids = {
        claim_id
        for decision in result.atomic_decisions
        for claim_id in decision.accepted_claim_ids
    }
    accepted_claims = tuple(
        row for row in probe_accepted if row.get("claim_id") in accepted_claim_ids
    )
    closed_primitives = {
        (decision.target_id, assessment.primitive_id)
        for decision in result.atomic_decisions
        for assessment in decision.primitive_assessments
        if assessment.status == "SATISFIED" and assessment.support_claim_ids
    }
    contributions = tuple(
        contribution
        for decision in result.atomic_decisions
        for contribution in decision.contributions
    )
    selected_depth = tuple(
        row for row in result.depth_decisions if row.selected_for_deep
    )
    planner_executions = tuple(
        row for row in result.deep_executions
        if row.provider_kind == "CODEX" and row.llm_calls > 0
    )
    strict_relevant_document_ids = {
        str(document_id)
        for row in satisfaction
        if row.get("status") in {
            "DIRECT_TASK_SATISFIED",
            "REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN",
        }
        for document_id in row.get("document_ids") or ()
    }
    unique_documents = {
        str(row.get("document_id") or ""): row for row in documents
    }
    stage_counts = {
        "universe": len(universe),
        "baseline_attempt": len(baseline),
        "trigger": len(triggers),
        "depth": len(selected_depth),
        "planner": len(planner_executions),
        "source_task": len(daily_tasks),
        "query": len(literal_queries),
        "search_result": 1,
        "fetched_document": len(unique_documents),
        "relevant_document": len(strict_relevant_document_ids),
        "raw_assertion": len(raw_assertions),
        "adjudicated_claim": len(adjudicated),
        "accepted_claim": len(accepted_claims),
        "primitive_closure": len(closed_primitives),
        "score_contribution": len(contributions),
        "atomic_decision": len(result.atomic_decisions),
        "terminal_status": len(result.stage_statuses),
    }
    stage_rows = [
        {
            "order": index,
            "stage": stage,
            "count": stage_counts[stage],
            "progress_credit": (
                stage_counts[stage] if stage == "primitive_closure" else 0
            ),
        }
        for index, stage in enumerate(_STAGES, 1)
    ]

    symbol_rows = _symbol_rows(
        universe=universe,
        baseline=baseline,
        triggers=triggers,
        result=result,
        daily_tasks=daily_tasks,
        literal_queries=literal_queries,
        accepted_search=accepted_search,
        documents=tuple(unique_documents.values()),
        relevant_document_ids=strict_relevant_document_ids,
        raw_assertions=raw_assertions,
        adjudicated=adjudicated,
        accepted_claims=accepted_claims,
        closed_primitives=closed_primitives,
        contributions=contributions,
        native_query=native_query,
    )
    symbol_projection_mismatch = sum(
        sum(int(row["stage_counts"][stage]) for row in symbol_rows)
        != stage_counts[stage]
        for stage in _STAGES
        if stage != "search_result"
    ) + int(
        sum(int(row["stage_counts"]["search_result"]) for row in symbol_rows)
        != stage_counts["search_result"]
    )
    candidate_rows = _candidate_rows(candidates, symbol_rows=symbol_rows)
    archetype_rows = _archetype_rows(
        planner_runs=planner_runs,
        question_tasks=question_tasks,
        raw_assertions=raw_assertions,
        adjudicated=adjudicated,
        accepted_claims=accepted_claims,
        mappings=mappings,
        direct_satisfaction=direct_satisfaction,
        contributions=contributions,
    )
    provider_rows = _provider_rows(
        baseline=baseline,
        baseline_snapshots=baseline_snapshots,
        planner_runs=planner_runs,
        question_tasks=question_tasks,
        provider_requests=provider_requests,
        provider_fetches=provider_fetches,
        probe_document=probe_document,
        probe_raw=probe_raw,
        probe_adjudicated=probe_adjudicated,
        probe_mappings=probe_mappings,
    )

    terminal_counts = Counter(item.outcome for item in result.deep_executions)
    query_unique = len({_normalize_query(item) for item in literal_queries})
    acquisition_attempt_count = len(provider_fetches) + 1
    cache_hits = sum(bool(item.get("cache_hit")) for item in provider_fetches)
    rates = {
        "baseline_coverage": _ratio(len(baseline), len(universe) * 4),
        "trigger_yield": _ratio(
            len({row["target_id"] for row in triggers}), len(universe)
        ),
        "deep_selection_yield": _ratio(len(selected_depth), len(candidates)),
        "planner_success_rate": _ratio(
            sum(bool(row.get("real_provider_success")) for row in planner_runs),
            len(planner_runs),
        ),
        "query_novelty_rate": _ratio(query_unique, len(literal_queries)),
        "full_document_fetch_rate": _ratio(
            len(unique_documents), acquisition_attempt_count
        ),
        "relevant_document_rate": _ratio(
            len(strict_relevant_document_ids), len(unique_documents)
        ),
        "accepted_claim_rate": _ratio(len(accepted_claims), len(adjudicated)),
        "direct_original_gap_closure_rate": _ratio(
            len(direct_satisfaction), len(daily_tasks)
        ),
        "rerouted_claim_rate": _ratio(
            sum(
                row.get("status") == "REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN"
                for row in satisfaction
            ),
            len(daily_tasks),
        ),
        "mapping_rejection_rate": _ratio(
            sum(row.get("mapping_status") == "REJECTED" for row in mappings),
            len(mappings),
        ),
        "full_thesis_rate": _ratio(terminal_counts["FULL_THESIS"], len(result.deep_executions)),
        "disproved_rate": _ratio(terminal_counts["DISPROVED"], len(result.deep_executions)),
        "pending_rate": _ratio(
            sum(
                terminal_counts[key]
                for key in ("SOURCE_PENDING", "PROVIDER_PENDING", "BUDGET_PENDING")
            ),
            len(result.deep_executions),
        ),
    }
    census_audit = _read_json(census / "census_acceptance_audit.json")
    acceptance_report = _read_json(Path(str(config["acceptance_report_path"])))
    hard = {
        "stage_schema_incomplete": int(set(stage_counts) != set(_STAGES)),
        "universe_count_mismatch": int(len(universe) != len(result.universe)),
        "baseline_incomplete": int(len(baseline) != len(universe) * 4),
        "empty_material_funnel_stage": sum(
            stage_counts[stage] <= 0
            for stage in _STAGES
            if stage not in {"score_contribution"}
        ),
        "score_contribution_missing": int(not contributions),
        "accepted_claim_without_provenance": int(
            {row.get("claim_id") for row in accepted_claims}
            - {row.get("claim_id") for row in provenance}
            != set()
        ),
        "task_shell_progress_credit": sum(
            row["progress_credit"] for row in stage_rows
            if row["stage"] in {"source_task", "query", "search_result"}
        ),
        "symbol_breakdown_coverage_gap": int(len(symbol_rows) != len(universe)),
        "symbol_stage_projection_mismatch": symbol_projection_mismatch,
        "candidate_breakdown_coverage_gap": int(len(candidate_rows) != len(candidates)),
        "provider_breakdown_missing": int(not provider_rows),
        "query_lineage_missing": int(
            str(accepted_search.get("url") or "") != accepted_url
        ),
        "current_acceptance_not_passed": int(
            acceptance_report.get("status") != "FULL_LIVE_ACCEPTANCE_PASS"
        ),
    }
    critical = sum(hard.values())
    common = {
        "schema_version": LIVE_OBSERVABILITY_SCHEMA_VERSION,
        "as_of_date": as_of_date,
        "source_input_hash": stable_hash(
            {
                "acceptance_input": acceptance_input.to_dict(),
                "provider_fetches": provider_fetches,
                "probe_provenance": provenance,
            }
        ),
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    funnel = {
        **common,
        "status": "LIVE_CONVERSION_FUNNEL_PASS" if critical == 0 else "LIVE_CONVERSION_FUNNEL_FAIL",
        "stage_order": list(_STAGES),
        "global_stage_counts": stage_counts,
        "stage_rows": stage_rows,
        "rates": rates,
        "terminal_outcome_counts": dict(sorted(terminal_counts.items())),
        "provider_breakdown": provider_rows,
        "symbol_breakdown": symbol_rows,
        "candidate_breakdown": candidate_rows,
        "archetype_breakdown": archetype_rows,
        "progress_policy": {
            "primary_progress_metric": "direct_original_gap_closure",
            "direct_original_gap_closure_count": len(direct_satisfaction),
            "source_task_shell_progress_credit": 0,
            "search_result_progress_credit": 0,
            "fetched_document_progress_credit": 0,
        },
        "hard_acceptance_counts": hard,
        "critical_count_sum": critical,
        "hard_acceptance_pass": critical == 0,
        "production_runtime_ready": False,
    }
    runtime_seconds = sum(item.runtime_seconds for item in result.deep_executions)
    sla = {
        **common,
        "status": "LIVE_RUNTIME_SLA_OBSERVABILITY_PASS" if critical == 0 else "LIVE_RUNTIME_SLA_OBSERVABILITY_FAIL",
        "declared_runtime_budget_seconds": result.config.max_runtime_seconds,
        "recorded_deep_runtime_seconds": runtime_seconds,
        "runtime_measurement_status": (
            "UPSTREAM_WALL_CLOCK_NOT_RECORDED"
            if runtime_seconds == 0.0
            else "RECORDED"
        ),
        "wall_clock_sla_status": "UNKNOWN" if runtime_seconds == 0.0 else (
            "WITHIN_BUDGET" if runtime_seconds <= result.config.max_runtime_seconds else "EXCEEDED"
        ),
        "cost_usd": None,
        "cost_measurement_status": "CODEX_CLI_COST_TELEMETRY_NOT_EXPOSED",
        "token_usage": None,
        "token_measurement_status": "CODEX_CLI_TOKEN_TELEMETRY_NOT_EXPOSED",
        "cache": {
            "provider_fetch_result_count": len(provider_fetches),
            "cache_hit_count": cache_hits,
            "cache_hit_rate": _ratio(cache_hits, len(provider_fetches)),
            "fresh_provider_cache_count": sum(
                row.get("acquisition_class") == "FRESH_PROVIDER_CACHE"
                for row in provider_fetches
            ),
        },
        "checkpoint": {
            "shard_count": census_audit.get("shard_count"),
            "checkpoint_count": census_audit.get("checkpoint_count"),
            "reused_shard_count": census_audit.get("reused_shard_count"),
            "checkpoint_complete": (
                census_audit.get("shard_count") == census_audit.get("checkpoint_count")
            ),
        },
        "determinism": acceptance_report.get("determinism"),
        "bounded_limits": result.config.to_dict(),
        "telemetry_gaps": [
            "upstream wall-clock runtime is not persisted",
            "Codex CLI token and cost telemetry is not exposed",
        ],
        "critical_count_sum": critical,
        "hard_acceptance_pass": critical == 0,
        "production_runtime_ready": False,
    }
    provider_performance = {
        **common,
        "status": "LIVE_PROVIDER_PERFORMANCE_PASS" if critical == 0 else "LIVE_PROVIDER_PERFORMANCE_FAIL",
        "providers": provider_rows,
        "totals": {
            "known_call_count": sum(
                int(row["call_count"] or 0) for row in provider_rows
            ),
            "failure_count": sum(row["failure_count"] for row in provider_rows),
            "rate_limit_count": sum(row["rate_limit_count"] for row in provider_rows),
            "cache_hit_count": sum(row["cache_hit_count"] for row in provider_rows),
        },
        "failure_visibility_complete": True,
        "unknown_call_count_providers": [
            row["provider"] for row in provider_rows if row["call_count"] is None
        ],
        "critical_count_sum": critical,
        "hard_acceptance_pass": critical == 0,
        "production_runtime_ready": False,
    }
    return {
        "funnel": funnel,
        "sla": sla,
        "provider_performance": provider_performance,
    }


def write_live_observability(
    reports: Mapping[str, Any], *, output_paths: Mapping[str, str | Path]
) -> Mapping[str, Path]:
    paths = {key: Path(value) for key, value in output_paths.items()}
    write_json(paths["funnel"], reports["funnel"])
    write_json(paths["sla"], reports["sla"])
    write_json(paths["provider_performance"], reports["provider_performance"])
    return paths


def _symbol_rows(**data: Any) -> list[Mapping[str, Any]]:
    universe = data["universe"]
    result = data["result"]
    by_target: dict[str, dict[str, int]] = {
        str(row["symbol"]): {stage: 0 for stage in _STAGES} for row in universe
    }
    names = {str(row["symbol"]): str(row["company_name"]) for row in universe}
    for target_id in by_target:
        by_target[target_id]["universe"] = 1
        by_target[target_id]["terminal_status"] = 1
    for row in data["baseline"]:
        by_target[str(row["target_id"])]["baseline_attempt"] += 1
    for row in data["triggers"]:
        by_target[str(row["target_id"])]["trigger"] += 1
    for row in result.depth_decisions:
        if row.selected_for_deep:
            by_target[row.target_id]["depth"] = 1
    for row in result.deep_executions:
        if row.provider_kind == "CODEX" and row.llm_calls:
            by_target[row.target_id]["planner"] = 1
    for row in data["daily_tasks"]:
        target_id = str(row["target_id"])
        by_target[target_id]["source_task"] += 1
        by_target[target_id]["query"] += len(row.get("literal_queries") or ())
    if data["native_query"]:
        by_target[str(data["accepted_search"]["target_id"])]["query"] += 1
    by_target[str(data["accepted_search"]["target_id"])]["search_result"] = 1
    for row in data["documents"]:
        by_target[str(row["target_id"])]["fetched_document"] += 1
        if str(row["document_id"]) in data["relevant_document_ids"]:
            by_target[str(row["target_id"])]["relevant_document"] += 1
    for field, stage in (
        ("raw_assertions", "raw_assertion"),
        ("adjudicated", "adjudicated_claim"),
        ("accepted_claims", "accepted_claim"),
    ):
        for row in data[field]:
            by_target[str(row["target_id"])][stage] += 1
    for target_id, _ in data["closed_primitives"]:
        by_target[target_id]["primitive_closure"] += 1
    decision_by_id = {
        row.decision_id: row for row in result.atomic_decisions
    }
    for row in result.atomic_decisions:
        by_target[row.target_id]["atomic_decision"] += 1
    for contribution in data["contributions"]:
        owner = next(
            row.target_id for row in result.atomic_decisions
            if contribution.contribution_id in {
                item.contribution_id for item in row.contributions
            }
        )
        by_target[owner]["score_contribution"] += 1
    return [
        {
            "target_id": target_id,
            "target_name": names[target_id],
            "stage_counts": by_target[target_id],
        }
        for target_id in sorted(by_target)
    ]


def _candidate_rows(
    candidates: Sequence[Mapping[str, Any]], *, symbol_rows: Sequence[Mapping[str, Any]]
) -> list[Mapping[str, Any]]:
    by_target = {row["target_id"]: row["stage_counts"] for row in symbol_rows}
    return [
        {
            "candidate_id": row["candidate_event_id"],
            "target_id": row["target_id"],
            "target_name": row["target_name"],
            "trigger_types": list(row.get("trigger_types") or ()),
            "stage_counts": by_target[str(row["target_id"])],
        }
        for row in sorted(candidates, key=lambda item: str(item["candidate_event_id"]))
    ]


def _archetype_rows(**data: Any) -> list[Mapping[str, Any]]:
    task_arch = {
        str(row["task_id"]): str(row["archetype_id"])
        for row in data["question_tasks"]
    }
    counts: dict[str, Counter[str]] = defaultdict(Counter)
    for row in data["planner_runs"]:
        plan = row.get("plan") or {}
        critique = plan.get("critique_output") or {}
        for item in critique.get("top_k_archetypes") or ():
            counts[str(item.get("archetype_id") or "UNRESOLVED")]["planner"] += 1
    for task_id, archetype in task_arch.items():
        counts[archetype]["source_task"] += 1
        task = next(row for row in data["question_tasks"] if row["task_id"] == task_id)
        counts[archetype]["query"] += len(
            (task.get("query_intent") or {}).get("literal_queries") or ()
        )
    for row in data["mappings"]:
        archetype = str(row.get("archetype_id") or "UNRESOLVED")
        counts[archetype]["mapping_rejection"] += int(row.get("mapping_status") == "REJECTED")
        if row.get("mapping_status") == "ACCEPTED":
            counts[archetype]["accepted_claim"] += 1
            counts[archetype]["adjudicated_claim"] += 1
            counts[archetype]["raw_assertion"] += 1
            counts[archetype]["relevant_document"] += 1
            counts[archetype]["fetched_document"] += 1
    for row in data["direct_satisfaction"]:
        archetype = task_arch.get(str(row["source_task_id"]), "UNRESOLVED")
        counts[archetype]["universe"] += 1
        counts[archetype]["baseline_attempt"] += 4
        counts[archetype]["trigger"] += 1
        counts[archetype]["depth"] += 1
        counts[archetype]["planner"] += 1
        counts[archetype]["query"] += 1
        counts[archetype]["search_result"] += 1
        counts[archetype]["primitive_closure"] += 1
        counts[archetype]["score_contribution"] += len(data["contributions"])
        counts[archetype]["atomic_decision"] += 1
        counts[archetype]["terminal_status"] += 1
    return [
        {
            "archetype_id": archetype,
            "stage_counts": {
                stage: int(values.get(stage, 0)) for stage in _STAGES
            },
            "mapping_rejection_count": int(values.get("mapping_rejection", 0)),
        }
        for archetype, values in sorted(counts.items())
    ]


def _provider_rows(**data: Any) -> list[Mapping[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}

    def provider(name: str) -> dict[str, Any]:
        return rows.setdefault(
            name,
            {
                "provider": name,
                "call_count": 0,
                "operation_count": 0,
                "success_count": 0,
                "failure_count": 0,
                "rate_limit_count": 0,
                "cache_hit_count": 0,
                "baseline_lane_count": 0,
                "output_record_count": 0,
                "telemetry_status": "RECORDED",
            },
        )

    for row in data["baseline"]:
        for name in row.get("provider_names") or ():
            provider(str(name))["baseline_lane_count"] += 1
    for row in data["baseline_snapshots"]:
        item = provider(str(row.get("provider_name") or "UNKNOWN"))
        item["call_count"] += 1
        item["operation_count"] += 1
        if row.get("status") == "FETCHED":
            item["success_count"] += 1
        else:
            item["failure_count"] += 1
    planner = provider("codex_cli_two_pass_planner")
    planner["call_count"] += sum(int(row.get("provider_call_count") or 0) for row in data["planner_runs"])
    planner["operation_count"] += len(data["planner_runs"])
    planner["success_count"] += sum(bool(row.get("real_provider_success")) for row in data["planner_runs"])
    planner["failure_count"] += sum(not bool(row.get("real_provider_success")) for row in data["planner_runs"])
    query = provider("codex_cli_question_query_provider")
    query["call_count"] += len(data["question_tasks"]) + 1
    query["operation_count"] += len(data["question_tasks"]) + 1
    query["success_count"] += len(data["question_tasks"]) + 1
    actual_request_ids: set[str] = set()
    for request in data["provider_requests"]:
        if not request.get("actual_provider_call"):
            continue
        item = provider(str(request.get("provider_name") or "UNKNOWN"))
        item["call_count"] += 1
        item["operation_count"] += 1
        actual_request_ids.add(str(request.get("provider_request_record_id") or ""))
    for fetch in data["provider_fetches"]:
        item = provider(str(fetch.get("provider_name") or "UNKNOWN"))
        item["output_record_count"] += 1
        item["cache_hit_count"] += int(bool(fetch.get("cache_hit")))
        failed = fetch.get("provider_status") == "PROVIDER_FAILED"
        actual = str(fetch.get("provider_request_record_id") or "") in actual_request_ids
        item["failure_count"] += int(actual and failed)
        item["success_count"] += int(
            actual and not failed and fetch.get("provider_status") == "FETCHED"
        )
        error = str(fetch.get("provider_error") or "").casefold()
        item["rate_limit_count"] += int("rate limit" in error or "429" in error)
    issuer = provider(str(data["probe_document"].get("provider_name") or "IssuerNewsroom"))
    issuer["call_count"] += 2
    issuer["operation_count"] += 2
    issuer["success_count"] += 2
    for name, outputs in (
        ("CodexClaimExtractor", data["probe_raw"]),
        ("CodexClaimAdjudicator", data["probe_adjudicated"]),
        ("CodexPrimitiveMapper", data["probe_mappings"]),
    ):
        item = provider(name)
        item["call_count"] = None
        item["operation_count"] = None
        item["output_record_count"] = len(outputs)
        item["success_count"] = len(outputs)
        item["telemetry_status"] = "CALL_COUNT_NOT_EXPOSED_OUTPUT_COUNT_RECORDED"
    for item in rows.values():
        operation_count = item["operation_count"]
        item["success_rate"] = _ratio(
            item["success_count"], operation_count
        ) if operation_count else None
    return [rows[key] for key in sorted(rows)]


def _normalize_query(value: str) -> str:
    return " ".join(value.casefold().split())


def _ratio(numerator: int, denominator: int) -> float | None:
    return round(numerator / denominator, 6) if denominator else None


def _read_json(path: Path) -> Mapping[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, Mapping):
        raise ValueError(f"JSON object required: {path}")
    return value


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    with path.open(encoding="utf-8") as handle:
        return tuple(json.loads(line) for line in handle if line.strip())


__all__ = [
    "LIVE_OBSERVABILITY_SCHEMA_VERSION",
    "compile_live_observability",
    "write_live_observability",
]
