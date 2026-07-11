from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.runtime.scoring_contracts import (
    audit_scoring_contract_catalog,
    load_archetype_scoring_contract,
    load_scoring_contract_catalog,
)


class CanonicalArchetypeScoringContractTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_every_profile_has_a_complete_100_point_component_contract(self) -> None:
        catalog = load_scoring_contract_catalog()
        audit = audit_scoring_contract_catalog(catalog)
        self.assertEqual(len(catalog.contracts), 36)
        self.assertEqual(audit["status"], "CANONICAL_SCORING_CONTRACT_PASS")
        self.assertEqual(audit["critical_count_sum"], 0)
        for contract in catalog.contracts.values():
            self.assertEqual(sum(contract.component_weights.values()), 100.0)

    def test_c06_uses_research_weights_not_source_task_count(self) -> None:
        contract = load_archetype_scoring_contract("C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertEqual(
            contract.component_weights,
            {
                "bottleneck_pricing": 19.0,
                "capital_allocation": 4.0,
                "earnings_visibility": 21.0,
                "eps_fcf_explosion": 24.0,
                "information_confidence": 5.0,
                "market_mispricing": 15.0,
                "valuation_rerating": 12.0,
            },
        )
        self.assertEqual(contract.edge_catalog_status, "EXPLICIT")
        self.assertIn(
            "bottleneck_pricing",
            contract.primitive_to_component_allowed_edges["memory_price_increase_mentioned"],
        )
        self.assertNotIn(
            "customer_preorder_or_allocation",
            contract.primitive_to_component_allowed_edges["memory_price_increase_mentioned"],
        )

    def test_unknown_archetype_does_not_silently_fallback(self) -> None:
        with self.assertRaisesRegex(ValueError, "unknown canonical archetype"):
            load_archetype_scoring_contract("C99_NOT_REAL")

    def test_operational_audit_is_recomputed_from_loader(self) -> None:
        catalog = load_scoring_contract_catalog()
        recomputed = audit_scoring_contract_catalog(catalog)
        artifact = json.loads(
            (self.ROOT / "docs/operational/e2r_canonical_scoring_contract_audit.json").read_text()
        )
        self.assertEqual(artifact["config_hash"], recomputed["config_hash"])
        self.assertEqual(artifact["contract_count"], recomputed["contract_count"])
        self.assertEqual(artifact["critical_counts"], recomputed["critical_counts"])
        c06 = catalog.get("C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertIsNotNone(c06)
        self.assertEqual(artifact["c06_contract"]["config_hash"], c06.config_hash)


if __name__ == "__main__":
    unittest.main()
