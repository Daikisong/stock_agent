from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round233_r3_loop10_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round233_r3_loop10_battery_ev_green_price_validation import (
    ROUND233_CASE_CANDIDATES,
    ROUND233_GREEN_FORBIDDEN_PATTERNS,
    ROUND233_GREEN_REQUIRED_FIELDS,
    ROUND233_HARD_4C_GATES,
    ROUND233_LARGE_SECTOR,
    ROUND233_PRICE_VALIDATION_FIELDS,
    ROUND233_REQUIRED_TARGET_ALIASES,
    ROUND233_SCORE_ADJUSTMENTS,
    ROUND233_SHADOW_WEIGHT_ROWS,
    ROUND233_STAGE4B_WATCH_TRIGGERS,
    render_round233_green_gate_review_markdown,
    render_round233_stage4b_4c_review_markdown,
    round233_audit_payload,
    round233_case_records,
    round233_case_rows,
    round233_deep_sub_archetype_rows,
    round233_shadow_weight_rows,
    round233_summary,
    write_round233_r3_loop10_reports,
)


class Round233R3Loop10BatteryEvGreenPriceValidationTests(unittest.TestCase):
    def test_round233_targets_map_to_existing_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND233_REQUIRED_TARGET_ALIASES), 13)
        self.assertTrue(set(ROUND233_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND233_REQUIRED_TARGET_ALIASES["EV_BATTERY_FACTORY_UTILIZATION_4C"],
            E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT.value,
        )
        self.assertEqual(
            ROUND233_REQUIRED_TARGET_ALIASES["CATHODE_SUPPLY_CHAIN_DERISKING"],
            E2RArchetype.CATHODE_LONG_CONTRACT_VISIBILITY.value,
        )
        self.assertEqual(
            ROUND233_REQUIRED_TARGET_ALIASES["LITHIUM_CYCLE_EVENT_PREMIUM"],
            E2RArchetype.EVENT_LITHIUM_PRICE_RALLY.value,
        )

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round233_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND233_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_treat_battery_ess_green_capex_lithium_or_jv_headline_as_green_alone", record.green_guardrails)

        summary = round233_summary()
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 6)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["watch_4c_count"], 3)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["target_archetype_count"], 13)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])

    def test_lges_ess_pivot_is_stage2_with_4c_watch_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND233_CASE_CANDIDATES}
        lges = by_id["r3_loop10_lges_ess_pivot_ev_utilization_watch"]

        self.assertEqual(lges.primary_archetype, E2RArchetype.ESS_LFP_GRID_STORAGE)
        self.assertEqual(lges.stage2_date.isoformat(), "2026-02-04")
        self.assertIsNone(lges.stage3_date)
        self.assertEqual(lges.stage4c_date.isoformat(), "2026-05-12")
        self.assertEqual(lges.extra_price_metrics["hanwha_qcells_ess_contract_gwh"], 5.0)
        self.assertEqual(lges.extra_price_metrics["nextstar_stake_acquired_pct"], 49.0)
        self.assertEqual(lges.extra_price_metrics["ohio_ultium_layoffs_since_january"], 850.0)
        self.assertEqual(lges.round_alignment_label, "success_candidate_4C_watch")
        self.assertIn("ess_margin_unconfirmed", lges.red_flag_fields)

    def test_samsung_sdi_jv_has_event_anchor_but_demand_risk_blocks_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND233_CASE_CANDIDATES}
        samsung = by_id["r3_loop10_samsung_sdi_gm_indiana_ev_jv"]

        self.assertEqual(samsung.primary_archetype, E2RArchetype.EV_BATTERY_JV_RESTRUCTURING)
        self.assertEqual(samsung.mfe_1d, 3.2)
        self.assertEqual(samsung.extra_price_metrics["forecast_cut_pct"], -16.7)
        self.assertEqual(samsung.extra_price_metrics["capacity_expansion_potential_pct"], 33.3)
        self.assertIsNone(samsung.stage3_date)
        self.assertEqual(samsung.score_price_alignment, "aligned")

    def test_watch_and_event_cases_are_contained(self) -> None:
        by_id = {case.case_id: case for case in ROUND233_CASE_CANDIDATES}
        qcells = by_id["r3_loop10_hanwha_qcells_uflpa_supply_chain_watch"]
        ford = by_id["r3_loop10_ev_supply_chain_ford_shock_skiet_ecopro"]
        lithium = by_id["r3_loop10_posco_future_m_lnf_lithium_event"]

        self.assertEqual(qcells.stage4c_date.isoformat(), "2025-11-01")
        self.assertEqual(qcells.extra_price_metrics["furlough_or_reduced_pay_hours_workers"], 1000.0)
        self.assertEqual(qcells.extra_price_metrics["contract_workers_laid_off"], 300.0)

        self.assertFalse(ford.hard_4c_confirmed)
        self.assertEqual(ford.mae_1d, -6.0)
        self.assertEqual(ford.stage_failure_type, "should_have_been_red")

        self.assertEqual(lithium.score_price_alignment, "price_moved_without_evidence")
        self.assertEqual(lithium.rerating_result, "event_premium")
        self.assertEqual(lithium.mfe_1d, 10.0)
        self.assertEqual(lithium.extra_price_metrics["lithium_price_decline_from_2022_peak_pct"], -90.0)

    def test_green_gate_and_stage4_rules_are_explicit(self) -> None:
        required = set(ROUND233_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND233_GREEN_FORBIDDEN_PATTERNS)
        review = render_round233_green_gate_review_markdown()
        stage_review = render_round233_stage4b_4c_review_markdown()

        self.assertIn("actual_calloff", required)
        self.assertIn("fcf_after_capex", required)
        self.assertIn("lithium_price_event_only", forbidden)
        self.assertIn("ev_demand_slowdown_ignored", forbidden)
        self.assertIn("lithium_price_event_materials_basket_rally", ROUND233_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("customer_ev_model_cancellation", ROUND233_HARD_4C_GATES)
        self.assertIn("ev_demand_shock", {item.axis for item in ROUND233_SCORE_ADJUSTMENTS})
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("5GWh ESS contract", review)
        self.assertIn("EV demand shock", stage_review)

    def test_price_fields_score_axes_shadow_and_deep_rows_cover_round233(self) -> None:
        fields = set(ROUND233_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND233_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round233_shadow_weight_rows()}
        deep_rows = round233_deep_sub_archetype_rows()

        self.assertIn("gwh_or_capacity_anchor", fields)
        self.assertIn("utilization_or_layoff_anchor", fields)
        self.assertIn("actual_calloff", axes)
        self.assertIn("ev_demand_shock", axes)
        self.assertEqual(len(ROUND233_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["ESS_LFP_GRID_STORAGE"]["gwh_volume"], "+5")
        self.assertEqual(shadow_rows["EVENT_LITHIUM_PRICE_RALLY"]["event_penalty"], "-5")
        self.assertTrue(any("LG Energy Solution" in row["terms"] for row in deep_rows))
        self.assertTrue(any("CATL Yichun" in row["terms"] for row in deep_rows))

    def test_summary_and_audit_payload_keep_non_production_guardrails(self) -> None:
        audit = round233_audit_payload()

        self.assertEqual(audit["source_round"], "docs/round/round_233.md")
        self.assertEqual(audit["large_sector"], ROUND233_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertEqual(len(audit["shadow_weights"]), 8)
        self.assertEqual(len(audit["deep_sub_archetypes"]), 8)
        self.assertIn("do_not_use_round233_cases_as_candidate_generation_input", audit["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round233_r3_loop10_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round233_case_rows()
            self.assertEqual(len(records), len(ROUND233_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND233_CASE_CANDIDATES))
            self.assertIn("LGES and SK On ESS pivots", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("actual_calloff", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("ESS_LFP_GRID_STORAGE", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("CATL Yichun", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["hanwha_qcells_ess_contract_gwh"], 5.0)


if __name__ == "__main__":
    unittest.main()
