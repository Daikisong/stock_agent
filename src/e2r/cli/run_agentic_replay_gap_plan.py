"""Build source-backed replay gap tasks from C01-C36 acceptance."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic import load_evidence_contracts_v2


DEFAULT_REPLAY_ACCEPTANCE = (
    "output/0621_agentic_replay/"
    "c01_c36_combined_replacement_metadata_asof_source_recovery_v13_replay_acceptance_acceptance.json"
)
DEFAULT_OUTPUT_DIRECTORY = "output/0621_agentic_replay"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build source-backed replay gap plan from replay acceptance.")
    parser.add_argument("--replay-acceptance", default=DEFAULT_REPLAY_ACCEPTANCE)
    parser.add_argument("--evidence-contracts-v2", default=None)
    parser.add_argument(
        "--source-backed-fixture-seeds",
        default=None,
        help=(
            "Optional fixture seed manifest. When provided, unsupported_source_gap tasks are "
            "split into source snapshot / EvidenceDocument fixture blockers instead of a vague source gap."
        ),
    )
    parser.add_argument(
        "--source-evidence-document-fixtures",
        default=None,
        help=(
            "Optional original-source EvidenceDocument fixture manifest. When provided, gap tasks show "
            "which source snapshots already passed as-of verification and need claim replay."
        ),
    )
    parser.add_argument(
        "--replacement-evidence-document-fixtures",
        default=None,
        help=(
            "Optional replacement EvidenceDocument fixture manifest. When provided, gap tasks show "
            "which archetypes already have verified EvidenceDocument fixtures but still need claim replay."
        ),
    )
    parser.add_argument(
        "--claim-replay-tasks",
        default=None,
        help=(
            "Optional claim replay task manifest. When provided, gap tasks show which verified fixtures "
            "already have contract-blind extraction tasks and only need extraction/adjudication execution."
        ),
    )
    parser.add_argument(
        "--claim-replay-results",
        default=None,
        help="Optional claim replay result manifest used to distinguish extraction-pending from no-raw-assertion gaps.",
    )
    parser.add_argument(
        "--adjudication-results",
        default=None,
        help="Optional adjudication result manifest used to distinguish target/temporal blockers.",
    )
    parser.add_argument(
        "--primitive-mapping-results",
        default=None,
        help="Optional primitive mapping result manifest used to distinguish all-rejected mapping gaps.",
    )
    parser.add_argument(
        "--eligibility-results",
        default=None,
        help="Optional eligibility result manifest used to distinguish source-anchor eligibility blockers.",
    )
    parser.add_argument(
        "--stage-court-results",
        default=None,
        help="Optional stage court result manifest used to identify downstream stage preview blockers.",
    )
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument(
        "--output-prefix",
        default="c01_c36_combined_replacement_metadata_asof_source_recovery_v13_replay_gap_plan",
    )
    return parser


def run_replay_gap_plan(
    *,
    replay_acceptance_manifest_path: str | Path,
    output_directory: str | Path,
    output_prefix: str = "c01_c36_combined_replacement_metadata_asof_source_recovery_v13_replay_gap_plan",
    evidence_contracts_v2_path: str | Path | None = None,
    source_backed_fixture_seed_manifest_path: str | Path | None = None,
    source_evidence_document_fixture_manifest_path: str | Path | None = None,
    replacement_evidence_document_fixture_manifest_path: str | Path | None = None,
    claim_replay_task_manifest_path: str | Path | None = None,
    claim_replay_result_manifest_path: str | Path | None = None,
    adjudication_result_manifest_path: str | Path | None = None,
    primitive_mapping_result_manifest_path: str | Path | None = None,
    eligibility_result_manifest_path: str | Path | None = None,
    stage_court_result_manifest_path: str | Path | None = None,
) -> Mapping[str, Path]:
    replay_acceptance = _read_json_mapping(Path(replay_acceptance_manifest_path))
    contracts = load_evidence_contracts_v2(path=evidence_contracts_v2_path)
    fixture_seed_manifest = (
        _read_json_mapping(Path(source_backed_fixture_seed_manifest_path))
        if source_backed_fixture_seed_manifest_path
        else None
    )
    replacement_fixture_manifest = (
        _read_json_mapping(Path(replacement_evidence_document_fixture_manifest_path))
        if replacement_evidence_document_fixture_manifest_path
        else None
    )
    source_fixture_manifest = (
        _read_json_mapping(Path(source_evidence_document_fixture_manifest_path))
        if source_evidence_document_fixture_manifest_path
        else None
    )
    claim_replay_task_manifest = (
        _read_json_mapping(Path(claim_replay_task_manifest_path))
        if claim_replay_task_manifest_path
        else None
    )
    claim_replay_result_manifest = (
        _read_json_mapping(Path(claim_replay_result_manifest_path))
        if claim_replay_result_manifest_path
        else None
    )
    adjudication_result_manifest = (
        _read_json_mapping(Path(adjudication_result_manifest_path))
        if adjudication_result_manifest_path
        else None
    )
    primitive_mapping_result_manifest = (
        _read_json_mapping(Path(primitive_mapping_result_manifest_path))
        if primitive_mapping_result_manifest_path
        else None
    )
    eligibility_result_manifest = (
        _read_json_mapping(Path(eligibility_result_manifest_path))
        if eligibility_result_manifest_path
        else None
    )
    stage_court_result_manifest = (
        _read_json_mapping(Path(stage_court_result_manifest_path))
        if stage_court_result_manifest_path
        else None
    )
    manifest = build_replay_gap_plan_manifest(
        replay_acceptance_manifest=replay_acceptance,
        contracts=contracts,
        source_backed_fixture_seed_manifest=fixture_seed_manifest,
        source_evidence_document_fixture_manifest=source_fixture_manifest,
        replacement_evidence_document_fixture_manifest=replacement_fixture_manifest,
        claim_replay_task_manifest=claim_replay_task_manifest,
        claim_replay_result_manifest=claim_replay_result_manifest,
        adjudication_result_manifest=adjudication_result_manifest,
        primitive_mapping_result_manifest=primitive_mapping_result_manifest,
        eligibility_result_manifest=eligibility_result_manifest,
        stage_court_result_manifest=stage_court_result_manifest,
    )
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "gap_plan_json": output_dir / f"{output_prefix}_gap_plan.json",
        "gap_plan_md": output_dir / f"{output_prefix}_gap_plan.md",
    }
    _write_json(paths["gap_plan_json"], manifest)
    paths["gap_plan_md"].write_text(_render_gap_plan_markdown(manifest), encoding="utf-8")
    return paths


def build_replay_gap_plan_manifest(
    *,
    replay_acceptance_manifest: Mapping[str, Any],
    contracts: Mapping[str, Any],
    source_backed_fixture_seed_manifest: Mapping[str, Any] | None = None,
    source_evidence_document_fixture_manifest: Mapping[str, Any] | None = None,
    replacement_evidence_document_fixture_manifest: Mapping[str, Any] | None = None,
    claim_replay_task_manifest: Mapping[str, Any] | None = None,
    claim_replay_result_manifest: Mapping[str, Any] | None = None,
    adjudication_result_manifest: Mapping[str, Any] | None = None,
    primitive_mapping_result_manifest: Mapping[str, Any] | None = None,
    eligibility_result_manifest: Mapping[str, Any] | None = None,
    stage_court_result_manifest: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    source_status_by_archetype = _source_status_by_archetype(source_backed_fixture_seed_manifest or {})
    fixture_status_by_archetype = _merge_status_maps(
        _fixture_status_by_archetype(source_evidence_document_fixture_manifest or {}),
        _fixture_status_by_archetype(replacement_evidence_document_fixture_manifest or {}),
    )
    claim_task_status_by_archetype = _claim_task_status_by_archetype(claim_replay_task_manifest or {})
    post_chain_status_by_archetype = _merge_status_maps(
        _claim_replay_result_status_by_archetype(claim_replay_result_manifest or {}),
        _adjudication_result_status_by_archetype(adjudication_result_manifest or {}),
        _primitive_mapping_result_status_by_archetype(primitive_mapping_result_manifest or {}),
        _eligibility_result_status_by_archetype(eligibility_result_manifest or {}),
        _stage_court_result_status_by_archetype(stage_court_result_manifest or {}),
    )
    tasks: list[Mapping[str, Any]] = []
    for row in replay_acceptance_manifest.get("rows") or ():
        if not isinstance(row, Mapping):
            continue
        status = str(row.get("coverage_status") or "")
        if status == "stage_preview_ready":
            continue
        archetype_id = str(row.get("archetype_id") or "")
        contract = contracts.get(archetype_id)
        required_primitives = list(getattr(contract, "required_primitives", ()) if contract else ())
        green_gate_primitives = list(contract.green_gate.primitive_ids() if contract else ())
        source_status = dict(source_status_by_archetype.get(archetype_id, {}))
        fixture_status = fixture_status_by_archetype.get(archetype_id, {})
        source_status["evidence_document_fixture_ready_count"] = fixture_status.get(
            "evidence_document_fixture_ready_count",
            source_status.get("evidence_document_fixture_ready_count", 0),
        )
        source_status["claim_replay_ready_count"] = fixture_status.get("claim_replay_ready_count", 0)
        source_status["replacement_fixture_row_count"] = fixture_status.get("replacement_fixture_row_count", 0)
        claim_task_status = claim_task_status_by_archetype.get(archetype_id, {})
        source_status["claim_replay_task_count"] = claim_task_status.get("claim_replay_task_count", 0)
        source_status["contract_blind_task_count"] = claim_task_status.get("contract_blind_task_count", 0)
        post_chain_status = dict(post_chain_status_by_archetype.get(archetype_id, {}))
        post_chain_gap_stage = _post_chain_gap_stage(status, source_status, post_chain_status)
        tasks.append(
            {
                "task_id": f"RPLAY-GAP-{len(tasks) + 1:03d}",
                "archetype_id": archetype_id,
                "coverage_status": status,
                "contract_present": bool(contract),
                "required_primitives": required_primitives,
                "green_gate_primitives": green_gate_primitives,
                "score_rubric_components": sorted((getattr(contract, "score_rubric", {}) or {}).keys()),
                "source_quorum_keys": sorted((getattr(contract, "source_quorum", {}) or {}).keys()),
                "source_backed_seed_count": source_status.get("source_backed_seed_count", 0),
                "snapshot_request_ready_count": source_status.get("snapshot_request_ready_count", 0),
                "pending_source_snapshot_count": source_status.get("pending_source_snapshot_count", 0),
                "evidence_document_fixture_ready_count": source_status.get("evidence_document_fixture_ready_count", 0),
                "claim_replay_ready_count": source_status.get("claim_replay_ready_count", 0),
                "claim_replay_task_count": source_status.get("claim_replay_task_count", 0),
                "contract_blind_task_count": source_status.get("contract_blind_task_count", 0),
                "replacement_fixture_row_count": source_status.get("replacement_fixture_row_count", 0),
                "production_score_fixture_count": source_status.get("production_score_fixture_count", 0),
                "source_gap_stage": _source_gap_stage(status, source_status),
                "next_action": _next_action_for_status(status, source_status),
                "post_chain_gap_stage": post_chain_gap_stage,
                "post_chain_next_action": _post_chain_next_action(post_chain_gap_stage),
                **post_chain_status,
                "production_score_fixture": False,
                "production_stage_fixture": False,
            }
        )

    status_counts: dict[str, int] = {}
    for task in tasks:
        status = str(task.get("coverage_status") or "")
        status_counts[status] = status_counts.get(status, 0) + 1
    replay_summary = replay_acceptance_manifest.get("summary")
    if not isinstance(replay_summary, Mapping):
        replay_summary = {}
    replay_ready = bool(
        replay_summary.get("replay_acceptance_ready") is True
        or replay_summary.get("production_cutover_ready") is True
    )
    no_remaining_gap_tasks = not tasks
    return {
        "schema_version": "e2r_replay_gap_plan_manifest_v1",
        "source_replay_acceptance_schema_version": replay_acceptance_manifest.get("schema_version"),
        "source_fixture_seed_schema_version": (source_backed_fixture_seed_manifest or {}).get("schema_version"),
        "source_evidence_document_fixture_schema_version": (
            source_evidence_document_fixture_manifest or {}
        ).get("schema_version"),
        "source_replacement_evidence_document_fixture_schema_version": (
            replacement_evidence_document_fixture_manifest or {}
        ).get("schema_version"),
        "source_claim_replay_task_schema_version": (claim_replay_task_manifest or {}).get("schema_version"),
        "summary": {
            "gap_task_count": len(tasks),
            "unsupported_source_gap_task_count": status_counts.get("unsupported_source_gap", 0),
            "primitive_state_present_stage_not_ready_task_count": status_counts.get(
                "primitive_state_present_stage_not_ready",
                0,
            ),
            "evidence_contract_missing_task_count": status_counts.get("evidence_contract_missing", 0),
            "replay_stage_preview_ready_count": replay_summary.get("stage_preview_ready_count"),
            "replay_unsupported_source_gap_count": replay_summary.get("unsupported_source_gap_count"),
            "source_backed_seed_gap_task_count": sum(
                1 for task in tasks if int(task.get("source_backed_seed_count") or 0) > 0
            ),
            "snapshot_request_ready_gap_task_count": sum(
                1 for task in tasks if int(task.get("snapshot_request_ready_count") or 0) > 0
            ),
            "evidence_document_fixture_ready_gap_task_count": sum(
                1 for task in tasks if int(task.get("evidence_document_fixture_ready_count") or 0) > 0
            ),
            "claim_replay_ready_gap_task_count": sum(
                1 for task in tasks if int(task.get("claim_replay_ready_count") or 0) > 0
            ),
            "claim_replay_task_ready_gap_task_count": sum(
                1 for task in tasks if int(task.get("claim_replay_task_count") or 0) > 0
            ),
            "post_chain_no_raw_assertion_gap_task_count": sum(
                1 for task in tasks if task.get("post_chain_gap_stage") == "claim_replay_executed_no_raw_assertions"
            ),
            "post_chain_adjudication_blocked_gap_task_count": sum(
                1 for task in tasks if task.get("post_chain_gap_stage") == "adjudication_blocked_all_assertions"
            ),
            "post_chain_mapping_rejected_gap_task_count": sum(
                1 for task in tasks if task.get("post_chain_gap_stage") == "primitive_mapping_all_rejected"
            ),
            "post_chain_eligibility_blocked_gap_task_count": sum(
                1 for task in tasks if task.get("post_chain_gap_stage") == "eligibility_blocked_all_mappings"
            ),
            "production_cutover_ready": replay_ready and no_remaining_gap_tasks,
        },
        "coverage_status_counts": dict(sorted(status_counts.items())),
        "tasks": tasks,
    }


def _next_action_for_status(status: str, source_status: Mapping[str, Any] | None = None) -> str:
    source_status = source_status or {}
    if status == "unsupported_source_gap":
        if int(source_status.get("claim_replay_task_count") or 0) > 0:
            return "run_contract_blind_claim_extraction_for_claim_replay_tasks"
        if int(source_status.get("claim_replay_ready_count") or 0) > 0:
            return "run_claim_replay_from_verified_evidence_document_fixtures"
        if int(source_status.get("evidence_document_fixture_ready_count") or 0) > 0:
            return "run_claim_replay_with_target_identity_from_fixture_seed_manifest"
        if int(source_status.get("snapshot_request_ready_count") or 0) > 0:
            return "verify_source_snapshots_and_promote_evidence_document_fixtures"
        if int(source_status.get("source_backed_seed_count") or 0) > 0:
            return "recover_as_of_date_or_snapshot_request_for_source_backed_seeds"
        return "add_source_backed_replay_fixture_or_current_document_for_required_primitives"
    if status == "primitive_state_present_stage_not_ready":
        return "inspect_primitive_state_to_score_snapshot_stage_court_blocker"
    if status == "evidence_contract_missing":
        return "add_or_fix_evidence_contract_v2_before_replay"
    return "inspect_replay_acceptance_status"


def _source_gap_stage(status: str, source_status: Mapping[str, Any] | None = None) -> str:
    if status != "unsupported_source_gap":
        return "not_source_gap"
    source_status = source_status or {}
    if int(source_status.get("claim_replay_task_count") or 0) > 0:
        return "claim_replay_task_ready"
    if int(source_status.get("claim_replay_ready_count") or 0) > 0:
        return "claim_replay_ready_but_not_replayed"
    if int(source_status.get("evidence_document_fixture_ready_count") or 0) > 0:
        return "evidence_document_fixture_ready_claim_replay_pending"
    if int(source_status.get("snapshot_request_ready_count") or 0) > 0:
        return "source_snapshot_verification_pending"
    if int(source_status.get("source_backed_seed_count") or 0) > 0:
        return "source_backed_seed_missing_snapshot_request"
    return "no_source_backed_seed"


def _post_chain_gap_stage(
    status: str,
    source_status: Mapping[str, Any],
    post_chain_status: Mapping[str, Any],
) -> str:
    if status != "unsupported_source_gap":
        return "not_source_gap"
    if int(post_chain_status.get("stage_court_result_count") or 0) > 0:
        return "stage_preview_exists_but_acceptance_missing"
    if int(post_chain_status.get("score_contribution_ready_count") or 0) > 0:
        return "score_contribution_ready_stage_not_built"
    if int(post_chain_status.get("eligibility_result_count") or 0) > 0:
        if int(post_chain_status.get("score_contribution_ready_count") or 0) <= 0:
            return "eligibility_blocked_all_mappings"
        return "eligibility_ready_downstream_pending"
    if int(post_chain_status.get("primitive_mapping_result_count") or 0) > 0:
        if int(post_chain_status.get("mapping_accepted_count") or 0) <= 0:
            return "primitive_mapping_all_rejected"
        return "primitive_mapping_accepted_eligibility_pending"
    if int(post_chain_status.get("adjudication_result_count") or 0) > 0:
        if int(post_chain_status.get("adjudication_mapping_ready_count") or 0) <= 0:
            return "adjudication_blocked_all_assertions"
        return "adjudication_ready_mapping_pending"
    if int(post_chain_status.get("claim_replay_result_count") or 0) > 0:
        if int(post_chain_status.get("raw_assertion_count") or 0) <= 0:
            return "claim_replay_executed_no_raw_assertions"
        return "claim_replay_executed_adjudication_pending"
    return _source_gap_stage(status, source_status)


def _post_chain_next_action(post_chain_gap_stage: str) -> str:
    if post_chain_gap_stage == "claim_replay_executed_no_raw_assertions":
        return "find_replacement_source_with_direct_target_assertion"
    if post_chain_gap_stage == "adjudication_blocked_all_assertions":
        return "find_source_with_direct_current_target_claim_or_review_entity_temporal_adjudication"
    if post_chain_gap_stage == "primitive_mapping_all_rejected":
        return "find_source_with_required_primitives_or_review_contract_mapping_rationale"
    if post_chain_gap_stage == "eligibility_blocked_all_mappings":
        return "inspect_eligibility_blockers_before_more_research"
    if post_chain_gap_stage == "primitive_mapping_accepted_eligibility_pending":
        return "run_eligibility_for_accepted_mappings"
    if post_chain_gap_stage == "adjudication_ready_mapping_pending":
        return "run_primitive_mapping_for_adjudicated_claims"
    if post_chain_gap_stage == "claim_replay_executed_adjudication_pending":
        return "run_target_temporal_adjudication_for_raw_assertions"
    if post_chain_gap_stage == "score_contribution_ready_stage_not_built":
        return "run_score_snapshot_and_stage_court"
    if post_chain_gap_stage == "stage_preview_exists_but_acceptance_missing":
        return "inspect_acceptance_union_or_archetype_deduplication"
    if post_chain_gap_stage == "source_snapshot_verification_pending":
        return "verify_source_snapshots_and_promote_evidence_document_fixtures"
    if post_chain_gap_stage == "claim_replay_task_ready":
        return "run_contract_blind_claim_extraction_for_claim_replay_tasks"
    if post_chain_gap_stage == "claim_replay_ready_but_not_replayed":
        return "run_claim_replay_from_verified_evidence_document_fixtures"
    if post_chain_gap_stage == "evidence_document_fixture_ready_claim_replay_pending":
        return "run_claim_replay_with_target_identity_from_fixture_seed_manifest"
    return "inspect_replay_acceptance_status"


def _claim_replay_result_status_by_archetype(manifest: Mapping[str, Any]) -> Mapping[str, Mapping[str, int]]:
    result: dict[str, dict[str, int]] = {}
    for row in _manifest_rows(manifest):
        archetype_id = str(row.get("archetype_id") or "").strip()
        if not archetype_id:
            continue
        bucket = result.setdefault(
            archetype_id,
            {
                "claim_replay_result_count": 0,
                "raw_assertion_count": 0,
                "no_raw_assertion_result_count": 0,
                "claim_replay_provider_error_count": 0,
            },
        )
        bucket["claim_replay_result_count"] += 1
        raw_assertions = row.get("raw_assertions") or ()
        raw_count = len(raw_assertions) if isinstance(raw_assertions, Sequence) and not isinstance(raw_assertions, (str, bytes, bytearray)) else 0
        bucket["raw_assertion_count"] += raw_count
        if raw_count <= 0:
            bucket["no_raw_assertion_result_count"] += 1
        if str(row.get("result_status") or row.get("replay_status") or "").strip() == "provider_error":
            bucket["claim_replay_provider_error_count"] += 1
    return result


def _adjudication_result_status_by_archetype(manifest: Mapping[str, Any]) -> Mapping[str, Mapping[str, int]]:
    result: dict[str, dict[str, int]] = {}
    for row in _manifest_rows(manifest):
        archetype_id = str(row.get("archetype_id") or "").strip()
        if not archetype_id:
            continue
        bucket = result.setdefault(
            archetype_id,
            {
                "adjudication_result_count": 0,
                "adjudication_mapping_ready_count": 0,
                "adjudication_target_scope_blocked_count": 0,
                "adjudication_temporal_blocked_count": 0,
                "adjudication_semantic_blocked_count": 0,
            },
        )
        bucket["adjudication_result_count"] += 1
        if _bool(row.get("mapping_ready")):
            bucket["adjudication_mapping_ready_count"] += 1
            continue
        target_scope = str(row.get("target_scope_status") or "").strip()
        temporal = str(row.get("temporal_status") or "").strip()
        semantic = str(row.get("semantic_status") or "").strip()
        if target_scope and target_scope != "DIRECT":
            bucket["adjudication_target_scope_blocked_count"] += 1
        if temporal and temporal != "CURRENT":
            bucket["adjudication_temporal_blocked_count"] += 1
        if semantic and semantic != "PASS":
            bucket["adjudication_semantic_blocked_count"] += 1
    return result


def _primitive_mapping_result_status_by_archetype(manifest: Mapping[str, Any]) -> Mapping[str, Mapping[str, int]]:
    result: dict[str, dict[str, int]] = {}
    for row in _manifest_rows(manifest):
        archetype_id = str(row.get("archetype_id") or "").strip()
        if not archetype_id:
            continue
        bucket = result.setdefault(
            archetype_id,
            {
                "primitive_mapping_result_count": 0,
                "mapping_accepted_count": 0,
                "mapping_rejected_count": 0,
                "eligibility_ready_mapping_count": 0,
            },
        )
        bucket["primitive_mapping_result_count"] += 1
        if str(row.get("mapping_status") or "").strip() == "ACCEPTED":
            bucket["mapping_accepted_count"] += 1
        if str(row.get("mapping_status") or "").strip() == "REJECTED":
            bucket["mapping_rejected_count"] += 1
        if _bool(row.get("eligibility_ready")):
            bucket["eligibility_ready_mapping_count"] += 1
    return result


def _eligibility_result_status_by_archetype(manifest: Mapping[str, Any]) -> Mapping[str, Mapping[str, int]]:
    result: dict[str, dict[str, int]] = {}
    for row in _manifest_rows(manifest):
        archetype_id = str(row.get("archetype_id") or "").strip()
        if not archetype_id:
            continue
        bucket = result.setdefault(
            archetype_id,
            {
                "eligibility_result_count": 0,
                "score_contribution_ready_count": 0,
                "source_anchor_unverified_count": 0,
                "future_leakage_blocked_count": 0,
                "snippet_only_blocked_count": 0,
            },
        )
        bucket["eligibility_result_count"] += 1
        if _bool(row.get("eligibility_ready")):
            bucket["score_contribution_ready_count"] += 1
        if not _bool(row.get("source_anchor_verified")):
            bucket["source_anchor_unverified_count"] += 1
        if _bool(row.get("future_leakage")):
            bucket["future_leakage_blocked_count"] += 1
        if _bool(row.get("snippet_only")):
            bucket["snippet_only_blocked_count"] += 1
    return result


def _stage_court_result_status_by_archetype(manifest: Mapping[str, Any]) -> Mapping[str, Mapping[str, int]]:
    result: dict[str, dict[str, int]] = {}
    for row in _manifest_rows(manifest):
        archetype_id = str(row.get("archetype_id") or "").strip()
        if not archetype_id:
            continue
        bucket = result.setdefault(
            archetype_id,
            {
                "stage_court_result_count": 0,
                "stage_court_ready_count": 0,
            },
        )
        bucket["stage_court_result_count"] += 1
        if _bool(row.get("stage_court_ready")) or str(row.get("result_status") or "").strip() == "stage_court_ready":
            bucket["stage_court_ready_count"] += 1
    return result


def _manifest_rows(manifest: Mapping[str, Any]) -> tuple[Mapping[str, Any], ...]:
    raw_rows = manifest.get("results") or manifest.get("rows") or manifest.get("tasks") or ()
    if not isinstance(raw_rows, Sequence) or isinstance(raw_rows, (str, bytes, bytearray)):
        return ()
    return tuple(row for row in raw_rows if isinstance(row, Mapping))


def _source_status_by_archetype(manifest: Mapping[str, Any]) -> Mapping[str, Mapping[str, int]]:
    if not manifest:
        return {}
    result: dict[str, dict[str, int]] = {}
    for row in manifest.get("seeds") or manifest.get("rows") or manifest.get("fixtures") or ():
        if not isinstance(row, Mapping):
            continue
        archetype_id = str(row.get("archetype_id") or "").strip()
        if not archetype_id:
            continue
        bucket = result.setdefault(
            archetype_id,
            {
                "source_backed_seed_count": 0,
                "snapshot_request_ready_count": 0,
                "pending_source_snapshot_count": 0,
                "evidence_document_fixture_ready_count": 0,
                "production_score_fixture_count": 0,
            },
        )
        bucket["source_backed_seed_count"] += 1
        if _bool(row.get("snapshot_request_ready")):
            bucket["snapshot_request_ready_count"] += 1
        if str(row.get("snapshot_status") or "").strip() == "pending_source_snapshot":
            bucket["pending_source_snapshot_count"] += 1
        fixture_ready = _bool(row.get("evidence_document_fixture_ready")) or _bool(
            row.get("evidence_document_ready")
        ) or str(row.get("fixture_status") or "").strip() in {
            "evidence_document_fixture_ready",
            "replacement_evidence_document_fixture_ready",
        }
        if fixture_ready:
            bucket["evidence_document_fixture_ready_count"] += 1
        if _bool(row.get("production_score_fixture")):
            bucket["production_score_fixture_count"] += 1
    return result


def _claim_task_status_by_archetype(manifest: Mapping[str, Any]) -> Mapping[str, Mapping[str, int]]:
    if not manifest:
        return {}
    result: dict[str, dict[str, int]] = {}
    for row in manifest.get("tasks") or manifest.get("rows") or ():
        if not isinstance(row, Mapping):
            continue
        archetype_id = str(row.get("archetype_id") or "").strip()
        if not archetype_id:
            continue
        bucket = result.setdefault(
            archetype_id,
            {
                "claim_replay_task_count": 0,
                "contract_blind_task_count": 0,
                "production_score_fixture_count": 0,
            },
        )
        bucket["claim_replay_task_count"] += 1
        if _bool(row.get("contract_blind_extraction")):
            bucket["contract_blind_task_count"] += 1
        if _bool(row.get("production_score_fixture")):
            bucket["production_score_fixture_count"] += 1
    return result


def _fixture_status_by_archetype(manifest: Mapping[str, Any]) -> Mapping[str, Mapping[str, int]]:
    if not manifest:
        return {}
    result: dict[str, dict[str, int]] = {}
    for row in manifest.get("rows") or manifest.get("fixtures") or ():
        if not isinstance(row, Mapping):
            continue
        archetype_id = str(row.get("archetype_id") or "").strip()
        if not archetype_id:
            continue
        bucket = result.setdefault(
            archetype_id,
            {
                "replacement_fixture_row_count": 0,
                "evidence_document_fixture_ready_count": 0,
                "claim_replay_ready_count": 0,
                "production_score_fixture_count": 0,
            },
        )
        bucket["replacement_fixture_row_count"] += 1
        if _bool(row.get("evidence_document_fixture_ready")):
            bucket["evidence_document_fixture_ready_count"] += 1
        if _bool(row.get("claim_replay_ready")):
            bucket["claim_replay_ready_count"] += 1
        if _bool(row.get("production_score_fixture")):
            bucket["production_score_fixture_count"] += 1
    return result


def _merge_status_maps(*maps: Mapping[str, Mapping[str, int]]) -> Mapping[str, Mapping[str, int]]:
    result: dict[str, dict[str, int]] = {}
    for mapping in maps:
        for archetype_id, values in mapping.items():
            bucket = result.setdefault(archetype_id, {})
            for key, value in values.items():
                bucket[key] = bucket.get(key, 0) + int(value or 0)
    return result


def _bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    return str(value).strip().lower() in {"true", "1", "yes", "y"}


def _read_json_mapping(path: Path) -> Mapping[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, Mapping):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def _write_json(path: Path, data: Mapping[str, Any]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def _render_gap_plan_markdown(manifest: Mapping[str, Any]) -> str:
    lines = ["# Evidence OS Replay Gap Plan", ""]
    summary = manifest.get("summary")
    if isinstance(summary, Mapping):
        lines.append("## Summary")
        for key in sorted(summary):
            lines.append(f"- {key}: `{summary[key]}`")
        lines.append("")
    lines.append("## Tasks")
    for task in manifest.get("tasks") or ():
        if not isinstance(task, Mapping):
            continue
        lines.append(
            f"- `{task.get('task_id')}` `{task.get('archetype_id')}`: "
            f"`{task.get('coverage_status')}` / `{task.get('source_gap_stage')}` -> `{task.get('next_action')}`"
        )
        seed_count = int(task.get("source_backed_seed_count") or 0)
        if seed_count:
            lines.append(
                f"  - seeds: `{seed_count}`, snapshot_ready: `{task.get('snapshot_request_ready_count')}`, "
                f"fixture_ready: `{task.get('evidence_document_fixture_ready_count')}`, "
                f"claim_replay_tasks: `{task.get('claim_replay_task_count')}`"
            )
    lines.append("")
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    paths = run_replay_gap_plan(
        replay_acceptance_manifest_path=args.replay_acceptance,
        output_directory=args.output_directory,
        output_prefix=args.output_prefix,
        evidence_contracts_v2_path=args.evidence_contracts_v2,
        source_backed_fixture_seed_manifest_path=args.source_backed_fixture_seeds,
        source_evidence_document_fixture_manifest_path=args.source_evidence_document_fixtures,
        replacement_evidence_document_fixture_manifest_path=args.replacement_evidence_document_fixtures,
        claim_replay_task_manifest_path=args.claim_replay_tasks,
        claim_replay_result_manifest_path=args.claim_replay_results,
        adjudication_result_manifest_path=args.adjudication_results,
        primitive_mapping_result_manifest_path=args.primitive_mapping_results,
        eligibility_result_manifest_path=args.eligibility_results,
        stage_court_result_manifest_path=args.stage_court_results,
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "DEFAULT_OUTPUT_DIRECTORY",
    "DEFAULT_REPLAY_ACCEPTANCE",
    "build_arg_parser",
    "build_replay_gap_plan_manifest",
    "main",
    "run_replay_gap_plan",
]
