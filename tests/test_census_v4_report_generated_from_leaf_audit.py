import unittest

from tests.census_v4_test_helpers import census_v4_artifacts, read_json


class CensusV4ReportGeneratedFromLeafAuditTests(unittest.TestCase):
    def test_acceptance_report_declares_leaf_audit_source_and_matches_metrics(self):
        artifacts = census_v4_artifacts()
        root = artifacts["output_root"]
        leaf = artifacts["leaf_audit"]
        readiness = artifacts["readiness"]
        report = (root / "acceptance_report.md").read_text(encoding="utf-8")
        audit = read_json(root / "report_generation_audit.json")

        metrics = leaf["metrics"]
        self.assertEqual(audit["verdict"], "PASS")
        self.assertTrue(audit["report_generated_from_leaf_audit"])
        self.assertEqual(audit["report_metrics_source"], "leaf_artifact_audit.json")
        self.assertEqual(audit["readiness_source"], "readiness_verdict.json")
        self.assertEqual(audit["in_memory_summary_used_for_acceptance_count"], 0)
        self.assertEqual(audit["leaf_report_metric_mismatch_count"], 0)
        self.assertFalse(audit["report_only_status_change_allowed"])
        self.assertIn("report_generated_from_leaf_audit=true", report)
        self.assertEqual(
            readiness["stage_scope_notice"],
            "FULL_THESIS_STAGE_ROWS_PRESENT_SCOPE_GUARD_REQUIRED",
        )
        self.assertFalse(readiness["operational_stage_use_allowed"])
        self.assertEqual(readiness["full_thesis_stage_row_count"], metrics["full_thesis_stage_row_count"])
        self.assertEqual(
            readiness["full_thesis_refresh_queue_candidate_count"],
            metrics["full_thesis_refresh_queue_candidate_count"],
        )
        self.assertEqual(readiness["event_board_non_stage0_count"], metrics["event_board_non_stage0_count"])
        self.assertIn(
            f"0. Operator stage warning: stage_scope_notice={readiness['stage_scope_notice']}; "
            f"operational_stage_use_allowed={readiness['operational_stage_use_allowed']}; "
            f"full_thesis_rows={metrics['full_thesis_stage_row_count']}; "
            f"full_thesis_refresh_queue_candidates={metrics['full_thesis_refresh_queue_candidate_count']}; "
            f"full_e2r_verified_score_rows={metrics['full_e2r_verified_score_present_count']}; "
            f"event_board_non_stage0_rows={metrics['event_board_non_stage0_count']}",
            report,
        )
        self.assertIn(f"7. Leaf artifact audit: {leaf['verdict']}", report)
        self.assertIn(
            f"8. Eligible / Stage rows: {metrics['eligible_symbol_count']} / {metrics['stage_status_count']}",
            report,
        )
        self.assertIn("11. Score scale distribution:", report)
        self.assertIn(
            f"17a. Full thesis stage rows: {metrics['full_thesis_stage_row_count']}; "
            f"refresh queue candidates: {metrics['full_thesis_refresh_queue_candidate_count']}; "
            f"event-board non-Stage0 rows: {metrics['event_board_non_stage0_count']}; "
            f"operator_stage_scope_notice={metrics['operator_stage_scope_notice']}",
            report,
        )
        for score_scale, count in metrics["score_scale_distribution"].items():
            self.assertIn(repr(score_scale), report)
            self.assertIn(str(count), report)
        brain_gate = read_json(root / "brain_web_readiness_gate_audit.json")
        goal_matrix = read_json(root / "goal_requirement_matrix_audit.json")
        self.assertIn(
            f"5e. Goal requirement matrix: minimum_pass={goal_matrix['goal_completion_minimum_pass']}; "
            f"pass={goal_matrix['required_goal_completion_pass_count']}/{goal_matrix['required_goal_completion_count']}; "
            f"pending={goal_matrix['required_goal_completion_pending_count']}; "
            f"fail={goal_matrix['required_goal_completion_fail_count']}",
            report,
        )
        self.assertIn(
            f"25. Brain/Web readiness gate: {brain_gate['verdict']}; "
            f"pass_allowed={brain_gate['brain_web_evidence_pass_allowed']}; "
            f"minimum_gate_applies={brain_gate['minimum_gate_applies']}; "
            f"operational_minimum_count_gate_applies={brain_gate['operational_minimum_count_gate_applies']}; "
            f"minimum_required_counts={brain_gate['minimum_required_counts']}",
            report,
        )
        self.assertIn(f"42. Final verdict: {readiness['verdict']}", report)


if __name__ == "__main__":
    unittest.main()
