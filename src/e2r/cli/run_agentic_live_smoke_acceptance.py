"""Summarise Samsung/SK Hynix bounded live smoke acceptance for Evidence OS."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic.source_router import primitive_operating_signal_count, text_has_cash_bridge_signal


DEFAULT_SMOKE_RUN_LOGS: tuple[str, ...] = (
    "output/0621_agentic_live_smoke/005930_after_cp182_legacy_quarantine/korea_live_lite/2026-06-28_run_log.json",
    "output/0621_agentic_live_smoke/000660_after_cp186_target_scoped_cash_guard_budget_open/korea_live_lite/2026-06-28_run_log.json",
)
DEFAULT_DEPRECATED_SUMMARIES: tuple[str, ...] = (
    "output/live_operational_semis_2026-06-21_gap_targeted_patch/summary_005930_gap_targeted_patch.json",
    "output/live_operational_semis_2026-06-21_gap_targeted_patch/summary_000660_gap_targeted_patch.json",
)
DEFAULT_OUTPUT_DIRECTORY = "output/0621_agentic_replay"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build bounded live smoke acceptance for Evidence OS.")
    parser.add_argument("--smoke-run-log", action="append", default=None)
    parser.add_argument("--deprecated-summary", action="append", default=None)
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument(
        "--output-prefix",
        default="samsung_hynix_bounded_live_smoke_evidence_os_acceptance",
    )
    return parser


def run_live_smoke_acceptance(
    *,
    smoke_run_log_paths: Sequence[str | Path],
    deprecated_summary_paths: Sequence[str | Path] = (),
    output_directory: str | Path,
    output_prefix: str = "samsung_hynix_bounded_live_smoke_evidence_os_acceptance",
) -> Mapping[str, Path]:
    smoke_manifests = [_read_smoke_run_log(Path(path)) for path in smoke_run_log_paths]
    deprecated_summaries = [_read_json_mapping(Path(path)) for path in deprecated_summary_paths]
    manifest = build_live_smoke_acceptance_manifest(
        smoke_run_logs=smoke_manifests,
        deprecated_summaries=deprecated_summaries,
    )
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "acceptance_json": output_dir / f"{output_prefix}_acceptance.json",
        "acceptance_md": output_dir / f"{output_prefix}_acceptance.md",
    }
    _write_json(paths["acceptance_json"], manifest)
    paths["acceptance_md"].write_text(_render_acceptance_markdown(manifest), encoding="utf-8")
    return paths


def build_live_smoke_acceptance_manifest(
    *,
    smoke_run_logs: Sequence[Mapping[str, Any]],
    deprecated_summaries: Sequence[Mapping[str, Any]] = (),
) -> Mapping[str, Any]:
    rows: list[Mapping[str, Any]] = []
    for run_log in smoke_run_logs:
        as_of_date = run_log.get("as_of_date")
        rows.extend(_rows_from_run_log(run_log, as_of_date=as_of_date))

    deprecated_rows = [_deprecated_row(summary) for summary in deprecated_summaries]
    pending_rows = [row for row in rows if row.get("acceptance_status") == "pending_not_operational_stage"]
    invalid_rows = [row for row in rows if row.get("acceptance_status") == "invalid_live_smoke_result"]
    operational_rows = [row for row in rows if row.get("acceptance_status") == "accepted_operational_stage"]
    stale_source_router_skip_rows = [
        row for row in rows if row.get("source_router_stale_primitive_signal_skip_summaries")
    ]
    stage_zero_not_operational_rows = [
        row
        for row in invalid_rows
        if "stage_zero_not_operational" in set(row.get("acceptance_block_reasons") or ())
    ]
    stage_zero_valid_score_rows = [
        row for row in stage_zero_not_operational_rows if row.get("score_valid") is True
    ]
    provider_failure_pending_rows = [
        row
        for row in pending_rows
        if row.get("pending_reason_group") in {"provider_failure", "provider_quota_exhausted"}
    ]
    provider_quota_exhausted_pending_rows = [
        row for row in pending_rows if row.get("pending_reason_group") == "provider_quota_exhausted"
    ]
    theme_review_timeout_pending_rows = [
        row for row in pending_rows if row.get("pending_reason_group") == "theme_review_timeout_pending"
    ]
    theme_review_timeout_observed_rows = [
        row for row in rows if row.get("theme_review_timeout_observed")
    ]
    score_gap_no_progress_pending_rows = [
        row for row in pending_rows if row.get("pending_reason_group") == "score_gap_no_progress"
    ]
    score_gap_budget_blocked_pending_rows = [
        row for row in pending_rows if row.get("pending_reason_group") == "score_gap_budget_blocked"
    ]
    score_gap_evidence_progress_pending_rows = [
        row for row in pending_rows if row.get("pending_reason_group") == "score_gap_evidence_progress_pending"
    ]
    score_gap_rejected_mapping_pending_rows = [
        row for row in pending_rows if row.get("post_score_gap_new_rejected_mapping_count", 0)
    ]
    cash_bridge_pending_rows = [
        row for row in rows if row.get("cash_bridge_pending")
    ]
    cash_bridge_quorum_without_signal_rows = [
        row for row in rows if row.get("cash_bridge_source_quorum_without_signal")
    ]
    legacy_parser_score_audit_missing_rows = [
        row for row in rows if not row.get("legacy_parser_score_audit_observed")
    ]
    legacy_parser_score_without_v2_rows = [
        row for row in rows if row.get("legacy_parser_score_claim_without_v2")
    ]
    legacy_parser_score_quarantined_rows = [
        row for row in rows if _int_count(row.get("legacy_parser_score_claim_without_v2_quarantined_count")) > 0
    ]
    evidence_family_gap_pending_rows = [
        row for row in pending_rows if row.get("evidence_family_missing_families")
    ]
    evidence_family_gap_current_rows = [
        row for row in rows if row.get("evidence_family_missing_families")
    ]
    deterministic_fallback_query_rows = [
        row for row in rows if row.get("post_score_gap_deterministic_fallback_query_used")
    ]
    query_origin_missing_rows = [
        row for row in rows if row.get("post_score_gap_query_origin_missing")
    ]
    append_only_violation_rows = [
        row for row in rows if row.get("post_score_gap_append_only_violation")
    ]
    mapper_empty_output_rows = [
        row
        for row in rows
        if int(row.get("agentic_evidence_mapping_empty_output_count") or 0) > 0
        or int(row.get("post_score_gap_new_trace_mapping_empty_output_count") or 0) > 0
    ]
    mapper_empty_retry_rows = [
        row
        for row in rows
        if int(row.get("agentic_evidence_mapping_empty_output_retry_count") or 0) > 0
        or int(row.get("post_score_gap_new_trace_mapping_empty_output_retry_count") or 0) > 0
    ]
    mapper_empty_recovered_rows = [
        row
        for row in rows
        if int(row.get("agentic_evidence_mapping_empty_output_recovered_count") or 0) > 0
        or int(row.get("post_score_gap_new_trace_mapping_empty_output_recovered_count") or 0) > 0
    ]
    mapper_fallback_full_map_rows = [
        row
        for row in rows
        if int(row.get("agentic_evidence_mapping_prefilter_fallback_full_map_count") or 0) > 0
        or int(row.get("post_score_gap_new_trace_mapping_prefilter_fallback_full_map_count") or 0) > 0
    ]
    material_score_interval_pending_rows = [
        row for row in rows if row.get("agentic_stage_court_runtime_score_status") == "PENDING_MATERIAL_GAPS"
    ]
    score_interval_boundary_crossing_rows = [
        row for row in rows if row.get("agentic_stage_court_material_stage_boundaries_crossed")
    ]
    structured_consensus_selected_without_signal_rows = [
        row for row in pending_rows if row.get("structured_consensus_selected_without_family_signal")
    ]
    structured_consensus_revision_selected_without_signal_rows = [
        row for row in pending_rows if row.get("structured_consensus_revision_selected_without_family_signal")
    ]
    consensus_family_missing_rows = [
        row for row in pending_rows if "consensus" in set(row.get("evidence_family_missing_families") or ())
    ]
    consensus_family_missing_current_rows = [
        row for row in rows if "consensus" in set(row.get("evidence_family_missing_families") or ())
    ]
    consensus_revision_family_missing_rows = [
        row
        for row in pending_rows
        if "consensus_revision" in set(row.get("evidence_family_missing_families") or ())
    ]
    consensus_revision_family_missing_current_rows = [
        row
        for row in rows
        if "consensus_revision" in set(row.get("evidence_family_missing_families") or ())
    ]
    consensus_proxy_only_gap_rows = [
        row
        for row in pending_rows
        if "consensus" in set(row.get("evidence_family_independent_missing_but_proxy_present_families") or ())
    ]
    consensus_revision_proxy_only_gap_rows = [
        row
        for row in pending_rows
        if "consensus_revision"
        in set(row.get("evidence_family_independent_missing_but_proxy_present_families") or ())
    ]
    source_count_summary = _source_call_count_summary(smoke_run_logs)
    deprecated_invalid_rows = [
        row for row in deprecated_rows if row.get("acceptance_status") == "deprecated_legacy_result_not_accepted"
    ]
    live_smoke_acceptance_ready = (
        bool(rows)
        and len(operational_rows) == len(rows)
        and not pending_rows
        and not invalid_rows
        and not cash_bridge_pending_rows
        and not cash_bridge_quorum_without_signal_rows
        and not legacy_parser_score_audit_missing_rows
        and not legacy_parser_score_without_v2_rows
    )
    return {
        "schema_version": "e2r_live_smoke_acceptance_manifest_v1",
        "summary": {
            "smoke_target_count": len(rows),
            "smoke_run_log_paths": _source_run_log_paths(smoke_run_logs),
            "accepted_operational_stage_count": len(operational_rows),
            "pending_not_operational_stage_count": len(pending_rows),
            "invalid_live_smoke_result_count": len(invalid_rows),
            "source_router_stale_primitive_signal_skip_count": len(stale_source_router_skip_rows),
            "stage_zero_not_operational_count": len(stage_zero_not_operational_rows),
            "stage_zero_valid_score_count": len(stage_zero_valid_score_rows),
            "provider_failure_pending_count": len(provider_failure_pending_rows),
            "provider_quota_exhausted_pending_count": len(provider_quota_exhausted_pending_rows),
            "theme_review_timeout_pending_count": len(theme_review_timeout_pending_rows),
            "theme_review_timeout_observed_count": len(theme_review_timeout_observed_rows),
            "score_gap_no_progress_pending_count": len(score_gap_no_progress_pending_rows),
            "score_gap_budget_blocked_pending_count": len(score_gap_budget_blocked_pending_rows),
            "score_gap_evidence_progress_pending_count": len(score_gap_evidence_progress_pending_rows),
            "score_gap_rejected_mapping_pending_count": len(score_gap_rejected_mapping_pending_rows),
            "cash_bridge_pending_count": len(cash_bridge_pending_rows),
            "cash_bridge_source_quorum_without_signal_count": len(cash_bridge_quorum_without_signal_rows),
            "legacy_parser_score_audit_missing_count": len(legacy_parser_score_audit_missing_rows),
            "legacy_parser_score_claim_without_v2_current_row_count": len(legacy_parser_score_without_v2_rows),
            "legacy_parser_score_claim_without_v2_quarantined_row_count": len(
                legacy_parser_score_quarantined_rows
            ),
            "legacy_parser_score_claim_without_v2_quarantined_total_count": sum(
                _int_count(row.get("legacy_parser_score_claim_without_v2_quarantined_count"))
                for row in legacy_parser_score_quarantined_rows
            ),
            "evidence_family_gap_pending_count": len(evidence_family_gap_pending_rows),
            "evidence_family_gap_current_row_count": len(evidence_family_gap_current_rows),
            "consensus_family_missing_pending_count": len(consensus_family_missing_rows),
            "consensus_family_missing_current_row_count": len(consensus_family_missing_current_rows),
            "consensus_revision_family_missing_pending_count": len(consensus_revision_family_missing_rows),
            "consensus_revision_family_missing_current_row_count": len(
                consensus_revision_family_missing_current_rows
            ),
            "consensus_proxy_only_gap_pending_count": len(consensus_proxy_only_gap_rows),
            "consensus_revision_proxy_only_gap_pending_count": len(consensus_revision_proxy_only_gap_rows),
            "company_guide_snapshot_call_count": source_count_summary["company_guide_snapshot_calls"],
            "company_guide_snapshot_empty_consensus_count": source_count_summary[
                "company_guide_snapshot_empty_consensus_count"
            ],
            "company_guide_recent_report_call_count": source_count_summary["company_guide_recent_report_calls"],
            "naver_finance_item_main_call_count": source_count_summary["naver_finance_item_main_calls"],
            "deterministic_fallback_query_used_count": len(deterministic_fallback_query_rows),
            "post_score_gap_query_origin_missing_count": len(query_origin_missing_rows),
            "post_score_gap_append_only_violation_count": len(append_only_violation_rows),
            "agentic_mapper_empty_output_count": len(mapper_empty_output_rows),
            "agentic_mapper_empty_output_retry_count": len(mapper_empty_retry_rows),
            "agentic_mapper_empty_output_recovered_count": len(mapper_empty_recovered_rows),
            "agentic_mapper_fallback_full_map_count": len(mapper_fallback_full_map_rows),
            "material_score_interval_pending_count": len(material_score_interval_pending_rows),
            "score_interval_boundary_crossing_pending_count": len(score_interval_boundary_crossing_rows),
            "structured_consensus_selected_without_family_signal_count": len(
                structured_consensus_selected_without_signal_rows
            ),
            "structured_consensus_revision_selected_without_family_signal_count": len(
                structured_consensus_revision_selected_without_signal_rows
            ),
            "deprecated_legacy_result_count": len(deprecated_rows),
            "deprecated_legacy_result_not_accepted_count": len(deprecated_invalid_rows),
            "live_smoke_acceptance_ready": live_smoke_acceptance_ready,
            "production_cutover_ready": live_smoke_acceptance_ready,
            "live_smoke_acceptance_status": (
                "live_smoke_acceptance_ready"
                if live_smoke_acceptance_ready
                else "pending_or_invalid_not_production_ready"
            ),
        },
        "rows": rows,
        "deprecated_rows": deprecated_rows,
    }


def _rows_from_run_log(run_log: Mapping[str, Any], *, as_of_date: Any) -> list[Mapping[str, Any]]:
    rows: list[Mapping[str, Any]] = []
    source_call_counts = run_log.get("source_call_counts") or {}
    phase_log_quota_symbols = {
        str(symbol)
        for symbol in run_log.get("_phase_log_provider_quota_exhausted_symbols") or ()
        if str(symbol).strip()
    }
    phase_log_mapper_metrics = {
        str(symbol): metrics
        for symbol, metrics in (run_log.get("_phase_log_agentic_mapper_metrics_by_symbol") or {}).items()
        if str(symbol).strip() and isinstance(metrics, Mapping)
    }
    for row in run_log.get("targeted_smoke_results") or ():
        if not isinstance(row, Mapping):
            continue
        row_with_sidecar = dict(row)
        if str(row.get("symbol")) in phase_log_quota_symbols:
            row_with_sidecar["_phase_log_provider_quota_exhausted"] = True
        metrics = phase_log_mapper_metrics.get(str(row.get("symbol")))
        if metrics:
            _apply_phase_log_mapper_metrics(row_with_sidecar, metrics)
        row = row_with_sidecar
        score_valid = row.get("score_valid")
        visible_score = row.get("visible_score")
        stage = row.get("stage")
        stage_court_stage = row.get("agentic_stage_court_runtime_stage")
        stage_court_score_status = row.get("agentic_stage_court_runtime_score_status")
        score_contribution_archetype_mismatch = bool(row.get("agentic_score_contribution_v2_archetype_mismatch"))
        legacy_parser_score_audit_observed = _legacy_parser_score_audit_observed(row)
        legacy_parser_score_claim_without_v2_count = _legacy_parser_score_claim_without_v2_count(row)
        legacy_parser_score_claim_without_v2_quarantined_count = (
            _legacy_parser_score_claim_without_v2_quarantined_count(row)
        )
        legacy_parser_score_claim_without_v2 = legacy_parser_score_claim_without_v2_count > 0
        deterministic_fallback_query_used = _row_uses_deterministic_fallback_query(row)
        query_origin_missing = _row_has_score_gap_route_plan_missing_query_origin(row)
        append_only_violation = bool(row.get("post_score_gap_append_only_violation"))
        mapper_empty_output_observed = (
            int(row.get("agentic_evidence_mapping_empty_output_count") or 0) > 0
            or int(row.get("post_score_gap_new_trace_mapping_empty_output_count") or 0) > 0
        )
        mapper_fallback_full_map_observed = (
            int(row.get("agentic_evidence_mapping_prefilter_fallback_full_map_count") or 0) > 0
            or int(row.get("post_score_gap_new_trace_mapping_prefilter_fallback_full_map_count") or 0) > 0
        )
        theme_review_timeout_observed = _row_has_theme_review_timeout(row)
        theme_review_timeout_blocks_operational_stage = (
            theme_review_timeout_observed
            and score_valid is False
            and stage in (0, "0", None)
            and visible_score is None
        )
        provider_failure_blocks_operational_stage = (
            score_valid is False
            and stage in (0, "0", None)
            and visible_score is None
            and (
                _row_has_provider_quota_failure(row)
                or _row_has_agentic_provider_failure(row)
                or _row_has_theme_route_provider_failure(row)
            )
        )
        cash_bridge_gaps = _cash_bridge_gap_summaries(row)
        stale_source_router_skips = _source_router_stale_primitive_signal_skip_summaries(row)
        if theme_review_timeout_blocks_operational_stage:
            status = "pending_not_operational_stage"
        elif provider_failure_blocks_operational_stage:
            status = "pending_not_operational_stage"
        elif score_contribution_archetype_mismatch:
            status = "invalid_live_smoke_result"
        elif score_valid is True and not legacy_parser_score_audit_observed:
            status = "invalid_live_smoke_result"
        elif score_valid is True and legacy_parser_score_claim_without_v2:
            status = "invalid_live_smoke_result"
        elif deterministic_fallback_query_used:
            status = "invalid_live_smoke_result"
        elif append_only_violation:
            status = "invalid_live_smoke_result"
        elif mapper_empty_output_observed:
            status = "invalid_live_smoke_result"
        elif mapper_fallback_full_map_observed:
            status = "invalid_live_smoke_result"
        elif query_origin_missing and score_valid is True:
            status = "invalid_live_smoke_result"
        elif cash_bridge_gaps and score_valid is True:
            status = "invalid_live_smoke_result"
        elif stale_source_router_skips and score_valid is True:
            status = "invalid_live_smoke_result"
        elif score_valid is False and (stage in (0, "0", None)) and visible_score is None:
            status = "pending_not_operational_stage"
        elif (
            score_valid is True
            and visible_score is not None
            and stage not in (0, "0", None)
            and row.get("scoring_canonical_archetype_id")
            and stage_court_stage is not None
            and stage_court_score_status in ("FINAL", "FINAL_WITH_NONMATERIAL_GAPS")
        ):
            status = "accepted_operational_stage"
        else:
            status = "invalid_live_smoke_result"
        production_fixture = status == "accepted_operational_stage"
        pending_reason_group = _pending_reason_group(row, acceptance_status=status)
        cash_bridge_quorum_without_signal = _cash_bridge_source_quorum_without_signal_summaries(row)
        acceptance_block_reasons = _acceptance_block_reasons(
            row,
            acceptance_status=status,
            pending_reason_group=pending_reason_group,
            score_contribution_archetype_mismatch=score_contribution_archetype_mismatch,
            legacy_parser_score_audit_observed=legacy_parser_score_audit_observed,
            legacy_parser_score_claim_without_v2=legacy_parser_score_claim_without_v2,
            deterministic_fallback_query_used=deterministic_fallback_query_used,
            query_origin_missing=query_origin_missing,
            append_only_violation=append_only_violation,
            mapper_empty_output_observed=mapper_empty_output_observed,
            mapper_fallback_full_map_observed=mapper_fallback_full_map_observed,
            cash_bridge_pending=bool(cash_bridge_gaps),
            cash_bridge_source_quorum_without_signal=bool(cash_bridge_quorum_without_signal),
            source_router_stale_primitive_signal_skip=bool(stale_source_router_skips),
            theme_review_timeout_blocks_operational_stage=theme_review_timeout_blocks_operational_stage,
        )
        material_gaps = list(row.get("material_score_gap_unresolved_gaps") or ())
        stage_zero_diagnostics = _stage_zero_not_operational_diagnostics(
            row,
            material_gaps=material_gaps,
        )
        evidence_family_row = _evidence_family_row(row)
        structured_consensus_without_signal = _structured_consensus_selected_without_family_signal_summaries(
            row,
            family="consensus",
        )
        structured_consensus_revision_without_signal = _structured_consensus_selected_without_family_signal_summaries(
            row,
            family="consensus_revision",
        )
        rows.append(
            {
                "symbol": row.get("symbol"),
                "company_name": row.get("company_name") or row.get("company"),
                "as_of_date": as_of_date,
                "smoke_run_log_path": run_log.get("_source_run_log_path"),
                "smoke_phase_log_path": run_log.get("_source_phase_log_path"),
                "company_guide_snapshot_calls": _int_count(
                    source_call_counts.get("company_guide_snapshot_calls")
                ),
                "company_guide_snapshot_empty_consensus_count": _int_count(
                    source_call_counts.get("company_guide_snapshot_empty_consensus_count")
                ),
                "company_guide_recent_report_calls": _int_count(
                    source_call_counts.get("company_guide_recent_report_calls")
                ),
                "naver_finance_item_main_calls": _int_count(
                    source_call_counts.get("naver_finance_item_main_calls")
                ),
                "company_guide_snapshot_empty_consensus_observed": _int_count(
                    source_call_counts.get("company_guide_snapshot_empty_consensus_count")
                )
                > 0,
                "stage": str(stage) if stage is not None else None,
                "visible_score": visible_score,
                "score_valid": score_valid,
                "stage_zero_not_operational_diagnostics": stage_zero_diagnostics,
                "score_blocked_reason": row.get("score_blocked_reason"),
                "score_status": row.get("score_status") or row.get("agentic_stage_court_runtime_score_status"),
                "verified_score": row.get("verified_score") or row.get("agentic_stage_court_verified_score"),
                "provisional_score": row.get("provisional_score"),
                "score_interval_lower": row.get("score_interval_lower") or row.get("agentic_stage_court_verified_score"),
                "score_interval_upper": row.get("score_interval_upper")
                or row.get("agentic_stage_court_potential_score_upper_bound"),
                "theme_route_status": row.get("theme_route_status"),
                "theme_route_blocked_reason": row.get("theme_route_blocked_reason"),
                "theme_route_timeout_seconds": row.get("theme_route_timeout_seconds"),
                "theme_evidence_review_status": row.get("theme_evidence_review_status"),
                "theme_evidence_review_blocked_reason": row.get("theme_evidence_review_blocked_reason"),
                "theme_canonical_archetype_id": row.get("theme_canonical_archetype_id"),
                "scoring_canonical_archetype_id": row.get("scoring_canonical_archetype_id"),
                "agentic_score_contribution_v2_archetype_id": row.get("agentic_score_contribution_v2_archetype_id"),
                "agentic_score_contribution_v2_archetype_mismatch": row.get(
                    "agentic_score_contribution_v2_archetype_mismatch",
                ),
                "legacy_parser_score_audit_observed": legacy_parser_score_audit_observed,
                "legacy_parser_score_claim_without_v2": legacy_parser_score_claim_without_v2,
                "legacy_parser_score_claim_without_v2_count": legacy_parser_score_claim_without_v2_count,
                "legacy_parser_score_claim_fields_without_v2": _string_list(
                    row.get("legacy_parser_score_claim_fields_without_v2")
                ),
                "legacy_parser_score_claim_quarantined_by_v2": (
                    legacy_parser_score_claim_without_v2_quarantined_count > 0
                ),
                "legacy_parser_score_claim_without_v2_quarantined_count": (
                    legacy_parser_score_claim_without_v2_quarantined_count
                ),
                "legacy_parser_score_claim_without_v2_quarantined_count_capped": _int_count(
                    row.get("legacy_parser_score_claim_without_v2_quarantined_count_capped")
                ),
                "legacy_parser_score_claim_fields_quarantined_by_v2": _string_list(
                    row.get("legacy_parser_score_claim_fields_quarantined_by_v2")
                ),
                "agentic_evidence_status": row.get("agentic_evidence_status"),
                "agentic_evidence_document_limit": row.get("agentic_evidence_document_limit"),
                "agentic_evidence_provider_timeout_seconds": row.get(
                    "agentic_evidence_provider_timeout_seconds"
                ),
                "agentic_evidence_document_count": row.get("agentic_evidence_document_count"),
                "agentic_evidence_claim_count": row.get("agentic_evidence_claim_count"),
                "agentic_evidence_accepted_mapping_count": row.get("agentic_evidence_accepted_mapping_count"),
                "agentic_evidence_mapping_prefilter_original_task_count": row.get(
                    "agentic_evidence_mapping_prefilter_original_task_count",
                    0,
                ),
                "agentic_evidence_mapping_prefilter_filtered_task_count": row.get(
                    "agentic_evidence_mapping_prefilter_filtered_task_count",
                    0,
                ),
                "agentic_evidence_mapping_prefilter_skipped_input_count": row.get(
                    "agentic_evidence_mapping_prefilter_skipped_input_count",
                    0,
                ),
                "agentic_evidence_mapping_prefilter_fallback_full_map_count": row.get(
                    "agentic_evidence_mapping_prefilter_fallback_full_map_count",
                    0,
                ),
                "agentic_evidence_mapping_prefilter_fallback_full_map_summaries": list(
                    row.get("agentic_evidence_mapping_prefilter_fallback_full_map_summaries") or ()
                ),
                "agentic_evidence_mapping_empty_output_count": row.get(
                    "agentic_evidence_mapping_empty_output_count",
                    0,
                ),
                "agentic_evidence_mapping_empty_output_retry_count": row.get(
                    "agentic_evidence_mapping_empty_output_retry_count",
                    0,
                ),
                "agentic_evidence_mapping_empty_output_recovered_count": row.get(
                    "agentic_evidence_mapping_empty_output_recovered_count",
                    0,
                ),
                "agentic_evidence_mapping_empty_output_summaries": list(
                    row.get("agentic_evidence_mapping_empty_output_summaries") or ()
                ),
                "agentic_evidence_mapping_empty_output_retry_summaries": list(
                    row.get("agentic_evidence_mapping_empty_output_retry_summaries") or ()
                ),
                "agentic_evidence_error_count": row.get("agentic_evidence_error_count", 0),
                "agentic_evidence_errors": list(row.get("agentic_evidence_errors") or ()),
                "agentic_evidence_present_primitives": list(row.get("agentic_evidence_present_primitives") or ()),
                "agentic_stage_court_runtime_stage": row.get("agentic_stage_court_runtime_stage"),
                "agentic_stage_court_runtime_score_status": row.get("agentic_stage_court_runtime_score_status"),
                "agentic_stage_court_verified_score": row.get("agentic_stage_court_verified_score"),
                "agentic_stage_court_potential_score_upper_bound": row.get(
                    "agentic_stage_court_potential_score_upper_bound"
                ),
                "agentic_stage_court_unresolved_material_gap_points": row.get(
                    "agentic_stage_court_unresolved_material_gap_points"
                ),
                "agentic_stage_court_score_interval_width": row.get("agentic_stage_court_score_interval_width"),
                "agentic_stage_court_material_stage_boundaries_crossed": list(
                    row.get("agentic_stage_court_material_stage_boundaries_crossed") or ()
                ),
                "agentic_stage_court_material_stage_boundary_crossed_count": row.get(
                    "agentic_stage_court_material_stage_boundary_crossed_count",
                    0,
                ),
                "post_score_gap_expansion_status": row.get("post_score_gap_expansion_status"),
                "post_score_gap_progress_reason": row.get("post_score_gap_progress_reason"),
                "post_score_gap_rejection_reasons": list(row.get("post_score_gap_rejection_reasons") or ()),
                "post_score_gap_append_only_violation": append_only_violation,
                "post_score_gap_reprocessed_document_count": row.get(
                    "post_score_gap_reprocessed_document_count",
                    0,
                ),
                "post_score_gap_reprocessed_document_ids": list(
                    row.get("post_score_gap_reprocessed_document_ids") or ()
                ),
                "post_score_gap_primitive_state_changed": row.get("post_score_gap_primitive_state_changed"),
                "post_score_gap_score_contribution_changed": row.get(
                    "post_score_gap_score_contribution_changed",
                ),
                "post_score_gap_score_contribution_delta_summaries": list(
                    row.get("post_score_gap_score_contribution_delta_summaries") or ()
                ),
                "post_score_gap_new_rejected_mapping_count": row.get(
                    "post_score_gap_new_rejected_mapping_count",
                    0,
                ),
                "post_score_gap_new_rejected_mapping_summaries": list(
                    row.get("post_score_gap_new_rejected_mapping_summaries") or ()
                ),
                "post_score_gap_new_eligibility_rejection_summaries": list(
                    row.get("post_score_gap_new_eligibility_rejection_summaries") or ()
                ),
                "post_score_gap_new_trace_status": row.get("post_score_gap_new_trace_status"),
                "post_score_gap_new_trace_mapping_prefilter_original_task_count": row.get(
                    "post_score_gap_new_trace_mapping_prefilter_original_task_count",
                    0,
                ),
                "post_score_gap_new_trace_mapping_prefilter_filtered_task_count": row.get(
                    "post_score_gap_new_trace_mapping_prefilter_filtered_task_count",
                    0,
                ),
                "post_score_gap_new_trace_mapping_prefilter_skipped_input_count": row.get(
                    "post_score_gap_new_trace_mapping_prefilter_skipped_input_count",
                    0,
                ),
                "post_score_gap_new_trace_mapping_prefilter_fallback_full_map_count": row.get(
                    "post_score_gap_new_trace_mapping_prefilter_fallback_full_map_count",
                    0,
                ),
                "post_score_gap_new_trace_mapping_prefilter_fallback_full_map_summaries": list(
                    row.get("post_score_gap_new_trace_mapping_prefilter_fallback_full_map_summaries") or ()
                ),
                "post_score_gap_new_trace_mapping_empty_output_count": row.get(
                    "post_score_gap_new_trace_mapping_empty_output_count",
                    0,
                ),
                "post_score_gap_new_trace_mapping_empty_output_retry_count": row.get(
                    "post_score_gap_new_trace_mapping_empty_output_retry_count",
                    0,
                ),
                "post_score_gap_new_trace_mapping_empty_output_recovered_count": row.get(
                    "post_score_gap_new_trace_mapping_empty_output_recovered_count",
                    0,
                ),
                "post_score_gap_new_trace_mapping_empty_output_summaries": list(
                    row.get("post_score_gap_new_trace_mapping_empty_output_summaries") or ()
                ),
                "post_score_gap_new_trace_mapping_empty_output_retry_summaries": list(
                    row.get("post_score_gap_new_trace_mapping_empty_output_retry_summaries") or ()
                ),
                "post_score_gap_new_trace_error_count": row.get("post_score_gap_new_trace_error_count", 0),
                "post_score_gap_new_trace_errors": list(row.get("post_score_gap_new_trace_errors") or ()),
                "post_score_gap_source_route_plan_count": len(row.get("post_score_gap_source_route_plans") or ()),
                "post_score_gap_source_route_plans": list(row.get("post_score_gap_source_route_plans") or ()),
                "source_router_stale_primitive_signal_skip_summaries": stale_source_router_skips,
                "post_score_gap_query_origins": _row_query_origins(row),
                "post_score_gap_query_origin_missing": query_origin_missing,
                "post_score_gap_query_origin_missing_summaries": _row_query_origin_missing_summaries(row),
                "post_score_gap_deterministic_fallback_query_used": deterministic_fallback_query_used,
                "material_gap_count": len(material_gaps),
                "material_score_gap_unresolved_gaps": material_gaps,
                "cash_bridge_pending": bool(cash_bridge_gaps),
                "cash_bridge_gap_summaries": cash_bridge_gaps,
                "cash_bridge_source_quorum_without_signal": bool(cash_bridge_quorum_without_signal),
                "cash_bridge_source_quorum_without_signal_summaries": cash_bridge_quorum_without_signal,
                **evidence_family_row,
                "structured_consensus_selected_without_family_signal": bool(structured_consensus_without_signal),
                "structured_consensus_selected_without_family_signal_summaries": structured_consensus_without_signal,
                "structured_consensus_revision_selected_without_family_signal": bool(
                    structured_consensus_revision_without_signal
                ),
                "structured_consensus_revision_selected_without_family_signal_summaries": (
                    structured_consensus_revision_without_signal
                ),
                "final_stage_after_agentic_court": row.get("final_stage_after_agentic_court"),
                "acceptance_status": status,
                "acceptance_block_reasons": acceptance_block_reasons,
                "pending_reason_group": pending_reason_group,
                "provider_failure_pending": pending_reason_group
                in {"provider_failure", "provider_quota_exhausted"},
                "provider_quota_exhausted_pending": pending_reason_group == "provider_quota_exhausted",
                "theme_review_timeout_pending": pending_reason_group == "theme_review_timeout_pending",
                "theme_review_timeout_observed": theme_review_timeout_observed,
                "production_score_fixture": production_fixture,
                "production_stage_fixture": production_fixture,
            }
        )
    return rows


def _source_call_count_summary(smoke_run_logs: Sequence[Mapping[str, Any]]) -> Mapping[str, int]:
    keys = (
        "company_guide_snapshot_calls",
        "company_guide_snapshot_empty_consensus_count",
        "company_guide_recent_report_calls",
        "naver_finance_item_main_calls",
    )
    totals = {key: 0 for key in keys}
    for run_log in smoke_run_logs:
        counts = run_log.get("source_call_counts") or {}
        if not isinstance(counts, Mapping):
            continue
        for key in keys:
            totals[key] += _int_count(counts.get(key))
    return totals


def _stage_zero_not_operational_diagnostics(
    row: Mapping[str, Any],
    *,
    material_gaps: Sequence[Any],
) -> list[str]:
    stage = row.get("stage")
    if not (row.get("score_valid") is True and row.get("visible_score") is not None and stage in (0, "0", None)):
        return []

    diagnostics = [
        (
            "score_valid_true_stage_zero:"
            f" visible_score={row.get('visible_score')};"
            f" verified_score={row.get('verified_score') or row.get('agentic_stage_court_verified_score')};"
            f" potential_score_upper_bound={row.get('score_interval_upper') or row.get('agentic_stage_court_potential_score_upper_bound')};"
            f" score_status={row.get('score_status') or row.get('agentic_stage_court_runtime_score_status')}"
        ),
        (
            "stage_court:"
            f" runtime_stage={row.get('agentic_stage_court_runtime_stage')};"
            f" unresolved_material_gap_points={row.get('agentic_stage_court_unresolved_material_gap_points')};"
            f" boundary_crossed={list(row.get('agentic_stage_court_material_stage_boundaries_crossed') or ())}"
        ),
    ]
    present_primitives = _string_list(row.get("agentic_evidence_present_primitives"))
    if present_primitives:
        diagnostics.append(f"present_primitives={present_primitives[:12]}")
    if material_gaps:
        diagnostics.append(f"material_gaps={len(material_gaps)}; first={list(material_gaps[:5])}")
    diagnostics.append(
        "post_score_gap:"
        f" expansion_status={row.get('post_score_gap_expansion_status')};"
        f" progress_reason={row.get('post_score_gap_progress_reason')};"
        f" rejection_reasons={list(row.get('post_score_gap_rejection_reasons') or ())[:8]};"
        f" new_rejected_mapping_count={row.get('post_score_gap_new_rejected_mapping_count', 0)};"
        f" primitive_state_changed={row.get('post_score_gap_primitive_state_changed')};"
        f" score_contribution_changed={row.get('post_score_gap_score_contribution_changed')}"
    )
    diagnostics.append(
        "legacy_parser_quarantine:"
        f" active_without_v2={_legacy_parser_score_claim_without_v2_count(row)};"
        f" quarantined_by_v2={_legacy_parser_score_claim_without_v2_quarantined_count(row)}"
    )
    return diagnostics


def _source_router_stale_primitive_signal_skip_summaries(row: Mapping[str, Any]) -> list[str]:
    summaries: list[str] = []
    for plan in row.get("post_score_gap_source_route_plans") or ():
        if not isinstance(plan, Mapping):
            continue
        primitive_gap = str(plan.get("primitive_gap") or "").strip()
        if not primitive_gap:
            continue
        for audit_row in plan.get("skipped_candidate_audit_rows") or ():
            if not isinstance(audit_row, Mapping):
                continue
            if str(audit_row.get("reason") or "").strip() != "primitive_operating_signal_missing":
                continue
            text_parts: list[str] = []
            for key in ("title", "snippet", "url", "source_family_id"):
                text_parts.extend(_string_list(audit_row.get(key)))
            text = " ".join(text_parts)
            signal_count = primitive_operating_signal_count(primitive_gap, text)
            if signal_count <= 0:
                continue
            summaries.append(
                "stale primitive signal skip:"
                f" primitive_gap={primitive_gap};"
                f" candidate_id={audit_row.get('candidate_id')};"
                f" signal_count={signal_count};"
                f" source_type={audit_row.get('source_type')};"
                f" published_at={audit_row.get('published_at')};"
                f" title={audit_row.get('title')}"
            )
            if len(summaries) >= 20:
                return summaries
    return list(dict.fromkeys(summaries))[:20]


def _int_count(value: Any) -> int:
    try:
        return int(value or 0)
    except (TypeError, ValueError):
        return 0


def _legacy_parser_score_audit_observed(row: Mapping[str, Any]) -> bool:
    return any(
        key in row
        for key in (
            "legacy_parser_score_claim_without_v2_count",
            "legacy_parser_score_claim_without_v2_count_capped",
            "legacy_parser_score_claim_fields_without_v2",
        )
    )


def _legacy_parser_score_claim_without_v2_count(row: Mapping[str, Any]) -> int:
    if "legacy_parser_score_claim_without_v2_count" in row:
        return _int_count(row.get("legacy_parser_score_claim_without_v2_count"))
    return _int_count(row.get("legacy_parser_score_claim_without_v2_count_capped"))


def _legacy_parser_score_claim_without_v2_quarantined_count(row: Mapping[str, Any]) -> int:
    if "legacy_parser_score_claim_without_v2_quarantined_count" in row:
        return _int_count(row.get("legacy_parser_score_claim_without_v2_quarantined_count"))
    return _int_count(row.get("legacy_parser_score_claim_without_v2_quarantined_count_capped"))


def _acceptance_block_reasons(
    row: Mapping[str, Any],
    *,
    acceptance_status: str,
    pending_reason_group: str | None,
    score_contribution_archetype_mismatch: bool,
    legacy_parser_score_audit_observed: bool,
    legacy_parser_score_claim_without_v2: bool,
    deterministic_fallback_query_used: bool,
    query_origin_missing: bool,
    append_only_violation: bool,
    mapper_empty_output_observed: bool,
    mapper_fallback_full_map_observed: bool,
    cash_bridge_pending: bool,
    cash_bridge_source_quorum_without_signal: bool,
    source_router_stale_primitive_signal_skip: bool,
    theme_review_timeout_blocks_operational_stage: bool,
) -> list[str]:
    if acceptance_status == "accepted_operational_stage":
        return []

    reasons: list[str] = []
    if acceptance_status == "pending_not_operational_stage":
        if pending_reason_group:
            reasons.append(str(pending_reason_group))
        if theme_review_timeout_blocks_operational_stage:
            reasons.append("theme_review_timeout_pending")

    if score_contribution_archetype_mismatch and pending_reason_group not in {
        "provider_failure",
        "provider_quota_exhausted",
    }:
        reasons.append("agentic_score_contribution_v2_archetype_mismatch")
    if row.get("score_valid") is True and not legacy_parser_score_audit_observed:
        reasons.append("legacy_parser_score_audit_missing")
    if row.get("score_valid") is True and legacy_parser_score_claim_without_v2:
        reasons.append("legacy_parser_score_claim_without_v2")
    if deterministic_fallback_query_used:
        reasons.append("deterministic_fallback_query_used")
    if append_only_violation:
        reasons.append("post_score_gap_append_only_violation")
    if mapper_empty_output_observed:
        reasons.append("agentic_mapper_empty_output")
    if mapper_fallback_full_map_observed:
        reasons.append("agentic_mapper_fallback_full_map")
    if query_origin_missing and row.get("score_valid") is True:
        reasons.append("post_score_gap_query_origin_missing")
    if cash_bridge_source_quorum_without_signal and row.get("score_valid") is True:
        reasons.append("cash_bridge_source_quorum_without_signal")
    if cash_bridge_pending and row.get("score_valid") is True:
        reasons.append("cash_bridge_pending")
    if source_router_stale_primitive_signal_skip and row.get("score_valid") is True:
        reasons.append("source_router_stale_primitive_signal_skip")

    stage = row.get("stage")
    if row.get("score_valid") is True and row.get("visible_score") is not None and stage in (0, "0", None):
        reasons.append("stage_zero_not_operational")
    if row.get("score_valid") is True and row.get("scoring_canonical_archetype_id") and row.get(
        "agentic_stage_court_runtime_stage"
    ) is None:
        reasons.append("missing_agentic_stage_court_runtime_stage")
    stage_court_score_status = row.get("agentic_stage_court_runtime_score_status")
    if (
        row.get("score_valid") is True
        and row.get("scoring_canonical_archetype_id")
        and stage_court_score_status is not None
        and stage_court_score_status not in ("FINAL", "FINAL_WITH_NONMATERIAL_GAPS")
    ):
        reasons.append("non_final_agentic_stage_court_score_status")
    if not reasons and acceptance_status != "accepted_operational_stage":
        reasons.append(acceptance_status)
    return list(dict.fromkeys(reasons))


_EVIDENCE_FAMILY_ROW_KEYS = (
    "cross_evidence_family_count",
    "evidence_family_price",
    "evidence_family_financial_actual",
    "evidence_family_disclosure",
    "evidence_family_research_report",
    "evidence_family_consensus",
    "evidence_family_consensus_revision",
    "evidence_family_news",
    "evidence_family_consensus_proxy",
    "evidence_family_consensus_structured",
    "evidence_family_consensus_revision_proxy",
    "evidence_family_search_snippet_news",
)


def _evidence_family_row(row: Mapping[str, Any]) -> Mapping[str, Any]:
    material_gap_missing = _missing_evidence_families_from_material_gaps(row)
    explicit_missing = list(row.get("evidence_family_missing_families") or ())
    missing_families = list(dict.fromkeys((*explicit_missing, *material_gap_missing)))
    proxy_present_families = _evidence_family_proxy_present_families(row)
    proxy_only_gap_families = _independent_missing_but_proxy_present_families(
        row,
        missing_families=missing_families,
        proxy_present_families=proxy_present_families,
    )
    return {
        **{key: row.get(key) for key in _EVIDENCE_FAMILY_ROW_KEYS},
        "evidence_family_present_families": list(row.get("evidence_family_present_families") or ()),
        "evidence_family_missing_families": missing_families,
        "evidence_family_missing_family_gap_summaries": _evidence_family_missing_gap_summaries(row),
        "evidence_family_proxy_present_families": proxy_present_families,
        "evidence_family_independent_missing_but_proxy_present_families": proxy_only_gap_families,
        "evidence_family_independent_missing_but_proxy_present_summaries": [
            (
                f"{family} independent evidence family missing while "
                f"{_proxy_family_for_independent_family(family)} is present"
            )
            for family in proxy_only_gap_families
        ],
    }


def _evidence_family_proxy_present_families(row: Mapping[str, Any]) -> list[str]:
    families = [str(value) for value in row.get("evidence_family_proxy_present_families") or () if str(value)]
    for proxy_family, diagnostic_key in (
        ("consensus_proxy", "evidence_family_consensus_proxy"),
        ("consensus_revision_proxy", "evidence_family_consensus_revision_proxy"),
        ("search_snippet_news", "evidence_family_search_snippet_news"),
    ):
        if _family_diagnostic_present(row.get(diagnostic_key)):
            families.append(proxy_family)
    return list(dict.fromkeys(families))


def _independent_missing_but_proxy_present_families(
    row: Mapping[str, Any],
    *,
    missing_families: Sequence[str],
    proxy_present_families: Sequence[str],
) -> list[str]:
    missing = {str(family) for family in missing_families}
    proxies = {str(family) for family in proxy_present_families}
    findings: list[str] = []
    for family in ("consensus", "consensus_revision"):
        if family not in missing:
            continue
        if _family_diagnostic_present(row.get(f"evidence_family_{family}")):
            continue
        proxy_family = _proxy_family_for_independent_family(family)
        if proxy_family in proxies:
            findings.append(family)
    return findings


def _proxy_family_for_independent_family(family: str) -> str:
    if family == "consensus_revision":
        return "consensus_revision_proxy"
    return f"{family}_proxy"


def _missing_evidence_families_from_material_gaps(row: Mapping[str, Any]) -> tuple[str, ...]:
    families: list[str] = []
    for text in _evidence_family_missing_gap_summaries(row):
        lowered = text.casefold()
        for family in (
            "price",
            "financial_actual",
            "disclosure",
            "research_report",
            "consensus_revision",
            "consensus",
            "news",
        ):
            if re.search(rf"(?<![a-z0-9_]){re.escape(family)}(?![a-z0-9_])", lowered):
                families.append(family)
    return tuple(dict.fromkeys(families))


def _evidence_family_missing_gap_summaries(row: Mapping[str, Any]) -> list[str]:
    findings: list[str] = []
    for value in tuple(row.get("material_score_gap_unresolved_gaps") or ()) + tuple(
        row.get("post_score_gap_unresolved_gaps") or ()
    ):
        text = str(value or "").strip()
        if not text:
            continue
        lowered = text.casefold()
        if "missing independent evidence families" in lowered or "missing evidence families" in lowered:
            findings.append(text)
    return list(dict.fromkeys(findings))[:20]


def _structured_consensus_selected_without_family_signal_summaries(
    row: Mapping[str, Any],
    *,
    family: str,
) -> list[str]:
    family_key = f"evidence_family_{family}"
    if _family_diagnostic_present(row.get(family_key)):
        return []
    findings: list[str] = []
    for plan in row.get("post_score_gap_source_route_plans") or ():
        if not isinstance(plan, Mapping):
            continue
        sources = (
            *_string_list(plan.get("selected_source_family_ids")),
            *_string_list(plan.get("selected_candidate_urls")),
        )
        matched_sources = tuple(
            source for source in sources if _is_structured_consensus_source_family(source, family=family)
        )
        if not matched_sources:
            continue
        findings.append(
            f"structured {family} source selected but evidence family signal missing:"
            f" task_id={plan.get('task_id')};"
            f" primitive_gap={plan.get('primitive_gap')};"
            f" selected_sources={list(dict.fromkeys(matched_sources))}"
        )
    return list(dict.fromkeys(findings))[:20]


def _family_diagnostic_present(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return float(value) > 0.0
    if value in (None, ""):
        return False
    try:
        return float(str(value)) > 0.0
    except ValueError:
        return str(value).strip().casefold() in {"true", "yes", "present"}


def _is_structured_consensus_source_family(value: Any, *, family: str) -> bool:
    text = str(value or "").strip().casefold()
    if "feature://" not in text:
        return False
    if family == "consensus_revision":
        return "/consensus_revision/" in text
    if family == "consensus":
        return "/consensus/" in text and "/consensus_revision/" not in text
    return False


def _row_query_origins(row: Mapping[str, Any]) -> list[str]:
    explicit_origins = [str(value) for value in row.get("post_score_gap_query_origins") or () if str(value).strip()]
    if explicit_origins:
        return explicit_origins
    origins: list[str] = []
    for plan in row.get("post_score_gap_source_route_plans") or ():
        if not isinstance(plan, Mapping):
            continue
        origin = str(plan.get("query_origin") or "").strip()
        if origin:
            origins.append(origin)
    return origins


def _row_uses_deterministic_fallback_query(row: Mapping[str, Any]) -> bool:
    if bool(row.get("post_score_gap_deterministic_fallback_query_used")):
        return True
    for plan in row.get("post_score_gap_source_route_plans") or ():
        if not isinstance(plan, Mapping):
            continue
        if bool(plan.get("deterministic_fallback_query_used")):
            return True
    return any("deterministic_fallback" in origin.casefold() for origin in _row_query_origins(row))


def _row_has_score_gap_route_plan_missing_query_origin(row: Mapping[str, Any]) -> bool:
    return bool(_row_query_origin_missing_summaries(row))


def _row_query_origin_missing_summaries(row: Mapping[str, Any]) -> list[str]:
    findings: list[str] = []
    for plan in row.get("post_score_gap_source_route_plans") or ():
        if not isinstance(plan, Mapping):
            continue
        if str(plan.get("query_origin") or "").strip():
            continue
        if not (plan.get("query") or plan.get("selected_source_family_ids") or plan.get("selected_candidate_urls")):
            continue
        findings.append(
            "post-score gap route plan missing query_origin:"
            f" task_id={plan.get('task_id')};"
            f" primitive_gap={plan.get('primitive_gap')};"
            f" query={plan.get('query')}"
        )
    return list(dict.fromkeys(findings))[:20]


def _pending_reason_group(row: Mapping[str, Any], *, acceptance_status: str) -> str | None:
    if acceptance_status != "pending_not_operational_stage":
        return None
    if _row_has_provider_quota_failure(row):
        return "provider_quota_exhausted"
    blocked_reason = str(row.get("score_blocked_reason") or "").strip()
    progress_reason = str(row.get("post_score_gap_progress_reason") or "").strip()
    expansion_status = str(row.get("post_score_gap_expansion_status") or "").strip()
    rejection_reasons = tuple(str(value) for value in row.get("post_score_gap_rejection_reasons") or ())
    evidence_progress = bool(
        row.get("post_score_gap_primitive_state_changed")
        or row.get("post_score_gap_score_contribution_changed")
        or progress_reason == "score_gap_evidence_progress_without_score_state_change"
    )
    if blocked_reason == "score_gap_material_gaps_pending" or evidence_progress:
        return "score_gap_evidence_progress_pending"
    if blocked_reason == "score_gap_no_progress" or progress_reason.startswith("score_gap_"):
        if progress_reason == "score_gap_new_claims_without_accepted_mappings":
            return "score_gap_new_claims_without_accepted_mappings"
        return "score_gap_no_progress"
    if _row_has_theme_review_timeout(row):
        return "theme_review_timeout_pending"
    if _row_has_agentic_provider_failure(row):
        return "provider_failure"
    if (
        expansion_status == "budget_blocked"
        or blocked_reason == "score_gap_budget_blocked"
        or any("budget_exhausted" in reason or "budget_blocked" in reason for reason in rejection_reasons)
    ):
        return "score_gap_budget_blocked"
    if blocked_reason.startswith("score_gap_") or expansion_status in {"no_progress", "round_limit_reached"}:
        return "score_gap_pending"
    if row.get("material_score_gap_unresolved_gaps"):
        return "material_gap_pending"
    if _row_has_theme_route_provider_failure(row):
        return "provider_failure"
    return "pending_invalid_score"


def _row_has_agentic_provider_failure(row: Mapping[str, Any]) -> bool:
    status_fields = (
        row.get("agentic_evidence_status"),
        row.get("post_score_gap_new_trace_status"),
    )
    if any(str(value or "").strip() == "provider_error" for value in status_fields):
        return True
    if int(row.get("post_score_gap_new_trace_error_count") or 0) > 0:
        return True
    error_text = " ".join(str(item) for item in row.get("post_score_gap_new_trace_errors") or ())
    error_text = f"{error_text} {' '.join(str(item) for item in row.get('agentic_evidence_errors') or ())}".casefold()
    return "provider_error" in error_text or "usage_limit" in error_text


def _row_has_theme_route_provider_failure(row: Mapping[str, Any]) -> bool:
    if str(row.get("theme_route_status") or "").strip() != "provider_error":
        return False
    return not _row_has_theme_review_timeout(row)


def _row_has_theme_review_timeout(row: Mapping[str, Any]) -> bool:
    route_status = str(row.get("theme_route_status") or "").strip()
    review_status = str(row.get("theme_evidence_review_status") or "").strip()
    if route_status != "provider_error" and review_status != "provider_error":
        return False
    blocked_reason = " ".join(
        str(value or "")
        for value in (
            row.get("theme_evidence_review_blocked_reason"),
            row.get("theme_route_blocked_reason"),
            row.get("score_blocked_reason"),
        )
    ).casefold()
    if "timeout" not in blocked_reason:
        return False
    return True


def _cash_bridge_gap_summaries(row: Mapping[str, Any]) -> list[str]:
    gaps: list[str] = []
    for value in tuple(row.get("material_score_gap_unresolved_gaps") or ()) + tuple(
        row.get("post_score_gap_unresolved_gaps") or ()
    ):
        text = str(value or "").strip()
        if not text:
            continue
        if _text_is_cash_bridge_pending_gap(text):
            gaps.append(text)
    return list(dict.fromkeys(gaps))[:20]


def _text_is_cash_bridge_pending_gap(text: str) -> bool:
    marker = str(text or "").casefold()
    explicit_cash_gap_markers = (
        "agentic primitive gap:cash_or_revision_conversion",
        "selected_fcf_source_missing",
        "source-backed fcf",
        "source-backed cash",
        "source-backed current claim for cash_or_revision_conversion",
    )
    return any(token in marker for token in explicit_cash_gap_markers)


def _text_is_cash_bridge_gap(text: str) -> bool:
    marker = text.casefold()
    return any(
        token in marker
        for token in (
            "cash_or_revision_conversion",
            "selected_fcf_source_missing",
            "fcf",
            "free cash flow",
            "operating-cash-flow",
            "operating cash flow",
            "cash-flow",
            "cash flow",
            "cash conversion",
            "현금흐름",
            "잉여현금",
        )
    )


def _cash_bridge_source_quorum_without_signal_summaries(row: Mapping[str, Any]) -> list[str]:
    findings: list[str] = []
    for plan in row.get("post_score_gap_source_route_plans") or ():
        if not isinstance(plan, Mapping):
            continue
        if not _route_plan_is_cash_bridge(plan):
            continue
        stop_reason = str(plan.get("stop_reason") or "").strip()
        if not stop_reason.startswith("source_quorum_contract"):
            continue
        if _route_plan_has_target_scoped_cash_bridge_source_signal(row, plan):
            continue
        source_families = _string_list(plan.get("selected_source_family_ids"))
        findings.append(
            "cash bridge source quorum without target-scoped cash/FCF signal:"
            f" task_id={plan.get('task_id')};"
            f" primitive_gap={plan.get('primitive_gap')};"
            f" stop_reason={stop_reason};"
            f" selected_source_family_ids={source_families}"
        )
    return list(dict.fromkeys(findings))[:20]


def _route_plan_is_cash_bridge(plan: Mapping[str, Any]) -> bool:
    return any(
        _text_is_cash_bridge_gap(str(plan.get(key) or ""))
        for key in (
            "primitive_gap",
            "stop_condition",
            "fallback_policy",
        )
    )


def _route_plan_selected_source_text(plan: Mapping[str, Any]) -> str:
    values: list[str] = []
    for key in (
        "selected_source_family_ids",
        "selected_candidate_ids",
        "selected_candidate_titles",
        "selected_candidate_snippets",
        "selected_candidate_urls",
    ):
        values.extend(_string_list(plan.get(key)))
    return " ".join(values)


def _route_plan_has_target_scoped_cash_bridge_source_signal(row: Mapping[str, Any], plan: Mapping[str, Any]) -> bool:
    explicit_counts = _numeric_list(plan.get("selected_candidate_target_scoped_cash_bridge_signal_counts"))
    explicit_present = _bool_list(plan.get("selected_candidate_target_scoped_cash_bridge_signal_present"))
    if explicit_counts or explicit_present:
        return any(value > 0 for value in explicit_counts) or any(explicit_present)

    selected_text = _route_plan_selected_source_text(plan)
    if not _text_has_cash_bridge_source_signal(selected_text):
        return False
    if _route_plan_has_structured_target_financial_actual(row, plan):
        return True

    aliases = _row_target_aliases(row)
    if not aliases:
        return True
    for text in _route_plan_selected_candidate_texts(plan):
        if _text_has_target_scoped_cash_bridge_signal(text, aliases):
            return True
    return False


def _route_plan_has_structured_target_financial_actual(row: Mapping[str, Any], plan: Mapping[str, Any]) -> bool:
    symbol = str(row.get("symbol") or "").strip().casefold()
    if not symbol:
        return False
    target_prefixes = (
        f"feature://{symbol}/financial_actual/",
        f"feature://{symbol}/xbrl/",
        f"opendart://{symbol}/",
    )
    for value in (
        *_string_list(plan.get("selected_source_family_ids")),
        *_string_list(plan.get("selected_candidate_urls")),
    ):
        text = str(value or "").strip().casefold()
        if any(text.startswith(prefix) for prefix in target_prefixes):
            return True
    return False


def _route_plan_selected_candidate_texts(plan: Mapping[str, Any]) -> list[str]:
    texts: list[str] = []
    for key in (
        "selected_source_family_ids",
        "selected_candidate_ids",
        "selected_candidate_titles",
        "selected_candidate_snippets",
        "selected_candidate_urls",
    ):
        texts.extend(_string_list(plan.get(key)))
    if not texts:
        selected_text = _route_plan_selected_source_text(plan)
        if selected_text:
            texts.append(selected_text)
    return texts


def _text_has_target_scoped_cash_bridge_signal(text: str, aliases: Sequence[str]) -> bool:
    for segment in _cash_bridge_scope_segments(text):
        if _text_has_cash_bridge_source_signal(segment) and _text_has_any_alias(segment, aliases):
            return True
    return False


def _cash_bridge_scope_segments(text: str) -> list[str]:
    raw = str(text or "")
    pieces = re.split(r"[\n\r]|(?<=[.!?。！？])\s+|[;；]", raw)
    return [piece.strip() for piece in pieces if piece.strip()]


def _row_target_aliases(row: Mapping[str, Any]) -> tuple[str, ...]:
    aliases = [
        str(row.get("company_name") or "").strip(),
        str(row.get("company") or "").strip(),
        str(row.get("symbol") or "").strip(),
    ]
    return tuple(dict.fromkeys(alias for alias in aliases if alias))


def _text_has_any_alias(text: str, aliases: Sequence[str]) -> bool:
    marker = str(text or "").casefold()
    compact_marker = re.sub(r"\s+", "", marker)
    for alias in aliases:
        normalized = str(alias or "").strip().casefold()
        if not normalized:
            continue
        if normalized in marker:
            return True
        compact_alias = re.sub(r"\s+", "", normalized)
        if compact_alias and compact_alias in compact_marker:
            return True
    return False


def _numeric_list(value: Any) -> list[float]:
    values = value if isinstance(value, Sequence) and not isinstance(value, str) else (value,)
    numbers: list[float] = []
    for item in values:
        try:
            numbers.append(float(item))
        except (TypeError, ValueError):
            continue
    return numbers


def _bool_list(value: Any) -> list[bool]:
    values = value if isinstance(value, Sequence) and not isinstance(value, str) else (value,)
    flags: list[bool] = []
    for item in values:
        if isinstance(item, bool):
            flags.append(item)
        elif isinstance(item, (int, float)):
            flags.append(float(item) > 0.0)
        elif isinstance(item, str):
            flags.append(item.strip().casefold() in {"1", "true", "yes", "present"})
    return flags


def _string_list(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, Sequence):
        return [str(item) for item in value if str(item).strip()]
    if value is None:
        return []
    return [str(value)]


def _text_has_cash_bridge_source_signal(text: str) -> bool:
    return text_has_cash_bridge_signal(text)


def _row_has_provider_quota_failure(row: Mapping[str, Any]) -> bool:
    if row.get("_phase_log_provider_quota_exhausted"):
        return True
    error_text = " ".join(str(item) for item in row.get("post_score_gap_new_trace_errors") or ())
    error_text = f"{error_text} {' '.join(str(item) for item in row.get('agentic_evidence_errors') or ())}".casefold()
    return _text_has_provider_quota_failure(error_text)


def _text_has_provider_quota_failure(text: str) -> bool:
    error_text = str(text or "").casefold()
    quota_needles = (
        "usage_limit",
        "usage limit",
        "hit your usage limit",
        "quota",
        "rate limit",
        "too many requests",
        "try again at",
    )
    return any(needle in error_text for needle in quota_needles)


def _deprecated_row(summary: Mapping[str, Any]) -> Mapping[str, Any]:
    claim_ratio_missing = summary.get("claim_backed_component_ratio") is None
    contract_missing = summary.get("canonical_archetype_id") is None
    status = (
        "deprecated_legacy_result_not_accepted"
        if claim_ratio_missing or contract_missing
        else "deprecated_result_requires_manual_review"
    )
    return {
        "symbol": summary.get("symbol"),
        "company": summary.get("company"),
        "stage": summary.get("stage"),
        "visible_score": summary.get("visible_score"),
        "score_valid": summary.get("score_valid"),
        "canonical_archetype_id": summary.get("canonical_archetype_id"),
        "claim_backed_component_ratio": summary.get("claim_backed_component_ratio"),
        "red_team_has_hard_break": summary.get("red_team_has_hard_break"),
        "red_team_status": summary.get("red_team_status"),
        "acceptance_status": status,
        "production_score_fixture": False,
        "production_stage_fixture": False,
        "rejection_reason": (
            "missing canonical_archetype_id or claim_backed_component_ratio; legacy 63-point result is not accepted"
        ),
    }


def _read_json_mapping(path: Path) -> Mapping[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, Mapping):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def _read_smoke_run_log(path: Path) -> Mapping[str, Any]:
    data = dict(_read_json_mapping(path))
    data["_source_run_log_path"] = str(path)
    phase_log_path = _phase_log_path_for_run_log(path)
    if phase_log_path.exists():
        data["_source_phase_log_path"] = str(phase_log_path)
    if phase_log_path.exists():
        quota_symbols = _phase_log_provider_quota_symbols(phase_log_path)
        if quota_symbols:
            data["_phase_log_provider_quota_exhausted_symbols"] = sorted(quota_symbols)
        mapper_metrics = _phase_log_agentic_mapper_metrics_by_symbol(phase_log_path)
        if mapper_metrics:
            data["_phase_log_agentic_mapper_metrics_by_symbol"] = mapper_metrics
    return data


def _source_run_log_paths(smoke_run_logs: Sequence[Mapping[str, Any]]) -> list[str]:
    paths = []
    for run_log in smoke_run_logs:
        path = run_log.get("_source_run_log_path")
        if path is not None:
            paths.append(str(path))
    return paths


def _phase_log_path_for_run_log(path: Path) -> Path:
    name = path.name
    if name.endswith("_run_log.json"):
        return path.with_name(f"{name[:-len('_run_log.json')]}_phase_log.jsonl")
    return path.with_name("phase_log.jsonl")


def _phase_log_provider_quota_symbols(path: Path) -> set[str]:
    symbols: set[str] = set()
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not _text_has_provider_quota_failure(line):
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(row, Mapping):
            continue
        symbol = str(row.get("symbol") or "").strip()
        if symbol:
            symbols.add(symbol)
    return symbols


def _phase_log_agentic_mapper_metrics_by_symbol(path: Path) -> Mapping[str, Mapping[str, Any]]:
    metrics_by_symbol: dict[str, dict[str, Any]] = {}
    score_gap_active_symbols: set[str] = set()
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(event, Mapping):
            continue
        symbol = str(event.get("symbol") or "").strip()
        if not symbol:
            continue
        phase = str(event.get("phase") or "").strip()
        if phase == "post_score_gap_web_research_start":
            score_gap_active_symbols.add(symbol)
            continue
        if phase not in {
            "agentic_evidence_mapping_prefilter_complete",
            "agentic_evidence_mapping_chunk_complete",
            "agentic_evidence_mapping_single_complete",
            "agentic_evidence_mapping_chunk_empty_retry_start",
            "agentic_evidence_mapping_single_empty_retry_start",
            "agentic_evidence_mapping_chunk_empty_retry_recovered",
            "agentic_evidence_mapping_single_empty_retry_recovered",
        }:
            continue
        metrics = metrics_by_symbol.setdefault(symbol, _empty_phase_log_mapper_metrics())
        _record_phase_log_mapper_event(metrics, phase, event, prefix="")
        if symbol in score_gap_active_symbols:
            _record_phase_log_mapper_event(metrics, phase, event, prefix="post_score_gap_new_trace_")
    return metrics_by_symbol


def _empty_phase_log_mapper_metrics() -> dict[str, Any]:
    return {
        "agentic_evidence_mapping_prefilter_original_task_count": 0,
        "agentic_evidence_mapping_prefilter_filtered_task_count": 0,
        "agentic_evidence_mapping_prefilter_skipped_input_count": 0,
        "agentic_evidence_mapping_prefilter_fallback_full_map_count": 0,
        "agentic_evidence_mapping_prefilter_fallback_full_map_summaries": [],
        "agentic_evidence_mapping_empty_output_count": 0,
        "agentic_evidence_mapping_empty_output_retry_count": 0,
        "agentic_evidence_mapping_empty_output_recovered_count": 0,
        "agentic_evidence_mapping_empty_output_summaries": [],
        "agentic_evidence_mapping_empty_output_retry_summaries": [],
        "post_score_gap_new_trace_mapping_prefilter_original_task_count": 0,
        "post_score_gap_new_trace_mapping_prefilter_filtered_task_count": 0,
        "post_score_gap_new_trace_mapping_prefilter_skipped_input_count": 0,
        "post_score_gap_new_trace_mapping_prefilter_fallback_full_map_count": 0,
        "post_score_gap_new_trace_mapping_prefilter_fallback_full_map_summaries": [],
        "post_score_gap_new_trace_mapping_empty_output_count": 0,
        "post_score_gap_new_trace_mapping_empty_output_retry_count": 0,
        "post_score_gap_new_trace_mapping_empty_output_recovered_count": 0,
        "post_score_gap_new_trace_mapping_empty_output_summaries": [],
        "post_score_gap_new_trace_mapping_empty_output_retry_summaries": [],
    }


def _record_phase_log_mapper_event(
    metrics: dict[str, Any],
    phase: str,
    event: Mapping[str, Any],
    *,
    prefix: str,
) -> None:
    if prefix:
        prefilter_base = f"{prefix}mapping_prefilter"
        empty_base = f"{prefix}mapping_empty_output"
    else:
        prefilter_base = "agentic_evidence_mapping_prefilter"
        empty_base = "agentic_evidence_mapping_empty_output"

    if phase == "agentic_evidence_mapping_prefilter_complete":
        metrics[f"{prefilter_base}_original_task_count"] += int(
            event.get("mapping_prefilter_original_task_count") or 0
        )
        metrics[f"{prefilter_base}_filtered_task_count"] += int(
            event.get("mapping_prefilter_filtered_task_count") or 0
        )
        metrics[f"{prefilter_base}_skipped_input_count"] += int(
            event.get("mapping_prefilter_skipped_input_count") or 0
        )
        metrics[f"{prefilter_base}_fallback_full_map_count"] += int(
            event.get("mapping_prefilter_fallback_full_map_count") or 0
        )
        summaries = metrics[f"{prefilter_base}_fallback_full_map_summaries"]
        if isinstance(summaries, list) and len(summaries) < 20:
            document_id = str(event.get("document_id") or "").strip()
            for row in event.get("mapping_prefilter_reason_by_claim") or ():
                if not isinstance(row, Mapping) or not row.get("fallback_full_map"):
                    continue
                summaries.append(
                    "fallback_full_map"
                    f"|document={document_id or 'unknown'}"
                    f"|claim={row.get('claim_id')}"
                    f"|reason={row.get('reason')}"
                )
                if len(summaries) >= 20:
                    break
        return

    if phase in {
        "agentic_evidence_mapping_chunk_empty_retry_start",
        "agentic_evidence_mapping_single_empty_retry_start",
    }:
        metrics[f"{empty_base}_retry_count"] += 1
        summaries = metrics[f"{empty_base}_retry_summaries"]
        if isinstance(summaries, list) and len(summaries) < 20:
            summaries.append(_phase_log_mapper_retry_summary(phase, event))
        return

    if phase in {
        "agentic_evidence_mapping_chunk_empty_retry_recovered",
        "agentic_evidence_mapping_single_empty_retry_recovered",
    }:
        metrics[f"{empty_base}_recovered_count"] += 1
        summaries = metrics[f"{empty_base}_retry_summaries"]
        if isinstance(summaries, list) and len(summaries) < 20:
            summaries.append(_phase_log_mapper_retry_summary(phase, event))
        return

    mapping_input_count = int(event.get("mapping_input_count") or 0)
    mapping_output_count = int(event.get("mapping_output_count") or 0)
    if mapping_input_count <= 0 or mapping_output_count != 0:
        return
    metrics[f"{empty_base}_count"] += 1
    summaries = metrics[f"{empty_base}_summaries"]
    if isinstance(summaries, list) and len(summaries) < 20:
        summaries.append(
            _phase_log_mapper_empty_output_summary(
                phase,
                event,
                mapping_input_count=mapping_input_count,
            )
        )


def _phase_log_mapper_retry_summary(phase: str, event: Mapping[str, Any]) -> str:
    return (
        "empty_mapper_retry"
        f"|phase={phase}"
        f"|document={event.get('document_id') or 'unknown'}"
        f"|round={event.get('round_index')}"
        f"|retry={event.get('retry_index')}"
        f"|chunk={event.get('chunk_index')}"
        f"|item={event.get('item_index')}"
        f"|mapping_input_count={event.get('mapping_input_count')}"
        f"|mapping_output_count={event.get('mapping_output_count')}"
    )


def _phase_log_mapper_empty_output_summary(
    phase: str,
    event: Mapping[str, Any],
    *,
    mapping_input_count: int,
) -> str:
    return (
        "empty_mapper_output"
        f"|phase={phase}"
        f"|document={event.get('document_id') or 'unknown'}"
        f"|round={event.get('round_index')}"
        f"|chunk={event.get('chunk_index')}"
        f"|item={event.get('item_index')}"
        f"|mapping_input_count={mapping_input_count}"
    )


def _apply_phase_log_mapper_metrics(row: dict[str, Any], metrics: Mapping[str, Any]) -> None:
    for key, value in metrics.items():
        if key not in row or row.get(key) in (None, (), [], 0):
            row[key] = tuple(value) if isinstance(value, list) else value


def _write_json(path: Path, data: Mapping[str, Any]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def _render_acceptance_markdown(manifest: Mapping[str, Any]) -> str:
    lines = ["# Evidence OS Live Smoke Acceptance", ""]
    summary = manifest.get("summary")
    if isinstance(summary, Mapping):
        lines.append("## Summary")
        for key in sorted(summary):
            lines.append(f"- {key}: `{summary[key]}`")
        lines.append("")
    lines.append("## Current Smoke Rows")
    for row in manifest.get("rows") or ():
        if isinstance(row, Mapping):
            reasons = ",".join(_string_list(row.get("acceptance_block_reasons"))) or "none"
            stage_zero_diagnostics = " | ".join(
                _string_list(row.get("stage_zero_not_operational_diagnostics"))[:2]
            ) or "none"
            lines.append(
                f"- `{row.get('symbol')}`: `{row.get('acceptance_status')}`, "
                f"pending=`{row.get('pending_reason_group')}`, stage=`{row.get('stage')}`, "
                f"reasons=`{reasons}`, "
                f"stage_zero_diagnostics=`{stage_zero_diagnostics}`, "
                f"legacy_active=`{row.get('legacy_parser_score_claim_without_v2_count')}`, "
                f"legacy_quarantined=`{row.get('legacy_parser_score_claim_without_v2_quarantined_count')}`"
            )
    lines.append("")
    lines.append("## Deprecated Rows")
    for row in manifest.get("deprecated_rows") or ():
        if isinstance(row, Mapping):
            lines.append(
                f"- `{row.get('symbol')}`: `{row.get('acceptance_status')}`, "
                f"legacy_stage=`{row.get('stage')}`, visible_score=`{row.get('visible_score')}`"
            )
    lines.append("")
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    smoke_run_logs = args.smoke_run_log if args.smoke_run_log is not None else list(DEFAULT_SMOKE_RUN_LOGS)
    deprecated_summaries = (
        args.deprecated_summary if args.deprecated_summary is not None else list(DEFAULT_DEPRECATED_SUMMARIES)
    )
    paths = run_live_smoke_acceptance(
        smoke_run_log_paths=smoke_run_logs,
        deprecated_summary_paths=deprecated_summaries,
        output_directory=args.output_directory,
        output_prefix=args.output_prefix,
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "DEFAULT_DEPRECATED_SUMMARIES",
    "DEFAULT_OUTPUT_DIRECTORY",
    "DEFAULT_SMOKE_RUN_LOGS",
    "build_arg_parser",
    "build_live_smoke_acceptance_manifest",
    "main",
    "run_live_smoke_acceptance",
]
