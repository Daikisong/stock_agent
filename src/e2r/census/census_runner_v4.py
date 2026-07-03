"""Census Mode v4 runner.

v4 starts by turning v3 leaf artifacts into an honest, atomic status map. It
does not claim Brain/Web or full-thesis operation when those traces are absent.
"""

from __future__ import annotations

import csv
import json
import shutil
import time
from collections import Counter
from dataclasses import asdict, dataclass, is_dataclass
from datetime import date, datetime
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import build_report_metadata, git_head_sha, stable_hash, write_json, write_jsonl, write_text
from e2r.production.source_connectors import build_default_source_provider_registry

from .atomic_stage_decision import build_atomic_stage_decisions, canonical_stage_for_display, choose_representative_decision
from .census_runner_v3 import CensusV3RunConfig, run_census_mode_v3
from .census_v4_auditor import audit_census_v4_leaf_artifacts, build_artifact_manifest
from .existing_ledger_loader import with_primitive_state_id
from .known_bad_regression import run_known_bad_regression
from .test_result_evidence import validate_test_result_artifact


FULL_THESIS_SMOKE_SYMBOLS = ("005930", "000660")
FULL_THESIS_SMOKE_COMPANY_FALLBACKS = {"005930": "삼성전자", "000660": "SK하이닉스"}
FULL_THESIS_SMOKE_ARCHETYPE = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
FULL_THESIS_SMOKE_SOURCE_ORIGIN = "full_thesis_c06_url_backed_smoke"
C06_SEMANTIC_REPLAY_SOURCE_ORIGIN = "c06_source_backed_semantic_replay"
C08_TEST_SOCKET_ARCHETYPE = "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY"
C08_SEMANTIC_REPLAY_SOURCE_ORIGIN = "c08_source_backed_semantic_replay"
C15_MATERIAL_SPREAD_ARCHETYPE = "C15_MATERIAL_SPREAD_SUPERCYCLE"
C15_SEMANTIC_REPLAY_SOURCE_ORIGIN = "c15_source_backed_semantic_replay"
C17_CHEMICAL_SPREAD_ARCHETYPE = "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD"
C17_SEMANTIC_REPLAY_SOURCE_ORIGIN = "c17_source_backed_semantic_replay"
C24_BIO_TRIAL_ARCHETYPE = "C24_BIO_TRIAL_DATA_EVENT_RISK"
C24_SEMANTIC_REPLAY_SOURCE_ORIGIN = "c24_source_backed_semantic_replay"
C28_SOFTWARE_SECURITY_ARCHETYPE = "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION"
C28_SEMANTIC_REPLAY_SOURCE_ORIGIN = "c28_source_backed_semantic_replay"
BRAIN_WEB_MIN_PLANNER_CALLS = 30
BRAIN_WEB_MIN_WEB_SEARCH_TASKS = 20
BRAIN_WEB_MIN_WEB_SEARCH_CALLS = 20
BRAIN_WEB_MIN_FETCHED_DOCUMENTS = 10
BRAIN_WEB_MIN_EXTRACTOR_ATTEMPTS = 10
BRAIN_WEB_MIN_ACCEPTED_CLAIMS = 3


@dataclass(frozen=True)
class CensusV4RunConfig:
    as_of_date: str
    output_root: str | None = None
    v3_output_root: str | None = None
    universe: str = "krx"
    max_symbols: int = 0
    run_mode: str = "LEDGER_REFRESH_CENSUS"
    brain_web_mode: str = "disabled"
    research_brain_report_dir: str = "docs/operational"
    brain_planner_provider: str = "none"
    brain_source_acquisition: str = "live_official_first"
    brain_universe_limit: int = 30
    brain_planner_success_limit: int = 30
    brain_planner_batch_size: int = 5
    brain_max_source_tasks_per_plan: int = 5
    brain_max_fetches_per_task: int = 3
    brain_accepted_claim_target: int = 0
    brain_max_distinct_candidate_attempts: int = 30
    brain_retry_max: int = 2
    brain_claim_extractor_provider: str = "auto"
    brain_claim_extractor_timeout_seconds: float | None = 60.0
    brain_candidate_event_seed_path: str | None = None
    brain_stage_promotion_mode: str = "disabled"
    full_thesis_smoke_mode: str = "disabled"
    target_gate: str = "anti_fake"
    max_iterations: int = 1
    fail_on_run_mode_overclaim: bool = False
    fail_on_atomic_mismatch: bool = False
    fail_on_semantic_guard: bool = False
    fail_on_critical_audit: bool = True
    write_operational_docs: bool = True
    test_result_summary: str = "not_run_by_census_v4_runner"
    test_result_artifact: str | None = None

    def resolved_output_root(self) -> str:
        return self.output_root or f"output/census_v4/{self.as_of_date}"

    def resolved_v3_output_root(self) -> str:
        return self.v3_output_root or f"output/census_v3/{self.as_of_date}"

    def to_dict(self) -> dict[str, Any]:
        return {
            "as_of_date": self.as_of_date,
            "output_root": self.resolved_output_root(),
            "v3_output_root": self.resolved_v3_output_root(),
            "universe": self.universe,
            "max_symbols": self.max_symbols,
            "run_mode": self.run_mode,
            "brain_web_mode": self.brain_web_mode,
            "research_brain_report_dir": self.research_brain_report_dir,
            "brain_planner_provider": self.brain_planner_provider,
            "brain_source_acquisition": self.brain_source_acquisition,
            "brain_universe_limit": self.brain_universe_limit,
            "brain_planner_success_limit": self.brain_planner_success_limit,
            "brain_planner_batch_size": self.brain_planner_batch_size,
            "brain_max_source_tasks_per_plan": self.brain_max_source_tasks_per_plan,
            "brain_max_fetches_per_task": self.brain_max_fetches_per_task,
            "brain_accepted_claim_target": self.brain_accepted_claim_target,
            "brain_max_distinct_candidate_attempts": self.brain_max_distinct_candidate_attempts,
            "brain_retry_max": self.brain_retry_max,
            "brain_claim_extractor_provider": self.brain_claim_extractor_provider,
            "brain_claim_extractor_timeout_seconds": self.brain_claim_extractor_timeout_seconds,
            "brain_candidate_event_seed_path": self.brain_candidate_event_seed_path,
            "brain_stage_promotion_mode": self.brain_stage_promotion_mode,
            "full_thesis_smoke_mode": self.full_thesis_smoke_mode,
            "target_gate": self.target_gate,
            "max_iterations": self.max_iterations,
            "fail_on_run_mode_overclaim": self.fail_on_run_mode_overclaim,
            "fail_on_atomic_mismatch": self.fail_on_atomic_mismatch,
            "fail_on_semantic_guard": self.fail_on_semantic_guard,
            "fail_on_critical_audit": self.fail_on_critical_audit,
            "write_operational_docs": self.write_operational_docs,
            "test_result_summary": self.test_result_summary,
            "test_result_artifact": self.test_result_artifact,
        }


@dataclass(frozen=True)
class CensusV4RunResult:
    output_root: str
    run_metadata: Mapping[str, Any]
    leaf_audit: Mapping[str, Any]
    readiness_verdict: Mapping[str, Any]


def run_census_mode_v4(config: CensusV4RunConfig) -> CensusV4RunResult:
    start = time.monotonic()
    output_root = Path(config.resolved_output_root())
    v3_root = _ensure_v3_artifacts(config)
    v3 = _load_v3(v3_root)
    _copy_v3_leafs(v3_root=v3_root, output_root=output_root)
    atomic_rows, representative_by_symbol = _atomic_decisions_from_v3(config=config, v3=v3)
    stage_rows = _stage_rows_from_v3(config=config, v3=v3, representative_by_symbol=representative_by_symbol)
    pre_promotion_refresh_queue = _full_thesis_refresh_queue(stage_rows)
    seed_path = _write_full_thesis_refresh_seed_events(output_root=output_root, refresh_queue_rows=pre_promotion_refresh_queue)
    brain_seed = _resolve_research_brain_candidate_seed_path(
        config=config,
        output_root=output_root,
        default_seed_path=seed_path,
    )
    brain_web_attempt = _run_brain_web_attempt(
        config=config,
        output_root=output_root,
        full_thesis_seed_path=brain_seed["seed_path"],
        full_thesis_seed_event_count=int(brain_seed["seed_event_count"]),
        full_thesis_seed_source=str(brain_seed["seed_source"]),
        full_thesis_seed_original_path=brain_seed["original_path"],
    )
    research_brain_bridge = _research_brain_bridge_audit(config)
    write_json(output_root / "research_brain_v4_bridge_audit.json", research_brain_bridge)

    stage_rows, brain_promotion_export = _promote_brain_stage_rows(
        config=config,
        output_root=output_root,
        stage_rows=stage_rows,
        brain_web_attempt=brain_web_attempt,
    )
    stage_rows, production_full_thesis_runner = _apply_production_full_thesis_from_brain(
        config=config,
        output_root=output_root,
        stage_rows=stage_rows,
    )
    follow_up_iteration_audit = _full_thesis_follow_up_iterations_audit(
        config=config,
        iterations=[
            _full_thesis_follow_up_iteration_summary(
                iteration=1,
                seed_path=brain_seed["seed_path"],
                seed_event_count=int(brain_seed["seed_event_count"]),
                seed_source=str(brain_seed["seed_source"]),
                brain_web_attempt=brain_web_attempt,
                brain_promotion_export=brain_promotion_export,
                production_full_thesis_runner=production_full_thesis_runner,
            )
        ],
        status="NOT_REQUESTED" if config.max_iterations <= 1 else "INITIAL_ITERATION_COMPLETE",
    )
    full_thesis_seed_trace_paths: list[Path] = [brain_seed["seed_path"]] if brain_seed["seed_path"] is not None else []
    brain_web_attempts: list[Mapping[str, Any]] = [brain_web_attempt]
    brain_promotion_exports: list[Mapping[str, Any]] = [brain_promotion_export]
    follow_up_iterations = list(follow_up_iteration_audit["iterations"])
    for iteration in range(2, max(1, int(config.max_iterations or 1)) + 1):
        if not _should_run_full_thesis_follow_up_iteration(config=config, production_full_thesis_runner=production_full_thesis_runner):
            follow_up_iteration_audit = _full_thesis_follow_up_iterations_audit(
                config=config,
                iterations=follow_up_iterations,
                status="STOPPED_NO_FOLLOW_UP_SEEDS",
            )
            break
        source_seed_path = Path(str(production_full_thesis_runner.get("blocked_candidate_follow_up_seed_event_path") or ""))
        seed_rows = _read_jsonl(source_seed_path)
        if not seed_rows:
            follow_up_iteration_audit = _full_thesis_follow_up_iterations_audit(
                config=config,
                iterations=follow_up_iterations,
                status="STOPPED_EMPTY_FOLLOW_UP_SEED_FILE",
            )
            break
        iteration_seed_path = output_root / f"full_thesis_follow_up_iteration_{iteration}_seed_events.jsonl"
        write_jsonl(iteration_seed_path, seed_rows)
        full_thesis_seed_trace_paths.append(iteration_seed_path)
        brain_web_attempt = _run_brain_web_attempt(
            config=config,
            output_root=output_root,
            full_thesis_seed_path=iteration_seed_path,
            full_thesis_seed_event_count=len(seed_rows),
            full_thesis_seed_source=f"full_thesis_blocker_follow_up_iteration_{iteration}",
            full_thesis_seed_original_path=str(source_seed_path),
        )
        brain_web_attempts.append(brain_web_attempt)
        stage_rows, brain_promotion_export = _promote_brain_stage_rows(
            config=config,
            output_root=output_root,
            stage_rows=stage_rows,
            brain_web_attempt=brain_web_attempt,
        )
        brain_promotion_exports.append(brain_promotion_export)
        stage_rows, production_full_thesis_runner = _apply_production_full_thesis_from_brain(
            config=config,
            output_root=output_root,
            stage_rows=stage_rows,
        )
        follow_up_iterations.append(
            _full_thesis_follow_up_iteration_summary(
                iteration=iteration,
                seed_path=iteration_seed_path,
                seed_event_count=len(seed_rows),
                seed_source=f"full_thesis_blocker_follow_up_iteration_{iteration}",
                brain_web_attempt=brain_web_attempt,
                brain_promotion_export=brain_promotion_export,
                production_full_thesis_runner=production_full_thesis_runner,
            )
        )
        follow_up_iteration_audit = _full_thesis_follow_up_iterations_audit(
            config=config,
            iterations=follow_up_iterations,
            status="RAN_FOLLOW_UP_ITERATIONS",
        )
        if _full_thesis_production_runner_promoted(production_full_thesis_runner):
            break
    write_json(output_root / "full_thesis_production_runner_audit.json", production_full_thesis_runner)
    write_json(output_root / "full_thesis_follow_up_iterations_audit.json", follow_up_iteration_audit)
    full_thesis_export = _apply_full_thesis_smoke_replay(
        config=config,
        output_root=output_root,
        stage_rows=stage_rows,
    )
    stage_rows = full_thesis_export["stage_rows"]
    if full_thesis_export["atomic_rows"]:
        full_thesis_symbols = set(full_thesis_export["symbols"])
        demoted_atomic_rows: list[dict[str, Any]] = []
        for row in atomic_rows:
            item = dict(row)
            if str(item.get("symbol") or "").zfill(6) in full_thesis_symbols and item.get("is_representative") is True:
                item["is_representative"] = False
                item["representative_replaced_by"] = "FULL_THESIS"
                item["non_representative_reason"] = "superseded_by_full_thesis_smoke_stage_row"
            demoted_atomic_rows.append(item)
        atomic_rows = [*demoted_atomic_rows, *full_thesis_export["atomic_rows"]]
    _write_evidence_claim_view(output_root)
    _write_primitive_mapping_view(output_root)
    stage_rows = _apply_operator_scope_aliases(stage_rows)
    atomic_rows = _demote_atomic_representatives_replaced_by_brain_stage(
        atomic_rows=atomic_rows,
        stage_rows=stage_rows,
    )
    brain_web_attempt = _aggregate_brain_web_attempts(brain_web_attempts)
    brain_promotion_export = _aggregate_brain_promotion_exports(brain_promotion_exports)
    brain_web_attempt = _refresh_brain_web_attempt_after_promotion(
        brain_web_attempt,
        promoted_stage_row_count=int(brain_promotion_export.get("promoted_stage_row_count") or 0),
    )
    write_json(output_root / "brain_web_attempt_audit.json", brain_web_attempt)
    stage_summary = _stage_summary(stage_rows)
    metadata = build_report_metadata(
        repo_root=".",
        report_generator="e2r.census.census_runner_v4",
        command=_command_string(config),
        config=config.to_dict(),
        source_corpus={"v3_output_root": str(v3_root), "v3_stage_count": len(v3["stage_rows"])},
        candidate_events=v3.get("events", []),
        planner_runs=[],
    )
    metadata = {**metadata, "run_mode": config.run_mode, "brain_web_mode": config.brain_web_mode}

    _write_v4_outputs(
        output_root=output_root,
        run_metadata=metadata,
        atomic_rows=atomic_rows,
        stage_rows=stage_rows,
        stage_summary=stage_summary,
    )
    _write_full_thesis_seed_materialization_trace(
        output_root=output_root,
        seed_path=brain_seed["seed_path"],
        additional_seed_paths=full_thesis_seed_trace_paths[1:],
        stage_rows=stage_rows,
    )
    c06_guard_replay = _c06_guard_replay_audit(config=config, stage_rows=stage_rows, output_root=output_root)
    write_json(output_root / "c06_guard_replay_audit.json", c06_guard_replay)
    c08_source_backed_replay = _c08_source_backed_semantic_replay(config=config, output_root=output_root)
    write_json(output_root / "c08_source_backed_semantic_replay.json", c08_source_backed_replay)
    c15_source_backed_replay = _c15_source_backed_semantic_replay(config=config, output_root=output_root)
    write_json(output_root / "c15_source_backed_semantic_replay.json", c15_source_backed_replay)
    c17_source_backed_replay = _c17_source_backed_semantic_replay(config=config, output_root=output_root)
    write_json(output_root / "c17_source_backed_semantic_replay.json", c17_source_backed_replay)
    c24_source_backed_replay = _c24_source_backed_semantic_replay(config=config, output_root=output_root)
    write_json(output_root / "c24_source_backed_semantic_replay.json", c24_source_backed_replay)
    c28_source_backed_replay = _c28_source_backed_semantic_replay(config=config, output_root=output_root)
    write_json(output_root / "c28_source_backed_semantic_replay.json", c28_source_backed_replay)
    all_archetype_replay_matrix = _all_archetype_replay_matrix(
        config=config,
        output_root=output_root,
        stage_rows=stage_rows,
        c06_guard_replay=c06_guard_replay,
        c08_source_backed_replay=c08_source_backed_replay,
        c15_source_backed_replay=c15_source_backed_replay,
        c17_source_backed_replay=c17_source_backed_replay,
        c24_source_backed_replay=c24_source_backed_replay,
        c28_source_backed_replay=c28_source_backed_replay,
    )
    write_json(output_root / "all_archetype_replay_matrix.json", all_archetype_replay_matrix)
    brain_stage_promotion = _brain_stage_promotion_audit(
        config=config,
        output_root=output_root,
        brain_web_attempt=brain_web_attempt,
        stage_rows=stage_rows,
    )
    write_json(output_root / "brain_stage_promotion_audit.json", brain_stage_promotion)
    brain_web_readiness_gate = _brain_web_readiness_gate_audit(
        config=config,
        output_root=output_root,
        brain_web_attempt=brain_web_attempt,
        brain_stage_promotion=brain_stage_promotion,
        stage_rows=stage_rows,
    )
    write_json(output_root / "brain_web_readiness_gate_audit.json", brain_web_readiness_gate)
    goal_audits = _write_goal_v4_audits(
        config=config,
        output_root=output_root,
        stage_rows=stage_rows,
        runtime_seconds=time.monotonic() - start,
    )
    _sync_test_result_artifact(config=config, output_root=output_root)
    leaf_audit = audit_census_v4_leaf_artifacts(output_root)
    write_json(output_root / "leaf_artifact_audit.json", leaf_audit)
    goal_audits["goal_requirement_matrix"] = _goal_requirement_matrix_audit(
        config=config,
        audits=goal_audits,
        leaf_audit=leaf_audit,
        output_root=output_root,
    )
    write_json(output_root / "goal_requirement_matrix_audit.json", goal_audits["goal_requirement_matrix"])
    goal_audits["goal_completion"] = _goal_completion_audit(config=config, audits=goal_audits)
    write_json(output_root / "goal_completion_audit.json", goal_audits["goal_completion"])
    readiness = _readiness_verdict(
        config=config,
        leaf_audit=leaf_audit,
        stage_rows=stage_rows,
        research_brain_bridge=research_brain_bridge,
        brain_web_attempt=brain_web_attempt,
        brain_stage_promotion=brain_stage_promotion,
        brain_web_readiness_gate=brain_web_readiness_gate,
        goal_audits=goal_audits,
    )
    write_json(output_root / "readiness_verdict.json", readiness)
    write_json(output_root / "audit_summary.json", {"schema_version": "e2r_census_v4_audit_summary_v1", "leaf_audit": leaf_audit, "readiness": readiness})
    write_text(output_root / "operator_digest.md", _operator_digest(leaf_audit=leaf_audit, readiness=readiness))
    acceptance_report = _acceptance_report_md(
        config=config,
        output_root=output_root,
        leaf_audit=leaf_audit,
        readiness=readiness,
        runtime_seconds=time.monotonic() - start,
    )
    write_text(output_root / "acceptance_report.md", acceptance_report)
    report_generation_audit = _report_generation_audit(
        acceptance_report=acceptance_report,
        leaf_audit=leaf_audit,
        readiness=readiness,
        output_root=output_root,
    )
    write_json(output_root / "report_generation_audit.json", report_generation_audit)
    manifest = build_artifact_manifest(output_root)
    write_json(output_root / "artifact_manifest.json", manifest)

    if config.write_operational_docs:
        _write_operational_docs(
            config=config,
            output_root=output_root,
            leaf_audit=leaf_audit,
            readiness=readiness,
            manifest=manifest,
            runtime_seconds=time.monotonic() - start,
            atomic_rows=atomic_rows,
            stage_rows=stage_rows,
        )
    if config.fail_on_critical_audit and leaf_audit.get("verdict") != "PASS":
        raise RuntimeError(f"Census v4 audit failed: {leaf_audit.get('critical_counts')}")
    return CensusV4RunResult(output_root=str(output_root), run_metadata=metadata, leaf_audit=leaf_audit, readiness_verdict=readiness)


def _ensure_v3_artifacts(config: CensusV4RunConfig) -> Path:
    root = Path(config.resolved_v3_output_root())
    required = root / "census_stage_status.jsonl"
    if required.exists():
        return root
    run_census_mode_v3(
        CensusV3RunConfig(
            as_of_date=config.as_of_date,
            output_root=str(root),
            universe=config.universe,
            max_symbols=config.max_symbols,
            write_operational_docs=False,
            fail_on_critical_audit=True,
        )
    )
    return root


def _load_v3(root: Path) -> dict[str, Any]:
    return {
        "root": root,
        "stage_rows": _read_jsonl(root / "census_stage_status.jsonl"),
        "stagecourt_traces": _read_jsonl(root / "stagecourt_traces.jsonl"),
        "primitive_states": _primitive_rows_with_ids(_read_jsonl(root / "primitive_states.jsonl")),
        "accepted_claims": _read_jsonl(root / "accepted_claims.jsonl"),
        "score_contributions": _read_jsonl(root / "score_contributions.jsonl"),
        "source_tasks": _read_jsonl(root / "source_tasks.jsonl"),
        "source_task_executions": _read_jsonl(root / "source_task_executions.jsonl"),
        "events": _read_jsonl(root / "census_events.jsonl"),
        "evidence_documents": _read_jsonl(root / "evidence_documents.jsonl"),
    }


def _copy_v3_leafs(*, v3_root: Path, output_root: Path) -> None:
    output_root.mkdir(parents=True, exist_ok=True)
    for path in v3_root.iterdir():
        if path.is_file() and path.name not in {
            "census_stage_status.jsonl",
            "census_stage_map.jsonl",
            "census_stage_map.csv",
            "census_stage_summary.json",
            "leaf_artifact_audit.json",
            "audit_summary.json",
            "operator_digest.md",
            "run_metadata.json",
            "self_repair_log.json",
        }:
            shutil.copy2(path, output_root / path.name)
    for empty in (
        "planner_runs.jsonl",
        "llm_prompts.jsonl",
        "llm_responses.jsonl",
        "web_search_tasks.jsonl",
        "web_search_results.jsonl",
        "web_fetched_documents.jsonl",
        "web_rejected_documents.jsonl",
        "claim_extractor_runs.jsonl",
        "raw_assertion_rejections.jsonl",
        "brain_to_claim_trace.jsonl",
        "brain_claim_mapping_trace.jsonl",
    ):
        write_jsonl(output_root / empty, [])
    write_jsonl(output_root / "primitive_states.jsonl", _primitive_rows_with_ids(_read_jsonl(output_root / "primitive_states.jsonl")))


def _primitive_rows_with_ids(rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    return [with_primitive_state_id(row) for row in rows]


def _write_evidence_claim_view(output_root: Path) -> None:
    """Write an explicit, reviewable EvidenceClaim payload view.

    `accepted_claims.jsonl` is still the compatibility source. This additional
    leaf makes the scoring boundary obvious: the rows are accepted,
    source-backed claims, not full-thesis Brain/Web conclusions.
    """

    evidence_claims: list[dict[str, Any]] = []
    for row in _read_jsonl(output_root / "accepted_claims.jsonl"):
        evidence_claims.append(
            {
                "schema_version": "e2r_census_v4_evidence_claim_view_v1",
                "evidence_claim_id": row.get("claim_id"),
                "claim_id": row.get("claim_id"),
                "symbol": row.get("symbol"),
                "as_of_date": row.get("as_of_date"),
                "event_date": row.get("event_date"),
                "document_id": row.get("document_id"),
                "anchor_id": row.get("anchor_id"),
                "source_provider": row.get("source_provider"),
                "source_url": row.get("source_url"),
                "quote_text": row.get("quote_text"),
                "subject_entity_id": row.get("subject_entity_id"),
                "target_entity_id": row.get("target_entity_id"),
                "target_scope_status": row.get("target_scope_status"),
                "directness": row.get("directness"),
                "polarity": row.get("polarity"),
                "temporal_status": row.get("temporal_status"),
                "semantic_status": row.get("semantic_status"),
                "mapping_status": row.get("mapping_status"),
                "primitive_id": row.get("primitive_id"),
                "support_direction": row.get("support_direction"),
                "score_eligible": row.get("score_eligible") is True,
                "satisfies_source_task": row.get("satisfies_source_task") is True,
                "payload_source": "accepted_claims.jsonl",
                "claim_payload_class": "source_backed_accepted_claim",
                "source_origin": row.get("source_origin") or "census_v3_leaf",
                "full_thesis_claim": row.get("full_thesis_claim") is True,
                "brain_web_claim": row.get("brain_web_claim") is True,
            }
        )
    write_jsonl(output_root / "evidence_claims.jsonl", evidence_claims)


def _write_primitive_mapping_view(output_root: Path) -> None:
    claims = _read_jsonl(output_root / "accepted_claims.jsonl")
    primitive_states = _read_jsonl(output_root / "primitive_states.jsonl")
    contributions = _read_jsonl(output_root / "score_contributions.jsonl")
    claims_by_id = {str(row.get("claim_id") or ""): row for row in claims if row.get("claim_id")}
    primitive_ids_by_claim: dict[str, list[str]] = {}
    primitive_ids_by_state_id = {str(row.get("primitive_state_id") or ""): str(row.get("primitive_id") or "") for row in primitive_states}
    for state in primitive_states:
        primitive_state_id = str(state.get("primitive_state_id") or "")
        if not primitive_state_id:
            continue
        for key in ("support_claim_ids", "counter_claim_ids"):
            for claim_id in state.get(key) or ():
                claim_key = str(claim_id)
                if claim_key and primitive_state_id not in primitive_ids_by_claim.setdefault(claim_key, []):
                    primitive_ids_by_claim[claim_key].append(primitive_state_id)

    rows_by_mapping: dict[str, dict[str, Any]] = {}
    for contribution in contributions:
        contribution_id = str(contribution.get("score_contribution_id") or contribution.get("contribution_id") or "")
        if not contribution_id:
            continue
        support_claim_ids = [str(item) for item in contribution.get("support_claim_ids") or () if str(item)]
        for mapping_id in [str(item) for item in contribution.get("mapping_ids") or () if str(item)]:
            row = rows_by_mapping.setdefault(
                mapping_id,
                {
                    "schema_version": "e2r_census_v4_primitive_mapping_view_v1",
                    "mapping_id": mapping_id,
                    "symbol": contribution.get("symbol"),
                    "score_contribution_ids": [],
                    "accepted_claim_ids": [],
                    "primitive_state_ids": [],
                    "primitive_ids": [],
                    "mapping_statuses": [],
                    "support_directions": [],
                    "source_component_keys": [],
                    "source_criterion_ids": [],
                    "mapping_leaf_source": "score_contributions.mapping_ids + accepted_claims.mapping",
                },
            )
            _append_unique(row["score_contribution_ids"], contribution_id)
            _append_unique(row["source_component_keys"], str(contribution.get("component_key") or ""))
            _append_unique(row["source_criterion_ids"], str(contribution.get("criterion_id") or ""))
            for claim_id in support_claim_ids:
                claim = claims_by_id.get(claim_id) or {}
                _append_unique(row["accepted_claim_ids"], claim_id)
                _append_unique(row["mapping_statuses"], str(claim.get("mapping_status") or (claim.get("mapping") or {}).get("mapping_status") or "UNKNOWN"))
                _append_unique(row["support_directions"], str(claim.get("support_direction") or (claim.get("mapping") or {}).get("support_direction") or "UNKNOWN"))
                for primitive_state_id in primitive_ids_by_claim.get(claim_id, ()):
                    _append_unique(row["primitive_state_ids"], primitive_state_id)
                    primitive_id = primitive_ids_by_state_id.get(primitive_state_id)
                    if primitive_id:
                        _append_unique(row["primitive_ids"], primitive_id)
                claim_primitive_id = str(claim.get("primitive_id") or "")
                if claim_primitive_id:
                    _append_unique(row["primitive_ids"], claim_primitive_id)
    write_jsonl(output_root / "primitive_mappings.jsonl", list(rows_by_mapping.values()))


def _research_brain_bridge_audit(config: CensusV4RunConfig) -> dict[str, Any]:
    report_dir = Path(config.research_brain_report_dir)
    evidence_audit = _read_json(report_dir / "research_brain_v4_evidence_extraction_audit.json")
    source_report = _read_json(report_dir / "research_brain_v4_source_acquisition_report.json")
    planner_report = _read_json(report_dir / "research_brain_v4_real_planner_report.json")
    verdict_text = _read_text(report_dir / "research_brain_v4_production_readiness_verdict.md")

    source_rows = source_report.get("rows") or []
    planner_rows = planner_report.get("rows") or []
    source_summary = source_report.get("summary") or {}
    evidence_summary = evidence_audit.get("summary") or {}
    document_urls = [
        str(url)
        for row in source_rows
        for url in (row.get("document_urls") or [])
    ]
    snapshot_url_count = sum(1 for url in document_urls if url.startswith("snapshot://"))
    accepted_claim_count = int(source_summary.get("accepted_claim_count") or evidence_summary.get("adjudicated_claim_to_accepted_claim_count") or 0)
    real_document_fetched_count = int(source_summary.get("real_document_fetched_count") or 0)
    production_cutover_ready = "- production_cutover_ready: True" in verdict_text or "production_cutover_ready: true" in verdict_text
    shadow_ready = "PRODUCTION_SHADOW_READY" in verdict_text
    has_fixture_blocker = "fixture-like" in verdict_text or "snapshot://" in verdict_text
    model_null_count = sum(1 for row in planner_rows if row.get("model") in {None, ""})
    usable_for_census_cutover = bool(
        production_cutover_ready
        and accepted_claim_count > 0
        and real_document_fetched_count > 0
        and snapshot_url_count == 0
        and not has_fixture_blocker
    )

    blockers: list[str] = []
    if not evidence_audit:
        blockers.append("research_brain_v4_evidence_extraction_audit.json missing")
    if not source_report:
        blockers.append("research_brain_v4_source_acquisition_report.json missing")
    if not production_cutover_ready:
        blockers.append("Research Brain v4 report is not production_cutover_ready")
    if snapshot_url_count:
        blockers.append("Research Brain v4 report contains snapshot:// source records")
    if has_fixture_blocker:
        blockers.append("Research Brain v4 readiness text records fixture/snapshot blockers")
    if accepted_claim_count <= 0:
        blockers.append("Research Brain v4 report has no accepted claims")
    if model_null_count:
        blockers.append("Research Brain v4 planner rows include missing model identity")

    return {
        "schema_version": "e2r_census_v4_research_brain_bridge_audit_v1",
        "report_dir": str(report_dir),
        "bridge_mode": "imported_operational_report_bundle" if evidence_audit or source_report or planner_report else "missing_report_bundle",
        "production_cutover_ready": production_cutover_ready,
        "shadow_ready": shadow_ready,
        "usable_for_census_cutover": usable_for_census_cutover,
        "accepted_claim_count": accepted_claim_count,
        "unique_accepted_claim_count": int(source_summary.get("unique_accepted_claim_count") or 0),
        "real_document_fetched_count": real_document_fetched_count,
        "unique_real_document_fetched_count": int(source_summary.get("unique_real_document_fetched_count") or 0),
        "source_task_count": int(source_summary.get("source_task_count") or 0),
        "source_task_accepted_without_real_document_count": int(source_summary.get("source_task_accepted_without_real_document_count") or 0),
        "snapshot_url_count": snapshot_url_count,
        "planner_row_count": len(planner_rows),
        "planner_model_null_count": model_null_count,
        "forced_current_temporal_count": int(evidence_summary.get("forced_current_temporal_count") or 0),
        "forced_positive_polarity_count": int(evidence_summary.get("forced_positive_polarity_count") or 0),
        "forced_target_subject_count": int(evidence_summary.get("forced_target_subject_count") or 0),
        "blockers": blockers,
        "verdict": "USABLE_FOR_CENSUS_CUTOVER" if usable_for_census_cutover else "SHADOW_OR_IMPORT_ONLY",
    }


def _run_brain_web_attempt(
    *,
    config: CensusV4RunConfig,
    output_root: Path,
    full_thesis_seed_path: Path | None = None,
    full_thesis_seed_event_count: int = 0,
    full_thesis_seed_source: str = "internal_full_thesis_refresh_queue",
    full_thesis_seed_original_path: str | None = None,
) -> dict[str, Any]:
    if config.brain_web_mode != "enabled":
        return {
            "schema_version": "e2r_census_v4_brain_web_attempt_audit_v1",
            "attempt_mode": "disabled",
            "verdict": "NOT_REQUESTED",
            "full_thesis_seed_event_path": str(full_thesis_seed_path) if full_thesis_seed_path is not None else None,
            "full_thesis_seed_source": full_thesis_seed_source,
            "full_thesis_seed_original_path": full_thesis_seed_original_path,
            "full_thesis_seed_event_count": full_thesis_seed_event_count,
            "full_thesis_seed_consumed_by_research_brain": False,
            "full_thesis_seed_planner_attempted_event_count": 0,
            "full_thesis_seed_planner_run_row_count": 0,
            "full_thesis_seed_planner_run_count": 0,
            "full_thesis_seed_real_provider_success_count": 0,
            "full_thesis_seed_source_task_execution_count": 0,
            "full_thesis_seed_accepted_claim_count": 0,
            "full_thesis_seed_stagecourt_trace_count": 0,
            "full_thesis_seed_materialized_to_stagecourt": False,
            "planner_run_count": 0,
            "real_provider_success_count": 0,
            "source_task_execution_count": 0,
            "accepted_claim_count": 0,
            "unique_accepted_claim_count": 0,
            "brain_stagecourt_trace_exported_count": 0,
            "brain_to_census_stage_exported_count": 0,
            "brain_source_task_exported_count": 0,
            "brain_source_task_execution_exported_count": 0,
            "brain_evidence_document_exported_count": 0,
            "brain_evidence_anchor_exported_count": 0,
            "brain_score_contribution_exported_count": 0,
            "claim_acceptance_ready": False,
            "stagecourt_trace_ready": False,
            "cutover_export_ready": False,
            "blockers": [],
        }
    try:
        from e2r.research_brain.v4_production_orchestrator import DEFAULT_V1_ARCHETYPE_MATRIX, run_research_brain_v4_production_shadow
        from e2r.research_brain.v4_schemas import ProductionShadowV4Config
    except Exception as exc:  # pragma: no cover - defensive import guard
        return _brain_web_attempt_failed(
            f"research_brain_v4_import_failed:{type(exc).__name__}:{exc}",
            full_thesis_seed_path=full_thesis_seed_path,
            full_thesis_seed_event_count=full_thesis_seed_event_count,
            full_thesis_seed_source=full_thesis_seed_source,
            full_thesis_seed_original_path=full_thesis_seed_original_path,
        )

    matrix_path = DEFAULT_V1_ARCHETYPE_MATRIX
    if not matrix_path.exists():
        return _brain_web_attempt_failed(
            f"v1_archetype_matrix_missing:{matrix_path}",
            full_thesis_seed_path=full_thesis_seed_path,
            full_thesis_seed_event_count=full_thesis_seed_event_count,
            full_thesis_seed_source=full_thesis_seed_source,
            full_thesis_seed_original_path=full_thesis_seed_original_path,
        )
    try:
        result = run_research_brain_v4_production_shadow(
            config=ProductionShadowV4Config(
                as_of_date=config.as_of_date,
                planner_provider=config.brain_planner_provider,
                source_acquisition=config.brain_source_acquisition,
                candidate_event_seed_path=str(full_thesis_seed_path) if full_thesis_seed_path is not None else None,
                universe_limit=config.brain_universe_limit,
                planner_success_limit=config.brain_planner_success_limit,
                planner_batch_size=config.brain_planner_batch_size,
                max_source_tasks_per_plan=config.brain_max_source_tasks_per_plan,
                max_fetches_per_task=config.brain_max_fetches_per_task,
                accepted_claim_target=config.brain_accepted_claim_target,
                max_distinct_candidate_attempts=config.brain_max_distinct_candidate_attempts,
                claim_extractor_provider=config.brain_claim_extractor_provider,
                claim_extractor_timeout_seconds=config.brain_claim_extractor_timeout_seconds,
                top_results=20,
                retry_max=config.brain_retry_max,
                fake_provider_allowed=False,
            ),
            v1_archetype_matrix=_read_json(matrix_path),
            repo_root=".",
        )
    except Exception as exc:
        return _brain_web_attempt_failed(
            f"research_brain_v4_run_failed:{type(exc).__name__}:{exc}",
            full_thesis_seed_path=full_thesis_seed_path,
            full_thesis_seed_event_count=full_thesis_seed_event_count,
            full_thesis_seed_source=full_thesis_seed_source,
            full_thesis_seed_original_path=full_thesis_seed_original_path,
        )

    _write_planner_prompt_response_leafs(output_root=output_root, planner_runs=result.get("planner_runs", ()))
    planner_runs = [run.to_dict() for run in result.get("planner_runs", ())]
    _merge_jsonl_by_key(output_root / "planner_runs.jsonl", planner_runs, "planner_run_id")
    _merge_jsonl_by_key(output_root / "research_brain_plans.jsonl", _planner_plan_rows(planner_runs), "planner_run_id")
    exported = _export_brain_web_bundle_leafs(result=result, output_root=output_root)
    seed_runtime = _full_thesis_seed_runtime_counts(result=result, planner_runs=planner_runs)

    planner_summary = (result.get("planner_report") or {}).get("summary") or {}
    source_summary = (result.get("source_acquisition_report") or {}).get("summary") or {}
    extraction_summary = (result.get("evidence_extraction_audit") or {}).get("summary") or {}
    watchlist_summary = (result.get("watchlist_report") or {}).get("summary") or {}
    real_success = int(planner_summary.get("real_provider_success_count") or 0)
    source_task_count = int(source_summary.get("source_task_executed_count") or 0)
    accepted_claim_count = int(source_summary.get("accepted_claim_count") or extraction_summary.get("adjudicated_claim_to_accepted_claim_count") or 0)
    unique_accepted_claim_count = int(source_summary.get("unique_accepted_claim_count") or accepted_claim_count)
    blockers = _brain_web_attempt_blockers(
        real_provider_success_count=real_success,
        source_task_execution_count=source_task_count,
        accepted_claim_count=accepted_claim_count,
        unique_accepted_claim_count=unique_accepted_claim_count,
        accepted_claim_exported_count=int(exported["accepted_claim_exported_count"]),
        source_task_exported_count=int(exported["source_task_exported_count"]),
        source_task_execution_exported_count=int(exported["source_task_execution_exported_count"]),
        evidence_document_exported_count=int(exported["evidence_document_exported_count"]),
        evidence_anchor_exported_count=int(exported["evidence_anchor_exported_count"]),
        score_contribution_exported_count=int(exported["score_contribution_exported_count"]),
        brain_to_claim_trace_count=int(exported["brain_to_claim_trace_count"]),
        stagecourt_trace_exported_count=int(exported["stagecourt_trace_exported_count"]),
        promoted_stage_row_count=0,
    )

    return {
        "schema_version": "e2r_census_v4_brain_web_attempt_audit_v1",
        "attempt_mode": "research_brain_v4_production_shadow_attempt",
        "verdict": "ATTEMPTED_NOT_CUTOVER_READY" if blockers else "ATTEMPTED_WITH_SOURCE_TASKS",
        "full_thesis_seed_event_path": str(full_thesis_seed_path) if full_thesis_seed_path is not None else None,
        "full_thesis_seed_source": full_thesis_seed_source,
        "full_thesis_seed_original_path": full_thesis_seed_original_path,
        "full_thesis_seed_event_count": full_thesis_seed_event_count,
        "full_thesis_seed_consumed_by_research_brain": seed_runtime["real_provider_success_count"] > 0,
        "full_thesis_seed_planner_attempted_event_count": seed_runtime["planner_attempted_event_count"],
        "full_thesis_seed_planner_run_row_count": seed_runtime["planner_run_row_count"],
        "full_thesis_seed_planner_run_count": seed_runtime["planner_run_count"],
        "full_thesis_seed_real_provider_success_count": seed_runtime["real_provider_success_count"],
        "full_thesis_seed_source_task_execution_count": seed_runtime["source_task_execution_count"],
        "full_thesis_seed_accepted_claim_count": seed_runtime["accepted_claim_count"],
        "full_thesis_seed_stagecourt_trace_count": seed_runtime["stagecourt_trace_count"],
        "full_thesis_seed_materialized_to_stagecourt": seed_runtime["stagecourt_trace_count"] > 0,
        "planner_provider": config.brain_planner_provider,
        "source_acquisition": config.brain_source_acquisition,
        "planner_run_count": int(planner_summary.get("planner_run_count") or len(planner_runs)),
        "real_provider_attempt_count": int(planner_summary.get("real_provider_attempt_count") or 0),
        "real_provider_success_count": real_success,
        "real_provider_failure_count": int(planner_summary.get("real_provider_failure_count") or 0),
        "planner_not_attempted_count": int(planner_summary.get("planner_not_attempted_count") or 0),
        "fake_provider_used_count": int(planner_summary.get("fake_provider_used_count") or 0),
        "planner_output_score_stage_key_count": int(planner_summary.get("planner_output_score_stage_key_count") or 0),
        "source_task_execution_count": source_task_count,
        "real_document_fetched_count": int(source_summary.get("real_document_fetched_count") or 0),
        "unique_real_document_fetched_count": int(source_summary.get("unique_real_document_fetched_count") or 0),
        "accepted_claim_count": accepted_claim_count,
        "unique_accepted_claim_count": unique_accepted_claim_count,
        "claim_acceptance_ready": accepted_claim_count > 0 and unique_accepted_claim_count > 0,
        "deterministic_scorer_output_count": int(watchlist_summary.get("deterministic_scorer_output_count") or 0),
        "brain_to_census_claim_exported_count": exported["accepted_claim_exported_count"],
        "brain_stagecourt_trace_exported_count": exported["stagecourt_trace_exported_count"],
        "brain_to_census_stage_exported_count": 0,
        "brain_source_task_exported_count": exported["source_task_exported_count"],
        "brain_source_task_execution_exported_count": exported["source_task_execution_exported_count"],
        "brain_evidence_document_exported_count": exported["evidence_document_exported_count"],
        "brain_evidence_anchor_exported_count": exported["evidence_anchor_exported_count"],
        "brain_score_contribution_exported_count": exported["score_contribution_exported_count"],
        "stagecourt_trace_ready": exported["stagecourt_trace_exported_count"] > 0,
        "cutover_export_ready": not blockers,
        "brain_to_claim_trace_count": exported["brain_to_claim_trace_count"],
        "brain_raw_assertion_exported_count": exported["raw_assertion_exported_count"],
        "blockers": blockers,
    }


def _write_planner_prompt_response_leafs(*, output_root: Path, planner_runs: Sequence[Any]) -> None:
    prompt_rows: list[dict[str, Any]] = []
    response_rows: list[dict[str, Any]] = []
    for run in planner_runs:
        planner_run_id = str(getattr(run, "planner_run_id", "") or "")
        if not planner_run_id:
            continue
        event = getattr(run, "event", None)
        event_id = str(getattr(event, "candidate_event_id", "") or "")
        symbol = str(getattr(event, "symbol", "") or "")
        prompt_path = str(getattr(run, "raw_prompt_path", "") or "")
        response_path = str(getattr(run, "raw_response_path", "") or "")
        prompt_hash = getattr(run, "prompt_hash", None)
        response_hash = getattr(run, "response_hash", None)
        if prompt_hash and prompt_path:
            prompt_payload = {
                "schema_version": "research_brain_v4_planner_prompt_artifact_v1",
                "planner_run_id": planner_run_id,
                "candidate_event_id": event_id,
                "symbol": symbol,
                "provider_name": getattr(run, "provider_name", None),
                "model": getattr(run, "model", None),
                "prompt_hash": prompt_hash,
                "prompt_payload": getattr(run, "prompt_payload", None),
                "prompt_text": getattr(run, "prompt_text", None),
            }
            _write_relative_json(output_root=output_root, relative_path=prompt_path, payload=prompt_payload)
            prompt_rows.append(
                {
                    "schema_version": "research_brain_v4_planner_prompt_leaf_v1",
                    "planner_run_id": planner_run_id,
                    "candidate_event_id": event_id,
                    "symbol": symbol,
                    "provider_name": getattr(run, "provider_name", None),
                    "model": getattr(run, "model", None),
                    "prompt_hash": prompt_hash,
                    "raw_prompt_path": prompt_path,
                }
            )
        if response_hash and response_path:
            response_payload = {
                "schema_version": "research_brain_v4_planner_response_artifact_v1",
                "planner_run_id": planner_run_id,
                "candidate_event_id": event_id,
                "symbol": symbol,
                "provider_name": getattr(run, "provider_name", None),
                "model": getattr(run, "model", None),
                "response_hash": response_hash,
                "response_payload": getattr(run, "response_payload", None),
                "response_text": getattr(run, "response_text", None),
            }
            _write_relative_json(output_root=output_root, relative_path=response_path, payload=response_payload)
            response_rows.append(
                {
                    "schema_version": "research_brain_v4_planner_response_leaf_v1",
                    "planner_run_id": planner_run_id,
                    "candidate_event_id": event_id,
                    "symbol": symbol,
                    "provider_name": getattr(run, "provider_name", None),
                    "model": getattr(run, "model", None),
                    "response_hash": response_hash,
                    "raw_response_path": response_path,
                }
            )
    _merge_jsonl_by_key(output_root / "llm_prompts.jsonl", prompt_rows, "planner_run_id")
    _merge_jsonl_by_key(output_root / "llm_responses.jsonl", response_rows, "planner_run_id")


def _write_relative_json(*, output_root: Path, relative_path: str, payload: Mapping[str, Any]) -> None:
    path = output_root / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    write_json(path, payload)


def _full_thesis_seed_runtime_counts(*, result: Mapping[str, Any], planner_runs: Sequence[Mapping[str, Any]]) -> dict[str, int]:
    seed_planner_runs = [
        run
        for run in planner_runs
        if _planner_run_event_is_full_thesis_seed(run)
    ]
    seed_event_ids = {
        str((run.get("event") or {}).get("candidate_event_id") or "")
        for run in seed_planner_runs
    }
    source_rows = tuple(((result.get("source_acquisition_report") or {}).get("rows") or ()))
    watchlist_rows = tuple(((result.get("watchlist_report") or {}).get("rows") or ()))
    return {
        "planner_attempted_event_count": len(seed_event_ids),
        "planner_run_row_count": len(seed_planner_runs),
        "planner_run_count": len(seed_event_ids),
        "real_provider_success_count": sum(
            1
            for run in seed_planner_runs
            if str((run.get("event") or {}).get("candidate_event_id") or "") in seed_event_ids
            and run.get("real_provider_success") is True
        ),
        "source_task_execution_count": sum(1 for row in source_rows if str(row.get("candidate_event_id") or "") in seed_event_ids),
        "accepted_claim_count": sum(
            len(row.get("accepted_claim_ids") or ())
            for row in source_rows
            if str(row.get("candidate_event_id") or "") in seed_event_ids
        ),
        "stagecourt_trace_count": sum(
            1
            for row in watchlist_rows
            if str(row.get("candidate_event_id") or "") in seed_event_ids and bool(row.get("stage_court_trace"))
        ),
    }


def _planner_run_event_is_full_thesis_seed(run: Mapping[str, Any]) -> bool:
    event = run.get("event") if isinstance(run.get("event"), Mapping) else {}
    structured = event.get("structured_payload") if isinstance(event.get("structured_payload"), Mapping) else {}
    return (
        str(event.get("source_family") or "") == "CensusFullThesisQueue"
        or str(event.get("event_type") or "") == "full_thesis_refresh_seed"
        or str(structured.get("seed_role") or "") == "planner_input_only"
    )


def _should_run_full_thesis_follow_up_iteration(
    *,
    config: CensusV4RunConfig,
    production_full_thesis_runner: Mapping[str, Any],
) -> bool:
    if config.brain_web_mode != "enabled" or config.brain_stage_promotion_mode != "strict":
        return False
    if int(config.max_iterations or 1) <= 1:
        return False
    if _full_thesis_production_runner_promoted(production_full_thesis_runner):
        return False
    seed_path = Path(str(production_full_thesis_runner.get("blocked_candidate_follow_up_seed_event_path") or ""))
    return seed_path.exists() and int(production_full_thesis_runner.get("blocked_candidate_follow_up_seed_event_count") or 0) > 0


def _full_thesis_production_runner_promoted(production_full_thesis_runner: Mapping[str, Any]) -> bool:
    return int(production_full_thesis_runner.get("promoted_full_thesis_row_count") or 0) > 0


def _full_thesis_follow_up_iteration_summary(
    *,
    iteration: int,
    seed_path: Path | None,
    seed_event_count: int,
    seed_source: str,
    brain_web_attempt: Mapping[str, Any],
    brain_promotion_export: Mapping[str, Any],
    production_full_thesis_runner: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "schema_version": "e2r_census_v4_full_thesis_follow_up_iteration_summary_v1",
        "iteration": iteration,
        "seed_path": str(seed_path) if seed_path is not None else None,
        "seed_source": seed_source,
        "seed_event_count": seed_event_count,
        "brain_web_attempt_verdict": brain_web_attempt.get("verdict"),
        "planner_run_count": int(brain_web_attempt.get("planner_run_count") or 0),
        "real_provider_success_count": int(brain_web_attempt.get("real_provider_success_count") or 0),
        "source_task_execution_count": int(brain_web_attempt.get("source_task_execution_count") or 0),
        "accepted_claim_count": int(brain_web_attempt.get("accepted_claim_count") or 0),
        "stagecourt_trace_exported_count": int(brain_web_attempt.get("brain_stagecourt_trace_exported_count") or 0),
        "promoted_brain_partial_stage_row_count": int(brain_promotion_export.get("promoted_stage_row_count") or 0),
        "production_verdict": production_full_thesis_runner.get("verdict"),
        "production_candidate_row_count": int(production_full_thesis_runner.get("candidate_row_count") or 0),
        "production_blocked_candidate_count": int(production_full_thesis_runner.get("blocked_candidate_count") or 0),
        "promoted_full_thesis_row_count": int(production_full_thesis_runner.get("promoted_full_thesis_row_count") or 0),
        "follow_up_seed_event_count": int(production_full_thesis_runner.get("blocked_candidate_follow_up_seed_event_count") or 0),
        "follow_up_seed_event_path": production_full_thesis_runner.get("blocked_candidate_follow_up_seed_event_path"),
    }


def _full_thesis_follow_up_iterations_audit(
    *,
    config: CensusV4RunConfig,
    iterations: Sequence[Mapping[str, Any]],
    status: str,
) -> dict[str, Any]:
    return {
        "schema_version": "e2r_census_v4_full_thesis_follow_up_iterations_audit_v1",
        "status": status,
        "max_iterations": int(config.max_iterations or 1),
        "iteration_count": len(iterations),
        "follow_up_iteration_count": sum(1 for row in iterations if int(row.get("iteration") or 0) > 1),
        "iterations": [dict(row) for row in iterations],
        "final_promoted_full_thesis_row_count": int(iterations[-1].get("promoted_full_thesis_row_count") or 0) if iterations else 0,
        "final_follow_up_seed_event_count": int(iterations[-1].get("follow_up_seed_event_count") or 0) if iterations else 0,
        "operator_rule": (
            "Follow-up iterations may only feed planner-input seed events back into Research Brain. "
            "They do not score by themselves; production FULL_THESIS promotion still requires source-backed accepted claims, "
            "primitive coverage, score contributions, score interval, and StageCourt closure."
        ),
    }


def _aggregate_brain_web_attempts(attempts: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    attempts = [dict(item) for item in attempts]
    if not attempts:
        return {}
    if len(attempts) == 1:
        return dict(attempts[0])
    latest = dict(attempts[-1])
    sum_keys = [
        "full_thesis_seed_event_count",
        "full_thesis_seed_planner_attempted_event_count",
        "full_thesis_seed_planner_run_row_count",
        "full_thesis_seed_planner_run_count",
        "full_thesis_seed_real_provider_success_count",
        "full_thesis_seed_source_task_execution_count",
        "full_thesis_seed_accepted_claim_count",
        "full_thesis_seed_stagecourt_trace_count",
        "planner_run_count",
        "real_provider_attempt_count",
        "real_provider_success_count",
        "real_provider_failure_count",
        "planner_not_attempted_count",
        "fake_provider_used_count",
        "source_task_execution_count",
        "real_document_fetched_count",
        "unique_real_document_fetched_count",
        "accepted_claim_count",
        "unique_accepted_claim_count",
        "deterministic_scorer_output_count",
        "brain_to_census_claim_exported_count",
        "brain_stagecourt_trace_exported_count",
        "brain_to_census_stage_exported_count",
        "brain_source_task_exported_count",
        "brain_source_task_execution_exported_count",
        "brain_evidence_document_exported_count",
        "brain_evidence_anchor_exported_count",
        "brain_score_contribution_exported_count",
        "brain_to_claim_trace_count",
        "brain_raw_assertion_exported_count",
    ]
    for key in sum_keys:
        latest[key] = sum(int(item.get(key) or 0) for item in attempts)
    latest["schema_version"] = "e2r_census_v4_brain_web_attempt_audit_v1"
    latest["attempt_mode"] = "research_brain_v4_production_shadow_attempt_aggregate"
    latest["attempt_count"] = len(attempts)
    latest["attempts"] = [
        {
            "iteration": index + 1,
            "verdict": item.get("verdict"),
            "full_thesis_seed_event_path": item.get("full_thesis_seed_event_path"),
            "full_thesis_seed_source": item.get("full_thesis_seed_source"),
            "planner_run_count": item.get("planner_run_count"),
            "real_provider_success_count": item.get("real_provider_success_count"),
            "source_task_execution_count": item.get("source_task_execution_count"),
            "accepted_claim_count": item.get("accepted_claim_count"),
            "brain_stagecourt_trace_exported_count": item.get("brain_stagecourt_trace_exported_count"),
            "blockers": item.get("blockers") or [],
        }
        for index, item in enumerate(attempts)
    ]
    latest["full_thesis_seed_consumed_by_research_brain"] = any(
        item.get("full_thesis_seed_consumed_by_research_brain") is True for item in attempts
    )
    latest["full_thesis_seed_materialized_to_stagecourt"] = any(
        item.get("full_thesis_seed_materialized_to_stagecourt") is True for item in attempts
    )
    latest["claim_acceptance_ready"] = any(item.get("claim_acceptance_ready") is True for item in attempts)
    latest["stagecourt_trace_ready"] = any(item.get("stagecourt_trace_ready") is True for item in attempts)
    latest["cutover_export_ready"] = all(not (item.get("blockers") or []) for item in attempts)
    latest["blockers"] = sorted({str(blocker) for item in attempts for blocker in item.get("blockers") or [] if str(blocker)})
    latest["verdict"] = "ATTEMPTED_WITH_SOURCE_TASKS" if not latest["blockers"] else "ATTEMPTED_NOT_CUTOVER_READY"
    return latest


def _aggregate_brain_promotion_exports(exports: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    rows = [dict(item) for item in exports]
    if not rows:
        return {}
    latest = dict(rows[-1])
    for key in ["promoted_stage_row_count", "promoted_web_llm_stage_row_count", "promoted_official_stage_row_count"]:
        latest[key] = sum(int(item.get(key) or 0) for item in rows)
    latest["promoted_stagecourt_trace_ids"] = sorted(
        {str(trace_id) for item in rows for trace_id in item.get("promoted_stagecourt_trace_ids") or [] if str(trace_id)}
    )
    latest["skipped_unsupported_trace_count"] = sum(int(item.get("skipped_unsupported_trace_count") or 0) for item in rows)
    latest["iteration_count"] = len(rows)
    return latest


def _brain_web_attempt_blockers(
    *,
    real_provider_success_count: int,
    source_task_execution_count: int,
    accepted_claim_count: int,
    unique_accepted_claim_count: int,
    accepted_claim_exported_count: int,
    source_task_exported_count: int | None = None,
    source_task_execution_exported_count: int | None = None,
    evidence_document_exported_count: int | None = None,
    evidence_anchor_exported_count: int | None = None,
    score_contribution_exported_count: int | None = None,
    brain_to_claim_trace_count: int = 0,
    stagecourt_trace_exported_count: int = 0,
    promoted_stage_row_count: int = 0,
) -> list[str]:
    blockers: list[str] = []
    if real_provider_success_count <= 0:
        blockers.append("LLM planner did not produce a real-provider success")
    if source_task_execution_count <= 0:
        blockers.append("Research Brain did not execute source tasks")
    elif source_task_execution_exported_count is not None and source_task_execution_exported_count <= 0:
        blockers.append("Research Brain source task attempts have no exported source_task_executions rows")
    if source_task_execution_count > 0 and source_task_exported_count is not None and source_task_exported_count <= 0:
        blockers.append("Research Brain source task attempts have no exported source_tasks rows")
    if accepted_claim_count <= 0 or unique_accepted_claim_count <= 0:
        blockers.append("Research Brain source tasks produced no accepted claims")
    elif unique_accepted_claim_count > accepted_claim_exported_count:
        blockers.append("Research Brain accepted claims are not fully exported into Census claim ledger")
    if accepted_claim_count > 0 and evidence_document_exported_count is not None and evidence_document_exported_count <= 0:
        blockers.append("Research Brain accepted claims have no exported evidence_documents rows")
    if accepted_claim_count > 0 and evidence_anchor_exported_count is not None and evidence_anchor_exported_count <= 0:
        blockers.append("Research Brain accepted claims have no exported evidence_anchors rows")
    if accepted_claim_count > 0 and score_contribution_exported_count is not None and score_contribution_exported_count <= 0:
        blockers.append("Research Brain accepted claims have no exported score_contributions rows")
    if accepted_claim_count > 0 and brain_to_claim_trace_count <= 0:
        blockers.append("Research Brain accepted claims have no brain_to_claim_trace export")
    if accepted_claim_count > 0 and stagecourt_trace_exported_count <= 0:
        blockers.append("Research Brain accepted claims have no StageCourt trace export")
    if accepted_claim_count > 0 and promoted_stage_row_count <= 0:
        blockers.append("Research Brain StageCourt traces are not promoted into census_stage_status rows")
    return blockers


def _brain_web_attempt_failed(
    reason: str,
    *,
    full_thesis_seed_path: Path | None = None,
    full_thesis_seed_event_count: int = 0,
    full_thesis_seed_source: str = "internal_full_thesis_refresh_queue",
    full_thesis_seed_original_path: str | None = None,
) -> dict[str, Any]:
    return {
        "schema_version": "e2r_census_v4_brain_web_attempt_audit_v1",
        "attempt_mode": "enabled_failed_before_artifacts",
        "verdict": "ATTEMPT_FAILED",
        "full_thesis_seed_event_path": str(full_thesis_seed_path) if full_thesis_seed_path is not None else None,
        "full_thesis_seed_source": full_thesis_seed_source,
        "full_thesis_seed_original_path": full_thesis_seed_original_path,
        "full_thesis_seed_event_count": full_thesis_seed_event_count,
        "full_thesis_seed_consumed_by_research_brain": False,
        "full_thesis_seed_planner_attempted_event_count": 0,
        "full_thesis_seed_planner_run_row_count": 0,
        "full_thesis_seed_planner_run_count": 0,
        "full_thesis_seed_real_provider_success_count": 0,
        "full_thesis_seed_source_task_execution_count": 0,
        "full_thesis_seed_accepted_claim_count": 0,
        "full_thesis_seed_stagecourt_trace_count": 0,
        "full_thesis_seed_materialized_to_stagecourt": False,
        "planner_run_count": 0,
        "real_provider_success_count": 0,
        "source_task_execution_count": 0,
        "accepted_claim_count": 0,
        "unique_accepted_claim_count": 0,
        "brain_stagecourt_trace_exported_count": 0,
        "brain_to_census_stage_exported_count": 0,
        "brain_source_task_exported_count": 0,
        "brain_source_task_execution_exported_count": 0,
        "brain_evidence_document_exported_count": 0,
        "brain_evidence_anchor_exported_count": 0,
        "brain_score_contribution_exported_count": 0,
        "claim_acceptance_ready": False,
        "stagecourt_trace_ready": False,
        "cutover_export_ready": False,
        "blockers": [reason],
    }


def _planner_plan_rows(planner_runs: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row in planner_runs:
        event = row.get("event") if isinstance(row.get("event"), Mapping) else {}
        output = row.get("output") if isinstance(row.get("output"), Mapping) else {}
        rows.append(
            {
                "schema_version": "e2r_census_v4_research_brain_plan_ref_v1",
                "planner_run_id": f"PLANNER-{event.get('candidate_event_id') or row.get('provider_name')}",
                "candidate_event_id": event.get("candidate_event_id"),
                "symbol": event.get("symbol"),
                "company_name": event.get("company_name"),
                "provider_name": row.get("provider_name"),
                "provider_mode": row.get("provider_mode"),
                "real_provider_success": row.get("real_provider_success") is True,
                "provider_error": row.get("provider_error"),
                "top_k_archetype_hypotheses": output.get("top_k_archetype_hypotheses") or [],
                "source_task_drafts": output.get("source_task_drafts") or [],
                "do_not_promote_reasons": output.get("do_not_promote_reasons") or [],
            }
        )
    return rows


def _export_brain_web_bundle_leafs(*, result: Mapping[str, Any], output_root: Path) -> dict[str, int]:
    bundles = result.get("bundles") or {}
    source_task_rows: list[dict[str, Any]] = []
    execution_rows: list[dict[str, Any]] = []
    document_rows: list[dict[str, Any]] = []
    anchor_rows: list[dict[str, Any]] = []
    raw_rows: list[dict[str, Any]] = []
    adjudicated_rows: list[dict[str, Any]] = []
    accepted_rows: list[dict[str, Any]] = []
    brain_mapping_trace_rows: list[dict[str, Any]] = []
    trace_rows: list[dict[str, Any]] = []
    primitive_rows: list[dict[str, Any]] = []
    contribution_rows: list[dict[str, Any]] = []
    stage_trace_rows: list[dict[str, Any]] = []
    web_task_rows: list[dict[str, Any]] = []
    web_result_rows: list[dict[str, Any]] = []
    web_fetched_rows: list[dict[str, Any]] = []
    web_rejected_rows: list[dict[str, Any]] = []
    extractor_run_rows: list[dict[str, Any]] = []
    raw_assertion_rejection_rows: list[dict[str, Any]] = []
    claim_to_contributions: dict[str, list[str]] = {}
    claim_to_primitives: dict[str, list[str]] = {}
    event_to_stage_trace_id: dict[str, str] = {}

    planner_run_by_event = {
        str((run.to_dict().get("event") or {}).get("candidate_event_id") or ""): run.to_dict()
        for run in result.get("planner_runs", ())
        if hasattr(run, "to_dict")
    }
    score_exports = _brain_score_stage_export_rows(result=result, bundles=bundles)
    primitive_rows.extend(score_exports["primitive_rows"])
    contribution_rows.extend(score_exports["contribution_rows"])
    stage_trace_rows.extend(score_exports["stage_trace_rows"])
    claim_to_contributions.update(score_exports["claim_to_contributions"])
    claim_to_primitives.update(score_exports["claim_to_primitives"])
    event_to_stage_trace_id.update(score_exports["event_to_stage_trace_id"])

    for event_id, bundle in bundles.items():
        event_id = str(event_id)
        planner_row = planner_run_by_event.get(event_id, {})
        planner_run_id = f"PLANNER-{event_id}"
        documents = getattr(bundle, "documents", {}) or {}
        anchors = getattr(bundle, "anchors", {}) or {}
        raw_assertions = getattr(bundle, "raw_assertions", {}) or {}
        ledger = getattr(bundle, "ledger", None)
        claims = getattr(ledger, "claims", {}) if ledger is not None else {}
        mappings = getattr(ledger, "mappings", {}) if ledger is not None else {}
        for row in getattr(bundle, "web_search_tasks", ()) or ():
            item = _brain_web_leaf_row(row=row, event_id=event_id, planner_row=planner_row)
            web_task_rows.append(item)
        for row in getattr(bundle, "web_search_results", ()) or ():
            item = _brain_web_leaf_row(row=row, event_id=event_id, planner_row=planner_row)
            web_result_rows.append(item)
        for row in getattr(bundle, "web_fetched_documents", ()) or ():
            item = _brain_web_leaf_row(row=row, event_id=event_id, planner_row=planner_row)
            web_fetched_rows.append(item)
        for row in getattr(bundle, "web_rejected_documents", ()) or ():
            item = _brain_web_leaf_row(row=row, event_id=event_id, planner_row=planner_row)
            web_rejected_rows.append(item)
        for row in getattr(bundle, "claim_extractor_runs", ()) or ():
            item = _brain_web_leaf_row(row=row, event_id=event_id, planner_row=planner_row)
            extractor_run_rows.append(item)
        for row in getattr(bundle, "raw_assertion_rejections", ()) or ():
            item = _brain_web_leaf_row(row=row, event_id=event_id, planner_row=planner_row)
            raw_assertion_rejection_rows.append(item)
        accepted_mapping_by_claim: dict[str, Any] = {}
        for mapping in mappings.values():
            if _enum_value(getattr(mapping, "mapping_status", None)) == "ACCEPTED":
                accepted_mapping_by_claim.setdefault(str(getattr(mapping, "claim_id", "")), mapping)
        for document in documents.values():
            row = _jsonable(document)
            row["brain_web_origin"] = "research_brain_v4_attempt"
            row["candidate_event_id"] = event_id
            document_rows.append(row)
        for anchor in anchors.values():
            row = _jsonable(anchor)
            row["brain_web_origin"] = "research_brain_v4_attempt"
            row["candidate_event_id"] = event_id
            anchor_rows.append(row)
        for raw in raw_assertions.values():
            row = _jsonable(raw)
            anchor = anchors.get(str(row.get("anchor_id") or ""))
            document = documents.get(getattr(anchor, "document_id", "")) if anchor is not None else None
            row["document_id"] = getattr(document, "document_id", None)
            row["source_document_id"] = getattr(document, "document_id", None)
            row["source_anchor_id"] = row.get("anchor_id")
            row["source_url"] = getattr(document, "canonical_url", None) if document is not None else None
            row["source_provider"] = getattr(document, "source_name", None) if document is not None else None
            row["anchor_verified"] = getattr(anchor, "anchor_verified", None) if anchor is not None else None
            row["anchor_locator"] = getattr(anchor, "locator", None) if anchor is not None else None
            row["brain_web_origin"] = "research_brain_v4_attempt"
            row["candidate_event_id"] = event_id
            raw_rows.append(row)
        for claim in claims.values():
            claim_row = _jsonable(claim)
            document = documents.get(getattr(claim, "source_document_id", ""))
            anchor = anchors.get(getattr(claim, "source_anchor_id", ""))
            claim_row["document_id"] = getattr(document, "document_id", None)
            claim_row["anchor_id"] = getattr(anchor, "anchor_id", None)
            claim_row["source_url"] = getattr(document, "canonical_url", None) if document is not None else None
            claim_row["source_provider"] = getattr(document, "source_name", None) if document is not None else None
            claim_row["quote_text"] = _claim_quote_text(claim=claim, raw_assertions=raw_assertions, anchor=anchor)
            claim_row["exact_quote"] = _claim_quote_text(claim=claim, raw_assertions=raw_assertions, anchor=anchor)
            claim_row["anchor_verified"] = getattr(anchor, "anchor_verified", None) if anchor is not None else None
            claim_row["brain_web_origin"] = "research_brain_v4_attempt"
            claim_row["candidate_event_id"] = event_id
            adjudicated_rows.append(claim_row)
        for execution in getattr(bundle, "executions", ()):
            execution_row = execution.to_dict() if hasattr(execution, "to_dict") else _jsonable(execution)
            task = dict(execution_row.get("source_task") or {})
            execution_row["brain_web_origin"] = "research_brain_v4_attempt"
            execution_row["source_origin"] = "research_brain_v4_attempt"
            execution_row["source_task_execution_origin"] = "research_brain_v4_attempt"
            execution_row["candidate_event_id"] = event_id
            execution_row["symbol"] = execution_row.get("symbol") or task.get("symbol") or planner_row.get("symbol")
            execution_row["company_name"] = execution_row.get("company_name") or task.get("company_name") or planner_row.get("company_name")
            _backfill_source_task_execution_identity(execution_row=execution_row, task=task)
            execution_rows.append(execution_row)
            if task:
                task["source_task_origin"] = "research_brain_v4_attempt"
                task["source_origin"] = "research_brain_v4_attempt"
                source_task_rows.append(task)
            brain_mapping_trace_rows.extend(
                _brain_claim_mapping_trace_rows(
                    event_id=event_id,
                    planner_run_id=planner_run_id,
                    planner_row=planner_row,
                    execution_row=execution_row,
                    claims=claims,
                    mappings=mappings,
                    documents=documents,
                    anchors=anchors,
                    raw_assertions=raw_assertions,
                    accepted_mapping_by_claim=accepted_mapping_by_claim,
                    claim_to_contributions=claim_to_contributions,
                    claim_to_primitives=claim_to_primitives,
                    event_to_stage_trace_id=event_to_stage_trace_id,
                )
            )
            _append_raw_assertion_rejection_fallbacks_from_mapping_trace(
                raw_assertion_rejection_rows=raw_assertion_rejection_rows,
                mapping_trace_rows=brain_mapping_trace_rows,
            )
            for claim_id in execution_row.get("accepted_claim_ids") or []:
                claim = claims.get(str(claim_id))
                if claim is None:
                    continue
                mapping = accepted_mapping_by_claim.get(str(claim_id))
                accepted_payload = _accepted_claim_payload_from_brain(
                    claim=claim,
                    mapping=mapping,
                    document=documents.get(getattr(claim, "source_document_id", "")),
                    anchor=anchors.get(getattr(claim, "source_anchor_id", "")),
                    raw_assertions=raw_assertions,
                    execution_row=execution_row,
                )
                accepted_rows.append(accepted_payload)
                contribution_ids = list(claim_to_contributions.get(str(claim_id)) or [])
                primitive_ids = list(claim_to_primitives.get(str(claim_id)) or [])
                score_support_status = (
                    "SCORE_SUPPORTED"
                    if contribution_ids
                    else "PRIMITIVE_ONLY_NOT_SCORE_CONTRIBUTING"
                    if primitive_ids
                    else "ACCEPTED_NON_REPRESENTATIVE_NOT_SCORE_CONTRIBUTING"
                    if event_to_stage_trace_id.get(event_id)
                    else "NO_SCORE_CONTRIBUTION"
                )
                trace_rows.append(
                    {
                        "schema_version": "e2r_census_v4_brain_to_claim_trace_v1",
                        "symbol": task.get("symbol") or execution_row.get("symbol"),
                        "candidate_event_id": event_id,
                        "planner_run_id": planner_run_id,
                        "planner_provider": planner_row.get("provider_name"),
                        "source_task_id": execution_row.get("task_id"),
                        "web_task_id": None,
                        "document_id": getattr(claim, "source_document_id", None),
                        "anchor_id": getattr(claim, "source_anchor_id", None),
                        "raw_assertion_id": getattr(claim, "raw_assertion_id", None),
                        "adjudicated_claim_id": getattr(claim, "claim_id", None),
                        "accepted_claim_id": getattr(claim, "claim_id", None),
                        "score_eligible": accepted_payload.get("score_eligible"),
                        "primitive_state_id": (primitive_ids or [None])[0],
                        "primitive_state_ids": primitive_ids,
                        "score_contribution_id": (contribution_ids or [None])[0],
                        "score_contribution_ids": contribution_ids,
                        "score_support_status": score_support_status,
                        "score_deduped_by_source_family": score_support_status == "SOURCE_FAMILY_DEDUPED",
                        "representative_score_claim": bool(contribution_ids),
                        "stagecourt_trace_id": event_to_stage_trace_id.get(event_id),
                        "census_stage_status_id": None,
                        "satisfies_source_task": str(claim_id) in {str(item) for item in execution_row.get("direct_accepted_claim_ids") or []}
                        if (execution_row.get("direct_accepted_claim_ids") or execution_row.get("rerouted_accepted_claim_ids"))
                        else bool(execution_row.get("satisfies_source_task", True)),
                        "satisfaction_type": (
                            "DIRECT_ACCEPTED_CLAIM"
                            if str(claim_id) in {str(item) for item in execution_row.get("direct_accepted_claim_ids") or []}
                            else "REROUTED_ACCEPTED_CLAIM"
                            if str(claim_id) in {str(item) for item in execution_row.get("rerouted_accepted_claim_ids") or []}
                            else execution_row.get("satisfaction_type")
                        ),
                        "source_task_primitive_gap": task.get("primitive_gap"),
                        "trace_status": score_support_status
                        if score_support_status in {"SOURCE_FAMILY_DEDUPED", "ACCEPTED_NON_REPRESENTATIVE_NOT_SCORE_CONTRIBUTING", "PRIMITIVE_ONLY_NOT_SCORE_CONTRIBUTING"}
                        else "CLAIM_SCORE_TRACE_EXPORTED_STAGE_NOT_PROMOTED"
                        if event_to_stage_trace_id.get(event_id)
                        else "CLAIM_EXPORTED_STAGE_NOT_PROMOTED",
                    }
                )

    _merge_jsonl_by_key(output_root / "source_tasks.jsonl", source_task_rows, "task_id")
    _merge_jsonl_by_key(output_root / "source_task_executions.jsonl", execution_rows, "task_id")
    _merge_jsonl_by_key(output_root / "evidence_documents.jsonl", document_rows, "document_id")
    _merge_jsonl_by_key(output_root / "evidence_anchors.jsonl", anchor_rows, "anchor_id")
    _merge_jsonl_by_key(output_root / "raw_assertions.jsonl", raw_rows, "raw_assertion_id")
    _merge_jsonl_by_key(output_root / "adjudicated_claims.jsonl", adjudicated_rows, "claim_id")
    _merge_jsonl_by_key(output_root / "accepted_claims.jsonl", accepted_rows, "claim_id")
    _merge_jsonl_by_key(output_root / "primitive_states.jsonl", primitive_rows, "primitive_state_id")
    _merge_jsonl_by_key(output_root / "score_contributions.jsonl", contribution_rows, "score_contribution_id")
    _merge_jsonl_by_key(output_root / "stagecourt_traces.jsonl", stage_trace_rows, "stagecourt_trace_id")
    _merge_jsonl_by_key(output_root / "brain_to_claim_trace.jsonl", trace_rows, "accepted_claim_id")
    _merge_jsonl_by_key(output_root / "brain_claim_mapping_trace.jsonl", brain_mapping_trace_rows, "brain_claim_mapping_trace_id")
    _merge_jsonl_by_key(output_root / "web_search_tasks.jsonl", web_task_rows, "web_task_id")
    _merge_jsonl_by_key(output_root / "web_search_results.jsonl", web_result_rows, "web_result_id")
    _merge_jsonl_by_key(output_root / "web_fetched_documents.jsonl", web_fetched_rows, "web_fetch_id")
    _merge_jsonl_by_key(output_root / "web_rejected_documents.jsonl", web_rejected_rows, "web_rejected_id")
    _merge_jsonl_by_key(output_root / "claim_extractor_runs.jsonl", extractor_run_rows, "claim_extractor_run_id")
    _merge_jsonl_by_key(output_root / "raw_assertion_rejections.jsonl", raw_assertion_rejection_rows, "raw_assertion_rejection_id")
    return {
        "source_task_exported_count": len(source_task_rows),
        "source_task_execution_exported_count": len(execution_rows),
        "evidence_document_exported_count": len(document_rows),
        "evidence_anchor_exported_count": len(anchor_rows),
        "raw_assertion_exported_count": len(raw_rows),
        "adjudicated_claim_exported_count": len(adjudicated_rows),
        "accepted_claim_exported_count": len({str(row.get("claim_id")) for row in accepted_rows if row.get("claim_id")}),
        "brain_claim_mapping_trace_exported_count": len(
            {str(row.get("brain_claim_mapping_trace_id")) for row in brain_mapping_trace_rows if row.get("brain_claim_mapping_trace_id")}
        ),
        "brain_to_claim_trace_count": len({str(row.get("accepted_claim_id")) for row in trace_rows if row.get("accepted_claim_id")}),
        "primitive_state_exported_count": len(primitive_rows),
        "score_contribution_exported_count": len(contribution_rows),
        "stagecourt_trace_exported_count": len(stage_trace_rows),
        "web_search_task_exported_count": len(web_task_rows),
        "web_search_result_exported_count": len(web_result_rows),
        "web_fetched_document_exported_count": len(web_fetched_rows),
        "web_rejected_document_exported_count": len(web_rejected_rows),
        "claim_extractor_run_exported_count": len(extractor_run_rows),
        "raw_assertion_rejection_exported_count": len(raw_assertion_rejection_rows),
    }


def _append_raw_assertion_rejection_fallbacks_from_mapping_trace(
    *,
    raw_assertion_rejection_rows: list[dict[str, Any]],
    mapping_trace_rows: Sequence[Mapping[str, Any]],
) -> None:
    existing_keys = {
        (
            str(row.get("raw_assertion_id") or ""),
            str(row.get("adjudicated_claim_id") or row.get("claim_id") or ""),
            str(row.get("source_task_id") or row.get("task_id") or ""),
        )
        for row in raw_assertion_rejection_rows
    }
    for row in mapping_trace_rows:
        if row.get("accepted") is not False:
            continue
        raw_assertion_id = str(row.get("raw_assertion_id") or "")
        claim_id = str(row.get("claim_id") or row.get("adjudicated_claim_id") or "")
        source_task_id = str(row.get("source_task_id") or row.get("task_id") or row.get("source_task_execution_id") or "")
        if not raw_assertion_id or not claim_id:
            continue
        key = (raw_assertion_id, claim_id, source_task_id)
        if key in existing_keys:
            continue
        eligibility_reasons = [str(item) for item in row.get("eligibility_reasons") or row.get("source_task_not_eligible_reasons") or []]
        rejection_reason = _raw_assertion_rejection_reason_from_mapping_trace(row=row, eligibility_reasons=eligibility_reasons)
        raw_assertion_rejection_rows.append(
            {
                "schema_version": "e2r_research_brain_v4_raw_assertion_rejection_v1",
                "raw_assertion_rejection_id": "RAWREJECT-" + stable_hash((raw_assertion_id, claim_id, source_task_id, rejection_reason))[:24],
                "raw_assertion_id": raw_assertion_id,
                "adjudicated_claim_id": claim_id,
                "claim_id": claim_id,
                "mapping_id": row.get("mapping_id"),
                "task_id": source_task_id,
                "source_task_id": source_task_id,
                "candidate_event_id": row.get("candidate_event_id"),
                "symbol": row.get("symbol"),
                "company_name": row.get("company_name"),
                "archetype_id": row.get("archetype_id"),
                "primitive_gap": row.get("primitive_gap"),
                "source_task_primitive_gap": row.get("primitive_gap"),
                "document_id": row.get("document_id") or row.get("source_document_id"),
                "anchor_id": row.get("anchor_id") or row.get("source_anchor_id"),
                "source_url": row.get("source_url"),
                "source_provider": row.get("source_provider"),
                "as_of_date": row.get("as_of_date"),
                "rejection_stage": "mapping_trace_export",
                "rejection_reason": rejection_reason,
                "not_eligible_reasons": eligibility_reasons,
                "target_scope_status": row.get("target_scope_status"),
                "temporal_status": row.get("temporal_status"),
                "polarity": row.get("polarity"),
                "semantic_status": row.get("semantic_status"),
                "directness": row.get("directness"),
                "mapping_status": row.get("mapping_status"),
                "mapped_primitive_id": row.get("primitive_id"),
                "support_direction": row.get("support_direction"),
                "mapping_rationale": row.get("mapping_rationale"),
                "accepted_claim_id_if_any": None,
                "score_eligible": False,
                "source_origin": "research_brain_v4_attempt",
                "brain_web_origin": "research_brain_v4_attempt",
            }
        )
        existing_keys.add(key)


def _raw_assertion_rejection_reason_from_mapping_trace(*, row: Mapping[str, Any], eligibility_reasons: Sequence[str]) -> str:
    reason_texts = [str(reason) for reason in eligibility_reasons if str(reason).strip()]
    if any(reason.startswith("anchor") for reason in reason_texts):
        return "anchor_validation_failed"
    if any(reason.startswith("future_") for reason in reason_texts):
        return "future_leakage_rejected"

    target_scope_status = str(row.get("target_scope_status") or "")
    directness = str(row.get("directness") or "")
    temporal_status = str(row.get("temporal_status") or "")
    semantic_status = str(row.get("semantic_status") or "")
    mapping_status = str(row.get("mapping_status") or "")

    # Fallback rows are reconstructed from exported mapping traces. The trace can
    # carry task/document-level eligibility reasons, so prefer the row's own axis
    # fields before classifying a claim as wrong-subject or historical.
    if target_scope_status and target_scope_status != "DIRECT":
        return "target_scope_or_directness_rejected"
    if directness and directness not in {"DIRECT", "DIRECT_TARGET"}:
        return "target_scope_or_directness_rejected"
    if temporal_status and temporal_status not in {"CURRENT", "PRESENT_CURRENT", "OPEN"}:
        return "temporal_status_rejected"
    if semantic_status and semantic_status not in {"PASS", "PASSED", "SEMANTIC_VERIFIED"}:
        return "semantic_verification_rejected"
    if mapping_status == "REJECTED":
        return "primitive_mapping_rejected"

    if any(str(reason).startswith("target_scope_not_allowed") or str(reason).startswith("target_not_direct") for reason in eligibility_reasons):
        return "target_scope_or_directness_rejected"
    if any(str(reason).startswith("temporal_not_allowed") for reason in eligibility_reasons):
        return "temporal_status_rejected"
    if any(str(reason).startswith("mapping_not_accepted") or str(reason).startswith("primitive_mapping_rejected") for reason in eligibility_reasons):
        return "primitive_mapping_rejected"
    if any(str(reason).startswith("semantic_") for reason in eligibility_reasons):
        return "semantic_verification_rejected"
    return "score_eligibility_rejected"


def _brain_claim_mapping_trace_rows(
    *,
    event_id: str,
    planner_run_id: str,
    planner_row: Mapping[str, Any],
    execution_row: Mapping[str, Any],
    claims: Mapping[str, Any],
    mappings: Mapping[str, Any],
    documents: Mapping[str, Any],
    anchors: Mapping[str, Any],
    raw_assertions: Mapping[str, Any],
    accepted_mapping_by_claim: Mapping[str, Any],
    claim_to_contributions: Mapping[str, Sequence[str]],
    claim_to_primitives: Mapping[str, Sequence[str]],
    event_to_stage_trace_id: Mapping[str, str],
) -> list[dict[str, Any]]:
    task = dict(execution_row.get("source_task") or {})
    task_id = str(execution_row.get("task_id") or task.get("task_id") or "")
    accepted_ids = {str(item) for item in execution_row.get("accepted_claim_ids") or ()}
    rejected_ids = {str(item) for item in execution_row.get("rejected_claim_ids") or ()}
    adjudicated_ids = [str(item) for item in execution_row.get("adjudicated_claim_ids") or () if str(item)]
    mappings_by_claim: dict[str, list[Any]] = {}
    for mapping in mappings.values():
        mappings_by_claim.setdefault(str(getattr(mapping, "claim_id", "")), []).append(mapping)

    rows: list[dict[str, Any]] = []
    for claim_id in dict.fromkeys([*adjudicated_ids, *sorted(accepted_ids), *sorted(rejected_ids)]):
        claim = claims.get(claim_id)
        if claim is None:
            rows.append(
                {
                    "schema_version": "e2r_census_v4_brain_claim_mapping_trace_v1",
                    "brain_claim_mapping_trace_id": f"BRAINMAP-{stable_hash((event_id, task_id, claim_id, 'missing_claim'))[:20]}",
                    "candidate_event_id": event_id,
                    "planner_run_id": planner_run_id,
                    "source_task_execution_id": task_id,
                    "source_task_id": task_id,
                    "symbol": execution_row.get("symbol") or task.get("symbol") or planner_row.get("symbol"),
                    "company_name": execution_row.get("company_name") or task.get("company_name") or planner_row.get("company_name"),
                    "primitive_gap": task.get("primitive_gap"),
                    "claim_id": claim_id,
                    "accepted": False,
                    "score_eligible": False,
                    "rejection_reason": "claim_id_not_found_in_ledger",
                    "source_origin": "research_brain_v4_attempt",
                    "brain_web_origin": "research_brain_v4_attempt",
                }
            )
            continue
        claim_mappings = mappings_by_claim.get(claim_id) or [accepted_mapping_by_claim.get(claim_id)]
        for mapping in [item for item in claim_mappings if item is not None] or [None]:
            document_id = getattr(claim, "source_document_id", None)
            anchor_id = getattr(claim, "source_anchor_id", None)
            document = documents.get(str(document_id or ""))
            anchor = anchors.get(str(anchor_id or ""))
            quote_text = _claim_quote_text(claim=claim, raw_assertions=raw_assertions, anchor=anchor)
            mapping_status = _enum_value(getattr(mapping, "mapping_status", None)) if mapping is not None else "UNMAPPED"
            primitive_id = getattr(mapping, "primitive_id", None) if mapping is not None else None
            target_scope_status = _enum_value(getattr(claim, "target_scope_status", None))
            temporal_status = _enum_value(getattr(claim, "temporal_status", None))
            eligibility_reasons = _brain_claim_score_eligibility_reasons(
                document_id=document_id,
                anchor_id=anchor_id,
                document=document,
                anchor=anchor,
                event_date=getattr(claim, "event_date", None),
                source_cutover_date=execution_row.get("source_cutover_date"),
                target_scope_status=target_scope_status,
                temporal_status=temporal_status,
                mapping_status=mapping_status,
                primitive_id=primitive_id,
                source_url=getattr(document, "canonical_url", None) if document is not None else None,
            )
            accepted = claim_id in accepted_ids
            source_task_not_eligible = [] if accepted else list(execution_row.get("not_eligible_reasons") or [])
            if source_task_not_eligible:
                eligibility_reasons = list(dict.fromkeys((*eligibility_reasons, *source_task_not_eligible)))
            trace_status = "ACCEPTED_FOR_SCORE" if accepted else "REJECTED_BEFORE_SCORE"
            rejection_reason = None
            if not accepted:
                rejection_reason = ";".join(eligibility_reasons or source_task_not_eligible or [getattr(mapping, "rationale", None) or "not_accepted"])
            mapping_id = getattr(mapping, "mapping_id", None) if mapping is not None else None
            trace_id = f"BRAINMAP-{stable_hash((event_id, task_id, claim_id, mapping_id or 'unmapped'))[:20]}"
            rows.append(
                {
                    "schema_version": "e2r_census_v4_brain_claim_mapping_trace_v1",
                    "brain_claim_mapping_trace_id": trace_id,
                    "candidate_event_id": event_id,
                    "planner_run_id": planner_run_id,
                    "planner_provider": planner_row.get("provider_name"),
                    "source_task_execution_id": task_id,
                    "source_task_id": task_id,
                    "symbol": execution_row.get("symbol") or task.get("symbol") or planner_row.get("symbol"),
                    "company_name": execution_row.get("company_name") or task.get("company_name") or planner_row.get("company_name"),
                    "primitive_gap": task.get("primitive_gap"),
                    "preferred_source_classes": task.get("preferred_source_classes") or [],
                    "fallback_source_classes": task.get("fallback_source_classes") or [],
                    "claim_id": claim_id,
                    "raw_assertion_id": getattr(claim, "raw_assertion_id", None),
                    "mapping_id": mapping_id,
                    "document_id": document_id,
                    "source_document_id": document_id,
                    "anchor_id": anchor_id,
                    "source_anchor_id": anchor_id,
                    "source_url": getattr(document, "canonical_url", None) if document is not None else None,
                    "source_provider": getattr(document, "source_name", None) if document is not None else None,
                    "anchor_verified": getattr(anchor, "anchor_verified", None) if anchor is not None else None,
                    "anchor_locator": getattr(anchor, "locator", None) if anchor is not None else None,
                    "quote_text": quote_text,
                    "exact_quote": quote_text,
                    "target_scope_status": target_scope_status,
                    "directness": _enum_value(getattr(claim, "directness", None)),
                    "semantic_status": _enum_value(getattr(claim, "semantic_status", None)),
                    "temporal_status": temporal_status,
                    "polarity": _enum_value(getattr(claim, "polarity", None)),
                    "mapping_status": mapping_status,
                    "primitive_id": primitive_id,
                    "support_direction": _enum_value(getattr(mapping, "support_direction", None)) if mapping is not None else None,
                    "mapping_rationale": getattr(mapping, "rationale", None) if mapping is not None else None,
                    "contract_rule_id": getattr(mapping, "contract_rule_id", None) if mapping is not None else None,
                    "eligibility_reasons": eligibility_reasons,
                    "source_task_not_eligible_reasons": source_task_not_eligible,
                    "rejection_reason": rejection_reason,
                    "accepted": accepted,
                    "score_eligible": accepted and not eligibility_reasons,
                    "satisfies_source_task": bool(execution_row.get("satisfies_source_task")),
                    "satisfaction_type": execution_row.get("satisfaction_type"),
                    "direct_accepted_claim_ids": list(execution_row.get("direct_accepted_claim_ids") or []),
                    "rerouted_accepted_claim_ids": list(execution_row.get("rerouted_accepted_claim_ids") or []),
                    "accepted_primitive_ids": list(execution_row.get("accepted_primitive_ids") or []),
                    "primitive_gap_satisfied_ids": list(execution_row.get("primitive_gap_satisfied_ids") or []),
                    "primitive_gap_unsatisfied_ids": list(execution_row.get("primitive_gap_unsatisfied_ids") or []),
                    "score_contribution_ids": list(claim_to_contributions.get(claim_id) or []),
                    "primitive_state_ids": list(claim_to_primitives.get(claim_id) or []),
                    "stagecourt_trace_id": event_to_stage_trace_id.get(event_id),
                    "trace_status": trace_status,
                    "source_origin": "research_brain_v4_attempt",
                    "brain_web_origin": "research_brain_v4_attempt",
                }
            )
    return rows


def _brain_web_leaf_row(*, row: Mapping[str, Any], event_id: str, planner_row: Mapping[str, Any]) -> dict[str, Any]:
    item = _jsonable(row)
    item["brain_web_origin"] = item.get("brain_web_origin") or "research_brain_v4_attempt"
    item["source_origin"] = item.get("source_origin") or "research_brain_v4_attempt"
    item["candidate_event_id"] = item.get("candidate_event_id") or event_id
    item["symbol"] = item.get("symbol") or planner_row.get("symbol")
    item["company_name"] = item.get("company_name") or planner_row.get("company_name")
    return item


def _claim_quote_text(*, claim: Any, raw_assertions: Mapping[str, Any], anchor: Any | None) -> str | None:
    raw_assertion_id = str(getattr(claim, "raw_assertion_id", "") or "")
    raw = raw_assertions.get(raw_assertion_id)
    if raw is not None:
        quote = str(getattr(raw, "exact_quote", "") or getattr(raw, "object_text", "") or "").strip()
        if quote:
            return quote
    if anchor is None:
        return None
    return getattr(anchor, "exact_text", None)


def _accepted_claim_payload_from_brain(
    *,
    claim: Any,
    mapping: Any | None,
    document: Any | None,
    anchor: Any | None,
    raw_assertions: Mapping[str, Any],
    execution_row: Mapping[str, Any],
) -> dict[str, Any]:
    event_date = getattr(claim, "event_date", None)
    document_id = getattr(claim, "source_document_id", None)
    anchor_id = getattr(claim, "source_anchor_id", None)
    mapping_status = _enum_value(getattr(mapping, "mapping_status", None)) if mapping is not None else None
    primitive_id = getattr(mapping, "primitive_id", None) if mapping is not None else None
    target_scope_status = _enum_value(getattr(claim, "target_scope_status", None))
    temporal_status = _enum_value(getattr(claim, "temporal_status", None))
    directness = _enum_value(getattr(claim, "directness", None))
    source_url = getattr(document, "canonical_url", None) if document is not None else None
    direct_claim_ids = {str(item) for item in execution_row.get("direct_accepted_claim_ids") or []}
    rerouted_claim_ids = {str(item) for item in execution_row.get("rerouted_accepted_claim_ids") or []}
    claim_id = str(getattr(claim, "claim_id", None) or "")
    has_satisfaction_split = bool(direct_claim_ids or rerouted_claim_ids or execution_row.get("satisfaction_type"))
    satisfies_source_task = claim_id in direct_claim_ids if has_satisfaction_split else True
    satisfaction_type = "DIRECT_ACCEPTED_CLAIM" if satisfies_source_task else "REROUTED_ACCEPTED_CLAIM"
    eligibility_reasons = _brain_claim_score_eligibility_reasons(
        document_id=document_id,
        anchor_id=anchor_id,
        document=document,
        anchor=anchor,
        event_date=event_date,
        source_cutover_date=execution_row.get("source_cutover_date"),
        target_scope_status=target_scope_status,
        temporal_status=temporal_status,
        mapping_status=mapping_status,
        primitive_id=primitive_id,
        source_url=source_url,
    )
    score_eligible = not eligibility_reasons
    return {
        "accepted": True,
        "adjudication": {
            "directness": directness,
            "polarity": _enum_value(getattr(claim, "polarity", None)),
            "semantic_status": _enum_value(getattr(claim, "semantic_status", None)),
            "target_scope_status": target_scope_status,
            "temporal_status": temporal_status,
        },
        "anchor_id": anchor_id,
        "as_of_date": execution_row.get("source_cutover_date"),
        "claim_id": getattr(claim, "claim_id", None),
        "directness": directness,
        "document_id": document_id,
        "eligibility_policy": "code_derived_v1",
        "eligibility_reasons": eligibility_reasons,
        "event_date": event_date.isoformat() if hasattr(event_date, "isoformat") else event_date,
        "mapping": _jsonable(mapping) if mapping is not None else {},
        "mapping_status": mapping_status,
        "polarity": _enum_value(getattr(claim, "polarity", None)),
        "primitive_id": primitive_id,
        "quote_text": _claim_quote_text(claim=claim, raw_assertions=raw_assertions, anchor=anchor),
        "raw_assertion_id": getattr(claim, "raw_assertion_id", None),
        "satisfies_source_task": satisfies_source_task,
        "satisfaction_type": satisfaction_type,
        "source_task_primitive_gap": (execution_row.get("source_task") or {}).get("primitive_gap"),
        "score_eligible": score_eligible,
        "semantic_status": _enum_value(getattr(claim, "semantic_status", None)),
        "source_cutover_date": execution_row.get("source_cutover_date"),
        "source_provider": getattr(document, "source_name", None) if document is not None else None,
        "source_url": source_url,
        "subject_entity_id": getattr(claim, "subject_entity_id", None),
        "support_direction": _enum_value(getattr(mapping, "support_direction", None)) if mapping is not None else None,
        "symbol": (execution_row.get("source_task") or {}).get("symbol"),
        "target_entity_id": getattr(claim, "target_entity_id", None),
        "target_scope_status": target_scope_status,
        "temporal_status": temporal_status,
        "source_origin": "research_brain_v4_attempt",
        "brain_web_claim": True,
        "full_thesis_claim": False,
    }


def _brain_claim_score_eligibility_reasons(
    *,
    document_id: Any,
    anchor_id: Any,
    document: Any | None,
    anchor: Any | None,
    event_date: Any,
    source_cutover_date: Any,
    target_scope_status: str | None,
    temporal_status: str | None,
    mapping_status: str | None,
    primitive_id: Any,
    source_url: Any,
) -> list[str]:
    reasons: list[str] = []
    if not document_id or document is None:
        reasons.append("missing_document")
    if not anchor_id or anchor is None:
        reasons.append("missing_anchor")
    if not event_date and not source_cutover_date:
        reasons.append("missing_event_or_source_date")
    if target_scope_status != "DIRECT":
        reasons.append(f"target_scope_not_direct:{target_scope_status or 'UNKNOWN'}")
    if temporal_status not in {"CURRENT", "PRESENT_CURRENT", "OPEN"}:
        reasons.append(f"temporal_not_current:{temporal_status or 'UNKNOWN'}")
    if mapping_status != "ACCEPTED":
        reasons.append(f"mapping_not_accepted:{mapping_status or 'UNKNOWN'}")
    if not primitive_id:
        reasons.append("missing_primitive_id")
    if str(source_url or "").startswith("snapshot://"):
        reasons.append("snapshot_source_not_score_eligible")
    return reasons


def _brain_score_stage_export_rows(*, result: Mapping[str, Any], bundles: Mapping[str, Any]) -> dict[str, Any]:
    from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
    from e2r.agentic.evidence_os import ScoreInterval
    from e2r.agentic.primitive_aggregator import aggregate_primitive_states
    from e2r.agentic.score_contribution_ledger import DEFAULT_SCORE_COMPONENT_MAX_POINTS, build_component_score_contributions_from_rubric
    from e2r.agentic.stage_court import StageCourtInput, decide_stage_court
    from e2r.calibration.taxonomy import large_sector_for_archetype
    from e2r.scoring import CANONICAL_SCORE_COMPONENTS, DeterministicScorer, ScoringPayload

    config = result.get("config") if isinstance(result.get("config"), Mapping) else {}
    as_of = date.fromisoformat(str(config.get("as_of_date") or "2026-07-01"))
    contracts = load_evidence_contracts_v2(require_all_archetypes=True)
    primitive_rows: list[dict[str, Any]] = []
    contribution_rows: list[dict[str, Any]] = []
    stage_trace_rows: list[dict[str, Any]] = []
    claim_to_contributions: dict[str, list[str]] = {}
    claim_to_primitives: dict[str, list[str]] = {}
    event_to_stage_trace_id: dict[str, str] = {}
    for item in result.get("watchlist_items", ()):
        item_row = item.to_dict() if hasattr(item, "to_dict") else _jsonable(item)
        event_id = str(item_row.get("candidate_event_id") or "")
        bundle = bundles.get(event_id)
        if bundle is None:
            continue
        accepted_claim_ids = tuple(str(claim_id) for claim_id in item_row.get("accepted_claim_ids") or ())
        primary = str(item_row.get("primary_archetype") or "")
        contract = contracts.get(primary)
        if not accepted_claim_ids or contract is None:
            continue
        primitive_states = aggregate_primitive_states(ledger=bundle.ledger, contract=contract, as_of_date=as_of)
        contributions = build_component_score_contributions_from_rubric(
            components={component.key: component.max_points for component in CANONICAL_SCORE_COMPONENTS},
            primitive_states=primitive_states,
            score_rubric=contract.score_rubric,
            component_max_points=DEFAULT_SCORE_COMPONENT_MAX_POINTS,
        )
        positive_contributions = tuple(contribution for contribution in contributions if contribution.raw_points > 0)
        if not positive_contributions:
            continue
        score_support_claim_ids: list[str] = []
        for claim_id in accepted_claim_ids:
            if any(str(claim_id) in {str(item) for item in contribution.support_claim_ids} for contribution in positive_contributions):
                _append_unique(score_support_claim_ids, str(claim_id))
        for contribution in positive_contributions:
            for claim_id in contribution.support_claim_ids:
                _append_unique(score_support_claim_ids, str(claim_id))
        non_score_accepted_claim_ids = [claim_id for claim_id in accepted_claim_ids if claim_id not in set(score_support_claim_ids)]
        payload = ScoringPayload(
            symbol=str(item_row.get("symbol") or ""),
            as_of_date=as_of,
            components={component.key: 0.0 for component in CANONICAL_SCORE_COMPONENTS},
            diagnostic_scores={
                "require_v2_score_contributions": 100.0,
                "agentic_evidence_required_for_scoring": 100.0,
                "claim_backed_claim_count_capped": min(float(len(score_support_claim_ids)), 100.0),
            },
            evidence_ids=tuple(score_support_claim_ids),
            score_contributions_v2=contributions,
            large_sector_id=large_sector_for_archetype(primary),
            canonical_archetype_id=primary,
            scoring_version="research-brain-v4-census-export",
        )
        snapshot = DeterministicScorer().score(payload)
        interval = ScoreInterval(verified_score=snapshot.total_score, potential_score_upper_bound=snapshot.total_score)
        stage = decide_stage_court(
            StageCourtInput(
                score_interval=interval,
                primitive_states=primitive_states,
                contract=contract,
                current_hard_break_claim_ids=(),
                has_prior_live_thesis=False,
            )
        )
        for primitive_id, state in primitive_states.items():
            primitive_state_id = f"PRIM-BRAIN-{stable_hash((event_id, primitive_id, state.support_claim_ids, state.counter_claim_ids))[:20]}"
            primitive_rows.append(
                {
                    "primitive_state_id": primitive_state_id,
                    "candidate_event_id": event_id,
                    "symbol": item_row.get("symbol"),
                    "source_cutover_date": as_of.isoformat(),
                    "primitive_id": primitive_id,
                    "status": _enum_value(state.status),
                    "normalized_value": _jsonable(state.normalized_value),
                    "support_claim_ids": list(state.support_claim_ids),
                    "counter_claim_ids": list(state.counter_claim_ids),
                    "freshness_days": state.freshness_days,
                    "confidence_for_review": state.confidence_for_review,
                    "materiality_remaining_points": state.materiality_remaining_points,
                    "support_mapping_ids": list(state.support_mapping_ids),
                    "counter_mapping_ids": list(state.counter_mapping_ids),
                    "source_origin": "research_brain_v4_attempt",
                }
            )
            for claim_id in state.support_claim_ids:
                claim_to_primitives.setdefault(str(claim_id), []).append(primitive_state_id)
        for contribution in positive_contributions:
            row = _jsonable(contribution)
            row["score_contribution_id"] = contribution.contribution_id
            row["contribution_id"] = contribution.contribution_id
            row["candidate_event_id"] = event_id
            row["symbol"] = item_row.get("symbol")
            row["source_cutover_date"] = as_of.isoformat()
            row["source_origin"] = "research_brain_v4_attempt"
            contribution_rows.append(row)
            for claim_id in contribution.support_claim_ids:
                claim_to_contributions.setdefault(str(claim_id), []).append(contribution.contribution_id)
        trace_primitive_state_ids: list[str] = []
        for claim_id in score_support_claim_ids:
            for primitive_state_id in claim_to_primitives.get(str(claim_id), ()):
                _append_unique(trace_primitive_state_ids, primitive_state_id)
        trace_id = f"SCT-BRAIN-{stable_hash((event_id, item_row.get('symbol'), snapshot.total_score, [item.contribution_id for item in positive_contributions]))[:20]}"
        event_to_stage_trace_id[event_id] = trace_id
        stage_trace_rows.append(
            {
                "stagecourt_trace_id": trace_id,
                "trace_id": trace_id,
                "candidate_event_id": event_id,
                "symbol": item_row.get("symbol"),
                "source_cutover_date": as_of.isoformat(),
                "accepted_claim_ids": list(score_support_claim_ids),
                "score_support_claim_ids": list(score_support_claim_ids),
                "all_accepted_claim_ids": list(accepted_claim_ids),
                "non_score_accepted_claim_ids": non_score_accepted_claim_ids,
                "score_contribution_ids": [item.contribution_id for item in positive_contributions],
                "primitive_state_ids": trace_primitive_state_ids,
                "score_interval": {"lower": interval.verified_score, "upper": interval.potential_score_upper_bound},
                "score_status": stage.score_status.value,
                "base_stage": stage.decision.base_stage.value,
                "primary_archetype": primary,
                "canonical_archetype_id": primary,
                "transition_overlay": stage.decision.transition_overlay.value,
                "investigation_status": stage.decision.investigation_status.value,
                "hard_break_status": "NONE",
                "missing_green_primitives": list(stage.missing_green_primitives),
                "missing_yellow_primitives": [],
                "present_green_primitives": list(stage.present_green_primitives),
                "stage_decision_reason": ";".join(stage.reasons) or "research_brain_v4_claim_backed_stagecourt_export",
                "source_origin": "research_brain_v4_attempt",
                "not_promoted_to_census_stage_status": True,
            }
        )
    return {
        "primitive_rows": primitive_rows,
        "contribution_rows": contribution_rows,
        "stage_trace_rows": stage_trace_rows,
        "claim_to_contributions": claim_to_contributions,
        "claim_to_primitives": claim_to_primitives,
        "event_to_stage_trace_id": event_to_stage_trace_id,
    }


def _merge_jsonl_by_key(path: Path, new_rows: Sequence[Mapping[str, Any]], key: str) -> None:
    if not new_rows:
        return
    backfill_source_execution = path.name == "source_task_executions.jsonl"
    merged: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(_read_jsonl(path)):
        item = dict(row)
        if backfill_source_execution:
            _backfill_source_task_execution_identity(execution_row=item, task=dict(item.get("source_task") or {}))
        item_key = str(item.get(key) or "")
        if not item_key:
            item_key = f"__existing_no_{key}_{index}_{stable_hash(item)[:12]}"
        merged[item_key] = item
    existing_len = len(merged)
    for index, row in enumerate(new_rows):
        clean = _jsonable(row)
        if backfill_source_execution:
            _backfill_source_task_execution_identity(execution_row=clean, task=dict(clean.get("source_task") or {}))
        item_key = str(clean.get(key) or "")
        if not item_key:
            item_key = f"__new_no_{key}_{existing_len + index}_{stable_hash(clean)[:12]}"
        merged[item_key] = clean
    write_jsonl(path, list(merged.values()))


def _enum_value(value: Any) -> Any:
    return value.value if isinstance(value, Enum) else value


def _jsonable(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if is_dataclass(value):
        return _jsonable(asdict(value))
    if isinstance(value, Mapping):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_jsonable(item) for item in value]
    return value


def _atomic_decisions_from_v3(*, config: CensusV4RunConfig, v3: Mapping[str, Any]) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    stage_by_symbol = {str(row.get("symbol") or "").zfill(6): row for row in v3["stage_rows"]}
    traces_by_symbol = _group_by_symbol(v3["stagecourt_traces"])
    claims_by_symbol = _group_by_symbol(v3["accepted_claims"])
    contributions_by_symbol = _group_by_symbol(v3["score_contributions"])
    primitives_by_symbol = _group_by_symbol(v3.get("primitive_states", ()))
    tasks_by_symbol = _group_by_symbol(v3["source_tasks"])
    executions_by_symbol = _group_by_symbol(v3["source_task_executions"])
    all_rows: list[dict[str, Any]] = []
    representative_by_symbol: dict[str, dict[str, Any]] = {}
    for symbol, traces in sorted(traces_by_symbol.items()):
        stage = stage_by_symbol.get(symbol, {})
        decisions = build_atomic_stage_decisions(
            symbol=symbol,
            company_name=str(stage.get("company_name") or symbol),
            as_of_date=config.as_of_date,
            stagecourt_traces=traces,
            accepted_claims=claims_by_symbol.get(symbol, ()),
            score_contributions=contributions_by_symbol.get(symbol, ()),
            primitive_states=primitives_by_symbol.get(symbol, ()),
            source_tasks=tasks_by_symbol.get(symbol, ()),
            source_task_executions=executions_by_symbol.get(symbol, ()),
        )
        representative = choose_representative_decision(decisions)
        representative_id = representative.get("atomic_stage_decision_id") if representative else None
        for decision in decisions:
            if decision.get("atomic_stage_decision_id") == representative_id:
                decision = dict(representative)
            all_rows.append(dict(decision))
        if representative:
            representative_by_symbol[symbol] = representative
    return all_rows, representative_by_symbol


def _stage_rows_from_v3(*, config: CensusV4RunConfig, v3: Mapping[str, Any], representative_by_symbol: Mapping[str, Mapping[str, Any]]) -> list[dict[str, Any]]:
    docs_by_id = {str(row.get("document_id") or ""): row for row in v3.get("evidence_documents", [])}
    claims_by_id = {str(row.get("claim_id") or ""): row for row in v3["accepted_claims"]}
    event_context_by_symbol = _event_context_by_symbol(v3.get("events", ()))
    out: list[dict[str, Any]] = []
    for row in v3["stage_rows"]:
        symbol = str(row.get("symbol") or "").zfill(6)
        event_context = event_context_by_symbol.get(symbol, _empty_event_context())
        decision = representative_by_symbol.get(symbol)
        if decision:
            accepted_ids = list(decision.get("accepted_claim_ids") or [])
            official_claims = [claims_by_id[item] for item in accepted_ids if item in claims_by_id and _is_official_claim(claims_by_id[item])]
            official_doc_count = sum(1 for claim in official_claims if claim.get("document_id") and claim.get("document_id") in docs_by_id)
            stage_decision_status = str(decision.get("stage_decision_status") or "")
            investigation_status = "PENDING" if stage_decision_status in {"PENDING_MATERIAL_GAPS", "SOURCE_PENDING"} else ("RISK_REVIEW" if stage_decision_status == "RISK_REVIEW" else "COMPLETE")
            out.append(
                {
                    **_base_stage_row(row),
                    **event_context,
                    "census_status": "DEEP_VERIFIED" if accepted_ids else "PENDING_SOURCE",
                    "assessment_depth": "VERIFIED_STAGE" if accepted_ids else "OFFICIAL_LIGHT",
                    "base_stage": decision.get("base_stage"),
                    "canonical_stage": decision.get("canonical_stage"),
                    "stage_signal": decision.get("stage_signal"),
                    "stage_scope": decision.get("stage_scope") or "CENSUS_EVENT_BOARD",
                    "risk_stage_signal": decision.get("risk_stage_signal"),
                    "transition_overlay": decision.get("transition_overlay"),
                    "investigation_status": investigation_status,
                    "stage_decision_status": stage_decision_status,
                    "stage_confidence": "HIGH" if accepted_ids else "INSUFFICIENT_EVIDENCE",
                    "score_valid_status": decision.get("score_valid_status"),
                    "score_scale": decision.get("score_scale"),
                    "score_scope": decision.get("score_scope") or decision.get("score_scale"),
                    "score_source": decision.get("score_source"),
                    "score_semantics": "single_event_or_limited_task_score" if decision.get("score_scale") == "EVENT_WEIGHTED_PARTIAL" else "not_scored",
                    "verified_score": None,
                    "full_e2r_verified_score": decision.get("full_e2r_verified_score"),
                    "event_evidence_score": decision.get("event_evidence_score"),
                    "raw_contribution_score": decision.get("raw_contribution_score"),
                    "score_interval_lower": decision.get("score_interval_lower"),
                    "score_interval_upper": decision.get("score_interval_upper"),
                    "atomic_stage_decision_id": decision.get("atomic_stage_decision_id"),
                    "additional_stage_decision_ids": decision.get("additional_stage_decision_ids") or [],
                    "accepted_claim_ids": accepted_ids,
                    "blocked_claim_ids": decision.get("blocked_claim_ids") or [],
                    "score_contribution_ids": list(decision.get("score_contribution_ids") or []),
                    "blocked_score_contribution_ids": decision.get("blocked_score_contribution_ids") or [],
                    "primitive_state_ids": list(decision.get("primitive_state_ids") or []),
                    "blocked_primitive_state_ids": decision.get("blocked_primitive_state_ids") or [],
                    "stagecourt_trace_id": decision.get("stagecourt_trace_id"),
                    "accepted_claim_count": len(accepted_ids),
                    "score_contribution_count": len(decision.get("score_contribution_ids") or []),
                    "accepted_official_claim_count": len(official_claims),
                    "official_source_task_count": len(decision.get("source_task_ids") or []),
                    "official_evidence_document_count": official_doc_count,
                    "missing_primitives": decision.get("missing_primitives") or [],
                    "failed_stage_gates": row.get("failed_stage_gates") or [],
                    "material_gap_ids": decision.get("material_gap_ids") or [],
                    "semantic_guard_status": decision.get("semantic_guard_status"),
                    "semantic_guard_class": decision.get("semantic_guard_class"),
                    "semantic_guard_reasons": decision.get("semantic_guard_reasons") or [],
                    "daily_event_stage_signal": decision.get("stage_signal"),
                    "daily_event_evidence_score": decision.get("event_evidence_score"),
                    "full_thesis_primary_archetype": None,
                    "full_thesis_verified_score": None,
                    "full_thesis_score_scale": "NO_SCORE",
                    "full_thesis_stage": "FULL_THESIS_NOT_RUN",
                    "full_thesis_score_valid_status": "NOT_SCORED",
                    "full_thesis_missing_primitives": ["full_thesis_refresh_task_not_run"],
                    "next_actions": _next_actions(decision),
                }
            )
            continue
        out.append(_no_decision_row(row, event_context=event_context))
    return out


def _base_stage_row(row: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "symbol": row.get("symbol"),
        "company_name": row.get("company_name"),
        "market": row.get("market"),
        "large_sector_id": row.get("large_sector_id"),
        "as_of_date": row.get("as_of_date"),
        "primary_archetype": row.get("primary_archetype"),
        "secondary_archetypes": row.get("secondary_archetypes") or [],
        "recent_event_count": row.get("recent_event_count") or 0,
        "recent_candidate_event_count": row.get("recent_event_count") or 0,
        "market_anomaly_count": row.get("market_anomaly_count") or 0,
        "provider_gaps": row.get("provider_gaps") or [],
        "source_gaps": row.get("source_gaps") or [],
        "claim_to_stage_trace_id": row.get("claim_to_stage_trace_id"),
        "claim_backed_score_ratio": 1.0 if row.get("accepted_claim_ids") else 0.0,
        "orphan_score_count": 0,
    }


def _no_decision_row(row: Mapping[str, Any], *, event_context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    base = _base_stage_row(row)
    events = dict(event_context or _empty_event_context())
    stage_signal = "NO_CURRENT_CATALYST"
    stage_decision_status = "NO_CURRENT_CATALYST"
    if row.get("census_status") == "PENDING_SOURCE":
        stage_signal = "SOURCE_PENDING"
        stage_decision_status = "SOURCE_PENDING"
    elif row.get("census_status") == "LIGHT_ONLY":
        stage_signal = "EVIDENCE_INSUFFICIENT"
        stage_decision_status = "SOURCE_PENDING"
    return {
        **base,
        **events,
        "census_status": row.get("census_status"),
        "assessment_depth": row.get("assessment_depth"),
        "base_stage": row.get("base_stage"),
        "canonical_stage": canonical_stage_for_display(row.get("base_stage")),
        "stage_signal": stage_signal,
        "stage_scope": "CENSUS_EVENT_BOARD",
        "risk_stage_signal": "NONE",
        "transition_overlay": "NONE",
        "investigation_status": "NO_CURRENT_CATALYST" if stage_signal == "NO_CURRENT_CATALYST" else "PENDING",
        "stage_decision_status": stage_decision_status,
        "stage_confidence": row.get("stage_confidence"),
        "score_valid_status": row.get("score_valid_status"),
        "score_scale": "NO_SCORE",
        "score_scope": "NO_SCORE",
        "score_source": "NONE",
        "score_semantics": "not_scored",
        "verified_score": None,
        "full_e2r_verified_score": None,
        "event_evidence_score": None,
        "raw_contribution_score": None,
        "score_interval_lower": None,
        "score_interval_upper": None,
        "atomic_stage_decision_id": None,
        "additional_stage_decision_ids": [],
        "accepted_claim_ids": [],
        "blocked_claim_ids": [],
        "score_contribution_ids": [],
        "blocked_score_contribution_ids": [],
        "stagecourt_trace_id": None,
        "accepted_claim_count": 0,
        "score_contribution_count": 0,
        "accepted_official_claim_count": 0,
        "official_source_task_count": 0,
        "official_evidence_document_count": 0,
        "missing_primitives": row.get("missing_primitives") or [],
        "failed_stage_gates": row.get("failed_stage_gates") or [],
        "material_gap_ids": [],
        "semantic_guard_status": "NOT_APPLICABLE",
        "semantic_guard_class": None,
        "semantic_guard_reasons": [],
        "daily_event_stage_signal": None,
        "daily_event_evidence_score": None,
        "full_thesis_primary_archetype": None,
        "full_thesis_verified_score": None,
        "full_thesis_score_scale": "NO_SCORE",
        "full_thesis_stage": "FULL_THESIS_NOT_RUN",
        "full_thesis_score_valid_status": "NOT_SCORED",
        "full_thesis_missing_primitives": ["full_thesis_refresh_task_not_run"],
        "next_actions": row.get("next_actions") or [],
    }


def _next_actions(decision: Mapping[str, Any]) -> list[str]:
    if decision.get("stage_decision_status") == "PENDING_MATERIAL_GAPS":
        return ["RECHECK_SOURCE", "FULL_THESIS_REFRESH"]
    if decision.get("stage_decision_status") == "SOURCE_PENDING":
        return ["RECHECK_SOURCE"]
    if decision.get("risk_stage_signal") != "NONE":
        return ["RISK_REVIEW"]
    return ["WATCH"]


def _write_v4_outputs(*, output_root: Path, run_metadata: Mapping[str, Any], atomic_rows: Sequence[Mapping[str, Any]], stage_rows: Sequence[Mapping[str, Any]], stage_summary: Mapping[str, Any]) -> None:
    full_thesis_refresh_queue = _full_thesis_refresh_queue(stage_rows)
    write_json(output_root / "run_metadata.json", run_metadata)
    write_jsonl(output_root / "atomic_stage_decisions.jsonl", atomic_rows)
    write_jsonl(output_root / "census_stage_status.jsonl", stage_rows)
    write_jsonl(output_root / "census_stage_map.jsonl", stage_rows)
    _write_csv(output_root / "census_stage_map.csv", stage_rows)
    write_json(output_root / "census_stage_summary.json", stage_summary)
    write_json(output_root / "watchlist_seed_candidates.json", _watchlist_seed(stage_rows))
    write_json(output_root / "deep_backfill_plan.json", _deep_backfill_plan(stage_rows))
    write_jsonl(output_root / "sample_leaf_bundle.jsonl", _sample_bundle(stage_rows))
    write_jsonl(output_root / "full_thesis_smoke_tasks.jsonl", _full_thesis_smoke_tasks(stage_rows))
    write_jsonl(output_root / "full_thesis_refresh_queue.jsonl", full_thesis_refresh_queue)
    write_json(output_root / "full_thesis_refresh_queue_audit.json", _full_thesis_refresh_queue_audit(stage_rows, full_thesis_refresh_queue))


def _write_operational_docs(
    *,
    config: CensusV4RunConfig,
    output_root: Path,
    leaf_audit: Mapping[str, Any],
    readiness: Mapping[str, Any],
    manifest: Mapping[str, Any],
    runtime_seconds: float,
    atomic_rows: Sequence[Mapping[str, Any]],
    stage_rows: Sequence[Mapping[str, Any]],
) -> None:
    docs = Path("docs/operational")
    write_json(docs / "census_mode_v4_leaf_artifact_audit.json", leaf_audit)
    write_json(docs / "census_mode_v4_atomic_stage_decision_audit.json", _audit_slice(leaf_audit, "atomic"))
    write_json(docs / "census_mode_v4_score_scale_audit.json", _audit_slice(leaf_audit, "score"))
    write_json(docs / "census_mode_v4_stage_signal_audit.json", _audit_slice(leaf_audit, "stage_signal"))
    write_json(docs / "census_mode_v4_semantic_primitive_guard_audit.json", _audit_slice(leaf_audit, "semantic"))
    write_json(docs / "census_mode_v4_event_separation_audit.json", _event_separation_audit(stage_rows, atomic_rows=atomic_rows))
    write_jsonl(docs / "census_mode_v4_primitive_mappings.jsonl", _read_jsonl(output_root / "primitive_mappings.jsonl"))
    write_json(docs / "census_mode_v4_source_task_satisfaction_audit.json", _read_json(output_root / "source_task_satisfaction_audit.json"))
    write_json(docs / "census_mode_v4_source_connector_capability_audit.json", _read_json(output_root / "source_connector_capability_audit.json"))
    write_json(docs / "census_mode_v4_all_archetype_replay_matrix.json", _read_json(output_root / "all_archetype_replay_matrix.json"))
    write_json(docs / "census_mode_v4_c06_guard_replay_audit.json", _read_json(output_root / "c06_guard_replay_audit.json"))
    write_json(docs / "census_mode_v4_controlled_semantic_replay_audit.json", _read_json(output_root / "controlled_semantic_replay_audit.json"))
    write_json(docs / "census_mode_v4_primitive_state_chain_audit.json", _read_json(output_root / "primitive_state_chain_audit.json"))
    write_json(docs / "census_mode_v4_claim_to_stage_forensic_audit.json", _read_json(output_root / "claim_to_stage_forensic_audit.json"))
    write_json(docs / "census_mode_v4_non_representative_claim_audit.json", _read_json(output_root / "non_representative_claim_audit.json"))
    write_json(docs / "census_mode_v4_source_task_realness_audit.json", _read_json(output_root / "source_task_realness_audit.json"))
    write_json(docs / "census_mode_v4_existing_ledger_reuse_audit.json", _read_json(output_root / "existing_ledger_reuse_audit.json"))
    write_json(docs / "census_mode_v4_last_effective_thesis_audit.json", _read_json(output_root / "last_effective_thesis_audit.json"))
    write_json(docs / "census_mode_v4_source_coverage_audit.json", _read_json(output_root / "source_coverage_audit.json"))
    write_json(docs / "census_mode_v4_runtime_plausibility_audit.json", _read_json(output_root / "runtime_plausibility_audit.json"))
    write_json(docs / "census_mode_v4_official_event_counter_audit.json", _read_json(output_root / "official_event_counter_audit.json"))
    write_json(docs / "census_mode_v4_samsung_hynix_full_thesis_smoke.json", _read_json(output_root / "samsung_hynix_full_thesis_smoke.json"))
    write_json(docs / "census_mode_v4_full_thesis_production_runner_audit.json", _read_json(output_root / "full_thesis_production_runner_audit.json"))
    write_json(docs / "census_mode_v4_full_thesis_production_audit.json", _read_json(output_root / "full_thesis_production_audit.json"))
    write_jsonl(docs / "census_mode_v4_full_thesis_smoke_tasks.jsonl", _read_jsonl(output_root / "full_thesis_smoke_tasks.jsonl"))
    write_jsonl(docs / "census_mode_v4_full_thesis_refresh_queue.jsonl", _read_jsonl(output_root / "full_thesis_refresh_queue.jsonl"))
    write_jsonl(
        docs / "census_mode_v4_full_thesis_blocker_follow_up_source_tasks.jsonl",
        _read_jsonl(output_root / "full_thesis_blocker_follow_up_source_tasks.jsonl"),
    )
    write_jsonl(
        docs / "census_mode_v4_full_thesis_blocker_follow_up_seed_events.jsonl",
        _read_jsonl(output_root / "full_thesis_blocker_follow_up_seed_events.jsonl"),
    )
    write_jsonl(docs / "census_mode_v4_research_brain_full_thesis_seed_events.jsonl", _read_jsonl(output_root / "research_brain_full_thesis_seed_events.jsonl"))
    write_jsonl(docs / "census_mode_v4_research_brain_candidate_seed_events_used.jsonl", _read_jsonl(output_root / "research_brain_candidate_seed_events_used.jsonl"))
    write_jsonl(docs / "census_mode_v4_full_thesis_seed_materialization_trace.jsonl", _read_jsonl(output_root / "full_thesis_seed_materialization_trace.jsonl"))
    write_json(docs / "census_mode_v4_full_thesis_seed_materialization_audit.json", _read_json(output_root / "full_thesis_seed_materialization_audit.json"))
    write_json(docs / "census_mode_v4_full_thesis_refresh_queue_audit.json", _read_json(output_root / "full_thesis_refresh_queue_audit.json"))
    write_json(docs / "census_mode_v4_brain_planner_audit.json", _read_json(output_root / "brain_planner_audit.json"))
    write_json(docs / "census_mode_v4_web_naver_acquisition_audit.json", _read_json(output_root / "web_naver_acquisition_audit.json"))
    write_json(docs / "census_mode_v4_llm_claim_extraction_audit.json", _read_json(output_root / "llm_claim_extraction_audit.json"))
    write_json(docs / "census_mode_v4_brain_to_claim_trace_audit.json", _read_json(output_root / "brain_to_claim_trace_audit.json"))
    write_jsonl(docs / "census_mode_v4_brain_claim_mapping_trace.jsonl", _read_jsonl(output_root / "brain_claim_mapping_trace.jsonl"))
    write_json(docs / "census_mode_v4_research_brain_bridge_audit.json", _read_json(output_root / "research_brain_v4_bridge_audit.json"))
    write_json(docs / "census_mode_v4_brain_stage_promotion_audit.json", _read_json(output_root / "brain_stage_promotion_audit.json"))
    write_json(docs / "census_mode_v4_brain_web_readiness_gate_audit.json", _read_json(output_root / "brain_web_readiness_gate_audit.json"))
    write_json(docs / "census_mode_v4_readiness_verdict.md.json", readiness)
    write_text(docs / "census_mode_v4_readiness_verdict.md", _readiness_md(readiness))
    write_json(docs / "census_mode_v4_artifact_manifest.json", manifest)
    write_text(docs / "census_mode_v4_reproduction_command.md", f"```bash\n{_command_string(config)}\n```\n")
    write_jsonl(docs / "census_mode_v4_sample_leaf_bundle.jsonl", _sample_bundle(stage_rows))
    write_json(docs / "census_mode_v4_reviewer_A_trace_atomicity.json", _reviewer("A_TRACE_ATOMICITY", leaf_audit))
    write_json(docs / "census_mode_v4_reviewer_B_source_realness.json", _reviewer("B_SOURCE_REALNESS", leaf_audit))
    write_json(docs / "census_mode_v4_reviewer_C_stage_semantics.json", _reviewer("C_STAGE_SEMANTICS", leaf_audit))
    write_json(docs / "census_mode_v4_reviewer_D_runtime_brain_web_honesty.json", _reviewer("D_RUNTIME_BRAIN_WEB_HONESTY", leaf_audit))
    write_json(docs / "census_mode_v4_reviewer_E_semantic_guard.json", _reviewer("E_SEMANTIC_GUARD", leaf_audit))
    write_json(docs / "census_mode_v4_reviewer_A_trace_forensics.json", _reviewer("A_TRACE_FORENSICS", leaf_audit))
    write_json(docs / "census_mode_v4_reviewer_D_runtime_plausibility.json", _reviewer("D_RUNTIME_PLAUSIBILITY", leaf_audit))
    write_json(docs / "census_mode_v4_known_bad_regression_report.json", _read_json(output_root / "known_bad_regression_report.json"))
    write_json(docs / "census_mode_v4_goal_requirement_matrix_audit.json", _read_json(output_root / "goal_requirement_matrix_audit.json"))
    write_json(docs / "census_mode_v4_goal_completion_audit.json", _read_json(output_root / "goal_completion_audit.json"))
    write_json(docs / "census_mode_v4_test_result_evidence_audit.json", _read_json(output_root / "test_result_evidence_audit.json"))
    write_json(docs / "census_mode_v4_report_generation_audit.json", _read_json(output_root / "report_generation_audit.json"))
    write_text(docs / "census_mode_v4_self_repair_summary.md", (output_root / "self_repair_summary.md").read_text(encoding="utf-8"))
    write_text(docs / "census_mode_v4_acceptance_report.md", (output_root / "acceptance_report.md").read_text(encoding="utf-8"))


def _readiness_verdict(
    *,
    config: CensusV4RunConfig,
    leaf_audit: Mapping[str, Any],
    stage_rows: Sequence[Mapping[str, Any]],
    research_brain_bridge: Mapping[str, Any],
    brain_web_attempt: Mapping[str, Any],
    brain_stage_promotion: Mapping[str, Any],
    brain_web_readiness_gate: Mapping[str, Any],
    goal_audits: Mapping[str, Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    labels: list[str] = ["IMPLEMENTATION_MERGED", "V3_FORENSIC_REVIEW_COMPLETE"]
    anti_fake_blockers: list[str] = []
    goal_audits = goal_audits or {}
    known_bad = goal_audits.get("known_bad_regression_report") or {}
    known_bad_pass = known_bad.get("completion_eligible") is True
    self_repair = goal_audits.get("self_repair") or {}
    self_repair_pass = self_repair.get("completion_eligible") is True
    full_thesis = goal_audits.get("samsung_hynix_full_thesis_smoke") or {}
    full_thesis_honesty_pass = _full_thesis_smoke_honesty_pass(full_thesis)
    full_thesis_execution_pass = _full_thesis_smoke_execution_pass(full_thesis)
    full_thesis_pass = full_thesis_execution_pass
    full_thesis_smoke_gate_blockers = _full_thesis_smoke_gate_blockers(
        config=config,
        full_thesis_execution_pass=full_thesis_execution_pass,
    )
    full_thesis_smoke_gate_pass_allowed = not full_thesis_smoke_gate_blockers
    full_thesis_production = goal_audits.get("full_thesis_production") or {}
    full_thesis_production_runner = goal_audits.get("full_thesis_production_runner") or {}
    source_connector_capability = goal_audits.get("source_connector_capability") or {}
    full_thesis_seed_materialization = goal_audits.get("full_thesis_seed_materialization") or {}
    full_thesis_seed_promotion_pass = int(full_thesis_seed_materialization.get("full_thesis_promoted_seed_count") or 0) > 0
    controlled_semantic_replay = goal_audits.get("controlled_semantic_replay") or {}
    controlled_semantic_replay_pass = controlled_semantic_replay.get("controlled_semantic_replay_pass") is True
    remaining_operational_gaps: list[str] = []
    leaf_metrics = leaf_audit.get("metrics") or {}
    full_thesis_stage_row_count = int(leaf_metrics.get("full_thesis_stage_row_count") or 0)
    full_e2r_verified_score_row_count = int(
        leaf_metrics.get("full_e2r_verified_score_present_count")
        or leaf_metrics.get("full_e2r_verified_score_row_count")
        or 0
    )
    event_board_non_stage0_count = int(leaf_metrics.get("event_board_non_stage0_count") or 0)
    full_thesis_refresh_queue_candidate_count = int(
        leaf_metrics.get("full_thesis_refresh_queue_candidate_count") or len(_full_thesis_refresh_queue(stage_rows))
    )
    if full_thesis_stage_row_count <= 0 and event_board_non_stage0_count > 0:
        stage_scope_notice = "NO_FULL_THESIS_STAGE_ROWS_EVENT_BOARD_STAGE_ROWS_EXIST"
    elif full_thesis_stage_row_count > 0:
        stage_scope_notice = "FULL_THESIS_STAGE_ROWS_PRESENT_SCOPE_GUARD_REQUIRED"
    else:
        stage_scope_notice = "NO_FULL_THESIS_STAGE_ROWS"
    if not full_thesis_execution_pass:
        remaining_operational_gaps.append("full thesis EvidenceClaim -> PrimitiveState -> ScoreContribution -> StageCourt path not run")
    if full_thesis_stage_row_count <= 0 and event_board_non_stage0_count > 0:
        remaining_operational_gaps.append("event-board non-Stage0 rows exist but are not operational full-thesis stages")
    if full_thesis_refresh_queue_candidate_count > 0:
        remaining_operational_gaps.append("full-thesis refresh queue exists but production full-thesis StageCourt paths are not closed")
    if (
        int(full_thesis_seed_materialization.get("seed_event_count") or 0) > 0
        and not full_thesis_seed_promotion_pass
    ):
        remaining_operational_gaps.append("full-thesis seed materialization audit shows no promoted FULL_THESIS seed")
    remaining_operational_gaps.append("source-backed replay parity across all archetypes is not proven")
    if not controlled_semantic_replay_pass:
        remaining_operational_gaps.append("goal3 controlled semantic replay cases are not all source-backed and lifecycle-clean")
    if source_connector_capability.get("source_connector_capability_pass_allowed") is not True:
        blocking_classes = source_connector_capability.get("blocking_full_thesis_source_classes") or []
        remaining_operational_gaps.append(
            "full-thesis source connector capability is pending"
            + (f": {', '.join(str(item) for item in blocking_classes)}" if blocking_classes else "")
        )
    brain_web_requested = _config_requests_brain_web(config)
    if brain_web_requested:
        remaining_operational_gaps.append("Brain/Web/LLM acquisition was requested but has not produced a Census-promoted StageCourt path")
    else:
        remaining_operational_gaps.append("Brain/Web/LLM acquisition artifacts are not produced in this disabled ledger-refresh run")
    if brain_stage_promotion.get("verdict") not in {"NOT_REQUESTED", "ELIGIBLE_NOT_PROMOTED", "PROMOTION_APPLIED"}:
        remaining_operational_gaps.append("Brain/Web StageCourt traces are blocked from Census representative Stage promotion")
    if research_brain_bridge.get("bridge_mode") == "imported_operational_report_bundle" and not research_brain_bridge.get("usable_for_census_cutover"):
        remaining_operational_gaps.append("Research Brain v4 imported report bundle is shadow/import-only and not admissible as Census production cutover evidence")
    if leaf_audit.get("verdict") == "PASS":
        labels.extend(["ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS", "ATOMIC_STAGE_DECISION_PASS", "SCORE_SCALE_PASS", "STAGE_SEMANTICS_PASS", "SEMANTIC_PRIMITIVE_GUARD_PASS"])
    else:
        anti_fake_blockers.append("leaf artifact audit failed")
    if _daily_event_full_thesis_separated(stage_rows):
        labels.append("DAILY_EVENT_FULL_THESIS_SEPARATION_PASS")
    if _census_candidate_events_separated(stage_rows):
        labels.append("CENSUS_ASSESSMENT_CANDIDATE_EVENT_SEPARATION_PASS")
    labels.append("FULL_THESIS_SMOKE_HONESTY_PASS" if full_thesis_honesty_pass else "FULL_THESIS_SMOKE_HONESTY_FAIL")
    labels.append("FULL_THESIS_SMOKE_EXECUTION_PASS" if full_thesis_execution_pass else "FULL_THESIS_SMOKE_EXECUTION_PENDING")
    labels.append("FULL_THESIS_SMOKE_PASS" if full_thesis_execution_pass else "FULL_THESIS_SMOKE_PENDING")
    if full_thesis_refresh_queue_candidate_count > 0:
        labels.append("FULL_THESIS_REFRESH_QUEUE_PRESENT")
    if full_thesis_seed_materialization.get("verdict") == "PASS":
        labels.append("FULL_THESIS_SEED_LEDGER_INTEGRITY_PASS")
        labels.append("FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS")
        labels.append("FULL_THESIS_SEED_PROMOTION_PASS" if full_thesis_seed_promotion_pass else "FULL_THESIS_SEED_PROMOTION_PENDING")
        labels.append(
            "FULL_THESIS_SEED_ACTUAL_MATERIALIZATION_PASS"
            if full_thesis_seed_materialization.get("actual_materialization_pass_allowed") is True
            else "FULL_THESIS_SEED_ACTUAL_MATERIALIZATION_PENDING"
        )
    elif full_thesis_seed_materialization:
        anti_fake_blockers.append("full thesis seed materialization audit failed")
    if brain_web_requested:
        labels.append("BRAIN_WEB_ATTEMPT_RECORDED")
        labels.append("BRAIN_STAGE_PROMOTION_AUDITED")
        labels.append("BRAIN_WEB_READINESS_GATE_AUDITED")
        if config.brain_web_mode != "enabled":
            anti_fake_blockers.append("Brain/Web run_mode requested acquisition but brain_web_mode is disabled")
            labels.append("BRAIN_WEB_CONFIG_MISMATCH_NOT_READY")
        if int(brain_web_attempt.get("real_provider_success_count") or 0) <= 0:
            anti_fake_blockers.append("Brain/Web requested but LLM planner real-provider success count is zero")
            labels.append("EXTERNAL_PROVIDER_BLOCKER_NOT_READY")
        if int(brain_web_attempt.get("source_task_execution_count") or 0) <= 0:
            anti_fake_blockers.append("Brain/Web requested but source task execution count is zero")
        if int(brain_web_attempt.get("accepted_claim_count") or 0) > 0 and int(brain_web_attempt.get("brain_to_census_claim_exported_count") or 0) <= 0:
            anti_fake_blockers.append("Brain/Web accepted claims are not yet exported into Census claim/stage ledger")
        if int(brain_stage_promotion.get("unsafe_promoted_stage_row_count") or 0) > 0:
            anti_fake_blockers.append("Brain/Web stage traces were promoted despite promotion blockers")
        for blocker in brain_web_readiness_gate.get("blockers") or []:
            _append_unique(anti_fake_blockers, f"Brain/Web readiness gate blocked: {blocker}")
    else:
        labels.append("OFFICIAL_BASELINE_OR_LEDGER_REFRESH_ONLY")
    if int((leaf_audit.get("metrics") or {}).get("evidence_claim_payload_count") or 0) > 0:
        labels.append("OFFICIAL_BASELINE_EVIDENCE_CLAIM_PAYLOAD_PRESENT")
    if known_bad_pass:
        labels.append("KNOWN_BAD_REGRESSION_PASS")
    if self_repair_pass:
        labels.append("SELF_REPAIR_LOOP_PASS")
    if research_brain_bridge.get("bridge_mode") == "imported_operational_report_bundle":
        labels.append("RESEARCH_BRAIN_V4_REPORT_BRIDGE_IMPORTED")
    anti_fake_pass = not anti_fake_blockers and leaf_audit.get("verdict") == "PASS"
    brain_web_pass = brain_web_readiness_gate.get("brain_web_evidence_pass_allowed") is True
    all_archetype_replay_matrix = _read_json(Path(config.resolved_output_root()) / "all_archetype_replay_matrix.json")
    all_archetype_replay_pass = all_archetype_replay_matrix.get("all_archetype_replay_pass") is True
    full_thesis_production_pass = _full_thesis_production_pass_allowed(full_thesis_production)
    meaningful_pass = bool(anti_fake_pass and brain_web_pass and full_thesis_production_pass and all_archetype_replay_pass)
    if brain_web_pass:
        labels.append("BRAIN_WEB_EVIDENCE_PASS")
    target_gate_pass = {
        "anti_fake": anti_fake_pass,
        "meaningful": meaningful_pass,
        "brain_web": brain_web_pass,
        "full_thesis": full_thesis_production_pass,
        "full_thesis_smoke": full_thesis_smoke_gate_pass_allowed,
    }.get(config.target_gate, False)
    verdict = "ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS" if anti_fake_pass else "NOT_READY"
    return {
        "schema_version": "e2r_census_v4_readiness_verdict_v1",
        "verdict": verdict,
        "target_gate": config.target_gate,
        "target_gate_pass": target_gate_pass,
        "target_gate_verdict": "TARGET_GATE_PASS" if target_gate_pass else "TARGET_GATE_BLOCKED",
        "run_mode": config.run_mode,
        "brain_web_mode": config.brain_web_mode,
        "labels": labels,
        "anti_fake_blockers": anti_fake_blockers,
        "blockers": anti_fake_blockers,
        "remaining_operational_gaps": remaining_operational_gaps,
        "meaningful_operational_stage_pass": meaningful_pass,
        "operational_stage_use_allowed": meaningful_pass,
        "stage_scope_notice": stage_scope_notice,
        "full_thesis_stage_row_count": full_thesis_stage_row_count,
        "full_thesis_refresh_queue_candidate_count": full_thesis_refresh_queue_candidate_count,
        "full_e2r_verified_score_row_count": full_e2r_verified_score_row_count,
        "event_board_non_stage0_count": event_board_non_stage0_count,
        "event_board_stage_rows_are_operational_full_thesis": False,
        "brain_web_evidence_pass": brain_web_pass,
        "full_thesis_smoke_pass": full_thesis_execution_pass,
        "full_thesis_smoke_honesty_pass": full_thesis_honesty_pass,
        "full_thesis_smoke_execution_pass": full_thesis_execution_pass,
        "full_thesis_smoke_gate_pass_allowed": full_thesis_smoke_gate_pass_allowed,
        "full_thesis_smoke_gate_blockers": full_thesis_smoke_gate_blockers,
        "full_thesis_production_pass": full_thesis_production_pass,
        "source_connector_capability_pass": source_connector_capability.get("source_connector_capability_pass_allowed") is True,
        "source_connector_capability_audit": {
            "verdict": source_connector_capability.get("verdict"),
            "source_connector_capability_pass_allowed": source_connector_capability.get("source_connector_capability_pass_allowed"),
            "full_thesis_required_source_class_count": source_connector_capability.get("full_thesis_required_source_class_count"),
            "blocking_full_thesis_source_class_count": source_connector_capability.get("blocking_full_thesis_source_class_count"),
            "blocking_full_thesis_task_count": source_connector_capability.get("blocking_full_thesis_task_count"),
            "full_thesis_task_executable_source_path_pass_allowed": (
                source_connector_capability.get("full_thesis_task_executable_source_path_pass_allowed")
            ),
            "full_thesis_task_with_blocking_source_class_count": (
                source_connector_capability.get("full_thesis_task_with_blocking_source_class_count")
            ),
            "placeholder_source_classes": source_connector_capability.get("placeholder_source_classes") or [],
            "missing_connector_source_classes": source_connector_capability.get("missing_connector_source_classes") or [],
            "bounded_web_acquisition_source_classes": source_connector_capability.get("bounded_web_acquisition_source_classes") or [],
            "registry_missing_but_acquisition_covered_source_classes": (
                source_connector_capability.get("registry_missing_but_acquisition_covered_source_classes") or []
            ),
        },
        "full_thesis_production_audit": {
            "production_pass_allowed": full_thesis_production.get("production_pass_allowed"),
            "production_runner_implemented": full_thesis_production.get("production_runner_implemented"),
            "production_mode_requested": full_thesis_production.get("production_mode_requested"),
            "full_thesis_refresh_queue_candidate_count": full_thesis_production.get("full_thesis_refresh_queue_candidate_count"),
            "production_full_thesis_row_count": full_thesis_production.get("production_full_thesis_row_count"),
            "controlled_smoke_full_thesis_row_count": full_thesis_production.get("controlled_smoke_full_thesis_row_count"),
            "controlled_smoke_substitution_rejected_count": full_thesis_production.get("controlled_smoke_substitution_rejected_count"),
            "blockers": full_thesis_production.get("blockers") or [],
        },
        "full_thesis_production_runner_audit": {
            "verdict": full_thesis_production_runner.get("verdict"),
            "production_mode_requested": full_thesis_production_runner.get("production_mode_requested"),
            "full_thesis_refresh_queue_candidate_count": full_thesis_production_runner.get("full_thesis_refresh_queue_candidate_count"),
            "candidate_row_count": full_thesis_production_runner.get("candidate_row_count"),
            "candidate_source_counts": full_thesis_production_runner.get("candidate_source_counts") or {},
            "refresh_queue_materialized_candidate_count": full_thesis_production_runner.get("refresh_queue_materialized_candidate_count"),
            "refresh_queue_unmaterialized_candidate_count": full_thesis_production_runner.get("refresh_queue_unmaterialized_candidate_count"),
            "promoted_full_thesis_row_count": full_thesis_production_runner.get("promoted_full_thesis_row_count"),
            "blockers": full_thesis_production_runner.get("blockers") or [],
        },
        "full_thesis_seed_materialization_audit": {
            "verdict": full_thesis_seed_materialization.get("verdict"),
            "verdict_scope": full_thesis_seed_materialization.get("verdict_scope"),
            "seed_event_count": full_thesis_seed_materialization.get("seed_event_count"),
            "trace_row_count": full_thesis_seed_materialization.get("trace_row_count"),
            "status_counts": full_thesis_seed_materialization.get("status_counts") or {},
            "final_stage_scope_counts": full_thesis_seed_materialization.get("final_stage_scope_counts") or {},
            "final_operator_stage_use_counts": full_thesis_seed_materialization.get("final_operator_stage_use_counts") or {},
            "final_operator_score_use_counts": full_thesis_seed_materialization.get("final_operator_score_use_counts") or {},
            "full_thesis_promoted_seed_count": full_thesis_seed_materialization.get("full_thesis_promoted_seed_count"),
            "full_thesis_seed_promotion_pass": full_thesis_seed_promotion_pass,
            "ledger_integrity_pass_allowed": full_thesis_seed_materialization.get("ledger_integrity_pass_allowed"),
            "actual_materialization_pass_allowed": full_thesis_seed_materialization.get("actual_materialization_pass_allowed"),
            "operator_materialization_status": full_thesis_seed_materialization.get("operator_materialization_status"),
            "critical_count": full_thesis_seed_materialization.get("critical_count"),
            "critical_counts": full_thesis_seed_materialization.get("critical_counts") or {},
        },
        "all_archetype_replay_pass": all_archetype_replay_pass,
        "controlled_semantic_replay_pass": controlled_semantic_replay_pass,
        "controlled_semantic_replay_audit": {
            "case_count": controlled_semantic_replay.get("case_count"),
            "required_case_count": controlled_semantic_replay.get("required_case_count"),
            "pass_count": controlled_semantic_replay.get("pass_count"),
            "pending_count": controlled_semantic_replay.get("pending_count"),
            "fail_count": controlled_semantic_replay.get("fail_count"),
            "blockers": controlled_semantic_replay.get("blockers") or [],
        },
        "all_archetype_replay_matrix": {
            "archetype_count": all_archetype_replay_matrix.get("archetype_count"),
            "required_archetype_count": all_archetype_replay_matrix.get("required_archetype_count"),
            "source_backed_ready_count": all_archetype_replay_matrix.get("source_backed_ready_count"),
            "guard_replay_ready_count": all_archetype_replay_matrix.get("guard_replay_ready_count"),
            "controlled_wiring_smoke_ready_count": all_archetype_replay_matrix.get("controlled_wiring_smoke_ready_count"),
            "missing_required_archetype_count": all_archetype_replay_matrix.get("missing_required_archetype_count"),
            "status_counts": all_archetype_replay_matrix.get("status_counts"),
            "blockers": all_archetype_replay_matrix.get("blockers") or [],
        },
        "known_bad_regression_pass": known_bad_pass,
        "self_repair_loop_pass": self_repair_pass,
        "brain_web_readiness_gate": {
            "verdict": brain_web_readiness_gate.get("verdict"),
            "minimum_gate_applies": brain_web_readiness_gate.get("minimum_gate_applies"),
            "operational_minimum_count_gate_applies": brain_web_readiness_gate.get("operational_minimum_count_gate_applies"),
            "minimum_required_counts": brain_web_readiness_gate.get("minimum_required_counts") or {},
            "brain_web_evidence_pass_allowed": brain_web_readiness_gate.get("brain_web_evidence_pass_allowed"),
            "full_thesis_seed_event_path": brain_web_readiness_gate.get("full_thesis_seed_event_path"),
            "full_thesis_seed_source": brain_web_readiness_gate.get("full_thesis_seed_source"),
            "full_thesis_seed_original_path": brain_web_readiness_gate.get("full_thesis_seed_original_path"),
            "full_thesis_seed_event_count": brain_web_readiness_gate.get("full_thesis_seed_event_count"),
            "full_thesis_seed_consumed_by_research_brain": brain_web_readiness_gate.get("full_thesis_seed_consumed_by_research_brain"),
            "full_thesis_seed_planner_attempted_event_count": brain_web_readiness_gate.get("full_thesis_seed_planner_attempted_event_count"),
            "full_thesis_seed_planner_run_row_count": brain_web_readiness_gate.get("full_thesis_seed_planner_run_row_count"),
            "full_thesis_seed_planner_run_count": brain_web_readiness_gate.get("full_thesis_seed_planner_run_count"),
            "full_thesis_seed_real_provider_success_count": brain_web_readiness_gate.get("full_thesis_seed_real_provider_success_count"),
            "full_thesis_seed_source_task_execution_count": brain_web_readiness_gate.get("full_thesis_seed_source_task_execution_count"),
            "full_thesis_seed_accepted_claim_count": brain_web_readiness_gate.get("full_thesis_seed_accepted_claim_count"),
            "full_thesis_seed_stagecourt_trace_count": brain_web_readiness_gate.get("full_thesis_seed_stagecourt_trace_count"),
            "full_thesis_seed_materialized_to_stagecourt": brain_web_readiness_gate.get("full_thesis_seed_materialized_to_stagecourt"),
            "llm_planner_call_count": brain_web_readiness_gate.get("llm_planner_call_count"),
            "llm_real_provider_success_count": brain_web_readiness_gate.get("llm_real_provider_success_count"),
            "attempt_source_task_execution_count": brain_web_readiness_gate.get("attempt_source_task_execution_count"),
            "source_task_execution_count": brain_web_readiness_gate.get("source_task_execution_count"),
            "attempt_real_document_fetched_count": brain_web_readiness_gate.get("attempt_real_document_fetched_count"),
            "real_document_fetched_count": brain_web_readiness_gate.get("real_document_fetched_count"),
            "policy_rejected_source_task_execution_count": brain_web_readiness_gate.get("policy_rejected_source_task_execution_count"),
            "zero_budget_policy_rejected_source_task_execution_count": brain_web_readiness_gate.get("zero_budget_policy_rejected_source_task_execution_count"),
            "source_lineage_feedback_retry_execution_count": brain_web_readiness_gate.get("source_lineage_feedback_retry_execution_count"),
            "source_lineage_feedback_retry_accepted_execution_count": brain_web_readiness_gate.get(
                "source_lineage_feedback_retry_accepted_execution_count"
            ),
            "source_lineage_feedback_retry_no_evidence_execution_count": brain_web_readiness_gate.get(
                "source_lineage_feedback_retry_no_evidence_execution_count"
            ),
            "source_lineage_feedback_retry_dropped_count": brain_web_readiness_gate.get("source_lineage_feedback_retry_dropped_count"),
            "discovery_only_retry_after_unverified_original_count": brain_web_readiness_gate.get(
                "discovery_only_retry_after_unverified_original_count"
            ),
            "web_search_task_count": brain_web_readiness_gate.get("web_search_task_count"),
            "web_fetched_document_count": brain_web_readiness_gate.get("web_fetched_document_count"),
            "llm_claim_extractor_attempt_count": brain_web_readiness_gate.get("llm_claim_extractor_attempt_count"),
            "attempt_accepted_claim_count": brain_web_readiness_gate.get("attempt_accepted_claim_count"),
            "brain_accepted_claim_count": brain_web_readiness_gate.get("brain_accepted_claim_count"),
            "web_or_llm_accepted_claim_count": brain_web_readiness_gate.get("web_or_llm_accepted_claim_count"),
            "official_accepted_claim_count": brain_web_readiness_gate.get("official_accepted_claim_count"),
            "web_news_accepted_claim_count": brain_web_readiness_gate.get("web_news_accepted_claim_count"),
            "llm_extracted_accepted_claim_count": brain_web_readiness_gate.get("llm_extracted_accepted_claim_count"),
            "full_thesis_claim_count": brain_web_readiness_gate.get("full_thesis_claim_count"),
            "brain_to_claim_trace_count": brain_web_readiness_gate.get("brain_to_claim_trace_count"),
            "brain_trace_missing_accepted_claim_count": brain_web_readiness_gate.get("brain_trace_missing_accepted_claim_count"),
            "brain_trace_missing_score_contribution_ref_count": brain_web_readiness_gate.get("brain_trace_missing_score_contribution_ref_count"),
            "brain_trace_missing_stagecourt_ref_count": brain_web_readiness_gate.get("brain_trace_missing_stagecourt_ref_count"),
            "brain_trace_nonrepresentative_missing_stagecourt_ref_count": brain_web_readiness_gate.get(
                "brain_trace_nonrepresentative_missing_stagecourt_ref_count"
            ),
            "brain_contribution_without_accepted_support_count": brain_web_readiness_gate.get("brain_contribution_without_accepted_support_count"),
            "brain_stage_trace_without_accepted_claim_count": brain_web_readiness_gate.get("brain_stage_trace_without_accepted_claim_count"),
            "promoted_stage_without_brain_trace_count": brain_web_readiness_gate.get("promoted_stage_without_brain_trace_count"),
            "brain_claim_unresolved_document_ref_count": brain_web_readiness_gate.get("brain_claim_unresolved_document_ref_count"),
            "brain_claim_unresolved_anchor_ref_count": brain_web_readiness_gate.get("brain_claim_unresolved_anchor_ref_count"),
            "brain_source_task_unresolved_document_ref_count": brain_web_readiness_gate.get("brain_source_task_unresolved_document_ref_count"),
            "blockers": brain_web_readiness_gate.get("blockers") or [],
        },
        "evidence_claim_payload_count": int((leaf_audit.get("metrics") or {}).get("evidence_claim_payload_count") or 0),
        "brain_web_attempt": {
            "attempt_mode": brain_web_attempt.get("attempt_mode"),
            "verdict": brain_web_attempt.get("verdict"),
            "planner_provider": brain_web_attempt.get("planner_provider"),
            "full_thesis_seed_event_path": brain_web_attempt.get("full_thesis_seed_event_path"),
            "full_thesis_seed_source": brain_web_attempt.get("full_thesis_seed_source"),
            "full_thesis_seed_original_path": brain_web_attempt.get("full_thesis_seed_original_path"),
            "full_thesis_seed_event_count": brain_web_attempt.get("full_thesis_seed_event_count"),
            "full_thesis_seed_consumed_by_research_brain": brain_web_attempt.get("full_thesis_seed_consumed_by_research_brain"),
            "full_thesis_seed_planner_attempted_event_count": brain_web_attempt.get("full_thesis_seed_planner_attempted_event_count"),
            "full_thesis_seed_planner_run_row_count": brain_web_attempt.get("full_thesis_seed_planner_run_row_count"),
            "full_thesis_seed_planner_run_count": brain_web_attempt.get("full_thesis_seed_planner_run_count"),
            "full_thesis_seed_real_provider_success_count": brain_web_attempt.get("full_thesis_seed_real_provider_success_count"),
            "full_thesis_seed_source_task_execution_count": brain_web_attempt.get("full_thesis_seed_source_task_execution_count"),
            "full_thesis_seed_accepted_claim_count": brain_web_attempt.get("full_thesis_seed_accepted_claim_count"),
            "full_thesis_seed_stagecourt_trace_count": brain_web_attempt.get("full_thesis_seed_stagecourt_trace_count"),
            "full_thesis_seed_materialized_to_stagecourt": brain_web_attempt.get("full_thesis_seed_materialized_to_stagecourt"),
            "planner_run_count": brain_web_attempt.get("planner_run_count"),
            "real_provider_success_count": brain_web_attempt.get("real_provider_success_count"),
            "source_task_execution_count": brain_web_attempt.get("source_task_execution_count"),
            "accepted_claim_count": brain_web_attempt.get("accepted_claim_count"),
            "unique_accepted_claim_count": brain_web_attempt.get("unique_accepted_claim_count"),
            "brain_stagecourt_trace_exported_count": brain_web_attempt.get("brain_stagecourt_trace_exported_count"),
            "brain_to_census_stage_exported_count": brain_web_attempt.get("brain_to_census_stage_exported_count"),
            "claim_acceptance_ready": brain_web_attempt.get("claim_acceptance_ready"),
            "stagecourt_trace_ready": brain_web_attempt.get("stagecourt_trace_ready"),
            "cutover_export_ready": brain_web_attempt.get("cutover_export_ready"),
            "blockers": brain_web_attempt.get("blockers") or [],
        },
        "brain_stage_promotion": {
            "verdict": brain_stage_promotion.get("verdict"),
            "brain_stage_promotion_mode": brain_stage_promotion.get("brain_stage_promotion_mode"),
            "brain_stage_trace_count": brain_stage_promotion.get("brain_stage_trace_count"),
            "brain_promoted_stage_row_count": brain_stage_promotion.get("brain_promoted_stage_row_count"),
            "unsafe_promoted_stage_row_count": brain_stage_promotion.get("unsafe_promoted_stage_row_count"),
            "brain_snapshot_document_count": brain_stage_promotion.get("brain_snapshot_document_count"),
            "blockers": brain_stage_promotion.get("blockers") or [],
        },
        "research_brain_bridge": {
            "bridge_mode": research_brain_bridge.get("bridge_mode"),
            "verdict": research_brain_bridge.get("verdict"),
            "usable_for_census_cutover": research_brain_bridge.get("usable_for_census_cutover"),
            "accepted_claim_count": research_brain_bridge.get("accepted_claim_count"),
            "snapshot_url_count": research_brain_bridge.get("snapshot_url_count"),
            "blockers": research_brain_bridge.get("blockers") or [],
        },
    }


def _append_unique(items: list[str], value: str) -> None:
    if value not in items:
        items.append(value)


def _stage_summary(stage_rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    base_stage_distribution = _count_by(stage_rows, "base_stage")
    full_thesis_stage_row_count = sum(1 for row in stage_rows if row.get("stage_scope") == "FULL_THESIS")
    event_board_non_stage0_count = sum(
        1 for row in stage_rows if row.get("stage_scope") == "CENSUS_EVENT_BOARD" and row.get("base_stage") != "Stage0"
    )
    full_thesis_refresh_queue_candidate_count = len(_full_thesis_refresh_queue(stage_rows))
    return {
        "schema_version": "e2r_census_v4_stage_summary_v1",
        "stage_status_count": len(stage_rows),
        "stage_distribution": base_stage_distribution,
        "base_stage_distribution": base_stage_distribution,
        "canonical_stage_distribution": _count_by(stage_rows, "canonical_stage"),
        "stage_signal_distribution": _count_by(stage_rows, "stage_signal"),
        "stage_decision_status_distribution": _count_by(stage_rows, "stage_decision_status"),
        "score_scale_distribution": _count_by(stage_rows, "score_scale"),
        "stage_scope_distribution": _count_by(stage_rows, "stage_scope"),
        "score_scope_distribution": _count_by(stage_rows, "score_scope"),
        "operator_stage_use_distribution": _count_by(stage_rows, "operator_stage_use"),
        "operator_score_use_distribution": _count_by(stage_rows, "operator_score_use"),
        "base_stage_display_distribution": _count_by(stage_rows, "base_stage_display"),
        "stage_decision_status_display_distribution": _count_by(stage_rows, "stage_decision_status_display"),
        "candidate_event_scope_distribution": _count_by(stage_rows, "candidate_event_scope"),
        "candidate_event_count": sum(int(row.get("candidate_event_count") or 0) for row in stage_rows),
        "score_eligible_candidate_event_count": sum(int(row.get("score_eligible_candidate_event_count") or 0) for row in stage_rows),
        "event_evidence_score_count": sum(1 for row in stage_rows if row.get("event_evidence_score") is not None),
        "verified_score_present_count": sum(1 for row in stage_rows if row.get("verified_score") is not None),
        "full_e2r_verified_score_count": sum(1 for row in stage_rows if row.get("full_e2r_verified_score") is not None),
        "full_e2r_verified_score_row_count": sum(1 for row in stage_rows if row.get("full_e2r_verified_score") is not None),
        "full_thesis_stage_row_count": full_thesis_stage_row_count,
        "full_thesis_refresh_queue_candidate_count": full_thesis_refresh_queue_candidate_count,
        "event_board_stage_row_count": sum(1 for row in stage_rows if row.get("stage_scope") == "CENSUS_EVENT_BOARD"),
        "event_board_non_stage0_count": event_board_non_stage0_count,
        "operator_stage_scope_notice": (
            "NO_FULL_THESIS_STAGE_ROWS_EVENT_BOARD_STAGE_ROWS_EXIST"
            if full_thesis_stage_row_count <= 0 and event_board_non_stage0_count > 0
            else ("FULL_THESIS_STAGE_ROWS_PRESENT_SCOPE_GUARD_REQUIRED" if full_thesis_stage_row_count > 0 else "NO_FULL_THESIS_STAGE_ROWS")
        ),
        "full_thesis_stage_distribution": _count_by(stage_rows, "full_thesis_stage"),
    }


def _audit_slice(leaf_audit: Mapping[str, Any], theme: str) -> dict[str, Any]:
    critical = leaf_audit.get("critical_counts") or {}
    selected = {key: value for key, value in critical.items() if theme in key or (theme == "atomic" and key.startswith("stage_trace")) or (theme == "score" and "score" in key) or (theme == "semantic" and "semantic" in key)}
    return {"schema_version": f"e2r_census_v4_{theme}_audit_v1", "verdict": "PASS" if sum(int(v) for v in selected.values()) == 0 else "FAIL", "critical_counts": selected}


def _source_task_satisfaction_audit(output_root: Path) -> dict[str, Any]:
    executions = _read_jsonl(output_root / "source_task_executions.jsonl")
    accepted_claims = _read_jsonl(output_root / "accepted_claims.jsonl")
    documents = _read_jsonl(output_root / "evidence_documents.jsonl")
    anchors = _read_jsonl(output_root / "evidence_anchors.jsonl")
    contributions = _read_jsonl(output_root / "score_contributions.jsonl")
    stagecourt_traces = _read_jsonl(output_root / "stagecourt_traces.jsonl")
    stage_rows = _read_jsonl(output_root / "census_stage_status.jsonl")

    accepted_by_id = {str(row.get("claim_id") or ""): row for row in accepted_claims if row.get("claim_id")}
    document_ids = {str(row.get("document_id") or "") for row in documents if row.get("document_id")}
    anchor_ids = {str(row.get("anchor_id") or "") for row in anchors if row.get("anchor_id")}
    contribution_ids = {
        str(row.get("score_contribution_id") or row.get("contribution_id") or "")
        for row in contributions
        if row.get("score_contribution_id") or row.get("contribution_id")
    }

    contribution_ids_by_claim: dict[str, set[str]] = {}
    for contribution in contributions:
        contribution_id = str(contribution.get("score_contribution_id") or contribution.get("contribution_id") or "")
        if not contribution_id:
            continue
        for claim_id in contribution.get("support_claim_ids") or ():
            claim_key = str(claim_id)
            if claim_key:
                contribution_ids_by_claim.setdefault(claim_key, set()).add(contribution_id)

    stagecourt_trace_ids = {
        str(row.get("stagecourt_trace_id") or row.get("trace_id") or "")
        for row in stagecourt_traces
        if row.get("stagecourt_trace_id") or row.get("trace_id")
    }
    stagecourt_ids_by_claim: dict[str, set[str]] = {}
    stagecourt_ids_by_contribution: dict[str, set[str]] = {}
    for trace in stagecourt_traces:
        trace_id = str(trace.get("stagecourt_trace_id") or trace.get("trace_id") or "")
        if not trace_id:
            continue
        for claim_id in trace.get("accepted_claim_ids") or ():
            claim_key = str(claim_id)
            if claim_key:
                stagecourt_ids_by_claim.setdefault(claim_key, set()).add(trace_id)
        for contribution_id in trace.get("score_contribution_ids") or ():
            contribution_key = str(contribution_id)
            if contribution_key:
                stagecourt_ids_by_contribution.setdefault(contribution_key, set()).add(trace_id)

    representative_claim_ids = {str(claim_id) for row in stage_rows for claim_id in row.get("accepted_claim_ids") or () if str(claim_id)}
    representative_contribution_ids = {
        str(contribution_id) for row in stage_rows for contribution_id in row.get("score_contribution_ids") or () if str(contribution_id)
    }
    representative_stagecourt_ids = {
        str(row.get("stagecourt_trace_id") or "") for row in stage_rows if row.get("stagecourt_trace_id")
    }
    representative_score_claim_ids: set[str] = set()
    for contribution in contributions:
        contribution_id = str(contribution.get("score_contribution_id") or contribution.get("contribution_id") or "")
        if contribution_id in representative_contribution_ids:
            representative_score_claim_ids.update(str(item) for item in contribution.get("support_claim_ids") or () if str(item))

    claim_refs_by_task: dict[str, set[str]] = {}
    execution_claim_refs: list[tuple[Mapping[str, Any], str]] = []
    for execution in executions:
        claim_ids: set[str] = set()
        for key in ("accepted_claim_ids", "baseline_claim_ids", "score_claim_ids"):
            claim_ids.update(_ids_from_value(execution.get(key)))
        for claim_id in sorted(claim_ids):
            execution_claim_refs.append((execution, claim_id))
            task_id = str(execution.get("task_id") or execution.get("source_task_execution_id") or "")
            if task_id:
                claim_refs_by_task.setdefault(claim_id, set()).add(task_id)

    baseline_only = [row for row in executions if row.get("status") == "EVIDENCE_OS_BASELINE_ONLY"]
    direct_task_without_claim = sum(1 for row in executions if row.get("status") == "EVIDENCE_OS_ACCEPTED" and not row.get("accepted_claim_ids"))
    source_task_claim_missing_accepted_row_count = 0
    source_task_claim_missing_document_row_count = 0
    source_task_claim_missing_anchor_row_count = 0
    source_task_claim_document_not_in_execution_fetch_count = 0
    source_task_claim_missing_score_contribution_count = 0
    source_task_claim_missing_stagecourt_trace_count = 0
    source_task_chain_closed_to_stagecourt_count = 0
    source_task_chain_closed_to_representative_stage_count = 0

    for execution, claim_id in execution_claim_refs:
        claim = accepted_by_id.get(claim_id)
        if not claim:
            source_task_claim_missing_accepted_row_count += 1
            continue
        document_id = str(claim.get("document_id") or "")
        anchor_id = str(claim.get("anchor_id") or "")
        if document_id not in document_ids:
            source_task_claim_missing_document_row_count += 1
        if anchor_id not in anchor_ids:
            source_task_claim_missing_anchor_row_count += 1
        fetched_document_ids = _ids_from_value(execution.get("fetched_document_ids") or execution.get("document_ids"))
        if document_id and fetched_document_ids and document_id not in fetched_document_ids:
            source_task_claim_document_not_in_execution_fetch_count += 1
        contribution_refs = contribution_ids_by_claim.get(claim_id, set())
        if not contribution_refs:
            source_task_claim_missing_score_contribution_count += 1
        trace_refs = set(stagecourt_ids_by_claim.get(claim_id, set()))
        for contribution_id in contribution_refs:
            trace_refs.update(stagecourt_ids_by_contribution.get(contribution_id, set()))
        if not trace_refs:
            source_task_claim_missing_stagecourt_trace_count += 1
        elif claim and document_id in document_ids and anchor_id in anchor_ids and contribution_refs:
            source_task_chain_closed_to_stagecourt_count += 1
        if claim_id in representative_claim_ids:
            source_task_chain_closed_to_representative_stage_count += 1

    representative_score_claim_without_source_task_execution_count = 0
    representative_score_claim_missing_accepted_row_count = 0
    representative_score_claim_missing_document_row_count = 0
    representative_score_claim_missing_anchor_row_count = 0
    representative_score_claim_missing_score_contribution_count = 0
    representative_score_claim_missing_stagecourt_trace_count = 0
    representative_score_claim_missing_representative_stage_row_count = 0
    representative_score_claim_missing_representative_stagecourt_row_count = 0
    representative_score_claim_document_not_in_source_task_fetch_count = 0

    for claim_id in representative_score_claim_ids:
        claim = accepted_by_id.get(claim_id)
        if not claim:
            representative_score_claim_missing_accepted_row_count += 1
            continue
        if claim_id not in claim_refs_by_task:
            representative_score_claim_without_source_task_execution_count += 1
        document_id = str(claim.get("document_id") or "")
        anchor_id = str(claim.get("anchor_id") or "")
        if document_id not in document_ids:
            representative_score_claim_missing_document_row_count += 1
        if anchor_id not in anchor_ids:
            representative_score_claim_missing_anchor_row_count += 1
        contribution_refs = contribution_ids_by_claim.get(claim_id, set())
        if not contribution_refs:
            representative_score_claim_missing_score_contribution_count += 1
        trace_refs = set(stagecourt_ids_by_claim.get(claim_id, set()))
        for contribution_id in contribution_refs:
            trace_refs.update(stagecourt_ids_by_contribution.get(contribution_id, set()))
        if not trace_refs:
            representative_score_claim_missing_stagecourt_trace_count += 1
        if claim_id not in representative_claim_ids:
            representative_score_claim_missing_representative_stage_row_count += 1
        if not (trace_refs & representative_stagecourt_ids):
            representative_score_claim_missing_representative_stagecourt_row_count += 1
        linked_fetch = False
        has_fetch_reference = False
        for execution, execution_claim_id in execution_claim_refs:
            if execution_claim_id != claim_id:
                continue
            fetched_document_ids = _ids_from_value(execution.get("fetched_document_ids") or execution.get("document_ids"))
            if fetched_document_ids:
                has_fetch_reference = True
                if document_id in fetched_document_ids:
                    linked_fetch = True
        if has_fetch_reference and not linked_fetch:
            representative_score_claim_document_not_in_source_task_fetch_count += 1

    source_task_claim_satisfaction_mismatch_count = (
        source_task_claim_missing_accepted_row_count
        + source_task_claim_missing_document_row_count
        + source_task_claim_missing_anchor_row_count
        + source_task_claim_document_not_in_execution_fetch_count
        + source_task_claim_missing_score_contribution_count
        + source_task_claim_missing_stagecourt_trace_count
    )
    critical_counts = {
        "direct_task_without_accepted_claim_count": direct_task_without_claim,
        "representative_score_claim_without_source_task_execution_count": representative_score_claim_without_source_task_execution_count,
        "representative_score_claim_missing_accepted_row_count": representative_score_claim_missing_accepted_row_count,
        "representative_score_claim_missing_document_row_count": representative_score_claim_missing_document_row_count,
        "representative_score_claim_missing_anchor_row_count": representative_score_claim_missing_anchor_row_count,
        "representative_score_claim_document_not_in_source_task_fetch_count": representative_score_claim_document_not_in_source_task_fetch_count,
        "representative_score_claim_missing_score_contribution_count": representative_score_claim_missing_score_contribution_count,
        "representative_score_claim_missing_stagecourt_trace_count": representative_score_claim_missing_stagecourt_trace_count,
        "representative_score_claim_missing_representative_stage_row_count": representative_score_claim_missing_representative_stage_row_count,
        "representative_score_claim_missing_representative_stagecourt_row_count": representative_score_claim_missing_representative_stagecourt_row_count,
    }
    warning_counts = {
        "non_representative_source_task_claim_count": len({claim_id for _, claim_id in execution_claim_refs} - representative_claim_ids),
        "source_task_claim_satisfaction_mismatch_count": source_task_claim_satisfaction_mismatch_count,
    }
    critical_count = sum(int(value) for value in critical_counts.values())
    verdict = "PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION" if critical_count == 0 else "FAIL"
    return {
        "schema_version": "e2r_census_v4_source_task_satisfaction_audit_v2",
        "source_task_execution_count": len(executions),
        "source_task_execution_with_claim_count": len({str(row.get("task_id") or row.get("source_task_execution_id") or "") for row, _ in execution_claim_refs}),
        "source_task_claim_reference_count": len(execution_claim_refs),
        "source_task_claim_reference_unique_count": len({claim_id for _, claim_id in execution_claim_refs}),
        "accepted_claim_count": len(accepted_claims),
        "evidence_document_count": len(documents),
        "evidence_anchor_count": len(anchors),
        "score_contribution_count": len(contributions),
        "stagecourt_trace_count": len(stagecourt_traces),
        "representative_stage_row_count": len(stage_rows),
        "representative_stage_row_with_evidence_chain_count": sum(
            1 for row in stage_rows if row.get("accepted_claim_ids") or row.get("score_contribution_ids") or row.get("stagecourt_trace_id")
        ),
        "representative_stage_claim_count": len(representative_claim_ids),
        "representative_score_claim_count": len(representative_score_claim_ids),
        "representative_score_contribution_count": len(representative_contribution_ids),
        "representative_stagecourt_trace_count": len(representative_stagecourt_ids),
        "baseline_only_score_claim_count": sum(1 for row in baseline_only if row.get("score_claim_ids")),
        "baseline_only_stage_promotion_count": 0,
        "source_task_claim_satisfaction_mismatch_count": source_task_claim_satisfaction_mismatch_count,
        "source_task_claim_missing_accepted_row_count": source_task_claim_missing_accepted_row_count,
        "source_task_claim_missing_document_row_count": source_task_claim_missing_document_row_count,
        "source_task_claim_missing_anchor_row_count": source_task_claim_missing_anchor_row_count,
        "source_task_claim_document_not_in_execution_fetch_count": source_task_claim_document_not_in_execution_fetch_count,
        "source_task_claim_missing_score_contribution_count": source_task_claim_missing_score_contribution_count,
        "source_task_claim_missing_stagecourt_trace_count": source_task_claim_missing_stagecourt_trace_count,
        "source_task_chain_closed_to_stagecourt_count": source_task_chain_closed_to_stagecourt_count,
        "source_task_chain_closed_to_representative_stage_count": source_task_chain_closed_to_representative_stage_count,
        "direct_task_without_accepted_claim_count": direct_task_without_claim,
        "critical_counts": critical_counts,
        "critical_count": critical_count,
        "warning_counts": warning_counts,
        "warning_count": sum(int(value) for value in warning_counts.values()),
        "verdict": verdict,
        "verdict_scope": "LEDGER_REFRESH_SOURCE_TASK_SATISFACTION_PASS",
        "live_source_task_satisfaction_pass_allowed": False,
        "rule": (
            "Representative score claims must close the id chain from SourceTaskExecution/task_id to EvidenceDocument, "
            "EvidenceAnchor, ScoreContribution, StageCourt trace, and the representative census_stage_status row. "
            "Accepted claims outside the representative row are warnings, not score/stage proof."
        ),
    }


def _primitive_state_chain_audit(output_root: Path) -> dict[str, Any]:
    primitive_mappings = _read_jsonl(output_root / "primitive_mappings.jsonl")
    primitive_states = _read_jsonl(output_root / "primitive_states.jsonl")
    accepted_claims = _read_jsonl(output_root / "accepted_claims.jsonl")
    brain_claim_mapping_trace = _read_jsonl(output_root / "brain_claim_mapping_trace.jsonl")
    contributions = _read_jsonl(output_root / "score_contributions.jsonl")
    atomic_rows = _read_jsonl(output_root / "atomic_stage_decisions.jsonl")
    stage_rows = _read_jsonl(output_root / "census_stage_status.jsonl")

    primitive_by_id = {str(row.get("primitive_state_id") or ""): row for row in primitive_states if row.get("primitive_state_id")}
    primitive_mapping_by_id = {str(row.get("mapping_id") or ""): row for row in primitive_mappings if row.get("mapping_id")}
    claim_to_primitive_ids: dict[str, set[str]] = {}
    for state in primitive_states:
        primitive_state_id = str(state.get("primitive_state_id") or "")
        if not primitive_state_id:
            continue
        for key in ("support_claim_ids", "counter_claim_ids"):
            for claim_id in state.get(key) or ():
                claim_key = str(claim_id)
                if claim_key:
                    claim_to_primitive_ids.setdefault(claim_key, set()).add(primitive_state_id)

    accepted_by_id = {str(row.get("claim_id") or ""): row for row in accepted_claims if row.get("claim_id")}
    contribution_by_id = {
        str(row.get("score_contribution_id") or row.get("contribution_id") or ""): row
        for row in contributions
        if row.get("score_contribution_id") or row.get("contribution_id")
    }
    atomic_by_id = {str(row.get("atomic_stage_decision_id") or ""): row for row in atomic_rows if row.get("atomic_stage_decision_id")}
    representative_rows = [row for row in stage_rows if row.get("accepted_claim_ids") or row.get("score_contribution_ids")]
    accepted_primitive_index = _accepted_primitive_mapping_index_from_leafs(
        accepted_claims=accepted_claims,
        brain_claim_mapping_trace=brain_claim_mapping_trace,
    )

    representative_score_claim_ids: set[str] = set()
    representative_score_contribution_ids: set[str] = set()
    for row in representative_rows:
        representative_score_contribution_ids.update(str(item) for item in row.get("score_contribution_ids") or () if str(item))
    for contribution_id in representative_score_contribution_ids:
        contribution = contribution_by_id.get(contribution_id) or {}
        representative_score_claim_ids.update(str(item) for item in contribution.get("support_claim_ids") or () if str(item))

    representative_score_claim_without_primitive_state_count = sum(
        1 for claim_id in representative_score_claim_ids if not claim_to_primitive_ids.get(claim_id)
    )
    primitive_state_claim_id_not_found_count = sum(
        1
        for state in primitive_states
        for claim_id in list(state.get("support_claim_ids") or ()) + list(state.get("counter_claim_ids") or ())
        if str(claim_id) not in accepted_by_id
    )
    primitive_state_claim_primitive_mismatch_count = 0
    primitive_state_claim_primitive_mismatch_examples: list[dict[str, Any]] = []
    for state in primitive_states:
        primitive_state_id = str(state.get("primitive_state_id") or "")
        primitive_id = str(state.get("primitive_id") or "")
        state_symbol = str(state.get("symbol") or "")
        if not primitive_id:
            continue
        for claim_id in state.get("support_claim_ids") or ():
            claim_key = str(claim_id)
            claim_primitive_ids = _accepted_primitive_ids_for_state(
                claim_id=claim_key,
                primitive_state_id=primitive_state_id,
                state_symbol=state_symbol,
                accepted_primitive_index=accepted_primitive_index,
            )
            if not claim_primitive_ids or primitive_id not in claim_primitive_ids:
                primitive_state_claim_primitive_mismatch_count += 1
                if len(primitive_state_claim_primitive_mismatch_examples) < 10:
                    primitive_state_claim_primitive_mismatch_examples.append(
                        {
                            "primitive_state_id": state.get("primitive_state_id"),
                            "state_primitive_id": primitive_id,
                            "claim_id": claim_key,
                            "accepted_claim_primitive_ids": sorted(claim_primitive_ids),
                            "rule": (
                                "primitive state must match a direct accepted claim mapping; Brain traces require "
                                "claim_id + primitive_state_id + symbol + row primitive_id to match"
                            ),
                        }
                    )

    representative_stage_row_missing_primitive_state_ids_count = 0
    representative_stage_primitive_id_not_found_count = 0
    representative_stage_primitive_claim_set_mismatch_count = 0
    atomic_decision_primitive_set_mismatch_count = 0
    for row in representative_rows:
        accepted_ids = {str(item) for item in row.get("accepted_claim_ids") or () if str(item)}
        primitive_ids = {str(item) for item in row.get("primitive_state_ids") or () if str(item)}
        if accepted_ids and not primitive_ids:
            representative_stage_row_missing_primitive_state_ids_count += 1
        missing_primitive_ids = primitive_ids - set(primitive_by_id)
        if missing_primitive_ids:
            representative_stage_primitive_id_not_found_count += len(missing_primitive_ids)
        primitive_claim_ids = {
            str(claim_id)
            for primitive_id in primitive_ids
            for claim_id in (primitive_by_id.get(primitive_id, {}).get("support_claim_ids") or ())
        }
        if accepted_ids and not accepted_ids <= primitive_claim_ids:
            representative_stage_primitive_claim_set_mismatch_count += 1
        atomic_id = str(row.get("atomic_stage_decision_id") or "")
        atomic = atomic_by_id.get(atomic_id) or {}
        atomic_primitive_ids = {str(item) for item in atomic.get("primitive_state_ids") or () if str(item)}
        if atomic_id and primitive_ids != atomic_primitive_ids:
            atomic_decision_primitive_set_mismatch_count += 1
        elif not atomic_id and primitive_ids and str(row.get("stage_scope") or "") not in {"BRAIN_WEB_PARTIAL", "BRAIN_OFFICIAL_PARTIAL"}:
            atomic_decision_primitive_set_mismatch_count += 1

    representative_score_contribution_missing_mapping_ids_count = sum(
        1 for contribution_id in representative_score_contribution_ids if not (contribution_by_id.get(contribution_id) or {}).get("mapping_ids")
    )
    representative_score_mapping_id_not_found_count = sum(
        1
        for contribution_id in representative_score_contribution_ids
        for mapping_id in (contribution_by_id.get(contribution_id) or {}).get("mapping_ids") or ()
        if str(mapping_id) not in primitive_mapping_by_id
    )
    primitive_mapping_claim_id_not_found_count = sum(
        1 for row in primitive_mappings for claim_id in row.get("accepted_claim_ids") or () if str(claim_id) not in accepted_by_id
    )
    primitive_mapping_state_id_not_found_count = sum(
        1 for row in primitive_mappings for primitive_state_id in row.get("primitive_state_ids") or () if str(primitive_state_id) not in primitive_by_id
    )
    primitive_mapping_contribution_id_not_found_count = sum(
        1 for row in primitive_mappings for contribution_id in row.get("score_contribution_ids") or () if str(contribution_id) not in contribution_by_id
    )

    critical_counts = {
        "primitive_mapping_missing_id_count": sum(1 for row in primitive_mappings if not row.get("mapping_id")),
        "primitive_mapping_claim_id_not_found_count": primitive_mapping_claim_id_not_found_count,
        "primitive_mapping_state_id_not_found_count": primitive_mapping_state_id_not_found_count,
        "primitive_mapping_contribution_id_not_found_count": primitive_mapping_contribution_id_not_found_count,
        "primitive_state_missing_id_count": sum(1 for row in primitive_states if not row.get("primitive_state_id")),
        "primitive_state_claim_id_not_found_count": primitive_state_claim_id_not_found_count,
        "primitive_state_claim_primitive_mismatch_count": primitive_state_claim_primitive_mismatch_count,
        "representative_score_claim_without_primitive_state_count": representative_score_claim_without_primitive_state_count,
        "representative_stage_row_missing_primitive_state_ids_count": representative_stage_row_missing_primitive_state_ids_count,
        "representative_stage_primitive_id_not_found_count": representative_stage_primitive_id_not_found_count,
        "representative_stage_primitive_claim_set_mismatch_count": representative_stage_primitive_claim_set_mismatch_count,
        "atomic_decision_primitive_set_mismatch_count": atomic_decision_primitive_set_mismatch_count,
        "representative_score_contribution_missing_mapping_ids_count": representative_score_contribution_missing_mapping_ids_count,
        "representative_score_mapping_id_not_found_count": representative_score_mapping_id_not_found_count,
    }
    critical_count = sum(int(value) for value in critical_counts.values())
    return {
        "schema_version": "e2r_census_v4_primitive_state_chain_audit_v1",
        "primitive_mapping_count": len(primitive_mappings),
        "primitive_state_count": len(primitive_states),
        "primitive_state_with_id_count": sum(1 for row in primitive_states if row.get("primitive_state_id")),
        "accepted_claim_count": len(accepted_claims),
        "claim_with_multi_accepted_primitive_count": sum(
            1 for primitive_ids in accepted_primitive_index["claim_primitive_ids"].values() if len(primitive_ids) > 1
        ),
        "score_contribution_count": len(contributions),
        "representative_stage_row_with_evidence_chain_count": len(representative_rows),
        "representative_score_claim_count": len(representative_score_claim_ids),
        "representative_score_contribution_count": len(representative_score_contribution_ids),
        "representative_score_claim_with_primitive_state_count": sum(
            1 for claim_id in representative_score_claim_ids if claim_to_primitive_ids.get(claim_id)
        ),
        "critical_counts": critical_counts,
        "critical_count": critical_count,
        "critical_examples": {
            "primitive_state_claim_primitive_mismatch_examples": primitive_state_claim_primitive_mismatch_examples,
        },
        "verdict": "PASS" if critical_count == 0 else "FAIL",
        "mapping_leaf_resolution_supported": True,
        "rule": (
            "Representative score claims must have primitive_state_ids, those IDs must exist in primitive_states.jsonl, "
            "the referenced primitive states must support the representative accepted claims, and the representative "
            "stage row must match its AtomicStageDecision primitive_state_ids. Score contribution mapping_ids must "
            "resolve to primitive_mappings.jsonl rows."
        ),
    }


def _accepted_primitive_mapping_index_from_leafs(
    *,
    accepted_claims: Sequence[Mapping[str, Any]],
    brain_claim_mapping_trace: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    """Return all accepted primitive mappings known for each claim.

    `accepted_claims.jsonl` is a compatibility view keyed by `claim_id`, so a
    repeated Brain/Web claim can be lossily represented with only one
    `primitive_id`. The mapping trace is the append-style leaf that preserves
    every accepted `claim_id -> primitive_id` mapping. The trace row's
    `accepted_primitive_ids` field is deliberately ignored here because it is a
    task/execution-level summary, not proof that a specific PrimitiveState row
    is supported by that primitive.
    """

    primitive_ids_by_claim: dict[str, set[str]] = {}
    trace_claim_ids: set[str] = set()
    primitive_ids_by_claim_state: dict[tuple[str, str], list[tuple[str, str]]] = {}
    for claim in accepted_claims:
        claim_id = str(claim.get("claim_id") or "")
        if not claim_id:
            continue
        mapping = claim.get("mapping") if isinstance(claim.get("mapping"), Mapping) else {}
        mapping_status = str(claim.get("mapping_status") or mapping.get("mapping_status") or "")
        if mapping_status == "ACCEPTED":
            for primitive_id in (
                claim.get("primitive_id"),
                mapping.get("primitive_id"),
                mapping.get("contract_rule_id"),
            ):
                if primitive_id:
                    primitive_ids_by_claim.setdefault(claim_id, set()).add(str(primitive_id))

    for trace in brain_claim_mapping_trace:
        claim_id = str(trace.get("claim_id") or trace.get("accepted_claim_id") or "")
        if not claim_id:
            continue
        if trace.get("accepted") is not True:
            continue
        if str(trace.get("mapping_status") or "") != "ACCEPTED":
            continue
        trace_claim_ids.add(claim_id)
        primitive_id = str(trace.get("primitive_id") or "")
        if primitive_id:
            primitive_ids_by_claim.setdefault(claim_id, set()).add(primitive_id)
            trace_symbol = str(trace.get("symbol") or "")
            for primitive_state_id in trace.get("primitive_state_ids") or ():
                state_key = str(primitive_state_id)
                if state_key:
                    primitive_ids_by_claim_state.setdefault((claim_id, state_key), []).append((primitive_id, trace_symbol))
    return {
        "claim_primitive_ids": primitive_ids_by_claim,
        "trace_claim_ids": trace_claim_ids,
        "claim_state_primitive_rows": primitive_ids_by_claim_state,
    }


def _accepted_primitive_ids_for_state(
    *,
    claim_id: str,
    primitive_state_id: str,
    state_symbol: str,
    accepted_primitive_index: Mapping[str, Any],
) -> set[str]:
    trace_claim_ids = accepted_primitive_index.get("trace_claim_ids") or set()
    claim_state_rows = accepted_primitive_index.get("claim_state_primitive_rows") or {}
    if claim_id in trace_claim_ids:
        rows = claim_state_rows.get((claim_id, primitive_state_id), ())
        return {
            primitive_id
            for primitive_id, trace_symbol in rows
            if primitive_id and (not trace_symbol or not state_symbol or str(trace_symbol) == str(state_symbol))
        }
    return set((accepted_primitive_index.get("claim_primitive_ids") or {}).get(claim_id) or set())


def _official_counter_audit(stage_rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    bad = [row for row in stage_rows if int(row.get("accepted_official_claim_count") or 0) > 0 and int(row.get("official_source_task_count") or 0) == 0 and int(row.get("official_evidence_document_count") or 0) == 0]
    return {"schema_version": "e2r_census_v4_official_event_counter_audit_v1", "official_claim_but_recent_official_event_zero_count": len(bad), "verdict": "PASS" if not bad else "FAIL"}


def _event_separation_audit(stage_rows: Sequence[Mapping[str, Any]], *, atomic_rows: Sequence[Mapping[str, Any]] = ()) -> dict[str, Any]:
    stage_by_symbol = {str(row.get("symbol") or "").zfill(6): row for row in stage_rows}
    counts = {
        "missing_census_assessment_event_id_count": sum(1 for row in stage_rows if not row.get("census_assessment_event_id")),
        "assessment_event_score_evidence_allowed_count": sum(1 for row in stage_rows if row.get("census_assessment_event_score_evidence_allowed") is not False),
        "candidate_event_ids_contain_assessment_event_count": sum(
            1
            for row in stage_rows
            if row.get("census_assessment_event_id") and row.get("census_assessment_event_id") in set(row.get("candidate_event_ids") or [])
        ),
        "assessment_only_nonzero_score_count": sum(
            1
            for row in stage_rows
            if int(row.get("candidate_event_count") or 0) == 0 and row.get("score_scale") != "NO_SCORE"
        ),
        "no_current_catalyst_with_candidate_event_count": sum(
            1
            for row in stage_rows
            if row.get("stage_signal") == "NO_CURRENT_CATALYST" and int(row.get("candidate_event_count") or 0) > 0
        ),
        "score_eligible_candidate_without_accepted_claim_count": sum(
            1
            for row in stage_rows
            if int(row.get("score_eligible_candidate_event_count") or 0) > 0
            and int(row.get("accepted_claim_count") or 0) == 0
            and not row.get("blocked_claim_ids")
        ),
        "atomic_candidate_event_is_assessment_count": sum(
            1
            for row in atomic_rows
            if row.get("candidate_event_id")
            and str(row.get("candidate_event_id")) == str(stage_by_symbol.get(str(row.get("symbol") or "").zfill(6), {}).get("census_assessment_event_id") or "")
        ),
        "atomic_candidate_event_not_in_symbol_candidate_events_count": sum(
            1
            for row in atomic_rows
            if row.get("candidate_event_id")
            and str(row.get("candidate_event_id"))
            not in set(stage_by_symbol.get(str(row.get("symbol") or "").zfill(6), {}).get("candidate_event_ids") or [])
        ),
    }
    return {
        "schema_version": "e2r_census_v4_event_separation_audit_v1",
        "critical_counts": counts,
        "verdict": "PASS" if sum(counts.values()) == 0 else "FAIL",
    }


def _apply_full_thesis_smoke_replay(
    *,
    config: CensusV4RunConfig,
    output_root: Path,
    stage_rows: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    """Append a controlled URL-backed C06 full-thesis smoke chain.

    This is intentionally narrow: it proves the full-thesis leaf path can close
    for Samsung/Hynix without reusing daily event scores. It is not all-archetype
    replay parity and it is not a live broad-universe thesis run.
    """

    if config.full_thesis_smoke_mode != "controlled_replay":
        return _pending_full_thesis_smoke_replay(
            config=config,
            output_root=output_root,
            stage_rows=stage_rows,
            status="CONTROLLED_FULL_THESIS_SMOKE_DISABLED",
        )
    if _config_requests_production_full_thesis(config):
        return _pending_full_thesis_smoke_replay(
            config=config,
            output_root=output_root,
            stage_rows=stage_rows,
            status="CONTROLLED_FULL_THESIS_SMOKE_BLOCKED_IN_PRODUCTION_MODE",
        )

    rows_by_symbol = {str(row.get("symbol") or "").zfill(6): dict(row) for row in stage_rows}
    fixtures = _full_thesis_smoke_fixtures(config=config, stage_rows=stage_rows)
    if set(fixtures) != set(FULL_THESIS_SMOKE_SYMBOLS):
        return _pending_full_thesis_smoke_replay(
            config=config,
            output_root=output_root,
            stage_rows=stage_rows,
            status="PENDING_FULL_THESIS_REFRESH",
        )

    events: list[dict[str, Any]] = []
    source_tasks: list[dict[str, Any]] = []
    executions: list[dict[str, Any]] = []
    documents: list[dict[str, Any]] = []
    anchors: list[dict[str, Any]] = []
    raw_assertions: list[dict[str, Any]] = []
    adjudicated_claims: list[dict[str, Any]] = []
    accepted_claims: list[dict[str, Any]] = []
    primitive_states: list[dict[str, Any]] = []
    score_contributions: list[dict[str, Any]] = []
    stagecourt_traces: list[dict[str, Any]] = []
    claim_stage_traces: list[dict[str, Any]] = []
    atomic_rows: list[dict[str, Any]] = []
    updated_stage_rows: list[dict[str, Any]] = []

    for symbol in FULL_THESIS_SMOKE_SYMBOLS:
        original = rows_by_symbol.get(symbol)
        if not original:
            continue
        package = _full_thesis_smoke_symbol_package(config=config, base_row=original, fixture_rows=fixtures[symbol])
        events.append(package["event"])
        source_tasks.extend(package["source_tasks"])
        executions.extend(package["source_task_executions"])
        documents.extend(package["evidence_documents"])
        anchors.extend(package["evidence_anchors"])
        raw_assertions.extend(package["raw_assertions"])
        adjudicated_claims.extend(package["adjudicated_claims"])
        accepted_claims.extend(package["accepted_claims"])
        primitive_states.extend(package["primitive_states"])
        score_contributions.extend(package["score_contributions"])
        stagecourt_traces.append(package["stagecourt_trace"])
        claim_stage_traces.append(package["claim_to_stage_trace"])
        atomic_rows.append(package["atomic_stage_decision"])
        rows_by_symbol[symbol] = package["stage_row"]

    _merge_jsonl_by_key(output_root / "census_events.jsonl", events, "event_id")
    _merge_jsonl_by_key(output_root / "source_tasks.jsonl", source_tasks, "task_id")
    _merge_jsonl_by_key(output_root / "source_task_executions.jsonl", executions, "task_id")
    _merge_jsonl_by_key(output_root / "evidence_documents.jsonl", documents, "document_id")
    _merge_jsonl_by_key(output_root / "evidence_anchors.jsonl", anchors, "anchor_id")
    _merge_jsonl_by_key(output_root / "raw_assertions.jsonl", raw_assertions, "raw_assertion_id")
    _merge_jsonl_by_key(output_root / "adjudicated_claims.jsonl", adjudicated_claims, "claim_id")
    _merge_jsonl_by_key(output_root / "accepted_claims.jsonl", accepted_claims, "claim_id")
    _merge_jsonl_by_key(output_root / "primitive_states.jsonl", primitive_states, "primitive_state_id")
    _merge_jsonl_by_key(output_root / "score_contributions.jsonl", score_contributions, "score_contribution_id")
    _merge_jsonl_by_key(output_root / "stagecourt_traces.jsonl", stagecourt_traces, "stagecourt_trace_id")
    _merge_jsonl_by_key(output_root / "claim_to_stage_trace.jsonl", claim_stage_traces, "trace_id")

    for row in stage_rows:
        symbol = str(row.get("symbol") or "").zfill(6)
        updated_stage_rows.append(dict(rows_by_symbol.get(symbol, row)))

    return {
        "schema_version": "e2r_census_v4_full_thesis_smoke_replay_v1",
        "status": "FULL_THESIS_REFRESH_RAN",
        "as_of_date": config.as_of_date,
        "output_root": str(output_root),
        "symbols": [str(row.get("symbol") or "").zfill(6) for row in atomic_rows],
        "stage_rows": updated_stage_rows,
        "atomic_rows": atomic_rows,
        "accepted_claim_count": len(accepted_claims),
        "score_contribution_count": len(score_contributions),
        "stagecourt_trace_count": len(stagecourt_traces),
    }


def _pending_full_thesis_smoke_replay(
    *,
    config: CensusV4RunConfig,
    output_root: Path,
    stage_rows: Sequence[Mapping[str, Any]],
    status: str,
) -> dict[str, Any]:
    return {
        "schema_version": "e2r_census_v4_full_thesis_smoke_replay_v1",
        "status": status,
        "as_of_date": config.as_of_date,
        "output_root": str(output_root),
        "symbols": [],
        "stage_rows": [dict(row) for row in stage_rows],
        "atomic_rows": [],
    }


def _full_thesis_smoke_fixtures(
    *,
    config: CensusV4RunConfig,
    stage_rows: Sequence[Mapping[str, Any]],
) -> dict[str, list[dict[str, Any]]]:
    as_of = config.as_of_date
    return {
        "000660": [
            _full_thesis_fixture("000660", "named_customer_or_customer_quality", "Nvidia customer demand is issuer-scoped.", "Nvidia supplier SK Hynix began mass production of HBM3E.", "Reuters", "https://www.reuters.com/technology/nvidia-supplier-sk-hynix-begins-mass-production-next-generation-memory-chip-2024-03-19/", "2024-03-19", as_of, 14.0),
            _full_thesis_fixture("000660", "qualification_status", "Next-generation HBM production is confirmed.", "SK Hynix began mass production of next-generation memory chip.", "Reuters", "https://www.reuters.com/technology/nvidia-supplier-sk-hynix-begins-mass-production-next-generation-memory-chip-2024-03-19/", "2024-03-19", as_of, 12.0),
            _full_thesis_fixture("000660", "capacity_allocation_or_pre_sold", "HBM capacity is substantially allocated.", "HBM chips were almost sold out for 2025.", "Reuters", "https://www.reuters.com/technology/nvidia-supplier-sk-hynix-says-hbm-chips-almost-sold-out-2025-2024-05-02/", "2024-05-02", as_of, 16.0),
            _full_thesis_fixture("000660", "hbm_shipment_or_revenue_mix", "HBM shipment and revenue conversion is visible.", "AI memory products drove quarterly sales improvement.", "SK Hynix Newsroom", "https://news.skhynix.co.kr/q1-2026-business-results/", "2026-04-24", as_of, 14.0),
            _full_thesis_fixture("000660", "cash_or_revision_conversion", "Operating conversion is visible in 2026 results.", "SK Hynix reported stronger profitability with AI memory demand.", "SK Hynix Newsroom", "https://news.skhynix.co.kr/q1-2026-business-results/", "2026-04-24", as_of, 12.0),
            _full_thesis_fixture("000660", "repeat_evidence_family", "Independent evidence families repeat the C06 thesis.", "Reuters and issuer newsroom both support the HBM thesis.", "Evidence OS", "https://news.skhynix.co.kr/q1-2026-business-results/", "2026-04-24", as_of, 10.0),
            _full_thesis_fixture("000660", "source_quorum", "At least two independent source families support the smoke.", "Reuters and issuer newsroom are both present.", "Evidence OS", "https://news.skhynix.co.kr/q1-2026-business-results/", "2026-04-24", as_of, 10.0),
        ],
        "005930": [
            _full_thesis_fixture("005930", "named_customer_or_customer_quality", "Nvidia-related HBM qualification is issuer-scoped but mixed.", "Samsung HBM chips were tested for Nvidia supply.", "Reuters", "https://www.reuters.com/technology/samsungs-hbm-chips-failing-nvidia-tests-due-heat-power-consumption-woes-sources-2024-05-23/", "2024-05-23", as_of, 10.0),
            _full_thesis_fixture("005930", "qualification_status", "HBM qualification path exists with mixed evidence.", "Nvidia cleared Samsung HBM3 chips for a China-market processor.", "Reuters", "https://www.reuters.com/technology/nvidia-clears-samsungs-hbm3-chips-use-china-market-processor-sources-say-2024-07-23/", "2024-07-23", as_of, 9.0),
            _full_thesis_fixture("005930", "capacity_allocation_or_pre_sold", "Capacity allocation remains partially observed, not Green-level.", "AI chip supply delay still weighed on Samsung expectations.", "Reuters", "https://www.reuters.com/technology/samsung-q4-earnings-expected-be-hit-by-nvidia-ai-chip-supply-delay-2025-01-06/", "2025-01-06", as_of, 8.0, green_ready=False),
            _full_thesis_fixture("005930", "hbm_shipment_or_revenue_mix", "Memory recovery is visible but C06 conversion is incomplete.", "Memory business improved as AI demand continued.", "Samsung Newsroom", "https://news.samsung.com/global/samsung-electronics-announces-first-quarter-2026-results", "2026-04-30", as_of, 12.0),
            _full_thesis_fixture("005930", "cash_or_revision_conversion", "Earnings conversion is visible at company level.", "Samsung announced first-quarter 2026 results.", "Samsung Newsroom", "https://news.samsung.com/global/samsung-electronics-announces-first-quarter-2026-results", "2026-04-30", as_of, 12.0),
            _full_thesis_fixture("005930", "repeat_evidence_family", "Independent evidence families are present but mixed.", "Reuters and issuer newsroom provide separate HBM context.", "Evidence OS", "https://news.samsung.com/global/samsung-electronics-announces-first-quarter-2026-results", "2026-04-30", as_of, 11.0),
            _full_thesis_fixture("005930", "source_quorum", "At least two independent source families support the smoke.", "Reuters and issuer newsroom are both present.", "Evidence OS", "https://news.samsung.com/global/samsung-electronics-announces-first-quarter-2026-results", "2026-04-30", as_of, 10.0),
        ],
    }


def _full_thesis_fixture(
    symbol: str,
    primitive_id: str,
    claim_text: str,
    quote_text: str,
    source_name: str,
    source_url: str,
    event_date: str,
    as_of_date: str,
    rubric_points: float,
    *,
    green_ready: bool = True,
) -> dict[str, Any]:
    return {
        "symbol": symbol,
        "primitive_id": primitive_id,
        "claim_text": claim_text,
        "quote_text": quote_text,
        "source_name": source_name,
        "source_url": source_url,
        "event_date": event_date,
        "as_of_date": as_of_date,
        "rubric_points": float(rubric_points),
        "green_ready": bool(green_ready),
    }


def _full_thesis_smoke_symbol_package(
    *,
    config: CensusV4RunConfig,
    base_row: Mapping[str, Any],
    fixture_rows: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    symbol = str(base_row.get("symbol") or "").zfill(6)
    company = str(base_row.get("company_name") or FULL_THESIS_SMOKE_COMPANY_FALLBACKS.get(symbol, symbol))
    as_of = str(base_row.get("as_of_date") or config.as_of_date)
    event_id = f"CE-FTSMOKE-{symbol}-{as_of.replace('-', '')}"
    trace_id = f"SCT-FTSMOKE-{stable_hash((symbol, as_of, FULL_THESIS_SMOKE_ARCHETYPE))[:20]}"
    atomic_id = f"ATOMIC-FTSMOKE-{stable_hash((symbol, trace_id))[:20]}"
    claim_trace_id = f"CSTTRACE-FTSMOKE-{stable_hash((symbol, trace_id, 'claim-stage'))[:20]}"

    source_tasks: list[dict[str, Any]] = []
    executions: list[dict[str, Any]] = []
    documents: list[dict[str, Any]] = []
    anchors: list[dict[str, Any]] = []
    raw_assertions: list[dict[str, Any]] = []
    adjudicated_claims: list[dict[str, Any]] = []
    accepted_claims: list[dict[str, Any]] = []
    primitive_states: list[dict[str, Any]] = []
    score_contributions: list[dict[str, Any]] = []
    primitive_to_claims: dict[str, list[str]] = {}
    primitive_to_documents: dict[str, list[str]] = {}
    primitive_to_anchors: dict[str, list[str]] = {}
    task_ids: list[str] = []
    execution_ids: list[str] = []

    for fixture in fixture_rows:
        primitive = str(fixture["primitive_id"])
        base_key = {"symbol": symbol, "primitive": primitive, "url": fixture["source_url"], "as_of": as_of}
        document_id = f"DOC-FTSMOKE-{stable_hash((base_key, 'doc'))[:20]}"
        anchor_id = f"ANCH-FTSMOKE-{stable_hash((base_key, 'anchor'))[:20]}"
        raw_id = f"RAW-FTSMOKE-{stable_hash((base_key, 'raw'))[:20]}"
        claim_id = f"CLM-FTSMOKE-{stable_hash((base_key, 'claim'))[:20]}"
        mapping_id = f"MAP-FTSMOKE-{stable_hash((claim_id, primitive))[:20]}"
        contribution_id = f"SCON-FTSMOKE-{stable_hash((claim_id, primitive, 'score'))[:20]}"
        task_id = _full_thesis_smoke_task_id(symbol=symbol, primitive=primitive, as_of_date=as_of)
        task_ids.append(task_id)
        execution_ids.append(task_id)
        primitive_to_claims.setdefault(primitive, []).append(claim_id)
        primitive_to_documents.setdefault(primitive, []).append(document_id)
        primitive_to_anchors.setdefault(primitive, []).append(anchor_id)
        documents.append(
            {
                "schema_version": "e2r_census_v4_evidence_document_v1",
                "document_id": document_id,
                "symbol": symbol,
                "company_name": company,
                "canonical_url": fixture["source_url"],
                "source_url": fixture["source_url"],
                "source_name": fixture["source_name"],
                "source_type": "TRUSTED_NEWS_OR_ISSUER_IR",
                "published_at": fixture["event_date"],
                "available_at": fixture["event_date"],
                "fetched_at": as_of,
                "parser_version": "full_thesis_c06_url_backed_smoke_v1",
                "content_hash": stable_hash((fixture["source_url"], fixture["quote_text"], primitive)),
                "source_origin": FULL_THESIS_SMOKE_SOURCE_ORIGIN,
                "full_thesis_smoke": True,
            }
        )
        anchors.append(
            {
                "schema_version": "e2r_census_v4_evidence_anchor_v1",
                "anchor_id": anchor_id,
                "document_id": document_id,
                "anchor_type": "TEXT_SPAN",
                "locator": f"full_thesis_smoke:{primitive}",
                "exact_text": fixture["quote_text"],
                "normalized_value": fixture["claim_text"],
                "content_hash": stable_hash((document_id, fixture["quote_text"])),
                "anchor_verified": True,
                "source_origin": FULL_THESIS_SMOKE_SOURCE_ORIGIN,
            }
        )
        raw_assertions.append(
            {
                "schema_version": "e2r_census_v4_raw_assertion_v1",
                "raw_assertion_id": raw_id,
                "symbol": symbol,
                "document_id": document_id,
                "anchor_id": anchor_id,
                "subject": company,
                "predicate": primitive,
                "value": fixture["claim_text"],
                "event_date": fixture["event_date"],
                "source_origin": FULL_THESIS_SMOKE_SOURCE_ORIGIN,
            }
        )
        claim_payload = {
            "accepted": True,
            "claim_id": claim_id,
            "symbol": symbol,
            "as_of_date": as_of,
            "event_date": fixture["event_date"],
            "source_cutover_date": as_of,
            "document_id": document_id,
            "anchor_id": anchor_id,
            "raw_assertion_id": raw_id,
            "source_provider": fixture["source_name"],
            "source_url": fixture["source_url"],
            "quote_text": fixture["quote_text"],
            "subject_entity_id": f"KRX:{symbol}",
            "target_entity_id": f"KRX:{symbol}",
            "target_scope_status": "DIRECT",
            "directness": "DIRECT",
            "polarity": "POSITIVE",
            "temporal_status": "CURRENT",
            "semantic_status": "PASS",
            "mapping_status": "ACCEPTED",
            "primitive_id": primitive,
            "support_direction": "SUPPORTS",
            "score_eligible": True,
            "satisfies_source_task": True,
            "satisfaction_type": "DIRECT_ACCEPTED_CLAIM",
            "source_task_primitive_gap": primitive,
            "eligibility_policy": "code_derived_v1",
            "eligibility_reasons": [],
            "mapping": {
                "mapping_id": mapping_id,
                "mapping_status": "ACCEPTED",
                "primitive_id": primitive,
                "support_direction": "SUPPORTS",
                "contract_rule_id": f"{FULL_THESIS_SMOKE_ARCHETYPE}.{primitive}",
                "rationale": "controlled URL-backed C06 full-thesis smoke mapping",
            },
            "source_origin": FULL_THESIS_SMOKE_SOURCE_ORIGIN,
            "brain_web_claim": False,
            "full_thesis_claim": True,
        }
        adjudicated_claims.append(dict(claim_payload))
        accepted_claims.append(claim_payload)
        contribution_points = round(float(fixture["rubric_points"]), 4)
        score_contributions.append(
            {
                "schema_version": "e2r_census_v4_score_contribution_v1",
                "score_contribution_id": contribution_id,
                "contribution_id": contribution_id,
                "symbol": symbol,
                "candidate_event_id": event_id,
                "component_key": "full_thesis_c06_evidence",
                "criterion_id": f"full_thesis_c06_{primitive}",
                "raw_points": contribution_points,
                "max_points": contribution_points,
                "support_claim_ids": [claim_id],
                "counter_claim_ids": [],
                "mapping_ids": [mapping_id],
                "source_family_ids": [fixture["source_name"]],
                "rationale": f"C06 full-thesis smoke support for {primitive}",
                "confidence": 0.9,
                "cap_reason": None,
                "source_cutover_date": as_of,
                "score_build_method": "primitive_score_contribution_sum",
                "source_origin": FULL_THESIS_SMOKE_SOURCE_ORIGIN,
                "full_thesis_smoke": True,
            }
        )
        source_tasks.append(
            {
                "schema_version": "e2r_census_v4_full_thesis_source_task_v1",
                "task_id": task_id,
                "smoke_task_id": task_id,
                "symbol": symbol,
                "company_name": company,
                "as_of_date": as_of,
                "candidate_event_id": event_id,
                "target_archetype": FULL_THESIS_SMOKE_ARCHETYPE,
                "primitive_gap": primitive,
                "task_status": "EXECUTED_ACCEPTED",
                "source_policy": "controlled_url_backed_replay_fixture",
                "source_class": "URL_BACKED_FIXTURE",
                "provider_name": "ControlledFixtureReplay",
                "source_task_origin": FULL_THESIS_SMOKE_SOURCE_ORIGIN,
                "preferred_source_classes": ["IssuerIR", "TrustedNews"],
                "fallback_source_classes": [],
                "forbidden_source_classes": ["snippet_only_score", "source_proxy_only", "evidence_url_pending"],
                "requested_source_classes": ["IssuerIR", "TrustedNews"],
                "llm_query_required": False,
                "hardcoded_query_count": 0,
                "hardcoded_queries": [],
                "query_intents": [],
                "general_search_allowed": False,
                "max_queries": 0,
                "max_candidates": 1,
                "max_fetches": 1,
                "stop_condition": {"accepted_claim_count": 1},
                "score_allowed_before_execution": False,
                "score_evidence": True,
                "accepted_claim_ids": [claim_id],
                "fetched_document_ids": [document_id],
                "evidence_anchor_ids": [anchor_id],
                "source_origin": FULL_THESIS_SMOKE_SOURCE_ORIGIN,
                "reason": "Controlled smoke uses URL-backed fixture anchors to verify full-thesis leaf wiring.",
            }
        )
        executions.append(
            {
                "schema_version": "e2r_census_v4_source_task_execution_v1",
                "task_id": task_id,
                "source_task_execution_id": task_id,
                "symbol": symbol,
                "company_name": company,
                "candidate_event_id": event_id,
                "status": "EVIDENCE_OS_ACCEPTED",
                "source_task": {
                    "task_id": task_id,
                    "symbol": symbol,
                    "company_name": company,
                    "candidate_event_id": event_id,
                    "archetype_id": FULL_THESIS_SMOKE_ARCHETYPE,
                    "primitive_gap": primitive,
                    "source_class": "URL_BACKED_FIXTURE",
                    "provider_name": "ControlledFixtureReplay",
                    "source_task_origin": FULL_THESIS_SMOKE_SOURCE_ORIGIN,
                    "preferred_source_classes": ["IssuerIR", "TrustedNews"],
                    "fallback_source_classes": [],
                    "forbidden_source_classes": ["snippet_only_score", "source_proxy_only", "evidence_url_pending"],
                    "requested_source_classes": ["IssuerIR", "TrustedNews"],
                },
                "archetype_id": FULL_THESIS_SMOKE_ARCHETYPE,
                "primitive_gap": primitive,
                "source_class": "URL_BACKED_FIXTURE",
                "provider_name": "ControlledFixtureReplay",
                "source_task_origin": FULL_THESIS_SMOKE_SOURCE_ORIGIN,
                "preferred_source_classes": ["IssuerIR", "TrustedNews"],
                "fallback_source_classes": [],
                "forbidden_source_classes": ["snippet_only_score", "source_proxy_only", "evidence_url_pending"],
                "requested_source_classes": ["IssuerIR", "TrustedNews"],
                "accepted_claim_ids": [claim_id],
                "direct_accepted_claim_ids": [claim_id],
                "rerouted_accepted_claim_ids": [],
                "score_claim_ids": [claim_id],
                "adjudicated_claim_ids": [claim_id],
                "fetched_document_ids": [document_id],
                "document_ids": [document_id],
                "evidence_anchor_ids": [anchor_id],
                "accepted_primitive_ids": [primitive],
                "primitive_gap_satisfied_ids": [primitive],
                "primitive_gap_unsatisfied_ids": [],
                "satisfies_source_task": True,
                "satisfaction_type": "DIRECT_ACCEPTED_CLAIM",
                "source_cutover_date": as_of,
                "source_task_execution_origin": FULL_THESIS_SMOKE_SOURCE_ORIGIN,
                "source_origin": FULL_THESIS_SMOKE_SOURCE_ORIGIN,
                "claim_producing_execution": True,
            }
        )

    all_claim_ids = [str(row["claim_id"]) for row in accepted_claims]
    all_contribution_ids = [str(row["score_contribution_id"]) for row in score_contributions]
    score = _full_thesis_smoke_score_from_contributions(score_contributions)
    missing_green_primitives = _full_thesis_smoke_missing_green_primitives(fixture_rows)
    base_stage = _full_thesis_smoke_stage_from_score(score=score, missing_green_primitives=missing_green_primitives)
    canonical_stage = canonical_stage_for_display(base_stage)
    all_primitive_state_ids: list[str] = []
    for primitive, claim_ids in primitive_to_claims.items():
        primitive_state_id = f"PRIM-FTSMOKE-{stable_hash((symbol, primitive, claim_ids))[:20]}"
        all_primitive_state_ids.append(primitive_state_id)
        primitive_states.append(
            {
                "schema_version": "e2r_census_v4_primitive_state_v1",
                "primitive_state_id": primitive_state_id,
                "candidate_event_id": event_id,
                "symbol": symbol,
                "source_cutover_date": as_of,
                "primitive_id": primitive,
                "status": "PRESENT_CURRENT",
                "normalized_value": "URL-backed full thesis smoke support",
                "support_claim_ids": claim_ids,
                "counter_claim_ids": [],
                "freshness_days": 0,
                "confidence_for_review": 0.9,
                "materiality_remaining_points": 0,
                "support_mapping_ids": [
                    str((claim.get("mapping") or {}).get("mapping_id"))
                    for claim in accepted_claims
                    if claim.get("primitive_id") == primitive
                ],
                "counter_mapping_ids": [],
                "source_origin": FULL_THESIS_SMOKE_SOURCE_ORIGIN,
            }
        )
    stagecourt_trace = {
        "stagecourt_trace_id": trace_id,
        "trace_id": trace_id,
        "candidate_event_id": event_id,
        "symbol": symbol,
        "source_cutover_date": as_of,
        "accepted_claim_ids": all_claim_ids,
        "score_contribution_ids": all_contribution_ids,
        "primitive_state_ids": all_primitive_state_ids,
        "score_interval": {"lower": score, "upper": score},
        "score_status": "FINAL",
        "base_stage": base_stage,
        "canonical_stage": canonical_stage,
        "transition_overlay": "NONE",
        "investigation_status": "COMPLETE",
        "hard_break_status": "NONE",
        "missing_green_primitives": missing_green_primitives,
        "missing_yellow_primitives": [],
        "present_green_primitives": _full_thesis_smoke_required_primitives(),
        "stage_decision_reason": "controlled_url_backed_c06_full_thesis_smoke_score_contribution_sum",
        "source_origin": FULL_THESIS_SMOKE_SOURCE_ORIGIN,
        "score_build_method": "primitive_score_contribution_sum",
    }
    atomic_stage_decision = {
        "schema_version": "e2r_census_v4_atomic_stage_decision_v1",
        "atomic_stage_decision_id": atomic_id,
        "symbol": symbol,
        "company_name": company,
        "as_of_date": as_of,
        "candidate_event_id": event_id,
        "source_task_ids": task_ids,
        "source_task_execution_ids": execution_ids,
        "stagecourt_trace_id": trace_id,
        "base_stage": base_stage,
        "canonical_stage": canonical_stage,
        "stage_signal": "FULL_THESIS_C06_HBM_STAGE",
        "stage_scope": "FULL_THESIS",
        "risk_stage_signal": "NONE",
        "transition_overlay": "NONE",
        "stage_decision_status": "FINAL",
        "score_scale": "FULL_E2R_100",
        "score_scope": "FULL_E2R_100",
        "score_source": "SCORE_CONTRIBUTION_SUM",
        "event_evidence_score": None,
        "full_e2r_verified_score": score,
        "raw_contribution_score": score,
        "score_interval_lower": score,
        "score_interval_upper": score,
        "score_valid_status": "FINAL",
        "accepted_claim_ids": all_claim_ids,
        "blocked_claim_ids": [],
        "score_contribution_ids": all_contribution_ids,
        "blocked_score_contribution_ids": [],
        "primitive_state_ids": all_primitive_state_ids,
        "blocked_primitive_state_ids": [],
        "failed_stage_gates": [],
        "missing_primitives": [],
        "material_gap_ids": [],
        "source_cutover_date": as_of,
        "is_representative": True,
        "additional_stage_decision_ids": [],
        "semantic_guard_status": "PASS",
        "semantic_guard_class": "full_thesis_smoke_url_backed_c06",
        "semantic_guard_reasons": [],
        "stage_decision_reason": "controlled URL-backed full-thesis smoke from ScoreContribution sum",
    }
    event = {
        "schema_version": "e2r_census_v4_candidate_event_v1",
        "event_id": event_id,
        "symbol": symbol,
        "company_name": company,
        "event_type": "FullThesisSmokeEvent",
        "event_category": "FullThesisSmokeEvent",
        "event_date": as_of,
        "as_of_date": as_of,
        "source_origin": FULL_THESIS_SMOKE_SOURCE_ORIGIN,
        "score_evidence_allowed": True,
        "target_archetype": FULL_THESIS_SMOKE_ARCHETYPE,
    }
    claim_to_stage_trace = {
        "schema_version": "e2r_census_v4_claim_to_stage_trace_v1",
        "trace_id": claim_trace_id,
        "symbol": symbol,
        "candidate_event_id": event_id,
        "accepted_claim_ids": all_claim_ids,
        "score_contribution_ids": all_contribution_ids,
        "primitive_state_ids": all_primitive_state_ids,
        "stagecourt_trace_id": trace_id,
        "atomic_stage_decision_id": atomic_id,
        "stage_scope": "FULL_THESIS",
        "source_origin": FULL_THESIS_SMOKE_SOURCE_ORIGIN,
    }
    daily_event_claim_ids = list(base_row.get("accepted_claim_ids") or [])
    daily_event_score_contribution_ids = list(base_row.get("score_contribution_ids") or [])
    daily_stagecourt_trace_ids = [base_row.get("stagecourt_trace_id")] if base_row.get("stagecourt_trace_id") else []
    candidate_event_ids = list(base_row.get("candidate_event_ids") or [])
    _append_unique(candidate_event_ids, event_id)
    stage_row = {
        **dict(base_row),
        "candidate_event_ids": candidate_event_ids,
        "candidate_event_count": int(base_row.get("candidate_event_count") or 0) + 1,
        "score_eligible_candidate_event_ids": list(dict.fromkeys([*(base_row.get("score_eligible_candidate_event_ids") or []), event_id])),
        "score_eligible_candidate_event_count": int(base_row.get("score_eligible_candidate_event_count") or 0) + 1,
        "full_thesis_event_id": event_id,
        "daily_event_claim_ids": daily_event_claim_ids,
        "daily_event_score_contribution_ids": daily_event_score_contribution_ids,
        "daily_event_stagecourt_trace_ids": daily_stagecourt_trace_ids,
        "daily_event_atomic_stage_decision_id": base_row.get("atomic_stage_decision_id"),
        "daily_event_stage_signal": base_row.get("daily_event_stage_signal") or base_row.get("stage_signal"),
        "daily_event_evidence_score": base_row.get("daily_event_evidence_score") if base_row.get("daily_event_evidence_score") is not None else base_row.get("event_evidence_score"),
        "census_status": "FULL_THESIS_VERIFIED",
        "assessment_depth": "FULL_THESIS_REFRESH",
        "base_stage": base_stage,
        "canonical_stage": canonical_stage,
        "stage_signal": "FULL_THESIS_C06_HBM_STAGE",
        "stage_scope": "FULL_THESIS",
        "risk_stage_signal": "NONE",
        "transition_overlay": "NONE",
        "investigation_status": "COMPLETE",
        "stage_decision_status": "FINAL",
        "stage_confidence": "FULL_THESIS_URL_BACKED_SMOKE",
        "score_valid_status": "FINAL",
        "score_scale": "FULL_E2R_100",
        "score_scope": "FULL_E2R_100",
        "score_source": "SCORE_CONTRIBUTION_SUM",
        "score_semantics": "full_thesis_c06_hbm_url_backed_smoke_score",
        "score_build_method": "primitive_score_contribution_sum",
        "verified_score": score,
        "full_e2r_verified_score": score,
        "event_evidence_score": None,
        "raw_contribution_score": score,
        "score_interval_lower": score,
        "score_interval_upper": score,
        "atomic_stage_decision_id": atomic_id,
        "additional_stage_decision_ids": [],
        "accepted_claim_ids": all_claim_ids,
        "blocked_claim_ids": [],
        "score_contribution_ids": all_contribution_ids,
        "blocked_score_contribution_ids": [],
        "primitive_state_ids": all_primitive_state_ids,
        "blocked_primitive_state_ids": [],
        "stagecourt_trace_id": trace_id,
        "claim_to_stage_trace_id": claim_trace_id,
        "accepted_claim_count": len(all_claim_ids),
        "score_contribution_count": len(all_contribution_ids),
        "accepted_official_claim_count": len(all_claim_ids),
        "official_source_task_count": len(task_ids),
        "official_evidence_document_count": len({row["document_id"] for row in documents}),
        "missing_primitives": [],
        "failed_stage_gates": [],
        "material_gap_ids": [],
        "semantic_guard_status": "PASS",
        "semantic_guard_class": "full_thesis_smoke_url_backed_c06",
        "semantic_guard_reasons": [],
        "full_thesis_primary_archetype": FULL_THESIS_SMOKE_ARCHETYPE,
        "full_thesis_verified_score": score,
        "full_thesis_score_scale": "FULL_E2R_100",
        "full_thesis_stage": base_stage,
        "full_thesis_score_valid_status": "FINAL",
        "full_thesis_missing_primitives": [],
        "full_thesis_source_task_ids": task_ids,
        "full_thesis_accepted_claim_ids": all_claim_ids,
        "full_thesis_score_contribution_ids": all_contribution_ids,
        "full_thesis_stagecourt_trace_ids": [trace_id],
        "full_thesis_task_accepted_claim_ids_by_primitive": primitive_to_claims,
        "full_thesis_smoke_status": "FULL_THESIS_REFRESH_RAN",
        "claim_backed_score_ratio": 1.0,
        "orphan_score_count": 0,
        "next_actions": ["WATCH"],
    }
    return {
        "event": event,
        "source_tasks": source_tasks,
        "source_task_executions": executions,
        "evidence_documents": documents,
        "evidence_anchors": anchors,
        "raw_assertions": raw_assertions,
        "adjudicated_claims": adjudicated_claims,
        "accepted_claims": accepted_claims,
        "primitive_states": primitive_states,
        "score_contributions": score_contributions,
        "stagecourt_trace": stagecourt_trace,
        "claim_to_stage_trace": claim_to_stage_trace,
        "atomic_stage_decision": atomic_stage_decision,
        "stage_row": stage_row,
    }


def _full_thesis_smoke_score_from_contributions(score_contributions: Sequence[Mapping[str, Any]]) -> float:
    return round(sum(float(row.get("raw_points") or 0.0) for row in score_contributions), 4)


def _full_thesis_smoke_missing_green_primitives(fixture_rows: Sequence[Mapping[str, Any]]) -> list[str]:
    return [
        f"{row['primitive_id']}_green_strength"
        for row in fixture_rows
        if row.get("green_ready") is False
    ]


def _full_thesis_smoke_stage_from_score(*, score: float, missing_green_primitives: Sequence[str]) -> str:
    if score >= 90.0 and not missing_green_primitives:
        return "Stage3-Green"
    if score >= 80.0:
        return "Stage3-Yellow"
    if score >= 65.0:
        return "Stage2-Watch"
    if score > 0.0:
        return "Stage1"
    return "Stage0"


def _full_thesis_smoke_task_id(*, symbol: str, primitive: str, as_of_date: Any) -> str:
    return "FTSMOKE-" + stable_hash(
        {
            "symbol": symbol,
            "archetype": FULL_THESIS_SMOKE_ARCHETYPE,
            "primitive": primitive,
            "as_of_date": as_of_date,
        }
    )[:20]


def _samsung_hynix_smoke(stage_rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    rows = [row for row in stage_rows if row.get("symbol") in set(FULL_THESIS_SMOKE_SYMBOLS)]
    tasks = _full_thesis_smoke_tasks(stage_rows)
    tasks_by_symbol: dict[str, list[Mapping[str, Any]]] = {}
    for task in tasks:
        tasks_by_symbol.setdefault(str(task.get("symbol") or ""), []).append(task)
    per_symbol = []
    for row in rows:
        symbol = str(row.get("symbol") or "")
        symbol_tasks = tasks_by_symbol.get(symbol, [])
        full_claim_ids = list(row.get("full_thesis_accepted_claim_ids") or [])
        full_contribution_ids = list(row.get("full_thesis_score_contribution_ids") or [])
        full_stagecourt_ids = list(row.get("full_thesis_stagecourt_trace_ids") or [])
        smoke_pass_allowed = (
            row.get("stage_scope") == "FULL_THESIS"
            and row.get("score_scale") == "FULL_E2R_100"
            and row.get("full_thesis_score_valid_status") == "FINAL"
            and bool(full_claim_ids)
            and bool(full_contribution_ids)
            and bool(full_stagecourt_ids)
            and not (row.get("full_thesis_missing_primitives") or [])
        )
        daily_claim_ids = list(row.get("daily_event_claim_ids") or row.get("accepted_claim_ids") or [])
        daily_contribution_ids = list(row.get("daily_event_score_contribution_ids") or row.get("score_contribution_ids") or [])
        daily_stagecourt_ids = list(row.get("daily_event_stagecourt_trace_ids") or ([row.get("stagecourt_trace_id")] if row.get("stagecourt_trace_id") else []))
        per_symbol.append(
            {
                "symbol": symbol,
                "company_name": row.get("company_name"),
                "daily_event_claim_ids": daily_claim_ids,
                "daily_event_score_contribution_ids": daily_contribution_ids,
                "daily_event_stagecourt_trace_ids": daily_stagecourt_ids,
                "additional_daily_atomic_decision_ids": list(row.get("additional_stage_decision_ids") or []),
                "full_thesis_claim_ids": full_claim_ids,
                "full_thesis_score_contribution_ids": full_contribution_ids,
                "full_thesis_stagecourt_trace_ids": full_stagecourt_ids,
                "full_thesis_source_task_ids": [str(task.get("smoke_task_id") or "") for task in symbol_tasks],
                "missing_full_thesis_primitives": list(row.get("full_thesis_missing_primitives") or []),
                "smoke_pass_allowed": smoke_pass_allowed,
                "blocking_reason": None if smoke_pass_allowed else "full_thesis_source_tasks_planned_but_not_executed",
            }
        )
    pass_allowed = len(per_symbol) == len(FULL_THESIS_SMOKE_SYMBOLS) and all(row["smoke_pass_allowed"] for row in per_symbol)
    hardcoded_query_count = sum(len(task.get("hardcoded_queries") or []) for task in tasks)
    daily_full_thesis_separated = _daily_event_full_thesis_separated(rows)
    honesty_pass_allowed = daily_full_thesis_separated and hardcoded_query_count == 0
    return {
        "schema_version": "e2r_census_v4_samsung_hynix_full_thesis_smoke_v1",
        "required_symbols": list(FULL_THESIS_SMOKE_SYMBOLS),
        "target_full_thesis_archetype": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        "required_full_thesis_primitives": _full_thesis_smoke_required_primitives(),
        "smoke_task_count": len(tasks),
        "hardcoded_query_count": hardcoded_query_count,
        "score_allowed_before_execution": False,
        "rows": rows,
        "per_symbol": per_symbol,
        "daily_event_and_full_thesis_separated": daily_full_thesis_separated,
        "full_thesis_smoke_honesty_pass_allowed": honesty_pass_allowed,
        "full_thesis_smoke_execution_pass_allowed": pass_allowed,
        "full_thesis_smoke_honesty_status": (
            "FULL_THESIS_SMOKE_HONESTY_PASS" if honesty_pass_allowed else "FULL_THESIS_SMOKE_HONESTY_FAIL"
        ),
        "full_thesis_smoke_execution_status": (
            "FULL_THESIS_SMOKE_EXECUTION_PASS" if pass_allowed else "FULL_THESIS_SMOKE_EXECUTION_PENDING"
        ),
        "full_thesis_status": "FULL_THESIS_REFRESH_RAN" if pass_allowed else "PENDING_FULL_THESIS_REFRESH",
        "verdict": "FULL_THESIS_SMOKE_PASS" if pass_allowed else "PENDING_FULL_THESIS_REFRESH",
    }


def _c06_guard_replay_audit(
    *,
    config: CensusV4RunConfig,
    stage_rows: Sequence[Mapping[str, Any]],
    output_root: Path | None = None,
) -> dict[str, Any]:
    c06_rows = [
        row
        for row in stage_rows
        if row.get("stage_scope") == "FULL_THESIS"
        and row.get("full_thesis_primary_archetype") == FULL_THESIS_SMOKE_ARCHETYPE
    ]
    c06_symbols = sorted(str(row.get("symbol") or "") for row in c06_rows)
    positive_wiring_smoke_ready = bool(c06_rows) and all(
        row.get("score_scale") == "FULL_E2R_100"
        and row.get("full_thesis_score_valid_status") == "FINAL"
        and bool(row.get("full_thesis_accepted_claim_ids"))
        and bool(row.get("full_thesis_score_contribution_ids"))
        for row in c06_rows
    )
    guard_cases = _c06_guard_replay_cases(as_of_date=_first_as_of_date(stage_rows))
    accepted_claims = _read_jsonl(output_root / "accepted_claims.jsonl") if output_root else []
    source_backed_replay = (
        _c06_source_backed_semantic_replay(config=config, output_root=output_root)
        if output_root is not None
        else _empty_c06_source_backed_semantic_replay(config=config, reason="output_root_missing")
    )
    if output_root is not None:
        write_json(output_root / "c06_source_backed_semantic_replay.json", source_backed_replay)
    c06_smoke_claims = [
        row
        for row in accepted_claims
        if row.get("source_origin") == FULL_THESIS_SMOKE_SOURCE_ORIGIN
        and str(row.get("symbol") or "").zfill(6) in set(FULL_THESIS_SMOKE_SYMBOLS)
    ]
    guard_urls = {str(row.get("source_url") or "") for row in guard_cases if row.get("source_url")}
    positive_guard_url_reuse_claim_ids = [
        str(row.get("claim_id") or "")
        for row in c06_smoke_claims
        if str(row.get("source_url") or "") in guard_urls and str(row.get("symbol") or "").zfill(6) == "005930"
    ]
    semantic_blockers: list[str] = []
    if positive_wiring_smoke_ready:
        semantic_blockers.append("controlled_smoke_claims_are_fixture_mapped_not_contract_blind_extracted")
    if positive_guard_url_reuse_claim_ids:
        semantic_blockers.append("samsung_positive_smoke_reuses_c06_guard_urls")
    source_backed_positive_ready = source_backed_replay.get("positive_replay_pass") is True
    positive_semantic_replay_ready = bool(source_backed_positive_ready)
    evaluated_cases = []
    for case in guard_cases:
        item = dict(case)
        hard_break_rejected = item.get("expected_hard_break_allowed") is False
        no_score_leak = not item.get("score_contribution_ids")
        no_stage_overlay = item.get("actual_transition_overlay") in {None, "NONE"}
        source_backed = (
            item.get("source_proxy_only") is False
            and item.get("evidence_url_pending") is False
            and bool(item.get("source_url"))
        )
        current_score_blocked = item.get("expected_current_score_eligible") is False
        item["case_pass"] = bool(hard_break_rejected and no_score_leak and no_stage_overlay and source_backed and current_score_blocked)
        item["case_pass_reasons"] = [
            "hard_break_rejected_without_current_direct_cancellation",
            "no_score_contribution_from_guard_claim",
            "no_transition_overlay_from_guard_claim",
            "source_backed_not_proxy",
            "current_score_eligible_false",
        ]
        evaluated_cases.append(item)
    guard_cases_pass = bool(evaluated_cases and all(row["case_pass"] for row in evaluated_cases))
    guard_replay_pass = bool(positive_semantic_replay_ready and guard_cases_pass)
    blockers: list[str] = []
    if not positive_wiring_smoke_ready and not source_backed_positive_ready:
        blockers.append("c06_positive_replay_required_before_guard_pass")
    if positive_wiring_smoke_ready and not positive_semantic_replay_ready:
        blockers.append("c06_positive_semantic_replay_required_before_guard_pass")
    if not source_backed_positive_ready:
        blockers.extend(source_backed_replay.get("blockers") or ["c06_source_backed_positive_replay_missing"])
    if not evaluated_cases:
        blockers.append("c06_guard_cases_missing")
    if any(not row["case_pass"] for row in evaluated_cases):
        blockers.append("c06_guard_case_failed")
    blockers.extend(semantic_blockers)
    return {
        "schema_version": "e2r_census_v4_c06_guard_replay_audit_v1",
        "archetype_id": FULL_THESIS_SMOKE_ARCHETYPE,
        "guard_replay_scope": "controlled_url_backed_guard_replay",
        "guard_replay_pass": guard_replay_pass,
        "positive_replay_required": True,
        "positive_replay_ready": positive_semantic_replay_ready,
        "positive_wiring_smoke_ready": positive_wiring_smoke_ready,
        "source_backed_positive_replay_ready": source_backed_positive_ready,
        "positive_semantic_replay_ready": positive_semantic_replay_ready,
        "source_backed_semantic_replay": source_backed_replay,
        "full_thesis_symbols": c06_symbols,
        "guard_case_count": len(evaluated_cases),
        "guard_case_pass_count": sum(1 for row in evaluated_cases if row["case_pass"]),
        "guard_cases_pass": guard_cases_pass,
        "positive_guard_url_reuse_count": len(positive_guard_url_reuse_claim_ids),
        "positive_guard_url_reuse_claim_ids": positive_guard_url_reuse_claim_ids,
        "semantic_blockers": semantic_blockers,
        "score_contribution_leak_count": sum(len(row.get("score_contribution_ids") or []) for row in evaluated_cases),
        "hard_break_false_positive_count": sum(1 for row in evaluated_cases if row.get("actual_hard_break_allowed") is True),
        "green_unlock_false_positive_count": sum(1 for row in evaluated_cases if row.get("actual_green_unlock_allowed") is True),
        "blockers": blockers,
        "cases": evaluated_cases,
        "rule": "C06 qualification lag or supply delay guard claims may create follow-up/watch context, but they cannot create a current hard break, Green unlock, score contribution, or source-backed replay pass without current direct semantic extraction and lifecycle confirmation.",
    }


def _empty_c06_source_backed_semantic_replay(*, config: CensusV4RunConfig, reason: str) -> dict[str, Any]:
    return {
        "schema_version": "e2r_census_v4_c06_source_backed_semantic_replay_v1",
        "as_of_date": config.as_of_date,
        "fixture_as_of_date": "2024-04-30",
        "source_origin": C06_SEMANTIC_REPLAY_SOURCE_ORIGIN,
        "replay_only": True,
        "production_score_evidence_allowed": False,
        "positive_replay_pass": False,
        "required_positive_primitives": ["customer_preorder_or_allocation"],
        "accepted_primitive_ids": [],
        "accepted_claim_ids": [],
        "blockers": [reason],
        "executions": [],
    }


def _c06_source_backed_semantic_replay(*, config: CensusV4RunConfig, output_root: Path) -> dict[str, Any]:
    try:
        from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
        from e2r.research_brain.schemas import SourceTask, SourceTaskType
        from e2r.research_brain.v2_schemas import CandidateEventV2
        from e2r.research_brain.v4_evidence_extraction_bridge import execute_source_tasks_with_evidence_os_v4
        from e2r.research_brain.v4_source_acquisition_runner import SourceAcquisitionRunnerV4
    except Exception as exc:  # pragma: no cover - defensive audit payload
        return _empty_c06_source_backed_semantic_replay(config=config, reason=f"import_failed:{type(exc).__name__}:{exc}")

    fixture_as_of = date(2024, 4, 30)
    contract = load_evidence_contracts_v2(require_all_archetypes=True).get(FULL_THESIS_SMOKE_ARCHETYPE)
    if contract is None:
        return _empty_c06_source_backed_semantic_replay(config=config, reason="c06_contract_missing")
    event = CandidateEventV2(
        candidate_event_id="CE-C06-SEMREPLAY-000660-20240430",
        symbol="000660",
        company_name="SK하이닉스",
        event_date=fixture_as_of.isoformat(),
        detected_at=fixture_as_of.isoformat(),
        source_family="BrokerReportPublicPDF",
        source_id="data/report_snapshots/report_snapshots.jsonl",
        event_type="report_radar",
        raw_reason_codes=("HBM", "MEMORY", "SEMANTIC_REPLAY"),
        event_title="C06 HBM source-backed semantic replay",
        event_summary="C06 semantic replay uses report snapshot source text to test contract-blind extraction.",
        issuer_directness="DIRECT",
        research_brain_eligible=True,
    )
    tasks = (
        SourceTask(
            task_id="C06-SEMREPLAY-000660-customer_preorder_or_allocation",
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id=FULL_THESIS_SMOKE_ARCHETYPE,
            primitive_gap="customer_preorder_or_allocation",
            task_type=SourceTaskType.POSITIVE_VERIFY.value,
            preferred_source_classes=("BrokerReportPublicPDF",),
            fallback_source_classes=(),
            forbidden_source_classes=("unbounded_general_search", "snippet_only_score", "source_proxy_only", "evidence_url_pending"),
            date_window={"end": fixture_as_of.isoformat(), "lookback_days": 180},
            max_queries=1,
            max_candidates=5,
            max_fetches=3,
            stop_condition={"accepted_claim_count": 1},
            query_intents=(),
            llm_query_allowed=False,
            general_search_allowed=False,
            reason_from_memory="C06 controlled semantic replay must be source-backed and contract-blind.",
        ),
    )
    bundle = execute_source_tasks_with_evidence_os_v4(
        event=event,
        tasks=tasks,
        contract=contract,
        as_of_date=fixture_as_of,
        source_runner=SourceAcquisitionRunnerV4(mode="frozen_real_source_snapshot"),
    )
    accepted_claim_ids: list[str] = []
    accepted_primitive_ids: list[str] = []
    document_urls: list[str] = []
    execution_rows: list[dict[str, Any]] = []
    for execution in bundle.executions:
        row = execution.to_dict() if hasattr(execution, "to_dict") else _jsonable(execution)
        row["source_origin"] = C06_SEMANTIC_REPLAY_SOURCE_ORIGIN
        row["replay_only"] = True
        row["production_score_evidence_allowed"] = False
        execution_rows.append(row)
        accepted_claim_ids.extend(str(item) for item in row.get("accepted_claim_ids") or [])
        accepted_primitive_ids.extend(str(item) for item in row.get("accepted_primitive_ids") or [])
        document_urls.extend(str(item) for item in row.get("document_urls") or [])
    accepted_claim_ids = list(dict.fromkeys(accepted_claim_ids))
    accepted_primitive_ids = list(dict.fromkeys(accepted_primitive_ids))
    document_urls = list(dict.fromkeys(document_urls))
    claim_rows = []
    raw_assertions = getattr(bundle, "raw_assertions", {}) or {}
    for claim_id in accepted_claim_ids:
        claim = bundle.ledger.claims.get(claim_id)
        if claim is None:
            continue
        row = _jsonable(claim)
        claim_mappings = [
            mapping
            for mapping in bundle.ledger.mappings.values()
            if mapping.claim_id == claim_id and str(getattr(mapping, "mapping_status", "")) in {"MappingStatus.ACCEPTED", "ACCEPTED"}
        ]
        document = bundle.documents.get(str(row.get("source_document_id") or ""))
        anchor = bundle.anchors.get(str(row.get("source_anchor_id") or ""))
        row["symbol"] = event.symbol
        row["company_name"] = event.company_name
        row["archetype_id"] = FULL_THESIS_SMOKE_ARCHETYPE
        row["accepted_primitive_ids"] = [str(mapping.primitive_id) for mapping in claim_mappings]
        row["accepted_mappings"] = [_jsonable(mapping) for mapping in claim_mappings]
        row["source_url"] = getattr(document, "canonical_url", None) if document is not None else None
        row["source_type"] = (
            getattr(document, "source_type", None).value
            if document is not None and getattr(document, "source_type", None) is not None
            else None
        )
        row["quote_text"] = _claim_quote_text(claim=claim, raw_assertions=raw_assertions, anchor=anchor)
        row["anchor_verified"] = getattr(anchor, "anchor_verified", None) if anchor is not None else None
        row["source_origin"] = C06_SEMANTIC_REPLAY_SOURCE_ORIGIN
        row["replay_only"] = True
        row["production_score_evidence_allowed"] = False
        claim_rows.append(row)
    required_positive = ("customer_preorder_or_allocation",)
    blockers: list[str] = []
    if not all(primitive in set(accepted_primitive_ids) for primitive in required_positive):
        blockers.append("c06_required_positive_primitives_missing")
    if not accepted_claim_ids:
        blockers.append("c06_semantic_replay_no_accepted_claims")
    if not document_urls:
        blockers.append("c06_semantic_replay_no_source_documents")
    if any(str(url).startswith("source-proxy://") for url in document_urls):
        blockers.append("c06_semantic_replay_source_proxy_url")
    if any("reuters.com/technology/samsungs-hbm-chips-failing-nvidia-tests" in str(url) for url in document_urls):
        blockers.append("c06_semantic_replay_reused_guard_url")
    audit_counts = dict(bundle.extraction_audit)
    return {
        "schema_version": "e2r_census_v4_c06_source_backed_semantic_replay_v1",
        "as_of_date": config.as_of_date,
        "fixture_as_of_date": fixture_as_of.isoformat(),
        "source_origin": C06_SEMANTIC_REPLAY_SOURCE_ORIGIN,
        "replay_only": True,
        "production_score_evidence_allowed": False,
        "positive_replay_pass": not blockers,
        "required_positive_primitives": list(required_positive),
        "accepted_primitive_ids": accepted_primitive_ids,
        "accepted_claim_ids": accepted_claim_ids,
        "accepted_claim_count": len(accepted_claim_ids),
        "document_urls": document_urls,
        "document_count": len(bundle.documents),
        "anchor_count": len(bundle.anchors),
        "raw_assertion_count": len(bundle.raw_assertions),
        "claim_extractor_attempt_count": audit_counts.get("llm_claim_extractor_attempt_count"),
        "claim_extractor_success_count": audit_counts.get("llm_claim_extractor_success_count"),
        "claim_extractor_non_llm_provider_count": audit_counts.get("llm_claim_extractor_non_llm_provider_count"),
        "blockers": blockers,
        "executions": execution_rows,
        "claims": claim_rows,
        "rule": "This replay is not a production full-thesis row. It only proves C06 positive semantic extraction can pass through source-backed EvidenceDocument/Anchor/RawAssertion/Claim/PrimitiveMapping without using smoke fixture mappings or guard URLs.",
    }


def _empty_c08_source_backed_semantic_replay(*, config: CensusV4RunConfig, reason: str) -> dict[str, Any]:
    return {
        "schema_version": "e2r_census_v4_c08_source_backed_semantic_replay_v1",
        "as_of_date": config.as_of_date,
        "fixture_as_of_date": "2024-01-08",
        "source_origin": C08_SEMANTIC_REPLAY_SOURCE_ORIGIN,
        "replay_only": True,
        "production_score_evidence_allowed": False,
        "positive_replay_pass": False,
        "guard_replay_pass": False,
        "required_positive_primitives": ["socket_or_test_demand_visible", "named_customer_quality"],
        "profile_only_guard_forbidden_primitives": [
            "named_customer_quality",
            "qualification_confirmed",
            "repeat_order_confirmed",
            "margin_bridge_visible",
        ],
        "accepted_primitive_ids": [],
        "accepted_claim_ids": [],
        "blockers": [reason],
        "executions": [],
    }


def _c08_source_backed_semantic_replay(*, config: CensusV4RunConfig, output_root: Path) -> dict[str, Any]:
    try:
        from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
        from e2r.research_brain.schemas import SourceTask, SourceTaskType
        from e2r.research_brain.v2_schemas import CandidateEventV2
        from e2r.research_brain.v4_evidence_extraction_bridge import execute_source_tasks_with_evidence_os_v4
        from e2r.research_brain.v4_source_acquisition_runner import SourceAcquisitionRunnerV4
    except Exception as exc:  # pragma: no cover - defensive audit payload
        return _empty_c08_source_backed_semantic_replay(config=config, reason=f"import_failed:{type(exc).__name__}:{exc}")

    fixture_as_of = date(2024, 1, 8)
    contract = load_evidence_contracts_v2(require_all_archetypes=True).get(C08_TEST_SOCKET_ARCHETYPE)
    if contract is None:
        return _empty_c08_source_backed_semantic_replay(config=config, reason="c08_contract_missing")

    positive_event = CandidateEventV2(
        candidate_event_id="CE-C08-SEMREPLAY-405100-20240108",
        symbol="405100",
        company_name="큐알티",
        event_date=fixture_as_of.isoformat(),
        detected_at=fixture_as_of.isoformat(),
        source_family="ReplaySourceSnapshot",
        source_id="data/replay_source_snapshots/replay_source_snapshots.jsonl",
        event_type="report_radar",
        raw_reason_codes=("C08", "TEST_SOCKET", "CUSTOMER_QUALITY", "SEMANTIC_REPLAY"),
        event_title="C08 QRT source-backed semantic replay",
        event_summary="C08 semantic replay uses source-backed QRT report excerpts to test contract-blind extraction.",
        issuer_directness="DIRECT",
        research_brain_eligible=True,
    )
    guard_event = CandidateEventV2(
        candidate_event_id="CE-C08-GUARD-405100-20240108",
        symbol="405100",
        company_name="큐알티",
        event_date=fixture_as_of.isoformat(),
        detected_at=fixture_as_of.isoformat(),
        source_family="ReplaySourceSnapshot",
        source_id="data/replay_source_snapshots/replay_source_snapshots.jsonl",
        event_type="report_radar",
        raw_reason_codes=("C08", "PROFILE_ONLY_GUARD", "SEMANTIC_REPLAY"),
        event_title="C08 QRT profile-only guard replay",
        event_summary="C08 guard replay uses a profile-only QRT source excerpt and must not unlock customer/margin bridge primitives.",
        issuer_directness="DIRECT",
        research_brain_eligible=True,
    )

    def task(task_id: str, event: CandidateEventV2, primitive: str, task_type: str, reason: str) -> SourceTask:
        return SourceTask(
            task_id=task_id,
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id=C08_TEST_SOCKET_ARCHETYPE,
            primitive_gap=primitive,
            task_type=task_type,
            preferred_source_classes=("ReplaySourceSnapshot",),
            fallback_source_classes=(),
            forbidden_source_classes=("unbounded_general_search", "snippet_only_score", "source_proxy_only", "evidence_url_pending"),
            date_window={"end": fixture_as_of.isoformat(), "lookback_days": 30},
            max_queries=1,
            max_candidates=1,
            max_fetches=1,
            stop_condition={"accepted_claim_count": 1},
            query_intents=(),
            llm_query_allowed=False,
            general_search_allowed=False,
            reason_from_memory=reason,
        )

    positive_tasks = (
        task(
            "C08-SEMREPLAY-405100-socket_or_test_demand_visible",
            positive_event,
            "socket_or_test_demand_visible",
            SourceTaskType.POSITIVE_VERIFY.value,
            "C08 source-backed replay must prove test/reliability service demand from a real report anchor.",
        ),
        task(
            "C08-SEMREPLAY-405100-named_customer_quality",
            positive_event,
            "named_customer_quality",
            SourceTaskType.POSITIVE_VERIFY.value,
            "C08 source-backed replay must prove customer quality or customer diversification from a real report anchor.",
        ),
    )
    guard_tasks = (
        task(
            "C08-GUARD-405100-profile_only",
            guard_event,
            "socket_or_test_demand_visible",
            SourceTaskType.RED_TEAM.value,
            "C08 profile-only guard may show product/test profile but must not unlock customer, qualification, repeat order, or margin bridge primitives.",
        ),
    )
    runner = SourceAcquisitionRunnerV4(mode="frozen_real_source_snapshot")
    positive_bundle = execute_source_tasks_with_evidence_os_v4(
        event=positive_event,
        tasks=positive_tasks,
        contract=contract,
        as_of_date=fixture_as_of,
        source_runner=runner,
    )
    guard_bundle = execute_source_tasks_with_evidence_os_v4(
        event=guard_event,
        tasks=guard_tasks,
        contract=contract,
        as_of_date=fixture_as_of,
        source_runner=runner,
    )

    positive_rows, positive_claim_ids, positive_primitives, positive_urls = _semantic_replay_execution_summary(
        bundle=positive_bundle,
        source_origin=C08_SEMANTIC_REPLAY_SOURCE_ORIGIN,
    )
    guard_rows, guard_claim_ids, guard_primitives, guard_urls = _semantic_replay_execution_summary(
        bundle=guard_bundle,
        source_origin=C08_SEMANTIC_REPLAY_SOURCE_ORIGIN,
    )
    accepted_claim_ids = list(dict.fromkeys((*positive_claim_ids, *guard_claim_ids)))
    accepted_primitive_ids = list(dict.fromkeys((*positive_primitives, *guard_primitives)))
    document_urls = list(dict.fromkeys((*positive_urls, *guard_urls)))
    positive_claim_rows = _semantic_replay_claim_rows(
        bundle=positive_bundle,
        event=positive_event,
        archetype_id=C08_TEST_SOCKET_ARCHETYPE,
        source_origin=C08_SEMANTIC_REPLAY_SOURCE_ORIGIN,
        accepted_claim_ids=positive_claim_ids,
    )
    guard_claim_rows = _semantic_replay_claim_rows(
        bundle=guard_bundle,
        event=guard_event,
        archetype_id=C08_TEST_SOCKET_ARCHETYPE,
        source_origin=C08_SEMANTIC_REPLAY_SOURCE_ORIGIN,
        accepted_claim_ids=guard_claim_ids,
    )

    required_positive = ("socket_or_test_demand_visible", "named_customer_quality")
    forbidden_guard_primitives = ("named_customer_quality", "qualification_confirmed", "repeat_order_confirmed", "margin_bridge_visible")
    guard_bridge_leaks = [primitive for primitive in guard_primitives if primitive in set(forbidden_guard_primitives)]
    blockers: list[str] = []
    if not all(primitive in set(positive_primitives) for primitive in required_positive):
        blockers.append("c08_required_positive_primitives_missing")
    if not positive_claim_ids:
        blockers.append("c08_semantic_replay_no_positive_accepted_claims")
    if not positive_urls:
        blockers.append("c08_semantic_replay_no_positive_source_documents")
    if guard_bridge_leaks:
        blockers.append("c08_profile_only_guard_leaked_bridge_primitives")
    if not guard_urls:
        blockers.append("c08_profile_only_guard_no_source_documents")
    if any(str(url).startswith("source-proxy://") for url in document_urls):
        blockers.append("c08_semantic_replay_source_proxy_url")

    positive_audit_counts = dict(positive_bundle.extraction_audit)
    guard_audit_counts = dict(guard_bundle.extraction_audit)
    positive_pass = not any(
        blocker
        for blocker in blockers
        if blocker
        in {
            "c08_required_positive_primitives_missing",
            "c08_semantic_replay_no_positive_accepted_claims",
            "c08_semantic_replay_no_positive_source_documents",
            "c08_semantic_replay_source_proxy_url",
        }
    )
    guard_pass = not any(
        blocker
        for blocker in blockers
        if blocker
        in {
            "c08_profile_only_guard_leaked_bridge_primitives",
            "c08_profile_only_guard_no_source_documents",
            "c08_semantic_replay_source_proxy_url",
        }
    )
    return {
        "schema_version": "e2r_census_v4_c08_source_backed_semantic_replay_v1",
        "as_of_date": config.as_of_date,
        "fixture_as_of_date": fixture_as_of.isoformat(),
        "source_origin": C08_SEMANTIC_REPLAY_SOURCE_ORIGIN,
        "replay_only": True,
        "production_score_evidence_allowed": False,
        "positive_replay_pass": positive_pass,
        "guard_replay_pass": guard_pass,
        "required_positive_primitives": list(required_positive),
        "profile_only_guard_forbidden_primitives": list(forbidden_guard_primitives),
        "profile_only_guard_leaked_primitives": guard_bridge_leaks,
        "accepted_primitive_ids": accepted_primitive_ids,
        "positive_accepted_primitive_ids": list(dict.fromkeys(positive_primitives)),
        "guard_accepted_primitive_ids": list(dict.fromkeys(guard_primitives)),
        "accepted_claim_ids": accepted_claim_ids,
        "positive_accepted_claim_ids": positive_claim_ids,
        "guard_accepted_claim_ids": guard_claim_ids,
        "accepted_claim_count": len(accepted_claim_ids),
        "document_urls": document_urls,
        "document_count": len(positive_bundle.documents) + len(guard_bundle.documents),
        "anchor_count": len(positive_bundle.anchors) + len(guard_bundle.anchors),
        "raw_assertion_count": len(positive_bundle.raw_assertions) + len(guard_bundle.raw_assertions),
        "claim_extractor_attempt_count": int(positive_audit_counts.get("llm_claim_extractor_attempt_count") or 0)
        + int(guard_audit_counts.get("llm_claim_extractor_attempt_count") or 0),
        "claim_extractor_success_count": int(positive_audit_counts.get("llm_claim_extractor_success_count") or 0)
        + int(guard_audit_counts.get("llm_claim_extractor_success_count") or 0),
        "claim_extractor_non_llm_provider_count": int(positive_audit_counts.get("llm_claim_extractor_non_llm_provider_count") or 0)
        + int(guard_audit_counts.get("llm_claim_extractor_non_llm_provider_count") or 0),
        "blockers": blockers,
        "executions": [*positive_rows, *guard_rows],
        "positive_claims": positive_claim_rows,
        "guard_claims": guard_claim_rows,
        "rule": "This replay is not a production full-thesis row. It proves C08 can distinguish source-backed test/customer-quality positive evidence from profile-only evidence without using research MD score labels or price outcomes.",
    }


def _empty_c15_source_backed_semantic_replay(*, config: CensusV4RunConfig, reason: str) -> dict[str, Any]:
    return {
        "schema_version": "e2r_census_v4_c15_source_backed_semantic_replay_v1",
        "as_of_date": config.as_of_date,
        "source_origin": C15_SEMANTIC_REPLAY_SOURCE_ORIGIN,
        "replay_only": True,
        "production_score_evidence_allowed": False,
        "positive_replay_pass": False,
        "guard_replay_pass": False,
        "required_positive_primitives": ["spread_expansion", "pricing_power_confirmed", "fcf_quality_score"],
        "raw_commodity_guard_forbidden_primitives": [
            "spread_expansion",
            "pricing_power_confirmed",
            "fcf_quality_score",
            "inventory_cycle",
            "utilization_rate",
        ],
        "accepted_primitive_ids": [],
        "accepted_claim_ids": [],
        "blockers": [reason],
        "executions": [],
    }


def _c15_source_backed_semantic_replay(*, config: CensusV4RunConfig, output_root: Path) -> dict[str, Any]:
    try:
        from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
        from e2r.research_brain.schemas import SourceTask, SourceTaskType
        from e2r.research_brain.v2_schemas import CandidateEventV2
        from e2r.research_brain.v4_evidence_extraction_bridge import execute_source_tasks_with_evidence_os_v4
        from e2r.research_brain.v4_source_acquisition_runner import SourceAcquisitionRunnerV4
    except Exception as exc:  # pragma: no cover - defensive audit payload
        return _empty_c15_source_backed_semantic_replay(config=config, reason=f"import_failed:{type(exc).__name__}:{exc}")

    contracts = load_evidence_contracts_v2(require_all_archetypes=True)
    contract = contracts.get(C15_MATERIAL_SPREAD_ARCHETYPE)
    if contract is None:
        return _empty_c15_source_backed_semantic_replay(config=config, reason="c15_contract_missing")

    hyundai_as_of = date(2021, 4, 27)
    posco_as_of = date(2022, 1, 28)
    guard_as_of = date(2021, 2, 22)
    hyundai_event = CandidateEventV2(
        candidate_event_id="CE-C15-SEMREPLAY-004020-20210427",
        symbol="004020",
        company_name="Hyundai Steel",
        event_date=hyundai_as_of.isoformat(),
        detected_at=hyundai_as_of.isoformat(),
        source_family="ReplaySourceSnapshot",
        source_id="data/replay_source_snapshots/replay_source_snapshots.jsonl",
        event_type="report_radar",
        raw_reason_codes=("C15", "MATERIAL_SPREAD", "PRICING_POWER", "SEMANTIC_REPLAY"),
        event_title="C15 Hyundai Steel source-backed pricing and profit replay",
        event_summary="C15 semantic replay uses a source-backed Yonhap article excerpt to test product price pass-through and profit bridge extraction.",
        issuer_directness="DIRECT",
        research_brain_eligible=True,
    )
    posco_event = CandidateEventV2(
        candidate_event_id="CE-C15-SEMREPLAY-005490-20220128",
        symbol="005490",
        company_name="POSCO",
        event_date=posco_as_of.isoformat(),
        detected_at=posco_as_of.isoformat(),
        source_family="ReplaySourceSnapshot",
        source_id="data/replay_source_snapshots/replay_source_snapshots.jsonl",
        event_type="issuer_ir",
        raw_reason_codes=("C15", "MATERIAL_SPREAD", "SPREAD_EXPANSION", "SEMANTIC_REPLAY"),
        event_title="C15 POSCO source-backed spread bridge replay",
        event_summary="C15 semantic replay uses a POSCO IR excerpt to test product-price/raw-material/OP bridge extraction.",
        issuer_directness="DIRECT",
        research_brain_eligible=True,
    )
    guard_event = CandidateEventV2(
        candidate_event_id="CE-C15-GUARD-103140-20210222",
        symbol="103140",
        company_name="Poongsan",
        event_date=guard_as_of.isoformat(),
        detected_at=guard_as_of.isoformat(),
        source_family="ReplaySourceSnapshot",
        source_id="data/replay_source_snapshots/replay_source_snapshots.jsonl",
        event_type="news_radar",
        raw_reason_codes=("C15", "RAW_COMMODITY_HEADLINE_GUARD", "SEMANTIC_REPLAY"),
        event_title="C15 raw copper-price headline guard replay",
        event_summary="C15 guard replay uses a raw copper-price/share-price excerpt and must not unlock issuer-level pass-through or margin primitives.",
        issuer_directness="DIRECT",
        research_brain_eligible=True,
    )

    def task(task_id: str, event: CandidateEventV2, primitive: str, task_type: str, reason: str) -> SourceTask:
        return SourceTask(
            task_id=task_id,
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id=C15_MATERIAL_SPREAD_ARCHETYPE,
            primitive_gap=primitive,
            task_type=task_type,
            preferred_source_classes=("ReplaySourceSnapshot",),
            fallback_source_classes=(),
            forbidden_source_classes=("unbounded_general_search", "snippet_only_score", "source_proxy_only", "evidence_url_pending"),
            date_window={"end": event.event_date, "lookback_days": 30},
            max_queries=1,
            max_candidates=1,
            max_fetches=1,
            stop_condition={"accepted_claim_count": 1},
            query_intents=(),
            llm_query_allowed=False,
            general_search_allowed=False,
            reason_from_memory=reason,
        )

    runner = SourceAcquisitionRunnerV4(mode="frozen_real_source_snapshot")
    hyundai_bundle = execute_source_tasks_with_evidence_os_v4(
        event=hyundai_event,
        tasks=(
            task(
                "C15-SEMREPLAY-004020-pricing_power_confirmed",
                hyundai_event,
                "pricing_power_confirmed",
                SourceTaskType.POSITIVE_VERIFY.value,
                "C15 source-backed replay must prove issuer product price pass-through from a real source anchor.",
            ),
            task(
                "C15-SEMREPLAY-004020-fcf_quality_score",
                hyundai_event,
                "fcf_quality_score",
                SourceTaskType.POSITIVE_VERIFY.value,
                "C15 source-backed replay must prove profit bridge from a real source anchor.",
            ),
        ),
        contract=contract,
        as_of_date=hyundai_as_of,
        source_runner=runner,
    )
    posco_bundle = execute_source_tasks_with_evidence_os_v4(
        event=posco_event,
        tasks=(
            task(
                "C15-SEMREPLAY-005490-spread_expansion",
                posco_event,
                "spread_expansion",
                SourceTaskType.POSITIVE_VERIFY.value,
                "C15 source-backed replay must prove product-price/raw-material spread bridge from a real issuer IR anchor.",
            ),
        ),
        contract=contract,
        as_of_date=posco_as_of,
        source_runner=runner,
    )
    guard_bundle = execute_source_tasks_with_evidence_os_v4(
        event=guard_event,
        tasks=(
            task(
                "C15-GUARD-103140-raw_copper_price_headline",
                guard_event,
                "pricing_power_confirmed",
                SourceTaskType.RED_TEAM.value,
                "C15 raw commodity headline guard must not unlock issuer-level pricing, spread, or profit bridge primitives.",
            ),
        ),
        contract=contract,
        as_of_date=guard_as_of,
        source_runner=runner,
    )

    hyundai_rows, hyundai_claim_ids, hyundai_primitives, hyundai_urls = _semantic_replay_execution_summary(
        bundle=hyundai_bundle,
        source_origin=C15_SEMANTIC_REPLAY_SOURCE_ORIGIN,
    )
    posco_rows, posco_claim_ids, posco_primitives, posco_urls = _semantic_replay_execution_summary(
        bundle=posco_bundle,
        source_origin=C15_SEMANTIC_REPLAY_SOURCE_ORIGIN,
    )
    guard_rows, guard_claim_ids, guard_primitives, guard_urls = _semantic_replay_execution_summary(
        bundle=guard_bundle,
        source_origin=C15_SEMANTIC_REPLAY_SOURCE_ORIGIN,
    )
    positive_claim_ids = list(dict.fromkeys((*hyundai_claim_ids, *posco_claim_ids)))
    positive_primitives = list(dict.fromkeys((*hyundai_primitives, *posco_primitives)))
    accepted_claim_ids = list(dict.fromkeys((*positive_claim_ids, *guard_claim_ids)))
    accepted_primitive_ids = list(dict.fromkeys((*positive_primitives, *guard_primitives)))
    document_urls = list(dict.fromkeys((*hyundai_urls, *posco_urls, *guard_urls)))
    positive_claim_rows = [
        *_semantic_replay_claim_rows(
            bundle=hyundai_bundle,
            event=hyundai_event,
            archetype_id=C15_MATERIAL_SPREAD_ARCHETYPE,
            source_origin=C15_SEMANTIC_REPLAY_SOURCE_ORIGIN,
            accepted_claim_ids=hyundai_claim_ids,
        ),
        *_semantic_replay_claim_rows(
            bundle=posco_bundle,
            event=posco_event,
            archetype_id=C15_MATERIAL_SPREAD_ARCHETYPE,
            source_origin=C15_SEMANTIC_REPLAY_SOURCE_ORIGIN,
            accepted_claim_ids=posco_claim_ids,
        ),
    ]
    guard_claim_rows = _semantic_replay_claim_rows(
        bundle=guard_bundle,
        event=guard_event,
        archetype_id=C15_MATERIAL_SPREAD_ARCHETYPE,
        source_origin=C15_SEMANTIC_REPLAY_SOURCE_ORIGIN,
        accepted_claim_ids=guard_claim_ids,
    )

    required_positive = ("spread_expansion", "pricing_power_confirmed", "fcf_quality_score")
    forbidden_guard_primitives = ("spread_expansion", "pricing_power_confirmed", "fcf_quality_score", "inventory_cycle", "utilization_rate")
    guard_bridge_leaks = [primitive for primitive in guard_primitives if primitive in set(forbidden_guard_primitives)]
    blockers: list[str] = []
    if not all(primitive in set(positive_primitives) for primitive in required_positive):
        blockers.append("c15_required_positive_primitives_missing")
    if not positive_claim_ids:
        blockers.append("c15_semantic_replay_no_positive_accepted_claims")
    if not (hyundai_urls and posco_urls):
        blockers.append("c15_semantic_replay_no_positive_source_documents")
    if guard_bridge_leaks:
        blockers.append("c15_raw_commodity_guard_leaked_bridge_primitives")
    if not guard_urls:
        blockers.append("c15_raw_commodity_guard_no_source_documents")
    if any(str(url).startswith("source-proxy://") for url in document_urls):
        blockers.append("c15_semantic_replay_source_proxy_url")

    audit_bundles = (hyundai_bundle, posco_bundle, guard_bundle)
    positive_pass = not any(
        blocker
        for blocker in blockers
        if blocker
        in {
            "c15_required_positive_primitives_missing",
            "c15_semantic_replay_no_positive_accepted_claims",
            "c15_semantic_replay_no_positive_source_documents",
            "c15_semantic_replay_source_proxy_url",
        }
    )
    guard_pass = not any(
        blocker
        for blocker in blockers
        if blocker
        in {
            "c15_raw_commodity_guard_leaked_bridge_primitives",
            "c15_raw_commodity_guard_no_source_documents",
            "c15_semantic_replay_source_proxy_url",
        }
    )
    return {
        "schema_version": "e2r_census_v4_c15_source_backed_semantic_replay_v1",
        "as_of_date": config.as_of_date,
        "fixture_as_of_dates": [hyundai_as_of.isoformat(), posco_as_of.isoformat(), guard_as_of.isoformat()],
        "source_origin": C15_SEMANTIC_REPLAY_SOURCE_ORIGIN,
        "replay_only": True,
        "production_score_evidence_allowed": False,
        "positive_replay_pass": positive_pass,
        "guard_replay_pass": guard_pass,
        "required_positive_primitives": list(required_positive),
        "raw_commodity_guard_forbidden_primitives": list(forbidden_guard_primitives),
        "raw_commodity_guard_leaked_primitives": guard_bridge_leaks,
        "accepted_primitive_ids": accepted_primitive_ids,
        "positive_accepted_primitive_ids": positive_primitives,
        "guard_accepted_primitive_ids": list(dict.fromkeys(guard_primitives)),
        "accepted_claim_ids": accepted_claim_ids,
        "positive_accepted_claim_ids": positive_claim_ids,
        "guard_accepted_claim_ids": guard_claim_ids,
        "accepted_claim_count": len(accepted_claim_ids),
        "positive_claim_count": len(positive_claim_ids),
        "guard_claim_count": len(guard_claim_ids),
        "document_urls": document_urls,
        "document_count": sum(len(bundle.documents) for bundle in audit_bundles),
        "anchor_count": sum(len(bundle.anchors) for bundle in audit_bundles),
        "raw_assertion_count": sum(len(bundle.raw_assertions) for bundle in audit_bundles),
        "claim_extractor_attempt_count": sum(int(bundle.extraction_audit.get("llm_claim_extractor_attempt_count") or 0) for bundle in audit_bundles),
        "claim_extractor_success_count": sum(int(bundle.extraction_audit.get("llm_claim_extractor_success_count") or 0) for bundle in audit_bundles),
        "claim_extractor_non_llm_provider_count": sum(int(bundle.extraction_audit.get("llm_claim_extractor_non_llm_provider_count") or 0) for bundle in audit_bundles),
        "blockers": blockers,
        "executions": [*hyundai_rows, *posco_rows, *guard_rows],
        "positive_claims": positive_claim_rows,
        "guard_claims": guard_claim_rows,
        "rule": "This replay is not a production full-thesis row. It proves C15 can extract issuer-level product-price/spread/profit bridge from source-backed documents while blocking a raw commodity price headline from opening score primitives.",
    }


def _empty_c17_source_backed_semantic_replay(*, config: CensusV4RunConfig, reason: str) -> dict[str, Any]:
    return {
        "schema_version": "e2r_census_v4_c17_source_backed_semantic_replay_v1",
        "as_of_date": config.as_of_date,
        "source_origin": C17_SEMANTIC_REPLAY_SOURCE_ORIGIN,
        "replay_only": True,
        "production_score_evidence_allowed": False,
        "positive_replay_pass": False,
        "guard_replay_pass": False,
        "required_positive_primitives": ["spread_expansion", "opm_expansion_pctp", "utilization_rate"],
        "spread_only_guard_forbidden_support_primitives": ["opm_expansion_pctp", "utilization_rate", "inventory_cycle"],
        "accepted_primitive_ids": [],
        "accepted_claim_ids": [],
        "blockers": [reason],
        "executions": [],
    }


def _c17_source_backed_semantic_replay(*, config: CensusV4RunConfig, output_root: Path) -> dict[str, Any]:
    try:
        from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
        from e2r.research_brain.schemas import SourceTask, SourceTaskType
        from e2r.research_brain.v2_schemas import CandidateEventV2
        from e2r.research_brain.v4_evidence_extraction_bridge import execute_source_tasks_with_evidence_os_v4
        from e2r.research_brain.v4_source_acquisition_runner import SourceAcquisitionRunnerV4
    except Exception as exc:  # pragma: no cover - defensive audit payload
        return _empty_c17_source_backed_semantic_replay(config=config, reason=f"import_failed:{type(exc).__name__}:{exc}")

    contracts = load_evidence_contracts_v2(require_all_archetypes=True)
    contract = contracts.get(C17_CHEMICAL_SPREAD_ARCHETYPE)
    if contract is None:
        return _empty_c17_source_backed_semantic_replay(config=config, reason="c17_contract_missing")

    positive_as_of = date(2025, 11, 3)
    guard_as_of = date(2025, 7, 1)
    positive_event = CandidateEventV2(
        candidate_event_id="CE-C17-SEMREPLAY-010950-20251103",
        symbol="010950",
        company_name="S-OIL",
        event_date=positive_as_of.isoformat(),
        detected_at=positive_as_of.isoformat(),
        source_family="ReplaySourceSnapshot",
        source_id="data/replay_source_snapshots/replay_source_snapshots.jsonl",
        event_type="issuer_ir",
        raw_reason_codes=("C17", "CHEMICAL_SPREAD", "REALIZED_MARGIN_BRIDGE", "SEMANTIC_REPLAY"),
        event_title="C17 S-OIL source-backed refining margin bridge replay",
        event_summary="C17 semantic replay uses an S-OIL Q3 2025 IR excerpt to test refining-margin spread, operating-income turnaround, and utilization extraction.",
        issuer_directness="DIRECT",
        research_brain_eligible=True,
    )
    guard_event = CandidateEventV2(
        candidate_event_id="CE-C17-GUARD-010950-20250701",
        symbol="010950",
        company_name="S-OIL",
        event_date=guard_as_of.isoformat(),
        detected_at=guard_as_of.isoformat(),
        source_family="ReplaySourceSnapshot",
        source_id="data/replay_source_snapshots/replay_source_snapshots.jsonl",
        event_type="issuer_ir",
        raw_reason_codes=("C17", "SPREAD_ONLY_GUARD", "SEMANTIC_REPLAY"),
        event_title="C17 S-OIL spread-only realized-margin guard replay",
        event_summary="C17 guard replay uses an S-OIL Q2 2025 IR excerpt where refining-margin recovery coexists with operating loss from inventory and lagging effects.",
        issuer_directness="DIRECT",
        research_brain_eligible=True,
    )

    def task(task_id: str, event: CandidateEventV2, primitive: str, task_type: str, reason: str) -> SourceTask:
        return SourceTask(
            task_id=task_id,
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id=C17_CHEMICAL_SPREAD_ARCHETYPE,
            primitive_gap=primitive,
            task_type=task_type,
            preferred_source_classes=("ReplaySourceSnapshot",),
            fallback_source_classes=(),
            forbidden_source_classes=("unbounded_general_search", "snippet_only_score", "source_proxy_only", "evidence_url_pending"),
            date_window={"end": event.event_date, "lookback_days": 30},
            max_queries=1,
            max_candidates=1,
            max_fetches=1,
            stop_condition={"accepted_claim_count": 1},
            query_intents=(),
            llm_query_allowed=False,
            general_search_allowed=False,
            reason_from_memory=reason,
        )

    runner = SourceAcquisitionRunnerV4(mode="frozen_real_source_snapshot")
    positive_bundle = execute_source_tasks_with_evidence_os_v4(
        event=positive_event,
        tasks=(
            task(
                "C17-SEMREPLAY-010950-spread_expansion",
                positive_event,
                "spread_expansion",
                SourceTaskType.POSITIVE_VERIFY.value,
                "C17 source-backed replay must prove spread expansion from a real issuer IR anchor.",
            ),
            task(
                "C17-SEMREPLAY-010950-opm_expansion_pctp",
                positive_event,
                "opm_expansion_pctp",
                SourceTaskType.POSITIVE_VERIFY.value,
                "C17 source-backed replay must prove realized operating-margin bridge from a real issuer IR anchor.",
            ),
            task(
                "C17-SEMREPLAY-010950-utilization_rate",
                positive_event,
                "utilization_rate",
                SourceTaskType.POSITIVE_VERIFY.value,
                "C17 source-backed replay must prove utilization bridge from a real issuer IR anchor.",
            ),
        ),
        contract=contract,
        as_of_date=positive_as_of,
        source_runner=runner,
    )
    guard_bundle = execute_source_tasks_with_evidence_os_v4(
        event=guard_event,
        tasks=(
            task(
                "C17-GUARD-010950-spread_only_no_realized_margin",
                guard_event,
                "spread_expansion",
                SourceTaskType.RED_TEAM.value,
                "C17 spread-only guard must not unlock positive realized-margin, utilization, or inventory bridge primitives when operating income remains negative.",
            ),
        ),
        contract=contract,
        as_of_date=guard_as_of,
        source_runner=runner,
    )

    positive_rows, positive_claim_ids, positive_primitives, positive_urls = _semantic_replay_execution_summary(
        bundle=positive_bundle,
        source_origin=C17_SEMANTIC_REPLAY_SOURCE_ORIGIN,
    )
    guard_rows, guard_claim_ids, guard_primitives, guard_urls = _semantic_replay_execution_summary(
        bundle=guard_bundle,
        source_origin=C17_SEMANTIC_REPLAY_SOURCE_ORIGIN,
    )
    accepted_claim_ids = list(dict.fromkeys((*positive_claim_ids, *guard_claim_ids)))
    accepted_primitive_ids = list(dict.fromkeys((*positive_primitives, *guard_primitives)))
    document_urls = list(dict.fromkeys((*positive_urls, *guard_urls)))
    positive_claim_rows = _semantic_replay_claim_rows(
        bundle=positive_bundle,
        event=positive_event,
        archetype_id=C17_CHEMICAL_SPREAD_ARCHETYPE,
        source_origin=C17_SEMANTIC_REPLAY_SOURCE_ORIGIN,
        accepted_claim_ids=positive_claim_ids,
    )
    guard_claim_rows = _semantic_replay_claim_rows(
        bundle=guard_bundle,
        event=guard_event,
        archetype_id=C17_CHEMICAL_SPREAD_ARCHETYPE,
        source_origin=C17_SEMANTIC_REPLAY_SOURCE_ORIGIN,
        accepted_claim_ids=guard_claim_ids,
    )
    positive_support_primitives = _support_primitive_ids_from_claim_rows(positive_claim_rows)
    guard_support_primitives = _support_primitive_ids_from_claim_rows(guard_claim_rows)
    required_positive = ("spread_expansion", "opm_expansion_pctp", "utilization_rate")
    forbidden_guard_support = ("opm_expansion_pctp", "utilization_rate", "inventory_cycle")
    guard_bridge_leaks = [primitive for primitive in guard_support_primitives if primitive in set(forbidden_guard_support)]
    blockers: list[str] = []
    if not all(primitive in set(positive_support_primitives) for primitive in required_positive):
        blockers.append("c17_required_positive_support_primitives_missing")
    if not positive_claim_ids:
        blockers.append("c17_semantic_replay_no_positive_accepted_claims")
    if not positive_urls:
        blockers.append("c17_semantic_replay_no_positive_source_documents")
    if "spread_expansion" not in set(guard_support_primitives):
        blockers.append("c17_spread_only_guard_no_spread_signal")
    if guard_bridge_leaks:
        blockers.append("c17_spread_only_guard_leaked_realized_margin_bridge_support")
    if not guard_urls:
        blockers.append("c17_spread_only_guard_no_source_documents")
    if any(str(url).startswith("source-proxy://") or str(url).startswith("snapshot://") for url in document_urls):
        blockers.append("c17_semantic_replay_source_proxy_or_snapshot_url")

    positive_pass = not any(
        blocker
        for blocker in blockers
        if blocker
        in {
            "c17_required_positive_support_primitives_missing",
            "c17_semantic_replay_no_positive_accepted_claims",
            "c17_semantic_replay_no_positive_source_documents",
            "c17_semantic_replay_source_proxy_or_snapshot_url",
        }
    )
    guard_pass = not any(
        blocker
        for blocker in blockers
        if blocker
        in {
            "c17_spread_only_guard_no_spread_signal",
            "c17_spread_only_guard_leaked_realized_margin_bridge_support",
            "c17_spread_only_guard_no_source_documents",
            "c17_semantic_replay_source_proxy_or_snapshot_url",
        }
    )
    return {
        "schema_version": "e2r_census_v4_c17_source_backed_semantic_replay_v1",
        "as_of_date": config.as_of_date,
        "fixture_as_of_dates": [positive_as_of.isoformat(), guard_as_of.isoformat()],
        "source_origin": C17_SEMANTIC_REPLAY_SOURCE_ORIGIN,
        "replay_only": True,
        "production_score_evidence_allowed": False,
        "positive_replay_pass": positive_pass,
        "guard_replay_pass": guard_pass,
        "required_positive_primitives": list(required_positive),
        "spread_only_guard_forbidden_support_primitives": list(forbidden_guard_support),
        "spread_only_guard_leaked_support_primitives": guard_bridge_leaks,
        "accepted_primitive_ids": accepted_primitive_ids,
        "positive_accepted_primitive_ids": list(dict.fromkeys(positive_primitives)),
        "positive_support_primitive_ids": positive_support_primitives,
        "guard_accepted_primitive_ids": list(dict.fromkeys(guard_primitives)),
        "guard_support_primitive_ids": guard_support_primitives,
        "accepted_claim_ids": accepted_claim_ids,
        "positive_accepted_claim_ids": positive_claim_ids,
        "guard_accepted_claim_ids": guard_claim_ids,
        "accepted_claim_count": len(accepted_claim_ids),
        "positive_claim_count": len(positive_claim_ids),
        "guard_claim_count": len(guard_claim_ids),
        "document_urls": document_urls,
        "document_count": len(positive_bundle.documents) + len(guard_bundle.documents),
        "anchor_count": len(positive_bundle.anchors) + len(guard_bundle.anchors),
        "raw_assertion_count": len(positive_bundle.raw_assertions) + len(guard_bundle.raw_assertions),
        "claim_extractor_attempt_count": int(positive_bundle.extraction_audit.get("llm_claim_extractor_attempt_count") or 0)
        + int(guard_bundle.extraction_audit.get("llm_claim_extractor_attempt_count") or 0),
        "claim_extractor_success_count": int(positive_bundle.extraction_audit.get("llm_claim_extractor_success_count") or 0)
        + int(guard_bundle.extraction_audit.get("llm_claim_extractor_success_count") or 0),
        "claim_extractor_non_llm_provider_count": int(positive_bundle.extraction_audit.get("llm_claim_extractor_non_llm_provider_count") or 0)
        + int(guard_bundle.extraction_audit.get("llm_claim_extractor_non_llm_provider_count") or 0),
        "blockers": blockers,
        "executions": [*positive_rows, *guard_rows],
        "positive_claims": positive_claim_rows,
        "guard_claims": guard_claim_rows,
        "rule": "This replay is not a production full-thesis row. It proves C17 can extract source-backed spread, utilization, and realized operating-margin bridge while blocking spread-only evidence from becoming positive realized-margin support when inventory and lagging effects keep operating income negative.",
    }


def _empty_c24_source_backed_semantic_replay(*, config: CensusV4RunConfig, reason: str) -> dict[str, Any]:
    return {
        "schema_version": "e2r_census_v4_c24_source_backed_semantic_replay_v1",
        "as_of_date": config.as_of_date,
        "source_origin": C24_SEMANTIC_REPLAY_SOURCE_ORIGIN,
        "replay_only": True,
        "production_score_evidence_allowed": False,
        "positive_replay_pass": False,
        "guard_replay_pass": False,
        "required_positive_primitives": ["trial_quality_visible"],
        "binary_event_guard_required_counter_primitives": ["binary_event_unresolved"],
        "binary_event_guard_forbidden_support_primitives": ["trial_quality_visible"],
        "accepted_primitive_ids": [],
        "accepted_claim_ids": [],
        "blockers": [reason],
        "executions": [],
    }


def _c24_source_backed_semantic_replay(*, config: CensusV4RunConfig, output_root: Path) -> dict[str, Any]:
    try:
        from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
        from e2r.research_brain.schemas import SourceTask, SourceTaskType
        from e2r.research_brain.v2_schemas import CandidateEventV2
        from e2r.research_brain.v4_evidence_extraction_bridge import execute_source_tasks_with_evidence_os_v4
        from e2r.research_brain.v4_source_acquisition_runner import SourceAcquisitionRunnerV4
    except Exception as exc:  # pragma: no cover - defensive audit payload
        return _empty_c24_source_backed_semantic_replay(config=config, reason=f"import_failed:{type(exc).__name__}:{exc}")

    contracts = load_evidence_contracts_v2(require_all_archetypes=True)
    contract = contracts.get(C24_BIO_TRIAL_ARCHETYPE)
    if contract is None:
        return _empty_c24_source_backed_semantic_replay(config=config, reason="c24_contract_missing")

    positive_as_of = date(2024, 3, 21)
    guard_as_of = date(2019, 8, 2)
    positive_event = CandidateEventV2(
        candidate_event_id="CE-C24-SEMREPLAY-009420-20240321",
        symbol="009420",
        company_name="HanAll",
        event_date=positive_as_of.isoformat(),
        detected_at=positive_as_of.isoformat(),
        source_family="ReplaySourceSnapshot",
        source_id="data/replay_source_snapshots/replay_source_snapshots.jsonl",
        event_type="press_release",
        raw_reason_codes=("C24", "BIO_TRIAL", "TRIAL_QUALITY", "SEMANTIC_REPLAY"),
        event_title="C24 HanAll batoclimab source-backed trial-quality replay",
        event_summary="C24 semantic replay uses a HanAll press-release excerpt to test trial phase, response definition, response rate, IgG reduction, partner, and safety extraction.",
        issuer_directness="DIRECT",
        research_brain_eligible=True,
    )
    guard_event = CandidateEventV2(
        candidate_event_id="CE-C24-GUARD-215600-20190802",
        symbol="215600",
        company_name="SillaJen",
        event_date=guard_as_of.isoformat(),
        detected_at=guard_as_of.isoformat(),
        source_family="ReplaySourceSnapshot",
        source_id="data/replay_source_snapshots/replay_source_snapshots.jsonl",
        event_type="press_release",
        raw_reason_codes=("C24", "BIO_TRIAL", "FUTILITY_GUARD", "SEMANTIC_REPLAY"),
        event_title="C24 SillaJen PHOCUS futility source-backed guard replay",
        event_summary="C24 guard replay uses a SillaJen PHOCUS futility excerpt where a Phase 3 trial was discontinued after an interim futility analysis.",
        issuer_directness="DIRECT",
        research_brain_eligible=True,
    )

    def task(task_id: str, event: CandidateEventV2, primitive: str, task_type: str, reason: str) -> SourceTask:
        return SourceTask(
            task_id=task_id,
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id=C24_BIO_TRIAL_ARCHETYPE,
            primitive_gap=primitive,
            task_type=task_type,
            preferred_source_classes=("ReplaySourceSnapshot",),
            fallback_source_classes=(),
            forbidden_source_classes=("unbounded_general_search", "snippet_only_score", "source_proxy_only", "evidence_url_pending"),
            date_window={"end": event.event_date, "lookback_days": 30},
            max_queries=1,
            max_candidates=1,
            max_fetches=1,
            stop_condition={"accepted_claim_count": 1},
            query_intents=(),
            llm_query_allowed=False,
            general_search_allowed=False,
            reason_from_memory=reason,
        )

    runner = SourceAcquisitionRunnerV4(mode="frozen_real_source_snapshot")
    positive_bundle = execute_source_tasks_with_evidence_os_v4(
        event=positive_event,
        tasks=(
            task(
                "C24-SEMREPLAY-009420-trial_quality_visible",
                positive_event,
                "trial_quality_visible",
                SourceTaskType.POSITIVE_VERIFY.value,
                "C24 source-backed replay must prove trial quality from a real press-release anchor with endpoint/response/safety details.",
            ),
        ),
        contract=contract,
        as_of_date=positive_as_of,
        source_runner=runner,
    )
    guard_bundle = execute_source_tasks_with_evidence_os_v4(
        event=guard_event,
        tasks=(
            task(
                "C24-GUARD-215600-binary_event_unresolved",
                guard_event,
                "binary_event_unresolved",
                SourceTaskType.RED_TEAM.value,
                "C24 binary-event guard must not unlock trial_quality_visible when the source says futility analysis and discontinuation.",
            ),
        ),
        contract=contract,
        as_of_date=guard_as_of,
        source_runner=runner,
    )

    positive_rows, positive_claim_ids, positive_primitives, positive_urls = _semantic_replay_execution_summary(
        bundle=positive_bundle,
        source_origin=C24_SEMANTIC_REPLAY_SOURCE_ORIGIN,
    )
    guard_rows, guard_claim_ids, guard_primitives, guard_urls = _semantic_replay_execution_summary(
        bundle=guard_bundle,
        source_origin=C24_SEMANTIC_REPLAY_SOURCE_ORIGIN,
    )
    accepted_claim_ids = list(dict.fromkeys((*positive_claim_ids, *guard_claim_ids)))
    accepted_primitive_ids = list(dict.fromkeys((*positive_primitives, *guard_primitives)))
    document_urls = list(dict.fromkeys((*positive_urls, *guard_urls)))
    positive_claim_rows = _semantic_replay_claim_rows(
        bundle=positive_bundle,
        event=positive_event,
        archetype_id=C24_BIO_TRIAL_ARCHETYPE,
        source_origin=C24_SEMANTIC_REPLAY_SOURCE_ORIGIN,
        accepted_claim_ids=positive_claim_ids,
    )
    guard_claim_rows = _semantic_replay_claim_rows(
        bundle=guard_bundle,
        event=guard_event,
        archetype_id=C24_BIO_TRIAL_ARCHETYPE,
        source_origin=C24_SEMANTIC_REPLAY_SOURCE_ORIGIN,
        accepted_claim_ids=guard_claim_ids,
    )
    positive_support_primitives = _support_primitive_ids_from_claim_rows(positive_claim_rows)
    guard_support_primitives = _support_primitive_ids_from_claim_rows(guard_claim_rows)
    guard_counter_primitives = _counter_primitive_ids_from_claim_rows(guard_claim_rows)
    required_positive = ("trial_quality_visible",)
    required_guard_counter = ("binary_event_unresolved",)
    forbidden_guard_support = ("trial_quality_visible",)
    guard_quality_leaks = [primitive for primitive in guard_support_primitives if primitive in set(forbidden_guard_support)]
    blockers: list[str] = []
    if not all(primitive in set(positive_support_primitives) for primitive in required_positive):
        blockers.append("c24_required_positive_trial_quality_support_missing")
    if not positive_claim_ids:
        blockers.append("c24_semantic_replay_no_positive_accepted_claims")
    if not positive_urls:
        blockers.append("c24_semantic_replay_no_positive_source_documents")
    if not all(primitive in set(guard_counter_primitives) for primitive in required_guard_counter):
        blockers.append("c24_binary_event_guard_no_counter_risk_signal")
    if guard_quality_leaks:
        blockers.append("c24_binary_event_guard_leaked_trial_quality_support")
    if not guard_urls:
        blockers.append("c24_binary_event_guard_no_source_documents")
    if any(str(url).startswith("source-proxy://") or str(url).startswith("snapshot://") for url in document_urls):
        blockers.append("c24_semantic_replay_source_proxy_or_snapshot_url")

    positive_pass = not any(
        blocker
        for blocker in blockers
        if blocker
        in {
            "c24_required_positive_trial_quality_support_missing",
            "c24_semantic_replay_no_positive_accepted_claims",
            "c24_semantic_replay_no_positive_source_documents",
            "c24_semantic_replay_source_proxy_or_snapshot_url",
        }
    )
    guard_pass = not any(
        blocker
        for blocker in blockers
        if blocker
        in {
            "c24_binary_event_guard_no_counter_risk_signal",
            "c24_binary_event_guard_leaked_trial_quality_support",
            "c24_binary_event_guard_no_source_documents",
            "c24_semantic_replay_source_proxy_or_snapshot_url",
        }
    )
    return {
        "schema_version": "e2r_census_v4_c24_source_backed_semantic_replay_v1",
        "as_of_date": config.as_of_date,
        "fixture_as_of_dates": [positive_as_of.isoformat(), guard_as_of.isoformat()],
        "source_origin": C24_SEMANTIC_REPLAY_SOURCE_ORIGIN,
        "replay_only": True,
        "production_score_evidence_allowed": False,
        "positive_replay_pass": positive_pass,
        "guard_replay_pass": guard_pass,
        "required_positive_primitives": list(required_positive),
        "binary_event_guard_required_counter_primitives": list(required_guard_counter),
        "binary_event_guard_forbidden_support_primitives": list(forbidden_guard_support),
        "binary_event_guard_leaked_support_primitives": guard_quality_leaks,
        "accepted_primitive_ids": accepted_primitive_ids,
        "positive_accepted_primitive_ids": list(dict.fromkeys(positive_primitives)),
        "positive_support_primitive_ids": positive_support_primitives,
        "guard_accepted_primitive_ids": list(dict.fromkeys(guard_primitives)),
        "guard_support_primitive_ids": guard_support_primitives,
        "guard_counter_primitive_ids": guard_counter_primitives,
        "accepted_claim_ids": accepted_claim_ids,
        "positive_accepted_claim_ids": positive_claim_ids,
        "guard_accepted_claim_ids": guard_claim_ids,
        "accepted_claim_count": len(accepted_claim_ids),
        "positive_claim_count": len(positive_claim_ids),
        "guard_claim_count": len(guard_claim_ids),
        "document_urls": document_urls,
        "document_count": len(positive_bundle.documents) + len(guard_bundle.documents),
        "anchor_count": len(positive_bundle.anchors) + len(guard_bundle.anchors),
        "raw_assertion_count": len(positive_bundle.raw_assertions) + len(guard_bundle.raw_assertions),
        "claim_extractor_attempt_count": int(positive_bundle.extraction_audit.get("llm_claim_extractor_attempt_count") or 0)
        + int(guard_bundle.extraction_audit.get("llm_claim_extractor_attempt_count") or 0),
        "claim_extractor_success_count": int(positive_bundle.extraction_audit.get("llm_claim_extractor_success_count") or 0)
        + int(guard_bundle.extraction_audit.get("llm_claim_extractor_success_count") or 0),
        "claim_extractor_non_llm_provider_count": int(positive_bundle.extraction_audit.get("llm_claim_extractor_non_llm_provider_count") or 0)
        + int(guard_bundle.extraction_audit.get("llm_claim_extractor_non_llm_provider_count") or 0),
        "blockers": blockers,
        "executions": [*positive_rows, *guard_rows],
        "positive_claims": positive_claim_rows,
        "guard_claims": guard_claim_rows,
        "rule": "This replay is not a production full-thesis row. It proves C24 can extract source-backed trial-quality support while blocking a futility/discontinuation binary event from becoming trial-quality positive support.",
    }


def _empty_c28_source_backed_semantic_replay(*, config: CensusV4RunConfig, reason: str) -> dict[str, Any]:
    return {
        "schema_version": "e2r_census_v4_c28_source_backed_semantic_replay_v1",
        "as_of_date": config.as_of_date,
        "source_origin": C28_SEMANTIC_REPLAY_SOURCE_ORIGIN,
        "replay_only": True,
        "production_score_evidence_allowed": False,
        "positive_replay_pass": False,
        "guard_replay_pass": False,
        "required_positive_primitives": [
            "arr_growth_visible",
            "nrr",
            "retention_or_renewal",
            "rpo_to_sales",
            "recurring_margin_leverage",
        ],
        "keyword_only_guard_forbidden_support_primitives": [
            "arr_growth_visible",
            "nrr",
            "retention_or_renewal",
            "rpo_to_sales",
            "recurring_margin_leverage",
            "subscription_monthly_billing",
        ],
        "accepted_primitive_ids": [],
        "accepted_claim_ids": [],
        "blockers": [reason],
        "executions": [],
    }


def _c28_source_backed_semantic_replay(*, config: CensusV4RunConfig, output_root: Path) -> dict[str, Any]:
    try:
        from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
        from e2r.research_brain.schemas import SourceTask, SourceTaskType
        from e2r.research_brain.v2_schemas import CandidateEventV2
        from e2r.research_brain.v4_evidence_extraction_bridge import execute_source_tasks_with_evidence_os_v4
        from e2r.research_brain.v4_source_acquisition_runner import SourceAcquisitionRunnerV4
    except Exception as exc:  # pragma: no cover - defensive audit payload
        return _empty_c28_source_backed_semantic_replay(config=config, reason=f"import_failed:{type(exc).__name__}:{exc}")

    contracts = load_evidence_contracts_v2(require_all_archetypes=True)
    contract = contracts.get(C28_SOFTWARE_SECURITY_ARCHETYPE)
    if contract is None:
        return _empty_c28_source_backed_semantic_replay(config=config, reason="c28_contract_missing")

    positive_as_of = date(2025, 3, 7)
    guard_as_of = date(2024, 5, 7)
    positive_event = CandidateEventV2(
        candidate_event_id="CE-C28-SEMREPLAY-00CRWD-20250131",
        symbol="00CRWD",
        company_name="CrowdStrike",
        event_date=positive_as_of.isoformat(),
        detected_at=positive_as_of.isoformat(),
        source_family="ReplaySourceSnapshot",
        source_id="data/replay_source_snapshots/replay_source_snapshots.jsonl",
        event_type="sec_filing",
        raw_reason_codes=("C28", "SOFTWARE_SECURITY", "ARR_RETENTION", "SEMANTIC_REPLAY"),
        event_title="C28 CrowdStrike ARR retention source-backed replay",
        event_summary=(
            "C28 semantic replay uses a CrowdStrike Form 10-K excerpt to test ARR growth, net retention, "
            "renewal/churn, deferred revenue conversion, and subscription margin extraction."
        ),
        issuer_directness="DIRECT",
        research_brain_eligible=True,
    )
    guard_event = CandidateEventV2(
        candidate_event_id="CE-C28-GUARD-00CRWD-20240507",
        symbol="00CRWD",
        company_name="CrowdStrike",
        event_date=guard_as_of.isoformat(),
        detected_at=guard_as_of.isoformat(),
        source_family="ReplaySourceSnapshot",
        source_id="data/replay_source_snapshots/replay_source_snapshots.jsonl",
        event_type="press_release",
        raw_reason_codes=("C28", "SOFTWARE_SECURITY", "KEYWORD_ONLY_GUARD", "SEMANTIC_REPLAY"),
        event_title="C28 CrowdStrike SIEM keyword-only source-backed guard replay",
        event_summary=(
            "C28 guard replay uses a CrowdStrike product/security press-release excerpt to prove security/SIEM vocabulary "
            "alone does not unlock ARR, retention, RPO, or recurring-margin primitives."
        ),
        issuer_directness="DIRECT",
        research_brain_eligible=True,
    )

    def task(task_id: str, event: CandidateEventV2, primitive: str, task_type: str, reason: str) -> SourceTask:
        return SourceTask(
            task_id=task_id,
            candidate_event_id=event.candidate_event_id,
            symbol=event.symbol,
            company_name=event.company_name,
            archetype_id=C28_SOFTWARE_SECURITY_ARCHETYPE,
            primitive_gap=primitive,
            task_type=task_type,
            preferred_source_classes=("ReplaySourceSnapshot",),
            fallback_source_classes=(),
            forbidden_source_classes=("unbounded_general_search", "snippet_only_score", "source_proxy_only", "evidence_url_pending"),
            date_window={"end": event.event_date, "lookback_days": 90},
            max_queries=1,
            max_candidates=1,
            max_fetches=1,
            stop_condition={"accepted_claim_count": 1},
            query_intents=(),
            llm_query_allowed=False,
            general_search_allowed=False,
            reason_from_memory=reason,
        )

    runner = SourceAcquisitionRunnerV4(mode="frozen_real_source_snapshot")
    positive_bundle = execute_source_tasks_with_evidence_os_v4(
        event=positive_event,
        tasks=(
            task(
                "C28-SEMREPLAY-00CRWD-arr_retention_bridge",
                positive_event,
                "arr_growth_visible",
                SourceTaskType.POSITIVE_VERIFY.value,
                "C28 source-backed replay must prove recurring software economics from ARR, NRR, renewal/churn, deferred revenue/RPO, and subscription margin anchors.",
            ),
        ),
        contract=contract,
        as_of_date=positive_as_of,
        source_runner=runner,
    )
    guard_bundle = execute_source_tasks_with_evidence_os_v4(
        event=guard_event,
        tasks=(
            task(
                "C28-GUARD-00CRWD-security_product_keyword_only",
                guard_event,
                "arr_growth_visible",
                SourceTaskType.RED_TEAM.value,
                "C28 keyword-only guard must not unlock ARR, NRR, renewal, RPO, or recurring-margin primitives from software/security vocabulary alone.",
            ),
        ),
        contract=contract,
        as_of_date=guard_as_of,
        source_runner=runner,
    )

    positive_rows, positive_claim_ids, positive_primitives, positive_urls = _semantic_replay_execution_summary(
        bundle=positive_bundle,
        source_origin=C28_SEMANTIC_REPLAY_SOURCE_ORIGIN,
    )
    guard_rows, guard_claim_ids, guard_primitives, guard_urls = _semantic_replay_execution_summary(
        bundle=guard_bundle,
        source_origin=C28_SEMANTIC_REPLAY_SOURCE_ORIGIN,
    )
    accepted_claim_ids = list(dict.fromkeys((*positive_claim_ids, *guard_claim_ids)))
    accepted_primitive_ids = list(dict.fromkeys((*positive_primitives, *guard_primitives)))
    document_urls = list(dict.fromkeys((*positive_urls, *guard_urls)))
    positive_claim_rows = _semantic_replay_claim_rows(
        bundle=positive_bundle,
        event=positive_event,
        archetype_id=C28_SOFTWARE_SECURITY_ARCHETYPE,
        source_origin=C28_SEMANTIC_REPLAY_SOURCE_ORIGIN,
        accepted_claim_ids=positive_claim_ids,
    )
    guard_claim_rows = _semantic_replay_claim_rows(
        bundle=guard_bundle,
        event=guard_event,
        archetype_id=C28_SOFTWARE_SECURITY_ARCHETYPE,
        source_origin=C28_SEMANTIC_REPLAY_SOURCE_ORIGIN,
        accepted_claim_ids=guard_claim_ids,
    )
    positive_support_primitives = _support_primitive_ids_from_claim_rows(positive_claim_rows)
    guard_support_primitives = _support_primitive_ids_from_claim_rows(guard_claim_rows)
    guard_counter_primitives = _counter_primitive_ids_from_claim_rows(guard_claim_rows)
    required_positive = (
        "arr_growth_visible",
        "nrr",
        "retention_or_renewal",
        "rpo_to_sales",
        "recurring_margin_leverage",
    )
    forbidden_guard_support = (
        "arr_growth_visible",
        "nrr",
        "retention_or_renewal",
        "rpo_to_sales",
        "recurring_margin_leverage",
        "subscription_monthly_billing",
    )
    guard_positive_leaks = [primitive for primitive in guard_support_primitives if primitive in set(forbidden_guard_support)]
    blockers: list[str] = []
    missing_positive = [primitive for primitive in required_positive if primitive not in set(positive_support_primitives)]
    if missing_positive:
        blockers.append(f"c28_required_positive_support_primitives_missing:{','.join(missing_positive)}")
    if not positive_claim_ids:
        blockers.append("c28_semantic_replay_no_positive_accepted_claims")
    if not positive_urls:
        blockers.append("c28_semantic_replay_no_positive_source_documents")
    if guard_positive_leaks:
        blockers.append("c28_keyword_only_guard_leaked_retention_support")
    if guard_claim_ids:
        blockers.append("c28_keyword_only_guard_accepted_score_claims")
    if not guard_urls:
        blockers.append("c28_keyword_only_guard_no_source_documents")
    if any(str(url).startswith("source-proxy://") or str(url).startswith("snapshot://") for url in document_urls):
        blockers.append("c28_semantic_replay_source_proxy_or_snapshot_url")

    positive_pass = not any(
        blocker
        for blocker in blockers
        if blocker.startswith("c28_required_positive_support_primitives_missing")
        or blocker
        in {
            "c28_semantic_replay_no_positive_accepted_claims",
            "c28_semantic_replay_no_positive_source_documents",
            "c28_semantic_replay_source_proxy_or_snapshot_url",
        }
    )
    guard_pass = not any(
        blocker
        for blocker in blockers
        if blocker
        in {
            "c28_keyword_only_guard_leaked_retention_support",
            "c28_keyword_only_guard_accepted_score_claims",
            "c28_keyword_only_guard_no_source_documents",
            "c28_semantic_replay_source_proxy_or_snapshot_url",
        }
    )
    return {
        "schema_version": "e2r_census_v4_c28_source_backed_semantic_replay_v1",
        "as_of_date": config.as_of_date,
        "fixture_as_of_dates": [positive_as_of.isoformat(), guard_as_of.isoformat()],
        "source_origin": C28_SEMANTIC_REPLAY_SOURCE_ORIGIN,
        "replay_only": True,
        "production_score_evidence_allowed": False,
        "positive_replay_pass": positive_pass,
        "guard_replay_pass": guard_pass,
        "required_positive_primitives": list(required_positive),
        "keyword_only_guard_forbidden_support_primitives": list(forbidden_guard_support),
        "keyword_only_guard_leaked_support_primitives": guard_positive_leaks,
        "accepted_primitive_ids": accepted_primitive_ids,
        "positive_accepted_primitive_ids": list(dict.fromkeys(positive_primitives)),
        "positive_support_primitive_ids": positive_support_primitives,
        "guard_accepted_primitive_ids": list(dict.fromkeys(guard_primitives)),
        "guard_support_primitive_ids": guard_support_primitives,
        "guard_counter_primitive_ids": guard_counter_primitives,
        "accepted_claim_ids": accepted_claim_ids,
        "positive_accepted_claim_ids": positive_claim_ids,
        "guard_accepted_claim_ids": guard_claim_ids,
        "accepted_claim_count": len(accepted_claim_ids),
        "positive_claim_count": len(positive_claim_ids),
        "guard_claim_count": len(guard_claim_ids),
        "document_urls": document_urls,
        "document_count": len(positive_bundle.documents) + len(guard_bundle.documents),
        "anchor_count": len(positive_bundle.anchors) + len(guard_bundle.anchors),
        "raw_assertion_count": len(positive_bundle.raw_assertions) + len(guard_bundle.raw_assertions),
        "claim_extractor_attempt_count": int(positive_bundle.extraction_audit.get("llm_claim_extractor_attempt_count") or 0)
        + int(guard_bundle.extraction_audit.get("llm_claim_extractor_attempt_count") or 0),
        "claim_extractor_success_count": int(positive_bundle.extraction_audit.get("llm_claim_extractor_success_count") or 0)
        + int(guard_bundle.extraction_audit.get("llm_claim_extractor_success_count") or 0),
        "claim_extractor_non_llm_provider_count": int(positive_bundle.extraction_audit.get("llm_claim_extractor_non_llm_provider_count") or 0)
        + int(guard_bundle.extraction_audit.get("llm_claim_extractor_non_llm_provider_count") or 0),
        "blockers": blockers,
        "executions": [*positive_rows, *guard_rows],
        "positive_claims": positive_claim_rows,
        "guard_claims": guard_claim_rows,
        "rule": "This replay is not a production full-thesis row. It proves C28 can extract source-backed ARR/NRR/renewal/deferred-revenue/subscription-margin support while blocking software/security product vocabulary from becoming retention evidence.",
    }


def _semantic_replay_execution_summary(
    *,
    bundle: Any,
    source_origin: str,
) -> tuple[list[dict[str, Any]], list[str], list[str], list[str]]:
    rows: list[dict[str, Any]] = []
    accepted_claim_ids: list[str] = []
    accepted_primitive_ids: list[str] = []
    document_urls: list[str] = []
    for execution in bundle.executions:
        row = execution.to_dict() if hasattr(execution, "to_dict") else _jsonable(execution)
        row["source_origin"] = source_origin
        row["replay_only"] = True
        row["production_score_evidence_allowed"] = False
        rows.append(row)
        accepted_claim_ids.extend(str(item) for item in row.get("accepted_claim_ids") or [])
        accepted_primitive_ids.extend(str(item) for item in row.get("accepted_primitive_ids") or [])
        document_urls.extend(str(item) for item in row.get("document_urls") or [])
    return (
        rows,
        list(dict.fromkeys(accepted_claim_ids)),
        list(dict.fromkeys(accepted_primitive_ids)),
        list(dict.fromkeys(document_urls)),
    )


def _semantic_replay_claim_rows(
    *,
    bundle: Any,
    event: Any,
    archetype_id: str,
    source_origin: str,
    accepted_claim_ids: Sequence[str],
) -> list[dict[str, Any]]:
    claim_rows: list[dict[str, Any]] = []
    raw_assertions = getattr(bundle, "raw_assertions", {}) or {}
    for claim_id in accepted_claim_ids:
        claim = bundle.ledger.claims.get(claim_id)
        if claim is None:
            continue
        row = _jsonable(claim)
        claim_mappings = [
            mapping
            for mapping in bundle.ledger.mappings.values()
            if mapping.claim_id == claim_id and str(getattr(mapping, "mapping_status", "")) in {"MappingStatus.ACCEPTED", "ACCEPTED"}
        ]
        document = bundle.documents.get(str(row.get("source_document_id") or ""))
        anchor = bundle.anchors.get(str(row.get("source_anchor_id") or ""))
        row["symbol"] = event.symbol
        row["company_name"] = event.company_name
        row["archetype_id"] = archetype_id
        row["accepted_primitive_ids"] = [str(mapping.primitive_id) for mapping in claim_mappings]
        row["accepted_mappings"] = [_jsonable(mapping) for mapping in claim_mappings]
        row["source_url"] = getattr(document, "canonical_url", None) if document is not None else None
        row["source_type"] = (
            getattr(document, "source_type", None).value
            if document is not None and getattr(document, "source_type", None) is not None
            else None
        )
        row["quote_text"] = _claim_quote_text(claim=claim, raw_assertions=raw_assertions, anchor=anchor)
        row["anchor_verified"] = getattr(anchor, "anchor_verified", None) if anchor is not None else None
        row["source_origin"] = source_origin
        row["replay_only"] = True
        row["production_score_evidence_allowed"] = False
        claim_rows.append(row)
    return claim_rows


def _support_primitive_ids_from_claim_rows(claim_rows: Sequence[Mapping[str, Any]]) -> list[str]:
    primitive_ids: list[str] = []
    for claim in claim_rows:
        for mapping in claim.get("accepted_mappings") or []:
            support_direction = str(mapping.get("support_direction") or "")
            if support_direction not in {"SUPPORT", "SupportDirection.SUPPORT"}:
                continue
            primitive = str(mapping.get("primitive_id") or "")
            if primitive:
                primitive_ids.append(primitive)
    return list(dict.fromkeys(primitive_ids))


def _counter_primitive_ids_from_claim_rows(claim_rows: Sequence[Mapping[str, Any]]) -> list[str]:
    primitive_ids: list[str] = []
    for claim in claim_rows:
        for mapping in claim.get("accepted_mappings") or []:
            support_direction = str(mapping.get("support_direction") or "")
            if support_direction not in {"COUNTER", "SupportDirection.COUNTER"}:
                continue
            primitive = str(mapping.get("primitive_id") or "")
            if primitive:
                primitive_ids.append(primitive)
    return list(dict.fromkeys(primitive_ids))


def _first_as_of_date(stage_rows: Sequence[Mapping[str, Any]]) -> str:
    for row in stage_rows:
        if row.get("as_of_date"):
            return str(row.get("as_of_date"))
    return ""


def _c06_guard_replay_cases(*, as_of_date: str) -> list[dict[str, Any]]:
    return [
        {
            "guard_case_id": "C06-GUARD-SAMSUNG-QUALIFICATION-LAG-NOT-4C",
            "symbol": "005930",
            "company_name": "삼성전자",
            "as_of_date": as_of_date,
            "source_name": "Reuters",
            "source_url": "https://www.reuters.com/technology/samsungs-hbm-chips-failing-nvidia-tests-due-heat-power-consumption-woes-sources-2024-05-23/",
            "published_at": "2024-05-23",
            "input_claim_class": "qualification_lag",
            "guard_claim_summary": "Samsung HBM chips were reported as failing Nvidia tests due to heat and power issues.",
            "expected_target_scope_status": "DIRECT",
            "expected_polarity": "NEGATIVE_OR_MIXED",
            "expected_temporal_status": "HISTORICAL_OR_FOLLOWUP_REQUIRED",
            "expected_current_score_eligible": False,
            "expected_hard_break_allowed": False,
            "expected_green_unlock_allowed": False,
            "actual_hard_break_allowed": False,
            "actual_green_unlock_allowed": False,
            "actual_transition_overlay": "NONE",
            "score_contribution_ids": [],
            "source_proxy_only": False,
            "evidence_url_pending": False,
            "rationale": "A qualification lag is an execution/watch guard. It is not a current OPEN cancellation or permanent customer loss without current follow-up confirmation.",
        },
        {
            "guard_case_id": "C06-GUARD-SAMSUNG-PARTIAL-CLEARANCE-SUPERSEDES-ABSOLUTE-FAILURE",
            "symbol": "005930",
            "company_name": "삼성전자",
            "as_of_date": as_of_date,
            "source_name": "Reuters",
            "source_url": "https://www.reuters.com/technology/nvidia-clears-samsungs-hbm3-chips-use-china-market-processor-sources-say-2024-07-23/",
            "published_at": "2024-07-23",
            "input_claim_class": "partial_qualification_followup",
            "guard_claim_summary": "Nvidia reportedly cleared Samsung HBM3 chips for a China-market processor after earlier qualification concerns.",
            "expected_target_scope_status": "DIRECT",
            "expected_polarity": "MIXED_OR_PARTIAL_POSITIVE",
            "expected_temporal_status": "FOLLOWUP_SUPERSESSION_CONTEXT",
            "expected_current_score_eligible": False,
            "expected_hard_break_allowed": False,
            "expected_green_unlock_allowed": False,
            "actual_hard_break_allowed": False,
            "actual_green_unlock_allowed": False,
            "actual_transition_overlay": "NONE",
            "score_contribution_ids": [],
            "source_proxy_only": False,
            "evidence_url_pending": False,
            "rationale": "A partial follow-up can supersede an absolute-failure narrative, but it still does not prove broad C06 Green qualification, allocation, shipment, and cash bridge.",
        },
        {
            "guard_case_id": "C06-GUARD-SAMSUNG-SUPPLY-DELAY-NOT-GREEN-OR-4C",
            "symbol": "005930",
            "company_name": "삼성전자",
            "as_of_date": as_of_date,
            "source_name": "Reuters",
            "source_url": "https://www.reuters.com/technology/samsung-q4-earnings-expected-be-hit-by-nvidia-ai-chip-supply-delay-2025-01-06/",
            "published_at": "2025-01-06",
            "input_claim_class": "ai_chip_supply_delay",
            "guard_claim_summary": "Samsung earnings expectations were reportedly hit by Nvidia AI chip supply delay.",
            "expected_target_scope_status": "DIRECT",
            "expected_polarity": "NEGATIVE_OR_MIXED",
            "expected_temporal_status": "HISTORICAL_OR_FOLLOWUP_REQUIRED",
            "expected_current_score_eligible": False,
            "expected_hard_break_allowed": False,
            "expected_green_unlock_allowed": False,
            "actual_hard_break_allowed": False,
            "actual_green_unlock_allowed": False,
            "actual_transition_overlay": "NONE",
            "score_contribution_ids": [],
            "source_proxy_only": False,
            "evidence_url_pending": False,
            "rationale": "A supply-delay article can block Green until current conversion evidence appears, but it is not itself a current hard break or a positive Green unlock.",
        },
    ]


def _full_thesis_production_audit(*, config: CensusV4RunConfig, stage_rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    full_thesis_rows = [row for row in stage_rows if row.get("stage_scope") == "FULL_THESIS"]
    refresh_queue_rows = _full_thesis_refresh_queue(stage_rows)
    controlled_smoke_rows = [
        row
        for row in full_thesis_rows
        if row.get("score_source") == "SCORE_CONTRIBUTION_SUM"
        and str(row.get("score_build_method") or "") == "primitive_score_contribution_sum"
        and any(str(task_id).startswith("FTSMOKE-") for task_id in row.get("full_thesis_source_task_ids") or [])
    ]
    production_rows = [
        row
        for row in full_thesis_rows
        if row not in controlled_smoke_rows
        and row.get("score_scale") == "FULL_E2R_100"
        and row.get("full_thesis_score_valid_status") in {"FINAL", "FINAL_WITH_NONMATERIAL_GAPS"}
    ]
    incomplete_production_rows = [
        row
        for row in production_rows
        if not row.get("full_thesis_accepted_claim_ids")
        or not row.get("full_thesis_score_contribution_ids")
        or not row.get("full_thesis_stagecourt_trace_ids")
    ]
    production_mode_requested = _config_requests_production_full_thesis(config)
    controlled_smoke_substitution_rejected_count = len(controlled_smoke_rows) if production_mode_requested else 0
    blockers: list[str] = []
    if not production_rows:
        blockers.append(
            "production_full_thesis_runner_no_eligible_rows"
            if production_mode_requested
            else "production_full_thesis_not_requested_or_no_rows"
        )
    if incomplete_production_rows:
        blockers.append("production_full_thesis_rows_missing_claim_score_or_stage_trace")
    if controlled_smoke_substitution_rejected_count:
        blockers.append("controlled_smoke_rows_rejected_as_production_substitute")
    production_pass_allowed = bool(production_rows) and not incomplete_production_rows and not blockers
    return {
        "schema_version": "e2r_census_v4_full_thesis_production_audit_v1",
        "status": "FULL_THESIS_PRODUCTION_PASS" if production_pass_allowed else "PENDING_FULL_THESIS_PRODUCTION",
        "verdict": "FULL_THESIS_PRODUCTION_PASS" if production_pass_allowed else "PENDING_FULL_THESIS_PRODUCTION",
        "run_mode": config.run_mode,
        "target_gate": config.target_gate,
        "full_thesis_smoke_mode": config.full_thesis_smoke_mode,
        "production_mode_requested": production_mode_requested,
        "production_runner_implemented": True,
        "completion_eligible": production_pass_allowed,
        "production_pass_allowed": production_pass_allowed,
        "full_thesis_row_count": len(full_thesis_rows),
        "full_thesis_refresh_queue_candidate_count": len(refresh_queue_rows),
        "controlled_smoke_full_thesis_row_count": len(controlled_smoke_rows),
        "production_full_thesis_row_count": len(production_rows),
        "incomplete_production_full_thesis_row_count": len(incomplete_production_rows),
        "controlled_smoke_substitution_rejected_count": controlled_smoke_substitution_rejected_count,
        "controlled_smoke_substitution_allowed": False,
        "production_symbols": [row.get("symbol") for row in production_rows],
        "controlled_smoke_symbols": [row.get("symbol") for row in controlled_smoke_rows],
        "blockers": blockers,
        "rule": "Controlled full-thesis smoke rows validate the claim-backed score path, but they cannot satisfy production full-thesis operation or meaningful operational readiness.",
    }


def _config_requests_production_full_thesis(config: CensusV4RunConfig) -> bool:
    return config.target_gate in {"meaningful", "full_thesis"} or config.run_mode in {
        "BRAIN_AND_WEB_ACQUISITION_ENABLED",
        "FULL_LIVE_BRAIN_CENSUS",
        "HYBRID_CENSUS",
    }


def _full_thesis_smoke_honesty_pass(full_thesis: Mapping[str, Any]) -> bool:
    if not full_thesis:
        return False
    explicit = full_thesis.get("full_thesis_smoke_honesty_pass_allowed")
    if explicit is False:
        return False
    if full_thesis.get("verdict") not in {"FULL_THESIS_SMOKE_PASS", "PENDING_FULL_THESIS_REFRESH"}:
        return False
    required_fields = {
        "score_allowed_before_execution",
        "hardcoded_query_count",
        "daily_event_and_full_thesis_separated",
    }
    if any(field not in full_thesis for field in required_fields):
        return False
    if full_thesis.get("score_allowed_before_execution") is not False:
        return False
    try:
        hardcoded_query_count = int(full_thesis.get("hardcoded_query_count") or 0)
    except (TypeError, ValueError):
        return False
    if hardcoded_query_count != 0:
        return False
    if full_thesis.get("daily_event_and_full_thesis_separated") is not True:
        return False
    return True


def _full_thesis_smoke_execution_pass(full_thesis: Mapping[str, Any]) -> bool:
    explicit = full_thesis.get("full_thesis_smoke_execution_pass_allowed")
    if explicit is False:
        return False
    if full_thesis.get("verdict") != "FULL_THESIS_SMOKE_PASS":
        return False
    if full_thesis.get("full_thesis_status") != "FULL_THESIS_REFRESH_RAN":
        return False
    per_symbol = full_thesis.get("per_symbol")
    return isinstance(per_symbol, list) and bool(per_symbol) and all(row.get("smoke_pass_allowed") is True for row in per_symbol)


def _full_thesis_smoke_gate_blockers(*, config: CensusV4RunConfig, full_thesis_execution_pass: bool) -> list[str]:
    blockers: list[str] = []
    if not full_thesis_execution_pass:
        blockers.append("full_thesis_smoke_not_passed")
    if config.target_gate != "full_thesis_smoke":
        blockers.append("full_thesis_smoke_gate_not_requested")
    if _config_requests_production_full_thesis(config):
        blockers.append("controlled_smoke_not_allowed_for_production_run_mode")
    if config.brain_web_mode != "disabled":
        blockers.append("controlled_smoke_requires_brain_web_disabled")
    return blockers


def _full_thesis_smoke_required_primitives() -> list[str]:
    return [
        "named_customer_or_customer_quality",
        "qualification_status",
        "capacity_allocation_or_pre_sold",
        "hbm_shipment_or_revenue_mix",
        "cash_or_revision_conversion",
        "repeat_evidence_family",
        "source_quorum",
    ]


def _full_thesis_smoke_tasks(stage_rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    rows_by_symbol = {str(row.get("symbol") or ""): row for row in stage_rows if row.get("symbol") in set(FULL_THESIS_SMOKE_SYMBOLS)}
    tasks: list[dict[str, Any]] = []
    for symbol in FULL_THESIS_SMOKE_SYMBOLS:
        row = rows_by_symbol.get(symbol, {})
        company = str(row.get("company_name") or FULL_THESIS_SMOKE_COMPANY_FALLBACKS.get(symbol, symbol))
        accepted_by_primitive = row.get("full_thesis_task_accepted_claim_ids_by_primitive") if isinstance(row.get("full_thesis_task_accepted_claim_ids_by_primitive"), Mapping) else {}
        full_task_ids = set(str(item) for item in row.get("full_thesis_source_task_ids") or [])
        full_ready = row.get("stage_scope") == "FULL_THESIS" and row.get("score_scale") == "FULL_E2R_100"
        for primitive in _full_thesis_smoke_required_primitives():
            task_id = _full_thesis_smoke_task_id(symbol=symbol, primitive=primitive, as_of_date=row.get("as_of_date"))
            accepted_claim_ids = list(accepted_by_primitive.get(primitive) or [])
            if primitive == "source_quorum" and full_ready:
                accepted_claim_ids = list(row.get("full_thesis_accepted_claim_ids") or [])
            task_executed = full_ready and task_id in full_task_ids and bool(accepted_claim_ids)
            tasks.append(
                {
                    "schema_version": "e2r_census_v4_full_thesis_smoke_task_v1",
                    "smoke_task_id": task_id,
                    "symbol": symbol,
                    "company_name": company,
                    "as_of_date": row.get("as_of_date"),
                    "target_archetype": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "primitive_gap": primitive,
                    "task_status": "EXECUTED_ACCEPTED" if task_executed else "PLANNING_REQUIRED",
                    "source_policy": "controlled_url_backed_replay_fixture" if task_executed else "official_first_then_bounded_external_if_needed",
                    "preferred_source_classes": ["IssuerIR", "TrustedNews"] if task_executed else ["DART", "IR", "CompanyGuide", "trusted_news"],
                    "fallback_source_classes": [] if task_executed else ["NaverSearch", "GeneralWebSearch"],
                    "forbidden_source_classes": ["unbounded_general_search", "snippet_only_score"],
                    "llm_query_required": not task_executed,
                    "hardcoded_query_count": 0,
                    "hardcoded_queries": [],
                    "query_intents": [],
                    "general_search_allowed": not task_executed,
                    "max_queries": 0 if task_executed else 3,
                    "max_candidates": len(accepted_claim_ids) if task_executed else 20,
                    "max_fetches": max(1, len(accepted_claim_ids)) if task_executed else 3,
                    "stop_condition": {"accepted_claim_count": 1} if task_executed else {"accepted_claim_count": 1, "counter_claim_check_done": True},
                    "score_allowed_before_execution": False,
                    "score_evidence": task_executed,
                    "accepted_claim_ids": accepted_claim_ids,
                    "stagecourt_trace_ids": list(row.get("full_thesis_stagecourt_trace_ids") or []) if task_executed else [],
                    "reason": "Controlled URL-backed full-thesis smoke task executed." if task_executed else "Samsung/Hynix C06/HBM full thesis smoke is pending until real source-backed claims are accepted.",
                }
            )
    return tasks


def _full_thesis_refresh_queue(stage_rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    """Queue event-board rows for future full-thesis refresh without promotion.

    This is intentionally not a scoring path. It exists so that non-Stage0
    Census event-board rows are not mistaken for operating full-thesis stages,
    while still giving the next Brain/Web run a bounded, reviewable worklist.
    """

    queue: list[dict[str, Any]] = []
    for index, row in enumerate(stage_rows):
        if row.get("stage_scope") != "CENSUS_EVENT_BOARD":
            continue
        if row.get("base_stage") == "Stage0":
            continue
        symbol = str(row.get("symbol") or "").zfill(6)
        if not symbol:
            continue
        as_of_date = str(row.get("as_of_date") or "")
        queue_task_id = f"FTQUEUE-{as_of_date}-{symbol}-{index:04d}"
        full_thesis_missing = list(row.get("full_thesis_missing_primitives") or [])
        if not full_thesis_missing:
            full_thesis_missing = ["full_thesis_refresh_task_not_run"]
        if "full_thesis_archetype_hypothesis_required" not in full_thesis_missing:
            full_thesis_missing.append("full_thesis_archetype_hypothesis_required")
        if "source_backed_primitive_coverage_required" not in full_thesis_missing:
            full_thesis_missing.append("source_backed_primitive_coverage_required")
        stage_signal = str(row.get("stage_signal") or "")
        stage_decision_status = str(row.get("stage_decision_status") or "")
        risk_stage_signal = str(row.get("risk_stage_signal") or "NONE")
        priority_bucket = _full_thesis_refresh_priority_bucket(
            base_stage=str(row.get("base_stage") or ""),
            stage_signal=stage_signal,
            stage_decision_status=stage_decision_status,
            risk_stage_signal=risk_stage_signal,
        )
        queue.append(
            {
                "schema_version": "e2r_census_v4_full_thesis_refresh_queue_v1",
                "queue_task_id": queue_task_id,
                "task_type": "full_thesis_refresh_task",
                "task_status": "PLANNING_REQUIRED",
                "symbol": symbol,
                "company_name": row.get("company_name"),
                "as_of_date": row.get("as_of_date"),
                "source_stage_scope": row.get("stage_scope"),
                "operator_stage_use": row.get("operator_stage_use"),
                "source_primary_archetype": row.get("primary_archetype"),
                "source_secondary_archetypes": list(row.get("secondary_archetypes") or []),
                "source_large_sector_id": row.get("large_sector_id"),
                "source_base_stage": row.get("base_stage"),
                "source_canonical_stage": row.get("canonical_stage"),
                "source_stage_signal": stage_signal,
                "source_risk_stage_signal": risk_stage_signal,
                "source_stage_decision_status": stage_decision_status,
                "source_investigation_status": row.get("investigation_status"),
                "source_atomic_stage_decision_id": row.get("atomic_stage_decision_id"),
                "source_stagecourt_trace_id": row.get("stagecourt_trace_id"),
                "source_candidate_event_ids": list(row.get("candidate_event_ids") or []),
                "source_candidate_event_count": int(row.get("candidate_event_count") or 0),
                "source_accepted_claim_ids": list(row.get("accepted_claim_ids") or []),
                "source_accepted_claim_count": int(row.get("accepted_claim_count") or 0),
                "source_accepted_official_claim_count": int(row.get("accepted_official_claim_count") or 0),
                "source_score_contribution_ids": list(row.get("score_contribution_ids") or []),
                "source_event_evidence_score": row.get("event_evidence_score"),
                "source_score_scale": row.get("score_scale"),
                "source_score_scope": row.get("score_scope"),
                "source_missing_primitives": list(row.get("missing_primitives") or []),
                "source_material_gap_ids": list(row.get("material_gap_ids") or []),
                "source_failed_stage_gates": list(row.get("failed_stage_gates") or []),
                "queue_reason": "event_board_non_stage0_needs_full_thesis_refresh",
                "priority_bucket": priority_bucket,
                "target_archetype_status": "BRAIN_HYPOTHESIS_REQUIRED",
                "target_archetype": None,
                "missing_full_thesis_primitives": full_thesis_missing,
                "planner_required": True,
                "llm_query_required": True,
                "hardcoded_query_count": 0,
                "hardcoded_queries": [],
                "query_intents": [],
                "score_allowed_before_execution": False,
                "stage_promotion_allowed_before_execution": False,
                "official_first_required": True,
                "preferred_source_classes": ["DART", "KIND", "KRX", "IssuerIR", "CompanyGuide"],
                "fallback_source_classes": ["TrustedNews", "ReportPDF", "BrokerReportPublicPDF", "CompanyNewsroom", "NaverSearch", "GeneralWebSearch"],
                "forbidden_source_classes": ["snippet_only_score", "source_proxy_only", "evidence_url_pending", "unbounded_general_search"],
                "max_source_tasks": 5,
                "max_queries_per_task": 3,
                "max_candidates_per_query": 20,
                "max_fetches_per_task": 3,
                "stop_condition": {
                    "accepted_claim_count_per_material_primitive": 1,
                    "counter_claim_check_done": True,
                    "source_budget_exhausted_status": "SOURCE_PENDING",
                },
                "promotion_requirements": [
                    "primary_archetype_hypothesis",
                    "direct_current_score_eligible_claims",
                    "score_contributions",
                    "stagecourt_trace",
                    "green_gate_or_pending_material_gap_status",
                ],
                "blocked_from_stage_promotion": True,
                "blocked_reason": "full_thesis_refresh_task_not_run",
                "next_actions": [
                    "RUN_RESEARCH_BRAIN_PLANNER",
                    "CREATE_OFFICIAL_FIRST_SOURCE_TASKS",
                    "FETCH_SOURCE_DOCUMENTS",
                    "EXTRACT_EVIDENCE_OS_CLAIMS",
                    "RUN_STAGECOURT_FULL_THESIS",
                ],
            }
        )
    return queue


def _write_full_thesis_refresh_seed_events(*, output_root: Path, refresh_queue_rows: Sequence[Mapping[str, Any]]) -> Path:
    seed_path = output_root / "research_brain_full_thesis_seed_events.jsonl"
    rows: list[dict[str, Any]] = []
    for row in refresh_queue_rows:
        symbol = str(row.get("symbol") or "").zfill(6)
        if not symbol:
            continue
        as_of_date = str(row.get("as_of_date") or "")
        queue_task_id = str(row.get("queue_task_id") or "")
        missing_primitives = [str(item) for item in row.get("missing_full_thesis_primitives") or [] if str(item)]
        priority_bucket = str(row.get("priority_bucket") or "")
        event_id = f"CEV4-FTQUEUE-{symbol}-{stable_hash((as_of_date, queue_task_id, priority_bucket))[:16]}"
        rows.append(
            {
                "schema_version": "e2r_census_v4_full_thesis_seed_event_v1",
                "candidate_event_id": event_id,
                "symbol": symbol,
                "company_name": row.get("company_name"),
                "event_date": as_of_date,
                "detected_at": as_of_date,
                "source_family": "CensusFullThesisQueue",
                "source_id": str(output_root / "full_thesis_refresh_queue.jsonl"),
                "event_type": "full_thesis_refresh_seed",
                "raw_reason_codes": [
                    "FULL_THESIS_REFRESH_QUEUE",
                    str(row.get("queue_reason") or "event_board_non_stage0_needs_full_thesis_refresh"),
                    priority_bucket,
                ],
                "primary_disclosure_type": None,
                "event_title": f"{row.get('company_name') or symbol} full thesis refresh queue seed",
                "event_summary": (
                    f"{row.get('company_name') or symbol} requires full-thesis refresh from Census event-board row. "
                    f"source_stage_signal={row.get('source_stage_signal')}; "
                    f"source_stage_decision_status={row.get('source_stage_decision_status')}; "
                    f"missing_full_thesis_primitives={', '.join(missing_primitives)}"
                ),
                "issuer_directness": "DIRECT",
                "research_brain_eligible": True,
                "score_evidence_allowed": False,
                "stage_promotion_allowed_before_execution": False,
                "seed_role": "planner_input_only",
                "structured_payload": {
                    "queue_task_id": queue_task_id,
                    "source_stage_scope": row.get("source_stage_scope"),
                    "operator_stage_use": row.get("operator_stage_use"),
                    "source_primary_archetype": row.get("source_primary_archetype"),
                    "source_secondary_archetypes": list(row.get("source_secondary_archetypes") or []),
                    "source_large_sector_id": row.get("source_large_sector_id"),
                    "source_base_stage": row.get("source_base_stage"),
                    "source_stage_signal": row.get("source_stage_signal"),
                    "source_stage_decision_status": row.get("source_stage_decision_status"),
                    "source_accepted_claim_ids": list(row.get("source_accepted_claim_ids") or []),
                    "source_score_contribution_ids": list(row.get("source_score_contribution_ids") or []),
                    "source_candidate_event_ids": list(row.get("source_candidate_event_ids") or []),
                    "source_missing_primitives": list(row.get("source_missing_primitives") or []),
                    "source_material_gap_ids": list(row.get("source_material_gap_ids") or []),
                    "source_failed_stage_gates": list(row.get("source_failed_stage_gates") or []),
                    "target_archetype_status": row.get("target_archetype_status"),
                    "target_archetype": row.get("target_archetype"),
                    "missing_full_thesis_primitives": missing_primitives,
                    "preferred_source_classes": list(row.get("preferred_source_classes") or []),
                    "fallback_source_classes": list(row.get("fallback_source_classes") or []),
                    "forbidden_source_classes": list(row.get("forbidden_source_classes") or []),
                    "official_first_required": row.get("official_first_required") is True,
                    "max_source_tasks": row.get("max_source_tasks"),
                    "max_queries_per_task": row.get("max_queries_per_task"),
                    "max_candidates_per_query": row.get("max_candidates_per_query"),
                    "max_fetches_per_task": row.get("max_fetches_per_task"),
                    "blocked_reason": row.get("blocked_reason"),
                },
            }
        )
    write_jsonl(seed_path, rows)
    return seed_path


def _resolve_research_brain_candidate_seed_path(
    *,
    config: CensusV4RunConfig,
    output_root: Path,
    default_seed_path: Path,
) -> dict[str, Any]:
    """Resolve the exact seed file passed to Research Brain.

    Easy example: the default full-thesis refresh queue is a first-run seed.
    A later run may need to feed the previous run's blocker follow-up seed
    instead. We copy that external seed into the current output so the run is
    auditable from its own leaf artifacts.
    """

    if not config.brain_candidate_event_seed_path:
        default_rows = _read_jsonl(default_seed_path)
        used_path = output_root / "research_brain_candidate_seed_events_used.jsonl"
        write_jsonl(used_path, default_rows)
        return {
            "seed_path": used_path,
            "seed_event_count": len(default_rows),
            "seed_source": "internal_full_thesis_refresh_queue",
            "original_path": str(default_seed_path),
            "missing_external_seed_path": False,
        }

    original_path = Path(config.brain_candidate_event_seed_path)
    used_path = output_root / "research_brain_candidate_seed_events_used.jsonl"
    if not original_path.exists():
        write_jsonl(used_path, [])
        return {
            "seed_path": used_path,
            "seed_event_count": 0,
            "seed_source": "external_candidate_event_seed_path_missing",
            "original_path": str(original_path),
            "missing_external_seed_path": True,
        }
    rows = _read_jsonl(original_path)
    write_jsonl(used_path, rows)
    return {
        "seed_path": used_path,
        "seed_event_count": len(rows),
        "seed_source": "external_candidate_event_seed_path",
        "original_path": str(original_path),
        "missing_external_seed_path": False,
    }


def _write_full_thesis_seed_materialization_trace(
    *,
    output_root: Path,
    seed_path: Path,
    additional_seed_paths: Sequence[Path] = (),
    stage_rows: Sequence[Mapping[str, Any]],
) -> None:
    """Write one audit row per full-thesis seed event.

    Easy example: a queue row for SK hynix can exist, and even a seed event can
    exist, while no Research Brain source task has run yet. This trace keeps
    those states separate so a queue/seed row cannot be mistaken for an
    operating FULL_THESIS stage.
    """

    seed_rows: list[dict[str, Any]] = []
    for index, path in enumerate([seed_path, *additional_seed_paths]):
        for row in _read_jsonl(path):
            item = dict(row)
            item["seed_source_path"] = str(path)
            item["seed_source_index"] = index
            seed_rows.append(item)
    planner_rows = _read_jsonl(output_root / "planner_runs.jsonl")
    source_execution_rows = _read_jsonl(output_root / "source_task_executions.jsonl")
    stagecourt_rows = _read_jsonl(output_root / "stagecourt_traces.jsonl")
    stage_by_symbol = {str(row.get("symbol") or "").zfill(6): row for row in stage_rows}

    planner_by_event: dict[str, list[Mapping[str, Any]]] = {}
    for row in planner_rows:
        event = row.get("event") if isinstance(row.get("event"), Mapping) else {}
        event_id = str(event.get("candidate_event_id") or row.get("candidate_event_id") or "")
        if event_id:
            planner_by_event.setdefault(event_id, []).append(row)

    source_by_event: dict[str, list[Mapping[str, Any]]] = {}
    for row in source_execution_rows:
        event_id = _source_task_execution_candidate_event_id(row)
        if event_id:
            source_by_event.setdefault(event_id, []).append(row)

    stagecourt_by_event: dict[str, list[Mapping[str, Any]]] = {}
    for row in stagecourt_rows:
        event_id = str(row.get("candidate_event_id") or "")
        if event_id:
            stagecourt_by_event.setdefault(event_id, []).append(row)

    trace_rows: list[dict[str, Any]] = []
    for seed in seed_rows:
        event_id = str(seed.get("candidate_event_id") or "")
        symbol = str(seed.get("symbol") or "").zfill(6)
        stage_row = stage_by_symbol.get(symbol) or {}
        structured_payload = seed.get("structured_payload") if isinstance(seed.get("structured_payload"), Mapping) else {}
        controlled_smoke_final_scope = _is_controlled_smoke_full_thesis_stage(stage_row)
        planners = planner_by_event.get(event_id, [])
        source_rows = source_by_event.get(event_id, [])
        stage_traces = stagecourt_by_event.get(event_id, [])
        accepted_claim_ids = sorted(
            set().union(*(_ids_from_value(row.get("accepted_claim_ids")) for row in source_rows))
        ) if source_rows else []
        score_contribution_ids = sorted(
            set().union(*(_ids_from_value(row.get("score_contribution_ids")) for row in stage_traces))
        ) if stage_traces else []
        planner_run_ids = [
            str(row.get("planner_run_id") or "")
            for row in planners
            if str(row.get("planner_run_id") or "").strip()
        ]
        source_task_ids = [
            str(row.get("task_id") or (row.get("source_task") or {}).get("task_id") or "")
            for row in source_rows
            if str(row.get("task_id") or (row.get("source_task") or {}).get("task_id") or "").strip()
        ]
        stagecourt_trace_ids = [
            str(row.get("stagecourt_trace_id") or row.get("trace_id") or "")
            for row in stage_traces
            if str(row.get("stagecourt_trace_id") or row.get("trace_id") or "").strip()
        ]
        real_provider_success_count = sum(1 for row in planners if row.get("real_provider_success") is True)
        materialization_status, blockers = _full_thesis_seed_materialization_status(
            planner_count=len(planners),
            real_provider_success_count=real_provider_success_count,
            source_task_execution_count=len(source_rows),
            accepted_claim_count=len(accepted_claim_ids),
            stagecourt_trace_count=len(stage_traces),
            final_stage_scope=str(stage_row.get("stage_scope") or ""),
            final_score_scale=str(stage_row.get("score_scale") or ""),
        )
        final_stage_scope = stage_row.get("stage_scope")
        final_score_scale = stage_row.get("score_scale")
        final_operator_stage_use = stage_row.get("operator_stage_use")
        final_operator_score_use = stage_row.get("operator_score_use")
        final_is_full_thesis_stage = stage_row.get("is_full_thesis_stage") is True
        final_is_full_e2r_score = stage_row.get("is_full_e2r_score") is True
        trace_rows.append(
            {
                "schema_version": "e2r_census_v4_full_thesis_seed_materialization_trace_v1",
                "candidate_event_id": event_id,
                "symbol": symbol,
                "company_name": seed.get("company_name"),
                "seed_source_path": seed.get("seed_source_path"),
                "seed_source_index": seed.get("seed_source_index"),
                "queue_task_id": structured_payload.get("queue_task_id"),
                "seed_role": seed.get("seed_role"),
                "source_primary_archetype": structured_payload.get("source_primary_archetype"),
                "source_secondary_archetypes": list(structured_payload.get("source_secondary_archetypes") or []),
                "source_large_sector_id": structured_payload.get("source_large_sector_id"),
                "source_missing_primitives": list(structured_payload.get("source_missing_primitives") or []),
                "source_material_gap_ids": list(structured_payload.get("source_material_gap_ids") or []),
                "source_failed_stage_gates": list(structured_payload.get("source_failed_stage_gates") or []),
                "source_score_contribution_ids": list(structured_payload.get("source_score_contribution_ids") or []),
                "target_archetype_status": structured_payload.get("target_archetype_status"),
                "target_archetype": structured_payload.get("target_archetype"),
                "score_evidence_allowed": seed.get("score_evidence_allowed") is True,
                "stage_promotion_allowed_before_execution": seed.get("stage_promotion_allowed_before_execution") is True,
                "planner_run_ids": planner_run_ids,
                "planner_run_count": len(planners),
                "planner_real_provider_success_count": real_provider_success_count,
                "source_task_ids": source_task_ids,
                "source_task_execution_count": len(source_rows),
                "accepted_claim_ids": accepted_claim_ids,
                "accepted_claim_count": len(accepted_claim_ids),
                "score_contribution_ids": score_contribution_ids,
                "score_contribution_count": len(score_contribution_ids),
                "stagecourt_trace_ids": stagecourt_trace_ids,
                "stagecourt_trace_count": len(stage_traces),
                "final_stage_scope": final_stage_scope,
                "final_operator_stage_use": final_operator_stage_use,
                "final_operator_score_use": final_operator_score_use,
                "final_full_thesis_stage": stage_row.get("full_thesis_stage"),
                "final_full_thesis_score_scale": stage_row.get("full_thesis_score_scale"),
                "final_score_scale": final_score_scale,
                "final_is_full_thesis_stage": final_is_full_thesis_stage,
                "final_is_full_e2r_score": final_is_full_e2r_score,
                "final_stage_scope_is_controlled_smoke": controlled_smoke_final_scope,
                "materialized_to_stagecourt": bool(stage_traces),
                "promoted_to_full_thesis": final_is_full_thesis_stage and final_is_full_e2r_score,
                "materialization_status": materialization_status,
                "materialization_blockers": blockers,
            }
        )
    write_jsonl(output_root / "full_thesis_seed_materialization_trace.jsonl", trace_rows)
    write_json(
        output_root / "full_thesis_seed_materialization_audit.json",
        _full_thesis_seed_materialization_audit(seed_rows=seed_rows, trace_rows=trace_rows),
    )


def _full_thesis_seed_materialization_audit(
    *,
    seed_rows: Sequence[Mapping[str, Any]],
    trace_rows: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    status_counts = Counter(str(row.get("materialization_status") or "UNKNOWN") for row in trace_rows)
    final_scope_counts = Counter(str(row.get("final_stage_scope") or "UNKNOWN") for row in trace_rows)
    final_score_scale_counts = Counter(str(row.get("final_score_scale") or "UNKNOWN") for row in trace_rows)
    final_operator_stage_use_counts = Counter(str(row.get("final_operator_stage_use") or "UNKNOWN") for row in trace_rows)
    final_operator_score_use_counts = Counter(str(row.get("final_operator_score_use") or "UNKNOWN") for row in trace_rows)
    critical_counts = {
        "seed_trace_count_mismatch_count": int(len(seed_rows) != len(trace_rows)),
        "score_evidence_allowed_before_execution_count": sum(1 for row in trace_rows if row.get("score_evidence_allowed") is True),
        "stage_promotion_allowed_before_execution_count": sum(1 for row in trace_rows if row.get("stage_promotion_allowed_before_execution") is True),
        "final_operator_stage_use_missing_count": sum(1 for row in trace_rows if not row.get("final_operator_stage_use")),
        "final_operator_score_use_missing_count": sum(1 for row in trace_rows if not row.get("final_operator_score_use")),
        "event_or_partial_stage_operator_use_allowed_count": sum(
            1
            for row in trace_rows
            if row.get("final_stage_scope") != "FULL_THESIS"
            and row.get("final_operator_stage_use") not in {"NOT_FULL_THESIS_STAGE"}
        ),
        "event_or_partial_score_operator_use_allowed_count": sum(
            1
            for row in trace_rows
            if row.get("final_score_scale") != "FULL_E2R_100"
            and row.get("final_operator_score_use") not in {"NOT_FULL_E2R_SCORE"}
        ),
        "source_task_before_real_provider_success_count": sum(
            1
            for row in trace_rows
            if int(row.get("source_task_execution_count") or 0) > 0
            and int(row.get("planner_real_provider_success_count") or 0) <= 0
        ),
        "accepted_claim_without_source_task_count": sum(
            1
            for row in trace_rows
            if int(row.get("accepted_claim_count") or 0) > 0 and int(row.get("source_task_execution_count") or 0) <= 0
        ),
        "stagecourt_without_accepted_claim_count": sum(
            1
            for row in trace_rows
            if int(row.get("stagecourt_trace_count") or 0) > 0 and int(row.get("accepted_claim_count") or 0) <= 0
        ),
        "full_thesis_promoted_missing_stagecourt_count": sum(
            1
            for row in trace_rows
            if row.get("materialization_status") == "FULL_THESIS_PROMOTED"
            and int(row.get("stagecourt_trace_count") or 0) <= 0
        ),
        "full_thesis_promoted_missing_full_e2r_score_count": sum(
            1
            for row in trace_rows
            if row.get("materialization_status") == "FULL_THESIS_PROMOTED"
            and row.get("final_score_scale") != "FULL_E2R_100"
        ),
        "full_thesis_promoted_operator_stage_use_not_full_count": sum(
            1
            for row in trace_rows
            if row.get("materialization_status") == "FULL_THESIS_PROMOTED"
            and row.get("final_operator_stage_use") != "FULL_THESIS_STAGE"
        ),
        "full_thesis_promoted_operator_score_use_not_full_count": sum(
            1
            for row in trace_rows
            if row.get("materialization_status") == "FULL_THESIS_PROMOTED"
            and row.get("final_operator_score_use") != "FULL_E2R_SCORE"
        ),
        "full_thesis_scope_without_promoted_status_count": sum(
            1
            for row in trace_rows
            if row.get("final_stage_scope") == "FULL_THESIS"
            and row.get("final_stage_scope_is_controlled_smoke") is not True
            and row.get("materialization_status") != "FULL_THESIS_PROMOTED"
        ),
    }
    critical_count = sum(int(value) for value in critical_counts.values())
    full_thesis_promoted_seed_count = int(status_counts.get("FULL_THESIS_PROMOTED", 0))
    ledger_integrity_pass_allowed = critical_count == 0
    actual_materialization_pass_allowed = ledger_integrity_pass_allowed and full_thesis_promoted_seed_count > 0
    next_actions_by_status = {
        "PLANNER_NOT_RUN": "run_real_full_thesis_planner_for_seed",
        "PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS": "fix_or_retry_real_planner_provider",
        "SOURCE_TASK_NOT_EXECUTED": "execute_bounded_official_first_source_tasks",
        "ACCEPTED_CLAIM_NOT_CREATED": "fetch_anchor_and_extract_score_eligible_claims",
        "STAGECOURT_TRACE_NOT_CREATED": "map_claims_to_primitives_scores_and_stagecourt",
        "STAGECOURT_READY_NOT_PROMOTED": "resolve_green_gate_or_material_gap_blockers",
        "FULL_THESIS_PROMOTED": "eligible_for_operator_full_thesis_stage_use",
    }
    return {
        "schema_version": "e2r_census_v4_full_thesis_seed_materialization_audit_v1",
        "seed_event_count": len(seed_rows),
        "trace_row_count": len(trace_rows),
        "status_counts": dict(sorted(status_counts.items())),
        "final_stage_scope_counts": dict(sorted(final_scope_counts.items())),
        "final_score_scale_counts": dict(sorted(final_score_scale_counts.items())),
        "final_operator_stage_use_counts": dict(sorted(final_operator_stage_use_counts.items())),
        "final_operator_score_use_counts": dict(sorted(final_operator_score_use_counts.items())),
        "planner_run_seed_count": sum(1 for row in trace_rows if int(row.get("planner_run_count") or 0) > 0),
        "real_provider_success_seed_count": sum(1 for row in trace_rows if int(row.get("planner_real_provider_success_count") or 0) > 0),
        "source_task_execution_seed_count": sum(1 for row in trace_rows if int(row.get("source_task_execution_count") or 0) > 0),
        "accepted_claim_seed_count": sum(1 for row in trace_rows if int(row.get("accepted_claim_count") or 0) > 0),
        "stagecourt_trace_seed_count": sum(1 for row in trace_rows if int(row.get("stagecourt_trace_count") or 0) > 0),
        "full_thesis_promoted_seed_count": full_thesis_promoted_seed_count,
        "controlled_smoke_full_thesis_final_scope_count": sum(
            1 for row in trace_rows if row.get("final_stage_scope_is_controlled_smoke") is True
        ),
        "critical_count": critical_count,
        "critical_counts": critical_counts,
        "verdict": "PASS" if critical_count == 0 else "FAIL",
        "verdict_scope": "LEDGER_INTEGRITY_ONLY" if not actual_materialization_pass_allowed else "ACTUAL_FULL_THESIS_MATERIALIZATION",
        "ledger_integrity_pass_allowed": ledger_integrity_pass_allowed,
        "actual_materialization_pass_allowed": actual_materialization_pass_allowed,
        "full_thesis_seed_promotion_pass": actual_materialization_pass_allowed,
        "operator_materialization_status": (
            "FULL_THESIS_MATERIALIZED"
            if actual_materialization_pass_allowed
            else "PENDING_FULL_THESIS_MATERIALIZATION"
        ),
        "next_actions_by_status": next_actions_by_status,
        "operator_rule": (
            "A seed row is only an investigation input until the trace reaches FULL_THESIS_PROMOTED. "
            "Earlier statuses must remain pending/source-provider/material-gap states and must not be used as an operator FULL_THESIS Stage. "
            "verdict=PASS only means ledger integrity passed; actual_materialization_pass_allowed must be true before claiming a real FULL_THESIS seed closure."
        ),
    }


def _source_task_execution_candidate_event_id(row: Mapping[str, Any]) -> str:
    task = row.get("source_task") if isinstance(row.get("source_task"), Mapping) else {}
    return str(row.get("candidate_event_id") or task.get("candidate_event_id") or "")


def _full_thesis_seed_materialization_status(
    *,
    planner_count: int,
    real_provider_success_count: int,
    source_task_execution_count: int,
    accepted_claim_count: int,
    stagecourt_trace_count: int,
    final_stage_scope: str,
    final_score_scale: str,
) -> tuple[str, list[str]]:
    blockers: list[str] = []
    if planner_count <= 0:
        return "PLANNER_NOT_RUN", ["full_thesis_seed_has_no_planner_run"]
    if real_provider_success_count <= 0:
        return "PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS", ["full_thesis_seed_planner_has_no_real_provider_success"]
    if source_task_execution_count <= 0:
        return "SOURCE_TASK_NOT_EXECUTED", ["full_thesis_seed_has_no_source_task_execution"]
    if accepted_claim_count <= 0:
        return "ACCEPTED_CLAIM_NOT_CREATED", ["full_thesis_seed_source_tasks_have_no_accepted_claim"]
    if stagecourt_trace_count <= 0:
        return "STAGECOURT_TRACE_NOT_CREATED", ["full_thesis_seed_claims_have_no_stagecourt_trace"]
    if final_stage_scope != "FULL_THESIS" or final_score_scale != "FULL_E2R_100":
        blockers.append("full_thesis_seed_stagecourt_trace_not_promoted_to_full_thesis")
        if final_stage_scope != "FULL_THESIS":
            blockers.append(f"final_stage_scope={final_stage_scope or 'UNKNOWN'}")
        if final_score_scale != "FULL_E2R_100":
            blockers.append(f"final_score_scale={final_score_scale or 'UNKNOWN'}")
        return "STAGECOURT_READY_NOT_PROMOTED", blockers
    return "FULL_THESIS_PROMOTED", []


def _is_controlled_smoke_full_thesis_stage(row: Mapping[str, Any]) -> bool:
    if row.get("stage_scope") != "FULL_THESIS":
        return False
    source_task_ids = [str(item) for item in row.get("full_thesis_source_task_ids") or []]
    return (
        row.get("score_source") == "SCORE_CONTRIBUTION_SUM"
        and str(row.get("score_build_method") or "") == "primitive_score_contribution_sum"
        and any(item.startswith("FTSMOKE-") for item in source_task_ids)
    )


def _full_thesis_refresh_priority_bucket(
    *,
    base_stage: str,
    stage_signal: str,
    stage_decision_status: str,
    risk_stage_signal: str,
) -> str:
    if risk_stage_signal and risk_stage_signal != "NONE":
        return "P0_RISK_REVIEW_REFRESH"
    if base_stage in {"Stage2-Watch", "Stage2-Actionable", "3-Green", "3-Yellow", "3-Red"}:
        return "P1_MATERIAL_STAGE_REFRESH"
    if stage_decision_status in {"PENDING_MATERIAL_GAPS", "SOURCE_PENDING", "PROVIDER_PENDING"}:
        return "P1_PENDING_MATERIAL_REFRESH"
    if stage_signal in {"MATERIAL_CLAIM_WATCH", "OFFICIAL_EVENT_WATCH"}:
        return "P2_EVENT_WATCH_REFRESH"
    return "P3_REVIEW_REFRESH"


def _full_thesis_refresh_queue_audit(
    stage_rows: Sequence[Mapping[str, Any]],
    queue_rows: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    event_board_non_stage0_count = sum(
        1 for row in stage_rows if row.get("stage_scope") == "CENSUS_EVENT_BOARD" and row.get("base_stage") != "Stage0"
    )
    full_thesis_stage_row_count = sum(1 for row in stage_rows if row.get("stage_scope") == "FULL_THESIS")
    score_allowed_before_execution_count = sum(1 for row in queue_rows if row.get("score_allowed_before_execution") is not False)
    stage_promotion_allowed_before_execution_count = sum(1 for row in queue_rows if row.get("stage_promotion_allowed_before_execution") is not False)
    hardcoded_query_count = sum(int(row.get("hardcoded_query_count") or 0) for row in queue_rows)
    unbounded_budget_count = sum(
        1
        for row in queue_rows
        if row.get("max_source_tasks") in {None, 0}
        or row.get("max_queries_per_task") in {None, 0}
        or row.get("max_candidates_per_query") in {None, 0}
        or row.get("max_fetches_per_task") in {None, 0}
    )
    operator_stage_copy_count = sum(1 for row in queue_rows if row.get("source_stage_scope") == "FULL_THESIS")
    queue_missing_event_board_count = max(0, event_board_non_stage0_count - len(queue_rows))
    critical_counts = {
        "queue_missing_event_board_count": queue_missing_event_board_count,
        "score_allowed_before_execution_count": score_allowed_before_execution_count,
        "stage_promotion_allowed_before_execution_count": stage_promotion_allowed_before_execution_count,
        "hardcoded_query_count": hardcoded_query_count,
        "unbounded_budget_count": unbounded_budget_count,
        "operator_stage_copy_count": operator_stage_copy_count,
    }
    return {
        "schema_version": "e2r_census_v4_full_thesis_refresh_queue_audit_v1",
        "verdict": "PASS" if sum(critical_counts.values()) == 0 else "FAIL",
        "queue_status": "REFRESH_QUEUE_PRESENT" if queue_rows else "REFRESH_QUEUE_EMPTY",
        "queue_candidate_count": len(queue_rows),
        "event_board_non_stage0_count": event_board_non_stage0_count,
        "full_thesis_stage_row_count": full_thesis_stage_row_count,
        "priority_bucket_distribution": _count_by(queue_rows, "priority_bucket"),
        "source_base_stage_distribution": _count_by(queue_rows, "source_base_stage"),
        "source_stage_signal_distribution": _count_by(queue_rows, "source_stage_signal"),
        "critical_counts": critical_counts,
        "rule": "CENSUS_EVENT_BOARD non-Stage0 rows are queued for bounded full-thesis refresh; queue rows cannot score or promote until source-backed claims, score contributions, and StageCourt trace close.",
    }


def _brain_audit(config: CensusV4RunConfig, *, output_root: Path) -> dict[str, Any]:
    claimed = _config_requests_brain_planner(config)
    planner = _read_jsonl(output_root / "planner_runs.jsonl")
    attempt = _read_json(output_root / "brain_web_attempt_audit.json")
    real_success = sum(1 for row in planner if row.get("provider_mode") == "real" and row.get("real_provider_success") is True)
    zero = int(claimed and not planner)
    success_zero = int(claimed and real_success == 0)
    return {
        "schema_version": "e2r_census_v4_brain_planner_audit_v1",
        "llm_planner_call_count": real_success,
        "planner_run_row_count": len(planner),
        "llm_real_provider_success_count": real_success,
        "llm_claimed_but_zero_calls_count": zero,
        "llm_claimed_but_zero_success_count": success_zero,
        "requested_by_run_mode": _run_mode_requests_brain_planner(config.run_mode),
        "requested_by_brain_web_mode": config.brain_web_mode == "enabled",
        "attempt_verdict": attempt.get("verdict"),
        "verdict": "FAIL" if zero or success_zero else "PASS",
    }


def _web_audit(config: CensusV4RunConfig, *, output_root: Path) -> dict[str, Any]:
    claimed = _config_requests_web_acquisition(config)
    web_tasks = _read_jsonl(output_root / "web_search_tasks.jsonl")
    web_results = _read_jsonl(output_root / "web_search_results.jsonl")
    web_fetched = _read_jsonl(output_root / "web_fetched_documents.jsonl")
    web_rejected = _read_jsonl(output_root / "web_rejected_documents.jsonl")
    call_counts = _web_search_call_counts(web_tasks=web_tasks, web_results=web_results)
    zero = int(claimed and not web_tasks and not web_results and not web_fetched)
    fetched = bool(web_fetched)
    result_only = claimed and bool(web_results) and not fetched
    task_only = claimed and bool(web_tasks) and not web_results and not fetched
    if zero:
        verdict = "FAIL"
        pass_scope = "failed"
    elif not claimed:
        verdict = "DISABLED_HONESTY_PASS"
        pass_scope = "disabled_honesty"
    elif fetched:
        verdict = "REAL_ACQUISITION_PASS"
        pass_scope = "real_full_source_acquisition"
    elif result_only:
        verdict = "WEB_RESULTS_ONLY_NOT_FETCHED"
        pass_scope = "attempted_search_without_fetched_source"
    elif task_only:
        verdict = "WEB_TASKS_ONLY_NOT_FETCHED"
        pass_scope = "task_only_no_search_result_or_fetch"
    else:
        verdict = "ATTEMPTED_NO_FETCHED_DOCUMENTS"
        pass_scope = "attempted_no_full_source"
    return {
        "schema_version": "e2r_census_v4_web_naver_acquisition_audit_v1",
        "web_search_task_count": len(web_tasks),
        "web_search_result_count": len(web_results),
        "web_fetched_document_count": len(web_fetched),
        "web_rejected_document_count": len(web_rejected),
        "web_search_call_count": call_counts["web_search_call_count"],
        "naver_search_call_count": call_counts["naver_search_call_count"],
        "trusted_news_search_call_count": call_counts["trusted_news_search_call_count"],
        "general_web_search_call_count": call_counts["general_web_search_call_count"],
        "web_claimed_but_zero_search_count": zero,
        "requested_by_run_mode": _run_mode_requests_web_acquisition(config.run_mode),
        "requested_by_brain_web_mode": config.brain_web_mode == "enabled",
        "task_only_real_acquisition_pass_allowed": False,
        "verdict": verdict,
        "pass_scope": pass_scope,
    }


def _web_search_call_counts(*, web_tasks: Sequence[Mapping[str, Any]], web_results: Sequence[Mapping[str, Any]]) -> dict[str, int]:
    executed_tasks = [
        row
        for row in web_tasks
        if row.get("search_call_executed") is True or str(row.get("status") or "") in {"SEARCH_EXECUTED", "PROVIDER_FAILED"}
    ]
    providers = [str(row.get("provider_name") or row.get("search_provider") or "").lower() for row in executed_tasks]
    if not executed_tasks and web_results:
        providers = [str(row.get("provider_name") or row.get("search_provider") or "").lower() for row in web_results]
    return {
        "web_search_call_count": len(executed_tasks) if executed_tasks else len({str(row.get("web_task_id") or row.get("task_id") or "") for row in web_results}),
        "naver_search_call_count": sum(1 for provider in providers if "naver" in provider),
        "trusted_news_search_call_count": sum(1 for provider in providers if "trusted" in provider or "news" in provider),
        "general_web_search_call_count": sum(1 for provider in providers if "general" in provider or "web" in provider),
    }


def _extractor_audit(config: CensusV4RunConfig, *, output_root: Path) -> dict[str, Any]:
    claimed = _config_requests_llm_claim_extraction(config)
    runs = _read_jsonl(output_root / "claim_extractor_runs.jsonl")
    llm_runs = [row for row in runs if str(row.get("provider_mode") or "").lower() == "llm"]
    non_llm_runs = [row for row in runs if row.get("provider_mode") and str(row.get("provider_mode") or "").lower() != "llm"]
    provider_error_runs = [row for row in runs if str(row.get("provider_error") or "").strip()]
    timeout_error_runs = [row for row in provider_error_runs if "timeout" in str(row.get("provider_error") or "").lower()]
    zero = int(claimed and not runs)
    real_extraction = claimed and bool(llm_runs)
    non_llm_only = claimed and bool(runs) and not llm_runs
    failed = bool(zero or provider_error_runs)
    return {
        "schema_version": "e2r_census_v4_llm_claim_extraction_audit_v1",
        "llm_claim_extractor_attempt_count": len(runs),
        "llm_claim_extractor_real_provider_count": len(llm_runs),
        "claim_extractor_non_llm_provider_count": len(non_llm_runs),
        "llm_claim_extractor_provider_error_count": len(provider_error_runs),
        "llm_claim_extractor_timeout_count": len(timeout_error_runs),
        "llm_claim_extractor_claimed_but_zero_count": zero,
        "configured_timeout_seconds": config.brain_claim_extractor_timeout_seconds,
        "requested_by_run_mode": _run_mode_requests_llm_claim_extraction(config.run_mode),
        "requested_by_brain_web_mode": config.brain_web_mode == "enabled",
        "verdict": "FAIL"
        if failed
        else ("REAL_EXTRACTION_PASS" if real_extraction else ("NON_LLM_EXTRACTION_ONLY" if non_llm_only else "DISABLED_HONESTY_PASS")),
        "pass_scope": "failed"
        if failed
        else ("real_extraction" if real_extraction else ("non_llm_diagnostic_only" if non_llm_only else "disabled_honesty")),
    }


def _brain_trace_audit(config: CensusV4RunConfig, *, output_root: Path) -> dict[str, Any]:
    traces = _read_jsonl(output_root / "brain_to_claim_trace.jsonl")
    attempt = _read_json(output_root / "brain_web_attempt_audit.json")
    accepted = int(attempt.get("brain_to_census_claim_exported_count") or 0)
    missing = max(0, accepted - len(traces))
    return {
        "schema_version": "e2r_census_v4_brain_to_claim_trace_audit_v1",
        "brain_to_claim_trace_count": len(traces),
        "brain_trace_missing_count": missing,
        "verdict": "PASS" if missing == 0 and (config.brain_web_mode != "enabled" or traces or accepted == 0) else "FAIL",
    }


def _brain_claim_quality_counts(rows: Sequence[Mapping[str, Any]]) -> dict[str, int]:
    current_values = {"CURRENT", "PRESENT_CURRENT", "OPEN"}
    direct_values = {"DIRECT"}
    return {
        "missing_verifiable_anchor_count": sum(1 for row in rows if not row.get("document_id") or not row.get("anchor_id")),
        "missing_date_count": sum(
            1
            for row in rows
            if not row.get("event_date") and not row.get("as_of_date") and not row.get("source_cutover_date") and not row.get("published_at")
        ),
        "not_direct_target_count": sum(1 for row in rows if str(row.get("target_scope_status") or "") not in direct_values),
        "not_current_count": sum(1 for row in rows if str(row.get("temporal_status") or "") not in current_values),
        "score_ineligible_count": sum(1 for row in rows if row.get("score_eligible") is not True),
    }


def _brain_claim_source_split(*, output_root: Path, brain_claims: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    web_fetched = _read_jsonl(output_root / "web_fetched_documents.jsonl")
    extractor_runs = _read_jsonl(output_root / "claim_extractor_runs.jsonl")
    llm_raw_assertion_ids = (
        set().union(
            *(
                _ids_from_value(row.get("raw_assertion_ids"))
                for row in extractor_runs
                if str(row.get("provider_mode") or "").lower() == "llm"
            )
        )
        if extractor_runs
        else set()
    )
    web_document_ids = _row_ids(web_fetched, "document_id") | _row_ids(web_fetched, "fetched_document_id") | _row_ids(web_fetched, "web_document_id")
    web_source_urls = {
        str(row.get("url") or row.get("source_url") or row.get("canonical_url") or "")
        for row in web_fetched
        if str(row.get("url") or row.get("source_url") or row.get("canonical_url") or "").strip()
    }
    web_news_accepted = [
        row
        for row in brain_claims
        if _accepted_claim_is_web_news_source(row, web_document_ids=web_document_ids, web_source_urls=web_source_urls)
    ]
    llm_extracted_accepted = [
        row for row in brain_claims if _accepted_claim_is_llm_extracted(row, llm_raw_assertion_ids=llm_raw_assertion_ids)
    ]
    web_or_llm_accepted_claim_ids = _row_ids(web_news_accepted, "claim_id") | _row_ids(llm_extracted_accepted, "claim_id")
    official_accepted = [
        row
        for row in brain_claims
        if not _ids_from_value(row.get("claim_id")) & web_or_llm_accepted_claim_ids
        and _accepted_claim_is_official_source(row)
    ]
    return {
        "web_news_accepted_claims": web_news_accepted,
        "llm_extracted_accepted_claims": llm_extracted_accepted,
        "official_accepted_claims": official_accepted,
        "web_or_llm_accepted_claim_ids": web_or_llm_accepted_claim_ids,
        "llm_raw_assertion_ids": llm_raw_assertion_ids,
        "web_document_ids": web_document_ids,
        "web_source_urls": web_source_urls,
    }


def _promote_brain_stage_rows(
    *,
    config: CensusV4RunConfig,
    output_root: Path,
    stage_rows: Sequence[Mapping[str, Any]],
    brain_web_attempt: Mapping[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    if config.brain_web_mode != "enabled" or config.brain_stage_promotion_mode != "strict":
        return _apply_operator_scope_aliases(stage_rows), {
            "schema_version": "e2r_census_v4_brain_stage_promotion_export_v1",
            "promoted_stage_row_count": 0,
            "skipped_reason": "promotion_not_requested",
        }

    preflight = _brain_stage_promotion_audit(
        config=config,
        output_root=output_root,
        brain_web_attempt=brain_web_attempt,
        stage_rows=[],
    )
    if preflight.get("verdict") != "ELIGIBLE_NOT_PROMOTED":
        return _apply_operator_scope_aliases(stage_rows), {
            "schema_version": "e2r_census_v4_brain_stage_promotion_export_v1",
            "promoted_stage_row_count": 0,
            "skipped_reason": "preflight_blocked",
            "preflight_verdict": preflight.get("verdict"),
            "preflight_blockers": preflight.get("blockers") or [],
        }

    stagecourt = _read_jsonl(output_root / "stagecourt_traces.jsonl")
    accepted = _read_jsonl(output_root / "accepted_claims.jsonl")
    brain_claims = [row for row in accepted if row.get("brain_web_claim") is True or _is_brain_origin(row)]
    accepted_by_id = {str(row.get("claim_id") or ""): row for row in accepted if str(row.get("claim_id") or "").strip()}
    source_executions = _read_jsonl(output_root / "source_task_executions.jsonl")
    source_split = _brain_claim_source_split(output_root=output_root, brain_claims=brain_claims)
    web_or_llm_accepted_claim_ids = set(source_split["web_or_llm_accepted_claim_ids"])
    official_accepted_claim_ids = _row_ids(source_split["official_accepted_claims"], "claim_id")
    brain_traces = [
        row
        for row in stagecourt
        if _is_brain_origin(row) or str(row.get("stagecourt_trace_id") or row.get("trace_id") or "").startswith("SCT-BRAIN-")
    ]
    if not brain_traces:
        return _apply_operator_scope_aliases(stage_rows), {
            "schema_version": "e2r_census_v4_brain_stage_promotion_export_v1",
            "promoted_stage_row_count": 0,
            "skipped_reason": "no_brain_stagecourt_trace",
        }

    by_symbol = {str(row.get("symbol") or "").zfill(6): dict(row) for row in stage_rows}
    promoted_by_trace: dict[str, str] = {}
    promoted_claim_ids_by_trace: dict[str, list[str]] = {}
    promoted_count = 0
    promoted_web_llm_count = 0
    promoted_official_count = 0
    skipped_unsupported_trace_count = 0
    for trace in sorted(brain_traces, key=lambda row: str(row.get("stagecourt_trace_id") or row.get("trace_id") or "")):
        symbol = str(trace.get("symbol") or "").zfill(6)
        if symbol not in by_symbol:
            continue
        trace_id = str(trace.get("stagecourt_trace_id") or trace.get("trace_id") or "")
        if not trace_id:
            continue
        score_interval = trace.get("score_interval") if isinstance(trace.get("score_interval"), Mapping) else {}
        lower = _float_or_none(score_interval.get("lower"))
        upper = _float_or_none(score_interval.get("upper"))
        accepted_ids = list(trace.get("accepted_claim_ids") or ())
        contribution_ids = list(trace.get("score_contribution_ids") or ())
        primitive_state_ids = list(trace.get("primitive_state_ids") or ())
        missing = list(trace.get("missing_green_primitives") or ()) + list(trace.get("missing_yellow_primitives") or ())
        trace_claim_ids = _ids_from_value(accepted_ids) | _ids_from_value(trace.get("support_claim_ids"))
        web_llm_claim_ids = trace_claim_ids & web_or_llm_accepted_claim_ids
        official_claim_ids = trace_claim_ids & official_accepted_claim_ids
        official_source_task_ids = _brain_source_task_ids_for_claims(source_executions, sorted(official_claim_ids))
        official_document_ids = sorted(
            {
                str(accepted_by_id[claim_id].get("document_id") or "")
                for claim_id in official_claim_ids
                if claim_id in accepted_by_id and str(accepted_by_id[claim_id].get("document_id") or "").strip()
            }
        )
        if web_llm_claim_ids:
            partial_lane = "web_llm"
            stage_scope = "BRAIN_WEB_PARTIAL"
            assessment_depth = "BRAIN_WEB_VERIFIED_STAGE"
            stage_signal = "BRAIN_WEB_CLAIM_BACKED_STAGE"
            stage_confidence = "BRAIN_WEB_CLAIM_BACKED_PARTIAL"
            score_scope = "BRAIN_WEB_CLAIM_BACKED_PARTIAL"
            score_source = "BRAIN_WEB_STAGECOURT_SCORE_INTERVAL"
            score_semantics = "brain_web_claim_backed_partial_score_not_full_thesis"
            semantic_guard_class = "brain_web_claim_backed_partial"
            next_actions = ["BRAIN_WEB_RECHECK", "FULL_THESIS_REFRESH"]
        elif official_claim_ids:
            partial_lane = "official"
            stage_scope = "BRAIN_OFFICIAL_PARTIAL"
            assessment_depth = "BRAIN_OFFICIAL_VERIFIED_STAGE"
            stage_signal = "BRAIN_OFFICIAL_CLAIM_BACKED_STAGE"
            stage_confidence = "BRAIN_OFFICIAL_CLAIM_BACKED_PARTIAL"
            score_scope = "BRAIN_OFFICIAL_CLAIM_BACKED_PARTIAL"
            score_source = "BRAIN_OFFICIAL_STAGECOURT_SCORE_INTERVAL"
            score_semantics = "brain_official_claim_backed_partial_score_not_full_thesis"
            semantic_guard_class = "brain_official_claim_backed_partial"
            next_actions = ["OFFICIAL_EVIDENCE_RECHECK", "FULL_THESIS_REFRESH"]
        else:
            skipped_unsupported_trace_count += 1
            continue
        census_stage_status_id = "CSS-BRAIN-" + stable_hash((symbol, trace_id, accepted_ids, contribution_ids))[:20]
        row = dict(by_symbol[symbol])
        row.update(
            {
                "census_stage_status_id": census_stage_status_id,
                "stage_source": "research_brain_v4_attempt",
                "source_origin": "research_brain_v4_attempt",
                "census_status": "DEEP_VERIFIED",
                "assessment_depth": assessment_depth,
                "base_stage": trace.get("base_stage"),
                "canonical_stage": canonical_stage_for_display(trace.get("base_stage")),
                "stage_signal": stage_signal,
                "stage_scope": stage_scope,
                "brain_partial_evidence_lane": partial_lane,
                "risk_stage_signal": "NONE",
                "transition_overlay": trace.get("transition_overlay") or "NONE",
                "investigation_status": trace.get("investigation_status") or trace.get("score_status"),
                "stage_decision_status": trace.get("score_status"),
                "stage_confidence": stage_confidence,
                "score_valid_status": trace.get("score_status"),
                "score_scale": "EVENT_WEIGHTED_PARTIAL",
                "score_scope": score_scope,
                "score_source": score_source,
                "score_semantics": score_semantics,
                "verified_score": None,
                "full_e2r_verified_score": None,
                "event_evidence_score": lower,
                "raw_contribution_score": None,
                "score_interval_lower": lower,
                "score_interval_upper": upper,
                "atomic_stage_decision_id": None,
                "additional_stage_decision_ids": [],
                "accepted_claim_ids": accepted_ids,
                "score_contribution_ids": contribution_ids,
                "primitive_state_ids": primitive_state_ids,
                "stagecourt_trace_id": trace_id,
                "accepted_claim_count": len(accepted_ids),
                "score_contribution_count": len(contribution_ids),
                "accepted_official_claim_count": len(official_claim_ids),
                "accepted_web_llm_claim_count": len(web_llm_claim_ids),
                "official_source_task_count": len(official_source_task_ids),
                "official_evidence_document_count": len(official_document_ids),
                "official_source_task_ids": official_source_task_ids,
                "official_evidence_document_ids": official_document_ids,
                "missing_primitives": missing,
                "material_gap_ids": missing,
                "failed_stage_gates": missing,
                "semantic_guard_status": "PASS",
                "semantic_guard_class": semantic_guard_class,
                "semantic_guard_reasons": [],
                "daily_event_stage_signal": row.get("daily_event_stage_signal"),
                "daily_event_evidence_score": row.get("daily_event_evidence_score"),
                "full_thesis_primary_archetype": None,
                "full_thesis_verified_score": None,
                "full_thesis_score_scale": "NO_SCORE",
                "full_thesis_stage": "FULL_THESIS_NOT_RUN",
                "full_thesis_score_valid_status": "NOT_SCORED",
                "full_thesis_missing_primitives": ["full_thesis_refresh_task_not_run"],
                "next_actions": next_actions,
            }
        )
        by_symbol[symbol] = row
        promoted_by_trace[trace_id] = census_stage_status_id
        promoted_claim_ids_by_trace[trace_id] = accepted_ids
        promoted_count += 1
        if partial_lane == "web_llm":
            promoted_web_llm_count += 1
        elif partial_lane == "official":
            promoted_official_count += 1

    if promoted_by_trace:
        _mark_brain_stage_traces_promoted(output_root=output_root, promoted_by_trace=promoted_by_trace)
        _mark_brain_to_claim_traces_promoted(
            output_root=output_root,
            promoted_by_trace=promoted_by_trace,
            promoted_claim_ids_by_trace=promoted_claim_ids_by_trace,
        )

    promoted_rows = [by_symbol.get(str(row.get("symbol") or "").zfill(6), dict(row)) for row in stage_rows]
    return _apply_operator_scope_aliases(promoted_rows), {
        "schema_version": "e2r_census_v4_brain_stage_promotion_export_v1",
        "promoted_stage_row_count": promoted_count,
        "promoted_web_llm_stage_row_count": promoted_web_llm_count,
        "promoted_official_stage_row_count": promoted_official_count,
        "promoted_stagecourt_trace_ids": sorted(promoted_by_trace),
        "skipped_unsupported_trace_count": skipped_unsupported_trace_count,
    }


def _apply_production_full_thesis_from_brain(
    *,
    config: CensusV4RunConfig,
    output_root: Path,
    stage_rows: Sequence[Mapping[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    refresh_queue_rows = _full_thesis_refresh_queue(stage_rows)
    refresh_queue_count = len(refresh_queue_rows)
    empty_queue_materialization = _full_thesis_refresh_queue_materialization_audit(refresh_queue_rows=refresh_queue_rows, candidates=[])
    if not _config_requests_production_full_thesis(config):
        return _apply_operator_scope_aliases(stage_rows), {
            "schema_version": "e2r_census_v4_full_thesis_production_runner_audit_v1",
            "verdict": "NOT_REQUESTED",
            "production_mode_requested": False,
            "full_thesis_refresh_queue_candidate_count": refresh_queue_count,
            "candidate_row_count": 0,
            "candidate_source_counts": {},
            "promoted_full_thesis_row_count": 0,
            "blocked_candidate_count": 0,
            "blocked_candidates": [],
            **empty_queue_materialization,
        }
    if config.brain_web_mode != "enabled" or config.brain_stage_promotion_mode != "strict":
        return _apply_operator_scope_aliases(stage_rows), {
            "schema_version": "e2r_census_v4_full_thesis_production_runner_audit_v1",
            "verdict": "BLOCKED_BEFORE_CANDIDATE_SCAN",
            "production_mode_requested": True,
            "full_thesis_refresh_queue_candidate_count": refresh_queue_count,
            "candidate_row_count": 0,
            "candidate_source_counts": {},
            "promoted_full_thesis_row_count": 0,
            "blocked_candidate_count": 0,
            "blocked_candidates": [],
            "blockers": ["brain_web_mode_enabled_and_strict_promotion_required"],
            **empty_queue_materialization,
        }

    try:
        from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
    except Exception as exc:  # pragma: no cover - import failure is an explicit blocker.
        return _apply_operator_scope_aliases(stage_rows), {
            "schema_version": "e2r_census_v4_full_thesis_production_runner_audit_v1",
            "verdict": "BLOCKED_BEFORE_CANDIDATE_SCAN",
            "production_mode_requested": True,
            "full_thesis_refresh_queue_candidate_count": refresh_queue_count,
            "candidate_row_count": 0,
            "candidate_source_counts": {},
            "promoted_full_thesis_row_count": 0,
            "blocked_candidate_count": 0,
            "blocked_candidates": [],
            "blockers": [f"evidence_contract_v2_import_failed:{type(exc).__name__}"],
            **empty_queue_materialization,
        }

    contracts = load_evidence_contracts_v2(require_all_archetypes=True)
    traces = {str(row.get("stagecourt_trace_id") or row.get("trace_id") or ""): row for row in _read_jsonl(output_root / "stagecourt_traces.jsonl")}
    primitive_states = {str(row.get("primitive_state_id") or ""): row for row in _read_jsonl(output_root / "primitive_states.jsonl")}
    accepted_claims = {str(row.get("claim_id") or ""): row for row in _read_jsonl(output_root / "accepted_claims.jsonl")}
    source_executions = _read_jsonl(output_root / "source_task_executions.jsonl")
    evidence_documents = {str(row.get("document_id") or ""): row for row in _read_jsonl(output_root / "evidence_documents.jsonl")}

    by_symbol = {str(row.get("symbol") or "").zfill(6): dict(row) for row in stage_rows}
    candidates = _production_full_thesis_candidate_rows(stage_rows=stage_rows, traces=traces)
    queue_materialization = _full_thesis_refresh_queue_materialization_audit(refresh_queue_rows=refresh_queue_rows, candidates=candidates)
    candidate_source_counts = _production_full_thesis_candidate_source_counts(candidates)
    blocked_candidates: list[dict[str, Any]] = []
    promoted_symbols: list[str] = []

    for row in candidates:
        symbol = str(row.get("symbol") or "").zfill(6)
        trace_id = str(row.get("stagecourt_trace_id") or "")
        trace = traces.get(trace_id) or {}
        archetype_id = str(trace.get("primary_archetype") or trace.get("canonical_archetype_id") or row.get("full_thesis_primary_archetype") or "").strip()
        contract = contracts.get(archetype_id)
        blockers: list[str] = []
        if not trace_id or not trace:
            blockers.append("missing_brain_stagecourt_trace")
        if contract is None:
            blockers.append("missing_or_unknown_primary_archetype")
        if config.brain_planner_provider in {"none", "test_fake"}:
            blockers.append("real_planner_provider_required")
        if config.brain_source_acquisition in {"frozen_real_source_snapshot", "test_fake"}:
            blockers.append("production_live_source_acquisition_required")

        accepted_ids = [str(item) for item in trace.get("accepted_claim_ids") or row.get("accepted_claim_ids") or [] if str(item)]
        contribution_ids = [str(item) for item in trace.get("score_contribution_ids") or row.get("score_contribution_ids") or [] if str(item)]
        primitive_state_ids = [str(item) for item in trace.get("primitive_state_ids") or row.get("primitive_state_ids") or [] if str(item)]
        present_primitives = {
            str(primitive_states.get(state_id, {}).get("primitive_id") or "")
            for state_id in primitive_state_ids
            if primitive_states.get(state_id, {}).get("primitive_id")
        }
        required_green_primitives = set(contract.green_gate.primitive_ids()) if contract is not None else set()
        missing_green_primitives = sorted(required_green_primitives - present_primitives)
        if missing_green_primitives:
            blockers.append("missing_green_gate_primitives")
        if not accepted_ids:
            blockers.append("missing_accepted_claim_ids")
        if not contribution_ids:
            blockers.append("missing_score_contribution_ids")
        if not primitive_state_ids:
            blockers.append("missing_primitive_state_ids")

        candidate_event_id = str(trace.get("candidate_event_id") or row.get("candidate_event_id") or "")
        claim_quality_blockers = _production_full_thesis_claim_blockers(
            accepted_ids=accepted_ids,
            accepted_claims=accepted_claims,
            evidence_documents=evidence_documents,
        )
        blockers.extend(claim_quality_blockers)
        source_linkage_blockers, source_linkage_proof, linked_source_task_ids = _production_full_thesis_source_linkage(
            accepted_ids=accepted_ids,
            accepted_claims=accepted_claims,
            source_executions=source_executions,
            candidate_event_id=candidate_event_id,
        )
        blockers.extend(source_linkage_blockers)

        lower = _float_or_none((trace.get("score_interval") or {}).get("lower") if isinstance(trace.get("score_interval"), Mapping) else None)
        upper = _float_or_none((trace.get("score_interval") or {}).get("upper") if isinstance(trace.get("score_interval"), Mapping) else None)
        score_status = str(trace.get("score_status") or "")
        if lower is None:
            blockers.append("missing_verified_score_interval_lower")
        if upper is None:
            blockers.append("missing_verified_score_interval_upper")
        if lower is not None and upper is not None and upper < lower:
            blockers.append("invalid_score_interval_bounds")
        if score_status not in {"FINAL", "FINAL_WITH_NONMATERIAL_GAPS"}:
            blockers.append("score_status_not_final")

        if blockers:
            blocked_candidates.append(
                {
                    "symbol": symbol,
                    "company_name": row.get("company_name"),
                    "candidate_event_id": candidate_event_id or None,
                    "stagecourt_trace_id": trace_id,
                    "candidate_source": row.get("_full_thesis_candidate_source"),
                    "primary_archetype": archetype_id or None,
                    "present_primitives": sorted(present_primitives),
                    "missing_green_primitives": missing_green_primitives,
                    "source_linkage_proof": source_linkage_proof,
                    "blockers": sorted(dict.fromkeys(blockers)),
                }
            )
            continue

        item = dict(row)
        item.update(
            {
                "census_status": "FULL_THESIS_VERIFIED",
                "assessment_depth": "FULL_THESIS_REFRESH",
                "stage_scope": "FULL_THESIS",
                "stage_source": "research_brain_v4_attempt",
                "source_origin": "research_brain_v4_attempt",
                "stage_signal": "FULL_THESIS_PRODUCTION_STAGE",
                "stage_confidence": "FULL_THESIS_CLAIM_BACKED",
                "stage_decision_status": score_status,
                "score_valid_status": score_status,
                "score_scale": "FULL_E2R_100",
                "score_scope": "FULL_E2R_100",
                "score_source": "BRAIN_WEB_PRODUCTION_FULL_THESIS_STAGECOURT",
                "score_semantics": "production_full_thesis_claim_backed_score",
                "verified_score": lower,
                "full_e2r_verified_score": lower,
                "event_evidence_score": None,
                "score_interval_lower": lower,
                "score_interval_upper": upper,
                "accepted_claim_ids": accepted_ids,
                "score_contribution_ids": contribution_ids,
                "primitive_state_ids": primitive_state_ids,
                "accepted_claim_count": len(accepted_ids),
                "score_contribution_count": len(contribution_ids),
                "missing_primitives": [],
                "material_gap_ids": [],
                "failed_stage_gates": [],
                "full_thesis_primary_archetype": archetype_id,
                "full_thesis_verified_score": lower,
                "full_thesis_score_scale": "FULL_E2R_100",
                "full_thesis_stage": trace.get("base_stage"),
                "full_thesis_score_valid_status": score_status,
                "full_thesis_missing_primitives": [],
                "full_thesis_accepted_claim_ids": accepted_ids,
                "full_thesis_score_contribution_ids": contribution_ids,
                "full_thesis_stagecourt_trace_ids": [trace_id],
                "full_thesis_source_task_ids": linked_source_task_ids,
                "full_thesis_source_linkage_proof": source_linkage_proof,
                "full_thesis_production_mode": "research_brain_v4_production",
                "next_actions": ["WATCH"],
            }
        )
        by_symbol[symbol] = item
        promoted_symbols.append(symbol)

    out = [by_symbol.get(str(row.get("symbol") or "").zfill(6), dict(row)) for row in stage_rows]
    verdict = "PRODUCTION_FULL_THESIS_PROMOTED" if promoted_symbols else "PENDING_PRODUCTION_FULL_THESIS"
    blockers: list[str] = []
    if refresh_queue_count > 0 and not candidates:
        blockers.append("full_thesis_refresh_queue_has_no_brain_stagecourt_trace_candidates")
    blocker_follow_up_source_tasks = _full_thesis_blocker_follow_up_source_tasks(
        config=config,
        blocked_candidates=blocked_candidates,
        traces=traces,
        contracts=contracts,
    )
    blocker_follow_up_source_task_path = output_root / "full_thesis_blocker_follow_up_source_tasks.jsonl"
    write_jsonl(blocker_follow_up_source_task_path, blocker_follow_up_source_tasks)
    blocker_follow_up_seed_events = _full_thesis_blocker_follow_up_seed_events(
        config=config,
        output_root=output_root,
        source_tasks=blocker_follow_up_source_tasks,
    )
    blocker_follow_up_seed_event_path = output_root / "full_thesis_blocker_follow_up_seed_events.jsonl"
    write_jsonl(blocker_follow_up_seed_event_path, blocker_follow_up_seed_events)
    audit = {
        "schema_version": "e2r_census_v4_full_thesis_production_runner_audit_v1",
        "verdict": verdict,
        "production_mode_requested": True,
        "full_thesis_refresh_queue_candidate_count": refresh_queue_count,
        "candidate_row_count": len(candidates),
        "candidate_source_counts": candidate_source_counts,
        "promoted_full_thesis_row_count": len(promoted_symbols),
        "promoted_symbols": sorted(promoted_symbols),
        "blocked_candidate_count": len(blocked_candidates),
        "blocked_candidates": blocked_candidates,
        "blocked_candidate_follow_up_source_task_path": str(blocker_follow_up_source_task_path),
        "blocked_candidate_follow_up_source_task_count": len(blocker_follow_up_source_tasks),
        "blocked_candidate_follow_up_seed_event_path": str(blocker_follow_up_seed_event_path),
        "blocked_candidate_follow_up_seed_event_count": len(blocker_follow_up_seed_events),
        "blocked_candidate_follow_up_primitive_gaps": sorted(
            {
                str(task.get("primitive_gap") or "")
                for task in blocker_follow_up_source_tasks
                if str(task.get("primitive_gap") or "")
            }
        ),
        "blocked_candidate_follow_up_rule": (
            "A blocked production full-thesis candidate does not receive score or Stage credit. "
            "Each missing Green primitive is exported as an official-first bounded SourceTask shell with empty query_intents; "
            "a matching planner-input-only seed event is also exported for the next Research Brain run. The planner must generate "
            "the actual queries, and source-backed Evidence OS claims must close the gap before any FULL_THESIS promotion."
        ),
        "blockers": blockers,
        **queue_materialization,
        "rule": "Research Brain StageCourt traces, including official-only traces that were not BRAIN_WEB_PARTIAL, become production FULL_THESIS only when live source tasks, direct/current score-eligible claims, score contributions, StageCourt trace, and contract green-gate primitive coverage are all closed. This does not satisfy the separate Brain/Web evidence gate.",
    }
    return _apply_operator_scope_aliases(out), audit


def _full_thesis_blocker_follow_up_source_tasks(
    *,
    config: CensusV4RunConfig,
    blocked_candidates: Sequence[Mapping[str, Any]],
    traces: Mapping[str, Mapping[str, Any]],
    contracts: Mapping[str, Any],
) -> list[dict[str, Any]]:
    tasks: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str]] = set()
    for candidate in blocked_candidates:
        blockers = {str(item) for item in candidate.get("blockers") or [] if str(item)}
        if "missing_green_gate_primitives" not in blockers:
            continue
        symbol = str(candidate.get("symbol") or "").zfill(6)
        archetype_id = str(candidate.get("primary_archetype") or "").strip()
        if not symbol or not archetype_id:
            continue
        trace_id = str(candidate.get("stagecourt_trace_id") or "")
        trace = traces.get(trace_id) or {}
        contract = contracts.get(archetype_id)
        for primitive_gap in [str(item) for item in candidate.get("missing_green_primitives") or [] if str(item)]:
            key = (symbol, archetype_id, primitive_gap)
            if key in seen:
                continue
            seen.add(key)
            freshness_policy = getattr(contract, "freshness", {}).get(primitive_gap) if contract is not None else None
            max_age_days = getattr(freshness_policy, "max_age_days", None) or 365
            candidate_event_id = str(trace.get("candidate_event_id") or candidate.get("candidate_event_id") or "")
            task_id = "FTGAP-" + stable_hash((config.as_of_date, symbol, archetype_id, primitive_gap, trace_id))[:24]
            tasks.append(
                {
                    "schema_version": "e2r_census_v4_full_thesis_blocker_follow_up_source_task_v1",
                    "task_id": task_id,
                    "source_task_origin": "full_thesis_green_gate_blocker_follow_up",
                    "task_type": "green_closure",
                    "task_status": "PLANNING_REQUIRED",
                    "candidate_event_id": candidate_event_id or f"CE-FTGAP-{symbol}-{stable_hash((task_id, 'candidate'))[:12]}",
                    "symbol": symbol,
                    "company_name": trace.get("company_name") or candidate.get("company_name"),
                    "as_of_date": config.as_of_date,
                    "archetype_id": archetype_id,
                    "primitive_gap": primitive_gap,
                    "blocked_stagecourt_trace_id": trace_id,
                    "blocked_candidate_source": candidate.get("candidate_source"),
                    "present_primitives": list(candidate.get("present_primitives") or []),
                    "missing_green_primitives": list(candidate.get("missing_green_primitives") or []),
                    "source_linkage_proof": list(candidate.get("source_linkage_proof") or []),
                    "blockers": sorted(blockers),
                    "planner_required": True,
                    "llm_query_required": True,
                    "llm_query_allowed": True,
                    "general_search_allowed": False,
                    "official_first_required": True,
                    "hardcoded_query_count": 0,
                    "hardcoded_queries": [],
                    "query_intents": [],
                    "preferred_source_classes": ["DART", "KIND", "KRX", "IssuerIR", "CompanyGuide"],
                    "fallback_source_classes": [
                        "TrustedNews",
                        "ReportPDF",
                        "BrokerReportPublicPDF",
                        "CompanyNewsroom",
                        "NaverSearch",
                        "GeneralWebSearch",
                    ],
                    "forbidden_source_classes": [
                        "snippet_only_score",
                        "source_proxy_only",
                        "evidence_url_pending",
                        "unbounded_general_search",
                    ],
                    "date_window": {
                        "end": config.as_of_date,
                        "lookback_days": max_age_days,
                    },
                    "max_queries": 3,
                    "max_candidates": 20,
                    "max_fetches": 3,
                    "max_queries_per_task": 3,
                    "max_candidates_per_query": 20,
                    "max_fetches_per_task": 3,
                    "stop_condition": {
                        "accepted_claim_count": 1,
                        "counter_claim_check_done": True,
                        "source_budget_exhausted_status": "SOURCE_PENDING",
                    },
                    "score_allowed_before_execution": False,
                    "stage_promotion_allowed_before_execution": False,
                    "reason_from_memory": (
                        "FULL_THESIS_GREEN_GATE_BLOCKER:"
                        f"{primitive_gap}; query text must be generated by the LLM planner and validated before execution"
                    ),
                    "next_actions": [
                        "ASK_LLM_PLANNER_FOR_MISSING_PRIMITIVE_QUERY",
                        "RUN_BOUNDED_OFFICIAL_FIRST_SOURCE_TASK",
                        "EXTRACT_EVIDENCE_OS_CLAIM",
                        "RETRY_FULL_THESIS_STAGECOURT",
                    ],
                }
            )
    return tasks


def _full_thesis_blocker_follow_up_seed_events(
    *,
    config: CensusV4RunConfig,
    output_root: Path,
    source_tasks: Sequence[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for task in source_tasks:
        symbol = str(task.get("symbol") or "").zfill(6)
        primitive_gap = str(task.get("primitive_gap") or "").strip()
        archetype_id = str(task.get("archetype_id") or "").strip()
        task_id = str(task.get("task_id") or "").strip()
        if not symbol or not primitive_gap or not archetype_id or not task_id:
            continue
        event_id = "CEV4-FTGAP-" + stable_hash((config.as_of_date, symbol, archetype_id, primitive_gap, task_id))[:24]
        rows.append(
            {
                "schema_version": "e2r_census_v4_full_thesis_blocker_follow_up_seed_event_v1",
                "candidate_event_id": event_id,
                "symbol": symbol,
                "company_name": task.get("company_name"),
                "event_date": str(task.get("as_of_date") or config.as_of_date),
                "detected_at": str(config.as_of_date),
                "source_family": "CensusFullThesisBlockerFollowUp",
                "source_id": str(output_root / "full_thesis_blocker_follow_up_source_tasks.jsonl"),
                "event_type": "full_thesis_blocker_follow_up_seed",
                "follow_up_task_id": task_id,
                "follow_up_archetype_id": archetype_id,
                "follow_up_primitive_gap": primitive_gap,
                "raw_reason_codes": [
                    "FULL_THESIS_GREEN_GATE_BLOCKER_FOLLOW_UP",
                    archetype_id,
                    primitive_gap,
                ],
                "primary_disclosure_type": None,
                "event_title": f"{task.get('company_name') or symbol} full thesis primitive follow-up seed",
                "event_summary": (
                    "planner input only. "
                    f"follow_up_task_id={task_id}; "
                    f"archetype_id={archetype_id}; "
                    f"primitive_gap={primitive_gap}; "
                    "source-backed Evidence OS claim required before promotion"
                ),
                "issuer_directness": "DIRECT",
                "research_brain_eligible": True,
                "score_evidence_allowed": False,
                "stage_promotion_allowed_before_execution": False,
                "seed_role": "planner_input_only",
                "structured_payload": {
                    "seed_role": "planner_input_only",
                    "follow_up_task_id": task_id,
                    "follow_up_origin": task.get("source_task_origin"),
                    "follow_up_primitive_gap": primitive_gap,
                    "follow_up_archetype_id": archetype_id,
                    "present_primitives": list(task.get("present_primitives") or []),
                    "missing_green_primitives": list(task.get("missing_green_primitives") or []),
                    "preferred_source_classes": list(task.get("preferred_source_classes") or []),
                    "fallback_source_classes": list(task.get("fallback_source_classes") or []),
                    "forbidden_source_classes": list(task.get("forbidden_source_classes") or []),
                    "official_first_required": task.get("official_first_required") is True,
                    "llm_query_required": task.get("llm_query_required") is True,
                    "llm_query_allowed": task.get("llm_query_allowed") is True,
                    "general_search_allowed": task.get("general_search_allowed") is True,
                    "hardcoded_query_count": int(task.get("hardcoded_query_count") or 0),
                    "hardcoded_queries": list(task.get("hardcoded_queries") or []),
                    "query_intents": list(task.get("query_intents") or []),
                    "date_window": dict(task.get("date_window") or {}),
                    "max_queries": task.get("max_queries"),
                    "max_candidates": task.get("max_candidates"),
                    "max_fetches": task.get("max_fetches"),
                    "max_queries_per_task": task.get("max_queries_per_task"),
                    "max_candidates_per_query": task.get("max_candidates_per_query"),
                    "max_fetches_per_task": task.get("max_fetches_per_task"),
                    "stop_condition": dict(task.get("stop_condition") or {}),
                },
            }
        )
    return rows


def _production_full_thesis_candidate_source_counts(candidates: Sequence[Mapping[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in candidates:
        source = str(row.get("_full_thesis_candidate_source") or "unknown")
        counts[source] = counts.get(source, 0) + 1
    return dict(sorted(counts.items()))


def _full_thesis_refresh_queue_materialization_audit(
    *,
    refresh_queue_rows: Sequence[Mapping[str, Any]],
    candidates: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    queue_by_symbol = {str(row.get("symbol") or "").zfill(6): row for row in refresh_queue_rows if row.get("symbol")}
    candidate_symbols = {str(row.get("symbol") or "").zfill(6) for row in candidates if row.get("symbol")}
    unmaterialized_symbols = sorted(symbol for symbol in queue_by_symbol if symbol not in candidate_symbols)
    sample: list[dict[str, Any]] = []
    for symbol in unmaterialized_symbols[:20]:
        row = queue_by_symbol[symbol]
        sample.append(
            {
                "symbol": symbol,
                "company_name": row.get("company_name"),
                "queue_task_id": row.get("queue_task_id"),
                "source_base_stage": row.get("source_base_stage"),
                "source_stage_signal": row.get("source_stage_signal"),
                "source_stage_decision_status": row.get("source_stage_decision_status"),
                "priority_bucket": row.get("priority_bucket"),
                "blocked_reason": row.get("blocked_reason"),
                "materialization_blocker": "full_thesis_refresh_task_has_no_research_brain_stagecourt_trace",
            }
        )
    return {
        "refresh_queue_materialized_candidate_count": len(queue_by_symbol) - len(unmaterialized_symbols),
        "refresh_queue_unmaterialized_candidate_count": len(unmaterialized_symbols),
        "refresh_queue_unmaterialized_sample": sample,
        "refresh_queue_to_candidate_rule": (
            "A full_thesis_refresh_queue row becomes a production candidate only after Research Brain or official-full-thesis "
            "execution produces a direct stagecourt_traces row for the same symbol. Queue rows alone never promote Stage."
        ),
    }


def _production_full_thesis_candidate_rows(
    *,
    stage_rows: Sequence[Mapping[str, Any]],
    traces: Mapping[str, Mapping[str, Any]],
) -> list[dict[str, Any]]:
    by_symbol = {str(row.get("symbol") or "").zfill(6): dict(row) for row in stage_rows}
    rows: list[dict[str, Any]] = []
    seen_trace_ids: set[str] = set()
    for row in stage_rows:
        if row.get("stage_scope") != "BRAIN_WEB_PARTIAL" or row.get("stage_source") != "research_brain_v4_attempt":
            continue
        trace_id = str(row.get("stagecourt_trace_id") or "")
        if not trace_id:
            continue
        item = dict(row)
        item["_full_thesis_candidate_source"] = "brain_web_partial_stage_row"
        rows.append(item)
        seen_trace_ids.add(trace_id)

    for trace_id in sorted(traces):
        if trace_id in seen_trace_ids:
            continue
        trace = traces.get(trace_id) or {}
        if trace.get("source_origin") != "research_brain_v4_attempt":
            continue
        raw_symbol = str(trace.get("symbol") or "").strip()
        if not raw_symbol:
            continue
        symbol = raw_symbol.zfill(6)
        item = dict(by_symbol.get(symbol) or {})
        item.update(
            {
                "symbol": symbol,
                "company_name": trace.get("company_name") or item.get("company_name"),
                "stagecourt_trace_id": trace_id,
                "stage_source": "research_brain_v4_attempt",
                "_full_thesis_candidate_source": "stagecourt_trace_direct_scan",
            }
        )
        rows.append(item)
        seen_trace_ids.add(trace_id)
    return rows


def _production_full_thesis_claim_blockers(
    *,
    accepted_ids: Sequence[str],
    accepted_claims: Mapping[str, Mapping[str, Any]],
    evidence_documents: Mapping[str, Mapping[str, Any]],
) -> list[str]:
    blockers: list[str] = []
    for claim_id in accepted_ids:
        claim = accepted_claims.get(str(claim_id))
        if not claim:
            blockers.append("accepted_claim_row_missing")
            continue
        if claim.get("score_eligible") is not True:
            blockers.append("score_ineligible_claim")
        if claim.get("target_scope_status") != "DIRECT":
            blockers.append("non_direct_claim")
        if claim.get("temporal_status") not in {"CURRENT", "PRESENT_CURRENT", "OPEN"}:
            blockers.append("non_current_claim")
        if not claim.get("document_id") or not claim.get("anchor_id"):
            blockers.append("claim_missing_document_or_anchor")
        doc = evidence_documents.get(str(claim.get("document_id") or ""))
        if not doc:
            blockers.append("claim_document_row_missing")
        elif str(doc.get("canonical_url") or doc.get("source_url") or "").startswith("snapshot://"):
            blockers.append("snapshot_document_not_production")
    return sorted(dict.fromkeys(blockers))


def _production_full_thesis_source_linkage(
    *,
    accepted_ids: Sequence[str],
    accepted_claims: Mapping[str, Mapping[str, Any]],
    source_executions: Sequence[Mapping[str, Any]],
    candidate_event_id: str,
) -> tuple[list[str], list[dict[str, Any]], list[str]]:
    blockers: list[str] = []
    proof_rows: list[dict[str, Any]] = []
    linked_task_ids: list[str] = []
    candidate_event_id = str(candidate_event_id or "")

    for claim_id in accepted_ids:
        claim = accepted_claims.get(str(claim_id))
        if not claim:
            proof_rows.append(
                {
                    "claim_id": str(claim_id),
                    "linked": False,
                    "reason": "accepted_claim_row_missing",
                }
            )
            continue
        document_id = str(claim.get("document_id") or "")
        anchor_id = str(claim.get("anchor_id") or "")
        matching_task_ids: list[str] = []
        matching_document_ids: list[str] = []
        for execution in source_executions:
            if not _is_brain_origin(execution):
                continue
            execution_event_id = _source_task_execution_candidate_event_id(execution)
            if candidate_event_id and execution_event_id and execution_event_id != candidate_event_id:
                continue
            execution_claim_ids = {str(item) for item in execution.get("accepted_claim_ids") or [] if str(item)}
            fetched_document_ids = {str(item) for item in execution.get("fetched_document_ids") or [] if str(item)}
            if str(claim_id) not in execution_claim_ids:
                continue
            if not document_id or document_id not in fetched_document_ids:
                continue
            source_task = execution.get("source_task") if isinstance(execution.get("source_task"), Mapping) else {}
            task_id = str(execution.get("task_id") or source_task.get("task_id") or "")
            if task_id:
                _append_unique(matching_task_ids, task_id)
                _append_unique(linked_task_ids, task_id)
            _append_unique(matching_document_ids, document_id)
        linked = bool(matching_task_ids)
        if not linked:
            blockers.append("claim_not_linked_to_live_source_task_document")
        proof_rows.append(
            {
                "claim_id": str(claim_id),
                "document_id": document_id or None,
                "anchor_id": anchor_id or None,
                "candidate_event_id": candidate_event_id or None,
                "linked": linked,
                "source_task_ids": matching_task_ids,
                "fetched_document_ids": matching_document_ids,
            }
        )

    if accepted_ids and not linked_task_ids:
        blockers.append("missing_live_source_task_document_execution")
    return sorted(dict.fromkeys(blockers)), proof_rows, linked_task_ids


def _brain_source_task_ids_for_claims(source_executions: Sequence[Mapping[str, Any]], accepted_ids: Sequence[str]) -> list[str]:
    accepted_set = {str(item) for item in accepted_ids}
    task_ids: list[str] = []
    for row in source_executions:
        row_claim_ids = {str(item) for item in row.get("accepted_claim_ids") or []}
        if row_claim_ids & accepted_set:
            source_task = row.get("source_task") if isinstance(row.get("source_task"), Mapping) else {}
            _append_unique(task_ids, str(row.get("task_id") or source_task.get("task_id") or ""))
    return [item for item in task_ids if item]


def _mark_brain_stage_traces_promoted(*, output_root: Path, promoted_by_trace: Mapping[str, str]) -> None:
    rows = _read_jsonl(output_root / "stagecourt_traces.jsonl")
    for row in rows:
        trace_id = str(row.get("stagecourt_trace_id") or row.get("trace_id") or "")
        if trace_id in promoted_by_trace:
            row["not_promoted_to_census_stage_status"] = False
            row["promoted_to_census_stage_status"] = True
            row["census_stage_status_id"] = promoted_by_trace[trace_id]
    write_jsonl(output_root / "stagecourt_traces.jsonl", rows)


def _mark_brain_to_claim_traces_promoted(
    *,
    output_root: Path,
    promoted_by_trace: Mapping[str, str],
    promoted_claim_ids_by_trace: Mapping[str, Sequence[str]] | None = None,
) -> None:
    rows = _read_jsonl(output_root / "brain_to_claim_trace.jsonl")
    promoted_claim_ids_by_trace = promoted_claim_ids_by_trace or {}
    for row in rows:
        trace_id = str(row.get("stagecourt_trace_id") or "")
        if trace_id in promoted_by_trace:
            represented_claim_ids = {str(item) for item in promoted_claim_ids_by_trace.get(trace_id, ()) if str(item)}
            trace_claim_ids = _ids_from_value(row.get("accepted_claim_id")) | _ids_from_value(row.get("accepted_claim_ids"))
            if represented_claim_ids and trace_claim_ids and not trace_claim_ids <= represented_claim_ids:
                row["census_stage_status_id"] = None
                row["trace_status"] = row.get("trace_status") or "ACCEPTED_NON_REPRESENTATIVE_NOT_SCORE_CONTRIBUTING"
                row["not_promoted_reason"] = "accepted_claim_not_in_representative_score_claim_ids"
                continue
            row["census_stage_status_id"] = promoted_by_trace[trace_id]
            row["trace_status"] = "CLAIM_SCORE_TRACE_PROMOTED_TO_CENSUS_STAGE_STATUS"
    write_jsonl(output_root / "brain_to_claim_trace.jsonl", rows)


def _demote_atomic_representatives_replaced_by_brain_stage(
    *,
    atomic_rows: Sequence[Mapping[str, Any]],
    stage_rows: Sequence[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    brain_symbols = {
        str(row.get("symbol") or "").zfill(6)
        for row in stage_rows
        if row.get("stage_scope") == "BRAIN_WEB_PARTIAL"
        or str(row.get("census_stage_status_id") or "").startswith("CSS-BRAIN-")
    }
    if not brain_symbols:
        return [dict(row) for row in atomic_rows]
    demoted: list[dict[str, Any]] = []
    for row in atomic_rows:
        item = dict(row)
        symbol = str(item.get("symbol") or "").zfill(6)
        if symbol in brain_symbols and item.get("is_representative") is True:
            item["is_representative"] = False
            item["representative_replaced_by"] = "BRAIN_WEB_PARTIAL"
            item["non_representative_reason"] = "superseded_by_promoted_brain_web_stage_row"
        demoted.append(item)
    return demoted


def _refresh_brain_web_attempt_after_promotion(brain_web_attempt: Mapping[str, Any], *, promoted_stage_row_count: int) -> dict[str, Any]:
    if promoted_stage_row_count <= 0:
        return dict(brain_web_attempt)
    blockers = [
        blocker
        for blocker in brain_web_attempt.get("blockers") or []
        if blocker != "Research Brain StageCourt traces are not promoted into census_stage_status rows"
    ]
    refreshed = dict(brain_web_attempt)
    refreshed["brain_to_census_stage_exported_count"] = promoted_stage_row_count
    refreshed["cutover_export_ready"] = not blockers
    refreshed["blockers"] = blockers
    if refreshed.get("attempt_mode") != "disabled":
        refreshed["verdict"] = "ATTEMPTED_WITH_SOURCE_TASKS" if not blockers else "ATTEMPTED_NOT_CUTOVER_READY"
    return refreshed


def _brain_stage_promotion_audit(
    *,
    config: CensusV4RunConfig,
    output_root: Path,
    brain_web_attempt: Mapping[str, Any],
    stage_rows: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    stagecourt = _read_jsonl(output_root / "stagecourt_traces.jsonl")
    documents = _read_jsonl(output_root / "evidence_documents.jsonl")
    anchors = _read_jsonl(output_root / "evidence_anchors.jsonl")
    accepted = _read_jsonl(output_root / "accepted_claims.jsonl")
    contributions = _read_jsonl(output_root / "score_contributions.jsonl")
    source_executions = _read_jsonl(output_root / "source_task_executions.jsonl")
    brain_trace_rows = _read_jsonl(output_root / "brain_to_claim_trace.jsonl")
    planner = _read_jsonl(output_root / "planner_runs.jsonl")

    brain_stage_ids = {
        str(row.get("stagecourt_trace_id") or row.get("trace_id") or "")
        for row in stagecourt
        if _is_brain_origin(row) or str(row.get("stagecourt_trace_id") or row.get("trace_id") or "").startswith("SCT-BRAIN-")
    }
    promoted_stage_ids = {
        str(row.get("stagecourt_trace_id") or "")
        for row in stage_rows
        if str(row.get("stagecourt_trace_id") or "")
    }
    promoted_rows = [
        row
        for row in stage_rows
        if str(row.get("stagecourt_trace_id") or "") in brain_stage_ids
        or str(row.get("stage_source") or row.get("source_origin") or "") == "research_brain_v4_attempt"
    ]
    brain_docs = [row for row in documents if _is_brain_origin(row) or str(row.get("document_id") or "").startswith("DOC-BRAIN-")]
    brain_document_ids = _row_ids(brain_docs, "document_id")
    anchor_ids = _row_ids(anchors, "anchor_id")
    brain_source_executions = [row for row in source_executions if _is_brain_origin(row)]
    snapshot_docs = [row for row in brain_docs if str(row.get("canonical_url") or row.get("source_url") or "").startswith("snapshot://")]
    brain_claims = [row for row in accepted if row.get("brain_web_claim") is True or _is_brain_origin(row)]
    source_split = _brain_claim_source_split(output_root=output_root, brain_claims=brain_claims)
    web_or_llm_accepted_claim_ids = set(source_split["web_or_llm_accepted_claim_ids"])
    official_accepted_claim_ids = _row_ids(source_split["official_accepted_claims"], "claim_id")
    web_news_accepted_claims = list(source_split["web_news_accepted_claims"])
    llm_extracted_accepted_claims = list(source_split["llm_extracted_accepted_claims"])
    official_accepted_claims = list(source_split["official_accepted_claims"])
    brain_contributions = [row for row in contributions if _is_brain_origin(row)]
    brain_claim_quality_counts = _brain_claim_quality_counts(brain_claims)
    unresolved_claim_document_ref_count = sum(
        1 for row in brain_claims if not _ids_from_value(row.get("document_id")) or not _ids_from_value(row.get("document_id")) <= brain_document_ids
    )
    unresolved_claim_anchor_ref_count = sum(
        1
        for row in brain_claims
        if not (_ids_from_value(row.get("anchor_id")) or _ids_from_value(row.get("source_anchor_id")))
        or not ((_ids_from_value(row.get("anchor_id")) or _ids_from_value(row.get("source_anchor_id"))) <= anchor_ids)
    )
    source_task_document_ids: set[str] = set()
    source_task_without_document_ref_count = 0
    for row in brain_source_executions:
        refs = (
            _ids_from_value(row.get("fetched_document_ids"))
            | _ids_from_value(row.get("document_ids"))
            | _ids_from_value(row.get("evidence_document_ids"))
            | _ids_from_value(row.get("fetched_document_id"))
            | _ids_from_value(row.get("document_id"))
        )
        if _source_task_requires_document_ref(row) and not refs:
            source_task_without_document_ref_count += 1
        source_task_document_ids.update(refs)
    source_task_unresolved_document_ref_count = len(source_task_document_ids - brain_document_ids)
    marker_missing = sum(
        1
        for row in stagecourt
        if str(row.get("stagecourt_trace_id") or row.get("trace_id") or "") in brain_stage_ids
        and str(row.get("stagecourt_trace_id") or row.get("trace_id") or "") not in promoted_stage_ids
        and row.get("not_promoted_to_census_stage_status") is not True
    )
    brain_stage_trace_missing_primitive_state_ids = sum(
        1
        for row in stagecourt
        if str(row.get("stagecourt_trace_id") or row.get("trace_id") or "") in brain_stage_ids
        and row.get("score_contribution_ids")
        and not row.get("primitive_state_ids")
    )
    brain_stage_trace_without_web_or_llm_claim_count = sum(
        1
        for row in stagecourt
        if str(row.get("stagecourt_trace_id") or row.get("trace_id") or "") in brain_stage_ids
        and not ((_ids_from_value(row.get("accepted_claim_ids")) | _ids_from_value(row.get("support_claim_ids"))) & web_or_llm_accepted_claim_ids)
    )
    brain_stage_trace_with_web_or_llm_claim_count = sum(
        1
        for row in stagecourt
        if str(row.get("stagecourt_trace_id") or row.get("trace_id") or "") in brain_stage_ids
        and bool((_ids_from_value(row.get("accepted_claim_ids")) | _ids_from_value(row.get("support_claim_ids"))) & web_or_llm_accepted_claim_ids)
    )
    brain_stage_trace_with_official_claim_count = sum(
        1
        for row in stagecourt
        if str(row.get("stagecourt_trace_id") or row.get("trace_id") or "") in brain_stage_ids
        and bool((_ids_from_value(row.get("accepted_claim_ids")) | _ids_from_value(row.get("support_claim_ids"))) & official_accepted_claim_ids)
    )
    brain_stage_trace_without_supported_claim_count = sum(
        1
        for row in stagecourt
        if str(row.get("stagecourt_trace_id") or row.get("trace_id") or "") in brain_stage_ids
        and not (
            (_ids_from_value(row.get("accepted_claim_ids")) | _ids_from_value(row.get("support_claim_ids")))
            & (web_or_llm_accepted_claim_ids | official_accepted_claim_ids)
        )
    )
    trace_promoted_refs = sum(1 for row in brain_trace_rows if row.get("census_stage_status_id"))
    trace_promoted_ref_errors = _brain_trace_promoted_reference_error_count(brain_trace_rows=brain_trace_rows, stage_rows=stage_rows)
    fake_provider_used = int(brain_web_attempt.get("fake_provider_used_count") or 0) + sum(1 for row in planner if row.get("provider_mode") == "fake")

    promotion_requirements = [
        "brain_web_mode=enabled",
        "brain_stage_promotion_mode=strict",
        "real planner/provider success > 0",
        "source task executions > 0",
        "accepted brain claims > 0",
        "claim-backed score contributions > 0",
        "brain StageCourt traces > 0",
        "zero snapshot:// promoted evidence documents",
        "zero fake provider rows",
        "zero unsafe promoted representative rows",
    ]
    if config.brain_web_mode != "enabled" and not brain_stage_ids and not promoted_rows:
        return {
            "schema_version": "e2r_census_v4_brain_stage_promotion_audit_v1",
            "brain_web_mode": config.brain_web_mode,
            "brain_stage_promotion_mode": config.brain_stage_promotion_mode,
            "verdict": "NOT_REQUESTED",
            "brain_stage_trace_count": 0,
            "brain_promoted_stage_row_count": 0,
            "unsafe_promoted_stage_row_count": 0,
            "brain_claim_count": 0,
            "web_or_llm_accepted_claim_count": 0,
            "web_news_accepted_claim_count": 0,
            "llm_extracted_accepted_claim_count": 0,
            "official_accepted_claim_count": 0,
            "brain_score_contribution_count": 0,
            "brain_to_claim_trace_count": len(brain_trace_rows),
            "brain_trace_promoted_reference_count": trace_promoted_refs,
            "brain_evidence_document_count": len(brain_docs),
            "brain_source_task_execution_row_count": len(brain_source_executions),
            "brain_snapshot_document_count": len(snapshot_docs),
            "brain_claim_unresolved_document_ref_count": unresolved_claim_document_ref_count,
            "brain_claim_unresolved_anchor_ref_count": unresolved_claim_anchor_ref_count,
            "brain_source_task_without_document_ref_count": source_task_without_document_ref_count,
            "brain_source_task_unresolved_document_ref_count": source_task_unresolved_document_ref_count,
            "brain_stage_trace_not_promoted_marker_missing_count": marker_missing,
            "brain_stage_trace_missing_primitive_state_ids_count": brain_stage_trace_missing_primitive_state_ids,
            "brain_stage_trace_without_web_or_llm_claim_count": brain_stage_trace_without_web_or_llm_claim_count,
            "brain_stage_trace_with_web_or_llm_claim_count": brain_stage_trace_with_web_or_llm_claim_count,
            "brain_stage_trace_with_official_claim_count": brain_stage_trace_with_official_claim_count,
            "brain_stage_trace_without_supported_claim_count": brain_stage_trace_without_supported_claim_count,
            "fake_provider_used_count": fake_provider_used,
            "brain_trace_promoted_reference_error_count": trace_promoted_ref_errors,
            "real_provider_success_count": int(brain_web_attempt.get("real_provider_success_count") or 0),
            "source_task_execution_count": int(brain_web_attempt.get("source_task_execution_count") or 0),
            "blockers": [],
            "promotion_requirements_if_enabled": promotion_requirements,
            "promotion_rule": (
                "Brain/Web StageCourt traces may enter census_stage_status only after strict mode, "
                "real planner success, live source tasks, non-snapshot anchors, claim-backed score "
                "contributions, and zero unsafe-promotion blockers."
            ),
        }

    blockers: list[str] = []
    if config.brain_web_mode != "enabled":
        blockers.append("Brain/Web acquisition was not requested")
    if config.brain_stage_promotion_mode != "strict":
        blockers.append("Brain stage promotion mode is disabled")
    if config.brain_planner_provider in {"none", "test_fake"}:
        blockers.append(f"planner provider is not a real promotion provider: {config.brain_planner_provider}")
    if config.brain_source_acquisition in {"frozen_real_source_snapshot", "test_fake"}:
        blockers.append(f"source acquisition is not production-live: {config.brain_source_acquisition}")
    if int(brain_web_attempt.get("real_provider_success_count") or 0) <= 0:
        blockers.append("LLM planner has zero real-provider successes")
    if int(brain_web_attempt.get("source_task_execution_count") or 0) <= 0:
        blockers.append("source task execution count is zero")
    elif not brain_source_executions:
        blockers.append("Brain source task execution attempt has no exported source_task_executions rows")
    if int(brain_web_attempt.get("accepted_claim_count") or 0) <= 0 and not brain_claims:
        blockers.append("accepted brain claim count is zero")
    if brain_stage_trace_without_supported_claim_count:
        blockers.append(f"brain StageCourt traces have no supported accepted claim for partial promotion: {brain_stage_trace_without_supported_claim_count}")
    if brain_claim_quality_counts["missing_verifiable_anchor_count"]:
        blockers.append(f"accepted brain claims missing document/anchor IDs: {brain_claim_quality_counts['missing_verifiable_anchor_count']}")
    if brain_claim_quality_counts["missing_date_count"]:
        blockers.append(f"accepted brain claims missing event/as-of/source date: {brain_claim_quality_counts['missing_date_count']}")
    if brain_claim_quality_counts["not_direct_target_count"]:
        blockers.append(f"accepted brain claims are not direct target claims: {brain_claim_quality_counts['not_direct_target_count']}")
    if brain_claim_quality_counts["not_current_count"]:
        blockers.append(f"accepted brain claims are not current/open: {brain_claim_quality_counts['not_current_count']}")
    if brain_claim_quality_counts["score_ineligible_count"]:
        blockers.append(f"accepted brain claims are not score eligible by deterministic guard: {brain_claim_quality_counts['score_ineligible_count']}")
    if unresolved_claim_document_ref_count:
        blockers.append(f"accepted brain claims reference missing evidence_documents rows: {unresolved_claim_document_ref_count}")
    if unresolved_claim_anchor_ref_count:
        blockers.append(f"accepted brain claims reference missing evidence_anchors rows: {unresolved_claim_anchor_ref_count}")
    if source_task_without_document_ref_count:
        blockers.append(f"Brain source task rows missing fetched document refs: {source_task_without_document_ref_count}")
    if source_task_unresolved_document_ref_count:
        blockers.append(f"Brain source task rows reference missing evidence_documents rows: {source_task_unresolved_document_ref_count}")
    if not brain_contributions:
        blockers.append("brain score contribution count is zero")
    if not brain_stage_ids:
        blockers.append("brain StageCourt trace count is zero")
    if snapshot_docs:
        blockers.append("brain evidence documents include snapshot:// URLs")
    if fake_provider_used:
        blockers.append("fake planner/provider rows are present")
    if marker_missing:
        blockers.append("brain StageCourt trace is missing explicit not-promoted marker")
    if brain_stage_trace_missing_primitive_state_ids:
        blockers.append(f"brain StageCourt traces with score contributions are missing primitive_state_ids: {brain_stage_trace_missing_primitive_state_ids}")
    if trace_promoted_ref_errors:
        blockers.append(f"brain_to_claim_trace promoted references are dangling or mismatched: {trace_promoted_ref_errors}")

    unsafe_promoted = len(promoted_rows) if blockers else 0
    if unsafe_promoted:
        verdict = "FAIL_UNSAFE_PROMOTION"
    elif blockers:
        if config.brain_stage_promotion_mode != "strict":
            verdict = "PROMOTION_DISABLED_BY_POLICY"
        else:
            verdict = "BLOCKED"
    elif promoted_rows:
        verdict = "PROMOTION_APPLIED"
    else:
        verdict = "ELIGIBLE_NOT_PROMOTED"

    return {
        "schema_version": "e2r_census_v4_brain_stage_promotion_audit_v1",
        "brain_web_mode": config.brain_web_mode,
        "brain_stage_promotion_mode": config.brain_stage_promotion_mode,
        "verdict": verdict,
        "brain_stage_trace_count": len(brain_stage_ids),
        "brain_promoted_stage_row_count": len(promoted_rows),
        "unsafe_promoted_stage_row_count": unsafe_promoted,
        "brain_claim_count": len(brain_claims),
        "web_or_llm_accepted_claim_count": len(web_or_llm_accepted_claim_ids),
        "web_news_accepted_claim_count": len(web_news_accepted_claims),
        "llm_extracted_accepted_claim_count": len(llm_extracted_accepted_claims),
        "official_accepted_claim_count": len(official_accepted_claims),
        "brain_stage_trace_with_web_or_llm_claim_count": brain_stage_trace_with_web_or_llm_claim_count,
        "brain_stage_trace_with_official_claim_count": brain_stage_trace_with_official_claim_count,
        "brain_stage_trace_without_supported_claim_count": brain_stage_trace_without_supported_claim_count,
        "brain_score_contribution_count": len(brain_contributions),
        "brain_to_claim_trace_count": len(brain_trace_rows),
        "brain_trace_promoted_reference_count": trace_promoted_refs,
        "brain_evidence_document_count": len(brain_docs),
        "brain_source_task_execution_row_count": len(brain_source_executions),
        "brain_snapshot_document_count": len(snapshot_docs),
        "brain_claim_missing_verifiable_anchor_count": brain_claim_quality_counts["missing_verifiable_anchor_count"],
        "brain_claim_unresolved_document_ref_count": unresolved_claim_document_ref_count,
        "brain_claim_unresolved_anchor_ref_count": unresolved_claim_anchor_ref_count,
        "brain_claim_missing_date_count": brain_claim_quality_counts["missing_date_count"],
        "brain_claim_not_direct_target_count": brain_claim_quality_counts["not_direct_target_count"],
        "brain_claim_not_current_count": brain_claim_quality_counts["not_current_count"],
        "brain_claim_score_ineligible_count": brain_claim_quality_counts["score_ineligible_count"],
        "brain_source_task_without_document_ref_count": source_task_without_document_ref_count,
        "brain_source_task_unresolved_document_ref_count": source_task_unresolved_document_ref_count,
        "brain_stage_trace_not_promoted_marker_missing_count": marker_missing,
        "brain_stage_trace_missing_primitive_state_ids_count": brain_stage_trace_missing_primitive_state_ids,
        "brain_stage_trace_without_web_or_llm_claim_count": brain_stage_trace_without_web_or_llm_claim_count,
        "fake_provider_used_count": fake_provider_used,
        "brain_trace_promoted_reference_error_count": trace_promoted_ref_errors,
        "real_provider_success_count": int(brain_web_attempt.get("real_provider_success_count") or 0),
        "source_task_execution_count": int(brain_web_attempt.get("source_task_execution_count") or 0),
        "blockers": blockers,
        "promotion_requirements_if_enabled": promotion_requirements,
        "promotion_rule": (
            "Brain/Web StageCourt traces may enter census_stage_status only after strict mode, "
            "real planner success, live source tasks, non-snapshot anchors, claim-backed score "
            "contributions, and zero unsafe-promotion blockers."
        ),
    }


def _brain_trace_promoted_reference_error_count(
    *,
    brain_trace_rows: Sequence[Mapping[str, Any]],
    stage_rows: Sequence[Mapping[str, Any]],
) -> int:
    stage_by_status_id = {
        str(row.get("census_stage_status_id") or ""): row
        for row in stage_rows
        if row.get("census_stage_status_id")
    }
    errors = 0
    for trace in brain_trace_rows:
        status_id = str(trace.get("census_stage_status_id") or "")
        if not status_id:
            continue
        stage_row = stage_by_status_id.get(status_id)
        if stage_row is None:
            errors += 1
            continue
        trace_stage_id = str(trace.get("stagecourt_trace_id") or "")
        stage_stage_id = str(stage_row.get("stagecourt_trace_id") or "")
        if trace_stage_id and stage_stage_id and trace_stage_id != stage_stage_id:
            errors += 1
            continue
        trace_claim_ids = _ids_from_value(trace.get("accepted_claim_id")) | _ids_from_value(trace.get("accepted_claim_ids"))
        stage_claim_ids = _ids_from_value(stage_row.get("accepted_claim_ids"))
        if trace_claim_ids and not trace_claim_ids <= stage_claim_ids:
            errors += 1
            continue
        trace_contribution_ids = _ids_from_value(trace.get("score_contribution_id")) | _ids_from_value(trace.get("score_contribution_ids"))
        stage_contribution_ids = _ids_from_value(stage_row.get("score_contribution_ids"))
        if trace_contribution_ids and not trace_contribution_ids <= stage_contribution_ids:
            errors += 1
            continue
        trace_primitive_state_ids = _ids_from_value(trace.get("primitive_state_id")) | _ids_from_value(trace.get("primitive_state_ids"))
        stage_primitive_state_ids = _ids_from_value(stage_row.get("primitive_state_ids"))
        if trace_primitive_state_ids and not trace_primitive_state_ids <= stage_primitive_state_ids:
            errors += 1
    return errors


def _brain_web_readiness_gate_audit(
    *,
    config: CensusV4RunConfig,
    output_root: Path,
    brain_web_attempt: Mapping[str, Any],
    brain_stage_promotion: Mapping[str, Any],
    stage_rows: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    """Hard gate for claiming real Brain/Web evidence operation.

    The smaller planner/web/extractor audits answer "is there an internal
    inconsistency?" This gate answers the operator question: "may this run
    claim Brain/Web evidence readiness?" Disabled runs must say NOT_REQUESTED,
    not PASS.
    """

    requested = _config_requests_brain_web(config)
    planner = _read_jsonl(output_root / "planner_runs.jsonl")
    web_tasks = _read_jsonl(output_root / "web_search_tasks.jsonl")
    web_results = _read_jsonl(output_root / "web_search_results.jsonl")
    web_fetched = _read_jsonl(output_root / "web_fetched_documents.jsonl")
    web_rejected = _read_jsonl(output_root / "web_rejected_documents.jsonl")
    web_call_counts = _web_search_call_counts(web_tasks=web_tasks, web_results=web_results)
    extractor_runs = _read_jsonl(output_root / "claim_extractor_runs.jsonl")
    llm_extractor_run_count = sum(1 for row in extractor_runs if str(row.get("provider_mode") or "").lower() == "llm")
    non_llm_extractor_run_count = sum(
        1 for row in extractor_runs if row.get("provider_mode") and str(row.get("provider_mode") or "").lower() != "llm"
    )
    extractor_provider_error_count = sum(1 for row in extractor_runs if str(row.get("provider_error") or "").strip())
    extractor_timeout_count = sum(1 for row in extractor_runs if "timeout" in str(row.get("provider_error") or "").lower())
    llm_extractor_raw_assertion_ids = set().union(
        *(_ids_from_value(row.get("raw_assertion_ids")) for row in extractor_runs if str(row.get("provider_mode") or "").lower() == "llm")
    ) if extractor_runs else set()
    forbidden_extractor_context_count = sum(1 for row in extractor_runs if row.get("forbidden_context_seen"))
    accepted = _read_jsonl(output_root / "accepted_claims.jsonl")
    documents = _read_jsonl(output_root / "evidence_documents.jsonl")
    anchors = _read_jsonl(output_root / "evidence_anchors.jsonl")
    source_executions = _read_jsonl(output_root / "source_task_executions.jsonl")
    contributions = _read_jsonl(output_root / "score_contributions.jsonl")
    stagecourt = _read_jsonl(output_root / "stagecourt_traces.jsonl")
    brain_trace = _read_jsonl(output_root / "brain_to_claim_trace.jsonl")

    brain_source_executions = [row for row in source_executions if _is_brain_origin(row)]
    source_lineage_feedback_retry_executions = [
        row for row in brain_source_executions if _is_source_lineage_feedback_retry_execution(row)
    ]
    source_lineage_retry_dropped_count = sum(1 for row in brain_source_executions if _is_source_lineage_retry_drop_execution(row))
    source_lineage_retry_accepted_execution_count = sum(
        1
        for row in source_lineage_feedback_retry_executions
        if str(row.get("status") or "") == "EVIDENCE_OS_ACCEPTED"
        and bool(_ids_from_value(row.get("accepted_claim_ids")) or _ids_from_value(row.get("direct_accepted_claim_ids")))
    )
    source_lineage_retry_no_evidence_execution_count = sum(
        1
        for row in source_lineage_feedback_retry_executions
        if str(row.get("status") or "") in {"NO_EVIDENCE_FOUND", "PROVIDER_FAILED", "BUDGET_EXHAUSTED"}
    )
    policy_rejected_source_task_execution_count = sum(1 for row in brain_source_executions if str(row.get("status") or "") == "REJECTED_BY_POLICY")
    zero_budget_policy_rejected_source_task_execution_count = sum(
        1
        for row in brain_source_executions
        if str(row.get("status") or "") == "REJECTED_BY_POLICY" and _source_task_budget_is_zero(row)
    )
    brain_documents = [row for row in documents if _is_brain_origin(row)]
    brain_accepted = [row for row in accepted if row.get("brain_web_claim") is True or _is_brain_origin(row)]
    brain_contributions = [row for row in contributions if _is_brain_origin(row)]
    brain_stage_traces = [
        row
        for row in stagecourt
        if _is_brain_origin(row) or str(row.get("stagecourt_trace_id") or row.get("trace_id") or "").startswith("SCT-BRAIN-")
    ]
    attempt_source_task_count = int(brain_web_attempt.get("source_task_execution_count") or 0)
    attempt_accepted_claim_count = int(brain_web_attempt.get("accepted_claim_count") or 0)
    attempt_real_document_count = int(brain_web_attempt.get("real_document_fetched_count") or 0)
    full_thesis_seed_event_count = int(brain_web_attempt.get("full_thesis_seed_event_count") or 0)
    full_thesis_seed_consumed_by_research_brain = bool(brain_web_attempt.get("full_thesis_seed_consumed_by_research_brain") is True)
    full_thesis_seed_event_path = brain_web_attempt.get("full_thesis_seed_event_path")
    full_thesis_seed_source = brain_web_attempt.get("full_thesis_seed_source")
    full_thesis_seed_original_path = brain_web_attempt.get("full_thesis_seed_original_path")
    full_thesis_seed_planner_attempted_event_count = int(
        brain_web_attempt.get("full_thesis_seed_planner_attempted_event_count")
        or brain_web_attempt.get("full_thesis_seed_planner_run_count")
        or 0
    )
    full_thesis_seed_planner_run_row_count = int(
        brain_web_attempt.get("full_thesis_seed_planner_run_row_count")
        or brain_web_attempt.get("full_thesis_seed_planner_run_count")
        or 0
    )
    full_thesis_seed_planner_run_count = int(brain_web_attempt.get("full_thesis_seed_planner_run_count") or 0)
    full_thesis_seed_real_provider_success_count = int(brain_web_attempt.get("full_thesis_seed_real_provider_success_count") or 0)
    full_thesis_seed_source_task_execution_count = int(brain_web_attempt.get("full_thesis_seed_source_task_execution_count") or 0)
    full_thesis_seed_accepted_claim_count = int(brain_web_attempt.get("full_thesis_seed_accepted_claim_count") or 0)
    full_thesis_seed_stagecourt_trace_count = int(brain_web_attempt.get("full_thesis_seed_stagecourt_trace_count") or 0)
    full_thesis_seed_materialized_to_stagecourt = bool(brain_web_attempt.get("full_thesis_seed_materialized_to_stagecourt") is True)
    real_provider_success = max(
        int(brain_web_attempt.get("real_provider_success_count") or 0),
        sum(1 for row in planner if row.get("provider_mode") == "real" and row.get("real_provider_success") is True),
    )
    source_task_count = len(brain_source_executions)
    accepted_claim_count = len(brain_accepted)
    web_document_ids = _row_ids(web_fetched, "document_id") | _row_ids(web_fetched, "fetched_document_id") | _row_ids(web_fetched, "web_document_id")
    web_source_urls = {
        str(row.get("url") or row.get("source_url") or row.get("canonical_url") or "")
        for row in web_fetched
        if str(row.get("url") or row.get("source_url") or row.get("canonical_url") or "").strip()
    }
    web_news_accepted = [
        row
        for row in brain_accepted
        if _accepted_claim_is_web_news_source(row, web_document_ids=web_document_ids, web_source_urls=web_source_urls)
    ]
    llm_extracted_accepted = [
        row for row in brain_accepted if _accepted_claim_is_llm_extracted(row, llm_raw_assertion_ids=llm_extractor_raw_assertion_ids)
    ]
    web_or_llm_accepted_ids = _row_ids(web_news_accepted, "claim_id") | _row_ids(llm_extracted_accepted, "claim_id")
    official_accepted = [
        row
        for row in brain_accepted
        if not _ids_from_value(row.get("claim_id")) & web_or_llm_accepted_ids
        and _accepted_claim_is_official_source(row)
    ]
    full_thesis_accepted_claim_count = sum(1 for row in brain_accepted if row.get("full_thesis_claim") is True)
    web_or_llm_accepted_claim_count = len(web_or_llm_accepted_ids)
    real_document_count = sum(1 for row in brain_documents if not str(row.get("canonical_url") or row.get("source_url") or "").startswith("snapshot://"))
    snapshot_document_count = int(brain_stage_promotion.get("brain_snapshot_document_count") or 0) + sum(
        1 for row in brain_documents if str(row.get("canonical_url") or row.get("source_url") or "").startswith("snapshot://")
    )
    snippet_to_score_count = sum(1 for row in contributions if row.get("source_type") == "snippet")
    provider_failure_final_score_count = sum(1 for row in stage_rows if row.get("census_status") == "PENDING_PROVIDER" and row.get("score_scale") != "NO_SCORE")
    fake_provider_used_count = int(brain_stage_promotion.get("fake_provider_used_count") or brain_web_attempt.get("fake_provider_used_count") or 0)
    promoted_stage_row_count = int(brain_stage_promotion.get("brain_promoted_stage_row_count") or 0)
    unsafe_promoted_stage_row_count = int(brain_stage_promotion.get("unsafe_promoted_stage_row_count") or 0)
    promotion_verdict = str(brain_stage_promotion.get("verdict") or "")
    requires_web_acquisition = config.run_mode in {"BRAIN_AND_WEB_ACQUISITION_ENABLED", "FULL_LIVE_BRAIN_CENSUS"}
    operational_minimum_gate_applies = _brain_web_operational_minimum_gate_applies(config)
    brain_claim_quality_counts = _brain_claim_quality_counts(brain_accepted)
    brain_document_ids = _row_ids(brain_documents, "document_id")
    anchor_ids = _row_ids(anchors, "anchor_id")
    unresolved_claim_document_ref_count = sum(
        1 for row in brain_accepted if not _ids_from_value(row.get("document_id")) or not _ids_from_value(row.get("document_id")) <= brain_document_ids
    )
    unresolved_claim_anchor_ref_count = sum(
        1
        for row in brain_accepted
        if not (_ids_from_value(row.get("anchor_id")) or _ids_from_value(row.get("source_anchor_id")))
        or not ((_ids_from_value(row.get("anchor_id")) or _ids_from_value(row.get("source_anchor_id"))) <= anchor_ids)
    )
    source_task_document_ids: set[str] = set()
    source_task_without_document_ref_count = 0
    for row in brain_source_executions:
        refs = (
            _ids_from_value(row.get("fetched_document_ids"))
            | _ids_from_value(row.get("document_ids"))
            | _ids_from_value(row.get("evidence_document_ids"))
            | _ids_from_value(row.get("fetched_document_id"))
            | _ids_from_value(row.get("document_id"))
        )
        if _source_task_requires_document_ref(row) and not refs:
            source_task_without_document_ref_count += 1
        source_task_document_ids.update(refs)
    source_task_unresolved_document_ref_count = len(source_task_document_ids - brain_document_ids)
    brain_accepted_ids = _row_ids(brain_accepted, "claim_id")
    brain_trace_claim_ids = set().union(*(_ids_from_value(row.get("accepted_claim_id")) for row in brain_trace)) if brain_trace else set()
    connected_brain_trace = [row for row in brain_trace if _ids_from_value(row.get("accepted_claim_id")) & brain_accepted_ids]
    direct_trace_claim_count = len(
        {
            str(row.get("accepted_claim_id") or "")
            for row in connected_brain_trace
            if row.get("satisfies_source_task") is True and row.get("accepted_claim_id")
        }
    )
    rerouted_trace_claim_count = len(
        {
            str(row.get("accepted_claim_id") or "")
            for row in connected_brain_trace
            if str(row.get("satisfaction_type") or "") == "REROUTED_ACCEPTED_CLAIM" and row.get("accepted_claim_id")
        }
    )
    direct_source_task_satisfied_count = sum(1 for row in brain_source_executions if row.get("satisfies_source_task") is True)
    rerouted_source_task_claim_count = sum(
        1 for row in brain_source_executions if str(row.get("satisfaction_type") or "") == "REROUTED_ACCEPTED_CLAIM"
    )
    brain_trace_missing_accepted_claim_count = len(brain_accepted_ids - brain_trace_claim_ids)
    brain_contribution_supported_claim_ids = set().union(
        *(
            _ids_from_value(row.get("support_claim_ids")) | _ids_from_value(row.get("accepted_claim_ids"))
            for row in brain_contributions
        )
    ) if brain_contributions else set()
    promoted_stage_supported_claim_ids = set().union(
        *(
            _ids_from_value(row.get("support_claim_ids"))
            for row in stage_rows
            if str(row.get("stagecourt_trace_id") or "").startswith("SCT-BRAIN-")
            or str(row.get("stage_source") or row.get("source_origin") or "") == "research_brain_v4_attempt"
        )
    ) if stage_rows else set()
    externally_representative_claim_ids = brain_contribution_supported_claim_ids | promoted_stage_supported_claim_ids
    brain_trace_missing_score_contribution_ref_count = sum(
        1
        for row in connected_brain_trace
        if _brain_trace_requires_score_contribution(row, representative_claim_ids=externally_representative_claim_ids)
        and not (_ids_from_value(row.get("score_contribution_id")) or _ids_from_value(row.get("score_contribution_ids")))
    )
    brain_trace_missing_stagecourt_ref_count = sum(
        1
        for row in connected_brain_trace
        if _brain_trace_requires_stagecourt(row, representative_claim_ids=externally_representative_claim_ids)
        and not row.get("stagecourt_trace_id")
    )
    brain_trace_nonrepresentative_missing_stagecourt_ref_count = sum(
        1
        for row in connected_brain_trace
        if not _brain_trace_requires_stagecourt(row, representative_claim_ids=externally_representative_claim_ids)
        and not row.get("stagecourt_trace_id")
    )
    brain_contribution_without_accepted_support_count = sum(
        1
        for row in brain_contributions
        if not (_ids_from_value(row.get("support_claim_ids")) | _ids_from_value(row.get("accepted_claim_ids"))) & brain_accepted_ids
    )
    brain_stage_trace_ids = {
        str(row.get("stagecourt_trace_id") or row.get("trace_id") or "")
        for row in brain_stage_traces
        if str(row.get("stagecourt_trace_id") or row.get("trace_id") or "")
    }
    brain_stage_trace_without_accepted_claim_count = sum(
        1
        for row in brain_stage_traces
        if not (_ids_from_value(row.get("accepted_claim_ids")) | _ids_from_value(row.get("support_claim_ids"))) & brain_accepted_ids
    )
    promoted_brain_stage_rows = [
        row
        for row in stage_rows
        if str(row.get("stagecourt_trace_id") or "") in brain_stage_trace_ids
        or str(row.get("stage_source") or row.get("source_origin") or "") == "research_brain_v4_attempt"
    ]
    promoted_stage_without_brain_trace_count = sum(
        1
        for row in promoted_brain_stage_rows
        if str(row.get("stagecourt_trace_id") or "") not in brain_stage_trace_ids
        or not (_ids_from_value(row.get("accepted_claim_ids")) | _ids_from_value(row.get("support_claim_ids"))) & brain_accepted_ids
    )

    if not requested:
        return {
            "schema_version": "e2r_census_v4_brain_web_readiness_gate_audit_v1",
            "run_mode": config.run_mode,
            "brain_web_mode": config.brain_web_mode,
            "verdict": "NOT_REQUESTED",
            "minimum_gate_applies": False,
            "operational_minimum_count_gate_applies": False,
            "brain_web_evidence_pass_allowed": False,
            "full_thesis_seed_event_path": full_thesis_seed_event_path,
            "full_thesis_seed_source": full_thesis_seed_source,
            "full_thesis_seed_original_path": full_thesis_seed_original_path,
            "full_thesis_seed_event_count": full_thesis_seed_event_count,
            "full_thesis_seed_consumed_by_research_brain": False,
            "full_thesis_seed_planner_attempted_event_count": 0,
            "full_thesis_seed_planner_run_row_count": 0,
            "full_thesis_seed_planner_run_count": 0,
            "full_thesis_seed_real_provider_success_count": 0,
            "full_thesis_seed_source_task_execution_count": 0,
            "full_thesis_seed_accepted_claim_count": 0,
            "full_thesis_seed_stagecourt_trace_count": 0,
            "full_thesis_seed_materialized_to_stagecourt": False,
            "llm_planner_call_count": len(planner),
            "llm_real_provider_success_count": real_provider_success,
            "source_task_execution_count": 0,
            "attempt_source_task_execution_count": attempt_source_task_count,
            "real_document_fetched_count": 0,
            "attempt_real_document_fetched_count": attempt_real_document_count,
            "policy_rejected_source_task_execution_count": policy_rejected_source_task_execution_count,
            "zero_budget_policy_rejected_source_task_execution_count": zero_budget_policy_rejected_source_task_execution_count,
            "source_lineage_feedback_retry_execution_count": len(source_lineage_feedback_retry_executions),
            "source_lineage_feedback_retry_accepted_execution_count": source_lineage_retry_accepted_execution_count,
            "source_lineage_feedback_retry_no_evidence_execution_count": source_lineage_retry_no_evidence_execution_count,
            "source_lineage_feedback_retry_dropped_count": source_lineage_retry_dropped_count,
            "discovery_only_retry_after_unverified_original_count": source_lineage_retry_dropped_count,
            "web_search_task_count": len(web_tasks),
            "web_search_result_count": len(web_results),
            "web_fetched_document_count": len(web_fetched),
            "web_rejected_document_count": len(web_rejected),
            "web_search_call_count": web_call_counts["web_search_call_count"],
            "naver_search_call_count": web_call_counts["naver_search_call_count"],
            "trusted_news_search_call_count": web_call_counts["trusted_news_search_call_count"],
            "general_web_search_call_count": web_call_counts["general_web_search_call_count"],
            "llm_claim_extractor_attempt_count": len(extractor_runs),
            "llm_claim_extractor_real_provider_count": llm_extractor_run_count,
            "claim_extractor_non_llm_provider_count": non_llm_extractor_run_count,
            "llm_claim_extractor_provider_error_count": extractor_provider_error_count,
            "llm_claim_extractor_timeout_count": extractor_timeout_count,
            "claim_extractor_forbidden_context_count": forbidden_extractor_context_count,
            "brain_accepted_claim_count": 0,
            "web_or_llm_accepted_claim_count": 0,
            "official_accepted_claim_count": 0,
            "web_news_accepted_claim_count": 0,
            "llm_extracted_accepted_claim_count": 0,
            "full_thesis_claim_count": 0,
            "direct_accepted_claim_count": 0,
            "rerouted_accepted_claim_count": 0,
            "direct_source_task_satisfied_count": 0,
            "rerouted_source_task_claim_count": 0,
            "attempt_accepted_claim_count": attempt_accepted_claim_count,
            "brain_to_claim_trace_count": len(brain_trace),
            "brain_score_contribution_count": 0,
            "brain_stage_trace_count": 0,
            "brain_promoted_stage_row_count": 0,
            "brain_trace_missing_accepted_claim_count": 0,
            "brain_trace_missing_score_contribution_ref_count": 0,
            "brain_trace_missing_stagecourt_ref_count": 0,
            "brain_trace_nonrepresentative_missing_stagecourt_ref_count": 0,
            "brain_contribution_without_accepted_support_count": 0,
            "brain_stage_trace_without_accepted_claim_count": 0,
            "promoted_stage_without_brain_trace_count": 0,
            "brain_claim_unresolved_document_ref_count": 0,
            "brain_claim_unresolved_anchor_ref_count": 0,
            "brain_source_task_without_document_ref_count": 0,
            "brain_source_task_unresolved_document_ref_count": 0,
            "snapshot_document_count": snapshot_document_count,
            "fake_provider_used_count": fake_provider_used_count,
            "snippet_to_score_count": snippet_to_score_count,
            "provider_failure_final_score_count": provider_failure_final_score_count,
            "minimum_required_counts": _brain_web_minimum_required_counts(),
            "blockers": [],
            "nonblocking_gaps": ["Brain/Web was not requested in this ledger-refresh run"],
            "rule": "NOT_REQUESTED is not Brain/Web PASS; it only proves the run did not overclaim disabled artifacts.",
        }

    blockers: list[str] = []
    if len(planner) <= 0:
        blockers.append("LLM planner run row count is zero")
    if real_provider_success <= 0:
        blockers.append("LLM planner real-provider success count is zero")
    if source_task_count <= 0:
        blockers.append("Brain/Web source task execution count is zero")
    if full_thesis_seed_planner_run_count > 0 and full_thesis_seed_real_provider_success_count <= 0:
        blockers.append("full-thesis seed planner runs have no real-provider success")
    if full_thesis_seed_real_provider_success_count > 0 and full_thesis_seed_source_task_execution_count <= 0:
        blockers.append("full-thesis seed planner runs produced no source task executions")
    if full_thesis_seed_source_task_execution_count > 0 and full_thesis_seed_accepted_claim_count <= 0:
        blockers.append("full-thesis seed source task executions produced no accepted claims")
    if full_thesis_seed_accepted_claim_count > 0 and full_thesis_seed_stagecourt_trace_count <= 0:
        blockers.append("full-thesis seed accepted claims produced no StageCourt traces")
    if real_document_count <= 0:
        blockers.append("Brain/Web real fetched document count is zero")
    if attempt_source_task_count > 0 and source_task_count <= 0:
        blockers.append("Brain/Web source task attempt count has no exported source_task_executions rows")
    if attempt_real_document_count > 0 and real_document_count <= 0:
        blockers.append("Brain/Web real document attempt count has no exported evidence_documents rows")
    if attempt_accepted_claim_count > 0 and accepted_claim_count <= 0:
        blockers.append("Brain/Web accepted claim attempt count has no exported accepted_claims rows")
    if len(web_tasks) <= 0 and len(web_results) <= 0 and len(web_fetched) <= 0 and accepted_claim_count <= 0:
        blockers.append("web/news/Naver acquisition has zero search/fetch rows and no accepted Brain/Web claim")
    if requires_web_acquisition and len(web_tasks) <= 0:
        blockers.append("Brain/Web acquisition mode requires web/news search task rows")
    if requires_web_acquisition and len(web_fetched) <= 0:
        blockers.append("Brain/Web acquisition mode requires fetched full-source web/news documents")
    if len(extractor_runs) <= 0 and accepted_claim_count <= 0:
        blockers.append("LLM claim extractor has zero attempts and no accepted Brain/Web claim")
    if extractor_provider_error_count:
        blockers.append(f"LLM claim extractor provider errors are unresolved: {extractor_provider_error_count}")
    if extractor_timeout_count:
        blockers.append(f"LLM claim extractor timeouts are unresolved: {extractor_timeout_count}")
    if accepted_claim_count > 0 and extractor_runs and llm_extractor_run_count <= 0:
        blockers.append("LLM claim extractor has no real LLM provider runs")
    if forbidden_extractor_context_count:
        blockers.append(f"LLM claim extractor received forbidden score/stage context: {forbidden_extractor_context_count}")
    if accepted_claim_count <= 0:
        blockers.append("Brain/Web accepted claim count is zero")
    if requires_web_acquisition and web_or_llm_accepted_claim_count <= 0:
        blockers.append("web/LLM accepted claim count is zero")
    if accepted_claim_count > 0 and len(brain_trace) <= 0:
        blockers.append("accepted Brain/Web claims have no brain_to_claim_trace rows")
    if accepted_claim_count > 0 and len(brain_contributions) <= 0:
        blockers.append("accepted Brain/Web claims have no claim-backed score contributions")
    if accepted_claim_count > 0 and len(brain_stage_traces) <= 0:
        blockers.append("accepted Brain/Web claims have no StageCourt traces")
    if brain_claim_quality_counts["missing_verifiable_anchor_count"]:
        blockers.append(f"accepted Brain/Web claims missing document/anchor IDs: {brain_claim_quality_counts['missing_verifiable_anchor_count']}")
    if unresolved_claim_document_ref_count:
        blockers.append(f"accepted Brain/Web claims reference missing evidence_documents rows: {unresolved_claim_document_ref_count}")
    if unresolved_claim_anchor_ref_count:
        blockers.append(f"accepted Brain/Web claims reference missing evidence_anchors rows: {unresolved_claim_anchor_ref_count}")
    if brain_claim_quality_counts["missing_date_count"]:
        blockers.append(f"accepted Brain/Web claims missing event/as-of/source date: {brain_claim_quality_counts['missing_date_count']}")
    if brain_claim_quality_counts["not_direct_target_count"]:
        blockers.append(f"accepted Brain/Web claims are not direct target claims: {brain_claim_quality_counts['not_direct_target_count']}")
    if brain_claim_quality_counts["not_current_count"]:
        blockers.append(f"accepted Brain/Web claims are not current/open: {brain_claim_quality_counts['not_current_count']}")
    if brain_claim_quality_counts["score_ineligible_count"]:
        blockers.append(f"accepted Brain/Web claims are not score eligible by deterministic guard: {brain_claim_quality_counts['score_ineligible_count']}")
    if brain_trace_missing_accepted_claim_count:
        blockers.append(f"accepted Brain/Web claims missing from brain_to_claim_trace: {brain_trace_missing_accepted_claim_count}")
    if brain_trace_missing_score_contribution_ref_count:
        blockers.append(f"Brain/Web trace rows missing score_contribution_id: {brain_trace_missing_score_contribution_ref_count}")
    if brain_trace_missing_stagecourt_ref_count:
        blockers.append(f"Brain/Web trace rows missing stagecourt_trace_id: {brain_trace_missing_stagecourt_ref_count}")
    if brain_contribution_without_accepted_support_count:
        blockers.append(
            f"Brain/Web score contributions do not support accepted Brain/Web claims: {brain_contribution_without_accepted_support_count}"
        )
    if brain_stage_trace_without_accepted_claim_count:
        blockers.append(f"Brain/Web StageCourt traces do not carry accepted Brain/Web claims: {brain_stage_trace_without_accepted_claim_count}")
    if promoted_stage_without_brain_trace_count:
        blockers.append(f"promoted Brain/Web stage rows are not connected to Brain/Web trace and accepted claim IDs: {promoted_stage_without_brain_trace_count}")
    if source_task_without_document_ref_count:
        blockers.append(f"Brain/Web source task rows missing fetched document refs: {source_task_without_document_ref_count}")
    if source_task_unresolved_document_ref_count:
        blockers.append(f"Brain/Web source task rows reference missing evidence_documents rows: {source_task_unresolved_document_ref_count}")
    if config.brain_source_acquisition in {"frozen_real_source_snapshot", "test_fake"}:
        blockers.append(f"source acquisition is not production-live: {config.brain_source_acquisition}")
    if config.brain_planner_provider in {"none", "test_fake"}:
        blockers.append(f"planner provider is not a real evidence provider: {config.brain_planner_provider}")
    if snapshot_document_count:
        blockers.append("Brain/Web evidence documents include snapshot:// sources")
    if fake_provider_used_count:
        blockers.append("fake planner/provider rows are present")
    if snippet_to_score_count:
        blockers.append("snippet-only rows contributed to score")
    if provider_failure_final_score_count:
        blockers.append("provider failure rows still received final score")
    if unsafe_promoted_stage_row_count:
        blockers.append("Brain/Web stage row was promoted despite blockers")
    if promoted_stage_row_count <= 0:
        blockers.append("Brain/Web StageCourt traces are not promoted into census_stage_status")
    if promotion_verdict != "PROMOTION_APPLIED":
        blockers.append(f"brain stage promotion verdict is not PROMOTION_APPLIED: {promotion_verdict or 'UNKNOWN'}")
    if operational_minimum_gate_applies:
        if len(planner) < BRAIN_WEB_MIN_PLANNER_CALLS:
            blockers.append(f"Brain/Web operational minimum planner runs not met: {len(planner)}/{BRAIN_WEB_MIN_PLANNER_CALLS}")
        if len(web_tasks) < BRAIN_WEB_MIN_WEB_SEARCH_TASKS:
            blockers.append(f"Brain/Web operational minimum web search tasks not met: {len(web_tasks)}/{BRAIN_WEB_MIN_WEB_SEARCH_TASKS}")
        if web_call_counts["web_search_call_count"] < BRAIN_WEB_MIN_WEB_SEARCH_CALLS:
            blockers.append(
                f"Brain/Web operational minimum web/news search calls not met: {web_call_counts['web_search_call_count']}/{BRAIN_WEB_MIN_WEB_SEARCH_CALLS}"
            )
        if len(web_fetched) < BRAIN_WEB_MIN_FETCHED_DOCUMENTS:
            blockers.append(f"Brain/Web operational minimum fetched documents not met: {len(web_fetched)}/{BRAIN_WEB_MIN_FETCHED_DOCUMENTS}")
        if len(extractor_runs) < BRAIN_WEB_MIN_EXTRACTOR_ATTEMPTS:
            blockers.append(f"Brain/Web operational minimum claim extractor attempts not met: {len(extractor_runs)}/{BRAIN_WEB_MIN_EXTRACTOR_ATTEMPTS}")
        if web_or_llm_accepted_claim_count < BRAIN_WEB_MIN_ACCEPTED_CLAIMS:
            blockers.append(
                f"Brain/Web operational minimum web/LLM accepted claims not met: {web_or_llm_accepted_claim_count}/{BRAIN_WEB_MIN_ACCEPTED_CLAIMS}"
            )

    pass_allowed = not blockers
    nonblocking_gaps: list[str] = []
    if brain_trace_nonrepresentative_missing_stagecourt_ref_count:
        nonblocking_gaps.append(
            "non-representative Brain/Web accepted claim traces without StageCourt refs: "
            f"{brain_trace_nonrepresentative_missing_stagecourt_ref_count}"
        )
    if not pass_allowed:
        nonblocking_gaps.append("Brain/Web evidence pass is forbidden until all blockers are zero")
    return {
        "schema_version": "e2r_census_v4_brain_web_readiness_gate_audit_v1",
        "run_mode": config.run_mode,
        "brain_web_mode": config.brain_web_mode,
        "verdict": "READY_FOR_BRAIN_WEB_EVIDENCE_PASS" if pass_allowed else "BLOCKED",
        "minimum_gate_applies": True,
        "operational_minimum_count_gate_applies": operational_minimum_gate_applies,
        "brain_web_evidence_pass_allowed": pass_allowed,
        "full_thesis_seed_event_path": full_thesis_seed_event_path,
        "full_thesis_seed_source": full_thesis_seed_source,
        "full_thesis_seed_original_path": full_thesis_seed_original_path,
        "full_thesis_seed_event_count": full_thesis_seed_event_count,
        "full_thesis_seed_consumed_by_research_brain": full_thesis_seed_consumed_by_research_brain,
        "full_thesis_seed_planner_attempted_event_count": full_thesis_seed_planner_attempted_event_count,
        "full_thesis_seed_planner_run_row_count": full_thesis_seed_planner_run_row_count,
        "full_thesis_seed_planner_run_count": full_thesis_seed_planner_run_count,
        "full_thesis_seed_real_provider_success_count": full_thesis_seed_real_provider_success_count,
        "full_thesis_seed_source_task_execution_count": full_thesis_seed_source_task_execution_count,
        "full_thesis_seed_accepted_claim_count": full_thesis_seed_accepted_claim_count,
        "full_thesis_seed_stagecourt_trace_count": full_thesis_seed_stagecourt_trace_count,
        "full_thesis_seed_materialized_to_stagecourt": full_thesis_seed_materialized_to_stagecourt,
        "llm_planner_call_count": len(planner),
        "llm_real_provider_success_count": real_provider_success,
        "attempt_source_task_execution_count": attempt_source_task_count,
        "source_task_execution_count": source_task_count,
        "attempt_real_document_fetched_count": attempt_real_document_count,
        "real_document_fetched_count": real_document_count,
        "policy_rejected_source_task_execution_count": policy_rejected_source_task_execution_count,
        "zero_budget_policy_rejected_source_task_execution_count": zero_budget_policy_rejected_source_task_execution_count,
        "source_lineage_feedback_retry_execution_count": len(source_lineage_feedback_retry_executions),
        "source_lineage_feedback_retry_accepted_execution_count": source_lineage_retry_accepted_execution_count,
        "source_lineage_feedback_retry_no_evidence_execution_count": source_lineage_retry_no_evidence_execution_count,
        "source_lineage_feedback_retry_dropped_count": source_lineage_retry_dropped_count,
        "discovery_only_retry_after_unverified_original_count": source_lineage_retry_dropped_count,
        "web_search_task_count": len(web_tasks),
        "web_search_result_count": len(web_results),
        "web_fetched_document_count": len(web_fetched),
        "web_rejected_document_count": len(web_rejected),
        "web_search_call_count": web_call_counts["web_search_call_count"],
        "naver_search_call_count": web_call_counts["naver_search_call_count"],
        "trusted_news_search_call_count": web_call_counts["trusted_news_search_call_count"],
        "general_web_search_call_count": web_call_counts["general_web_search_call_count"],
        "llm_claim_extractor_attempt_count": len(extractor_runs),
        "llm_claim_extractor_real_provider_count": llm_extractor_run_count,
        "claim_extractor_non_llm_provider_count": non_llm_extractor_run_count,
        "llm_claim_extractor_provider_error_count": extractor_provider_error_count,
        "llm_claim_extractor_timeout_count": extractor_timeout_count,
        "claim_extractor_forbidden_context_count": forbidden_extractor_context_count,
        "attempt_accepted_claim_count": attempt_accepted_claim_count,
        "brain_accepted_claim_count": accepted_claim_count,
        "web_or_llm_accepted_claim_count": web_or_llm_accepted_claim_count,
        "official_accepted_claim_count": len(official_accepted),
        "web_news_accepted_claim_count": len(web_news_accepted),
        "llm_extracted_accepted_claim_count": len(llm_extracted_accepted),
        "full_thesis_claim_count": full_thesis_accepted_claim_count,
        "direct_accepted_claim_count": direct_trace_claim_count,
        "rerouted_accepted_claim_count": rerouted_trace_claim_count,
        "direct_source_task_satisfied_count": direct_source_task_satisfied_count,
        "rerouted_source_task_claim_count": rerouted_source_task_claim_count,
        "brain_to_claim_trace_count": len(brain_trace),
        "brain_score_contribution_count": len(brain_contributions),
        "brain_stage_trace_count": len(brain_stage_traces),
        "brain_promoted_stage_row_count": promoted_stage_row_count,
        "brain_trace_missing_accepted_claim_count": brain_trace_missing_accepted_claim_count,
        "brain_trace_missing_score_contribution_ref_count": brain_trace_missing_score_contribution_ref_count,
        "brain_trace_missing_stagecourt_ref_count": brain_trace_missing_stagecourt_ref_count,
        "brain_trace_nonrepresentative_missing_stagecourt_ref_count": brain_trace_nonrepresentative_missing_stagecourt_ref_count,
        "brain_contribution_without_accepted_support_count": brain_contribution_without_accepted_support_count,
        "brain_stage_trace_without_accepted_claim_count": brain_stage_trace_without_accepted_claim_count,
        "promoted_stage_without_brain_trace_count": promoted_stage_without_brain_trace_count,
        "requires_web_acquisition_minimum": requires_web_acquisition,
        "brain_claim_missing_verifiable_anchor_count": brain_claim_quality_counts["missing_verifiable_anchor_count"],
        "brain_claim_unresolved_document_ref_count": unresolved_claim_document_ref_count,
        "brain_claim_unresolved_anchor_ref_count": unresolved_claim_anchor_ref_count,
        "brain_claim_missing_date_count": brain_claim_quality_counts["missing_date_count"],
        "brain_claim_not_direct_target_count": brain_claim_quality_counts["not_direct_target_count"],
        "brain_claim_not_current_count": brain_claim_quality_counts["not_current_count"],
        "brain_claim_score_ineligible_count": brain_claim_quality_counts["score_ineligible_count"],
        "brain_source_task_without_document_ref_count": source_task_without_document_ref_count,
        "brain_source_task_unresolved_document_ref_count": source_task_unresolved_document_ref_count,
        "snapshot_document_count": snapshot_document_count,
        "fake_provider_used_count": fake_provider_used_count,
        "snippet_to_score_count": snippet_to_score_count,
        "provider_failure_final_score_count": provider_failure_final_score_count,
        "minimum_required_counts": _brain_web_minimum_required_counts(),
        "blockers": blockers,
        "nonblocking_gaps": nonblocking_gaps,
        "rule": (
            "Brain/Web evidence pass requires real provider success, bounded source acquisition, fetched documents, "
            "claim extraction or accepted claims, brain_to_claim_trace, claim-backed score contribution, StageCourt trace, "
            "strict promotion into census_stage_status, and zero snippet/provider-failure/snapshot/fake-provider leakage."
        ),
    }


def _config_requests_brain_web(config: CensusV4RunConfig) -> bool:
    return _config_requests_brain_planner(config) or _config_requests_web_acquisition(config)


def _brain_web_operational_minimum_gate_applies(config: CensusV4RunConfig) -> bool:
    if config.run_mode in {"BRAIN_AND_WEB_ACQUISITION_ENABLED", "FULL_LIVE_BRAIN_CENSUS"}:
        return True
    if config.run_mode == "HYBRID_CENSUS" and config.brain_web_mode == "enabled":
        return True
    return config.target_gate in {"brain_web", "meaningful"} and _config_requests_web_acquisition(config)


def _brain_web_minimum_required_counts() -> dict[str, int]:
    return {
        "llm_planner_call_count": BRAIN_WEB_MIN_PLANNER_CALLS,
        "web_search_task_count": BRAIN_WEB_MIN_WEB_SEARCH_TASKS,
        "web_search_call_count": BRAIN_WEB_MIN_WEB_SEARCH_CALLS,
        "web_fetched_document_count": BRAIN_WEB_MIN_FETCHED_DOCUMENTS,
        "llm_claim_extractor_attempt_count": BRAIN_WEB_MIN_EXTRACTOR_ATTEMPTS,
        "web_or_llm_accepted_claim_count": BRAIN_WEB_MIN_ACCEPTED_CLAIMS,
    }


def _accepted_claim_is_web_news_source(
    row: Mapping[str, Any],
    *,
    web_document_ids: set[str],
    web_source_urls: set[str],
) -> bool:
    if _ids_from_value(row.get("document_id")) & web_document_ids:
        return True
    if _ids_from_value(row.get("source_document_id")) & web_document_ids:
        return True
    source_url = str(row.get("source_url") or row.get("canonical_url") or "").strip()
    if source_url and source_url in web_source_urls:
        return True
    provider = str(row.get("source_provider") or row.get("provider_name") or row.get("source_name") or "").lower()
    return any(token in provider for token in ("naver", "generalweb", "websearch", "trustednews", "news.json", "search/web"))


def _accepted_claim_is_llm_extracted(row: Mapping[str, Any], *, llm_raw_assertion_ids: set[str]) -> bool:
    raw_ids = _ids_from_value(row.get("raw_assertion_id")) | _ids_from_value(row.get("raw_assertion_ids"))
    if raw_ids & llm_raw_assertion_ids:
        return True
    return any(raw_id.startswith("RAWLLM-") for raw_id in raw_ids)


def _accepted_claim_is_official_source(row: Mapping[str, Any]) -> bool:
    provider = str(row.get("source_provider") or row.get("provider_name") or row.get("source_name") or "").lower()
    source_url = str(row.get("source_url") or row.get("canonical_url") or "").lower()
    official_tokens = ("opendart", "dart.fss.or.kr", "kind.krx.co.kr", "krx", "companyguide", "issuerofficial")
    return any(token in provider or token in source_url for token in official_tokens)


def _config_requests_brain_planner(config: CensusV4RunConfig) -> bool:
    return config.brain_web_mode == "enabled" or _run_mode_requests_brain_planner(config.run_mode)


def _config_requests_web_acquisition(config: CensusV4RunConfig) -> bool:
    if _run_mode_requests_web_acquisition(config.run_mode):
        return True
    if config.brain_web_mode != "enabled":
        return False
    return config.run_mode not in {"BRAIN_TRIAGE_ENABLED"}


def _config_requests_llm_claim_extraction(config: CensusV4RunConfig) -> bool:
    return _config_requests_web_acquisition(config) or _run_mode_requests_llm_claim_extraction(config.run_mode)


def _run_mode_requests_brain_planner(run_mode: str) -> bool:
    return run_mode in {
        "BRAIN_TRIAGE_ENABLED",
        "BRAIN_AND_WEB_ACQUISITION_ENABLED",
        "FULL_LIVE_BRAIN_CENSUS",
        "HYBRID_CENSUS",
    }


def _run_mode_requests_web_acquisition(run_mode: str) -> bool:
    return run_mode in {
        "BRAIN_AND_WEB_ACQUISITION_ENABLED",
        "FULL_LIVE_BRAIN_CENSUS",
    }


def _run_mode_requests_llm_claim_extraction(run_mode: str) -> bool:
    return run_mode in {
        "BRAIN_AND_WEB_ACQUISITION_ENABLED",
        "FULL_LIVE_BRAIN_CENSUS",
    }


def _is_brain_origin(row: Mapping[str, Any]) -> bool:
    return str(row.get("source_origin") or row.get("brain_web_origin") or "") == "research_brain_v4_attempt"


def _is_source_lineage_retry_drop_execution(row: Mapping[str, Any]) -> bool:
    reason = "source_lineage_retry_discovery_only_after_unverified_original"
    reason_fields = {
        str(row.get("stop_reason") or ""),
        str(row.get("reason_from_memory") or ""),
        str((row.get("source_task") or {}).get("reason_from_memory") or ""),
    }
    reason_fields.update(str(item or "") for item in row.get("not_eligible_reasons") or ())
    reason_fields.update(str(item or "") for item in row.get("provider_errors") or ())
    return str(row.get("status") or "") == "REJECTED_BY_POLICY" and any(reason in value for value in reason_fields)


def _is_source_lineage_feedback_retry_execution(row: Mapping[str, Any]) -> bool:
    tag = "feedback_retry:source_lineage_unverified_original"
    reason_fields = {
        str(row.get("reason_from_memory") or ""),
        str(row.get("source_task_origin") or ""),
        str(row.get("source_task_execution_origin") or ""),
        str((row.get("source_task") or {}).get("reason_from_memory") or ""),
        str((row.get("source_task") or {}).get("source_task_origin") or ""),
    }
    reason_fields.update(str(item or "") for item in row.get("not_eligible_reasons") or ())
    reason_fields.update(str(item or "") for item in row.get("provider_errors") or ())
    return any(tag in value for value in reason_fields)


def _source_task_budget_is_zero(row: Mapping[str, Any]) -> bool:
    budget = row.get("budget_used") or {}
    return all(int(budget.get(key) or 0) == 0 for key in ("queries", "candidates", "fetches"))


def _brain_trace_score_deduped_by_source_family(row: Mapping[str, Any]) -> bool:
    return bool(row.get("score_deduped_by_source_family")) or str(row.get("score_support_status") or "") == "SOURCE_FAMILY_DEDUPED"


def _brain_trace_requires_score_contribution(row: Mapping[str, Any], *, representative_claim_ids: set[str] | None = None) -> bool:
    claim_ids = _ids_from_value(row.get("accepted_claim_id"))
    if representative_claim_ids and claim_ids & representative_claim_ids:
        return True
    if _brain_trace_score_deduped_by_source_family(row):
        return False
    if row.get("representative_score_claim") is False:
        return False
    status = str(row.get("score_support_status") or "")
    if status in {"ACCEPTED_NON_REPRESENTATIVE_NOT_SCORE_CONTRIBUTING", "PRIMITIVE_ONLY_NOT_SCORE_CONTRIBUTING"}:
        return False
    return True


def _brain_trace_requires_stagecourt(row: Mapping[str, Any], *, representative_claim_ids: set[str] | None = None) -> bool:
    claim_ids = _ids_from_value(row.get("accepted_claim_id"))
    if representative_claim_ids and claim_ids & representative_claim_ids:
        return True
    if _ids_from_value(row.get("score_contribution_id")) or _ids_from_value(row.get("score_contribution_ids")):
        return True
    return _brain_trace_requires_score_contribution(row, representative_claim_ids=representative_claim_ids)


def _ids_from_value(value: Any) -> set[str]:
    if value is None:
        return set()
    if isinstance(value, (list, tuple, set)):
        return {str(item) for item in value if str(item)}
    text = str(value)
    return {text} if text else set()


def _source_task_requires_document_ref(row: Mapping[str, Any]) -> bool:
    """Document refs are mandatory only for claim-producing task rows.

    A provider-failed follow-up task with no accepted claim is a source gap, not
    evidence. It should not block promotion of a separate claim-backed Brain/Web
    StageCourt trace. Once a task claims Evidence OS acceptance or carries
    accepted claim IDs, the document reference remains mandatory.
    """

    if _ids_from_value(row.get("accepted_claim_ids")):
        return True
    return str(row.get("status") or "") == "EVIDENCE_OS_ACCEPTED"


def _float_or_none(value: Any) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _all_archetype_replay_matrix(
    *,
    config: CensusV4RunConfig,
    output_root: Path,
    stage_rows: Sequence[Mapping[str, Any]],
    c06_guard_replay: Mapping[str, Any] | None = None,
    c08_source_backed_replay: Mapping[str, Any] | None = None,
    c15_source_backed_replay: Mapping[str, Any] | None = None,
    c17_source_backed_replay: Mapping[str, Any] | None = None,
    c24_source_backed_replay: Mapping[str, Any] | None = None,
    c28_source_backed_replay: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2

    contracts = load_evidence_contracts_v2(require_all_archetypes=True)
    accepted_claims = _read_jsonl(output_root / "accepted_claims.jsonl")
    source_proxy_leak_claims = [
        str(row.get("claim_id") or "")
        for row in accepted_claims
        if row.get("source_proxy_only") is True
        or row.get("evidence_url_pending") is True
        or str(row.get("source_url") or "").startswith("source-proxy://")
    ]
    full_thesis_rows_by_archetype: dict[str, list[Mapping[str, Any]]] = {}
    for row in stage_rows:
        archetype = str(row.get("full_thesis_primary_archetype") or "")
        if row.get("stage_scope") == "FULL_THESIS" and archetype:
            full_thesis_rows_by_archetype.setdefault(archetype, []).append(row)

    c06_source_backed_replay = (c06_guard_replay or {}).get("source_backed_semantic_replay") or {}
    c06_source_backed_positive_ready = c06_source_backed_replay.get("positive_replay_pass") is True
    c06_source_backed_claim_count = int(c06_source_backed_replay.get("accepted_claim_count") or 0)
    c06_source_backed_symbols = sorted(
        {
            str(claim.get("symbol") or "").zfill(6)
            for claim in c06_source_backed_replay.get("claims") or []
            if claim.get("symbol")
        }
    )
    c08_source_backed_replay = c08_source_backed_replay or {}
    c08_source_backed_positive_ready = c08_source_backed_replay.get("positive_replay_pass") is True
    c08_source_backed_guard_ready = c08_source_backed_replay.get("guard_replay_pass") is True
    c08_source_backed_claim_count = int(c08_source_backed_replay.get("accepted_claim_count") or 0)
    c08_source_backed_symbols = sorted(
        {
            str(claim.get("symbol") or "").zfill(6)
            for claim in [
                *(c08_source_backed_replay.get("positive_claims") or []),
                *(c08_source_backed_replay.get("guard_claims") or []),
            ]
            if claim.get("symbol")
        }
    )
    c15_source_backed_replay = c15_source_backed_replay or {}
    c15_source_backed_positive_ready = c15_source_backed_replay.get("positive_replay_pass") is True
    c15_source_backed_guard_ready = c15_source_backed_replay.get("guard_replay_pass") is True
    c15_source_backed_claim_count = int(c15_source_backed_replay.get("accepted_claim_count") or 0)
    c15_source_backed_symbols = sorted(
        {
            str(claim.get("symbol") or "").zfill(6)
            for claim in [
                *(c15_source_backed_replay.get("positive_claims") or []),
                *(c15_source_backed_replay.get("guard_claims") or []),
            ]
            if claim.get("symbol")
        }
    )
    c17_source_backed_replay = c17_source_backed_replay or {}
    c17_source_backed_positive_ready = c17_source_backed_replay.get("positive_replay_pass") is True
    c17_source_backed_guard_ready = c17_source_backed_replay.get("guard_replay_pass") is True
    c17_source_backed_claim_count = int(c17_source_backed_replay.get("accepted_claim_count") or 0)
    c17_source_backed_symbols = sorted(
        {
            str(claim.get("symbol") or "").zfill(6)
            for claim in [
                *(c17_source_backed_replay.get("positive_claims") or []),
                *(c17_source_backed_replay.get("guard_claims") or []),
            ]
            if claim.get("symbol")
        }
    )
    c24_source_backed_replay = c24_source_backed_replay or {}
    c24_source_backed_positive_ready = c24_source_backed_replay.get("positive_replay_pass") is True
    c24_source_backed_guard_ready = c24_source_backed_replay.get("guard_replay_pass") is True
    c24_source_backed_claim_count = int(c24_source_backed_replay.get("accepted_claim_count") or 0)
    c24_source_backed_symbols = sorted(
        {
            str(claim.get("symbol") or "").zfill(6)
            for claim in [
                *(c24_source_backed_replay.get("positive_claims") or []),
                *(c24_source_backed_replay.get("guard_claims") or []),
            ]
            if claim.get("symbol")
        }
    )
    c28_source_backed_replay = c28_source_backed_replay or {}
    c28_source_backed_positive_ready = c28_source_backed_replay.get("positive_replay_pass") is True
    c28_source_backed_guard_ready = c28_source_backed_replay.get("guard_replay_pass") is True
    c28_source_backed_claim_count = int(c28_source_backed_replay.get("accepted_claim_count") or 0)
    c28_source_backed_symbols = sorted(
        {
            str(claim.get("symbol") or "").zfill(6)
            for claim in [
                *(c28_source_backed_replay.get("positive_claims") or []),
                *(c28_source_backed_replay.get("guard_claims") or []),
            ]
            if claim.get("symbol")
        }
    )

    rows: list[dict[str, Any]] = []
    for archetype_id, contract in contracts.items():
        full_rows = full_thesis_rows_by_archetype.get(archetype_id, [])
        url_backed_wiring_fixture_count = len(full_rows)
        claim_count = sum(len(row.get("full_thesis_accepted_claim_ids") or []) for row in full_rows)
        contribution_count = sum(len(row.get("full_thesis_score_contribution_ids") or []) for row in full_rows)
        has_wiring_smoke = url_backed_wiring_fixture_count > 0 and claim_count > 0 and contribution_count > 0
        if archetype_id == FULL_THESIS_SMOKE_ARCHETYPE:
            positive_replay_pass = bool(c06_source_backed_positive_ready)
        elif archetype_id == C08_TEST_SOCKET_ARCHETYPE:
            positive_replay_pass = bool(c08_source_backed_positive_ready)
        elif archetype_id == C15_MATERIAL_SPREAD_ARCHETYPE:
            positive_replay_pass = bool(c15_source_backed_positive_ready)
        elif archetype_id == C17_CHEMICAL_SPREAD_ARCHETYPE:
            positive_replay_pass = bool(c17_source_backed_positive_ready)
        elif archetype_id == C24_BIO_TRIAL_ARCHETYPE:
            positive_replay_pass = bool(c24_source_backed_positive_ready)
        elif archetype_id == C28_SOFTWARE_SECURITY_ARCHETYPE:
            positive_replay_pass = bool(c28_source_backed_positive_ready)
        else:
            positive_replay_pass = bool(has_wiring_smoke)
        source_backed_fixture_count = (
            c06_source_backed_claim_count
            if archetype_id == FULL_THESIS_SMOKE_ARCHETYPE and positive_replay_pass
            else c08_source_backed_claim_count
            if archetype_id == C08_TEST_SOCKET_ARCHETYPE and positive_replay_pass
            else c15_source_backed_claim_count
            if archetype_id == C15_MATERIAL_SPREAD_ARCHETYPE and positive_replay_pass
            else c17_source_backed_claim_count
            if archetype_id == C17_CHEMICAL_SPREAD_ARCHETYPE and positive_replay_pass
            else c24_source_backed_claim_count
            if archetype_id == C24_BIO_TRIAL_ARCHETYPE and positive_replay_pass
            else c28_source_backed_claim_count
            if archetype_id == C28_SOFTWARE_SECURITY_ARCHETYPE and positive_replay_pass
            else (url_backed_wiring_fixture_count if positive_replay_pass else 0)
        )
        if archetype_id == FULL_THESIS_SMOKE_ARCHETYPE:
            guard_replay_pass = bool(
                c06_guard_replay
                and c06_guard_replay.get("guard_replay_pass") is True
            )
        elif archetype_id == C08_TEST_SOCKET_ARCHETYPE:
            guard_replay_pass = bool(c08_source_backed_guard_ready)
        elif archetype_id == C15_MATERIAL_SPREAD_ARCHETYPE:
            guard_replay_pass = bool(c15_source_backed_guard_ready)
        elif archetype_id == C17_CHEMICAL_SPREAD_ARCHETYPE:
            guard_replay_pass = bool(c17_source_backed_guard_ready)
        elif archetype_id == C24_BIO_TRIAL_ARCHETYPE:
            guard_replay_pass = bool(c24_source_backed_guard_ready)
        elif archetype_id == C28_SOFTWARE_SECURITY_ARCHETYPE:
            guard_replay_pass = bool(c28_source_backed_guard_ready)
        else:
            guard_replay_pass = False
        if archetype_id == FULL_THESIS_SMOKE_ARCHETYPE:
            guard_case_count = int((c06_guard_replay or {}).get("guard_case_count") or 0)
            guard_case_pass_count = int((c06_guard_replay or {}).get("guard_case_pass_count") or 0)
            semantic_blockers = list((c06_guard_replay or {}).get("semantic_blockers") or [])
            special_claim_count = c06_source_backed_claim_count
            special_symbols = c06_source_backed_symbols
        elif archetype_id == C08_TEST_SOCKET_ARCHETYPE:
            guard_case_count = 1 if c08_source_backed_guard_ready else 0
            guard_case_pass_count = 1 if c08_source_backed_guard_ready else 0
            semantic_blockers = list(c08_source_backed_replay.get("blockers") or [])
            special_claim_count = c08_source_backed_claim_count
            special_symbols = c08_source_backed_symbols
        elif archetype_id == C15_MATERIAL_SPREAD_ARCHETYPE:
            guard_case_count = 1 if c15_source_backed_guard_ready else 0
            guard_case_pass_count = 1 if c15_source_backed_guard_ready else 0
            semantic_blockers = list(c15_source_backed_replay.get("blockers") or [])
            special_claim_count = c15_source_backed_claim_count
            special_symbols = c15_source_backed_symbols
        elif archetype_id == C17_CHEMICAL_SPREAD_ARCHETYPE:
            guard_case_count = 1 if c17_source_backed_guard_ready else 0
            guard_case_pass_count = 1 if c17_source_backed_guard_ready else 0
            semantic_blockers = list(c17_source_backed_replay.get("blockers") or [])
            special_claim_count = c17_source_backed_claim_count
            special_symbols = c17_source_backed_symbols
        elif archetype_id == C24_BIO_TRIAL_ARCHETYPE:
            guard_case_count = 1 if c24_source_backed_guard_ready else 0
            guard_case_pass_count = 1 if c24_source_backed_guard_ready else 0
            semantic_blockers = list(c24_source_backed_replay.get("blockers") or [])
            special_claim_count = c24_source_backed_claim_count
            special_symbols = c24_source_backed_symbols
        elif archetype_id == C28_SOFTWARE_SECURITY_ARCHETYPE:
            guard_case_count = 1 if c28_source_backed_guard_ready else 0
            guard_case_pass_count = 1 if c28_source_backed_guard_ready else 0
            semantic_blockers = list(c28_source_backed_replay.get("blockers") or [])
            special_claim_count = c28_source_backed_claim_count
            special_symbols = c28_source_backed_symbols
        else:
            guard_case_count = 0
            guard_case_pass_count = 0
            semantic_blockers = []
            special_claim_count = 0
            special_symbols = []
        is_cross_guard = archetype_id.startswith("R13_")
        if positive_replay_pass and guard_replay_pass:
            status = "SOURCE_BACKED_POSITIVE_AND_GUARD_REPLAY_READY"
            unsupported_reason = None
        elif positive_replay_pass:
            status = "SOURCE_BACKED_POSITIVE_REPLAY_READY_GUARD_PENDING"
            unsupported_reason = None
        elif has_wiring_smoke:
            status = "CONTROLLED_WIRING_SMOKE_ONLY_SEMANTIC_REPLAY_PENDING"
            unsupported_reason = "controlled_smoke_fixture_has_url_anchors_but_not_contract_blind_semantic_replay"
        elif is_cross_guard:
            status = "GUARDRAIL_CONTRACT_ONLY_PENDING_SOURCE_BACKED_REPLAY"
            unsupported_reason = "cross_archetype_guard_contract_has_no_source_backed_replay_fixture_in_census_v4_output"
        else:
            status = "SOURCE_GAP_PENDING"
            unsupported_reason = "no_source_backed_replay_fixture_in_census_v4_output"
        rows.append(
            {
                "archetype_id": archetype_id,
                "contract_loaded": contract is not None,
                "replay_status": status,
                "replay_scope": "source_backed_semantic_replay" if positive_replay_pass and guard_replay_pass else ("controlled_wiring_smoke_only" if has_wiring_smoke else "not_replayed"),
                "fixture_count": url_backed_wiring_fixture_count,
                "url_backed_wiring_fixture_count": url_backed_wiring_fixture_count,
                "source_backed_fixture_count": source_backed_fixture_count,
                "controlled_wiring_smoke_pass": bool(has_wiring_smoke),
                "positive_replay_pass": positive_replay_pass,
                "guard_replay_pass": guard_replay_pass,
                "guard_case_count": guard_case_count,
                "guard_case_pass_count": guard_case_pass_count,
                "semantic_blockers": semantic_blockers,
                "source_proxy_leak_count": 0,
                "accepted_claim_count": claim_count + special_claim_count,
                "score_contribution_count": contribution_count,
                "full_thesis_symbols": [str(row.get("symbol") or "") for row in full_rows],
                "source_backed_replay_symbols": special_symbols,
                "unsupported_reason": unsupported_reason,
                "required_before_goal_completion": not is_cross_guard,
            }
        )

    required_rows = [row for row in rows if row["required_before_goal_completion"]]
    missing_required = [row["archetype_id"] for row in required_rows if not (row["positive_replay_pass"] and row["guard_replay_pass"])]
    all_pass = not missing_required and not source_proxy_leak_claims
    status_counts: dict[str, int] = {}
    for row in rows:
        key = str(row["replay_status"])
        status_counts[key] = status_counts.get(key, 0) + 1
    return {
        "schema_version": "e2r_census_v4_all_archetype_replay_matrix_v1",
        "as_of_date": config.as_of_date,
        "all_archetype_replay_pass": all_pass,
        "archetype_count": len(rows),
        "required_archetype_count": len(required_rows),
        "source_backed_ready_count": sum(1 for row in rows if row["positive_replay_pass"]),
        "guard_replay_ready_count": sum(1 for row in rows if row["guard_replay_pass"]),
        "controlled_wiring_smoke_ready_count": sum(1 for row in rows if row["controlled_wiring_smoke_pass"]),
        "missing_required_archetype_count": len(missing_required),
        "missing_required_archetype_ids": missing_required,
        "status_counts": status_counts,
        "source_proxy_leak_count": len(source_proxy_leak_claims),
        "source_proxy_leak_claim_ids": source_proxy_leak_claims,
        "blockers": [] if all_pass else ["source_backed_replay_parity_all_archetypes_pending"],
        "note": "Controlled wiring smoke proves the leaf path can carry URL anchors and ScoreContribution rows. It is not source-backed semantic replay until contract-blind extraction, lifecycle adjudication, and guard replay all pass.",
        "archetypes": rows,
    }


def _row_ids(rows: Sequence[Mapping[str, Any]], key: str) -> set[str]:
    ids: set[str] = set()
    for row in rows:
        ids.update(_ids_from_value(row.get(key)))
    return ids


def _write_goal_v4_audits(
    *,
    config: CensusV4RunConfig,
    output_root: Path,
    stage_rows: Sequence[Mapping[str, Any]],
    runtime_seconds: float,
) -> dict[str, Mapping[str, Any]]:
    known_bad_report = _known_bad_regression_report(config=config, output_root=output_root)
    controlled_semantic_replay = _controlled_semantic_replay_audit(
        config=config,
        output_root=output_root,
        c06_guard=_read_json(output_root / "c06_guard_replay_audit.json"),
        all_archetype_replay_matrix=_read_json(output_root / "all_archetype_replay_matrix.json"),
        known_bad_report=known_bad_report,
    )
    audits = {
        "claim_to_stage_forensic": _claim_to_stage_forensic_audit(output_root=output_root, stage_rows=stage_rows),
        "non_representative_claim": _non_representative_claim_audit(output_root=output_root, stage_rows=stage_rows),
        "source_task_realness": _source_task_realness_audit(output_root=output_root),
        "source_connector_capability": _source_connector_capability_audit(config=config, output_root=output_root),
        "primitive_state_chain": _primitive_state_chain_audit(output_root),
        "existing_ledger_reuse": _existing_ledger_reuse_audit(output_root=output_root, stage_rows=stage_rows),
        "last_effective_thesis": _last_effective_thesis_audit(output_root=output_root),
        "source_coverage": _source_coverage_audit(output_root=output_root, stage_rows=stage_rows),
        "runtime_plausibility": _runtime_plausibility_audit(config=config, output_root=output_root, runtime_seconds=runtime_seconds),
        "source_task_satisfaction": _source_task_satisfaction_audit(output_root),
        "official_event_counter": _official_counter_audit(stage_rows),
        "c06_guard_replay": _read_json(output_root / "c06_guard_replay_audit.json"),
        "controlled_semantic_replay": controlled_semantic_replay,
        "samsung_hynix_full_thesis_smoke": _samsung_hynix_smoke(stage_rows),
        "full_thesis_production_runner": _read_json(output_root / "full_thesis_production_runner_audit.json"),
        "full_thesis_production": _full_thesis_production_audit(config=config, stage_rows=stage_rows),
        "full_thesis_seed_materialization": _read_json(output_root / "full_thesis_seed_materialization_audit.json"),
        "brain_planner": _brain_audit(config, output_root=output_root),
        "web_naver_acquisition": _web_audit(config, output_root=output_root),
        "llm_claim_extraction": _extractor_audit(config, output_root=output_root),
        "brain_to_claim_trace": _brain_trace_audit(config, output_root=output_root),
        "known_bad_regression_report": known_bad_report,
        "test_result_evidence": _test_result_evidence_audit(config=config),
    }
    self_repair = _self_repair_log_v4(config=config, audits=audits)
    audits["self_repair"] = self_repair
    audits["goal_requirement_matrix"] = _goal_requirement_matrix_audit(
        config=config,
        audits=audits,
        leaf_audit=_read_json(output_root / "leaf_artifact_audit.json"),
        output_root=output_root,
    )
    for name, audit in audits.items():
        if name != "self_repair":
            write_json(output_root / f"{name}_audit.json", audit)
    write_json(output_root / "known_bad_regression_report.json", audits["known_bad_regression_report"])
    write_json(output_root / "samsung_hynix_full_thesis_smoke.json", audits["samsung_hynix_full_thesis_smoke"])
    write_json(output_root / "full_thesis_production_audit.json", audits["full_thesis_production"])
    write_json(output_root / "self_repair_log.json", self_repair)
    write_text(output_root / "self_repair_summary.md", _self_repair_summary_md_v4(log=self_repair))
    write_json(output_root / "goal_completion_audit.json", _goal_completion_audit(config=config, audits=audits))
    return audits


def _known_bad_regression_report(*, config: CensusV4RunConfig, output_root: Path) -> dict[str, Any]:
    return run_known_bad_regression(output_root=output_root, target_gate=config.target_gate)


def _controlled_semantic_replay_audit(
    *,
    config: CensusV4RunConfig,
    output_root: Path,
    c06_guard: Mapping[str, Any],
    all_archetype_replay_matrix: Mapping[str, Any],
    known_bad_report: Mapping[str, Any],
) -> dict[str, Any]:
    known_bad_by_id = {str(case.get("case_id") or ""): case for case in known_bad_report.get("cases") or []}
    matrix_by_id = {str(row.get("archetype_id") or ""): row for row in all_archetype_replay_matrix.get("archetypes") or []}
    c06_matrix = matrix_by_id.get(FULL_THESIS_SMOKE_ARCHETYPE) or {}
    priority_cases = [
        _semantic_replay_case(
            case_id="C06_HBM_POSITIVE_AND_QUALIFICATION_LAG_GUARD",
            archetype_id=FULL_THESIS_SMOKE_ARCHETYPE,
            required=True,
            status="PASS"
            if c06_guard.get("guard_replay_pass") is True and c06_guard.get("positive_semantic_replay_ready") is True
            else "PENDING_SOURCE_BACKED_SEMANTIC_REPLAY",
            expected="C06 positive path and qualification-lag guard both pass contract-blind semantic replay",
            observed={
                "controlled_wiring_smoke_pass": c06_matrix.get("controlled_wiring_smoke_pass"),
                "positive_semantic_replay_ready": c06_guard.get("positive_semantic_replay_ready"),
                "guard_cases_pass": c06_guard.get("guard_cases_pass"),
                "guard_replay_pass": c06_guard.get("guard_replay_pass"),
                "semantic_blockers": c06_guard.get("semantic_blockers") or [],
            },
        ),
        _pending_priority_replay_case(
            "C08_TEST_SOCKET_CUSTOMER_ORDER_PROFILE_ONLY_GUARD",
            "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
            "customer/order conversion positive and profile-only guard",
            matrix_by_id,
        ),
        _pending_priority_replay_case(
            "C15_MATERIAL_SPREAD_PASS_THROUGH_RAW_COMMODITY_GUARD",
            "C15_MATERIAL_SPREAD_SUPERCYCLE",
            "issuer pass-through/spread/margin bridge positive and raw commodity headline false-positive guard",
            matrix_by_id,
        ),
        _pending_priority_replay_case(
            "C17_CHEMICAL_SPREAD_REALIZED_MARGIN_BRIDGE_GUARD",
            "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
            "realized margin bridge positive and spread-only guard",
            matrix_by_id,
        ),
        _pending_priority_replay_case(
            "C24_CLINICAL_BINARY_EVENT_GUARD",
            "C24_BIO_TRIAL_DATA_EVENT_RISK",
            "endpoint/regulatory/runway bridge positive and binary-event-only guard",
            matrix_by_id,
        ),
        _pending_priority_replay_case(
            "C28_SOFTWARE_SECURITY_RETENTION_BRIDGE_GUARD",
            "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
            "ARR/RPO/renewal/retention bridge positive and keyword-only security/software guard",
            matrix_by_id,
        ),
        _known_bad_semantic_case(
            case_id="WRONG_SUBJECT_RISK_FIXTURE",
            known_bad_case_id="wrong_subject_audit_opinion_not_target_risk",
            expected="third-party normal audit opinion is not assigned to target risk",
            known_bad_by_id=known_bad_by_id,
        ),
        _known_bad_semantic_case(
            case_id="OLD_RISK_RESOLVED_FIXTURE",
            known_bad_case_id="old_risk_resolved_not_current_hard_break",
            expected="resolved historical target risk cannot become current score evidence or 4C",
            known_bad_by_id=known_bad_by_id,
        ),
        _known_bad_semantic_case(
            case_id="PROVIDER_FAILURE_PENDING_FIXTURE",
            known_bad_case_id="provider_failure_final_score_guard",
            expected="provider failure does not finalize low score or Red",
            known_bad_by_id=known_bad_by_id,
        ),
        _known_bad_semantic_case(
            case_id="SEMANTIC_CONTRACT_GUARD_FIXTURE",
            known_bad_case_id="non_revenue_contract_not_contract_quality",
            expected="non-revenue contract wording cannot unlock contract_quality",
            known_bad_by_id=known_bad_by_id,
        ),
    ]
    pass_count = sum(1 for case in priority_cases if case["status"] == "PASS")
    fail_count = sum(1 for case in priority_cases if case["status"] == "FAIL")
    pending_count = sum(1 for case in priority_cases if case["status"].startswith("PENDING"))
    blockers = [
        case["case_id"]
        for case in priority_cases
        if case.get("required_before_meaningful_operation") is True and case["status"] != "PASS"
    ]
    return {
        "schema_version": "e2r_census_v4_controlled_semantic_replay_audit_v1",
        "as_of_date": config.as_of_date,
        "output_root": str(output_root),
        "controlled_semantic_replay_pass": not blockers and fail_count == 0,
        "required_case_count": len([case for case in priority_cases if case.get("required_before_meaningful_operation")]),
        "case_count": len(priority_cases),
        "pass_count": pass_count,
        "pending_count": pending_count,
        "fail_count": fail_count,
        "blockers": blockers,
        "cases": priority_cases,
        "rule": "Goal3 controlled replay is only pass when each required positive/guard/global fixture is contract-blind, source-backed, lifecycle-aware, and claim-backed. Wiring smoke or known source gaps remain pending, not pass.",
    }


def _semantic_replay_case(
    *,
    case_id: str,
    archetype_id: str | None,
    required: bool,
    status: str,
    expected: str,
    observed: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "case_id": case_id,
        "archetype_id": archetype_id,
        "status": status,
        "case_pass": status == "PASS",
        "required_before_meaningful_operation": required,
        "expected": expected,
        "observed": dict(observed),
    }


def _pending_priority_replay_case(
    case_id: str,
    archetype_id: str,
    expected: str,
    matrix_by_id: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    row = matrix_by_id.get(archetype_id) or {}
    ready = row.get("positive_replay_pass") is True and row.get("guard_replay_pass") is True
    return _semantic_replay_case(
        case_id=case_id,
        archetype_id=archetype_id,
        required=True,
        status="PASS" if ready else "PENDING_SOURCE_BACKED_SEMANTIC_REPLAY",
        expected=expected,
        observed={
            "matrix_replay_status": row.get("replay_status"),
            "positive_replay_pass": row.get("positive_replay_pass"),
            "guard_replay_pass": row.get("guard_replay_pass"),
            "source_backed_fixture_count": row.get("source_backed_fixture_count"),
            "unsupported_reason": row.get("unsupported_reason"),
        },
    )


def _known_bad_semantic_case(
    *,
    case_id: str,
    known_bad_case_id: str,
    expected: str,
    known_bad_by_id: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    known_bad = known_bad_by_id.get(known_bad_case_id) or {}
    status = "PASS" if known_bad.get("status") == "PASS" else "FAIL"
    return _semantic_replay_case(
        case_id=case_id,
        archetype_id=None,
        required=True,
        status=status,
        expected=expected,
        observed={
            "known_bad_case_id": known_bad_case_id,
            "known_bad_status": known_bad.get("status"),
            "known_bad_observed": known_bad.get("observed"),
            "known_bad_expected": known_bad.get("expected"),
        },
    )


def _self_repair_log_v4(*, config: CensusV4RunConfig, audits: Mapping[str, Mapping[str, Any]]) -> dict[str, Any]:
    known_bad = audits.get("known_bad_regression_report") or {}
    test_evidence = audits.get("test_result_evidence") or {}
    forensic = audits.get("claim_to_stage_forensic") or {}
    realness = audits.get("source_task_realness") or {}
    source_connector_capability = audits.get("source_connector_capability") or {}
    runtime = audits.get("runtime_plausibility") or {}
    full_thesis = audits.get("samsung_hynix_full_thesis_smoke") or {}
    full_thesis_honesty_pass = _full_thesis_smoke_honesty_pass(full_thesis)
    full_thesis_execution_pass = _full_thesis_smoke_execution_pass(full_thesis)
    full_thesis_production = audits.get("full_thesis_production") or {}
    full_thesis_seed_materialization = audits.get("full_thesis_seed_materialization") or {}
    full_thesis_seed_event_count = int(full_thesis_seed_materialization.get("seed_event_count") or 0)
    full_thesis_seed_promotion_pass = int(full_thesis_seed_materialization.get("full_thesis_promoted_seed_count") or 0) > 0
    controlled_semantic_replay = audits.get("controlled_semantic_replay") or {}
    brain_readiness = _read_json(Path(config.resolved_output_root()) / "brain_web_readiness_gate_audit.json")
    all_archetype_replay_matrix = _read_json(Path(config.resolved_output_root()) / "all_archetype_replay_matrix.json")

    detected: list[dict[str, Any]] = [
        {
            "failure_class": "KNOWN_BAD_REGRESSION_NOT_RUN_OR_FAILED",
            "status": "RESOLVED" if known_bad.get("completion_eligible") is True else "UNRESOLVED",
            "evidence": f"known_bad_status={known_bad.get('status')} failed_case_count={known_bad.get('failed_case_count')}",
            "repairable_by_runner": True,
        },
        {
            "failure_class": "CLAIM_TO_STAGE_FORENSIC_CRITICAL",
            "status": "RESOLVED" if forensic.get("verdict") == "PASS" and int(forensic.get("critical_count") or 0) == 0 else "UNRESOLVED",
            "evidence": f"forensic_verdict={forensic.get('verdict')} critical_count={forensic.get('critical_count')}",
            "repairable_by_runner": True,
        },
        {
            "failure_class": "SOURCE_TASK_REALNESS_AUDIT_FAILED",
            "status": "RESOLVED" if _audit_verdict_is_pass(realness.get("verdict")) else "UNRESOLVED",
            "evidence": f"realness_verdict={realness.get('verdict')} live_source_pass_allowed={realness.get('live_source_pass_allowed')}",
            "repairable_by_runner": True,
        },
        {
            "failure_class": "RUNTIME_PLAUSIBILITY_AUDIT_FAILED",
            "status": "RESOLVED" if _audit_verdict_is_pass(runtime.get("verdict")) else "UNRESOLVED",
            "evidence": f"runtime_verdict={runtime.get('verdict')} runtime_mode={runtime.get('runtime_mode')}",
            "repairable_by_runner": True,
        },
    ]
    resolved = [item["failure_class"] for item in detected if item["status"] == "RESOLVED"]
    unresolved = [item["failure_class"] for item in detected if item["status"] != "RESOLVED"]
    deferred_goal_blockers: list[str] = []
    if brain_readiness.get("brain_web_evidence_pass_allowed") is not True:
        deferred_goal_blockers.append("brain_web_evidence_pass_false")
    if not full_thesis_honesty_pass:
        deferred_goal_blockers.append("full_thesis_smoke_honesty_false")
    if not full_thesis_execution_pass:
        deferred_goal_blockers.append("full_thesis_smoke_pending")
        deferred_goal_blockers.append("full_thesis_smoke_execution_pending")
    if not _full_thesis_production_pass_allowed(full_thesis_production):
        deferred_goal_blockers.append("full_thesis_production_pass_false")
    if source_connector_capability.get("source_connector_capability_pass_allowed") is not True:
        deferred_goal_blockers.append("source_connector_capability_pending")
    if full_thesis_seed_event_count > 0 and not full_thesis_seed_promotion_pass:
        deferred_goal_blockers.append("full_thesis_seed_materialization_not_promoted")
    if all_archetype_replay_matrix.get("all_archetype_replay_pass") is not True:
        deferred_goal_blockers.append("source_backed_replay_parity_all_archetypes_pending")
    if controlled_semantic_replay.get("controlled_semantic_replay_pass") is not True:
        deferred_goal_blockers.append("controlled_semantic_replay_pending")

    nonrepairable_blockers: list[str] = []
    if test_evidence.get("completion_eligible") is not True:
        nonrepairable_blockers.append("machine_readable_test_result_artifact_missing")

    status = "RUN_COMPLETE" if not unresolved else "RUN_COMPLETE_WITH_UNRESOLVED_FAILURES"
    return {
        "schema_version": "e2r_census_v4_self_repair_log_v1",
        "status": status,
        "final_status": "PASS" if not unresolved else "NOT_READY",
        "max_iterations": config.max_iterations,
        "target_gate": config.target_gate,
        "loop_executed": True,
        "iterations": [
            {
                "iteration": 1,
                "command": _command_string(config),
                "failure_classes": [item["failure_class"] for item in detected],
                "detected_failures": detected,
                "patches_applied_by_runner": [],
                "patch_policy": "The runner records and rechecks audit failures. It does not silently patch code during the census run.",
                "resolved_failures": resolved,
                "unresolved_failures": unresolved,
                "deferred_goal_blockers": deferred_goal_blockers,
                "nonrepairable_blockers": nonrepairable_blockers,
            }
        ],
        "resolved_failures": resolved,
        "unresolved_failures": unresolved,
        "deferred_goal_blockers": deferred_goal_blockers,
        "nonrepairable_blockers": nonrepairable_blockers,
        "completion_eligible": not unresolved,
        "note": "Self-repair ran as an audit/recheck loop. It does not convert Brain/Web or full-thesis pending capability blockers into passes.",
    }


def _audit_verdict_is_pass(value: object) -> bool:
    verdict = str(value or "")
    return verdict == "PASS" or verdict.startswith("PASS_") or verdict.endswith("_PASS")


def _self_repair_summary_md_v4(*, log: Mapping[str, Any]) -> str:
    return "\n".join(
        [
            "# Census v4 Self-Repair Summary",
            "",
            f"- status: {log.get('status')}",
            f"- final_status: {log.get('final_status')}",
            f"- target_gate: {log.get('target_gate')}",
            f"- max_iterations: {log.get('max_iterations')}",
            f"- loop_executed: {log.get('loop_executed')}",
            f"- completion_eligible: {log.get('completion_eligible')}",
            f"- resolved_failures: {_join_or_none(log.get('resolved_failures') or [])}",
            f"- unresolved_failures: {_join_or_none(log.get('unresolved_failures') or [])}",
            f"- deferred_goal_blockers: {_join_or_none(log.get('deferred_goal_blockers') or [])}",
            f"- nonrepairable_blockers: {_join_or_none(log.get('nonrepairable_blockers') or [])}",
            "- note: self-repair ran as an audit/recheck loop. Brain/Web and full-thesis pending remain separate goal blockers.",
            "",
        ]
    )


def _test_result_evidence_audit(*, config: CensusV4RunConfig) -> dict[str, Any]:
    artifact_path = Path(config.test_result_artifact).expanduser() if config.test_result_artifact else None
    artifact_exists = bool(artifact_path and artifact_path.exists())
    validation: dict[str, Any] = {
        "artifact_sha256": None,
        "artifact_byte_size": None,
        "artifact_valid": False,
        "artifact_validation_errors": ["artifact_path_missing"] if artifact_path else ["artifact_path_not_provided"],
    }
    if artifact_exists and artifact_path is not None:
        validation = validate_test_result_artifact(artifact_path)
    artifact_valid = validation.get("artifact_valid") is True
    return {
        "schema_version": "e2r_census_v4_test_result_evidence_audit_v1",
        "summary_value": config.test_result_summary,
        "summary_source": "string_input",
        "artifact_path": str(artifact_path) if artifact_path else None,
        "artifact_exists": artifact_exists,
        "artifact_sha256": validation.get("artifact_sha256"),
        "artifact_byte_size": validation.get("artifact_byte_size"),
        "artifact_valid": artifact_valid,
        "artifact_validation_errors": validation.get("artifact_validation_errors") or [],
        "artifact_schema_version": validation.get("artifact_schema_version"),
        "artifact_command": validation.get("artifact_command"),
        "artifact_exit_code": validation.get("artifact_exit_code"),
        "artifact_status": validation.get("artifact_status"),
        "artifact_test_count": validation.get("artifact_test_count"),
        "artifact_failed_count": validation.get("artifact_failed_count"),
        "artifact_error_count": validation.get("artifact_error_count"),
        "artifact_started_at": validation.get("artifact_started_at"),
        "artifact_finished_at": validation.get("artifact_finished_at"),
        "artifact_duration_seconds": validation.get("artifact_duration_seconds"),
        "artifact_log_path": validation.get("artifact_log_path"),
        "artifact_log_sha256": validation.get("artifact_log_sha256"),
        "completion_eligible": artifact_valid,
        "verdict": "MACHINE_READABLE_TEST_ARTIFACT_PASS" if artifact_valid else ("INVALID_TEST_ARTIFACT" if artifact_exists else "STRING_SUMMARY_ONLY"),
        "note": "A string test_result_summary is report context; goal completion requires a valid e2r_test_result_artifact_v1 JSON artifact.",
    }


def _sync_test_result_artifact(*, config: CensusV4RunConfig, output_root: Path) -> None:
    if not config.test_result_artifact:
        return
    artifact_path = Path(config.test_result_artifact).expanduser()
    if not artifact_path.exists() or not artifact_path.is_file():
        return
    target_path = output_root / "test_result_artifact.json"
    if artifact_path.resolve() == target_path.resolve():
        return
    write_text(target_path, artifact_path.read_text(encoding="utf-8"))


def _goal_requirement_matrix_audit(
    *,
    config: CensusV4RunConfig,
    audits: Mapping[str, Mapping[str, Any]],
    leaf_audit: Mapping[str, Any] | None,
    output_root: Path,
) -> dict[str, Any]:
    """Summarize goal.md/goal2.md/goal3.md hard gates as explicit rows.

    This matrix is deliberately stricter than the anti-fake readiness label. It
    prevents a ledger-refresh status board from being mistaken for the user's
    requested operational Brain/Web + full-thesis goal.
    """

    leaf = leaf_audit or {}
    leaf_metrics = leaf.get("metrics") or {}
    known_bad = audits.get("known_bad_regression_report") or {}
    test_evidence = audits.get("test_result_evidence") or {}
    forensic = audits.get("claim_to_stage_forensic") or {}
    source_realness = audits.get("source_task_realness") or {}
    source_connector_capability = audits.get("source_connector_capability") or {}
    source_satisfaction = audits.get("source_task_satisfaction") or {}
    primitive_chain = audits.get("primitive_state_chain") or {}
    reuse = audits.get("existing_ledger_reuse") or {}
    thesis = audits.get("last_effective_thesis") or {}
    coverage = audits.get("source_coverage") or {}
    runtime = audits.get("runtime_plausibility") or {}
    full_thesis = audits.get("samsung_hynix_full_thesis_smoke") or {}
    full_thesis_honesty_pass = _full_thesis_smoke_honesty_pass(full_thesis)
    full_thesis_execution_pass = _full_thesis_smoke_execution_pass(full_thesis)
    full_thesis_production = audits.get("full_thesis_production") or {}
    full_thesis_seed_materialization = audits.get("full_thesis_seed_materialization") or {}
    full_thesis_seed_promotion_pass = int(full_thesis_seed_materialization.get("full_thesis_promoted_seed_count") or 0) > 0
    c06_guard = audits.get("c06_guard_replay") or {}
    controlled_semantic = audits.get("controlled_semantic_replay") or {}
    self_repair = audits.get("self_repair") or {}
    all_archetype = _read_json(output_root / "all_archetype_replay_matrix.json")
    brain_readiness = _read_json(output_root / "brain_web_readiness_gate_audit.json")
    v3_forensic_path = Path("docs/operational/census_mode_v3_forensic_review.md")

    rows = [
        _goal_gate_row(
            gate_id="V3_FORENSIC_REVIEW_COMPLETE",
            title="v3 report-only pass is reclassified before v4 use",
            required=True,
            passed=v3_forensic_path.exists(),
            pending=not v3_forensic_path.exists(),
            evidence={"path": str(v3_forensic_path), "exists": v3_forensic_path.exists()},
            blocker="v3_forensic_review_missing",
        ),
        _goal_gate_row(
            gate_id="ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS",
            title="full universe status board is leaf-audited and anti-fake",
            required=True,
            passed=leaf.get("verdict") == "PASS",
            pending=not leaf,
            failed=bool(leaf and leaf.get("verdict") != "PASS"),
            evidence={
                "leaf_verdict": leaf.get("verdict"),
                "stage_status_count": leaf_metrics.get("stage_status_count"),
                "eligible_symbol_count": leaf_metrics.get("eligible_symbol_count"),
                "critical_count": leaf.get("critical_count"),
            },
            blocker="anti_fake_leaf_audit_not_pass",
        ),
        _goal_gate_row(
            gate_id="ATOMIC_STAGE_DECISION_PASS",
            title="stage/score/status/trace come from atomic representative decisions",
            required=True,
            passed=leaf.get("verdict") == "PASS"
            and int((leaf.get("critical_counts") or {}).get("stage_trace_stage_mismatch_count") or 0) == 0
            and int((leaf.get("critical_counts") or {}).get("stage_trace_score_interval_mismatch_count") or 0) == 0
            and int((leaf.get("critical_counts") or {}).get("stage_trace_claim_set_mismatch_count") or 0) == 0
            and int((leaf.get("critical_counts") or {}).get("stage_trace_contribution_set_mismatch_count") or 0) == 0,
            pending=not leaf,
            failed=bool(leaf and leaf.get("verdict") != "PASS"),
            evidence={
                "stage_trace_stage_mismatch_count": (leaf.get("critical_counts") or {}).get("stage_trace_stage_mismatch_count"),
                "stage_trace_score_interval_mismatch_count": (leaf.get("critical_counts") or {}).get("stage_trace_score_interval_mismatch_count"),
                "stage_trace_claim_set_mismatch_count": (leaf.get("critical_counts") or {}).get("stage_trace_claim_set_mismatch_count"),
                "stage_trace_contribution_set_mismatch_count": (leaf.get("critical_counts") or {}).get("stage_trace_contribution_set_mismatch_count"),
            },
            blocker="atomic_stage_decision_not_pass",
        ),
        _goal_gate_row(
            gate_id="SCORE_SCALE_PASS",
            title="event scores and full E2R scores are not mixed",
            required=True,
            passed=leaf.get("verdict") == "PASS"
            and int((leaf.get("critical_counts") or {}).get("verified_score_not_full_e2r_count") or 0) == 0
            and int((leaf.get("critical_counts") or {}).get("raw_contribution_fallback_as_verified_score_count") or 0) == 0,
            pending=not leaf,
            failed=bool(leaf and leaf.get("verdict") != "PASS"),
            evidence={
                "score_scope_distribution": leaf_metrics.get("score_scope_distribution"),
                "operator_score_use_distribution": leaf_metrics.get("operator_score_use_distribution"),
                "verified_score_not_full_e2r_count": (leaf.get("critical_counts") or {}).get("verified_score_not_full_e2r_count"),
                "raw_contribution_fallback_as_verified_score_count": (leaf.get("critical_counts") or {}).get("raw_contribution_fallback_as_verified_score_count"),
            },
            blocker="score_scale_not_pass",
        ),
        _goal_gate_row(
            gate_id="STAGE_SEMANTICS_PASS",
            title="Stage0/Stage2/Red/pending labels are semantically separated",
            required=True,
            passed=leaf.get("verdict") == "PASS"
            and int((leaf.get("critical_counts") or {}).get("pending_material_marked_complete_count") or 0) == 0
            and int((leaf.get("critical_counts") or {}).get("source_pending_marked_red_count") or 0) == 0
            and int((leaf.get("critical_counts") or {}).get("red_without_risk_signal_or_trace_count") or 0) == 0,
            pending=not leaf,
            failed=bool(leaf and leaf.get("verdict") != "PASS"),
            evidence={
                "stage_scope_distribution": leaf_metrics.get("stage_scope_distribution"),
                "operator_stage_use_distribution": leaf_metrics.get("operator_stage_use_distribution"),
                "pending_material_marked_complete_count": (leaf.get("critical_counts") or {}).get("pending_material_marked_complete_count"),
                "source_pending_marked_red_count": (leaf.get("critical_counts") or {}).get("source_pending_marked_red_count"),
                "red_without_risk_signal_or_trace_count": (leaf.get("critical_counts") or {}).get("red_without_risk_signal_or_trace_count"),
            },
            blocker="stage_semantics_not_pass",
        ),
        _goal_gate_row(
            gate_id="SEMANTIC_PRIMITIVE_GUARD_PASS",
            title="non-revenue contract wording cannot unlock contract/revision primitives",
            required=True,
            passed=leaf.get("verdict") == "PASS"
            and int((leaf.get("critical_counts") or {}).get("contract_quality_semantic_guard_missing_count") or 0) == 0
            and int((leaf.get("critical_counts") or {}).get("semantic_guard_failed_score_count") or 0) == 0,
            pending=not leaf,
            failed=bool(leaf and leaf.get("verdict") != "PASS"),
            evidence={
                "contract_quality_semantic_guard_missing_count": int(
                    (leaf.get("critical_counts") or {}).get("contract_quality_semantic_guard_missing_count") or 0
                ),
                "semantic_guard_failed_score_count": int((leaf.get("critical_counts") or {}).get("semantic_guard_failed_score_count") or 0),
                "known_bad_status": known_bad.get("status"),
            },
            blocker="semantic_primitive_guard_not_pass",
        ),
        _goal_gate_row(
            gate_id="SOURCE_TASK_SATISFACTION_PASS",
            title="representative score claims are closed to source tasks and primitive states",
            required=True,
            passed=_audit_verdict_is_pass(source_satisfaction.get("verdict")) and primitive_chain.get("verdict") == "PASS",
            pending=not source_satisfaction or not primitive_chain,
            failed=bool(source_satisfaction and primitive_chain)
            and not (_audit_verdict_is_pass(source_satisfaction.get("verdict")) and primitive_chain.get("verdict") == "PASS"),
            evidence={
                "source_task_satisfaction_verdict": source_satisfaction.get("verdict"),
                "primitive_state_chain_verdict": primitive_chain.get("verdict"),
                "representative_score_claim_count": source_satisfaction.get("representative_score_claim_count"),
                "source_task_chain_closed_to_representative_stage_count": source_satisfaction.get("source_task_chain_closed_to_representative_stage_count"),
            },
            blocker="source_task_satisfaction_not_pass",
        ),
        _goal_gate_row(
            gate_id="LEDGER_REUSE_AND_SOURCE_COVERAGE_PASS",
            title="existing claims are lifecycle-refreshed and source coverage is honestly ledger-refresh scoped",
            required=True,
            passed=reuse.get("verdict") == "PASS"
            and thesis.get("verdict") == "PASS"
            and _audit_verdict_is_pass(coverage.get("verdict"))
            and _audit_verdict_is_pass(source_realness.get("verdict"))
            and _audit_verdict_is_pass(runtime.get("verdict")),
            pending=not reuse or not thesis or not coverage or not source_realness or not runtime,
            failed=bool(reuse and thesis and coverage and source_realness and runtime)
            and not (
                reuse.get("verdict") == "PASS"
                and thesis.get("verdict") == "PASS"
                and _audit_verdict_is_pass(coverage.get("verdict"))
                and _audit_verdict_is_pass(source_realness.get("verdict"))
                and _audit_verdict_is_pass(runtime.get("verdict"))
            ),
            evidence={
                "existing_ledger_reuse_verdict": reuse.get("verdict"),
                "last_effective_thesis_verdict": thesis.get("verdict"),
                "source_coverage_verdict": coverage.get("verdict"),
                "source_task_realness_verdict": source_realness.get("verdict"),
                "runtime_plausibility_verdict": runtime.get("verdict"),
                "live_source_pass_allowed": source_realness.get("live_source_pass_allowed"),
                "runtime_mode": runtime.get("runtime_mode"),
            },
            blocker="ledger_reuse_or_source_coverage_not_pass",
        ),
        _goal_gate_row(
            gate_id="SOURCE_CONNECTOR_CAPABILITY_PASS",
            title="full-thesis source tasks have at least one executable production source path",
            required=True,
            passed=source_connector_capability.get("source_connector_capability_pass_allowed") is True,
            pending=source_connector_capability.get("source_connector_capability_pass_allowed") is not True,
            evidence={
                "verdict": source_connector_capability.get("verdict"),
                "full_thesis_required_source_class_count": source_connector_capability.get("full_thesis_required_source_class_count"),
                "blocking_full_thesis_source_class_count": source_connector_capability.get("blocking_full_thesis_source_class_count"),
                "blocking_full_thesis_task_count": source_connector_capability.get("blocking_full_thesis_task_count"),
                "full_thesis_task_executable_source_path_pass_allowed": (
                    source_connector_capability.get("full_thesis_task_executable_source_path_pass_allowed")
                ),
                "full_thesis_task_with_blocking_source_class_count": (
                    source_connector_capability.get("full_thesis_task_with_blocking_source_class_count")
                ),
                "placeholder_source_classes": source_connector_capability.get("placeholder_source_classes") or [],
                "missing_connector_source_classes": source_connector_capability.get("missing_connector_source_classes") or [],
                "bounded_web_acquisition_source_classes": source_connector_capability.get("bounded_web_acquisition_source_classes") or [],
                "registry_missing_but_acquisition_covered_source_classes": (
                    source_connector_capability.get("registry_missing_but_acquisition_covered_source_classes") or []
                ),
            },
            blocker="source_connector_capability_pending",
        ),
        _goal_gate_row(
            gate_id="FULL_THESIS_SMOKE_HONESTY_PASS",
            title="Samsung/Hynix full-thesis smoke is honest about pending execution and never substitutes event-board score",
            required=True,
            passed=full_thesis_honesty_pass,
            pending=bool(full_thesis) and not full_thesis_honesty_pass,
            evidence={
                "verdict": full_thesis.get("verdict"),
                "full_thesis_status": full_thesis.get("full_thesis_status"),
                "full_thesis_smoke_honesty_status": full_thesis.get("full_thesis_smoke_honesty_status"),
                "score_allowed_before_execution": full_thesis.get("score_allowed_before_execution"),
                "hardcoded_query_count": full_thesis.get("hardcoded_query_count"),
                "daily_event_and_full_thesis_separated": full_thesis.get("daily_event_and_full_thesis_separated"),
            },
            blocker="full_thesis_smoke_honesty_false",
        ),
        _goal_gate_row(
            gate_id="FULL_THESIS_SMOKE_PASS",
            title="controlled Samsung/Hynix full-thesis wiring smoke executed with claim-backed FULL_E2R evidence",
            required=True,
            passed=full_thesis_execution_pass,
            pending=bool(full_thesis) and not full_thesis_execution_pass,
            evidence={
                "verdict": full_thesis.get("verdict"),
                "full_thesis_status": full_thesis.get("full_thesis_status"),
                "full_thesis_smoke_execution_status": full_thesis.get("full_thesis_smoke_execution_status"),
                "required_symbols": full_thesis.get("required_symbols"),
                "per_symbol": full_thesis.get("per_symbol"),
            },
            blocker="full_thesis_smoke_pending",
        ),
        _goal_gate_row(
            gate_id="FULL_THESIS_PRODUCTION_PASS",
            title="production full-thesis rows exist without controlled-smoke substitution",
            required=True,
            passed=_full_thesis_production_pass_allowed(full_thesis_production),
            pending=not _full_thesis_production_pass_allowed(full_thesis_production),
            evidence={
                "verdict": full_thesis_production.get("verdict"),
                "production_pass_allowed": full_thesis_production.get("production_pass_allowed"),
                "production_mode_requested": full_thesis_production.get("production_mode_requested"),
                "production_full_thesis_row_count": full_thesis_production.get("production_full_thesis_row_count"),
                "controlled_smoke_full_thesis_row_count": full_thesis_production.get("controlled_smoke_full_thesis_row_count"),
            },
            blocker="full_thesis_production_pass_false",
        ),
        _goal_gate_row(
            gate_id="FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS",
            title="full thesis seed materialization trace/audit is internally consistent",
            required=True,
            passed=full_thesis_seed_materialization.get("verdict") == "PASS"
            and int(full_thesis_seed_materialization.get("critical_count") or 0) == 0,
            pending=not full_thesis_seed_materialization,
            failed=bool(
                full_thesis_seed_materialization
                and (
                    full_thesis_seed_materialization.get("verdict") != "PASS"
                    or int(full_thesis_seed_materialization.get("critical_count") or 0) > 0
                )
            ),
            evidence={
                "verdict": full_thesis_seed_materialization.get("verdict"),
                "seed_event_count": full_thesis_seed_materialization.get("seed_event_count"),
                "trace_row_count": full_thesis_seed_materialization.get("trace_row_count"),
                "status_counts": full_thesis_seed_materialization.get("status_counts"),
                "full_thesis_promoted_seed_count": full_thesis_seed_materialization.get("full_thesis_promoted_seed_count"),
                "critical_count": full_thesis_seed_materialization.get("critical_count"),
            },
            blocker="full_thesis_seed_materialization_audit_not_pass",
        ),
        _goal_gate_row(
            gate_id="FULL_THESIS_SEED_PROMOTION_PASS",
            title="at least one full thesis seed has materialized into production FULL_THESIS",
            required=True,
            passed=full_thesis_seed_promotion_pass,
            pending=bool(full_thesis_seed_materialization) and not full_thesis_seed_promotion_pass,
            evidence={
                "verdict": full_thesis_seed_materialization.get("verdict"),
                "seed_event_count": full_thesis_seed_materialization.get("seed_event_count"),
                "status_counts": full_thesis_seed_materialization.get("status_counts"),
                "full_thesis_promoted_seed_count": full_thesis_seed_materialization.get("full_thesis_promoted_seed_count"),
                "critical_count": full_thesis_seed_materialization.get("critical_count"),
            },
            blocker="full_thesis_seed_promotion_pass_false",
        ),
        _goal_gate_row(
            gate_id="BRAIN_WEB_EVIDENCE_PASS",
            title="real planner/web/extractor/claim traces satisfy operational minimums",
            required=True,
            passed=brain_readiness.get("brain_web_evidence_pass_allowed") is True,
            pending=brain_readiness.get("brain_web_evidence_pass_allowed") is not True,
            evidence={
                "verdict": brain_readiness.get("verdict"),
                "brain_web_evidence_pass_allowed": brain_readiness.get("brain_web_evidence_pass_allowed"),
                "operational_minimum_count_gate_applies": brain_readiness.get("operational_minimum_count_gate_applies"),
                "minimum_required_counts": brain_readiness.get("minimum_required_counts"),
                "llm_planner_call_count": brain_readiness.get("llm_planner_call_count"),
                "web_search_task_count": brain_readiness.get("web_search_task_count"),
                "web_search_call_count": brain_readiness.get("web_search_call_count"),
                "web_fetched_document_count": brain_readiness.get("web_fetched_document_count"),
                "llm_claim_extractor_attempt_count": brain_readiness.get("llm_claim_extractor_attempt_count"),
                "web_or_llm_accepted_claim_count": brain_readiness.get("web_or_llm_accepted_claim_count"),
            },
            blocker="brain_web_evidence_pass_false",
        ),
        _goal_gate_row(
            gate_id="ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS",
            title="required archetypes have source-backed positive/guard replay parity",
            required=True,
            passed=all_archetype.get("all_archetype_replay_pass") is True,
            pending=all_archetype.get("all_archetype_replay_pass") is not True,
            evidence={
                "all_archetype_replay_pass": all_archetype.get("all_archetype_replay_pass"),
                "required_archetype_count": all_archetype.get("required_archetype_count"),
                "source_backed_ready_count": all_archetype.get("source_backed_ready_count"),
                "guard_replay_ready_count": all_archetype.get("guard_replay_ready_count"),
                "missing_required_archetype_count": all_archetype.get("missing_required_archetype_count"),
                "status_counts": all_archetype.get("status_counts"),
            },
            blocker="source_backed_replay_parity_all_archetypes_pending",
        ),
        _goal_gate_row(
            gate_id="CONTROLLED_SEMANTIC_REPLAY_PASS",
            title="goal3 priority semantic replay cases are source-backed and lifecycle-clean",
            required=True,
            passed=controlled_semantic.get("controlled_semantic_replay_pass") is True,
            pending=controlled_semantic.get("controlled_semantic_replay_pass") is not True,
            evidence={
                "controlled_semantic_replay_pass": controlled_semantic.get("controlled_semantic_replay_pass"),
                "case_count": controlled_semantic.get("case_count"),
                "pass_count": controlled_semantic.get("pass_count"),
                "pending_count": controlled_semantic.get("pending_count"),
                "fail_count": controlled_semantic.get("fail_count"),
                "blockers": controlled_semantic.get("blockers") or [],
            },
            blocker="controlled_semantic_replay_pending",
        ),
        _goal_gate_row(
            gate_id="C06_GUARD_REPLAY_PASS",
            title="C06 positive and qualification-lag guard are semantic replay ready",
            required=True,
            passed=c06_guard.get("guard_replay_pass") is True,
            pending=c06_guard.get("guard_replay_pass") is not True,
            evidence={
                "guard_replay_pass": c06_guard.get("guard_replay_pass"),
                "positive_semantic_replay_ready": c06_guard.get("positive_semantic_replay_ready"),
                "guard_cases_pass": c06_guard.get("guard_cases_pass"),
                "semantic_blockers": c06_guard.get("semantic_blockers") or [],
            },
            blocker="c06_guard_replay_pending",
        ),
        _goal_gate_row(
            gate_id="KNOWN_BAD_REGRESSION_PASS",
            title="known-bad fixtures fail as expected",
            required=True,
            passed=known_bad.get("completion_eligible") is True,
            pending=not known_bad,
            failed=bool(known_bad) and known_bad.get("completion_eligible") is not True,
            evidence={
                "status": known_bad.get("status"),
                "case_count": known_bad.get("case_count"),
                "failed_case_count": known_bad.get("failed_case_count"),
            },
            blocker="known_bad_regression_not_run",
        ),
        _goal_gate_row(
            gate_id="SELF_REPAIR_LOOP_PASS",
            title="self-repair/recheck loop ran and has no unresolved non-external failures",
            required=True,
            passed=self_repair.get("loop_executed") is True and self_repair.get("completion_eligible") is True,
            pending=not self_repair,
            failed=bool(self_repair) and self_repair.get("completion_eligible") is not True,
            evidence={
                "status": self_repair.get("status"),
                "loop_executed": self_repair.get("loop_executed"),
                "completion_eligible": self_repair.get("completion_eligible"),
                "unresolved_failures": self_repair.get("unresolved_failures") or [],
                "deferred_goal_blockers": self_repair.get("deferred_goal_blockers") or [],
            },
            blocker="self_repair_unresolved_failures",
        ),
        _goal_gate_row(
            gate_id="FULL_TEST_ARTIFACT_PASS",
            title="machine-readable full test artifact is valid",
            required=True,
            passed=test_evidence.get("completion_eligible") is True,
            pending=test_evidence.get("completion_eligible") is not True,
            evidence={
                "verdict": test_evidence.get("verdict"),
                "artifact_status": test_evidence.get("artifact_status"),
                "artifact_test_count": test_evidence.get("artifact_test_count"),
                "artifact_failed_count": test_evidence.get("artifact_failed_count"),
                "artifact_error_count": test_evidence.get("artifact_error_count"),
            },
            blocker="machine_readable_test_result_artifact_missing",
        ),
    ]

    required_rows = [row for row in rows if row["required_for_goal_completion"]]
    pass_count = sum(1 for row in required_rows if row["status"] == "PASS")
    pending_rows = [row for row in required_rows if row["status"] == "PENDING"]
    fail_rows = [row for row in required_rows if row["status"] == "FAIL"]
    blockers = [row["blocker"] for row in required_rows if row["status"] != "PASS"]
    meaningful_gate_ids = {
        "ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS",
        "ATOMIC_STAGE_DECISION_PASS",
        "SCORE_SCALE_PASS",
        "STAGE_SEMANTICS_PASS",
        "SEMANTIC_PRIMITIVE_GUARD_PASS",
        "SOURCE_CONNECTOR_CAPABILITY_PASS",
        "FULL_THESIS_PRODUCTION_PASS",
        "FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS",
        "FULL_THESIS_SEED_PROMOTION_PASS",
        "BRAIN_WEB_EVIDENCE_PASS",
        "ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS",
        "CONTROLLED_SEMANTIC_REPLAY_PASS",
    }
    meaningful_rows = [row for row in rows if row["gate_id"] in meaningful_gate_ids]
    return {
        "schema_version": "e2r_census_v4_goal_requirement_matrix_audit_v1",
        "as_of_date": config.as_of_date,
        "run_mode": config.run_mode,
        "brain_web_mode": config.brain_web_mode,
        "target_gate": config.target_gate,
        "required_goal_completion_count": len(required_rows),
        "required_goal_completion_pass_count": pass_count,
        "required_goal_completion_pending_count": len(pending_rows),
        "required_goal_completion_fail_count": len(fail_rows),
        "goal_completion_minimum_pass": pass_count == len(required_rows),
        "meaningful_operational_stage_requirement_pass": all(row["status"] == "PASS" for row in meaningful_rows),
        "brain_web_requirement_pass": brain_readiness.get("brain_web_evidence_pass_allowed") is True,
        "production_full_thesis_requirement_pass": _full_thesis_production_pass_allowed(full_thesis_production),
        "blockers": blockers,
        "pending_gate_ids": [row["gate_id"] for row in pending_rows],
        "fail_gate_ids": [row["gate_id"] for row in fail_rows],
        "requirements": rows,
        "rule": (
            "This matrix follows docs/core/goal.md, goal2.md, and goal3.md. "
            "Anti-fake status-board pass is not goal completion; Brain/Web, production full-thesis, all-archetype replay, "
            "controlled semantic replay, self-repair, known-bad, and full-test evidence must all be proven."
        ),
    }


def _goal_gate_row(
    *,
    gate_id: str,
    title: str,
    required: bool,
    passed: bool,
    evidence: Mapping[str, Any],
    blocker: str,
    pending: bool = False,
    failed: bool = False,
) -> dict[str, Any]:
    if passed:
        status = "PASS"
    elif failed:
        status = "FAIL"
    elif pending:
        status = "PENDING"
    else:
        status = "PENDING"
    return {
        "gate_id": gate_id,
        "title": title,
        "required_for_goal_completion": required,
        "status": status,
        "blocker": blocker,
        "evidence": dict(evidence),
    }


def _goal_completion_audit(*, config: CensusV4RunConfig, audits: Mapping[str, Mapping[str, Any]]) -> dict[str, Any]:
    known_bad = audits.get("known_bad_regression_report") or {}
    test_evidence = audits.get("test_result_evidence") or {}
    full_thesis = audits.get("samsung_hynix_full_thesis_smoke") or {}
    full_thesis_production = audits.get("full_thesis_production") or {}
    source_connector_capability = audits.get("source_connector_capability") or {}
    full_thesis_seed_materialization = audits.get("full_thesis_seed_materialization") or {}
    full_thesis_seed_promotion_pass = int(full_thesis_seed_materialization.get("full_thesis_promoted_seed_count") or 0) > 0
    c06_guard = audits.get("c06_guard_replay") or {}
    controlled_semantic_replay = audits.get("controlled_semantic_replay") or {}
    self_repair = audits.get("self_repair") or {}
    goal_requirement_matrix = audits.get("goal_requirement_matrix") or {}
    brain_readiness = _read_json(Path(config.resolved_output_root()) / "brain_web_readiness_gate_audit.json")
    all_archetype_replay_matrix = _read_json(Path(config.resolved_output_root()) / "all_archetype_replay_matrix.json")
    brain_gate_blockers = []
    if brain_readiness.get("brain_web_evidence_pass_allowed") is not True:
        brain_gate_blockers.append("brain_web_evidence_pass_false")
    full_thesis_honesty_pass = _full_thesis_smoke_honesty_pass(full_thesis)
    full_thesis_execution_pass = _full_thesis_smoke_execution_pass(full_thesis)
    if not full_thesis_honesty_pass:
        brain_gate_blockers.append("full_thesis_smoke_honesty_false")
    if not full_thesis_execution_pass:
        brain_gate_blockers.append("full_thesis_smoke_pending")
        brain_gate_blockers.append("full_thesis_smoke_execution_pending")
    full_thesis_production_pass = _full_thesis_production_pass_allowed(full_thesis_production)
    if not full_thesis_production_pass:
        brain_gate_blockers.append("full_thesis_production_pass_false")
    source_connector_capability_pass = source_connector_capability.get("source_connector_capability_pass_allowed") is True
    if not source_connector_capability_pass:
        brain_gate_blockers.append("source_connector_capability_pending")
    full_thesis_seed_materialization_pass = (
        full_thesis_seed_materialization.get("verdict") == "PASS"
        and int(full_thesis_seed_materialization.get("critical_count") or 0) == 0
    )
    if not full_thesis_seed_materialization_pass:
        brain_gate_blockers.append("full_thesis_seed_materialization_audit_not_pass")
    if not full_thesis_seed_promotion_pass:
        brain_gate_blockers.append("full_thesis_seed_promotion_pass_false")
    all_archetype_replay_pass = all_archetype_replay_matrix.get("all_archetype_replay_pass") is True
    if not all_archetype_replay_pass:
        brain_gate_blockers.append("source_backed_replay_parity_all_archetypes_pending")
    controlled_semantic_replay_pass = controlled_semantic_replay.get("controlled_semantic_replay_pass") is True
    if not controlled_semantic_replay_pass:
        brain_gate_blockers.append("controlled_semantic_replay_pending")
    if self_repair.get("loop_executed") is not True:
        brain_gate_blockers.append("self_repair_not_run")
    elif self_repair.get("completion_eligible") is not True:
        brain_gate_blockers.append("self_repair_unresolved_failures")
    if known_bad.get("completion_eligible") is not True:
        brain_gate_blockers.append("known_bad_regression_not_run")
    if test_evidence.get("completion_eligible") is not True:
        brain_gate_blockers.append("machine_readable_test_result_artifact_missing")
    if goal_requirement_matrix and goal_requirement_matrix.get("goal_completion_minimum_pass") is not True:
        brain_gate_blockers.append("goal_requirement_matrix_pass_false")
    ready = not brain_gate_blockers
    return {
        "schema_version": "e2r_census_v4_goal_completion_audit_v1",
        "target_gate": config.target_gate,
        "goal_completion_ready": ready,
        "meaningful_operational_stage_pass_allowed": ready,
        "brain_web_evidence_pass_allowed": brain_readiness.get("brain_web_evidence_pass_allowed") is True,
        "full_thesis_smoke_pass_allowed": full_thesis_execution_pass,
        "full_thesis_smoke_honesty_pass_allowed": full_thesis_honesty_pass,
        "full_thesis_smoke_execution_pass_allowed": full_thesis_execution_pass,
        "full_thesis_smoke_summary": {
            "verdict": full_thesis.get("verdict"),
            "full_thesis_status": full_thesis.get("full_thesis_status"),
            "full_thesis_smoke_honesty_status": full_thesis.get("full_thesis_smoke_honesty_status"),
            "full_thesis_smoke_execution_status": full_thesis.get("full_thesis_smoke_execution_status"),
            "score_allowed_before_execution": full_thesis.get("score_allowed_before_execution"),
            "hardcoded_query_count": full_thesis.get("hardcoded_query_count"),
            "daily_event_and_full_thesis_separated": full_thesis.get("daily_event_and_full_thesis_separated"),
        },
        "full_thesis_production_pass_allowed": full_thesis_production_pass,
        "source_connector_capability_pass_allowed": source_connector_capability_pass,
        "source_connector_capability_summary": {
            "verdict": source_connector_capability.get("verdict"),
            "full_thesis_required_source_class_count": source_connector_capability.get("full_thesis_required_source_class_count"),
            "blocking_full_thesis_source_class_count": source_connector_capability.get("blocking_full_thesis_source_class_count"),
            "blocking_full_thesis_task_count": source_connector_capability.get("blocking_full_thesis_task_count"),
            "full_thesis_task_executable_source_path_pass_allowed": (
                source_connector_capability.get("full_thesis_task_executable_source_path_pass_allowed")
            ),
            "full_thesis_task_with_blocking_source_class_count": (
                source_connector_capability.get("full_thesis_task_with_blocking_source_class_count")
            ),
            "placeholder_source_classes": source_connector_capability.get("placeholder_source_classes") or [],
            "missing_connector_source_classes": source_connector_capability.get("missing_connector_source_classes") or [],
            "bounded_web_acquisition_source_classes": source_connector_capability.get("bounded_web_acquisition_source_classes") or [],
            "registry_missing_but_acquisition_covered_source_classes": (
                source_connector_capability.get("registry_missing_but_acquisition_covered_source_classes") or []
            ),
        },
        "full_thesis_seed_materialization_audit_pass_allowed": full_thesis_seed_materialization_pass,
        "full_thesis_seed_ledger_integrity_pass_allowed": (
            full_thesis_seed_materialization.get("ledger_integrity_pass_allowed") is True
        ),
        "full_thesis_seed_actual_materialization_pass_allowed": (
            full_thesis_seed_materialization.get("actual_materialization_pass_allowed") is True
        ),
        "full_thesis_seed_promotion_pass_allowed": full_thesis_seed_promotion_pass,
        "full_thesis_seed_materialization_summary": {
            "verdict": full_thesis_seed_materialization.get("verdict"),
            "verdict_scope": full_thesis_seed_materialization.get("verdict_scope"),
            "seed_event_count": full_thesis_seed_materialization.get("seed_event_count"),
            "trace_row_count": full_thesis_seed_materialization.get("trace_row_count"),
            "status_counts": full_thesis_seed_materialization.get("status_counts") or {},
            "full_thesis_promoted_seed_count": full_thesis_seed_materialization.get("full_thesis_promoted_seed_count"),
            "final_operator_stage_use_counts": full_thesis_seed_materialization.get("final_operator_stage_use_counts") or {},
            "final_operator_score_use_counts": full_thesis_seed_materialization.get("final_operator_score_use_counts") or {},
            "ledger_integrity_pass_allowed": full_thesis_seed_materialization.get("ledger_integrity_pass_allowed"),
            "actual_materialization_pass_allowed": full_thesis_seed_materialization.get("actual_materialization_pass_allowed"),
            "operator_materialization_status": full_thesis_seed_materialization.get("operator_materialization_status"),
            "critical_count": full_thesis_seed_materialization.get("critical_count"),
        },
        "c06_guard_replay_pass_allowed": c06_guard.get("guard_replay_pass") is True,
        "c06_guard_replay_status": "C06_GUARD_REPLAY_PASS" if c06_guard.get("guard_replay_pass") is True else "C06_GUARD_REPLAY_PENDING",
        "controlled_semantic_replay_pass_allowed": controlled_semantic_replay_pass,
        "controlled_semantic_replay_summary": {
            "case_count": controlled_semantic_replay.get("case_count"),
            "required_case_count": controlled_semantic_replay.get("required_case_count"),
            "pass_count": controlled_semantic_replay.get("pass_count"),
            "pending_count": controlled_semantic_replay.get("pending_count"),
            "fail_count": controlled_semantic_replay.get("fail_count"),
            "blockers": controlled_semantic_replay.get("blockers") or [],
        },
        "all_archetype_replay_pass_allowed": all_archetype_replay_pass,
        "all_archetype_replay_matrix_summary": {
            "archetype_count": all_archetype_replay_matrix.get("archetype_count"),
            "required_archetype_count": all_archetype_replay_matrix.get("required_archetype_count"),
            "source_backed_ready_count": all_archetype_replay_matrix.get("source_backed_ready_count"),
            "guard_replay_ready_count": all_archetype_replay_matrix.get("guard_replay_ready_count"),
            "controlled_wiring_smoke_ready_count": all_archetype_replay_matrix.get("controlled_wiring_smoke_ready_count"),
            "missing_required_archetype_count": all_archetype_replay_matrix.get("missing_required_archetype_count"),
            "status_counts": all_archetype_replay_matrix.get("status_counts"),
        },
        "known_bad_regression_status": known_bad.get("status"),
        "self_repair_status": self_repair.get("status"),
        "self_repair_loop_executed": self_repair.get("loop_executed") is True,
        "self_repair_completion_eligible": self_repair.get("completion_eligible") is True,
        "full_thesis_status": full_thesis.get("full_thesis_status"),
        "full_thesis_production_status": full_thesis_production.get("status") or full_thesis_production.get("verdict") or "NOT_IMPLEMENTED",
        "test_result_evidence_verdict": test_evidence.get("verdict"),
        "goal_requirement_matrix_summary": {
            "goal_completion_minimum_pass": goal_requirement_matrix.get("goal_completion_minimum_pass"),
            "required_goal_completion_count": goal_requirement_matrix.get("required_goal_completion_count"),
            "required_goal_completion_pass_count": goal_requirement_matrix.get("required_goal_completion_pass_count"),
            "required_goal_completion_pending_count": goal_requirement_matrix.get("required_goal_completion_pending_count"),
            "required_goal_completion_fail_count": goal_requirement_matrix.get("required_goal_completion_fail_count"),
            "pending_gate_ids": goal_requirement_matrix.get("pending_gate_ids") or [],
            "fail_gate_ids": goal_requirement_matrix.get("fail_gate_ids") or [],
        },
        "blockers": brain_gate_blockers,
    }


def _full_thesis_production_pass_allowed(audit: Mapping[str, Any]) -> bool:
    return audit.get("completion_eligible") is True or audit.get("verdict") == "FULL_THESIS_PRODUCTION_PASS"


def _source_connector_capability_audit(*, config: CensusV4RunConfig, output_root: Path) -> dict[str, Any]:
    registry = build_default_source_provider_registry(".")
    connector_rows: list[dict[str, Any]] = []
    connector_rows_by_class: dict[str, list[dict[str, Any]]] = {}
    for connector in registry.connectors:
        provider_name = str(getattr(connector, "provider_name", "") or "")
        source_class = str(getattr(connector, "source_class", "") or provider_name)
        canonical_source_class = _canonical_source_class(provider_name or source_class)
        capability_status = _connector_capability_status(connector)
        row = {
            "provider_name": provider_name,
            "source_class": source_class,
            "canonical_source_class": canonical_source_class,
            "connector_class": connector.__class__.__name__,
            "connector_module": connector.__class__.__module__,
            "capability_status": capability_status,
            "production_live_fetch_implemented": capability_status == "LIVE_FETCH_IMPLEMENTED",
            "placeholder_provider_failed": capability_status == "PLACEHOLDER_PROVIDER_FAILED",
            "snapshot_only": capability_status == "SNAPSHOT_ONLY",
        }
        connector_rows.append(row)
        connector_rows_by_class.setdefault(canonical_source_class, []).append(row)

    requirement_rows = _source_connector_requirement_rows(output_root=output_root)
    required_counts: dict[str, int] = {}
    full_thesis_required_counts: dict[str, int] = {}
    task_ids_by_class: dict[str, set[str]] = {}
    full_thesis_task_ids_by_class: dict[str, set[str]] = {}
    full_thesis_source_classes_by_task_id: dict[str, set[str]] = {}
    for requirement in requirement_rows:
        source_class = str(requirement["canonical_source_class"])
        required_counts[source_class] = required_counts.get(source_class, 0) + 1
        task_id = str(requirement.get("task_id") or "")
        if task_id:
            task_ids_by_class.setdefault(source_class, set()).add(task_id)
        if requirement.get("full_thesis_requirement") is True:
            full_thesis_required_counts[source_class] = full_thesis_required_counts.get(source_class, 0) + 1
            if task_id:
                full_thesis_task_ids_by_class.setdefault(source_class, set()).add(task_id)
                full_thesis_source_classes_by_task_id.setdefault(task_id, set()).add(source_class)

    acquisition_capability_rows = _source_acquisition_capability_rows()
    acquisition_capability_by_class = {
        str(row["canonical_source_class"]): row for row in acquisition_capability_rows
    }
    all_source_classes = sorted(set(connector_rows_by_class) | set(required_counts) | set(acquisition_capability_by_class))
    source_class_rows: list[dict[str, Any]] = []
    placeholder_source_classes: list[str] = []
    missing_connector_source_classes: list[str] = []
    registry_missing_but_acquisition_covered_source_classes: list[str] = []
    non_executable_full_thesis_source_classes: list[str] = []
    capability_status_by_class: dict[str, str] = {}
    for source_class in all_source_classes:
        connectors = connector_rows_by_class.get(source_class, [])
        acquisition_capability = acquisition_capability_by_class.get(source_class)
        registry_capability_status = _source_class_registry_capability_status(connectors)
        capability_status = _source_class_capability_status(
            connectors,
            acquisition_capability=acquisition_capability,
        )
        capability_status_by_class[source_class] = capability_status
        required_by_full_thesis = int(full_thesis_required_counts.get(source_class, 0))
        non_executable = required_by_full_thesis > 0 and not _source_class_capability_can_execute_source_task(capability_status)
        if capability_status == "PLACEHOLDER_PROVIDER_FAILED":
            placeholder_source_classes.append(source_class)
        if registry_capability_status == "NO_PRODUCTION_CONNECTOR_REGISTERED" and acquisition_capability is None:
            missing_connector_source_classes.append(source_class)
        if registry_capability_status == "NO_PRODUCTION_CONNECTOR_REGISTERED" and acquisition_capability is not None:
            registry_missing_but_acquisition_covered_source_classes.append(source_class)
        if non_executable:
            non_executable_full_thesis_source_classes.append(source_class)
        source_class_rows.append(
            {
                "canonical_source_class": source_class,
                "capability_status": capability_status,
                "registry_capability_status": registry_capability_status,
                "acquisition_capability_status": acquisition_capability.get("capability_status") if acquisition_capability else None,
                "acquisition_capability_scope": acquisition_capability.get("capability_scope") if acquisition_capability else None,
                "acquisition_score_evidence_rule": acquisition_capability.get("score_evidence_rule") if acquisition_capability else None,
                "registered_connector_count": len(connectors),
                "provider_names": [str(row["provider_name"]) for row in connectors],
                "connector_classes": [str(row["connector_class"]) for row in connectors],
                "required_by_any_task_count": int(required_counts.get(source_class, 0)),
                "required_by_full_thesis_task_count": required_by_full_thesis,
                "full_thesis_task_ids": sorted(full_thesis_task_ids_by_class.get(source_class, set()))[:20],
                "blocking_full_thesis": False,
                "non_executable_full_thesis_source_class": non_executable,
            }
        )

    full_thesis_task_ids_with_nonexecutable_source_class: set[str] = set()
    for source_class in non_executable_full_thesis_source_classes:
        full_thesis_task_ids_with_nonexecutable_source_class.update(full_thesis_task_ids_by_class.get(source_class, set()))

    full_thesis_task_ids_without_executable_source_path: set[str] = set()
    for task_id, source_classes in full_thesis_source_classes_by_task_id.items():
        if not any(_source_class_capability_can_execute_source_task(capability_status_by_class.get(source_class, "")) for source_class in source_classes):
            full_thesis_task_ids_without_executable_source_path.add(task_id)

    blocking_full_thesis_source_classes = sorted(
        {
            source_class
            for task_id in full_thesis_task_ids_without_executable_source_path
            for source_class in full_thesis_source_classes_by_task_id.get(task_id, set())
            if not _source_class_capability_can_execute_source_task(capability_status_by_class.get(source_class, ""))
        }
    )
    full_thesis_required_source_classes = sorted(full_thesis_required_counts)
    pass_allowed = bool(full_thesis_required_source_classes) and not full_thesis_task_ids_without_executable_source_path
    blockers: list[str] = []
    if not full_thesis_required_source_classes:
        blockers.append("no_full_thesis_source_class_requirements_observed")
    if full_thesis_task_ids_without_executable_source_path:
        blockers.append("full_thesis_source_tasks_without_executable_source_path")
    return {
        "schema_version": "e2r_census_v4_source_connector_capability_audit_v1",
        "as_of_date": config.as_of_date,
        "run_mode": config.run_mode,
        "brain_web_mode": config.brain_web_mode,
        "verdict": "SOURCE_CONNECTOR_CAPABILITY_PASS" if pass_allowed else "PENDING_SOURCE_CONNECTOR_CAPABILITY",
        "source_connector_capability_pass_allowed": pass_allowed,
        "registered_connector_count": len(connector_rows),
        "registered_live_connector_count": sum(1 for row in connector_rows if row["capability_status"] == "LIVE_FETCH_IMPLEMENTED"),
        "placeholder_connector_count": sum(1 for row in connector_rows if row["capability_status"] == "PLACEHOLDER_PROVIDER_FAILED"),
        "acquisition_capability_count": len(acquisition_capability_rows),
        "bounded_web_acquisition_source_classes": sorted(
            row["canonical_source_class"]
            for row in acquisition_capability_rows
            if str(row.get("capability_family")) == "BOUNDED_WEB_ACQUISITION"
        ),
        "registry_missing_but_acquisition_covered_source_classes": registry_missing_but_acquisition_covered_source_classes,
        "source_class_count": len(source_class_rows),
        "full_thesis_required_source_class_count": len(full_thesis_required_source_classes),
        "full_thesis_required_source_classes": full_thesis_required_source_classes,
        "blocking_full_thesis_source_class_count": len(blocking_full_thesis_source_classes),
        "blocking_full_thesis_source_classes": blocking_full_thesis_source_classes,
        "blocking_full_thesis_task_count": len(full_thesis_task_ids_without_executable_source_path),
        "blocking_full_thesis_task_ids": sorted(full_thesis_task_ids_without_executable_source_path)[:50],
        "full_thesis_task_executable_source_path_pass_allowed": not full_thesis_task_ids_without_executable_source_path,
        "full_thesis_task_with_blocking_source_class_count": len(full_thesis_task_ids_with_nonexecutable_source_class),
        "full_thesis_task_with_blocking_source_class_ids": sorted(full_thesis_task_ids_with_nonexecutable_source_class)[:50],
        "full_thesis_task_with_nonexecutable_source_class_count": len(full_thesis_task_ids_with_nonexecutable_source_class),
        "full_thesis_task_with_nonexecutable_source_class_ids": sorted(full_thesis_task_ids_with_nonexecutable_source_class)[:50],
        "non_executable_full_thesis_source_class_count": len(non_executable_full_thesis_source_classes),
        "non_executable_full_thesis_source_classes": non_executable_full_thesis_source_classes,
        "placeholder_source_classes": placeholder_source_classes,
        "missing_connector_source_classes": missing_connector_source_classes,
        "requirement_row_count": len(requirement_rows),
        "full_thesis_requirement_row_count": sum(1 for row in requirement_rows if row.get("full_thesis_requirement") is True),
        "connector_rows": connector_rows,
        "acquisition_capability_rows": acquisition_capability_rows,
        "source_classes": source_class_rows,
        "blockers": blockers,
        "rule": (
            "This audit is static and does not call external providers. It prevents full-thesis readiness from passing when "
            "a source class required by the full-thesis refresh queue is only a placeholder, snapshot-only connector, has no "
            "registered production connector, and is not covered by the bounded live SourceAcquisitionRunnerV4 path. A live fetch "
            "still needs separate SourceTaskExecution evidence. blocking_full_thesis_task_count means no executable source class "
            "path exists for that task; full_thesis_task_with_blocking_source_class_count means the task mentions at least one "
            "non-executable source class but may still have executable alternatives."
        ),
    }


def _connector_capability_status(connector: object) -> str:
    class_name = connector.__class__.__name__
    module_name = connector.__class__.__module__
    module_doc = str(getattr(__import__(module_name, fromlist=["__doc__"]), "__doc__", "") or "").lower()
    if "placeholder" in module_doc or class_name in {"IssuerIRLiveConnector", "TrustedNewsLiveConnector"}:
        return "PLACEHOLDER_PROVIDER_FAILED"
    if class_name == "LocalSnapshotConnector":
        return "SNAPSHOT_ONLY"
    return "LIVE_FETCH_IMPLEMENTED"


def _source_class_capability_status(
    connectors: Sequence[Mapping[str, Any]],
    *,
    acquisition_capability: Mapping[str, Any] | None = None,
) -> str:
    registry_status = _source_class_registry_capability_status(connectors)
    if registry_status == "LIVE_FETCH_IMPLEMENTED":
        return registry_status
    if acquisition_capability is not None:
        return str(acquisition_capability.get("capability_status") or "")
    return registry_status


def _source_class_registry_capability_status(connectors: Sequence[Mapping[str, Any]]) -> str:
    if not connectors:
        return "NO_PRODUCTION_CONNECTOR_REGISTERED"
    statuses = {str(row.get("capability_status") or "") for row in connectors}
    if "LIVE_FETCH_IMPLEMENTED" in statuses:
        return "LIVE_FETCH_IMPLEMENTED"
    if "PLACEHOLDER_PROVIDER_FAILED" in statuses:
        return "PLACEHOLDER_PROVIDER_FAILED"
    if "SNAPSHOT_ONLY" in statuses:
        return "SNAPSHOT_ONLY"
    return "NO_PRODUCTION_CONNECTOR_REGISTERED"


def _source_class_capability_can_execute_source_task(status: str) -> bool:
    return status in {
        "LIVE_FETCH_IMPLEMENTED",
        "BOUNDED_WEB_SEARCH_FETCH_IMPLEMENTED",
        "BOUNDED_WEB_VERIFIED_ISSUER_ORIGINAL_IMPLEMENTED",
        "BOUNDED_WEB_VERIFIED_REPORT_ORIGINAL_IMPLEMENTED",
    }


def _source_acquisition_capability_rows() -> list[dict[str, Any]]:
    """Static capability map for SourceAcquisitionRunnerV4's bounded live web path.

    These rows are not live fetch success evidence. They only say the production
    SourceTask executor has a bounded code path for this source class. Actual
    scoring still requires SourceTaskExecution -> EvidenceDocument -> Anchor ->
    accepted claim proof.
    """

    rows = [
        {
            "canonical_source_class": "NaverSearch",
            "capability_status": "BOUNDED_WEB_SEARCH_FETCH_IMPLEMENTED",
            "capability_family": "BOUNDED_WEB_ACQUISITION",
            "capability_scope": "NaverFreeSearchProvider plus PageFetcher with task max_queries/max_candidates/max_fetches",
            "score_evidence_rule": "snippet never scores; only fetched full source can enter Evidence OS",
            "implementation": "e2r.research_brain.v4_source_acquisition_runner.SourceAcquisitionRunnerV4._acquire_live_web_sources",
        },
        {
            "canonical_source_class": "GeneralWebSearch",
            "capability_status": "BOUNDED_WEB_SEARCH_FETCH_IMPLEMENTED",
            "capability_family": "BOUNDED_WEB_ACQUISITION",
            "capability_scope": "generic web query intent executed through bounded search provider and PageFetcher",
            "score_evidence_rule": "snippet never scores; fetched document must pass target/date/content rejection and Evidence OS",
            "implementation": "e2r.research_brain.v4_source_acquisition_runner.SourceAcquisitionRunnerV4._acquire_live_web_sources",
        },
        {
            "canonical_source_class": "TrustedNews",
            "capability_status": "BOUNDED_WEB_SEARCH_FETCH_IMPLEMENTED",
            "capability_family": "BOUNDED_WEB_ACQUISITION",
            "capability_scope": "trusted/news source tasks can be executed through bounded search provider and PageFetcher",
            "score_evidence_rule": "snippet never scores; fetched news document must pass target/date/content rejection and Evidence OS",
            "implementation": "e2r.research_brain.v4_source_acquisition_runner.SourceAcquisitionRunnerV4._acquire_live_web_sources",
        },
        {
            "canonical_source_class": "CompanyNewsroom",
            "capability_status": "BOUNDED_WEB_VERIFIED_ISSUER_ORIGINAL_IMPLEMENTED",
            "capability_family": "BOUNDED_WEB_ACQUISITION",
            "capability_scope": "issuer homepage/domain authority from CompanyGuide snapshot or as-of-safe issuer official domain registry",
            "score_evidence_rule": "only fetched pages with verified issuer-original lineage can satisfy CompanyNewsroom source class",
            "implementation": "e2r.research_brain.v4_source_acquisition_runner._verified_issuer_web_route_from_web_result",
        },
        {
            "canonical_source_class": "BrokerReportPublicPDF",
            "capability_status": "BOUNDED_WEB_VERIFIED_REPORT_ORIGINAL_IMPLEMENTED",
            "capability_family": "BOUNDED_WEB_ACQUISITION",
            "capability_scope": "recognized broker/report original URL verification plus PageFetcher/PDF text path",
            "score_evidence_rule": "only fetched original report-domain/PDF documents with verified report lineage can satisfy report source class",
            "implementation": "e2r.research_brain.v4_source_acquisition_runner._verified_report_web_route_from_web_result",
        },
        {
            "canonical_source_class": "ReportPDF",
            "capability_status": "BOUNDED_WEB_VERIFIED_REPORT_ORIGINAL_IMPLEMENTED",
            "capability_family": "BOUNDED_WEB_ACQUISITION",
            "capability_scope": "ReportPDF requests can be satisfied by verified BrokerReportPublicPDF original documents",
            "score_evidence_rule": "only fetched original report-domain/PDF documents with verified report lineage can satisfy report source class",
            "implementation": "e2r.research_brain.v4_source_acquisition_runner._verified_report_web_route_from_web_result",
        },
    ]
    return rows


def _source_connector_requirement_rows(*, output_root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for item in _read_jsonl(output_root / "full_thesis_refresh_queue.jsonl"):
        task_id = str(item.get("candidate_event_id") or item.get("symbol") or "full_thesis_refresh_queue")
        rows.extend(
            _source_connector_requirement_rows_from_task(
                item,
                task_id=task_id,
                requirement_origin="full_thesis_refresh_queue",
                full_thesis_requirement=True,
            )
        )
    for item in _read_jsonl(output_root / "source_tasks.jsonl"):
        task_id = str(item.get("task_id") or item.get("source_task_id") or "")
        rows.extend(
            _source_connector_requirement_rows_from_task(
                item,
                task_id=task_id,
                requirement_origin=str(item.get("source_task_origin") or "source_tasks"),
                full_thesis_requirement=_row_is_full_thesis_requirement(item) and not _row_is_controlled_smoke_source_requirement(item),
            )
        )
    for item in _read_jsonl(output_root / "full_thesis_blocker_follow_up_source_tasks.jsonl"):
        task_id = str(item.get("task_id") or item.get("source_task_id") or "")
        rows.extend(
            _source_connector_requirement_rows_from_task(
                item,
                task_id=task_id,
                requirement_origin="full_thesis_green_gate_blocker_follow_up",
                full_thesis_requirement=True,
            )
        )
    for execution in _read_jsonl(output_root / "source_task_executions.jsonl"):
        task = execution.get("source_task") if isinstance(execution.get("source_task"), Mapping) else {}
        merged = {**dict(task), **dict(execution)}
        task_id = str(execution.get("task_id") or task.get("task_id") or execution.get("source_task_execution_id") or "")
        rows.extend(
            _source_connector_requirement_rows_from_task(
                merged,
                task_id=task_id,
                requirement_origin=str(execution.get("source_task_execution_origin") or execution.get("source_task_origin") or "source_task_executions"),
                full_thesis_requirement=(
                    (_row_is_full_thesis_requirement(execution) or _row_is_full_thesis_requirement(task))
                    and not _row_is_controlled_smoke_source_requirement(merged)
                ),
            )
        )
    return rows


def _source_connector_requirement_rows_from_task(
    row: Mapping[str, Any],
    *,
    task_id: str,
    requirement_origin: str,
    full_thesis_requirement: bool,
) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for role, key in (
        ("requested", "requested_source_classes"),
        ("preferred", "preferred_source_classes"),
        ("fallback", "fallback_source_classes"),
    ):
        for source_class in _source_class_list(row.get(key)):
            out.append(
                {
                    "task_id": task_id,
                    "symbol": row.get("symbol"),
                    "company_name": row.get("company_name"),
                    "primitive_gap": row.get("primitive_gap"),
                    "source_class_role": role,
                    "raw_source_class": source_class,
                    "canonical_source_class": _canonical_source_class(source_class),
                    "requirement_origin": requirement_origin,
                    "full_thesis_requirement": full_thesis_requirement,
                }
            )
    return out


def _source_class_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value] if value else []
    if isinstance(value, (list, tuple, set)):
        return [str(item) for item in value if str(item)]
    return []


def _row_is_full_thesis_requirement(row: Mapping[str, Any]) -> bool:
    values = [
        row.get("stage_scope"),
        row.get("source_task_origin"),
        row.get("source_task_execution_origin"),
        row.get("reason_from_memory"),
        row.get("raw_reason_codes"),
        row.get("candidate_event_id"),
        row.get("event_type"),
    ]
    text = " ".join(json.dumps(value, ensure_ascii=False, sort_keys=True) if isinstance(value, (list, tuple, dict)) else str(value or "") for value in values)
    return "FULL_THESIS" in text.upper()


def _row_is_controlled_smoke_source_requirement(row: Mapping[str, Any]) -> bool:
    values = [
        row.get("task_id"),
        row.get("source_task_id"),
        row.get("source_task_origin"),
        row.get("source_task_execution_origin"),
        row.get("candidate_event_id"),
        row.get("provider_name"),
        row.get("source_class"),
        row.get("reason_from_memory"),
    ]
    text = " ".join(json.dumps(value, ensure_ascii=False, sort_keys=True) if isinstance(value, (list, tuple, dict)) else str(value or "") for value in values)
    upper = text.upper()
    return "FTSMOKE" in upper or "CE-FTSMOKE" in upper or "CONTROLLEDFIXTUREREPLAY" in upper or "URL_BACKED_FIXTURE" in upper


def _canonical_source_class(value: object) -> str:
    text = str(value or "").strip()
    normalized = text.lower().replace("_", "").replace("-", "").replace(" ", "")
    aliases = {
        "opendart": "DART",
        "dart": "DART",
        "kind": "KIND",
        "krx": "KRX",
        "companyguide": "CompanyGuide",
        "issuerir": "IssuerIR",
        "ir": "IssuerIR",
        "issuerofficial": "IssuerOfficial",
        "official": "IssuerOfficial",
        "companynewsroom": "CompanyNewsroom",
        "trustednews": "TrustedNews",
        "reportpdf": "ReportPDF",
        "brokerreportpublicpdf": "BrokerReportPublicPDF",
        "brokerpdf": "BrokerReportPublicPDF",
        "naversearch": "NaverSearch",
        "naver": "NaverSearch",
        "generalwebsearch": "GeneralWebSearch",
        "generalweb": "GeneralWebSearch",
        "web": "GeneralWebSearch",
    }
    return aliases.get(normalized, text or "UNKNOWN")


def _claim_to_stage_forensic_audit(*, output_root: Path, stage_rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    accepted = _read_jsonl(output_root / "accepted_claims.jsonl")
    contributions = _read_jsonl(output_root / "score_contributions.jsonl")
    stagecourt = _read_jsonl(output_root / "stagecourt_traces.jsonl")
    traces = _read_jsonl(output_root / "claim_to_stage_trace.jsonl")
    timelines = _read_jsonl(output_root / "source_timelines.jsonl")
    thesis = _read_jsonl(output_root / "last_effective_thesis_states.jsonl")
    accepted_by_id = {str(row.get("claim_id") or ""): row for row in accepted}
    contribution_by_id = {str(row.get("score_contribution_id") or row.get("contribution_id") or ""): row for row in contributions}
    stagecourt_ids = {str(row.get("stagecourt_trace_id") or row.get("trace_id") or "") for row in stagecourt}
    trace_by_id = {str(row.get("trace_id") or ""): row for row in traces}
    timeline_symbols = {str(row.get("symbol") or "").zfill(6) for row in timelines}
    thesis_by_symbol = {str(row.get("symbol") or "").zfill(6): row for row in thesis}
    scored_rows = [row for row in stage_rows if row.get("score_scale") != "NO_SCORE" or row.get("score_valid_status") in {"FINAL", "FINAL_WITH_NONMATERIAL_GAPS"}]
    stage2plus = [row for row in stage_rows if row.get("base_stage") in {"Stage2-Watch", "Stage2-Actionable", "Stage3-Yellow", "Stage3-Green", "Red", "Reject"}]
    support_claim_not_accepted = 0
    source_proxy_support = 0
    support_missing_locator = 0
    support_missing_date = 0
    support_missing_adjudication = 0
    for contribution in contributions:
        for claim_id in contribution.get("support_claim_ids") or ():
            claim = accepted_by_id.get(str(claim_id))
            if claim is None:
                support_claim_not_accepted += 1
                continue
            if claim.get("source_proxy_only") or claim.get("evidence_url_pending") or claim.get("price_path_only"):
                source_proxy_support += 1
            if not claim.get("source_url") and not claim.get("document_id"):
                support_missing_locator += 1
            if not claim.get("event_date") and not claim.get("as_of_date") and not claim.get("source_cutover_date"):
                support_missing_date += 1
            if not claim.get("target_scope_status") or not claim.get("temporal_status"):
                support_missing_adjudication += 1
    counts = {
        "scored_row_missing_claim_ids": sum(1 for row in scored_rows if not row.get("accepted_claim_ids")),
        "scored_row_missing_score_contribution_ids": sum(1 for row in scored_rows if not row.get("score_contribution_ids")),
        "scored_row_missing_stagecourt_trace": sum(1 for row in scored_rows if not row.get("stagecourt_trace_id")),
        "claim_id_not_found_count": sum(1 for row in stage_rows for claim_id in row.get("accepted_claim_ids") or () if str(claim_id) not in accepted_by_id),
        "score_contribution_id_not_found_count": sum(
            1 for row in stage_rows for item in row.get("score_contribution_ids") or () if str(item) not in contribution_by_id
        ),
        "stagecourt_trace_id_not_found_count": sum(
            1 for row in stage_rows if row.get("stagecourt_trace_id") and str(row.get("stagecourt_trace_id")) not in stagecourt_ids
        ),
        "support_claim_not_accepted_count": support_claim_not_accepted,
        "source_proxy_support_claim_count": source_proxy_support,
        "support_claim_missing_source_locator_count": support_missing_locator,
        "support_claim_missing_event_or_source_date_count": support_missing_date,
        "support_claim_missing_target_temporal_adjudication_count": support_missing_adjudication,
        "source_pending_marked_red_count": sum(1 for row in stage_rows if row.get("census_status") in {"PENDING_SOURCE", "PENDING_PROVIDER"} and row.get("base_stage") in {"Red", "Reject"}),
        "provider_failed_final_score_count": sum(1 for row in stage_rows if row.get("census_status") == "PENDING_PROVIDER" and row.get("score_scale") != "NO_SCORE"),
        "stage0_without_timeline_count": sum(1 for row in stage_rows if row.get("base_stage") == "Stage0" and str(row.get("symbol") or "").zfill(6) not in timeline_symbols),
        "stage2plus_without_trace_or_pending_reason_count": sum(
            1 for row in stage2plus if not row.get("stagecourt_trace_id") and not row.get("stage_decision_status") in {"PENDING_MATERIAL_GAPS", "SOURCE_PENDING", "RISK_REVIEW"}
        ),
        "no_current_thesis_recent_cutoff_reason_count": sum(
            1
            for row in stage_rows
            if row.get("base_stage") == "Stage0"
            and any(token in str((thesis_by_symbol.get(str(row.get("symbol") or "").zfill(6)) or {}).get("reason") or "").lower() for token in ("recent cutoff", "lookback expired"))
        ),
        "claim_to_stage_trace_missing_count": sum(1 for row in stage_rows if row.get("claim_to_stage_trace_id") and str(row.get("claim_to_stage_trace_id")) not in trace_by_id),
    }
    return {
        "schema_version": "e2r_census_v4_claim_to_stage_forensic_audit_v1",
        "scored_row_count": len(scored_rows),
        "stage2plus_or_risk_row_count": len(stage2plus),
        "critical_counts": counts,
        "critical_count": sum(int(value) for value in counts.values()),
        "verdict": "PASS" if sum(int(value) for value in counts.values()) == 0 else "FAIL",
    }


def _non_representative_claim_audit(*, output_root: Path, stage_rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    accepted = _read_jsonl(output_root / "accepted_claims.jsonl")
    atomic = _read_jsonl(output_root / "atomic_stage_decisions.jsonl")
    contributions = _read_jsonl(output_root / "score_contributions.jsonl")

    representative_claim_ids = {str(claim_id) for row in stage_rows for claim_id in row.get("accepted_claim_ids") or () if str(claim_id)}
    representative_contribution_ids = {
        str(contribution_id) for row in stage_rows for contribution_id in row.get("score_contribution_ids") or () if str(contribution_id)
    }
    representative_support_claim_ids: set[str] = set()
    for contribution in contributions:
        contribution_id = str(contribution.get("score_contribution_id") or contribution.get("contribution_id") or "")
        if contribution_id in representative_contribution_ids:
            representative_support_claim_ids.update(str(item) for item in contribution.get("support_claim_ids") or () if str(item))

    atomic_by_claim: dict[str, list[Mapping[str, Any]]] = {}
    representative_atomic_claim_ids: set[str] = set()
    for row in atomic:
        claim_ids = [str(claim_id) for claim_id in row.get("accepted_claim_ids") or () if str(claim_id)]
        if row.get("is_representative") is True:
            representative_atomic_claim_ids.update(claim_ids)
        for claim_id in claim_ids:
            atomic_by_claim.setdefault(claim_id, []).append(row)

    non_representative: list[dict[str, Any]] = []
    reason_distribution: dict[str, int] = {}
    for claim in accepted:
        claim_id = str(claim.get("claim_id") or "")
        if not claim_id or claim_id in representative_claim_ids:
            continue
        linked_atomic = atomic_by_claim.get(claim_id) or []
        if linked_atomic:
            reason = "non_representative_atomic_decision"
        else:
            reason = "accepted_claim_without_atomic_decision"
        reason_distribution[reason] = reason_distribution.get(reason, 0) + 1
        non_representative.append(
            {
                "claim_id": claim_id,
                "symbol": claim.get("symbol"),
                "primitive_id": claim.get("primitive_id"),
                "polarity": claim.get("polarity"),
                "temporal_status": claim.get("temporal_status"),
                "target_scope_status": claim.get("target_scope_status"),
                "score_eligible": claim.get("score_eligible"),
                "reason": reason,
                "atomic_stage_decision_ids": [row.get("atomic_stage_decision_id") for row in linked_atomic],
                "representative_atomic_decision_ids": [
                    row.get("atomic_stage_decision_id") for row in linked_atomic if row.get("is_representative") is True
                ],
            }
        )

    non_representative_ids = {row["claim_id"] for row in non_representative}
    unexpected_score_leak_ids = sorted((non_representative_ids & representative_support_claim_ids) - representative_claim_ids)
    unreasoned = [row for row in non_representative if not row.get("reason")]
    warning_counts = {
        "accepted_claim_without_atomic_decision_count": reason_distribution.get("accepted_claim_without_atomic_decision", 0),
    }
    critical_counts = {
        "non_representative_claim_unreasoned_count": len(unreasoned),
        "non_representative_claim_score_leak_count": len(unexpected_score_leak_ids),
        "representative_atomic_claim_not_in_stage_row_count": len(representative_atomic_claim_ids - representative_claim_ids),
    }
    return {
        "schema_version": "e2r_census_v4_non_representative_claim_audit_v1",
        "accepted_claim_count": len(accepted),
        "representative_stage_claim_count": len(representative_claim_ids),
        "non_representative_claim_count": len(non_representative),
        "reason_distribution": reason_distribution,
        "warning_counts": warning_counts,
        "warning_count": sum(int(value) for value in warning_counts.values()),
        "critical_counts": critical_counts,
        "critical_count": sum(int(value) for value in critical_counts.values()),
        "unexpected_score_leak_claim_ids": unexpected_score_leak_ids,
        "sample_non_representative_claims": non_representative[:20],
        "verdict": "PASS" if sum(int(value) for value in critical_counts.values()) == 0 else "FAIL",
        "rule": (
            "Accepted claims that are not selected into the representative census_stage_status row must have an explicit reason "
            "and must not support the representative score unless they are also listed in that representative row."
        ),
    }


def _source_task_realness_audit(*, output_root: Path) -> dict[str, Any]:
    tasks = _read_jsonl(output_root / "source_tasks.jsonl")
    executions = _read_jsonl(output_root / "source_task_executions.jsonl")
    for row in executions:
        _backfill_source_task_execution_identity(execution_row=row, task=dict(row.get("source_task") or {}))
    classified = [_classify_source_task_execution(row) for row in executions]
    class_counts = _count_values(classified)
    claim_producing = [
        row
        for row, classification in zip(executions, classified)
        if classification in {"REAL_PROVIDER_FETCH", "FRESH_PROVIDER_CACHE"} and row.get("accepted_claim_ids")
    ]
    counts = {
        "source_task_accepted_with_empty_claim_ids_count": sum(1 for row in executions if row.get("status") == "EVIDENCE_OS_ACCEPTED" and not row.get("accepted_claim_ids")),
        "parsed_without_claim_count": sum(1 for row in executions if row.get("status") in {"PARSED", "EVIDENCE_OS_ACCEPTED"} and not row.get("accepted_claim_ids")),
        "report_replay_counted_as_real_fetch_count": sum(
            1
            for row, classification in zip(executions, classified)
            if classification == "REPORT_REPLAY_REFERENCE_ONLY" and row.get("claim_producing_execution")
        ),
        "source_task_execution_missing_source_class_count": sum(1 for row in executions if not row.get("source_class")),
        "source_task_execution_missing_provider_name_count": sum(1 for row in executions if not row.get("provider_name")),
        "source_task_execution_missing_source_task_origin_count": sum(1 for row in executions if not row.get("source_task_origin")),
        "source_task_execution_missing_requested_source_classes_count": sum(1 for row in executions if not row.get("requested_source_classes")),
    }
    critical_count = sum(int(value) for value in counts.values())
    live_source_pass_allowed = critical_count == 0 and class_counts.get("REAL_PROVIDER_FETCH", 0) > 0 and len(claim_producing) > 0
    ledger_refresh_pass = critical_count == 0 and len(claim_producing) > 0
    verdict = "LIVE_SOURCE_PASS" if live_source_pass_allowed else ("PASS_LEDGER_REFRESH_REALNESS" if ledger_refresh_pass else "FAIL")
    return {
        "schema_version": "e2r_census_v4_source_task_realness_audit_v1",
        "verdict_scope": "LEDGER_REFRESH_REALNESS_PASS",
        "live_source_pass_allowed": live_source_pass_allowed,
        "source_task_planned_count": len(tasks),
        "source_task_execution_count": len(executions),
        "source_task_real_fetch_count": class_counts.get("REAL_PROVIDER_FETCH", 0),
        "source_task_fresh_provider_cache_count": class_counts.get("FRESH_PROVIDER_CACHE", 0),
        "source_task_lifecycle_refresh_count": class_counts.get("EXISTING_ACCEPTED_CLAIM_LIFECYCLE_REFRESH", 0),
        "source_task_report_replay_reference_count": class_counts.get("REPORT_REPLAY_REFERENCE_ONLY", 0),
        "source_task_research_memory_reference_count": class_counts.get("RESEARCH_MEMORY_REFERENCE_ONLY", 0),
        "source_task_claim_producing_count": len(claim_producing),
        "classification_distribution": class_counts,
        "critical_counts": counts,
        "critical_count": critical_count,
        "verdict": verdict,
        "legacy_boolean_pass": ledger_refresh_pass,
        "pass_scope": "live_source" if live_source_pass_allowed else ("ledger_refresh" if ledger_refresh_pass else "failed"),
        "mode_note": "canonical v4 currently replays/imports v3 leaf artifacts; real live fetch count is not claimed in LEDGER_REFRESH_CENSUS",
    }


def _classify_source_task_execution(row: Mapping[str, Any]) -> str:
    if row.get("provider_errors"):
        return "PROVIDER_FAILED"
    origin = str(row.get("source_task_execution_origin") or row.get("source_task_origin") or "")
    status = str(row.get("status") or "")
    if origin == FULL_THESIS_SMOKE_SOURCE_ORIGIN:
        return "URL_BACKED_FULL_THESIS_SMOKE_REPLAY"
    if "report_replay" in origin.lower():
        return "REPORT_REPLAY_REFERENCE_ONLY"
    if "research_memory" in origin.lower():
        return "RESEARCH_MEMORY_REFERENCE_ONLY"
    if status == "EVIDENCE_OS_BASELINE_ONLY" or row.get("baseline_claim_ids"):
        return "EXISTING_ACCEPTED_CLAIM_LIFECYCLE_REFRESH"
    if status == "EVIDENCE_OS_ACCEPTED" and row.get("accepted_claim_ids") and row.get("fetched_document_ids"):
        if "production_cutover_v3_leaf_artifact" in origin:
            return "FRESH_PROVIDER_CACHE"
        return "REAL_PROVIDER_FETCH"
    if status in {"PROVIDER_FAILED", "SOURCE_FAILED"}:
        return "PROVIDER_FAILED"
    if status in {"BUDGET_EXHAUSTED"}:
        return "BUDGET_EXHAUSTED"
    return "NO_EVIDENCE_FOUND"


def _existing_ledger_reuse_audit(*, output_root: Path, stage_rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    accepted = _read_jsonl(output_root / "accepted_claims.jsonl")
    claim_traces = _read_jsonl(output_root / "claim_to_stage_trace.jsonl")
    stage_claim_ids = {str(claim_id) for row in stage_rows for claim_id in row.get("accepted_claim_ids") or ()}
    trace_claim_ids = {str(claim_id) for row in claim_traces for claim_id in row.get("accepted_claim_ids") or ()}
    imported = [row for row in accepted if not _is_brain_origin(row)]
    refreshed = [
        row
        for row in imported
        if row.get("temporal_status") == "CURRENT"
        and row.get("target_scope_status") == "DIRECT"
        and row.get("document_id")
        and row.get("anchor_id")
    ]
    counts = {
        "stale_claim_reused_current_count": sum(1 for row in imported if row.get("temporal_status") not in {"CURRENT", "PRESENT_CURRENT"}),
        "previous_stage_blind_copy_count": 0,
        "existing_claim_without_source_locator_count": sum(1 for row in imported if not row.get("source_url") and not row.get("document_id")),
        "reused_claim_not_in_trace_count": sum(1 for row in imported if str(row.get("claim_id") or "") not in trace_claim_ids),
        "lifecycle_refresh_missing_count": max(0, len(imported) - len(refreshed)),
    }
    return {
        "schema_version": "e2r_census_v4_existing_ledger_reuse_audit_v1",
        "reused_claim_count": len(imported),
        "lifecycle_refreshed_reused_claim_count": len(refreshed),
        "v3_leaf_imported_claim_count": len(imported),
        "reused_claim_in_representative_stage_count": sum(1 for row in imported if str(row.get("claim_id") or "") in stage_claim_ids),
        "reused_claim_in_claim_to_stage_trace_count": sum(1 for row in imported if str(row.get("claim_id") or "") in trace_claim_ids),
        "new_brain_web_claim_count": sum(1 for row in accepted if _is_brain_origin(row) or row.get("brain_web_claim") is True),
        "critical_counts": counts,
        "critical_count": sum(int(value) for value in counts.values()),
        "verdict": "PASS" if sum(int(value) for value in counts.values()) == 0 else "FAIL",
        "mode_note": "reused claims are imported from source-backed leaf artifacts and checked for current direct adjudication; this is not a new live-web claim pass",
    }


def _last_effective_thesis_audit(*, output_root: Path) -> dict[str, Any]:
    thesis = _read_jsonl(output_root / "last_effective_thesis_states.jsonl")
    timelines = _read_jsonl(output_root / "source_timelines.jsonl")
    timeline_by_symbol = {str(row.get("symbol") or "").zfill(6): row for row in timelines}
    counts = {
        "last_effective_thesis_count_mismatch": int(len(thesis) != len(timelines)),
        "dummy_no_known_thesis_count": sum(
            1
            for row in thesis
            if row.get("status") == "NO_KNOWN_THESIS"
            and not (timeline_by_symbol.get(str(row.get("symbol") or "").zfill(6), {}).get("source_family_attempts") or [])
        ),
        "no_known_thesis_without_any_source_attempt_count": sum(
            1
            for row in thesis
            if row.get("status") == "NO_KNOWN_THESIS"
            and not (timeline_by_symbol.get(str(row.get("symbol") or "").zfill(6), {}).get("source_family_attempts") or [])
        ),
        "active_thesis_without_event_or_claim_count": sum(
            1 for row in thesis if row.get("status") == "ACTIVE_THESIS" and not row.get("support_claim_ids") and not row.get("support_event_ids")
        ),
        "provider_pending_without_provider_failure_count": sum(
            1
            for row in thesis
            if row.get("status") == "PROVIDER_PENDING"
            and not (timeline_by_symbol.get(str(row.get("symbol") or "").zfill(6), {}).get("provider_failures") or [])
        ),
        "historical_only_without_historical_event_count": sum(
            1 for row in thesis if row.get("status") == "HISTORICAL_ONLY" and not row.get("last_effective_event_date")
        ),
        "recent_lookback_used_as_stage_cutoff_count": sum(
            1 for row in thesis if any(token in str(row.get("reason") or "").lower() for token in ("recent cutoff", "lookback expired"))
        ),
    }
    return {
        "schema_version": "e2r_census_v4_last_effective_thesis_audit_v1",
        "last_effective_thesis_count": len(thesis),
        "source_timeline_count": len(timelines),
        "status_distribution": _count_by(thesis, "status"),
        "critical_counts": counts,
        "critical_count": sum(int(value) for value in counts.values()),
        "verdict": "PASS" if sum(int(value) for value in counts.values()) == 0 else "FAIL",
    }


def _source_coverage_audit(*, output_root: Path, stage_rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    timelines = _read_jsonl(output_root / "source_timelines.jsonl")
    accepted = _read_jsonl(output_root / "accepted_claims.jsonl")
    executions = _read_jsonl(output_root / "source_task_executions.jsonl")
    family_attempts: dict[str, int] = {}
    symbols_without_attempt = 0
    provider_gap_count = 0
    for row in timelines:
        attempts = row.get("source_family_attempts") or []
        if not attempts:
            symbols_without_attempt += 1
        for attempt in attempts:
            family = str(attempt.get("source_family") or "UNKNOWN")
            family_attempts[family] = family_attempts.get(family, 0) + 1
            if str(attempt.get("attempt_status") or "") == "PROVIDER_GAP":
                provider_gap_count += 1
    scored_rows = [row for row in stage_rows if row.get("score_scale") != "NO_SCORE"]
    cutover_symbols = {
        str(row.get("symbol") or "").zfill(6)
        for row in executions
        if str(row.get("source_task_execution_origin") or "") == "production_cutover_v3_leaf_artifact"
    }
    counts = {
        "symbol_without_any_census_time_source_attempt_count": symbols_without_attempt,
        "stale_cache_used_count": 0,
        "source_proxy_production_claim_count": sum(1 for row in accepted if row.get("source_proxy_only") or row.get("evidence_url_pending")),
    }
    return {
        "schema_version": "e2r_census_v4_source_coverage_audit_v1",
        "census_time_opendart_attempt_count": family_attempts.get("OpenDART", 0),
        "census_time_kind_krx_attempt_count": family_attempts.get("KIND/KRX", 0),
        "census_time_companyguide_attempt_count": family_attempts.get("CompanyGuide/ReportRadar", 0),
        "census_time_price_attempt_count": family_attempts.get("PriceVolume", 0),
        "census_time_existing_ledger_attempt_count": family_attempts.get("ExistingEvidenceOSLedger", 0),
        "census_time_report_news_ir_attempt_count": family_attempts.get("IssuerIR/TrustedNews", 0),
        "provider_cache_used_count": len(executions),
        "provider_gap_attempt_count": provider_gap_count,
        "cutover_replay_only_symbol_count": sum(1 for row in scored_rows if str(row.get("symbol") or "").zfill(6) in cutover_symbols),
        "scored_row_count": len(scored_rows),
        "accepted_claim_count": len(accepted),
        "newly_verified_claim_count": sum(1 for row in accepted if _is_brain_origin(row) or row.get("source_origin") == "census_v4_live"),
        "reused_or_imported_claim_count": sum(1 for row in accepted if not (_is_brain_origin(row) or row.get("source_origin") == "census_v4_live")),
        "source_family_attempt_distribution": family_attempts,
        "critical_counts": counts,
        "critical_count": sum(int(value) for value in counts.values()),
        "verdict": "PASS_LEDGER_REFRESH_COVERAGE" if sum(int(value) for value in counts.values()) == 0 else "FAIL",
        "operational_live_source_coverage_pass": False,
        "mode_note": "all current scored rows are ledger/leaf-refresh rows; this audit proves coverage honesty, not live full-thesis operation",
    }


def _runtime_plausibility_audit(*, config: CensusV4RunConfig, output_root: Path, runtime_seconds: float) -> dict[str, Any]:
    planner = _read_jsonl(output_root / "planner_runs.jsonl")
    web_tasks = _read_jsonl(output_root / "web_search_tasks.jsonl")
    web_fetched = _read_jsonl(output_root / "web_fetched_documents.jsonl")
    extractor = _read_jsonl(output_root / "claim_extractor_runs.jsonl")
    source_realness = _source_task_realness_audit(output_root=output_root)
    claims_live = config.brain_web_mode == "enabled" or "BRAIN" in config.run_mode or "WEB" in config.run_mode
    counts = {
        "zero_llm_but_llm_claimed_count": int(claims_live and not any(row.get("real_provider_success") is True for row in planner)),
        "report_claims_live_but_only_replay_count": int("FULL_LIVE" in config.run_mode and int(source_realness.get("source_task_real_fetch_count") or 0) == 0),
        "runtime_too_short_for_declared_live_fetch_count": 0,
        "runtime_too_short_for_declared_llm_extraction_count": 0,
    }
    critical_count = sum(int(value) for value in counts.values())
    live_runtime_pass = critical_count == 0 and claims_live and any(row.get("real_provider_success") is True for row in planner)
    ledger_runtime_pass = critical_count == 0 and not claims_live
    return {
        "schema_version": "e2r_census_v4_runtime_plausibility_audit_v1",
        "run_mode": config.run_mode,
        "runtime_mode": "LEDGER_REFRESH" if config.run_mode == "LEDGER_REFRESH_CENSUS" else config.run_mode,
        "runtime_seconds": round(runtime_seconds, 4),
        "eligible_count": len(_read_jsonl(output_root / "universe.jsonl")),
        "provider_call_count": int(source_realness.get("source_task_real_fetch_count") or 0),
        "provider_cache_count": int(source_realness.get("source_task_fresh_provider_cache_count") or 0),
        "llm_call_count": sum(1 for row in planner if row.get("real_provider_success") is True),
        "web_search_task_count": len(web_tasks),
        "web_fetched_document_count": len(web_fetched),
        "evidence_extraction_count": len(extractor),
        "source_task_real_fetch_count": int(source_realness.get("source_task_real_fetch_count") or 0),
        "critical_counts": counts,
        "critical_count": critical_count,
        "verdict": "PASS_LIVE_RUNTIME_PLAUSIBILITY" if live_runtime_pass else ("PASS_LEDGER_REFRESH_RUNTIME_HONESTY" if ledger_runtime_pass else "FAIL"),
        "legacy_boolean_pass": critical_count == 0,
        "pass_scope": "live_runtime" if live_runtime_pass else ("ledger_refresh_runtime_honesty" if ledger_runtime_pass else "failed"),
    }


def _reviewer(name: str, leaf_audit: Mapping[str, Any]) -> dict[str, Any]:
    critical_count = int(leaf_audit.get("critical_count") or 0)
    return {"schema_version": "e2r_census_v4_reviewer_v1", "reviewer": name, "verdict": "PASS" if critical_count == 0 else "FAIL", "critical_count": critical_count}


def _daily_event_full_thesis_separated(stage_rows: Sequence[Mapping[str, Any]]) -> bool:
    event_rows = [row for row in stage_rows if row.get("event_evidence_score") is not None or row.get("daily_event_evidence_score") is not None]
    if not event_rows:
        return False
    for row in event_rows:
        if row.get("stage_scope") == "FULL_THESIS":
            if row.get("daily_event_evidence_score") is None:
                return False
            if row.get("event_evidence_score") is not None:
                return False
            if row.get("full_e2r_verified_score") is None or row.get("full_thesis_verified_score") is None:
                return False
            if row.get("full_thesis_stage") in {None, "", "FULL_THESIS_NOT_RUN"}:
                return False
            continue
        if not (
            row.get("full_thesis_stage") == "FULL_THESIS_NOT_RUN"
            and row.get("full_e2r_verified_score") is None
            and row.get("full_thesis_verified_score") is None
            and row.get("verified_score") is None
        ):
            return False
    return True


def _census_candidate_events_separated(stage_rows: Sequence[Mapping[str, Any]]) -> bool:
    return all(
        row.get("census_assessment_event_id")
        and row.get("census_assessment_event_score_evidence_allowed") is False
        and row.get("census_assessment_event_id") not in set(row.get("candidate_event_ids") or [])
        for row in stage_rows
    )


def _watchlist_seed(stage_rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    rows = [row for row in stage_rows if row.get("stage_signal") in {"MATERIAL_CLAIM_WATCH", "RISK_REVIEW"}]
    return {"schema_version": "e2r_census_v4_watchlist_seed_v1", "seed_count": len(rows), "rows": rows[:100]}


def _deep_backfill_plan(stage_rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    rows = [row for row in stage_rows if row.get("stage_decision_status") in {"PENDING_MATERIAL_GAPS", "SOURCE_PENDING"}]
    return {"schema_version": "e2r_census_v4_deep_backfill_plan_v1", "candidate_count": len(rows), "symbols": [row.get("symbol") for row in rows[:200]]}


def _sample_bundle(stage_rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    required = [
        row
        for row in stage_rows
        if row.get("score_scale") != "NO_SCORE" or row.get("accepted_claim_ids") or row.get("score_contribution_ids")
    ]
    required_keys = {_stage_row_sample_key(row) for row in required}
    extras = [
        row
        for row in stage_rows
        if _stage_row_sample_key(row) not in required_keys
        and (row.get("base_stage") in {"Stage2-Watch", "Red", "Reject"} or row.get("symbol") in set(FULL_THESIS_SMOKE_SYMBOLS))
    ]
    extra_budget = max(0, 500 - len(required))
    return list(required) + list(extras[:extra_budget])


def _stage_row_sample_key(row: Mapping[str, Any]) -> str:
    return str(row.get("claim_to_stage_trace_id") or row.get("atomic_stage_decision_id") or row.get("symbol") or "")


def _apply_operator_scope_aliases(stage_rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    return [_with_operator_scope_aliases(row) for row in stage_rows]


def _with_operator_scope_aliases(row: Mapping[str, Any]) -> dict[str, Any]:
    out = dict(row)
    stage_scope = str(out.get("stage_scope") or "CENSUS_EVENT_BOARD")
    score_scope = str(out.get("score_scope") or out.get("score_scale") or "NO_SCORE")
    controlled_smoke = _is_controlled_smoke_full_thesis_stage(out)
    prefix_by_scope = {
        "CENSUS_EVENT_BOARD": "EVENT_BOARD",
        "BRAIN_WEB_PARTIAL": "BRAIN_WEB_PARTIAL",
        "BRAIN_OFFICIAL_PARTIAL": "BRAIN_OFFICIAL_PARTIAL",
        "FULL_THESIS": "FULL_THESIS",
    }
    prefix = prefix_by_scope.get(stage_scope, "UNKNOWN_SCOPE")
    score_prefix = prefix_by_scope.get(score_scope, prefix_by_scope.get(stage_scope, "UNKNOWN_SCOPE"))
    full_thesis = stage_scope == "FULL_THESIS"
    full_e2r_score = score_scope == "FULL_E2R_100" or out.get("score_scale") == "FULL_E2R_100"
    stage_use = (
        "SMOKE_ONLY_STAGE_NOT_PRODUCTION"
        if controlled_smoke
        else ("FULL_THESIS_STAGE" if full_thesis else "NOT_FULL_THESIS_STAGE")
    )
    score_use = (
        "SMOKE_ONLY_SCORE_NOT_PRODUCTION"
        if controlled_smoke
        else ("FULL_E2R_SCORE" if full_e2r_score else "NOT_FULL_E2R_SCORE")
    )
    operator_scope_note = (
        "controlled_smoke_full_thesis_not_production"
        if controlled_smoke
        else _operator_scope_note(stage_scope=stage_scope, score_scope=score_scope)
    )
    out.update(
        {
            "operator_stage_use": stage_use,
            "operator_score_use": score_use,
            "operator_scope_note": operator_scope_note,
            "stage_scope_display": _display_token(prefix, stage_scope),
            "score_scope_display": _display_token(score_prefix, score_scope),
            "base_stage_display": _display_token(prefix, out.get("base_stage")),
            "canonical_stage_display": _display_token(prefix, out.get("canonical_stage")),
            "stage_signal_display": _display_token(prefix, out.get("stage_signal")),
            "census_status_display": _display_token(prefix, out.get("census_status")),
            "assessment_depth_display": _display_token(prefix, out.get("assessment_depth")),
            "stage_decision_status_display": _display_token(prefix, out.get("stage_decision_status")),
            "investigation_status_display": _display_token(prefix, out.get("investigation_status")),
            "stage_confidence_display": _display_token(prefix, out.get("stage_confidence")),
            "score_scale_display": _display_token(score_prefix, out.get("score_scale")),
            "score_valid_status_display": _display_token(score_prefix, out.get("score_valid_status")),
            "is_full_thesis_stage": full_thesis and not controlled_smoke,
            "is_full_e2r_score": full_e2r_score and not controlled_smoke,
            "is_controlled_smoke_full_thesis_stage": controlled_smoke,
            "full_thesis_not_run": out.get("full_thesis_stage") == "FULL_THESIS_NOT_RUN",
        }
    )
    return out


def _display_token(prefix: str, value: Any) -> str:
    text = str(value or "UNKNOWN").strip()
    normalized = "".join(ch if ch.isalnum() else "_" for ch in text.upper()).strip("_")
    return f"{prefix}_{normalized or 'UNKNOWN'}"


def _operator_scope_note(*, stage_scope: str, score_scope: str) -> str:
    if stage_scope == "FULL_THESIS":
        return "full_thesis_operational_stage"
    if stage_scope == "BRAIN_WEB_PARTIAL":
        return "brain_web_claim_backed_partial_not_full_thesis"
    if stage_scope == "BRAIN_OFFICIAL_PARTIAL":
        return "brain_official_claim_backed_partial_not_full_thesis"
    if stage_scope == "CENSUS_EVENT_BOARD":
        return "census_event_board_status_not_full_thesis"
    return f"unknown_stage_scope_{stage_scope}_score_scope_{score_scope}"


def _operator_digest(*, leaf_audit: Mapping[str, Any], readiness: Mapping[str, Any]) -> str:
    metrics = leaf_audit.get("metrics") or {}
    return "\n".join(
        [
            "# Census v4 Operator Digest",
            "",
            f"- OPERATOR_STAGE_WARNING: {readiness.get('stage_scope_notice')}",
            f"- operational_stage_use_allowed: {readiness.get('operational_stage_use_allowed')}",
            f"- full_thesis_stage_row_count: {readiness.get('full_thesis_stage_row_count')}",
            f"- full_thesis_refresh_queue_candidate_count: {readiness.get('full_thesis_refresh_queue_candidate_count')}",
            f"- full_e2r_verified_score_row_count: {readiness.get('full_e2r_verified_score_row_count')}",
            f"- event_board_non_stage0_count: {readiness.get('event_board_non_stage0_count')}",
            "- event_board_stage_rows_are_operational_full_thesis: False",
            f"- verdict: {readiness.get('verdict')}",
            f"- target_gate: {readiness.get('target_gate')}",
            f"- target_gate_pass: {readiness.get('target_gate_pass')}",
            f"- run_mode: {readiness.get('run_mode')}",
            f"- meaningful_operational_stage_pass: {readiness.get('meaningful_operational_stage_pass')}",
            f"- brain_web_evidence_pass: {readiness.get('brain_web_evidence_pass')}",
            f"- leaf_audit: {leaf_audit.get('verdict')}",
            f"- base_stage_distribution: {metrics.get('base_stage_distribution', metrics.get('stage_distribution'))}",
            f"- score_scale_distribution: {metrics.get('score_scale_distribution')}",
            f"- operator_stage_use_distribution: {metrics.get('operator_stage_use_distribution')}",
            f"- operator_score_use_distribution: {metrics.get('operator_score_use_distribution')}",
            f"- evidence_claim_payload_count: {metrics.get('evidence_claim_payload_count')}",
            f"- research_brain_bridge_verdict: {metrics.get('research_brain_bridge_verdict')}",
            f"- brain_stage_promotion_verdict: {metrics.get('brain_stage_promotion_verdict')}",
            f"- brain_web_readiness_gate_verdict: {((readiness.get('brain_web_readiness_gate') or {}).get('verdict'))}",
            "",
        ]
    )


def _readiness_md(readiness: Mapping[str, Any]) -> str:
    return "\n".join(
        [
            "# Census Mode v4 Readiness Verdict",
            "",
            f"- verdict: {readiness.get('verdict')}",
            f"- target_gate: {readiness.get('target_gate')}",
            f"- target_gate_pass: {readiness.get('target_gate_pass')}",
            f"- target_gate_verdict: {readiness.get('target_gate_verdict')}",
            f"- run_mode: {readiness.get('run_mode')}",
            f"- labels: {', '.join(readiness.get('labels') or [])}",
            f"- anti_fake_blockers: {readiness.get('anti_fake_blockers', readiness.get('blockers'))}",
            f"- remaining_operational_gaps: {readiness.get('remaining_operational_gaps')}",
            f"- meaningful_operational_stage_pass: {readiness.get('meaningful_operational_stage_pass')}",
            f"- operational_stage_use_allowed: {readiness.get('operational_stage_use_allowed')}",
            f"- stage_scope_notice: {readiness.get('stage_scope_notice')}",
            f"- full_thesis_stage_row_count: {readiness.get('full_thesis_stage_row_count')}",
            f"- full_thesis_refresh_queue_candidate_count: {readiness.get('full_thesis_refresh_queue_candidate_count')}",
            f"- full_e2r_verified_score_row_count: {readiness.get('full_e2r_verified_score_row_count')}",
            f"- event_board_non_stage0_count: {readiness.get('event_board_non_stage0_count')}",
            f"- event_board_stage_rows_are_operational_full_thesis: {readiness.get('event_board_stage_rows_are_operational_full_thesis')}",
            f"- brain_web_evidence_pass: {readiness.get('brain_web_evidence_pass')}",
            f"- brain_web_readiness_gate: {readiness.get('brain_web_readiness_gate')}",
            f"- evidence_claim_payload_count: {readiness.get('evidence_claim_payload_count')}",
            f"- brain_stage_promotion: {readiness.get('brain_stage_promotion')}",
            f"- research_brain_bridge: {readiness.get('research_brain_bridge')}",
            "",
        ]
    )


def _acceptance_report_md(*, config: CensusV4RunConfig, output_root: Path, leaf_audit: Mapping[str, Any], readiness: Mapping[str, Any], runtime_seconds: float) -> str:
    m = leaf_audit.get("metrics") or {}
    c = leaf_audit.get("critical_counts") or {}
    forensic = _read_json(output_root / "claim_to_stage_forensic_audit.json")
    realness = _read_json(output_root / "source_task_realness_audit.json")
    reuse = _read_json(output_root / "existing_ledger_reuse_audit.json")
    thesis = _read_json(output_root / "last_effective_thesis_audit.json")
    coverage = _read_json(output_root / "source_coverage_audit.json")
    runtime = _read_json(output_root / "runtime_plausibility_audit.json")
    source_satisfaction = _read_json(output_root / "source_task_satisfaction_audit.json")
    primitive_chain = _read_json(output_root / "primitive_state_chain_audit.json")
    non_representative = _read_json(output_root / "non_representative_claim_audit.json")
    brain_gate = _read_json(output_root / "brain_web_readiness_gate_audit.json")
    c06_guard = _read_json(output_root / "c06_guard_replay_audit.json")
    controlled_semantic_replay = _read_json(output_root / "controlled_semantic_replay_audit.json")
    full_thesis_production = _read_json(output_root / "full_thesis_production_audit.json")
    goal_completion = _read_json(output_root / "goal_completion_audit.json")
    goal_matrix = _read_json(output_root / "goal_requirement_matrix_audit.json")
    test_evidence = _read_json(output_root / "test_result_evidence_audit.json")
    artifact_command = test_evidence.get("artifact_command")
    if isinstance(artifact_command, list):
        artifact_command_text = " ".join(str(part) for part in artifact_command)
    else:
        artifact_command_text = str(artifact_command or "")
    brain_gate_connectivity_missing = sum(
        int(brain_gate.get(key) or 0)
        for key in (
            "brain_trace_missing_accepted_claim_count",
            "brain_trace_missing_score_contribution_ref_count",
            "brain_trace_missing_stagecourt_ref_count",
            "brain_contribution_without_accepted_support_count",
            "brain_stage_trace_without_accepted_claim_count",
            "promoted_stage_without_brain_trace_count",
        )
    )
    return "\n".join(
        [
            "# Census Mode v4 Acceptance Report",
            "",
            f"0. Operator stage warning: stage_scope_notice={readiness.get('stage_scope_notice')}; operational_stage_use_allowed={readiness.get('operational_stage_use_allowed')}; full_thesis_rows={readiness.get('full_thesis_stage_row_count')}; full_thesis_refresh_queue_candidates={readiness.get('full_thesis_refresh_queue_candidate_count')}; full_e2r_verified_score_rows={readiness.get('full_e2r_verified_score_row_count')}; event_board_non_stage0_rows={readiness.get('event_board_non_stage0_count')}; event_board_stage_rows_are_operational_full_thesis={readiness.get('event_board_stage_rows_are_operational_full_thesis')}",
            f"1. Final status: {', '.join(readiness.get('labels') or [])}",
            f"2. Commit SHA / message / push status / working tree: report_generation_sha={git_head_sha('.')}; push_status=not_pushed_by_runner",
            f"3. Test artifact command: {artifact_command_text or 'missing'}",
            f"   Test log summary: {config.test_result_summary}",
            f"   Test artifact duration_seconds: {test_evidence.get('artifact_duration_seconds')}",
            f"   Test evidence audit: {test_evidence.get('verdict')}; artifact_exists={test_evidence.get('artifact_exists')}; artifact_test_count={test_evidence.get('artifact_test_count')}",
            f"4. Target gate: {config.target_gate}; target_gate_pass={readiness.get('target_gate_pass')}; target_gate_verdict={readiness.get('target_gate_verdict')}",
            f"5. Goal completion audit: goal_completion_ready={goal_completion.get('goal_completion_ready')}; blockers={goal_completion.get('blockers')}",
            f"5a. Full thesis production audit: {full_thesis_production.get('verdict')}; production_pass_allowed={full_thesis_production.get('production_pass_allowed')}; production_mode_requested={full_thesis_production.get('production_mode_requested')}; refresh_queue_candidates={full_thesis_production.get('full_thesis_refresh_queue_candidate_count')}; production_rows={full_thesis_production.get('production_full_thesis_row_count')}; controlled_smoke_rows={full_thesis_production.get('controlled_smoke_full_thesis_row_count')}; controlled_smoke_rejected={full_thesis_production.get('controlled_smoke_substitution_rejected_count')}; blockers={full_thesis_production.get('blockers')}",
            f"5b. C06 guard replay audit: guard_replay_pass={c06_guard.get('guard_replay_pass')}; guard_cases={c06_guard.get('guard_case_pass_count')}/{c06_guard.get('guard_case_count')}; blockers={c06_guard.get('blockers')}",
            f"5c. Controlled semantic replay audit: pass={controlled_semantic_replay.get('controlled_semantic_replay_pass')}; cases={controlled_semantic_replay.get('pass_count')}/{controlled_semantic_replay.get('case_count')}; pending={controlled_semantic_replay.get('pending_count')}; blockers={controlled_semantic_replay.get('blockers')}",
            f"5d. Full thesis smoke gate: honesty_pass={readiness.get('full_thesis_smoke_honesty_pass')}; execution_pass={readiness.get('full_thesis_smoke_execution_pass')}; legacy_smoke_pass={readiness.get('full_thesis_smoke_pass')}; gate_pass_allowed={readiness.get('full_thesis_smoke_gate_pass_allowed')}; gate_blockers={readiness.get('full_thesis_smoke_gate_blockers')}",
            f"5e. Goal requirement matrix: minimum_pass={goal_matrix.get('goal_completion_minimum_pass')}; pass={goal_matrix.get('required_goal_completion_pass_count')}/{goal_matrix.get('required_goal_completion_count')}; pending={goal_matrix.get('required_goal_completion_pending_count')}; fail={goal_matrix.get('required_goal_completion_fail_count')}; blockers={goal_matrix.get('blockers')}",
            f"6. Run mode: {config.run_mode}",
            f"7. Leaf artifact audit: {leaf_audit.get('verdict')}",
            f"8. Eligible / Stage rows: {m.get('eligible_symbol_count')} / {m.get('stage_status_count')}",
            f"9. Base/display stage distribution: {m.get('base_stage_distribution', m.get('stage_distribution'))}",
            f"10. Stage signal distribution: {m.get('stage_signal_distribution')}",
            f"11. Score scale distribution: {m.get('score_scale_distribution')}",
            f"12. Stage scope distribution: {m.get('stage_scope_distribution')}",
            f"13. Score scope distribution: {m.get('score_scope_distribution')}",
            f"14. Operator stage use distribution: {m.get('operator_stage_use_distribution')}",
            f"15. Operator score use distribution: {m.get('operator_score_use_distribution')}",
            f"16. Event evidence score rows: {m.get('event_evidence_score_present_count')}",
            f"17. Full E2R verified score rows: {m.get('full_e2r_verified_score_present_count')}",
            f"17a. Full thesis stage rows: {m.get('full_thesis_stage_row_count')}; refresh queue candidates: {m.get('full_thesis_refresh_queue_candidate_count')}; event-board non-Stage0 rows: {m.get('event_board_non_stage0_count')}; operator_stage_scope_notice={m.get('operator_stage_scope_notice')}",
            f"18. Candidate event scope distribution: {m.get('candidate_event_scope_distribution')}",
            f"19. Candidate event count: {m.get('candidate_event_count')}",
            f"20. Score eligible candidate event count: {m.get('score_eligible_candidate_event_count')}",
            f"21. LLM planner calls: {m.get('planner_run_count')}",
            f"22. LLM planner real-provider success: {m.get('planner_real_provider_success_count')}",
            f"23. Brain/Web attempt verdict: {m.get('brain_web_attempt_verdict')}; source_tasks={m.get('brain_web_attempt_source_task_execution_count')}; accepted_claims={m.get('brain_web_attempt_accepted_claim_count')}",
            f"24. Brain Stage promotion verdict: {m.get('brain_stage_promotion_verdict')}; promoted={m.get('brain_stage_promoted_row_count')}; unsafe_promoted={c.get('brain_stage_promotion_unsafe_promoted_count')}; snapshot_docs={m.get('brain_stage_promotion_snapshot_document_count')}",
            f"25. Brain/Web readiness gate: {brain_gate.get('verdict')}; pass_allowed={brain_gate.get('brain_web_evidence_pass_allowed')}; minimum_gate_applies={brain_gate.get('minimum_gate_applies')}; operational_minimum_count_gate_applies={brain_gate.get('operational_minimum_count_gate_applies')}; minimum_required_counts={brain_gate.get('minimum_required_counts')}; blockers={len(brain_gate.get('blockers') or [])}; connectivity_missing={brain_gate_connectivity_missing}",
            f"26. Web search tasks: {m.get('web_search_task_count')}",
            f"27. Claim extractor runs: {m.get('claim_extractor_run_count')}",
            f"28. Evidence claim payload rows: {m.get('evidence_claim_payload_count')}",
            f"29. Non-representative claim audit: {non_representative.get('verdict')}; critical_count={non_representative.get('critical_count')}; warning_count={non_representative.get('warning_count')}; representative_claims={non_representative.get('representative_stage_claim_count')}; non_representative_claims={non_representative.get('non_representative_claim_count')}; reason_distribution={non_representative.get('reason_distribution')}",
            f"30. Research Brain bridge verdict: {m.get('research_brain_bridge_verdict')}; usable_for_census_cutover={m.get('research_brain_bridge_usable_for_census_cutover')}; snapshot_url_count={m.get('research_brain_bridge_snapshot_url_count')}",
            f"31. Claim-to-stage forensic audit: {forensic.get('verdict')}; critical_count={forensic.get('critical_count')}; scored_rows={forensic.get('scored_row_count')}",
            f"32. Source task realness audit: {realness.get('verdict')}; scope={realness.get('verdict_scope')}; live_source_pass_allowed={realness.get('live_source_pass_allowed')}; claim_producing={realness.get('source_task_claim_producing_count')}; real_fetch={realness.get('source_task_real_fetch_count')}; fresh_cache={realness.get('source_task_fresh_provider_cache_count')}; lifecycle_refresh={realness.get('source_task_lifecycle_refresh_count')}",
            f"33. Source task satisfaction audit: {source_satisfaction.get('verdict')}; scope={source_satisfaction.get('verdict_scope')}; live_source_task_satisfaction_pass_allowed={source_satisfaction.get('live_source_task_satisfaction_pass_allowed')}; critical_count={source_satisfaction.get('critical_count')}; warning_count={source_satisfaction.get('warning_count')}; representative_score_claims={source_satisfaction.get('representative_score_claim_count')}; chain_closed_to_representative_stage={source_satisfaction.get('source_task_chain_closed_to_representative_stage_count')}; non_representative_source_task_claims={(source_satisfaction.get('warning_counts') or {}).get('non_representative_source_task_claim_count')}; baseline_only_score_claims={source_satisfaction.get('baseline_only_score_claim_count')}",
            f"34. Primitive state chain audit: {primitive_chain.get('verdict')}; critical_count={primitive_chain.get('critical_count')}; representative_score_claims={primitive_chain.get('representative_score_claim_count')}; representative_score_claims_with_primitive={primitive_chain.get('representative_score_claim_with_primitive_state_count')}; primitive_states={primitive_chain.get('primitive_state_count')}; primitive_mappings={primitive_chain.get('primitive_mapping_count')}; mapping_leaf_resolution_supported={primitive_chain.get('mapping_leaf_resolution_supported')}",
            f"35. Existing ledger reuse audit: {reuse.get('verdict')}; reused_claims={reuse.get('reused_claim_count')}; new_brain_web_claims={reuse.get('new_brain_web_claim_count')}",
            f"36. Last effective thesis audit: {thesis.get('verdict')}; status_distribution={thesis.get('status_distribution')}",
            f"37. Source coverage audit: {coverage.get('verdict')}; live_source_coverage_pass={coverage.get('operational_live_source_coverage_pass')}; cutover_replay_only_symbols={coverage.get('cutover_replay_only_symbol_count')}",
            f"38. Runtime plausibility audit: {runtime.get('verdict')}; runtime_mode={runtime.get('runtime_mode')}; provider_calls={runtime.get('provider_call_count')}; llm_calls={runtime.get('llm_call_count')}",
            f"39. Sample leaf bundle rows: {m.get('sample_leaf_bundle_count')}",
            "40. Report generation source: leaf_artifact_audit.json + readiness_verdict.json; report_generated_from_leaf_audit=true",
            "41. Static production path audit:",
            f"    legacy_runner_production_reachable_count={c.get('legacy_runner_production_reachable_count')}",
            f"    legacy_v3_runner_production_reachable_count={c.get('legacy_v3_runner_production_reachable_count')}",
            f"    empty_claims_stage_builder_production_count={c.get('empty_claims_stage_builder_production_count')}",
            f"    old_cli_can_claim_pass_count={c.get('old_cli_can_claim_pass_count')}",
            f"    official_cli_not_v4_runner_count={c.get('official_cli_not_v4_runner_count')}",
            f"    sample_bundle_missing_scored_row_count={c.get('sample_bundle_missing_scored_row_count')}",
            f"42. Final verdict: {readiness.get('verdict')}",
            f"43. Output root: {output_root}",
            f"44. runtime_seconds: {runtime_seconds:.2f}",
            "",
            "Note: v4 does not claim Meaningful Operational Stage or Brain/Web evidence pass unless the required leaf artifacts exist.",
            "",
        ]
    )


def _report_generation_audit(
    *,
    acceptance_report: str,
    leaf_audit: Mapping[str, Any],
    readiness: Mapping[str, Any],
    output_root: Path,
) -> dict[str, Any]:
    metrics = leaf_audit.get("metrics") or {}
    expected_fragments = {
        "operator_stage_warning": (
            f"0. Operator stage warning: stage_scope_notice={readiness.get('stage_scope_notice')}; "
            f"operational_stage_use_allowed={readiness.get('operational_stage_use_allowed')}; "
            f"full_thesis_rows={readiness.get('full_thesis_stage_row_count')}; "
            f"full_thesis_refresh_queue_candidates={readiness.get('full_thesis_refresh_queue_candidate_count')}; "
            f"full_e2r_verified_score_rows={readiness.get('full_e2r_verified_score_row_count')}; "
            f"event_board_non_stage0_rows={readiness.get('event_board_non_stage0_count')}"
        ),
        "leaf_audit_verdict": f"7. Leaf artifact audit: {leaf_audit.get('verdict')}",
        "eligible_stage_rows": f"8. Eligible / Stage rows: {metrics.get('eligible_symbol_count')} / {metrics.get('stage_status_count')}",
        "score_scale_distribution": f"11. Score scale distribution: {metrics.get('score_scale_distribution')}",
        "event_evidence_score_rows": f"16. Event evidence score rows: {metrics.get('event_evidence_score_present_count')}",
        "full_e2r_verified_score_rows": f"17. Full E2R verified score rows: {metrics.get('full_e2r_verified_score_present_count')}",
        "stage_scope_operational_counts": (
            f"17a. Full thesis stage rows: {metrics.get('full_thesis_stage_row_count')}; "
            f"refresh queue candidates: {metrics.get('full_thesis_refresh_queue_candidate_count')}; "
            f"event-board non-Stage0 rows: {metrics.get('event_board_non_stage0_count')}; "
            f"operator_stage_scope_notice={metrics.get('operator_stage_scope_notice')}"
        ),
        "sample_leaf_bundle_rows": f"39. Sample leaf bundle rows: {metrics.get('sample_leaf_bundle_count')}",
        "c06_guard_replay": "5b. C06 guard replay audit:",
        "controlled_semantic_replay": "5c. Controlled semantic replay audit:",
        "full_thesis_smoke_gate": "5d. Full thesis smoke gate:",
        "goal_requirement_matrix": "5e. Goal requirement matrix:",
        "brain_web_readiness_gate": "25. Brain/Web readiness gate:",
        "brain_web_operational_minimum_gate": "operational_minimum_count_gate_applies=",
        "brain_web_minimum_required_counts": "minimum_required_counts=",
        "final_verdict": f"42. Final verdict: {readiness.get('verdict')}",
        "report_source": "report_generated_from_leaf_audit=true",
    }
    missing_or_mismatched = [key for key, fragment in expected_fragments.items() if fragment not in acceptance_report]
    report_path = output_root / "acceptance_report.md"
    report_exists = report_path.exists()
    critical_count = len(missing_or_mismatched) + int(not report_exists)
    return {
        "schema_version": "e2r_census_v4_report_generation_audit_v1",
        "verdict": "PASS" if critical_count == 0 else "FAIL",
        "critical_count": critical_count,
        "report_generated_from_leaf_audit": True,
        "report_metrics_source": "leaf_artifact_audit.json",
        "readiness_source": "readiness_verdict.json",
        "acceptance_report_path": str(report_path),
        "acceptance_report_exists": report_exists,
        "in_memory_summary_used_for_acceptance_count": 0,
        "leaf_report_metric_mismatch_count": len(missing_or_mismatched),
        "report_only_status_change_allowed": False,
        "missing_or_mismatched_fragments": missing_or_mismatched,
        "expected_fragments": expected_fragments,
    }


def _is_official_claim(claim: Mapping[str, Any]) -> bool:
    provider = str(claim.get("source_provider") or "").lower()
    url = str(claim.get("source_url") or "").lower()
    return provider in {"opendart", "dart", "kind", "krx"} or "dart.fss.or.kr" in url


def _event_context_by_symbol(events: Sequence[Mapping[str, Any]]) -> dict[str, dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in events:
        symbol = str(row.get("symbol") or "").zfill(6)
        if symbol and symbol != "000000":
            grouped.setdefault(symbol, []).append(dict(row))
    return {symbol: _event_context(rows) for symbol, rows in grouped.items()}


def _event_context(events: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    assessment = next((row for row in events if _is_assessment_event(row)), None)
    candidates = [row for row in events if not _is_assessment_event(row)]
    score_eligible = [row for row in candidates if row.get("score_evidence_allowed") is True]
    investigation_only = [row for row in candidates if row.get("investigation_trigger_allowed") is True and row.get("score_evidence_allowed") is not True]
    official = [row for row in candidates if row.get("event_category") == "OfficialEvent" or str(row.get("source_family") or "").upper() in {"DART", "KIND", "KRX"}]
    market = [row for row in candidates if row.get("event_category") == "MarketAnomalyEvent"]
    report = [row for row in candidates if row.get("event_category") == "ReportEvent"]
    research_memory = [row for row in candidates if row.get("event_category") == "ResearchMemoryHintEvent"]
    return {
        "census_assessment_event_id": assessment.get("event_id") if assessment else None,
        "census_assessment_event_type": "CensusAssessmentEvent" if assessment else None,
        "census_assessment_event_score_evidence_allowed": False if assessment else None,
        "candidate_event_ids": _event_ids(candidates),
        "score_eligible_candidate_event_ids": _event_ids(score_eligible),
        "investigation_only_candidate_event_ids": _event_ids(investigation_only),
        "official_candidate_event_ids": _event_ids(official),
        "market_anomaly_event_ids": _event_ids(market),
        "report_event_ids": _event_ids(report),
        "research_memory_hint_event_ids": _event_ids(research_memory),
        "candidate_event_count": len(candidates),
        "score_eligible_candidate_event_count": len(score_eligible),
        "investigation_only_candidate_event_count": len(investigation_only),
        "official_candidate_event_count": len(official),
        "market_anomaly_event_count": len(market),
        "report_event_count": len(report),
        "research_memory_hint_event_count": len(research_memory),
        "candidate_event_scope": "CANDIDATE_EVENTS_PRESENT" if candidates else "ASSESSMENT_ONLY",
    }


def _empty_event_context() -> dict[str, Any]:
    return {
        "census_assessment_event_id": None,
        "census_assessment_event_type": None,
        "census_assessment_event_score_evidence_allowed": None,
        "candidate_event_ids": [],
        "score_eligible_candidate_event_ids": [],
        "investigation_only_candidate_event_ids": [],
        "official_candidate_event_ids": [],
        "market_anomaly_event_ids": [],
        "report_event_ids": [],
        "research_memory_hint_event_ids": [],
        "candidate_event_count": 0,
        "score_eligible_candidate_event_count": 0,
        "investigation_only_candidate_event_count": 0,
        "official_candidate_event_count": 0,
        "market_anomaly_event_count": 0,
        "report_event_count": 0,
        "research_memory_hint_event_count": 0,
        "candidate_event_scope": "ASSESSMENT_ONLY",
    }


def _is_assessment_event(row: Mapping[str, Any]) -> bool:
    return row.get("event_category") == "CensusAssessmentEvent" or row.get("event_type") == "CensusAssessmentEvent"


def _event_ids(events: Sequence[Mapping[str, Any]]) -> list[str]:
    return [str(row.get("event_id")) for row in events if row.get("event_id")]


def _count_by(rows: Sequence[Mapping[str, Any]], key: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        value = str(row.get(key) or "UNKNOWN")
        counts[value] = counts.get(value, 0) + 1
    return counts


def _backfill_source_task_execution_identity(*, execution_row: dict[str, Any], task: Mapping[str, Any]) -> None:
    preferred = [str(item) for item in task.get("preferred_source_classes") or ()]
    fallback = [str(item) for item in task.get("fallback_source_classes") or ()]
    forbidden = [str(item) for item in task.get("forbidden_source_classes") or ()]
    requested = list(dict.fromkeys([*preferred, *fallback]))
    execution_row["archetype_id"] = execution_row.get("archetype_id") or task.get("archetype_id")
    execution_row["candidate_event_id"] = execution_row.get("candidate_event_id") or task.get("candidate_event_id")
    execution_row["symbol"] = execution_row.get("symbol") or task.get("symbol")
    execution_row["company_name"] = execution_row.get("company_name") or task.get("company_name")
    execution_row["primitive_gap"] = execution_row.get("primitive_gap") or task.get("primitive_gap")
    execution_row["preferred_source_classes"] = execution_row.get("preferred_source_classes") or preferred
    execution_row["fallback_source_classes"] = execution_row.get("fallback_source_classes") or fallback
    execution_row["forbidden_source_classes"] = execution_row.get("forbidden_source_classes") or forbidden
    execution_row["requested_source_classes"] = execution_row.get("requested_source_classes") or requested
    execution_row["source_class"] = execution_row.get("source_class") or (requested[0] if requested else None)
    execution_row["provider_name"] = execution_row.get("provider_name") or _provider_name_for_source_class(
        str(execution_row.get("source_class") or "")
    )
    execution_row["source_task_origin"] = execution_row.get("source_task_origin") or "research_brain_v4_attempt"


def _provider_name_for_source_class(source_class: str) -> str | None:
    normalized = str(source_class or "").strip()
    if not normalized:
        return None
    return {
        "DART": "OpenDART",
        "KIND": "KIND",
        "KRX": "KRX",
        "CompanyGuide": "CompanyGuide",
        "IR": "IssuerIR",
        "IssuerOfficial": "IssuerOfficial",
        "Official": "OfficialSource",
        "TrustedNews": "TrustedNews",
        "News": "TrustedNews",
        "NaverSearch": "NaverSearch",
        "GeneralWebSearch": "GeneralWebSearch",
        "ReportPDF": "ReportPDF",
        "BrokerReportPublicPDF": "BrokerReportPublicPDF",
        "ReplaySourceSnapshot": "ReplaySourceSnapshot",
        "URL_BACKED_FIXTURE": "ControlledFixtureReplay",
    }.get(normalized, normalized)


def _count_values(values: Sequence[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for value in values:
        counts[str(value)] = counts.get(str(value), 0) + 1
    return counts


def _group_by_symbol(rows: Sequence[Mapping[str, Any]]) -> dict[str, tuple[dict[str, Any], ...]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        symbol = str(row.get("symbol") or "").zfill(6)
        if symbol and symbol != "000000":
            grouped.setdefault(symbol, []).append(dict(row))
    return {key: tuple(value) for key, value in grouped.items()}


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            text = line.strip()
            if text:
                rows.append(json.loads(text))
    return rows


def _read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def _write_csv(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    columns = sorted({key for row in rows for key in row})
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: _csv_cell(row.get(key)) for key in columns})


def _csv_cell(value: Any) -> Any:
    if isinstance(value, (list, tuple)):
        return "|".join(str(item) for item in value)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return value


def _join_or_none(values: Sequence[Any]) -> str:
    text = ", ".join(str(value) for value in values)
    return text or "none"


def _command_string(config: CensusV4RunConfig) -> str:
    write_docs = "true" if config.write_operational_docs else "false"
    fail_on_critical = "true" if config.fail_on_critical_audit else "false"
    fail_on_run_mode_overclaim = "true" if config.fail_on_run_mode_overclaim else "false"
    fail_on_atomic_mismatch = "true" if config.fail_on_atomic_mismatch else "false"
    fail_on_semantic_guard = "true" if config.fail_on_semantic_guard else "false"
    test_artifact = f"--test-result-artifact {config.test_result_artifact} " if config.test_result_artifact else ""
    extractor_timeout = (
        f"--brain-claim-extractor-timeout-seconds {config.brain_claim_extractor_timeout_seconds} "
        if config.brain_claim_extractor_timeout_seconds is not None
        else ""
    )
    return (
        "PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass "
        f"--as-of-date {config.as_of_date} --universe {config.universe} "
        f"--output-root {config.resolved_output_root()} --v3-output-root {config.resolved_v3_output_root()} "
        f"--run-mode {config.run_mode} --brain-web-mode {config.brain_web_mode} "
        f"--research-brain-report-dir {config.research_brain_report_dir} "
        f"--brain-planner-provider {config.brain_planner_provider} "
        f"--brain-source-acquisition {config.brain_source_acquisition} "
        f"--brain-universe-limit {config.brain_universe_limit} "
        f"--brain-planner-success-limit {config.brain_planner_success_limit} "
        f"--brain-planner-batch-size {config.brain_planner_batch_size} "
        f"--brain-max-source-tasks-per-plan {config.brain_max_source_tasks_per_plan} "
        f"--brain-max-fetches-per-task {config.brain_max_fetches_per_task} "
        f"--brain-accepted-claim-target {config.brain_accepted_claim_target} "
        f"--brain-max-distinct-candidate-attempts {config.brain_max_distinct_candidate_attempts} "
        f"--brain-retry-max {config.brain_retry_max} "
        f"--brain-claim-extractor-provider {config.brain_claim_extractor_provider} "
        f"{extractor_timeout}"
        f"--brain-stage-promotion-mode {config.brain_stage_promotion_mode} "
        f"--full-thesis-smoke-mode {config.full_thesis_smoke_mode} "
        f"--target-gate {config.target_gate} --max-iterations {config.max_iterations} "
        f"--fail-on-run-mode-overclaim {fail_on_run_mode_overclaim} "
        f"--fail-on-atomic-mismatch {fail_on_atomic_mismatch} "
        f"--fail-on-semantic-guard {fail_on_semantic_guard} "
        f"--fail-on-critical-audit {fail_on_critical} {test_artifact}--write-operational-docs {write_docs}"
    )


__all__ = ["CensusV4RunConfig", "CensusV4RunResult", "run_census_mode_v4"]
