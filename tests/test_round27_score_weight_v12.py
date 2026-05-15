import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round27_score_weight_report import build_parser
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10ThemePosture
from e2r.sector.round27_score_weight_v12 import (
    ROUND27_CASE_CANDIDATES,
    ROUND27_SCORE_TARGETS,
    render_round27_false_success_boundary_markdown,
    render_round27_summary_markdown,
    round27_case_records,
    round27_score_profile_rows,
    round27_summary,
    target_for,
    write_round27_score_weight_reports,
)


class Round27ScoreWeightV12Tests(unittest.TestCase):
    def test_round27_targets_include_v12_calibration_families(self):
        labels = {target.target_id for target in ROUND27_SCORE_TARGETS}

        self.assertIn("GAME_CONTENT_IP", labels)
        self.assertIn("MEDICAL_DEVICE_HEALTHCARE_EXPORT", labels)
        self.assertIn("DIGITAL_HEALTHCARE_AI", labels)
        self.assertIn("RETAIL_ECOMMERCE_LOGISTICS", labels)
        self.assertIn("EDUCATION_SPECIALTY_SERVICES", labels)
        self.assertIn("TELECOM_GRID_AI_NETWORK", labels)
        self.assertIn("AI_DATA_CENTER_COOLING", labels)
        self.assertIn("SECURITY_IDENTITY_DEEPFAKE", labels)
        self.assertIn("CLOUD_AI_SOFTWARE_INFRA", labels)
        self.assertIn("INSURANCE_UNDERWRITING_CYCLE", labels)

    def test_game_ip_is_watch_first_and_downloads_are_not_green_evidence(self):
        target = target_for("GAME_CONTENT_IP")
        records = {record.case_id: record for record in round27_case_records()}
        markdown = render_round27_false_success_boundary_markdown()

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("monetization_confirmed", target.green_conditions)
        self.assertIn("data_security", target.red_flags)
        self.assertIn("single_ip_dependency", target.red_flags)
        self.assertEqual(records["new_game_hype_no_revenue_counterexample"].case_type, "failed_rerating")
        self.assertEqual(records["single_ip_dependency_4c"].case_type, "4c_thesis_break")
        self.assertIn("downloads or new-game hype must not become Green", markdown)

    def test_medical_device_can_be_green_but_safety_and_recurring_revenue_are_gates(self):
        target = target_for("MEDICAL_DEVICE_HEALTHCARE_EXPORT")
        records = {record.case_id: record for record in round27_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("recurring_consumables_or_procedure", target.green_conditions)
        self.assertIn("approval_stable", target.green_conditions)
        self.assertIn("counterfeit", target.red_flags)
        self.assertEqual(records["botox_counterfeit_safety_risk_4c"].case_type, "4c_thesis_break")
        self.assertEqual(records["single_device_no_consumable_counterexample"].case_type, "failed_rerating")

    def test_medical_ai_requires_paid_workflow_not_paper_only(self):
        target = target_for("DIGITAL_HEALTHCARE_AI")
        records = {record.case_id: record for record in round27_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertEqual(target.score_weight.information_confidence, 7)
        self.assertIn("reimbursement_or_paid_usage", target.green_conditions)
        self.assertIn("subgroup_bias", target.red_flags)
        self.assertEqual(records["lunit_subgroup_performance_risk_counterexample"].case_type, "failed_rerating")
        self.assertEqual(records["medical_ai_liability_risk_4c"].case_type, "4c_thesis_break")

    def test_retail_education_and_grid_are_watch_first_with_false_success_risks(self):
        for target_id in (
            "RETAIL_ECOMMERCE_LOGISTICS",
            "EDUCATION_SPECIALTY_SERVICES",
            "TELECOM_GRID_AI_NETWORK",
        ):
            target = target_for(target_id)
            self.assertIsNotNone(target)
            assert target is not None
            self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)

        retail = target_for("RETAIL_ECOMMERCE_LOGISTICS")
        education = target_for("EDUCATION_SPECIALTY_SERVICES")
        grid = target_for("TELECOM_GRID_AI_NETWORK")
        assert retail is not None
        assert education is not None
        assert grid is not None
        self.assertIn("supplier_regulation", retail.red_flags)
        self.assertIn("data_security", retail.red_flags)
        self.assertIn("birthrate", education.red_flags)
        self.assertIn("offline_fixed_cost", education.red_flags)
        self.assertIn("policy_keyword_only", grid.red_flags)
        self.assertIn("capex_burden", grid.red_flags)

    def test_existing_green_possible_priorities_remain_strict(self):
        for target_id in (
            "AI_DATA_CENTER_COOLING",
            "SECURITY_IDENTITY_DEEPFAKE",
            "CLOUD_AI_SOFTWARE_INFRA",
            "INSURANCE_UNDERWRITING_CYCLE",
        ):
            target = target_for(target_id)
            self.assertIsNotNone(target)
            assert target is not None
            self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)

        insurance = target_for("INSURANCE_UNDERWRITING_CYCLE")
        cloud = target_for("CLOUD_AI_SOFTWARE_INFRA")
        assert insurance is not None
        assert cloud is not None
        self.assertEqual(insurance.score_weight.valuation, 25)
        self.assertEqual(insurance.score_weight.capital_allocation, 10)
        self.assertIn("ai_cost_control", cloud.green_conditions)
        self.assertIn("ai_feature_only", cloud.red_flags)

    def test_case_records_validate_and_keep_backfill_open(self):
        records = round27_case_records()

        self.assertEqual(len(records), len(ROUND27_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.price_validation.price_validation_status, "needs_price_backfill")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_change_production_scoring", record.green_guardrails)

    def test_score_profile_rows_mark_no_production_change(self):
        for row in round27_score_profile_rows():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_summary_reports_v12_not_production_scoring(self):
        summary = round27_summary()
        markdown = render_round27_summary_markdown()

        self.assertEqual(summary["target_count"], 10)
        self.assertEqual(summary["case_candidate_count"], 28)
        self.assertEqual(summary["success_candidate_count"], 12)
        self.assertEqual(summary["stage4b_case_count"], 0)
        self.assertEqual(summary["stage4c_case_count"], 6)
        self.assertEqual(summary["green_possible_count"], 5)
        self.assertEqual(summary["watch_yellow_first_count"], 5)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("production_scoring_changed: false", markdown)
        self.assertIn("Theme names, case IDs, policies, PoCs, and revenue growth headlines are not score evidence", markdown)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round27_score_weight_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_v09_round27.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round27_v12.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["false_success_boundary"].exists())
            self.assertTrue(paths["risk_boundary"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND27_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round27_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round27_score_weight_v12", text)


if __name__ == "__main__":
    unittest.main()
