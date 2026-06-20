from pathlib import Path
import tempfile
import unittest

from e2r.calibration.v12_representative_case_runtime_trajectory import (
    build_v12_representative_case_runtime_trajectory,
    render_v12_representative_case_runtime_trajectory,
)


class V12RepresentativeCaseRuntimeTrajectoryTests(unittest.TestCase):
    def test_trajectory_keeps_hbm_case_as_cross_archetype_example(self) -> None:
        cross_trace = {
            "ready_archetype_count": 3,
            "spec_row_count": 6,
            "loss_layer_counts_by_archetype": {
                "candidate_funnel_or_replay_coverage": 1,
                "research_axis_to_runtime_field_translation": 1,
                "weighted_component_or_stage3_gate": 1,
            },
            "gap_status_counts_by_archetype": {
                "not_in_current_benchmark": 1,
                "runtime_bridge_axes_missing": 1,
                "runtime_stage3_gate_blocked": 1,
            },
            "missing_required_bridge_axis_counts": {"backlog": 1, "capital_return": 1},
            "rows": [
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "runtime_gap_status": "runtime_bridge_axes_missing",
                    "loss_layer": "research_axis_to_runtime_field_translation",
                    "runtime_candidate_count": 19,
                    "runtime_max_score": 76.7,
                    "missing_required_bridge_axes": ["backlog"],
                    "next_action": "Patch bridge fields.",
                },
                {
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "runtime_gap_status": "not_in_current_benchmark",
                    "loss_layer": "candidate_funnel_or_replay_coverage",
                    "runtime_candidate_count": 0,
                    "runtime_max_score": None,
                    "missing_required_bridge_axes": ["capital_return"],
                    "next_action": "Materialize fixtures.",
                },
                {
                    "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
                    "runtime_gap_status": "runtime_stage3_gate_blocked",
                    "loss_layer": "weighted_component_or_stage3_gate",
                    "runtime_candidate_count": 4,
                    "runtime_max_score": 72.0,
                    "missing_required_bridge_axes": [],
                    "next_action": "Verify gates with guard pair.",
                },
            ],
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "score_components_by_candidate.csv").write_text(
                "\n".join(
                    [
                        "symbol,company_name,as_of_date,current_stage,current_score,canonical_archetype_id,archetype_component_eps_fcf_explosion,archetype_component_earnings_visibility,archetype_component_bottleneck_pricing,revision_score,research_axis_bridge_margin,research_axis_bridge_customer,research_axis_bridge_backlog,research_axis_bridge_contract,contract_quality,backlog_rpo_visibility,capa_constraint,green_gate_deficit_summary",
                        "000660,SK하이닉스,2024-04-25,3-Yellow,76.0596,C06_HBM_MEMORY_CUSTOMER_CAPACITY,24.0,15.441,10.8262,100.0,100.0,100.0,0.0,0.0,0.0,15.0,0.0,total:76.06/87.00(-10.94)",
                        "000660,SK하이닉스,2024-04-30,3-Yellow,76.7639,C06_HBM_MEMORY_CUSTOMER_CAPACITY,24.0,15.9077,11.0522,100.0,100.0,100.0,0.0,0.0,0.0,15.0,0.0,total:76.76/87.00(-10.24)",
                        "005930,삼성전자,2024-04-25,2,68.6752,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,22.0,11.1963,6.94,80.0,100.0,0.0,0.0,0.0,0.0,0.0,0.0,total:68.68/87.00(-18.32)",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            (root / "stage_gate_matrix.csv").write_text(
                "\n".join(
                    [
                        "symbol,as_of_date,failed_stage3_total_score,failed_stage3_visibility,failed_stage3_bottleneck",
                        "000660,2024-04-25,True,True,True",
                        "000660,2024-04-30,True,False,True",
                        "005930,2024-04-25,True,True,True",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )

            payload = build_v12_representative_case_runtime_trajectory(
                autopsy_directories=[root],
                cross_trace_payload=cross_trace,
            )

        self.assertEqual(payload["summary"]["runtime_trajectory_row_count"], 3)
        self.assertEqual(payload["summary"]["symbol_reaches_stage3_green_count"], 0)
        self.assertEqual(payload["summary"]["cross_archetype_non_hbm_count"], 2)
        self.assertEqual(
            payload["summary"]["non_hbm_loss_layer_counts"],
            {
                "candidate_funnel_or_replay_coverage": 1,
                "weighted_component_or_stage3_gate": 1,
            },
        )
        self.assertIn(
            "research_axis_bridge_contract",
            payload["symbol_summaries"]["000660"]["persistent_zero_important_fields"],
        )
        self.assertIn("capa_constraint", payload["symbol_summaries"]["005930"]["persistent_zero_important_fields"])
        report = render_v12_representative_case_runtime_trajectory(payload)

        self.assertIn("HBM 특례", report)
        self.assertIn("C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", report)
        self.assertIn("비-HBM row도 같은 기준", report)


if __name__ == "__main__":
    unittest.main()
