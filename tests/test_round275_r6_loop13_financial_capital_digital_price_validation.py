from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round275_r6_loop13_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round275_r6_loop13_financial_capital_digital_price_validation import (
    ROUND275_CASE_CANDIDATES,
    ROUND275_GREEN_FORBIDDEN_PATTERNS,
    ROUND275_GREEN_REQUIRED_FIELDS,
    ROUND275_HARD_4C_GATES,
    ROUND275_LARGE_SECTOR,
    ROUND275_PRICE_VALIDATION_FIELDS,
    ROUND275_REQUIRED_TARGET_ALIASES,
    ROUND275_SCORE_ADJUSTMENTS,
    ROUND275_SHADOW_WEIGHT_ROWS,
    ROUND275_STAGE4B_WATCH_TRIGGERS,
    render_round275_green_gate_review_markdown,
    render_round275_stage4b_4c_review_markdown,
    round275_audit_payload,
    round275_case_records,
    round275_case_rows,
    round275_deep_sub_archetype_rows,
    round275_shadow_weight_rows,
    round275_summary,
    write_round275_r6_loop13_reports,
)


class Round275R6Loop13FinancialCapitalDigitalPriceValidationTests(unittest.TestCase):
    def test_round275_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND275_REQUIRED_TARGET_ALIASES), 9)
        self.assertTrue(set(ROUND275_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND275_REQUIRED_TARGET_ALIASES["BANK_VALUE_UP_RERATING_STAGE2"],
            E2RArchetype.BANK_VALUE_UP_RERATING_STAGE2.value,
        )
        self.assertEqual(
            ROUND275_REQUIRED_TARGET_ALIASES["FINTECH_CRYPTO_M_AND_A_TRUST_GATE"],
            E2RArchetype.FINTECH_CRYPTO_M_AND_A_TRUST_GATE.value,
        )
        self.assertEqual(
            ROUND275_REQUIRED_TARGET_ALIASES["CRYPTO_EXCHANGE_OPERATIONAL_HARD_REFERENCE"],
            E2RArchetype.CRYPTO_EXCHANGE_OPERATIONAL_HARD_REFERENCE.value,
        )

    def test_round275_archetype_definitions_capture_r6_loop13_gates(self) -> None:
        bank = archetype_definition(E2RArchetype.BANK_VALUE_UP_RERATING_STAGE2)
        holdco = archetype_definition(E2RArchetype.HOLDCO_DISCOUNT_BUYBACK_CANCELLATION)
        insurance = archetype_definition(E2RArchetype.INSURANCE_HOLDING_STAKE_REGULATORY_GATE)
        stake = archetype_definition(E2RArchetype.DIGITAL_ASSET_BANK_STAKE_STAGE2)
        mna = archetype_definition(E2RArchetype.FINTECH_CRYPTO_M_AND_A_TRUST_GATE)
        ipo = archetype_definition(E2RArchetype.INTERNET_BANK_IPO_OVERHANG)
        exchange = archetype_definition(E2RArchetype.CRYPTO_EXCHANGE_OPERATIONAL_HARD_REFERENCE)
        securities = archetype_definition(E2RArchetype.SECURITIES_TRADING_VOLUME_EVENT_PREMIUM)

        self.assertIn("executed payout, CET1/NIM/credit-cost/ROE and RWA control confirmed", bank.stage3_high_conviction_signals)
        self.assertIn("NAV discount narrowing, recurring capital return, governance durability, non-Hynix asset clarity", holdco.stage3_high_conviction_signals)
        self.assertIn("Samsung Electronics stake value treated as insurance Green", insurance.false_positive_patterns)
        self.assertIn("digital-asset equity stake treated as bank earnings", stake.false_positive_patterns)
        self.assertIn("M&A synergy priced while abnormal withdrawal unresolved", mna.false_positive_patterns)
        self.assertIn("IPO valuation or customer count treated as bank quality", ipo.false_positive_patterns)
        self.assertIn("operational error", exchange.stage4c_thesis_break_signals)
        self.assertIn("trading-volume spike treated as recurring earnings", securities.false_positive_patterns)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round275_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND275_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round275_cases_as_candidate_generation_input", record.green_guardrails)

        summary = round275_summary()
        self.assertEqual(summary["round_id"], "round_203")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 5)
        self.assertEqual(summary["event_premium_count"], 2)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["direct_listed_hard_4c_case_count"], 0)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 7)
        self.assertEqual(summary["stage4c_watch_count"], 4)
        self.assertEqual(summary["price_moved_without_evidence_count"], 2)
        self.assertEqual(summary["target_archetype_count"], 9)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["hard_4c_confirmed"])
        self.assertFalse(summary["direct_listed_hard_4c_confirmed"])

    def test_financial_valueup_holdco_insurance_and_hana_cases_are_guarded(self) -> None:
        by_id = {case.case_id: case for case in ROUND275_CASE_CANDIDATES}
        valueup = by_id["r6_loop13_financial_holdings_valueup_sector_4b"]
        sk_square = by_id["r6_loop13_sk_square_holdco_discount_buyback"]
        samsung_life = by_id["r6_loop13_samsung_life_samsung_electronics_stake_regulatory_gate"]
        hana = by_id["r6_loop13_hana_bank_dunamu_digital_asset_stake"]

        self.assertEqual(valueup.primary_archetype, E2RArchetype.BANK_VALUE_UP_RERATING_STAGE2)
        self.assertEqual(valueup.extra_price_metrics["financial_groups_event_mfe_pct"], 4.2)
        self.assertFalse(valueup.extra_price_metrics["actual_bank_cet1_credit_cost_nim_verified"])
        self.assertIn("sector_rally_without_bank_metrics", valueup.red_flag_fields)

        self.assertEqual(sk_square.primary_archetype, E2RArchetype.HOLDCO_DISCOUNT_BUYBACK_CANCELLATION)
        self.assertEqual(sk_square.extra_price_metrics["total_buyback_cancel_krw_bn"], 200.0)
        self.assertEqual(sk_square.extra_price_metrics["sk_hynix_stake_pct"], 20.0)
        self.assertEqual(sk_square.extra_price_metrics["discount_min_pct"], 50.0)

        self.assertEqual(samsung_life.primary_archetype, E2RArchetype.INSURANCE_HOLDING_STAKE_REGULATORY_GATE)
        self.assertEqual(samsung_life.extra_price_metrics["stake_sale_krw_trn"], 1.3)
        self.assertFalse(samsung_life.extra_price_metrics["insurance_capital_return_bridge_confirmed"])
        self.assertIn("regulatory_capital_uncertainty", samsung_life.red_flag_fields)

        self.assertEqual(hana.primary_archetype, E2RArchetype.DIGITAL_ASSET_BANK_STAKE_STAGE2)
        self.assertEqual(hana.extra_price_metrics["stake_acquired_pct"], 6.55)
        self.assertEqual(hana.extra_price_metrics["implied_dunamu_equity_value_krw_trn"], 15.31)
        self.assertFalse(hana.extra_price_metrics["regulatory_bridge_confirmed"])

    def test_naver_kbank_stablecoin_and_bithumb_do_not_force_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND275_CASE_CANDIDATES}
        naver = by_id["r6_loop13_naver_dunamu_fintech_ma_trust_gate"]
        kbank = by_id["r6_loop13_kbank_internet_bank_ipo_overhang"]
        stablecoin = by_id["r6_loop13_stablecoin_policy_overheat_fx_gate"]
        bithumb = by_id["r6_loop13_bithumb_operational_error_hard_reference"]

        self.assertEqual(naver.primary_archetype, E2RArchetype.FINTECH_CRYPTO_M_AND_A_TRUST_GATE)
        self.assertEqual(naver.event_mfe_pct, 7.0)
        self.assertEqual(naver.event_mae_pct, -4.2)
        self.assertEqual(naver.extra_price_metrics["abnormal_withdrawal_krw_bn"], 54.0)
        self.assertEqual(naver.stage_failure_type, "should_have_been_red")

        self.assertEqual(kbank.primary_archetype, E2RArchetype.INTERNET_BANK_IPO_OVERHANG)
        self.assertEqual(kbank.extra_price_metrics["max_valuation_krw_trn"], 5.0)
        self.assertEqual(kbank.extra_price_metrics["customers_mn"], 10.0)
        self.assertFalse(kbank.extra_price_metrics["credit_nim_deposit_confirmed"])

        self.assertEqual(stablecoin.primary_archetype, E2RArchetype.STABLECOIN_POLICY_OVERHEAT_FX_GATE)
        self.assertEqual(stablecoin.extra_price_metrics["me2on_mfe_pct"], 200.0)
        self.assertEqual(stablecoin.score_price_alignment, "price_moved_without_evidence")
        self.assertIn("stablecoin_theme_only", stablecoin.red_flag_fields)

        self.assertEqual(bithumb.primary_archetype, E2RArchetype.CRYPTO_EXCHANGE_OPERATIONAL_HARD_REFERENCE)
        self.assertTrue(bithumb.hard_4c_confirmed)
        self.assertFalse(bithumb.direct_listed_hard_4c_confirmed)
        self.assertEqual(bithumb.extra_price_metrics["erroneous_btc_total"], 620000.0)
        self.assertEqual(bithumb.extra_price_metrics["recovered_share_pct"], 99.7)
        self.assertEqual(bithumb.rerating_result, "thesis_break")

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND275_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND275_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND275_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND275_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round275_shadow_weight_rows()}
        deep_rows = round275_deep_sub_archetype_rows()
        green_markdown = render_round275_green_gate_review_markdown()
        stage_markdown = render_round275_stage4b_4c_review_markdown()

        self.assertIn("cet1_rbc_capital_buffer_stable", required)
        self.assertIn("exchange_internal_control_confirmed", required)
        self.assertIn("IPO_valuation_without_credit_quality", forbidden)
        self.assertIn("trading_volume_event_only", forbidden)
        self.assertIn("stablecoin_basket_2x_to_3x_before_regulated_revenue", ROUND275_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("crypto_exchange_abnormal_withdrawal_or_operational_error", ROUND275_HARD_4C_GATES)
        self.assertIn("digital_asset_trust_gate", fields)
        self.assertIn("exchange_trust_incident", axes)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("Dunamu stake", green_markdown)
        self.assertIn("hard 4C", stage_markdown)
        self.assertEqual(len(ROUND275_SHADOW_WEIGHT_ROWS), 9)
        self.assertEqual(shadow_rows["STABLECOIN_POLICY_OVERHEAT_FX_GATE"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["CRYPTO_EXCHANGE_OPERATIONAL_HARD_REFERENCE"]["hard_4c_sensitivity"], "+5")
        self.assertTrue(any("SK Square" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Bithumb" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round275_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_275.md")
        self.assertEqual(audit["round_id"], "round_203")
        self.assertEqual(audit["large_sector"], ROUND275_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertFalse(audit["summary"]["direct_listed_hard_4c_confirmed"])
        self.assertIn("do_not_use_round275_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round275_r6_loop13_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round275_case_rows()
            self.assertEqual(len(records), len(ROUND275_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND275_CASE_CANDIDATES))
            self.assertIn("financial holding basket", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("cet1_rbc_capital_buffer_stable", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("CRYPTO_EXCHANGE_OPERATIONAL_HARD_REFERENCE", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("digital_asset_trust_gate", paths["price_validation_plan"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["financial_groups_event_mfe_pct"], 4.2)


if __name__ == "__main__":
    unittest.main()
