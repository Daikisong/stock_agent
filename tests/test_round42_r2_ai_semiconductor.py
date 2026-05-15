import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round42_r2_report import build_parser
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round42_r2_ai_semiconductor import (
    ROUND42_CASE_CANDIDATES,
    ROUND42_PRICE_FIELDS,
    ROUND42_SCORE_TARGETS,
    render_round42_green_guardrail_markdown,
    render_round42_price_validation_plan_markdown,
    render_round42_summary_markdown,
    round42_case_candidate_rows,
    round42_case_records,
    round42_price_field_rows,
    round42_score_profile_rows,
    round42_stage_date_rows,
    round42_summary,
    target_for,
    write_round42_r2_reports,
)


class Round42R2AISemiconductorTests(unittest.TestCase):
    def test_round42_targets_cover_r2_archetypes(self):
        labels = {target.target_id for target in ROUND42_SCORE_TARGETS}

        self.assertEqual(len(labels), 18)
        self.assertIn("MEMORY_HBM_CAPACITY", labels)
        self.assertIn("COMMODITY_MEMORY_GENERAL_SEMI", labels)
        self.assertIn("ADVANCED_PACKAGING_COWOS_EMIB", labels)
        self.assertIn("OPTICAL_NETWORKING_AI_DATACENTER", labels)
        self.assertIn("AI_DATA_CENTER_COOLING", labels)
        self.assertIn("REDTEAM_ACCOUNTING_TRUST_OVERLAY", labels)
        for target in ROUND42_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS)
            self.assertFalse(target.production_scoring_changed)

    def test_hbm_optical_and_cooling_are_green_possible_with_specific_guards(self):
        hbm = target_for("MEMORY_HBM_CAPACITY")
        optical = target_for("OPTICAL_NETWORKING_AI_DATACENTER")
        cooling = target_for("AI_DATA_CENTER_COOLING")

        self.assertIsNotNone(hbm)
        self.assertIsNotNone(optical)
        self.assertIsNotNone(cooling)
        assert hbm is not None
        assert optical is not None
        assert cooling is not None
        self.assertEqual(hbm.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(hbm.score_weight.eps_fcf, 24)
        self.assertEqual(hbm.score_weight.bottleneck_pricing, 19)
        self.assertIn("multi_year_eps_revision", hbm.green_conditions)
        self.assertIn("customer_price_resistance", hbm.red_flags)
        self.assertEqual(optical.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("hyperscaler_contract", optical.green_conditions)
        self.assertEqual(cooling.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("thermal_bottleneck", cooling.green_conditions)

    def test_neocloud_and_ai_chip_are_watch_not_green(self):
        neocloud = target_for("NEOCLOUD_GPU_RENTAL")
        ai_chip = target_for("AI_CHIP_FABRIC_INFRA")

        self.assertIsNotNone(neocloud)
        self.assertIsNotNone(ai_chip)
        assert neocloud is not None
        assert ai_chip is not None
        self.assertEqual(neocloud.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("high_debt", neocloud.red_flags)
        self.assertIn("fcf_negative", neocloud.red_flags)
        self.assertEqual(ai_chip.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("no_revenue", ai_chip.red_flags)

    def test_accounting_trust_overlay_is_hard_redteam_gate(self):
        overlay = target_for("REDTEAM_ACCOUNTING_TRUST_OVERLAY")

        self.assertIsNotNone(overlay)
        assert overlay is not None
        self.assertEqual(overlay.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertTrue(overlay.gate_only)
        self.assertEqual(overlay.score_weight.eps_fcf, 0)
        self.assertIn("auditor_resignation", overlay.red_flags)
        self.assertIn("filing_delay", overlay.red_flags)
        self.assertIn("internal_control_weakness", overlay.red_flags)

    def test_case_records_validate_and_keep_price_backfill_open(self):
        records = round42_case_records()

        self.assertEqual(len(records), len(ROUND42_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("theme_label_is_not_score_evidence", record.green_guardrails)
            self.assertIn("hbm_is_not_same_as_all_ai_semiconductor", record.green_guardrails)

    def test_required_round42_cases_are_present_with_stage_dates(self):
        records = {record.case_id: record for record in round42_case_records()}

        self.assertIn("sk_hynix_hbm_rerating_success_case", records)
        self.assertEqual(str(records["sk_hynix_hbm_rerating_success_case"].stage2_date), "2026-05-14")
        self.assertEqual(str(records["sk_hynix_hbm_rerating_success_case"].stage4b_date), "2026-05-14")
        self.assertEqual(records["sk_hynix_hbm_rerating_success_case"].case_type, "structural_success")
        self.assertEqual(records["sk_hynix_hbm_rerating_success_case"].rerating_result, "true_rerating")
        self.assertIn("supermicro_ey_resignation_4c_case", records)
        self.assertEqual(str(records["supermicro_ey_resignation_4c_case"].stage4c_date), "2024-10-30")
        self.assertEqual(records["supermicro_ey_resignation_4c_case"].rerating_result, "thesis_break")
        self.assertEqual(records["blackstone_data_center_reit_case"].case_type, "failed_rerating")
        self.assertEqual(records["coreweave_neocloud_high_debt_case"].case_type, "4b_watch")

    def test_score_profile_rows_mark_no_production_change(self):
        rows = {row["target_id"]: row for row in round42_score_profile_rows()}

        self.assertEqual(rows["MEMORY_HBM_CAPACITY"]["large_sector"], "AI_SEMICONDUCTOR_ELECTRONICS")
        self.assertEqual(rows["MEMORY_HBM_CAPACITY"]["production_scoring_changed"], "false")
        self.assertIn("stage4c_conditions", rows["MEMORY_HBM_CAPACITY"])
        self.assertEqual(rows["REDTEAM_ACCOUNTING_TRUST_OVERLAY"]["gate_only"], "true")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round42_stage_date_rows()}
        fields = {row["field"] for row in round42_price_field_rows()}

        self.assertIn("MEMORY_HBM_CAPACITY", rows)
        self.assertIn("multi_year_eps_revision", rows["MEMORY_HBM_CAPACITY"]["stage3"])
        for field in (
            "stage2_price",
            "MFE_180D",
            "customer_concentration",
            "auditor_resignation",
            "fcf_margin",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND42_PRICE_FIELDS))

    def test_summary_and_markdown_explain_r2_guardrails(self):
        summary = round42_summary()
        summary_md = render_round42_summary_markdown()
        guardrails = render_round42_green_guardrail_markdown()
        price_plan = render_round42_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 18)
        self.assertEqual(summary["case_candidate_count"], 18)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("R2 must not score every AI tag equally", summary_md)
        self.assertIn("Do not apply these R2 v1.0 weights", guardrails)
        self.assertIn("sk_hynix_hbm_rerating_success_case", price_plan)
        self.assertIn("supermicro_ey_resignation_4c_case", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round42_r2_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r2_round42.jsonl",
                score_profile_path=Path(tmp) / "score_profiles.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["stage_date_plan"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertTrue(paths["price_fields"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND42_CASE_CANDIDATES))

    def test_case_matrix_records_are_not_production_inputs(self):
        rows = round42_case_candidate_rows()

        self.assertTrue(rows)
        for row in rows:
            self.assertEqual(row["production_input"], "false")

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

    def test_production_scoring_modules_do_not_import_round42_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round42_r2_ai_semiconductor", text)


if __name__ == "__main__":
    unittest.main()
