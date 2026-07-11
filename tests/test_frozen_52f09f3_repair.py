from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.scoring.frozen_corpus_repair import (
    FROZEN_REPAIR_PASS,
    compile_frozen_52f09f3_repair_audit,
)


class Frozen52f09f3RepairTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]
    CONFIG = ROOT / "configs/e2r_frozen_52f09f3_repair_v1.json"
    ARTIFACT = (
        ROOT / "docs/operational/e2r_frozen_52f09f3_repair_audit.json"
    )

    @classmethod
    def setUpClass(cls) -> None:
        cls.actual = compile_frozen_52f09f3_repair_audit(
            config_path=cls.CONFIG
        )

    def test_frozen_repair_recompiles_to_committed_pass(self) -> None:
        expected = json.loads(self.ARTIFACT.read_text(encoding="utf-8"))
        self.assertEqual(self.actual, expected)
        self.assertEqual(self.actual["status"], FROZEN_REPAIR_PASS)
        self.assertEqual(self.actual["critical_count_sum"], 0)
        self.assertFalse(self.actual["search_or_fetch_performed"])

    def test_same_documents_claims_and_provenance_are_byte_identical(self) -> None:
        for target in self.actual["target_results"]:
            with self.subTest(target_id=target["target_id"]):
                frozen = target["frozen_input"]
                self.assertEqual(frozen["mismatched_leaves"], [])
                self.assertEqual(frozen["new_document_ids"], [])
                self.assertEqual(frozen["missing_document_ids"], [])
                self.assertEqual(frozen["document_payload_mismatch_ids"], [])
                self.assertEqual(
                    frozen["before_document_count"],
                    frozen["after_document_count"],
                )

    def test_hynix_supported_facts_and_capacity_counter_are_nonzero(self) -> None:
        target = self._target("000660")
        self.assertEqual(target["missing_required_supported_questions"], [])
        counter = target["counter_capacity"]
        self.assertTrue(counter["impact_ids"])
        self.assertTrue(
            set(counter["impact_ids"])
            <= set(counter["accounted_counter_impact_ids"])
        )
        repairs = target["before_after"]["missing_cap_impact_repairs"]
        self.assertTrue(repairs)
        self.assertTrue(all(row["repaired"] for row in repairs))

    def test_samsung_foundry_is_excluded_but_hbm_facts_remain(self) -> None:
        target = self._target("005930")
        foundry = target["foundry_scope"]
        self.assertTrue(foundry["source_claim_ids"])
        self.assertEqual(foundry["validated_credit_impact_ids"], [])
        self.assertEqual(foundry["forbidden_question_links"], [])
        self.assertTrue(foundry["rerouted_or_rejected_impacts"])
        self.assertEqual(target["missing_required_supported_questions"], [])
        self.assertEqual(
            target["missing_required_bounded_impact_labels"], []
        )
        self.assertEqual(
            {
                row["label"]
                for row in target["required_bounded_impacts"]
                if row["satisfied"]
            },
            {
                "hbm4_shipment_to_earnings_visibility",
                "memory_asp_to_pricing",
                "actual_earnings_bounded_conversion",
            },
        )

    def test_no_silent_zero_or_semantic_internal_error_remains(self) -> None:
        for target in self.actual["target_results"]:
            with self.subTest(target_id=target["target_id"]):
                for name in (
                    "partial_bridge_missing_cap_zero_count",
                    "supported_question_absent_component_count",
                    "positive_impact_internal_error_count",
                    "counter_capacity_impact_ignored_count",
                    "provider_error_count",
                ):
                    self.assertEqual(target["critical_counts"][name], 0)

    def _target(self, target_id: str):
        return next(
            row
            for row in self.actual["target_results"]
            if row["target_id"] == target_id
        )


if __name__ == "__main__":
    unittest.main()
