"""Independent P9 audit for the V2.1 fresh-session efficiency receipts."""

from __future__ import annotations

import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

from ..ids import canonical_hash


DEFAULT_COMPARISON_PATH = Path(
    "docs/operational/e2r_pro_first_v2_1/fresh_session_comparison.json"
)

EXPECTED_FRESH_RECEIPTS = {
    "C06_HBM_MEMORY_CUSTOMER_CAPACITY": Path(
        "docs/operational/e2r_pro_first_v2_1/"
        "p7_c06_fresh_initial_success_receipt.json"
    ),
    "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD": Path(
        "docs/operational/e2r_pro_first_v2_1/"
        "p8_c17_fresh_initial_success_receipt_r6.json"
    ),
    "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION": Path(
        "docs/operational/e2r_pro_first_v2_1/"
        "p8_c28_fresh_initial_success_receipt_r3.json"
    ),
}

EXPECTED_OLD_FREEZE_PATH = Path(
    "docs/operational/e2r_pro_first_v2_1/old_run_freeze_summary.json"
)
EXPECTED_OLD_TAXONOMY_PATH = Path(
    "docs/operational/e2r_pro_first_v2_1/old_run_rejection_taxonomy.json"
)

REQUIRED_ZERO_COUNTER_KEYS = (
    "old_conversation_new_submit_count",
    "old_fact_in_fresh_packet_count",
    "old_score_stage_in_fresh_packet_count",
    "local_normalizable_sent_to_pro_count",
    "source_representation_sent_to_pro_count",
    "full_dossier_repair_response_required_count",
    "multi_source_atomic_fact_count",
    "derived_metric_mixed_fact_count",
    "tracking_url_fact_count",
    "question_unbound_material_fact_count",
    "repair_deferred_batch_count",
    "second_repair_pass_count",
    "partial_score_published_count",
)

REQUIRED_RECEIPT_FIELDS = (
    "target_id",
    "company_name",
    "as_of_date",
    "archetype_id",
    "fresh_session_id",
    "job_id",
    "run_id",
    "research_pass_id",
    "conversation_id",
    "submit_count",
    "capture_count",
    "automatic_resubmit_count",
    "new_conversation",
    "source_document_count",
    "all_fact_count",
    "initial_material_candidate_count",
    "accepted_material_count",
    "post_preflight_acceptance_ratio",
    "accepted_fact_candidate_count",
    "mandatory_question_count",
    "mandatory_question_covered_count",
    "unresolved_gap_count",
    "genuine_semantic_repair_candidate_count",
    "repair_pass_count",
    "initial_prompt_char_count",
    "initial_response_char_count",
    "initial_research_elapsed_seconds",
    "total_elapsed_seconds",
    "query_count",
    "search_count",
    "source_fetch_count",
    "score_authority",
    "stage_authority",
    "publication_withheld",
    "initial_gate_status",
)

AGGREGATE_SUM_FIELDS = (
    "source_document_count",
    "all_fact_count",
    "initial_material_candidate_count",
    "accepted_material_count",
    "accepted_fact_candidate_count",
    "mandatory_question_count",
    "mandatory_question_covered_count",
    "unresolved_gap_count",
    "genuine_semantic_repair_candidate_count",
    "repair_pass_count",
    "initial_prompt_char_count",
    "initial_response_char_count",
    "initial_research_elapsed_seconds",
    "total_elapsed_seconds",
    "query_count",
    "search_count",
    "source_fetch_count",
)


def _repo_json(repo_root: Path, relative_path: Path) -> Mapping[str, Any]:
    root = repo_root.resolve()
    path = (root / relative_path).resolve()
    if path != root and root not in path.parents:
        raise ValueError(f"receipt path escapes repository root: {relative_path}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError(f"JSON receipt must be an object: {relative_path}")
    return payload


def _fresh_projection(
    receipt_path: Path, receipt: Mapping[str, Any]
) -> dict[str, Any]:
    return {
        "receipt_path": receipt_path.as_posix(),
        **{field: receipt.get(field) for field in REQUIRED_RECEIPT_FIELDS},
    }


def _old_projection(
    freeze: Mapping[str, Any], taxonomy: Mapping[str, Any]
) -> dict[str, Any]:
    aggregates = taxonomy.get("aggregates", {})
    if not isinstance(aggregates, Mapping):
        aggregates = {}
    root_counts = aggregates.get("root_cause_class_counts", {})
    if not isinstance(root_counts, Mapping):
        root_counts = {}
    effective = freeze.get("effective_dossier", {})
    if not isinstance(effective, Mapping):
        effective = {}
    final_verification = freeze.get("final_source_verification", {})
    if not isinstance(final_verification, Mapping):
        final_verification = {}
    return {
        "freeze_receipt_path": EXPECTED_OLD_FREEZE_PATH.as_posix(),
        "taxonomy_receipt_path": EXPECTED_OLD_TAXONOMY_PATH.as_posix(),
        "disposition": taxonomy.get("old_run_disposition"),
        "job_id": freeze.get("job_id"),
        "run_id": freeze.get("run_id"),
        "conversation_id": freeze.get("conversation_id"),
        "initial_submit_count": freeze.get("initial_submit_count_at_freeze"),
        "repair_submit_count": freeze.get("followup_submit_count_at_freeze"),
        "total_submitted_pass_count": freeze.get("submitted_pass_count_at_freeze"),
        "new_submit_count_after_freeze": freeze.get(
            "new_submit_count_after_freeze"
        ),
        "initial_material_candidate_count": freeze.get(
            "initial_material_candidate_count"
        ),
        "initial_accepted_material_count": freeze.get(
            "initial_accepted_material_count"
        ),
        "initial_acceptance_ratio": freeze.get("initial_acceptance_ratio"),
        "initial_acceptance_boundary_status": freeze.get(
            "initial_acceptance_boundary_status"
        ),
        "initial_prompt_char_count": freeze.get("initial_prompt_char_count"),
        "initial_response_char_count": freeze.get("initial_response_char_count"),
        "total_prompt_char_count": freeze.get("total_prompt_char_count"),
        "total_response_char_count": freeze.get("total_response_char_count"),
        "total_character_telemetry_status": freeze.get(
            "total_character_telemetry_status"
        ),
        "durable_run_elapsed_seconds": freeze.get("durable_run_elapsed_seconds"),
        "initial_prompt_defect_rejection_count": root_counts.get(
            "INITIAL_PROMPT_OUTPUT_DEFECT"
        ),
        "local_or_verifier_rejection_count": root_counts.get(
            "LOCAL_NORMALIZATION_OR_VERIFIER_DEFECT"
        ),
        "genuine_semantic_rejection_count": root_counts.get(
            "GENUINE_SEMANTIC_OR_SOURCE_DEFECT"
        ),
        "total_rejection_count": aggregates.get("total_rejection_count"),
        "final_effective_fact_count": effective.get("fact_count"),
        "final_verified_fact_count": final_verification.get(
            "accepted_fact_candidate_count"
        ),
        "final_question_row_count": effective.get("question_count"),
        "terminal_question_closure_proven": freeze.get(
            "terminal_question_closure_proven"
        ),
        "unresolved_repair_packet_count": freeze.get(
            "unresolved_repair_packet_count"
        ),
        "score_authority": freeze.get("score_authority"),
        "stage_authority": freeze.get("stage_authority"),
        "publication_withheld": freeze.get("publication_withheld"),
    }


def _fresh_aggregates(rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    totals: dict[str, Any] = {}
    for field in AGGREGATE_SUM_FIELDS:
        totals[field] = round(sum(float(row[field]) for row in rows), 6)
        if field not in {
            "initial_research_elapsed_seconds",
            "total_elapsed_seconds",
        }:
            totals[field] = int(totals[field])
    candidates = int(totals["initial_material_candidate_count"])
    accepted = int(totals["accepted_material_count"])
    totals.update(
        {
            "fresh_conversation_count": len(rows),
            "initial_acceptance_ratio": round(accepted / candidates, 6),
            "total_pro_pass_count": len(rows)
            + int(totals["repair_pass_count"]),
            "terminal_question_closure_proven": False,
        }
    )
    return totals


def audit_fresh_session_comparison(
    repo_root: str | Path, comparison: Mapping[str, Any]
) -> dict[str, Any]:
    """Recompute P9 from tracked source receipts and reject self-asserted totals."""

    root = Path(repo_root).expanduser().resolve()
    issues: list[str] = []
    fresh_rows: list[dict[str, Any]] = []
    receipts: list[Mapping[str, Any]] = []

    for archetype_id, receipt_path in EXPECTED_FRESH_RECEIPTS.items():
        try:
            receipt = _repo_json(root, receipt_path)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            issues.append(f"missing_or_invalid_receipt:{receipt_path}:{exc}")
            continue
        receipts.append(receipt)
        missing = [
            field for field in REQUIRED_RECEIPT_FIELDS if field not in receipt
        ]
        if missing:
            issues.append(
                f"missing_receipt_fields:{archetype_id}:{','.join(missing)}"
            )
        if receipt.get("archetype_id") != archetype_id:
            issues.append(f"archetype_identity_mismatch:{archetype_id}")
        if receipt.get("initial_gate_status") != "PASS":
            issues.append(f"initial_gate_not_passed:{archetype_id}")
        if not str(receipt.get("status", "")).endswith("FRESH_SESSION_PASS"):
            issues.append(f"success_status_missing:{archetype_id}")
        if receipt.get("submit_count") != 1 or receipt.get("capture_count") != 1:
            issues.append(f"single_submit_capture_violation:{archetype_id}")
        if receipt.get("automatic_resubmit_count") != 0:
            issues.append(f"automatic_resubmit_violation:{archetype_id}")
        if receipt.get("new_conversation") is not True:
            issues.append(f"new_conversation_not_proven:{archetype_id}")
        candidates = receipt.get("initial_material_candidate_count")
        accepted = receipt.get("accepted_material_count")
        ratio = receipt.get("post_preflight_acceptance_ratio")
        if (
            not isinstance(candidates, int)
            or isinstance(candidates, bool)
            or candidates <= 0
        ):
            issues.append(f"invalid_initial_candidate_count:{archetype_id}")
        elif not isinstance(accepted, int) or isinstance(accepted, bool):
            issues.append(f"invalid_accepted_material_count:{archetype_id}")
        else:
            expected_ratio = round(accepted / candidates, 6)
            if ratio != expected_ratio:
                issues.append(f"acceptance_ratio_mismatch:{archetype_id}")
            if expected_ratio < 0.8:
                issues.append(f"acceptance_ratio_below_80_percent:{archetype_id}")
        if receipt.get("mandatory_question_count") != receipt.get(
            "mandatory_question_covered_count"
        ):
            issues.append(f"mandatory_question_coverage_failure:{archetype_id}")
        if receipt.get("score_authority") is not False:
            issues.append(f"score_authority_exposed:{archetype_id}")
        if receipt.get("stage_authority") is not False:
            issues.append(f"stage_authority_exposed:{archetype_id}")
        if receipt.get("publication_withheld") is not True:
            issues.append(f"publication_not_withheld:{archetype_id}")
        fresh_rows.append(_fresh_projection(receipt_path, receipt))

    identity_fields = (
        "fresh_session_id",
        "job_id",
        "run_id",
        "research_pass_id",
        "conversation_id",
    )
    for field in identity_fields:
        values = [row.get(field) for row in fresh_rows]
        valid_values = [value for value in values if isinstance(value, str) and value]
        if len(valid_values) != len(values) or len(valid_values) != len(
            set(valid_values)
        ):
            issues.append(f"fresh_identity_not_unique:{field}")

    zero_counters: dict[str, int] = {}
    for key in REQUIRED_ZERO_COUNTER_KEYS:
        values: list[int] = []
        for receipt in receipts:
            value = receipt.get(key)
            if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                issues.append(f"missing_or_invalid_zero_counter:{key}")
                continue
            values.append(value)
        zero_counters[key] = sum(values)
        if zero_counters[key] != 0:
            issues.append(f"nonzero_efficiency_counter:{key}:{zero_counters[key]}")

    try:
        freeze = _repo_json(root, EXPECTED_OLD_FREEZE_PATH)
        taxonomy = _repo_json(root, EXPECTED_OLD_TAXONOMY_PATH)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        issues.append(f"missing_or_invalid_old_receipt:{exc}")
        freeze = {}
        taxonomy = {}
    old_row = _old_projection(freeze, taxonomy)
    if old_row["new_submit_count_after_freeze"] != 0:
        issues.append("old_run_received_submit_after_freeze")
    if old_row["score_authority"] is not False or old_row["stage_authority"] is not False:
        issues.append("old_diagnostic_run_has_score_or_stage_authority")
    if old_row["publication_withheld"] is not True:
        issues.append("old_diagnostic_run_publication_not_withheld")

    aggregates: dict[str, Any] = {}
    if len(fresh_rows) == len(EXPECTED_FRESH_RECEIPTS):
        try:
            aggregates = _fresh_aggregates(fresh_rows)
        except (KeyError, TypeError, ValueError, ZeroDivisionError):
            issues.append("fresh_aggregate_source_metric_invalid")
    if comparison.get("schema_version") != "e2r_pro_fresh_session_comparison_v1":
        issues.append("comparison_schema_version_mismatch")
    if comparison.get("score_parity_allowed") is not False:
        issues.append("score_parity_must_be_prohibited")
    if comparison.get("fresh_runs") != fresh_rows:
        issues.append("fresh_run_projection_mismatch")
    if comparison.get("old_run") != old_row:
        issues.append("old_run_projection_mismatch")
    if comparison.get("fresh_aggregates") != aggregates:
        issues.append("fresh_aggregate_mismatch")
    if comparison.get("required_zero_counters") != zero_counters:
        issues.append("required_zero_counter_projection_mismatch")
    verdicts = comparison.get("verdicts", {})
    if not isinstance(verdicts, Mapping):
        verdicts = {}
    required_passes = (
        "verifier_ready_pipeline",
        "c06_fresh_initial",
        "c17_fresh_initial",
        "c28_fresh_initial",
        "multi_archetype_fresh_session",
    )
    if any(verdicts.get(key) != "PASS" for key in required_passes):
        issues.append("required_fresh_session_verdict_missing")
    if (
        verdicts.get("operational_research_readiness")
        != "WITHHELD_FULL_THESIS_PENDING"
    ):
        issues.append("operational_readiness_overclaim_or_missing_withhold")
    if (
        comparison.get("status")
        != "PRO_FIRST_V2_1_MULTI_ARCHETYPE_FRESH_SESSION_PASS"
    ):
        issues.append("comparison_status_mismatch")

    payload = {
        "schema_version": "e2r_pro_v2_1_fresh_efficiency_audit_v1",
        "status": "PASS" if not issues else "FAIL",
        "critical_count": len(issues),
        "issues": sorted(issues),
        "fresh_archetype_count": len(fresh_rows),
        "fresh_runs": fresh_rows,
        "old_run": old_row,
        "fresh_aggregates": aggregates,
        "required_zero_counters": zero_counters,
        "comparison_hash": canonical_hash(comparison),
    }
    return {**payload, "audit_hash": canonical_hash(payload)}


def compile_fresh_session_efficiency_audit(
    repo_root: str | Path,
    comparison_path: str | Path = DEFAULT_COMPARISON_PATH,
) -> dict[str, Any]:
    root = Path(repo_root).expanduser().resolve()
    path = Path(comparison_path)
    if path.is_absolute():
        try:
            relative = path.resolve().relative_to(root)
        except ValueError as exc:
            raise ValueError("comparison path must be inside repository root") from exc
    else:
        relative = path
    comparison = _repo_json(root, relative)
    return audit_fresh_session_comparison(root, comparison)


__all__ = [
    "DEFAULT_COMPARISON_PATH",
    "EXPECTED_FRESH_RECEIPTS",
    "REQUIRED_ZERO_COUNTER_KEYS",
    "audit_fresh_session_comparison",
    "compile_fresh_session_efficiency_audit",
]
