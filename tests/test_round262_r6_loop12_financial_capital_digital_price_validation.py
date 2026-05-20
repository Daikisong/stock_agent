from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round262_r6_loop12_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round262_r6_loop12_financial_capital_digital_price_validation import (
    ROUND262_CASE_CANDIDATES,
    ROUND262_GREEN_FORBIDDEN_PATTERNS,
    ROUND262_GREEN_REQUIRED_FIELDS,
    ROUND262_HARD_4C_GATES,
    ROUND262_LARGE_SECTOR,
    ROUND262_PRICE_VALIDATION_FIELDS,
    ROUND262_REQUIRED_TARGET_ALIASES,
    ROUND262_SCORE_ADJUSTMENTS,
    ROUND262_SHADOW_WEIGHT_ROWS,
    ROUND262_STAGE4B_WATCH_TRIGGERS,
    render_round262_green_gate_review_markdown,
    render_round262_stage4b_4c_review_markdown,
    round262_audit_payload,
    round262_case_records,
    round262_case_rows,
    round262_deep_sub_archetype_rows,
    round262_shadow_weight_rows,
    round262_summary,
    write_round262_r6_loop12_reports,
)


class Round262R6Loop12FinancialCapitalDigitalPriceValidationTests(unittest.TestCase):
    def test_round262_targets_are_explicit_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND262_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND262_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND262_REQUIRED_TARGET_ALIASES["BROKERAGE_MARKET_VOLUME_CYCLE"],
            E2RArchetype.BROKERAGE_MARKET_VOLUME_CYCLE.value,
        )
        self.assertEqual(
            ROUND262_REQUIRED_TARGET_ALIASES["BANK_DIGITAL_ASSET_EQUITY_OPTION"],
            E2RArchetype.BANK_DIGITAL_ASSET_EQUITY_OPTION.value,
        )
        self.assertEqual(
            ROUND262_REQUIRED_TARGET_ALIASES["FINTECH_SUPERAPP_BIOMETRIC_PAYMENT"],
            E2RArchetype.FINTECH_SUPERAPP_BIOMETRIC_PAYMENT.value,
        )
        self.assertEqual(
            ROUND262_REQUIRED_TARGET_ALIASES["STABLECOIN_POLICY_OVERHEAT_FX_GATE"],
            E2RArchetype.STABLECOIN_POLICY_OVERHEAT_FX_GATE.value,
        )

    def test_round262_archetype_definitions_capture_green_guards(self) -> None:
        brokerage = archetype_definition(E2RArchetype.BROKERAGE_MARKET_VOLUME_CYCLE)
        bank_digital = archetype_definition(E2RArchetype.BANK_DIGITAL_ASSET_EQUITY_OPTION)
        fintech = archetype_definition(E2RArchetype.FINTECH_SUPERAPP_BIOMETRIC_PAYMENT)
        stablecoin = archetype_definition(E2RArchetype.STABLECOIN_POLICY_OVERHEAT_FX_GATE)

        self.assertIn("brokerage and IB revenue realized", brokerage.stage3_high_conviction_signals)
        self.assertIn("market volume spike treated as structural Green", brokerage.false_positive_patterns)
        self.assertIn("equity-method income", bank_digital.stage3_high_conviction_signals)
        self.assertIn("biometric data breach", fintech.stage4c_thesis_break_signals)
        self.assertIn("stablecoin-driven FX outflow", stablecoin.stage4c_thesis_break_signals)
        self.assertIn("regulated issuer economics, reserve income, fee revenue and FX stability required", stablecoin.stage3_high_conviction_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round262_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND262_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)
            self.assertIn(
                "do_not_treat_low_pbr_valueup_volume_digital_asset_stablecoin_or_ipo_headline_as_green_alone",
                record.green_guardrails,
            )

        summary = round262_summary()
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 5)
        self.assertEqual(summary["cyclical_success_count"], 1)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["watch_case_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 6)
        self.assertEqual(summary["watch_4c_count"], 3)
        self.assertEqual(summary["price_moved_without_evidence_count"], 2)
        self.assertEqual(summary["reported_price_anchor_count"], 6)
        self.assertEqual(summary["target_archetype_count"], 8)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_financial_valueup_brokerage_insurance_and_hana_cases_are_guarded(self) -> None:
        by_id = {case.case_id: case for case in ROUND262_CASE_CANDIDATES}
        valueup = by_id["r6_loop12_financial_holdings_valueup_stage2"]
        brokerage = by_id["r6_loop12_securities_market_volume_cycle"]
        samsung_life = by_id["r6_loop12_samsung_life_nav_capital_release"]
        hana = by_id["r6_loop12_hana_bank_dunamu_equity_option"]

        self.assertEqual(valueup.primary_archetype, E2RArchetype.BANK_VALUEUP_ROE_PBR_RERATING)
        self.assertEqual(valueup.extra_price_metrics["financial_groups_event_mfe_pct"], 4.2)
        self.assertEqual(valueup.extra_price_metrics["relative_performance_vs_kospi_pp"], -2.25)
        self.assertIn("roe_cet1_credit_cost_unconfirmed", valueup.red_flag_fields)

        self.assertEqual(brokerage.primary_archetype, E2RArchetype.BROKERAGE_MARKET_VOLUME_CYCLE)
        self.assertEqual(brokerage.extra_price_metrics["securities_firms_event_mfe_pct"], 13.5)
        self.assertEqual(brokerage.extra_price_metrics["securities_relative_outperformance_vs_kospi_pp"], 7.05)
        self.assertEqual(brokerage.rerating_result, "cyclical_rerating")

        self.assertEqual(samsung_life.primary_archetype, E2RArchetype.INSURANCE_NAV_CAPITAL_RELEASE)
        self.assertEqual(samsung_life.extra_price_metrics["samsung_electronics_stake_sale_krw_trn"], 1.3)
        self.assertEqual(samsung_life.extra_price_metrics["fx_rate_krw_per_usd"], 1499.3)
        self.assertIn("use_of_proceeds_unconfirmed", samsung_life.red_flag_fields)

        self.assertEqual(hana.primary_archetype, E2RArchetype.BANK_DIGITAL_ASSET_EQUITY_OPTION)
        self.assertEqual(hana.extra_price_metrics["stake_acquired_pct"], 6.55)
        self.assertEqual(hana.extra_price_metrics["implied_dunamu_equity_value_krw_trn"], 15.27)
        self.assertEqual(hana.extra_price_metrics["upbit_trading_volume_share_pct_min"], 80.0)
        self.assertEqual(hana.extra_price_metrics["expected_closing"], "2026-06-15")

    def test_platform_fintech_governance_and_stablecoin_cases_are_separated(self) -> None:
        by_id = {case.case_id: case for case in ROUND262_CASE_CANDIDATES}
        naver = by_id["r6_loop12_naver_dunamu_platform_merger_trust_watch"]
        toss = by_id["r6_loop12_toss_facepay_fintech_superapp_privacy_watch"]
        kakao = by_id["r6_loop12_kakao_kakaobank_governance_gate"]
        stablecoin = by_id["r6_loop12_stablecoin_policy_overheat_fx_gate"]

        self.assertEqual(naver.primary_archetype, E2RArchetype.DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH)
        self.assertEqual(naver.score_price_alignment, "price_moved_without_evidence")
        self.assertEqual(naver.extra_price_metrics["event_initial_mfe_pct"], 7.0)
        self.assertEqual(naver.extra_price_metrics["event_later_mae_pct"], -4.2)
        self.assertEqual(naver.extra_price_metrics["abnormal_withdrawal_krw_bn"], 54.0)

        self.assertEqual(toss.primary_archetype, E2RArchetype.FINTECH_SUPERAPP_BIOMETRIC_PAYMENT)
        self.assertEqual(toss.extra_price_metrics["facepay_users_mn"], 4.8)
        self.assertEqual(toss.extra_price_metrics["user_target_growth_needed_pct"], 108.3)
        self.assertEqual(toss.extra_price_metrics["merchant_target_growth_needed_pct"], 203.0)
        self.assertEqual(toss.price_validation_status, "unlisted_no_ohlc")

        self.assertEqual(kakao.primary_archetype, E2RArchetype.INTERNET_BANK_GOVERNANCE_4C)
        self.assertEqual(kakao.case_type, "4b_watch")
        self.assertEqual(kakao.stage4c_date.isoformat(), "2024-07-22")
        self.assertEqual(kakao.extra_price_metrics["kakao_event_mae_pct"], -3.4)
        self.assertIn("bank_ownership_suitability_failure_watch", kakao.red_flag_fields)

        self.assertEqual(stablecoin.primary_archetype, E2RArchetype.STABLECOIN_POLICY_OVERHEAT_FX_GATE)
        self.assertEqual(stablecoin.mfe_1d, 200.0)
        self.assertEqual(stablecoin.extra_price_metrics["stablecoin_trading_q1_krw_trn"], 57.0)
        self.assertEqual(stablecoin.extra_price_metrics["capital_outflow_context_usd_bn_min"], 19.0)
        self.assertEqual(stablecoin.score_price_alignment, "price_moved_without_evidence")
        self.assertFalse(stablecoin.hard_4c_confirmed)

    def test_green_gate_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND262_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND262_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND262_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND262_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round262_shadow_weight_rows()}
        deep_rows = round262_deep_sub_archetype_rows()
        green_markdown = render_round262_green_gate_review_markdown()
        stage_markdown = render_round262_stage4b_4c_review_markdown()

        self.assertIn("roe_improvement_or_sustainability", required)
        self.assertIn("fx_outflow_and_stablecoin_macro_risk_passed", required)
        self.assertIn("stablecoin_theme_only", forbidden)
        self.assertIn("market_volume_spike_only", forbidden)
        self.assertIn("securities_basket_plus_10pct_on_volume_cycle", ROUND262_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("exchange_abnormal_withdrawal_or_hack", ROUND262_HARD_4C_GATES)
        self.assertIn("trust_privacy_or_fx_gate", fields)
        self.assertIn("stablecoin_policy_theme_only", axes)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("low PBR bank", green_markdown)
        self.assertIn("r6_loop12_stablecoin_policy_overheat_fx_gate", stage_markdown)
        self.assertEqual(len(ROUND262_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["BANK_VALUEUP_ROE_PBR_RERATING"]["real_buyback_cancel"], "+5")
        self.assertEqual(shadow_rows["STABLECOIN_POLICY_OVERHEAT_FX_GATE"]["event_penalty"], "-5")
        self.assertTrue(any("Dunamu" in row["terms"] for row in deep_rows))
        self.assertTrue(any("FacePay" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round262_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_262.md")
        self.assertEqual(audit["round_id"], "round_190")
        self.assertEqual(audit["large_sector"], ROUND262_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round262_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round262_r6_loop12_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round262_case_rows()
            self.assertEqual(len(records), len(ROUND262_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND262_CASE_CANDIDATES))
            self.assertIn("Korean financial holding", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("roe_improvement_or_sustainability", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("STABLECOIN_POLICY_OVERHEAT_FX_GATE", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("trust_privacy_or_fx_gate", paths["price_validation_plan"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["relative_performance_vs_kospi_pp"], -2.25)


if __name__ == "__main__":
    unittest.main()
