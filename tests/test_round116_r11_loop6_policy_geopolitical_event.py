import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round116_r11_loop6_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round116_r11_loop6_policy_geopolitical_event import (
    ROUND116_CASE_CANDIDATES,
    ROUND116_PRICE_FIELDS,
    ROUND116_SCORE_TARGETS,
    render_round116_event_false_positive_caps_markdown,
    render_round116_green_guardrail_markdown,
    render_round116_price_validation_plan_markdown,
    render_round116_summary_markdown,
    round116_case_candidate_rows,
    round116_case_records,
    round116_price_field_rows,
    round116_score_profile_rows,
    round116_stage_date_rows,
    round116_summary,
    target_for,
    write_round116_r11_loop6_reports,
)


class Round116R11Loop6PolicyGeopoliticalEventTests(unittest.TestCase):
    def test_round116_targets_cover_r11_loop6_archetypes(self):
        labels = {target.target_id for target in ROUND116_SCORE_TARGETS}

        self.assertEqual(len(labels), 24)
        for label in (
            "NORTH_KOREA_POLICY_EVENT",
            "GEOPOLITICAL_RECONSTRUCTION",
            "REAL_RECONSTRUCTION_FINANCING",
            "CRITICAL_INFRA_RECONSTRUCTION_FINANCING",
            "STRATEGIC_SUPPLY_CHAIN_EXPORT_CONTROL_EVENT",
            "EXPORT_CONTROL_TO_OFFTAKE_ESCALATION",
            "DISASTER_REBUILD_EVENT",
            "CLIMATE_DISASTER_EVENT",
            "CLIMATE_EVENT_TO_GRID_INFRA",
            "EVENT_DISEASE_PEST_DEMAND",
            "GOVERNMENT_STOCKPILE_REVENUE_GUIDANCE",
            "PUBLIC_HEALTH_PROCUREMENT_REVERSAL",
            "DIAGNOSTICS_INFECTIOUS_EVENT",
            "SPECULATIVE_SCIENCE_THEME",
            "ADVANCED_MATERIAL_SPECULATIVE_THEME",
            "POLICY_LOCAL_THEME",
            "TOURISM_POLICY_EVENT",
            "INDUSTRIAL_POLICY_TARIFF_EVENT",
            "POLICY_MARKET_SHOCK_EVENT",
            "AI_WINDFALL_CITIZEN_DIVIDEND_POLICY_SHOCK",
            "ONE_OFF_EVENT_DEMAND",
            "EVENT_TO_CONTRACT_ESCALATION",
            "THEME_VALUATION_OVERHEAT",
            "DISCLOSURE_CONFIDENCE_CAP",
        ):
            self.assertIn(label, labels)
        for target in ROUND116_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.POLICY_GEOPOLITICAL_EVENT)
            self.assertFalse(target.production_scoring_changed)

    def test_event_procurement_and_disclosure_gates_are_explicit(self):
        event_to_contract = target_for("EVENT_TO_CONTRACT_ESCALATION")
        policy_shock = target_for("POLICY_MARKET_SHOCK_EVENT")
        overheat = target_for("THEME_VALUATION_OVERHEAT")
        north_korea = target_for("NORTH_KOREA_POLICY_EVENT")
        real_reconstruction = target_for("REAL_RECONSTRUCTION_FINANCING")
        critical_infra = target_for("CRITICAL_INFRA_RECONSTRUCTION_FINANCING")
        export_control = target_for("STRATEGIC_SUPPLY_CHAIN_EXPORT_CONTROL_EVENT")
        export_to_offtake = target_for("EXPORT_CONTROL_TO_OFFTAKE_ESCALATION")
        climate_grid = target_for("CLIMATE_EVENT_TO_GRID_INFRA")
        gov_stockpile = target_for("GOVERNMENT_STOCKPILE_REVENUE_GUIDANCE")
        public_health = target_for("PUBLIC_HEALTH_PROCUREMENT_REVERSAL")
        tourism = target_for("TOURISM_POLICY_EVENT")
        industrial_tariff = target_for("INDUSTRIAL_POLICY_TARIFF_EVENT")
        ai_policy_shock = target_for("AI_WINDFALL_CITIZEN_DIVIDEND_POLICY_SHOCK")
        disclosure_cap = target_for("DISCLOSURE_CONFIDENCE_CAP")

        assert event_to_contract is not None
        assert policy_shock is not None
        assert overheat is not None
        assert north_korea is not None
        assert real_reconstruction is not None
        assert critical_infra is not None
        assert export_control is not None
        assert export_to_offtake is not None
        assert climate_grid is not None
        assert gov_stockpile is not None
        assert public_health is not None
        assert tourism is not None
        assert industrial_tariff is not None
        assert ai_policy_shock is not None
        assert disclosure_cap is not None
        self.assertEqual(event_to_contract.canonical_archetype, E2RArchetype.EVENT_TO_CONTRACT_ESCALATION)
        self.assertEqual(event_to_contract.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("actual_contract", event_to_contract.green_conditions)
        self.assertIn("budget_or_financing", event_to_contract.green_conditions)
        self.assertEqual(event_to_contract.score_weight.eps_fcf, 15)
        self.assertEqual(gov_stockpile.canonical_archetype, E2RArchetype.GOVERNMENT_STOCKPILE_REVENUE_GUIDANCE)
        self.assertEqual(gov_stockpile.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertEqual(gov_stockpile.score_weight.eps_fcf, 16)
        self.assertIn("guidance_raised_flag", gov_stockpile.green_conditions)
        self.assertEqual(public_health.score_weight.as_csv_dict()["eps_fcf"], "gate")
        self.assertTrue(public_health.gate_only)
        self.assertIn("funding_withdrawal", public_health.stage4c_conditions)
        self.assertEqual(policy_shock.score_weight.as_csv_dict()["eps_fcf"], "gate")
        self.assertTrue(policy_shock.gate_only)
        self.assertIn("market_wide_policy_shock", policy_shock.stage4c_conditions)
        self.assertEqual(overheat.score_weight.as_csv_dict()["eps_fcf"], "gate")
        self.assertTrue(overheat.gate_only)
        self.assertEqual(north_korea.score_weight.structural_visibility, 3)
        self.assertIn("facility_dismantle", north_korea.stage4c_conditions)
        self.assertEqual(real_reconstruction.canonical_archetype, E2RArchetype.REAL_RECONSTRUCTION_FINANCING)
        self.assertIn("operating_company", real_reconstruction.green_conditions)
        self.assertEqual(real_reconstruction.score_weight.structural_visibility, 15)
        self.assertEqual(critical_infra.canonical_archetype, E2RArchetype.CRITICAL_INFRA_RECONSTRUCTION_FINANCING)
        self.assertIn("critical_infra_asset", critical_infra.green_conditions)
        self.assertEqual(critical_infra.score_weight.structural_visibility, 16)
        self.assertEqual(export_control.canonical_archetype, E2RArchetype.STRATEGIC_SUPPLY_CHAIN_EXPORT_CONTROL_EVENT)
        self.assertIn("domestic_capacity_flag", export_control.green_conditions)
        self.assertEqual(export_control.score_weight.bottleneck_pricing, 17)
        self.assertEqual(export_to_offtake.canonical_archetype, E2RArchetype.EXPORT_CONTROL_TO_OFFTAKE_ESCALATION)
        self.assertIn("offtake_contract_flag", export_to_offtake.green_conditions)
        self.assertEqual(export_to_offtake.score_weight.structural_visibility, 17)
        self.assertEqual(climate_grid.canonical_archetype, E2RArchetype.CLIMATE_EVENT_TO_GRID_INFRA)
        self.assertIn("vpp_program", climate_grid.green_conditions)
        self.assertEqual(climate_grid.score_weight.bottleneck_pricing, 13)
        self.assertEqual(tourism.canonical_archetype, E2RArchetype.TOURISM_POLICY_EVENT)
        self.assertIn("hotel_revpar", tourism.green_conditions)
        self.assertEqual(tourism.score_weight.market_mispricing, 10)
        self.assertEqual(industrial_tariff.canonical_archetype, E2RArchetype.INDUSTRIAL_POLICY_TARIFF_EVENT)
        self.assertIn("tariff_reversal", industrial_tariff.red_flags)
        self.assertEqual(ai_policy_shock.score_weight.as_csv_dict()["eps_fcf"], "gate")
        self.assertTrue(ai_policy_shock.gate_only)
        self.assertIn("crowded_trade_unwind", ai_policy_shock.stage4c_conditions)
        self.assertEqual(disclosure_cap.score_weight.as_csv_dict()["eps_fcf"], "cap")
        self.assertEqual(disclosure_cap.score_weight.as_csv_dict()["information_confidence"], "+")
        self.assertFalse(disclosure_cap.gate_only)

    def test_required_round116_cases_are_present_with_stage_dates(self):
        rows = {row["case_id"]: row for row in round116_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND116_CASE_CANDIDATES))
        self.assertEqual(rows["bavarian_nordic_us_stockpile_contract_case"]["target_id"], "GOVERNMENT_STOCKPILE_REVENUE_GUIDANCE")
        self.assertEqual(rows["bavarian_nordic_us_stockpile_contract_case"]["stage2_date"], "2026-05-11")
        self.assertEqual(rows["moderna_cepi_bird_flu_funding_case"]["target_id"], "PUBLIC_HEALTH_PROCUREMENT_REVERSAL")
        self.assertEqual(rows["moderna_cepi_bird_flu_funding_case"]["stage2_date"], "2025-12-18")
        self.assertEqual(rows["moderna_barda_contract_cancel_case"]["stage4c_date"], "2025-05-29")
        self.assertEqual(rows["bavarian_nordic_2024_mpox_order_case"]["case_type"], "event_premium")
        self.assertEqual(rows["bavarian_nordic_2024_mpox_order_case"]["stage4b_date"], "2024-08-16")
        self.assertEqual(rows["ukraine_telecom_ebrd_ifc_case"]["stage2_date"], "2024-10-10")
        self.assertEqual(rows["ukraine_telecom_ebrd_ifc_case"]["target_id"], "REAL_RECONSTRUCTION_FINANCING")
        self.assertEqual(rows["ukraine_ebrd_power_port_concession_case"]["target_id"], "CRITICAL_INFRA_RECONSTRUCTION_FINANCING")
        self.assertEqual(rows["ukraine_ebrd_power_port_concession_case"]["stage2_date"], "2026-05-15")
        self.assertEqual(rows["china_rare_earth_export_delay_case"]["target_id"], "STRATEGIC_SUPPLY_CHAIN_EXPORT_CONTROL_EVENT")
        self.assertEqual(rows["china_rare_earth_export_delay_case"]["stage2_date"], "2026-05-15")
        self.assertEqual(rows["china_rare_earth_export_delay_case"]["stage4b_date"], "2026-05-15")
        self.assertEqual(rows["heatwave_ac_grid_stress_case"]["stage2_date"], "2025-07-18")
        self.assertEqual(rows["heatwave_ac_grid_stress_case"]["target_id"], "CLIMATE_EVENT_TO_GRID_INFRA")
        self.assertEqual(rows["nyc_ac_battery_vpp_case"]["stage2_date"], "2026-05-01")
        self.assertEqual(rows["nyc_ac_battery_vpp_case"]["target_id"], "CLIMATE_EVENT_TO_GRID_INFRA")
        self.assertEqual(rows["north_korea_kumgang_dismantle_case"]["stage4c_date"], "2025-02-13")
        self.assertEqual(rows["lk99_superconductor_no_replication_case"]["stage4c_date"], "2023-08-08")
        self.assertEqual(rows["lk99_cu2s_impurity_case"]["stage4c_date"], "2023-11-01")
        self.assertEqual(rows["abbott_diagnostics_demand_wane_case"]["stage4c_date"], "2025-10-15")
        self.assertEqual(rows["yellow_dust_mask_event_case"]["target_id"], "ONE_OFF_EVENT_DEMAND")
        self.assertEqual(rows["china_group_visa_tourism_policy_case"]["target_id"], "TOURISM_POLICY_EVENT")
        self.assertEqual(rows["china_group_visa_tourism_policy_case"]["case_type"], "event_premium")
        self.assertEqual(rows["ai_citizen_dividend_policy_shock_case"]["target_id"], "AI_WINDFALL_CITIZEN_DIVIDEND_POLICY_SHOCK")
        self.assertEqual(rows["ai_citizen_dividend_policy_shock_case"]["stage4b_date"], "2026-05-12")

    def test_case_records_validate_and_keep_round116_guardrails(self):
        records = round116_case_records()

        self.assertEqual(len(records), len(ROUND116_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_change_production_scoring", record.green_guardrails)
            self.assertIn("event_news_is_not_green_evidence_alone", record.green_guardrails)
            self.assertIn("contract_budget_order_financing_revenue_or_eps_required", record.green_guardrails)
            self.assertIn("do_not_invent_contracts_budgets_orders_financing_stage_prices_or_guidance", record.green_guardrails)
        by_id = {record.case_id: record for record in records}
        self.assertEqual(by_id["bavarian_nordic_us_stockpile_contract_case"].score_price_alignment, "aligned")
        self.assertEqual(by_id["bavarian_nordic_us_stockpile_contract_case"].primary_archetype, E2RArchetype.GOVERNMENT_STOCKPILE_REVENUE_GUIDANCE)
        self.assertEqual(by_id["moderna_cepi_bird_flu_funding_case"].score_price_alignment, "aligned")
        self.assertEqual(by_id["moderna_barda_contract_cancel_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["ukraine_ebrd_power_port_concession_case"].score_price_alignment, "aligned")
        self.assertEqual(by_id["china_rare_earth_export_delay_case"].score_price_alignment, "aligned")
        self.assertEqual(by_id["china_rare_earth_export_delay_case"].primary_archetype, E2RArchetype.STRATEGIC_SUPPLY_CHAIN_EXPORT_CONTROL_EVENT)
        self.assertEqual(by_id["yellow_dust_mask_event_case"].score_price_alignment, "price_moved_without_evidence")
        self.assertEqual(by_id["ai_citizen_dividend_policy_shock_case"].rerating_result, "theme_overheat")
        self.assertEqual(by_id["lk99_superconductor_no_replication_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["abbott_diagnostics_demand_wane_case"].rerating_result, "thesis_break")

    def test_score_profile_rows_match_round116_weight_table(self):
        rows = {row["target_id"]: row for row in round116_score_profile_rows()}

        self.assertEqual(rows["NORTH_KOREA_POLICY_EVENT"]["eps_fcf"], "4")
        self.assertEqual(rows["NORTH_KOREA_POLICY_EVENT"]["structural_visibility"], "3")
        self.assertEqual(rows["GEOPOLITICAL_RECONSTRUCTION"]["structural_visibility"], "11")
        self.assertEqual(rows["REAL_RECONSTRUCTION_FINANCING"]["structural_visibility"], "15")
        self.assertEqual(rows["CRITICAL_INFRA_RECONSTRUCTION_FINANCING"]["structural_visibility"], "16")
        self.assertEqual(rows["STRATEGIC_SUPPLY_CHAIN_EXPORT_CONTROL_EVENT"]["bottleneck_pricing"], "17")
        self.assertEqual(rows["EXPORT_CONTROL_TO_OFFTAKE_ESCALATION"]["structural_visibility"], "17")
        self.assertEqual(rows["CLIMATE_DISASTER_EVENT"]["structural_visibility"], "14")
        self.assertEqual(rows["CLIMATE_DISASTER_EVENT"]["bottleneck_pricing"], "11")
        self.assertEqual(rows["CLIMATE_EVENT_TO_GRID_INFRA"]["structural_visibility"], "16")
        self.assertEqual(rows["CLIMATE_EVENT_TO_GRID_INFRA"]["bottleneck_pricing"], "13")
        self.assertEqual(rows["EVENT_DISEASE_PEST_DEMAND"]["eps_fcf"], "13")
        self.assertEqual(rows["GOVERNMENT_STOCKPILE_REVENUE_GUIDANCE"]["eps_fcf"], "16")
        self.assertEqual(rows["PUBLIC_HEALTH_PROCUREMENT_REVERSAL"]["eps_fcf"], "gate")
        self.assertEqual(rows["PUBLIC_HEALTH_PROCUREMENT_REVERSAL"]["gate_only"], "true")
        self.assertEqual(rows["DIAGNOSTICS_INFECTIOUS_EVENT"]["eps_fcf"], "19")
        self.assertEqual(rows["EVENT_TO_CONTRACT_ESCALATION"]["eps_fcf"], "15")
        self.assertEqual(rows["TOURISM_POLICY_EVENT"]["eps_fcf"], "8")
        self.assertEqual(rows["TOURISM_POLICY_EVENT"]["market_mispricing"], "10")
        self.assertEqual(rows["INDUSTRIAL_POLICY_TARIFF_EVENT"]["eps_fcf"], "10")
        self.assertEqual(rows["POLICY_MARKET_SHOCK_EVENT"]["eps_fcf"], "gate")
        self.assertEqual(rows["POLICY_MARKET_SHOCK_EVENT"]["gate_only"], "true")
        self.assertEqual(rows["AI_WINDFALL_CITIZEN_DIVIDEND_POLICY_SHOCK"]["eps_fcf"], "gate")
        self.assertEqual(rows["AI_WINDFALL_CITIZEN_DIVIDEND_POLICY_SHOCK"]["gate_only"], "true")
        self.assertEqual(rows["THEME_VALUATION_OVERHEAT"]["eps_fcf"], "gate")
        self.assertEqual(rows["THEME_VALUATION_OVERHEAT"]["gate_only"], "true")
        self.assertEqual(rows["DISCLOSURE_CONFIDENCE_CAP"]["eps_fcf"], "cap")
        self.assertEqual(rows["DISCLOSURE_CONFIDENCE_CAP"]["information_confidence"], "+")
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round116_stage_date_rows()}
        fields = {row["field"] for row in round116_price_field_rows()}

        self.assertIn("sanctions_relief", rows["NORTH_KOREA_POLICY_EVENT"]["stage2"])
        self.assertIn("project_financing", rows["GEOPOLITICAL_RECONSTRUCTION"]["stage2"])
        self.assertIn("ebrd_ifc_financing", rows["REAL_RECONSTRUCTION_FINANCING"]["stage2"])
        self.assertIn("concession_signed", rows["CRITICAL_INFRA_RECONSTRUCTION_FINANCING"]["stage2"])
        self.assertIn("export_license_delay_flag", rows["STRATEGIC_SUPPLY_CHAIN_EXPORT_CONTROL_EVENT"]["stage2"])
        self.assertIn("offtake_contract", rows["EXPORT_CONTROL_TO_OFFTAKE_ESCALATION"]["stage2"])
        self.assertIn("vpp_program", rows["CLIMATE_DISASTER_EVENT"]["stage2"])
        self.assertIn("vpp_program", rows["CLIMATE_EVENT_TO_GRID_INFRA"]["stage2"])
        self.assertIn("guidance_raised_flag", rows["GOVERNMENT_STOCKPILE_REVENUE_GUIDANCE"]["stage2"])
        self.assertIn("funding_withdrawal", rows["PUBLIC_HEALTH_PROCUREMENT_REVERSAL"]["stage4c"])
        self.assertIn("tourist_arrivals_after_policy", rows["TOURISM_POLICY_EVENT"]["stage2"])
        self.assertIn("actual_bill_or_rule", rows["INDUSTRIAL_POLICY_TARIFF_EVENT"]["stage2"])
        self.assertIn("market_wide_policy_shock", rows["POLICY_MARKET_SHOCK_EVENT"]["stage4c"])
        self.assertIn("crowded_trade_unwind", rows["AI_WINDFALL_CITIZEN_DIVIDEND_POLICY_SHOCK"]["stage4c"])
        self.assertIn("replication_failure", rows["SPECULATIVE_SCIENCE_THEME"]["stage4c"])
        self.assertIn("detail_fetch_required", rows["DISCLOSURE_CONFIDENCE_CAP"]["stage2"])
        for field in (
            "MFE_5D",
            "MFE_180D",
            "MAE_5D",
            "MAE_180D",
            "actual_contract_flag",
            "stockpile_contract_flag",
            "vaccine_stockpile_flag",
            "public_procurement_agency",
            "procurement_reversal_flag",
            "government_funding_cancelled_flag",
            "funding_withdrawal_amount",
            "project_financing_flag",
            "financing_amount",
            "guarantee_structure_flag",
            "operating_company_flag",
            "infrastructure_asset_flag",
            "critical_infra_flag",
            "port_concession_flag",
            "transformer_shelter_flag",
            "renewable_capacity_mw",
            "export_control_flag",
            "export_license_delay_flag",
            "rare_earth_export_control_flag",
            "yttrium_delay_flag",
            "alternative_supply_contract_flag",
            "offtake_contract_flag",
            "price_floor_flag",
            "domestic_capacity_flag",
            "vpp_program_flag",
            "battery_program_capacity",
            "battery_program_households",
            "guidance_raised_flag",
            "tax_policy_event_flag",
            "visa_policy_event_flag",
            "tourist_arrivals_after_policy",
            "duty_free_sales_after_policy",
            "hotel_revpar_after_policy",
            "citizen_dividend_comment_flag",
            "market_wide_selloff_flag",
            "replication_failure_flag",
            "impurity_explanation_flag",
            "diagnostic_sales_change",
            "facility_dismantle_flag",
            "road_rail_destroyed_flag",
            "event_to_contract_flag",
            "event_to_infra_crossover_flag",
            "supply_chain_export_control_event_flag",
            "export_control_to_offtake_escalation_flag",
            "government_stockpile_guidance_aligned_flag",
            "procurement_reversal_4c_flag",
            "critical_infra_financing_aligned_flag",
            "disclosure_confidence_capped_flag",
            "opendart_detail_fetched_flag",
            "disclosure_signal_class",
            "speculative_science_failure_flag",
            "score_price_alignment",
            "review_notes",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND116_PRICE_FIELDS))

    def test_summary_and_markdown_explain_r11_loop6_guardrails(self):
        summary = round116_summary()
        summary_md = render_round116_summary_markdown()
        guardrails = render_round116_green_guardrail_markdown()
        caps = render_round116_event_false_positive_caps_markdown()
        price_plan = render_round116_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 24)
        self.assertEqual(summary["case_candidate_count"], 18)
        self.assertEqual(summary["success_candidate_count"], 7)
        self.assertEqual(summary["event_premium_count"], 5)
        self.assertEqual(summary["stage4b_case_count"], 3)
        self.assertEqual(summary["stage4c_case_count"], 5)
        self.assertEqual(summary["green_possible_count"], 0)
        self.assertEqual(summary["watch_yellow_first_count"], 12)
        self.assertEqual(summary["redteam_first_count"], 12)
        self.assertEqual(summary["gate_only_target_count"], 4)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("Round-116", summary_md)
        self.assertIn("Do not apply these R11 Loop-6 v6 weights", guardrails)
        self.assertIn("REAL_RECONSTRUCTION_FINANCING", guardrails)
        self.assertIn("CRITICAL_INFRA_RECONSTRUCTION_FINANCING", guardrails)
        self.assertIn("STRATEGIC_SUPPLY_CHAIN_EXPORT_CONTROL_EVENT", guardrails)
        self.assertIn("EXPORT_CONTROL_TO_OFFTAKE_ESCALATION", guardrails)
        self.assertIn("CLIMATE_EVENT_TO_GRID_INFRA", guardrails)
        self.assertIn("TOURISM_POLICY_EVENT", guardrails)
        self.assertIn("EVENT_TO_CONTRACT", caps)
        self.assertIn("GOVERNMENT_STOCKPILE_GUIDANCE_ALIGNED", caps)
        self.assertIn("PROCUREMENT_REVERSAL_4C", caps)
        self.assertIn("CRITICAL_INFRA_FINANCING_ALIGNED", caps)
        self.assertIn("SUPPLY_CHAIN_EXPORT_CONTROL_EVENT", caps)
        self.assertIn("EXPORT_CONTROL_TO_OFFTAKE_ESCALATION", caps)
        self.assertIn("DISCLOSURE_CONFIDENCE_CAPPED", caps)
        self.assertIn("POLICY_MARKET_SHOCK", caps)
        self.assertIn("moderna_barda_contract_cancel_case", price_plan)
        self.assertIn("china_rare_earth_export_delay_case", price_plan)
        self.assertIn("ai_citizen_dividend_policy_shock_case", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round116_r11_loop6_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r11_loop6_round116.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round116_r11_loop6_v6.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["stage_date_plan"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["event_false_positive_caps"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertTrue(paths["price_fields"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND116_CASE_CANDIDATES))

    def test_cli_argument_parser_supports_paths(self):
        args = build_parser().parse_args(
            [
                "--output-directory",
                "out",
                "--cases",
                "cases.jsonl",
                "--score-profiles",
                "scores.csv",
            ]
        )

        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.score_profiles, "scores.csv")

    def test_production_scoring_modules_do_not_import_round116_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round116_r11_loop6_policy_geopolitical_event", text)


if __name__ == "__main__":
    unittest.main()
