from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.scoring.business_mechanism_scope import (
    BusinessMechanismScope,
    MechanismScopeValidator,
    audit_business_mechanism_scope,
    load_mechanism_scope_contracts,
)


class BusinessMechanismScopeTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

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
