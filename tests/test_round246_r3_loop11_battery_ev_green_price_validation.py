from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round246_r3_loop11_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round246_r3_loop11_battery_ev_green_price_validation import (
    ROUND246_CASE_CANDIDATES,
    ROUND246_GREEN_FORBIDDEN_PATTERNS,
    ROUND246_GREEN_REQUIRED_FIELDS,
    ROUND246_HARD_4C_GATES,
    ROUND246_LARGE_SECTOR,
    ROUND246_PRICE_VALIDATION_FIELDS,
    ROUND246_REQUIRED_TARGET_ALIASES,
    ROUND246_SCORE_ADJUSTMENTS,
    ROUND246_SHADOW_WEIGHT_ROWS,
    ROUND246_STAGE4B_WATCH_TRIGGERS,
    render_round246_green_gate_review_markdown,
    render_round246_stage4b_4c_review_markdown,
    round246_audit_payload,
    round246_case_records,
    round246_case_rows,
    round246_deep_sub_archetype_rows,
    round246_shadow_weight_rows,
    round246_summary,
    write_round246_r3_loop11_reports,
)


class Round246R3Loop11BatteryEvGreenPriceValidationTests(unittest.TestCase):
    def test_round246_targets_are_explicit_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND246_REQUIRED_TARGET_ALIASES), 10)
        self.assertTrue(set(ROUND246_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND246_REQUIRED_TARGET_ALIASES["US_BATTERY_LOCALIZATION"],
            E2RArchetype.US_BATTERY_LOCALIZATION.value,
        )
        self.assertEqual(
            ROUND246_REQUIRED_TARGET_ALIASES["EV_BATTERY_CONTRACT_QUALITY_BREAK"],
            E2RArchetype.EV_BATTERY_CONTRACT_QUALITY_BREAK.value,
        )
        self.assertEqual(
            ROUND246_REQUIRED_TARGET_ALIASES["EV_FACTORY_EXECUTION_LABOR_IMMIGRATION_RISK"],
            E2RArchetype.EV_FACTORY_EXECUTION_LABOR_IMMIGRATION_RISK.value,
        )

    def test_round246_archetype_definitions_are_available(self) -> None:
        ess = archetype_definition(E2RArchetype.ESS_LFP_GRID_STORAGE)
        localization = archetype_definition(E2RArchetype.US_BATTERY_LOCALIZATION)
        quality_break = archetype_definition(E2RArchetype.EV_BATTERY_CONTRACT_QUALITY_BREAK)
        lithium = archetype_definition(E2RArchetype.LITHIUM_RESOURCE_SECURITY)
        solar = archetype_definition(E2RArchetype.SOLAR_CUSTOMS_UFLPA_4C_WATCH)
        labor = archetype_definition(E2RArchetype.EV_FACTORY_EXECUTION_LABOR_IMMIGRATION_RISK)

        self.assertIn("actual delivery or revenue recognition", ess.stage3_high_conviction_signals)
        self.assertIn("customs/labor risk cleared", localization.stage3_high_conviction_signals)
        self.assertIn("contract cancellation", quality_break.stage4c_thesis_break_signals)
        self.assertIn("downstream margin", lithium.stage3_high_conviction_signals)
        self.assertIn("production furlough", solar.stage4c_thesis_break_signals)
        self.assertIn("immigration raid", labor.stage4c_thesis_break_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round246_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND246_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_treat_ess_lfp_lithium_solar_localization_or_factory_construction_as_green_alone", record.green_guardrails)

        summary = round246_summary()
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 5)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 5)
        self.assertEqual(summary["watch_4c_count"], 4)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 4)
        self.assertEqual(summary["target_archetype_count"], 10)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["hard_4c_confirmed"])

    def test_ess_contract_cases_are_stage2_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND246_CASE_CANDIDATES}
        samsung = by_id["r3_loop11_samsung_sdi_lfp_ess_us_contract"]
        lges = by_id["r3_loop11_lges_tesla_lfp_ess_contract"]
        skon = by_id["r3_loop11_skon_flatiron_lfp_ess"]

        self.assertEqual(samsung.primary_archetype, E2RArchetype.ESS_LFP_GRID_STORAGE)
        self.assertEqual(samsung.stage2_date.isoformat(), "2025-12-09")
        self.assertEqual(samsung.stage4b_date.isoformat(), "2025-12-09")
        self.assertEqual(samsung.mfe_1d, 6.1)
        self.assertEqual(samsung.extra_price_metrics["relative_outperformance_pp"], 6.2)
        self.assertIsNone(samsung.stage3_date)

        self.assertEqual(lges.stage2_date.isoformat(), "2025-07-30")
        self.assertEqual(lges.extra_price_metrics["contract_value_usd_bn"], 4.3)
        self.assertEqual(lges.extra_price_metrics["official_customer_disclosure"], "not_disclosed_by_LGES")
        self.assertIn("unofficial_customer_source_only", lges.red_flag_fields)

        self.assertEqual(skon.stage2_date.isoformat(), "2025-09-03")
        self.assertEqual(skon.extra_price_metrics["contract_volume_gwh"], 7.2)
        self.assertEqual(skon.extra_price_metrics["contract_value"], "not_disclosed")

    def test_hard_4c_and_4c_watch_cases_are_separated(self) -> None:
        by_id = {case.case_id: case for case in ROUND246_CASE_CANDIDATES}
        cancel = by_id["r3_loop11_lges_ford_freudenberg_contract_hard_4c"]
        ford = by_id["r3_loop11_ford_ev_retreat_supply_chain_shock"]
        georgia = by_id["r3_loop11_hyundai_lg_georgia_battery_raid_execution_watch"]

        self.assertTrue(cancel.hard_4c_confirmed)
        self.assertEqual(cancel.stage4c_date.isoformat(), "2025-12-17")
        self.assertEqual(cancel.extra_price_metrics["total_lost_expected_revenue_krw_trn"], 13.5)
        self.assertEqual(cancel.extra_price_metrics["lost_revenue_vs_2024_revenue_pct"], 52.7)
        self.assertEqual(cancel.mae_1d, -7.6)
        self.assertEqual(cancel.rerating_result, "thesis_break")

        self.assertFalse(ford.hard_4c_confirmed)
        self.assertEqual(ford.stage4c_date.isoformat(), "2025-12-16")
        self.assertEqual(ford.extra_price_metrics["posco_future_m_event_mae_pct"], -8.2)
        self.assertEqual(ford.stage_failure_type, "should_have_been_red")

        self.assertIsNone(georgia.stage4c_date)
        self.assertEqual(georgia.extra_price_metrics["stage4c_month"], "2025-09")
        self.assertEqual(georgia.extra_price_metrics["ap_update_koreans"], 316)
        self.assertIn("immigration_skilled_worker_execution_failure", georgia.red_flag_fields)

    def test_lithium_and_solar_cases_keep_stage2_and_watch_status(self) -> None:
        by_id = {case.case_id: case for case in ROUND246_CASE_CANDIDATES}
        posco = by_id["r3_loop11_posco_minres_lithium_resource_security"]
        qcells = by_id["r3_loop11_hanwha_qcells_customs_supply_chain_4c_watch"]

        self.assertEqual(posco.primary_archetype, E2RArchetype.LITHIUM_RESOURCE_SECURITY)
        self.assertEqual(posco.stage2_date.isoformat(), "2025-11-11")
        self.assertEqual(posco.extra_price_metrics["spodumene_drawdown_peak_to_low_pct"], -89.8)
        self.assertEqual(posco.rerating_result, "unknown")

        self.assertEqual(qcells.primary_archetype, E2RArchetype.SOLAR_US_SUPPLY_CHAIN_LOCALIZATION)
        self.assertEqual(qcells.stage2_date.isoformat(), "2024-08-08")
        self.assertEqual(qcells.stage4c_date.isoformat(), "2025-11-08")
        self.assertEqual(qcells.extra_price_metrics["furloughed_or_reduced_hours_workers"], 1000)
        self.assertEqual(qcells.score_price_alignment, "evidence_good_but_price_failed")

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND246_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND246_GREEN_FORBIDDEN_PATTERNS)
        review = render_round246_green_gate_review_markdown()
        stage_review = render_round246_stage4b_4c_review_markdown()
        fields = set(ROUND246_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND246_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round246_shadow_weight_rows()}
        deep_rows = round246_deep_sub_archetype_rows()

        self.assertIn("binding_contract", required)
        self.assertIn("actual_delivery_or_revenue_recognition_started", required)
        self.assertIn("unofficial_customer_source_only", forbidden)
        self.assertIn("contract_value_without_utilization", forbidden)
        self.assertIn("unofficial_customer_name_rally", ROUND246_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("contract_cancellation", ROUND246_HARD_4C_GATES)
        self.assertIn("gwh_or_capacity_anchor", fields)
        self.assertIn("contract_cancellation", axes)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("hard 4C catches contract cancellation", stage_review)
        self.assertEqual(len(ROUND246_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["ESS_LFP_GRID_STORAGE"]["binding_contract"], "+5")
        self.assertEqual(shadow_rows["EV_BATTERY_CONTRACT_QUALITY_BREAK"]["hard_4c_sensitivity"], "+5")
        self.assertEqual(shadow_rows["BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK"]["execution_redteam"], "+5")
        self.assertTrue(any("Samsung SDI America" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Ford EV retreat" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round246_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_246.md")
        self.assertEqual(audit["round_id"], "round_174")
        self.assertEqual(audit["large_sector"], ROUND246_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round246_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round246_r3_loop11_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round246_case_rows()
            self.assertEqual(len(records), len(ROUND246_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND246_CASE_CANDIDATES))
            self.assertIn("Samsung SDI", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("unofficial_customer_source_only", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("EV_BATTERY_CONTRACT_QUALITY_BREAK", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("Hyundai-LG Georgia", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["contract_value_usd_bn"], 1.36)


if __name__ == "__main__":
    unittest.main()
