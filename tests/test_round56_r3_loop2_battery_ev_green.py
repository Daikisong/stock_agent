import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round56_r3_loop2_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round56_r3_loop2_battery_ev_green import (
    ROUND56_CASE_CANDIDATES,
    ROUND56_PRICE_FIELDS,
    ROUND56_SCORE_TARGETS,
    render_round56_green_guardrail_markdown,
    render_round56_price_validation_plan_markdown,
    render_round56_risk_overlay_markdown,
    render_round56_summary_markdown,
    round56_case_candidate_rows,
    round56_case_records,
    round56_price_field_rows,
    round56_score_profile_rows,
    round56_stage_date_rows,
    round56_summary,
    target_for,
    write_round56_r3_loop2_reports,
)


class Round56R3Loop2BatteryEVGreenTests(unittest.TestCase):
    def test_round56_targets_cover_r3_loop2_archetypes(self):
        labels = {target.target_id for target in ROUND56_SCORE_TARGETS}

        self.assertEqual(len(labels), 12)
        for label in (
            "BATTERY_MATERIALS_CAPEX_OVERHEAT",
            "BATTERY_EQUIPMENT_PARTS",
            "BATTERY_RECYCLING_ESS_SHIFT",
            "EV_INFRASTRUCTURE",
            "HYDROGEN_FUEL_CELL_INFRA",
            "SOLAR_TARIFF_SUPPLYCHAIN",
            "RENEWABLE_ENERGY_POLICY",
            "WASTE_RECYCLING_ENVIRONMENT",
            "CARBON_CREDIT_CBAM_COMPLIANCE",
            "DATA_CENTER_WATER_REUSE_INFRA",
            "EV_FIRE_RISK_OVERLAY",
        ):
            self.assertIn(label, labels)
        for target in ROUND56_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.BATTERY_EV_GREEN)
            self.assertFalse(target.production_scoring_changed)

    def test_new_r3_loop2_canonical_archetypes_exist(self):
        expected = (
            E2RArchetype.BATTERY_EQUIPMENT_PARTS,
            E2RArchetype.BATTERY_RECYCLING_ESS_SHIFT,
            E2RArchetype.EV_INFRASTRUCTURE,
            E2RArchetype.HYDROGEN_FUEL_CELL_INFRA,
            E2RArchetype.SOLAR_TARIFF_SUPPLYCHAIN,
            E2RArchetype.RENEWABLE_ENERGY_POLICY,
            E2RArchetype.WASTE_RECYCLING_ENVIRONMENT,
            E2RArchetype.CARBON_CREDIT_CBAM_COMPLIANCE,
            E2RArchetype.DATA_CENTER_WATER_REUSE_INFRA,
            E2RArchetype.EV_FIRE_RISK_OVERLAY,
        )

        for archetype in expected:
            self.assertIsInstance(archetype.value, str)

    def test_waste_is_green_possible_while_materials_solar_and_fire_are_redteam_first(self):
        waste = target_for("WASTE_RECYCLING_ENVIRONMENT")
        materials = target_for("BATTERY_MATERIALS_CAPEX_OVERHEAT")
        solar = target_for("SOLAR_TARIFF_SUPPLYCHAIN")
        fire = target_for("EV_FIRE_RISK_OVERLAY")

        self.assertIsNotNone(waste)
        self.assertIsNotNone(materials)
        self.assertIsNotNone(solar)
        self.assertIsNotNone(fire)
        assert waste is not None
        assert materials is not None
        assert solar is not None
        assert fire is not None
        self.assertEqual(waste.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("recurring_fcf", waste.green_conditions)
        self.assertEqual(materials.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertIn("customer_contract_cancelled", materials.red_flags)
        self.assertIn("plant_idle", materials.red_flags)
        self.assertEqual(solar.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertIn("customs_detention", solar.red_flags)
        self.assertIn("uflpa_detention", solar.red_flags)
        self.assertEqual(fire.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertTrue(fire.gate_only)
        self.assertEqual(fire.score_weight.eps_fcf, "gate")

    def test_ess_is_upweighted_but_still_needs_contract_value_margin_and_utilization(self):
        ess = target_for("BATTERY_RECYCLING_ESS_SHIFT")

        self.assertIsNotNone(ess)
        assert ess is not None
        self.assertEqual(ess.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertEqual(ess.score_weight.eps_fcf, 21)
        self.assertEqual(ess.score_weight.structural_visibility, 18)
        self.assertIn("ess_contract", ess.green_conditions)
        self.assertIn("metal_recovery_revenue", ess.green_conditions)
        self.assertIn("contract_value_missing", ess.red_flags)

    def test_solar_wind_and_lithium_have_explicit_4c_risks(self):
        solar = target_for("SOLAR_TARIFF_SUPPLYCHAIN")
        wind = target_for("RENEWABLE_ENERGY_POLICY")
        materials = target_for("BATTERY_MATERIALS_CAPEX_OVERHEAT")

        assert solar is not None
        assert wind is not None
        assert materials is not None
        self.assertIn("customs_detention", solar.stage4c_conditions)
        self.assertIn("feoc_risk", solar.stage4c_conditions)
        self.assertIn("impairment", wind.stage4c_conditions)
        self.assertIn("foundation_cost", wind.stage4c_conditions)
        self.assertIn("lithium_price_crash", materials.red_flags)

    def test_required_round56_cases_are_present_with_dates_and_alignment(self):
        rows = {row["case_id"]: row for row in round56_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND56_CASE_CANDIDATES))
        self.assertEqual(rows["lg_energy_solution_ess_shift_case"]["stage2_date"], "2025-07-25")
        self.assertEqual(rows["lg_energy_tesla_lfp_ess_contract_case"]["stage2_date"], "2025-07-30")
        self.assertEqual(rows["sk_on_flatiron_ess_7_2gwh_case"]["stage2_date"], "2025-09-03")
        self.assertEqual(rows["redwood_recycling_energy_storage_case"]["stage4b_date"], "2025-10-23")
        self.assertEqual(rows["hyundai_hydrogen_fuel_cell_plant_case"]["stage2_date"], "2025-10-30")
        self.assertEqual(rows["eqt_kj_environment_waste_platform_case"]["stage2_date"], "2024-08-16")
        self.assertEqual(rows["gm_lg_ultium_ohio_idle_case"]["stage4c_date"], "2026-05-12")
        self.assertEqual(rows["ford_lges_ev_contract_cancel_case"]["stage4c_date"], "2025-12-17")
        self.assertEqual(rows["qcells_customs_detention_furlough_case"]["stage4c_date"], "2025-11-08")
        self.assertEqual(rows["orsted_sunrise_wind_impairment_case"]["stage4c_date"], "2025-01-20")
        self.assertEqual(rows["korea_ev_battery_certification_fire_case"]["stage4c_date"], "2024-08-25")

    def test_case_records_validate_and_keep_loop2_guardrails(self):
        records = round56_case_records()

        self.assertEqual(len(records), len(ROUND56_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_change_production_scoring", record.green_guardrails)
            self.assertIn("ev_growth_is_not_fcf_evidence", record.green_guardrails)
            self.assertIn("do_not_invent_contract_value_margin_utilization_or_stage_prices", record.green_guardrails)
        by_id = {record.case_id: record for record in records}
        self.assertEqual(by_id["lg_energy_solution_ess_shift_case"].score_price_alignment, "evidence_good_but_price_failed")
        self.assertEqual(by_id["eqt_kj_environment_waste_platform_case"].rerating_result, "true_rerating")
        self.assertEqual(by_id["ford_lges_ev_contract_cancel_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["gm_lg_ultium_ohio_idle_case"].score_price_alignment, "false_positive_score")

    def test_score_profile_rows_match_round56_weight_table(self):
        rows = {row["target_id"]: row for row in round56_score_profile_rows()}

        self.assertEqual(rows["BATTERY_MATERIALS_CAPEX_OVERHEAT"]["eps_fcf"], "18")
        self.assertEqual(rows["BATTERY_MATERIALS_CAPEX_OVERHEAT"]["valuation"], "8")
        self.assertEqual(rows["BATTERY_RECYCLING_ESS_SHIFT"]["eps_fcf"], "21")
        self.assertEqual(rows["WASTE_RECYCLING_ENVIRONMENT"]["structural_visibility"], "22")
        self.assertEqual(rows["CARBON_CREDIT_CBAM_COMPLIANCE"]["information_confidence"], "6")
        self.assertEqual(rows["EV_FIRE_RISK_OVERLAY"]["gate_only"], "true")
        self.assertEqual(rows["EV_FIRE_RISK_OVERLAY"]["eps_fcf"], "gate")
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round56_stage_date_rows()}
        fields = {row["field"] for row in round56_price_field_rows()}

        self.assertIn("customer_contract_cancelled", rows["BATTERY_MATERIALS_CAPEX_OVERHEAT"]["stage4c"])
        self.assertIn("ess_contract_value", rows["BATTERY_RECYCLING_ESS_SHIFT"]["stage2"])
        self.assertIn("customs_detention", rows["SOLAR_TARIFF_SUPPLYCHAIN"]["stage4c"])
        self.assertIn("impairment", rows["RENEWABLE_ENERGY_POLICY"]["stage4c"])
        self.assertIn("battery_supplier_disclosure", rows["EV_FIRE_RISK_OVERLAY"]["stage4c"])
        for field in (
            "ess_contract_value",
            "ess_contract_duration_months",
            "ess_contract_volume_gwh",
            "plant_idle_flag",
            "contract_cancelled_flag",
            "lithium_price_change",
            "waste_treatment_volume",
            "hydrogen_capex_amount",
            "customs_detention_flag",
            "uflpa_flag",
            "wind_project_impairment",
            "battery_certification_flag",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND56_PRICE_FIELDS))

    def test_summary_and_markdown_explain_r3_loop2_guardrails(self):
        summary = round56_summary()
        summary_md = render_round56_summary_markdown()
        guardrails = render_round56_green_guardrail_markdown()
        overlays = render_round56_risk_overlay_markdown()
        price_plan = render_round56_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 12)
        self.assertEqual(summary["case_candidate_count"], 13)
        self.assertEqual(summary["structural_success_count"], 1)
        self.assertEqual(summary["success_candidate_count"], 5)
        self.assertEqual(summary["cyclical_success_count"], 1)
        self.assertEqual(summary["stage4b_case_count"], 2)
        self.assertEqual(summary["stage4c_case_count"], 6)
        self.assertEqual(summary["green_possible_count"], 1)
        self.assertEqual(summary["redteam_first_count"], 3)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("R3 Loop 2", summary_md)
        self.assertIn("Do not apply R3 Loop-2 v2.0 weights", guardrails)
        self.assertIn("EV_CAPA_FALSE_GREEN", overlays)
        self.assertIn("lg_energy_tesla_lfp_ess_contract_case", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round56_r3_loop2_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r3_loop2_round56.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round56_r3_loop2_v2.csv",
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
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND56_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round56_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round56_r3_loop2_battery_ev_green", text)


if __name__ == "__main__":
    unittest.main()
