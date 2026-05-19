from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round210_r6_loop8_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round210_r6_loop8_financial_capital_digital_price_validation import (
    ROUND210_CASE_CANDIDATES,
    ROUND210_GREEN_FORBIDDEN_PATTERNS,
    ROUND210_GREEN_REQUIRED_FIELDS,
    ROUND210_HARD_4C_GATES,
    ROUND210_PRICE_VALIDATION_FIELDS,
    ROUND210_REQUIRED_TARGET_ALIASES,
    ROUND210_SCORE_ADJUSTMENTS,
    ROUND210_STAGE4B_WATCH_TRIGGERS,
    render_round210_green_gate_review_markdown,
    render_round210_stage4b_4c_review_markdown,
    round210_audit_payload,
    round210_case_records,
    round210_case_rows,
    round210_summary,
    write_round210_r6_loop8_reports,
)


class Round210R6Loop8FinancialCapitalDigitalPriceValidationTests(unittest.TestCase):
    def test_round210_targets_are_existing_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertGreaterEqual(len(ROUND210_REQUIRED_TARGET_ALIASES), 16)
        self.assertTrue(set(ROUND210_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND210_REQUIRED_TARGET_ALIASES["VALUE_UP_SHAREHOLDER_RETURN"],
            E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN.value,
        )
        self.assertEqual(
            ROUND210_REQUIRED_TARGET_ALIASES["PAYMENT_PRIVACY_REGULATORY_4C"],
            E2RArchetype.PAYMENT_PRIVACY_REGULATORY_4C.value,
        )

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round210_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)

        summary = round210_summary()
        self.assertEqual(summary["case_candidate_count"], 7)
        self.assertEqual(summary["success_candidate_count"], 3)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["thesis_break_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["full_ohlc_complete"])

    def test_sk_square_valueup_requires_real_cancellation_and_discount_narrowing(self) -> None:
        by_id = {case.case_id: case for case in ROUND210_CASE_CANDIDATES}
        sk_square = by_id["r6_loop8_sk_square_valueup_nav_discount"]

        self.assertEqual(sk_square.primary_archetype, E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN)
        self.assertEqual(sk_square.stage2_date.isoformat(), "2024-11-21")
        self.assertIsNone(sk_square.stage3_date)
        self.assertEqual(sk_square.stage4b_date.isoformat(), "2026-05-14")
        self.assertEqual(sk_square.extra_price_metrics["total_announced_buyback_cancel_krw_bn"], 200.0)
        self.assertEqual(sk_square.extra_price_metrics["discount_to_sk_hynix_exposure_pct"], 47.0)
        self.assertIn("discount_narrowing_price_path_unverified", sk_square.red_flag_fields)

    def test_hana_and_samsung_life_are_stage2_until_capital_quality_confirms(self) -> None:
        by_id = {case.case_id: case for case in ROUND210_CASE_CANDIDATES}
        hana = by_id["r6_loop8_hana_dunamu_equity_option"]
        samsung_life = by_id["r6_loop8_samsung_life_nav_valueup"]

        self.assertEqual(hana.primary_archetype, E2RArchetype.DIGITAL_ASSET_BANK_EQUITY_OPTION)
        self.assertEqual(hana.stage2_date.isoformat(), "2026-05-14")
        self.assertIsNone(hana.stage3_date)
        self.assertEqual(hana.extra_price_metrics["implied_dunamu_value_krw_trn"], 15.31)
        self.assertIn("capital_ratio_impact_unverified", hana.red_flag_fields)

        self.assertEqual(samsung_life.primary_archetype, E2RArchetype.INSURANCE_NAV_VALUEUP_SAMSUNG_ELECTRONICS_STAKE)
        self.assertEqual(samsung_life.stage2_date.isoformat(), "2026-03-19")
        self.assertEqual(samsung_life.extra_price_metrics["implied_book_discount_pct"], 50.0)
        self.assertIn("kics_csm_unverified", samsung_life.red_flag_fields)

    def test_naver_dunamu_is_event_premium_with_exchange_trust_watch(self) -> None:
        by_id = {case.case_id: case for case in ROUND210_CASE_CANDIDATES}
        naver = by_id["r6_loop8_naver_dunamu_digital_asset_event"]

        self.assertEqual(naver.primary_archetype, E2RArchetype.DIGITAL_ASSET_TOKENIZATION)
        self.assertEqual(naver.case_type, "event_premium")
        self.assertEqual(naver.stage2_date.isoformat(), "2025-11-27")
        self.assertEqual(naver.stage4b_date.isoformat(), "2025-11-27")
        self.assertEqual(naver.stage4c_date.isoformat(), "2025-11-27")
        self.assertEqual(naver.mfe_1d, 7.0)
        self.assertEqual(naver.mae_1d, -4.2)
        self.assertEqual(naver.extra_price_metrics["event_swing_pp"], -11.2)
        self.assertIn("abnormal_withdrawal_54bn_krw", naver.red_flag_fields)

    def test_kakao_governance_stablecoin_and_privacy_block_green(self) -> None:
        rows = {row["case_id"]: row for row in round210_case_rows()}
        governance = rows["r6_loop8_kakaobank_kakao_governance_watch"]
        stablecoin = rows["r6_loop8_stablecoin_theme_overheat"]
        privacy = rows["r6_loop8_kakao_pay_privacy_4c_watch"]

        self.assertEqual(governance["case_type"], "failed_rerating")
        self.assertEqual(governance["stage4c_date"], "2024-07-23")
        self.assertEqual(governance["hard_4c_confirmed"], "true")
        self.assertIn("major_shareholder_legal_risk", governance["red_flag_fields"])

        self.assertEqual(stablecoin["case_type"], "overheat")
        self.assertEqual(stablecoin["stage4b_date"], "2025-06-01")
        self.assertEqual(stablecoin["score_price_alignment"], "price_moved_without_evidence")
        self.assertIn("stablecoin_policy_theme_only", stablecoin["red_flag_fields"])

        self.assertEqual(privacy["case_type"], "4c_thesis_break")
        self.assertEqual(privacy["hard_4c_confirmed"], "true")
        self.assertIn("privacy_data_trust_break", privacy["red_flag_fields"])

    def test_green_gate_and_4c_rules_are_explicit(self) -> None:
        required = set(ROUND210_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND210_GREEN_FORBIDDEN_PATTERNS)
        review = render_round210_green_gate_review_markdown()
        stage_review = render_round210_stage4b_4c_review_markdown()

        self.assertIn("roe_improvement_or_sustainability", required)
        self.assertIn("cet1_or_kics_capital_buffer", required)
        self.assertIn("actual_buyback_cancellation", required)
        self.assertIn("stablecoin_policy_theme_only", forbidden)
        self.assertIn("privacy_or_data_trust_break", forbidden)
        self.assertIn("major_shareholder_legal_risk", forbidden)
        self.assertIn("privacy_data_transfer_fine", ROUND210_HARD_4C_GATES)
        self.assertIn("stablecoin_theme_two_to_three_x_without_revenue", ROUND210_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("r6_loop8_kakao_pay_privacy_4c_watch", stage_review)

    def test_price_validation_fields_and_score_adjustments_cover_r6_axes(self) -> None:
        fields = set(ROUND210_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND210_SCORE_ADJUSTMENTS}

        self.assertIn("discount_to_nav_or_book", fields)
        self.assertIn("transaction_value", fields)
        self.assertIn("event_swing_pp", fields)
        self.assertIn("reported_theme_basket_return", fields)
        self.assertIn("roe_sustainability", axes)
        self.assertIn("real_buyback_cancellation", axes)
        self.assertIn("stablecoin_policy_theme_only", axes)
        self.assertIn("privacy_or_data_trust_break", axes)

    def test_summary_and_audit_payload_keep_non_production_guardrails(self) -> None:
        audit = round210_audit_payload()

        self.assertEqual(audit["source_round"], "docs/round/round_210.md")
        self.assertEqual(audit["large_sector"], Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL.value)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round210_cases_as_candidate_generation_input", audit["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round210_r6_loop8_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round210_case_rows()
            self.assertEqual(len(records), len(ROUND210_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND210_CASE_CANDIDATES))
            self.assertIn("SK스퀘어", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("real_buyback_cancellation", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("privacy_data_transfer_fine", paths["stage4b_4c_review"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[1]["extra_price_metrics"])["implied_dunamu_value_krw_trn"], 15.31)


if __name__ == "__main__":
    unittest.main()
