import unittest

from e2r.calibration.v12_fixture_runtime_coverage import (
    build_v12_fixture_runtime_coverage_board,
    render_v12_fixture_runtime_coverage_board,
)


class V12FixtureRuntimeCoverageTests(unittest.TestCase):
    def test_board_separates_benchmark_coverage_from_bridge_missing(self) -> None:
        fixture_payload = {
            "archetypes": [
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
                    "runtime_bridge_group": "semiconductor_customer_capacity_bridge",
                    "fixture_status": "ready_for_runtime_replay_fixture",
                    "raw_stage3_green_row_count": 2,
                    "green_row_count": 2,
                    "clean_green_row_count": 2,
                    "green_guard_marker_row_count": 0,
                    "clean_guard_row_count": 1,
                    "green_fixture_candidate": {
                        "symbol": "000660",
                        "trigger_date": "2024-04-25",
                    },
                    "guard_fixture_candidate": {
                        "symbol": "005930",
                        "trigger_date": "2024-04-05",
                    },
                },
                {
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
                    "runtime_bridge_group": "financial_capital_return_bridge",
                    "fixture_status": "ready_for_runtime_replay_fixture",
                    "raw_stage3_green_row_count": 1,
                    "green_row_count": 1,
                    "clean_green_row_count": 1,
                    "green_guard_marker_row_count": 0,
                    "clean_guard_row_count": 1,
                    "green_fixture_candidate": {
                        "symbol": "000810",
                        "trigger_date": "2024-05-16",
                    },
                },
            ]
        }
        score_rows = [
            {
                "symbol": "000660",
                "as_of_date": "2024-04-25",
                "current_stage": "3-Yellow",
                "current_score": "76.7",
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "research_axis_bridge_customer": "100",
                "research_axis_bridge_backlog": "0",
                "research_axis_bridge_contract": "0",
                "research_axis_bridge_margin": "80",
            }
        ]
        gate_rows = [
            {
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "failed_stage3_total_score": "True",
                "failed_stage3_bottleneck": "True",
            }
        ]

        payload = build_v12_fixture_runtime_coverage_board(
            fixture_payload=fixture_payload,
            score_rows=score_rows,
            gate_rows=gate_rows,
        )
        by_arch = {row["canonical_archetype_id"]: row for row in payload["archetypes"]}

        self.assertEqual(payload["ready_fixture_archetype_count"], 2)
        self.assertEqual(payload["runtime_covered_archetype_count"], 1)
        self.assertEqual(payload["ready_fixture_not_in_current_benchmark_count"], 1)
        self.assertEqual(by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["runtime_gap_status"], "runtime_bridge_axes_missing")
        self.assertEqual(
            by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["missing_required_bridge_axes"],
            ["backlog", "contract"],
        )
        self.assertTrue(by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["green_fixture_in_current_benchmark"])
        self.assertEqual(by_arch["C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN"]["runtime_gap_status"], "not_in_current_benchmark")

        report = render_v12_fixture_runtime_coverage_board(payload)
        self.assertIn("runtime_bridge_axes_missing", report)
        self.assertIn("not_in_current_benchmark", report)

    def test_board_separates_runtime_input_evidence_missing_from_parser_bridge_gap(self) -> None:
        fixture_payload = {
            "archetypes": [
                {
                    "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
                    "runtime_bridge_group": "industrial_backlog_margin_bridge",
                    "fixture_status": "ready_for_runtime_replay_fixture",
                },
                {
                    "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
                    "runtime_bridge_group": "semiconductor_memory_recovery_bridge",
                    "fixture_status": "ready_for_runtime_replay_fixture",
                },
            ]
        }
        score_rows = [
            {
                "symbol": "001440",
                "as_of_date": "2026-02-01",
                "current_stage": "1",
                "current_score": "0",
                "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
                "research_axis_bridge_margin": "0",
                "research_axis_bridge_backlog": "0",
                "research_axis_bridge_contract": "0",
                "research_axis_bridge_customer": "0",
                "cross_evidence_families_present": "price, disclosure",
                "score_variability_drivers": (
                    "input_count:price_bar=2|input_count:financial_actual=0|"
                    "input_count:research_report=0|input_count:news_item=0|"
                    "input_count:consensus=0|input_count:consensus_revision=0|evidence_count:1"
                ),
            },
            {
                "symbol": "005930",
                "as_of_date": "2024-04-01",
                "current_stage": "2",
                "current_score": "68.6",
                "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
                "research_axis_bridge_margin": "100",
                "research_axis_bridge_backlog": "0",
                "research_axis_bridge_contract": "0",
                "research_axis_bridge_customer": "0",
                "cross_evidence_families_present": "price, financial_actual, disclosure, research_report",
                "score_variability_drivers": (
                    "input_count:price_bar=2|input_count:financial_actual=1|"
                    "input_count:research_report=1|input_count:news_item=0|"
                    "input_count:consensus=2|input_count:consensus_revision=1|evidence_count:6"
                ),
            },
        ]

        payload = build_v12_fixture_runtime_coverage_board(
            fixture_payload=fixture_payload,
            score_rows=score_rows,
            gate_rows=[],
        )
        by_arch = {row["canonical_archetype_id"]: row for row in payload["archetypes"]}

        self.assertEqual(
            by_arch["C01_ORDER_BACKLOG_MARGIN_BRIDGE"]["runtime_gap_status"],
            "runtime_input_evidence_missing",
        )
        self.assertEqual(
            by_arch["C01_ORDER_BACKLOG_MARGIN_BRIDGE"]["runtime_input_evidence_summary"]["reason"],
            "bridge_source_families_missing",
        )
        self.assertEqual(
            by_arch["C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE"]["runtime_gap_status"],
            "runtime_bridge_axes_missing",
        )
        self.assertNotIn(
            "contract",
            by_arch["C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE"]["missing_required_bridge_axes"],
        )

        report = render_v12_fixture_runtime_coverage_board(payload)
        self.assertIn("runtime_input_evidence_missing", report)

    def test_memory_recovery_bridge_does_not_require_contract_axis(self) -> None:
        fixture_payload = {
            "archetypes": [
                {
                    "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
                    "runtime_bridge_group": "semiconductor_memory_recovery_bridge",
                    "fixture_status": "ready_for_runtime_replay_fixture",
                },
            ]
        }
        score_rows = [
            {
                "symbol": "005930",
                "as_of_date": "2024-04-01",
                "current_stage": "2",
                "current_score": "72.0",
                "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
                "research_axis_bridge_margin": "100",
                "research_axis_bridge_backlog": "100",
                "research_axis_bridge_contract": "0",
                "research_axis_bridge_customer": "100",
                "research_axis_bridge_valuation_repricing": "100",
                "cross_evidence_families_present": "price, financial_actual, disclosure, research_report",
                "score_variability_drivers": "input_count:research_report=1|input_count:consensus=1|evidence_count:5",
            },
        ]
        gate_rows = [
            {
                "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
                "failed_stage3_total_score": "True",
            }
        ]

        payload = build_v12_fixture_runtime_coverage_board(
            fixture_payload=fixture_payload,
            score_rows=score_rows,
            gate_rows=gate_rows,
        )
        row = payload["archetypes"][0]

        self.assertEqual(row["runtime_gap_status"], "runtime_stage3_gate_blocked")
        self.assertEqual(row["missing_required_bridge_axes"], [])
        self.assertEqual(row["required_bridge_axes"], ["customer", "backlog", "margin", "valuation_repricing"])


if __name__ == "__main__":
    unittest.main()
