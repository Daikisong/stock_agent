import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round98_r6_loop5_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round98_r6_loop5_financial_capital_digital import (
    ROUND98_CASE_CANDIDATES,
    ROUND98_PRICE_FIELDS,
    ROUND98_SCORE_TARGETS,
    render_round98_green_guardrail_markdown,
    render_round98_price_validation_plan_markdown,
    render_round98_risk_overlay_markdown,
    render_round98_summary_markdown,
    round98_case_candidate_rows,
    round98_case_records,
    round98_price_field_rows,
    round98_score_profile_rows,
    round98_stage_date_rows,
    round98_summary,
    round98_target_for,
    write_round98_r6_loop5_reports,
)


class Round98R6Loop5FinancialCapitalDigitalTests(unittest.TestCase):
    def test_round98_targets_cover_r6_loop5_archetypes_and_overlays(self):
        labels = {target.target_id for target in ROUND98_SCORE_TARGETS}

        self.assertEqual(len(labels), 25)
        for label in (
            "FINANCIAL_SPREAD_BALANCE_SHEET",
            "BANK_HOLDING_VALUEUP_CAPITAL_RETURN",
            "INSURANCE_UNDERWRITING_CYCLE",
            "SECURITIES_BROKERAGE_CYCLE",
            "VALUE_UP_SHAREHOLDER_RETURN",
            "TREASURY_SHARE_CANCEL_EXECUTION",
            "TREASURY_CANCEL_MANDATE_POLICY",
            "HOLDING_RESTRUCTURING_GOVERNANCE",
            "EVENT_PREMIUM_GOVERNANCE_BATTLE",
            "PAYMENT_FINTECH_INFRA",
            "FINTECH_SUPERAPP_IPO_OPTION",
            "KRW_STABLECOIN_INFRA_OPTION",
            "DIGITAL_ASSET_TOKENIZATION",
            "REGULATED_STABLECOIN_INFRA",
            "STABLECOIN_BANK_DEPOSIT_DISINTERMEDIATION",
            "ALGORITHMIC_STABLECOIN_FAILURE",
            "CREDIT_DATA_INFRA",
            "VC_EXIT_MARKET_CYCLE",
            "FINTECH_IPO_VALUATION_RISK",
            "DIGITAL_ASSET_EXCHANGE_CONSOLIDATION",
            "BANK_DIGITAL_ASSET_EQUITY_STAKE",
            "TAX_POLICY_MARKET_SHOCK_OVERLAY",
            "AI_WINDFALL_CITIZEN_DIVIDEND_POLICY_SHOCK",
            "GOVERNANCE_EXECUTION_FAILURE_OVERLAY",
            "STABLECOIN_CONVERTIBILITY_OVERLAY",
        ):
            self.assertIn(label, labels)
        for target in ROUND98_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL)
            self.assertFalse(target.production_scoring_changed)

    def test_new_loop5_canonical_archetypes_exist(self):
        expected = (
            E2RArchetype.BANK_HOLDING_VALUEUP_CAPITAL_RETURN,
            E2RArchetype.TREASURY_SHARE_CANCEL_EXECUTION,
            E2RArchetype.TREASURY_CANCEL_MANDATE_POLICY,
            E2RArchetype.FINTECH_SUPERAPP_IPO_OPTION,
            E2RArchetype.KRW_STABLECOIN_INFRA_OPTION,
            E2RArchetype.FINTECH_IPO_VALUATION_RISK,
            E2RArchetype.BANK_DIGITAL_ASSET_EQUITY_STAKE,
            E2RArchetype.EVENT_PREMIUM_GOVERNANCE_BATTLE,
            E2RArchetype.REGULATED_STABLECOIN_INFRA,
            E2RArchetype.ALGORITHMIC_STABLECOIN_FAILURE,
            E2RArchetype.DIGITAL_ASSET_EXCHANGE_CONSOLIDATION,
            E2RArchetype.STABLECOIN_BANK_DEPOSIT_DISINTERMEDIATION,
            E2RArchetype.AI_WINDFALL_CITIZEN_DIVIDEND_POLICY_SHOCK,
        )

        for archetype in expected:
            self.assertIsInstance(archetype.value, str)

    def test_financial_insurance_stablecoin_and_exchange_policies_are_separated(self):
        financial = round98_target_for("FINANCIAL_SPREAD_BALANCE_SHEET")
        bank_holding = round98_target_for("BANK_HOLDING_VALUEUP_CAPITAL_RETURN")
        insurance = round98_target_for("INSURANCE_UNDERWRITING_CYCLE")
        superapp = round98_target_for("FINTECH_SUPERAPP_IPO_OPTION")
        krw_stablecoin = round98_target_for("KRW_STABLECOIN_INFRA_OPTION")
        stablecoin = round98_target_for("REGULATED_STABLECOIN_INFRA")
        algorithmic = round98_target_for("ALGORITHMIC_STABLECOIN_FAILURE")
        stablecoin_bank = round98_target_for("STABLECOIN_BANK_DEPOSIT_DISINTERMEDIATION")
        exchange = round98_target_for("DIGITAL_ASSET_EXCHANGE_CONSOLIDATION")
        bank_stake = round98_target_for("BANK_DIGITAL_ASSET_EQUITY_STAKE")
        fintech_ipo = round98_target_for("FINTECH_IPO_VALUATION_RISK")

        for target in (financial, bank_holding, insurance, superapp, krw_stablecoin, stablecoin, algorithmic, stablecoin_bank, exchange, bank_stake, fintech_ipo):
            self.assertIsNotNone(target)
        assert financial is not None
        assert bank_holding is not None
        assert insurance is not None
        assert krw_stablecoin is not None
        assert stablecoin is not None
        assert algorithmic is not None
        assert stablecoin_bank is not None
        assert exchange is not None
        assert superapp is not None
        assert bank_stake is not None
        assert fintech_ipo is not None
        self.assertEqual(financial.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("cet1_ratio", financial.green_conditions)
        self.assertIn("tax_policy_shock", financial.red_flags)
        self.assertEqual(bank_holding.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("pbr_roe_band_change", bank_holding.green_conditions)
        self.assertEqual(insurance.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("k_ics_ratio", insurance.green_conditions)
        self.assertIn("csm_quality_damage", insurance.red_flags)
        self.assertEqual(krw_stablecoin.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("regulatory_approval_missing", krw_stablecoin.red_flags)
        self.assertEqual(stablecoin.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("reserve_transparency", stablecoin.green_conditions)
        self.assertIn("credit_loss_control", superapp.stage2_signals)
        self.assertEqual(algorithmic.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertTrue(algorithmic.gate_only)
        self.assertTrue(stablecoin_bank.gate_only)
        self.assertIn("bank_deposit_disintermediation", stablecoin_bank.red_flags)
        self.assertIn("abnormal_withdrawal", exchange.red_flags)
        self.assertIn("equity_method_income", bank_stake.green_conditions)
        self.assertEqual(fintech_ipo.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertIn("ipo_valuation_cut", fintech_ipo.red_flags)

    def test_valueup_execution_and_event_premium_are_not_the_same(self):
        valueup = round98_target_for("VALUE_UP_SHAREHOLDER_RETURN")
        treasury = round98_target_for("TREASURY_SHARE_CANCEL_EXECUTION")
        mandate = round98_target_for("TREASURY_CANCEL_MANDATE_POLICY")
        holding = round98_target_for("HOLDING_RESTRUCTURING_GOVERNANCE")
        event = round98_target_for("EVENT_PREMIUM_GOVERNANCE_BATTLE")

        assert valueup is not None
        assert treasury is not None
        assert mandate is not None
        assert holding is not None
        assert event is not None
        self.assertEqual(valueup.score_weight.capital_allocation, 12)
        self.assertIn("treasury_share_cancellation", valueup.stage2_signals)
        self.assertIn("buyback_only", valueup.red_flags)
        self.assertEqual(treasury.score_weight.capital_allocation, 13)
        self.assertIn("treasury_share_cancellation_completed", treasury.stage2_signals)
        self.assertIn("business_execution_failure", treasury.stage4c_conditions)
        self.assertEqual(mandate.score_weight.structural_visibility, 18)
        self.assertIn("treasury_cancel_mandate", mandate.stage1_signals)
        self.assertIn("policy_only_no_execution", mandate.red_flags)
        self.assertIn("actual_cancellation", holding.green_conditions)
        self.assertIn("share_issuance_defense", holding.red_flags)
        self.assertEqual(event.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertFalse(event.gate_only)
        self.assertIn("tender_offer", event.red_flags)

    def test_overlays_are_gate_only_redteam(self):
        algorithmic = round98_target_for("ALGORITHMIC_STABLECOIN_FAILURE")
        stablecoin_bank = round98_target_for("STABLECOIN_BANK_DEPOSIT_DISINTERMEDIATION")
        tax = round98_target_for("TAX_POLICY_MARKET_SHOCK_OVERLAY")
        ai_shock = round98_target_for("AI_WINDFALL_CITIZEN_DIVIDEND_POLICY_SHOCK")
        governance = round98_target_for("GOVERNANCE_EXECUTION_FAILURE_OVERLAY")
        convertibility = round98_target_for("STABLECOIN_CONVERTIBILITY_OVERLAY")

        for target in (algorithmic, stablecoin_bank, tax, ai_shock, governance, convertibility):
            assert target is not None
            self.assertEqual(target.posture, Round10ThemePosture.REDTEAM_FIRST)
            self.assertTrue(target.gate_only)
            self.assertEqual(target.score_weight.eps_fcf, "gate")
        assert tax is not None
        assert ai_shock is not None
        assert governance is not None
        assert convertibility is not None
        assert stablecoin_bank is not None
        self.assertIn("issuer_margin_compression", stablecoin_bank.stage4c_conditions)
        self.assertIn("ai_windfall_policy_shock", ai_shock.stage4c_conditions)
        self.assertIn("activist_rejection", governance.stage4c_conditions)
        self.assertIn("issuer_margin_compression", convertibility.stage4c_conditions)

    def test_required_round98_cases_are_present_with_stage_dates(self):
        rows = {row["case_id"]: row for row in round98_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND98_CASE_CANDIDATES))
        self.assertEqual(rows["korea_commercial_act_treasury_cancel_case"]["stage1_date"], "2026-02-25")
        self.assertEqual(rows["korea_commercial_act_treasury_cancel_case"]["target_id"], "TREASURY_CANCEL_MANDATE_POLICY")
        self.assertEqual(rows["korea_commercial_act_treasury_cancel_case"]["stage2_date"], "")
        self.assertEqual(rows["sk_square_buyback_cancel_case"]["stage2_date"], "2024-11-21")
        self.assertEqual(rows["samsung_electronics_treasury_cancel_case"]["case_type"], "failed_rerating")
        self.assertEqual(rows["samsung_electronics_treasury_cancel_case"]["target_id"], "TREASURY_SHARE_CANCEL_EXECUTION")
        self.assertEqual(rows["samsung_electronics_treasury_cancel_case"]["stage2_date"], "2026-03-31")
        self.assertEqual(rows["korea_bank_financial_holding_valueup_candidate"]["target_id"], "BANK_HOLDING_VALUEUP_CAPITAL_RETURN")
        self.assertEqual(rows["korea_bank_financial_holding_valueup_candidate"]["stage2_date"], "")
        self.assertEqual(rows["korea_insurance_underwriting_valueup_candidate"]["target_id"], "INSURANCE_UNDERWRITING_CYCLE")
        self.assertEqual(rows["korea_insurance_underwriting_valueup_candidate"]["stage2_date"], "")
        self.assertEqual(rows["samsung_ct_activist_rejection_case"]["stage4c_date"], "")
        self.assertEqual(rows["korea_zinc_tender_offer_event_case"]["target_id"], "EVENT_PREMIUM_GOVERNANCE_BATTLE")
        self.assertEqual(rows["korea_zinc_tender_offer_event_case"]["stage2_date"], "2024-09-13")
        self.assertEqual(rows["korea_zinc_share_issue_probe_case"]["stage4c_date"], "2024-10-31")
        self.assertEqual(rows["korea_capital_gains_tax_scrap_case"]["stage4c_date"], "2025-09-11")
        self.assertEqual(rows["ai_citizen_dividend_policy_shock_case"]["target_id"], "AI_WINDFALL_CITIZEN_DIVIDEND_POLICY_SHOCK")
        self.assertEqual(rows["ai_citizen_dividend_policy_shock_case"]["stage4c_date"], "2026-05-12")
        self.assertEqual(rows["clear_street_ipo_valuation_cut_case"]["target_id"], "FINTECH_IPO_VALUATION_RISK")
        self.assertEqual(rows["clear_street_ipo_valuation_cut_case"]["stage4c_date"], "2026-02-12")
        self.assertEqual(rows["mynt_gcash_ipo_case"]["target_id"], "FINTECH_SUPERAPP_IPO_OPTION")
        self.assertEqual(rows["mynt_gcash_ipo_case"]["stage2_date"], "2026-05-14")
        self.assertEqual(rows["toss_global_stablecoin_case"]["target_id"], "PAYMENT_FINTECH_INFRA")
        self.assertEqual(rows["toss_global_stablecoin_case"]["stage2_date"], "2025-09-09")
        self.assertEqual(rows["circle_usdc_stablecoin_earnings_case"]["stage4b_date"], "2026-05-11")
        self.assertEqual(rows["boe_stablecoin_rules_reconsider_case"]["target_id"], "STABLECOIN_BANK_DEPOSIT_DISINTERMEDIATION")
        self.assertEqual(rows["boe_stablecoin_rules_reconsider_case"]["stage4c_date"], "2026-05-14")
        self.assertEqual(rows["terrausd_do_kwon_case"]["stage4c_date"], "")
        self.assertEqual(rows["hana_bank_dunamu_stake_case"]["target_id"], "BANK_DIGITAL_ASSET_EQUITY_STAKE")
        self.assertEqual(rows["hana_bank_dunamu_stake_case"]["stage2_date"], "2026-05-14")
        self.assertEqual(rows["hana_bank_dunamu_stake_case"]["stage4c_date"], "")
        self.assertEqual(rows["dunamu_naver_financial_merger_option_case"]["target_id"], "DIGITAL_ASSET_EXCHANGE_CONSOLIDATION")
        self.assertEqual(rows["dunamu_naver_financial_merger_option_case"]["stage2_date"], "")
        self.assertEqual(rows["digital_asset_exchange_security_cycle_case"]["case_type"], "4c_thesis_break")

    def test_case_records_validate_and_keep_round98_guardrails(self):
        records = round98_case_records()

        self.assertEqual(len(records), len(ROUND98_CASE_CANDIDATES))
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
        self.assertEqual(by_id["korea_commercial_act_treasury_cancel_case"].primary_archetype, E2RArchetype.TREASURY_CANCEL_MANDATE_POLICY)
        self.assertEqual(by_id["korea_commercial_act_treasury_cancel_case"].price_pattern, "treasury_cancel_policy_tailwind")
        self.assertEqual(by_id["sk_square_buyback_cancel_case"].score_price_alignment, "aligned")
        self.assertEqual(by_id["samsung_electronics_treasury_cancel_case"].score_price_alignment, "evidence_good_but_price_failed")
        self.assertEqual(by_id["korea_bank_financial_holding_valueup_candidate"].price_validation.price_validation_status, "needs_named_case_and_price_backfill")
        self.assertIn("roe", "|".join(by_id["korea_bank_financial_holding_valueup_candidate"].must_have_fields))
        self.assertEqual(by_id["korea_insurance_underwriting_valueup_candidate"].price_validation.price_validation_status, "needs_named_case_and_price_backfill")
        self.assertIn("k_ics_ratio", by_id["korea_insurance_underwriting_valueup_candidate"].must_have_fields)
        self.assertEqual(by_id["korea_zinc_tender_offer_event_case"].rerating_result, "event_premium")
        self.assertEqual(by_id["circle_usdc_stablecoin_earnings_case"].rerating_result, "theme_overheat")
        self.assertEqual(by_id["terrausd_do_kwon_case"].score_price_alignment, "false_positive_score")
        self.assertEqual(by_id["clear_street_ipo_valuation_cut_case"].score_price_alignment, "false_positive_score")
        self.assertIn("ipo_valuation_cut", by_id["clear_street_ipo_valuation_cut_case"].red_flag_fields)
        self.assertIn(E2RArchetype.KRW_STABLECOIN_INFRA_OPTION, by_id["toss_global_stablecoin_case"].secondary_archetypes)
        self.assertIn(E2RArchetype.REGULATED_STABLECOIN_INFRA, by_id["toss_global_stablecoin_case"].secondary_archetypes)
        self.assertIn(E2RArchetype.DIGITAL_ASSET_EXCHANGE_CONSOLIDATION, by_id["hana_bank_dunamu_stake_case"].secondary_archetypes)
        self.assertIn(E2RArchetype.PAYMENT_FINTECH_INFRA, by_id["dunamu_naver_financial_merger_option_case"].secondary_archetypes)

    def test_score_profile_rows_match_round98_weight_table(self):
        rows = {row["target_id"]: row for row in round98_score_profile_rows()}

        self.assertEqual(rows["FINANCIAL_SPREAD_BALANCE_SHEET"]["eps_fcf"], "15")
        self.assertEqual(rows["BANK_HOLDING_VALUEUP_CAPITAL_RETURN"]["structural_visibility"], "21")
        self.assertEqual(rows["INSURANCE_UNDERWRITING_CYCLE"]["structural_visibility"], "21")
        self.assertEqual(rows["SECURITIES_BROKERAGE_CYCLE"]["capital_allocation"], "6")
        self.assertEqual(rows["VALUE_UP_SHAREHOLDER_RETURN"]["capital_allocation"], "12")
        self.assertEqual(rows["TREASURY_SHARE_CANCEL_EXECUTION"]["capital_allocation"], "13")
        self.assertEqual(rows["TREASURY_CANCEL_MANDATE_POLICY"]["eps_fcf"], "10")
        self.assertEqual(rows["HOLDING_RESTRUCTURING_GOVERNANCE"]["market_mispricing"], "22")
        self.assertEqual(rows["EVENT_PREMIUM_GOVERNANCE_BATTLE"]["eps_fcf"], "8")
        self.assertEqual(rows["FINTECH_SUPERAPP_IPO_OPTION"]["valuation"], "10")
        self.assertEqual(rows["KRW_STABLECOIN_INFRA_OPTION"]["information_confidence"], "6")
        self.assertEqual(rows["REGULATED_STABLECOIN_INFRA"]["information_confidence"], "6")
        self.assertEqual(rows["STABLECOIN_BANK_DEPOSIT_DISINTERMEDIATION"]["gate_only"], "true")
        self.assertEqual(rows["BANK_DIGITAL_ASSET_EQUITY_STAKE"]["eps_fcf"], "15")
        self.assertEqual(rows["FINTECH_IPO_VALUATION_RISK"]["valuation"], "6")
        self.assertEqual(rows["ALGORITHMIC_STABLECOIN_FAILURE"]["gate_only"], "true")
        self.assertEqual(rows["TAX_POLICY_MARKET_SHOCK_OVERLAY"]["eps_fcf"], "gate")
        self.assertEqual(rows["AI_WINDFALL_CITIZEN_DIVIDEND_POLICY_SHOCK"]["eps_fcf"], "gate")
        self.assertEqual(rows["STABLECOIN_CONVERTIBILITY_OVERLAY"]["gate_only"], "true")
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round98_stage_date_rows()}
        fields = {row["field"] for row in round98_price_field_rows()}

        self.assertIn("treasury_share_cancellation", rows["VALUE_UP_SHAREHOLDER_RETURN"]["stage2"])
        self.assertIn("treasury_share_cancellation_completed", rows["TREASURY_SHARE_CANCEL_EXECUTION"]["stage2"])
        self.assertIn("treasury_cancel_mandate", rows["TREASURY_CANCEL_MANDATE_POLICY"]["stage1"])
        self.assertIn("tender_offer", rows["EVENT_PREMIUM_GOVERNANCE_BATTLE"]["stage1"])
        self.assertIn("credit_loss_control", rows["FINTECH_SUPERAPP_IPO_OPTION"]["stage2"])
        self.assertIn("won_stablecoin_plan", rows["KRW_STABLECOIN_INFRA_OPTION"]["stage1"])
        self.assertIn("issuer_margin_compression", rows["REGULATED_STABLECOIN_INFRA"]["stage4c"])
        self.assertIn("bank_deposit_outflow", rows["STABLECOIN_BANK_DEPOSIT_DISINTERMEDIATION"]["stage4c"])
        self.assertIn("depeg", rows["ALGORITHMIC_STABLECOIN_FAILURE"]["stage4c"])
        self.assertIn("abnormal_crypto_withdrawal", rows["DIGITAL_ASSET_EXCHANGE_CONSOLIDATION"]["stage4c"])
        self.assertIn("equity_method_income", rows["BANK_DIGITAL_ASSET_EQUITY_STAKE"]["stage3"])
        self.assertIn("ipo_valuation_cut", rows["FINTECH_IPO_VALUATION_RISK"]["stage4c"])
        self.assertIn("tax_policy_shock", rows["TAX_POLICY_MARKET_SHOCK_OVERLAY"]["stage4c"])
        self.assertIn("citizen_dividend_policy_shock", rows["AI_WINDFALL_CITIZEN_DIVIDEND_POLICY_SHOCK"]["stage4c"])
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
            "treasury_share_cancel_execution_date",
            "treasury_share_cancel_required_flag",
            "treasury_cancel_mandate_flag",
            "existing_treasury_grace_period_flag",
            "buyback_only_flag",
            "nav_discount",
            "activist_proposal_rejection_flag",
            "share_issuance_after_tender_flag",
            "unfair_trading_probe_flag",
            "capital_gains_tax_threshold_change_flag",
            "securities_transaction_tax_hike_flag",
            "dividend_tax_change_flag",
            "dividend_tax_uncertainty_flag",
            "ai_windfall_tax_comment_flag",
            "citizen_dividend_comment_flag",
            "payment_volume",
            "take_rate",
            "ipo_timeline_status",
            "ipo_size_cut_flag",
            "ipo_valuation_cut_flag",
            "crypto_exposure_flag",
            "stablecoin_transaction_volume",
            "stablecoin_circulation",
            "reserve_income",
            "reserve_yield",
            "reserve_asset_type",
            "redemption_at_par_flag",
            "user_cap_flag",
            "unremunerated_reserve_requirement_flag",
            "krw_stablecoin_flag",
            "bank_deposit_disintermediation_flag",
            "crypto_exchange_market_share",
            "equity_stake_purchase_amount",
            "equity_method_income",
            "bank_exchange_partnership_flag",
            "strategic_collaboration_revenue",
            "fintech_exchange_merger_flag",
            "share_swap_ratio",
            "regulatory_approval_status",
            "shareholder_approval_status",
            "abnormal_withdrawal_flag",
            "deal_dilution_flag",
            "opendart_rcept_no",
            "disclosure_confidence_score",
            "detail_parser_confidence",
            "disclosure_signal_class",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND98_PRICE_FIELDS))

    def test_summary_and_markdown_explain_r6_loop5_guardrails(self):
        summary = round98_summary()
        summary_md = render_round98_summary_markdown()
        guardrails = render_round98_green_guardrail_markdown()
        overlays = render_round98_risk_overlay_markdown()
        price_plan = render_round98_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 25)
        self.assertEqual(summary["case_candidate_count"], 19)
        self.assertEqual(summary["success_candidate_count"], 8)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["stage4b_case_count"], 1)
        self.assertEqual(summary["stage4c_case_count"], 8)
        self.assertEqual(summary["green_possible_count"], 3)
        self.assertEqual(summary["watch_yellow_first_count"], 13)
        self.assertEqual(summary["redteam_first_count"], 9)
        self.assertEqual(summary["gate_only_target_count"], 6)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("R6 Loop 5", summary_md)
        self.assertIn("Do not apply R6 Loop-5 v5.0 weights", guardrails)
        self.assertIn("TREASURY_CANCEL_POLICY_ONLY", overlays)
        self.assertIn("FINTECH_IPO_VALUATION_COMPRESSION", overlays)
        self.assertIn("KRW_STABLECOIN_OPTION_NOT_REVENUE", overlays)
        self.assertIn("STABLECOIN_REGULATION_FLUID_WATCH", overlays)
        self.assertIn("AI_CITIZEN_DIVIDEND_POLICY_SHOCK", overlays)
        self.assertIn("DIGITAL_ASSET_EXCHANGE_SECURITY_4C", overlays)
        self.assertIn("BANK_DIGITAL_ASSET_STAKE_WATCH", overlays)
        self.assertIn("circle_usdc_stablecoin_earnings_case", price_plan)
        self.assertIn("hana_bank_dunamu_stake_case", price_plan)
        self.assertIn("dunamu_naver_financial_merger_option_case", price_plan)
        self.assertIn("clear_street_ipo_valuation_cut_case", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round98_r6_loop5_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r6_loop5_round98.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round98_r6_loop5_v5.csv",
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
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND98_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round98_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round98_r6_loop5_financial_capital_digital", text)


if __name__ == "__main__":
    unittest.main()
