import unittest

from e2r.calibration.v12_runtime_repair_execution_backlog import (
    build_v12_runtime_repair_execution_backlog,
    render_v12_runtime_repair_execution_backlog,
)


class V12RuntimeRepairExecutionBacklogTests(unittest.TestCase):
    def test_backlog_splits_archive_bridge_and_gate_implementation_lanes(self) -> None:
        execution_path = {
            "archetype_rows": [
                {
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "stop_layer": "candidate_replay_archive",
                    "weight_support_row_count": 413,
                    "runtime_candidate_count": 0,
                    "runtime_max_score": None,
                    "missing_required_bridge_axes": ["capital_return"],
                },
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "stop_layer": "parser_feature_bridge",
                    "weight_support_row_count": 229,
                    "runtime_candidate_count": 19,
                    "runtime_max_score": 76.7,
                    "missing_required_bridge_axes": ["backlog", "contract"],
                },
                {
                    "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                    "stop_layer": "stage_gate",
                    "weight_support_row_count": 277,
                    "runtime_candidate_count": 44,
                    "runtime_max_score": 72.9,
                    "missing_required_bridge_axes": [],
                },
                {
                    "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
                    "stop_layer": "manual_review",
                    "weight_support_row_count": 80,
                    "runtime_candidate_count": 4,
                    "runtime_max_score": 0,
                    "missing_required_bridge_axes": ["margin", "backlog", "contract", "customer"],
                },
            ]
        }
        repair_board = {
            "rows": [
                {
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "primary_repair_lane": "candidate_funnel_or_benchmark_replay",
                    "priority_score": 101.8,
                },
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "primary_repair_lane": "gate_bridge_axis_alignment",
                    "priority_score": 56.6,
                },
                {
                    "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                    "primary_repair_lane": "weighted_gate_threshold_or_component_balance",
                    "priority_score": 40.0,
                },
                {
                    "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
                    "primary_repair_lane": "runtime_input_evidence_coverage",
                    "priority_score": 22.0,
                    "missing_required_bridge_axes": ["margin", "backlog", "contract", "customer"],
                },
            ]
        }
        field_audit = {
            "rows": [
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "missing_feature_parser_contract_primitives": [],
                    "axis_contract_statuses": [
                        {"axis": "backlog", "status": "bridge_spec_axis_present_but_runtime_field_missing_or_too_weak"},
                        {"axis": "contract", "status": "required_by_gate_but_absent_from_bridge_spec"},
                    ],
                }
            ]
        }
        replay_spec = {
            "rows": [
                {
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "role": "green",
                    "candidate": {"symbol": "105560", "as_of_date": "2024-02-07"},
                }
            ]
        }
        readiness = {
            "archetype_pair_rows": [
                {
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "pair_retrospective_ready": False,
                    "pair_strict_pit_ready": False,
                }
            ],
            "rows": [
                {
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "retrospective_readiness_status": "missing_candidate_generation_inputs",
                    "retrospective_missing_inputs": ["official_universe", "price_history_370d"],
                }
            ],
        }
        funnel = {
            "rows": [
                {
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "fixture_funnel_status": "symbol_never_reached_current_runtime",
                    "funnel_root_cause": "benchmark_universe_or_official_cheap_scan_funnel_gap",
                }
            ]
        }
        payload = build_v12_runtime_repair_execution_backlog(
            execution_path_payload=execution_path,
            repair_board_payload=repair_board,
            field_audit_payload=field_audit,
            replay_spec_payload=replay_spec,
            readiness_payload=readiness,
            funnel_audit_payload=funnel,
        )
        by_arch = {row["canonical_archetype_id"]: row for row in payload["rows"]}

        self.assertEqual(
            by_arch["C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN"]["implementation_lane"],
            "01_fixture_archive_and_candidate_funnel",
        )
        self.assertEqual(
            by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["implementation_lane"],
            "02_parser_feature_bridge_contract",
        )
        self.assertEqual(
            by_arch["C02_POWER_GRID_DATACENTER_CAPEX"]["implementation_lane"],
            "03_weighted_gate_validation_after_fields",
        )
        self.assertEqual(
            by_arch["C01_ORDER_BACKLOG_MARGIN_BRIDGE"]["implementation_lane"],
            "01_fixture_archive_and_candidate_funnel",
        )
        self.assertEqual(payload["summary"]["implementation_lane_counts"]["01_fixture_archive_and_candidate_funnel"], 2)
        self.assertEqual(payload["summary"]["missing_required_axis_counts"]["contract"], 2)
        self.assertIn({"axis": "contract", "count": 2}, payload["summary"]["top_missing_required_axes"])
        self.assertIn("src/e2r/features.py::DeterministicFeatureEngineer.engineer", by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["code_files_to_touch"])

        report = render_v12_runtime_repair_execution_backlog(payload)
        self.assertIn("HBM 과적합", report)
        self.assertIn("시험 문제지도 없는데", report)

    def test_repair_board_can_supersede_stale_execution_path_missing_axes(self) -> None:
        execution_path = {
            "archetype_rows": [
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "stop_layer": "parser_feature_bridge",
                    "weight_support_row_count": 229,
                    "runtime_candidate_count": 19,
                    "runtime_max_score": 76.7,
                    "missing_required_bridge_axes": ["backlog", "contract"],
                }
            ]
        }
        repair_board = {
            "rows": [
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "primary_repair_lane": "weighted_gate_threshold_or_component_balance",
                    "priority_score": 54.6,
                    "missing_required_bridge_axes": [],
                }
            ]
        }
        field_audit = {
            "rows": [
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "missing_feature_parser_contract_primitives": [],
                    "axis_contract_statuses": [
                        {"axis": "customer", "status": "covered_by_bridge_spec_and_runtime"},
                        {"axis": "backlog", "status": "covered_by_bridge_spec_and_runtime"},
                        {"axis": "contract", "status": "covered_by_bridge_spec_and_runtime"},
                        {"axis": "margin", "status": "covered_by_bridge_spec_and_runtime"},
                    ],
                }
            ]
        }

        payload = build_v12_runtime_repair_execution_backlog(
            execution_path_payload=execution_path,
            repair_board_payload=repair_board,
            field_audit_payload=field_audit,
            replay_spec_payload={"rows": []},
            readiness_payload={"rows": [], "archetype_pair_rows": []},
            funnel_audit_payload={"rows": []},
        )
        row = payload["rows"][0]

        self.assertEqual(row["implementation_lane"], "03_weighted_gate_validation_after_fields")
        self.assertEqual(row["stop_layer"], "stage_gate")
        self.assertEqual(row["missing_required_bridge_axes"], [])
        self.assertNotIn("contract", payload["summary"]["missing_required_axis_counts"])


if __name__ == "__main__":
    unittest.main()
