from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round285_r3_loop14_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round285_r3_loop14_secondary_battery_ev_green_energy_price_validation import (
    ROUND285_CASE_CANDIDATES,
    ROUND285_GREEN_FORBIDDEN_PATTERNS,
    ROUND285_GREEN_REQUIRED_FIELDS,
    ROUND285_HARD_4C_GATES,
    ROUND285_LARGE_SECTOR,
    ROUND285_PRICE_VALIDATION_FIELDS,
    ROUND285_REQUIRED_TARGET_ALIASES,
    ROUND285_SHADOW_WEIGHT_ROWS,
    ROUND285_STAGE4B_WATCH_TRIGGERS,
    render_round285_green_gate_review_markdown,
    render_round285_stage4b_4c_review_markdown,
    round285_audit_payload,
    round285_case_records,
    round285_case_rows,
    round285_deep_sub_archetype_rows,
    round285_shadow_weight_rows,
    round285_summary,
    write_round285_r3_loop14_reports,
)


class Round285R3Loop14SecondaryBatteryEVGreenEnergyTests(unittest.TestCase):
    def test_round285_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND285_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND285_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND285_REQUIRED_TARGET_ALIASES["EV_BATTERY_CONTRACT_CANCELLATION_HARD_4C"],
            E2RArchetype.EV_BATTERY_CONTRACT_CANCELLATION_HARD_4C.value,
        )
        self.assertEqual(
            ROUND285_REQUIRED_TARGET_ALIASES["SK_ON_RESTRUCTURING_ESS_PIVOT_STAGE2"],
            E2RArchetype.SK_ON_RESTRUCTURING_ESS_PIVOT_STAGE2.value,
        )
        self.assertEqual(
            ROUND285_REQUIRED_TARGET_ALIASES["BATTERY_DEMAND_POLICY_OVERHANG_CROSS_REFERENCE"],
            E2RArchetype.BATTERY_DEMAND_POLICY_OVERHANG_CROSS_REFERENCE.value,
        )

    def test_round285_archetype_definitions_capture_r3_loop14_gates(self) -> None:
        lges = archetype_definition(E2RArchetype.EV_BATTERY_CONTRACT_CANCELLATION_HARD_4C)
        jv = archetype_definition(E2RArchetype.BATTERY_JV_STAGE2_WITH_EV_DEMAND_WATCH)
        skon = archetype_definition(E2RArchetype.SK_ON_RESTRUCTURING_ESS_PIVOT_STAGE2)
        materials = archetype_definition(E2RArchetype.BATTERY_MATERIAL_SUPPLY_CHAIN_BETA_4C)
        solar = archetype_definition(E2RArchetype.SOLAR_US_MANUFACTURING_POLICY_STAGE2_CUSTOMS_4C)
        hydrogen = archetype_definition(E2RArchetype.HYDROGEN_FUEL_CELL_CAPEX_STAGE2)
        silicon = archetype_definition(E2RArchetype.SILICON_ANODE_SCALEUP_STAGE2)
        ess = archetype_definition(E2RArchetype.BATTERY_DEMAND_POLICY_OVERHANG_CROSS_REFERENCE)

        self.assertIn("major customer contract cancellation", lges.stage4c_thesis_break_signals)
        self.assertIn("JV capacity treated as revenue", jv.false_positive_patterns)
        self.assertIn("ESS GWh headline without contract value", skon.false_positive_patterns)
        self.assertIn("BEV-to-hybrid shift lowering battery content", materials.stage4c_thesis_break_signals)
        self.assertIn("customs detention", solar.stage4c_thesis_break_signals)
        self.assertIn("hydrogen capex without demand", hydrogen.false_positive_patterns)
        self.assertIn("unlisted material tech readthrough", silicon.false_positive_patterns)
        self.assertIn("ESS pivot without contract value", ess.false_positive_patterns)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round285_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND285_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("round285_hard_4c_confirmed_true", record.green_guardrails)
            self.assertIn("do_not_use_round285_cases_as_candidate_generation_input", record.green_guardrails)

        summary = round285_summary()
        self.assertEqual(summary["round_id"], "round_213")
        self.assertEqual(summary["large_sector"], "SECONDARY_BATTERY_EV_GREEN_ENERGY")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["structural_success_count"], 0)
        self.assertEqual(summary["success_candidate_count"], 6)
        self.assertEqual(summary["event_premium_count"], 0)
        self.assertEqual(summary["event_premium_or_result_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 0)
        self.assertEqual(summary["overheat_count"], 0)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["hard_4c_watch_case_count"], 4)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 2)
        self.assertEqual(summary["stage4c_watch_count"], 5)
        self.assertEqual(summary["price_moved_without_evidence_count"], 1)
        self.assertEqual(summary["false_positive_score_count"], 2)
        self.assertEqual(summary["unknown_alignment_count"], 5)
        self.assertEqual(summary["aligned_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["hard_4c_confirmed"])
        self.assertTrue(summary["hard_4c_watch_confirmed"])

    def test_round285_cases_keep_battery_ev_anchors_separate_from_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND285_CASE_CANDIDATES}
        lges = by_id["r3_loop14_lges_ford_freudenberg_contract_cancellation_hard_4c"]
        sdi = by_id["r3_loop14_samsung_sdi_gm_jv_stage2_ev_demand_watch"]
        skon = by_id["r3_loop14_sk_innovation_skon_restructuring_ess_pivot"]
        materials = by_id["r3_loop14_battery_material_supply_chain_ford_beta"]
        qcells = by_id["r3_loop14_hanwha_qcells_solar_policy_customs_gate"]
        hyundai = by_id["r3_loop14_hyundai_hydrogen_fuel_cell_capex_stage2"]
        group14 = by_id["r3_loop14_sk_group14_silicon_anode_stage2"]
        ess = by_id["r3_loop14_korean_battery_ess_pivot_cross_reference"]

        self.assertEqual(lges.primary_archetype, E2RArchetype.EV_BATTERY_CONTRACT_CANCELLATION_HARD_4C)
        self.assertTrue(lges.hard_4c_confirmed)
        self.assertEqual(lges.extra_price_metrics["combined_cancelled_expected_revenue_krw_trn"], 13.5)
        self.assertEqual(lges.extra_price_metrics["cancelled_revenue_as_share_of_2024_revenue_pct"], 52.7)
        self.assertEqual(lges.event_mae_pct, -7.6)
        self.assertEqual(lges.rerating_result, "thesis_break")

        self.assertEqual(sdi.primary_archetype, E2RArchetype.BATTERY_JV_STAGE2_WITH_EV_DEMAND_WATCH)
        self.assertEqual(sdi.extra_price_metrics["gm_jv_investment_usd_bn"], 3.5)
        self.assertEqual(sdi.extra_price_metrics["potential_expansion_capacity_gwh"], 36)
        self.assertEqual(sdi.extra_price_metrics["q4_2024_operating_loss_krw_bn"], 257)
        self.assertTrue(sdi.hard_4c_watch_confirmed)

        self.assertEqual(skon.primary_archetype, E2RArchetype.SK_ON_RESTRUCTURING_ESS_PIVOT_STAGE2)
        self.assertEqual(skon.extra_price_metrics["merged_company_assets_krw_trn"], 100)
        self.assertEqual(skon.extra_price_metrics["q3_loss_vs_q2_loss_increase_pct"], 88.0)
        self.assertFalse(skon.extra_price_metrics["ess_contract_value_disclosed"])

        self.assertEqual(materials.primary_archetype, E2RArchetype.BATTERY_MATERIAL_SUPPLY_CHAIN_BETA_4C)
        self.assertEqual(materials.extra_price_metrics["lg_energy_solution_event_mae_pct"], -6)
        self.assertIn("lower_battery_content", materials.extra_price_metrics["battery_content_risk"])
        self.assertEqual(materials.score_price_alignment, "false_positive_score")

        self.assertEqual(qcells.primary_archetype, E2RArchetype.SOLAR_US_MANUFACTURING_POLICY_STAGE2_CUSTOMS_4C)
        self.assertEqual(qcells.extra_price_metrics["doe_conditional_loan_guarantee_usd_bn"], 1.45)
        self.assertEqual(qcells.extra_price_metrics["furloughed_workers"], 1000)
        self.assertFalse(qcells.extra_price_metrics["full_production_resumption_confirmed"])

        self.assertEqual(hyundai.primary_archetype, E2RArchetype.HYDROGEN_FUEL_CELL_CAPEX_STAGE2)
        self.assertEqual(hyundai.extra_price_metrics["facility_investment_krw_bn"], 930)
        self.assertFalse(hyundai.extra_price_metrics["customer_demand_confirmed"])
        self.assertFalse(hyundai.extra_price_metrics["unit_economics_confirmed"])

        self.assertEqual(group14.primary_archetype, E2RArchetype.SILICON_ANODE_SCALEUP_STAGE2)
        self.assertEqual(group14.extra_price_metrics["series_d_funding_usd_mn"], 463)
        self.assertEqual(group14.extra_price_metrics["remaining_jv_stake_acquired_pct"], 75)
        self.assertFalse(group14.extra_price_metrics["listed_sk_value_bridge_confirmed"])

        self.assertEqual(ess.primary_archetype, E2RArchetype.BATTERY_DEMAND_POLICY_OVERHANG_CROSS_REFERENCE)
        self.assertEqual(ess.extra_price_metrics["flatiron_ess_supply_gwh"], 7.2)
        self.assertFalse(ess.extra_price_metrics["contract_value_disclosed"])
        self.assertEqual(ess.score_price_alignment, "price_moved_without_evidence")

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND285_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND285_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND285_PRICE_VALIDATION_FIELDS)
        shadow_rows = {row["archetype"]: row for row in round285_shadow_weight_rows()}
        deep_rows = round285_deep_sub_archetype_rows()
        green_markdown = render_round285_green_gate_review_markdown()
        stage_markdown = render_round285_stage4b_4c_review_markdown()

        self.assertIn("customer_calloff_visibility_confirmed", required)
        self.assertIn("ESS_PO_value_and_margin_confirmed", required)
        self.assertIn("supply_chain_customs_clearance_confirmed", required)
        self.assertIn("signed_contract_without_calloff", forbidden)
        self.assertIn("hydrogen_capex_without_demand", forbidden)
        self.assertIn("ESS_pivot_headline_before_disclosed_margin", ROUND285_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("major_customer_contract_cancellation", ROUND285_HARD_4C_GATES)
        self.assertIn("customs_supply_chain_anchor", fields)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("Hard 4C Gates", stage_markdown)
        self.assertEqual(len(ROUND285_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["EV_BATTERY_CONTRACT_CANCELLATION_HARD_4C"]["hard_4c_sensitivity"], "+5")
        self.assertEqual(shadow_rows["SOLAR_US_MANUFACTURING_POLICY_STAGE2_CUSTOMS_4C"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["BATTERY_DEMAND_POLICY_OVERHANG_CROSS_REFERENCE"]["ess_po_value_margin"], "+5")
        self.assertTrue(any("LG Energy Solution" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Qcells" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Group14" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round285_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_285.md")
        self.assertEqual(audit["round_id"], "round_213")
        self.assertEqual(audit["large_sector"], ROUND285_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertTrue(audit["summary"]["hard_4c_watch_confirmed"])
        self.assertIn("do_not_use_round285_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round285_r3_loop14_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round285_case_rows()
            self.assertEqual(len(records), len(ROUND285_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND285_CASE_CANDIDATES))
            self.assertIn("LGES Ford/Freudenberg cancellation", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("customer_calloff_visibility_confirmed", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("BATTERY_DEMAND_POLICY_OVERHANG_CROSS_REFERENCE", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("customs_supply_chain_anchor", paths["price_validation_plan"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["combined_cancelled_expected_revenue_krw_trn"], 13.5)


if __name__ == "__main__":
    unittest.main()
