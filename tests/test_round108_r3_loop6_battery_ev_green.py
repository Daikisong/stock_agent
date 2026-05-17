import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round108_r3_loop6_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round108_r3_loop6_battery_ev_green import (
    ROUND108_CASE_CANDIDATES,
    ROUND108_PRICE_FIELDS,
    ROUND108_SCORE_TARGETS,
    render_round108_green_guardrail_markdown,
    render_round108_price_validation_plan_markdown,
    render_round108_risk_overlay_markdown,
    render_round108_summary_markdown,
    round108_case_candidate_rows,
    round108_case_records,
    round108_price_field_rows,
    round108_score_profile_rows,
    round108_stage_date_rows,
    round108_summary,
    round108_target_for,
    write_round108_r3_loop6_reports,
)


class Round108R3Loop6BatteryEVGreenTests(unittest.TestCase):
    def test_round108_targets_cover_r3_loop6_archetypes_and_overlays(self):
        labels = {target.target_id for target in ROUND108_SCORE_TARGETS}

        self.assertEqual(len(labels), 26)
        for label in (
            "BATTERY_MATERIALS_CAPEX_OVERHEAT",
            "BATTERY_EQUIPMENT_PARTS",
            "BATTERY_RECYCLING_ESS_SHIFT",
            "SECOND_LIFE_BATTERY_GRID_STORAGE",
            "ESS_LFP_GRID_STORAGE",
            "ESS_TESLA_MEGAPACK_SUPPLY_CHAIN",
            "ESS_AI_DATA_CENTER_STORAGE",
            "EV_TO_ESS_CAPACITY_REDEPLOYMENT",
            "EV_BATTERY_JV_RESTRUCTURING",
            "EV_CAPA_CONTRACT_CANCELLATION",
            "BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE",
            "EV_INFRASTRUCTURE",
            "HYDROGEN_FUEL_CELL_INFRA",
            "SOLAR_TARIFF_SUPPLYCHAIN",
            "RENEWABLE_ENERGY_PROJECT_ECONOMICS",
            "WASTE_RECYCLING_ENVIRONMENT",
            "CARBON_CREDIT_CBAM_COMPLIANCE",
            "DATA_CENTER_WATER_REUSE_INFRA",
            "EV_FIRE_BESS_SAFETY_OVERLAY",
            "BESS_SAFETY_PERMITTING",
            "BATTERY_SOH_SECOND_LIFE_TRANSPARENCY",
            "BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY",
            "LITHIUM_ESS_DEMAND_CYCLE",
            "SODIUM_ION_SUBSTITUTION_OVERLAY",
            "SOLID_STATE_COMMERCIALIZATION_LICENSE",
            "SPECULATIVE_BATTERY_TECH",
        ):
            self.assertIn(label, labels)
        for target in ROUND108_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.BATTERY_EV_GREEN)
            self.assertFalse(target.production_scoring_changed)

    def test_new_loop6_canonical_archetypes_exist(self):
        expected = (
            E2RArchetype.ESS_LFP_GRID_STORAGE,
            E2RArchetype.ESS_TESLA_MEGAPACK_SUPPLY_CHAIN,
            E2RArchetype.ESS_AI_DATA_CENTER_STORAGE,
            E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT,
            E2RArchetype.EV_BATTERY_JV_RESTRUCTURING,
            E2RArchetype.EV_CAPA_CONTRACT_CANCELLATION,
            E2RArchetype.BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE,
            E2RArchetype.SECOND_LIFE_BATTERY_GRID_STORAGE,
            E2RArchetype.BATTERY_SOH_SECOND_LIFE_TRANSPARENCY,
            E2RArchetype.EV_FIRE_BESS_SAFETY_OVERLAY,
            E2RArchetype.BESS_SAFETY_PERMITTING,
            E2RArchetype.RENEWABLE_ENERGY_PROJECT_ECONOMICS,
            E2RArchetype.BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY,
            E2RArchetype.LITHIUM_ESS_DEMAND_CYCLE,
            E2RArchetype.SODIUM_ION_SUBSTITUTION_OVERLAY,
            E2RArchetype.SOLID_STATE_COMMERCIALIZATION_LICENSE,
            E2RArchetype.SPECULATIVE_BATTERY_TECH,
        )

        for archetype in expected:
            self.assertIsInstance(archetype.value, str)

    def test_ess_and_waste_are_green_possible_while_materials_solar_and_health_are_guarded(self):
        ess = round108_target_for("ESS_LFP_GRID_STORAGE")
        waste = round108_target_for("WASTE_RECYCLING_ENVIRONMENT")
        materials = round108_target_for("BATTERY_MATERIALS_CAPEX_OVERHEAT")
        solar = round108_target_for("SOLAR_TARIFF_SUPPLYCHAIN")
        health = round108_target_for("BATTERY_SOH_SECOND_LIFE_TRANSPARENCY")
        disclosure = round108_target_for("BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE")
        ev_cancel = round108_target_for("EV_CAPA_CONTRACT_CANCELLATION")
        fire = round108_target_for("EV_FIRE_BESS_SAFETY_OVERLAY")
        bess = round108_target_for("BESS_SAFETY_PERMITTING")
        graphite = round108_target_for("BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY")
        solid_state = round108_target_for("SOLID_STATE_COMMERCIALIZATION_LICENSE")

        for target in (ess, waste, materials, solar, health, disclosure, ev_cancel, fire, bess, graphite, solid_state):
            self.assertIsNotNone(target)
        assert ess is not None
        assert waste is not None
        assert materials is not None
        assert solar is not None
        assert health is not None
        assert disclosure is not None
        assert ev_cancel is not None
        assert fire is not None
        assert bess is not None
        assert graphite is not None
        assert solid_state is not None
        self.assertEqual(ess.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("ess_contract_value", ess.green_conditions)
        self.assertIn("gwh_volume", ess.green_conditions)
        self.assertEqual(waste.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("recurring_fcf", waste.green_conditions)
        self.assertEqual(materials.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertIn("customer_contract_cancelled", materials.red_flags)
        self.assertEqual(solar.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertIn("uflpa_detention", solar.red_flags)
        self.assertEqual(health.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertTrue(health.gate_only)
        self.assertEqual(health.score_weight.eps_fcf, "gate")
        self.assertTrue(disclosure.gate_only)
        self.assertIn("customer_undisclosed", disclosure.red_flags)
        self.assertTrue(ev_cancel.gate_only)
        self.assertEqual(ev_cancel.score_weight.eps_fcf, "gate")
        self.assertIn("expected_revenue_loss", ev_cancel.red_flags)
        self.assertTrue(fire.gate_only)
        self.assertIn("bess_fire", fire.red_flags)
        self.assertTrue(bess.gate_only)
        self.assertIn("facility_permitting_delay", bess.red_flags)
        self.assertEqual(graphite.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("graphite_offtake", graphite.green_conditions)
        self.assertEqual(solid_state.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("royalty_framework", solid_state.stage2_signals)

    def test_tesla_megapack_supply_chain_is_watch_until_ramp_and_margin_are_visible(self):
        tesla = round108_target_for("ESS_TESLA_MEGAPACK_SUPPLY_CHAIN")

        self.assertIsNotNone(tesla)
        assert tesla is not None
        self.assertEqual(tesla.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertEqual(tesla.score_weight.eps_fcf, 23)
        self.assertEqual(tesla.score_weight.structural_visibility, 24)
        self.assertEqual(tesla.score_weight.information_confidence, 6)
        self.assertIn("tesla_megapack_use_case_confirmed", tesla.stage2_signals)
        self.assertIn("lansing_ramp_delay", tesla.red_flags)
        self.assertIn("ess_opm_unverified", tesla.red_flags)

    def test_lithium_is_cycle_overlay_not_structural_green_by_default(self):
        lithium = round108_target_for("LITHIUM_ESS_DEMAND_CYCLE")

        self.assertIsNotNone(lithium)
        assert lithium is not None
        self.assertEqual(lithium.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertEqual(lithium.score_weight.eps_fcf, "cycle")
        self.assertIn("mine_restart", lithium.red_flags)
        self.assertIn("sodium_ion", lithium.loop6_penalty_axes)

    def test_required_round108_cases_are_present_with_stage_markers(self):
        rows = {row["case_id"]: row for row in round108_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND108_CASE_CANDIDATES))
        self.assertEqual(rows["lg_energy_lfp_4_3b_contract_initial_case"]["target_id"], "BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE")
        self.assertEqual(rows["lg_energy_lfp_4_3b_contract_initial_case"]["stage2_date"], "2025-07-30")
        self.assertEqual(rows["tesla_lges_megapack3_lansing_case"]["target_id"], "ESS_TESLA_MEGAPACK_SUPPLY_CHAIN")
        self.assertEqual(rows["tesla_lges_megapack3_lansing_case"]["stage2_date"], "2026-03-17")
        self.assertEqual(rows["sk_on_flatiron_ess_7_2gwh_case"]["stage2_date"], "2025-09-03")
        self.assertEqual(rows["gm_lg_ultium_ohio_idle_case"]["target_id"], "EV_TO_ESS_CAPACITY_REDEPLOYMENT")
        self.assertEqual(rows["gm_lg_ultium_ohio_idle_case"]["stage4c_date"], "2026-05-12")
        self.assertEqual(rows["sk_on_ford_jv_dissolution_case"]["target_id"], "EV_BATTERY_JV_RESTRUCTURING")
        self.assertEqual(rows["sk_on_ford_jv_dissolution_case"]["stage2_date"], "2025-12-11")
        self.assertEqual(rows["ford_energy_storage_pivot_case"]["target_id"], "ESS_AI_DATA_CENTER_STORAGE")
        self.assertEqual(rows["ford_energy_storage_pivot_case"]["price_validation_status"], "needs_exact_stage_date_backfill")
        self.assertEqual(rows["ford_lges_ev_contract_cancel_case"]["target_id"], "EV_CAPA_CONTRACT_CANCELLATION")
        self.assertEqual(rows["ford_lges_ev_contract_cancel_case"]["stage4c_date"], "2025-12-17")
        self.assertEqual(rows["lges_freudenberg_contract_cancel_case"]["stage4c_date"], "2025-12-26")
        self.assertEqual(rows["redwood_recycling_energy_storage_case"]["stage4b_date"], "2025-10-23")
        self.assertEqual(rows["second_life_battery_grid_storage_reference_case"]["target_id"], "SECOND_LIFE_BATTERY_GRID_STORAGE")
        self.assertEqual(rows["graphite_supply_security_case"]["target_id"], "BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY")
        self.assertEqual(rows["eqt_kj_environment_waste_platform_case"]["case_type"], "structural_success")
        self.assertEqual(rows["hyundai_hydrogen_fuel_cell_plant_case"]["stage4b_date"], "2025-10-30")
        self.assertEqual(rows["qcells_customs_detention_furlough_case"]["stage4c_date"], "2025-11-08")
        self.assertEqual(rows["orsted_sunrise_wind_impairment_case"]["stage4c_date"], "2025-01-20")
        self.assertEqual(rows["lithium_price_86pct_crash_case"]["target_id"], "LITHIUM_ESS_DEMAND_CYCLE")
        self.assertEqual(rows["lithium_price_86pct_crash_case"]["stage4c_date"], "2025-01-13")
        self.assertEqual(rows["lithium_ess_demand_recovery_case"]["stage2_date"], "2026-01-04")
        self.assertEqual(rows["lithium_ess_demand_recovery_case"]["case_type"], "cyclical_success")
        self.assertEqual(rows["sodium_ion_substitution_watch_case"]["target_id"], "SODIUM_ION_SUBSTITUTION_OVERLAY")
        self.assertEqual(rows["korea_ev_battery_certification_fire_case"]["stage4c_date"], "2024-08-25")
        self.assertEqual(rows["moss_landing_bess_fire_case"]["target_id"], "BESS_SAFETY_PERMITTING")
        self.assertEqual(rows["moss_landing_bess_fire_case"]["stage4c_date"], "2025-01-17")
        self.assertEqual(rows["battery_soh_transparency_case"]["target_id"], "BATTERY_SOH_SECOND_LIFE_TRANSPARENCY")
        self.assertEqual(rows["quantumscape_vw_solid_state_license_case"]["target_id"], "SOLID_STATE_COMMERCIALIZATION_LICENSE")
        self.assertEqual(rows["quantumscape_vw_solid_state_license_case"]["stage2_date"], "2024-07-11")
        self.assertEqual(rows["speculative_solid_state_theme_case"]["target_id"], "SPECULATIVE_BATTERY_TECH")

    def test_case_records_validate_and_keep_loop6_guardrails(self):
        records = round108_case_records()

        self.assertEqual(len(records), len(ROUND108_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, "BATTERY_EV_GREEN")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_change_production_scoring", record.green_guardrails)
            self.assertIn("ev_growth_is_not_fcf_evidence", record.green_guardrails)
            self.assertIn("do_not_invent_contract_value_margin_utilization_customer_or_stage_prices", record.green_guardrails)
        by_id = {record.case_id: record for record in records}
        self.assertEqual(by_id["eqt_kj_environment_waste_platform_case"].rerating_result, "true_rerating")
        self.assertEqual(by_id["ford_lges_ev_contract_cancel_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["lges_freudenberg_contract_cancel_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["lg_energy_lfp_4_3b_contract_initial_case"].score_price_alignment, "evidence_good_but_price_failed")
        self.assertEqual(by_id["tesla_lges_megapack3_lansing_case"].score_price_alignment, "aligned")
        self.assertEqual(by_id["sk_on_flatiron_ess_7_2gwh_case"].score_price_alignment, "evidence_good_but_price_failed")
        self.assertEqual(by_id["sk_on_ford_jv_dissolution_case"].score_price_alignment, "aligned")
        self.assertEqual(by_id["graphite_supply_security_case"].score_price_alignment, "aligned")
        self.assertEqual(by_id["sodium_ion_substitution_watch_case"].score_price_alignment, "evidence_good_but_price_failed")
        self.assertEqual(by_id["lithium_ess_demand_recovery_case"].rerating_result, "cyclical_rerating")
        self.assertIn("soh_validation_failure", by_id["battery_soh_transparency_case"].red_flag_fields)
        self.assertEqual(by_id["quantumscape_vw_solid_state_license_case"].rerating_result, "unknown")
        self.assertEqual(by_id["speculative_solid_state_theme_case"].rerating_result, "theme_overheat")

    def test_score_profile_rows_match_round108_weight_table(self):
        rows = {row["target_id"]: row for row in round108_score_profile_rows()}

        self.assertEqual(rows["BATTERY_MATERIALS_CAPEX_OVERHEAT"]["eps_fcf"], "14")
        self.assertEqual(rows["BATTERY_MATERIALS_CAPEX_OVERHEAT"]["structural_visibility"], "9")
        self.assertEqual(rows["BATTERY_MATERIALS_CAPEX_OVERHEAT"]["valuation"], "6")
        self.assertEqual(rows["BATTERY_EQUIPMENT_PARTS"]["eps_fcf"], "18")
        self.assertEqual(rows["BATTERY_EQUIPMENT_PARTS"]["structural_visibility"], "15")
        self.assertEqual(rows["ESS_LFP_GRID_STORAGE"]["eps_fcf"], "22")
        self.assertEqual(rows["ESS_LFP_GRID_STORAGE"]["structural_visibility"], "21")
        self.assertEqual(rows["ESS_TESLA_MEGAPACK_SUPPLY_CHAIN"]["eps_fcf"], "23")
        self.assertEqual(rows["ESS_TESLA_MEGAPACK_SUPPLY_CHAIN"]["structural_visibility"], "24")
        self.assertEqual(rows["ESS_TESLA_MEGAPACK_SUPPLY_CHAIN"]["information_confidence"], "6")
        self.assertEqual(rows["ESS_AI_DATA_CENTER_STORAGE"]["bottleneck_pricing"], "16")
        self.assertEqual(rows["EV_TO_ESS_CAPACITY_REDEPLOYMENT"]["structural_visibility"], "17")
        self.assertEqual(rows["EV_BATTERY_JV_RESTRUCTURING"]["eps_fcf"], "15")
        self.assertEqual(rows["EV_BATTERY_JV_RESTRUCTURING"]["structural_visibility"], "13")
        self.assertEqual(rows["EV_CAPA_CONTRACT_CANCELLATION"]["gate_only"], "true")
        self.assertEqual(rows["BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE"]["gate_only"], "true")
        self.assertEqual(rows["SOLAR_TARIFF_SUPPLYCHAIN"]["eps_fcf"], "14")
        self.assertEqual(rows["SOLAR_TARIFF_SUPPLYCHAIN"]["structural_visibility"], "11")
        self.assertEqual(rows["RENEWABLE_ENERGY_PROJECT_ECONOMICS"]["eps_fcf"], "14")
        self.assertEqual(rows["RENEWABLE_ENERGY_PROJECT_ECONOMICS"]["structural_visibility"], "11")
        self.assertEqual(rows["WASTE_RECYCLING_ENVIRONMENT"]["structural_visibility"], "22")
        self.assertEqual(rows["CARBON_CREDIT_CBAM_COMPLIANCE"]["information_confidence"], "6")
        self.assertEqual(rows["SECOND_LIFE_BATTERY_GRID_STORAGE"]["eps_fcf"], "18")
        self.assertEqual(rows["SECOND_LIFE_BATTERY_GRID_STORAGE"]["structural_visibility"], "16")
        self.assertEqual(rows["BATTERY_SOH_SECOND_LIFE_TRANSPARENCY"]["gate_only"], "true")
        self.assertEqual(rows["BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY"]["bottleneck_pricing"], "16")
        self.assertEqual(rows["EV_FIRE_BESS_SAFETY_OVERLAY"]["gate_only"], "true")
        self.assertEqual(rows["BESS_SAFETY_PERMITTING"]["gate_only"], "true")
        self.assertEqual(rows["LITHIUM_ESS_DEMAND_CYCLE"]["eps_fcf"], "cycle")
        self.assertEqual(rows["SODIUM_ION_SUBSTITUTION_OVERLAY"]["gate_only"], "true")
        self.assertEqual(rows["SOLID_STATE_COMMERCIALIZATION_LICENSE"]["eps_fcf"], "12")
        self.assertEqual(rows["SPECULATIVE_BATTERY_TECH"]["eps_fcf"], "6")
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round108_stage_date_rows()}
        fields = {row["field"] for row in round108_price_field_rows()}

        self.assertIn("customer_contract_cancelled", rows["BATTERY_MATERIALS_CAPEX_OVERHEAT"]["stage4c"])
        self.assertIn("ess_contract_value", rows["ESS_LFP_GRID_STORAGE"]["stage2"])
        self.assertIn("tesla_megapack_use_case_confirmed", rows["ESS_TESLA_MEGAPACK_SUPPLY_CHAIN"]["stage2"])
        self.assertIn("expected_revenue_loss", rows["EV_CAPA_CONTRACT_CANCELLATION"]["stage4c"])
        self.assertIn("soh_validation_failure", rows["BATTERY_RECYCLING_ESS_SHIFT"]["stage4c"])
        self.assertIn("customs_detention", rows["SOLAR_TARIFF_SUPPLYCHAIN"]["stage4c"])
        self.assertIn("data_center_storage_customer", rows["ESS_AI_DATA_CENTER_STORAGE"]["stage2"])
        self.assertIn("ess_line_conversion_complete", rows["EV_TO_ESS_CAPACITY_REDEPLOYMENT"]["stage2"])
        self.assertIn("jv_dissolution", rows["EV_BATTERY_JV_RESTRUCTURING"]["stage1"])
        self.assertIn("customer_undisclosed", rows["BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE"]["stage4c"])
        self.assertIn("impairment", rows["RENEWABLE_ENERGY_PROJECT_ECONOMICS"]["stage4c"])
        self.assertIn("battery_supplier_disclosure", rows["EV_FIRE_BESS_SAFETY_OVERLAY"]["stage4c"])
        self.assertIn("bess_fire", rows["BESS_SAFETY_PERMITTING"]["stage4c"])
        self.assertIn("soh_unreliable", rows["BATTERY_SOH_SECOND_LIFE_TRANSPARENCY"]["stage4c"])
        self.assertIn("graphite_offtake", rows["BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY"]["stage2"])
        self.assertIn("mine_restart_supply_rebound", rows["LITHIUM_ESS_DEMAND_CYCLE"]["stage4c"])
        self.assertIn("sodium_ion_substitution", rows["SODIUM_ION_SUBSTITUTION_OVERLAY"]["stage4c"])
        self.assertIn("royalty_framework", rows["SOLID_STATE_COMMERCIALIZATION_LICENSE"]["stage2"])
        for field in (
            "ess_contract_value",
            "grid_storage_flag",
            "data_center_storage_flag",
            "ess_customer_disclosed_flag",
            "ess_use_case_disclosed_flag",
            "disclosure_confidence_score",
            "tesla_megapack_flag",
            "megapack_version",
            "lansing_production_flag",
            "production_start_year",
            "expected_revenue_loss",
            "contract_cancellation_reason",
            "opendart_rcept_no",
            "detail_parser_confidence",
            "ev_battery_jv_restructuring_flag",
            "jv_dissolution_flag",
            "plant_ownership_change",
            "operating_loss_amount",
            "ess_pivot_flag",
            "ev_to_ess_conversion_flag",
            "ai_data_center_storage_customer_flag",
            "ev_model_discontinued_flag",
            "recovery_rate",
            "graphite_supplychain_security_flag",
            "china_graphite_dependency_pct",
            "us_graphite_cost_premium",
            "policy_financing_flag",
            "graphite_offtake_flag",
            "soh_validation_flag",
            "second_life_grid_storage_flag",
            "battery_passport_compliance_flag",
            "battery_grading_cost",
            "solid_state_license_flag",
            "solid_state_license_capacity_gwh",
            "royalty_structure_flag",
            "vehicle_series_adoption_flag",
            "sodium_ion_substitution_flag",
            "sodium_ion_ess_flag",
            "sodium_ion_price_pressure_flag",
            "catchment_area_population_share",
            "hydrogen_capacity_utilization",
            "grid_connection_delay_flag",
            "underground_parking_regulation_flag",
            "overcharge_prevention_charger_flag",
            "bess_fire_event_flag",
            "facility_permitting_delay_flag",
            "fire_safety_capex_flag",
            "evacuation_flag",
            "local_opposition_flag",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND108_PRICE_FIELDS))

    def test_summary_and_markdown_explain_r3_loop6_guardrails(self):
        summary = round108_summary()
        summary_md = render_round108_summary_markdown()
        guardrails = render_round108_green_guardrail_markdown()
        overlays = render_round108_risk_overlay_markdown()
        price_plan = render_round108_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 26)
        self.assertEqual(summary["case_candidate_count"], 23)
        self.assertEqual(summary["structural_success_count"], 1)
        self.assertEqual(summary["success_candidate_count"], 10)
        self.assertEqual(summary["cyclical_success_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["stage4b_case_count"], 2)
        self.assertEqual(summary["stage4c_case_count"], 8)
        self.assertEqual(summary["green_possible_count"], 2)
        self.assertEqual(summary["watch_yellow_first_count"], 14)
        self.assertEqual(summary["redteam_first_count"], 10)
        self.assertEqual(summary["gate_only_target_count"], 6)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("R3 Loop 6", summary_md)
        self.assertIn("Do not apply R3 Loop-6 v6.0 weights", guardrails)
        self.assertIn("EV_CONTRACT_CANCELLATION_4C", overlays)
        self.assertIn("EV_JV_RESTRUCTURING_WATCH", overlays)
        self.assertIn("ESS_TESLA_MEGAPACK_ALIGNED", overlays)
        self.assertIn("ESS_DISCLOSURE_CAPPED", overlays)
        self.assertIn("GRAPHITE_SECURITY_BUT_COST_RISK", overlays)
        self.assertIn("SOLID_STATE_LICENSE_NOT_COMMERCIALIZATION", overlays)
        self.assertIn("EV_BESS_SAFETY_REGULATORY_OVERLAY", overlays)
        self.assertIn("BESS_SAFETY_PERMITTING_4C_WATCH", overlays)
        self.assertIn("tesla_lges_megapack3_lansing_case", price_plan)
        self.assertIn("lges_freudenberg_contract_cancel_case", price_plan)
        self.assertIn("sk_on_ford_jv_dissolution_case", price_plan)
        self.assertIn("quantumscape_vw_solid_state_license_case", price_plan)
        self.assertIn("battery_soh_transparency_case", price_plan)
        self.assertIn("speculative_solid_state_theme_case", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round108_r3_loop6_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r3_loop6_round108.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round108_r3_loop6_v6.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["stage_date_plan"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["risk_overlays"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertTrue(paths["price_fields"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND108_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round108_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round108_r3_loop6_battery_ev_green", text)


if __name__ == "__main__":
    unittest.main()
