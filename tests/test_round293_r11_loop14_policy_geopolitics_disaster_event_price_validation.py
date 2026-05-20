from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round293_r11_loop14_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round293_r11_loop14_policy_geopolitics_disaster_event_price_validation import (
    ROUND293_CASE_CANDIDATES,
    ROUND293_GREEN_FORBIDDEN_PATTERNS,
    ROUND293_GREEN_REQUIRED_FIELDS,
    ROUND293_HARD_4C_GATES,
    ROUND293_LARGE_SECTOR,
    ROUND293_PRICE_VALIDATION_FIELDS,
    ROUND293_REQUIRED_TARGET_ALIASES,
    ROUND293_SHADOW_WEIGHT_ROWS,
    ROUND293_STAGE4B_WATCH_TRIGGERS,
    render_round293_green_gate_review_markdown,
    render_round293_stage4b_4c_review_markdown,
    round293_audit_payload,
    round293_case_records,
    round293_case_rows,
    round293_deep_sub_archetype_rows,
    round293_shadow_weight_rows,
    round293_summary,
    write_round293_r11_loop14_reports,
)


class Round293R11Loop14PolicyGeopoliticsDisasterEventTests(unittest.TestCase):
    def test_round293_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND293_REQUIRED_TARGET_ALIASES), 9)
        self.assertTrue(set(ROUND293_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND293_REQUIRED_TARGET_ALIASES["RESOURCE_DISCOVERY_POLICY_EVENT_PREMIUM"],
            E2RArchetype.RESOURCE_DISCOVERY_POLICY_EVENT_PREMIUM.value,
        )
        self.assertEqual(
            ROUND293_REQUIRED_TARGET_ALIASES["POLITICAL_LIQUIDITY_SHOCK_HARD_REFERENCE"],
            E2RArchetype.POLITICAL_LIQUIDITY_SHOCK_HARD_REFERENCE.value,
        )
        self.assertEqual(
            ROUND293_REQUIRED_TARGET_ALIASES["LABOR_POLICY_SYSTEMIC_EXPORT_RISK_4C"],
            E2RArchetype.LABOR_POLICY_SYSTEMIC_EXPORT_RISK_4C.value,
        )

    def test_round293_archetype_definitions_capture_loop14_gates(self) -> None:
        resource = archetype_definition(E2RArchetype.RESOURCE_DISCOVERY_POLICY_EVENT_PREMIUM)
        sanction = archetype_definition(E2RArchetype.GEOPOLITICAL_SANCTIONS_SUPPLY_CHAIN_4C)
        political = archetype_definition(E2RArchetype.POLITICAL_LIQUIDITY_SHOCK_HARD_REFERENCE)
        tax = archetype_definition(E2RArchetype.TAX_POLICY_MARKET_CONFIDENCE_4C)
        market_access = archetype_definition(E2RArchetype.MARKET_ACCESS_REFORM_STAGE2)
        medical = archetype_definition(E2RArchetype.MEDICAL_REFORM_SERVICE_DISRUPTION_4C_REFERENCE)
        disaster = archetype_definition(E2RArchetype.NATURAL_DISASTER_RECOVERY_POLICY_REFERENCE)
        defense = archetype_definition(E2RArchetype.GEOPOLITICAL_DEFENSE_ORDER_STAGE2)
        labor = archetype_definition(E2RArchetype.LABOR_POLICY_SYSTEMIC_EXPORT_RISK_4C)

        self.assertIn("resource estimate without drilling", resource.false_positive_patterns)
        self.assertIn("foreign sanctions blocking transactions", sanction.stage4c_thesis_break_signals)
        self.assertIn("martial law liquidity shock", political.stage4c_thesis_break_signals)
        self.assertIn("capital-gains threshold shock", tax.stage4c_thesis_break_signals)
        self.assertIn("foreign flow", market_access.stage3_high_conviction_signals)
        self.assertIn("service disruption", medical.stage4c_thesis_break_signals)
        self.assertIn("recovery trade before claims/budget", disaster.false_positive_patterns)
        self.assertIn("delivery margin cash collection", defense.stage3_high_conviction_signals)
        self.assertIn("systemic exporter production disruption", labor.stage4c_thesis_break_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round293_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND293_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round293_cases_as_candidate_generation_input", record.green_guardrails)

        summary = round293_summary()
        self.assertEqual(summary["round_id"], "round_221")
        self.assertEqual(summary["large_sector"], "POLICY_GEOPOLITICS_DISASTER_EVENT")
        self.assertEqual(summary["case_candidate_count"], 9)
        self.assertEqual(summary["success_candidate_count"], 2)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 5)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 3)
        self.assertEqual(summary["stage4c_watch_count"], 6)
        self.assertEqual(summary["price_moved_without_evidence_count"], 2)
        self.assertEqual(summary["false_positive_score_count"], 6)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["hard_4c_confirmed"])

    def test_policy_event_cases_keep_stage2_4b_and_4c_separate(self) -> None:
        by_id = {case.case_id: case for case in ROUND293_CASE_CANDIDATES}
        blue_whale = by_id["r11_loop14_kogas_blue_whale_resource_event_premium"]
        sanctions = by_id["r11_loop14_hanwha_ocean_china_sanctions_4c_watch"]
        martial = by_id["r11_loop14_martial_law_political_liquidity_shock"]
        tax = by_id["r11_loop14_tax_policy_market_confidence_4c"]
        market = by_id["r11_loop14_short_selling_market_access_reform_stage2"]
        medical = by_id["r11_loop14_medical_reform_doctors_strike_service_disruption"]
        wildfire = by_id["r11_loop14_2025_wildfire_disaster_recovery_reference"]
        defense = by_id["r11_loop14_hanwha_aerospace_romania_k9_geopolitical_order"]
        labor = by_id["r11_loop14_samsung_strike_labor_policy_systemic_export_risk"]

        self.assertEqual(blue_whale.primary_archetype, E2RArchetype.RESOURCE_DISCOVERY_POLICY_EVENT_PREMIUM)
        self.assertEqual(blue_whale.extra_price_metrics["potential_resource_boe_bn"], 14.0)
        self.assertEqual(blue_whale.extra_price_metrics["success_probability_pct"], 20)
        self.assertEqual(blue_whale.event_mfe_pct, 30.0)
        self.assertEqual(blue_whale.score_price_alignment, "price_moved_without_evidence")

        self.assertTrue(sanctions.hard_4c_confirmed)
        self.assertEqual(sanctions.extra_price_metrics["hanwha_ocean_event_mae_pct"], -5.8)
        self.assertEqual(sanctions.extra_price_metrics["sanctioned_units_count"], 5)
        self.assertEqual(sanctions.rerating_result, "thesis_break")

        self.assertTrue(martial.hard_4c_confirmed)
        self.assertEqual(martial.extra_price_metrics["stock_stabilization_fund_krw_trn"], 10)
        self.assertEqual(martial.extra_price_metrics["bond_market_stabilization_fund_krw_trn"], 40)

        self.assertEqual(tax.extra_price_metrics["capital_gains_threshold_proposed_krw_bn"], 1)
        self.assertEqual(tax.extra_price_metrics["ai_tax_intraday_mae_pct"], -5.0)
        self.assertEqual(tax.stage4b_date.isoformat(), "2026-05-12")

        self.assertEqual(market.extra_price_metrics["short_selling_ban_lifted_after_years"], 5)
        self.assertEqual(market.extra_price_metrics["serious_short_sale_violation_fine_pct_of_order"], 100)
        self.assertEqual(market.stage_failure_type, "stage2_watch_success")

        self.assertTrue(medical.hard_4c_confirmed)
        self.assertEqual(medical.extra_price_metrics["trainee_doctors_walkout_count_reuters"], 9000)
        self.assertIn("surgery_cancellations", medical.extra_price_metrics["service_disruptions"])

        self.assertEqual(wildfire.extra_price_metrics["ap_later_deaths"], 28)
        self.assertEqual(wildfire.extra_price_metrics["ap_acres_burned"], 118265)
        self.assertTrue(wildfire.hard_4c_confirmed)

        self.assertEqual(defense.extra_price_metrics["order_value_usd_bn"], 1.0)
        self.assertEqual(defense.extra_price_metrics["backlog_growth_multiple"], 5.88)
        self.assertEqual(defense.stage_failure_type, "stage2_watch_success")

        self.assertTrue(labor.hard_4c_confirmed)
        self.assertEqual(labor.extra_price_metrics["single_day_halt_loss_krw_trn_max"], 1)
        self.assertEqual(labor.extra_price_metrics["prolonged_disruption_damage_krw_trn_max"], 100)
        self.assertEqual(labor.extra_price_metrics["samsung_export_share_pct"], 22.8)

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND293_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND293_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND293_PRICE_VALIDATION_FIELDS)
        shadow_rows = {row["archetype"]: row for row in round293_shadow_weight_rows()}
        deep_rows = round293_deep_sub_archetype_rows()
        green_markdown = render_round293_green_gate_review_markdown()
        stage_markdown = render_round293_stage4b_4c_review_markdown()

        self.assertIn("policy_implementation_certainty_confirmed", required)
        self.assertIn("defense_delivery_margin_cash_collection_confirmed", required)
        self.assertIn("resource_estimate_without_drilling", forbidden)
        self.assertIn("labor_relief_without_production_continuity", forbidden)
        self.assertIn("presidential_resource_announcement_plus_20_to_30pct", ROUND293_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("foreign_sanctions_blocking_transactions_or_cooperation", ROUND293_HARD_4C_GATES)
        self.assertIn("liquidity_facility_anchor", fields)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("Hanwha Ocean", stage_markdown)
        self.assertIn("hard-4C", stage_markdown)
        self.assertEqual(len(ROUND293_SHADOW_WEIGHT_ROWS), 9)
        self.assertEqual(shadow_rows["RESOURCE_DISCOVERY_POLICY_EVENT_PREMIUM"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["POLITICAL_LIQUIDITY_SHOCK_HARD_REFERENCE"]["hard_4c_sensitivity"], "+5")
        self.assertEqual(shadow_rows["MARKET_ACCESS_REFORM_STAGE2"]["market_access_flow"], "+5")
        self.assertTrue(any("Blue Whale" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Samsung strike" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round293_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_293.md")
        self.assertEqual(audit["round_id"], "round_221")
        self.assertEqual(audit["large_sector"], ROUND293_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round293_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round293_r11_loop14_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round293_case_rows()
            self.assertEqual(len(records), len(ROUND293_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND293_CASE_CANDIDATES))
            self.assertIn("Blue Whale", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("policy_implementation_certainty_confirmed", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("POLITICAL_LIQUIDITY_SHOCK_HARD_REFERENCE", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("liquidity_facility_anchor", paths["price_validation_plan"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["potential_resource_boe_bn"], 14.0)


if __name__ == "__main__":
    unittest.main()
