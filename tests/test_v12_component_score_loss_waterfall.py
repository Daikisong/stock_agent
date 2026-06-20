from pathlib import Path
import tempfile
import unittest

from e2r.calibration.v12_component_score_loss_waterfall import (
    build_v12_component_score_loss_waterfall,
    render_v12_component_score_loss_waterfall,
)


class V12ComponentScoreLossWaterfallTests(unittest.TestCase):
    def test_waterfall_calculates_weighted_component_losses(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            score_csv = root / "score_components_by_candidate.csv"
            gate_csv = root / "stage_gate_matrix.csv"
            weight_profile = root / "weights.json"
            score_csv.write_text(
                "\n".join(
                    [
                        "symbol,company_name,as_of_date,current_stage,current_score,large_sector_id,canonical_archetype_id,sector_profile,"
                        "archetype_weight_eps_fcf_explosion,archetype_weight_earnings_visibility,archetype_weight_bottleneck_pricing,archetype_weight_market_mispricing,archetype_weight_valuation_rerating,archetype_weight_capital_allocation,archetype_weight_information_confidence,"
                        "archetype_component_eps_fcf_explosion,archetype_component_earnings_visibility,archetype_component_bottleneck_pricing,archetype_component_market_mispricing,archetype_component_valuation_rerating,archetype_component_capital_allocation,archetype_component_information_confidence,"
                        "research_axis_bridge_margin,research_axis_bridge_customer,research_axis_bridge_backlog,research_axis_bridge_contract,green_gate_deficit_summary",
                        "000660,SK하이닉스,2024-05-01,3-Yellow,76.7639,L2,C06_HBM_MEMORY_CUSTOMER_CAPACITY,MEMORY_HBM,"
                        "24,21,19,15,12,4,5,"
                        "24,15.9077,11.0522,12.852,9.8712,0.0808,3,"
                        "100,100,0,0,total:76.76/87(-10.24)",
                        "005930,삼성전자,2024-04-01,2,68.6752,L2,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,MEMORY_RECOVERY,"
                        "22,18,14,12,10,5,19,"
                        "22,11.1963,6.94,9.2784,7.799,0.0615,11.4,"
                        "100,0,0,0,total:68.68/87(-18.32)",
                        "267260,HD현대일렉트릭,2023-08-01,2,72.9633,L1,C02_POWER_GRID_DATACENTER_CAPEX,POWER_EQUIPMENT,"
                        "21,24,20,13,12,5,5,"
                        "21,19.3259,9.905,10.1855,8.0775,1.4694,3,"
                        "100,100,100,100,total:72.96/87(-14.04)",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            gate_csv.write_text(
                "\n".join(
                    [
                        "symbol,as_of_date,canonical_archetype_id,failed_stage3_total_score,failed_stage3_bottleneck,failed_stage3_visibility",
                        "000660,2024-05-01,C06_HBM_MEMORY_CUSTOMER_CAPACITY,True,True,False",
                        "005930,2024-04-01,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,True,True,True",
                        "267260,2023-08-01,C02_POWER_GRID_DATACENTER_CAPEX,True,True,False",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            weight_profile.write_text(
                '{"archetype_weights":{"C02_POWER_GRID_DATACENTER_CAPEX":{},"C06_HBM_MEMORY_CUSTOMER_CAPACITY":{},"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE":{},"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN":{}}}',
                encoding="utf-8",
            )

            payload = build_v12_component_score_loss_waterfall(
                score_csv_path=score_csv,
                gate_csv_path=gate_csv,
                weight_profile_path=weight_profile,
            )

        self.assertEqual(payload["summary"]["candidate_row_count"], 3)
        self.assertEqual(payload["summary"]["runtime_exercised_archetype_count"], 3)
        self.assertEqual(payload["summary"]["runtime_unexercised_archetype_count"], 1)
        self.assertEqual(payload["summary"]["stage3_green_count"], 0)
        self.assertEqual(payload["scoring_policy"], "diagnostic_only_no_weight_or_stage_change")

        focus_by_symbol = {row["symbol"]: row for row in payload["focus_rows"]}
        hynix = focus_by_symbol["000660"]
        hynix_components = {row["component"]: row for row in hynix["components"]}
        self.assertEqual(hynix_components["eps_fcf_explosion"]["loss_points"], 0.0)
        self.assertAlmostEqual(hynix_components["bottleneck_pricing"]["loss_points"], 7.9478)
        self.assertEqual(hynix["failed_gates"], ["failed_stage3_total_score", "failed_stage3_bottleneck"])

        by_arch = {row["group_key"]: row for row in payload["archetype_rows"]}
        c02_best = by_arch["C02_POWER_GRID_DATACENTER_CAPEX"]["best_row_waterfall"]
        self.assertEqual(c02_best["symbol"], "267260")
        self.assertAlmostEqual(c02_best["green_shortfall_to_87"], 14.0367)
        self.assertIn("bottleneck_pricing", c02_best["top_component_losses"][0]["component"])

        report = render_v12_component_score_loss_waterfall(payload)
        self.assertIn("HBM 점수를 올리기 위한 문서가 아니다", report)
        self.assertIn("bottleneck/pricing:11.0522/19.0(-7.9478)", report)
        self.assertIn("C02_POWER_GRID_DATACENTER_CAPEX", report)


if __name__ == "__main__":
    unittest.main()
