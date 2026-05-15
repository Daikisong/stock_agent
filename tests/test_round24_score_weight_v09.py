import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round24_score_weight_report import build_parser
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10ThemePosture
from e2r.sector.round24_score_weight_v09 import (
    ROUND24_CASE_CANDIDATES,
    ROUND24_SCORE_TARGETS,
    render_round24_risk_boundary_markdown,
    render_round24_summary_markdown,
    round24_case_records,
    round24_score_profile_rows,
    round24_summary,
    target_for,
    write_round24_score_weight_reports,
)


class Round24ScoreWeightV09Tests(unittest.TestCase):
    def test_round24_targets_include_v09_calibration_families(self):
        labels = {target.target_id for target in ROUND24_SCORE_TARGETS}

        self.assertIn("RAIL_INFRASTRUCTURE", labels)
        self.assertIn("CLOUD_AI_SOFTWARE_INFRA", labels)
        self.assertIn("CRO_CLINICAL_SERVICE", labels)
        self.assertIn("RETAIL_ECOMMERCE_LOGISTICS", labels)
        self.assertIn("SOLAR_TARIFF_SUPPLYCHAIN", labels)
        self.assertIn("INSURANCE_UNDERWRITING_CYCLE", labels)
        self.assertIn("DIGITAL_HEALTHCARE_AI", labels)
        self.assertIn("SECURITY_IDENTITY_DEEPFAKE", labels)
        self.assertIn("BATTERY_RECYCLING_ESS_SHIFT", labels)
        self.assertIn("SECURITIES_BROKERAGE_CYCLE", labels)

    def test_rail_requires_contract_delivery_margin_and_financing_evidence(self):
        target = target_for("RAIL_INFRASTRUCTURE")
        records = {record.case_id: record for record in round24_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("signed_contract", target.green_conditions)
        self.assertIn("delivery_schedule", target.green_conditions)
        self.assertIn("margin_visibility", target.green_conditions)
        self.assertIn("financing_risk_low", target.green_conditions)
        self.assertEqual(records["reconstruction_rail_theme_event_watch"].case_type, "event_premium")
        self.assertIn("no_delivery_schedule", records["reconstruction_rail_theme_event_watch"].red_flag_fields)

    def test_cloud_saas_is_green_possible_but_ai_feature_alone_is_blocked(self):
        target = target_for("CLOUD_AI_SOFTWARE_INFRA")
        records = {record.case_id: record for record in round24_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("recurring_revenue", target.green_conditions)
        self.assertIn("ai_cost_control", target.green_conditions)
        self.assertIn("ai_feature_only", target.red_flags)
        self.assertEqual(records["ai_feature_no_fcf_counterexample"].case_type, "failed_rerating")
        self.assertIn("no_fcf", records["ai_feature_no_fcf_counterexample"].red_flag_fields)

    def test_cro_is_watch_first_and_funding_cycle_sensitive(self):
        target = target_for("CRO_CLINICAL_SERVICE")
        records = {record.case_id: record for record in round24_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("funding_cycle_stable", target.green_conditions)
        self.assertIn("biotech_funding_cycle_down", target.red_flags)
        self.assertEqual(records["charles_river_funding_crunch_4c"].case_type, "4c_thesis_break")
        self.assertIn("forecast_cut", records["charles_river_funding_crunch_4c"].red_flag_fields)

    def test_solar_battery_and_ecommerce_stay_watch_first(self):
        for target_id in (
            "SOLAR_TARIFF_SUPPLYCHAIN",
            "BATTERY_RECYCLING_ESS_SHIFT",
            "RETAIL_ECOMMERCE_LOGISTICS",
            "SECURITIES_BROKERAGE_CYCLE",
        ):
            target = target_for(target_id)
            self.assertIsNotNone(target)
            assert target is not None
            self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)

        solar = target_for("SOLAR_TARIFF_SUPPLYCHAIN")
        assert solar is not None
        self.assertIn("customs", solar.red_flags)
        self.assertIn("component_delay", solar.stage4c_conditions)

    def test_insurance_and_security_are_green_possible_with_hard_risk_gates(self):
        insurance = target_for("INSURANCE_UNDERWRITING_CYCLE")
        security = target_for("SECURITY_IDENTITY_DEEPFAKE")
        markdown = render_round24_risk_boundary_markdown()

        self.assertIsNotNone(insurance)
        self.assertIsNotNone(security)
        assert insurance is not None
        assert security is not None
        self.assertEqual(insurance.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(security.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("shareholder_return_execution", insurance.green_conditions)
        self.assertIn("no_major_outage", security.green_conditions)
        self.assertIn("major_outage", security.stage4c_conditions)
        self.assertIn("hard 4C", markdown)

    def test_digital_healthcare_ai_requires_paid_workflow_not_poc_only(self):
        target = target_for("DIGITAL_HEALTHCARE_AI")
        records = {record.case_id: record for record in round24_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertEqual(target.score_weight.information_confidence, 7)
        self.assertIn("reimbursement_or_paid_usage", target.green_conditions)
        self.assertEqual(records["hospital_ai_poc_no_revenue_counterexample"].case_type, "failed_rerating")
        self.assertIn("poc_only", records["hospital_ai_poc_no_revenue_counterexample"].red_flag_fields)

    def test_case_records_validate_and_keep_backfill_open(self):
        records = round24_case_records()

        self.assertEqual(len(records), len(ROUND24_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.price_validation.price_validation_status, "needs_price_backfill")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_change_production_scoring", record.green_guardrails)

    def test_score_profile_rows_mark_no_production_change(self):
        for row in round24_score_profile_rows():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_summary_reports_v09_not_production_scoring(self):
        summary = round24_summary()
        markdown = render_round24_summary_markdown()

        self.assertEqual(summary["target_count"], 10)
        self.assertEqual(summary["case_candidate_count"], 40)
        self.assertEqual(summary["success_candidate_count"], 14)
        self.assertEqual(summary["stage4c_case_count"], 9)
        self.assertEqual(summary["green_possible_count"], 4)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("production_scoring_changed: false", markdown)
        self.assertIn("Theme names, case IDs, policies, PoCs, and revenue growth headlines are not score evidence", markdown)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round24_score_weight_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_v06_round24.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round24_v09.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["risk_boundary"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND24_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round24_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round24_score_weight_v09", text)


if __name__ == "__main__":
    unittest.main()
