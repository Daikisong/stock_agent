import unittest

from e2r.calibration.v12_green_score_axis_runtime_contract_audit import (
    build_v12_green_score_axis_runtime_contract_audit,
    render_v12_green_score_axis_runtime_contract_audit,
)


class V12GreenScoreAxisRuntimeContractAuditTests(unittest.TestCase):
    def test_audit_maps_green_score_axes_to_runtime_contract_statuses(self) -> None:
        score_rows = [
            {
                "row_type": "score_simulation",
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "stage_label_after": "Stage3-Green",
                "raw_component_scores_after": {
                    "customer_quality_score": 9,
                    "margin_bridge_score": 8,
                    "revision_score": 8,
                },
                "changed_components": ["capacity_or_shipment_score"],
            },
            {
                "row_type": "score_simulation",
                "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                "stage_label_after": "Stage3-Green",
                "raw_component_scores_after": {
                    "roe_pbr_capital_return_score": 12,
                    "capital_return_execution": 1,
                    "valuation_repricing_score": 7,
                },
                "changed_components": ["shareholder_return_quality_score"],
            },
            {
                "row_type": "score_simulation",
                "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                "stage_label_after": "Stage2-Watch",
                "raw_component_scores_after": {"margin_bridge_score": 2},
            },
        ]
        runtime_inventory = {
            "feature_method_arg_keys": [
                "customer_preorder_or_allocation",
                "capacity_precommitted",
                "capital_return_execution",
            ],
            "parser_output_keys": [],
            "bridge_diagnostic_group_keys": [],
            "derived_runtime_metrics": ["revision_score"],
        }
        causal_chain = {
            "focus_archetype_rows": [
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "stop_layer": "parser_feature_bridge",
                    "plain_failure": "후보는 들어왔지만 backlog/contract가 비어 있다.",
                },
                {
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "stop_layer": "candidate_replay_archive",
                    "plain_failure": "시험지가 current replay에 없다.",
                },
            ]
        }

        payload = build_v12_green_score_axis_runtime_contract_audit(
            score_simulation_rows=score_rows,
            runtime_inventory=runtime_inventory,
            causal_chain_payload=causal_chain,
        )
        rows_by_key = {row["research_score_key"]: row for row in payload["green_score_axis_contract_rows"]}

        self.assertEqual(payload["summary"]["green_related_score_simulation_row_count"], 2)
        self.assertEqual(payload["summary"]["strict_stage3_green_score_simulation_row_count"], 2)
        self.assertEqual(payload["summary"]["green_score_key_exact_source_field_matches"], ["capital_return_execution"])
        self.assertEqual(payload["summary"]["green_score_key_exact_derived_metric_only_matches"], ["revision_score"])
        self.assertEqual(
            rows_by_key["customer_quality_score"]["runtime_contract_status"],
            "requires_axis_bridge_to_runtime_primitives",
        )
        self.assertIn(
            "customer_preorder_or_allocation",
            rows_by_key["customer_quality_score"]["supported_candidate_runtime_fields"],
        )
        self.assertEqual(
            rows_by_key["capital_return_execution"]["runtime_contract_status"],
            "exact_source_runtime_field",
        )
        self.assertEqual(rows_by_key["roe_pbr_capital_return_score"]["family"], "capital_return")
        self.assertEqual(rows_by_key["valuation_repricing_score"]["family"], "valuation_repricing")

        report = render_v12_green_score_axis_runtime_contract_audit(payload)
        self.assertIn("연구 score axis", report)
        self.assertIn("source-backed primitive", report)
        self.assertIn("시험지가 current replay에 없다", report)


if __name__ == "__main__":
    unittest.main()
