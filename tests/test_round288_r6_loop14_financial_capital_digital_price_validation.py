from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round288_r6_loop14_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round288_r6_loop14_financial_capital_digital_price_validation import (
    ROUND288_CASE_CANDIDATES,
    ROUND288_GREEN_FORBIDDEN_PATTERNS,
    ROUND288_GREEN_REQUIRED_FIELDS,
    ROUND288_HARD_4C_GATES,
    ROUND288_LARGE_SECTOR,
    ROUND288_PRICE_VALIDATION_FIELDS,
    ROUND288_REQUIRED_TARGET_ALIASES,
    ROUND288_SCORE_ADJUSTMENTS,
    ROUND288_SHADOW_WEIGHT_ROWS,
    ROUND288_STAGE4B_WATCH_TRIGGERS,
    render_round288_green_gate_review_markdown,
    render_round288_stage4b_4c_review_markdown,
    round288_audit_payload,
    round288_case_records,
    round288_deep_sub_archetype_rows,
    round288_shadow_weight_rows,
    round288_summary,
    write_round288_r6_loop14_reports,
)


class Round288R6Loop14FinancialCapitalDigitalPriceValidationTests(unittest.TestCase):
    def test_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND288_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND288_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND288_REQUIRED_TARGET_ALIASES["VALUE_UP_FINANCIAL_HOLDING_STAGE2"],
            E2RArchetype.VALUE_UP_FINANCIAL_HOLDING_STAGE2.value,
        )
        self.assertEqual(
            ROUND288_REQUIRED_TARGET_ALIASES["PRIVATE_CAPITAL_CB_STABLECOIN_EVENT_PREMIUM"],
            E2RArchetype.PRIVATE_CAPITAL_CB_STABLECOIN_EVENT_PREMIUM.value,
        )

    def test_archetype_definitions_encode_round288_gates(self) -> None:
        valueup = archetype_definition(E2RArchetype.VALUE_UP_FINANCIAL_HOLDING_STAGE2)
        holdco = archetype_definition(E2RArchetype.HOLDCO_DISCOUNT_BUYBACK_STAGE2)
        proposal = archetype_definition(E2RArchetype.SHAREHOLDER_RETURN_FAILURE_FALSE_POSITIVE)
        ipo = archetype_definition(E2RArchetype.DIGITAL_BANK_IPO_QUALITY_GATE)
        control = archetype_definition(E2RArchetype.DIGITAL_BANK_CONTROL_RISK_4C_WATCH)
        ma = archetype_definition(E2RArchetype.DIGITAL_ASSET_MA_TRUST_4C_WATCH)
        bank_stake = archetype_definition(E2RArchetype.BANK_DIGITAL_ASSET_STAKE_STAGE2)
        cb = archetype_definition(E2RArchetype.PRIVATE_CAPITAL_CB_STABLECOIN_EVENT_PREMIUM)

        self.assertIn("CET1 buffer", valueup.stage3_high_conviction_signals)
        self.assertIn("actual payout and treasury-share cancellation", valueup.stage3_high_conviction_signals)
        self.assertIn("discount compression", holdco.stage3_high_conviction_signals)
        self.assertIn("shareholder-return proposal failure", proposal.stage4c_thesis_break_signals)
        self.assertIn("IPO size or customer count only", ipo.false_positive_patterns)
        self.assertIn("bank ownership loss due financial-crime conviction", control.stage4c_thesis_break_signals)
        self.assertIn("abnormal withdrawal or custody failure", ma.stage4c_thesis_break_signals)
        self.assertIn("capital treatment", bank_stake.stage3_high_conviction_signals)
        self.assertIn("dilution-adjusted ROIC", cb.stage3_high_conviction_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round288_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND288_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("hard_4c_not_confirmed_true", record.green_guardrails)
            self.assertIn("do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist", record.green_guardrails)

        summary = round288_summary()
        self.assertEqual(summary["round_id"], "round_216")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 4)
        self.assertEqual(summary["event_premium_count"], 2)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 7)
        self.assertEqual(summary["stage4c_watch_count"], 4)
        self.assertEqual(summary["price_moved_without_evidence_count"], 2)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertFalse(summary["hard_4c_confirmed"])
        self.assertTrue(summary["hard_4c_not_confirmed"])

    def test_financial_capital_and_digital_cases_capture_round_anchors(self) -> None:
        by_id = {case.case_id: case for case in ROUND288_CASE_CANDIDATES}
        valueup = by_id["r6_loop14_financial_holding_value_up_policy_stage2"]
        sk_square = by_id["r6_loop14_sk_square_holdco_discount_buyback"]
        samsung_ct = by_id["r6_loop14_samsung_ct_activist_valueup_failure"]
        kbank = by_id["r6_loop14_kbank_digital_bank_ipo_quality_gate"]
        kakaobank = by_id["r6_loop14_kakaobank_control_risk_kakao_founder"]
        naver = by_id["r6_loop14_naver_financial_dunamu_upbit_trust_gate"]
        hana = by_id["r6_loop14_hana_bank_dunamu_digital_asset_stake"]
        sds = by_id["r6_loop14_samsung_sds_kkr_cb_stablecoin_event"]

        self.assertEqual(valueup.extra_price_metrics["treasury_share_new_cancellation_deadline_years"], 1)
        self.assertEqual(valueup.extra_price_metrics["existing_treasury_share_grace_period_months"], 6)
        self.assertIn("CET1 buffer", valueup.extra_price_metrics["stage3_conditions"])

        self.assertEqual(sk_square.extra_price_metrics["total_announced_cancellation_related_krw_bn"], 200)
        self.assertEqual(sk_square.extra_price_metrics["sk_hynix_stake_pct"], 20)
        self.assertEqual(sk_square.extra_price_metrics["sk_hynix_stake_value_usd_bn_context"], 18)
        self.assertTrue(sk_square.extra_price_metrics["market_value_less_than_half_stake_value"])

        self.assertEqual(samsung_ct.extra_price_metrics["event_mae_pct"], -10.0)
        self.assertFalse(samsung_ct.extra_price_metrics["proposal_passed"])

        self.assertEqual(kbank.extra_price_metrics["ipo_raise_max_krw_bn"], 984)
        self.assertEqual(kbank.extra_price_metrics["shares_to_sell_mn"], 82)
        self.assertEqual(kbank.extra_price_metrics["valuation_max_krw_trn"], 5)
        self.assertEqual(kbank.extra_price_metrics["h1_2024_operating_profit_krw_bn"], 86.7)
        self.assertEqual(kbank.extra_price_metrics["customer_count_context_mn"], 10)

        self.assertEqual(kakaobank.extra_price_metrics["kakao_event_mae_pct"], -3.4)
        self.assertEqual(kakaobank.extra_price_metrics["kakao_ytd_decline_context_pct"], -24)
        self.assertEqual(kakaobank.extra_price_metrics["founder_affiliated_stake_pct"], 24)
        self.assertEqual(kakaobank.extra_price_metrics["bank_ownership_limit_if_financial_crime_conviction_pct"], 10)
        self.assertTrue(kakaobank.extra_price_metrics["acquittal_relief"])

        self.assertEqual(naver.extra_price_metrics["deal_value_krw_trn"], 15.13)
        self.assertEqual(naver.extra_price_metrics["event_initial_mfe_pct"], 7.0)
        self.assertEqual(naver.extra_price_metrics["event_later_mae_pct"], -4.2)
        self.assertEqual(naver.extra_price_metrics["abnormal_withdrawal_krw_bn"], 54)

        self.assertEqual(hana.extra_price_metrics["stake_purchase_krw_trn"], 1.0)
        self.assertEqual(hana.extra_price_metrics["dunamu_stake_acquired_pct"], 6.55)
        self.assertEqual(hana.extra_price_metrics["implied_dunamu_equity_value_krw_trn"], 15.27)
        self.assertEqual(hana.extra_price_metrics["upbit_trading_volume_share_context_pct"], 80)

        self.assertEqual(sds.extra_price_metrics["kkr_cb_investment_usd_mn"], 820)
        self.assertEqual(sds.extra_price_metrics["event_intraday_mfe_pct"], 20.8)
        self.assertEqual(sds.extra_price_metrics["relative_outperformance_intraday_pp"], 17.8)
        self.assertFalse(sds.extra_price_metrics["stablecoin_revenue_confirmed"])

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND288_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND288_GREEN_FORBIDDEN_PATTERNS)
        review = render_round288_green_gate_review_markdown()
        stage_review = render_round288_stage4b_4c_review_markdown()
        fields = set(ROUND288_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND288_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round288_shadow_weight_rows()}
        deep_rows = round288_deep_sub_archetype_rows()

        self.assertIn("cet1_capital_buffer_confirmed", required)
        self.assertIn("digital_asset_custody_control_confirmed", required)
        self.assertIn("cb_dilution_adjusted_roic_confirmed", required)
        self.assertIn("Value_Up_headline_only", forbidden)
        self.assertIn("M&A_synergy_without_custody_control", forbidden)
        self.assertIn("stablecoin_keyword_without_revenue", forbidden)
        self.assertIn("CET1_capital_buffer", axes)
        self.assertIn("founder_legal_risk_unresolved", axes)
        self.assertIn("stake_percent_anchor", fields)
        self.assertIn("PE_CB_investment_plus_15_to_20pct", ROUND288_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("abnormal_withdrawal_or_custody_failure", ROUND288_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("strong watch", stage_review)
        self.assertEqual(len(ROUND288_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["VALUE_UP_FINANCIAL_HOLDING_STAGE2"]["cet1_capital_buffer"], "+5")
        self.assertEqual(shadow_rows["DIGITAL_ASSET_MA_TRUST_4C_WATCH"]["digital_asset_custody_control"], "+5")
        self.assertEqual(shadow_rows["PRIVATE_CAPITAL_CB_STABLECOIN_EVENT_PREMIUM"]["cb_dilution_adjusted_roic"], "+5")
        self.assertTrue(any("SK Square" in row["terms"] for row in deep_rows))
        self.assertTrue(any("K Bank" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Samsung SDS" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round288_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_288.md")
        self.assertEqual(audit["round_id"], "round_216")
        self.assertEqual(audit["large_sector"], ROUND288_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertFalse(audit["summary"]["hard_4c_confirmed"])
        self.assertTrue(audit["summary"]["hard_4c_not_confirmed"])
        self.assertEqual(len(audit["shadow_weights"]), 8)
        self.assertEqual(len(audit["deep_sub_archetypes"]), 8)
        self.assertIn("do_not_use_round288_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round288_r6_loop14_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)
            loaded = load_case_library(root / "cases.jsonl")
            self.assertEqual(len(loaded), 8)
            self.assertIn(
                "Naver/Dunamu",
                (root / "out" / "round288_r6_loop14_price_validation_summary.md").read_text(encoding="utf-8"),
            )


if __name__ == "__main__":
    unittest.main()
