import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round72_r6_loop3_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round72_r6_loop3_financial_capital_digital import (
    ROUND72_CASE_CANDIDATES,
    ROUND72_PRICE_FIELDS,
    ROUND72_SCORE_TARGETS,
    render_round72_green_guardrail_markdown,
    render_round72_price_validation_plan_markdown,
    render_round72_risk_overlay_markdown,
    render_round72_summary_markdown,
    round72_case_candidate_rows,
    round72_case_records,
    round72_price_field_rows,
    round72_score_profile_rows,
    round72_stage_date_rows,
    round72_summary,
    round72_target_for,
    write_round72_r6_loop3_reports,
)


class Round72R6Loop3FinancialCapitalDigitalTests(unittest.TestCase):
    def test_round72_targets_cover_r6_loop3_archetypes_and_overlays(self):
        labels = {target.target_id for target in ROUND72_SCORE_TARGETS}

        self.assertEqual(len(labels), 16)
        for label in (
            "FINANCIAL_SPREAD_BALANCE_SHEET",
            "INSURANCE_UNDERWRITING_CYCLE",
            "SECURITIES_BROKERAGE_CYCLE",
            "VALUE_UP_SHAREHOLDER_RETURN",
            "HOLDING_RESTRUCTURING_GOVERNANCE",
            "EVENT_PREMIUM_GOVERNANCE_BATTLE",
            "PAYMENT_FINTECH_INFRA",
            "DIGITAL_ASSET_TOKENIZATION",
            "REGULATED_STABLECOIN_INFRA",
            "ALGORITHMIC_STABLECOIN_FAILURE",
            "CREDIT_DATA_INFRA",
            "VC_EXIT_MARKET_CYCLE",
            "DIGITAL_ASSET_EXCHANGE_CONSOLIDATION",
            "TAX_POLICY_MARKET_SHOCK_OVERLAY",
            "GOVERNANCE_EXECUTION_FAILURE_OVERLAY",
            "STABLECOIN_CONVERTIBILITY_OVERLAY",
        ):
            self.assertIn(label, labels)
        for target in ROUND72_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL)
            self.assertFalse(target.production_scoring_changed)

    def test_new_loop3_canonical_archetypes_exist(self):
        expected = (
            E2RArchetype.EVENT_PREMIUM_GOVERNANCE_BATTLE,
            E2RArchetype.REGULATED_STABLECOIN_INFRA,
            E2RArchetype.ALGORITHMIC_STABLECOIN_FAILURE,
            E2RArchetype.DIGITAL_ASSET_EXCHANGE_CONSOLIDATION,
        )

        for archetype in expected:
            self.assertIsInstance(archetype.value, str)

    def test_financial_insurance_stablecoin_and_exchange_policies_are_separated(self):
        financial = round72_target_for("FINANCIAL_SPREAD_BALANCE_SHEET")
        insurance = round72_target_for("INSURANCE_UNDERWRITING_CYCLE")
        stablecoin = round72_target_for("REGULATED_STABLECOIN_INFRA")
        algorithmic = round72_target_for("ALGORITHMIC_STABLECOIN_FAILURE")
        exchange = round72_target_for("DIGITAL_ASSET_EXCHANGE_CONSOLIDATION")

        for target in (financial, insurance, stablecoin, algorithmic, exchange):
            self.assertIsNotNone(target)
        assert financial is not None
        assert insurance is not None
        assert stablecoin is not None
        assert algorithmic is not None
        assert exchange is not None
        self.assertEqual(financial.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("cet1_ratio", financial.green_conditions)
        self.assertIn("tax_policy_shock", financial.red_flags)
        self.assertEqual(insurance.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("k_ics_ratio", insurance.green_conditions)
        self.assertIn("csm_quality_damage", insurance.red_flags)
        self.assertEqual(stablecoin.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("reserve_transparency", stablecoin.green_conditions)
        self.assertEqual(algorithmic.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertTrue(algorithmic.gate_only)
        self.assertIn("abnormal_withdrawal", exchange.red_flags)

    def test_valueup_execution_and_event_premium_are_not_the_same(self):
        valueup = round72_target_for("VALUE_UP_SHAREHOLDER_RETURN")
        holding = round72_target_for("HOLDING_RESTRUCTURING_GOVERNANCE")
        event = round72_target_for("EVENT_PREMIUM_GOVERNANCE_BATTLE")

        assert valueup is not None
        assert holding is not None
        assert event is not None
        self.assertEqual(valueup.score_weight.capital_allocation, 12)
        self.assertIn("treasury_share_cancellation", valueup.stage2_signals)
        self.assertIn("buyback_only", valueup.red_flags)
        self.assertIn("actual_cancellation", holding.green_conditions)
        self.assertIn("share_issuance_defense", holding.red_flags)
        self.assertEqual(event.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertFalse(event.gate_only)
        self.assertIn("tender_offer", event.red_flags)

    def test_overlays_are_gate_only_redteam(self):
        algorithmic = round72_target_for("ALGORITHMIC_STABLECOIN_FAILURE")
        tax = round72_target_for("TAX_POLICY_MARKET_SHOCK_OVERLAY")
        governance = round72_target_for("GOVERNANCE_EXECUTION_FAILURE_OVERLAY")
        convertibility = round72_target_for("STABLECOIN_CONVERTIBILITY_OVERLAY")

        for target in (algorithmic, tax, governance, convertibility):
            assert target is not None
            self.assertEqual(target.posture, Round10ThemePosture.REDTEAM_FIRST)
            self.assertTrue(target.gate_only)
            self.assertEqual(target.score_weight.eps_fcf, "gate")
        assert tax is not None
        assert governance is not None
        assert convertibility is not None
        self.assertIn("ai_windfall_tax_comment", tax.stage4c_conditions)
        self.assertIn("activist_rejection", governance.stage4c_conditions)
        self.assertIn("issuer_margin_compression", convertibility.stage4c_conditions)

    def test_required_round72_cases_are_present_with_stage_dates(self):
        rows = {row["case_id"]: row for row in round72_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND72_CASE_CANDIDATES))
        self.assertEqual(rows["korea_commercial_act_treasury_cancel_case"]["stage2_date"], "2026-02-25")
        self.assertEqual(rows["sk_square_buyback_cancel_case"]["stage2_date"], "2024-11-21")
        self.assertEqual(rows["samsung_electronics_treasury_cancel_case"]["case_type"], "failed_rerating")
        self.assertEqual(rows["samsung_electronics_treasury_cancel_case"]["stage2_date"], "2026-03-31")
        self.assertEqual(rows["korea_bank_financial_holding_valueup_candidate"]["target_id"], "FINANCIAL_SPREAD_BALANCE_SHEET")
        self.assertEqual(rows["korea_bank_financial_holding_valueup_candidate"]["stage2_date"], "")
        self.assertEqual(rows["korea_insurance_underwriting_valueup_candidate"]["target_id"], "INSURANCE_UNDERWRITING_CYCLE")
        self.assertEqual(rows["korea_insurance_underwriting_valueup_candidate"]["stage2_date"], "")
        self.assertEqual(rows["samsung_ct_activist_rejection_case"]["stage4c_date"], "")
        self.assertEqual(rows["korea_zinc_tender_offer_event_case"]["target_id"], "EVENT_PREMIUM_GOVERNANCE_BATTLE")
        self.assertEqual(rows["korea_zinc_tender_offer_event_case"]["stage2_date"], "2024-09-13")
        self.assertEqual(rows["korea_zinc_share_issue_probe_case"]["stage4c_date"], "2024-10-31")
        self.assertEqual(rows["korea_tax_policy_shock_case"]["stage4c_date"], "2025-08-06")
        self.assertEqual(rows["ai_windfall_tax_comment_case"]["stage4c_date"], "")
        self.assertEqual(rows["stripe_payment_infra_profit_case"]["stage2_date"], "2025-02-27")
        self.assertEqual(rows["mynt_gcash_ipo_case"]["stage2_date"], "2026-05-14")
        self.assertEqual(rows["toss_global_stablecoin_case"]["stage2_date"], "2025-09-09")
        self.assertEqual(rows["circle_stablecoin_ipo_valuation_case"]["stage4b_date"], "2025-06-30")
        self.assertEqual(rows["boe_stablecoin_rules_reconsider_case"]["stage4c_date"], "2026-05-14")
        self.assertEqual(rows["terrausd_do_kwon_case"]["stage4c_date"], "")
        self.assertEqual(rows["naver_dunamu_upbit_deal_case"]["stage2_date"], "2025-11-27")
        self.assertEqual(rows["naver_dunamu_upbit_deal_case"]["stage4c_date"], "2025-11-27")

    def test_case_records_validate_and_keep_round72_guardrails(self):
        records = round72_case_records()

        self.assertEqual(len(records), len(ROUND72_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, "FINANCIAL_CAPITAL_DIGITAL")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("do_not_change_production_scoring", record.green_guardrails)
            self.assertIn("low_pbr_or_policy_name_is_not_structural_evidence_alone", record.green_guardrails)
            self.assertIn("buyback_is_not_cancellation", record.green_guardrails)
            self.assertIn("fintech_user_count_is_not_take_rate_or_fcf", record.green_guardrails)
            self.assertIn("stablecoin_news_is_not_regulated_revenue", record.green_guardrails)
            self.assertIn("exchange_market_share_is_not_security_cleanliness", record.green_guardrails)
        by_id = {record.case_id: record for record in records}
        self.assertEqual(by_id["sk_square_buyback_cancel_case"].score_price_alignment, "aligned")
        self.assertEqual(by_id["samsung_electronics_treasury_cancel_case"].score_price_alignment, "evidence_good_but_price_failed")
        self.assertEqual(by_id["korea_bank_financial_holding_valueup_candidate"].price_validation.price_validation_status, "needs_named_case_and_price_backfill")
        self.assertIn("roe", "|".join(by_id["korea_bank_financial_holding_valueup_candidate"].must_have_fields))
        self.assertEqual(by_id["korea_insurance_underwriting_valueup_candidate"].price_validation.price_validation_status, "needs_named_case_and_price_backfill")
        self.assertIn("k_ics_ratio", by_id["korea_insurance_underwriting_valueup_candidate"].must_have_fields)
        self.assertEqual(by_id["korea_zinc_tender_offer_event_case"].rerating_result, "event_premium")
        self.assertEqual(by_id["circle_stablecoin_ipo_valuation_case"].rerating_result, "theme_overheat")
        self.assertEqual(by_id["terrausd_do_kwon_case"].score_price_alignment, "false_positive_score")
        self.assertIn(E2RArchetype.REGULATED_STABLECOIN_INFRA, by_id["toss_global_stablecoin_case"].secondary_archetypes)

    def test_score_profile_rows_match_round72_weight_table(self):
        rows = {row["target_id"]: row for row in round72_score_profile_rows()}

        self.assertEqual(rows["FINANCIAL_SPREAD_BALANCE_SHEET"]["eps_fcf"], "15")
        self.assertEqual(rows["INSURANCE_UNDERWRITING_CYCLE"]["structural_visibility"], "21")
        self.assertEqual(rows["SECURITIES_BROKERAGE_CYCLE"]["capital_allocation"], "6")
        self.assertEqual(rows["VALUE_UP_SHAREHOLDER_RETURN"]["capital_allocation"], "12")
        self.assertEqual(rows["HOLDING_RESTRUCTURING_GOVERNANCE"]["market_mispricing"], "22")
        self.assertEqual(rows["EVENT_PREMIUM_GOVERNANCE_BATTLE"]["eps_fcf"], "8")
        self.assertEqual(rows["REGULATED_STABLECOIN_INFRA"]["information_confidence"], "6")
        self.assertEqual(rows["ALGORITHMIC_STABLECOIN_FAILURE"]["gate_only"], "true")
        self.assertEqual(rows["TAX_POLICY_MARKET_SHOCK_OVERLAY"]["eps_fcf"], "gate")
        self.assertEqual(rows["STABLECOIN_CONVERTIBILITY_OVERLAY"]["gate_only"], "true")
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round72_stage_date_rows()}
        fields = {row["field"] for row in round72_price_field_rows()}

        self.assertIn("treasury_share_cancellation", rows["VALUE_UP_SHAREHOLDER_RETURN"]["stage2"])
        self.assertIn("tender_offer", rows["EVENT_PREMIUM_GOVERNANCE_BATTLE"]["stage1"])
        self.assertIn("issuer_margin_compression", rows["REGULATED_STABLECOIN_INFRA"]["stage4c"])
        self.assertIn("depeg", rows["ALGORITHMIC_STABLECOIN_FAILURE"]["stage4c"])
        self.assertIn("abnormal_crypto_withdrawal", rows["DIGITAL_ASSET_EXCHANGE_CONSOLIDATION"]["stage4c"])
        self.assertIn("tax_policy_shock", rows["TAX_POLICY_MARKET_SHOCK_OVERLAY"]["stage4c"])
        for field in (
            "stage2_price",
            "below_stage2_price_flag",
            "roe",
            "pbr_band_before",
            "cet1_ratio",
            "k_ics_ratio",
            "csm_quality_signal",
            "buyback_cancelled_flag",
            "treasury_share_cancel_amount",
            "buyback_only_flag",
            "nav_discount",
            "activist_proposal_rejection_flag",
            "share_issuance_after_tender_flag",
            "unfair_trading_probe_flag",
            "dividend_tax_change_flag",
            "ai_windfall_tax_comment_flag",
            "payment_volume",
            "take_rate",
            "stablecoin_transaction_volume",
            "reserve_asset_type",
            "user_cap_flag",
            "unremunerated_reserve_requirement_flag",
            "crypto_exchange_market_share",
            "abnormal_withdrawal_flag",
            "deal_dilution_flag",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND72_PRICE_FIELDS))

    def test_summary_and_markdown_explain_r6_loop3_guardrails(self):
        summary = round72_summary()
        summary_md = render_round72_summary_markdown()
        guardrails = render_round72_green_guardrail_markdown()
        overlays = render_round72_risk_overlay_markdown()
        price_plan = render_round72_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 16)
        self.assertEqual(summary["case_candidate_count"], 17)
        self.assertEqual(summary["success_candidate_count"], 7)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["stage4b_case_count"], 1)
        self.assertEqual(summary["stage4c_case_count"], 7)
        self.assertEqual(summary["green_possible_count"], 2)
        self.assertEqual(summary["watch_yellow_first_count"], 8)
        self.assertEqual(summary["redteam_first_count"], 6)
        self.assertEqual(summary["gate_only_target_count"], 4)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("R6 Loop 3", summary_md)
        self.assertIn("Do not apply R6 Loop-3 v3.0 weights", guardrails)
        self.assertIn("DIGITAL_ASSET_EXCHANGE_SECURITY_4C", overlays)
        self.assertIn("circle_stablecoin_ipo_valuation_case", price_plan)
        self.assertIn("naver_dunamu_upbit_deal_case", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round72_r6_loop3_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r6_loop3_round72.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round72_r6_loop3_v3.csv",
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
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND72_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round72_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round72_r6_loop3_financial_capital_digital", text)


if __name__ == "__main__":
    unittest.main()
