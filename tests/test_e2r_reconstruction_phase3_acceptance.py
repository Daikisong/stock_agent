from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class E2RReconstructionPhase3AcceptanceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.path = REPO_ROOT / "e2r_reconstruction_phase3_acceptance.json"
        self.payload = json.loads(self.path.read_text(encoding="utf-8"))

    def test_status_is_compiler_scoped_and_not_runtime_ready(self) -> None:
        self.assertEqual(self.payload["phase"], 3)
        self.assertEqual(
            self.payload["status"],
            "CASE_LEVEL_SOURCE_VERIFICATION_COMPILER_PASS",
        )
        self.assertFalse(self.payload["production_runtime_ready"])
        self.assertNotIn("MEANINGFUL_E2R_RUNTIME_READY", self.path.read_text())

    def test_full_registry_does_not_overclaim_without_snapshots(self) -> None:
        full = self.payload["full_registry_without_registered_snapshots"]
        self.assertEqual(full["case_count"], 10920)
        self.assertEqual(full["historical_replay_ready_count"], 0)
        self.assertEqual(full["repair_task_count"], full["case_count"])
        self.assertGreater(full["source_state_counts"]["URL_PRESENT_UNVERIFIED"], 0)

    def test_controlled_snapshot_has_exactly_one_fully_checked_ready_case(self) -> None:
        controlled = self.payload["controlled_historical_snapshot_golden"]
        self.assertEqual(controlled["historical_replay_ready_count"], 1)
        self.assertEqual(controlled["ready_case_id"], "PHASE3_C15_HYUNDAI_READY")
        self.assertEqual(len(controlled["content_sha256"]), 64)
        self.assertFalse(controlled["current_score_eligible"])
        self.assertEqual(
            controlled["source_state_counts"]["URL_FETCHED_WRONG_SUBJECT"],
            1,
        )
        self.assertEqual(
            controlled["source_state_counts"]["URL_FETCHED_DATE_INVALID"],
            1,
        )

    def test_hard_acceptance_counts_are_all_zero(self) -> None:
        for key, value in self.payload["hard_acceptance"].items():
            self.assertEqual(value, 0, key)

    def test_mandatory_golden_is_ready_or_exactly_blocked(self) -> None:
        golden = self.payload["mandatory_phase2_golden"]
        self.assertEqual(golden["url_backed_case_count"], 3)
        self.assertEqual(golden["url_backed_ready_or_exact_blocker_count"], 3)
        self.assertEqual(golden["source_proxy_case_count"], 3)
        self.assertEqual(golden["source_proxy_planning_only_count"], 3)
        self.assertEqual(golden["historical_replay_ready_count"], 0)

    def test_phase3_operational_report_exists(self) -> None:
        report = (
            REPO_ROOT
            / "docs"
            / "operational"
            / "e2r_reconstruction_phase3_source_verification.md"
        )
        text = report.read_text(encoding="utf-8")
        self.assertIn("CASE_LEVEL_SOURCE_VERIFICATION_COMPILER_PASS", text)
        self.assertIn("URL_FETCHED_WRONG_SUBJECT", text)
        self.assertIn("Phase 4", text)


if __name__ == "__main__":
    unittest.main()
