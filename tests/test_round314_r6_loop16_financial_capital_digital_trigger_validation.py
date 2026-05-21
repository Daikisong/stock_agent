from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round314_r6_loop16_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round314_r6_loop16_financial_capital_digital_trigger_validation import (
    ROUND314_4C_WATCH_GATES,
    ROUND314_CASE_CANDIDATES,
    ROUND314_GREEN_BLOCKERS,
    ROUND314_LARGE_SECTOR,
    ROUND314_REQUIRED_TARGET_ALIASES,
    ROUND314_ROW_SEPARATION_RULES,
    ROUND314_SCORE_DOWN_AXES,
    ROUND314_SCORE_UP_AXES,
    ROUND314_SHADOW_WEIGHT_ROWS,
    ROUND314_STAGE2_ACTIONABLE_RULES,
    ROUND314_STAGE3_GREEN_RULES,
    ROUND314_STAGE3_YELLOW_RULES,
    ROUND314_STAGE4B_WATCH_TRIGGERS,
    ROUND314_TRIGGER_RECORDS,
    render_round314_stage4b_4c_review_markdown,
    render_round314_stage_rules_markdown,
    render_round314_trigger_grid_markdown,
    round314_audit_payload,
    round314_case_records,
    round314_case_rows,
    round314_shadow_weight_rows,
    round314_summary,
    round314_trigger_rows,
    write_round314_r6_loop16_reports,
)


class Round314R6Loop16FinancialCapitalDigitalTests(unittest.TestCase):
    def test_round314_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND314_REQUIRED_TARGET_ALIASES), 9)
        self.assertTrue(set(ROUND314_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND314_REQUIRED_TARGET_ALIASES["BUYBACK_CANCELLATION_VALUEUP_STAGE2_ACTIONABLE"],
            E2RArchetype.BUYBACK_CANCELLATION_VALUEUP_STAGE2_ACTIONABLE.value,
        )
        self.assertEqual(
            ROUND314_REQUIRED_TARGET_ALIASES["BANK_DIGITAL_ASSET_STAKE_STAGE2_WITH_CAPITAL_GATE"],
            E2RArchetype.BANK_DIGITAL_ASSET_STAKE_STAGE2_WITH_CAPITAL_GATE.value,
        )
        self.assertEqual(
            ROUND314_REQUIRED_TARGET_ALIASES["ELS_MISSELLING_CONSUMER_PROTECTION_4C"],
            E2RArchetype.ELS_MISSELLING_CONSUMER_PROTECTION_4C.value,
        )

    def test_archetype_definitions_capture_round314_financial_rules(self) -> None:
        buyback = archetype_definition(E2RArchetype.BUYBACK_CANCELLATION_VALUEUP_STAGE2_ACTIONABLE)
        brokerage = archetype_definition(E2RArchetype.BROKERAGE_TRADING_VOLUME_STAGE2_BETA)
        bank_stake = archetype_definition(E2RArchetype.BANK_DIGITAL_ASSET_STAKE_STAGE2_WITH_CAPITAL_GATE)
        crypto_ma = archetype_definition(E2RArchetype.FINTECH_CRYPTO_EXCHANGE_MA_STAGE2_WITH_SECURITY_4B)
        stablecoin = archetype_definition(E2RArchetype.STABLECOIN_POLICY_EVENT_PREMIUM_4B)
        els = archetype_definition(E2RArchetype.ELS_MISSELLING_CONSUMER_PROTECTION_4C)
        fx = archetype_definition(E2RArchetype.FX_OVERSEAS_STOCK_FLOW_4C_WATCH)
        private = archetype_definition(E2RArchetype.PRIVATE_FINTECH_STABLECOIN_IPO_OPTIONALITY_STAGE2)

        self.assertIn("ROE/EPS", " ".join(buyback.stage3_high_conviction_signals))
        self.assertIn("fee income", " ".join(brokerage.stage3_high_conviction_signals))
        self.assertIn("capital ratio", " ".join(bank_stake.stage3_high_conviction_signals))
        self.assertIn("custody/security", " ".join(crypto_ma.stage3_high_conviction_signals))
        self.assertIn("reserve", " ".join(stablecoin.stage4c_thesis_break_signals))
        self.assertIn("consumer-protection", " ".join(els.stage4c_thesis_break_signals))
        self.assertIn("FX risk", " ".join(fx.false_positive_patterns))
        self.assertIn("listed price", " ".join(private.stage3_high_conviction_signals))

    def test_case_records_validate_and_remain_calibration_only(self) -> None:
        records = round314_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND314_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round314_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn(
                "do_not_treat_buyback_stablecoin_crypto_MA_market_beta_or_private_fintech_headline_as_Green_without_ROE_EPS_security_approval_revenue_or_FCF",
                record.green_guardrails,
            )

        summary = round314_summary()
        self.assertEqual(summary["round_id"], "round_242")
        self.assertEqual(summary["large_sector"], ROUND314_LARGE_SECTOR)
        self.assertEqual(summary["case_candidate_count"], 9)
        self.assertEqual(summary["trigger_count"], 9)
        self.assertEqual(summary["target_archetype_count"], 9)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 3)
        self.assertEqual(summary["stage2_event_candidate_count"], 5)
        self.assertEqual(summary["private_stage2_reference_count"], 1)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 0)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 6)
        self.assertEqual(summary["stage4c_watch_count"], 4)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])

    def test_case_metrics_separate_buyback_digital_asset_stablecoin_fx_and_els(self) -> None:
        by_id = {case.case_id: case for case in ROUND314_CASE_CANDIDATES}
        samsung = by_id["r6_loop16_samsung_buyback_capital_allocation"]
        sk_square = by_id["r6_loop16_sk_square_buyback_holdco_discount"]
        brokerage = by_id["r6_loop16_kospi_brokerage_financial_beta"]
        naver = by_id["r6_loop16_naver_financial_dunamu_ma"]
        hana = by_id["r6_loop16_hana_bank_dunamu_stake"]
        stablecoin = by_id["r6_loop16_won_stablecoin_policy_mania"]
        els = by_id["r6_loop16_hongkong_els_misselling_banks"]
        fx = by_id["r6_loop16_overseas_stock_fx_flow"]
        toss = by_id["r6_loop16_toss_global_stablecoin_ipo"]

        self.assertEqual(samsung.extra_price_metrics["buyback_krw_tn"], 10)
        self.assertIn("ROE_EPS_recovery_missing", samsung.red_flag_fields)

        self.assertEqual(sk_square.extra_price_metrics["sk_hynix_stake_pct"], 20)
        self.assertEqual(sk_square.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(brokerage.extra_price_metrics["securities_return_pct"], 13.5)
        self.assertIn("market_beta_without_earnings_4B", brokerage.red_flag_fields)

        self.assertEqual(naver.extra_price_metrics["deal_value_krw_tn"], 15.13)
        self.assertEqual(naver.extra_price_metrics["abnormal_withdrawal_krw_bn"], 54)

        self.assertEqual(hana.extra_price_metrics["stake_pct"], 6.55)
        self.assertIn("capital_ratio_treatment_missing", hana.red_flag_fields)

        self.assertEqual(stablecoin.score_price_alignment, "false_positive_score")
        self.assertIn("issuer_license_missing", stablecoin.red_flag_fields)

        self.assertTrue(els.hard_4c_confirmed)
        self.assertEqual(els.rerating_result, "thesis_break")
        self.assertEqual(els.extra_price_metrics["losses_krw_tn"], 5.8)

        self.assertEqual(fx.extra_price_metrics["holdings_usd_bn"], 171)
        self.assertIn("FX_risk_disclosure_missing", fx.red_flag_fields)

        self.assertEqual(toss.symbol, "private")
        self.assertEqual(toss.extra_price_metrics["users_mn"], 30)

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round314_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round314_shadow_weight_rows()}
        rules_md = render_round314_stage_rules_markdown()
        trigger_md = render_round314_trigger_grid_markdown()
        stage_md = render_round314_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND314_TRIGGER_RECORDS), 9)
        self.assertEqual(trigger_rows["r6l16_samsung_buyback_T1"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r6l16_stablecoin_policy_T1"]["promote_to"], "4B-watch")
        self.assertEqual(trigger_rows["r6l16_els_misselling_T0"]["promote_to"], "4C")
        self.assertEqual(len(ROUND314_SHADOW_WEIGHT_ROWS), 9)
        self.assertEqual(shadow_rows["BUYBACK_CANCELLATION_VALUEUP_STAGE2_ACTIONABLE"]["buyback_cancellation"], "+5")
        self.assertEqual(shadow_rows["BANK_DIGITAL_ASSET_STAKE_STAGE2_WITH_CAPITAL_GATE"]["bank_capital_ratio"], "+5")
        self.assertEqual(shadow_rows["STABLECOIN_POLICY_EVENT_PREMIUM_4B"]["policy_without_license_penalty"], "-5")
        self.assertIn("large_buyback_and_actual_cancellation_disclosed", ROUND314_STAGE2_ACTIONABLE_RULES)
        self.assertIn("reported_price_anchor_supports_trigger_but_full_adjusted_OHLC_is_missing", ROUND314_STAGE3_YELLOW_RULES)
        self.assertIn("custody_security_AML_controls_are_proven", ROUND314_STAGE3_GREEN_RULES)
        self.assertIn("market_beta_without_earnings", ROUND314_GREEN_BLOCKERS)
        self.assertIn("actual_buyback_cancellation", ROUND314_SCORE_UP_AXES)
        self.assertIn("crypto_MA_without_security_controls", ROUND314_SCORE_DOWN_AXES)
        self.assertIn("crypto_exchange_MA_rallies_before_security_or_custody_controls", ROUND314_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("mis_selling_consumer_protection_fine", ROUND314_4C_WATCH_GATES)
        self.assertIn("trigger_calibration_row_stores_event_anchor_buyback_deal_policy_flow_or_penalty_metrics", ROUND314_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r6_loop16_samsung_buyback_capital_allocation", trigger_md)
        self.assertIn("r6_loop16_hongkong_els_misselling_banks", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round314_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_314.md")
        self.assertEqual(audit["round_id"], "round_242")
        self.assertEqual(audit["large_sector"], ROUND314_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_buyback_stablecoin_crypto_MA_market_beta_or_private_fintech_headline_as_green_without_ROE_EPS_security_approval_revenue_or_FCF", audit["what_not_to_change"])

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
            paths = write_round314_r6_loop16_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round314_case_rows()
            self.assertEqual(len(records), len(ROUND314_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND314_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND314_TRIGGER_RECORDS))
            self.assertIn("Samsung", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Stage2-Actionable", paths["stage_rules"].read_text(encoding="utf-8"))
            self.assertIn("r6l16_els_misselling_T0", paths["trigger_grid_md"].read_text(encoding="utf-8"))
            self.assertIn("PRIVATE_FINTECH_STABLECOIN_IPO_OPTIONALITY_STAGE2", paths["weight_profiles"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
