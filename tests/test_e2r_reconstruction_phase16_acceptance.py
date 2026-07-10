from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.runtime import REQUIRED_COMMAND_HASH_CATEGORIES


class E2RReconstructionPhase16AcceptanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.repo_root = Path(__file__).resolve().parents[1]
        cls.acceptance = json.loads(
            (
                cls.repo_root / "e2r_reconstruction_phase16_acceptance.json"
            ).read_text(encoding="utf-8")
        )

    def test_phase_status_and_external_readiness_boundary_are_explicit(self) -> None:
        self.assertEqual(self.acceptance["phase"], 16)
        self.assertEqual(
            self.acceptance["status"], "PHASE16_RUNTIME_COMMAND_AUDIT_PASS"
        )
        self.assertEqual(
            self.acceptance["overall_readiness"],
            "EXTERNAL_SOURCE_BLOCKER_NOT_READY",
        )
        self.assertTrue(self.acceptance["phase_internal_complete"])
        self.assertFalse(self.acceptance["production_runtime_ready"])

    def test_four_official_commands_and_six_hash_categories_are_frozen(self) -> None:
        commands = self.acceptance["canonical_commands"]
        self.assertEqual(set(commands), {"compile", "replay", "current", "census"})
        self.assertEqual(commands["compile"]["observed_exit_code"], 0)
        self.assertEqual(commands["replay"]["observed_exit_code"], 0)
        self.assertEqual(commands["current"]["observed_exit_code"], 3)
        self.assertEqual(commands["census"]["observed_exit_code"], 3)
        self.assertEqual(
            tuple(
                self.acceptance["reproducibility_contract"][
                    "required_hash_categories"
                ]
            ),
            REQUIRED_COMMAND_HASH_CATEGORIES,
        )
        self.assertTrue(
            all(
                value
                for key, value in self.acceptance[
                    "reproducibility_contract"
                ].items()
                if key != "required_hash_categories"
            )
        )

    def test_compile_and_replay_observations_keep_source_gaps_visible(self) -> None:
        compile_observation = self.acceptance["canonical_compile_observation"]
        self.assertEqual(compile_observation["artifact_count"], 2260)
        self.assertEqual(compile_observation["historical_case_count"], 10920)
        self.assertEqual(compile_observation["historical_replay_ready_source_count"], 0)
        self.assertEqual(compile_observation["source_repair_task_count"], 10920)
        self.assertEqual(compile_observation["critical_count_sum"], 0)
        replay = self.acceptance["canonical_replay_observation"]
        self.assertEqual(replay["registry_archetype_count"], 36)
        self.assertEqual(replay["exact_source_blocker_archetype_count"], 36)
        self.assertEqual(replay["future_leakage_count"], 0)
        self.assertEqual(replay["source_proxy_score_credit_count"], 0)
        self.assertFalse(replay["production_runtime_ready"])

    def test_current_pending_and_provenance_rules_cannot_be_misread_as_score(self) -> None:
        boundary = self.acceptance["production_current_boundary"]
        self.assertEqual(boundary["canonical_stage"], "0")
        self.assertFalse(boundary["score_valid"])
        self.assertIsNone(boundary["raw_reference_score"])
        self.assertFalse(boundary["new_live_scraping_or_api_wiring_added"])
        self.assertTrue(boundary["production_claim_rejects_snapshot_or_reserved_test_url"])
        self.assertTrue(
            boundary[
                "production_claim_rejects_impossible_publication_availability_order"
            ]
        )

    def test_independent_review_and_final_ready_gate_are_fail_closed(self) -> None:
        review = self.acceptance["independent_review_contract"]
        self.assertEqual(review["reviewer_ids"], ["A", "B", "C", "D", "E"])
        self.assertTrue(review["each_reviewer_reads_leaf_artifacts_independently"])
        self.assertTrue(review["watchlist_projection_mutation_is_detected"])
        self.assertTrue(review["production_provenance_mutation_is_detected"])
        final = self.acceptance["final_audit_boundary"]
        self.assertEqual(final["observed_status"], "EXTERNAL_SOURCE_BLOCKER_NOT_READY")
        self.assertFalse(final["production_runtime_ready"])
        self.assertTrue(final["disabling_live_requirement_is_itself_critical"])
        self.assertTrue(all(value == 0 for value in self.acceptance["hard_acceptance"].values()))

    def test_operational_report_explains_results_limits_and_easy_examples(self) -> None:
        report = (
            self.repo_root
            / "docs"
            / "operational"
            / "e2r_reconstruction_phase16_runtime_commands.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "EXTERNAL_SOURCE_BLOCKER_NOT_READY",
            "HISTORICAL_REPLAY_PARITY_PASS",
            "CURRENT_KRX_UNIVERSE_AND_LIVE_SOURCE_INPUT_MANIFEST_UNAVAILABLE",
            "Stage 0 / Source Pending",
            "Reviewer A–E",
            "snapshot://",
            "MEANINGFUL_E2R_RUNTIME_READY",
            "production_runtime_ready=false",
        ):
            self.assertIn(phrase, report)


if __name__ == "__main__":
    unittest.main()
