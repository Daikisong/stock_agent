import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round89_r10_loop4_report import build_parser
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round89_r10_loop4_construction_real_estate_materials import (
    ROUND89_CASE_CANDIDATES,
    ROUND89_PRICE_FIELDS,
    ROUND89_SCORE_TARGETS,
    render_round89_green_guardrail_markdown,
    render_round89_price_validation_plan_markdown,
    render_round89_risk_overlay_markdown,
    render_round89_summary_markdown,
    round89_case_candidate_rows,
    round89_case_records,
    round89_price_field_rows,
    round89_score_profile_rows,
    round89_stage_date_rows,
    round89_summary,
    target_for,
    write_round89_r10_reports,
)


class Round89R10Loop4ConstructionRealEstateMaterialsTests(unittest.TestCase):
    def test_round89_targets_cover_r10_loop4_archetypes(self):
        labels = {target.target_id for target in ROUND89_SCORE_TARGETS}

        self.assertEqual(len(labels), 19)
        for label in (
            "CONSTRUCTION_REAL_ESTATE_CREDIT",
            "PF_RESTRUCTURING_RELIEF",
            "RESIDENTIAL_HOUSING_CYCLE",
            "REIT_DEVELOPMENT_TRUST",
            "COMMERCIAL_REAL_ESTATE_CREDIT",
            "DATA_CENTER_REIT_INFRASTRUCTURE",
            "DATA_CENTER_REIT_IPO_NO_ASSET",
            "AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT",
            "DATA_CENTER_POWER_WATER_PERMITTING",
            "DATA_CENTER_CAPEX_AFFO_DILUTION",
            "COLD_CHAIN_REIT_LOGISTICS",
            "COLD_CHAIN_DEBT_OCCUPANCY_RISK",
            "BUILDING_MATERIALS_PRICE_COST",
            "BUILDING_MATERIALS_VOLUME_FAILURE",
            "INFRA_RECONSTRUCTION_POLICY",
            "POLICY_LOCAL_REAL_ESTATE_THEME",
            "PF_CREDIT_REDTEAM_OVERLAY",
            "REIT_AFFO_INTEGRITY_OVERLAY",
            "AI_INFRA_REAL_ASSET_THEME_OVERLAY",
        ):
            self.assertIn(label, labels)
        for target in ROUND89_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS)
            self.assertFalse(target.production_scoring_changed)

    def test_data_center_cold_chain_and_materials_are_green_possible_but_guardrailed(self):
        dc_reit = target_for("DATA_CENTER_REIT_INFRASTRUCTURE")
        dc_ipo = target_for("DATA_CENTER_REIT_IPO_NO_ASSET")
        cold_chain = target_for("COLD_CHAIN_REIT_LOGISTICS")
        materials = target_for("BUILDING_MATERIALS_PRICE_COST")

        assert dc_reit is not None
        assert dc_ipo is not None
        assert cold_chain is not None
        assert materials is not None
        self.assertEqual(dc_reit.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("power_water_secured", dc_reit.green_conditions)
        self.assertIn("no_acquired_assets", dc_reit.stage4c_conditions)
        self.assertEqual(dc_ipo.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("no_acquired_assets", dc_ipo.stage4c_conditions)
        self.assertIn("asset_acquired_flag", dc_ipo.green_conditions)
        self.assertEqual(cold_chain.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("dividend_coverage", cold_chain.green_conditions)
        self.assertIn("net_loss", cold_chain.red_flags)
        self.assertEqual(materials.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("volume_recovery", materials.green_conditions)
        self.assertIn("volume_decline", materials.red_flags)

    def test_pf_affo_power_water_and_ai_theme_overlays_are_gate_only(self):
        pf = target_for("PF_CREDIT_REDTEAM_OVERLAY")
        affo = target_for("REIT_AFFO_INTEGRITY_OVERLAY")
        power_water = target_for("DATA_CENTER_POWER_WATER_PERMITTING")
        capex_affo = target_for("DATA_CENTER_CAPEX_AFFO_DILUTION")
        cold_debt = target_for("COLD_CHAIN_DEBT_OCCUPANCY_RISK")
        ai_theme = target_for("AI_INFRA_REAL_ASSET_THEME_OVERLAY")

        for target in (pf, affo, power_water, capex_affo, cold_debt, ai_theme):
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
        assert ai_theme is not None
        self.assertIn("no_revenue", ai_theme.stage4c_conditions)

    def test_required_round89_cases_are_present_with_stage_dates(self):
        rows = {row["case_id"]: row for row in round89_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND89_CASE_CANDIDATES))
        self.assertEqual(rows["korea_pf_delinquency_restructuring_case"]["target_id"], "PF_CREDIT_REDTEAM_OVERLAY")
        self.assertEqual(rows["korea_pf_delinquency_restructuring_case"]["stage4c_date"], "2024-05-13")
        self.assertEqual(rows["korea_builder_support_relief_case"]["target_id"], "PF_RESTRUCTURING_RELIEF")
        self.assertEqual(rows["korea_builder_support_relief_case"]["stage4b_date"], "2024-03-27")
        self.assertEqual(rows["blackstone_mortgage_trust_dividend_cut_case"]["stage4c_date"], "2024-07-24")
        self.assertEqual(rows["equinix_affo_integrity_short_case"]["target_id"], "REIT_AFFO_INTEGRITY_OVERLAY")
        self.assertEqual(rows["equinix_affo_integrity_short_case"]["stage4c_date"], "2024-03-20")
        self.assertEqual(rows["equinix_ai_capex_burden_case"]["target_id"], "DATA_CENTER_CAPEX_AFFO_DILUTION")
        self.assertEqual(rows["equinix_ai_capex_burden_case"]["stage4b_date"], "2025-06-26")
        self.assertEqual(rows["equinix_malaysia_ai_liquid_cooling_case"]["target_id"], "DATA_CENTER_REIT_INFRASTRUCTURE")
        self.assertEqual(rows["equinix_malaysia_ai_liquid_cooling_case"]["stage2_date"], "2026-05-12")
        self.assertEqual(rows["blackstone_data_center_reit_flat_debut_case"]["target_id"], "DATA_CENTER_REIT_IPO_NO_ASSET")
        self.assertEqual(rows["blackstone_data_center_reit_flat_debut_case"]["stage4b_date"], "2026-05-14")
        self.assertEqual(rows["fermi_ai_data_center_no_revenue_case"]["target_id"], "AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT")
        self.assertEqual(rows["fermi_no_tenant_net_loss_case"]["target_id"], "AI_INFRA_REAL_ASSET_THEME_OVERLAY")
        self.assertEqual(rows["fermi_no_tenant_net_loss_case"]["stage4c_date"], "2026-03-30")
        self.assertEqual(rows["perth_datacenter_withdrawal_case"]["stage4c_date"], "2026-05-15")
        self.assertEqual(rows["utah_stratos_datacenter_backlash_case"]["stage4b_date"], "2026-05-13")
        self.assertEqual(rows["lineage_cold_storage_ipo_case"]["stage2_date"], "2024-07-25")
        self.assertEqual(rows["lineage_cold_storage_debt_occupancy_case"]["target_id"], "COLD_CHAIN_DEBT_OCCUPANCY_RISK")
        self.assertEqual(rows["lineage_cold_storage_debt_occupancy_case"]["stage4c_date"], "2025-10-01")
        self.assertEqual(rows["heidelberg_materials_price_cost_case"]["target_id"], "BUILDING_MATERIALS_PRICE_COST")
        self.assertEqual(rows["cemex_demand_slowdown_costcut_case"]["target_id"], "BUILDING_MATERIALS_VOLUME_FAILURE")
        self.assertEqual(rows["cemex_price_cost_restructuring_case"]["target_id"], "BUILDING_MATERIALS_PRICE_COST")
        self.assertEqual(rows["cemex_price_cost_restructuring_case"]["stage2_date"], "2025-10-27")
        self.assertEqual(rows["sejong_policy_theme_case"]["target_id"], "POLICY_LOCAL_REAL_ESTATE_THEME")

    def test_case_records_validate_and_keep_round89_guardrails(self):
        records = round89_case_records()

        self.assertEqual(len(records), len(ROUND89_CASE_CANDIDATES))
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

    def test_score_profile_rows_match_round89_weight_table(self):
        rows = {row["target_id"]: row for row in round89_score_profile_rows()}

        self.assertEqual(rows["CONSTRUCTION_REAL_ESTATE_CREDIT"]["eps_fcf"], "12")
        self.assertEqual(rows["PF_RESTRUCTURING_RELIEF"]["structural_visibility"], "8")
        self.assertEqual(rows["DATA_CENTER_REIT_INFRASTRUCTURE"]["structural_visibility"], "22")
        self.assertEqual(rows["DATA_CENTER_REIT_IPO_NO_ASSET"]["eps_fcf"], "11")
        self.assertEqual(rows["AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT"]["bottleneck_pricing"], "16")
        self.assertEqual(rows["DATA_CENTER_CAPEX_AFFO_DILUTION"]["gate_only"], "true")
        self.assertEqual(rows["COLD_CHAIN_REIT_LOGISTICS"]["valuation"], "10")
        self.assertEqual(rows["COLD_CHAIN_DEBT_OCCUPANCY_RISK"]["eps_fcf"], "gate")
        self.assertEqual(rows["BUILDING_MATERIALS_PRICE_COST"]["eps_fcf"], "18")
        self.assertEqual(rows["BUILDING_MATERIALS_VOLUME_FAILURE"]["structural_visibility"], "9")
        self.assertEqual(rows["DATA_CENTER_POWER_WATER_PERMITTING"]["eps_fcf"], "gate")
        self.assertEqual(rows["REIT_AFFO_INTEGRITY_OVERLAY"]["gate_only"], "true")
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round89_stage_date_rows()}
        fields = {row["field"] for row in round89_price_field_rows()}

        self.assertIn("refinancing_success", rows["CONSTRUCTION_REAL_ESTATE_CREDIT"]["stage2"])
        self.assertIn("binding_tenant_lease", rows["DATA_CENTER_REIT_INFRASTRUCTURE"]["stage2"])
        self.assertIn("asset_acquired_flag", rows["DATA_CENTER_REIT_IPO_NO_ASSET"]["stage2"])
        self.assertIn("project_withdrawal", rows["DATA_CENTER_POWER_WATER_PERMITTING"]["stage4c"])
        self.assertIn("per_share_affo_slowdown", rows["DATA_CENTER_CAPEX_AFFO_DILUTION"]["stage4c"])
        self.assertIn("occupancy_decline", rows["COLD_CHAIN_DEBT_OCCUPANCY_RISK"]["stage4c"])
        self.assertIn("maintenance_capex_misclassification", rows["REIT_AFFO_INTEGRITY_OVERLAY"]["stage4c"])
        self.assertIn("volume_decline", rows["BUILDING_MATERIALS_VOLUME_FAILURE"]["stage4c"])
        for field in (
            "stage2_price",
            "below_stage2_price_flag",
            "pf_exposure",
            "pf_delinquency_rate",
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
            "funding_agreement_terminated_flag",
            "power_secured_flag",
            "water_permitting_flag",
            "advanced_liquid_cooling_flag",
            "grid_interconnection_flag",
            "local_opposition_flag",
            "referendum_or_moratorium_flag",
            "project_withdrawal_flag",
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
            "budget_allocated_flag",
            "financing_failure_flag",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND89_PRICE_FIELDS))

    def test_summary_and_markdown_explain_r10_loop4_guardrails(self):
        summary = round89_summary()
        summary_md = render_round89_summary_markdown()
        guardrails = render_round89_green_guardrail_markdown()
        overlays = render_round89_risk_overlay_markdown()
        price_plan = render_round89_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 19)
        self.assertEqual(summary["case_candidate_count"], 19)
        self.assertEqual(summary["success_candidate_count"], 3)
        self.assertEqual(summary["event_premium_count"], 4)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["stage4b_case_count"], 11)
        self.assertEqual(summary["stage4c_case_count"], 7)
        self.assertEqual(summary["green_possible_count"], 3)
        self.assertEqual(summary["watch_yellow_first_count"], 6)
        self.assertEqual(summary["redteam_first_count"], 10)
        self.assertEqual(summary["gate_only_target_count"], 6)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("Round 89", summary_md)
        self.assertIn("Do not apply R10 Loop-4 v4.0 weights", guardrails)
        self.assertIn("REIT_AFFO_INTEGRITY_OVERLAY", overlays)
        self.assertIn("blackstone_data_center_reit_flat_debut_case", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round89_r10_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r10_loop4_round89.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round89_r10_loop4_v4.csv",
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
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND89_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round89_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round89_r10_loop4_construction_real_estate_materials", text)


if __name__ == "__main__":
    unittest.main()
