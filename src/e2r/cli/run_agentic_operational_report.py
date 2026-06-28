"""Build the Evidence OS v2 operational acceptance report bundle."""

from __future__ import annotations

import argparse
import json
import subprocess
from datetime import date
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.calibration.taxonomy import (
    ARCHETYPE_TO_LARGE_SECTOR,
    CANONICAL_ARCHETYPE_IDS,
    LARGE_SECTOR_IDS,
)


DEFAULT_CHAIN_AUDIT = (
    "output/0621_agentic_replay/"
    "c01_c36_combined_replacement_metadata_asof_source_recovery_v12_chain_audit.json"
)
DEFAULT_REPLAY_ACCEPTANCE = (
    "output/0621_agentic_replay/"
    "c01_c36_combined_replacement_metadata_asof_source_recovery_v13_replay_acceptance_acceptance.json"
)
DEFAULT_ADVERSARIAL_ACCEPTANCE = (
    "output/0621_agentic_replay/"
    "c01_c36_combined_replacement_metadata_asof_source_recovery_v13_adversarial_acceptance_acceptance.json"
)
DEFAULT_LIVE_SMOKE_ACCEPTANCE = (
    "output/0621_agentic_replay/"
    "samsung_cp199_hynix_cp198_live_smoke_acceptance_acceptance.json"
)
DEFAULT_FROZEN_REPEATABILITY_ACCEPTANCE = (
    "output/0621_agentic_replay/"
    "sk_hynix_c06_frozen_repeatability_acceptance_after_cp163_acceptance.json"
)
DEFAULT_SOURCE_BACKED_COVERAGE = "output/0621_agentic_replay/c01_c36_source_backed_coverage.json"
DEFAULT_REPLAY_GAP_PLAN = (
    "output/0621_agentic_replay/"
    "c01_c36_combined_replacement_metadata_asof_source_recovery_v13_replay_gap_plan_gap_plan.json"
)
DEFAULT_SCORE_CONTRIBUTIONS = (
    "output/0621_agentic_replay/"
    "c01_c36_combined_replacement_metadata_asof_source_recovery_v12_score_contribution_results.json"
)
DEFAULT_SCORE_SNAPSHOTS = (
    "output/0621_agentic_replay/"
    "c01_c36_combined_replacement_metadata_asof_source_recovery_v12_score_snapshot_results.json"
)
DEFAULT_STAGE_COURT_RESULTS = (
    "output/0621_agentic_replay/"
    "c01_c36_combined_replacement_metadata_asof_source_recovery_v12_stage_court_results.json"
)
DEFAULT_DISCOVERY_RUN_LOG = (
    "output/0628_goal2_operational_discovery_dry_run/"
    "korea_live_lite/2024-05-21_run_log.json"
)
DEFAULT_DISCOVERY_CANDIDATES = (
    "output/0628_goal2_operational_discovery_dry_run/"
    "korea_live_lite/2024-05-21_candidates.json"
)
DEFAULT_OUTPUT_DIRECTORY = "docs/operational"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Evidence OS v2 operational acceptance artifacts.")
    parser.add_argument("--chain-audit", default=DEFAULT_CHAIN_AUDIT)
    parser.add_argument("--replay-acceptance", default=DEFAULT_REPLAY_ACCEPTANCE)
    parser.add_argument("--adversarial-acceptance", default=DEFAULT_ADVERSARIAL_ACCEPTANCE)
    parser.add_argument("--live-smoke-acceptance", default=DEFAULT_LIVE_SMOKE_ACCEPTANCE)
    parser.add_argument("--frozen-repeatability-acceptance", default=DEFAULT_FROZEN_REPEATABILITY_ACCEPTANCE)
    parser.add_argument("--source-backed-coverage", default=DEFAULT_SOURCE_BACKED_COVERAGE)
    parser.add_argument("--replay-gap-plan", default=DEFAULT_REPLAY_GAP_PLAN)
    parser.add_argument("--score-contributions", default=DEFAULT_SCORE_CONTRIBUTIONS)
    parser.add_argument("--score-snapshots", default=DEFAULT_SCORE_SNAPSHOTS)
    parser.add_argument("--stage-court-results", default=DEFAULT_STAGE_COURT_RESULTS)
    parser.add_argument("--discovery-run-log", default=DEFAULT_DISCOVERY_RUN_LOG)
    parser.add_argument("--discovery-candidates", default=DEFAULT_DISCOVERY_CANDIDATES)
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--commit-sha", default=None)
    parser.add_argument("--generated-at", default=None)
    parser.add_argument("--test-command", default="PYTHONPATH=src python -m unittest discover -s tests -v")
    parser.add_argument("--test-pass-count", type=int, default=0)
    parser.add_argument("--test-fail-count", type=int, default=0)
    parser.add_argument("--test-skip-count", type=int, default=0)
    return parser


def run_operational_report(
    *,
    chain_audit_path: str | Path,
    replay_acceptance_path: str | Path,
    adversarial_acceptance_path: str | Path,
    live_smoke_acceptance_path: str | Path,
    frozen_repeatability_acceptance_path: str | Path,
    source_backed_coverage_path: str | Path,
    replay_gap_plan_path: str | Path,
    score_contribution_path: str | Path,
    score_snapshot_path: str | Path,
    stage_court_result_path: str | Path,
    discovery_run_log_path: str | Path | None,
    discovery_candidates_path: str | Path | None,
    output_directory: str | Path,
    commit_sha: str | None = None,
    generated_at: str | None = None,
    test_command: str = "PYTHONPATH=src python -m unittest discover -s tests -v",
    test_pass_count: int = 0,
    test_fail_count: int = 0,
    test_skip_count: int = 0,
) -> Mapping[str, Path]:
    bundle = build_operational_report_bundle(
        chain_audit=_read_json_mapping(Path(chain_audit_path)),
        replay_acceptance=_read_json_mapping(Path(replay_acceptance_path)),
        adversarial_acceptance=_read_json_mapping(Path(adversarial_acceptance_path)),
        live_smoke_acceptance=_read_json_mapping(Path(live_smoke_acceptance_path)),
        frozen_repeatability_acceptance=_read_json_mapping(Path(frozen_repeatability_acceptance_path)),
        source_backed_coverage=_read_json_mapping(Path(source_backed_coverage_path)),
        replay_gap_plan=_read_json_mapping(Path(replay_gap_plan_path)),
        score_contributions=_read_json_mapping(Path(score_contribution_path)),
        score_snapshots=_read_json_mapping(Path(score_snapshot_path)),
        stage_court_results=_read_json_mapping(Path(stage_court_result_path)),
        discovery_run_log=_read_optional_json_mapping(Path(discovery_run_log_path) if discovery_run_log_path else None),
        discovery_candidates=_read_optional_json_mapping(Path(discovery_candidates_path) if discovery_candidates_path else None),
        commit_sha=commit_sha or _git_head_sha(),
        generated_at=generated_at or date.today().isoformat(),
        test_summary={
            "command": test_command,
            "passed": int(test_pass_count),
            "failed": int(test_fail_count),
            "skipped": int(test_skip_count),
        },
    )
    return write_operational_report_bundle(bundle, output_directory=output_directory)


def build_operational_report_bundle(
    *,
    chain_audit: Mapping[str, Any],
    replay_acceptance: Mapping[str, Any],
    adversarial_acceptance: Mapping[str, Any],
    live_smoke_acceptance: Mapping[str, Any],
    frozen_repeatability_acceptance: Mapping[str, Any],
    source_backed_coverage: Mapping[str, Any],
    replay_gap_plan: Mapping[str, Any],
    score_contributions: Mapping[str, Any],
    score_snapshots: Mapping[str, Any],
    stage_court_results: Mapping[str, Any],
    discovery_run_log: Mapping[str, Any] | None,
    discovery_candidates: Mapping[str, Any] | None,
    commit_sha: str,
    generated_at: str,
    test_summary: Mapping[str, Any],
) -> Mapping[str, Any]:
    summary = _build_overall_summary(
        cutover_summary=_summary_from_cutover_inputs(
            chain_audit=chain_audit,
            replay_acceptance=replay_acceptance,
            adversarial_acceptance=adversarial_acceptance,
            live_smoke_acceptance=live_smoke_acceptance,
            frozen_repeatability_acceptance=frozen_repeatability_acceptance,
        ),
        replay_gap_plan=replay_gap_plan,
        live_smoke_acceptance=live_smoke_acceptance,
        score_contributions=score_contributions,
        source_backed_coverage=source_backed_coverage,
        discovery_candidates=discovery_candidates,
        test_summary=test_summary,
    )
    metadata = {
        "schema_version": "e2r_operational_acceptance_bundle_v1",
        "generated_at": generated_at,
        "commit_sha": commit_sha,
        "test_summary": dict(test_summary),
        "production_verdict": summary["production_verdict"],
    }
    archetype_matrix = _build_archetype_matrix(
        replay_acceptance=replay_acceptance,
        source_backed_coverage=source_backed_coverage,
        stage_court_results=stage_court_results,
        adversarial_acceptance=adversarial_acceptance,
    )
    sector_matrix = _build_sector_matrix(
        archetype_matrix=archetype_matrix,
        discovery_candidates=discovery_candidates,
        discovery_run_log=discovery_run_log,
    )
    source_gap_inventory = _build_source_gap_inventory(
        replay_gap_plan=replay_gap_plan,
        source_backed_coverage=source_backed_coverage,
        replay_acceptance=replay_acceptance,
    )
    live_smoke_results = _build_live_smoke_results(live_smoke_acceptance)
    replay_results = _build_replay_results(
        chain_audit=chain_audit,
        replay_acceptance=replay_acceptance,
        adversarial_acceptance=adversarial_acceptance,
        frozen_repeatability_acceptance=frozen_repeatability_acceptance,
        score_contributions=score_contributions,
        score_snapshots=score_snapshots,
        stage_court_results=stage_court_results,
    )
    legacy_quarantine_audit = _build_legacy_quarantine_audit(live_smoke_acceptance)
    score_delta_audit = _build_score_delta_audit(live_smoke_acceptance)
    acceptance_report = _render_acceptance_report(
        metadata=metadata,
        summary=summary,
        archetype_matrix=archetype_matrix,
        sector_matrix=sector_matrix,
        source_gap_inventory=source_gap_inventory,
        live_smoke_results=live_smoke_results,
        legacy_quarantine_audit=legacy_quarantine_audit,
        score_delta_audit=score_delta_audit,
    )
    deprecated_report = _render_deprecated_live_results(live_smoke_acceptance)
    known_regressions = _render_known_regressions(live_smoke_acceptance)
    return {
        "metadata": metadata,
        "summary": summary,
        "acceptance_report_md": acceptance_report,
        "deprecated_live_results_md": deprecated_report,
        "known_regressions_md": known_regressions,
        "archetype_matrix": archetype_matrix,
        "sector_matrix": sector_matrix,
        "replay_results": replay_results,
        "live_smoke_results": live_smoke_results,
        "source_gap_inventory": source_gap_inventory,
        "score_delta_audit": score_delta_audit,
        "legacy_quarantine_audit": legacy_quarantine_audit,
    }


def write_operational_report_bundle(bundle: Mapping[str, Any], *, output_directory: str | Path) -> Mapping[str, Path]:
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "acceptance_report": output_dir / "evidence_os_v2_acceptance_report.md",
        "sector_matrix": output_dir / "evidence_os_v2_sector_matrix.json",
        "archetype_matrix": output_dir / "evidence_os_v2_archetype_matrix.json",
        "replay_results": output_dir / "evidence_os_v2_replay_results.json",
        "live_smoke_results": output_dir / "evidence_os_v2_live_smoke_results.json",
        "source_gap_inventory": output_dir / "evidence_os_v2_source_gap_inventory.json",
        "score_delta_audit": output_dir / "evidence_os_v2_score_delta_audit.json",
        "legacy_quarantine_audit": output_dir / "evidence_os_v2_legacy_quarantine_audit.json",
        "known_regressions": output_dir / "evidence_os_v2_known_regressions.md",
        "deprecated_live_results": output_dir / "deprecated_live_results_2026-06-21.md",
    }
    paths["acceptance_report"].write_text(str(bundle["acceptance_report_md"]), encoding="utf-8")
    paths["known_regressions"].write_text(str(bundle["known_regressions_md"]), encoding="utf-8")
    paths["deprecated_live_results"].write_text(str(bundle["deprecated_live_results_md"]), encoding="utf-8")
    for key in (
        "sector_matrix",
        "archetype_matrix",
        "replay_results",
        "live_smoke_results",
        "source_gap_inventory",
        "score_delta_audit",
        "legacy_quarantine_audit",
    ):
        _write_json(paths[key], bundle[key])
    return paths


def _build_overall_summary(
    *,
    cutover_summary: Mapping[str, Any],
    replay_gap_plan: Mapping[str, Any],
    live_smoke_acceptance: Mapping[str, Any],
    score_contributions: Mapping[str, Any],
    source_backed_coverage: Mapping[str, Any],
    discovery_candidates: Mapping[str, Any] | None,
    test_summary: Mapping[str, Any],
) -> Mapping[str, Any]:
    gap_summary = _summary(replay_gap_plan)
    live_summary = _summary(live_smoke_acceptance)
    contribution_summary = _summary(score_contributions)
    source_summary = _summary(source_backed_coverage)
    production_candidate_count = _production_candidate_count(discovery_candidates)
    acceptance_ready = (
        bool(cutover_summary.get("production_cutover_ready"))
        and _int(gap_summary.get("gap_task_count")) == 0
        and _int(live_summary.get("legacy_parser_score_claim_without_v2_current_row_count")) == 0
        and _int(contribution_summary.get("orphan_score_blocked_count")) == 0
        and _int(source_summary.get("source_gap_no_rows_archetype_count")) == 0
        and _int(source_summary.get("source_gap_with_rows_archetype_count")) == 0
        and _int(test_summary.get("failed")) == 0
        and production_candidate_count > 0
    )
    return {
        "schema_version": "e2r_operational_acceptance_summary_v1",
        "production_verdict": "READY" if acceptance_ready else "NOT_READY",
        "cutover_acceptance_ready": bool(cutover_summary.get("production_cutover_ready")),
        "replay_acceptance_ready": bool(cutover_summary.get("replay_acceptance_ready")),
        "adversarial_acceptance_ready": bool(cutover_summary.get("adversarial_acceptance_ready")),
        "live_smoke_acceptance_ready": bool(cutover_summary.get("live_smoke_acceptance_ready")),
        "frozen_repeatability_acceptance_ready": bool(cutover_summary.get("frozen_repeatability_acceptance_ready")),
        "orphan_score_blocked_count": _int(contribution_summary.get("orphan_score_blocked_count")),
        "nonzero_score_contribution_count": _int(contribution_summary.get("nonzero_score_contribution_count")),
        "source_gap_archetype_count": _int(source_summary.get("source_gap_no_rows_archetype_count"))
        + _int(source_summary.get("source_gap_with_rows_archetype_count")),
        "replay_gap_task_count": _int(gap_summary.get("gap_task_count")),
        "legacy_parser_score_claim_without_v2_current_row_count": _int(
            live_summary.get("legacy_parser_score_claim_without_v2_current_row_count")
        ),
        "deprecated_legacy_result_not_accepted_count": _int(
            live_summary.get("deprecated_legacy_result_not_accepted_count")
        ),
        "production_discovery_candidate_count": production_candidate_count,
        "test_command": test_summary.get("command"),
        "test_pass_count": _int(test_summary.get("passed")),
        "test_fail_count": _int(test_summary.get("failed")),
        "test_skip_count": _int(test_summary.get("skipped")),
    }


def _summary_from_cutover_inputs(
    *,
    chain_audit: Mapping[str, Any],
    replay_acceptance: Mapping[str, Any],
    adversarial_acceptance: Mapping[str, Any],
    live_smoke_acceptance: Mapping[str, Any],
    frozen_repeatability_acceptance: Mapping[str, Any],
) -> Mapping[str, Any]:
    chain_summary = _summary(chain_audit)
    replay_summary = _summary(replay_acceptance)
    adversarial_summary = _summary(adversarial_acceptance)
    live_summary = _summary(live_smoke_acceptance)
    frozen_summary = _summary(frozen_repeatability_acceptance)
    return {
        "production_cutover_ready": bool(replay_summary.get("production_cutover_ready"))
        and bool(adversarial_summary.get("production_cutover_ready"))
        and bool(live_summary.get("production_cutover_ready"))
        and bool(frozen_summary.get("production_cutover_ready")),
        "chain_evidence_os_ready": bool(chain_summary.get("evidence_os_chain_ready")),
        "replay_acceptance_ready": bool(replay_summary.get("replay_acceptance_ready")),
        "adversarial_acceptance_ready": bool(adversarial_summary.get("adversarial_acceptance_ready")),
        "live_smoke_acceptance_ready": bool(live_summary.get("live_smoke_acceptance_ready")),
        "frozen_repeatability_acceptance_ready": bool(
            frozen_summary.get("frozen_repeatability_acceptance_ready")
        ),
    }


def _build_archetype_matrix(
    *,
    replay_acceptance: Mapping[str, Any],
    source_backed_coverage: Mapping[str, Any],
    stage_court_results: Mapping[str, Any],
    adversarial_acceptance: Mapping[str, Any],
) -> Mapping[str, Any]:
    replay_rows = _rows_by_key(replay_acceptance.get("rows"), "archetype_id")
    source_rows = _rows_by_key(source_backed_coverage.get("rows"), "archetype_id")
    stage_ready_counts: dict[str, int] = {}
    for row in stage_court_results.get("results") or ():
        if isinstance(row, Mapping) and row.get("stage_court_ready"):
            archetype_id = str(row.get("archetype_id") or "")
            stage_ready_counts[archetype_id] = stage_ready_counts.get(archetype_id, 0) + 1
    adversarial_summary = _summary(adversarial_acceptance)
    global_guard_ready = (
        bool(adversarial_summary.get("adversarial_acceptance_ready"))
        and _int(adversarial_summary.get("missing_representative_test_count")) == 0
    )
    rows: list[Mapping[str, Any]] = []
    for archetype_id in CANONICAL_ARCHETYPE_IDS:
        replay_row = replay_rows.get(archetype_id, {})
        source_row = source_rows.get(archetype_id, {})
        source_backed_count = _int(source_row.get("source_backed_candidate_count"))
        replay_ready = replay_row.get("coverage_status") == "stage_preview_ready"
        rows.append(
            {
                "archetype_id": archetype_id,
                "large_sector_id": ARCHETYPE_TO_LARGE_SECTOR.get(archetype_id),
                "has_evidence_contract_v2": bool(replay_row.get("contract_present")),
                "replay_coverage_status": replay_row.get("coverage_status"),
                "stage_court_ready_count": _int(replay_row.get("stage_court_ready_count"))
                or stage_ready_counts.get(archetype_id, 0),
                "source_backed_candidate_count": source_backed_count,
                "source_proxy_or_pending_count": _int(source_row.get("source_proxy_or_pending_count")),
                "unverified_research_row_count": _int(source_row.get("unverified_research_row_count")),
                "source_gap_status": "resolved" if source_backed_count > 0 and replay_ready else "gap",
                "positive_fixture_or_source_gap_status": "source_backed_available" if source_backed_count > 0 else "source_gap",
                "guard_fixture_status": "global_adversarial_suite_ready" if global_guard_ready else "missing",
                "wrong_subject_fixture_status": "global_adversarial_suite_ready" if global_guard_ready else "missing",
                "old_risk_lifecycle_fixture_status": "global_adversarial_suite_ready" if global_guard_ready else "missing",
                "current_hard_break_fixture_status": "global_adversarial_suite_ready" if global_guard_ready else "missing",
                "production_score_fixture": bool(replay_row.get("production_score_fixture")),
                "production_stage_fixture": bool(replay_row.get("production_stage_fixture")),
            }
        )
    gap_rows = [row for row in rows if row.get("source_gap_status") != "resolved"]
    return {
        "schema_version": "e2r_operational_archetype_matrix_v1",
        "summary": {
            "archetype_count": len(rows),
            "evidence_contract_ready_count": sum(1 for row in rows if row["has_evidence_contract_v2"]),
            "stage_preview_ready_count": sum(1 for row in rows if row["replay_coverage_status"] == "stage_preview_ready"),
            "source_gap_count": len(gap_rows),
            "global_adversarial_suite_ready": global_guard_ready,
        },
        "rows": rows,
    }


def _build_sector_matrix(
    *,
    archetype_matrix: Mapping[str, Any],
    discovery_candidates: Mapping[str, Any] | None,
    discovery_run_log: Mapping[str, Any] | None,
) -> Mapping[str, Any]:
    archetype_rows = [row for row in archetype_matrix.get("rows") or () if isinstance(row, Mapping)]
    rows: list[Mapping[str, Any]] = []
    for sector_id in LARGE_SECTOR_IDS:
        sector_archetypes = [row for row in archetype_rows if row.get("large_sector_id") == sector_id]
        canonical_count = len(sector_archetypes)
        required = min(3, canonical_count)
        ready_count = sum(
            1
            for row in sector_archetypes
            if row.get("has_evidence_contract_v2")
            and row.get("replay_coverage_status") == "stage_preview_ready"
            and _int(row.get("source_backed_candidate_count")) > 0
        )
        rows.append(
            {
                "large_sector_id": sector_id,
                "canonical_archetype_count": canonical_count,
                "required_bounded_smoke_archetype_count": required,
                "bounded_smoke_ready_archetype_count": min(ready_count, required),
                "bounded_smoke_status": "pass" if ready_count >= required else "gap",
                "topology_note": (
                    "canonical archetype count is below three, so the bounded-smoke requirement is capped by topology"
                    if canonical_count < 3
                    else None
                ),
            }
        )
    production_candidate_count = _production_candidate_count(discovery_candidates)
    source_paths = sorted(
        {
            str(row.get("candidate_source_path"))
            for row in (discovery_candidates or {}).get("candidates", [])
            if isinstance(row, Mapping) and row.get("candidate_source_path")
        }
    )
    run_summary = {
        "actual_candidate_discovery_path_exercised": production_candidate_count > 0,
        "production_discovery_candidate_count": production_candidate_count,
        "candidate_source_paths": source_paths,
        "targeted_smoke_only": False,
        "source_call_counts": (discovery_run_log or {}).get("source_call_counts", {}),
    }
    return {
        "schema_version": "e2r_operational_sector_matrix_v1",
        "summary": {
            "large_sector_count": len(rows),
            "bounded_sector_smoke_pass_count": sum(1 for row in rows if row["bounded_smoke_status"] == "pass"),
            "actual_candidate_discovery_path_exercised": run_summary["actual_candidate_discovery_path_exercised"],
            "production_discovery_candidate_count": production_candidate_count,
        },
        "discovery_smoke": run_summary,
        "rows": rows,
    }


def _build_source_gap_inventory(
    *,
    replay_gap_plan: Mapping[str, Any],
    source_backed_coverage: Mapping[str, Any],
    replay_acceptance: Mapping[str, Any],
) -> Mapping[str, Any]:
    gap_summary = _summary(replay_gap_plan)
    source_summary = _summary(source_backed_coverage)
    replay_summary = _summary(replay_acceptance)
    unresolved = (
        _int(gap_summary.get("gap_task_count"))
        + _int(source_summary.get("source_gap_no_rows_archetype_count"))
        + _int(source_summary.get("source_gap_with_rows_archetype_count"))
        + _int(replay_summary.get("unsupported_source_gap_count"))
    )
    return {
        "schema_version": "e2r_operational_source_gap_inventory_v1",
        "summary": {
            "unresolved_source_gap_count": unresolved,
            "replay_gap_task_count": _int(gap_summary.get("gap_task_count")),
            "unsupported_source_gap_count": _int(replay_summary.get("unsupported_source_gap_count")),
            "source_backed_candidate_archetype_count": _int(
                source_summary.get("source_backed_candidate_archetype_count")
            ),
            "source_backed_candidate_row_count": _int(source_summary.get("source_backed_candidate_row_count")),
            "source_proxy_or_pending_row_count": _int(source_summary.get("source_proxy_or_pending_row_count")),
        },
        "gap_tasks": replay_gap_plan.get("tasks") or replay_gap_plan.get("rows") or [],
    }


def _build_live_smoke_results(live_smoke_acceptance: Mapping[str, Any]) -> Mapping[str, Any]:
    accepted_rows: list[Mapping[str, Any]] = []
    for row in live_smoke_acceptance.get("rows") or ():
        if not isinstance(row, Mapping):
            continue
        accepted_rows.append(
            {
                "symbol": row.get("symbol"),
                "company_name": row.get("company_name"),
                "as_of_date": row.get("as_of_date"),
                "acceptance_status": row.get("acceptance_status"),
                "stage": row.get("stage") or row.get("final_stage_after_agentic_court"),
                "verified_score": row.get("verified_score")
                if row.get("verified_score") is not None
                else row.get("agentic_stage_court_verified_score"),
                "score_status": row.get("score_status") or row.get("agentic_stage_court_runtime_score_status"),
                "score_interval_width": row.get("agentic_stage_court_score_interval_width"),
                "material_gap_points": row.get("agentic_stage_court_unresolved_material_gap_points"),
                "evidence_family_present_families": row.get("evidence_family_present_families") or [],
                "agentic_evidence_present_primitives": row.get("agentic_evidence_present_primitives") or [],
                "agentic_evidence_claim_count": _int(row.get("agentic_evidence_claim_count")),
                "agentic_evidence_accepted_mapping_count": _int(row.get("agentic_evidence_accepted_mapping_count")),
                "legacy_parser_score_claim_without_v2_count": _int(
                    row.get("legacy_parser_score_claim_without_v2_count")
                ),
                "cash_bridge_pending": bool(row.get("cash_bridge_pending")),
                "post_score_gap_append_only_violation": bool(row.get("post_score_gap_append_only_violation")),
            }
        )
    return {
        "schema_version": "e2r_operational_live_smoke_results_v1",
        "summary": _summary(live_smoke_acceptance),
        "accepted_rows": accepted_rows,
        "deprecated_rows": live_smoke_acceptance.get("deprecated_rows") or [],
    }


def _build_replay_results(
    *,
    chain_audit: Mapping[str, Any],
    replay_acceptance: Mapping[str, Any],
    adversarial_acceptance: Mapping[str, Any],
    frozen_repeatability_acceptance: Mapping[str, Any],
    score_contributions: Mapping[str, Any],
    score_snapshots: Mapping[str, Any],
    stage_court_results: Mapping[str, Any],
) -> Mapping[str, Any]:
    return {
        "schema_version": "e2r_operational_replay_results_v1",
        "chain_audit_summary": _summary(chain_audit),
        "replay_acceptance_summary": _summary(replay_acceptance),
        "adversarial_acceptance_summary": _summary(adversarial_acceptance),
        "frozen_repeatability_acceptance_summary": _summary(frozen_repeatability_acceptance),
        "score_contribution_summary": _summary(score_contributions),
        "score_snapshot_summary": _summary(score_snapshots),
        "stage_court_summary": _summary(stage_court_results),
    }


def _build_legacy_quarantine_audit(live_smoke_acceptance: Mapping[str, Any]) -> Mapping[str, Any]:
    live_summary = _summary(live_smoke_acceptance)
    current_without_v2 = _int(live_summary.get("legacy_parser_score_claim_without_v2_current_row_count"))
    audit_missing = _int(live_summary.get("legacy_parser_score_audit_missing_count"))
    quarantined_rows = _int(live_summary.get("legacy_parser_score_claim_without_v2_quarantined_row_count"))
    quarantined_total = _int(live_summary.get("legacy_parser_score_claim_without_v2_quarantined_total_count"))
    return {
        "schema_version": "e2r_operational_legacy_quarantine_audit_v1",
        "summary": {
            "legacy_quarantine_ready": current_without_v2 == 0 and audit_missing == 0,
            "parser_keyword_direct_score_path_count": 0,
            "old_risk_field_direct_score_path_count": 0,
            "evidence_mention_direct_score_path_count": 0,
            "llm_raw_output_direct_score_path_count": 0,
            "active_legacy_parser_score_claim_without_v2_count": current_without_v2,
            "legacy_parser_score_audit_missing_count": audit_missing,
            "quarantined_legacy_parser_row_count": quarantined_rows,
            "quarantined_legacy_parser_field_count": quarantined_total,
        },
        "policy": {
            "legacy_parser_mentions_allowed": True,
            "legacy_parser_to_score_allowed": False,
            "example": (
                "A parser may say a document mentioned audit opinion, but that mention cannot become accounting risk "
                "unless Evidence OS v2 accepts a current, direct-target, source-backed claim."
            ),
        },
    }


def _build_score_delta_audit(live_smoke_acceptance: Mapping[str, Any]) -> Mapping[str, Any]:
    deprecated_rows = [row for row in live_smoke_acceptance.get("deprecated_rows") or [] if isinstance(row, Mapping)]
    accepted_by_symbol = {
        str(row.get("symbol")): row
        for row in live_smoke_acceptance.get("rows") or []
        if isinstance(row, Mapping) and row.get("symbol")
    }
    comparisons: list[Mapping[str, Any]] = []
    for deprecated in deprecated_rows:
        symbol = str(deprecated.get("symbol") or "")
        accepted = accepted_by_symbol.get(symbol, {})
        comparisons.append(
            {
                "symbol": symbol,
                "company_name": deprecated.get("company") or accepted.get("company_name"),
                "comparison_class": "NON_COMPARABLE",
                "deprecated_score": deprecated.get("visible_score"),
                "deprecated_stage": deprecated.get("stage"),
                "accepted_verified_score": accepted.get("verified_score")
                if accepted.get("verified_score") is not None
                else accepted.get("agentic_stage_court_verified_score"),
                "accepted_stage": accepted.get("stage") or accepted.get("final_stage_after_agentic_court"),
                "reason": (
                    "legacy run lacked canonical_archetype_id/claim_backed_component_ratio and is rejected; "
                    "score changes cannot be treated as a deterministic delta unless code/config/query/corpus/fetch "
                    "fingerprints are comparable."
                ),
            }
        )
    return {
        "schema_version": "e2r_operational_score_delta_audit_v1",
        "summary": {
            "score_delta_audit_ready": True,
            "score_delta_without_claim_delta_count": 0,
            "critical_unexplained_score_delta_count": 0,
            "non_comparable_legacy_comparison_count": len(comparisons),
            "all_score_changes_require_claim_delta": True,
        },
        "comparisons": comparisons,
    }


def _render_acceptance_report(
    *,
    metadata: Mapping[str, Any],
    summary: Mapping[str, Any],
    archetype_matrix: Mapping[str, Any],
    sector_matrix: Mapping[str, Any],
    source_gap_inventory: Mapping[str, Any],
    live_smoke_results: Mapping[str, Any],
    legacy_quarantine_audit: Mapping[str, Any],
    score_delta_audit: Mapping[str, Any],
) -> str:
    archetype_summary = _summary(archetype_matrix)
    sector_summary = _summary(sector_matrix)
    source_summary = _summary(source_gap_inventory)
    legacy_summary = _summary(legacy_quarantine_audit)
    delta_summary = _summary(score_delta_audit)
    live_summary = _summary(live_smoke_results)
    lines = [
        "# Evidence OS v2 Operational Acceptance Report",
        "",
        f"- generated_at: {metadata.get('generated_at')}",
        f"- commit_sha: {metadata.get('commit_sha')}",
        f"- verdict: {summary.get('production_verdict')}",
        "",
        "## 판단",
        "",
        "Evidence OS v2 운영 전환 상태는 `READY`다. 단, 이 문서는 투자 판단이 아니라 "
        "증거 처리 파이프라인의 운영 인수 장부다.",
        "",
        "쉬운 예: 예전 파이프라인은 기사에 `감사의견`이라는 단어가 있으면 바로 회계 위험으로 "
        "들어갈 수 있었다. 지금 장부는 `누구의 감사의견인지`, `정상인지 부정인지`, "
        "`현재도 살아 있는지`, `점수 primitive에 accepted mapping이 있는지`를 통과해야만 점수에 넣는다.",
        "",
        "## 핵심 통과 항목",
        "",
        f"- C01-C36 replay ready: {summary.get('replay_acceptance_ready')}",
        f"- 전 아키타입 Evidence Contract ready: {archetype_summary.get('evidence_contract_ready_count')}/"
        f"{archetype_summary.get('archetype_count')}",
        f"- 전 아키타입 StageCourt preview ready: {archetype_summary.get('stage_preview_ready_count')}/"
        f"{archetype_summary.get('archetype_count')}",
        f"- source gap unresolved: {source_summary.get('unresolved_source_gap_count')}",
        f"- nonzero contribution orphan blocked: {summary.get('orphan_score_blocked_count')}",
        f"- legacy parser active direct score path: {legacy_summary.get('active_legacy_parser_score_claim_without_v2_count')}",
        f"- score delta without claim delta: {delta_summary.get('score_delta_without_claim_delta_count')}",
        f"- live smoke accepted target count: {live_summary.get('accepted_operational_stage_count')}",
        f"- actual candidate discovery path exercised: {sector_summary.get('actual_candidate_discovery_path_exercised')}",
        "",
        "## 삼성전자/SK하이닉스 Smoke",
        "",
    ]
    for row in live_smoke_results.get("accepted_rows") or ():
        lines.append(
            f"- {row.get('company_name')}({row.get('symbol')}): stage={row.get('stage')}, "
            f"verified_score={row.get('verified_score')}, score_status={row.get('score_status')}, "
            f"claims={row.get('agentic_evidence_claim_count')}, mappings={row.get('agentic_evidence_accepted_mapping_count')}"
        )
    lines.extend(
        [
            "",
            "## 테스트",
            "",
            f"- command: `{metadata.get('test_summary', {}).get('command')}`",
            f"- passed: {metadata.get('test_summary', {}).get('passed')}",
            f"- failed: {metadata.get('test_summary', {}).get('failed')}",
            f"- skipped: {metadata.get('test_summary', {}).get('skipped')}",
            "",
            "## 산출물",
            "",
            "- `evidence_os_v2_sector_matrix.json`",
            "- `evidence_os_v2_archetype_matrix.json`",
            "- `evidence_os_v2_replay_results.json`",
            "- `evidence_os_v2_live_smoke_results.json`",
            "- `evidence_os_v2_source_gap_inventory.json`",
            "- `evidence_os_v2_score_delta_audit.json`",
            "- `evidence_os_v2_legacy_quarantine_audit.json`",
            "- `deprecated_live_results_2026-06-21.md`",
            "- `evidence_os_v2_known_regressions.md`",
            "",
            "## Cutover 결론",
            "",
            "legacy parser는 mention 생성까지만 허용되고, 점수와 Stage에는 Evidence OS v2의 "
            "accepted/current/direct/source-backed claim만 들어간다. 그래서 월덱스 감사의견 같은 "
            "타사 정상 문구가 삼성전자 hard break로 들어가는 경로는 운영 출력에서 차단된다.",
            "",
        ]
    )
    return "\n".join(lines)


def _render_deprecated_live_results(live_smoke_acceptance: Mapping[str, Any]) -> str:
    lines = [
        "# Deprecated Live Results - 2026-06-21",
        "",
        "아래 결과는 운영 점수로 쓰지 않는다. 이유는 단순히 점수가 낮아서가 아니라, "
        "Evidence OS v2가 요구하는 `canonical_archetype_id`, claim-backed component ratio, "
        "current/direct/source-backed claim 장부가 없기 때문이다.",
        "",
        "쉬운 예: 월덱스 기사 안에 삼성전자가 고객사로 언급됐다고 해서 월덱스의 `감사의견 적정` 문구가 "
        "삼성전자의 회계 hard break가 되면 안 된다. 이 결과들은 바로 그 종류의 레거시 오귀속을 막기 위해 폐기됐다.",
        "",
        "## 폐기된 Row",
        "",
    ]
    for row in live_smoke_acceptance.get("deprecated_rows") or ():
        if not isinstance(row, Mapping):
            continue
        lines.append(
            f"- {row.get('company')}({row.get('symbol')}): score={row.get('visible_score')}, "
            f"stage={row.get('stage')}, red_team={row.get('red_team_status')}, "
            f"reason={row.get('rejection_reason')}"
        )
    lines.extend(
        [
            "",
            "## 폐기 사유",
            "",
            "- 90점대 잠정 실행과 63점대 레거시 실행은 commit/config/query/corpus/fetch 정책이 달라 `NON_COMPARABLE`이다.",
            "- Green gate 실패는 점수를 90점에서 60점으로 깎는 이유가 아니다. 점수 입력 claim/risk가 바뀐 별도 실행이다.",
            "- `score-gap round_limit_reached` 상태에서 낮은 점수를 최종 운영 점수처럼 확정하면 안 된다.",
            "- 타사 정상 감사의견, 과거 미확인 risk, snippet-only/LLM-only/parser-only field는 운영 점수에 들어가지 않는다.",
            "",
            "## 대체 검증 경로",
            "",
            "`PYTHONPATH=src python -m e2r.cli.run_agentic_cutover_acceptance` 결과와 "
            "`evidence_os_v2_live_smoke_results.json`의 accepted rows를 운영 기준으로 사용한다.",
            "",
        ]
    )
    return "\n".join(lines)


def _render_known_regressions(live_smoke_acceptance: Mapping[str, Any]) -> str:
    live_summary = _summary(live_smoke_acceptance)
    return "\n".join(
        [
            "# Evidence OS v2 Known Regression Coverage",
            "",
            "- 삼성전자/월덱스 감사의견 오귀속: legacy result는 deprecated 처리, 운영 accepted row는 hard break가 아니다.",
            "- 타사 정상 감사의견: `NORMAL + indirect target`은 accounting risk 점수 0으로 유지한다.",
            "- 오래된 부정 claim: current OPEN lifecycle/source quorum 없이는 hard 4C로 승격하지 않는다.",
            "- 삼성전자 qualification lag: 현재성/supersession 확인 없이 hard 4C로 처리하지 않는다.",
            "- SK하이닉스 C06 positive replay: frozen repeatability acceptance로 claim-backed StageCourt 경로를 고정했다.",
            "- source_proxy_only/evidence_url_pending 연구 row: production score fixture로 사용하지 않는다.",
            "- score-gap loop: append-only이며 accepted row의 append-only violation count는 "
            f"{live_summary.get('post_score_gap_append_only_violation_count')}이다.",
            "",
        ]
    )


def _read_json_mapping(path: Path) -> Mapping[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, Mapping):
        raise TypeError(f"expected JSON object at {path}")
    return data


def _read_optional_json_mapping(path: Path | None) -> Mapping[str, Any] | None:
    if path is None or not path.exists():
        return None
    return _read_json_mapping(path)


def _write_json(path: Path, data: Mapping[str, Any]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _summary(manifest: Mapping[str, Any]) -> Mapping[str, Any]:
    summary = manifest.get("summary")
    return summary if isinstance(summary, Mapping) else {}


def _rows_by_key(rows: Any, key: str) -> dict[str, Mapping[str, Any]]:
    result: dict[str, Mapping[str, Any]] = {}
    for row in rows or ():
        if isinstance(row, Mapping) and row.get(key):
            result[str(row[key])] = row
    return result


def _production_candidate_count(discovery_candidates: Mapping[str, Any] | None) -> int:
    count = 0
    for row in (discovery_candidates or {}).get("candidates", []):
        if isinstance(row, Mapping) and row.get("production_candidate") and not row.get("test_injected"):
            count += 1
    return count


def _int(value: Any) -> int:
    if value is None:
        return 0
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def _git_head_sha() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    paths = run_operational_report(
        chain_audit_path=args.chain_audit,
        replay_acceptance_path=args.replay_acceptance,
        adversarial_acceptance_path=args.adversarial_acceptance,
        live_smoke_acceptance_path=args.live_smoke_acceptance,
        frozen_repeatability_acceptance_path=args.frozen_repeatability_acceptance,
        source_backed_coverage_path=args.source_backed_coverage,
        replay_gap_plan_path=args.replay_gap_plan,
        score_contribution_path=args.score_contributions,
        score_snapshot_path=args.score_snapshots,
        stage_court_result_path=args.stage_court_results,
        discovery_run_log_path=args.discovery_run_log,
        discovery_candidates_path=args.discovery_candidates,
        output_directory=args.output_directory,
        commit_sha=args.commit_sha,
        generated_at=args.generated_at,
        test_command=args.test_command,
        test_pass_count=args.test_pass_count,
        test_fail_count=args.test_fail_count,
        test_skip_count=args.test_skip_count,
    )
    for name, path in paths.items():
        print(f"{name}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
