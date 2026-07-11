from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.scoring.question_impact_contract import (
    QUESTION_CLOSURE_STATUSES,
    audit_question_impact_contracts,
    compile_question_closures_v2,
    load_question_impact_contracts,
)


class QuestionImpactContractTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_c06_twelve_families_have_total_semantic_contracts(self) -> None:
        contracts = load_question_impact_contracts(
            self.ROOT / "configs/e2r_question_impact_contracts_v1.json"
        )
        self.assertEqual(len(contracts), 12)
        self.assertEqual(
            QUESTION_CLOSURE_STATUSES,
            {
                "SUPPORTED_SCORING",
                "PARTIALLY_SUPPORTED_SCORING",
                "SUPPORTED_NON_SCORING",
                "COUNTER_SUPPORTED",
                "EVALUATED_ABSENT",
                "SOURCE_PENDING",
                "PROVIDER_PENDING",
                "BUDGET_PENDING",
            },
        )
        for contract in contracts.values():
            self.assertEqual(
                contract.archetype_id,
                "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            )
            self.assertTrue(contract.accepted_claim_predicates)
            self.assertTrue(contract.allowed_primitive_ids)
            self.assertTrue(contract.allowed_component_ids)
            self.assertTrue(contract.required_source_routes)
            self.assertTrue(contract.required_counter_routes)
            self.assertEqual(
                contract.terminal_absence_policy,
                "REQUIRE_ADEQUATE_SEARCH",
            )

    def test_foundry_candidate_cannot_close_hbm_allocation_as_scoring(self) -> None:
        closure = self._compile_one(
            family="current_customer_allocation_commitment",
            claim={
                "claim_id": "C-FOUNDRY",
                "raw_assertion": {
                    "predicate": "semiconductor foundry supply contract",
                    "object_text": "Tesla foundry capacity contract",
                },
            },
            primitive_id="revenue_visibility_contract",
            eligibility={
                "component_scoring_eligibility": False,
                "eligibility_status": "INELIGIBLE_WRONG_MECHANISM",
            },
            impact=True,
        )
        self.assertEqual(closure["status"], "SUPPORTED_NON_SCORING")
        self.assertEqual(closure["supporting_claim_ids"], [])
        self.assertEqual(closure["non_scoring_claim_ids"], ["C-FOUNDRY"])
        self.assertEqual(closure["eligibility_decision_ids"], [])

    def test_forward_mass_production_is_partial_but_actual_shipment_scores(self) -> None:
        planned = self._compile_one(
            family="shipment_mass_production_generation",
            claim={
                "claim_id": "C-PLAN",
                "raw_assertion": {
                    "predicate": "plans to begin mass production",
                    "object_text": "HBM4E after initial sample shipments",
                },
            },
            primitive_id="hbm_product_profile",
            eligibility={"component_scoring_eligibility": True},
            impact=True,
        )
        actual = self._compile_one(
            family="shipment_mass_production_generation",
            claim={
                "claim_id": "C-ACTUAL",
                "raw_assertion": {
                    "predicate": "commercially shipped",
                    "object_text": "HBM4 commercial products",
                },
            },
            primitive_id="hbm_product_profile",
            eligibility={"component_scoring_eligibility": True},
            impact=True,
        )
        self.assertEqual(planned["status"], "PARTIALLY_SUPPORTED_SCORING")
        self.assertEqual(actual["status"], "SUPPORTED_SCORING")

    def test_claim_without_allowed_positive_impact_is_non_scoring(self) -> None:
        closure = self._compile_one(
            family="shipment_mass_production_generation",
            claim={
                "claim_id": "C-PROFILE",
                "raw_assertion": {
                    "predicate": "commercially shipped",
                    "object_text": "HBM4 commercial products",
                },
            },
            primitive_id="hbm_product_profile",
            eligibility={"component_scoring_eligibility": True},
            impact=False,
        )
        self.assertEqual(closure["status"], "SUPPORTED_NON_SCORING")

    def test_impact_for_another_question_cannot_close_this_question(self) -> None:
        closure = self._compile_one(
            family="shipment_mass_production_generation",
            claim={
                "claim_id": "C-QUESTION-BOUND",
                "raw_assertion": {
                    "predicate": "commercially shipped",
                    "object_text": "HBM sales increased",
                },
            },
            primitive_id="shipment_or_revenue_mix",
            eligibility={"component_scoring_eligibility": True},
            impact=True,
            impact_question="hbm_ai_memory_revenue_mix",
        )
        self.assertEqual(closure["status"], "SUPPORTED_NON_SCORING")

    def test_frozen_audit_matches_committed_pass_artifact(self) -> None:
        actual = audit_question_impact_contracts(repo_root=self.ROOT)
        expected = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_question_impact_contract_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(actual, expected)
        self.assertEqual(actual["status"], "QUESTION_IMPACT_CONTRACT_PASS")
        self.assertEqual(actual["critical_count_sum"], 0)

    def _compile_one(
        self,
        *,
        family: str,
        claim,
        primitive_id: str,
        eligibility,
        impact: bool,
        impact_question: str | None = None,
    ):
        contract = load_question_impact_contracts(
            self.ROOT / "configs/e2r_question_impact_contracts_v1.json"
        )[family]
        claim_id = claim["claim_id"]
        decision = {
            "eligibility_decision_id": f"ELIG-{claim_id}",
            "claim_id": claim_id,
            "risk_scoring_eligibility": False,
            **eligibility,
        }
        impacts = []
        if impact:
            impacts.append(
                {
                    "claim_id": claim_id,
                    "mapping_id": "M-1",
                    "lineage_mapping_ids": [],
                    "primitive_id": primitive_id,
                    "component_id": contract.allowed_component_ids[0],
                    "direction": "SUPPORT",
                    "validated_credit_fraction": 0.5,
                    **(
                        {"question_family_id": impact_question}
                        if impact_question
                        else {}
                    ),
                }
            )
        return compile_question_closures_v2(
            contracts={family: contract},
            claims=[claim],
            primitive_mappings=[
                {
                    "mapping_id": "M-1",
                    "claim_id": claim_id,
                    "primitive_id": primitive_id,
                    "support_direction": "SUPPORT",
                    "accepted_by_evidence_os": True,
                }
            ],
            eligibility_decisions=[decision],
            validated_impacts=impacts,
        )[0]


if __name__ == "__main__":
    unittest.main()
