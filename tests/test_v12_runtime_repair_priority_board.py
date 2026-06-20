import unittest

from e2r.calibration.v12_runtime_repair_priority_board import (
    build_v12_runtime_repair_priority_board,
    render_v12_runtime_repair_priority_board,
)


class V12RuntimeRepairPriorityBoardTests(unittest.TestCase):
    def test_board_separates_candidate_field_contract_and_gate_alignment_repairs(self) -> None:
        signal_payload = {
            "rows": [
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "runtime_gap_status": "runtime_bridge_axes_missing",
                    "diagnosis": "research_signal_not_structured_into_runtime_fields",
                    "research_clean_green_count": 6,
                    "research_raw_stage3_green_count": 9,
                    "runtime_candidate_count": 19,
                    "runtime_max_score": 76.7,
                    "missing_required_bridge_axes": ["backlog", "contract"],
                },
                {
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "runtime_gap_status": "not_in_current_benchmark",
                    "diagnosis": "research_green_fixture_not_archived_for_runtime_replay",
                    "research_clean_green_count": 32,
                    "research_raw_stage3_green_count": 37,
                    "runtime_candidate_count": 0,
                    "runtime_max_score": None,
                    "missing_required_bridge_axes": ["capital_return"],
                },
                {
                    "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
                    "runtime_gap_status": "runtime_bridge_axes_missing",
                    "diagnosis": "research_signal_not_structured_into_runtime_fields",
                    "research_clean_green_count": 12,
                    "research_raw_stage3_green_count": 19,
                    "runtime_candidate_count": 3,
                    "runtime_max_score": 40.0,
                    "missing_required_bridge_axes": ["software_retention"],
                },
                {
                    "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                    "runtime_gap_status": "runtime_stage3_gate_blocked",
                    "diagnosis": "weighted_stage3_gate_blocks_after_fields_present",
                    "research_clean_green_count": 3,
                    "research_raw_stage3_green_count": 5,
                    "runtime_candidate_count": 44,
                    "runtime_max_score": 72.9,
                    "missing_required_bridge_axes": [],
                },
                {
                    "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
                    "runtime_gap_status": "runtime_input_evidence_missing",
                    "diagnosis": "runtime_candidate_input_evidence_missing_for_bridge",
                    "research_clean_green_count": 4,
                    "research_raw_stage3_green_count": 6,
                    "runtime_candidate_count": 4,
                    "runtime_max_score": 0,
                    "missing_required_bridge_axes": ["margin", "backlog", "contract", "customer"],
                },
            ]
        }
        field_payload = {
            "rows": [
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "missing_feature_parser_contract_count": 0,
                    "missing_feature_parser_contract_primitives": [],
                    "axis_contract_statuses": [
                        {"axis": "backlog", "status": "bridge_spec_axis_present_but_runtime_field_missing_or_too_weak"},
                        {"axis": "contract", "status": "required_by_gate_but_absent_from_bridge_spec"},
                    ],
                },
                {
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "missing_feature_parser_contract_count": 0,
                    "missing_feature_parser_contract_primitives": [],
                    "axis_contract_statuses": [
                        {
                            "axis": "capital_return",
                            "status": "bridge_spec_axis_present_but_runtime_field_missing_or_too_weak",
                        }
                    ],
                },
                {
                    "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
                    "missing_feature_parser_contract_count": 5,
                    "missing_feature_parser_contract_primitives": [
                        "arpu_growth_pct",
                        "ad_revenue_growth_pct",
                        "take_rate_improvement",
                    ],
                    "axis_contract_statuses": [
                        {"axis": "software_retention", "status": "required_by_gate_but_absent_from_bridge_spec"}
                    ],
                },
                {
                    "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                    "missing_feature_parser_contract_count": 1,
                    "missing_feature_parser_contract_primitives": ["datacenter_customer"],
                    "axis_contract_statuses": [{"axis": "contract", "status": "runtime_present_but_not_explicit_in_bridge_spec"}],
                },
                {
                    "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
                    "missing_feature_parser_contract_count": 0,
                    "missing_feature_parser_contract_primitives": [],
                    "axis_contract_statuses": [],
                },
            ]
        }
        readiness_payload = {
            "archetype_pair_rows": [
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "green_retrospective_ready": True,
                    "guard_retrospective_ready": False,
                    "pair_retrospective_ready": False,
                },
                {
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "green_retrospective_ready": False,
                    "guard_retrospective_ready": False,
                    "pair_retrospective_ready": False,
                },
                {
                    "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
                    "green_retrospective_ready": False,
                    "guard_retrospective_ready": False,
                    "pair_retrospective_ready": False,
                },
                {
                    "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                    "green_retrospective_ready": True,
                    "guard_retrospective_ready": False,
                    "pair_retrospective_ready": False,
                },
                {
                    "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
                    "green_retrospective_ready": True,
                    "guard_retrospective_ready": True,
                    "pair_retrospective_ready": True,
                },
            ]
        }

        payload = build_v12_runtime_repair_priority_board(
            signal_audit_payload=signal_payload,
            field_audit_payload=field_payload,
            readiness_payload=readiness_payload,
        )
        by_arch = {row["canonical_archetype_id"]: row for row in payload["rows"]}

        self.assertEqual(
            by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["primary_repair_lane"],
            "gate_bridge_axis_alignment",
        )
        self.assertEqual(
            by_arch["C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN"]["primary_repair_lane"],
            "candidate_funnel_or_benchmark_replay",
        )
        self.assertEqual(
            by_arch["C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE"]["primary_repair_lane"],
            "parser_feature_field_contract",
        )
        self.assertEqual(
            by_arch["C02_POWER_GRID_DATACENTER_CAPEX"]["primary_repair_lane"],
            "weighted_gate_threshold_or_component_balance",
        )
        self.assertEqual(
            by_arch["C01_ORDER_BACKLOG_MARGIN_BRIDGE"]["primary_repair_lane"],
            "runtime_input_evidence_coverage",
        )
        self.assertIn("exact_fixture_archive", by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["repair_lanes"])
        self.assertGreater(
            by_arch["C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN"]["priority_score"],
            by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["priority_score"],
        )

        report = render_v12_runtime_repair_priority_board(payload)
        self.assertIn("V12 Runtime Repair Priority Board", report)
        self.assertIn("C06 하닉형 문제", report)
        self.assertIn("candidate_funnel_or_benchmark_replay", report)


if __name__ == "__main__":
    unittest.main()
