from __future__ import annotations

from e2r.research_brain.scoring import FullScoreValidityEvidenceV2


def passing_full_score_validity_evidence(
    source_id: str = "CONTROLLED-UNIT-VALIDITY",
) -> FullScoreValidityEvidenceV2:
    return FullScoreValidityEvidenceV2(
        schema_totality_status="SCORING_SCHEMA_TOTALITY_PASS",
        scoring_schema_critical_count=0,
        silent_zero_default_count=0,
        positive_impact_zeroed_by_missing_cap_count=0,
        counter_impact_zeroed_by_missing_cap_count=0,
        mechanism_scope_failure_count=0,
        question_component_reconciliation_critical_count=0,
        unresolved_contradiction_count=0,
        pending_state_count=0,
        absence_without_adequacy_count=0,
        gold_critical_fact_miss_count=0,
        cross_business_question_closure_count=0,
        same_fact_duplicate_credit_count=0,
        same_document_duplicate_credit_count=0,
        source_audit_ids=(source_id,),
    )
