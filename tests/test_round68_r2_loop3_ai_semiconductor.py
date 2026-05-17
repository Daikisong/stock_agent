import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round68_r2_loop3_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round68_r2_loop3_ai_semiconductor import (
    ROUND68_CASE_CANDIDATES,
    ROUND68_PRICE_FIELDS,
    ROUND68_SCORE_TARGETS,
    render_round68_green_guardrail_markdown,
    render_round68_loop3_risk_overlay_markdown,
    render_round68_price_validation_plan_markdown,
    render_round68_summary_markdown,
    round68_case_candidate_rows,
    round68_case_records,
    round68_price_field_rows,
    round68_score_profile_rows,
    round68_stage_date_rows,
    round68_summary,
    round68_target_for,
    write_round68_r2_loop3_reports,
)


class Round68R2Loop3AISemiconductorTests(unittest.TestCase):
    def test_round68_targets_cover_loop3_ai_semiconductor_archetypes_and_overlays(self):
        labels = {target.target_id for target in ROUND68_SCORE_TARGETS}

        self.assertEqual(len(labels), 17)
        for label in (
            "MEMORY_HBM_CAPACITY",
            "COMMODITY_MEMORY_GENERAL_SEMI",
            "SEMI_EQUIPMENT_CAPEX",
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
        for target in ROUND68_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS)
            self.assertFalse(target.production_scoring_changed)

    def test_new_loop3_canonical_overlay_exists(self):
        self.assertIsInstance(E2RArchetype.AI_CAPEX_CROWDING_OVERLAY.value, str)

    def test_loop3_weights_distinguish_hbm_optical_server_and_neocloud(self):
        hbm = round68_target_for("MEMORY_HBM_CAPACITY")
        optical = round68_target_for("OPTICAL_NETWORKING_AI_DATACENTER")
        server = round68_target_for("AI_SERVER_ODM_EMS_SUPPLY_CHAIN")
        neocloud = round68_target_for("NEOCLOUD_GPU_RENTAL")
        capex_overlay = round68_target_for("AI_CAPEX_CROWDING_OVERLAY")

        self.assertIsNotNone(hbm)
        self.assertIsNotNone(optical)
        self.assertIsNotNone(server)
        self.assertIsNotNone(neocloud)
        self.assertIsNotNone(capex_overlay)
        assert hbm is not None
        assert optical is not None
        assert server is not None
        assert neocloud is not None
        assert capex_overlay is not None
        self.assertEqual(hbm.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(hbm.score_weight.eps_fcf, 24)
        self.assertEqual(hbm.score_weight.valuation, 10)
        self.assertIn("customer_price_resistance", hbm.loop3_penalty_axes)
        self.assertEqual(optical.score_weight.bottleneck_pricing, 21)
        self.assertIn("lead_time_normalization", optical.red_flags)
        self.assertEqual(server.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("consignment_model", server.red_flags)
        self.assertEqual(neocloud.score_weight.valuation, 8)
        self.assertIn("fcf_negative", neocloud.red_flags)
        self.assertEqual(capex_overlay.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertFalse(capex_overlay.hard_gate)
        self.assertIn("revision_slowdown", capex_overlay.red_flags)

    def test_accounting_trust_overlay_is_hard_gate(self):
        overlay = round68_target_for("REDTEAM_ACCOUNTING_TRUST_OVERLAY")

        self.assertIsNotNone(overlay)
        assert overlay is not None
        self.assertEqual(overlay.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertTrue(overlay.hard_gate)
        self.assertEqual(overlay.score_weight.eps_fcf, "gate")
        self.assertIn("auditor_resignation", overlay.red_flags)
        self.assertIn("internal_control_weakness", overlay.red_flags)

    def test_required_round68_cases_are_present_with_loop3_stage_markers(self):
        rows = {row["case_id"]: row for row in round68_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND68_CASE_CANDIDATES))
        self.assertEqual(rows["sk_hynix_hbm_trillion_case"]["stage2_date"], "2026-05-14")
        self.assertEqual(rows["sk_hynix_hbm_trillion_case"]["stage3_date"], "2026-05-14")
        self.assertEqual(rows["sk_hynix_hbm_trillion_case"]["stage4b_date"], "2026-05-14")
        self.assertEqual(rows["samsung_hbm4_shipping_case"]["stage2_date"], "2026-02-12")
        self.assertEqual(rows["samsung_labor_strike_execution_case"]["stage2_date"], "2026-05-15")
        self.assertEqual(rows["kioxia_ai_nand_profit_case"]["case_type"], "4b_watch")
        self.assertEqual(rows["kioxia_ai_nand_profit_case"]["stage4b_date"], "2026-05-15")
        self.assertEqual(rows["applied_materials_ai_packaging_growth_case"]["stage2_date"], "2026-05-14")
        self.assertEqual(rows["nvidia_cowos_l_transition_case"]["stage2_date"], "2025-01-16")
        self.assertEqual(rows["broadcom_optical_pcb_leadtime_case"]["stage2_date"], "2026-03-24")
        self.assertEqual(rows["foxconn_ai_server_rack_growth_case"]["stage2_date"], "2026-05-14")
        self.assertEqual(rows["ecolab_coolit_liquid_cooling_case"]["stage2_date"], "2026-03-20")
        self.assertEqual(rows["coreweave_openai_contract_case"]["stage2_date"], "2025-03-20")
        self.assertEqual(rows["coreweave_downsized_ipo_debt_case"]["stage2_date"], "2025-03-28")
        self.assertEqual(rows["supermicro_ey_resignation_case"]["stage4c_date"], "2024-10-30")
        self.assertEqual(rows["cxl_glass_substrate_theme_case"]["case_type"], "overheat")
        self.assertEqual(rows["ai_capex_crowding_overlay_case"]["target_id"], "AI_CAPEX_CROWDING_OVERLAY")

    def test_case_records_validate_and_keep_loop3_guardrails(self):
        records = round68_case_records()

        self.assertEqual(len(records), len(ROUND68_CASE_CANDIDATES))
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
        self.assertEqual(by_id["supermicro_ey_resignation_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["cxl_glass_substrate_theme_case"].score_price_alignment, "price_moved_without_evidence")
        self.assertIn("labor_strike", by_id["samsung_labor_strike_execution_case"].red_flag_fields)

    def test_score_profile_rows_match_round68_weight_table(self):
        rows = {row["target_id"]: row for row in round68_score_profile_rows()}

        self.assertEqual(rows["MEMORY_HBM_CAPACITY"]["eps_fcf"], "24")
        self.assertEqual(rows["MEMORY_HBM_CAPACITY"]["structural_visibility"], "22")
        self.assertEqual(rows["MEMORY_HBM_CAPACITY"]["valuation"], "10")
        self.assertEqual(rows["COMMODITY_MEMORY_GENERAL_SEMI"]["eps_fcf"], "23")
        self.assertEqual(rows["OPTICAL_NETWORKING_AI_DATACENTER"]["bottleneck_pricing"], "21")
        self.assertEqual(rows["AI_SERVER_ODM_EMS_SUPPLY_CHAIN"]["valuation"], "9")
        self.assertEqual(rows["NEOCLOUD_GPU_RENTAL"]["valuation"], "8")
        self.assertEqual(rows["REDTEAM_ACCOUNTING_TRUST_OVERLAY"]["hard_gate"], "true")
        self.assertEqual(rows["AI_CAPEX_CROWDING_OVERLAY"]["hard_gate"], "false")
        self.assertEqual(rows["AI_CAPEX_CROWDING_OVERLAY"]["eps_fcf"], "gate")
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round68_stage_date_rows()}
        fields = {row["field"] for row in round68_price_field_rows()}

        self.assertIn("hbm_capacity_constraint", rows["MEMORY_HBM_CAPACITY"]["stage3"])
        self.assertIn("lead_time_normalization", rows["OPTICAL_NETWORKING_AI_DATACENTER"]["stage4b"])
        self.assertIn("refinancing_pressure", rows["NEOCLOUD_GPU_RENTAL"]["stage4c"])
        self.assertIn("auditor_resignation", rows["REDTEAM_ACCOUNTING_TRUST_OVERLAY"]["stage4c"])
        self.assertIn("customer_capex_cut", rows["AI_CAPEX_CROWDING_OVERLAY"]["stage4c"])
        for field in (
            "hbm4_shipping_flag",
            "hbm4_yield_signal",
            "qualification_status",
            "nand_profit_growth",
            "pcb_lead_time_weeks",
            "silicon_photonics_revenue",
            "working_capital_pressure",
            "gpu_depreciation",
            "delivery_issue_flag",
            "mna_multiple",
            "auditor_resignation_flag",
            "labor_strike_flag",
            "theme_only_flag",
            "customer_validation_flag",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND68_PRICE_FIELDS))

    def test_summary_and_markdown_explain_loop3_ai_distinctions(self):
        summary = round68_summary()
        summary_md = render_round68_summary_markdown()
        guardrails = render_round68_green_guardrail_markdown()
        overlays = render_round68_loop3_risk_overlay_markdown()
        price_plan = render_round68_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 17)
        self.assertEqual(summary["case_candidate_count"], 15)
        self.assertEqual(summary["structural_success_count"], 1)
        self.assertEqual(summary["success_candidate_count"], 7)
        self.assertEqual(summary["overheat_count"], 2)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["stage4b_case_count"], 3)
        self.assertEqual(summary["stage4c_case_count"], 1)
        self.assertEqual(summary["green_possible_count"], 4)
        self.assertEqual(summary["watch_yellow_first_count"], 11)
        self.assertEqual(summary["redteam_first_count"], 2)
        self.assertEqual(summary["hard_gate_target_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("R2 Loop 3", summary_md)
        self.assertIn("Do not apply R2 Loop-3 v3.0 weights", guardrails)
        self.assertIn("OpenAI contract", overlays)
        self.assertIn("supermicro_ey_resignation_case", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round68_r2_loop3_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r2_loop3_round68.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round68_r2_loop3_v3.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["stage_date_plan"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["loop3_risk_overlays"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertTrue(paths["price_fields"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND68_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round68_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round68_r2_loop3_ai_semiconductor", text)


if __name__ == "__main__":
    unittest.main()
