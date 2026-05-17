import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round117_r12_loop6_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round117_r12_loop6_agri_life_misc import (
    ROUND117_CASE_CANDIDATES,
    ROUND117_PRICE_FIELDS,
    ROUND117_SCORE_TARGETS,
    render_round117_green_guardrail_markdown,
    render_round117_price_validation_plan_markdown,
    render_round117_summary_markdown,
    render_round117_unit_economics_cap_markdown,
    round117_case_candidate_rows,
    round117_case_records,
    round117_price_field_rows,
    round117_score_profile_rows,
    round117_stage_date_rows,
    round117_summary,
    target_for,
    write_round117_r12_loop6_reports,
)


class Round117R12Loop6AgriLifeMiscTests(unittest.TestCase):
    def test_round117_targets_cover_r12_loop6_archetypes_and_overlays(self):
        labels = {target.target_id for target in ROUND117_SCORE_TARGETS}

        self.assertEqual(len(labels), 33)
        for label in (
            "SMART_FARM_AGRI_TECH",
            "VERTICAL_FARMING_UNIT_ECONOMICS",
            "AGRI_MACHINERY_PRECISION_CYCLE",
            "AGRI_MACHINERY_DEMAND_CYCLE",
            "AGRI_MACHINERY_SOFTWARE_LOCKIN",
            "RIGHT_TO_REPAIR_REGULATORY_OVERLAY",
            "RIGHT_TO_REPAIR_CONSTRUCTION_EXPANSION",
            "AGRI_INPUT_SEED_CROP_PROTECTION",
            "FERTILIZER_INPUT_COST_CYCLE",
            "FERTILIZER_STRATEGIC_PHOSPHATE_OPTION",
            "AGRI_LIVESTOCK_FOOD_COMMODITY",
            "LIVESTOCK_DISEASE_PRICE_REGULATORY",
            "ANIMAL_HEALTH_BIOSECURITY",
            "AGRI_DISEASE_AI_MONITORING",
            "EDUCATION_SPECIALTY_SERVICES",
            "EDTECH_AI_MONETIZATION_TRADEOFF",
            "EDTECH_AI_DISRUPTION",
            "EDTECH_AI_SEARCH_DISINTERMEDIATION",
            "ONLINE_EDUCATION_OPM_DISTRESS",
            "HOME_CHILD_EDUCATION",
            "HOME_LIVING_APPLIANCE_RENTAL",
            "HOME_APPLIANCE_HARDWARE_CYCLE",
            "SERVICE_KIOSK_SELF_CHECKOUT",
            "SELF_CHECKOUT_LOCAL_REGULATION_OVERLAY",
            "CONSUMER_REGULATED_PRODUCT",
            "NICOTINE_ALTERNATIVE_REGULATED",
            "NICOTINE_POUCH_YOUTH_SAFETY_OVERLAY",
            "CANNABIS_REGULATED_PRODUCT",
            "CANNABIS_PARTIAL_RESCHEDULING_LIMIT",
            "FOOD_INPUT_REGULATED_CYCLE",
            "AGRI_DISEASE_EVENT_OVERLAY",
            "REGULATED_CONSUMER_APPROVAL_OVERLAY",
            "DISCLOSURE_CONFIDENCE_CAP",
        ):
            self.assertIn(label, labels)
        for target in ROUND117_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.EDUCATION_LIFE_AGRI_MISC)
            self.assertFalse(target.production_scoring_changed)

    def test_new_round117_archetypes_exist_and_gates_are_explicit(self):
        for archetype in (
            E2RArchetype.VERTICAL_FARMING_UNIT_ECONOMICS,
            E2RArchetype.AGRI_MACHINERY_DEMAND_CYCLE,
            E2RArchetype.AGRI_MACHINERY_SOFTWARE_LOCKIN,
            E2RArchetype.RIGHT_TO_REPAIR_REGULATORY_OVERLAY,
            E2RArchetype.RIGHT_TO_REPAIR_CONSTRUCTION_EXPANSION,
            E2RArchetype.AGRI_INPUT_SEED_CROP_PROTECTION,
            E2RArchetype.FERTILIZER_INPUT_COST_CYCLE,
            E2RArchetype.FERTILIZER_STRATEGIC_PHOSPHATE_OPTION,
            E2RArchetype.LIVESTOCK_DISEASE_PRICE_REGULATORY,
            E2RArchetype.AGRI_DISEASE_AI_MONITORING,
            E2RArchetype.EDTECH_AI_MONETIZATION_TRADEOFF,
            E2RArchetype.EDTECH_AI_DISRUPTION,
            E2RArchetype.EDTECH_AI_SEARCH_DISINTERMEDIATION,
            E2RArchetype.ONLINE_EDUCATION_OPM_DISTRESS,
            E2RArchetype.HOME_APPLIANCE_HARDWARE_CYCLE,
            E2RArchetype.SELF_CHECKOUT_LOCAL_REGULATION_OVERLAY,
            E2RArchetype.NICOTINE_ALTERNATIVE_REGULATED,
            E2RArchetype.NICOTINE_POUCH_YOUTH_SAFETY_OVERLAY,
            E2RArchetype.CANNABIS_REGULATED_PRODUCT,
            E2RArchetype.CANNABIS_PARTIAL_RESCHEDULING_LIMIT,
        ):
            self.assertIsInstance(archetype.value, str)

        edtech = target_for("EDTECH_AI_DISRUPTION")
        edtech_search = target_for("EDTECH_AI_SEARCH_DISINTERMEDIATION")
        repair = target_for("RIGHT_TO_REPAIR_REGULATORY_OVERLAY")
        construction_repair = target_for("RIGHT_TO_REPAIR_CONSTRUCTION_EXPANSION")
        livestock_reg = target_for("LIVESTOCK_DISEASE_PRICE_REGULATORY")
        checkout_reg = target_for("SELF_CHECKOUT_LOCAL_REGULATION_OVERLAY")
        pouch = target_for("NICOTINE_POUCH_YOUTH_SAFETY_OVERLAY")
        cannabis_partial = target_for("CANNABIS_PARTIAL_RESCHEDULING_LIMIT")
        disease = target_for("AGRI_DISEASE_EVENT_OVERLAY")
        approval = target_for("REGULATED_CONSUMER_APPROVAL_OVERLAY")
        disclosure_cap = target_for("DISCLOSURE_CONFIDENCE_CAP")
        vertical = target_for("VERTICAL_FARMING_UNIT_ECONOMICS")
        assert edtech is not None
        assert edtech_search is not None
        assert repair is not None
        assert construction_repair is not None
        assert livestock_reg is not None
        assert checkout_reg is not None
        assert pouch is not None
        assert cannabis_partial is not None
        assert disease is not None
        assert approval is not None
        assert disclosure_cap is not None
        assert vertical is not None
        for target in (
            edtech,
            edtech_search,
            repair,
            construction_repair,
            livestock_reg,
            checkout_reg,
            pouch,
            cannabis_partial,
            disease,
            approval,
        ):
            self.assertTrue(target.gate_only)
            self.assertEqual(target.posture, Round10ThemePosture.REDTEAM_FIRST)
            self.assertEqual(target.score_weight.as_csv_dict()["eps_fcf"], "gate")
        self.assertFalse(disclosure_cap.gate_only)
        self.assertEqual(disclosure_cap.score_weight.as_csv_dict()["eps_fcf"], "cap")
        self.assertFalse(vertical.gate_only)
        self.assertIn("premium_pricing_failure", vertical.stage4c_conditions)

    def test_score_profile_rows_match_round117_weight_table(self):
        rows = {row["target_id"]: row for row in round117_score_profile_rows()}

        self.assertEqual(rows["SMART_FARM_AGRI_TECH"]["eps_fcf"], "17")
        self.assertEqual(rows["VERTICAL_FARMING_UNIT_ECONOMICS"]["eps_fcf"], "8")
        self.assertEqual(rows["AGRI_MACHINERY_PRECISION_CYCLE"]["eps_fcf"], "16")
        self.assertEqual(rows["AGRI_MACHINERY_DEMAND_CYCLE"]["eps_fcf"], "14")
        self.assertEqual(rows["AGRI_MACHINERY_SOFTWARE_LOCKIN"]["structural_visibility"], "14")
        self.assertEqual(rows["RIGHT_TO_REPAIR_REGULATORY_OVERLAY"]["gate_only"], "true")
        self.assertEqual(rows["RIGHT_TO_REPAIR_CONSTRUCTION_EXPANSION"]["gate_only"], "true")
        self.assertEqual(rows["AGRI_INPUT_SEED_CROP_PROTECTION"]["structural_visibility"], "16")
        self.assertEqual(rows["FERTILIZER_INPUT_COST_CYCLE"]["bottleneck_pricing"], "14")
        self.assertEqual(rows["FERTILIZER_STRATEGIC_PHOSPHATE_OPTION"]["eps_fcf"], "16")
        self.assertEqual(rows["FERTILIZER_STRATEGIC_PHOSPHATE_OPTION"]["structural_visibility"], "12")
        self.assertEqual(rows["AGRI_LIVESTOCK_FOOD_COMMODITY"]["structural_visibility"], "8")
        self.assertEqual(rows["LIVESTOCK_DISEASE_PRICE_REGULATORY"]["gate_only"], "true")
        self.assertEqual(rows["ANIMAL_HEALTH_BIOSECURITY"]["eps_fcf"], "18")
        self.assertEqual(rows["ANIMAL_HEALTH_BIOSECURITY"]["structural_visibility"], "16")
        self.assertEqual(rows["AGRI_DISEASE_AI_MONITORING"]["eps_fcf"], "14")
        self.assertEqual(rows["EDUCATION_SPECIALTY_SERVICES"]["valuation"], "10")
        self.assertEqual(rows["EDTECH_AI_MONETIZATION_TRADEOFF"]["structural_visibility"], "15")
        self.assertEqual(rows["EDTECH_AI_SEARCH_DISINTERMEDIATION"]["gate_only"], "true")
        self.assertEqual(rows["ONLINE_EDUCATION_OPM_DISTRESS"]["eps_fcf"], "10")
        self.assertEqual(rows["HOME_APPLIANCE_HARDWARE_CYCLE"]["eps_fcf"], "14")
        self.assertEqual(rows["SERVICE_KIOSK_SELF_CHECKOUT"]["eps_fcf"], "15")
        self.assertEqual(rows["SELF_CHECKOUT_LOCAL_REGULATION_OVERLAY"]["gate_only"], "true")
        self.assertEqual(rows["CONSUMER_REGULATED_PRODUCT"]["structural_visibility"], "15")
        self.assertEqual(rows["NICOTINE_ALTERNATIVE_REGULATED"]["eps_fcf"], "16")
        self.assertEqual(rows["NICOTINE_POUCH_YOUTH_SAFETY_OVERLAY"]["gate_only"], "true")
        self.assertEqual(rows["CANNABIS_REGULATED_PRODUCT"]["valuation"], "8")
        self.assertEqual(rows["CANNABIS_PARTIAL_RESCHEDULING_LIMIT"]["gate_only"], "true")
        self.assertEqual(rows["EDTECH_AI_DISRUPTION"]["gate_only"], "true")
        self.assertEqual(rows["DISCLOSURE_CONFIDENCE_CAP"]["eps_fcf"], "cap")
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_required_round117_cases_are_present_with_stage_dates(self):
        rows = {row["case_id"]: row for row in round117_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND117_CASE_CANDIDATES))
        self.assertEqual(rows["john_deere_autonomous_agri_ces_case"]["stage1_date"], "2025-01-06")
        self.assertEqual(rows["deere_farm_equipment_demand_slowdown_case"]["target_id"], "AGRI_MACHINERY_DEMAND_CYCLE")
        self.assertEqual(rows["deere_farm_equipment_demand_slowdown_case"]["stage4c_date"], "2025-02-13")
        self.assertEqual(rows["deere_right_to_repair_settlement_case"]["target_id"], "RIGHT_TO_REPAIR_REGULATORY_OVERLAY")
        self.assertEqual(rows["deere_construction_right_to_repair_case"]["target_id"], "RIGHT_TO_REPAIR_CONSTRUCTION_EXPANSION")
        self.assertEqual(rows["deere_construction_right_to_repair_case"]["stage1_date"], "2026-05-15")
        self.assertEqual(rows["cnh_weak_farm_equipment_demand_case"]["target_id"], "AGRI_MACHINERY_DEMAND_CYCLE")
        self.assertEqual(rows["cnh_weak_farm_equipment_demand_case"]["stage4c_date"], "2025-11-07")
        self.assertEqual(rows["bayer_soy_seed_license_crop_science_case"]["target_id"], "AGRI_INPUT_SEED_CROP_PROTECTION")
        self.assertEqual(rows["bayer_soy_seed_license_crop_science_case"]["stage2_date"], "2026-05-12")
        self.assertEqual(rows["nutrien_potash_phosphate_option_case"]["target_id"], "FERTILIZER_STRATEGIC_PHOSPHATE_OPTION")
        self.assertEqual(rows["nutrien_potash_phosphate_option_case"]["stage2_date"], "2025-11-06")
        self.assertEqual(rows["zoetis_bird_flu_vaccine_conditional_case"]["stage2_date"], "2025-02-14")
        self.assertEqual(rows["calmaine_egg_price_regulatory_case"]["target_id"], "LIVESTOCK_DISEASE_PRICE_REGULATORY")
        self.assertEqual(rows["calmaine_egg_price_regulatory_case"]["case_type"], "cyclical_success")
        self.assertEqual(rows["bowery_vertical_farming_shutdown_case"]["target_id"], "VERTICAL_FARMING_UNIT_ECONOMICS")
        self.assertEqual(rows["bowery_vertical_farming_shutdown_case"]["stage4c_date"], "2024-11-05")
        self.assertEqual(rows["appharvest_chapter11_case"]["stage4c_date"], "2023-07-24")
        self.assertEqual(rows["duolingo_ai_strategy_bookings_miss_case"]["target_id"], "EDTECH_AI_MONETIZATION_TRADEOFF")
        self.assertEqual(rows["duolingo_ai_strategy_bookings_miss_case"]["stage4c_date"], "2026-02-26")
        self.assertEqual(rows["chegg_ai_disruption_case"]["target_id"], "EDTECH_AI_DISRUPTION")
        self.assertEqual(rows["chegg_ai_disruption_case"]["stage4c_date"], "2023-05-02")
        self.assertEqual(rows["chegg_ai_search_disintermediation_case"]["target_id"], "EDTECH_AI_SEARCH_DISINTERMEDIATION")
        self.assertEqual(rows["chegg_ai_search_disintermediation_case"]["stage4c_date"], "2025-05-01")
        self.assertEqual(rows["2u_chapter11_case"]["target_id"], "ONLINE_EDUCATION_OPM_DISTRESS")
        self.assertEqual(rows["2u_chapter11_case"]["stage4c_date"], "2024-07-25")
        self.assertEqual(rows["whirlpool_dividend_suspension_case"]["target_id"], "HOME_APPLIANCE_HARDWARE_CYCLE")
        self.assertEqual(rows["whirlpool_dividend_suspension_case"]["stage4c_date"], "2026-05-07")
        self.assertEqual(rows["santa_ana_self_checkout_regulation_case"]["target_id"], "SELF_CHECKOUT_LOCAL_REGULATION_OVERLAY")
        self.assertEqual(rows["juul_fda_approval_case"]["stage2_date"], "2025-07-17")
        self.assertEqual(rows["fda_vape_enforcement_easing_case"]["target_id"], "NICOTINE_ALTERNATIVE_REGULATED")
        self.assertEqual(rows["who_nicotine_pouch_youth_warning_case"]["target_id"], "NICOTINE_POUCH_YOUTH_SAFETY_OVERLAY")
        self.assertEqual(rows["who_nicotine_pouch_youth_warning_case"]["case_type"], "failed_rerating")
        self.assertEqual(rows["cannabis_schedule3_limited_case"]["target_id"], "CANNABIS_PARTIAL_RESCHEDULING_LIMIT")
        self.assertEqual(rows["cannabis_schedule3_limited_case"]["stage4b_date"], "2026-05-12")

    def test_case_records_validate_and_keep_round117_guardrails(self):
        records = round117_case_records()

        self.assertEqual(len(records), len(ROUND117_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.price_validation.price_validation_status, "needs_price_backfill")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("life_essential_policy_or_disease_label_is_not_green_evidence_alone", record.green_guardrails)
            self.assertIn("repeat_contract_repeat_revenue_unit_economics_or_regulatory_scope_required", record.green_guardrails)
            self.assertIn("do_not_invent_unit_economics_orders_cac_churn_regulatory_scope_or_stage_prices", record.green_guardrails)
        by_id = {record.case_id: record for record in records}
        self.assertEqual(by_id["calmaine_egg_price_regulatory_case"].rerating_result, "cyclical_rerating")
        self.assertEqual(by_id["target_self_checkout_limit_case"].rerating_result, "no_rerating")
        self.assertEqual(by_id["chegg_ai_disruption_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["chegg_ai_search_disintermediation_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["fda_vape_enforcement_easing_case"].score_price_alignment, "price_moved_without_evidence")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        stage_rows = {row["target_id"]: row for row in round117_stage_date_rows()}
        price_fields = {row["field"] for row in round117_price_field_rows()}

        self.assertIn("shutdown", stage_rows["VERTICAL_FARMING_UNIT_ECONOMICS"]["stage4c"])
        self.assertIn("dealer_inventory_increase", stage_rows["AGRI_MACHINERY_DEMAND_CYCLE"]["stage4c"])
        self.assertIn("right_to_repair_lawsuit", stage_rows["AGRI_MACHINERY_SOFTWARE_LOCKIN"]["stage4c"])
        self.assertIn("ftc_lawsuit", stage_rows["RIGHT_TO_REPAIR_REGULATORY_OVERLAY"]["stage4c"])
        self.assertIn("class_action_expansion_risk", stage_rows["RIGHT_TO_REPAIR_CONSTRUCTION_EXPANSION"]["stage4c"])
        self.assertIn("crop_protection_litigation", stage_rows["AGRI_INPUT_SEED_CROP_PROTECTION"]["stage4c"])
        self.assertIn("demand_deferral", stage_rows["FERTILIZER_INPUT_COST_CYCLE"]["stage4c"])
        self.assertIn("asset_sale_uncertainty", stage_rows["FERTILIZER_STRATEGIC_PHOSPHATE_OPTION"]["stage4c"])
        self.assertIn("price_fixing_investigation", stage_rows["AGRI_LIVESTOCK_FOOD_COMMODITY"]["stage4c"])
        self.assertIn("doj_investigation", stage_rows["LIVESTOCK_DISEASE_PRICE_REGULATORY"]["stage4c"])
        self.assertIn("data_quality_failure", stage_rows["AGRI_DISEASE_AI_MONITORING"]["stage4c"])
        self.assertIn("monetization_retreat", stage_rows["EDTECH_AI_MONETIZATION_TRADEOFF"]["stage4c"])
        self.assertIn("bookings_miss", stage_rows["EDTECH_AI_DISRUPTION"]["stage4c"])
        self.assertIn("paid_conversion_decline", stage_rows["EDTECH_AI_SEARCH_DISINTERMEDIATION"]["stage4c"])
        self.assertIn("guidance_cut", stage_rows["HOME_APPLIANCE_HARDWARE_CYCLE"]["stage4c"])
        self.assertIn("staff_required_per_kiosk", stage_rows["SELF_CHECKOUT_LOCAL_REGULATION_OVERLAY"]["stage4c"])
        self.assertIn("sales_authorization", stage_rows["CONSUMER_REGULATED_PRODUCT"]["stage2"])
        self.assertIn("advertising_ban", stage_rows["NICOTINE_POUCH_YOUTH_SAFETY_OVERLAY"]["stage4c"])
        self.assertIn("state_federal_conflict", stage_rows["CANNABIS_REGULATED_PRODUCT"]["stage4c"])
        self.assertIn("medical_cannabis_only", stage_rows["CANNABIS_PARTIAL_RESCHEDULING_LIMIT"]["stage4c"])
        self.assertIn("unit_economics_missing", stage_rows["DISCLOSURE_CONFIDENCE_CAP"]["stage4c"])
        for field in (
            "dealer_inventory",
            "dealer_inventory_increase_flag",
            "crop_price",
            "crop_price_change",
            "right_to_repair_flag",
            "repair_settlement_amount",
            "repair_monopoly_allegation_flag",
            "construction_equipment_repair_lawsuit_flag",
            "independent_repair_access_flag",
            "dealer_network_dependency",
            "ftc_lawsuit_flag",
            "soy_seed_license_flag",
            "seed_licensing_revenue",
            "seed_revenue_growth",
            "licensing_revenue",
            "farmer_roi_metric",
            "crop_science_ebitda_growth",
            "roundup_litigation_flag",
            "fertilizer_volume",
            "fertilizer_price_change",
            "phosphate_revenue",
            "phosphate_strategic_mineral_flag",
            "phosphate_asset_review_flag",
            "farmer_margin_indicator",
            "supply_disruption_flag",
            "potash_sales_forecast",
            "input_cost_spike_flag",
            "premium_pricing_success_flag",
            "shutdown_flag",
            "debt_burden_flag",
            "conditional_license_flag",
            "agri_disease_ai_monitoring_flag",
            "agri_ai_monitoring_contract",
            "farm_deployment_contract_flag",
            "farm_data_privacy_flag",
            "dataset_quality_flag",
            "farm_privacy_risk_flag",
            "price_fixing_investigation_flag",
            "bookings_growth",
            "paid_conversion_rate",
            "ai_monetization_tradeoff_flag",
            "ai_feature_cost",
            "monetization_retreat_flag",
            "ai_search_disintermediation_flag",
            "traffic_decline_flag",
            "subscriber_decline_flag",
            "opm_model_flag",
            "partner_concentration_flag",
            "self_checkout_limit_flag",
            "staffed_lane_requirement_flag",
            "staff_required_per_kiosk_flag",
            "employee_workload_flag",
            "loss_prevention_effect",
            "hardware_guidance_cut_flag",
            "fcf_guidance_cut_flag",
            "fda_enforcement_easing_flag",
            "dea_registration_required_flag",
            "state_federal_conflict_flag",
            "sales_channel",
            "medical_only_scope",
            "recreational_benefit_limited_flag",
            "sales_channel_authorized_flag",
            "nicotine_pouch_flag",
            "age_verification_flag",
            "flavor_restriction_flag",
            "advertising_ban_flag",
            "who_warning_flag",
            "contract_value_missing_flag",
            "regulatory_scope_missing_flag",
            "unit_economics_missing_flag",
            "parser_confidence",
            "score_price_alignment",
            "review_notes",
        ):
            self.assertIn(field, price_fields)
        self.assertEqual(len(price_fields), len(ROUND117_PRICE_FIELDS))

    def test_summary_and_markdown_explain_r12_loop6_guardrails(self):
        summary = round117_summary()
        summary_md = render_round117_summary_markdown()
        guardrails = render_round117_green_guardrail_markdown()
        caps = render_round117_unit_economics_cap_markdown()
        price_plan = render_round117_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 33)
        self.assertEqual(summary["case_candidate_count"], 23)
        self.assertEqual(summary["success_candidate_count"], 5)
        self.assertEqual(summary["cyclical_success_count"], 2)
        self.assertEqual(summary["event_premium_count"], 2)
        self.assertEqual(summary["failed_rerating_count"], 5)
        self.assertEqual(summary["stage4b_case_count"], 3)
        self.assertEqual(summary["stage4c_case_count"], 9)
        self.assertEqual(summary["green_possible_count"], 0)
        self.assertEqual(summary["watch_yellow_first_count"], 18)
        self.assertEqual(summary["redteam_first_count"], 15)
        self.assertEqual(summary["gate_only_target_count"], 10)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("Round-117", summary_md)
        self.assertIn("Do not apply these R12 Loop-6 v6 weights", guardrails)
        self.assertIn("right-to-repair", caps)
        self.assertIn("vertical_farming_4c", price_plan)
        self.assertIn("agri_machinery_demand_4c", price_plan)
        self.assertIn("fertilizer_cycle_with_input_risk", price_plan)
        self.assertIn("right_to_repair_expansion_4c", price_plan)
        self.assertIn("edtech_search_disintermediation_4c", price_plan)
        self.assertIn("cannabis_rescheduling_limited_stage2", price_plan)
        self.assertIn("nicotine_alternative_regulatory_watch", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round117_r12_loop6_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r12_loop6_round117.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round117_r12_loop6_v6.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["stage_date_plan"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["unit_economics_caps"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertTrue(paths["price_fields"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND117_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round117_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round117_r12_loop6_agri_life_misc", text)


if __name__ == "__main__":
    unittest.main()
