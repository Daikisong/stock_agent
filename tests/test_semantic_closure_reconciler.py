from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.scoring.question_impact_contract import (
    load_question_impact_contracts,
)
from e2r.research_brain.scoring.semantic_closure_reconciler import (
    SemanticClosureReconciler,
    audit_question_component_reconciliation,
)


class SemanticClosureReconcilerTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def setUp(self) -> None:
        self.contracts = {
            key: value
            for key, value in load_question_impact_contracts().items()
            if value.archetype_id == "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
        }

    def test_valid_question_claim_impact_component_chain_has_zero_critical(self) -> None:
        result = self._valid_result()
        self.assertEqual(
            result.status, "QUESTION_COMPONENT_RECONCILIATION_PASS"
        )
        self.assertEqual(result.audit["critical_count_sum"], 0)
        supported = next(
            row
            for row in result.reconciliations
            if row.question_family_id
            == "current_customer_allocation_commitment"
        )
        self.assertEqual(supported.credit_result, "NONZERO_BOUNDED_SUPPORT")
        self.assertEqual(supported.validated_impact_ids, ("I-SUPPORT",))
        self.assertEqual(supported.component_ids, ("earnings_visibility",))

    def test_operational_audit_matches_recompiled_semantic_chain(self) -> None:
        actual = audit_question_component_reconciliation()
        expected = json.loads(
            (
                self.ROOT
                / "docs/operational/"
                "e2r_question_component_reconciliation_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(actual, expected)
        self.assertEqual(actual["critical_count_sum"], 0)
        for name in (
            "supported_question_zero_credit_count",
            "partially_supported_question_zero_credit_count",
            "supported_question_absent_component_count",
            "positive_claim_absent_component_count",
            "positive_proposal_absent_component_count",
            "absence_with_internal_rejection_count",
            "absence_with_provider_failure_count",
            "absence_with_inadequate_search_count",
        ):
            self.assertEqual(actual["critical_counts"][name], 0)

    def test_supported_scoring_without_credit_is_pipeline_error(self) -> None:
        result = self._reconcile(
            closures=(
                {
                    "question_family_id": "current_customer_allocation_commitment",
                    "status": "SUPPORTED_SCORING",
                    "supporting_claim_ids": ["C-MISSING"],
                },
            ),
            claims=(self._claim("C-MISSING"),),
            mappings=(
                self._mapping(
                    "C-MISSING", "customer_preorder_or_allocation"
                ),
            ),
            eligibility=(self._eligibility("C-MISSING", True),),
        )
        row = self._row(result, "current_customer_allocation_commitment")
        self.assertEqual(row.reconciled_closure_status, "SCORING_PIPELINE_ERROR")
        self.assertGreater(
            result.audit["critical_counts"][
                "supported_question_zero_credit_count"
            ],
            0,
        )
        self.assertGreater(
            result.audit["critical_counts"][
                "positive_claim_absent_component_count"
            ],
            0,
        )

    def test_absence_never_masks_provider_or_search_failure(self) -> None:
        provider = self._reconcile(
            closures=(
                {
                    "question_family_id": "qualification_pass_lag_reopen",
                    "status": "EVALUATED_ABSENT",
                    "search_exhaustion_proof": ["SEARCH-Q"],
                    "failure_class": "SOURCE_EXHAUSTED",
                },
            ),
            claims=(self._claim("C-PROVIDER"),),
            mappings=(self._mapping("C-PROVIDER", "qualification_state"),),
            eligibility=(self._eligibility("C-PROVIDER", True),),
            adjudications=(
                {
                    "claim_id": "C-PROVIDER",
                    "status": "IMPACT_ADJUDICATION_FAIL",
                },
            ),
        )
        self.assertEqual(
            self._row(provider, "qualification_pass_lag_reopen").reconciled_closure_status,
            "PROVIDER_PENDING",
        )
        self.assertEqual(
            provider.audit["critical_counts"][
                "absence_with_provider_failure_count"
            ],
            1,
        )
        inadequate = self._reconcile(
            closures=(
                {
                    "question_family_id": "qualification_pass_lag_reopen",
                    "status": "EVALUATED_ABSENT",
                    "search_exhaustion_proof": [],
                },
            ),
        )
        self.assertEqual(
            self._row(inadequate, "qualification_pass_lag_reopen").reconciled_closure_status,
            "SOURCE_PENDING",
        )
        self.assertEqual(
            inadequate.audit["critical_counts"][
                "absence_with_inadequate_search_count"
            ],
            1,
        )

    def test_internal_rejection_cannot_be_relabelled_as_absence(self) -> None:
        proposal = self._proposal(
            "I-REJECTED",
            "C-REJECTED",
            "qualification_pass_lag_reopen",
            "qualification_state",
            "earnings_visibility",
            "C06_VIS_QUALIFICATION",
        )
        result = self._reconcile(
            closures=(
                {
                    "question_family_id": "qualification_pass_lag_reopen",
                    "status": "EVALUATED_ABSENT",
                    "search_exhaustion_proof": ["SEARCH-Q"],
                    "failure_class": "SOURCE_EXHAUSTED",
                },
            ),
            claims=(self._claim("C-REJECTED"),),
            mappings=(self._mapping("C-REJECTED", "qualification_state"),),
            eligibility=(self._eligibility("C-REJECTED", True),),
            proposals=(proposal,),
            rejected=(
                {"impact_id": "I-REJECTED", "reason": "RUBRIC_EDGE_VIOLATION"},
            ),
        )
        row = self._row(result, "qualification_pass_lag_reopen")
        self.assertEqual(row.reconciled_closure_status, "SCORING_PIPELINE_ERROR")
        self.assertEqual(
            result.audit["critical_counts"][
                "absence_with_internal_rejection_count"
            ],
            1,
        )

    def test_one_valid_impact_cannot_hide_another_missing_claim_lineage(self) -> None:
        first = self._proposal(
            "I-FIRST",
            "C-FIRST",
            "qualification_pass_lag_reopen",
            "qualification_state",
            "earnings_visibility",
            "C06_VIS_QUALIFICATION",
        )
        missing = self._proposal(
            "I-MISSING",
            "C-MISSING",
            "qualification_pass_lag_reopen",
            "qualification_state",
            "earnings_visibility",
            "C06_VIS_QUALIFICATION",
        )
        result = self._reconcile(
            closures=(
                {
                    "question_family_id": "qualification_pass_lag_reopen",
                    "status": "SUPPORTED_SCORING",
                    "supporting_claim_ids": ["C-FIRST", "C-MISSING"],
                },
            ),
            claims=(self._claim("C-FIRST"), self._claim("C-MISSING")),
            mappings=(
                self._mapping("C-FIRST", "qualification_state"),
                self._mapping("C-MISSING", "qualification_state"),
            ),
            eligibility=(
                self._eligibility("C-FIRST", True),
                self._eligibility("C-MISSING", True),
            ),
            proposals=(first, missing),
            impacts=(self._impact(first, support=0.6),),
            assessments=(
                {
                    "component_id": "earnings_visibility",
                    "status": "VERIFIED_WEAK_SUPPORT",
                },
            ),
        )
        self.assertEqual(
            result.audit["critical_counts"][
                "positive_claim_absent_component_count"
            ],
            1,
        )
        self.assertEqual(
            result.audit["critical_counts"][
                "positive_proposal_absent_component_count"
            ],
            1,
        )

    def _valid_result(self):
        claims = (
            self._claim("C-SUPPORT"),
            self._claim("C-PARTIAL"),
            self._claim("C-NONSCORING"),
            {**self._claim("C-COUNTER"), "polarity": "COUNTER"},
        )
        mappings = (
            self._mapping("C-SUPPORT", "customer_preorder_or_allocation"),
            self._mapping("C-PARTIAL", "actual_earnings_conversion"),
            self._mapping("C-NONSCORING", "hbm_product_profile"),
            self._mapping(
                "C-COUNTER", "conventional_memory_drag", direction="COUNTER"
            ),
        )
        eligibility = (
            self._eligibility("C-SUPPORT", True),
            self._eligibility("C-PARTIAL", True),
            self._eligibility("C-NONSCORING", False),
            self._eligibility("C-COUNTER", False),
        )
        closures = (
            {
                "question_family_id": "current_customer_allocation_commitment",
                "status": "SUPPORTED_SCORING",
                "supporting_claim_ids": ["C-SUPPORT"],
            },
            {
                "question_family_id": "revenue_operating_profit_conversion",
                "status": "PARTIALLY_SUPPORTED_SCORING",
                "partial_supporting_claim_ids": ["C-PARTIAL"],
            },
            {
                "question_family_id": "shipment_mass_production_generation",
                "status": "SUPPORTED_NON_SCORING",
                "non_scoring_claim_ids": ["C-NONSCORING"],
            },
            {
                "question_family_id": "qualification_pass_lag_reopen",
                "status": "EVALUATED_ABSENT",
                "search_exhaustion_proof": ["SEARCH-QUALIFICATION"],
                "failure_class": "SOURCE_EXHAUSTED",
            },
            {
                "question_family_id": "conventional_memory_drag",
                "status": "COUNTER_SUPPORTED",
                "counter_claim_ids": ["C-COUNTER"],
            },
        )
        support_proposal = self._proposal(
            "I-SUPPORT",
            "C-SUPPORT",
            "current_customer_allocation_commitment",
            "customer_preorder_or_allocation",
            "earnings_visibility",
            "C06_VIS_CUSTOMER_COMMITMENT",
        )
        partial_proposal = self._proposal(
            "I-PARTIAL",
            "C-PARTIAL",
            "revenue_operating_profit_conversion",
            "actual_earnings_conversion",
            "eps_fcf_explosion",
            "C06_EPS_ACTUAL_REVENUE_PROFIT",
        )
        counter_proposal = self._proposal(
            "I-COUNTER",
            "C-COUNTER",
            "conventional_memory_drag",
            "conventional_memory_drag",
            "earnings_visibility",
            "C06_VIS_MEDIUM_REVISION",
            direction="COUNTER",
        )
        impacts = (
            self._impact(support_proposal, support=0.8),
            self._impact(partial_proposal, support=0.4),
            self._impact(counter_proposal, counter=0.6),
        )
        assessments = (
            {"component_id": "earnings_visibility", "status": "SUPPORT_WITH_COUNTER_CAP"},
            {"component_id": "eps_fcf_explosion", "status": "VERIFIED_WEAK_SUPPORT"},
        )
        return self._reconcile(
            closures=closures,
            claims=claims,
            mappings=mappings,
            eligibility=eligibility,
            proposals=(support_proposal, partial_proposal, counter_proposal),
            impacts=impacts,
            assessments=assessments,
        )

    def _reconcile(
        self,
        *,
        closures=(),
        claims=(),
        mappings=(),
        eligibility=(),
        proposals=(),
        impacts=(),
        assessments=(),
        rejected=(),
        adjudications=(),
    ):
        return SemanticClosureReconciler().reconcile(
            contracts=self.contracts,
            question_closures=closures,
            claims=claims,
            primitive_mappings=mappings,
            eligibility_decisions=eligibility,
            proposed_impacts=proposals,
            validated_impacts=impacts,
            component_assessments=assessments,
            rejected_impacts=rejected,
            adjudications=adjudications,
        )

    @staticmethod
    def _row(result, question_id):
        return next(
            row
            for row in result.reconciliations
            if row.question_family_id == question_id
        )

    @staticmethod
    def _claim(claim_id):
        return {"claim_id": claim_id, "accepted": True}

    @staticmethod
    def _mapping(claim_id, primitive_id, *, direction="SUPPORT"):
        return {
            "claim_id": claim_id,
            "primitive_id": primitive_id,
            "support_direction": direction,
            "accepted_by_evidence_os": True,
        }

    @staticmethod
    def _eligibility(claim_id, component):
        return {
            "claim_id": claim_id,
            "eligibility_decision_id": f"ELIG-{claim_id}",
            "component_scoring_eligibility": component,
        }

    @staticmethod
    def _proposal(
        impact_id,
        claim_id,
        question_id,
        primitive_id,
        component_id,
        subcriterion_id,
        *,
        direction="SUPPORT",
    ):
        return {
            "impact_id": impact_id,
            "claim_id": claim_id,
            "question_family_id": question_id,
            "primitive_id": primitive_id,
            "component_id": component_id,
            "component_subcriterion_id": subcriterion_id,
            "direction": direction,
        }

    @staticmethod
    def _impact(proposal, *, support=0.0, counter=0.0):
        return {
            **proposal,
            "eligibility_decision_id": f"ELIG-{proposal['claim_id']}",
            "validated_credit_fraction": max(support, counter),
            "support_credit_fraction": support,
            "counter_effect_fraction": counter,
            "resolution_effect": 0.0,
            "support_type": "PARTIAL_BRIDGE" if support < 1 else "DIRECT_ACTUAL",
        }


if __name__ == "__main__":
    unittest.main()
