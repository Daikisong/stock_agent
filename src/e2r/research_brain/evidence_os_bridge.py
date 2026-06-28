"""Evidence OS bridge guardrails for Research Brain outputs."""

from __future__ import annotations

from typing import Mapping, Sequence

from e2r.research_brain.schemas import ResearchBrainPlan


FORBIDDEN_DIRECT_SCORE_KEYS = {
    "score",
    "stage",
    "current_score_eligible",
    "hard_break_final",
    "verified_final",
    "accepted_claim_final",
    "feature_input",
    "score_contribution",
}


def audit_plan_does_not_mutate_evidence_os(plans: Sequence[ResearchBrainPlan]) -> Mapping[str, int]:
    forbidden_count = 0
    direct_feature_input_mutation_count = 0
    direct_score_contribution_mutation_count = 0
    for plan in plans:
        payload = plan.to_dict()
        forbidden_count += sum(1 for key in FORBIDDEN_DIRECT_SCORE_KEYS if key in payload)
        direct_feature_input_mutation_count += int("feature_input" in payload)
        direct_score_contribution_mutation_count += int("score_contribution" in payload)
    return {
        "research_brain_score_output_key_count": forbidden_count,
        "research_brain_stage_override_key_count": 0,
        "research_brain_direct_feature_input_mutation_count": direct_feature_input_mutation_count,
        "research_brain_direct_score_contribution_mutation_count": direct_score_contribution_mutation_count,
        "evidence_os_only_bridge_ready": forbidden_count == 0
        and direct_feature_input_mutation_count == 0
        and direct_score_contribution_mutation_count == 0,
    }


__all__ = ["FORBIDDEN_DIRECT_SCORE_KEYS", "audit_plan_does_not_mutate_evidence_os"]
