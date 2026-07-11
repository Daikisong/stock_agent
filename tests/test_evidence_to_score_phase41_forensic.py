from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class EvidenceToScorePhase41ForensicTests(unittest.TestCase):
    def test_forensic_artifacts_record_the_reachable_legacy_bridge(self) -> None:
        inventory = json.loads(
            (ROOT / "docs/operational/e2r_current_score_contract_inventory.json").read_text()
        )
        self.assertEqual(
            inventory["critical_counts"]["production_balanced_points_usage_count"],
            1,
        )
        self.assertFalse(inventory["current_live_contract"]["profile_loaded"])

    def test_c06_canonical_profile_is_not_the_balanced_live_rule(self) -> None:
        profile = json.loads(
            (ROOT / "configs/e2r_archetype_weight_profile_v2_2.json").read_text()
        )
        inventory = json.loads(
            (ROOT / "docs/operational/e2r_current_score_contract_inventory.json").read_text()
        )
        weights = profile["archetype_weights"]["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["weights"]
        self.assertEqual(weights, inventory["canonical_profile"]["weights"])
        self.assertEqual(sum(weights.values()), 100.0)
        self.assertNotEqual(sorted(weights.values()), sorted(inventory["current_live_contract"]["points"]))

    def test_mapping_loss_inventory_names_all_structural_loss_paths(self) -> None:
        inventory = json.loads(
            (ROOT / "docs/operational/e2r_claim_mapping_loss_inventory.json").read_text()
        )
        self.assertEqual(inventory["production_structural_loss_path_count"], 3)
        self.assertFalse(
            inventory["required_separation"]["original_gap_closed_by_rerouted"]
        )

    def test_runtime_ready_is_reclassified_until_scoring_bridge_closes(self) -> None:
        text = (
            ROOT
            / "docs/operational/e2r_evidence_to_score_current_state_reclassification.md"
        ).read_text()
        self.assertIn("ORGANIC_EVIDENCE_TO_SCORE_BRIDGE_NOT_READY", text)
        self.assertIn("MEANINGFUL_E2R_SCORING_NOT_READY", text)
        self.assertIn("organic accepted claim은 0건", text)


if __name__ == "__main__":
    unittest.main()
