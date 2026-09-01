"""Exact P8 known-bad corpus contract and independent manifest audit."""

from __future__ import annotations

from typing import Any, Mapping, Sequence

from ..ids import canonical_hash


REQUIRED_V2_KNOWN_BAD_CASE_IDS = (
    "generic_component_only_prompt",
    "forced_complete_status",
    "one_pass_full_thesis_publication",
    "component_one_fact_completeness",
    "one_fact_seven_component_completeness",
    "public_gap_corroboration_downgrade",
    "thirteen_material_gaps_zero_followup",
    "verifier_rejection_score_only",
    "quote_mismatch_repack",
    "wrong_subject_repack",
    "likely_nonpublic_absent_zero",
    "future_event_current_failure",
    "provider_failure_fixpoint",
    "transport_limit_saturation",
    "same_gap_infinite_reopen",
    "pro_score_authority",
    "pro_stage_authority",
    "historical_price_outcome_leakage",
    "c06_questions_in_c28",
    "security_keyword_arr",
    "bio_headline_endpoint_success",
    "commodity_headline_realized_margin",
    "policy_headline_direct_cash",
    "low_pbr_capital_return_execution",
    "old_accounting_risk_current_hard_break",
    "partial_score_dashboard_current",
    "v1_canary_receipt_overwrite",
    "fixture_answer_live_injection",
    "symbol_specific_branch",
    "deterministic_query_literal",
)


ALLOWED_OUTCOMES = frozenset({"REJECTED", "BLOCKED", "WITHHELD", "PENDING"})


def audit_v2_known_bad_corpus(
    corpus: Mapping[str, Any],
) -> Mapping[str, Any]:
    rows = tuple(corpus.get("cases") or ())
    ids = tuple(str(row.get("case_id") or "") for row in rows)
    duplicate_ids = sorted({value for value in ids if ids.count(value) > 1})
    missing_ids = [value for value in REQUIRED_V2_KNOWN_BAD_CASE_IDS if value not in ids]
    extra_ids = [value for value in ids if value not in REQUIRED_V2_KNOWN_BAD_CASE_IDS]
    order_mismatch = ids != REQUIRED_V2_KNOWN_BAD_CASE_IDS
    invalid_rows = []
    detector_ids: list[str] = []
    category_counts: dict[str, int] = {}
    for index, row in enumerate(rows):
        category = str(row.get("category") or "")
        detectors = row.get("detector_test_ids")
        outcome = str(row.get("expected_outcome") or "")
        if category:
            category_counts[category] = category_counts.get(category, 0) + 1
        if isinstance(detectors, Sequence) and not isinstance(detectors, (str, bytes)):
            normalized_detectors = tuple(str(value) for value in detectors if str(value))
            detector_ids.extend(normalized_detectors)
        else:
            normalized_detectors = ()
        if (
            not str(row.get("case_id") or "")
            or not category
            or not str(row.get("mutation") or "")
            or outcome not in ALLOWED_OUTCOMES
            or not normalized_detectors
            or any(".test_" not in value for value in normalized_detectors)
            or row.get("score_authority") is not False
            or row.get("stage_authority") is not False
        ):
            invalid_rows.append(index)
    critical_counts = {
        "missing_required_case_count": len(missing_ids),
        "extra_case_count": len(extra_ids),
        "duplicate_case_count": len(duplicate_ids),
        "case_order_mismatch_count": int(order_mismatch),
        "invalid_case_contract_count": len(invalid_rows),
        "corpus_schema_mismatch_count": int(
            corpus.get("schema_version") != "e2r_pro_v2_known_bad_corpus_v1"
        ),
        "production_authority_overclaim_count": int(
            corpus.get("production_runtime_ready") is not False
        ),
    }
    critical_sum = sum(critical_counts.values())
    leaf_payload = [
        {
            "case_id": str(row.get("case_id") or ""),
            "category": str(row.get("category") or ""),
            "mutation": str(row.get("mutation") or ""),
            "expected_outcome": str(row.get("expected_outcome") or ""),
            "detector_test_ids": list(row.get("detector_test_ids") or ()),
        }
        for row in rows
    ]
    return {
        "schema_version": "e2r_pro_v2_known_bad_audit_v1",
        "status": "PASS" if critical_sum == 0 else "FAIL",
        "required_case_count": len(REQUIRED_V2_KNOWN_BAD_CASE_IDS),
        "observed_case_count": len(rows),
        "unique_detector_count": len(set(detector_ids)),
        "category_counts": dict(sorted(category_counts.items())),
        "missing_required_case_ids": missing_ids,
        "extra_case_ids": extra_ids,
        "duplicate_case_ids": duplicate_ids,
        "invalid_case_indexes": invalid_rows,
        "critical_counts": critical_counts,
        "critical_count_sum": critical_sum,
        "production_runtime_ready": False,
        "fixture_only": True,
        "corpus_leaf_hash": canonical_hash(leaf_payload),
    }


__all__ = [
    "ALLOWED_OUTCOMES",
    "REQUIRED_V2_KNOWN_BAD_CASE_IDS",
    "audit_v2_known_bad_corpus",
]
