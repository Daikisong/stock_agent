from pathlib import Path
import tempfile
import unittest

from e2r.calibration.v12_current_runtime_field_failure_census import (
    build_v12_current_runtime_field_failure_census,
    render_v12_current_runtime_field_failure_census,
)


class V12CurrentRuntimeFieldFailureCensusTests(unittest.TestCase):
    def test_census_counts_zero_fields_gates_and_unexercised_archetypes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            score_csv = root / "score_components_by_candidate.csv"
            gate_csv = root / "stage_gate_matrix.csv"
            weight_profile = root / "weights.json"
            score_csv.write_text(
                "\n".join(
                    [
                        "symbol,company_name,as_of_date,current_stage,current_score,canonical_archetype_id,sector_profile,archetype_component_eps_fcf_explosion,archetype_component_earnings_visibility,archetype_component_bottleneck_pricing,archetype_component_market_mispricing,archetype_component_valuation_rerating,archetype_component_capital_allocation,archetype_component_information_confidence,revision_score,contract_quality,backlog_rpo_visibility,capa_constraint,structural_visibility_quality,sector_visibility_score,sector_bottleneck_score,domain_specific_evidence_score,actual_profit_conversion_score,research_axis_bridge_margin,research_axis_bridge_customer,research_axis_bridge_backlog,research_axis_bridge_contract,bottleneck_selected_path,stage3_total_deficit,stage3_bottleneck_deficit,stage3_visibility_deficit,green_gate_deficit_summary",
                        "000660,SK하이닉스,2024-04-30,3-Yellow,76.7,C06_HBM_MEMORY_CUSTOMER_CAPACITY,MEMORY_HBM,24,15.9,11.0,12.8,9.8,0,3,100,0,15,0,70,70,55,80,80,100,100,0,0,actual_conversion_bridge,10.3,3.2,0,total:76.7/87(-10.3)",
                        "005930,삼성전자,2024-04-01,2,68.6,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,MEMORY_HBM,22,11.2,6.9,9.2,7.8,0,11.4,80,0,0,0,60,60,40,60,62,100,0,0,0,actual_conversion_bridge,18.4,3.6,2.3,total:68.6/87(-18.4)",
                        "267260,HD현대일렉트릭,2023-08-01,2,72.9,C02_POWER_GRID_DATACENTER_CAPEX,POWER_EQUIPMENT,20,16.1,9.9,10.0,10.1,0,6.8,100,41.5,70,40,70,65,45,40,75,100,100,100,100,industrial_bridge,14.1,5.1,0,total:72.9/87(-14.1)",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            gate_csv.write_text(
                "\n".join(
                    [
                        "symbol,as_of_date,canonical_archetype_id,failed_stage3_total_score,failed_stage3_bottleneck,failed_stage3_visibility,failed_stage3_contract_quality",
                        "000660,2024-04-30,C06_HBM_MEMORY_CUSTOMER_CAPACITY,True,True,False,False",
                        "005930,2024-04-01,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,True,True,True,False",
                        "267260,2023-08-01,C02_POWER_GRID_DATACENTER_CAPEX,True,True,False,True",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            weight_profile.write_text(
                '{"archetype_weights":{"C02_POWER_GRID_DATACENTER_CAPEX":{},"C06_HBM_MEMORY_CUSTOMER_CAPACITY":{},"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE":{},"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN":{}}}',
                encoding="utf-8",
            )

            payload = build_v12_current_runtime_field_failure_census(
                score_csv_path=score_csv,
                gate_csv_path=gate_csv,
                weight_profile_path=weight_profile,
            )

        self.assertEqual(payload["summary"]["candidate_row_count"], 3)
        self.assertEqual(payload["summary"]["stage3_green_count"], 0)
        self.assertTrue(payload["summary"]["all_candidates_failed_stage3_total"])
        self.assertTrue(payload["summary"]["all_candidates_failed_stage3_bottleneck"])
        self.assertEqual(payload["summary"]["runtime_exercised_archetype_count"], 3)
        self.assertEqual(payload["summary"]["runtime_unexercised_archetype_count"], 1)

        by_arch = {row["group_key"]: row for row in payload["archetype_rows"]}
        c06_zeros = by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["zero_field_counts"]
        self.assertEqual(c06_zeros["research_axis_bridge_backlog"]["zero_count"], 1)
        self.assertEqual(c06_zeros["research_axis_bridge_contract"]["zero_count"], 1)
        self.assertIn("HBM 전망/revision", by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["plain_diagnosis"])

        report = render_v12_current_runtime_field_failure_census(payload)
        self.assertIn("Stage3 total과 bottleneck", report)
        self.assertIn("C02_POWER_GRID_DATACENTER_CAPEX", report)
        self.assertIn("runtime_unexercised_archetype_count", report)


if __name__ == "__main__":
    unittest.main()
