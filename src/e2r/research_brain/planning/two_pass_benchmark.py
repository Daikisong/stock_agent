"""Evaluator-only benchmark for the canonical two-pass Research Brain."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS
from e2r.production.metadata import stable_hash, write_json, write_jsonl, write_text
from e2r.research_brain.intelligence_schema import PlannerStatus
from e2r.research_brain.planning.two_pass_brain_planner import (
    TwoPassPlannerProvider,
    compile_blind_hypothesis_input,
    run_two_pass_planner,
)
from e2r.research_brain.retrieval import SemanticMemoryIndex
from e2r.research_brain.retrieval.balanced_case_retriever import (
    BlindRetrievalBenchmarkCase,
)


TWO_PASS_BENCHMARK_SCHEMA_VERSION = "e2r_two_pass_planner_benchmark_v1"
_CRITICAL_GUARD_ROLES = {"GUARD", "HARD_BREAK"}


@dataclass(frozen=True)
class TwoPassPlannerBenchmarkAudit:
    rows: tuple[Mapping[str, Any], ...]
    manifest: Mapping[str, Any]


def evaluate_two_pass_planner_benchmark(
    *,
    memory_index: SemanticMemoryIndex,
    benchmark_cases: Iterable[BlindRetrievalBenchmarkCase],
    provider: TwoPassPlannerProvider,
    test_mode: bool,
) -> TwoPassPlannerBenchmarkAudit:
    recipe_role_by_pair = {
        (node.archetype_id, node.primitive_id): str(
            node.planner_payload.get("role") or ""
        )
        for node in memory_index.graph.nodes
        if node.node_type == "RECIPE"
        and node.archetype_id
        and node.primitive_id
    }
    rows: list[Mapping[str, Any]] = []
    for benchmark in benchmark_cases:
        compiled = compile_blind_hypothesis_input(
            target_id="BLIND-BENCHMARK-TARGET",
            target_name="Blind benchmark target",
            target_aliases=(),
            as_of_date=benchmark.as_of_date,
            evidence_rows=(
                {
                    "fact_id": "CURRENT-FACT-1",
                    "text": benchmark.current_evidence,
                    "observed_date": benchmark.as_of_date,
                    "target_relation": "DIRECT",
                    "current_status": "CURRENT",
                },
            ),
        )
        plan = run_two_pass_planner(
            blind_input=compiled.blind_input,
            memory_index=memory_index,
            provider=provider,
            test_mode=test_mode,
        )
        critique = plan.critique_output
        top_ids = tuple(
            hypothesis.archetype_id
            for hypothesis in (critique.top_k_archetypes if critique else ())
        )
        evaluated = benchmark.archetype_retrieval_expected
        top3_hit = (
            benchmark.expected_archetype_id in top_ids[:3]
            if evaluated
            else None
        )
        top1_hit = (
            bool(top_ids and top_ids[0] == benchmark.expected_archetype_id)
            if evaluated
            else None
        )
        expected_role = recipe_role_by_pair.get(
            (benchmark.expected_archetype_id, benchmark.expected_primitive_id),
            "",
        )
        critical_guard_case = expected_role in _CRITICAL_GUARD_ROLES
        critical_guard_misroute = bool(
            critical_guard_case
            and (
                benchmark.expected_archetype_id not in top_ids[:3]
                or (
                    top_ids
                    and top_ids[0] == benchmark.expected_archetype_id
                    and critique is not None
                    and not critique.do_not_promote_reasons
                )
            )
        )
        trace_hash_missing = sum(
            not trace.prompt_hash or not trace.response_hash
            for trace in plan.provider_traces
        )
        payload_text = json.dumps(plan.to_dict(), ensure_ascii=False, sort_keys=True)
        rows.append(
            {
                "schema_version": TWO_PASS_BENCHMARK_SCHEMA_VERSION,
                "benchmark_id": benchmark.benchmark_id,
                "expected_archetype_id": benchmark.expected_archetype_id,
                "expected_primitive_id": benchmark.expected_primitive_id,
                "archetype_retrieval_expected": evaluated,
                "plan_id": plan.plan_id,
                "plan_status": plan.status,
                "top_archetype_ids": list(top_ids),
                "top3_hit": top3_hit,
                "top1_hit": top1_hit,
                "critical_guard_case": critical_guard_case,
                "critical_guard_misroute": critical_guard_misroute,
                "abstained": plan.status == PlannerStatus.ABSTAINED.value,
                "pending": plan.status == PlannerStatus.PENDING.value,
                "pending_reason_code": plan.pending.reason_code if plan.pending else None,
                "provider_name": provider.provider_name,
                "real_provider": bool(provider.real_provider),
                "fake_provider": bool(provider.fake_provider),
                "provider_trace_count": len(plan.provider_traces),
                "provider_trace_hashes": [
                    {
                        "planner_pass": trace.planner_pass,
                        "prompt_hash": trace.prompt_hash,
                        "response_hash": trace.response_hash,
                    }
                    for trace in plan.provider_traces
                ],
                "trace_hash_missing_count": trace_hash_missing,
                "deterministic_mutation": plan.deterministic_stage_or_score_mutation,
                "source_primary_copy_count": payload_text.lower().count("source_primary"),
                "input_audit": dict(compiled.audit),
            }
        )

    evaluated_rows = [row for row in rows if row["archetype_retrieval_expected"]]
    top3_rate = _rate(evaluated_rows, "top3_hit")
    top1_rate = _rate(evaluated_rows, "top1_hit")
    pending_count = sum(row["pending"] for row in rows)
    abstention_count = sum(row["abstained"] for row in rows)
    critical_guard_misroute_count = sum(
        row["critical_guard_misroute"] for row in rows
    )
    impossible_assignment_count = sum(
        any(item not in CANONICAL_ARCHETYPE_IDS for item in row["top_archetype_ids"])
        for row in rows
    )
    trace_hash_missing_count = sum(row["trace_hash_missing_count"] for row in rows)
    planner_mutation_count = sum(row["deterministic_mutation"] for row in rows)
    source_primary_copy_count = sum(row["source_primary_copy_count"] for row in rows)
    critical = {
        "blind_top3_rate_below_0_95": int(top3_rate < 0.95),
        "blind_top1_rate_below_0_85": int(top1_rate < 0.85),
        "critical_guard_misroute": critical_guard_misroute_count,
        "impossible_archetype_assignment": impossible_assignment_count,
        "planner_score_stage_mutation": planner_mutation_count,
        "source_primary_copy_without_reason": source_primary_copy_count,
        "prompt_response_hash_missing": trace_hash_missing_count,
        "benchmark_provider_pending": pending_count,
        "ambiguous_abstention_missing": int(abstention_count == 0),
    }
    status_prefix = "REAL" if provider.real_provider else "TEST"
    manifest = {
        "schema_version": TWO_PASS_BENCHMARK_SCHEMA_VERSION,
        "status": (
            f"TWO_PASS_PLANNER_{status_prefix}_BENCHMARK_PASS"
            if rows and sum(critical.values()) == 0
            else f"TWO_PASS_PLANNER_{status_prefix}_BENCHMARK_FAIL"
        ),
        "provider_name": provider.provider_name,
        "real_provider": bool(provider.real_provider),
        "fake_provider": bool(provider.fake_provider),
        "benchmark_count": len(rows),
        "archetype_benchmark_count": len(evaluated_rows),
        "top3_hit_count": sum(bool(row["top3_hit"]) for row in evaluated_rows),
        "top3_hit_rate": top3_rate,
        "top1_hit_count": sum(bool(row["top1_hit"]) for row in evaluated_rows),
        "top1_hit_rate": top1_rate,
        "abstention_count": abstention_count,
        "pending_count": pending_count,
        "critical_guard_case_count": sum(row["critical_guard_case"] for row in rows),
        "critical_guard_misroute_count": critical_guard_misroute_count,
        "impossible_archetype_assignment_count": impossible_assignment_count,
        "planner_score_stage_mutation_count": planner_mutation_count,
        "source_primary_copy_without_reason_count": source_primary_copy_count,
        "prompt_response_hash_missing_count": trace_hash_missing_count,
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "result_hash": stable_hash(rows),
        "production_runtime_ready": False,
    }
    return TwoPassPlannerBenchmarkAudit(rows=tuple(rows), manifest=manifest)


def write_two_pass_planner_benchmark(
    audit: TwoPassPlannerBenchmarkAudit,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root) / "planning"
    paths = {
        "rows": root / "two_pass_blind_benchmark.jsonl",
        "acceptance": root / "two_pass_benchmark_acceptance.json",
        "report": root / "two_pass_benchmark_report.md",
    }
    write_jsonl(paths["rows"], audit.rows)
    write_json(paths["acceptance"], dict(audit.manifest))
    write_text(paths["report"], render_two_pass_benchmark_report(audit.manifest))
    return paths


def render_two_pass_benchmark_report(manifest: Mapping[str, Any]) -> str:
    lines = [
        "# E2R Two-Pass Planner Blind Benchmark",
        "",
        f"- status: {manifest['status']}",
        f"- provider_name: {manifest['provider_name']}",
        f"- benchmark_count: {manifest['benchmark_count']}",
        f"- top3_hit_rate: {manifest['top3_hit_rate']:.4f}",
        f"- top1_hit_rate: {manifest['top1_hit_rate']:.4f}",
        f"- abstention_count: {manifest['abstention_count']}",
        f"- critical_guard_misroute_count: {manifest['critical_guard_misroute_count']}",
        f"- critical_count_sum: {manifest['critical_count_sum']}",
        "",
        "Test-provider results validate orchestration and safety contracts only;",
        "they never declare production readiness.",
    ]
    return "\n".join(lines) + "\n"


def _rate(rows: Sequence[Mapping[str, Any]], key: str) -> float:
    if not rows:
        return 0.0
    return round(sum(bool(row[key]) for row in rows) / len(rows), 6)


__all__ = [
    "TWO_PASS_BENCHMARK_SCHEMA_VERSION",
    "TwoPassPlannerBenchmarkAudit",
    "evaluate_two_pass_planner_benchmark",
    "render_two_pass_benchmark_report",
    "write_two_pass_planner_benchmark",
]
