from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round267_r11_loop12_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round267_r11_loop12_policy_geopolitical_event_price_validation import (
    ROUND267_CASE_CANDIDATES,
    ROUND267_GREEN_FORBIDDEN_PATTERNS,
    ROUND267_GREEN_REQUIRED_FIELDS,
    ROUND267_HARD_4C_GATES,
    ROUND267_PRICE_VALIDATION_FIELDS,
    ROUND267_REQUIRED_TARGET_ALIASES,
    ROUND267_SCORE_ADJUSTMENTS,
    ROUND267_SHADOW_WEIGHT_ROWS,
    ROUND267_STAGE4B_WATCH_TRIGGERS,
    render_round267_green_gate_review_markdown,
    render_round267_stage4b_4c_review_markdown,
    round267_audit_payload,
    round267_case_records,
    round267_case_rows,
    round267_deep_sub_archetype_rows,
    round267_shadow_weight_rows,
    round267_summary,
    write_round267_r11_loop12_reports,
)


class Round267R11Loop12PolicyGeopoliticalEventPriceValidationTests(unittest.TestCase):
    def test_round267_targets_map_to_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND267_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND267_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND267_REQUIRED_TARGET_ALIASES["LABOR_DISRUPTION_SYSTEMIC_POLICY_4C"],
            E2RArchetype.LABOR_DISRUPTION_SYSTEMIC_POLICY_4C.value,
        )
        self.assertEqual(
            ROUND267_REQUIRED_TARGET_ALIASES["GEOPOLITICAL_ENERGY_MACRO_HARD_4C"],
            E2RArchetype.GEOPOLITICAL_ENERGY_MACRO_HARD_4C.value,
        )
        self.assertEqual(
            ROUND267_REQUIRED_TARGET_ALIASES["CRITICAL_MINERALS_POLICY_RELIEF"],
            E2RArchetype.CRITICAL_MINERALS_POLICY_RELIEF.value,
        )

    def test_case_records_validate_and_keep_calibration_guardrails(self) -> None:
        records = round267_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.POLICY_GEOPOLITICAL_EVENT.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("do_not_treat_policy_geopolitical_disaster_fx_energy_labor_stablecoin_or_capex_headline_as_green", record.green_guardrails)

        summary = round267_summary()
        self.assertEqual(summary["analyst_round_id"], "round_195")
        self.assertEqual(summary["analyst_large_sector"], "POLICY_GEOPOLITICAL_DISASTER_EVENT")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 2)
        self.assertEqual(summary["event_premium_count"], 2)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 7)
        self.assertEqual(summary["stage4c_watch_count"], 3)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["policy_relief_count"], 3)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_round267_archetype_definitions_encode_policy_event_gates(self) -> None:
        labor = archetype_definition(E2RArchetype.LABOR_DISRUPTION_SYSTEMIC_POLICY_4C)
        energy = archetype_definition(E2RArchetype.GEOPOLITICAL_ENERGY_MACRO_HARD_4C)
        fiscal = archetype_definition(E2RArchetype.FISCAL_POLICY_RELIEF_NOT_GREEN)
        stablecoin = archetype_definition(E2RArchetype.STABLECOIN_FX_POLICY_OVERHEAT)
        rare_earth = archetype_definition(E2RArchetype.RARE_EARTH_END_USE_RESTRICTION_4C)
        capex = archetype_definition(E2RArchetype.REGIONAL_POLICY_CAPEX_EVENT_PREMIUM)

        self.assertIn("national export supply-chain risk", labor.stage1_radar_signals)
        self.assertIn("index, FX, oil and exporter shock is macro hard 4C", energy.stage3_high_conviction_signals)
        self.assertIn("only after company-level revenue, margin, EPS and FCF bridge is verified", fiscal.stage3_high_conviction_signals)
        self.assertIn("regulated revenue, FX stability, capital-flow control and company EPS/FCF bridge all verified", stablecoin.stage3_high_conviction_signals)
        self.assertIn("end-use license denial", rare_earth.stage4c_thesis_break_signals)
        self.assertIn("media-reported capex treated as Stage 3-Green before ROI", capex.false_positive_patterns)

    def test_middle_east_is_hard_4c_and_samsung_is_watch(self) -> None:
        by_id = {case.case_id: case for case in ROUND267_CASE_CANDIDATES}
        samsung = by_id["r11_loop12_samsung_strike_systemic_policy_4c_watch"]
        shock = by_id["r11_loop12_middle_east_iran_energy_macro_hard_4c"]

        self.assertFalse(samsung.hard_4c_confirmed)
        self.assertEqual(samsung.stage4c_date.isoformat(), "2026-05-15")
        self.assertEqual(samsung.mae_event, -9.3)
        self.assertEqual(samsung.extra_price_metrics["planned_strike_duration_days"], 18)
        self.assertEqual(samsung.extra_price_metrics["potential_workers_involved"], 50000)
        self.assertIn("strike_unresolved", samsung.red_flag_fields)

        self.assertTrue(shock.hard_4c_confirmed)
        self.assertEqual(shock.stage4c_date.isoformat(), "2026-03-04")
        self.assertEqual(shock.mae_event, -12.06)
        self.assertEqual(shock.stage4c_price_anchor, 5093.54)
        self.assertEqual(shock.extra_price_metrics["market_cap_wipeout_2d_krw_trn"], 817.6)
        self.assertEqual(shock.extra_price_metrics["krw_20260323_per_usd"], 1517.3)
        self.assertIn("kospi_historic_crash", shock.red_flag_fields)

    def test_policy_relief_and_event_premium_are_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND267_CASE_CANDIDATES}
        energy = by_id["r11_loop12_energy_saving_oil_budget_policy_relief"]
        fiscal = by_id["r11_loop12_ai_fiscal_room_policy_relief"]
        kospi = by_id["r11_loop12_kospi_7000_ai_capital_confidence_4b"]
        hyundai = by_id["r11_loop12_hyundai_saemangeum_regional_capex_event"]

        self.assertEqual(energy.extra_price_metrics["lng_saving_share_pct"], 20.3)
        self.assertEqual(energy.extra_price_metrics["supplementary_budget_krw_trn"], 26.2)
        self.assertFalse(energy.extra_price_metrics["new_bond_issuance"])
        self.assertIsNone(energy.stage3_date)

        self.assertFalse(fiscal.extra_price_metrics["new_treasury_bonds"])
        self.assertEqual(fiscal.extra_price_metrics["debt_to_gdp_after_budget_pct"], 50.6)

        self.assertEqual(kospi.stage4b_date.isoformat(), "2026-05-06")
        self.assertEqual(kospi.extra_price_metrics["samsung_mfe_pct"], 14.4)
        self.assertEqual(kospi.extra_price_metrics["foreign_net_purchase_krw_trn"], 3.1)
        self.assertIn("index_milestone_only", kospi.red_flag_fields)

        self.assertEqual(hyundai.extra_price_metrics["hyundai_mfe_pct"], 10.5)
        self.assertEqual(hyundai.extra_price_metrics["kia_mfe_pct"], 15.0)
        self.assertIn("capex_roi_unconfirmed", hyundai.red_flag_fields)

    def test_stablecoin_and_rare_earth_are_4c_watch_overlays(self) -> None:
        by_id = {case.case_id: case for case in ROUND267_CASE_CANDIDATES}
        stablecoin = by_id["r11_loop12_stablecoin_fx_policy_overheat"]
        rare_earth = by_id["r11_loop12_rare_earth_critical_minerals_policy_overlay"]

        self.assertEqual(stablecoin.primary_archetype, E2RArchetype.STABLECOIN_FX_POLICY_OVERHEAT)
        self.assertEqual(stablecoin.extra_price_metrics["me2on_mfe_pct"], 200.0)
        self.assertEqual(stablecoin.extra_price_metrics["stablecoin_trading_q1_krw_trn"], 57.0)
        self.assertFalse(stablecoin.extra_price_metrics["issuer_license_confirmed"])
        self.assertEqual(stablecoin.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(rare_earth.primary_archetype, E2RArchetype.RARE_EARTH_END_USE_RESTRICTION_4C)
        self.assertEqual(rare_earth.stage2_date.isoformat(), "2026-02-05")
        self.assertTrue(rare_earth.extra_price_metrics["sanction_warning"])
        self.assertEqual(rare_earth.extra_price_metrics["critical_minerals_monitored"], 17)
        self.assertEqual(rare_earth.extra_price_metrics["overseas_mining_support_krw_bn"], 250.0)
        self.assertIn("critical_mineral_export_block", rare_earth.red_flag_fields)

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND267_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND267_GREEN_FORBIDDEN_PATTERNS)
        review = render_round267_green_gate_review_markdown()
        stage_review = render_round267_stage4b_4c_review_markdown()
        fields = set(ROUND267_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND267_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round267_shadow_weight_rows()}
        deep_rows = round267_deep_sub_archetype_rows()

        self.assertIn("company_revenue_eps_fcf_bridge_exists", required)
        self.assertIn("operational_continuity_and_labor_risk_cleared", required)
        self.assertIn("stablecoin_theme_only", forbidden)
        self.assertIn("regional_capex_media_report_only", forbidden)
        self.assertIn("actual_supply_contract", axes)
        self.assertIn("energy_shock_unhedged", axes)
        self.assertIn("reported_price_anchor", fields)
        self.assertIn("supply_chain_anchor", fields)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("stablecoin policy + 2x basket rally before license revenue", review)
        self.assertIn("geopolitical_energy_chokepoint_closure", ROUND267_HARD_4C_GATES)
        self.assertIn("stablecoin_basket_two_to_three_times", ROUND267_STAGE4B_WATCH_TRIGGERS)
        self.assertEqual(len(ROUND267_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["GEOPOLITICAL_ENERGY_MACRO_HARD_4C"]["hard_4c_sensitivity"], "+5")
        self.assertEqual(shadow_rows["STABLECOIN_FX_POLICY_OVERHEAT"]["event_penalty"], "-5")
        self.assertTrue(any("Samsung strike" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Hyundai Saemangeum" in row["terms"] for row in deep_rows))
        self.assertIn("r11_loop12_middle_east_iran_energy_macro_hard_4c", stage_review)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round267_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_267.md")
        self.assertEqual(audit["analyst_round_id"], "round_195")
        self.assertEqual(audit["large_sector"], Round10LargeSector.POLICY_GEOPOLITICAL_EVENT.value)
        self.assertEqual(audit["analyst_large_sector"], "POLICY_GEOPOLITICAL_DISASTER_EVENT")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round267_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round267_r11_loop12_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round267_case_rows()
            self.assertEqual(len(records), len(ROUND267_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND267_CASE_CANDIDATES))
            self.assertIn("Middle East / Iran energy shock", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("systemic_operational_risk", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("STABLECOIN_FX_POLICY_OVERHEAT", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("Hyundai Saemangeum", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[-1]["extra_price_metrics"])["group_domestic_investment_plan_krw_trn"], 125.2)


if __name__ == "__main__":
    unittest.main()
