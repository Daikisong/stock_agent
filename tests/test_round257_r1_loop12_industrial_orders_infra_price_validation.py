from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round257_r1_loop12_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round257_r1_loop12_industrial_orders_infra_price_validation import (
    ROUND257_CASE_CANDIDATES,
    ROUND257_GREEN_FORBIDDEN_PATTERNS,
    ROUND257_GREEN_REQUIRED_FIELDS,
    ROUND257_HARD_4C_GATES,
    ROUND257_LARGE_SECTOR,
    ROUND257_PRICE_VALIDATION_FIELDS,
    ROUND257_REQUIRED_TARGET_ALIASES,
    ROUND257_SCORE_ADJUSTMENTS,
    ROUND257_SHADOW_WEIGHT_ROWS,
    ROUND257_STAGE4B_WATCH_TRIGGERS,
    render_round257_green_gate_review_markdown,
    render_round257_stage4b_4c_review_markdown,
    round257_audit_payload,
    round257_case_records,
    round257_case_rows,
    round257_deep_sub_archetype_rows,
    round257_shadow_weight_rows,
    round257_summary,
    write_round257_r1_loop12_reports,
)


class Round257R1Loop12IndustrialOrdersInfraPriceValidationTests(unittest.TestCase):
    def test_round257_targets_are_explicit_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND257_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND257_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND257_REQUIRED_TARGET_ALIASES["DEFENSE_EXPORT_BACKLOG_COMPOUNDING"],
            E2RArchetype.DEFENSE_EXPORT_BACKLOG_COMPOUNDING.value,
        )
        self.assertEqual(
            ROUND257_REQUIRED_TARGET_ALIASES["GRID_TRANSFORMER_DATA_CENTER_BOTTLENECK"],
            E2RArchetype.GRID_TRANSFORMER_DATA_CENTER_BOTTLENECK.value,
        )
        self.assertEqual(
            ROUND257_REQUIRED_TARGET_ALIASES["DILUTION_AFTER_RERATING_4B"],
            E2RArchetype.DILUTION_AFTER_RERATING_4B.value,
        )

    def test_new_round257_archetype_definitions_are_available(self) -> None:
        defense = archetype_definition(E2RArchetype.DEFENSE_EXPORT_BACKLOG_COMPOUNDING)
        missile = archetype_definition(E2RArchetype.MISSILE_DEFENSE_COMBAT_VALIDATION)
        armored = archetype_definition(E2RArchetype.ARMORED_VEHICLE_DELIVERY_TO_REVENUE)
        grid = archetype_definition(E2RArchetype.GRID_TRANSFORMER_DATA_CENTER_BOTTLENECK)
        localization = archetype_definition(E2RArchetype.US_GRID_EQUIPMENT_LOCALIZATION)
        dilution = archetype_definition(E2RArchetype.DILUTION_AFTER_RERATING_4B)

        self.assertIn("delivery to revenue", defense.stage3_high_conviction_signals)
        self.assertIn("production cycle advantage", missile.stage2_candidate_signals)
        self.assertIn("export revenue contribution", armored.stage2_candidate_signals)
        self.assertIn("copper/GOES cost pass-through", grid.stage3_high_conviction_signals)
        self.assertIn("firm backlog", localization.stage3_high_conviction_signals)
        self.assertIn("large capital raise after rerating", dilution.stage1_radar_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round257_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND257_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)

        summary = round257_summary()
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 5)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["watch_4b_case_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 7)
        self.assertEqual(summary["price_data_unavailable_count"], 2)
        self.assertEqual(summary["target_archetype_count"], 8)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_defense_export_and_missile_cases_are_stage2_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND257_CASE_CANDIDATES}
        hanwha = by_id["r1_loop12_hanwha_aerospace_romania_k9_dilution_watch"]
        lig = by_id["r1_loop12_lig_nex1_iraq_cheongung_missile_defense"]

        self.assertEqual(hanwha.primary_archetype, E2RArchetype.DEFENSE_EXPORT_BACKLOG_COMPOUNDING)
        self.assertEqual(hanwha.stage2_date.isoformat(), "2024-07-10")
        self.assertIsNone(hanwha.stage3_date)
        self.assertEqual(hanwha.stage4b_date.isoformat(), "2024-07-10")
        self.assertEqual(hanwha.extra_price_metrics["backlog_growth_pct"], 488.2)
        self.assertEqual(hanwha.mae_1d, -13.0)
        self.assertIn("dilution_after_rerating", hanwha.red_flag_fields)

        self.assertEqual(lig.primary_archetype, E2RArchetype.MISSILE_DEFENSE_COMBAT_VALIDATION)
        self.assertEqual(lig.stage2_date.isoformat(), "2024-09-20")
        self.assertEqual(lig.extra_price_metrics["relative_outperformance_pp"], 2.7)
        self.assertEqual(lig.extra_price_metrics["relative_cost_advantage_pct"], 70.3)
        self.assertEqual(lig.round_stage_failure_label, "stage2_order_not_green_until_delivery_margin_replenishment")

    def test_delivery_grid_epc_and_policy_capex_cases_are_separated(self) -> None:
        by_id = {case.case_id: case for case in ROUND257_CASE_CANDIDATES}
        rotem = by_id["r1_loop12_hyundai_rotem_k2_poland_delivery_to_revenue"]
        ls = by_id["r1_loop12_ls_electric_us_datacenter_transformer"]
        hyosung = by_id["r1_loop12_hyosung_hico_us_grid_equipment_localization"]
        epc = by_id["r1_loop12_samsung_ea_fadhili_epc_stage2"]
        steel = by_id["r1_loop12_hyundai_steel_us_policy_capex_false_positive"]

        self.assertEqual(rotem.primary_archetype, E2RArchetype.ARMORED_VEHICLE_DELIVERY_TO_REVENUE)
        self.assertEqual(rotem.stage2_price_anchor, 41300.0)
        self.assertEqual(rotem.extra_price_metrics["op_forecast_vs_consensus_pct"], 33.1)
        self.assertEqual(rotem.extra_price_metrics["k2_export_revenue_q1_krw_bn"], 270.0)

        self.assertEqual(ls.primary_archetype, E2RArchetype.GRID_TRANSFORMER_DATA_CENTER_BOTTLENECK)
        self.assertEqual(ls.price_validation_status, "price_data_unavailable_after_deep_search")
        self.assertEqual(ls.extra_price_metrics["contract_value_usd_mn"], 312.0)
        self.assertEqual(ls.extra_price_metrics["us_gsu_transformer_demand_growth_pct"], 274.0)

        self.assertEqual(hyosung.primary_archetype, E2RArchetype.US_GRID_EQUIPMENT_LOCALIZATION)
        self.assertEqual(hyosung.extra_price_metrics["gsu_lead_time_weeks"], 143.0)
        self.assertIn("capacity_expansion_without_order", hyosung.red_flag_fields)

        self.assertEqual(epc.primary_archetype, E2RArchetype.OVERSEAS_EPC_MEGA_ORDER)
        self.assertEqual(epc.case_type, "event_premium")
        self.assertEqual(epc.stage4b_date.isoformat(), "2024-04-03")
        self.assertEqual(epc.extra_price_metrics["contract_share_pct"], 77.9)

        self.assertEqual(steel.primary_archetype, E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE)
        self.assertEqual(steel.score_price_alignment, "false_positive_score")
        self.assertEqual(steel.stage4c_date.isoformat(), "2025-04-22")
        self.assertFalse(steel.hard_4c_confirmed)
        self.assertEqual(steel.extra_price_metrics["relative_underperformance_vs_kospi_pp"], -15.7)

    def test_dilution_case_is_4b_watch_not_hard_4c(self) -> None:
        by_id = {case.case_id: case for case in ROUND257_CASE_CANDIDATES}
        dilution = by_id["r1_loop12_hanwha_aerospace_capital_raise_dilution_4b"]

        self.assertEqual(dilution.primary_archetype, E2RArchetype.DILUTION_AFTER_RERATING_4B)
        self.assertEqual(dilution.case_type, "4b_watch")
        self.assertEqual(dilution.stage4b_date.isoformat(), "2025-03-27")
        self.assertIsNone(dilution.stage4c_date)
        self.assertFalse(dilution.hard_4c_confirmed)
        self.assertEqual(dilution.extra_price_metrics["initial_capital_raise_krw_trn"], 3.6)
        self.assertEqual(dilution.mae_1d, -13.0)

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND257_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND257_GREEN_FORBIDDEN_PATTERNS)
        review = render_round257_green_gate_review_markdown()
        stage_review = render_round257_stage4b_4c_review_markdown()
        fields = set(ROUND257_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND257_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round257_shadow_weight_rows()}
        deep_rows = round257_deep_sub_archetype_rows()

        self.assertIn("delivery_to_revenue_or_progress_revenue_confirmed", required)
        self.assertIn("working_capital_receivables_cash_collection_stable", required)
        self.assertIn("policy_capex_only", forbidden)
        self.assertIn("dilution_shock_present", forbidden)
        self.assertIn("large_capital_raise_after_rerating", ROUND257_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("policy_capex_failure", ROUND257_HARD_4C_GATES)
        self.assertIn("dilution_anchor", fields)
        self.assertIn("delivery_to_revenue", axes)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("4C-watch is not hard 4C", stage_review)
        self.assertEqual(len(ROUND257_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["DEFENSE_EXPORT_BACKLOG_COMPOUNDING"]["confirmed_order"], "+5")
        self.assertEqual(shadow_rows["OVERSEAS_EPC_MEGA_ORDER"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["POLICY_CAPEX_FALSE_POSITIVE"]["event_penalty"], "-5")
        self.assertTrue(any("Romania K9" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Hyosung HICO" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Louisiana plant" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round257_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_257.md")
        self.assertEqual(audit["round_id"], "round_185")
        self.assertEqual(audit["large_sector"], ROUND257_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round257_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round257_r1_loop12_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round257_case_rows()
            self.assertEqual(len(records), len(ROUND257_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND257_CASE_CANDIDATES))
            self.assertIn("Hanwha Aerospace", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("policy_capex_only", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("GRID_TRANSFORMER_DATA_CENTER_BOTTLENECK", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("Hyundai Steel", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["backlog_growth_pct"], 488.2)


if __name__ == "__main__":
    unittest.main()
