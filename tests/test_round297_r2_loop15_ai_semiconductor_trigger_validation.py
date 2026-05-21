from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round297_r2_loop15_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round297_r2_loop15_ai_semiconductor_trigger_validation import (
    ROUND297_CASE_CANDIDATES,
    ROUND297_GREEN_BLOCKERS,
    ROUND297_HARD_4C_GATES,
    ROUND297_LARGE_SECTOR,
    ROUND297_REQUIRED_TARGET_ALIASES,
    ROUND297_SCORE_DOWN_AXES,
    ROUND297_SCORE_UP_AXES,
    ROUND297_SHADOW_WEIGHT_ROWS,
    ROUND297_STAGE2_ACTIONABLE_RULES,
    ROUND297_STAGE3_GREEN_RULES,
    ROUND297_STAGE3_YELLOW_RULES,
    ROUND297_STAGE4B_WATCH_TRIGGERS,
    ROUND297_TRIGGER_RECORDS,
    render_round297_stage_rules_markdown,
    render_round297_stage4b_4c_review_markdown,
    render_round297_trigger_grid_markdown,
    round297_audit_payload,
    round297_case_records,
    round297_case_rows,
    round297_shadow_weight_rows,
    round297_summary,
    round297_trigger_rows,
    write_round297_r2_loop15_reports,
)


class Round297R2Loop15AISemiconductorTriggerValidationTests(unittest.TestCase):
    def test_round297_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND297_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND297_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND297_REQUIRED_TARGET_ALIASES["HBM_FIRST_MOVER_STAGE2_TO_GREEN"],
            E2RArchetype.HBM_FIRST_MOVER_STAGE2_TO_GREEN.value,
        )
        self.assertEqual(
            ROUND297_REQUIRED_TARGET_ALIASES["SEMICONDUCTOR_LABOR_SUPPLY_CHAIN_4C"],
            E2RArchetype.SEMICONDUCTOR_LABOR_SUPPLY_CHAIN_4C.value,
        )

    def test_archetype_definitions_capture_r2_loop15_rules(self) -> None:
        first = archetype_definition(E2RArchetype.HBM_FIRST_MOVER_STAGE2_TO_GREEN)
        equipment = archetype_definition(E2RArchetype.HBM_EQUIPMENT_STAGE2_ACTIONABLE)
        catchup = archetype_definition(E2RArchetype.HBM_CATCHUP_LATE_STAGE2)
        stargate = archetype_definition(E2RArchetype.OPENAI_STARGATE_MEMORY_4B_WATCH)
        export_control = archetype_definition(E2RArchetype.SEMICONDUCTOR_EXPORT_CONTROL_4C_WATCH)
        device = archetype_definition(E2RArchetype.AI_DEVICE_COMPONENT_STAGE2_ACTIONABLE)
        display = archetype_definition(E2RArchetype.DISPLAY_OLED_APPLE_RECOVERY_STAGE2)
        labor = archetype_definition(E2RArchetype.SEMICONDUCTOR_LABOR_SUPPLY_CHAIN_4C)

        self.assertIn("HBM mix, OP estimate revision, mass production and relative strength are visible", first.stage2_candidate_signals)
        self.assertIn("HBM equipment rumor without named customer order", equipment.false_positive_patterns)
        self.assertIn("late catch-up treated like first-mover Green", catchup.false_positive_patterns)
        self.assertIn("OpenAI or Nvidia headline after parabolic rally", stargate.stage4b_graduation_overheat_signals)
        self.assertIn("equipment license denial", export_control.stage4c_thesis_break_signals)
        self.assertIn("target-price raise treated as sell-through", device.false_positive_patterns)
        self.assertIn("loss beat treated as sustained profit", display.false_positive_patterns)
        self.assertIn("major strike disrupts DRAM/NAND supply", labor.stage4c_thesis_break_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round297_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND297_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("hard_4c_confirmed_false", record.green_guardrails)
            self.assertIn("do_not_use_round297_cases_as_candidate_generation_input", record.green_guardrails)

        summary = round297_summary()
        self.assertEqual(summary["round_id"], "round_225")
        self.assertEqual(summary["large_sector"], ROUND297_LARGE_SECTOR)
        self.assertEqual(summary["method"], "trigger_level_backtest_v1")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 10)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 6)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 4)
        self.assertEqual(summary["stage3_green_candidate_count"], 2)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 3)
        self.assertEqual(summary["stage4c_watch_count"], 5)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertEqual(summary["missed_structural_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_keep_trigger_quality_separate_from_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND297_CASE_CANDIDATES}
        hynix = by_id["r2_loop15_sk_hynix_hbm_first_mover"]
        hanmi = by_id["r2_loop15_hanmi_semiconductor_hbm_equipment"]
        samsung = by_id["r2_loop15_samsung_electronics_hbm_catchup_labor_watch"]
        openai = by_id["r2_loop15_sk_hynix_openai_asml_4b"]
        export = by_id["r2_loop15_memory_china_equipment_export_control"]
        innotek = by_id["r2_loop15_lg_innotek_apple_ai_upgrade"]
        display = by_id["r2_loop15_lg_display_apple_oled_recovery"]
        labor = by_id["r2_loop15_samsung_labor_supply_chain_4c"]

        self.assertEqual(hynix.primary_archetype, E2RArchetype.HBM_FIRST_MOVER_STAGE2_TO_GREEN)
        self.assertEqual(hynix.extra_price_metrics["t1_entry_price_anchor_krw"], 234500)
        self.assertEqual(hynix.extra_price_metrics["t2_market_relative_return_pp"], 7.3)
        self.assertEqual(hynix.extra_price_metrics["forward_return_anchor_2025_pct"], 274)
        self.assertEqual(hynix.score_price_alignment, "missed_due_to_score")

        self.assertEqual(hanmi.primary_archetype, E2RArchetype.HBM_EQUIPMENT_STAGE2_ACTIONABLE)
        self.assertEqual(hanmi.extra_price_metrics["sk_hynix_supply_deal_krw_bn"], 21.48)
        self.assertEqual(hanmi.extra_price_metrics["market_relative_return_pp"], 15.3)

        self.assertEqual(samsung.primary_archetype, E2RArchetype.HBM_CATCHUP_LATE_STAGE2)
        self.assertEqual(samsung.extra_price_metrics["relative_to_sk_hynix_pp"], -7.3)
        self.assertEqual(samsung.extra_price_metrics["labor_strike_workers_context"], 48000)
        self.assertIn(E2RArchetype.SEMICONDUCTOR_LABOR_SUPPLY_CHAIN_4C, samsung.secondary_archetypes)

        self.assertEqual(openai.primary_archetype, E2RArchetype.OPENAI_STARGATE_MEMORY_4B_WATCH)
        self.assertEqual(openai.extra_price_metrics["t2_event_price_krw"], 1447000)
        self.assertEqual(openai.extra_price_metrics["asml_order_krw_trn"], 11.95)
        self.assertEqual(openai.case_type, "4b_watch")

        self.assertEqual(export.primary_archetype, E2RArchetype.SEMICONDUCTOR_EXPORT_CONTROL_4C_WATCH)
        self.assertEqual(export.extra_price_metrics["sk_hynix_event_mae_pct"], -5.0)
        self.assertFalse(export.hard_4c_confirmed)

        self.assertEqual(innotek.primary_archetype, E2RArchetype.AI_DEVICE_COMPONENT_STAGE2_ACTIONABLE)
        self.assertEqual(innotek.stage2_price_anchor, 272000)
        self.assertEqual(innotek.extra_price_metrics["t2_op_estimate_vs_consensus_pct"], 31.2)

        self.assertEqual(display.primary_archetype, E2RArchetype.DISPLAY_OLED_APPLE_RECOVERY_STAGE2)
        self.assertEqual(display.extra_price_metrics["loss_beat_amount_krw_bn"], 214)
        self.assertTrue(display.extra_price_metrics["second_half_profitability_guidance_refused"])

        self.assertEqual(labor.primary_archetype, E2RArchetype.SEMICONDUCTOR_LABOR_SUPPLY_CHAIN_4C)
        self.assertEqual(labor.extra_price_metrics["strike_days"], 18)
        self.assertFalse(labor.hard_4c_confirmed)

    def test_trigger_rows_and_shadow_rules_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round297_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round297_shadow_weight_rows()}
        rules_md = render_round297_stage_rules_markdown()
        trigger_md = render_round297_trigger_grid_markdown()
        stage_md = render_round297_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND297_TRIGGER_RECORDS), 10)
        self.assertEqual(trigger_rows["r2l15_skhynix_T2"]["promote_to"], "Stage3-Yellow")
        self.assertEqual(trigger_rows["r2l15_skhynix_openai_T1"]["promote_to"], "Stage3-Green+4B")
        self.assertEqual(trigger_rows["r2l15_export_control_T1"]["promote_to"], "4C-watch")
        self.assertEqual(len(ROUND297_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["HBM_FIRST_MOVER_STAGE2_TO_GREEN"]["hbm_mix_revenue_share"], "+5")
        self.assertEqual(shadow_rows["HBM_CATCHUP_LATE_STAGE2"]["late_catchup_penalty"], "-4")
        self.assertEqual(shadow_rows["SEMICONDUCTOR_LABOR_SUPPLY_CHAIN_4C"]["labor_continuity_4c_overlay"], "+5")
        self.assertIn("hbm_mix_or_ai_revenue_share_or_op_estimate_is_quantified", ROUND297_STAGE2_ACTIONABLE_RULES)
        self.assertIn("forward_allocation_margin_capacity_or_customer_concentration_still_pending", ROUND297_STAGE3_YELLOW_RULES)
        self.assertIn("hbm_or_ai_component_revenue_confirmed_in_actual_results", ROUND297_STAGE3_GREEN_RULES)
        self.assertIn("late_catchup_without_relative_strength", ROUND297_GREEN_BLOCKERS)
        self.assertIn("hbm_mix_revenue_share", ROUND297_SCORE_UP_AXES)
        self.assertIn("openai_or_nvidia_headline_after_parabolic_rally", ROUND297_SCORE_DOWN_AXES)
        self.assertIn("possible_listing_or_share_issuance_after_success", ROUND297_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("major_labor_strike_disrupting_memory_supply", ROUND297_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("SK Hynix", trigger_md)
        self.assertIn("hard 4C 확정은 없다", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round297_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_297.md")
        self.assertEqual(audit["round_id"], "round_225")
        self.assertEqual(audit["large_sector"], ROUND297_LARGE_SECTOR)
        self.assertEqual(audit["method"], "trigger_level_backtest_v1")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_AI_HBM_theme_only_as_revenue_margin_evidence", audit["what_not_to_change"])

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
            paths = write_round297_r2_loop15_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round297_case_rows()
            self.assertEqual(len(records), len(ROUND297_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND297_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND297_TRIGGER_RECORDS))
            self.assertIn("SK Hynix", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Stage2-Actionable", paths["stage_rules"].read_text(encoding="utf-8"))
            self.assertIn("r2l15_lginnotek_T1", paths["trigger_grid_md"].read_text(encoding="utf-8"))
            self.assertIn("HBM_FIRST_MOVER_STAGE2_TO_GREEN", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("SEMICONDUCTOR_EXPORT_CONTROL_4C_WATCH", paths["weight_profile"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["t1_entry_price_anchor_krw"], 234500)


if __name__ == "__main__":
    unittest.main()
