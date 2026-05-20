from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round283_r1_loop14_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round283_r1_loop14_industrial_orders_infrastructure_price_validation import (
    ROUND283_CASE_CANDIDATES,
    ROUND283_GREEN_FORBIDDEN_PATTERNS,
    ROUND283_GREEN_REQUIRED_FIELDS,
    ROUND283_HARD_4C_GATES,
    ROUND283_LARGE_SECTOR,
    ROUND283_PRICE_VALIDATION_FIELDS,
    ROUND283_REQUIRED_TARGET_ALIASES,
    ROUND283_SHADOW_WEIGHT_ROWS,
    ROUND283_STAGE4B_WATCH_TRIGGERS,
    render_round283_green_gate_review_markdown,
    render_round283_stage4b_4c_review_markdown,
    round283_audit_payload,
    round283_case_records,
    round283_case_rows,
    round283_deep_sub_archetype_rows,
    round283_shadow_weight_rows,
    round283_summary,
    write_round283_r1_loop14_reports,
)


class Round283R1Loop14IndustrialsPriceValidationTests(unittest.TestCase):
    def test_round283_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND283_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND283_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND283_REQUIRED_TARGET_ALIASES["DEFENSE_EXPORT_DELIVERY_STAGE3_CANDIDATE"],
            E2RArchetype.DEFENSE_EXPORT_DELIVERY_STAGE3_CANDIDATE.value,
        )
        self.assertEqual(
            ROUND283_REQUIRED_TARGET_ALIASES["SHIPBUILDING_ORDER_CANCELLATION_HARD_4C"],
            E2RArchetype.SHIPBUILDING_ORDER_CANCELLATION_HARD_4C.value,
        )
        self.assertEqual(
            ROUND283_REQUIRED_TARGET_ALIASES["INDUSTRIAL_SERVICE_IPO_OVERHEAT"],
            E2RArchetype.INDUSTRIAL_SERVICE_IPO_OVERHEAT.value,
        )

    def test_round283_archetype_definitions_capture_r1_loop14_gates(self) -> None:
        defense = archetype_definition(E2RArchetype.DEFENSE_EXPORT_DELIVERY_STAGE3_CANDIDATE)
        grid = archetype_definition(E2RArchetype.GRID_EQUIPMENT_US_GROWTH_STAGE2)
        transformer = archetype_definition(E2RArchetype.TRANSFORMER_CAPACITY_EXPANSION_STAGE2)
        merger = archetype_definition(E2RArchetype.SHIPBUILDING_MERGER_MASGA_4B)
        cancellation = archetype_definition(E2RArchetype.SHIPBUILDING_ORDER_CANCELLATION_HARD_4C)
        dilution = archetype_definition(E2RArchetype.DEFENSE_DILUTION_FALSE_POSITIVE)
        robotics = archetype_definition(E2RArchetype.ROBOTICS_STRATEGIC_STAKE_EVENT_PREMIUM)
        ipo = archetype_definition(E2RArchetype.INDUSTRIAL_SERVICE_IPO_OVERHEAT)

        self.assertIn("actual delivery revenue recognition", defense.stage3_high_conviction_signals)
        self.assertIn("estimate upgrade treated as Green without backlog/margin", grid.false_positive_patterns)
        self.assertIn("capacity expansion without backlog", transformer.false_positive_patterns)
        self.assertIn("MASGA headline treated as funded order", merger.false_positive_patterns)
        self.assertIn("large contract cancellation", cancellation.stage4c_thesis_break_signals)
        self.assertIn("dilutive share issue after theme rally", dilution.stage4c_thesis_break_signals)
        self.assertIn("parent name treated as robot shipment", robotics.false_positive_patterns)
        self.assertIn("IPO first-day pop only", ipo.false_positive_patterns)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round283_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND283_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("hard_4c_confirmed_true_for_samsung_heavy_zvezda", record.green_guardrails)
            self.assertIn("do_not_use_round283_cases_as_candidate_generation_input", record.green_guardrails)

        summary = round283_summary()
        self.assertEqual(summary["round_id"], "round_211")
        self.assertEqual(summary["large_sector"], "INDUSTRIALS_ORDERS_INFRASTRUCTURE")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 2)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["event_premium_or_result_count"], 3)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 1)
        self.assertEqual(summary["stage4b_watch_count"], 4)
        self.assertEqual(summary["stage4c_watch_count"], 2)
        self.assertEqual(summary["price_moved_without_evidence_count"], 2)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 1)
        self.assertEqual(summary["false_positive_score_count"], 3)
        self.assertEqual(summary["aligned_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["hard_4c_confirmed"])

    def test_round283_cases_keep_industrial_anchors_separate_from_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND283_CASE_CANDIDATES}
        rotem = by_id["r1_loop14_hyundai_rotem_k2_poland_delivery_stage3_candidate"]
        ls = by_id["r1_loop14_ls_electric_us_grid_growth_price_failed"]
        hyosung = by_id["r1_loop14_hyosung_heavy_hico_transformer_capacity"]
        merger = by_id["r1_loop14_hd_hhi_mipo_merger_masga_4b"]
        samsung = by_id["r1_loop14_samsung_heavy_zvezda_cancellation_hard_4c"]
        hanwha = by_id["r1_loop14_hanwha_aerospace_share_sale_dilution"]
        rainbow = by_id["r1_loop14_rainbow_robotics_samsung_stake_event"]
        marine = by_id["r1_loop14_hd_hyundai_marine_ipo_overheat"]

        self.assertEqual(rotem.primary_archetype, E2RArchetype.DEFENSE_EXPORT_DELIVERY_STAGE3_CANDIDATE)
        self.assertEqual(rotem.stage3_price_anchor, 41300)
        self.assertEqual(rotem.event_mfe_pct, 9.3)
        self.assertEqual(rotem.extra_price_metrics["q1_revenue_from_18_k2_shipments_krw_bn"], 270)
        self.assertEqual(rotem.extra_price_metrics["q1_op_estimate_krw_bn"], 59.1)
        self.assertEqual(rotem.extra_price_metrics["second_contract_value_usd_bn"], 6.5)
        self.assertEqual(rotem.score_price_alignment, "aligned")

        self.assertEqual(ls.primary_archetype, E2RArchetype.GRID_EQUIPMENT_US_GROWTH_STAGE2)
        self.assertEqual(ls.stage2_price_anchor, 208500)
        self.assertEqual(ls.event_mae_pct, -5.4)
        self.assertEqual(ls.extra_price_metrics["us_revenue_share_2024_expected_pct"], 20)
        self.assertEqual(ls.extra_price_metrics["target_price_raise_pct"], 87)
        self.assertEqual(ls.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(hyosung.primary_archetype, E2RArchetype.TRANSFORMER_CAPACITY_EXPANSION_STAGE2)
        self.assertEqual(hyosung.extra_price_metrics["gsu_transformer_demand_growth_since_2019_pct"], 274)
        self.assertEqual(hyosung.extra_price_metrics["gsu_delivery_delay_weeks"], 143)
        self.assertEqual(hyosung.extra_price_metrics["hyosung_hico_memphis_expansion_usd_mn"], 157)
        self.assertEqual(hyosung.score_price_alignment, "unknown")

        self.assertEqual(merger.primary_archetype, E2RArchetype.SHIPBUILDING_MERGER_MASGA_4B)
        self.assertEqual(merger.extra_price_metrics["hd_hyundai_heavy_event_mfe_pct"], 11.3)
        self.assertEqual(merger.extra_price_metrics["hd_hyundai_mipo_event_mfe_pct"], 14.6)
        self.assertEqual(merger.extra_price_metrics["exchange_ratio_mipo_to_hhi"], 1.04059146)
        self.assertEqual(merger.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(samsung.primary_archetype, E2RArchetype.SHIPBUILDING_ORDER_CANCELLATION_HARD_4C)
        self.assertEqual(samsung.extra_price_metrics["cancelled_contract_value_krw_trn"], 4.85)
        self.assertEqual(samsung.extra_price_metrics["cancelled_contract_value_usd_bn"], 3.54)
        self.assertEqual(samsung.extra_price_metrics["icebreaker_lng_carriers"], 10)
        self.assertEqual(samsung.extra_price_metrics["icebreaker_shuttle_tankers"], 7)
        self.assertTrue(samsung.hard_4c_confirmed)
        self.assertEqual(samsung.rerating_result, "thesis_break")

        self.assertEqual(hanwha.primary_archetype, E2RArchetype.DEFENSE_DILUTION_FALSE_POSITIVE)
        self.assertEqual(hanwha.extra_price_metrics["initial_share_sale_krw_trn"], 3.6)
        self.assertEqual(hanwha.event_mae_pct, -13.0)
        self.assertEqual(hanwha.extra_price_metrics["planned_new_shares_mn"], 6)
        self.assertEqual(hanwha.extra_price_metrics["initial_issue_price_krw"], 605000)
        self.assertEqual(hanwha.extra_price_metrics["revised_affiliate_issue_krw_trn"], 1.3)
        self.assertEqual(hanwha.extra_price_metrics["separate_rights_offering_krw_trn"], 2.3)
        self.assertEqual(hanwha.score_price_alignment, "false_positive_score")

        self.assertEqual(rainbow.primary_archetype, E2RArchetype.ROBOTICS_STRATEGIC_STAKE_EVENT_PREMIUM)
        self.assertEqual(rainbow.extra_price_metrics["new_samsung_stake_investment_krw_bn"], 267)
        self.assertEqual(rainbow.extra_price_metrics["new_samsung_stake_investment_usd_mn"], 181)
        self.assertEqual(rainbow.extra_price_metrics["samsung_prior_stake_pct"], 14.71)
        self.assertFalse(rainbow.extra_price_metrics["actual_robot_shipments_confirmed"])

        self.assertEqual(marine.primary_archetype, E2RArchetype.INDUSTRIAL_SERVICE_IPO_OVERHEAT)
        self.assertEqual(marine.extra_price_metrics["ipo_price_krw"], 83400)
        self.assertEqual(marine.extra_price_metrics["close_price_krw"], 163900)
        self.assertEqual(marine.extra_price_metrics["debut_mfe_pct"], 96.5)
        self.assertEqual(marine.extra_price_metrics["revenue_2023_krw_trn"], 1.43)
        self.assertEqual(marine.extra_price_metrics["op_2023_krw_bn"], 201.47)
        self.assertEqual(marine.score_price_alignment, "false_positive_score")

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND283_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND283_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND283_PRICE_VALIDATION_FIELDS)
        shadow_rows = {row["archetype"]: row for row in round283_shadow_weight_rows()}
        deep_rows = round283_deep_sub_archetype_rows()
        green_markdown = render_round283_green_gate_review_markdown()
        stage_markdown = render_round283_stage4b_4c_review_markdown()

        self.assertIn("actual_delivery_revenue_confirmed", required)
        self.assertIn("working_capital_control_confirmed", required)
        self.assertIn("aftermarket_IPO_demand_confirmed", required)
        self.assertIn("IPO_first_day_pop_only", forbidden)
        self.assertIn("strategic_stake_only", forbidden)
        self.assertIn("IPO_debut_40_100pct_pop", ROUND283_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("large_contract_cancellation", ROUND283_HARD_4C_GATES)
        self.assertIn("dilutive_share_issue_after_theme_rally", ROUND283_HARD_4C_GATES)
        self.assertIn("cancellation_value_anchor", fields)
        self.assertIn("IPO_price_anchor", fields)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("Samsung Heavy", stage_markdown)
        self.assertIn("hard-4C", stage_markdown)
        self.assertEqual(len(ROUND283_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["DEFENSE_EXPORT_DELIVERY_STAGE3_CANDIDATE"]["actual_delivery_revenue"], "+5")
        self.assertEqual(shadow_rows["SHIPBUILDING_ORDER_CANCELLATION_HARD_4C"]["hard_4c_sensitivity"], "+5")
        self.assertEqual(shadow_rows["INDUSTRIAL_SERVICE_IPO_OVERHEAT"]["event_penalty"], "-5")
        self.assertTrue(any("Hyundai Rotem" in row["terms"] for row in deep_rows))
        self.assertTrue(any("HD Hyundai Marine Solution" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round283_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_283.md")
        self.assertEqual(audit["round_id"], "round_211")
        self.assertEqual(audit["large_sector"], ROUND283_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertIn("do_not_use_round283_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round283_r1_loop14_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round283_case_rows()
            self.assertEqual(len(records), len(ROUND283_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND283_CASE_CANDIDATES))
            self.assertIn("Hyundai Rotem", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("actual_delivery_revenue_confirmed", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("DEFENSE_DILUTION_FALSE_POSITIVE", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("cancellation_value_anchor", paths["price_validation_plan"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["q1_revenue_from_18_k2_shipments_krw_bn"], 270)


if __name__ == "__main__":
    unittest.main()
