import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round129_r10_loop7_report import build_parser
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round129_r10_loop7_construction_real_estate_materials import (
    ROUND129_BASE_SCORE_AXES,
    ROUND129_CASE_CANDIDATES,
    ROUND129_PRICE_FIELDS,
    ROUND129_SCORE_TARGETS,
    render_round129_green_guardrail_markdown,
    render_round129_price_validation_plan_markdown,
    render_round129_risk_overlay_markdown,
    render_round129_summary_markdown,
    round129_base_score_axis_rows,
    round129_case_candidate_rows,
    round129_case_records,
    round129_price_field_rows,
    round129_score_profile_rows,
    round129_stage_date_rows,
    round129_summary,
    target_for,
    write_round129_r10_reports,
)


class Round129R10Loop7ConstructionRealEstateMaterialsTests(unittest.TestCase):
    def test_round129_targets_cover_r10_loop7_archetypes(self):
        labels = {target.target_id for target in ROUND129_SCORE_TARGETS}

        self.assertEqual(len(labels), 28)
        for label in (
            "CONSTRUCTION_REAL_ESTATE_CREDIT",
            "PF_RESTRUCTURING_RELIEF",
            "PF_SYNDICATED_LOAN_SOFT_LANDING",
            "RESIDENTIAL_HOUSING_CYCLE",
            "REIT_DEVELOPMENT_TRUST",
            "COMMERCIAL_REAL_ESTATE_CREDIT",
            "DATA_CENTER_REIT_INFRASTRUCTURE",
            "DATA_CENTER_REIT_IPO_NO_ASSET",
            "DATA_CENTER_SPONSOR_PREMIUM_PIPELINE",
            "AI_DATA_CENTER_POWER_CAMPUS",
            "AI_DATA_CENTER_NO_REVENUE_NO_TENANT",
            "DATA_CENTER_POWER_WATER_PERMITTING",
            "DATA_CENTER_LOCAL_MORATORIUM_OVERLAY",
            "DATA_CENTER_WATER_RIGHTS_REFERENDUM",
            "DATA_CENTER_RATEPAYER_UTILITY_COST_OVERLAY",
            "DATA_CENTER_CAPEX_AFFO_DILUTION",
            "COLD_CHAIN_REIT_LOGISTICS",
            "COLD_CHAIN_DEBT_OCCUPANCY_RISK",
            "BUILDING_MATERIALS_PRICE_COST",
            "BUILDING_MATERIALS_VOLUME_FAILURE",
            "LOW_CARBON_CEMENT_PREMIUM",
            "BUILDING_PRODUCTS_MNA_SHIFT",
            "PRECAST_WALLING_BUILDING_SOLUTIONS",
            "INFRA_RECONSTRUCTION_POLICY",
            "POLICY_LOCAL_REAL_ESTATE_THEME",
            "PF_CREDIT_REDTEAM_OVERLAY",
            "REIT_AFFO_INTEGRITY_OVERLAY",
            "DISCLOSURE_CONFIDENCE_CAP",
        ):
            self.assertIn(label, labels)
        for target in ROUND129_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS)
            self.assertFalse(target.production_scoring_changed)

    def test_data_center_cold_chain_and_materials_are_green_possible_but_guardrailed(self):
        dc_reit = target_for("DATA_CENTER_REIT_INFRASTRUCTURE")
        dc_ipo = target_for("DATA_CENTER_REIT_IPO_NO_ASSET")
        sponsor = target_for("DATA_CENTER_SPONSOR_PREMIUM_PIPELINE")
        cold_chain = target_for("COLD_CHAIN_REIT_LOGISTICS")
        materials = target_for("BUILDING_MATERIALS_PRICE_COST")
        low_carbon = target_for("LOW_CARBON_CEMENT_PREMIUM")
        building_products = target_for("BUILDING_PRODUCTS_MNA_SHIFT")
        precast = target_for("PRECAST_WALLING_BUILDING_SOLUTIONS")

        assert dc_reit is not None
        assert dc_ipo is not None
        assert sponsor is not None
        assert cold_chain is not None
        assert materials is not None
        assert low_carbon is not None
        assert building_products is not None
        assert precast is not None
        self.assertEqual(dc_reit.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("power_water_secured", dc_reit.green_conditions)
        self.assertIn("no_acquired_assets", dc_reit.stage4c_conditions)
        self.assertEqual(dc_ipo.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("no_acquired_assets", dc_ipo.stage4c_conditions)
        self.assertIn("asset_acquired_flag", dc_ipo.green_conditions)
        self.assertEqual(sponsor.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("sponsor_premium", sponsor.red_flags)
        self.assertEqual(cold_chain.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("dividend_coverage", cold_chain.green_conditions)
        self.assertIn("net_loss", cold_chain.red_flags)
        self.assertEqual(materials.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("volume_recovery", materials.green_conditions)
        self.assertIn("volume_decline", materials.red_flags)
        self.assertEqual(low_carbon.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("product_presold_flag", low_carbon.green_conditions)
        self.assertIn("subsidy_durability_risk", low_carbon.red_flags)
        self.assertEqual(building_products.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("earnings_accretive_guidance_flag", building_products.green_conditions)
        self.assertIn("integration_risk", building_products.red_flags)
        self.assertEqual(precast.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("earnings_accretive_guidance_flag", precast.green_conditions)
        self.assertIn("deal_price_unknown", precast.red_flags)

    def test_pf_affo_power_water_and_ai_theme_overlays_are_gate_only(self):
        pf = target_for("PF_CREDIT_REDTEAM_OVERLAY")
        affo = target_for("REIT_AFFO_INTEGRITY_OVERLAY")
        power_water = target_for("DATA_CENTER_POWER_WATER_PERMITTING")
        local_moratorium = target_for("DATA_CENTER_LOCAL_MORATORIUM_OVERLAY")
        water_rights = target_for("DATA_CENTER_WATER_RIGHTS_REFERENDUM")
        ratepayer = target_for("DATA_CENTER_RATEPAYER_UTILITY_COST_OVERLAY")
        capex_affo = target_for("DATA_CENTER_CAPEX_AFFO_DILUTION")
        cold_debt = target_for("COLD_CHAIN_DEBT_OCCUPANCY_RISK")
        no_revenue = target_for("AI_DATA_CENTER_NO_REVENUE_NO_TENANT")
        disclosure_cap = target_for("DISCLOSURE_CONFIDENCE_CAP")

        for target in (pf, affo, power_water, local_moratorium, water_rights, ratepayer, capex_affo, cold_debt, no_revenue):
            assert target is not None
            self.assertTrue(target.gate_only)
            self.assertEqual(target.score_weight.eps_fcf, "gate")
            self.assertEqual(target.posture, Round10ThemePosture.REDTEAM_FIRST)
        assert power_water is not None
        self.assertIn("project_withdrawal", power_water.stage4c_conditions)
        assert affo is not None
        self.assertIn("maintenance_capex_misclassification", affo.stage4c_conditions)
        assert capex_affo is not None
        self.assertIn("per_share_affo_slowdown", capex_affo.stage4c_conditions)
        assert cold_debt is not None
        self.assertIn("debt_burden", cold_debt.stage4c_conditions)
        assert no_revenue is not None
        self.assertIn("no_revenue", no_revenue.stage4c_conditions)
        assert local_moratorium is not None
        self.assertIn("moratorium", local_moratorium.stage4c_conditions)
        assert water_rights is not None
        self.assertIn("water_rights_delay", water_rights.stage4c_conditions)
        assert ratepayer is not None
        self.assertIn("ratepayer_cost_risk", ratepayer.stage4c_conditions)
        assert disclosure_cap is not None
        self.assertFalse(disclosure_cap.gate_only)
        self.assertEqual(disclosure_cap.score_weight.eps_fcf, "cap")
        self.assertEqual(disclosure_cap.score_weight.information_confidence, "+")
        self.assertIn("disclosure_confidence_low", disclosure_cap.stage4c_conditions)

    def test_required_round129_cases_are_present_with_stage_dates(self):
        rows = {row["case_id"]: row for row in round129_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND129_CASE_CANDIDATES))
        self.assertEqual(rows["korea_pf_delinquency_restructuring_case"]["target_id"], "PF_CREDIT_REDTEAM_OVERLAY")
        self.assertEqual(rows["korea_pf_delinquency_restructuring_case"]["stage4c_date"], "2024-05-13")
        self.assertEqual(rows["korea_builder_support_relief_case"]["target_id"], "PF_RESTRUCTURING_RELIEF")
        self.assertEqual(rows["korea_builder_support_relief_case"]["stage4b_date"], "2024-03-27")
        self.assertEqual(rows["korea_pf_syndicated_loan_soft_landing_case"]["target_id"], "PF_SYNDICATED_LOAN_SOFT_LANDING")
        self.assertEqual(rows["korea_pf_syndicated_loan_soft_landing_case"]["stage2_date"], "2024-05-13")
        self.assertEqual(rows["blackstone_mortgage_trust_dividend_cut_case"]["stage4c_date"], "2024-07-24")
        self.assertEqual(rows["equinix_affo_integrity_short_case"]["target_id"], "REIT_AFFO_INTEGRITY_OVERLAY")
        self.assertEqual(rows["equinix_affo_integrity_short_case"]["stage4c_date"], "2024-03-20")
        self.assertEqual(rows["equinix_ai_capex_burden_case"]["target_id"], "DATA_CENTER_CAPEX_AFFO_DILUTION")
        self.assertEqual(rows["equinix_ai_capex_burden_case"]["stage4b_date"], "2025-06-26")
        self.assertEqual(rows["equinix_ai_revenue_guidance_case"]["target_id"], "DATA_CENTER_REIT_INFRASTRUCTURE")
        self.assertEqual(rows["equinix_ai_revenue_guidance_case"]["stage2_date"], "2026-02-11")
        self.assertEqual(rows["blackstone_data_center_reit_ipo_case"]["target_id"], "DATA_CENTER_REIT_IPO_NO_ASSET")
        self.assertEqual(rows["blackstone_data_center_reit_ipo_case"]["stage4b_date"], "2026-05-13")
        self.assertEqual(rows["fermi_ai_data_center_no_revenue_ipo_case"]["target_id"], "AI_DATA_CENTER_NO_REVENUE_NO_TENANT")
        self.assertEqual(rows["fermi_ai_data_center_no_revenue_ipo_case"]["stage4b_date"], "2025-10-01")
        self.assertEqual(rows["fermi_no_tenant_net_loss_case"]["target_id"], "AI_DATA_CENTER_NO_REVENUE_NO_TENANT")
        self.assertEqual(rows["fermi_no_tenant_net_loss_case"]["stage4c_date"], "2026-03-30")
        self.assertEqual(rows["perth_datacenter_withdrawal_case"]["stage4c_date"], "2026-05-15")
        self.assertEqual(rows["utah_stratos_datacenter_backlash_case"]["target_id"], "DATA_CENTER_WATER_RIGHTS_REFERENDUM")
        self.assertEqual(rows["utah_stratos_datacenter_backlash_case"]["stage4b_date"], "2026-05-13")
        self.assertEqual(rows["seattle_datacenter_moratorium_case"]["target_id"], "DATA_CENTER_LOCAL_MORATORIUM_OVERLAY")
        self.assertEqual(rows["indianapolis_datacenter_moratorium_case"]["stage4b_date"], "2026-05-15")
        self.assertEqual(rows["lineage_cold_storage_ipo_case"]["stage2_date"], "2024-07-25")
        self.assertEqual(rows["lineage_cold_storage_debt_occupancy_case"]["target_id"], "COLD_CHAIN_DEBT_OCCUPANCY_RISK")
        self.assertEqual(rows["lineage_cold_storage_debt_occupancy_case"]["stage4c_date"], "2025-10-01")
        self.assertEqual(rows["heidelberg_materials_price_cost_case"]["target_id"], "BUILDING_MATERIALS_PRICE_COST")
        self.assertEqual(rows["heidelberg_evozero_low_carbon_cement_case"]["target_id"], "LOW_CARBON_CEMENT_PREMIUM")
        self.assertEqual(rows["heidelberg_evozero_low_carbon_cement_case"]["stage2_date"], "2025-06-18")
        self.assertEqual(rows["cemex_demand_slowdown_costcut_case"]["target_id"], "BUILDING_MATERIALS_VOLUME_FAILURE")
        self.assertEqual(rows["cemex_price_cost_restructuring_case"]["target_id"], "BUILDING_MATERIALS_PRICE_COST")
        self.assertEqual(rows["cemex_price_cost_restructuring_case"]["stage2_date"], "2025-10-27")
        self.assertEqual(rows["holcim_xella_building_products_mna_case"]["target_id"], "BUILDING_PRODUCTS_MNA_SHIFT")
        self.assertEqual(rows["holcim_xella_building_products_mna_case"]["stage2_date"], "2025-10-20")
        self.assertEqual(rows["holcim_alkern_precast_case"]["target_id"], "PRECAST_WALLING_BUILDING_SOLUTIONS")
        self.assertEqual(rows["holcim_alkern_precast_case"]["stage2_date"], "2026-01-06")
        self.assertEqual(rows["sejong_policy_theme_case"]["target_id"], "POLICY_LOCAL_REAL_ESTATE_THEME")

    def test_case_records_validate_and_keep_round129_guardrails(self):
        records = round129_case_records()

        self.assertEqual(len(records), len(ROUND129_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("pf_support_or_rate_cut_is_not_green_evidence_alone", record.green_guardrails)
            self.assertIn("backlog_dividend_ai_datacenter_or_reconstruction_headline_is_not_green_evidence_alone", record.green_guardrails)
            self.assertIn("cashflow_occupancy_affo_tenant_power_water_volume_and_funding_cost_required_for_green", record.green_guardrails)
        by_id = {record.case_id: record for record in records}
        self.assertEqual(by_id["korea_builder_support_relief_case"].rerating_result, "credit_relief_rally")
        self.assertEqual(by_id["equinix_affo_integrity_short_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["heidelberg_materials_price_cost_case"].score_price_alignment, "aligned")
        self.assertEqual(by_id["cemex_demand_slowdown_costcut_case"].score_price_alignment, "false_positive_score")
        self.assertEqual(by_id["korea_pf_syndicated_loan_soft_landing_case"].rerating_result, "event_premium")
        self.assertEqual(by_id["heidelberg_evozero_low_carbon_cement_case"].price_validation.price_validation_status, "needs_price_backfill")

    def test_score_profile_rows_match_round129_weight_table(self):
        rows = {row["target_id"]: row for row in round129_score_profile_rows()}

        self.assertEqual(rows["CONSTRUCTION_REAL_ESTATE_CREDIT"]["eps_fcf"], "12")
        self.assertEqual(rows["PF_RESTRUCTURING_RELIEF"]["structural_visibility"], "8")
        self.assertEqual(rows["PF_SYNDICATED_LOAN_SOFT_LANDING"]["structural_visibility"], "9")
        self.assertEqual(rows["DATA_CENTER_REIT_INFRASTRUCTURE"]["structural_visibility"], "22")
        self.assertEqual(rows["DATA_CENTER_REIT_IPO_NO_ASSET"]["eps_fcf"], "11")
        self.assertEqual(rows["DATA_CENTER_SPONSOR_PREMIUM_PIPELINE"]["structural_visibility"], "13")
        self.assertEqual(rows["AI_DATA_CENTER_POWER_CAMPUS"]["bottleneck_pricing"], "18")
        self.assertEqual(rows["AI_DATA_CENTER_NO_REVENUE_NO_TENANT"]["gate_only"], "true")
        self.assertEqual(rows["DATA_CENTER_LOCAL_MORATORIUM_OVERLAY"]["eps_fcf"], "gate")
        self.assertEqual(rows["DATA_CENTER_WATER_RIGHTS_REFERENDUM"]["eps_fcf"], "gate")
        self.assertEqual(rows["DATA_CENTER_RATEPAYER_UTILITY_COST_OVERLAY"]["gate_only"], "true")
        self.assertEqual(rows["DATA_CENTER_CAPEX_AFFO_DILUTION"]["gate_only"], "true")
        self.assertEqual(rows["COLD_CHAIN_REIT_LOGISTICS"]["valuation"], "10")
        self.assertEqual(rows["COLD_CHAIN_DEBT_OCCUPANCY_RISK"]["eps_fcf"], "gate")
        self.assertEqual(rows["BUILDING_MATERIALS_PRICE_COST"]["eps_fcf"], "18")
        self.assertEqual(rows["BUILDING_MATERIALS_VOLUME_FAILURE"]["structural_visibility"], "9")
        self.assertEqual(rows["LOW_CARBON_CEMENT_PREMIUM"]["eps_fcf"], "16")
        self.assertEqual(rows["BUILDING_PRODUCTS_MNA_SHIFT"]["structural_visibility"], "16")
        self.assertEqual(rows["PRECAST_WALLING_BUILDING_SOLUTIONS"]["structural_visibility"], "16")
        self.assertEqual(rows["DATA_CENTER_POWER_WATER_PERMITTING"]["eps_fcf"], "gate")
        self.assertEqual(rows["REIT_AFFO_INTEGRITY_OVERLAY"]["gate_only"], "true")
        self.assertEqual(rows["DISCLOSURE_CONFIDENCE_CAP"]["information_confidence"], "+")
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_base_score_axes_match_round129_v7_weight_table(self):
        rows = {row["axis_id"]: row for row in round129_base_score_axis_rows()}

        self.assertEqual(len(rows), 7)
        self.assertEqual(len(ROUND129_BASE_SCORE_AXES), 7)
        self.assertEqual(rows["eps_fcf_affo_noi_conversion"]["score_weight"], "24")
        self.assertIn("affo_per_share_growth", rows["eps_fcf_affo_noi_conversion"]["stage3_evidence"])
        self.assertIn("dividend_cut", rows["eps_fcf_affo_noi_conversion"]["hard_redteam_flags"])
        self.assertEqual(rows["asset_tenant_contract_pf_visibility"]["score_weight"], "20")
        self.assertIn("binding_lease_flag", rows["asset_tenant_contract_pf_visibility"]["stage2_evidence"])
        self.assertIn("no_acquired_assets", rows["asset_tenant_contract_pf_visibility"]["hard_redteam_flags"])
        self.assertEqual(rows["power_water_permitting_local_acceptance"]["score_weight"], "16")
        self.assertIn("water_rights_delay", rows["power_water_permitting_local_acceptance"]["hard_redteam_flags"])
        self.assertEqual(rows["cost_ratio_price_volume_mna_synergy"]["score_weight"], "14")
        self.assertIn("volume_and_price_aligned", rows["cost_ratio_price_volume_mna_synergy"]["stage3_evidence"])
        self.assertEqual(rows["market_mispricing_rerating_gap"]["score_weight"], "8")
        self.assertEqual(rows["valuation_room_4b_margin"]["score_weight"], "6")
        self.assertEqual(rows["leverage_capex_affo_integrity_disclosure"]["score_weight"], "12")
        self.assertIn("maintenance_capex_misclassification", rows["leverage_capex_affo_integrity_disclosure"]["hard_redteam_flags"])
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round129_stage_date_rows()}
        fields = {row["field"] for row in round129_price_field_rows()}

        self.assertIn("refinancing_success", rows["CONSTRUCTION_REAL_ESTATE_CREDIT"]["stage2"])
        self.assertIn("binding_tenant_lease", rows["DATA_CENTER_REIT_INFRASTRUCTURE"]["stage2"])
        self.assertIn("asset_acquired_flag", rows["DATA_CENTER_REIT_IPO_NO_ASSET"]["stage2"])
        self.assertIn("asset_acquired_flag", rows["DATA_CENTER_SPONSOR_PREMIUM_PIPELINE"]["stage2"])
        self.assertIn("no_revenue", rows["AI_DATA_CENTER_NO_REVENUE_NO_TENANT"]["stage4c"])
        self.assertIn("project_withdrawal", rows["DATA_CENTER_POWER_WATER_PERMITTING"]["stage4c"])
        self.assertIn("moratorium", rows["DATA_CENTER_LOCAL_MORATORIUM_OVERLAY"]["stage4c"])
        self.assertIn("water_rights_delay", rows["DATA_CENTER_WATER_RIGHTS_REFERENDUM"]["stage4c"])
        self.assertIn("ratepayer_cost_risk", rows["DATA_CENTER_RATEPAYER_UTILITY_COST_OVERLAY"]["stage4c"])
        self.assertIn("per_share_affo_slowdown", rows["DATA_CENTER_CAPEX_AFFO_DILUTION"]["stage4c"])
        self.assertIn("occupancy_decline", rows["COLD_CHAIN_DEBT_OCCUPANCY_RISK"]["stage4c"])
        self.assertIn("maintenance_capex_misclassification", rows["REIT_AFFO_INTEGRITY_OVERLAY"]["stage4c"])
        self.assertIn("volume_decline", rows["BUILDING_MATERIALS_VOLUME_FAILURE"]["stage4c"])
        self.assertIn("green_premium_not_accepted", rows["LOW_CARBON_CEMENT_PREMIUM"]["stage4c"])
        self.assertIn("integration_failure", rows["BUILDING_PRODUCTS_MNA_SHIFT"]["stage4c"])
        self.assertIn("deal_price_unknown", rows["PRECAST_WALLING_BUILDING_SOLUTIONS"]["stage4c"])
        self.assertIn("contract_value_missing", rows["DISCLOSURE_CONFIDENCE_CAP"]["stage4c"])
        for field in (
            "stage2_price",
            "below_stage2_price_flag",
            "pf_exposure",
            "pf_delinquency_rate",
            "syndicated_loan_amount",
            "pf_soft_landing_support_flag",
            "refinancing_success_flag",
            "cash_conversion_cycle",
            "construction_cost_ratio",
            "occupancy_rate",
            "noi_growth",
            "affo_growth",
            "affo_per_share_growth",
            "dividend_coverage_ratio",
            "maintenance_capex",
            "expansion_capex",
            "capex_amount",
            "capex_to_affo_ratio",
            "affo_integrity_risk_flag",
            "data_center_asset_acquired_flag",
            "binding_lease_flag",
            "non_binding_loi_flag",
            "tenant_funding_agreement_terminated_flag",
            "power_secured_flag",
            "water_permitting_flag",
            "water_rights_flag",
            "ratepayer_cost_risk_flag",
            "utility_strain_flag",
            "power_cost_concern_flag",
            "public_hearing_delay_flag",
            "advanced_liquid_cooling_flag",
            "grid_interconnection_flag",
            "local_opposition_flag",
            "referendum_or_moratorium_flag",
            "project_withdrawal_flag",
            "urban_datacenter_moratorium_flag",
            "zoning_pause_flag",
            "community_submission_count",
            "ai_power_campus_flag",
            "planned_power_gw",
            "planned_power_delivery_year",
            "tenant_signed_flag",
            "cold_storage_warehouse_count",
            "energy_cost_ratio",
            "net_loss_flag",
            "post_ipo_drawdown_flag",
            "debt_to_ebitda",
            "building_material_volume",
            "price_hike_flag",
            "cost_saving_amount",
            "ebitda_change",
            "volume_decline_flag",
            "low_carbon_cement_flag",
            "net_zero_cement_flag",
            "carbon_capture_capacity_tons",
            "building_products_mna_flag",
            "precast_concrete_flag",
            "walling_systems_flag",
            "water_management_systems_flag",
            "production_site_count",
            "target_revenue",
            "target_ebitda",
            "mna_multiple",
            "systems_selling_opportunity",
            "deal_price_unknown",
            "budget_allocated_flag",
            "financing_failure_flag",
            "disclosure_confidence_score",
            "detail_parser_confidence",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND129_PRICE_FIELDS))

    def test_summary_and_markdown_explain_r10_loop7_guardrails(self):
        summary = round129_summary()
        summary_md = render_round129_summary_markdown()
        guardrails = render_round129_green_guardrail_markdown()
        overlays = render_round129_risk_overlay_markdown()
        price_plan = render_round129_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 28)
        self.assertEqual(summary["base_score_axis_count"], 7)
        self.assertEqual(summary["case_candidate_count"], 25)
        self.assertEqual(summary["success_candidate_count"], 6)
        self.assertEqual(summary["event_premium_count"], 5)
        self.assertEqual(summary["failed_rerating_count"], 0)
        self.assertEqual(summary["stage4b_case_count"], 13)
        self.assertEqual(summary["stage4c_case_count"], 7)
        self.assertEqual(summary["green_possible_count"], 6)
        self.assertEqual(summary["watch_yellow_first_count"], 8)
        self.assertEqual(summary["redteam_first_count"], 14)
        self.assertEqual(summary["gate_only_target_count"], 9)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("Round 129", summary_md)
        self.assertIn("R10 v7 Base Score Axes", summary_md)
        self.assertIn("eps_fcf_affo_noi_conversion: 24", summary_md)
        self.assertIn("Do not apply R10 Loop-7 v7.0 weights", guardrails)
        self.assertIn("REIT_AFFO_INTEGRITY_OVERLAY", overlays)
        self.assertIn("DATA_CENTER_WATER_RIGHTS_REFERENDUM", overlays)
        self.assertIn("blackstone_data_center_reit_ipo_case", price_plan)
        self.assertIn("holcim_alkern_precast_case", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round129_r10_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r10_loop7_round129.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round129_r10_loop7_v7.csv",
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
            self.assertTrue(paths["base_score_axes"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND129_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round129_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round129_r10_loop7_construction_real_estate_materials", text)


if __name__ == "__main__":
    unittest.main()
