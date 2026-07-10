from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.runtime import (
    KNOWN_BAD_SUITE_AUDIT_SCHEMA_VERSION,
    KNOWN_BAD_SUITE_SCHEMA_VERSION,
    REQUIRED_KNOWN_BAD_PROBE_IDS,
)
from tests.known_bad_suite_fixture import build_known_bad_suite_fixture


class E2RReconstructionPhase15AcceptanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.repo_root = Path(__file__).resolve().parents[1]
        cls.acceptance = json.loads(
            (
                cls.repo_root / "e2r_reconstruction_phase15_acceptance.json"
            ).read_text(encoding="utf-8")
        )
        cls.result = build_known_bad_suite_fixture()

    def test_phase_status_schema_and_test_only_boundary_are_frozen(self) -> None:
        self.assertEqual(self.acceptance["phase"], 15)
        self.assertEqual(
            self.acceptance["status"],
            "UNIFIED_KNOWN_BAD_SUITE_PASS",
        )
        self.assertEqual(
            KNOWN_BAD_SUITE_SCHEMA_VERSION,
            "e2r_unified_known_bad_suite_v1",
        )
        self.assertEqual(
            KNOWN_BAD_SUITE_AUDIT_SCHEMA_VERSION,
            "e2r_unified_known_bad_suite_audit_v1",
        )
        self.assertTrue(self.acceptance["test_only"])
        self.assertFalse(self.acceptance["production_runtime_ready"])
        self.assertFalse(self.result.production_runtime_ready)

    def test_frozen_run_hash_counts_and_categories_recompute_exactly(self) -> None:
        frozen = self.acceptance["frozen_known_bad_run"]
        self.assertEqual(self.result.run_id, frozen["run_id"])
        self.assertEqual(self.result.manifest["leaf_hash"], frozen["leaf_hash"])
        self.assertEqual(
            len(self.result.observations),
            frozen["observed_probe_count"],
        )
        self.assertEqual(
            self.result.manifest["detected_probe_count"],
            frozen["detected_probe_count"],
        )
        self.assertEqual(
            self.result.manifest["undetected_probe_count"],
            frozen["undetected_probe_count"],
        )
        self.assertEqual(
            self.result.manifest["unique_detector_count"],
            frozen["unique_detector_count"],
        )
        self.assertEqual(
            self.result.manifest["category_counts"],
            self.acceptance["category_counts"],
        )

    def test_every_goal_requirement_has_an_executed_detector_and_signal(self) -> None:
        self.assertEqual(
            tuple(self.acceptance["required_probe_ids"]),
            REQUIRED_KNOWN_BAD_PROBE_IDS,
        )
        self.assertEqual(
            tuple(item.probe_id for item in self.result.observations),
            REQUIRED_KNOWN_BAD_PROBE_IDS,
        )
        self.assertTrue(all(item.detected for item in self.result.observations))
        self.assertTrue(
            all(item.detector_ids for item in self.result.observations)
        )
        self.assertTrue(all(item.signal_ids for item in self.result.observations))
        self.assertTrue(
            all(
                signal.startswith("unittest_pass:")
                for item in self.result.observations
                for signal in item.signal_ids
            )
        )
        coverage = self.acceptance["goal_coverage"]
        self.assertEqual(coverage["goal_requirement_count"], 25)
        self.assertEqual(coverage["suite_probe_count"], 26)
        self.assertEqual(coverage["c05_context_copy_split_count"], 2)
        self.assertTrue(coverage["all_goal_requirements_covered"])

    def test_all_phase_boundaries_and_required_mutation_families_are_covered(self) -> None:
        self.assertTrue(all(self.acceptance["phase_boundary_coverage"].values()))
        detector_contract = self.acceptance["detector_contract"]
        self.assertTrue(
            all(
                value
                for key, value in detector_contract.items()
                if key != "production_acceptance_credit"
            )
        )
        self.assertFalse(detector_contract["production_acceptance_credit"])
        self.assertTrue(
            all(self.acceptance["independent_mutation_audit"].values())
        )
        self.assertTrue(
            all(value == 0 for value in self.acceptance["hard_acceptance"].values())
        )

    def test_independent_audit_and_manifest_integrity_are_zero_critical(self) -> None:
        audit = self.acceptance["integrity_audit"]
        self.assertEqual(audit["status"], "UNIFIED_KNOWN_BAD_SUITE_PASS")
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertEqual(
            audit["critical_check_count"],
            len(self.result.audit["critical_counts"]),
        )
        self.assertEqual(audit["result_hash"], self.result.audit["result_hash"])
        self.assertTrue(
            all(value == 0 for value in self.result.audit["critical_counts"].values())
        )
        self.assertEqual(
            self.result.manifest["status"],
            "UNIFIED_KNOWN_BAD_SUITE_PASS",
        )
        self.assertFalse(self.result.manifest["production_runtime_ready"])

        verification = self.acceptance["verification"]
        self.assertEqual(
            verification["phase0_through_phase15_targeted_test_count"],
            264,
        )
        self.assertEqual(verification["phase15_contract_test_count"], 12)
        self.assertEqual(verification["full_suite_test_count"], 5569)
        self.assertEqual(verification["full_suite_failure_count"], 0)
        self.assertEqual(
            verification["phase16_resolved_baseline_failure_count"], 18
        )
        self.assertEqual(verification["new_failure_count"], 0)

    def test_operational_report_explains_examples_limits_and_phase16_handoff(self) -> None:
        report = (
            self.repo_root
            / "docs"
            / "operational"
            / "e2r_reconstruction_phase15_known_bad_suite.md"
        ).read_text(encoding="utf-8")
        self.assertIn("UNIFIED_KNOWN_BAD_SUITE_PASS", report)
        self.assertIn("26/26", report)
        self.assertIn("C05 context copy", report)
        self.assertIn("고객의 CAPA", report)
        self.assertIn("provider failure", report)
        self.assertIn("test-only", report)
        self.assertIn("production_runtime_ready=false", report)
        self.assertIn("Phase 16", report)


if __name__ == "__main__":
    unittest.main()
