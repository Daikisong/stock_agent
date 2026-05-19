import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round197_r6_loop7_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round197_r6_loop7_financial_capital_digital_price_validation import (
    ROUND197_CASE_CANDIDATES,
    ROUND197_GREEN_FORBIDDEN_PATTERNS,
    ROUND197_GREEN_REQUIRED_FIELDS,
    ROUND197_HARD_4C_GATES,
    ROUND197_PRICE_BACKFILL_FIELDS,
    ROUND197_REQUIRED_TARGET_ALIASES,
    render_round197_green_gate_review_markdown,
    render_round197_stage4b_4c_review_markdown,
    round197_audit_payload,
    round197_case_records,
    round197_case_rows,
    round197_price_backfill_field_rows,
    round197_score_adjustment_rows,
    round197_summary,
    write_round197_r6_loop7_reports,
)


class Round197R6Loop7FinancialCapitalDigitalPriceValidationTests(unittest.TestCase):
    def test_round197_targets_are_existing_canonical_archetypes(self):
        self.assertGreaterEqual(len(ROUND197_REQUIRED_TARGET_ALIASES), 16)
        self.assertEqual(
            ROUND197_REQUIRED_TARGET_ALIASES["FINANCIAL_SPREAD_BALANCE_SHEET"],
            E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET.value,
        )
        self.assertEqual(
            ROUND197_REQUIRED_TARGET_ALIASES["DIGITAL_ASSET_BANK_EQUITY_OPTION"],
            E2RArchetype.DIGITAL_ASSET_BANK_EQUITY_OPTION.value,
        )
        self.assertEqual(
            ROUND197_REQUIRED_TARGET_ALIASES["STABLECOIN_CONVERTIBILITY_OVERLAY"],
            E2RArchetype.STABLECOIN_CONVERTIBILITY_OVERLAY.value,
        )
        for canonical in ROUND197_REQUIRED_TARGET_ALIASES.values():
            self.assertIsInstance(E2RArchetype(canonical), E2RArchetype)

    def test_case_records_validate_and_remain_shadow_only(self):
        records = {record.case_id: record for record in round197_case_records()}

        self.assertEqual(len(records), 7)
        self.assertEqual(records["sk_square_valueup_buyback_nav_discount_stage2_4b_watch"].case_type, "structural_success")
        self.assertEqual(records["hana_financial_dunamu_equity_option_stage2_watch"].case_type, "success_candidate")
        self.assertEqual(records["kakaopay_aton_krw_stablecoin_policy_theme_overheat"].case_type, "overheat")
        self.assertEqual(records["kakaopay_privacy_data_transfer_fine_payment_4c_break"].case_type, "4c_thesis_break")
        for record in records.values():
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertEqual(record.price_validation.price_validation_status, "needs_ohlc_backfill")

    def test_valueup_and_digital_asset_cases_are_stage2_not_forced_green(self):
        rows = {row["case_id"]: row for row in round197_case_rows()}
        sk_square = rows["sk_square_valueup_buyback_nav_discount_stage2_4b_watch"]
        hana = rows["hana_financial_dunamu_equity_option_stage2_watch"]

        self.assertEqual(sk_square["stage2_date"], "2024-11-21")
        self.assertEqual(sk_square["stage3_date"], "")
        self.assertEqual(sk_square["stage4b_status"], "watch")
        self.assertIn("skhynix_price_dependency", sk_square["red_flag_fields"])
        self.assertEqual(hana["stage2_date"], "2026-05-14")
        self.assertEqual(hana["stage3_date"], "")
        self.assertIn("equity_method_income", hana["stage3_decision"])
        self.assertIn("stablecoin_forex_concern", hana["red_flag_fields"])

    def test_insurance_nav_and_bank_expansion_require_capital_quality(self):
        rows = {row["case_id"]: row for row in round197_case_rows()}
        samsung_life = rows["samsung_life_nav_valueup_forced_stake_sale_regulatory_watch"]
        woori = rows["woori_financial_valueup_nonbank_expansion_capital_buffer_watch"]

        self.assertEqual(samsung_life["stage2_date"], "2026-03-19")
        self.assertEqual(samsung_life["stage3_date"], "")
        self.assertIn("forced_sale_or_regulatory_overhang", samsung_life["red_flag_fields"])
        self.assertEqual(woori["stage3_date"], "")
        self.assertIn("cet1_unverified", woori["red_flag_fields"])
        self.assertIn("credit_cost", woori["stage3_decision"])

    def test_fintech_governance_privacy_and_stablecoin_theme_block_green(self):
        rows = {row["case_id"]: row for row in round197_case_rows()}
        kakaobank = rows["kakaobank_internet_bank_governance_ownership_4c_watch"]
        stablecoin = rows["kakaopay_aton_krw_stablecoin_policy_theme_overheat"]
        privacy = rows["kakaopay_privacy_data_transfer_fine_payment_4c_break"]

        self.assertEqual(kakaobank["stage4c_date"], "2024-07-22")
        self.assertEqual(kakaobank["hard_4c_confirmed"], "true")
        self.assertIn("major_shareholder_legal_risk", kakaobank["red_flag_fields"])
        self.assertEqual(stablecoin["stage1_date"], "2025-06-18")
        self.assertEqual(stablecoin["stage4b_date"], "2025-06-18")
        self.assertEqual(stablecoin["score_price_alignment"], "price_moved_without_evidence")
        self.assertEqual(privacy["case_type"], "4c_thesis_break")
        self.assertEqual(privacy["hard_4c_confirmed"], "true")
        self.assertIn("privacy_data_trust_break", privacy["red_flag_fields"])

    def test_green_gate_requires_roe_capital_return_and_blocks_policy_buzz(self):
        required = set(ROUND197_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND197_GREEN_FORBIDDEN_PATTERNS)
        adjustments = {row["axis"]: row for row in round197_score_adjustment_rows()}
        markdown = render_round197_green_gate_review_markdown()

        self.assertIn("roe_structurally_improving_or_sustained", required)
        self.assertIn("cet1_or_kics_capital_buffer", required)
        self.assertIn("actual_buyback_cancellation", required)
        self.assertIn("credit_cost_pf_risk_passed", required)
        self.assertIn("low_pbr_only", forbidden)
        self.assertIn("stablecoin_policy_theme_only", forbidden)
        self.assertIn("privacy_or_data_trust_break", forbidden)
        self.assertEqual(adjustments["real_buyback_cancellation"]["points"], "5")
        self.assertEqual(adjustments["stablecoin_policy_theme_only"]["points"], "-5")
        self.assertIn("Do not apply these weights to production scoring yet", markdown)

    def test_price_backfill_fields_include_r6_quality_inputs(self):
        fields = {row["field"] for row in round197_price_backfill_field_rows()}

        self.assertGreaterEqual(len(ROUND197_PRICE_BACKFILL_FIELDS), 50)
        for field in (
            "roe",
            "cet1_ratio",
            "kics_ratio",
            "credit_cost",
            "pf_exposure",
            "buyback_cancelled",
            "dividend_payout_ratio",
            "pbr_roe_gap",
            "equity_method_income",
            "privacy_data_trust_break_flag",
            "hard_4c_confirmed",
        ):
            self.assertIn(field, fields)

    def test_stage4b_4c_review_contains_financial_hard_gates(self):
        review = render_round197_stage4b_4c_review_markdown()

        self.assertIn("pf_credit_cost_spike", ROUND197_HARD_4C_GATES)
        self.assertIn("cet1_or_kics_weakening", ROUND197_HARD_4C_GATES)
        self.assertIn("privacy_data_transfer_fine", ROUND197_HARD_4C_GATES)
        self.assertIn("stablecoin_forex_risk_regulation_tightening", ROUND197_HARD_4C_GATES)
        self.assertIn("kakaobank_internet_bank_governance_ownership_4c_watch", review)

    def test_summary_and_audit_payload_are_calibration_only(self):
        summary = round197_summary()
        payload = round197_audit_payload()

        self.assertEqual(summary["case_candidate_count"], len(ROUND197_CASE_CANDIDATES))
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage3_conditional_candidate_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertIn("do_not_use_round197_cases_as_candidate_generation_input", payload["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self):
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])

        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = write_round197_r6_loop7_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)
            records = load_case_library(root / "cases.jsonl")
            self.assertEqual(len(records), 7)
            self.assertIn("Stage 3-Green", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("real_buyback_cancellation", paths["score_adjustments"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
