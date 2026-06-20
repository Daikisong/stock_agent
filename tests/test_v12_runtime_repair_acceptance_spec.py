import unittest

from e2r.calibration.v12_runtime_repair_acceptance_spec import (
    build_v12_runtime_repair_acceptance_spec,
    render_v12_runtime_repair_acceptance_spec,
)


class V12RuntimeRepairAcceptanceSpecTests(unittest.TestCase):
    def test_acceptance_spec_requires_replay_inputs_bridge_fields_and_gate_parity(self) -> None:
        backlog = {
            "rows": [
                {
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "implementation_lane": "01_fixture_archive_and_candidate_funnel",
                    "priority_score": 101.8,
                    "runtime_candidate_count": 0,
                    "runtime_max_score": None,
                    "missing_required_bridge_axes": ["capital_return"],
                    "missing_feature_parser_contract_primitives": [],
                    "pair_retrospective_ready": False,
                    "pair_strict_pit_ready": False,
                    "readiness_summary": {
                        "retrospective_missing_input_counts": {"official_universe": 1},
                    },
                    "funnel_summary": {
                        "fixture_funnel_status_counts": {"symbol_never_reached_current_runtime": 2},
                    },
                    "do_not_do": "do not use labels as score inputs",
                },
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "implementation_lane": "02_parser_feature_bridge_contract",
                    "priority_score": 56.6,
                    "runtime_candidate_count": 19,
                    "runtime_max_score": 76.7,
                    "missing_required_bridge_axes": ["backlog", "contract"],
                    "missing_feature_parser_contract_primitives": [],
                    "pair_retrospective_ready": False,
                    "pair_strict_pit_ready": False,
                    "do_not_do": "do not add HBM name bonus",
                },
                {
                    "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                    "implementation_lane": "03_weighted_gate_validation_after_fields",
                    "priority_score": 41.0,
                    "runtime_candidate_count": 44,
                    "runtime_max_score": 72.9,
                    "missing_required_bridge_axes": [],
                    "missing_feature_parser_contract_primitives": ["datacenter_customer"],
                    "pair_retrospective_ready": False,
                    "pair_strict_pit_ready": False,
                    "do_not_do": "do not lower threshold before fields are present",
                },
            ]
        }

        payload = build_v12_runtime_repair_acceptance_spec(backlog_payload=backlog)
        by_arch = {row["canonical_archetype_id"]: row for row in payload["rows"]}

        self.assertEqual(
            by_arch["C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN"]["acceptance_status_current"],
            "blocked_missing_exact_fixture_archive_or_candidate_funnel",
        )
        self.assertEqual(
            by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["acceptance_status_current"],
            "blocked_missing_parser_feature_or_gate_axis_contract",
        )
        self.assertEqual(
            by_arch["C02_POWER_GRID_DATACENTER_CAPEX"]["acceptance_status_current"],
            "blocked_weighted_gate_after_fields_present",
        )
        self.assertIn(
            "test_c06_hbm_memory_customer_capacity_feature_bridge_populates_missing_axes_without_name_special_case",
            by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["acceptance_tests_to_add"],
        )
        self.assertEqual(payload["summary"]["acceptance_status_counts"]["blocked_weighted_gate_after_fields_present"], 1)

        report = render_v12_runtime_repair_acceptance_spec(payload)
        self.assertIn("하닉/HBM만 올리는 보너스", report)
        self.assertIn("정답지를 보고 채점한 점수", report)


if __name__ == "__main__":
    unittest.main()
