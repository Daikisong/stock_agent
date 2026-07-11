from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.runtime.scoring_contracts import (
    load_archetype_scoring_contract,
)
from e2r.research_brain.scoring import (
    AtomicStageCourtV2,
    ComponentAssessmentBuilder,
    ResearchCalibratedComponentScorer,
    audit_full_score_validity_v2,
    compile_full_score_validity_evidence_v2,
)
from tests.full_score_validity_fixture import (
    passing_full_score_validity_evidence,
)
from tests.test_component_assessment_states import supported_impact


class FullScoreValidityV2Tests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def setUp(self) -> None:
        self.contract = load_archetype_scoring_contract(
            "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
        )
        self.impact = supported_impact()
        terminal = {
            component_id: {
                "status": "VERIFIED_ABSENT_AFTER_SEARCH",
                "search_exhaustion_proof": [f"SEARCH-{component_id}"],
            }
            for component_id in self.contract.component_weights
            if component_id != self.impact.component_id
        }
        self.assessments = ComponentAssessmentBuilder().build(
            contract=self.contract,
            impacts=(self.impact,),
            terminal_evidence=terminal,
        ).assessments

    def test_operational_audit_matches_all_semantic_gate_canaries(self) -> None:
        actual = audit_full_score_validity_v2()
        expected = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_full_score_validity_v2_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(actual, expected)
        self.assertEqual(actual["status"], "FULL_SCORE_VALIDITY_V2_AUDIT_PASS")
        self.assertEqual(actual["critical_count_sum"], 0)
        self.assertEqual(len(actual["failure_cases"]), 13)

    def test_invalid_semantics_preserve_verified_score_and_interval(self) -> None:
        scorer = ResearchCalibratedComponentScorer()
        valid = scorer.score(
            contract=self.contract,
            impacts=(self.impact,),
            assessments=self.assessments,
            validity_evidence=passing_full_score_validity_evidence(),
        )
        invalid_evidence = passing_full_score_validity_evidence()
        invalid_evidence = type(invalid_evidence)(
            **{
                **invalid_evidence.to_dict(),
                "cross_business_question_closure_count": 1,
            }
        )
        invalid = scorer.score(
            contract=self.contract,
            impacts=(self.impact,),
            assessments=self.assessments,
            validity_evidence=invalid_evidence,
        )
        self.assertTrue(valid.full_score_valid)
        self.assertFalse(invalid.full_score_valid)
        self.assertIsNone(invalid.full_e2r_score)
        self.assertEqual(
            invalid.verified_supported_score, valid.verified_supported_score
        )
        self.assertEqual(
            (
                invalid.provisional_score_lower,
                invalid.provisional_score_upper,
            ),
            (valid.provisional_score_lower, valid.provisional_score_upper),
        )
        decision = AtomicStageCourtV2().decide(
            target_id="TARGET-SEMANTIC-PENDING",
            as_of_date="2026-07-11",
            contract=self.contract,
            score=invalid,
            assessments=self.assessments,
            impacts=(self.impact,),
            accepted_claim_ids=(self.impact.claim_id,),
        )
        self.assertEqual(decision.canonical_stage, "0")
        self.assertEqual(decision.decision_status, "SEMANTIC_VALIDITY_PENDING")

    def test_absence_requires_explicit_evidence_search_adequacy_pass(self) -> None:
        absent_components = {
            row.component_id
            for row in self.assessments
            if row.status == "VERIFIED_ABSENT_AFTER_SEARCH"
        }
        reconciliations = tuple(
            {
                "reconciliation_id": f"RECON-{component_id}",
                "question_family_id": f"question-{component_id}",
                "input_closure_status": "EVALUATED_ABSENT",
                "reconciled_closure_status": "EVALUATED_ABSENT",
                "component_states": {
                    component_id: "VERIFIED_ABSENT_AFTER_SEARCH"
                },
                "component_links": [],
            }
            for component_id in absent_components
        )
        missing = self._compile(reconciliations, search_adequacy=())
        self.assertEqual(
            missing.absence_without_adequacy_count,
            len(absent_components),
        )
        adequate = self._compile(
            reconciliations,
            search_adequacy=tuple(
                {
                    "adequacy_id": f"ADEQ-{component_id}",
                    "question_family_id": f"question-{component_id}",
                    "saturation_status": "ADEQUATE_ABSENCE",
                    "adequate_absence_allowed": True,
                    "provider_failures": 0,
                    "budget_exhausted": False,
                    "missing_route_categories": [],
                    "positive_proposal_zeroed_by_internal_validation_count": 0,
                    "gold_material_fact_miss_count": 0,
                }
                for component_id in absent_components
            ),
        )
        self.assertEqual(adequate.absence_without_adequacy_count, 0)

    def test_missing_validity_evidence_is_fail_closed(self) -> None:
        result = ResearchCalibratedComponentScorer().score(
            contract=self.contract,
            impacts=(self.impact,),
            assessments=self.assessments,
        )
        self.assertFalse(result.full_score_valid)
        self.assertIsNone(result.full_e2r_score)
        self.assertIn(
            "validity_evidence_missing_count",
            result.audit["full_score_validity"]["blocking_reasons"],
        )

    def _compile(self, reconciliations, *, search_adequacy):
        return compile_full_score_validity_evidence_v2(
            assessments=self.assessments,
            scoring_schema_audit={
                "status": "SCORING_SCHEMA_TOTALITY_PASS",
                "critical_count_sum": 0,
                "critical_counts": {"silent_zero_default_count": 0},
                "policy_config_hash": "POLICY-TEST",
            },
            impact_validation_audit={
                "critical_count_sum": 0,
                "critical_counts": {
                    "cross_mechanism_impact_count": 0,
                    "positive_impact_zeroed_by_missing_cap_count": 0,
                    "counter_impact_zeroed_by_missing_cap_count": 0,
                    "same_fact_duplicate_credit_count": 0,
                    "same_document_duplicate_credit_count": 0,
                },
            },
            validated_impacts=(self.impact,),
            reconciliation_audit={"critical_count_sum": 0},
            reconciliations=reconciliations,
            search_adequacy=search_adequacy,
        )


if __name__ == "__main__":
    unittest.main()
