import unittest

from e2r.calibration.v12_runtime_execution_path_map import (
    build_v12_runtime_execution_path_map,
    render_v12_runtime_execution_path_map,
)


class V12RuntimeExecutionPathMapTests(unittest.TestCase):
    def test_runtime_path_separates_weight_support_from_feature_execution(self) -> None:
        weight_audit = {
            "summary": {
                "total_archetype_support_rows": 642,
                "total_archetype_positive_cases": 100,
                "total_archetype_counterexamples": 50,
                "archetype_weight_count": 2,
                "feature_layer_status_counts": {
                    "weight_supported_but_gate_axis_not_aligned": 1,
                    "weight_supported_but_candidate_not_exercised": 1,
                    "weight_supported_but_runtime_input_evidence_missing": 1,
                },
            },
            "rows": [
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "weight_support_row_count": 229,
                    "weight_support_positive_case_count": 40,
                    "weight_support_counterexample_count": 20,
                    "top_weight_axes": ["eps_fcf_explosion", "earnings_visibility", "bottleneck_pricing"],
                    "feature_layer_status": "weight_supported_but_gate_axis_not_aligned",
                    "runtime_gap_status": "runtime_bridge_axes_missing",
                    "runtime_candidate_count": 19,
                    "runtime_max_score": 76.7,
                    "missing_required_bridge_axes": ["backlog", "contract"],
                },
                {
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "weight_support_row_count": 413,
                    "weight_support_positive_case_count": 60,
                    "weight_support_counterexample_count": 30,
                    "top_weight_axes": ["capital_allocation", "valuation_rerating", "earnings_visibility"],
                    "feature_layer_status": "weight_supported_but_candidate_not_exercised",
                    "runtime_gap_status": "not_in_current_benchmark",
                    "runtime_candidate_count": 0,
                    "runtime_max_score": None,
                    "missing_required_bridge_axes": ["capital_return"],
                },
                {
                    "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                    "weight_support_row_count": 277,
                    "weight_support_positive_case_count": 25,
                    "weight_support_counterexample_count": 50,
                    "top_weight_axes": ["bottleneck_pricing", "earnings_visibility", "eps_fcf_explosion"],
                    "feature_layer_status": "weight_supported_but_weighted_gate_still_blocks",
                    "runtime_gap_status": "runtime_stage3_gate_blocked",
                    "runtime_candidate_count": 44,
                    "runtime_max_score": 72.9,
                    "missing_required_bridge_axes": [],
                },
                {
                    "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
                    "weight_support_row_count": 80,
                    "weight_support_positive_case_count": 12,
                    "weight_support_counterexample_count": 6,
                    "top_weight_axes": ["bottleneck_pricing", "earnings_visibility", "eps_fcf_explosion"],
                    "feature_layer_status": "weight_supported_but_runtime_input_evidence_missing",
                    "runtime_gap_status": "runtime_input_evidence_missing",
                    "runtime_candidate_count": 4,
                    "runtime_max_score": 0,
                    "missing_required_bridge_axes": ["margin", "backlog", "contract", "customer"],
                },
            ],
        }
        repair_board = {
            "summary": {"repair_lane_counts": {"candidate_funnel_or_benchmark_replay": 1}},
            "rows": [],
        }
        payload = build_v12_runtime_execution_path_map(
            weight_audit_payload=weight_audit,
            repair_board_payload=repair_board,
            field_audit_payload={"summary": {"primitive_support_status_counts": {"score_and_parser_exact": 3}}},
            hbm_trace_payload={"summary": {"sk_hynix_max_score": 76.7, "samsung_max_score": 68.6}},
            signal_audit_payload={"runtime_gap_status_counts": {"not_in_current_benchmark": 1}},
        )
        by_arch = {row["canonical_archetype_id"]: row for row in payload["archetype_rows"]}

        self.assertEqual(payload["summary"]["execution_layer_count"], 6)
        self.assertEqual(payload["summary"]["stop_layer_counts"]["parser_feature_bridge"], 1)
        self.assertEqual(payload["summary"]["stop_layer_counts"]["candidate_replay_archive"], 2)
        self.assertEqual(payload["summary"]["stop_layer_counts"]["stage_gate"], 1)
        self.assertEqual(by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["stop_layer"], "parser_feature_bridge")
        self.assertIn(
            "src/e2r/features.py::_backlog_rpo_visibility_score",
            by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["code_owners"],
        )
        self.assertEqual(
            by_arch["C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN"]["stop_layer"],
            "candidate_replay_archive",
        )
        self.assertEqual(
            by_arch["C02_POWER_GRID_DATACENTER_CAPEX"]["stop_layer"],
            "stage_gate",
        )
        self.assertEqual(
            by_arch["C01_ORDER_BACKLOG_MARGIN_BRIDGE"]["stop_layer"],
            "candidate_replay_archive",
        )

        report = render_v12_runtime_execution_path_map(payload)
        self.assertIn("HBM 특례", report)
        self.assertIn("src/e2r/staging.py::StageClassifier._is_stage_3_green", report)
        self.assertIn("시험 배점", report)


if __name__ == "__main__":
    unittest.main()
