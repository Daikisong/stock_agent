from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round254_r11_loop11_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round254_r11_loop11_policy_geopolitical_event_price_validation import (
    ROUND254_CASE_CANDIDATES,
    ROUND254_GREEN_FORBIDDEN_PATTERNS,
    ROUND254_GREEN_REQUIRED_FIELDS,
    ROUND254_HARD_4C_GATES,
    ROUND254_PRICE_VALIDATION_FIELDS,
    ROUND254_REQUIRED_TARGET_ALIASES,
    ROUND254_SCORE_ADJUSTMENTS,
    ROUND254_SHADOW_WEIGHT_ROWS,
    ROUND254_STAGE4B_WATCH_TRIGGERS,
    render_round254_green_gate_review_markdown,
    render_round254_stage4b_4c_review_markdown,
    round254_audit_payload,
    round254_case_records,
    round254_case_rows,
    round254_deep_sub_archetype_rows,
    round254_shadow_weight_rows,
    round254_summary,
    write_round254_r11_loop11_reports,
)


class Round254R11Loop11PolicyGeopoliticalEventPriceValidationTests(unittest.TestCase):
    def test_round254_targets_map_to_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND254_REQUIRED_TARGET_ALIASES), 10)
        self.assertTrue(set(ROUND254_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND254_REQUIRED_TARGET_ALIASES["GLOBAL_INDEX_INCLUSION_CAPITAL_FLOW"],
            E2RArchetype.GLOBAL_INDEX_INCLUSION_CAPITAL_FLOW.value,
        )
        self.assertEqual(
            ROUND254_REQUIRED_TARGET_ALIASES["GEOPOLITICAL_ENERGY_SECURITY_HARD_4C"],
            E2RArchetype.GEOPOLITICAL_ENERGY_SECURITY_HARD_4C.value,
        )
        self.assertEqual(
            ROUND254_REQUIRED_TARGET_ALIASES["POLICY_HEADLINE_NOT_GREEN"],
            E2RArchetype.POLICY_HEADLINE_NOT_GREEN.value,
        )

    def test_case_records_validate_and_keep_calibration_guardrails(self) -> None:
        records = round254_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.POLICY_GEOPOLITICAL_EVENT.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("do_not_treat_policy_geopolitical_disaster_fx_or_index_headline_as_green", record.green_guardrails)

        summary = round254_summary()
        self.assertEqual(summary["analyst_round_id"], "round_182")
        self.assertEqual(summary["case_candidate_count"], 9)
        self.assertEqual(summary["success_candidate_count"], 5)
        self.assertEqual(summary["failed_rerating_count"], 3)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 8)
        self.assertEqual(summary["stage4c_watch_count"], 4)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["policy_relief_count"], 2)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_round254_archetype_definitions_encode_policy_gates(self) -> None:
        wgbi = archetype_definition(E2RArchetype.GLOBAL_INDEX_INCLUSION_CAPITAL_FLOW)
        short_selling = archetype_definition(E2RArchetype.SHORT_SELLING_MARKET_ACCESS_REFORM)
        valueup = archetype_definition(E2RArchetype.CORPORATE_GOVERNANCE_VALUEUP_POLICY)
        hormuz = archetype_definition(E2RArchetype.GEOPOLITICAL_ENERGY_SECURITY_HARD_4C)
        stablecoin = archetype_definition(E2RArchetype.FX_LIQUIDITY_STABLECOIN_OUTFLOW)
        headline = archetype_definition(E2RArchetype.POLICY_HEADLINE_NOT_GREEN)

        self.assertIn("actual foreign bond inflow", wgbi.stage2_candidate_signals)
        self.assertIn("actual foreign flow plus rates, FX, funding-cost, and company EPS/FCF bridge", wgbi.stage3_high_conviction_signals)
        self.assertIn("MSCI short-selling accessibility improved", short_selling.stage2_candidate_signals)
        self.assertIn("treasury share cancellation mandate", valueup.stage2_candidate_signals)
        self.assertIn("not a Green source; energy chokepoint shock is a macro hard 4C gate", hormuz.stage3_high_conviction_signals)
        self.assertIn("stablecoin-driven capital outflow", stablecoin.stage4c_thesis_break_signals)
        self.assertIn("policy headline or theme rally treated as Stage 3-Green", headline.false_positive_patterns)

    def test_martial_law_and_ai_tax_are_4c_watch_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND254_CASE_CANDIDATES}
        martial = by_id["r11_loop11_martial_law_institutional_trust_4c_watch"]
        ai_tax = by_id["r11_loop11_ai_dividend_tax_policy_confidence_shock"]

        self.assertEqual(martial.primary_archetype, E2RArchetype.POLITICAL_INSTITUTIONAL_TRUST_BREAK)
        self.assertEqual(martial.stage4c_date.isoformat(), "2024-12-04")
        self.assertFalse(martial.hard_4c_confirmed)
        self.assertEqual(martial.mae_1d, -2.0)
        self.assertEqual(martial.extra_price_metrics["market_stabilization_fund_krw_trn"], 10.0)
        self.assertIn("martial_law_or_institutional_shock", martial.red_flag_fields)

        self.assertEqual(ai_tax.primary_archetype, E2RArchetype.AI_WINDFALL_TAX_POLICY_CONFIDENCE_SHOCK)
        self.assertEqual(ai_tax.stage4c_date.isoformat(), "2026-05-12")
        self.assertEqual(ai_tax.extra_price_metrics["kospi_intraday_mae_pct"], -5.1)
        self.assertEqual(ai_tax.extra_price_metrics["kospi_close_mae_pct"], -2.3)
        self.assertIn("excess tax revenue", ai_tax.extra_price_metrics["clarification"])
        self.assertIn("tax_or_redistribution_surprise", ai_tax.red_flag_fields)

    def test_market_structure_valueup_and_capital_flow_are_stage2_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND254_CASE_CANDIDATES}
        wgbi = by_id["r11_loop11_wgbi_actual_bond_inflow_stage2"]
        short_selling = by_id["r11_loop11_short_selling_market_access_reform"]
        valueup = by_id["r11_loop11_commercial_act_treasury_share_valueup"]

        self.assertEqual(wgbi.stage2_date.isoformat(), "2025-12-15")
        self.assertEqual(wgbi.extra_price_metrics["wgbi_weight_pct"], 2.22)
        self.assertEqual(wgbi.extra_price_metrics["foreign_bond_inflow_nov_2025_usd_bn"], 11.08)
        self.assertEqual(wgbi.extra_price_metrics["regional_bond_inflows_nov_2025_usd_bn"], 10.86)
        self.assertIsNone(wgbi.stage3_date)

        self.assertEqual(short_selling.stage2_date.isoformat(), "2025-06-20")
        self.assertEqual(short_selling.extra_price_metrics["ban_duration_years"], 5.0)
        self.assertEqual(short_selling.extra_price_metrics["penalty_for_serious_short_sale_violation_pct_of_orders"], 100.0)

        self.assertEqual(valueup.stage2_date.isoformat(), "2026-02-25")
        self.assertEqual(valueup.extra_price_metrics["newly_acquired_treasury_share_cancel_within_years"], 1.0)
        self.assertEqual(valueup.extra_price_metrics["existing_treasury_share_grace_months"], 6.0)

    def test_hormuz_hard_4c_and_relief_are_separated(self) -> None:
        by_id = {case.case_id: case for case in ROUND254_CASE_CANDIDATES}
        shock = by_id["r11_loop11_hormuz_iran_energy_security_hard_4c"]
        relief = by_id["r11_loop11_hormuz_policy_relief_response"]

        self.assertEqual(shock.primary_archetype, E2RArchetype.GEOPOLITICAL_ENERGY_SECURITY_HARD_4C)
        self.assertTrue(shock.hard_4c_confirmed)
        self.assertEqual(shock.stage4c_date.isoformat(), "2026-03-04")
        self.assertEqual(shock.mae_1d, -12.06)
        self.assertEqual(shock.stage4c_price_anchor, 5093.54)
        self.assertEqual(shock.extra_price_metrics["market_cap_wipeout_2d_usd_bn"], 553.82)
        self.assertEqual(shock.extra_price_metrics["krw_intraday_low_per_usd"], 1505.8)
        self.assertEqual(shock.extra_price_metrics["hyundai_motor_mae_pct"], -15.8)
        self.assertEqual(shock.extra_price_metrics["samsung_electronics_mae_pct"], -11.7)
        self.assertEqual(shock.extra_price_metrics["sk_hynix_mae_pct"], -9.6)
        self.assertEqual(shock.extra_price_metrics["middle_east_oil_import_dependency_pct"], 70.0)

        self.assertEqual(relief.primary_archetype, E2RArchetype.HORMUZ_POLICY_RELIEF_RESPONSE)
        self.assertEqual(relief.stage2_date.isoformat(), "2026-05-12")
        self.assertFalse(relief.extra_price_metrics["troop_expansion_immediate"])
        self.assertEqual(relief.extra_price_metrics["global_company_cost_from_iran_war_usd_bn"], 25.0)
        self.assertEqual(relief.extra_price_metrics["oil_price_context_usd_per_bbl_above"], 100.0)

    def test_fx_stablecoin_and_us_investment_outflow_watch_are_not_company_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND254_CASE_CANDIDATES}
        stablecoin = by_id["r11_loop11_fx_stablecoin_kimchi_bond_outflow_watch"]
        pledge = by_id["r11_loop11_us_investment_pledge_fx_outflow_watch"]

        self.assertEqual(stablecoin.primary_archetype, E2RArchetype.FX_LIQUIDITY_STABLECOIN_OUTFLOW)
        self.assertEqual(stablecoin.stage4c_date.isoformat(), "2025-07-27")
        self.assertEqual(stablecoin.extra_price_metrics["stablecoin_trading_q1_2025_krw_trn"], 57.0)
        self.assertEqual(stablecoin.extra_price_metrics["stablecoin_trading_q1_2025_usd_bn"], 42.0)
        self.assertEqual(stablecoin.extra_price_metrics["krw_strength_after_policy_per_usd"], 1347.0)
        self.assertEqual(stablecoin.extra_price_metrics["krw_stabilization_level_per_usd"], 1353.0)
        self.assertEqual(stablecoin.extra_price_metrics["kimchi_bond_ban_duration_years"], 14.0)
        self.assertEqual(stablecoin.extra_price_metrics["capital_outflow_context_usd_bn"], 19.0)
        self.assertEqual(stablecoin.extra_price_metrics["proposed_minimum_equity_for_won_stablecoin_issuers_krw_mn"], 500.0)

        self.assertEqual(pledge.primary_archetype, E2RArchetype.FOREIGN_INVESTMENT_PLEDGE_FX_OUTFLOW)
        self.assertEqual(pledge.extra_price_metrics["us_investment_pledge_usd_bn"], 350.0)
        self.assertEqual(pledge.extra_price_metrics["annual_dollar_outflow_limit_usd_bn"], 20.0)
        self.assertEqual(pledge.extra_price_metrics["fx_bond_cap_2026_usd_bn"], 5.0)
        self.assertEqual(pledge.extra_price_metrics["fx_bond_cap_2025_usd_bn"], 3.5)
        self.assertEqual(pledge.extra_price_metrics["cap_increase_pct"], 42.9)
        self.assertEqual(pledge.extra_price_metrics["retail_us_stock_net_buy_2025_usd_bn"], 30.0)
        self.assertEqual(pledge.extra_price_metrics["retail_us_stock_holdings_usd_bn"], 160.0)
        self.assertEqual(pledge.extra_price_metrics["krw_decline_since_end_june_pct"], -8.0)
        self.assertEqual(pledge.extra_price_metrics["fx_reserves_context_usd_bn"], 430.7)

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND254_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND254_GREEN_FORBIDDEN_PATTERNS)
        review = render_round254_green_gate_review_markdown()
        stage_review = render_round254_stage4b_4c_review_markdown()
        fields = set(ROUND254_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND254_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round254_shadow_weight_rows()}
        deep_rows = round254_deep_sub_archetype_rows()

        self.assertIn("company_revenue_eps_fcf_bridge_exists", required)
        self.assertIn("no_tax_or_redistribution_surprise", required)
        self.assertIn("policy_speech_only", forbidden)
        self.assertIn("stablecoin_theme_only", forbidden)
        self.assertIn("foreign_investment_pledge_outflow", axes)
        self.assertIn("stablecoin_policy_theme_only", axes)
        self.assertIn("reported_price_anchor", fields)
        self.assertIn("capital_flow_anchor", fields)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("AI dividend/tax speech + KOSPI selloff", review)
        self.assertIn("geopolitical_energy_chokepoint_closure", ROUND254_HARD_4C_GATES)
        self.assertIn("stablecoin_theme_two_to_three_times", ROUND254_STAGE4B_WATCH_TRIGGERS)
        self.assertEqual(len(ROUND254_SHADOW_WEIGHT_ROWS), 10)
        self.assertEqual(shadow_rows["GLOBAL_INDEX_INCLUSION_CAPITAL_FLOW"]["actual_capital_inflow"], "+5")
        self.assertEqual(shadow_rows["GEOPOLITICAL_ENERGY_SECURITY_HARD_4C"]["macro_4c_sensitivity"], "+5")
        self.assertTrue(any("WGBI inclusion" in row["terms"] for row in deep_rows))
        self.assertTrue(any("kimchi bond deregulation" in row["terms"] for row in deep_rows))
        self.assertIn("r11_loop11_hormuz_iran_energy_security_hard_4c", stage_review)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round254_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_254.md")
        self.assertEqual(audit["analyst_round_id"], "round_182")
        self.assertEqual(audit["large_sector"], Round10LargeSector.POLICY_GEOPOLITICAL_EVENT.value)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round254_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round254_r11_loop11_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round254_case_rows()
            self.assertEqual(len(records), len(ROUND254_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND254_CASE_CANDIDATES))
            self.assertIn("Hormuz/Iran energy shock", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("actual_capital_inflow", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("GLOBAL_INDEX_INCLUSION_CAPITAL_FLOW", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("WGBI inclusion", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[-1]["extra_price_metrics"])["us_investment_pledge_usd_bn"], 350.0)


if __name__ == "__main__":
    unittest.main()
