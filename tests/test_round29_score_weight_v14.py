import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round29_score_weight_report import build_parser
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10ThemePosture
from e2r.sector.round29_score_weight_v14 import (
    ROUND29_CASE_CANDIDATES,
    ROUND29_SCORE_TARGETS,
    render_round29_capital_allocation_markdown,
    render_round29_summary_markdown,
    round29_case_records,
    round29_score_profile_rows,
    round29_summary,
    target_for,
    write_round29_score_weight_reports,
)


class Round29ScoreWeightV14Tests(unittest.TestCase):
    def test_round29_targets_include_v14_calibration_families(self):
        labels = {target.target_id for target in ROUND29_SCORE_TARGETS}

        self.assertEqual(len(labels), 12)
        self.assertIn("DEFENSE_GOVERNMENT_BACKLOG", labels)
        self.assertIn("SHIPBUILDING_OFFSHORE_BACKLOG", labels)
        self.assertIn("EXPORT_RECURRING_CONSUMER", labels)
        self.assertIn("RAIL_INFRASTRUCTURE", labels)
        self.assertIn("CHEMICAL_SPREAD", labels)
        self.assertIn("DIGITAL_ASSET_TOKENIZATION", labels)
        self.assertIn("SECURITY_IDENTITY_DEEPFAKE", labels)
        self.assertIn("RETAIL_ECOMMERCE_LOGISTICS", labels)
        self.assertIn("BATTERY_MATERIALS_ESS", labels)
        self.assertIn("INSURANCE_UNDERWRITING", labels)
        self.assertIn("SECURITIES_BROKERAGE", labels)
        self.assertIn("VALUE_UP_SHAREHOLDER", labels)

    def test_defense_is_green_possible_but_dilution_and_delivery_are_guardrails(self):
        target = target_for("DEFENSE_GOVERNMENT_BACKLOG")
        records = {record.case_id: record for record in round29_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(target.score_weight.capital_allocation, 3)
        self.assertIn("government_customer", target.green_conditions)
        self.assertIn("dilution", target.red_flags)
        self.assertEqual(records["hanwha_aerospace_romania_k9_success_case"].case_type, "structural_success")
        self.assertEqual(records["hanwha_aerospace_dilution_capital_allocation_risk"].case_type, "failed_rerating")
        self.assertEqual(records["defense_cost_delay_4c"].case_type, "4c_thesis_break")

    def test_shipbuilding_requires_price_margin_and_low_margin_backlog_rolloff(self):
        target = target_for("SHIPBUILDING_OFFSHORE_BACKLOG")
        records = {record.case_id: record for record in round29_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("newbuilding_price_up", target.green_conditions)
        self.assertIn("low_margin_backlog_rolloff", target.green_conditions)
        self.assertIn("low_margin_backlog", target.red_flags)
        self.assertEqual(records["low_margin_backlog_counterexample"].case_type, "failed_rerating")
        self.assertEqual(records["shipbuilding_cost_inflation_4c"].case_type, "4c_thesis_break")

    def test_export_consumer_can_pass_visibility_without_contract_quality(self):
        target = target_for("EXPORT_RECURRING_CONSUMER")
        records = {record.case_id: record for record in round29_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("repeat_consumer_demand", target.green_conditions)
        self.assertIn("overseas_channel_expansion", target.green_conditions)
        self.assertNotIn("contract_quality", target.green_conditions)
        self.assertIn("single_product", target.red_flags)
        self.assertEqual(records["samyang_buldak_export_rerating_success"].case_type, "structural_success")
        self.assertEqual(records["export_inventory_channel_stuffing_4c"].case_type, "4c_thesis_break")

    def test_rail_uses_contract_backlog_archetype_but_margin_and_financing_gates(self):
        target = target_for("RAIL_INFRASTRUCTURE")
        records = {record.case_id: record for record in round29_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("actual_contract", target.green_conditions)
        self.assertIn("financing", target.red_flags)
        self.assertEqual(records["hyundai_rotem_morocco_rail_order_candidate"].case_type, "success_candidate")
        self.assertEqual(records["reconstruction_rail_theme_event_watch"].case_type, "event_premium")

    def test_chemical_digital_retail_battery_and_securities_stay_watch_first(self):
        for target_id in (
            "CHEMICAL_SPREAD",
            "DIGITAL_ASSET_TOKENIZATION",
            "RETAIL_ECOMMERCE_LOGISTICS",
            "BATTERY_MATERIALS_ESS",
            "SECURITIES_BROKERAGE",
        ):
            target = target_for(target_id)
            self.assertIsNotNone(target)
            assert target is not None
            self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)

        chemical = target_for("CHEMICAL_SPREAD")
        digital = target_for("DIGITAL_ASSET_TOKENIZATION")
        assert chemical is not None
        assert digital is not None
        self.assertEqual(chemical.score_weight.structural_visibility, 8)
        self.assertIn("china_middle_east_overcapacity", chemical.red_flags)
        self.assertIn("regulatory_approval", digital.green_conditions)
        self.assertIn("no_revenue", digital.red_flags)

    def test_security_is_green_possible_but_operational_trust_is_hard_gate(self):
        target = target_for("SECURITY_IDENTITY_DEEPFAKE")
        records = {record.case_id: record for record in round29_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("recurring_subscription_revenue", target.green_conditions)
        self.assertIn("operational_trust_intact", target.green_conditions)
        self.assertIn("major_outage", target.stage4c_conditions)
        self.assertEqual(records["crowdstrike_outage_4c"].case_type, "4c_thesis_break")
        self.assertEqual(records["security_theme_no_contract_counterexample"].case_type, "failed_rerating")

    def test_financial_valueup_splits_insurance_securities_and_shareholder_return(self):
        insurance = target_for("INSURANCE_UNDERWRITING")
        securities = target_for("SECURITIES_BROKERAGE")
        valueup = target_for("VALUE_UP_SHAREHOLDER")
        records = {record.case_id: record for record in round29_case_records()}

        self.assertIsNotNone(insurance)
        self.assertIsNotNone(securities)
        self.assertIsNotNone(valueup)
        assert insurance is not None
        assert securities is not None
        assert valueup is not None
        self.assertEqual(insurance.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(securities.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertEqual(valueup.score_weight.valuation, 25)
        self.assertEqual(valueup.score_weight.capital_allocation, 10)
        self.assertIn("actual_cancellation", valueup.green_conditions)
        self.assertEqual(records["low_pbr_no_roe_value_trap"].case_type, "failed_rerating")
        self.assertEqual(records["buyback_no_cancel_counterexample"].case_type, "failed_rerating")

    def test_case_records_validate_and_keep_backfill_open(self):
        records = round29_case_records()

        self.assertEqual(len(records), len(ROUND29_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.price_validation.price_validation_status, "needs_price_backfill")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("theme_label_is_not_score_evidence", record.green_guardrails)

    def test_score_profile_rows_mark_no_production_change(self):
        for row in round29_score_profile_rows():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_summary_reports_v14_not_production_scoring(self):
        summary = round29_summary()
        markdown = render_round29_summary_markdown()
        capital_markdown = render_round29_capital_allocation_markdown()

        self.assertEqual(summary["target_count"], 12)
        self.assertEqual(summary["case_candidate_count"], 40)
        self.assertEqual(summary["success_candidate_count"], 13)
        self.assertEqual(summary["stage4b_case_count"], 0)
        self.assertEqual(summary["stage4c_case_count"], 10)
        self.assertEqual(summary["green_possible_count"], 7)
        self.assertEqual(summary["watch_yellow_first_count"], 5)
        self.assertEqual(summary["redteam_first_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("production_scoring_changed: false", markdown)
        self.assertIn("Theme names, case IDs, policies, search labels, and price rallies are not score evidence", markdown)
        self.assertIn("Capital allocation can support confidence", capital_markdown)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round29_score_weight_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_v11_round29.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round29_v14.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["risk_boundary"].exists())
            self.assertTrue(paths["capital_allocation"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND29_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round29_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round29_score_weight_v14", text)


if __name__ == "__main__":
    unittest.main()
