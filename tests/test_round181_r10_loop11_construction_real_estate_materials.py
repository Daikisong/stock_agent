import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round181_r10_loop11_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round181_r10_loop11_construction_real_estate_materials import (
    ROUND181_BASE_SCORE_WEIGHTS,
    ROUND181_CASE_CANDIDATES,
    ROUND181_PRICE_FIELDS,
    ROUND181_SCORE_STAGE_PRICE_ALIGNMENT,
    ROUND181_SCORE_TARGETS,
    ROUND181_SOURCE_CANONICAL_TARGET_COUNT,
    ROUND181_SOURCE_CANONICAL_TARGET_IDS,
    ROUND181_STAGE_CAPS,
    render_round181_green_guardrail_markdown,
    render_round181_price_validation_plan_markdown,
    render_round181_risk_overlay_markdown,
    render_round181_score_stage_price_alignment_markdown,
    render_round181_summary_markdown,
    round181_base_score_weight_rows,
    round181_case_candidate_rows,
    round181_case_records,
    round181_price_field_rows,
    round181_score_profile_rows,
    round181_score_stage_price_alignment_rows,
    round181_stage_cap_rows,
    round181_stage_date_rows,
    round181_summary,
    round181_target_for,
    write_round181_r10_loop11_reports,
)


class Round181R10Loop11ConstructionRealEstateMaterialsTests(unittest.TestCase):
    def test_round181_targets_cover_source_archetypes(self):
        labels = {target.target_id for target in ROUND181_SCORE_TARGETS}

        self.assertEqual(ROUND181_SOURCE_CANONICAL_TARGET_COUNT, 13)
        self.assertEqual(len(labels), 13)
        self.assertEqual(set(ROUND181_SOURCE_CANONICAL_TARGET_IDS), labels)
        for target in ROUND181_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS)
            self.assertFalse(target.production_scoring_changed)

    def test_new_r10_loop11_korea_construction_archetypes_exist(self):
        expected = (
            E2RArchetype.OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA,
            E2RArchetype.EPC_LOW_MARGIN_ORDER_OVERLAY,
            E2RArchetype.AI_DATA_CENTER_REAL_ASSET_KOREA,
            E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT_KOREA,
            E2RArchetype.PF_RESTRUCTURING_RELIEF_KOREA,
            E2RArchetype.APARTMENT_QUALITY_SAFETY_OVERLAY,
            E2RArchetype.LARGE_BUILDER_BALANCE_SHEET_DEFENSE,
            E2RArchetype.K_REIT_DIVIDEND_COVERAGE,
            E2RArchetype.LOGISTICS_REIT_OCCUPANCY_KOREA,
            E2RArchetype.BUILDING_MATERIALS_PRICE_COST_KOREA,
            E2RArchetype.CEMENT_REGULATORY_COLLUSION_OVERLAY,
            E2RArchetype.HOME_INTERIOR_HOUSING_CYCLE,
        )

        for archetype in expected:
            self.assertIsInstance(archetype.value, str)

    def test_loop11_base_score_weights_and_stage_caps_match_round_note(self):
        weights = {row["component"]: row for row in round181_base_score_weight_rows()}
        caps = {row["stage_band"]: row for row in round181_stage_cap_rows()}

        self.assertEqual(len(ROUND181_BASE_SCORE_WEIGHTS), 7)
        self.assertEqual(weights["eps_fcf_noi_affo_conversion"]["points"], "24")
        self.assertEqual(weights["contract_asset_tenant_pf_visibility"]["points"], "20")
        self.assertEqual(weights["cash_conversion_cost_ratio_dividend_coverage"]["points"], "18")
        self.assertEqual(weights["pf_safety_quality_regulatory_risk"]["points"], "16")
        self.assertEqual(weights["early_price_path_validation"]["points"], "8")
        self.assertEqual(weights["market_mispricing_rerating_gap"]["points"], "8")
        self.assertEqual(weights["valuation_room_4b_runway"]["points"], "6")
        self.assertEqual(len(ROUND181_STAGE_CAPS), 5)
        self.assertEqual(caps["Stage 1"]["max_score"], "45")
        self.assertEqual(caps["Stage 2"]["max_score"], "70")
        self.assertIn("requires_5_of_8", caps["Stage 3"]["max_score"])
        self.assertIn("cash_conversion_improves", caps["Stage 3"]["required_evidence"])
        self.assertIn("requires_3_of_5", caps["Stage 4B"]["max_score"])
        self.assertIn("pf_workout_or_debt_rescheduling", caps["Stage 4C"]["required_evidence"])

    def test_target_rules_separate_cashflow_from_headline(self):
        epc = round181_target_for("OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA")
        epc_gate = round181_target_for("EPC_LOW_MARGIN_ORDER_OVERLAY")
        ai_dc = round181_target_for("AI_DATA_CENTER_REAL_ASSET_KOREA")
        credit = round181_target_for("CONSTRUCTION_REAL_ESTATE_CREDIT_KOREA")
        pf_relief = round181_target_for("PF_RESTRUCTURING_RELIEF_KOREA")
        safety = round181_target_for("APARTMENT_QUALITY_SAFETY_OVERLAY")
        builder = round181_target_for("LARGE_BUILDER_BALANCE_SHEET_DEFENSE")
        reit = round181_target_for("K_REIT_DIVIDEND_COVERAGE")
        logistics_reit = round181_target_for("LOGISTICS_REIT_OCCUPANCY_KOREA")
        materials = round181_target_for("BUILDING_MATERIALS_PRICE_COST_KOREA")
        cement = round181_target_for("CEMENT_REGULATORY_COLLUSION_OVERLAY")
        interior = round181_target_for("HOME_INTERIOR_HOUSING_CYCLE")
        disclosure = round181_target_for("DISCLOSURE_CONFIDENCE_CAP")

        for target in (epc, epc_gate, ai_dc, credit, pf_relief, safety, builder, reit, logistics_reit, materials, cement, interior, disclosure):
            self.assertIsNotNone(target)
        assert epc is not None
        assert epc_gate is not None
        assert ai_dc is not None
        assert credit is not None
        assert pf_relief is not None
        assert safety is not None
        assert builder is not None
        assert reit is not None
        assert logistics_reit is not None
        assert materials is not None
        assert cement is not None
        assert interior is not None
        assert disclosure is not None
        self.assertEqual(epc.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("cost_ratio_stable", epc.green_conditions)
        self.assertTrue(epc_gate.gate_only)
        self.assertEqual(ai_dc.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("actual_contract_missing", ai_dc.red_flags)
        self.assertTrue(credit.gate_only)
        self.assertEqual(pf_relief.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertTrue(safety.gate_only)
        self.assertEqual(builder.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(reit.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertEqual(logistics_reit.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(materials.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertTrue(cement.gate_only)
        self.assertEqual(interior.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertEqual(disclosure.score_weight.eps_fcf_noi_affo_conversion, "cap")

    def test_required_round181_cases_are_present_with_stage_markers(self):
        rows = {row["case_id"]: row for row in round181_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND181_CASE_CANDIDATES))
        self.assertEqual(rows["samsung_ea_fadhili_epc_stage2_strong_case"]["stage2_date"], "2024-04-02")
        self.assertIn("samsung_ea_6bn_usd_contract", rows["samsung_ea_fadhili_epc_stage2_strong_case"]["evidence_fields"])
        self.assertEqual(rows["gs_construction_fadhili_epc_pf_quality_cap_case"]["stage2_date"], "2024-04-02")
        self.assertEqual(rows["samsung_ct_ai_data_center_option_no_contract_cap_case"]["stage1_date"], "2025-10-02")
        self.assertEqual(rows["samsung_ct_ai_data_center_option_no_contract_cap_case"]["stage2_date"], "2025-10-29")
        self.assertEqual(rows["samsung_ct_ai_data_center_option_no_contract_cap_case"]["stage4b_date"], "2025-10-02")
        self.assertEqual(rows["large_builder_pf_relief_balance_sheet_defense_case"]["stage1_date"], "2024-03-27")
        self.assertEqual(rows["large_builder_pf_relief_balance_sheet_defense_case"]["stage2_date"], "2024-03-27")
        self.assertEqual(rows["taeyoung_construction_pf_workout_hard_4c_case"]["stage4c_date"], "2024-03-27")
        self.assertEqual(rows["hdc_hyundai_development_gwangju_collapse_hard_4c_case"]["stage4c_date"], "2022-01-11")
        self.assertEqual(rows["hanil_cement_price_pass_collusion_regulatory_cap_case"]["target_id"], "BUILDING_MATERIALS_PRICE_COST_KOREA")
        self.assertEqual(rows["r10_disclosure_confidence_cap_case"]["target_id"], "DISCLOSURE_CONFIDENCE_CAP")

    def test_case_records_validate_and_keep_round181_guardrails(self):
        records = round181_case_records()

        self.assertEqual(len(records), len(ROUND181_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, "CONSTRUCTION_REAL_ESTATE_MATERIALS")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_change_production_scoring", record.green_guardrails)
            self.assertIn("construction_pf_reit_ai_dc_headline_is_not_stage3", record.green_guardrails)
            self.assertIn("require_contract_cost_cash_pf_or_noi_affo_evidence_for_green", record.green_guardrails)
            self.assertIn("stage3_early_catch_requires_5_of_8_loop11_conditions", record.green_guardrails)
            self.assertIn("do_not_invent_contract_amount_pf_noi_affo_cost_ratio_stage_prices_or_mfe_mae", record.green_guardrails)
        by_id = {record.case_id: record for record in records}
        self.assertIn(E2RArchetype.EPC_LOW_MARGIN_ORDER_OVERLAY, by_id["samsung_ea_fadhili_epc_stage2_strong_case"].secondary_archetypes)
        self.assertIn(E2RArchetype.PF_RESTRUCTURING_RELIEF_KOREA, by_id["gs_construction_fadhili_epc_pf_quality_cap_case"].secondary_archetypes)
        self.assertEqual(by_id["samsung_ct_ai_data_center_option_no_contract_cap_case"].score_price_alignment, "price_moved_without_evidence")
        self.assertEqual(by_id["taeyoung_construction_pf_workout_hard_4c_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["ai_data_center_no_contract_4b_watch_case"].rerating_result, "theme_overheat")
        self.assertEqual(by_id["r10_disclosure_confidence_cap_case"].score_price_alignment, "evidence_good_but_price_failed")

    def test_score_profile_rows_mark_no_production_change(self):
        rows = round181_score_profile_rows()

        self.assertEqual(len(rows), len(ROUND181_SCORE_TARGETS))
        for row in rows:
            self.assertEqual(row["large_sector"], "CONSTRUCTION_REAL_ESTATE_MATERIALS")
            self.assertEqual(row["production_scoring_changed"], "false")
            self.assertIn("loop11_penalty_axes", row)
        by_target = {row["target_id"]: row for row in rows}
        self.assertEqual(by_target["OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA"]["eps_fcf_noi_affo_conversion"], "24")
        self.assertEqual(by_target["LOGISTICS_REIT_OCCUPANCY_KOREA"]["posture"], Round10ThemePosture.GREEN_POSSIBLE.value)
        self.assertEqual(by_target["EPC_LOW_MARGIN_ORDER_OVERLAY"]["gate_only"], "true")
        self.assertEqual(by_target["K_REIT_DIVIDEND_COVERAGE"]["cash_conversion_cost_ratio_dividend_coverage"], "22")
        self.assertEqual(by_target["CONSTRUCTION_REAL_ESTATE_CREDIT_KOREA"]["eps_fcf_noi_affo_conversion"], "gate")
        self.assertEqual(by_target["DISCLOSURE_CONFIDENCE_CAP"]["eps_fcf_noi_affo_conversion"], "cap")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round181_stage_date_rows()}
        fields = {row["field"] for row in round181_price_field_rows()}

        self.assertIn("cash_conversion_improves", rows["OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA"]["stage3"])
        self.assertIn("cost_overrun", rows["EPC_LOW_MARGIN_ORDER_OVERLAY"]["stage4c"])
        self.assertIn("tenant_lease", rows["AI_DATA_CENTER_REAL_ASSET_KOREA"]["stage3"])
        self.assertIn("pf_workout", rows["CONSTRUCTION_REAL_ESTATE_CREDIT_KOREA"]["stage4c"])
        self.assertIn("fatal_collapse", rows["APARTMENT_QUALITY_SAFETY_OVERLAY"]["stage4c"])
        self.assertIn("affo_per_share_improves", rows["K_REIT_DIVIDEND_COVERAGE"]["stage3"])
        self.assertIn("collusion_fine", rows["CEMENT_REGULATORY_COLLUSION_OVERLAY"]["stage4c"])
        for field in (
            "return_1d_after_event",
            "return_5d_after_event",
            "return_60d_after_stage2",
            "mfe_60d_after_stage2",
            "relative_strength_vs_construction_basket",
            "relative_strength_vs_reit_basket",
            "relative_strength_vs_building_materials_basket",
            "contract_amount",
            "contract_counterparty",
            "contract_period",
            "project_completion_date",
            "cost_ratio",
            "cash_conversion_signal",
            "pf_exposure",
            "pf_refinancing_success_flag",
            "workout_flag",
            "debt_rescheduling_flag",
            "tenant_lease_flag",
            "occupancy",
            "noi",
            "affo",
            "affo_per_share",
            "dividend_coverage",
            "ltv",
            "refinancing_rate",
            "safety_accident_flag",
            "fatal_accident_flag",
            "government_investigation_flag",
            "quality_cost_flag",
            "business_suspension_flag",
            "building_material_volume",
            "price_pass_through_signal",
            "energy_cost_signal",
            "regulatory_collusion_flag",
        ):
            self.assertIn(field, fields)

    def test_score_stage_price_alignment_rows_and_markdown(self):
        rows = {row["case_id"]: row for row in round181_score_stage_price_alignment_rows()}
        markdown = render_round181_score_stage_price_alignment_markdown()

        self.assertEqual(len(rows), len(ROUND181_SCORE_STAGE_PRICE_ALIGNMENT))
        self.assertEqual(rows["samsung_ea_fadhili_epc_stage2_strong_case"]["verdict"], "epc_stage2_strong_not_green_until_margin_cash")
        self.assertEqual(rows["taeyoung_construction_pf_workout_hard_4c_case"]["verdict"], "pf_workout_hard_gate")
        self.assertEqual(rows["hdc_hyundai_development_gwangju_collapse_hard_4c_case"]["verdict"], "safety_quality_hard_gate")
        self.assertIn("Samsung E&A", markdown)
        self.assertIn("Taeyoung", markdown)
        self.assertIn("HDC", markdown)

    def test_summary_and_markdown_explain_r10_loop11_guardrails(self):
        summary = round181_summary()
        summary_md = render_round181_summary_markdown()
        guardrails = render_round181_green_guardrail_markdown()
        overlays = render_round181_risk_overlay_markdown()
        price_plan = render_round181_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 13)
        self.assertEqual(summary["source_canonical_target_count"], 13)
        self.assertEqual(summary["case_candidate_count"], len(ROUND181_CASE_CANDIDATES))
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["case_records_are_candidate_generation_input"])
        self.assertIn("Samsung E&A", summary_md)
        self.assertIn("NOI/AFFO", summary_md)
        self.assertIn("PF support", guardrails)
        self.assertIn("AFFO/share", overlays)
        self.assertIn("contract_amount", price_plan)
        self.assertIn("samsung_ea_fadhili_epc_stage2_strong_case", price_plan)

    def test_reports_are_written_and_case_jsonl_loads(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round181_r10_loop11_reports(
                output_directory=root / "reports",
                cases_path=root / "cases.jsonl",
                score_profile_path=root / "score_profiles.csv",
            )
            records = load_case_library(paths["cases"])

            self.assertEqual(len(records), len(ROUND181_CASE_CANDIDATES))
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["stage_date_plan"].exists())
            self.assertTrue(paths["price_fields"].exists())
            self.assertIn("Samsung E&A", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("construction_pf_reit_ai_dc_headline_is_not_stage3", paths["cases"].read_text(encoding="utf-8"))

    def test_cli_argument_parsing(self):
        args = build_parser().parse_args(
            [
                "--output-directory",
                "tmp_reports",
                "--cases",
                "tmp_cases.jsonl",
                "--score-profiles",
                "tmp_profiles.csv",
            ]
        )

        self.assertEqual(args.output_directory, "tmp_reports")
        self.assertEqual(args.cases, "tmp_cases.jsonl")
        self.assertEqual(args.score_profiles, "tmp_profiles.csv")

    def test_production_modules_do_not_import_round181(self):
        forbidden = "round181_r10_loop11_construction_real_estate_materials"
        for rel_path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(rel_path).read_text(encoding="utf-8")
            self.assertNotIn(forbidden, text)


if __name__ == "__main__":
    unittest.main()
