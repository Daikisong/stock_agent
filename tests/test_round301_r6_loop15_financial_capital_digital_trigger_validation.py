from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round301_r6_loop15_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round301_r6_loop15_financial_capital_digital_trigger_validation import (
    ROUND301_CASE_CANDIDATES,
    ROUND301_GREEN_BLOCKERS,
    ROUND301_HARD_4C_GATES,
    ROUND301_LARGE_SECTOR,
    ROUND301_REQUIRED_TARGET_ALIASES,
    ROUND301_SCORE_DOWN_AXES,
    ROUND301_SCORE_UP_AXES,
    ROUND301_SHADOW_WEIGHT_ROWS,
    ROUND301_STAGE2_ACTIONABLE_RULES,
    ROUND301_STAGE3_GREEN_RULES,
    ROUND301_STAGE3_YELLOW_RULES,
    ROUND301_STAGE4B_WATCH_TRIGGERS,
    ROUND301_TRIGGER_RECORDS,
    render_round301_stage_rules_markdown,
    render_round301_stage4b_4c_review_markdown,
    render_round301_trigger_grid_markdown,
    round301_audit_payload,
    round301_case_records,
    round301_case_rows,
    round301_shadow_weight_rows,
    round301_summary,
    round301_trigger_rows,
    write_round301_r6_loop15_reports,
)


class Round301R6Loop15FinancialCapitalDigitalTriggerValidationTests(unittest.TestCase):
    def test_round301_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND301_REQUIRED_TARGET_ALIASES), 9)
        self.assertTrue(set(ROUND301_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND301_REQUIRED_TARGET_ALIASES["BROKERAGE_MARKET_VOLUME_STAGE2_ACTIONABLE"],
            E2RArchetype.BROKERAGE_MARKET_VOLUME_STAGE2_ACTIONABLE.value,
        )
        self.assertEqual(
            ROUND301_REQUIRED_TARGET_ALIASES["STABLECOIN_POLICY_4B_OVERHEAT"],
            E2RArchetype.STABLECOIN_POLICY_4B_OVERHEAT.value,
        )
        self.assertEqual(
            ROUND301_REQUIRED_TARGET_ALIASES["KAKAO_BANK_CONTROL_REGULATORY_4C"],
            E2RArchetype.KAKAO_BANK_CONTROL_REGULATORY_4C.value,
        )

    def test_archetype_definitions_capture_r6_loop15_rules(self) -> None:
        brokerage = archetype_definition(E2RArchetype.BROKERAGE_MARKET_VOLUME_STAGE2_ACTIONABLE)
        valueup = archetype_definition(E2RArchetype.FINANCIAL_GROUP_VALUEUP_STAGE2)
        buyback = archetype_definition(E2RArchetype.BUYBACK_CAPITAL_ALLOCATION_STAGE2_ACTIONABLE)
        holdco = archetype_definition(E2RArchetype.HOLDCO_DISCOUNT_ACTIVIST_STAGE2)
        digital_bank = archetype_definition(E2RArchetype.DIGITAL_ASSET_BANK_ENTRY_STAGE2)
        crypto_ma = archetype_definition(E2RArchetype.CRYPTO_EXCHANGE_MA_STAGE2_WITH_SECURITY_4C)
        stablecoin = archetype_definition(E2RArchetype.STABLECOIN_POLICY_4B_OVERHEAT)
        data_governance = archetype_definition(E2RArchetype.FINTECH_DATA_GOVERNANCE_4C)
        kakao_control = archetype_definition(E2RArchetype.KAKAO_BANK_CONTROL_REGULATORY_4C)

        self.assertIn("daily trading value", " ".join(brokerage.stage2_candidate_signals))
        self.assertIn("CET1", " ".join(valueup.stage3_high_conviction_signals))
        self.assertIn("immediate cancellation", " ".join(buyback.stage2_candidate_signals))
        self.assertIn("measurable NAV discount", " ".join(holdco.stage2_candidate_signals))
        self.assertIn("capital-ratio impact", " ".join(digital_bank.stage3_high_conviction_signals))
        self.assertIn("abnormal withdrawal", " ".join(crypto_ma.stage4c_thesis_break_signals))
        self.assertIn("related stocks double or triple", " ".join(stablecoin.stage4b_graduation_overheat_signals))
        self.assertIn("data-sharing restriction", " ".join(data_governance.stage4c_thesis_break_signals))
        self.assertIn("bank ownership cap violation", " ".join(kakao_control.stage4c_thesis_break_signals))

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round301_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND301_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round301_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("do_not_treat_policy_buyback_ma_or_market_share_headline_as_green", record.green_guardrails)
            self.assertIn("hard_4c_confirmed_false", record.green_guardrails)

        summary = round301_summary()
        self.assertEqual(summary["round_id"], "round_229")
        self.assertEqual(summary["large_sector"], ROUND301_LARGE_SECTOR)
        self.assertEqual(summary["method"], "trigger_level_backtest_v1")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 8)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 4)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 3)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertEqual(summary["missed_structural_count"], 2)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_separate_execution_from_headline(self) -> None:
        by_id = {case.case_id: case for case in ROUND301_CASE_CANDIDATES}
        brokerage = by_id["r6_loop15_brokerage_kospi_liquidity_boom"]
        valueup = by_id["r6_loop15_financial_group_valueup_basket"]
        samsung = by_id["r6_loop15_samsung_buyback_capital_allocation"]
        sk_square = by_id["r6_loop15_sk_square_activist_buyback"]
        hana = by_id["r6_loop15_hana_dunamu_digital_asset_entry"]
        naver = by_id["r6_loop15_naver_financial_dunamu_ma_security"]
        stablecoin = by_id["r6_loop15_stablecoin_policy_fintech_frenzy"]
        kakao = by_id["r6_loop15_kakao_founder_kakaobank_control_risk"]

        self.assertEqual(brokerage.primary_archetype, E2RArchetype.BROKERAGE_MARKET_VOLUME_STAGE2_ACTIONABLE)
        self.assertEqual(brokerage.extra_price_metrics["securities_firms_index_return_pct"], 13.5)
        self.assertIn("daily_trading_value_missing", brokerage.red_flag_fields)

        self.assertEqual(valueup.primary_archetype, E2RArchetype.FINANCIAL_GROUP_VALUEUP_STAGE2)
        self.assertIn("CET1_ratio_missing", valueup.red_flag_fields)

        self.assertEqual(samsung.primary_archetype, E2RArchetype.BUYBACK_CAPITAL_ALLOCATION_STAGE2_ACTIONABLE)
        self.assertEqual(samsung.extra_price_metrics["immediate_buyback_cancel_krw_trn"], 3)
        self.assertEqual(samsung.event_mfe_pct, 7.2)

        self.assertEqual(sk_square.primary_archetype, E2RArchetype.HOLDCO_DISCOUNT_ACTIVIST_STAGE2)
        self.assertEqual(sk_square.extra_price_metrics["new_buyback_krw_bn"], 100)
        self.assertIn("NAV_discount_narrowing_missing", sk_square.red_flag_fields)

        self.assertEqual(hana.primary_archetype, E2RArchetype.DIGITAL_ASSET_BANK_ENTRY_STAGE2)
        self.assertEqual(hana.extra_price_metrics["upbit_korea_virtual_asset_volume_share_pct"], 80)

        self.assertEqual(naver.primary_archetype, E2RArchetype.CRYPTO_EXCHANGE_MA_STAGE2_WITH_SECURITY_4C)
        self.assertEqual(naver.extra_price_metrics["abnormal_withdrawal_krw_bn"], 54)
        self.assertEqual(naver.event_mae_pct, -4.2)
        self.assertEqual(naver.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(stablecoin.primary_archetype, E2RArchetype.STABLECOIN_POLICY_4B_OVERHEAT)
        self.assertEqual(stablecoin.extra_price_metrics["margin_loans_krw_trn"], 20.5)
        self.assertEqual(stablecoin.stage_failure_type, "false_green")

        self.assertEqual(kakao.primary_archetype, E2RArchetype.KAKAO_BANK_CONTROL_REGULATORY_4C)
        self.assertTrue(kakao.extra_price_metrics["kakaobank_control_risk_if_convicted"])
        self.assertEqual(kakao.stage_failure_type, "should_have_been_red")

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round301_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round301_shadow_weight_rows()}
        rules_md = render_round301_stage_rules_markdown()
        trigger_md = render_round301_trigger_grid_markdown()
        stage_md = render_round301_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND301_TRIGGER_RECORDS), 8)
        self.assertEqual(trigger_rows["r6l15_brokerage_T1"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r6l15_naver_T1"]["promote_to"], "Stage2-Actionable+4C-watch")
        self.assertEqual(trigger_rows["r6l15_stablecoin_T2"]["promote_to"], "4B-watch")
        self.assertEqual(len(ROUND301_SHADOW_WEIGHT_ROWS), 9)
        self.assertEqual(shadow_rows["BROKERAGE_MARKET_VOLUME_STAGE2_ACTIONABLE"]["brokerage_trading_value_conversion"], "+5")
        self.assertEqual(shadow_rows["BUYBACK_CAPITAL_ALLOCATION_STAGE2_ACTIONABLE"]["actual_buyback_cancellation"], "+5")
        self.assertEqual(shadow_rows["STABLECOIN_POLICY_4B_OVERHEAT"]["stablecoin_hype_only_penalty"], "-5")
        self.assertIn("actual_buyback_cancellation_is_disclosed", ROUND301_STAGE2_ACTIONABLE_RULES)
        self.assertIn("financial_trigger_likely_connects_to_earnings_but_one_gate_remains", ROUND301_STAGE3_YELLOW_RULES)
        self.assertIn("stablecoin_license_reserve_quality_fee_revenue_and_redemption_are_verified", ROUND301_STAGE3_GREEN_RULES)
        self.assertIn("stablecoin_policy_hype_only", ROUND301_GREEN_BLOCKERS)
        self.assertIn("custody_security_trust", ROUND301_SCORE_UP_AXES)
        self.assertIn("founder_legal_risk_ignored", ROUND301_SCORE_DOWN_AXES)
        self.assertIn("ma_headline_price_pop_before_security_or_regulatory_clearance", ROUND301_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("crypto_exchange_abnormal_withdrawal_or_custody_failure", ROUND301_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r6_loop15_brokerage_kospi_liquidity_boom", trigger_md)
        self.assertIn("policy, buyback, M&A, stablecoin headline", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round301_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_301.md")
        self.assertEqual(audit["round_id"], "round_229")
        self.assertEqual(audit["large_sector"], ROUND301_LARGE_SECTOR)
        self.assertEqual(audit["method"], "trigger_level_backtest_v1")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_policy_buyback_ma_market_share_or_stablecoin_headline_as_green", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(
            [
                "--output-directory",
                "out",
                "--cases",
                "cases.jsonl",
                "--triggers",
                "triggers.jsonl",
                "--audit",
                "audit.json",
                "--weight-profile",
                "weights.csv",
            ]
        )
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.triggers, "triggers.jsonl")
        self.assertEqual(args.audit, "audit.json")
        self.assertEqual(args.weight_profile, "weights.csv")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round301_r6_loop15_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round301_case_rows()
            self.assertEqual(len(records), len(ROUND301_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND301_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND301_TRIGGER_RECORDS))
            self.assertIn("Samsung buyback", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Stage2-Actionable", paths["stage_rules"].read_text(encoding="utf-8"))
            self.assertIn("r6l15_naver_T1", paths["trigger_grid_md"].read_text(encoding="utf-8"))
            self.assertIn("STABLECOIN_POLICY_4B_OVERHEAT", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("BROKERAGE_MARKET_VOLUME_STAGE2_ACTIONABLE", paths["weight_profile"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["securities_firms_index_return_pct"], 13.5)


if __name__ == "__main__":
    unittest.main()
