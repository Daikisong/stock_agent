"""Census v4 leaf auditor.

This auditor is intentionally stricter than v3 on semantics that caused
operator confusion: atomic trace matching, score scale, pending status, and
semantic contract guards.
"""

from __future__ import annotations

import ast
import csv
import hashlib
import json
from datetime import date
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic import ScoreContributionV2
from e2r.calibration.taxonomy import large_sector_for_archetype
from e2r.scoring import CANONICAL_SCORE_COMPONENTS, DeterministicScorer, ScoringPayload


REQUIRED_JSONL = (
    "universe.jsonl",
    "source_timelines.jsonl",
    "last_effective_thesis_states.jsonl",
    "baseline_scan_results.jsonl",
    "census_events.jsonl",
    "depth_decisions.jsonl",
    "atomic_stage_decisions.jsonl",
    "source_tasks.jsonl",
    "source_task_executions.jsonl",
    "evidence_documents.jsonl",
    "evidence_anchors.jsonl",
    "raw_assertions.jsonl",
    "adjudicated_claims.jsonl",
    "accepted_claims.jsonl",
    "evidence_claims.jsonl",
    "primitive_mappings.jsonl",
    "primitive_states.jsonl",
    "score_contributions.jsonl",
    "stagecourt_traces.jsonl",
    "claim_to_stage_trace.jsonl",
    "brain_to_claim_trace.jsonl",
    "brain_claim_mapping_trace.jsonl",
    "planner_runs.jsonl",
    "llm_prompts.jsonl",
    "llm_responses.jsonl",
    "web_search_tasks.jsonl",
    "web_search_results.jsonl",
    "web_fetched_documents.jsonl",
    "web_rejected_documents.jsonl",
    "claim_extractor_runs.jsonl",
    "census_stage_status.jsonl",
    "census_stage_map.jsonl",
    "sample_leaf_bundle.jsonl",
    "full_thesis_smoke_tasks.jsonl",
    "full_thesis_refresh_queue.jsonl",
    "full_thesis_seed_materialization_trace.jsonl",
)

REQUIRED_JSON = (
    "run_metadata.json",
    "census_stage_summary.json",
    "brain_web_attempt_audit.json",
    "brain_stage_promotion_audit.json",
    "brain_web_readiness_gate_audit.json",
    "research_brain_v4_bridge_audit.json",
    "source_task_satisfaction_audit.json",
    "primitive_state_chain_audit.json",
    "non_representative_claim_audit.json",
    "official_event_counter_audit.json",
    "samsung_hynix_full_thesis_smoke.json",
    "full_thesis_refresh_queue_audit.json",
    "full_thesis_seed_materialization_audit.json",
    "c06_source_backed_semantic_replay.json",
    "c08_source_backed_semantic_replay.json",
    "c15_source_backed_semantic_replay.json",
    "c17_source_backed_semantic_replay.json",
    "c24_source_backed_semantic_replay.json",
    "c28_source_backed_semantic_replay.json",
    "brain_planner_audit.json",
    "web_naver_acquisition_audit.json",
    "llm_claim_extraction_audit.json",
    "brain_to_claim_trace_audit.json",
    "known_bad_regression_report.json",
    "self_repair_log.json",
    "test_result_evidence_audit.json",
    "goal_requirement_matrix_audit.json",
    "goal_completion_audit.json",
)

CANONICAL_STAGES = {"0", "1", "2", "3-Green", "3-Yellow", "3-Red", "4A", "4B", "4C", "5"}


def audit_census_v4_leaf_artifacts(output_root: str | Path) -> dict[str, Any]:
    root = Path(output_root)
    repo_root = _repo_root_for(root)
    rows = {name: _read_jsonl(root / name) for name in REQUIRED_JSONL if (root / name).exists()}
    missing_files = [name for name in REQUIRED_JSONL if not (root / name).exists()]
    missing_files.extend(name for name in REQUIRED_JSON if not (root / name).exists())
    universe = rows.get("universe.jsonl", [])
    eligible = [row for row in universe if row.get("eligible_for_census", True)]
    stage_rows = rows.get("census_stage_status.jsonl", [])
    atomic = rows.get("atomic_stage_decisions.jsonl", [])
    accepted = rows.get("accepted_claims.jsonl", [])
    evidence_documents = rows.get("evidence_documents.jsonl", [])
    evidence_claims = rows.get("evidence_claims.jsonl", [])
    primitive_mappings = rows.get("primitive_mappings.jsonl", [])
    primitive_states = rows.get("primitive_states.jsonl", [])
    contributions = rows.get("score_contributions.jsonl", [])
    stagecourt = rows.get("stagecourt_traces.jsonl", [])
    events = rows.get("census_events.jsonl", [])
    timelines = rows.get("source_timelines.jsonl", [])
    thesis = rows.get("last_effective_thesis_states.jsonl", [])
    planner = rows.get("planner_runs.jsonl", [])
    web_tasks = rows.get("web_search_tasks.jsonl", [])
    web_results = rows.get("web_search_results.jsonl", [])
    web_fetched = rows.get("web_fetched_documents.jsonl", [])
    web_rejected = rows.get("web_rejected_documents.jsonl", [])
    extractor = rows.get("claim_extractor_runs.jsonl", [])
    sample_bundle = rows.get("sample_leaf_bundle.jsonl", [])
    full_thesis_refresh_queue = rows.get("full_thesis_refresh_queue.jsonl", [])
    metadata = _read_json(root / "run_metadata.json")
    brain_web_attempt = _read_json(root / "brain_web_attempt_audit.json")
    brain_stage_promotion = _read_json(root / "brain_stage_promotion_audit.json")
    brain_web_readiness_gate = _read_json(root / "brain_web_readiness_gate_audit.json")
    research_brain_bridge = _read_json(root / "research_brain_v4_bridge_audit.json")
    non_representative_claim_audit = _read_json(root / "non_representative_claim_audit.json")
    planner_real_provider_attempt_count = sum(1 for row in planner if row.get("provider_mode") == "real" and row.get("real_provider_exercised") is True)
    planner_real_provider_success_count = sum(1 for row in planner if row.get("provider_mode") == "real" and row.get("real_provider_success") is True)

    eligible_symbols = {str(row.get("symbol") or "").zfill(6) for row in eligible}
    stage_symbols = [str(row.get("symbol") or "").zfill(6) for row in stage_rows]
    atomic_by_id = {str(row.get("atomic_stage_decision_id") or ""): row for row in atomic}
    accepted_ids = {str(row.get("claim_id") or "") for row in accepted}
    evidence_claim_ids = {str(row.get("claim_id") or row.get("evidence_claim_id") or "") for row in evidence_claims}
    contribution_ids = {str(row.get("score_contribution_id") or row.get("contribution_id") or "") for row in contributions}
    contributions_by_id = {
        str(row.get("score_contribution_id") or row.get("contribution_id") or ""): row
        for row in contributions
        if str(row.get("score_contribution_id") or row.get("contribution_id") or "")
    }
    primitive_mapping_ids = {str(row.get("mapping_id") or "") for row in primitive_mappings}
    primitive_state_ids = {str(row.get("primitive_state_id") or "") for row in primitive_states}
    primitive_ids_by_claim = _primitive_ids_by_claim(primitive_states)
    stagecourt_ids = {str(row.get("stagecourt_trace_id") or row.get("trace_id") or "") for row in stagecourt}
    assessment_event_ids = {
        str(row.get("event_id") or "")
        for row in events
        if row.get("event_category") == "CensusAssessmentEvent" or row.get("event_type") == "CensusAssessmentEvent"
    }
    candidate_event_ids_by_symbol: dict[str, set[str]] = {}
    for row in events:
        event_id = str(row.get("event_id") or "")
        symbol = str(row.get("symbol") or "").zfill(6)
        if not event_id or not symbol or event_id in assessment_event_ids:
            continue
        candidate_event_ids_by_symbol.setdefault(symbol, set()).add(event_id)

    nonzero_or_final = [
        row
        for row in stage_rows
        if row.get("event_evidence_score") is not None
        or row.get("full_e2r_verified_score") is not None
        or row.get("verified_score") is not None
        or row.get("score_valid_status") in {"FINAL", "FINAL_WITH_NONMATERIAL_GAPS"}
    ]
    event_board_non_stage0_count = sum(
        1 for row in stage_rows if row.get("stage_scope") == "CENSUS_EVENT_BOARD" and row.get("base_stage") != "Stage0"
    )
    full_thesis_refresh_queue_candidate_count = len(full_thesis_refresh_queue)
    critical = {
        "missing_leaf_artifact_count": len(missing_files),
        "missing_symbol_count": len(eligible_symbols - set(stage_symbols)),
        "duplicate_symbol_count": _duplicate_count(stage_symbols),
        "stage_status_count_mismatch": int(len(stage_rows) != len(eligible_symbols)),
        "source_timeline_missing_count": len(eligible_symbols - {str(row.get("symbol") or "").zfill(6) for row in timelines}),
        "last_effective_thesis_missing_count": len(eligible_symbols - {str(row.get("symbol") or "").zfill(6) for row in thesis}),
        "stage_trace_stage_mismatch_count": _stage_trace_mismatch(stage_rows, atomic_by_id, "base_stage"),
        "stage_trace_canonical_stage_mismatch_count": _stage_trace_mismatch(stage_rows, atomic_by_id, "canonical_stage"),
        "stage_trace_scope_mismatch_count": _stage_trace_mismatch(stage_rows, atomic_by_id, "stage_scope"),
        "stage_trace_score_scope_mismatch_count": _stage_trace_mismatch(stage_rows, atomic_by_id, "score_scope"),
        "stage_trace_score_interval_mismatch_count": _stage_trace_score_mismatch(stage_rows, atomic_by_id),
        "stage_trace_score_status_mismatch_count": _stage_trace_mismatch(stage_rows, atomic_by_id, "score_valid_status"),
        "stage_trace_claim_set_mismatch_count": _stage_trace_set_mismatch(stage_rows, atomic_by_id, "accepted_claim_ids"),
        "stage_trace_contribution_set_mismatch_count": _stage_trace_set_mismatch(stage_rows, atomic_by_id, "score_contribution_ids"),
        "stagecourt_score_recompute_mismatch_count": _stagecourt_score_recompute_mismatch_count(
            stagecourt, contributions_by_id
        ),
        "stagecourt_score_contribution_ref_missing_count": _stagecourt_score_contribution_ref_missing_count(
            stagecourt, contributions_by_id
        ),
        "scored_row_missing_claim_ids": sum(1 for row in nonzero_or_final if row.get("score_scale") != "NO_SCORE" and not row.get("accepted_claim_ids")),
        "scored_row_missing_score_contribution_ids": sum(1 for row in nonzero_or_final if row.get("score_scale") != "NO_SCORE" and not row.get("score_contribution_ids")),
        "scored_row_missing_stagecourt_trace": sum(1 for row in nonzero_or_final if row.get("score_scale") != "NO_SCORE" and not row.get("stagecourt_trace_id")),
        "claim_id_not_found_count": sum(1 for row in stage_rows for claim_id in row.get("accepted_claim_ids") or [] if str(claim_id) not in accepted_ids),
        "accepted_claim_without_evidence_claim_payload_count": sum(1 for claim_id in accepted_ids if claim_id and claim_id not in evidence_claim_ids),
        "evidence_claim_payload_without_accepted_claim_count": sum(1 for claim_id in evidence_claim_ids if claim_id and claim_id not in accepted_ids),
        "evidence_claim_missing_verifiable_anchor_count": sum(1 for row in evidence_claims if not row.get("document_id") or not row.get("anchor_id")),
        "evidence_claim_marked_brain_web_in_disabled_run_count": sum(1 for row in evidence_claims if row.get("brain_web_claim") is True and not _claims_brain(metadata)),
        "score_contribution_id_not_found_count": sum(1 for row in stage_rows for item in row.get("score_contribution_ids") or [] if str(item) not in contribution_ids),
        "primitive_state_missing_id_count": sum(1 for row in primitive_states if not row.get("primitive_state_id")),
        "primitive_mapping_missing_id_count": sum(1 for row in primitive_mappings if not row.get("mapping_id")),
        "score_contribution_mapping_id_not_found_count": sum(
            1 for row in contributions for item in row.get("mapping_ids") or [] if str(item) not in primitive_mapping_ids
        ),
        "primitive_mapping_claim_id_not_found_count": sum(
            1 for row in primitive_mappings for item in row.get("accepted_claim_ids") or [] if str(item) not in accepted_ids
        ),
        "primitive_mapping_state_id_not_found_count": sum(
            1 for row in primitive_mappings for item in row.get("primitive_state_ids") or [] if str(item) not in primitive_state_ids
        ),
        "primitive_mapping_contribution_id_not_found_count": sum(
            1 for row in primitive_mappings for item in row.get("score_contribution_ids") or [] if str(item) not in contribution_ids
        ),
        "primitive_state_id_not_found_count": sum(1 for row in stage_rows for item in row.get("primitive_state_ids") or [] if str(item) not in primitive_state_ids),
        "scored_row_missing_primitive_state_ids": sum(1 for row in nonzero_or_final if row.get("score_scale") != "NO_SCORE" and not row.get("primitive_state_ids")),
        "scored_claim_without_primitive_state_count": sum(
            1
            for row in nonzero_or_final
            if row.get("score_scale") != "NO_SCORE"
            for claim_id in row.get("accepted_claim_ids") or []
            if not primitive_ids_by_claim.get(str(claim_id))
        ),
        "stagecourt_trace_id_not_found_count": sum(1 for row in stage_rows if row.get("stagecourt_trace_id") and str(row.get("stagecourt_trace_id")) not in stagecourt_ids),
        "score_scale_missing_count": sum(1 for row in stage_rows if not row.get("score_scale")),
        "score_source_missing_count": sum(1 for row in stage_rows if not row.get("score_source")),
        "stage_scope_missing_count": sum(1 for row in stage_rows if not row.get("stage_scope")),
        "score_scope_missing_count": sum(1 for row in stage_rows if not row.get("score_scope")),
        "stage_scope_invalid_count": sum(
            1
            for row in stage_rows
            if row.get("stage_scope") not in {"CENSUS_EVENT_BOARD", "BRAIN_WEB_PARTIAL", "BRAIN_OFFICIAL_PARTIAL", "FULL_THESIS"}
        ),
        "operator_scope_alias_missing_count": sum(1 for row in stage_rows if _operator_scope_alias_missing(row)),
        "event_board_operator_alias_unscoped_count": sum(
            1
            for row in stage_rows
            if row.get("stage_scope") == "CENSUS_EVENT_BOARD" and not _operator_aliases_have_prefix(row, "EVENT_BOARD")
        ),
        "brain_web_operator_alias_unscoped_count": sum(
            1
            for row in stage_rows
            if row.get("stage_scope") == "BRAIN_WEB_PARTIAL" and not _operator_aliases_have_prefix(row, "BRAIN_WEB_PARTIAL")
        ),
        "brain_official_operator_alias_unscoped_count": sum(
            1
            for row in stage_rows
            if row.get("stage_scope") == "BRAIN_OFFICIAL_PARTIAL" and not _operator_aliases_have_prefix(row, "BRAIN_OFFICIAL_PARTIAL")
        ),
        "full_thesis_operator_alias_unscoped_count": sum(
            1
            for row in stage_rows
            if row.get("stage_scope") == "FULL_THESIS" and not _operator_aliases_have_prefix(row, "FULL_THESIS")
        ),
        "non_full_thesis_operator_use_overclaim_count": sum(
            1 for row in stage_rows if row.get("stage_scope") != "FULL_THESIS" and row.get("operator_stage_use") != "NOT_FULL_THESIS_STAGE"
        ),
        "non_full_e2r_operator_score_overclaim_count": sum(
            1 for row in stage_rows if row.get("score_scale") != "FULL_E2R_100" and row.get("operator_score_use") != "NOT_FULL_E2R_SCORE"
        ),
        "full_thesis_stage_without_full_thesis_scope_count": sum(
            1
            for row in stage_rows
            if row.get("full_thesis_stage") not in {None, "", "FULL_THESIS_NOT_RUN"} and row.get("stage_scope") != "FULL_THESIS"
        ),
        "full_thesis_scope_without_full_e2r_score_count": sum(
            1 for row in stage_rows if row.get("stage_scope") == "FULL_THESIS" and row.get("score_scale") != "FULL_E2R_100"
        ),
        "event_board_scope_with_full_e2r_verified_score_count": sum(
            1 for row in stage_rows if row.get("stage_scope") == "CENSUS_EVENT_BOARD" and row.get("full_e2r_verified_score") is not None
        ),
        "canonical_stage_invalid_count": sum(1 for row in stage_rows if row.get("canonical_stage") not in CANONICAL_STAGES),
        "canonical_stage_display_label_count": sum(
            1 for row in stage_rows if row.get("canonical_stage") in {"Stage0", "Stage1", "Stage2-Watch", "Stage2-Actionable", "Red", "Reject"}
        ),
        "verified_score_not_full_e2r_count": sum(1 for row in stage_rows if row.get("verified_score") is not None and row.get("score_scale") != "FULL_E2R_100"),
        "raw_contribution_fallback_as_verified_score_count": sum(1 for row in stage_rows if row.get("score_source") == "RAW_CONTRIBUTION_FALLBACK" and row.get("verified_score") is not None),
        "pending_material_marked_complete_count": sum(1 for row in stage_rows if row.get("stage_decision_status") == "PENDING_MATERIAL_GAPS" and row.get("investigation_status") == "COMPLETE"),
        "stage2_without_stage_signal_count": sum(1 for row in stage_rows if row.get("base_stage") == "Stage2-Watch" and not row.get("stage_signal")),
        "red_without_risk_signal_or_trace_count": sum(1 for row in stage_rows if row.get("base_stage") in {"Red", "Reject"} and row.get("risk_stage_signal") in {None, "", "NONE"} and not row.get("stagecourt_trace_id")),
        "source_pending_marked_red_count": sum(1 for row in stage_rows if row.get("census_status") in {"PENDING_SOURCE", "PENDING_PROVIDER"} and row.get("base_stage") in {"Red", "Reject"}),
        "missing_census_assessment_event_id_count": sum(1 for row in stage_rows if not row.get("census_assessment_event_id")),
        "assessment_event_score_evidence_allowed_count": sum(1 for row in stage_rows if row.get("census_assessment_event_score_evidence_allowed") is not False),
        "candidate_event_ids_contain_assessment_event_count": sum(
            1
            for row in stage_rows
            if row.get("census_assessment_event_id") and row.get("census_assessment_event_id") in set(row.get("candidate_event_ids") or [])
        ),
        "assessment_only_nonzero_score_count": sum(1 for row in stage_rows if int(row.get("candidate_event_count") or 0) == 0 and row.get("score_scale") != "NO_SCORE"),
        "assessment_event_used_as_score_evidence_count": sum(
            1
            for row in stage_rows
            if row.get("census_assessment_event_score_evidence_allowed") is not False
            or (
                row.get("census_assessment_event_id")
                and row.get("census_assessment_event_id") in set(row.get("candidate_event_ids") or [])
            )
            or (int(row.get("candidate_event_count") or 0) == 0 and row.get("score_scale") != "NO_SCORE")
        ),
        "event_without_accepted_claim_nonzero_score_count": sum(
            1 for row in stage_rows if row.get("score_scale") != "NO_SCORE" and not row.get("accepted_claim_ids")
        ),
        "score_contribution_without_accepted_claim_support_count": sum(
            1 for row in contributions if not (row.get("accepted_claim_ids") or row.get("support_claim_ids"))
        ),
        "no_current_catalyst_with_candidate_event_count": sum(1 for row in stage_rows if row.get("stage_signal") == "NO_CURRENT_CATALYST" and int(row.get("candidate_event_count") or 0) > 0),
        "score_eligible_candidate_without_accepted_claim_count": sum(
            1
            for row in stage_rows
            if int(row.get("score_eligible_candidate_event_count") or 0) > 0
            and int(row.get("accepted_claim_count") or 0) == 0
            and not row.get("blocked_claim_ids")
        ),
        "atomic_candidate_event_is_assessment_count": sum(
            1
            for row in atomic
            if row.get("candidate_event_id") and str(row.get("candidate_event_id")) in assessment_event_ids
        ),
        "atomic_candidate_event_not_in_symbol_candidate_events_count": sum(
            1
            for row in atomic
            if row.get("candidate_event_id")
            and str(row.get("candidate_event_id")) not in candidate_event_ids_by_symbol.get(str(row.get("symbol") or "").zfill(6), set())
        ),
        "semantic_guard_blocked_score_count": sum(1 for row in stage_rows if row.get("semantic_guard_status") == "BLOCKED" and row.get("score_scale") != "NO_SCORE"),
        "contract_quality_semantic_guard_missing_count": sum(1 for row in atomic if row.get("semantic_guard_class") in {None, "", "no_score_contribution"} and row.get("score_contribution_ids")),
        "official_claim_but_recent_official_event_zero_count": sum(1 for row in stage_rows if int(row.get("accepted_official_claim_count") or 0) > 0 and int(row.get("official_source_task_count") or 0) == 0 and int(row.get("official_evidence_document_count") or 0) == 0),
        "provider_failed_final_score_count": sum(1 for row in stage_rows if row.get("census_status") == "PENDING_PROVIDER" and row.get("score_scale") != "NO_SCORE"),
        "source_proxy_to_score_count": sum(1 for row in contributions if row.get("source_proxy_only")),
        "evidence_url_pending_to_score_count": sum(1 for row in contributions if row.get("evidence_url_pending")),
        "price_path_only_to_score_count": sum(1 for row in contributions if row.get("price_path_only")),
        "market_anomaly_to_score_count": sum(1 for row in stage_rows if row.get("market_anomaly_count") and row.get("score_scale") != "NO_SCORE"),
        "news_snippet_to_score_count": sum(1 for row in contributions if row.get("source_type") == "snippet"),
        "llm_claimed_but_zero_calls_count": int(_claims_brain(metadata) and len(planner) == 0),
        "llm_claimed_but_zero_real_success_count": int(_claims_brain(metadata) and planner_real_provider_success_count == 0),
        "brain_enabled_without_attempt_audit_count": int(_claims_brain(metadata) and not brain_web_attempt),
        "brain_attempt_overclaims_success_count": int(
            brain_web_attempt.get("verdict") in {"ATTEMPTED_WITH_SOURCE_TASKS", "BRAIN_WEB_EVIDENCE_PASS"}
            and int(brain_web_attempt.get("real_provider_success_count") or 0) <= 0
        ),
        "brain_attempt_cutover_without_promotion_count": int(
            brain_web_attempt.get("cutover_export_ready") is True
            and (
                brain_stage_promotion.get("verdict") != "PROMOTION_APPLIED"
                or int(brain_stage_promotion.get("brain_promoted_stage_row_count") or 0) <= 0
            )
        ),
        "brain_stage_promotion_unsafe_promoted_count": int(brain_stage_promotion.get("unsafe_promoted_stage_row_count") or 0),
        "brain_stage_promotion_trace_promoted_reference_count": int(
            brain_stage_promotion.get("brain_trace_promoted_reference_error_count") or 0
        ),
        "brain_stage_trace_not_promoted_marker_missing_count": int(brain_stage_promotion.get("brain_stage_trace_not_promoted_marker_missing_count") or 0),
        "brain_stage_promotion_overclaim_count": int(
            brain_stage_promotion.get("verdict") in {"PROMOTION_APPLIED", "ELIGIBLE_NOT_PROMOTED"}
            and int(brain_stage_promotion.get("brain_stage_trace_count") or 0) <= 0
        ),
        "brain_web_readiness_gate_missing_count": int(_claims_brain(metadata) and not brain_web_readiness_gate),
        "brain_web_readiness_gate_overclaim_count": int(
            brain_web_readiness_gate.get("brain_web_evidence_pass_allowed") is True
            and (
                brain_web_readiness_gate.get("verdict") != "READY_FOR_BRAIN_WEB_EVIDENCE_PASS"
                or int(brain_web_readiness_gate.get("brain_promoted_stage_row_count") or 0) <= 0
            )
        ),
        "web_claimed_but_zero_search_count": int(_claims_web(metadata) and len(web_tasks) == 0 and len(web_results) == 0 and len(web_fetched) == 0),
        "llm_claim_extractor_claimed_but_zero_count": int(
            _claims_brain(metadata)
            and len(extractor) == 0
            and any(_is_unstructured_brain_document(row) for row in evidence_documents)
        ),
        "research_brain_bridge_cutover_overclaim_count": int(
            research_brain_bridge.get("usable_for_census_cutover") is True
            and (
                int(research_brain_bridge.get("snapshot_url_count") or 0) > 0
                or research_brain_bridge.get("production_cutover_ready") is not True
            )
        ),
        "legacy_runner_production_reachable_count": _legacy_runner_production_reachable_count(repo_root),
        "legacy_v3_runner_production_reachable_count": _legacy_v3_runner_production_reachable_count(repo_root),
        "empty_claims_stage_builder_production_count": _empty_claims_stage_builder_production_count(repo_root),
        "old_cli_can_claim_pass_count": _old_cli_can_claim_pass_count(repo_root),
        "official_cli_not_v4_runner_count": _official_cli_not_v4_runner_count(repo_root),
        "sample_bundle_missing_scored_row_count": _sample_bundle_missing_scored_row_count(stage_rows, sample_bundle),
        "non_representative_claim_audit_missing_count": int(not non_representative_claim_audit),
        "non_representative_claim_audit_failed_count": int(bool(non_representative_claim_audit) and non_representative_claim_audit.get("verdict") != "PASS"),
        "non_representative_claim_score_leak_count": int(
            ((non_representative_claim_audit.get("critical_counts") or {}).get("non_representative_claim_score_leak_count") or 0)
        ),
        "full_thesis_refresh_queue_missing_event_board_count": max(
            0, event_board_non_stage0_count - full_thesis_refresh_queue_candidate_count
        ),
    }
    base_stage_distribution = _count_by(stage_rows, "base_stage")
    full_thesis_stage_row_count = sum(1 for row in stage_rows if row.get("stage_scope") == "FULL_THESIS")
    metrics = {
        "eligible_symbol_count": len(eligible_symbols),
        "stage_status_count": len(stage_rows),
        "atomic_stage_decision_count": len(atomic),
        "representative_atomic_decision_count": sum(1 for row in atomic if row.get("is_representative")),
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
        "score_source_distribution": _count_by(stage_rows, "score_source"),
        "census_status_distribution": _count_by(stage_rows, "census_status"),
        "candidate_event_scope_distribution": _count_by(stage_rows, "candidate_event_scope"),
        "candidate_event_count": sum(int(row.get("candidate_event_count") or 0) for row in stage_rows),
        "score_eligible_candidate_event_count": sum(int(row.get("score_eligible_candidate_event_count") or 0) for row in stage_rows),
        "event_evidence_score_present_count": sum(1 for row in stage_rows if row.get("event_evidence_score") is not None),
        "full_e2r_verified_score_present_count": sum(1 for row in stage_rows if row.get("full_e2r_verified_score") is not None),
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
        "planner_run_count": len(planner),
        "planner_real_provider_attempt_count": planner_real_provider_attempt_count,
        "planner_real_provider_success_count": planner_real_provider_success_count,
        "brain_web_attempt_verdict": brain_web_attempt.get("verdict"),
        "brain_web_attempt_blocker_count": len(brain_web_attempt.get("blockers") or []),
        "brain_web_attempt_source_task_execution_count": int(brain_web_attempt.get("source_task_execution_count") or 0),
        "brain_web_attempt_accepted_claim_count": int(brain_web_attempt.get("accepted_claim_count") or 0),
        "brain_stage_promotion_verdict": brain_stage_promotion.get("verdict"),
        "brain_stage_promotion_mode": brain_stage_promotion.get("brain_stage_promotion_mode"),
        "brain_stage_trace_count": int(brain_stage_promotion.get("brain_stage_trace_count") or 0),
        "brain_stage_promoted_row_count": int(brain_stage_promotion.get("brain_promoted_stage_row_count") or 0),
        "brain_stage_promotion_unsafe_promoted_count": int(brain_stage_promotion.get("unsafe_promoted_stage_row_count") or 0),
        "brain_stage_promotion_snapshot_document_count": int(brain_stage_promotion.get("brain_snapshot_document_count") or 0),
        "brain_stage_promotion_blocker_count": len(brain_stage_promotion.get("blockers") or []),
        "brain_web_readiness_gate_verdict": brain_web_readiness_gate.get("verdict"),
        "brain_web_readiness_gate_pass_allowed": bool(brain_web_readiness_gate.get("brain_web_evidence_pass_allowed")),
        "brain_web_readiness_gate_blocker_count": len(brain_web_readiness_gate.get("blockers") or []),
        "brain_web_readiness_gate_minimum_applies": bool(brain_web_readiness_gate.get("minimum_gate_applies")),
        "web_search_task_count": len(web_tasks),
        "web_search_result_count": len(web_results),
        "web_fetched_document_count": len(web_fetched),
        "web_rejected_document_count": len(web_rejected),
        "claim_extractor_run_count": len(extractor),
        "evidence_claim_payload_count": len(evidence_claims),
        "non_representative_claim_count": int(non_representative_claim_audit.get("non_representative_claim_count") or 0),
        "non_representative_claim_warning_count": int(non_representative_claim_audit.get("warning_count") or 0),
        "non_representative_claim_critical_count": int(non_representative_claim_audit.get("critical_count") or 0),
        "research_brain_bridge_verdict": research_brain_bridge.get("verdict"),
        "research_brain_bridge_usable_for_census_cutover": bool(research_brain_bridge.get("usable_for_census_cutover")),
        "research_brain_bridge_snapshot_url_count": int(research_brain_bridge.get("snapshot_url_count") or 0),
        "sample_leaf_bundle_count": len(sample_bundle),
        "static_source_audit_repo_root": str(repo_root),
        "critical_count": sum(int(value) for value in critical.values()),
        "stagecourt_score_recompute_mismatch_samples": _stagecourt_score_recompute_mismatch_samples(
            stagecourt, contributions_by_id
        ),
    }
    verdict = "PASS" if metrics["critical_count"] == 0 else "FAIL"
    return {
        "schema_version": "e2r_census_v4_leaf_artifact_audit_v1",
        "output_root": str(root),
        "verdict": verdict,
        "critical_count": metrics["critical_count"],
        "critical_counts": critical,
        "metrics": metrics,
        "missing_leaf_artifacts": missing_files,
    }


def build_artifact_manifest(output_root: str | Path) -> dict[str, Any]:
    root = Path(output_root)
    artifacts: list[dict[str, Any]] = []
    for path in sorted(item for item in root.iterdir() if item.is_file() and item.name != "artifact_manifest.json"):
        content = path.read_bytes()
        row_count = None
        if path.suffix == ".jsonl":
            row_count = sum(1 for line in content.splitlines() if line.strip())
        elif path.suffix == ".csv":
            text = content.decode("utf-8-sig")
            rows = list(csv.reader(text.splitlines()))
            row_count = max(0, len(rows) - 1) if rows else 0
        artifacts.append(
            {
                "path": str(path),
                "name": path.name,
                "byte_size": len(content),
                "sha256": hashlib.sha256(content).hexdigest(),
                "row_count": row_count,
            }
        )
    return {"schema_version": "e2r_census_v4_artifact_manifest_v1", "output_root": str(root), "artifacts": artifacts}


def _stage_trace_mismatch(stage_rows: Sequence[Mapping[str, Any]], atomic_by_id: Mapping[str, Mapping[str, Any]], key: str) -> int:
    count = 0
    for row in stage_rows:
        decision = atomic_by_id.get(str(row.get("atomic_stage_decision_id") or ""))
        if not decision:
            continue
        if row.get(key) != decision.get(key):
            count += 1
    return count


def _stage_trace_score_mismatch(stage_rows: Sequence[Mapping[str, Any]], atomic_by_id: Mapping[str, Mapping[str, Any]]) -> int:
    count = 0
    for row in stage_rows:
        decision = atomic_by_id.get(str(row.get("atomic_stage_decision_id") or ""))
        if not decision:
            continue
        if row.get("score_interval_lower") != decision.get("score_interval_lower") or row.get("score_interval_upper") != decision.get("score_interval_upper"):
            count += 1
    return count


def _stage_trace_set_mismatch(stage_rows: Sequence[Mapping[str, Any]], atomic_by_id: Mapping[str, Mapping[str, Any]], key: str) -> int:
    count = 0
    for row in stage_rows:
        decision = atomic_by_id.get(str(row.get("atomic_stage_decision_id") or ""))
        if not decision:
            continue
        if set(str(item) for item in (row.get(key) or ())) != set(str(item) for item in (decision.get(key) or ())):
            count += 1
    return count


def _stagecourt_score_recompute_mismatch_count(
    stagecourt_rows: Sequence[Mapping[str, Any]],
    contributions_by_id: Mapping[str, Mapping[str, Any]],
) -> int:
    return len(_stagecourt_score_recompute_mismatches(stagecourt_rows, contributions_by_id))


def _stagecourt_score_recompute_mismatch_samples(
    stagecourt_rows: Sequence[Mapping[str, Any]],
    contributions_by_id: Mapping[str, Mapping[str, Any]],
    *,
    limit: int = 20,
) -> list[dict[str, Any]]:
    return _stagecourt_score_recompute_mismatches(stagecourt_rows, contributions_by_id)[:limit]


def _stagecourt_score_recompute_mismatches(
    stagecourt_rows: Sequence[Mapping[str, Any]],
    contributions_by_id: Mapping[str, Mapping[str, Any]],
) -> list[dict[str, Any]]:
    mismatches: list[dict[str, Any]] = []
    for row in stagecourt_rows:
        contribution_ids = _unique_strings(row.get("score_contribution_ids") or ())
        if not contribution_ids:
            continue
        archetype_id = _trace_archetype_id(row)
        if not archetype_id:
            continue
        if any(contribution_id not in contributions_by_id for contribution_id in contribution_ids):
            continue
        score_interval = row.get("score_interval") or {}
        if not isinstance(score_interval, Mapping):
            continue
        lower = _float_or_none(score_interval.get("lower"))
        if lower is None:
            continue
        recomputed = _recompute_stagecourt_verified_score(row, contribution_ids, contributions_by_id, archetype_id)
        if recomputed is None:
            continue
        if abs(lower - recomputed["verified_score"]) <= 0.0001:
            continue
        mismatches.append(
            {
                "stagecourt_trace_id": row.get("stagecourt_trace_id") or row.get("trace_id"),
                "symbol": row.get("symbol"),
                "candidate_event_id": row.get("candidate_event_id"),
                "primary_archetype": archetype_id,
                "score_interval_lower": lower,
                "recomputed_verified_score": recomputed["verified_score"],
                "referenced_raw_point_sum": recomputed["raw_point_sum"],
                "weighted_component_sum": recomputed["weighted_component_sum"],
                "scoring_version": recomputed["scoring_version"],
                "score_contribution_ids": contribution_ids,
            }
        )
    return mismatches


def _stagecourt_score_contribution_ref_missing_count(
    stagecourt_rows: Sequence[Mapping[str, Any]],
    contributions_by_id: Mapping[str, Mapping[str, Any]],
) -> int:
    count = 0
    for row in stagecourt_rows:
        contribution_ids = _unique_strings(row.get("score_contribution_ids") or ())
        if not contribution_ids:
            continue
        if any(contribution_id not in contributions_by_id for contribution_id in contribution_ids):
            count += 1
    return count


def _trace_archetype_id(row: Mapping[str, Any]) -> str:
    return str(row.get("primary_archetype") or row.get("canonical_archetype_id") or "").strip()


def _recompute_stagecourt_verified_score(
    row: Mapping[str, Any],
    contribution_ids: Sequence[str],
    contributions_by_id: Mapping[str, Mapping[str, Any]],
    archetype_id: str,
) -> dict[str, Any] | None:
    contribution_rows = [contributions_by_id[contribution_id] for contribution_id in contribution_ids]
    contributions = _score_contribution_v2_rows(contribution_rows)
    if not contributions:
        return None
    as_of = _trace_as_of_date(row)
    if as_of is None:
        return None
    large_sector_id = large_sector_for_archetype(archetype_id)
    if not large_sector_id:
        return None
    payload = ScoringPayload(
        symbol=str(row.get("symbol") or "UNKNOWN"),
        as_of_date=as_of,
        components={component.key: 0.0 for component in CANONICAL_SCORE_COMPONENTS},
        diagnostic_scores={
            "require_v2_score_contributions": 100.0,
            "agentic_evidence_required_for_scoring": 100.0,
            "claim_backed_claim_count_capped": min(float(len(_support_claim_ids(contribution_rows))), 100.0),
        },
        evidence_ids=tuple(_support_claim_ids(contribution_rows)),
        score_contributions_v2=tuple(contributions),
        large_sector_id=large_sector_id,
        canonical_archetype_id=archetype_id,
        scoring_version="census-v4-audit-recompute",
    )
    snapshot = DeterministicScorer().score(payload)
    weighted_component_sum = _float_or_none(snapshot.diagnostic_scores.get("archetype_weighted_total_before_calibration"))
    if weighted_component_sum is None or weighted_component_sum <= 0:
        weighted_component_sum = round(
            sum(
                getattr(
                    snapshot,
                    {
                        "eps_fcf_explosion": "eps_fcf_explosion_score",
                        "earnings_visibility": "earnings_visibility_score",
                        "bottleneck_pricing": "bottleneck_pricing_score",
                        "market_mispricing": "market_mispricing_score",
                        "valuation_rerating": "valuation_rerating_score",
                        "capital_allocation": "capital_allocation_score",
                        "information_confidence": "information_confidence_score",
                    }[component.key],
                )
                for component in CANONICAL_SCORE_COMPONENTS
            ),
            4,
        )
    return {
        "verified_score": float(snapshot.total_score),
        "raw_point_sum": round(sum(_float_or_none(row.get("raw_points")) or 0.0 for row in contribution_rows), 4),
        "weighted_component_sum": weighted_component_sum,
        "scoring_version": snapshot.scoring_version,
    }


def _score_contribution_v2_rows(rows: Sequence[Mapping[str, Any]]) -> list[ScoreContributionV2]:
    contributions: list[ScoreContributionV2] = []
    for row in rows:
        contribution_id = str(row.get("score_contribution_id") or row.get("contribution_id") or "")
        component_key = str(row.get("component_key") or "")
        criterion_id = str(row.get("criterion_id") or component_key)
        raw_points = _float_or_none(row.get("raw_points"))
        max_points = _float_or_none(row.get("max_points"))
        support_claim_ids = tuple(_unique_strings(row.get("support_claim_ids") or ()))
        if not contribution_id or not component_key or raw_points is None or max_points is None:
            continue
        try:
            contributions.append(
                ScoreContributionV2(
                    contribution_id=contribution_id,
                    component_key=component_key,
                    criterion_id=criterion_id,
                    raw_points=raw_points,
                    max_points=max_points,
                    support_claim_ids=support_claim_ids,
                    counter_claim_ids=tuple(_unique_strings(row.get("counter_claim_ids") or ())),
                    mapping_ids=tuple(_unique_strings(row.get("mapping_ids") or ())),
                    source_family_ids=tuple(_unique_strings(row.get("source_family_ids") or ())),
                    cap_reason=str(row.get("cap_reason") or "") or None,
                    rationale=str(row.get("rationale") or ""),
                )
            )
        except ValueError:
            continue
    return contributions


def _support_claim_ids(rows: Sequence[Mapping[str, Any]]) -> list[str]:
    values: list[str] = []
    for row in rows:
        for claim_id in _unique_strings(row.get("support_claim_ids") or ()):
            if claim_id not in values:
                values.append(claim_id)
    return values


def _trace_as_of_date(row: Mapping[str, Any]) -> date | None:
    for key in ("source_cutover_date", "as_of_date"):
        text = str(row.get(key) or "").strip()
        if not text:
            continue
        try:
            return date.fromisoformat(text)
        except ValueError:
            continue
    return None


def _unique_strings(values: Sequence[Any]) -> list[str]:
    if isinstance(values, str):
        values = [values]
    out: list[str] = []
    seen: set[str] = set()
    for value in values:
        text = str(value or "")
        if not text or text in seen:
            continue
        out.append(text)
        seen.add(text)
    return out


def _float_or_none(value: Any) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


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


def _count_by(rows: Sequence[Mapping[str, Any]], key: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        value = str(row.get(key) or "UNKNOWN")
        counts[value] = counts.get(value, 0) + 1
    return counts


def _duplicate_count(values: Sequence[str]) -> int:
    seen: set[str] = set()
    dupes = 0
    for value in values:
        if value in seen:
            dupes += 1
        seen.add(value)
    return dupes


def _claims_brain(metadata: Mapping[str, Any]) -> bool:
    run_mode = str(metadata.get("run_mode") or "")
    brain_web_mode = str(metadata.get("brain_web_mode") or "")
    return "BRAIN" in run_mode or brain_web_mode == "enabled"


def _claims_web(metadata: Mapping[str, Any]) -> bool:
    run_mode = str(metadata.get("run_mode") or "")
    brain_web_mode = str(metadata.get("brain_web_mode") or "")
    return "WEB" in run_mode or brain_web_mode == "enabled"


def _is_unstructured_brain_document(row: Mapping[str, Any]) -> bool:
    if str(row.get("source_origin") or row.get("brain_web_origin") or "") != "research_brain_v4_attempt":
        return False
    parser = str(row.get("parser_version") or "")
    if parser == "research_brain_v4_live_web_fetch":
        return True
    source_type = str(row.get("source_type") or "").upper()
    return source_type in {"NEWS", "RESEARCH_REPORT", "OTHER"} and not str(row.get("canonical_url") or "").startswith("snapshot://")


def _repo_root_for(path: Path) -> Path:
    current = path.resolve()
    for candidate in (current, *current.parents):
        if (candidate / "src" / "e2r").exists() and (candidate / "tests").exists():
            return candidate
    return Path.cwd().resolve()


def _text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def _parse(path: Path) -> ast.Module | None:
    text = _text(path)
    if not text:
        return None
    try:
        return ast.parse(text)
    except SyntaxError:
        return None


def _imports_from(tree: ast.AST | None, module: str, name: str | None = None) -> bool:
    if tree is None:
        return False
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module == module:
            if name is None or any(alias.name == name for alias in node.names):
                return True
    return False


def _calls_name(tree: ast.AST | None, name: str) -> bool:
    if tree is None:
        return False
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if isinstance(func, ast.Name) and func.id == name:
            return True
        if isinstance(func, ast.Attribute) and func.attr == name:
            return True
    return False


def _has_legacy_guard(tree: ast.AST | None, flag_name: str) -> bool:
    if tree is None:
        return False
    for node in ast.walk(tree):
        if not isinstance(node, ast.If):
            continue
        if not _is_not_args_attr(node.test, flag_name):
            continue
        if any(isinstance(child, ast.Return) and _literal_int(child.value) == 2 for child in node.body):
            return True
    return False


def _is_not_args_attr(node: ast.AST, attr: str) -> bool:
    return (
        isinstance(node, ast.UnaryOp)
        and isinstance(node.op, ast.Not)
        and isinstance(node.operand, ast.Attribute)
        and node.operand.attr == attr
        and isinstance(node.operand.value, ast.Name)
        and node.operand.value.id == "args"
    )


def _literal_int(node: ast.AST | None) -> int | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return node.value
    return None


def _legacy_runner_production_reachable_count(repo_root: Path) -> int:
    tree = _parse(repo_root / "src" / "e2r" / "cli" / "run_e2r_census_mode.py")
    imports_legacy = _imports_from(tree, "e2r.census.census_runner", "run_census_mode")
    return int(imports_legacy and not _has_legacy_guard(tree, "allow_legacy_v1"))


def _legacy_v3_runner_production_reachable_count(repo_root: Path) -> int:
    tree = _parse(repo_root / "src" / "e2r" / "cli" / "run_e2r_census_v3_until_pass.py")
    imports_v3 = _imports_from(tree, "e2r.census.census_runner_v3", "run_census_mode_v3")
    return int(imports_v3 and not _has_legacy_guard(tree, "allow_legacy_v3"))


def _empty_claims_stage_builder_production_count(repo_root: Path) -> int:
    count = 0
    for rel in (
        "src/e2r/cli/run_e2r_census_v4_until_pass.py",
        "src/e2r/census/census_runner_v4.py",
    ):
        count += _empty_claim_builder_call_count(_parse(repo_root / rel))
    return count


def _old_cli_can_claim_pass_count(repo_root: Path) -> int:
    return _legacy_runner_production_reachable_count(repo_root) + _legacy_v3_runner_production_reachable_count(repo_root)


def _official_cli_not_v4_runner_count(repo_root: Path) -> int:
    tree = _parse(repo_root / "src" / "e2r" / "cli" / "run_e2r_census_v4_until_pass.py")
    imports_v4_runner = _imports_from(tree, "e2r.census.census_runner_v4", "run_census_mode_v4")
    imports_v4_config = _imports_from(tree, "e2r.census.census_runner_v4", "CensusV4RunConfig")
    calls_v4_runner = _calls_name(tree, "run_census_mode_v4")
    calls_v4_config = _calls_name(tree, "CensusV4RunConfig")
    imports_legacy = _imports_from(tree, "e2r.census.census_runner") or _imports_from(tree, "e2r.census.census_runner_v3")
    return int(not (imports_v4_runner and imports_v4_config and calls_v4_runner and calls_v4_config) or imports_legacy)


def _empty_claim_builder_call_count(tree: ast.AST | None) -> int:
    if tree is None:
        return 1
    empty_names = _empty_sequence_names(tree)
    count = 0
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not _call_func_name_in(node, {"build_atomic_stage_decisions", "AtomicStageDecision"}):
            continue
        for keyword in node.keywords:
            if keyword.arg in {"accepted_claims", "score_contributions"} and _is_empty_sequence_expr(keyword.value, empty_names):
                count += 1
    return count


def _empty_sequence_names(tree: ast.AST) -> set[str]:
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and _is_empty_sequence_expr(node.value, set()):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    names.add(target.id)
        elif isinstance(node, ast.AnnAssign) and node.value is not None and _is_empty_sequence_expr(node.value, set()):
            if isinstance(node.target, ast.Name):
                names.add(node.target.id)
    return names


def _call_func_name_in(node: ast.Call, names: set[str]) -> bool:
    func = node.func
    if isinstance(func, ast.Name):
        return func.id in names
    if isinstance(func, ast.Attribute):
        return func.attr in names
    return False


def _is_empty_sequence_expr(node: ast.AST, empty_names: set[str]) -> bool:
    if isinstance(node, (ast.Tuple, ast.List, ast.Set)) and not node.elts:
        return True
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in {"tuple", "list", "set"} and not node.args and not node.keywords:
        return True
    if isinstance(node, ast.Name) and node.id in empty_names:
        return True
    return False


OPERATOR_SCOPE_ALIAS_FIELDS = (
    "operator_stage_use",
    "operator_score_use",
    "operator_scope_note",
    "stage_scope_display",
    "score_scope_display",
    "base_stage_display",
    "canonical_stage_display",
    "stage_signal_display",
    "census_status_display",
    "assessment_depth_display",
    "stage_decision_status_display",
    "investigation_status_display",
    "stage_confidence_display",
    "score_scale_display",
    "score_valid_status_display",
)

PREFIXED_OPERATOR_ALIAS_FIELDS = (
    "base_stage_display",
    "canonical_stage_display",
    "stage_signal_display",
    "census_status_display",
    "assessment_depth_display",
    "stage_decision_status_display",
    "investigation_status_display",
    "stage_confidence_display",
)


def _operator_scope_alias_missing(row: Mapping[str, Any]) -> bool:
    return any(not row.get(field) for field in OPERATOR_SCOPE_ALIAS_FIELDS)


def _operator_aliases_have_prefix(row: Mapping[str, Any], prefix: str) -> bool:
    expected = prefix + "_"
    return all(str(row.get(field) or "").startswith(expected) for field in PREFIXED_OPERATOR_ALIAS_FIELDS)


def _primitive_ids_by_claim(primitive_states: Sequence[Mapping[str, Any]]) -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for state in primitive_states:
        primitive_state_id = str(state.get("primitive_state_id") or "")
        if not primitive_state_id:
            continue
        for key in ("support_claim_ids", "counter_claim_ids"):
            for claim_id in state.get(key) or ():
                claim_key = str(claim_id)
                if claim_key:
                    out.setdefault(claim_key, set()).add(primitive_state_id)
    return out


def _sample_bundle_missing_scored_row_count(stage_rows: Sequence[Mapping[str, Any]], sample_bundle: Sequence[Mapping[str, Any]]) -> int:
    sample_fingerprints = {_stage_row_fingerprint(row) for row in sample_bundle}
    return sum(
        1
        for row in stage_rows
        if (row.get("score_scale") != "NO_SCORE" or row.get("accepted_claim_ids") or row.get("score_contribution_ids"))
        and _stage_row_fingerprint(row) not in sample_fingerprints
    )


def _stage_row_fingerprint(row: Mapping[str, Any]) -> str:
    content = json.dumps(row, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(content).hexdigest()


__all__ = ["audit_census_v4_leaf_artifacts", "build_artifact_manifest"]
