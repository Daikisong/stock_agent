import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round81_r2_loop4_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round81_r2_loop4_ai_semiconductor import (
    ROUND81_CASE_CANDIDATES,
    ROUND81_PRICE_FIELDS,
    ROUND81_SCORE_TARGETS,
    render_round81_green_guardrail_markdown,
    render_round81_loop4_risk_overlay_markdown,
    render_round81_price_validation_plan_markdown,
    render_round81_summary_markdown,
    round81_case_candidate_rows,
    round81_case_records,
    round81_price_field_rows,
    round81_score_profile_rows,
    round81_stage_date_rows,
    round81_summary,
    round81_target_for,
    write_round81_r2_loop4_reports,
)


class Round81R2Loop4AISemiconductorTests(unittest.TestCase):
    def test_round81_targets_cover_loop4_ai_semiconductor_archetypes_and_overlays(self):
        labels = {target.target_id for target in ROUND81_SCORE_TARGETS}

        self.assertEqual(len(labels), 19)
        for label in (
            "MEMORY_HBM_CAPACITY",
            "HBM_CATCHUP_EXECUTION",
            "AI_STORAGE_NAND_SHORTAGE",
            "COMMODITY_MEMORY_GENERAL_SEMI",
            "SEMI_EQUIPMENT_AI_CAPEX",
            "SEMI_MATERIALS_PROCESS",
            "ADVANCED_PACKAGING_COWOS_EMIB",
            "ADVANCED_PACKAGING_PCB",
            "OPTICAL_NETWORKING_AI_DATACENTER",
            "AI_SERVER_ODM_EMS_SUPPLY_CHAIN",
            "NEOCLOUD_GPU_RENTAL",
            "AI_DATA_CENTER_COOLING",
            "INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA",
            "AI_CHIP_FABRIC_INFRA",
            "AI_ACCELERATOR_CHIP_PUREPLAY",
            "DISPLAY_OLED_SUPPLYCHAIN",
            "ELECTRONIC_COMPONENTS_MLCC_SENSOR",
            "REDTEAM_ACCOUNTING_TRUST_OVERLAY",
            "AI_CAPEX_CROWDING_OVERLAY",
        ):
            self.assertIn(label, labels)
        for target in ROUND81_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS)
            self.assertFalse(target.production_scoring_changed)

    def test_new_loop4_canonical_archetypes_exist(self):
        self.assertIsInstance(E2RArchetype.HBM_CATCHUP_EXECUTION.value, str)
        self.assertIsInstance(E2RArchetype.AI_STORAGE_NAND_SHORTAGE.value, str)
        self.assertIsInstance(E2RArchetype.SEMI_EQUIPMENT_AI_CAPEX.value, str)
        self.assertIsInstance(E2RArchetype.AI_CAPEX_CROWDING_OVERLAY.value, str)

    def test_loop4_weights_distinguish_hbm_optical_server_and_neocloud(self):
        hbm = round81_target_for("MEMORY_HBM_CAPACITY")
        hbm_catchup = round81_target_for("HBM_CATCHUP_EXECUTION")
        ai_storage = round81_target_for("AI_STORAGE_NAND_SHORTAGE")
        equipment = round81_target_for("SEMI_EQUIPMENT_AI_CAPEX")
        optical = round81_target_for("OPTICAL_NETWORKING_AI_DATACENTER")
        server = round81_target_for("AI_SERVER_ODM_EMS_SUPPLY_CHAIN")
        neocloud = round81_target_for("NEOCLOUD_GPU_RENTAL")
        capex_overlay = round81_target_for("AI_CAPEX_CROWDING_OVERLAY")

        self.assertIsNotNone(hbm)
        self.assertIsNotNone(hbm_catchup)
        self.assertIsNotNone(ai_storage)
        self.assertIsNotNone(equipment)
        self.assertIsNotNone(optical)
        self.assertIsNotNone(server)
        self.assertIsNotNone(neocloud)
        self.assertIsNotNone(capex_overlay)
        assert hbm is not None
        assert hbm_catchup is not None
        assert ai_storage is not None
        assert equipment is not None
        assert optical is not None
        assert server is not None
        assert neocloud is not None
        assert capex_overlay is not None
        self.assertEqual(hbm.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(hbm.score_weight.eps_fcf, 24)
        self.assertEqual(hbm.score_weight.valuation, 9)
        self.assertIn("customer_price_resistance", hbm.loop4_penalty_axes)
        self.assertEqual(hbm_catchup.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertEqual(hbm_catchup.score_weight.valuation, 10)
        self.assertIn("labor_strike", hbm_catchup.red_flags)
        self.assertEqual(ai_storage.score_weight.eps_fcf, 23)
        self.assertIn("consumer_demand_destruction", ai_storage.red_flags)
        self.assertEqual(equipment.score_weight.valuation, 11)
        self.assertIn("order_pushout", equipment.red_flags)
        self.assertEqual(optical.score_weight.bottleneck_pricing, 21)
        self.assertIn("lead_time_normalization", optical.red_flags)
        self.assertEqual(server.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("consignment_model", server.red_flags)
        self.assertEqual(neocloud.score_weight.valuation, 7)
        self.assertIn("fcf_negative", neocloud.red_flags)
        self.assertEqual(capex_overlay.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertFalse(capex_overlay.hard_gate)
        self.assertIn("revision_slowdown", capex_overlay.red_flags)

    def test_accounting_trust_overlay_is_hard_gate(self):
        overlay = round81_target_for("REDTEAM_ACCOUNTING_TRUST_OVERLAY")

        self.assertIsNotNone(overlay)
        assert overlay is not None
        self.assertEqual(overlay.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertTrue(overlay.hard_gate)
        self.assertEqual(overlay.score_weight.eps_fcf, "gate")
        self.assertIn("auditor_resignation", overlay.red_flags)
        self.assertIn("internal_control_weakness", overlay.red_flags)

    def test_required_round81_cases_are_present_with_loop4_stage_markers(self):
        rows = {row["case_id"]: row for row in round81_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND81_CASE_CANDIDATES))
        self.assertEqual(rows["sk_hynix_hbm_trillion_case"]["stage2_date"], "2026-05-14")
        self.assertEqual(rows["sk_hynix_hbm_trillion_case"]["stage3_date"], "2026-05-14")
        self.assertEqual(rows["sk_hynix_hbm_trillion_case"]["stage4b_date"], "2026-05-14")
        self.assertEqual(rows["samsung_hbm4_shipping_case"]["target_id"], "HBM_CATCHUP_EXECUTION")
        self.assertEqual(rows["samsung_hbm4_shipping_case"]["stage2_date"], "2026-02-12")
        self.assertEqual(rows["samsung_amd_hbm4_mou_case"]["target_id"], "HBM_CATCHUP_EXECUTION")
        self.assertEqual(rows["samsung_amd_hbm4_mou_case"]["stage2_date"], "2026-03-18")
        self.assertEqual(rows["samsung_labor_strike_execution_case"]["target_id"], "HBM_CATCHUP_EXECUTION")
        self.assertEqual(rows["samsung_labor_strike_execution_case"]["stage2_date"], "2026-05-15")
        self.assertEqual(rows["kioxia_ai_nand_profit_case"]["target_id"], "AI_STORAGE_NAND_SHORTAGE")
        self.assertEqual(rows["kioxia_ai_nand_profit_case"]["case_type"], "4b_watch")
        self.assertEqual(rows["kioxia_ai_nand_profit_case"]["stage4b_date"], "2026-05-15")
        self.assertEqual(rows["applied_materials_ai_packaging_growth_case"]["target_id"], "SEMI_EQUIPMENT_AI_CAPEX")
        self.assertEqual(rows["applied_materials_ai_packaging_growth_case"]["stage2_date"], "2026-05-14")
        self.assertEqual(rows["nvidia_cowos_l_transition_case"]["stage2_date"], "2025-01-16")
        self.assertEqual(rows["broadcom_optical_pcb_leadtime_case"]["stage2_date"], "2026-03-24")
        self.assertEqual(rows["foxconn_ai_server_rack_growth_case"]["stage2_date"], "2026-05-14")
        self.assertEqual(rows["ecolab_coolit_liquid_cooling_case"]["stage2_date"], "2026-03-20")
        self.assertEqual(rows["coreweave_openai_contract_case"]["stage2_date"], "2025-03-10")
        self.assertEqual(rows["coreweave_expanded_openai_contract_case"]["stage2_date"], "2025-09-25")
        self.assertEqual(rows["coreweave_downsized_ipo_debt_case"]["stage2_date"], "2025-03-28")
        self.assertEqual(rows["cerebras_ai_accelerator_ipo_case"]["case_type"], "event_premium")
        self.assertEqual(rows["cerebras_ai_accelerator_ipo_case"]["stage2_date"], "2026-05-14")
        self.assertEqual(rows["supermicro_ey_resignation_case"]["stage4c_date"], "2024-10-30")
        self.assertEqual(rows["cxl_glass_substrate_theme_case"]["case_type"], "overheat")
        self.assertEqual(rows["ai_capex_crowding_overlay_case"]["target_id"], "AI_CAPEX_CROWDING_OVERLAY")

    def test_case_records_validate_and_keep_loop4_guardrails(self):
        records = round81_case_records()

        self.assertEqual(len(records), len(ROUND81_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, "AI_SEMICONDUCTOR_ELECTRONICS")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_change_production_scoring", record.green_guardrails)
            self.assertIn("ai_beneficiary_is_not_one_archetype", record.green_guardrails)
            self.assertIn("do_not_invent_contract_prices_margins_customers_stage_prices_or_yield", record.green_guardrails)
        by_id = {record.case_id: record for record in records}
        self.assertEqual(by_id["sk_hynix_hbm_trillion_case"].rerating_result, "true_rerating")
        self.assertEqual(by_id["coreweave_openai_contract_case"].score_price_alignment, "evidence_good_but_price_failed")
        self.assertEqual(by_id["cerebras_ai_accelerator_ipo_case"].rerating_result, "event_premium")
        self.assertEqual(by_id["supermicro_ey_resignation_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["cxl_glass_substrate_theme_case"].score_price_alignment, "price_moved_without_evidence")
        self.assertIn("labor_strike", by_id["samsung_labor_strike_execution_case"].red_flag_fields)

    def test_score_profile_rows_match_round81_weight_table(self):
        rows = {row["target_id"]: row for row in round81_score_profile_rows()}

        self.assertEqual(rows["MEMORY_HBM_CAPACITY"]["eps_fcf"], "24")
        self.assertEqual(rows["MEMORY_HBM_CAPACITY"]["structural_visibility"], "22")
        self.assertEqual(rows["MEMORY_HBM_CAPACITY"]["valuation"], "9")
        self.assertEqual(rows["HBM_CATCHUP_EXECUTION"]["eps_fcf"], "22")
        self.assertEqual(rows["AI_STORAGE_NAND_SHORTAGE"]["eps_fcf"], "23")
        self.assertEqual(rows["COMMODITY_MEMORY_GENERAL_SEMI"]["eps_fcf"], "22")
        self.assertEqual(rows["SEMI_EQUIPMENT_AI_CAPEX"]["valuation"], "11")
        self.assertEqual(rows["OPTICAL_NETWORKING_AI_DATACENTER"]["bottleneck_pricing"], "21")
        self.assertEqual(rows["AI_SERVER_ODM_EMS_SUPPLY_CHAIN"]["valuation"], "8")
        self.assertEqual(rows["NEOCLOUD_GPU_RENTAL"]["valuation"], "7")
        self.assertEqual(rows["REDTEAM_ACCOUNTING_TRUST_OVERLAY"]["hard_gate"], "true")
        self.assertEqual(rows["AI_CAPEX_CROWDING_OVERLAY"]["hard_gate"], "false")
        self.assertEqual(rows["AI_CAPEX_CROWDING_OVERLAY"]["eps_fcf"], "gate")
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round81_stage_date_rows()}
        fields = {row["field"] for row in round81_price_field_rows()}

        self.assertIn("hbm_capacity_constraint", rows["MEMORY_HBM_CAPACITY"]["stage3"])
        self.assertIn("customer_qualification", rows["HBM_CATCHUP_EXECUTION"]["stage2"])
        self.assertIn("enterprise_ssd_revenue", rows["AI_STORAGE_NAND_SHORTAGE"]["stage2"])
        self.assertIn("order_pushout", rows["SEMI_EQUIPMENT_AI_CAPEX"]["stage4c"])
        self.assertIn("lead_time_normalization", rows["OPTICAL_NETWORKING_AI_DATACENTER"]["stage4b"])
        self.assertIn("refinancing_pressure", rows["NEOCLOUD_GPU_RENTAL"]["stage4c"])
        self.assertIn("auditor_resignation", rows["REDTEAM_ACCOUNTING_TRUST_OVERLAY"]["stage4c"])
        self.assertIn("customer_capex_cut", rows["AI_CAPEX_CROWDING_OVERLAY"]["stage4c"])
        for field in (
            "hbm4_shipping_flag",
            "hbm4_yield_signal",
            "qualification_status",
            "customer_specific_base_die_flag",
            "nand_profit_growth",
            "enterprise_ssd_revenue",
            "consumer_demand_destruction_flag",
            "customer_forecast_duration_quarters",
            "emib_revenue_flag",
            "pcb_lead_time_weeks",
            "optical_networking_inventory_flag",
            "silicon_photonics_revenue",
            "working_capital_pressure",
            "gpu_depreciation",
            "ipo_downsize_flag",
            "delivery_issue_flag",
            "mna_multiple",
            "ai_accelerator_revenue",
            "software_ecosystem_score",
            "nvidia_competition_flag",
            "ipo_first_day_return",
            "auditor_resignation_flag",
            "labor_strike_flag",
            "talent_retention_risk_flag",
            "theme_only_flag",
            "customer_validation_flag",
            "direct_equity_exposure_flag",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND81_PRICE_FIELDS))

    def test_summary_and_markdown_explain_loop4_ai_distinctions(self):
        summary = round81_summary()
        summary_md = render_round81_summary_markdown()
        guardrails = render_round81_green_guardrail_markdown()
        overlays = render_round81_loop4_risk_overlay_markdown()
        price_plan = render_round81_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 19)
        self.assertEqual(summary["case_candidate_count"], 18)
        self.assertEqual(summary["structural_success_count"], 1)
        self.assertEqual(summary["success_candidate_count"], 9)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["overheat_count"], 2)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["stage4b_case_count"], 3)
        self.assertEqual(summary["stage4c_case_count"], 1)
        self.assertEqual(summary["green_possible_count"], 4)
        self.assertEqual(summary["watch_yellow_first_count"], 13)
        self.assertEqual(summary["redteam_first_count"], 2)
        self.assertEqual(summary["hard_gate_target_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("R2 Loop 4", summary_md)
        self.assertIn("Do not apply R2 Loop-4 v4.0 weights", guardrails)
        self.assertIn("OpenAI contract", overlays)
        self.assertIn("supermicro_ey_resignation_case", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round81_r2_loop4_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r2_loop4_round81.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round81_r2_loop4_v4.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["stage_date_plan"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["loop4_risk_overlays"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertTrue(paths["price_fields"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND81_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round81_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round81_r2_loop4_ai_semiconductor", text)


if __name__ == "__main__":
    unittest.main()
