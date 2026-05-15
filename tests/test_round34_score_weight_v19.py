import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round34_score_weight_report import build_parser
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10ThemePosture
from e2r.sector.round34_score_weight_v19 import (
    ROUND34_CASE_CANDIDATES,
    ROUND34_SCORE_TARGETS,
    render_round34_carbon_payment_markdown,
    render_round34_cycle_unit_economics_markdown,
    render_round34_optical_telecom_split_markdown,
    render_round34_summary_markdown,
    round34_case_records,
    round34_score_profile_rows,
    round34_summary,
    target_for,
    write_round34_score_weight_reports,
)


class Round34ScoreWeightV19Tests(unittest.TestCase):
    def test_round34_targets_include_v19_hard_to_score_theme_families(self):
        labels = {target.target_id for target in ROUND34_SCORE_TARGETS}

        self.assertEqual(len(labels), 8)
        self.assertIn("CARBON_CREDIT_CBAM_COMPLIANCE", labels)
        self.assertIn("PAYMENT_FINTECH_INFRA", labels)
        self.assertIn("OPTICAL_NETWORKING_AI_DATACENTER", labels)
        self.assertIn("TELECOM_5G_6G_CAPEX_CYCLE", labels)
        self.assertIn("LITHIUM_BATTERY_RAW_MATERIAL", labels)
        self.assertIn("HOME_LIVING_APPLIANCE_RENTAL", labels)
        self.assertIn("AI_ACCELERATOR_CHIP_PUREPLAY", labels)
        self.assertIn("MOBILITY_RENTAL_MICROMOBILITY", labels)

    def test_carbon_is_watch_first_and_payment_is_green_possible_with_fcf(self):
        carbon = target_for("CARBON_CREDIT_CBAM_COMPLIANCE")
        payment = target_for("PAYMENT_FINTECH_INFRA")
        markdown = render_round34_carbon_payment_markdown()
        records = {record.case_id: record for record in round34_case_records()}

        self.assertIsNotNone(carbon)
        self.assertIsNotNone(payment)
        assert carbon is not None
        assert payment is not None
        self.assertEqual(carbon.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertEqual(payment.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(carbon.score_weight.information_confidence, 6)
        self.assertIn("pass_through_possible", carbon.green_conditions)
        self.assertIn("take_rate_stable", payment.green_conditions)
        self.assertIn("user_count_only", payment.red_flags)
        self.assertEqual(records["voluntary_carbon_credit_integrity_counterexample"].case_type, "failed_rerating")
        self.assertEqual(records["stripe_profitable_payment_infra_candidate"].case_type, "success_candidate")
        self.assertIn("User count, token label, or stablecoin headline alone is not enough", markdown)

    def test_optical_ai_datacenter_is_green_possible_but_telecom_capex_is_redteam_first(self):
        optical = target_for("OPTICAL_NETWORKING_AI_DATACENTER")
        telecom = target_for("TELECOM_5G_6G_CAPEX_CYCLE")
        split = render_round34_optical_telecom_split_markdown()
        records = {record.case_id: record for record in round34_case_records()}

        self.assertIsNotNone(optical)
        self.assertIsNotNone(telecom)
        assert optical is not None
        assert telecom is not None
        self.assertEqual(optical.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(telecom.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertIn("hyperscaler_long_contract", optical.green_conditions)
        self.assertIn("valuation_crowding", optical.red_flags)
        self.assertIn("operator_delay", telecom.red_flags)
        self.assertEqual(records["meta_corning_fiber_ai_datacenter_contract_candidate"].case_type, "success_candidate")
        self.assertEqual(records["optical_stock_valuation_crowding_4b"].case_type, "4b_watch")
        self.assertEqual(records["nokia_5g_capex_slowdown_4c"].case_type, "4c_thesis_break")
        self.assertIn("must not share the same Green profile", split)

    def test_lithium_is_cycle_capped_and_home_rental_needs_subscription_revenue(self):
        lithium = target_for("LITHIUM_BATTERY_RAW_MATERIAL")
        home = target_for("HOME_LIVING_APPLIANCE_RENTAL")
        cycle_review = render_round34_cycle_unit_economics_markdown()
        records = {record.case_id: record for record in round34_case_records()}

        self.assertIsNotNone(lithium)
        self.assertIsNotNone(home)
        assert lithium is not None
        assert home is not None
        self.assertEqual(lithium.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertEqual(home.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("price_rebound_only", lithium.red_flags)
        self.assertIn("rental_subscription_revenue", home.green_conditions)
        self.assertIn("hardware_only", home.red_flags)
        self.assertEqual(records["albemarle_cost_cut_low_lithium_price_case"].case_type, "cyclical_success")
        self.assertEqual(records["whirlpool_replacement_cycle_4c"].case_type, "4c_thesis_break")
        self.assertIn("Lithium raw materials", cycle_review)

    def test_ai_accelerator_is_watch_to_green_with_validation_and_yield_gates(self):
        target = target_for("AI_ACCELERATOR_CHIP_PUREPLAY")
        records = {record.case_id: record for record in round34_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("actual_revenue", target.green_conditions)
        self.assertIn("customer_mass_production", target.green_conditions)
        self.assertIn("foundry_yield", target.red_flags)
        self.assertIn("nvidia_competition", target.red_flags)
        self.assertEqual(records["cerebras_ipo_revenue_growth_candidate"].case_type, "success_candidate")
        self.assertEqual(records["ai_chip_valuation_overheat_4b"].case_type, "4b_watch")
        self.assertEqual(records["foundry_yield_risk_4c"].case_type, "4c_thesis_break")

    def test_mobility_requires_positive_fcf_and_unit_economics(self):
        target = target_for("MOBILITY_RENTAL_MICROMOBILITY")
        records = {record.case_id: record for record in round34_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("positive_fcf", target.green_conditions)
        self.assertIn("unit_economics", target.red_flags)
        self.assertIn("maintenance_cost", target.red_flags)
        self.assertEqual(records["lime_positive_fcf_candidate"].case_type, "success_candidate")
        self.assertEqual(records["micromobility_revenue_growth_no_profit_counterexample"].case_type, "failed_rerating")
        self.assertEqual(records["city_regulation_4c"].case_type, "4c_thesis_break")

    def test_case_records_validate_and_keep_backfill_open(self):
        records = round34_case_records()

        self.assertEqual(len(records), len(ROUND34_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.price_validation.price_validation_status, "needs_price_backfill")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("theme_label_is_not_score_evidence", record.green_guardrails)

    def test_score_profile_rows_mark_no_production_change(self):
        for row in round34_score_profile_rows():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_summary_reports_v19_not_production_scoring(self):
        summary = round34_summary()
        markdown = render_round34_summary_markdown()

        self.assertEqual(summary["target_count"], 8)
        self.assertEqual(summary["case_candidate_count"], 32)
        self.assertEqual(summary["success_candidate_count"], 11)
        self.assertEqual(summary["stage4b_case_count"], 2)
        self.assertEqual(summary["stage4c_case_count"], 8)
        self.assertEqual(summary["green_possible_count"], 3)
        self.assertEqual(summary["watch_yellow_first_count"], 4)
        self.assertEqual(summary["redteam_first_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("production_scoring_changed: false", markdown)
        self.assertIn("Theme names, case IDs, policy labels, CAPEX headlines, and price rallies are not score evidence", markdown)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round34_score_weight_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_v16_round34.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round34_v19.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["carbon_payment"].exists())
            self.assertTrue(paths["optical_telecom_split"].exists())
            self.assertTrue(paths["cycle_unit_economics"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND34_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round34_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round34_score_weight_v19", text)


if __name__ == "__main__":
    unittest.main()
