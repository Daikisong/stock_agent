from pathlib import Path
import tempfile
import unittest

from e2r.calibration.v12_hbm_score_loss_trace import (
    build_v12_hbm_score_loss_trace,
    render_v12_hbm_score_loss_trace,
)


class V12HbmScoreLossTraceTests(unittest.TestCase):
    def test_trace_extracts_hynix_and_samsung_loss_fields(self) -> None:
        spec_payload = {
            "rows": [
                {
                    "role": "green",
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "candidate": {"symbol": "000660", "case_id": "C06_GREEN"},
                }
            ]
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "score_components_by_candidate.csv").write_text(
                "\n".join(
                    [
                        "symbol,company_name,as_of_date,current_stage,current_score,canonical_archetype_id,research_axis_bridge_margin,research_axis_bridge_customer,research_axis_bridge_backlog,research_axis_bridge_contract,revision_score,archetype_component_eps_fcf_explosion,green_gate_deficit_summary",
                        "000660,SK하이닉스,2024-04-25,3-Yellow,76.0596,C06_HBM_MEMORY_CUSTOMER_CAPACITY,100.0,100.0,0.0,0.0,100.0,24.0,total:76.06/87.00(-10.94)",
                        "005930,삼성전자,2024-04-25,2,68.6752,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,100.0,0.0,0.0,0.0,80.0,22.0,total:68.68/87.00(-18.32)",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            (root / "stage_gate_matrix.csv").write_text(
                "\n".join(
                    [
                        "symbol,as_of_date,failed_stage3_total_score,failed_stage3_bottleneck",
                        "000660,2024-04-25,True,True",
                        "005930,2024-04-25,True,True",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            payload = build_v12_hbm_score_loss_trace(
                spec_payload=spec_payload,
                autopsy_directories=[root],
            )

        self.assertEqual(payload["summary"]["sk_hynix_runtime_row_count"], 1)
        self.assertEqual(payload["summary"]["samsung_runtime_row_count"], 1)
        self.assertEqual(len(payload["runtime_rows"]), 2)
        report = render_v12_hbm_score_loss_trace(payload)

        self.assertIn("SK하이닉스", report)
        self.assertIn("삼성전자", report)
        self.assertIn("100.0/100.0/0.0/0.0", report)
        self.assertIn("failed_stage3_bottleneck", report)


if __name__ == "__main__":
    unittest.main()
