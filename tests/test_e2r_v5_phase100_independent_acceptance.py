from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from e2r.research_brain.researcher_mode.independent_acceptance import (
    FINAL_NOT_READY_LABEL,
    FINAL_READY_LABEL,
    REVIEWER_GATE_FAIL,
    REVIEWER_SPECS,
    compile_phase100_acceptance_bundle,
    validate_full_test_evidence,
    verification_tree_hash,
)
from e2r.research_brain.researcher_mode.canary_leaf_contract import (
    CANARY_MASTER_LEAF_FILES,
)


class E2RV5Phase100IndependentAcceptanceTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    @classmethod
    def setUpClass(cls) -> None:
        cls.bundle = compile_phase100_acceptance_bundle(cls.ROOT)
        cls.gate = cls.bundle["reviewer_gate"]

    def test_exact_a_to_j_roster_recomputes_independently(self) -> None:
        self.assertEqual(tuple(spec.reviewer_id for spec in REVIEWER_SPECS), tuple("ABCDEFGHIJ"))
        self.assertEqual(self.gate["reviewer_roster"], list("ABCDEFGHIJ"))
        self.assertEqual(self.gate["reviewer_count"], 10)
        self.assertTrue(self.gate["all_reviewers_independently_recomputed"])
        self.assertTrue(self.gate["one_critical_forces_failure"])
        for row in self.gate["reviewers"]:
            self.assertEqual(row["detector_run_count"], len(row["detector_ids"]))
            self.assertEqual(row["detector_pass_count"], len(row["detector_ids"]))
            self.assertEqual(row["status"], "PASS" if row["critical_count_sum"] == 0 else "FAIL")

    def test_current_gate_fails_exactly_instead_of_claiming_readiness(self) -> None:
        by_id = {row["reviewer_id"]: row for row in self.gate["reviewers"]}
        self.assertEqual(self.gate["status"], REVIEWER_GATE_FAIL)
        self.assertGreater(self.gate["critical_count_sum"], 0)
        self.assertEqual(self.gate["exact_verdict"], FINAL_NOT_READY_LABEL)
        self.assertFalse(self.gate["production_readiness_authority"])
        for reviewer_id in ("A", "C", "D", "E", "H", "I"):
            self.assertEqual(by_id[reviewer_id]["status"], "PASS")
        for reviewer_id in ("B", "F", "G", "J"):
            self.assertEqual(by_id[reviewer_id]["status"], "FAIL")
        self.assertNotEqual(self.gate["exact_verdict"], FINAL_READY_LABEL)

    def test_live_canary_reviewer_has_no_fixed_score_or_stage(self) -> None:
        reviewer = next(row for row in self.gate["reviewers"] if row["reviewer_id"] == "F")
        targets = reviewer["recomputed_metrics"]["targets"]
        self.assertEqual(len(targets), 2)
        self.assertTrue(all(not row["score_valid"] for row in targets))
        self.assertTrue(all(not row["stage_final"] for row in targets))
        self.assertTrue(
            all(
                "score" not in row or isinstance(row.get("score_valid"), bool)
                for row in targets
            )
        )

    def test_live_canary_reviewer_uses_exact_master_leaf_and_real_tree_hash(self) -> None:
        reviewer = next(row for row in self.gate["reviewers"] if row["reviewer_id"] == "F")
        targets = reviewer["recomputed_metrics"]["targets"]
        for row in targets:
            self.assertEqual(
                set(row["leaf_presence"]),
                set(CANARY_MASTER_LEAF_FILES.values()),
            )
            if row["output_root"]:
                self.assertTrue(row["actual_output_tree_hash"])
                self.assertEqual(
                    row["output_tree_hash_matches"],
                    row["output_tree_hash"] == row["actual_output_tree_hash"],
                )

    def test_component_calibration_recomputes_historical_thresholds(self) -> None:
        calibration = self.bundle["component_score_calibration"]
        metrics = calibration["historical_parity_metrics"]
        self.assertEqual(calibration["status"], "COMPONENT_SCORE_CALIBRATION_PASS")
        self.assertLessEqual(metrics["component_normalized_mae"], 0.12)
        self.assertLessEqual(metrics["total_proxy_mae"], 8.0)
        self.assertGreaterEqual(metrics["spearman_rank_correlation"], 0.85)
        self.assertGreaterEqual(metrics["stage_band_accuracy"], 0.90)
        self.assertEqual(calibration["critical_count_sum"], 0)
        self.assertEqual(
            calibration["strong_anchor_equivalent_undercredit_count"], 0
        )
        self.assertFalse(calibration["production_current_score_authority"])

    def test_stagecourt_audit_keeps_canonical_enum_and_current_pending(self) -> None:
        stagecourt = self.bundle["stagecourt_audit"]
        self.assertEqual(
            stagecourt["canonical_stage_enum"],
            ["0", "1", "2", "3-Green", "3-Yellow", "3-Red", "4A", "4B", "4C", "5"],
        )
        self.assertEqual(stagecourt["status"], "FINAL_STAGECOURT_PENDING")
        self.assertFalse(stagecourt["llm_stage_authority"])
        self.assertFalse(stagecourt["event_overlay_can_change_canonical_stage"])

    def test_required_dossiers_are_honest_pending_monitoring_documents(self) -> None:
        dossiers = self.bundle["dossiers"]
        self.assertEqual(len(dossiers), 2)
        for text in dossiers.values():
            self.assertIn("production research complete: `false`", text)
            self.assertIn("score valid: `false`", text)
            self.assertIn("FINAL StageCourt: `false`", text)
            self.assertNotIn("FULL_E2R_100", text)
            self.assertNotIn("비중 확대", text)

    def test_committed_phase100_artifacts_recompile_byte_for_byte(self) -> None:
        gate = json.loads(
            (self.ROOT / "docs/operational/e2r_v5_reviewer_gate.json").read_text(encoding="utf-8")
        )
        calibration = json.loads(
            (self.ROOT / "docs/operational/e2r_v5_component_score_calibration.json").read_text(encoding="utf-8")
        )
        stagecourt = json.loads(
            (self.ROOT / "docs/operational/e2r_v5_stagecourt_audit.json").read_text(encoding="utf-8")
        )
        readiness = (self.ROOT / "docs/operational/e2r_v5_final_readiness.md").read_text(encoding="utf-8")
        self.assertEqual(gate, self.gate)
        self.assertEqual(calibration, self.bundle["component_score_calibration"])
        self.assertEqual(stagecourt, self.bundle["stagecourt_audit"])
        self.assertEqual(readiness, self.bundle["final_readiness"])

        specs = json.loads(
            (self.ROOT / "configs/e2r_targeted_live_smoke_v1.json").read_text(encoding="utf-8")
        )["mandatory_targets"]
        paths = (
            self.ROOT / "docs/operational/e2r_v5_samsung_researcher_dossier.md",
            self.ROOT / "docs/operational/e2r_v5_hynix_researcher_dossier.md",
        )
        for spec, path in zip(specs, paths):
            self.assertEqual(
                path.read_text(encoding="utf-8"),
                self.bundle["dossiers"][spec["symbol"]],
            )

    def test_full_test_evidence_is_bound_to_current_executable_tree_when_present(self) -> None:
        path = self.ROOT / "docs/operational/e2r_v5_full_test_result.json"
        if not path.is_file():
            self.assertIn("CURRENT_FULL_TEST_EVIDENCE_MISSING_OR_STALE", self.gate["blockers"])
            return
        evidence = json.loads(path.read_text(encoding="utf-8"))
        current_hash = verification_tree_hash(self.ROOT)
        reviewer = next(row for row in self.gate["reviewers"] if row["reviewer_id"] == "J")
        if evidence["verification_tree_hash"] != current_hash:
            self.assertFalse(reviewer["recomputed_metrics"]["full_test_evidence_valid"])
            self.assertIn("CURRENT_FULL_TEST_EVIDENCE_MISSING_OR_STALE", self.gate["blockers"])
            return
        if evidence["status"] == "PASS":
            self.assertTrue(reviewer["recomputed_metrics"]["full_test_evidence_valid"])
            self.assertTrue(
                all(
                    reviewer["recomputed_metrics"]["full_test_evidence_validation"][
                        "checks"
                    ].values()
                )
            )

    def test_full_test_receipt_rejects_tampered_or_missing_source_log(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            log = root / "full.log"
            raw = "Ran 3 tests in 0.010s\n\nOK\n"
            log.write_text(raw, encoding="utf-8")
            evidence = {
                "status": "PASS",
                "full_discovery": True,
                "exit_code": 0,
                "verification_tree_stable_during_run": True,
                "verification_tree_hash": "TREE",
                "test_count": 3,
                "command": [
                    "/usr/bin/python",
                    "-m",
                    "unittest",
                    "discover",
                    "-s",
                    "tests",
                    "-v",
                ],
                "log_path": "full.log",
                "log_sha256": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
            }
            valid = validate_full_test_evidence(
                root,
                evidence,
                expected_tree_hash="TREE",
            )
            self.assertTrue(valid["valid"])

            log.write_text(raw.replace("OK", "FAILED (failures=1)"), encoding="utf-8")
            tampered = validate_full_test_evidence(
                root,
                evidence,
                expected_tree_hash="TREE",
            )
            self.assertFalse(tampered["valid"])
            self.assertFalse(tampered["checks"]["log_sha256_matches"])
            self.assertFalse(tampered["checks"]["log_reports_ok"])

            log.unlink()
            missing = validate_full_test_evidence(
                root,
                evidence,
                expected_tree_hash="TREE",
            )
            self.assertFalse(missing["valid"])
            self.assertFalse(missing["checks"]["log_exists"])

    def test_full_test_runner_publishes_log_only_after_test_process_finishes(self) -> None:
        source = (
            self.ROOT / "src/e2r/cli/run_e2r_v5_full_test_evidence.py"
        ).read_text(encoding="utf-8")
        self.assertIn('with running_log_path.open("w", encoding="utf-8")', source)
        self.assertIn("running_log_path.replace(log_path)", source)
        self.assertNotIn('with log_path.open("w", encoding="utf-8")', source)

    def test_reviewers_recompute_recall_capability_and_self_repair_gates(self) -> None:
        by_id = {row["reviewer_id"]: row for row in self.gate["reviewers"]}
        research_aperture = by_id["B"]
        for metric_name in (
            "critical_material_fact_recall",
            "counter_supersession_recall",
            "all_material_fact_recall",
            "component_research_topic_coverage",
        ):
            self.assertEqual(
                research_aperture["critical_counts"][
                    f"{metric_name}_threshold_failure_count"
                ],
                1,
            )
        runtime = by_id["J"]
        self.assertEqual(runtime["critical_counts"]["capability_regression_critical_count"], 0)
        self.assertEqual(runtime["critical_counts"]["self_repair_critical_count"], 0)

    def test_final_readiness_lists_blockers_and_forbids_ready_label(self) -> None:
        readiness = self.bundle["final_readiness"]
        self.assertIn(FINAL_NOT_READY_LABEL, readiness)
        self.assertIn("PHASE94_CLEAN_GOLD_RECALL_COMPARISON_PENDING", readiness)
        self.assertIn("LIVE_CANARY_DOSSIER_INCOMPLETE", readiness)
        self.assertIn("CANARY_LEAF_CONTRACT_PENDING", readiness)
        self.assertIn("FINAL_STAGECOURT_PENDING", readiness)
        self.assertIn(
            "CODEX_PROVIDER_USAGE_LIMIT_UNTIL_2026-07-20T03:58:00+09:00",
            readiness,
        )
        self.assertIn(f"`{FINAL_READY_LABEL}`는", readiness)
        self.assertNotIn(f"exact verdict: `{FINAL_READY_LABEL}`", readiness)


if __name__ == "__main__":
    unittest.main()
