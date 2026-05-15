import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round46_r6_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round46_r6_financial_capital_digital import (
    ROUND46_CASE_CANDIDATES,
    ROUND46_PRICE_FIELDS,
    ROUND46_SCORE_TARGETS,
    render_round46_green_guardrail_markdown,
    render_round46_price_validation_plan_markdown,
    render_round46_summary_markdown,
    round46_case_candidate_rows,
    round46_case_records,
    round46_price_field_rows,
    round46_score_profile_rows,
    round46_stage_date_rows,
    round46_summary,
    target_for,
    write_round46_r6_reports,
)


class Round46R6FinancialCapitalDigitalTests(unittest.TestCase):
    def test_round46_targets_cover_r6_archetypes(self):
        labels = {target.target_id for target in ROUND46_SCORE_TARGETS}

        self.assertEqual(len(labels), 10)
        self.assertIn("FINANCIAL_SPREAD_BALANCE_SHEET", labels)
        self.assertIn("INSURANCE_UNDERWRITING_CYCLE", labels)
        self.assertIn("SECURITIES_BROKERAGE_CYCLE", labels)
        self.assertIn("VALUE_UP_SHAREHOLDER_RETURN", labels)
        self.assertIn("PAYMENT_FINTECH_INFRA", labels)
        self.assertIn("DIGITAL_ASSET_TOKENIZATION", labels)
        for target in ROUND46_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL)
            self.assertFalse(target.production_scoring_changed)

    def test_new_r6_canonical_archetypes_exist(self):
        expected = {
            E2RArchetype.INSURANCE_UNDERWRITING_CYCLE,
            E2RArchetype.SECURITIES_BROKERAGE_CYCLE,
            E2RArchetype.PAYMENT_FINTECH_INFRA,
            E2RArchetype.DIGITAL_ASSET_TOKENIZATION,
            E2RArchetype.CREDIT_DATA_INFRA,
            E2RArchetype.VC_EXIT_MARKET_CYCLE,
            E2RArchetype.DIGITAL_ASSET_THEME_OVERHEAT,
        }

        self.assertTrue(expected.issubset(set(E2RArchetype)))

    def test_financial_and_insurance_are_green_possible_but_guardrailed(self):
        financial = target_for("FINANCIAL_SPREAD_BALANCE_SHEET")
        insurance = target_for("INSURANCE_UNDERWRITING_CYCLE")

        self.assertIsNotNone(financial)
        self.assertIsNotNone(insurance)
        assert financial is not None
        assert insurance is not None
        self.assertEqual(financial.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("cet1_ratio", financial.green_conditions)
        self.assertIn("credit_cost", financial.red_flags)
        self.assertEqual(insurance.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("k_ics_ratio", insurance.green_conditions)
        self.assertIn("loss_ratio", insurance.red_flags)

    def test_digital_asset_and_vc_are_not_auto_green(self):
        tokenization = target_for("DIGITAL_ASSET_TOKENIZATION")
        theme = target_for("DIGITAL_ASSET_THEME_OVERHEAT")
        vc = target_for("VC_EXIT_MARKET_CYCLE")

        self.assertIsNotNone(tokenization)
        self.assertIsNotNone(theme)
        self.assertIsNotNone(vc)
        assert tokenization is not None
        assert theme is not None
        assert vc is not None
        self.assertEqual(tokenization.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("convertibility_risk", tokenization.red_flags)
        self.assertEqual(theme.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertIn("depeg", theme.red_flags)
        self.assertEqual(vc.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertIn("ipo_slowdown", vc.red_flags)

    def test_case_records_validate_and_keep_price_backfill_open(self):
        records = round46_case_records()

        self.assertEqual(len(records), len(ROUND46_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("low_pbr_or_policy_name_is_not_structural_evidence_alone", record.green_guardrails)
            self.assertIn("roe_capital_return_or_regulated_revenue_required_for_green", record.green_guardrails)

    def test_required_round46_cases_are_present_with_stage_dates(self):
        records = {record.case_id: record for record in round46_case_records()}

        self.assertEqual(str(records["korea_commercial_act_treasury_share_cancel_case"].stage2_date), "2026-02-25")
        self.assertEqual(str(records["korea_dividend_tax_reform_case"].stage2_date), "2025-06-11")
        self.assertEqual(str(records["sk_square_buyback_cancel_case"].stage2_date), "2024-11-21")
        self.assertEqual(str(records["samsung_electronics_buyback_mixed_case"].stage2_date), "2024-11-15")
        self.assertEqual(records["samsung_electronics_buyback_mixed_case"].case_type, "event_premium")
        self.assertIsNone(records["samsung_ct_activist_rejection_case"].stage4c_date)
        self.assertEqual(str(records["korea_zinc_buyback_event_case"].stage2_date), "2024-10-21")
        self.assertEqual(str(records["korea_tax_policy_shock_case"].stage4c_date), "2025-08-01")
        self.assertIsNone(records["terrausd_do_kwon_collapse_case"].stage4c_date)
        self.assertEqual(str(records["boe_stablecoin_convertibility_warning_case"].stage4c_date), "2026-05-08")

    def test_score_profile_rows_mark_no_production_change(self):
        rows = {row["target_id"]: row for row in round46_score_profile_rows()}

        self.assertEqual(rows["VALUE_UP_SHAREHOLDER_RETURN"]["large_sector"], "FINANCIAL_CAPITAL_DIGITAL")
        self.assertEqual(rows["VALUE_UP_SHAREHOLDER_RETURN"]["production_scoring_changed"], "false")
        self.assertEqual(rows["DIGITAL_ASSET_THEME_OVERHEAT"]["posture"], "REDTEAM_FIRST")
        self.assertIn("stage4c_conditions", rows["DIGITAL_ASSET_TOKENIZATION"])

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round46_stage_date_rows()}
        fields = {row["field"] for row in round46_price_field_rows()}

        self.assertIn("VALUE_UP_SHAREHOLDER_RETURN", rows)
        self.assertIn("treasury_share_cancellation", rows["VALUE_UP_SHAREHOLDER_RETURN"]["stage2"])
        for field in (
            "stage2_price",
            "MFE_180D",
            "roe",
            "cet1_ratio",
            "buyback_cancelled_flag",
            "payment_volume",
            "take_rate",
            "stablecoin_transaction_volume",
            "convertibility_risk_flag",
            "minority_shareholder_protection_flag",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND46_PRICE_FIELDS))

    def test_summary_and_markdown_explain_r6_guardrails(self):
        summary = round46_summary()
        summary_md = render_round46_summary_markdown()
        guardrails = render_round46_green_guardrail_markdown()
        price_plan = render_round46_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 10)
        self.assertEqual(summary["case_candidate_count"], len(ROUND46_CASE_CANDIDATES))
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("true discount removal", summary_md)
        self.assertIn("Do not apply these R6 v1.0 weights", guardrails)
        self.assertIn("sk_square_buyback_cancel_case", price_plan)
        self.assertIn("terrausd_do_kwon_collapse_case", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round46_r6_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r6_round46.jsonl",
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
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND46_CASE_CANDIDATES))

    def test_case_matrix_records_are_not_production_inputs(self):
        rows = round46_case_candidate_rows()

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

    def test_production_scoring_modules_do_not_import_round46_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round46_r6_financial_capital_digital", text)


if __name__ == "__main__":
    unittest.main()
