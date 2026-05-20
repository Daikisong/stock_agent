from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round241_r11_loop10_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round241_r11_loop10_policy_geopolitical_event_price_validation import (
    ROUND241_CASE_CANDIDATES,
    ROUND241_GREEN_FORBIDDEN_PATTERNS,
    ROUND241_GREEN_REQUIRED_FIELDS,
    ROUND241_HARD_4C_GATES,
    ROUND241_PRICE_VALIDATION_FIELDS,
    ROUND241_REQUIRED_TARGET_ALIASES,
    ROUND241_SCORE_ADJUSTMENTS,
    ROUND241_SHADOW_WEIGHT_ROWS,
    ROUND241_STAGE4B_WATCH_TRIGGERS,
    render_round241_green_gate_review_markdown,
    render_round241_stage4b_4c_review_markdown,
    round241_audit_payload,
    round241_case_records,
    round241_case_rows,
    round241_deep_sub_archetype_rows,
    round241_shadow_weight_rows,
    round241_summary,
    write_round241_r11_loop10_reports,
)


class Round241R11Loop10PolicyGeopoliticalEventPriceValidationTests(unittest.TestCase):
    def test_round241_targets_map_to_existing_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND241_REQUIRED_TARGET_ALIASES), 12)
        self.assertTrue(set(ROUND241_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND241_REQUIRED_TARGET_ALIASES["POLITICAL_INSTITUTIONAL_TRUST_BREAK"],
            E2RArchetype.POLITICAL_INSTITUTIONAL_TRUST_BREAK.value,
        )
        self.assertEqual(
            ROUND241_REQUIRED_TARGET_ALIASES["GLOBAL_INDEX_INCLUSION"],
            E2RArchetype.GLOBAL_INDEX_INCLUSION.value,
        )
        self.assertEqual(
            ROUND241_REQUIRED_TARGET_ALIASES["MACRO_HARD_4C"],
            E2RArchetype.MACRO_HARD_4C.value,
        )

    def test_case_records_validate_and_keep_calibration_guardrails(self) -> None:
        records = round241_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.POLICY_GEOPOLITICAL_EVENT.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)

        summary = round241_summary()
        self.assertEqual(summary["analyst_round_id"], "round_169")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 4)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 7)
        self.assertEqual(summary["stage4c_watch_count"], 3)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["policy_relief_count"], 2)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_new_r11_loop10_archetype_definitions_are_available(self) -> None:
        trust = archetype_definition(E2RArchetype.POLITICAL_INSTITUTIONAL_TRUST_BREAK)
        wgbi = archetype_definition(E2RArchetype.GLOBAL_INDEX_INCLUSION)
        hormuz = archetype_definition(E2RArchetype.GEOPOLITICAL_ENERGY_SUPPLY_SHOCK)
        hard_4c = archetype_definition(E2RArchetype.MACRO_HARD_4C)

        self.assertIn("martial-law declaration", trust.stage4c_thesis_break_signals)
        self.assertIn("confirmed index inclusion", wgbi.stage2_candidate_signals)
        self.assertIn("actual inflow plus rates, FX, funding-cost, and company EPS/FCF bridge", wgbi.stage3_high_conviction_signals)
        self.assertIn("geopolitical energy chokepoint closure", hormuz.stage4c_thesis_break_signals)
        self.assertIn("not a Green source; macro hard 4C blocks unsafe promotion", hard_4c.stage3_high_conviction_signals)

    def test_martial_law_and_ai_tax_are_4c_watch_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND241_CASE_CANDIDATES}
        martial = by_id["r11_loop10_martial_law_institutional_trust_shock"]
        ai_tax = by_id["r11_loop10_ai_dividend_tax_policy_confidence_shock"]

        self.assertEqual(martial.primary_archetype, E2RArchetype.POLITICAL_INSTITUTIONAL_TRUST_BREAK)
        self.assertEqual(martial.stage4c_date.isoformat(), "2024-12-04")
        self.assertFalse(martial.hard_4c_confirmed)
        self.assertEqual(martial.mae_1d, -2.0)
        self.assertEqual(martial.extra_price_metrics["krw_status"], "two-year low")
        self.assertIn("martial_law_or_institutional_shock", martial.red_flag_fields)

        self.assertEqual(ai_tax.primary_archetype, E2RArchetype.AI_WINDFALL_TAX_POLICY_SHOCK)
        self.assertEqual(ai_tax.stage4c_date.isoformat(), "2026-05-12")
        self.assertEqual(ai_tax.extra_price_metrics["kospi_intraday_mae_pct"], -5.1)
        self.assertEqual(ai_tax.extra_price_metrics["kospi_close_mae_pct"], -2.3)
        self.assertIn("tax_or_redistribution_surprise", ai_tax.red_flag_fields)

    def test_wgbi_and_short_selling_are_stage2_market_structure_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND241_CASE_CANDIDATES}
        wgbi = by_id["r11_loop10_wgbi_inclusion_market_structure"]
        short_selling = by_id["r11_loop10_short_selling_msci_access_reform"]

        self.assertEqual(wgbi.primary_archetype, E2RArchetype.GLOBAL_INDEX_INCLUSION)
        self.assertEqual(wgbi.stage2_date.isoformat(), "2025-11-01")
        self.assertIsNone(wgbi.stage3_date)
        self.assertEqual(wgbi.extra_price_metrics["expected_inflows_krw_trn"], 80.0)
        self.assertEqual(wgbi.extra_price_metrics["wgbi_weight_pct"], 2.22)
        self.assertIn("actual_flow_unverified", wgbi.red_flag_fields)

        self.assertEqual(short_selling.primary_archetype, E2RArchetype.SHORT_SELLING_NORMALIZATION)
        self.assertEqual(short_selling.stage2_date.isoformat(), "2025-04-21")
        self.assertEqual(short_selling.extra_price_metrics["ban_duration_years"], 5.0)
        self.assertEqual(short_selling.extra_price_metrics["msci_issue_resolution_pct"], 90.0)
        self.assertEqual(short_selling.extra_price_metrics["penalty_for_serious_short_sale_violation_pct_of_orders"], 100.0)
        self.assertIn("market_reform_without_foreign_flow", short_selling.red_flag_fields)

    def test_hormuz_hard_4c_and_policy_relief_are_separated(self) -> None:
        by_id = {case.case_id: case for case in ROUND241_CASE_CANDIDATES}
        shock = by_id["r11_loop10_hormuz_iran_energy_shock_hard_4c"]
        relief = by_id["r11_loop10_hormuz_energy_security_policy_relief"]

        self.assertEqual(shock.primary_archetype, E2RArchetype.GEOPOLITICAL_ENERGY_SUPPLY_SHOCK)
        self.assertTrue(shock.hard_4c_confirmed)
        self.assertEqual(shock.stage4c_date.isoformat(), "2026-03-04")
        self.assertEqual(shock.mae_1d, -12.06)
        self.assertEqual(shock.stage4c_price_anchor, 5093.54)
        self.assertEqual(shock.extra_price_metrics["krw_intraday_low_per_usd"], 1505.8)
        self.assertEqual(shock.extra_price_metrics["hyundai_motor_mae_pct"], -15.8)
        self.assertIn("geopolitical_energy_chokepoint_closure", shock.red_flag_fields)

        self.assertEqual(relief.primary_archetype, E2RArchetype.POLICY_RELIEF_RESPONSE)
        self.assertEqual(relief.stage2_date.isoformat(), "2026-05-12")
        self.assertFalse(relief.hard_4c_confirmed)
        self.assertIn("strategic_oil_reserves", relief.extra_price_metrics["policy_tools"])
        self.assertIn("energy_security_headline_without_cost_stabilization", relief.red_flag_fields)

    def test_fx_policy_and_us_investment_outflow_watch_are_not_company_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND241_CASE_CANDIDATES}
        kimchi = by_id["r11_loop10_kimchi_bond_fx_liquidity_policy"]
        outflow = by_id["r11_loop10_us_investment_fx_outflow_watch"]

        self.assertEqual(kimchi.primary_archetype, E2RArchetype.FX_LIQUIDITY_POLICY_RESPONSE)
        self.assertEqual(kimchi.extra_price_metrics["q1_stablecoin_trading_krw_trn"], 57.0)
        self.assertEqual(kimchi.extra_price_metrics["krw_strength_after_policy_per_usd"], 1347.0)
        self.assertEqual(kimchi.extra_price_metrics["ceiling_increase_pct"], 50.0)
        self.assertIn("fx_policy_without_actual_flow", kimchi.red_flag_fields)

        self.assertEqual(outflow.primary_archetype, E2RArchetype.FX_OUTFLOW_TRADE_DEAL_OVERLAY)
        self.assertEqual(outflow.stage4c_date.isoformat(), "2025-12-03")
        self.assertEqual(outflow.extra_price_metrics["us_investment_pledge_usd_bn"], 350.0)
        self.assertEqual(outflow.extra_price_metrics["cap_increase_pct"], 42.9)
        self.assertEqual(outflow.extra_price_metrics["retail_us_stock_holdings_usd_bn"], 160.0)
        self.assertIn("capital_outflow_pressure", outflow.red_flag_fields)

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND241_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND241_GREEN_FORBIDDEN_PATTERNS)
        review = render_round241_green_gate_review_markdown()
        stage_review = render_round241_stage4b_4c_review_markdown()
        fields = set(ROUND241_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND241_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round241_shadow_weight_rows()}
        deep_rows = round241_deep_sub_archetype_rows()

        self.assertIn("company_revenue_eps_fcf_bridge_exists", required)
        self.assertIn("political_institutional_regulatory_trust_intact", required)
        self.assertIn("policy_speech_only", forbidden)
        self.assertIn("tax_or_redistribution_surprise", forbidden)
        self.assertIn("fx_policy_without_actual_flow", axes)
        self.assertIn("capital_outflow_pressure", axes)
        self.assertIn("reported_price_anchor", fields)
        self.assertIn("fx_anchor", fields)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("AI tax speech + KOSPI selloff", review)
        self.assertIn("geopolitical_energy_chokepoint_closure", ROUND241_HARD_4C_GATES)
        self.assertIn("fx_policy_relief_rally_without_krw_stabilization", ROUND241_STAGE4B_WATCH_TRIGGERS)
        self.assertEqual(len(ROUND241_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["GLOBAL_INDEX_INCLUSION"]["capital_inflow"], "+5")
        self.assertEqual(shadow_rows["GEOPOLITICAL_ENERGY_SUPPLY_SHOCK"]["macro_4c_sensitivity"], "+5")
        self.assertTrue(any("WGBI inclusion" in row["terms"] for row in deep_rows))
        self.assertTrue(any("kimchi bond ban lifted" in row["terms"] for row in deep_rows))
        self.assertIn("r11_loop10_hormuz_iran_energy_shock_hard_4c", stage_review)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round241_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_241.md")
        self.assertEqual(audit["analyst_round_id"], "round_169")
        self.assertEqual(audit["large_sector"], Round10LargeSector.POLICY_GEOPOLITICAL_EVENT.value)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round241_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round241_r11_loop10_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round241_case_rows()
            self.assertEqual(len(records), len(ROUND241_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND241_CASE_CANDIDATES))
            self.assertIn("Hormuz/Iran energy shock", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("actual_capital_inflow", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("GLOBAL_INDEX_INCLUSION", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("WGBI inclusion", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[-1]["extra_price_metrics"])["us_investment_pledge_usd_bn"], 350.0)


if __name__ == "__main__":
    unittest.main()
