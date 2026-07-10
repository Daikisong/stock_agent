from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.runtime import TaskSatisfactionStatus


class E2RReconstructionPhase9AcceptanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.repo_root = Path(__file__).resolve().parents[1]
        cls.acceptance = json.loads(
            (cls.repo_root / "e2r_reconstruction_phase9_acceptance.json").read_text(
                encoding="utf-8"
            )
        )

    def test_status_is_phase_scoped_and_not_runtime_ready(self) -> None:
        self.assertEqual(self.acceptance["phase"], 9)
        self.assertEqual(
            self.acceptance["status"],
            "CONTRACT_BLIND_CLAIM_COMPILER_PASS",
        )
        self.assertFalse(self.acceptance["production_runtime_ready"])

    def test_raw_extractor_visibility_is_contract_blind(self) -> None:
        contract = self.acceptance["raw_extractor_contract"]
        self.assertTrue(contract["visible_target_identity"])
        self.assertTrue(contract["visible_as_of_date"])
        self.assertTrue(contract["visible_source_document_and_verified_anchor_context"])
        for key in (
            "primitive_gap_visible",
            "desired_archetype_visible",
            "score_visible",
            "stage_visible",
            "historical_outcome_visible",
        ):
            self.assertFalse(contract[key], key)
        self.assertTrue(contract["prompt_input_hash_preserved"])
        self.assertTrue(contract["response_hash_preserved"])

    def test_compilation_order_places_mapping_and_eligibility_last(self) -> None:
        order = self.acceptance["compilation_order"]
        self.assertEqual(order[0], "ANCHOR")
        self.assertLess(order.index("ENTITY_SUBJECT"), order.index("RECIPE_PRIMITIVE_MAPPING"))
        self.assertLess(order.index("CONTRADICTION_SUPERSESSION"), order.index("SCORE_ELIGIBILITY"))
        self.assertEqual(order[-1], "TASK_SATISFACTION")

    def test_all_task_satisfaction_statuses_are_frozen(self) -> None:
        expected = {status.value for status in TaskSatisfactionStatus}
        actual = self.acceptance["task_satisfaction_statuses"]
        self.assertEqual(set(actual), expected)
        self.assertTrue(all(actual.values()))

    def test_claim_audit_has_zero_critical_gaps_and_frozen_hash(self) -> None:
        audit = self.acceptance["claim_compiler_audit"]
        self.assertEqual(audit["status"], "CONTRACT_BLIND_CLAIM_COMPILER_PASS")
        self.assertEqual(audit["result_count"], 6)
        self.assertEqual(audit["direct_original_gap_closure_count"], 1)
        self.assertEqual(audit["rerouted_claim_event_count"], 1)
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertTrue(all(value == 0 for value in audit["critical_counts"].values()))
        self.assertEqual(
            audit["result_hash"],
            "dd1f97a90b17c6d35453063d63ecd0a16aa233de7706a9471a86df74f93f8c78",
        )
        self.assertFalse(audit["production_runtime_ready"])

    def test_legacy_rule_parser_and_mapping_fallback_have_zero_credit(self) -> None:
        migration = self.acceptance["legacy_migration"]
        self.assertFalse(migration["legacy_bundle_canonical_execution_allowed"])
        for key, value in migration.items():
            if key.endswith("_count"):
                self.assertEqual(value, 0, key)
        mapping = self.acceptance["mapping_contract"]
        self.assertTrue(mapping["no_deterministic_primitive_fallback"])
        self.assertFalse(mapping["mappingless_claim_score_eligible"])

    def test_report_explains_reroute_and_fixture_boundary(self) -> None:
        report = (
            self.repo_root
            / "docs"
            / "operational"
            / "e2r_reconstruction_phase9_contract_blind_claim_compiler.md"
        ).read_text(encoding="utf-8")
        self.assertIn("CONTRACT_BLIND_CLAIM_COMPILER_PASS", report)
        self.assertIn("production_runtime_ready=false", report)
        self.assertIn("REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN", report)
        self.assertIn("rule fallback", report)
        self.assertIn("fixture LLM", report)
        self.assertIn("원래 질문은 닫히지 않는다", report)


if __name__ == "__main__":
    unittest.main()
