import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round59_r6_loop2_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round59_r6_loop2_financial_capital_digital import (
    ROUND59_CASE_CANDIDATES,
    ROUND59_PRICE_FIELDS,
    ROUND59_SCORE_TARGETS,
    render_round59_green_guardrail_markdown,
    render_round59_price_validation_plan_markdown,
    render_round59_risk_overlay_markdown,
    render_round59_summary_markdown,
    round59_case_candidate_rows,
    round59_case_records,
    round59_price_field_rows,
    round59_score_profile_rows,
    round59_stage_date_rows,
    round59_summary,
    target_for,
    write_round59_r6_loop2_reports,
)


class Round59R6Loop2FinancialCapitalDigitalTests(unittest.TestCase):
    def test_round59_targets_cover_r6_loop2_archetypes(self):
        labels = {target.target_id for target in ROUND59_SCORE_TARGETS}

        self.assertEqual(len(labels), 13)
        for label in (
            "FINANCIAL_SPREAD_BALANCE_SHEET",
            "INSURANCE_UNDERWRITING_CYCLE",
            "SECURITIES_BROKERAGE_CYCLE",
            "VALUE_UP_SHAREHOLDER_RETURN",
            "HOLDING_RESTRUCTURING_GOVERNANCE",
            "PAYMENT_FINTECH_INFRA",
            "DIGITAL_ASSET_TOKENIZATION",
            "CREDIT_DATA_INFRA",
            "VC_EXIT_MARKET_CYCLE",
            "DIGITAL_ASSET_THEME_OVERHEAT",
            "GOVERNANCE_EXECUTION_FAILURE_OVERLAY",
            "TAX_POLICY_MARKET_SHOCK_OVERLAY",
            "STABLECOIN_CONVERTIBILITY_OVERLAY",
        ):
            self.assertIn(label, labels)
        for target in ROUND59_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL)
            self.assertFalse(target.production_scoring_changed)

    def test_new_r6_loop2_overlays_exist(self):
        expected = (
            E2RArchetype.GOVERNANCE_EXECUTION_FAILURE_OVERLAY,
            E2RArchetype.TAX_POLICY_MARKET_SHOCK_OVERLAY,
            E2RArchetype.STABLECOIN_CONVERTIBILITY_OVERLAY,
        )

        for archetype in expected:
            self.assertIsInstance(archetype.value, str)

    def test_financial_and_insurance_are_green_possible_but_guardrailed(self):
        financial = target_for("FINANCIAL_SPREAD_BALANCE_SHEET")
        insurance = target_for("INSURANCE_UNDERWRITING_CYCLE")

        assert financial is not None
        assert insurance is not None
        self.assertEqual(financial.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("cet1_ratio", financial.green_conditions)
        self.assertIn("credit_cost", financial.red_flags)
        self.assertIn("tax_policy", financial.loop2_penalty_axes)
        self.assertEqual(insurance.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("k_ics_ratio", insurance.green_conditions)
        self.assertIn("loss_ratio", insurance.red_flags)

    def test_valueup_requires_execution_not_policy_or_buyback_only(self):
        valueup = target_for("VALUE_UP_SHAREHOLDER_RETURN")
        holding = target_for("HOLDING_RESTRUCTURING_GOVERNANCE")

        assert valueup is not None
        assert holding is not None
        self.assertEqual(valueup.score_weight.capital_allocation, 11)
        self.assertIn("buyback_cancelled", valueup.green_conditions)
        self.assertIn("roe_improvement", valueup.stage2_signals)
        self.assertIn("buyback_only", valueup.red_flags)
        self.assertIn("actual_cancellation", holding.green_conditions)
        self.assertIn("event_premium", holding.red_flags)

    def test_overlays_are_gate_only_redteam(self):
        governance = target_for("GOVERNANCE_EXECUTION_FAILURE_OVERLAY")
        tax = target_for("TAX_POLICY_MARKET_SHOCK_OVERLAY")
        stablecoin = target_for("STABLECOIN_CONVERTIBILITY_OVERLAY")

        for target in (governance, tax, stablecoin):
            assert target is not None
            self.assertEqual(target.posture, Round10ThemePosture.REDTEAM_FIRST)
            self.assertTrue(target.gate_only)
            self.assertEqual(target.score_weight.eps_fcf, "gate")
        assert governance is not None
        assert tax is not None
        assert stablecoin is not None
        self.assertIn("activist_rejection", governance.stage4c_conditions)
        self.assertIn("transaction_tax_change", tax.red_flags)
        self.assertIn("convertibility_failure", stablecoin.stage4c_conditions)

    def test_required_round59_cases_are_present_with_stage_dates(self):
        rows = {row["case_id"]: row for row in round59_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND59_CASE_CANDIDATES))
        self.assertEqual(rows["korea_commercial_act_treasury_cancel_case"]["stage2_date"], "2026-02-25")
        self.assertEqual(rows["sk_square_buyback_cancel_case"]["stage2_date"], "2024-11-21")
        self.assertEqual(rows["samsung_electronics_buyback_case"]["stage2_date"], "2024-11-15")
        self.assertEqual(rows["samsung_electronics_treasury_cancel_case"]["stage2_date"], "2026-03-31")
        self.assertEqual(rows["samsung_ct_activist_rejection_case"]["stage4c_date"], "")
        self.assertEqual(rows["korea_zinc_tender_offer_event_case"]["stage2_date"], "2024-09-13")
        self.assertEqual(rows["korea_zinc_buyback_court_case"]["stage2_date"], "2024-10-21")
        self.assertEqual(rows["korea_zinc_share_issue_probe_case"]["stage4c_date"], "2024-10-31")
        self.assertEqual(rows["korea_tax_policy_shock_case"]["stage4c_date"], "2025-08-06")
        self.assertEqual(rows["ai_windfall_tax_comment_case"]["stage4c_date"], "2026-05-12")
        self.assertEqual(rows["stripe_payment_infra_profit_case"]["stage2_date"], "2025-02-27")
        self.assertEqual(rows["mynt_gcash_ipo_case"]["stage2_date"], "2026-05-14")
        self.assertEqual(rows["toss_global_stablecoin_case"]["stage2_date"], "2025-09-09")
        self.assertEqual(rows["boe_stablecoin_convertibility_case"]["stage4c_date"], "2026-05-08")
        self.assertEqual(rows["terrausd_do_kwon_case"]["stage4c_date"], "")

    def test_case_records_validate_and_keep_round59_guardrails(self):
        records = round59_case_records()

        self.assertEqual(len(records), len(ROUND59_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_change_production_scoring", record.green_guardrails)
            self.assertIn("low_pbr_or_policy_name_is_not_structural_evidence_alone", record.green_guardrails)
            self.assertIn("buyback_is_not_cancellation", record.green_guardrails)
            self.assertIn("fintech_user_count_is_not_take_rate_or_fcf", record.green_guardrails)
            self.assertIn("stablecoin_news_is_not_regulated_revenue", record.green_guardrails)
        by_id = {record.case_id: record for record in records}
        self.assertEqual(by_id["sk_square_buyback_cancel_case"].score_price_alignment, "aligned")
        self.assertEqual(by_id["samsung_electronics_buyback_case"].score_price_alignment, "price_moved_without_evidence")
        self.assertEqual(by_id["korea_zinc_tender_offer_event_case"].rerating_result, "event_premium")
        self.assertEqual(by_id["korea_tax_policy_shock_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["terrausd_do_kwon_case"].score_price_alignment, "false_positive_score")
        self.assertIn(E2RArchetype.DIGITAL_ASSET_TOKENIZATION, by_id["toss_global_stablecoin_case"].secondary_archetypes)

    def test_score_profile_rows_match_round59_weight_table(self):
        rows = {row["target_id"]: row for row in round59_score_profile_rows()}

        self.assertEqual(rows["FINANCIAL_SPREAD_BALANCE_SHEET"]["eps_fcf"], "15")
        self.assertEqual(rows["INSURANCE_UNDERWRITING_CYCLE"]["structural_visibility"], "21")
        self.assertEqual(rows["SECURITIES_BROKERAGE_CYCLE"]["capital_allocation"], "7")
        self.assertEqual(rows["VALUE_UP_SHAREHOLDER_RETURN"]["capital_allocation"], "11")
        self.assertEqual(rows["HOLDING_RESTRUCTURING_GOVERNANCE"]["market_mispricing"], "22")
        self.assertEqual(rows["DIGITAL_ASSET_THEME_OVERHEAT"]["information_confidence"], "3")
        self.assertEqual(rows["GOVERNANCE_EXECUTION_FAILURE_OVERLAY"]["gate_only"], "true")
        self.assertEqual(rows["TAX_POLICY_MARKET_SHOCK_OVERLAY"]["eps_fcf"], "gate")
        self.assertEqual(rows["STABLECOIN_CONVERTIBILITY_OVERLAY"]["gate_only"], "true")
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round59_stage_date_rows()}
        fields = {row["field"] for row in round59_price_field_rows()}

        self.assertIn("treasury_share_cancellation", rows["VALUE_UP_SHAREHOLDER_RETURN"]["stage2"])
        self.assertIn("event_premium", rows["HOLDING_RESTRUCTURING_GOVERNANCE"]["red_flags"])
        self.assertIn("convertibility_failure", rows["DIGITAL_ASSET_TOKENIZATION"]["stage4c"])
        self.assertIn("tax_policy_shock", rows["TAX_POLICY_MARKET_SHOCK_OVERLAY"]["stage4c"])
        for field in (
            "stage2_price",
            "below_stage2_price_flag",
            "roe",
            "pbr_band_before",
            "cet1_ratio",
            "k_ics_ratio",
            "csm_growth",
            "buyback_cancelled_flag",
            "treasury_share_cancel_amount",
            "shareholder_return_execution_flag",
            "nav_discount",
            "minority_shareholder_protection_flag",
            "share_issuance_amount",
            "transaction_tax_change_flag",
            "payment_volume",
            "take_rate",
            "stablecoin_transaction_volume",
            "reserve_asset_type",
            "convertibility_risk_flag",
            "algorithmic_stablecoin_flag",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND59_PRICE_FIELDS))

    def test_summary_and_markdown_explain_r6_loop2_guardrails(self):
        summary = round59_summary()
        summary_md = render_round59_summary_markdown()
        guardrails = render_round59_green_guardrail_markdown()
        overlays = render_round59_risk_overlay_markdown()
        price_plan = render_round59_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 13)
        self.assertEqual(summary["case_candidate_count"], 15)
        self.assertEqual(summary["success_candidate_count"], 5)
        self.assertEqual(summary["event_premium_count"], 4)
        self.assertEqual(summary["stage4b_case_count"], 0)
        self.assertEqual(summary["stage4c_case_count"], 6)
        self.assertEqual(summary["green_possible_count"], 2)
        self.assertEqual(summary["watch_yellow_first_count"], 6)
        self.assertEqual(summary["redteam_first_count"], 5)
        self.assertEqual(summary["gate_only_target_count"], 3)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("R6 Loop 2", summary_md)
        self.assertIn("Do not apply R6 Loop-2 v2.0 weights", guardrails)
        self.assertIn("EVENT_PREMIUM_NOT_VALUEUP", overlays)
        self.assertIn("korea_commercial_act_treasury_cancel_case", price_plan)
        self.assertIn("terrausd_do_kwon_case", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round59_r6_loop2_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r6_loop2_round59.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round59_r6_loop2_v2.csv",
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
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND59_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round59_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round59_r6_loop2_financial_capital_digital", text)


if __name__ == "__main__":
    unittest.main()
