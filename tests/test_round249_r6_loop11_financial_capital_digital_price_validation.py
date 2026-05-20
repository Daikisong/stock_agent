from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round249_r6_loop11_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round249_r6_loop11_financial_capital_digital_price_validation import (
    ROUND249_CASE_CANDIDATES,
    ROUND249_GREEN_FORBIDDEN_PATTERNS,
    ROUND249_GREEN_REQUIRED_FIELDS,
    ROUND249_HARD_4C_GATES,
    ROUND249_LARGE_SECTOR,
    ROUND249_PRICE_VALIDATION_FIELDS,
    ROUND249_REQUIRED_TARGET_ALIASES,
    ROUND249_SCORE_ADJUSTMENTS,
    ROUND249_SHADOW_WEIGHT_ROWS,
    ROUND249_STAGE4B_WATCH_TRIGGERS,
    render_round249_green_gate_review_markdown,
    render_round249_stage4b_4c_review_markdown,
    round249_audit_payload,
    round249_case_records,
    round249_case_rows,
    round249_deep_sub_archetype_rows,
    round249_shadow_weight_rows,
    round249_summary,
    write_round249_r6_loop11_reports,
)


class Round249R6Loop11FinancialCapitalDigitalPriceValidationTests(unittest.TestCase):
    def test_targets_are_explicit_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND249_REQUIRED_TARGET_ALIASES), 11)
        self.assertTrue(set(ROUND249_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND249_REQUIRED_TARGET_ALIASES["BANK_VALUEUP_ROE_PBR_RERATING"],
            E2RArchetype.BANK_VALUEUP_ROE_PBR_RERATING.value,
        )
        self.assertEqual(
            ROUND249_REQUIRED_TARGET_ALIASES["DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH"],
            E2RArchetype.DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH.value,
        )
        self.assertEqual(
            ROUND249_REQUIRED_TARGET_ALIASES["KRW_STABLECOIN_POLICY_OVERHEAT"],
            E2RArchetype.KRW_STABLECOIN_POLICY_OVERHEAT.value,
        )

    def test_archetype_definitions_capture_round249_gates(self) -> None:
        bank = archetype_definition(E2RArchetype.BANK_VALUEUP_ROE_PBR_RERATING)
        securities = archetype_definition(E2RArchetype.SECURITIES_MARKET_VOLUME_CYCLE)
        holding = archetype_definition(E2RArchetype.HOLDING_NAV_DISCOUNT_VALUEUP)
        digital = archetype_definition(E2RArchetype.DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH)
        stablecoin = archetype_definition(E2RArchetype.KRW_STABLECOIN_POLICY_OVERHEAT)

        self.assertIn("ROE sustained", bank.stage3_high_conviction_signals)
        self.assertIn("PF credit cost spike", bank.stage4c_thesis_break_signals)
        self.assertIn("securities basket jumps before revenue proof", securities.stage4b_graduation_overheat_signals)
        self.assertIn("buyback cancellation", holding.stage2_candidate_signals)
        self.assertIn("abnormal withdrawal", digital.stage4c_thesis_break_signals)
        self.assertIn("related stocks double or triple before revenue evidence", stablecoin.stage4b_graduation_overheat_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round249_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND249_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_treat_low_pbr_valueup_stablecoin_digital_asset_or_ipo_headline_as_green", record.green_guardrails)

        summary = round249_summary()
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 5)
        self.assertEqual(summary["cyclical_success_count"], 1)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 8)
        self.assertEqual(summary["watch_4c_count"], 2)
        self.assertEqual(summary["price_moved_without_evidence_count"], 2)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertFalse(summary["hard_4c_confirmed"])

    def test_bank_securities_holding_and_insurance_cases_keep_green_blocked(self) -> None:
        by_id = {case.case_id: case for case in ROUND249_CASE_CANDIDATES}
        bank = by_id["r6_loop11_big4_financial_valueup_stage2"]
        securities = by_id["r6_loop11_securities_capital_market_boom"]
        sk_square = by_id["r6_loop11_sk_square_nav_discount_valueup"]
        samsung_life = by_id["r6_loop11_samsung_life_nav_capital_release"]

        self.assertEqual(bank.primary_archetype, E2RArchetype.BANK_VALUEUP_ROE_PBR_RERATING)
        self.assertEqual(bank.stage2_date.isoformat(), "2026-02-25")
        self.assertEqual(bank.stage4b_date.isoformat(), "2026-05-06")
        self.assertEqual(bank.extra_price_metrics["relative_underperformance_vs_kospi_pp"], -2.25)
        self.assertIn("cet1_unconfirmed", bank.red_flag_fields)

        self.assertEqual(securities.primary_archetype, E2RArchetype.SECURITIES_MARKET_VOLUME_CYCLE)
        self.assertEqual(securities.mfe_1d, 13.5)
        self.assertEqual(securities.extra_price_metrics["relative_outperformance_vs_kospi_pp"], 7.05)
        self.assertEqual(securities.rerating_result, "cyclical_rerating")

        self.assertEqual(sk_square.primary_archetype, E2RArchetype.HOLDING_NAV_DISCOUNT_VALUEUP)
        self.assertEqual(sk_square.extra_price_metrics["total_buyback_cancel_program_krw_bn"], 200.0)
        self.assertEqual(sk_square.extra_price_metrics["minimum_nav_discount_2024_pct"], 50.0)

        self.assertEqual(samsung_life.primary_archetype, E2RArchetype.INSURANCE_NAV_CAPITAL_RELEASE)
        self.assertEqual(samsung_life.extra_price_metrics["samsung_electronics_stake_sale_krw_trn"], 1.3)
        self.assertIn("kics_unconfirmed", samsung_life.red_flag_fields)

    def test_digital_asset_internet_bank_and_stablecoin_cases_are_guardrailed(self) -> None:
        by_id = {case.case_id: case for case in ROUND249_CASE_CANDIDATES}
        hana = by_id["r6_loop11_hana_dunamu_equity_option"]
        naver = by_id["r6_loop11_naver_dunamu_platform_merger_trust_watch"]
        internet_bank = by_id["r6_loop11_internet_bank_kbank_kakaobank_watch"]
        stablecoin = by_id["r6_loop11_stablecoin_policy_theme_overheat"]

        self.assertEqual(hana.primary_archetype, E2RArchetype.DIGITAL_ASSET_BANK_EQUITY_OPTION)
        self.assertEqual(hana.extra_price_metrics["stake_acquired_pct"], 6.55)
        self.assertEqual(hana.extra_price_metrics["implied_dunamu_equity_value_krw_trn"], 15.27)
        self.assertIn("equity_method_income_unconfirmed", hana.red_flag_fields)

        self.assertEqual(naver.primary_archetype, E2RArchetype.DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH)
        self.assertEqual(naver.stage4c_date.isoformat(), "2025-11-27")
        self.assertEqual(naver.mfe_1d, 7.0)
        self.assertEqual(naver.mae_1d, -4.2)
        self.assertEqual(naver.extra_price_metrics["event_swing_pp"], -11.2)
        self.assertIn("abnormal_withdrawal_54bn_krw", naver.red_flag_fields)

        self.assertEqual(internet_bank.primary_archetype, E2RArchetype.INTERNET_BANK_IPO_PROFITABILITY)
        self.assertIn(E2RArchetype.INTERNET_BANK_GOVERNANCE_4C, internet_bank.secondary_archetypes)
        self.assertEqual(internet_bank.extra_price_metrics["kbank_ipo_raise_max_krw_bn"], 984.0)
        self.assertEqual(internet_bank.extra_price_metrics["kakao_event_mae_1d_pct"], -3.4)

        self.assertEqual(stablecoin.primary_archetype, E2RArchetype.KRW_STABLECOIN_POLICY_OVERHEAT)
        self.assertEqual(stablecoin.case_type, "overheat")
        self.assertEqual(stablecoin.score_price_alignment, "price_moved_without_evidence")
        self.assertEqual(stablecoin.extra_price_metrics["me2on_mfe_month_pct"], 200.0)
        self.assertFalse(stablecoin.extra_price_metrics["issuer_license_confirmed"])

    def test_green_gate_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND249_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND249_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND249_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND249_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round249_shadow_weight_rows()}
        deep_rows = round249_deep_sub_archetype_rows()
        green_markdown = render_round249_green_gate_review_markdown()
        stage_markdown = render_round249_stage4b_4c_review_markdown()

        self.assertIn("roe_improving_or_sustained", required)
        self.assertIn("regulated_revenue_or_equity_method_income", required)
        self.assertIn("low_pbr_only", forbidden)
        self.assertIn("stablecoin_policy_theme_only", forbidden)
        self.assertIn("stablecoin_related_stock_doubles_or_triples_before_license", ROUND249_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("exchange_abnormal_withdrawal", ROUND249_HARD_4C_GATES)
        self.assertIn("transaction_value_anchor", fields)
        self.assertIn("credit_cost_control", axes)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("low PBR", green_markdown)
        self.assertIn("r6_loop11_naver_dunamu_platform_merger_trust_watch", stage_markdown)
        self.assertEqual(len(ROUND249_SHADOW_WEIGHT_ROWS), 9)
        self.assertEqual(shadow_rows["BANK_VALUEUP_ROE_PBR_RERATING"]["roe"], "+5")
        self.assertEqual(shadow_rows["KRW_STABLECOIN_POLICY_OVERHEAT"]["event_penalty"], "-5")
        self.assertTrue(any("Dunamu" in row["terms"] for row in deep_rows))
        self.assertTrue(any("KOSPI 7000" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round249_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_249.md")
        self.assertEqual(audit["round_id"], "round_177")
        self.assertEqual(audit["large_sector"], ROUND249_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round249_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round249_r6_loop11_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round249_case_rows()
            self.assertEqual(len(records), len(ROUND249_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND249_CASE_CANDIDATES))
            self.assertIn("Big-4", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("roe_improving_or_sustained", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("DIGITAL_ASSET_BANK_EQUITY_OPTION", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("Dunamu", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["financial_groups_event_mfe_1d_pct"], 4.2)


if __name__ == "__main__":
    unittest.main()
