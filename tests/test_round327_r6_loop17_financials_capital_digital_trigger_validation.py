from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round327_r6_loop17_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round327_r6_loop17_financials_capital_digital_trigger_validation import (
    ROUND327_CASE_CANDIDATES,
    ROUND327_GREEN_BLOCKERS,
    ROUND327_HARD_4C_GATES,
    ROUND327_LARGE_SECTOR,
    ROUND327_REQUIRED_TARGET_ALIASES,
    ROUND327_ROW_SEPARATION_RULES,
    ROUND327_SCORE_DOWN_AXES,
    ROUND327_SCORE_UP_AXES,
    ROUND327_SHADOW_WEIGHT_ROWS,
    ROUND327_STAGE2_ACTIONABLE_RULES,
    ROUND327_STAGE3_GREEN_RULES,
    ROUND327_STAGE3_YELLOW_RULES,
    ROUND327_STAGE4B_WATCH_TRIGGERS,
    ROUND327_TRIGGER_RECORDS,
    render_round327_stage4b_4c_review_markdown,
    render_round327_stage_rules_markdown,
    render_round327_trigger_grid_markdown,
    round327_audit_payload,
    round327_case_records,
    round327_case_rows,
    round327_shadow_weight_rows,
    round327_summary,
    round327_trigger_rows,
    write_round327_r6_loop17_reports,
)


class Round327R6Loop17FinancialCapitalDigitalTests(unittest.TestCase):
    def test_round327_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND327_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND327_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND327_REQUIRED_TARGET_ALIASES["KOSPI_BOOM_SECURITIES_STAGE2_ACTIONABLE"],
            E2RArchetype.KOSPI_BOOM_SECURITIES_STAGE2_ACTIONABLE.value,
        )
        self.assertEqual(
            ROUND327_REQUIRED_TARGET_ALIASES["FINTECH_CRYPTO_EXCHANGE_MA_STAGE2_WITH_CYBER_4B"],
            E2RArchetype.FINTECH_CRYPTO_EXCHANGE_MA_STAGE2_WITH_CYBER_4B.value,
        )
        self.assertEqual(
            ROUND327_REQUIRED_TARGET_ALIASES["ELS_MISSELLING_SANCTION_4B"],
            E2RArchetype.ELS_MISSELLING_SANCTION_4B.value,
        )

    def test_archetype_definitions_capture_round327_financial_rules(self) -> None:
        securities = archetype_definition(E2RArchetype.KOSPI_BOOM_SECURITIES_STAGE2_ACTIONABLE)
        holdco = archetype_definition(E2RArchetype.VALUE_UP_CAPITAL_RETURN_HOLDCO_STAGE2_ACTIONABLE)
        bank_stake = archetype_definition(E2RArchetype.BANK_CRYPTO_EXCHANGE_STRATEGIC_STAKE_STAGE2)
        fintech_ma = archetype_definition(E2RArchetype.FINTECH_CRYPTO_EXCHANGE_MA_STAGE2_WITH_CYBER_4B)
        stablecoin = archetype_definition(E2RArchetype.WON_STABLECOIN_RETAIL_FRENZY_STAGE2_OVERHEAT)
        bank_policy = archetype_definition(E2RArchetype.BANK_STABLECOIN_POLICY_STAGE2_WITH_FX_4B)
        els = archetype_definition(E2RArchetype.ELS_MISSELLING_SANCTION_4B)
        short_selling = archetype_definition(E2RArchetype.SHORT_SELLING_NORMALIZATION_INFRA_STAGE2_4B)

        self.assertIn("recurring fee income", " ".join(securities.stage3_high_conviction_signals))
        self.assertIn("recurring buyback", " ".join(holdco.stage3_high_conviction_signals))
        self.assertIn("fee income", " ".join(bank_stake.stage3_high_conviction_signals))
        self.assertIn("cyber/custody incident", " ".join(fintech_ma.stage3_high_conviction_signals))
        self.assertIn("issuer license", " ".join(stablecoin.stage3_high_conviction_signals))
        self.assertIn("FX stability", " ".join(bank_policy.stage3_high_conviction_signals))
        self.assertIn("consumer-protection", " ".join(els.stage4b_graduation_overheat_signals))
        self.assertIn("retail backlash", " ".join(short_selling.stage4b_graduation_overheat_signals))

    def test_case_records_validate_and_remain_calibration_only(self) -> None:
        records = round327_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND327_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round327_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertEqual(record.price_validation.price_validation_status, "price_data_unavailable_after_deep_search")

        summary = round327_summary()
        self.assertEqual(summary["source_round"], "docs/round/round_327.md")
        self.assertEqual(summary["round_id"], "round_255")
        self.assertEqual(summary["large_sector"], ROUND327_LARGE_SECTOR)
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 10)
        self.assertEqual(summary["target_archetype_count"], 8)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 2)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 0)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_separate_brokerage_holdco_crypto_stablecoin_els_and_short_selling(self) -> None:
        by_id = {case.case_id: case for case in ROUND327_CASE_CANDIDATES}
        securities = by_id["r6_loop17_kospi_boom_securities_financials"]
        sk_square = by_id["r6_loop17_sk_square_buyback_holding_discount"]
        hana = by_id["r6_loop17_hana_bank_dunamu_stake"]
        naver = by_id["r6_loop17_naver_financial_dunamu_merger"]
        kakao = by_id["r6_loop17_kakao_pay_won_stablecoin_frenzy"]
        bok = by_id["r6_loop17_bok_stablecoin_kimchi_bond_fx_policy"]
        els = by_id["r6_loop17_hong_kong_els_bank_sanctions"]
        short_selling = by_id["r6_loop17_short_selling_normalization"]

        self.assertEqual(securities.extra_price_metrics["securities_firms_index_event_return_pct"], 13.5)
        self.assertIn("banks_not_green_from_index_beta", securities.red_flag_fields)

        self.assertEqual(sk_square.extra_price_metrics["new_buyback_cancel_krw_bn"], 100)
        self.assertIn("one_off_buyback_risk_4B", sk_square.red_flag_fields)

        self.assertEqual(hana.extra_price_metrics["hana_bank_dunamu_stake_pct"], 6.55)
        self.assertIn("earnings_contribution_missing", hana.red_flag_fields)

        self.assertEqual(naver.extra_price_metrics["upbit_abnormal_withdrawal_krw_bn"], 54)
        self.assertEqual(naver.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(kakao.score_price_alignment, "false_positive_score")
        self.assertIn("regulatory_framework_missing_4B", kakao.red_flag_fields)

        self.assertEqual(bok.extra_price_metrics["stablecoin_trading_q1_2025_krw_trn"], 57)
        self.assertIn("FX_liquidity_pressure_4B", bok.red_flag_fields)

        self.assertEqual(els.stage_candidate, "4B-watch")
        self.assertFalse(els.hard_4c_confirmed)

        self.assertTrue(short_selling.extra_price_metrics["illegal_trade_detection_system"])
        self.assertIn("retail_backlash_4B", short_selling.red_flag_fields)

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round327_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round327_shadow_weight_rows()}
        rules_md = render_round327_stage_rules_markdown()
        trigger_md = render_round327_trigger_grid_markdown()
        stage_md = render_round327_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND327_TRIGGER_RECORDS), 10)
        self.assertEqual(trigger_rows["r6l17_kospi_securities_T2"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r6l17_upbit_withdrawal_T2"]["promote_to"], "4B-watch")
        self.assertEqual(trigger_rows["r6l17_els_sanction_T1"]["promote_to"], "4B-watch")
        self.assertEqual(len(ROUND327_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["KOSPI_BOOM_SECURITIES_STAGE2_ACTIONABLE"]["securities_turnover_beta"], "+5")
        self.assertEqual(shadow_rows["VALUE_UP_CAPITAL_RETURN_HOLDCO_STAGE2_ACTIONABLE"]["capital_return_cancellation"], "+5")
        self.assertEqual(shadow_rows["WON_STABLECOIN_RETAIL_FRENZY_STAGE2_OVERHEAT"]["stablecoin_theme_without_regulation_penalty"], "-5")
        self.assertIn("buyback_plus_cancellation_is_explicit", ROUND327_STAGE2_ACTIONABLE_RULES)
        self.assertIn("stablecoin_law_passes_and_issuer_reserve_rules_are_clear", ROUND327_STAGE3_YELLOW_RULES)
        self.assertIn("digital_finance_revenue_is_visible_not_only_equity_stake_or_theme", ROUND327_STAGE3_GREEN_RULES)
        self.assertIn("stablecoin_theme_without_regulation", ROUND327_GREEN_BLOCKERS)
        self.assertIn("securities_turnover_beta", ROUND327_SCORE_UP_AXES)
        self.assertIn("ELS_sanction_ignored", ROUND327_SCORE_DOWN_AXES)
        self.assertIn("short_selling_retail_backlash", ROUND327_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("stablecoin_issuer_collapse_or_reserve_mismatch", ROUND327_HARD_4C_GATES)
        self.assertIn("do_not_create_MFE_MAE_without_full_adjusted_OHLC", ROUND327_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r6_loop17_kospi_boom_securities_financials", trigger_md)
        self.assertIn("r6_loop17_hong_kong_els_bank_sanctions", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round327_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_327.md")
        self.assertEqual(audit["round_id"], "round_255")
        self.assertEqual(audit["large_sector"], ROUND327_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round327_cases_as_candidate_generation_input", audit["what_not_to_change"])

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
            paths = write_round327_r6_loop17_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)
            records = load_case_library(paths["cases"])
            self.assertEqual(len(records), len(ROUND327_CASE_CANDIDATES))
            self.assertEqual(len(round327_case_rows()), len(ROUND327_CASE_CANDIDATES))
            self.assertIn("Stage3-Green confirmed: `0`", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Full adjusted OHLC", paths["price_validation_plan"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
