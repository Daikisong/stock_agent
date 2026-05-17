import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round55_r2_loop2_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round55_r2_loop2_ai_semiconductor import (
    ROUND55_CASE_CANDIDATES,
    ROUND55_PRICE_FIELDS,
    ROUND55_SCORE_TARGETS,
    render_round55_green_guardrail_markdown,
    render_round55_price_validation_plan_markdown,
    render_round55_risk_overlay_markdown,
    render_round55_summary_markdown,
    round55_case_candidate_rows,
    round55_case_records,
    round55_price_field_rows,
    round55_score_profile_rows,
    round55_stage_date_rows,
    round55_summary,
    target_for,
    write_round55_r2_loop2_reports,
)


class Round55R2Loop2AISemiconductorTests(unittest.TestCase):
    def test_round55_targets_cover_loop2_ai_semiconductor_archetypes(self):
        labels = {target.target_id for target in ROUND55_SCORE_TARGETS}

        self.assertEqual(len(labels), 18)
        for label in (
            "MEMORY_HBM_CAPACITY",
            "COMMODITY_MEMORY_GENERAL_SEMI",
            "SEMI_EQUIPMENT_CAPEX",
            "SEMI_MATERIALS_PROCESS",
            "ADVANCED_PACKAGING_PCB",
            "ADVANCED_PACKAGING_COWOS_EMIB",
            "AI_SERVER_ODM_EMS_SUPPLY_CHAIN",
            "NEOCLOUD_GPU_RENTAL",
            "OPTICAL_NETWORKING_AI_DATACENTER",
            "AI_DATA_CENTER_COOLING",
            "REDTEAM_ACCOUNTING_TRUST_OVERLAY",
        ):
            self.assertIn(label, labels)
        for target in ROUND55_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS)
            self.assertFalse(target.production_scoring_changed)

    def test_new_loop2_canonical_archetypes_exist(self):
        expected = (
            E2RArchetype.COMMODITY_MEMORY_GENERAL_SEMI,
            E2RArchetype.SEMI_MATERIALS_PROCESS,
            E2RArchetype.ADVANCED_PACKAGING_PCB,
            E2RArchetype.ADVANCED_PACKAGING_COWOS_EMIB,
            E2RArchetype.AI_SERVER_ODM_EMS_SUPPLY_CHAIN,
            E2RArchetype.NEOCLOUD_GPU_RENTAL,
            E2RArchetype.OPTICAL_NETWORKING_AI_DATACENTER,
            E2RArchetype.INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA,
            E2RArchetype.AI_DATA_CENTER_COOLING,
            E2RArchetype.REDTEAM_ACCOUNTING_TRUST_OVERLAY,
        )

        for archetype in expected:
            self.assertIsInstance(archetype.value, str)

    def test_hbm_cowos_optical_and_cooling_are_green_possible_with_specific_guards(self):
        hbm = target_for("MEMORY_HBM_CAPACITY")
        cowos = target_for("ADVANCED_PACKAGING_COWOS_EMIB")
        optical = target_for("OPTICAL_NETWORKING_AI_DATACENTER")
        cooling = target_for("AI_DATA_CENTER_COOLING")

        for target in (hbm, cowos, optical, cooling):
            self.assertIsNotNone(target)
            assert target is not None
            self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        assert hbm is not None
        self.assertEqual(hbm.score_weight.eps_fcf, 24)
        self.assertEqual(hbm.score_weight.structural_visibility, 21)
        self.assertEqual(hbm.score_weight.bottleneck_pricing, 19)
        self.assertEqual(hbm.score_weight.market_mispricing, 14)
        self.assertEqual(hbm.score_weight.valuation, 11)
        self.assertIn("customer_price_resistance", hbm.red_flags)
        assert cowos is not None
        self.assertIn("bottleneck_normalization", cowos.loop2_penalty_axes)
        assert optical is not None
        self.assertIn("hyperscaler_contract", optical.green_conditions)
        assert cooling is not None
        self.assertIn("mna_overpay", cooling.loop2_penalty_axes)

    def test_watch_targets_are_not_hbm_style_green_by_default(self):
        neocloud = target_for("NEOCLOUD_GPU_RENTAL")
        ai_server = target_for("AI_SERVER_ODM_EMS_SUPPLY_CHAIN")
        pureplay = target_for("AI_ACCELERATOR_CHIP_PUREPLAY")
        commodity = target_for("COMMODITY_MEMORY_GENERAL_SEMI")

        for target in (neocloud, ai_server, pureplay, commodity):
            self.assertIsNotNone(target)
            assert target is not None
            self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        assert neocloud is not None
        self.assertIn("high_debt", neocloud.red_flags)
        self.assertIn("fcf_negative", neocloud.red_flags)
        assert ai_server is not None
        self.assertIn("low_margin", ai_server.red_flags)
        self.assertIn("accounting_issue", ai_server.red_flags)
        assert pureplay is not None
        self.assertIn("no_revenue", pureplay.red_flags)

    def test_accounting_trust_overlay_is_gate_only_redteam(self):
        overlay = target_for("REDTEAM_ACCOUNTING_TRUST_OVERLAY")

        self.assertIsNotNone(overlay)
        assert overlay is not None
        self.assertEqual(overlay.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertTrue(overlay.gate_only)
        self.assertEqual(overlay.score_weight.eps_fcf, "gate")
        self.assertIn("auditor_resignation", overlay.red_flags)
        self.assertIn("filing_delay", overlay.red_flags)
        self.assertIn("internal_control_weakness", overlay.red_flags)

    def test_required_round55_cases_are_present_with_stage_markers(self):
        rows = {row["case_id"]: row for row in round55_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND55_CASE_CANDIDATES))
        self.assertEqual(rows["sk_hynix_hbm_rerating_success_case"]["stage2_date"], "2026-05-14")
        self.assertEqual(rows["sk_hynix_hbm_rerating_success_case"]["stage3_date"], "2026-05-14")
        self.assertEqual(rows["sk_hynix_hbm_rerating_success_case"]["stage4b_date"], "2026-05-14")
        self.assertEqual(rows["applied_materials_ai_packaging_growth_case"]["stage2_date"], "2026-05-14")
        self.assertEqual(rows["nvidia_cowos_l_transition_case"]["stage2_date"], "2025-01-16")
        self.assertEqual(rows["broadcom_optical_pcb_leadtime_case"]["stage2_date"], "2026-03-24")
        self.assertEqual(rows["foxconn_ai_server_rack_growth_case"]["stage2_date"], "2026-05-14")
        self.assertEqual(rows["ecolab_coolit_liquid_cooling_case"]["stage2_date"], "2026-03-20")
        self.assertEqual(rows["coreweave_openai_contract_ipo_case"]["stage2_date"], "2025-03-20")
        self.assertEqual(rows["supermicro_ey_resignation_case"]["stage4c_date"], "2024-10-30")
        self.assertEqual(rows["cxl_glass_substrate_theme_case"]["case_type"], "overheat")

    def test_case_records_validate_and_keep_loop2_guardrails(self):
        records = round55_case_records()

        self.assertEqual(len(records), len(ROUND55_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_change_production_scoring", record.green_guardrails)
            self.assertIn("hbm_is_not_same_as_all_ai_semiconductor", record.green_guardrails)
            self.assertIn("do_not_invent_contract_prices_margins_or_stage_prices", record.green_guardrails)
        by_id = {record.case_id: record for record in records}
        self.assertEqual(by_id["sk_hynix_hbm_rerating_success_case"].rerating_result, "true_rerating")
        self.assertEqual(by_id["coreweave_downsized_ipo_debt_case"].score_price_alignment, "evidence_good_but_price_failed")
        self.assertEqual(by_id["supermicro_ey_resignation_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["cxl_glass_substrate_theme_case"].score_price_alignment, "price_moved_without_evidence")

    def test_score_profile_rows_match_round55_weight_table(self):
        rows = {row["target_id"]: row for row in round55_score_profile_rows()}

        self.assertEqual(rows["MEMORY_HBM_CAPACITY"]["eps_fcf"], "24")
        self.assertEqual(rows["MEMORY_HBM_CAPACITY"]["market_mispricing"], "14")
        self.assertEqual(rows["MEMORY_HBM_CAPACITY"]["valuation"], "11")
        self.assertEqual(rows["NEOCLOUD_GPU_RENTAL"]["valuation"], "9")
        self.assertEqual(rows["AI_SERVER_ODM_EMS_SUPPLY_CHAIN"]["structural_visibility"], "18")
        self.assertEqual(rows["AI_SERVER_ODM_EMS_SUPPLY_CHAIN"]["valuation"], "10")
        self.assertEqual(rows["REDTEAM_ACCOUNTING_TRUST_OVERLAY"]["gate_only"], "true")
        self.assertEqual(rows["REDTEAM_ACCOUNTING_TRUST_OVERLAY"]["eps_fcf"], "gate")
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round55_stage_date_rows()}
        fields = {row["field"] for row in round55_price_field_rows()}

        self.assertIn("crowded_hbm_consensus", rows["MEMORY_HBM_CAPACITY"]["stage4b"])
        self.assertIn("refinancing_pressure", rows["NEOCLOUD_GPU_RENTAL"]["stage4c"])
        self.assertIn("auditor_resignation", rows["REDTEAM_ACCOUNTING_TRUST_OVERLAY"]["stage4c"])
        for field in (
            "hbm_revenue_share",
            "hbm_price_band_flag",
            "equipment_order_growth",
            "packaging_revenue_growth",
            "pcb_lead_time_weeks",
            "ai_server_margin",
            "gpu_depreciation",
            "mna_debt_financing_flag",
            "auditor_resignation_flag",
            "labor_strike_flag",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND55_PRICE_FIELDS))

    def test_summary_and_markdown_explain_loop2_ai_distinctions(self):
        summary = round55_summary()
        summary_md = render_round55_summary_markdown()
        guardrails = render_round55_green_guardrail_markdown()
        overlays = render_round55_risk_overlay_markdown()
        price_plan = render_round55_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 18)
        self.assertEqual(summary["case_candidate_count"], 12)
        self.assertEqual(summary["structural_success_count"], 1)
        self.assertEqual(summary["success_candidate_count"], 5)
        self.assertEqual(summary["cyclical_success_count"], 1)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["stage4b_case_count"], 2)
        self.assertEqual(summary["stage4c_case_count"], 1)
        self.assertEqual(summary["green_possible_count"], 4)
        self.assertEqual(summary["redteam_first_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("R2 Loop 2", summary_md)
        self.assertIn("Do not apply R2 Loop-2 v2.0 weights", guardrails)
        self.assertIn("OpenAI contract", overlays)
        self.assertIn("supermicro_ey_resignation_case", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round55_r2_loop2_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r2_loop2_round55.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round55_r2_loop2_v2.csv",
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
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND55_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round55_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round55_r2_loop2_ai_semiconductor", text)


if __name__ == "__main__":
    unittest.main()
