import json
import unittest
from pathlib import Path


class E2RReconstructionPhase0BaselineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.repo_root = Path(__file__).resolve().parents[1]
        cls.docs = cls.repo_root / "docs" / "operational"

    def _load(self, name: str) -> dict:
        return json.loads((self.docs / name).read_text(encoding="utf-8"))

    def test_required_phase0_artifacts_exist(self) -> None:
        required = {
            "e2r_reconstruction_forensic_baseline.md",
            "e2r_runtime_call_graph_before.json",
            "e2r_duplicate_brain_stack_inventory.json",
            "e2r_current_conversion_funnel_baseline.json",
            "e2r_reconstruction_master_plan.md",
            "e2r_reconstruction_phase0_baseline.md",
            "e2r_legacy_artifact_classification.json",
        }
        self.assertEqual(
            {path.name for path in self.docs.iterdir() if path.name in required},
            required,
        )

    def test_baseline_preserves_not_ready_and_zero_full_thesis(self) -> None:
        funnel = self._load("e2r_current_conversion_funnel_baseline.json")
        self.assertEqual(funnel["official_verdict"], "MEANINGFUL_RUNTIME_PARITY_NOT_READY")
        self.assertEqual(funnel["current_leaf_counts"]["production_full_thesis_rows"], 0)
        self.assertEqual(funnel["current_leaf_counts"]["full_e2r_verified_score_rows"], 0)
        self.assertFalse(funnel["hard_truths"]["task_shells_are_evidence"])
        self.assertFalse(funnel["hard_truths"]["accepted_claim_total_proves_original_gap_closure"])

    def test_heuristic_counts_are_not_promoted_to_semantic_proof(self) -> None:
        funnel = self._load("e2r_current_conversion_funnel_baseline.json")
        self.assertIsNone(funnel["historical_corpus"]["semantic_case_count"])
        self.assertIsNone(funnel["historical_corpus"]["historical_replay_ready_case_count"])
        self.assertEqual(funnel["provisional_runtime_intelligence"]["executable_evidence_recipe_count"], 0)

        classification = self._load("e2r_legacy_artifact_classification.json")
        acceptance = classification["hard_acceptance"]
        self.assertFalse(acceptance["research_case_count_11394_counted_as_meaningful"])
        self.assertFalse(acceptance["source_route_pattern_count_1855_counted_as_recovered"])
        self.assertFalse(acceptance["task_shell_count_111_counted_as_evidence"])
        self.assertEqual(acceptance["status"], "PASS")

    def test_call_graph_records_production_reachable_duplicate_brain(self) -> None:
        graph = self._load("e2r_runtime_call_graph_before.json")
        entrypoints = {row["id"]: row for row in graph["entrypoints"]}
        self.assertTrue(entrypoints["census_v4_until_pass"]["production_reachable"])
        self.assertTrue(entrypoints["research_to_runtime_parity"]["production_reachable"])
        self.assertIn(
            "e2r.research_reverse.reports.write_research_reverse_bundle",
            entrypoints["research_to_runtime_parity"]["call_chain"],
        )
        self.assertIn(
            "e2r.source_routing.research_source_route_recovery.write_source_route_recovery_reports",
            entrypoints["research_to_runtime_parity"]["call_chain"],
        )

    def test_duplicate_inventory_names_canonical_target_and_fail_state(self) -> None:
        inventory = self._load("e2r_duplicate_brain_stack_inventory.json")
        self.assertEqual(inventory["canonical_target"], "src/e2r/research_brain")
        self.assertGreater(inventory["duplicate_schema_source_of_truth_count"], 1)
        self.assertGreater(inventory["production_reachable_primitive_name_route_guesser_count"], 0)
        self.assertEqual(
            inventory["baseline_acceptance"]["status"],
            "FAIL_EXPECTED_BEFORE_RECONSTRUCTION",
        )

    def test_legacy_classification_uses_only_goal_allowed_classes(self) -> None:
        classification = self._load("e2r_legacy_artifact_classification.json")
        allowed = set(classification["allowed_classes"])
        seen = {row["classification"] for row in classification["artifacts"]}
        self.assertTrue(seen)
        self.assertTrue(seen <= allowed)
        self.assertIn("RUNTIME_PROOF", seen)
        self.assertIn("HEURISTIC_RESEARCH_REVERSE", seen)
        self.assertIn("HEURISTIC_SOURCE_ROUTE", seen)

    def test_master_plan_covers_every_phase_and_required_fields(self) -> None:
        text = (self.docs / "e2r_reconstruction_master_plan.md").read_text(encoding="utf-8")
        for phase in range(17):
            self.assertIn(f"## Phase {phase} ", text)
        for required_field in (
            "문제:",
            "Root cause:",
            "제거할 legacy path:",
            "새 schema/API:",
            "Migration:",
            "구현 파일:",
            "테스트:",
            "Runtime acceptance:",
            "Rollback point:",
            "Commit message:",
        ):
            self.assertEqual(text.count(required_field), 17, required_field)


if __name__ == "__main__":
    unittest.main()
