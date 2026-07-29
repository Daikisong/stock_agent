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
    REVIEWER_GATE_PASS,
    REVIEWER_SPECS,
    compile_phase100_acceptance_bundle,
    validate_full_test_evidence,
    verification_tree_hash,
)
from e2r.research_brain.researcher_mode.canary_leaf_contract import (
    CANARY_MASTER_LEAF_FILES,
)
from e2r.research_brain.researcher_mode import (
    independent_acceptance as acceptance_module,
)
from e2r.research_brain.researcher_mode.full_thesis_gold_benchmark import (
    PHASE93_POST_RUN_PASS,
    PHASE93_RECALL_THRESHOLDS,
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

    def test_current_gate_verdict_exactly_matches_critical_truth(self) -> None:
        critical_sum = self.gate["critical_count_sum"]
        failed_reviewers = [
            row["reviewer_id"]
            for row in self.gate["reviewers"]
            if row["critical_count_sum"] > 0
        ]
        self.assertEqual(self.gate["failed_reviewers"], failed_reviewers)
        if critical_sum == 0:
            self.assertEqual(self.gate["status"], REVIEWER_GATE_PASS)
            self.assertEqual(self.gate["exact_verdict"], FINAL_READY_LABEL)
            self.assertTrue(self.gate["production_readiness_authority"])
            self.assertEqual(failed_reviewers, [])
            self.assertEqual(self.gate["blockers"], [])
            self.assertTrue(
                all(row["status"] == "PASS" for row in self.gate["reviewers"])
            )
        else:
            self.assertEqual(self.gate["status"], REVIEWER_GATE_FAIL)
            self.assertEqual(self.gate["exact_verdict"], FINAL_NOT_READY_LABEL)
            self.assertFalse(self.gate["production_readiness_authority"])
            self.assertTrue(failed_reviewers)
            self.assertNotEqual(self.gate["exact_verdict"], FINAL_READY_LABEL)

    def test_live_canary_reviewer_has_no_fixed_score_or_stage(self) -> None:
        by_id = {row["reviewer_id"]: row for row in self.gate["reviewers"]}
        reviewer = by_id["F"]
        targets = reviewer["recomputed_metrics"]["targets"]
        self.assertEqual(len(targets), 2)
        self.assertEqual({row["target_id"] for row in targets}, {"005930", "000660"})
        self.assertEqual(
            reviewer["critical_counts"]["incomplete_production_research_count"],
            sum(not row["production_research_complete"] for row in targets),
        )
        stage_reviewer = by_id["G"]
        expected_stagecourt_leaf_missing = sum(
            not row["leaf_presence"].get("atomic_stage_decision.json")
            or not row["leaf_presence"].get("stagecourt_trace.json")
            for row in targets
        )
        self.assertEqual(
            stage_reviewer["critical_counts"]["canary_score_valid_missing_count"],
            sum(not row["score_valid"] for row in targets),
        )
        self.assertEqual(
            stage_reviewer["critical_counts"]["canary_final_stagecourt_missing_count"],
            expected_stagecourt_leaf_missing,
        )
        self.assertTrue(
            all(
                isinstance(row["production_research_complete"], bool)
                and isinstance(row["score_valid"], bool)
                and isinstance(row["stage_final"], bool)
                for row in targets
            )
        )
        if self.gate["critical_count_sum"] == 0:
            self.assertTrue(
                all(
                    row["production_research_complete"]
                    and row["score_valid"]
                    and row["stage_final"]
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

    def test_stagecourt_audit_keeps_canonical_enum_and_reports_current_truth(self) -> None:
        stagecourt = self.bundle["stagecourt_audit"]
        self.assertEqual(
            stagecourt["canonical_stage_enum"],
            ["0", "1", "2", "3-Green", "3-Yellow", "3-Red", "4A", "4B", "4C", "5"],
        )
        self.assertFalse(stagecourt["llm_stage_authority"])
        self.assertFalse(stagecourt["event_overlay_can_change_canonical_stage"])
        expected_critical = sum(stagecourt["critical_counts"].values())
        self.assertEqual(stagecourt["critical_count_sum"], expected_critical)
        self.assertEqual(
            stagecourt["status"],
            "FINAL_STAGECOURT_PASS"
            if expected_critical == 0
            else "FINAL_STAGECOURT_PENDING",
        )
        if self.gate["critical_count_sum"] == 0:
            self.assertEqual(expected_critical, 0)
            self.assertEqual(stagecourt["status"], "FINAL_STAGECOURT_PASS")
            self.assertTrue(
                all(
                    row["score_valid"] and row["stage_final"]
                    for row in stagecourt["targets"]
                )
            )

    def test_required_dossiers_truthfully_match_current_canary_state(self) -> None:
        dossiers = self.bundle["dossiers"]
        self.assertEqual(len(dossiers), 2)
        reviewer = next(
            row for row in self.gate["reviewers"] if row["reviewer_id"] == "F"
        )
        targets = {
            row["target_id"]: row
            for row in reviewer["recomputed_metrics"]["targets"]
        }
        self.assertEqual(set(dossiers), set(targets))
        for target_id, text in dossiers.items():
            row = targets[target_id]
            self.assertIn(
                "production research complete: "
                f"`{str(row['production_research_complete']).lower()}`",
                text,
            )
            self.assertIn(
                f"score valid: `{str(row['score_valid']).lower()}`",
                text,
            )
            self.assertIn(
                f"FINAL StageCourt: `{str(row['stage_final']).lower()}`",
                text,
            )
            self.assertIn(
                f"complete component memos: `{row['component_memo_count']}` / `7`",
                text,
            )
            self.assertNotIn("FULL_E2R_100", text)
            self.assertNotIn("비중 확대", text)
        if self.gate["critical_count_sum"] == 0:
            for row in targets.values():
                self.assertTrue(row["production_research_complete"])
                self.assertTrue(row["score_valid"])
                self.assertTrue(row["stage_final"])
                self.assertEqual(row["component_memo_count"], 7)
                self.assertEqual(row["canary_leaf_contract_critical_count"], 0)
                self.assertTrue(all(row["leaf_presence"].values()))

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
        metrics = research_aperture["recomputed_metrics"]
        for metric_name in (
            "critical_material_fact_recall",
            "counter_supersession_recall",
            "all_material_fact_recall",
            "component_research_topic_coverage",
        ):
            value = metrics.get(metric_name)
            threshold = metrics["thresholds"].get(f"{metric_name}_min")
            expected_failure = int(
                not isinstance(value, (int, float))
                or isinstance(value, bool)
                or not isinstance(threshold, (int, float))
                or isinstance(threshold, bool)
                or float(value) < float(threshold)
            )
            self.assertEqual(
                research_aperture["critical_counts"][
                    f"{metric_name}_threshold_failure_count"
                ],
                expected_failure,
            )
        runtime = by_id["J"]
        self.assertEqual(runtime["critical_counts"]["capability_regression_critical_count"], 0)
        self.assertEqual(runtime["critical_counts"]["self_repair_critical_count"], 0)

    def test_actual_phase93_post_run_pass_closes_reviewer_b_recall_gate(self) -> None:
        metrics = {
            name.removesuffix("_min"): threshold
            for name, threshold in PHASE93_RECALL_THRESHOLDS.items()
        }
        result = acceptance_module._review_b(
            {
                "documents": {
                    "legacy": {
                        "critical_count_sum": 0,
                        "metric_values": {
                            "legacy_valid_material_fact_recall": 1.0,
                        },
                    },
                    "source_graph": {"critical_count_sum": 0},
                    "gold": {
                        "critical_count_sum": 0,
                        "post_run_comparison": {
                            "status": PHASE93_POST_RUN_PASS,
                            "thresholds": dict(PHASE93_RECALL_THRESHOLDS),
                            **metrics,
                        },
                    },
                },
            },
            self.ROOT,
        )
        self.assertEqual(sum(result["critical_counts"].values()), 0)
        self.assertEqual(result["blockers"], [])

    def test_final_readiness_matches_gate_and_never_claims_false_ready(self) -> None:
        readiness = self.bundle["final_readiness"]
        critical_sum = self.gate["critical_count_sum"]
        self.assertIn(
            f"reviewer critical sum: `{critical_sum}`",
            readiness,
        )
        self.assertIn(
            f"reviewer gate: `{self.gate['status']}`",
            readiness,
        )
        for blocker in self.gate["blockers"]:
            self.assertIn(f"- `{blocker}`", readiness)
        self.assertIn(f"`{FINAL_READY_LABEL}`는", readiness)
        if critical_sum == 0:
            self.assertEqual(self.gate["blockers"], [])
            self.assertIn(f"exact verdict: `{FINAL_READY_LABEL}`", readiness)
            self.assertNotIn(
                f"exact verdict: `{FINAL_NOT_READY_LABEL}`",
                readiness,
            )
            self.assertIn("StageCourt acceptance: `FINAL_STAGECOURT_PASS`", readiness)
            for target_id in ("005930", "000660"):
                dossier = self.bundle["dossiers"][target_id]
                self.assertIn("production research complete: `true`", dossier)
                self.assertIn("score valid: `true`", dossier)
                self.assertIn("FINAL StageCourt: `true`", dossier)
        else:
            self.assertIn(f"exact verdict: `{FINAL_NOT_READY_LABEL}`", readiness)
            self.assertNotIn(f"exact verdict: `{FINAL_READY_LABEL}`", readiness)


if __name__ == "__main__":
    unittest.main()
