import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round23_score_weight_report import build_parser
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10ThemePosture
from e2r.sector.round23_score_weight_v08 import (
    ROUND23_CASE_CANDIDATES,
    ROUND23_SCORE_TARGETS,
    render_round23_stage4b_watch_markdown,
    render_round23_summary_markdown,
    round23_case_records,
    round23_score_profile_rows,
    round23_summary,
    target_for,
    write_round23_score_weight_reports,
)


class Round23ScoreWeightV08Tests(unittest.TestCase):
    def test_round23_targets_include_thin_archetype_and_recalibration_families(self):
        labels = {target.target_id for target in ROUND23_SCORE_TARGETS}

        self.assertIn("DIGITAL_HEALTHCARE_AI", labels)
        self.assertIn("TELECOM_5G_6G_AI_NETWORK", labels)
        self.assertIn("MEDIA_AD_CONTENT_CYCLE", labels)
        self.assertIn("SERVICE_KIOSK_AUTOMATION", labels)
        self.assertIn("SMART_FARM_AGRI_TECH", labels)
        self.assertIn("HOME_LIVING_APPLIANCE", labels)
        self.assertIn("CONSUMER_REGULATED_PRODUCT", labels)
        self.assertIn("MEMORY_HBM_CAPACITY", labels)
        self.assertIn("AI_DATA_CENTER_INFRASTRUCTURE", labels)

    def test_medical_ai_is_watch_first_until_paid_adoption_and_validation(self):
        target = target_for("DIGITAL_HEALTHCARE_AI")

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertEqual(target.score_weight.information_confidence, 7)
        self.assertIn("reimbursement_or_paid_usage", target.green_conditions)
        self.assertIn("external_clinical_validation", target.green_conditions)
        self.assertIn("no_reimbursement", target.red_flags)
        self.assertIn("overtrust_risk", target.red_flags)

    def test_telecom_policy_is_routing_evidence_not_green_evidence(self):
        target = target_for("TELECOM_5G_6G_AI_NETWORK")
        records = {record.case_id: record for record in round23_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("no_revenue_conversion", target.red_flags)
        self.assertIn("capex_burden", target.red_flags)
        self.assertEqual(records["6g_policy_no_revenue_watch"].case_type, "event_premium")
        self.assertIn("policy_theme_only", records["6g_policy_no_revenue_watch"].red_flag_fields)

    def test_watch_first_targets_keep_theme_and_oneoff_guardrails(self):
        for target_id in (
            "MEDIA_AD_CONTENT_CYCLE",
            "SERVICE_KIOSK_AUTOMATION",
            "HOME_LIVING_APPLIANCE",
            "CONSUMER_REGULATED_PRODUCT",
        ):
            target = target_for(target_id)
            self.assertIsNotNone(target)
            assert target is not None
            self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
            self.assertGreater(len(target.red_flags), 0)

        service_target = target_for("SERVICE_KIOSK_AUTOMATION")
        assert service_target is not None
        self.assertIn("maintenance_or_saas_revenue", service_target.green_conditions)
        self.assertIn("one_off_hardware_sales", service_target.red_flags)

    def test_hbm_and_ai_data_center_remain_green_possible_with_4b_watch(self):
        hbm = target_for("MEMORY_HBM_CAPACITY")
        ai_dc = target_for("AI_DATA_CENTER_INFRASTRUCTURE")
        markdown = render_round23_stage4b_watch_markdown()

        self.assertIsNotNone(hbm)
        self.assertIsNotNone(ai_dc)
        assert hbm is not None
        assert ai_dc is not None
        self.assertEqual(hbm.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(ai_dc.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("global_hardware_crowding", hbm.stage4b_conditions)
        self.assertIn("orders_fully_priced", ai_dc.stage4b_conditions)
        self.assertIn("price_only_4b_watch", markdown)

    def test_case_records_validate_and_keep_backfill_open(self):
        records = round23_case_records()

        self.assertEqual(len(records), len(ROUND23_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.price_validation.price_validation_status, "needs_price_backfill")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_change_production_scoring", record.green_guardrails)

    def test_score_profile_rows_mark_no_production_change(self):
        for row in round23_score_profile_rows():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_summary_reports_v08_not_production_scoring(self):
        summary = round23_summary()
        markdown = render_round23_summary_markdown()

        self.assertEqual(summary["target_count"], 9)
        self.assertEqual(summary["case_candidate_count"], 28)
        self.assertEqual(summary["success_candidate_count"], 12)
        self.assertEqual(summary["green_possible_count"], 2)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("production_scoring_changed: false", markdown)
        self.assertIn("Theme names, case IDs, papers, PoCs, and policy headlines are not score evidence", markdown)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round23_score_weight_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_v05_round23.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round23_v08.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertTrue(paths["stage4b_watch_review"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND23_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round23_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round23_score_weight_v08", text)


if __name__ == "__main__":
    unittest.main()
