import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round31_score_weight_report import build_parser
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10ThemePosture
from e2r.sector.round31_score_weight_v16 import (
    ROUND31_CASE_CANDIDATES,
    ROUND31_SCORE_TARGETS,
    render_round31_ai_infra_split_markdown,
    render_round31_regulated_risk_markdown,
    render_round31_summary_markdown,
    round31_case_records,
    round31_score_profile_rows,
    round31_summary,
    target_for,
    write_round31_score_weight_reports,
)


class Round31ScoreWeightV16Tests(unittest.TestCase):
    def test_round31_targets_include_v16_calibration_families(self):
        labels = {target.target_id for target in ROUND31_SCORE_TARGETS}

        self.assertEqual(len(labels), 8)
        self.assertIn("DATA_CENTER_REIT_INFRASTRUCTURE", labels)
        self.assertIn("WASTE_RECYCLING_ENVIRONMENT", labels)
        self.assertIn("MEDICAL_DEVICE_DENTAL_IMPLANT", labels)
        self.assertIn("CONSUMER_REGULATED_PRODUCT", labels)
        self.assertIn("APPAREL_FAST_FASHION_BRAND_OEM", labels)
        self.assertIn("DIGITAL_ASSET_TOKENIZATION", labels)
        self.assertIn("AI_DATA_CENTER_INFRASTRUCTURE", labels)
        self.assertIn("VALUE_UP_SHAREHOLDER_RETURN", labels)

    def test_data_center_reit_is_green_possible_but_requires_affo_tenant_and_funding(self):
        target = target_for("DATA_CENTER_REIT_INFRASTRUCTURE")
        records = {record.case_id: record for record in round31_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("ffo_affo_growth", target.green_conditions)
        self.assertIn("funding_cost_controlled", target.green_conditions)
        self.assertIn("power_water_constraint", target.red_flags)
        self.assertEqual(records["blackstone_digital_infra_reit_candidate"].case_type, "success_candidate")
        self.assertEqual(records["data_center_reit_power_water_constraint_4c"].case_type, "4c_thesis_break")

    def test_waste_recycling_can_be_green_with_permit_utilization_and_recurring_fcf(self):
        target = target_for("WASTE_RECYCLING_ENVIRONMENT")
        records = {record.case_id: record for record in round31_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("permit_or_license", target.green_conditions)
        self.assertIn("facility_utilization", target.green_conditions)
        self.assertIn("recurring_fcf", target.green_conditions)
        self.assertEqual(records["eqt_kj_environment_waste_platform_candidate"].case_type, "success_candidate")
        self.assertEqual(records["recycling_capex_low_utilization_4c"].case_type, "4c_thesis_break")

    def test_medical_device_dental_is_green_possible_but_vbp_and_approval_are_gates(self):
        target = target_for("MEDICAL_DEVICE_DENTAL_IMPLANT")
        records = {record.case_id: record for record in round31_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("recurring_procedure_consumable", target.green_conditions)
        self.assertIn("approval_stable", target.green_conditions)
        self.assertIn("vbp_price_control", target.red_flags)
        self.assertEqual(records["straumann_dental_implant_growth_candidate"].case_type, "success_candidate")
        self.assertEqual(records["medical_device_approval_delay_4c"].case_type, "4c_thesis_break")

    def test_regulated_consumer_and_apparel_are_watch_first_with_legal_and_inventory_risk(self):
        regulated = target_for("CONSUMER_REGULATED_PRODUCT")
        apparel = target_for("APPAREL_FAST_FASHION_BRAND_OEM")
        records = {record.case_id: record for record in round31_case_records()}
        risk_review = render_round31_regulated_risk_markdown()

        self.assertIsNotNone(regulated)
        self.assertIsNotNone(apparel)
        assert regulated is not None
        assert apparel is not None
        self.assertEqual(regulated.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertEqual(apparel.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("regulatory_approval", regulated.green_conditions)
        self.assertIn("sales_ban", regulated.stage4c_conditions)
        self.assertIn("inventory", apparel.red_flags)
        self.assertIn("ip_legal_risk", apparel.red_flags)
        self.assertEqual(records["juul_prior_fda_ban_4c"].case_type, "4c_thesis_break")
        self.assertEqual(records["shein_temu_ip_litigation_risk_4c"].case_type, "4c_thesis_break")
        self.assertIn("approval can create Stage 2", risk_review)

    def test_digital_asset_splits_stablecoin_infra_from_nft_theme(self):
        target = target_for("DIGITAL_ASSET_TOKENIZATION")
        records = {record.case_id: record for record in round31_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("fee_or_deposit_revenue", target.green_conditions)
        self.assertIn("nft_theme_only", target.red_flags)
        self.assertEqual(records["stablecoin_payment_infra_candidate"].case_type, "success_candidate")
        self.assertEqual(records["nft_theme_overheat_counterexample"].case_type, "overheat")

    def test_ai_infrastructure_is_green_possible_but_must_be_split_by_axis(self):
        target = target_for("AI_DATA_CENTER_INFRASTRUCTURE")
        split_review = render_round31_ai_infra_split_markdown()

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("orders_or_leases", target.green_conditions)
        self.assertIn("bottleneck_asset", target.green_conditions)
        self.assertIn("water_power_constraint", target.red_flags)
        self.assertIn("Power equipment, transformers, and cables", split_review)
        self.assertIn("Generic HVAC or IDC theme", split_review)

    def test_valueup_requires_execution_not_policy_label(self):
        target = target_for("VALUE_UP_SHAREHOLDER_RETURN")
        records = {record.case_id: record for record in round31_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertEqual(target.score_weight.valuation, 25)
        self.assertEqual(target.score_weight.capital_allocation, 10)
        self.assertIn("actual_cancellation", target.green_conditions)
        self.assertIn("index_inclusion_only", target.red_flags)
        self.assertEqual(records["buyback_cancellation_success_candidate"].case_type, "success_candidate")
        self.assertEqual(records["governance_discount_persistent_counterexample"].case_type, "failed_rerating")

    def test_case_records_validate_and_keep_backfill_open(self):
        records = round31_case_records()

        self.assertEqual(len(records), len(ROUND31_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.price_validation.price_validation_status, "needs_price_backfill")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("theme_label_is_not_score_evidence", record.green_guardrails)

    def test_score_profile_rows_mark_no_production_change(self):
        for row in round31_score_profile_rows():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_summary_reports_v16_not_production_scoring(self):
        summary = round31_summary()
        markdown = render_round31_summary_markdown()

        self.assertEqual(summary["target_count"], 8)
        self.assertEqual(summary["case_candidate_count"], 32)
        self.assertEqual(summary["success_candidate_count"], 12)
        self.assertEqual(summary["stage4b_case_count"], 0)
        self.assertEqual(summary["stage4c_case_count"], 6)
        self.assertEqual(summary["green_possible_count"], 5)
        self.assertEqual(summary["watch_yellow_first_count"], 3)
        self.assertEqual(summary["redteam_first_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("production_scoring_changed: false", markdown)
        self.assertIn("Theme names, case IDs, policy approvals, store/channel labels, and price rallies are not score evidence", markdown)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round31_score_weight_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_v13_round31.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round31_v16.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["regulated_risk"].exists())
            self.assertTrue(paths["ai_infra_split"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND31_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round31_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round31_score_weight_v16", text)


if __name__ == "__main__":
    unittest.main()
