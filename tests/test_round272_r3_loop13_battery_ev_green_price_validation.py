from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round272_r3_loop13_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round272_r3_loop13_battery_ev_green_price_validation import (
    ROUND272_CASE_CANDIDATES,
    ROUND272_GREEN_FORBIDDEN_PATTERNS,
    ROUND272_GREEN_REQUIRED_FIELDS,
    ROUND272_HARD_4C_GATES,
    ROUND272_LARGE_SECTOR,
    ROUND272_PRICE_VALIDATION_FIELDS,
    ROUND272_REQUIRED_TARGET_ALIASES,
    ROUND272_SCORE_ADJUSTMENTS,
    ROUND272_SHADOW_WEIGHT_ROWS,
    ROUND272_STAGE4B_WATCH_TRIGGERS,
    render_round272_green_gate_review_markdown,
    render_round272_stage4b_4c_review_markdown,
    round272_audit_payload,
    round272_case_records,
    round272_case_rows,
    round272_deep_sub_archetype_rows,
    round272_shadow_weight_rows,
    round272_summary,
    write_round272_r3_loop13_reports,
)


class Round272R3Loop13BatteryEVGreenPriceValidationTests(unittest.TestCase):
    def test_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND272_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND272_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND272_REQUIRED_TARGET_ALIASES["EV_BATTERY_MATERIAL_CONTRACT_COLLAPSE"],
            E2RArchetype.EV_BATTERY_MATERIAL_CONTRACT_COLLAPSE.value,
        )
        self.assertEqual(
            ROUND272_REQUIRED_TARGET_ALIASES["ESS_LFP_CONTRACT_STAGE2_NOT_GREEN"],
            E2RArchetype.ESS_LFP_CONTRACT_STAGE2_NOT_GREEN.value,
        )
        self.assertEqual(
            ROUND272_REQUIRED_TARGET_ALIASES["FEOC_GRAPHITE_POLICY_RELIEF_NOT_GREEN"],
            E2RArchetype.FEOC_GRAPHITE_POLICY_RELIEF_NOT_GREEN.value,
        )

    def test_archetype_definitions_encode_r3_loop13_gates(self) -> None:
        lnf = archetype_definition(E2RArchetype.EV_BATTERY_MATERIAL_CONTRACT_COLLAPSE)
        ess = archetype_definition(E2RArchetype.ESS_LFP_CONTRACT_STAGE2_NOT_GREEN)
        ira = archetype_definition(E2RArchetype.IRA_SUBSIDY_DEPENDENCE_QUALITY_GATE)
        parent = archetype_definition(E2RArchetype.BATTERY_PARENT_CAPITAL_RECYCLING)
        report = archetype_definition(E2RArchetype.ESS_REPORT_UNCONFIRMED_EVENT_PREMIUM)
        precursor = archetype_definition(E2RArchetype.PRECURSOR_IPO_OVERHEAT_DEMAND_BREAK)
        safety = archetype_definition(E2RArchetype.BATTERY_SAFETY_HARD_REFERENCE)
        feoc = archetype_definition(E2RArchetype.FEOC_GRAPHITE_POLICY_RELIEF_NOT_GREEN)

        self.assertIn("actual call-off, material volume, delivery start, utilization, margin, FCF, and counterparty program health confirmed", lnf.stage3_high_conviction_signals)
        self.assertIn("actual GWh volume, shipment, utilization, ESS margin, ex-subsidy OP, and FCF confirmed", ess.stage3_high_conviction_signals)
        self.assertIn("reported OP treated as structural despite tax-credit dependency", ira.false_positive_patterns)
        self.assertIn("debt reduction, ROIC improvement, shareholder return, battery-material margin, and FCF bridge confirmed", parent.stage3_high_conviction_signals)
        self.assertIn("press report treated as signed contract", report.false_positive_patterns)
        self.assertIn("IPO demand treated as customer demand", precursor.false_positive_patterns)
        self.assertIn("fatal battery fire", safety.stage4c_thesis_break_signals)
        self.assertIn("company-level non-China supply contract, customer certification, margin, utilization, and FCF confirmed", feoc.stage3_high_conviction_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round272_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND272_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_invent_price_or_stage_dates", record.green_guardrails)

        summary = round272_summary()
        self.assertEqual(summary["round_id"], "round_200")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 3)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["hard_4c_reference_count"], 2)
        self.assertEqual(summary["hard_4c_case_count"], 2)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 6)
        self.assertEqual(summary["stage4c_watch_count"], 4)
        self.assertEqual(summary["price_data_unavailable_count"], 1)
        self.assertEqual(summary["price_moved_without_evidence_count"], 2)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 3)
        self.assertEqual(summary["aligned_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["hard_4c_confirmed"])

    def test_lnf_lges_and_ira_quality_cases_are_separated(self) -> None:
        by_id = {case.case_id: case for case in ROUND272_CASE_CANDIDATES}
        lnf = by_id["r3_loop13_lnf_tesla_4680_contract_collapse"]
        lges_ess = by_id["r3_loop13_lges_tesla_lfp_ess_stage2"]
        lges_ira = by_id["r3_loop13_lges_ira_subsidy_op_quality_gate"]

        self.assertEqual(lnf.primary_archetype, E2RArchetype.EV_BATTERY_MATERIAL_CONTRACT_COLLAPSE)
        self.assertTrue(lnf.hard_4c_confirmed)
        self.assertEqual(lnf.stage4c_date.isoformat(), "2025-12-29")
        self.assertEqual(lnf.extra_price_metrics["initial_contract_projection_usd_bn"], 2.9)
        self.assertEqual(lnf.extra_price_metrics["revised_contract_value_usd"], 7386.0)
        self.assertEqual(lnf.extra_price_metrics["contract_value_collapse_pct"], -99.9997)

        self.assertEqual(lges_ess.primary_archetype, E2RArchetype.ESS_LFP_CONTRACT_STAGE2_NOT_GREEN)
        self.assertEqual(lges_ess.extra_price_metrics["contract_value_usd_bn"], 4.3)
        self.assertEqual(lges_ess.extra_price_metrics["extension_option_years"], 7.0)
        self.assertEqual(lges_ess.event_mfe_pct, 0.6)
        self.assertIn("actual_gwh_volume_not_disclosed", lges_ess.red_flag_fields)

        self.assertEqual(lges_ira.primary_archetype, E2RArchetype.IRA_SUBSIDY_DEPENDENCE_QUALITY_GATE)
        self.assertEqual(lges_ira.extra_price_metrics["q2_2025_op_krw_bn"], 492.0)
        self.assertEqual(lges_ira.extra_price_metrics["ex_ira_tax_credit_op_krw_bn"], 1.4)
        self.assertEqual(lges_ira.extra_price_metrics["ex_ira_share_of_reported_op_pct"], 0.28)
        self.assertEqual(lges_ira.event_mae_pct, -2.3)

    def test_event_premium_precursor_safety_and_policy_do_not_force_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND272_CASE_CANDIDATES}
        samsung = by_id["r3_loop13_samsung_sdi_tesla_ess_unconfirmed_report"]
        ecopro = by_id["r3_loop13_ecopro_materials_precursor_demand_break"]
        aricell = by_id["r3_loop13_aricell_sconnect_battery_safety_hard_reference"]
        feoc = by_id["r3_loop13_feoc_graphite_policy_relief"]

        self.assertEqual(samsung.primary_archetype, E2RArchetype.ESS_REPORT_UNCONFIRMED_EVENT_PREMIUM)
        self.assertFalse(samsung.extra_price_metrics["actual_signed_contract"])
        self.assertEqual(samsung.score_price_alignment, "price_moved_without_evidence")
        self.assertIn("reported_deal_without_confirmation", samsung.red_flag_fields)

        self.assertEqual(ecopro.primary_archetype, E2RArchetype.PRECURSOR_IPO_OVERHEAT_DEMAND_BREAK)
        self.assertEqual(ecopro.stage4c_price_anchor, 119200.0)
        self.assertEqual(ecopro.extra_price_metrics["event_mae_pct"], -11.0)
        self.assertEqual(ecopro.score_price_alignment, "false_positive_score")

        self.assertEqual(aricell.primary_archetype, E2RArchetype.BATTERY_SAFETY_HARD_REFERENCE)
        self.assertTrue(aricell.hard_4c_confirmed)
        self.assertEqual(aricell.extra_price_metrics["fatalities"], 23.0)
        self.assertEqual(aricell.extra_price_metrics["ceo_sentence_years"], 15.0)
        self.assertEqual(aricell.event_mae_pct, -23.0)

        self.assertEqual(feoc.primary_archetype, E2RArchetype.FEOC_GRAPHITE_POLICY_RELIEF_NOT_GREEN)
        self.assertEqual(feoc.extra_price_metrics["korea_support_package_krw_trn"], 9.7)
        self.assertFalse(feoc.extra_price_metrics["company_level_contracts_confirmed"])
        self.assertIn("policy_support_without_contracts", feoc.red_flag_fields)

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND272_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND272_GREEN_FORBIDDEN_PATTERNS)
        review = render_round272_green_gate_review_markdown()
        stage_review = render_round272_stage4b_4c_review_markdown()
        fields = set(ROUND272_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND272_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round272_shadow_weight_rows()}
        deep_rows = round272_deep_sub_archetype_rows()

        self.assertIn("signed_contract_and_actual_calloff", required)
        self.assertIn("ex_subsidy_op_quality_confirmed", required)
        self.assertIn("battery_safety_quality_risk_clear", required)
        self.assertIn("contract_value_without_calloff", forbidden)
        self.assertIn("ira_subsidy_driven_op_only", forbidden)
        self.assertIn("policy_support_only", forbidden)
        self.assertIn("actual_calloff", axes)
        self.assertIn("counterparty_4680_or_EV_program_risk", axes)
        self.assertIn("contract_value_collapse_pct", fields)
        self.assertIn("reported_contract_before_company_confirmation", ROUND272_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("battery_fire_or_fatal_safety_incident", ROUND272_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("hard 4C", stage_review)
        self.assertEqual(len(ROUND272_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["EV_BATTERY_MATERIAL_CONTRACT_COLLAPSE"]["hard_4c_sensitivity"], "+5")
        self.assertEqual(shadow_rows["ESS_REPORT_UNCONFIRMED_EVENT_PREMIUM"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["FEOC_GRAPHITE_POLICY_RELIEF_NOT_GREEN"]["non_china_sourcing_certification"], "+5")
        self.assertTrue(any("L&F" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Aricell" in row["terms"] for row in deep_rows))
        self.assertTrue(any("FEOC" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round272_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_272.md")
        self.assertEqual(audit["round_id"], "round_200")
        self.assertEqual(audit["large_sector"], ROUND272_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertEqual(len(audit["shadow_weights"]), 8)
        self.assertEqual(len(audit["deep_sub_archetypes"]), 8)
        self.assertIn("do_not_use_round272_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round272_r3_loop13_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round272_case_rows()
            self.assertEqual(len(records), len(ROUND272_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND272_CASE_CANDIDATES))
            self.assertIn("L&F", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("LG Energy Solution", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Aricell", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("actual_calloff", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("BATTERY_SAFETY_HARD_REFERENCE", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("EcoPro Materials", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["contract_value_collapse_pct"], -99.9997)


if __name__ == "__main__":
    unittest.main()
