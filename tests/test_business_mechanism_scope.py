from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.production.v6_canary_selection import REQUIRED_ARCHETYPES
from e2r.research_brain.scoring.business_mechanism_scope import (
    BusinessMechanismScope,
    ISSUER_CONSOLIDATED_ACTUAL_SCOPE_CONTRACT,
    MechanismScopeValidator,
    audit_business_mechanism_scope,
    infer_business_mechanism_scope,
    load_mechanism_scope_contracts,
)


class BusinessMechanismScopeTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_current_live_canaries_all_have_scope_contracts(self) -> None:
        contracts = load_mechanism_scope_contracts()
        self.assertEqual(
            set(REQUIRED_ARCHETYPES) - set(contracts),
            set(),
        )

    def test_explicit_validated_scope_is_reused_without_prose_guessing(self) -> None:
        claim = {
            "target_id": "TARGET",
            "period": "2026Q2",
            "exact_quote": "Operating margin increased.",
            "scope_business_segment": "MATERIALS",
            "scope_product_family": "COMMODITY_PRODUCT",
            "scope_technology_family": "METAL_PROCESS",
            "scope_transaction_type": "REVENUE_ACTUAL",
            "scope_economic_mechanism": "REVENUE_CONVERSION",
            "scope_confidence": 0.94,
        }
        scope = infer_business_mechanism_scope(
            claim,
            primitive_id="opm_expansion_pctp",
            archetype_id="C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
        )
        self.assertEqual(scope.business_segment, "MATERIALS")
        self.assertEqual(scope.product_family, "COMMODITY_PRODUCT")
        result = MechanismScopeValidator().validate(
            scope=scope,
            contract=load_mechanism_scope_contracts()[
                "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD"
            ],
            component_id="earnings_visibility",
        )
        self.assertTrue(result.scope_match)

    def test_same_issuer_wrong_segment_is_rejected_and_rerouted(self) -> None:
        contract = load_mechanism_scope_contracts()[
            "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
        ]
        scope = BusinessMechanismScope(
            issuer_id="005930",
            business_segment="FOUNDRY",
            product_family="LOGIC_FOUNDRY",
            technology_family="FOUNDRY",
            customer_or_counterparty="Tesla",
            transaction_type="CUSTOMER_COMMITMENT",
            economic_mechanism="CUSTOMER_ALLOCATION",
            geography="GLOBAL",
            effective_period="2025-07-26/2033-12-31",
            scope_confidence=1.0,
        )
        result = MechanismScopeValidator().validate(
            scope=scope,
            contract=contract,
            component_id="earnings_visibility",
        )
        self.assertFalse(result.scope_match)
        self.assertEqual(result.status, "REROUTED_TO_OTHER_MECHANISM")
        self.assertEqual(
            result.rerouted_archetype_id,
            "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
        )
        self.assertTrue(result.original_gap_open)

    def test_adjacent_substrate_cannot_be_target_hbm_capacity(self) -> None:
        contract = load_mechanism_scope_contracts()[
            "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
        ]
        scope = BusinessMechanismScope(
            issuer_id="005930",
            business_segment="SEMICONDUCTOR_COMPONENT",
            product_family="PACKAGE_SUBSTRATE_ADJACENT",
            technology_family="PACKAGE_SUBSTRATE",
            customer_or_counterparty="",
            transaction_type="PRODUCT_PROFILE",
            economic_mechanism="INFORMATION_ONLY",
            geography="GLOBAL",
            effective_period="CURRENT",
            scope_confidence=0.9,
        )
        result = MechanismScopeValidator().validate(
            scope=scope,
            contract=contract,
            component_id="bottleneck_pricing",
        )
        self.assertFalse(result.scope_match)
        self.assertEqual(result.reason_code, "WRONG_PRODUCT_FAMILY")

    def test_mixed_memory_context_does_not_select_one_subtype_by_priority(
        self,
    ) -> None:
        claim = {
            "target_id": "TARGET",
            "raw_assertion": {
                "predicate": "reported actual revenue",
                "object_text": "quarterly consolidated revenue",
            },
            "document_context_excerpt": (
                "NAND shipment volume changed during the quarter. "
                "The issuer also disclosed its aggregate memory ASP."
            ),
        }
        scope = infer_business_mechanism_scope(
            claim,
            primitive_id="actual_earnings_conversion",
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        )
        self.assertEqual(scope.business_segment, "MEMORY")
        self.assertEqual(scope.product_family, "MEMORY_GENERIC")

    def test_mixed_foundry_and_memory_context_is_fail_closed(self) -> None:
        claim = {
            "target_id": "TARGET",
            "raw_assertion": {
                "predicate": "reported actual revenue",
                "object_text": "quarterly consolidated revenue",
            },
            "document_context_excerpt": (
                "Foundry revenue increased while memory ASP also changed."
            ),
        }
        scope = infer_business_mechanism_scope(
            claim,
            primitive_id="actual_earnings_conversion",
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        )
        self.assertEqual(scope.business_segment, "CORPORATE_GENERIC")
        self.assertEqual(scope.product_family, "CORPORATE_GENERIC")

    def test_issuer_consolidated_actuals_are_common_eps_fcf_only_contract(
        self,
    ) -> None:
        """가상 발행사의 연결 실제치는 섹터와 무관하게 같은 규칙을 쓴다."""

        validator = MechanismScopeValidator()
        contracts = load_mechanism_scope_contracts()
        common = ISSUER_CONSOLIDATED_ACTUAL_SCOPE_CONTRACT
        for archetype_id, contract in contracts.items():
            for _, transaction_type, economic_mechanism in common.metric_scope_rows:
                scope = BusinessMechanismScope(
                    issuer_id="SYNTHETIC-TARGET",
                    business_segment="CORPORATE_GENERIC",
                    product_family="CORPORATE_GENERIC",
                    technology_family="CORPORATE_GENERIC",
                    customer_or_counterparty="",
                    transaction_type=transaction_type,
                    economic_mechanism=economic_mechanism,
                    geography="GLOBAL",
                    effective_period="2026Q1",
                    scope_confidence=1.0,
                )
                self.assertTrue(
                    validator.validate(
                        scope=scope,
                        contract=contract,
                        component_id="eps_fcf_explosion",
                    ).scope_match,
                    archetype_id,
                )
                self.assertFalse(
                    validator.validate(
                        scope=scope,
                        contract=contract,
                        component_id="bottleneck_pricing",
                    ).scope_match,
                    archetype_id,
                )

        attributed = BusinessMechanismScope(
            issuer_id="SYNTHETIC-TARGET",
            business_segment="CORPORATE_GENERIC",
            product_family="HBM",
            technology_family="HBM",
            customer_or_counterparty="",
            transaction_type="CONSOLIDATED_REVENUE_ACTUAL",
            economic_mechanism="CONSOLIDATED_EARNINGS_ACTUAL",
            geography="GLOBAL",
            effective_period="2026Q1",
            scope_confidence=1.0,
        )
        self.assertFalse(
            validator.validate(
                scope=attributed,
                contract=contracts["C06_HBM_MEMORY_CUSTOMER_CAPACITY"],
                component_id="eps_fcf_explosion",
            ).scope_match
        )

    def test_operational_scope_audit_recomputes_from_frozen_leaves(self) -> None:
        audit = audit_business_mechanism_scope(repo_root=self.ROOT)
        artifact = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_business_mechanism_scope_audit.json"
            ).read_text()
        )
        self.assertEqual(audit, artifact)
        self.assertEqual(audit["status"], "BUSINESS_MECHANISM_SCOPE_PASS")
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertGreater(audit["wrong_scope_rejected_impact_count"], 0)
        self.assertGreater(audit["filtered_question_claim_count"], 0)


if __name__ == "__main__":
    unittest.main()
