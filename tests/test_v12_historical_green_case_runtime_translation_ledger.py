import unittest

from e2r.calibration.v12_historical_green_case_runtime_translation_ledger import (
    build_v12_historical_green_case_runtime_translation_ledger,
    render_v12_historical_green_case_runtime_translation_ledger,
)


class V12HistoricalGreenCaseRuntimeTranslationLedgerTests(unittest.TestCase):
    def test_ledger_links_historical_green_axes_to_current_runtime_status(self) -> None:
        score_rows = [
            {
                "row_type": "score_simulation",
                "case_id": "C21_GREEN",
                "trigger_id": "T_C21",
                "symbol": "105560",
                "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                "raw_component_scores_after": {
                    "roe_pbr_capital_return_score": 9,
                    "capital_return_execution_score": 9,
                    "valuation_repricing_score": 8,
                    "execution_risk_score": 2,
                },
                "weighted_score_after": 88,
                "stage_label_after": "Stage3-Green",
                "score_return_alignment_label": "aligned_positive",
                "current_profile_verdict": "current_profile_correct",
            },
            {
                "row_type": "score_simulation",
                "case_id": "C20_GREEN",
                "trigger_id": "T_C20",
                "symbol": "257720",
                "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION",
                "raw_component_scores_after": {
                    "margin_bridge_score": 9,
                    "revision_score": 9,
                    "customer_quality_score": 9,
                    "relative_strength_score": 9,
                },
                "weighted_score_after": 94,
                "stage_label_after": "Stage3-Green",
                "score_return_alignment_label": "aligned",
                "current_profile_verdict": "current_profile_too_late",
            },
            {
                "row_type": "score_simulation",
                "case_id": "GREEN_TRAP",
                "symbol": "028050",
                "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
                "raw_component_scores_after": {"margin_bridge_score": 2},
                "stage_label_before": "Stage3-Green",
                "stage_label_after": "Stage2-Actionable",
            },
        ]
        current_census = {
            "archetype_rows": [
                {
                    "group_key": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION",
                    "row_count": 22,
                    "max_score": 62.55,
                    "stage_counts": {"1": 22},
                    "zero_field_counts": {
                        "research_axis_bridge_backlog": {"zero_count": 22, "row_count": 22},
                        "research_axis_bridge_contract": {"zero_count": 22, "row_count": 22},
                    },
                    "failed_gate_counts": {
                        "failed_stage3_total_score": 22,
                        "failed_stage3_bottleneck": 22,
                    },
                    "best_row": {
                        "current_stage": "1",
                        "current_score": "62.55",
                        "symbol": "003230",
                    },
                }
            ]
        }
        runtime_inventory = {
            "feature_method_arg_keys": [
                "capital_return_execution",
                "actual_profit_conversion_score",
                "revision_score",
                "customer_preorder_or_allocation",
            ],
            "parser_output_keys": [],
            "bridge_diagnostic_group_keys": [],
            "derived_runtime_metrics": ["price_stage_score"],
        }

        payload = build_v12_historical_green_case_runtime_translation_ledger(
            score_simulation_rows=score_rows,
            runtime_inventory=runtime_inventory,
            current_census_payload=current_census,
            sample_limit=10,
        )

        self.assertEqual(payload["summary"]["historical_stage3_green_after_case_count"], 2)
        self.assertEqual(payload["summary"]["historical_green_trap_downgrade_count"], 1)
        self.assertEqual(payload["summary"]["historical_green_archetype_count"], 2)
        self.assertEqual(payload["summary"]["historical_green_archetype_exercised_in_current_benchmark_count"], 1)
        self.assertEqual(payload["summary"]["historical_green_archetype_unexercised_in_current_benchmark_count"], 1)

        by_arch = {row["canonical_archetype_id"]: row for row in payload["archetype_rows"]}
        self.assertEqual(
            by_arch["C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN"]["current_runtime_status"],
            "not_exercised_in_current_benchmark",
        )
        self.assertEqual(
            by_arch["C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION"]["current_runtime_status"],
            "exercised_in_current_benchmark",
        )
        report = render_v12_historical_green_case_runtime_translation_ledger(payload)

        self.assertIn("과거 Green은 실제로 있었다", report)
        self.assertIn("C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", report)
        self.assertIn("not exercised", report)
        self.assertIn("failed_stage3_bottleneck", report)


if __name__ == "__main__":
    unittest.main()
