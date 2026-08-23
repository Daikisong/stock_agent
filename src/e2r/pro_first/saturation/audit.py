"""Leaf audit for deterministic question-family saturation receipts."""

from __future__ import annotations

from typing import Any, Mapping

from .models import ResearchSaturationReceipt


def compile_saturation_audit(
    receipt: ResearchSaturationReceipt,
) -> Mapping[str, Any]:
    decisions = receipt.question_decisions
    critical_counts = {
        "mandatory_question_missing_count": len(
            receipt.missing_mandatory_question_ids
        ),
        "mandatory_question_nonterminal_count": len(
            receipt.nonterminal_mandatory_question_ids
        ),
        "public_material_gap_count": len(
            receipt.public_material_gap_question_ids
        ),
        "verifier_repair_pending_count": len(receipt.verifier_repair_pending_ids),
        "provider_parser_core_pending_count": len(
            receipt.provider_parser_core_pending_question_ids
        ),
        "lifecycle_hard_break_pending_count": len(
            receipt.lifecycle_hard_break_pending_ids
        ),
        "question_source_linkage_incomplete_count": len(
            receipt.source_linkage_incomplete_question_ids
        ),
        "component_fact_count_adequacy_reference_count": 0,
        "pro_score_authority_count": int(receipt.score_authority),
        "pro_stage_authority_count": int(receipt.stage_authority),
    }
    return {
        "schema_version": "e2r_pro_first_v2_saturation_audit_v1",
        "status": (
            "FULL_THESIS_READY"
            if receipt.research_saturation_valid
            else "RESEARCH_SATURATION_PENDING"
        ),
        "critical_counts": critical_counts,
        "critical_count_sum": sum(critical_counts.values()),
        "expected_mandatory_question_count": len(
            receipt.expected_mandatory_question_ids
        ),
        "question_decision_count": len(decisions),
        "question_terminal_count": sum(row.terminal for row in decisions),
        "gap_class_counts": {
            key: sum(row.gap_class == key for row in decisions)
            for key in (
                "NO_GAP",
                "CORE_SCORE_BLOCKER",
                "STAGE_BOUNDARY_GAP",
                "HARD_BREAK_GAP",
                "CORROBORATION_CAP",
                "MONITORING_GAP",
            )
        },
        "materiality_divergence_count": sum(
            row.deterministic_materiality_diverged for row in decisions
        ),
        "research_saturation_valid": receipt.research_saturation_valid,
        "component_entry_allowed": receipt.component_entry_allowed,
        "score_authority": False,
        "stage_authority": False,
        "receipt_hash": receipt.receipt_hash,
    }


__all__ = ["compile_saturation_audit"]
