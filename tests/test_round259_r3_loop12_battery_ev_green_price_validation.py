from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round259_r3_loop12_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round259_r3_loop12_battery_ev_green_price_validation import (
    ROUND259_CASE_CANDIDATES,
    ROUND259_GREEN_FORBIDDEN_PATTERNS,
    ROUND259_GREEN_REQUIRED_FIELDS,
    ROUND259_HARD_4C_GATES,
    ROUND259_LARGE_SECTOR,
    ROUND259_PRICE_VALIDATION_FIELDS,
    ROUND259_REQUIRED_TARGET_ALIASES,
    ROUND259_SCORE_ADJUSTMENTS,
    ROUND259_SHADOW_WEIGHT_ROWS,
    ROUND259_STAGE4B_WATCH_TRIGGERS,
    render_round259_green_gate_review_markdown,
    render_round259_stage4b_4c_review_markdown,
    round259_audit_payload,
    round259_case_records,
    round259_case_rows,
    round259_deep_sub_archetype_rows,
    round259_shadow_weight_rows,
    round259_summary,
    write_round259_r3_loop12_reports,
)


class Round259R3Loop12BatteryEvGreenPriceValidationTests(unittest.TestCase):
    def test_round259_targets_are_explicit_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND259_REQUIRED_TARGET_ALIASES), 10)
        self.assertTrue(set(ROUND259_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND259_REQUIRED_TARGET_ALIASES["US_BATTERY_LOCALIZATION_DILUTION"],
            E2RArchetype.US_BATTERY_LOCALIZATION_DILUTION.value,
        )
        self.assertEqual(
            ROUND259_REQUIRED_TARGET_ALIASES["SILICON_ANODE_OPTIONALITY"],
            E2RArchetype.SILICON_ANODE_OPTIONALITY.value,
        )
        self.assertEqual(
            ROUND259_REQUIRED_TARGET_ALIASES["HYDROGEN_FUELCELL_CAPEX_OPTIONALITY"],
            E2RArchetype.HYDROGEN_FUELCELL_CAPEX_OPTIONALITY.value,
        )
        self.assertEqual(
            ROUND259_REQUIRED_TARGET_ALIASES["US_FACTORY_EXECUTION_VISA_RISK"],
            E2RArchetype.US_FACTORY_EXECUTION_VISA_RISK.value,
        )

    def test_round259_archetype_definitions_are_available(self) -> None:
        dilution = archetype_definition(E2RArchetype.US_BATTERY_LOCALIZATION_DILUTION)
        jv = archetype_definition(E2RArchetype.EV_BATTERY_JV_RESTRUCTURING)
        silicon = archetype_definition(E2RArchetype.SILICON_ANODE_OPTIONALITY)
        hydrogen = archetype_definition(E2RArchetype.HYDROGEN_FUELCELL_CAPEX_OPTIONALITY)
        factory = archetype_definition(E2RArchetype.US_FACTORY_EXECUTION_VISA_RISK)

        self.assertIn("share-sale dilution", dilution.stage4c_thesis_break_signals)
        self.assertIn("JV dissolution", jv.stage4c_thesis_break_signals)
        self.assertIn("customer offtake", silicon.stage3_high_conviction_signals)
        self.assertIn("hydrogen unit economics", hydrogen.stage3_high_conviction_signals)
        self.assertIn("visa raid", factory.stage4c_thesis_break_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round259_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND259_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_treat_ev_jv_ess_hydrogen_solar_silicon_or_localization_as_green_alone", record.green_guardrails)

        summary = round259_summary()
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 4)
        self.assertEqual(summary["failed_rerating_count"], 3)
        self.assertEqual(summary["thesis_break_case_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["watch_4c_or_hard_count"], 6)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 5)
        self.assertEqual(summary["price_data_unavailable_count"], 5)
        self.assertEqual(summary["target_archetype_count"], 10)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["hard_4c_confirmed"])

    def test_samsung_sdi_and_lges_separate_watch_from_hard_4c(self) -> None:
        by_id = {case.case_id: case for case in ROUND259_CASE_CANDIDATES}
        sdi = by_id["r3_loop12_samsung_sdi_starplus_share_sale_4c_watch"]
        lges = by_id["r3_loop12_lges_contract_quality_ultium_utilization_break"]

        self.assertEqual(sdi.primary_archetype, E2RArchetype.US_BATTERY_LOCALIZATION_DILUTION)
        self.assertEqual(sdi.stage2_date.isoformat(), "2025-04-09")
        self.assertEqual(sdi.stage4c_date.isoformat(), "2026-02-10")
        self.assertFalse(sdi.hard_4c_confirmed)
        self.assertEqual(sdi.extra_price_metrics["offering_price_cut_pct"], -13.59)
        self.assertEqual(sdi.extra_price_metrics["samsung_sdi_ytd_drawdown_context_pct"], -29.5)
        self.assertIn("stellantis_starplus_exit_report_not_final", sdi.red_flag_fields)

        self.assertEqual(lges.primary_archetype, E2RArchetype.EV_BATTERY_CONTRACT_QUALITY_BREAK)
        self.assertEqual(lges.case_type, "4c_thesis_break")
        self.assertTrue(lges.hard_4c_confirmed)
        self.assertEqual(lges.stage4c_date.isoformat(), "2025-12-17")
        self.assertEqual(lges.extra_price_metrics["total_lost_expected_revenue_krw_trn"], 13.5)
        self.assertEqual(lges.extra_price_metrics["lost_revenue_vs_2024_revenue_pct"], 52.7)
        self.assertEqual(lges.mae_1d, -7.6)
        self.assertEqual(lges.rerating_result, "thesis_break")

    def test_jv_supply_chain_and_optional_cases_are_stage2_or_watch(self) -> None:
        by_id = {case.case_id: case for case in ROUND259_CASE_CANDIDATES}
        skon = by_id["r3_loop12_skon_ford_jv_split_ess_pivot"]
        basket = by_id["r3_loop12_battery_supply_chain_ford_demand_shock"]
        group14 = by_id["r3_loop12_sk_group14_silicon_anode_optional"]

        self.assertEqual(skon.primary_archetype, E2RArchetype.EV_BATTERY_JV_RESTRUCTURING)
        self.assertEqual(skon.stage2_date.isoformat(), "2025-09-03")
        self.assertEqual(skon.stage4c_date.isoformat(), "2025-12-11")
        self.assertEqual(skon.extra_price_metrics["original_ford_sk_jv_investment_usd_bn"], 11.4)
        self.assertEqual(skon.extra_price_metrics["flatiron_ess_contract_volume_gwh"], 7.2)
        self.assertEqual(skon.extra_price_metrics["loss_worsening_pct"], 88.0)

        self.assertEqual(basket.primary_archetype, E2RArchetype.BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK)
        self.assertEqual(basket.stage4c_date.isoformat(), "2025-12-16")
        self.assertEqual(basket.extra_price_metrics["posco_future_m_event_mae_pct"], -8.2)
        self.assertEqual(basket.extra_price_metrics["sk_ie_technology_event_mae_pct"], -5.0)
        self.assertEqual(basket.stage_failure_type, "should_have_been_red")

        self.assertEqual(group14.primary_archetype, E2RArchetype.SILICON_ANODE_OPTIONALITY)
        self.assertEqual(group14.stage2_date.isoformat(), "2025-08-20")
        self.assertEqual(group14.extra_price_metrics["series_d_funding_usd_mn"], 463.0)
        self.assertEqual(group14.extra_price_metrics["jv_stake_acquired_by_group14_pct"], 75.0)
        self.assertIn("offtake_unconfirmed", group14.red_flag_fields)

    def test_solar_hydrogen_and_factory_execution_are_guarded(self) -> None:
        by_id = {case.case_id: case for case in ROUND259_CASE_CANDIDATES}
        qcells = by_id["r3_loop12_hanwha_qcells_solar_uflpa_4c_watch"]
        hydrogen = by_id["r3_loop12_hyundai_hydrogen_fuelcell_capex"]
        georgia = by_id["r3_loop12_hyundai_lg_georgia_factory_visa_execution_watch"]

        self.assertEqual(qcells.primary_archetype, E2RArchetype.SOLAR_US_SUPPLY_CHAIN_LOCALIZATION)
        self.assertEqual(qcells.stage2_date.isoformat(), "2024-08-08")
        self.assertEqual(qcells.stage4c_date.isoformat(), "2025-11-08")
        self.assertEqual(qcells.extra_price_metrics["doe_conditional_loan_guarantee_usd_bn"], 1.45)
        self.assertEqual(qcells.extra_price_metrics["furloughed_or_reduced_hours_workers"], 1000)

        self.assertEqual(hydrogen.primary_archetype, E2RArchetype.HYDROGEN_FUELCELL_CAPEX_OPTIONALITY)
        self.assertEqual(hydrogen.stage2_date.isoformat(), "2025-10-30")
        self.assertEqual(hydrogen.extra_price_metrics["investment_krw_bn"], 930.0)
        self.assertEqual(hydrogen.extra_price_metrics["facility_area_sqm"], 43000)
        self.assertIn("hydrogen_capex_without_offtake", hydrogen.red_flag_fields)

        self.assertEqual(georgia.primary_archetype, E2RArchetype.US_FACTORY_EXECUTION_VISA_RISK)
        self.assertIsNone(georgia.stage4c_date)
        self.assertEqual(georgia.extra_price_metrics["stage4c_month"], "2025-09")
        self.assertEqual(georgia.extra_price_metrics["detained_workers_reuters_context"], 475)
        self.assertEqual(georgia.extra_price_metrics["startup_delay_months"], "2-3")
        self.assertIn("visa_raid", georgia.red_flag_fields)

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND259_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND259_GREEN_FORBIDDEN_PATTERNS)
        review = render_round259_green_gate_review_markdown()
        stage_review = render_round259_stage4b_4c_review_markdown()
        fields = set(ROUND259_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND259_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round259_shadow_weight_rows()}
        deep_rows = round259_deep_sub_archetype_rows()

        self.assertIn("actual_calloff_or_take_or_pay_confirmed", required)
        self.assertIn("customs_visa_labor_supply_chain_flow_risk_passed", required)
        self.assertIn("us_localization_capex_only", forbidden)
        self.assertIn("contract_cancellation_present", forbidden)
        self.assertIn("ess_pivot_news_rally_before_contract_value", ROUND259_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("contract_cancellation", ROUND259_HARD_4C_GATES)
        self.assertIn("customs_visa_factory_execution_anchor", fields)
        self.assertIn("actual_calloff", axes)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("LGES Ford/Freudenberg as hard 4C", stage_review)
        self.assertEqual(len(ROUND259_SHADOW_WEIGHT_ROWS), 9)
        self.assertEqual(shadow_rows["EV_BATTERY_CONTRACT_QUALITY_BREAK"]["hard_4c_sensitivity"], "+5")
        self.assertEqual(shadow_rows["US_BATTERY_LOCALIZATION_DILUTION"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["US_FACTORY_EXECUTION_VISA_RISK"]["factory_execution"], "+5")
        self.assertTrue(any("Group14" in row["terms"] for row in deep_rows))
        self.assertTrue(any("UFLPA" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Hyundai-LG Georgia" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round259_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_259.md")
        self.assertEqual(audit["round_id"], "round_187")
        self.assertEqual(audit["large_sector"], ROUND259_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round259_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round259_r3_loop12_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round259_case_rows()
            self.assertEqual(len(records), len(ROUND259_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND259_CASE_CANDIDATES))
            self.assertIn("LG Energy Solution", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("contract_cancellation_present", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("US_FACTORY_EXECUTION_VISA_RISK", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("Hyundai-LG Georgia", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[1]["extra_price_metrics"])["total_lost_expected_revenue_krw_trn"], 13.5)


if __name__ == "__main__":
    unittest.main()
