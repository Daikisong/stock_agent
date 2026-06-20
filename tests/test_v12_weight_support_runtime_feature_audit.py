import unittest

from e2r.calibration.v12_weight_support_runtime_feature_audit import (
    build_v12_weight_support_runtime_feature_audit,
    render_v12_weight_support_runtime_feature_audit,
)


def weight_row(row_count: int, positive: int, counter: int) -> dict:
    return {
        "weights": {
            "eps_fcf_explosion": 24,
            "earnings_visibility": 21,
            "bottleneck_pricing": 19,
            "market_mispricing": 15,
            "valuation_rerating": 12,
            "capital_allocation": 4,
            "information_confidence": 5,
        },
        "green_policy": "green_allowed_with_evidence",
        "support": {
            "row_count": row_count,
            "unique_symbol_count": 10,
            "positive_case_count": positive,
            "counterexample_count": counter,
        },
    }


class V12WeightSupportRuntimeFeatureAuditTests(unittest.TestCase):
    def test_weight_support_is_separated_from_runtime_feature_execution(self) -> None:
        profile = {
            "profile_id": "test_profile",
            "enabled": True,
            "archetype_weights": {
                "C06_HBM_MEMORY_CUSTOMER_CAPACITY": weight_row(229, 40, 20),
                "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN": weight_row(413, 60, 30),
                "C01_ORDER_BACKLOG_MARGIN_BRIDGE": weight_row(80, 12, 6),
            },
        }
        repair_board = {
            "rows": [
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "runtime_gap_status": "runtime_bridge_axes_missing",
                    "repair_lanes": ["gate_bridge_axis_alignment", "runtime_field_strength"],
                    "primary_repair_lane": "gate_bridge_axis_alignment",
                    "runtime_candidate_count": 19,
                    "runtime_max_score": 76.7,
                    "missing_required_bridge_axes": ["backlog", "contract"],
                    "pair_retrospective_ready": False,
                },
                {
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "runtime_gap_status": "not_in_current_benchmark",
                    "repair_lanes": ["candidate_funnel_or_benchmark_replay"],
                    "primary_repair_lane": "candidate_funnel_or_benchmark_replay",
                    "runtime_candidate_count": 0,
                    "runtime_max_score": None,
                    "missing_required_bridge_axes": ["capital_return"],
                    "pair_retrospective_ready": False,
                },
                {
                    "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
                    "runtime_gap_status": "runtime_input_evidence_missing",
                    "repair_lanes": ["runtime_input_evidence_coverage"],
                    "primary_repair_lane": "runtime_input_evidence_coverage",
                    "runtime_candidate_count": 4,
                    "runtime_max_score": 0,
                    "missing_required_bridge_axes": ["margin", "backlog", "contract", "customer"],
                    "pair_retrospective_ready": True,
                },
            ]
        }
        signal_audit = {
            "rows": [
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "research_clean_green_count": 6,
                    "research_raw_stage3_green_count": 9,
                    "runtime_gap_status": "runtime_bridge_axes_missing",
                },
                {
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "research_clean_green_count": 32,
                    "research_raw_stage3_green_count": 37,
                    "runtime_gap_status": "not_in_current_benchmark",
                },
                {
                    "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
                    "research_clean_green_count": 4,
                    "research_raw_stage3_green_count": 6,
                    "runtime_gap_status": "runtime_input_evidence_missing",
                },
            ]
        }
        payload = build_v12_weight_support_runtime_feature_audit(
            weight_profile_payload=profile,
            repair_board_payload=repair_board,
            signal_audit_payload=signal_audit,
            field_audit_payload={"rows": []},
        )
        by_arch = {row["canonical_archetype_id"]: row for row in payload["rows"]}

        self.assertEqual(payload["summary"]["archetype_weight_count"], 3)
        self.assertEqual(payload["summary"]["total_archetype_support_rows"], 722)
        self.assertEqual(
            by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["feature_layer_status"],
            "weight_supported_but_gate_axis_not_aligned",
        )
        self.assertEqual(
            by_arch["C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN"]["feature_layer_status"],
            "weight_supported_but_candidate_not_exercised",
        )
        self.assertEqual(
            by_arch["C01_ORDER_BACKLOG_MARGIN_BRIDGE"]["feature_layer_status"],
            "weight_supported_but_runtime_input_evidence_missing",
        )

        report = render_v12_weight_support_runtime_feature_audit(payload)
        self.assertIn("Weight layer", report)
        self.assertIn("답안지의 수학 답이 빈칸", report)


if __name__ == "__main__":
    unittest.main()
