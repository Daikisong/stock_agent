from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.runtime import AcquisitionMode


class E2RReconstructionPhase8AcceptanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.repo_root = Path(__file__).resolve().parents[1]
        cls.acceptance = json.loads(
            (cls.repo_root / "e2r_reconstruction_phase8_acceptance.json").read_text(
                encoding="utf-8"
            )
        )

    def test_status_is_phase_scoped_and_not_runtime_ready(self) -> None:
        self.assertEqual(self.acceptance["phase"], 8)
        self.assertEqual(
            self.acceptance["status"],
            "SOURCE_ACQUISITION_CONTRACT_PASS",
        )
        self.assertFalse(self.acceptance["production_runtime_ready"])

    def test_all_four_canonical_modes_are_frozen(self) -> None:
        expected = {mode.value for mode in AcquisitionMode}
        self.assertEqual(set(self.acceptance["modes"]), expected)
        self.assertTrue(all(self.acceptance["modes"].values()))

    def test_mode_and_discovery_safety_contracts_are_complete(self) -> None:
        self.assertTrue(all(self.acceptance["mode_contract"].values()))
        self.assertTrue(all(self.acceptance["discovery_contract"].values()))
        self.assertTrue(all(self.acceptance["document_selection_contract"].values()))

    def test_audit_has_zero_critical_gaps_and_frozen_hash(self) -> None:
        audit = self.acceptance["source_acquisition_audit"]
        self.assertEqual(audit["status"], "SOURCE_ACQUISITION_CONTRACT_PASS")
        self.assertEqual(audit["result_count"], 4)
        self.assertEqual(audit["document_count"], 3)
        self.assertEqual(audit["naver_terminal_candidate_count"], 2)
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertTrue(all(value == 0 for value in audit["critical_counts"].values()))
        self.assertEqual(
            audit["result_hash"],
            "cebcdea9ed8b1d0df34f5b30818ac6eeef2c4543ab921a59ebf3315e83d5b1bc",
        )
        self.assertFalse(audit["production_runtime_ready"])

    def test_v4_migration_blocks_undated_and_snapshot_promotion(self) -> None:
        migration = self.acceptance["legacy_migration"]
        self.assertTrue(all(migration.values()))
        self.assertTrue(migration["legacy_as_of_date_fallback_restored_to_unknown"])
        self.assertTrue(migration["undated_legacy_document_rejected_as_UNKNOWN_DATE"])
        self.assertTrue(migration["v4_report_replay_cannot_be_real_fetch"])

    def test_every_hard_acceptance_count_is_zero(self) -> None:
        hard = self.acceptance["hard_acceptance"]
        self.assertTrue(hard)
        for key, value in hard.items():
            if key.endswith("_count") or key == "critical_count_sum":
                self.assertEqual(value, 0, key)

    def test_report_explains_fixture_limit_and_document_boundary(self) -> None:
        report = (
            self.repo_root
            / "docs"
            / "operational"
            / "e2r_reconstruction_phase8_source_acquisition.md"
        ).read_text(encoding="utf-8")
        self.assertIn("SOURCE_ACQUISITION_CONTRACT_PASS", report)
        self.assertIn("production_runtime_ready=false", report)
        self.assertIn("UNKNOWN_DATE", report)
        self.assertIn("snippet은 문서가 아니다", report)
        self.assertIn("fixture/contract test", report)
        self.assertIn("QuestionSourceTask", report)
        self.assertIn("EvidenceRecipe", report)


if __name__ == "__main__":
    unittest.main()
