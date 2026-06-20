import unittest

from e2r.calibration.v12_cross_archetype_score_loss_trace import (
    build_v12_cross_archetype_score_loss_trace,
    render_v12_cross_archetype_score_loss_trace,
)


class V12CrossArchetypeScoreLossTraceTests(unittest.TestCase):
    def test_trace_groups_ready_fixture_pairs_by_loss_layer(self) -> None:
        spec_payload = {
            "rows": [
                {
                    "role": "green",
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
                    "runtime_bridge_group": "semiconductor_customer_capacity_bridge",
                    "current_runtime_gap_status": "runtime_bridge_axes_missing",
                    "expected_runtime_primitives": ["customer_preorder_or_allocation", "hbm_capacity_constraint"],
                    "candidate": {"case_id": "C06_GREEN", "symbol": "000660", "as_of_date": "2024-04-25"},
                },
                {
                    "role": "guard",
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "current_runtime_gap_status": "runtime_bridge_axes_missing",
                    "candidate": {"case_id": "C06_GUARD", "symbol": "356860", "as_of_date": "2024-03-06"},
                },
                {
                    "role": "green",
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
                    "runtime_bridge_group": "financial_capital_return_bridge",
                    "current_runtime_gap_status": "not_in_current_benchmark",
                    "expected_runtime_primitives": ["buyback_cancelled", "roe_pbr_repricing"],
                    "candidate": {"case_id": "C21_GREEN", "symbol": "000810", "as_of_date": "2024-05-16"},
                },
                {
                    "role": "guard",
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "current_runtime_gap_status": "not_in_current_benchmark",
                    "candidate": {"case_id": "C21_GUARD", "symbol": "323410", "as_of_date": "2024-02-26"},
                },
                {
                    "role": "green",
                    "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                    "large_sector_id": "L1_INDUSTRIAL_INFRA",
                    "runtime_bridge_group": "industrial_backlog_margin_bridge",
                    "current_runtime_gap_status": "runtime_stage3_gate_blocked",
                    "expected_runtime_primitives": ["transformer_backlog", "datacenter_capex"],
                    "candidate": {"case_id": "C02_GREEN", "symbol": "267260", "as_of_date": "2024-02-16"},
                },
                {
                    "role": "guard",
                    "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                    "current_runtime_gap_status": "runtime_stage3_gate_blocked",
                    "candidate": {"case_id": "C02_GUARD", "symbol": "001440", "as_of_date": "2024-04-04"},
                },
                {
                    "role": "green",
                    "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
                    "large_sector_id": "L1_INDUSTRIAL_INFRA",
                    "runtime_bridge_group": "industrial_backlog_margin_bridge",
                    "current_runtime_gap_status": "runtime_input_evidence_missing",
                    "expected_runtime_primitives": ["order_backlog", "contract_margin_bridge"],
                    "candidate": {"case_id": "C01_GREEN", "symbol": "001440", "as_of_date": "2026-02-01"},
                },
            ]
        }
        coverage_payload = {
            "archetypes": [
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "runtime_gap_status": "runtime_bridge_axes_missing",
                    "runtime_candidate_count": 19,
                    "runtime_max_score": 76.7639,
                    "missing_required_bridge_axes": ["backlog", "contract"],
                    "top_failed_gates": [{"gate": "failed_stage3_bottleneck", "count": 19}],
                },
                {
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "runtime_gap_status": "not_in_current_benchmark",
                    "runtime_candidate_count": 0,
                    "runtime_max_score": None,
                    "missing_required_bridge_axes": ["capital_return", "valuation_repricing", "guard_risk"],
                    "top_failed_gates": [],
                },
                {
                    "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                    "runtime_gap_status": "runtime_stage3_gate_blocked",
                    "runtime_candidate_count": 44,
                    "runtime_max_score": 72.9633,
                    "missing_required_bridge_axes": [],
                    "top_failed_gates": [{"gate": "failed_stage3_total_score", "count": 44}],
                },
                {
                    "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
                    "runtime_gap_status": "runtime_input_evidence_missing",
                    "runtime_candidate_count": 4,
                    "runtime_max_score": 0,
                    "missing_required_bridge_axes": ["margin", "backlog", "contract", "customer"],
                    "top_failed_gates": [],
                },
            ]
        }

        payload = build_v12_cross_archetype_score_loss_trace(
            spec_payload=spec_payload,
            coverage_payload=coverage_payload,
        )

        self.assertEqual(payload["ready_archetype_count"], 4)
        self.assertEqual(payload["spec_row_count"], 7)
        self.assertEqual(payload["role_counts"], {"green": 4, "guard": 3})
        self.assertEqual(
            payload["gap_status_counts_by_archetype"],
            {
                "not_in_current_benchmark": 1,
                "runtime_bridge_axes_missing": 1,
                "runtime_input_evidence_missing": 1,
                "runtime_stage3_gate_blocked": 1,
            },
        )
        self.assertEqual(payload["missing_required_bridge_axis_counts"]["capital_return"], 1)
        report = render_v12_cross_archetype_score_loss_trace(payload)

        self.assertIn("HBM에 점수를 더 주기 위한 문서가 아니다", report)
        self.assertIn("C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", report)
        self.assertIn("candidate_funnel_or_replay_coverage", report)
        self.assertIn("research_axis_to_runtime_field_translation", report)
        self.assertIn("runtime_input_evidence_coverage", report)
        self.assertIn("weighted_component_or_stage3_gate", report)


if __name__ == "__main__":
    unittest.main()
