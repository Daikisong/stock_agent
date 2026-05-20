from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round296_r1_loop15_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round296_r1_loop15_industrial_trigger_validation import (
    ROUND296_CASE_CANDIDATES,
    ROUND296_HARD_4C_GATES,
    ROUND296_LARGE_SECTOR,
    ROUND296_REQUIRED_TARGET_ALIASES,
    ROUND296_SCORE_DOWN_AXES,
    ROUND296_SCORE_UP_AXES,
    ROUND296_SHADOW_WEIGHT_ROWS,
    ROUND296_STAGE2_ACTIONABLE_RULES,
    ROUND296_STAGE3_YELLOW_RULES,
    ROUND296_STAGE4B_WATCH_TRIGGERS,
    ROUND296_TRIGGER_RECORDS,
    render_round296_stage_rules_markdown,
    render_round296_stage4b_4c_review_markdown,
    render_round296_trigger_grid_markdown,
    round296_audit_payload,
    round296_case_records,
    round296_case_rows,
    round296_shadow_weight_rows,
    round296_summary,
    round296_trigger_rows,
    write_round296_r1_loop15_reports,
)


class Round296R1Loop15IndustrialTriggerValidationTests(unittest.TestCase):
    def test_round296_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND296_REQUIRED_TARGET_ALIASES), 7)
        self.assertTrue(set(ROUND296_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND296_REQUIRED_TARGET_ALIASES["DEFENSE_EXPORT_STAGE2_ACTIONABLE"],
            E2RArchetype.DEFENSE_EXPORT_STAGE2_ACTIONABLE.value,
        )
        self.assertEqual(
            ROUND296_REQUIRED_TARGET_ALIASES["NUCLEAR_EXPORT_PREFERRED_BIDDER_STAGE2"],
            E2RArchetype.NUCLEAR_EXPORT_PREFERRED_BIDDER_STAGE2.value,
        )

    def test_archetype_definitions_capture_trigger_level_rules(self) -> None:
        rotem = archetype_definition(E2RArchetype.DEFENSE_EXPORT_STAGE2_ACTIONABLE)
        lig = archetype_definition(E2RArchetype.MISSILE_DEFENSE_ORDER_4B_TIMING)
        hanwha = archetype_definition(E2RArchetype.DEFENSE_BACKLOG_DILUTION_OVERLAY)
        ship = archetype_definition(E2RArchetype.SHIPBUILDING_BACKLOG_PRICE_STAGE2_ACTIONABLE)
        grid = archetype_definition(E2RArchetype.GRID_EQUIPMENT_US_GROWTH_STAGE2_PROMOTE)
        epc = archetype_definition(E2RArchetype.OVERSEAS_EPC_ORDER_STAGE2_YELLOW)
        nuclear = archetype_definition(E2RArchetype.NUCLEAR_EXPORT_PREFERRED_BIDDER_STAGE2)

        self.assertIn("shipment, OP estimate beat, export revenue contribution and relative strength are visible", rotem.stage2_candidate_signals)
        self.assertIn("4B trim treated as hard exit while order pipeline remains", lig.false_positive_patterns)
        self.assertIn("4B dilution cancels historical Stage3 evidence", hanwha.false_positive_patterns)
        self.assertIn("orders, ship-price index, backlog duration and broad relative strength are visible", ship.stage2_candidate_signals)
        self.assertIn("target price raise without price strength", grid.false_positive_patterns)
        self.assertIn("event pop without margin visibility", epc.false_positive_patterns)
        self.assertIn("court blocks signing", nuclear.stage4c_thesis_break_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round296_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND296_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("stage_candidate_not_downgraded_for_missing_full_ohlc", record.green_guardrails)
            self.assertIn("do_not_use_round296_cases_as_candidate_generation_input", record.green_guardrails)

        summary = round296_summary()
        self.assertEqual(summary["round_id"], "round_224")
        self.assertEqual(summary["large_sector"], ROUND296_LARGE_SECTOR)
        self.assertEqual(summary["method"], "trigger_level_backtest_v1")
        self.assertEqual(summary["case_candidate_count"], 7)
        self.assertEqual(summary["trigger_count"], 9)
        self.assertEqual(summary["stage2_promote_candidate_count"], 7)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 4)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 4)
        self.assertEqual(summary["legal_4c_watch_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 1)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_keep_trigger_quality_separate_from_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND296_CASE_CANDIDATES}
        rotem = by_id["r1_loop15_hyundai_rotem_k2_poland"]
        lig = by_id["r1_loop15_lig_nex1_msam"]
        hanwha = by_id["r1_loop15_hanwha_aerospace_k9_backlog_dilution"]
        ship = by_id["r1_loop15_shipbuilding_order_price_basket"]
        ls = by_id["r1_loop15_ls_electric_us_grid"]
        ena = by_id["r1_loop15_samsung_ena_fadhili"]
        nuclear = by_id["r1_loop15_czech_nuclear_doosan"]

        self.assertEqual(rotem.primary_archetype, E2RArchetype.DEFENSE_EXPORT_STAGE2_ACTIONABLE)
        self.assertEqual(rotem.best_trigger, "T2/T3")
        self.assertEqual(rotem.extra_price_metrics["op_estimate_vs_consensus_pct"], 33.1)
        self.assertEqual(rotem.extra_price_metrics["market_relative_return_pp"], 9.6)
        self.assertEqual(rotem.score_price_alignment, "missed_due_to_score")

        self.assertEqual(lig.primary_archetype, E2RArchetype.MISSILE_DEFENSE_ORDER_4B_TIMING)
        self.assertEqual(lig.extra_price_metrics["t2_4b_event_mae_pct"], -11)
        self.assertEqual(lig.extra_price_metrics["iraq_order_value_usd_bn"], 2.8)

        self.assertEqual(hanwha.primary_archetype, E2RArchetype.DEFENSE_BACKLOG_DILUTION_OVERLAY)
        self.assertEqual(hanwha.extra_price_metrics["backlog_growth_multiple"], 5.88)
        self.assertEqual(hanwha.extra_price_metrics["t4_event_mae_pct"], -13)
        self.assertEqual(hanwha.rerating_result, "true_rerating")

        self.assertEqual(ship.primary_archetype, E2RArchetype.SHIPBUILDING_BACKLOG_PRICE_STAGE2_ACTIONABLE)
        self.assertEqual(ship.extra_price_metrics["global_new_orders_yoy_pct"], 18)
        self.assertEqual(ship.extra_price_metrics["newbuilding_price_index"], 181.81)

        self.assertEqual(ls.primary_archetype, E2RArchetype.GRID_EQUIPMENT_US_GROWTH_STAGE2_PROMOTE)
        self.assertEqual(ls.extra_price_metrics["target_raise_pct"], 86.7)
        self.assertEqual(ls.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(ena.primary_archetype, E2RArchetype.OVERSEAS_EPC_ORDER_STAGE2_YELLOW)
        self.assertIn("working_capital", ena.extra_price_metrics["stage3_green_gate_missing"])
        self.assertEqual(ena.stage_candidate, "Stage3-Yellow")

        self.assertEqual(nuclear.primary_archetype, E2RArchetype.NUCLEAR_EXPORT_PREFERRED_BIDDER_STAGE2)
        self.assertFalse(nuclear.extra_price_metrics["final_contract_signed"])
        self.assertEqual(nuclear.case_type, "event_premium")

    def test_trigger_rows_and_shadow_rules_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round296_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round296_shadow_weight_rows()}
        rules_md = render_round296_stage_rules_markdown()
        trigger_md = render_round296_trigger_grid_markdown()
        stage_md = render_round296_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND296_TRIGGER_RECORDS), 9)
        self.assertEqual(trigger_rows["r1l15_hyundai_rotem_T2"]["promote_to"], "Stage3-Yellow")
        self.assertEqual(trigger_rows["r1l15_lig_nex1_T2"]["promote_to"], "4B_trim")
        self.assertEqual(trigger_rows["r1l15_ls_electric_T2"]["event_return_pct"], "-5.4")
        self.assertEqual(len(ROUND296_SHADOW_WEIGHT_ROWS), 7)
        self.assertEqual(shadow_rows["DEFENSE_EXPORT_STAGE2_ACTIONABLE"]["shipment_revenue_contribution"], "+5")
        self.assertEqual(shadow_rows["NUCLEAR_EXPORT_PREFERRED_BIDDER_STAGE2"]["preferred_bidder_only_penalty"], "-5")
        self.assertIn("shipment_delivery_calloff_or_revenue_contribution_confirmed", ROUND296_STAGE2_ACTIONABLE_RULES)
        self.assertIn("margin_cash_collection_final_delivery_or_legal_clearance_still_pending", ROUND296_STAGE3_YELLOW_RULES)
        self.assertIn("shipment_revenue_contribution", ROUND296_SCORE_UP_AXES)
        self.assertIn("preferred_bidder_only", ROUND296_SCORE_DOWN_AXES)
        self.assertIn("YTD_double_plus_then_large_share_sale_CB_or_capital_raise", ROUND296_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("final_contract_blocked_by_court_or_regulator", ROUND296_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("Hyundai Rotem", trigger_md)
        self.assertIn("hard 4C 확정은 없다", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round296_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_296.md")
        self.assertEqual(audit["round_id"], "round_224")
        self.assertEqual(audit["large_sector"], ROUND296_LARGE_SECTOR)
        self.assertEqual(audit["method"], "trigger_level_backtest_v1")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_downgrade_stage_candidate_merely_because_full_ohlc_is_missing", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--triggers", "triggers.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.triggers, "triggers.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round296_r1_loop15_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round296_case_rows()
            self.assertEqual(len(records), len(ROUND296_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND296_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND296_TRIGGER_RECORDS))
            self.assertIn("Hyundai Rotem", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Stage2-Actionable", paths["stage_rules"].read_text(encoding="utf-8"))
            self.assertIn("r1l15_samsung_ena_T2", paths["trigger_grid_md"].read_text(encoding="utf-8"))
            self.assertIn("DEFENSE_EXPORT_STAGE2_ACTIONABLE", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["target_upside_from_event_price_pct"], 15.0)


if __name__ == "__main__":
    unittest.main()
