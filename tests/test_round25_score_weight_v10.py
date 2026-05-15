import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round25_score_weight_report import build_parser
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10ThemePosture
from e2r.sector.round25_score_weight_v10 import (
    ROUND25_CASE_CANDIDATES,
    ROUND25_SCORE_TARGETS,
    render_round25_stage4b_watch_markdown,
    render_round25_summary_markdown,
    round25_case_records,
    round25_score_profile_rows,
    round25_summary,
    target_for,
    write_round25_score_weight_reports,
)


class Round25ScoreWeightV10Tests(unittest.TestCase):
    def test_round25_targets_include_v10_calibration_families(self):
        labels = {target.target_id for target in ROUND25_SCORE_TARGETS}

        self.assertIn("AI_DATA_CENTER_COOLING", labels)
        self.assertIn("SECURITY_IDENTITY_DEEPFAKE", labels)
        self.assertIn("CRO_CLINICAL_SERVICE", labels)
        self.assertIn("SOLAR_TARIFF_SUPPLYCHAIN", labels)
        self.assertIn("RETAIL_ECOMMERCE_LOGISTICS", labels)
        self.assertIn("INSURANCE_UNDERWRITING_CYCLE", labels)
        self.assertIn("DIGITAL_HEALTHCARE_AI", labels)
        self.assertIn("BATTERY_RECYCLING_ESS_SHIFT", labels)
        self.assertIn("SECURITIES_BROKERAGE_CYCLE", labels)
        self.assertIn("MEMORY_HBM_CAPACITY", labels)

    def test_ai_cooling_is_green_possible_but_order_and_service_required(self):
        target = target_for("AI_DATA_CENTER_COOLING")
        records = {record.case_id: record for record in round25_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(target.score_weight.bottleneck_pricing, 22)
        self.assertIn("confirmed_order_or_delivery", target.green_conditions)
        self.assertIn("repeat_service_revenue", target.green_conditions)
        self.assertIn("liquid_cooling_theme_only", target.red_flags)
        self.assertEqual(records["liquid_cooling_theme_no_order_counterexample"].case_type, "failed_rerating")
        self.assertIn("no_customer_order", records["liquid_cooling_theme_no_order_counterexample"].red_flag_fields)

    def test_security_outage_is_hard_4c_boundary(self):
        target = target_for("SECURITY_IDENTITY_DEEPFAKE")
        records = {record.case_id: record for record in round25_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("no_major_outage", target.green_conditions)
        self.assertIn("major_outage", target.stage4c_conditions)
        self.assertEqual(records["crowdstrike_outage_4c"].case_type, "4c_thesis_break")
        self.assertIn("legal_claim", records["crowdstrike_outage_4c"].red_flag_fields)

    def test_watch_first_targets_keep_cycle_and_policy_risks(self):
        for target_id in (
            "CRO_CLINICAL_SERVICE",
            "SOLAR_TARIFF_SUPPLYCHAIN",
            "RETAIL_ECOMMERCE_LOGISTICS",
            "DIGITAL_HEALTHCARE_AI",
            "BATTERY_RECYCLING_ESS_SHIFT",
            "SECURITIES_BROKERAGE_CYCLE",
        ):
            target = target_for(target_id)
            self.assertIsNotNone(target)
            assert target is not None
            self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)

        cro = target_for("CRO_CLINICAL_SERVICE")
        solar = target_for("SOLAR_TARIFF_SUPPLYCHAIN")
        assert cro is not None
        assert solar is not None
        self.assertIn("biotech_funding_cycle_down", cro.red_flags)
        self.assertIn("customs", solar.red_flags)

    def test_insurance_is_pbr_roe_return_not_eps_explosion(self):
        target = target_for("INSURANCE_UNDERWRITING_CYCLE")

        self.assertIsNotNone(target)
        assert target is not None
        weights = target.score_weight.as_dict()
        self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(weights["valuation"], 25)
        self.assertEqual(weights["capital_allocation"], 10)
        self.assertIn("shareholder_return_execution", target.green_conditions)
        self.assertIn("low_pbr_only", target.red_flags)

    def test_hbm_has_success_case_and_4b_crowding_watch(self):
        target = target_for("MEMORY_HBM_CAPACITY")
        records = {record.case_id: record for record in round25_case_records()}
        markdown = render_round25_stage4b_watch_markdown()

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("global_crowding", target.stage4b_conditions)
        self.assertIn("market_cap_multiple_saturation", target.stage4b_conditions)
        self.assertEqual(records["sk_hynix_hbm_success_case"].case_type, "structural_success")
        self.assertEqual(records["sk_hynix_4b_crowding_watch"].case_type, "4b_watch")
        self.assertIn("price_only_4b_watch", markdown)

    def test_case_records_validate_and_keep_backfill_open(self):
        records = round25_case_records()

        self.assertEqual(len(records), len(ROUND25_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.price_validation.price_validation_status, "needs_price_backfill")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_change_production_scoring", record.green_guardrails)

    def test_score_profile_rows_mark_no_production_change(self):
        for row in round25_score_profile_rows():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_summary_reports_v10_not_production_scoring(self):
        summary = round25_summary()
        markdown = render_round25_summary_markdown()

        self.assertEqual(summary["target_count"], 10)
        self.assertEqual(summary["case_candidate_count"], 40)
        self.assertEqual(summary["success_candidate_count"], 15)
        self.assertEqual(summary["stage4b_case_count"], 1)
        self.assertEqual(summary["stage4c_case_count"], 9)
        self.assertEqual(summary["green_possible_count"], 4)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("production_scoring_changed: false", markdown)
        self.assertIn("Theme names, case IDs, policies, PoCs, and revenue growth headlines are not score evidence", markdown)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round25_score_weight_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_v07_round25.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round25_v10.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["stage4b_watch"].exists())
            self.assertTrue(paths["risk_boundary"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND25_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round25_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round25_score_weight_v10", text)


if __name__ == "__main__":
    unittest.main()
