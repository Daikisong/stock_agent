from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round270_r1_loop13_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round270_r1_loop13_industrial_orders_infra_price_validation import (
    ROUND270_CASE_CANDIDATES,
    ROUND270_GREEN_FORBIDDEN_PATTERNS,
    ROUND270_GREEN_REQUIRED_FIELDS,
    ROUND270_HARD_4C_GATES,
    ROUND270_LARGE_SECTOR,
    ROUND270_PRICE_VALIDATION_FIELDS,
    ROUND270_REQUIRED_TARGET_ALIASES,
    ROUND270_SCORE_ADJUSTMENTS,
    ROUND270_SHADOW_WEIGHT_ROWS,
    ROUND270_STAGE4B_WATCH_TRIGGERS,
    render_round270_green_gate_review_markdown,
    render_round270_stage4b_4c_review_markdown,
    round270_audit_payload,
    round270_case_records,
    round270_case_rows,
    round270_deep_sub_archetype_rows,
    round270_shadow_weight_rows,
    round270_summary,
    write_round270_r1_loop13_reports,
)


class Round270R1Loop13IndustrialOrdersInfraPriceValidationTests(unittest.TestCase):
    def test_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND270_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND270_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND270_REQUIRED_TARGET_ALIASES["US_NAVAL_SHIPBUILDING_MASGA_CONSOLIDATION"],
            E2RArchetype.US_NAVAL_SHIPBUILDING_MASGA_CONSOLIDATION.value,
        )
        self.assertEqual(
            ROUND270_REQUIRED_TARGET_ALIASES["SHIPBUILDING_CONTRACT_CANCELLATION_HARD_4C"],
            E2RArchetype.SHIPBUILDING_CONTRACT_CANCELLATION_HARD_4C.value,
        )
        self.assertEqual(
            ROUND270_REQUIRED_TARGET_ALIASES["INDUSTRIAL_ROBOTICS_STRATEGIC_EQUITY_OPTION"],
            E2RArchetype.INDUSTRIAL_ROBOTICS_STRATEGIC_EQUITY_OPTION.value,
        )

    def test_archetype_definitions_encode_r1_loop13_gates(self) -> None:
        masga = archetype_definition(E2RArchetype.US_NAVAL_SHIPBUILDING_MASGA_CONSOLIDATION)
        sanction = archetype_definition(E2RArchetype.SHIPBUILDING_GEOPOLITICAL_SANCTION_4C)
        cancellation = archetype_definition(E2RArchetype.SHIPBUILDING_CONTRACT_CANCELLATION_HARD_4C)
        rail = archetype_definition(E2RArchetype.RAIL_EXPORT_MEGA_ORDER_STAGE2)
        marine = archetype_definition(E2RArchetype.MARINE_AFTERMARKET_RECURRING_SERVICE)
        robotics = archetype_definition(E2RArchetype.INDUSTRIAL_ROBOTICS_STRATEGIC_EQUITY_OPTION)
        kai = archetype_definition(E2RArchetype.DEFENSE_AEROSPACE_EXPORT_OPTIONALITY)

        self.assertIn("actual U.S. awards, integration synergy, margin, FCF and cash collection confirmed", masga.stage3_high_conviction_signals)
        self.assertIn("sanctioned subsidiary", sanction.stage4c_thesis_break_signals)
        self.assertIn("contract cancellation", cancellation.stage4c_thesis_break_signals)
        self.assertIn("delivery, localization, margin, FX, financing, and cash collection confirmed", rail.stage3_high_conviction_signals)
        self.assertIn("IPO pop or event premium prices the story before durability proof", marine.stage4b_graduation_overheat_signals)
        self.assertIn("strategic equity stake treated as robot revenue", robotics.false_positive_patterns)
        self.assertIn("sector YTD rally runs ahead of company-specific evidence", kai.stage4b_graduation_overheat_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round270_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND270_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_invent_price_or_stage_dates", record.green_guardrails)

        summary = round270_summary()
        self.assertEqual(summary["round_id"], "round_198")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 5)
        self.assertEqual(summary["cyclical_success_count"], 1)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 7)
        self.assertEqual(summary["stage4c_watch_or_hard_count"], 2)
        self.assertEqual(summary["price_data_unavailable_count"], 2)
        self.assertEqual(summary["price_moved_without_evidence_count"], 3)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["hard_4c_confirmed"])

    def test_shipbuilding_masga_sanction_and_cancellation_cases(self) -> None:
        by_id = {case.case_id: case for case in ROUND270_CASE_CANDIDATES}
        merger = by_id["r1_loop13_hd_hyundai_heavy_mipo_masga_merger"]
        hanwha = by_id["r1_loop13_hanwha_ocean_us_mro_china_sanction_watch"]
        samsung = by_id["r1_loop13_samsung_heavy_zvezda_cancellation_hard_4c"]

        self.assertEqual(merger.primary_archetype, E2RArchetype.US_NAVAL_SHIPBUILDING_MASGA_CONSOLIDATION)
        self.assertEqual(merger.stage2_date.isoformat(), "2025-08-27")
        self.assertEqual(merger.stage4b_date.isoformat(), "2025-08-27")
        self.assertEqual(merger.extra_price_metrics["hd_hyundai_heavy_event_mfe_pct"], 11.3)
        self.assertEqual(merger.extra_price_metrics["hd_hyundai_mipo_event_mfe_pct"], 14.6)
        self.assertIn("merger_headline_only", merger.red_flag_fields)

        self.assertEqual(hanwha.primary_archetype, E2RArchetype.SHIPBUILDING_GEOPOLITICAL_SANCTION_4C)
        self.assertEqual(hanwha.extra_price_metrics["reported_ytd_return_2025_pct"], 139.0)
        self.assertEqual(hanwha.extra_price_metrics["china_sanction_event_close_mae_pct"], -5.8)
        self.assertEqual(hanwha.extra_price_metrics["sanctioned_us_linked_subsidiaries"], 5.0)
        self.assertFalse(hanwha.hard_4c_confirmed)
        self.assertIn("geopolitical_retaliation_risk", hanwha.red_flag_fields)

        self.assertEqual(samsung.primary_archetype, E2RArchetype.SHIPBUILDING_CONTRACT_CANCELLATION_HARD_4C)
        self.assertEqual(samsung.stage4c_date.isoformat(), "2025-06-18")
        self.assertTrue(samsung.hard_4c_confirmed)
        self.assertEqual(samsung.extra_price_metrics["cancelled_orders_krw_trn"], 4.85)
        self.assertEqual(samsung.extra_price_metrics["cancelled_orders_usd_bn"], 3.54)
        self.assertEqual(samsung.rerating_result, "thesis_break")

    def test_rail_marine_robotics_kai_and_broad_cycle_cases_do_not_force_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND270_CASE_CANDIDATES}
        rotem = by_id["r1_loop13_hyundai_rotem_morocco_oncf_rail_order"]
        marine = by_id["r1_loop13_hd_hyundai_marine_solution_ipo_aftermarket"]
        rainbow = by_id["r1_loop13_rainbow_robotics_samsung_strategic_equity"]
        kai = by_id["r1_loop13_kai_defense_aerospace_export_optionality"]
        basket = by_id["r1_loop13_korean_shipbuilders_contract_cycle_4b"]

        self.assertIsNone(rotem.stage3_date)
        self.assertEqual(rotem.extra_price_metrics["order_value_krw_trn"], 2.2)
        self.assertEqual(rotem.extra_price_metrics["hyundai_rotem_unit_share_pct"], 65.5)
        self.assertIn("delivery_margin_cash_collection_unconfirmed", rotem.red_flag_fields)

        self.assertEqual(marine.case_type, "overheat")
        self.assertEqual(marine.stage2_price_anchor, 163900.0)
        self.assertEqual(marine.event_mfe_pct, 96.5)
        self.assertEqual(marine.extra_price_metrics["market_cap_to_op_2023"], 36.2)
        self.assertEqual(marine.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(rainbow.primary_archetype, E2RArchetype.INDUSTRIAL_ROBOTICS_STRATEGIC_EQUITY_OPTION)
        self.assertEqual(rainbow.extra_price_metrics["samsung_new_stake_value_krw_bn"], 267.0)
        self.assertFalse(rainbow.extra_price_metrics["actual_robot_order_revenue_confirmed"])
        self.assertIn("strategic_equity_investment_only", rainbow.red_flag_fields)

        self.assertEqual(kai.event_mfe_pct, 55.0)
        self.assertEqual(kai.extra_price_metrics["potential_korean_defense_orders_krw_trn"], 154.0)
        self.assertFalse(kai.extra_price_metrics["actual_kai_contract_delivery_margin_confirmed_in_source"])
        self.assertIn("defense_sector_rerating_only", kai.red_flag_fields)

        self.assertEqual(basket.case_type, "cyclical_success")
        self.assertEqual(basket.extra_price_metrics["samsung_heavy_event_mfe_pct"], 16.0)
        self.assertEqual(basket.extra_price_metrics["south_korea_global_orders_share_pct"], 50.0)
        self.assertIn("sector_order_cycle_not_individual_green", basket.red_flag_fields)

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND270_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND270_GREEN_FORBIDDEN_PATTERNS)
        review = render_round270_green_gate_review_markdown()
        stage_review = render_round270_stage4b_4c_review_markdown()
        fields = set(ROUND270_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND270_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round270_shadow_weight_rows()}
        deep_rows = round270_deep_sub_archetype_rows()

        self.assertIn("final_contract_signed", required)
        self.assertIn("cash_collection_confirmed", required)
        self.assertIn("actual_robot_order_and_revenue_confirmed", required)
        self.assertIn("merger_headline_only", forbidden)
        self.assertIn("ipo_pop_only", forbidden)
        self.assertIn("defense_sector_ytd_rally_only", forbidden)
        self.assertIn("final_contract_quality", axes)
        self.assertIn("contract_cancellation_risk", axes)
        self.assertIn("event_mfe_pct", fields)
        self.assertIn("ipo_day_plus_40_to_100pct", ROUND270_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("contract_cancellation", ROUND270_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("hard 4C", stage_review)
        self.assertEqual(len(ROUND270_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["SHIPBUILDING_CONTRACT_CANCELLATION_HARD_4C"]["hard_4c_sensitivity"], "+5")
        self.assertEqual(shadow_rows["MARINE_AFTERMARKET_RECURRING_SERVICE"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["INDUSTRIAL_ROBOTICS_STRATEGIC_EQUITY_OPTION"]["actual_robot_order_revenue"], "+5")
        self.assertTrue(any("MASGA" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Morocco ONCF" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Rainbow Robotics" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round270_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_270.md")
        self.assertEqual(audit["round_id"], "round_198")
        self.assertEqual(audit["large_sector"], ROUND270_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertEqual(len(audit["shadow_weights"]), 8)
        self.assertEqual(len(audit["deep_sub_archetypes"]), 8)
        self.assertIn("do_not_use_round270_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round270_r1_loop13_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round270_case_rows()
            self.assertEqual(len(records), len(ROUND270_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND270_CASE_CANDIDATES))
            self.assertIn("HD Hyundai Heavy", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Samsung Heavy", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Rainbow Robotics", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("final_contract_quality", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("US_NAVAL_SHIPBUILDING_MASGA_CONSOLIDATION", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("HD Hyundai Heavy", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["us_total_investment_package_usd_bn"], 350.0)


if __name__ == "__main__":
    unittest.main()
