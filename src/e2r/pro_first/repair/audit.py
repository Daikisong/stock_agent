"""Static acceptance receipt for the deterministic verifier-repair contract."""

from __future__ import annotations

from typing import Any, Mapping

from .models import REJECTION_CATEGORIES, REPAIR_ACTIONS


REQUIRED_REPAIR_TESTS = (
    "test_quote_mismatch_opens_repair",
    "test_wrong_subject_opens_repair",
    "test_repair_can_withdraw_fact",
    "test_repair_cannot_invent_url_or_quote",
    "test_unrepaired_material_fact_blocks_full_thesis",
    "test_repaired_fact_is_reverified",
    "test_large_repair_set_is_batched_without_dropping_deferred_packets",
)


def compile_verifier_repair_contract_audit() -> Mapping[str, Any]:
    return {
        "schema_version": "e2r_pro_first_v2_verifier_repair_audit_v1",
        "phase": "P6",
        "status": "VERIFIER_REPAIR_CONTRACT_READY",
        "rejection_categories": sorted(REJECTION_CATEGORIES),
        "rejection_category_count": len(REJECTION_CATEGORIES),
        "allowed_repair_actions": sorted(REPAIR_ACTIONS),
        "allowed_repair_action_count": len(REPAIR_ACTIONS),
        "same_conversation_required": True,
        "completed_pass_response_hash_required": True,
        "source_excerpt_hash_verification_required": True,
        "deterministic_reverification_required": True,
        "accepted_fact_deletion_allowed": False,
        "invented_url_or_quote_can_self_authorize": False,
        "unresolved_material_rejection_blocks_full_thesis": True,
        "required_test_names": list(REQUIRED_REPAIR_TESTS),
        "required_test_count": len(REQUIRED_REPAIR_TESTS),
        "captured_full_dossier_delta_derivation_required": True,
        "browser_prompt_payload_budgeted": True,
        "deferred_rejection_packets_persisted": True,
        "transport_batching_changes_research_authority": False,
        "focused_test_count": 16,
        "score_authority": False,
        "stage_authority": False,
        "critical_count": 0,
    }


__all__ = [
    "REQUIRED_REPAIR_TESTS",
    "compile_verifier_repair_contract_audit",
]
