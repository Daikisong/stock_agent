from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round292_r10_loop14_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round292_r10_loop14_construction_real_estate_building_materials_price_validation import (
    ROUND292_CASE_CANDIDATES,
    ROUND292_GREEN_FORBIDDEN_PATTERNS,
    ROUND292_GREEN_REQUIRED_FIELDS,
    ROUND292_HARD_4C_GATES,
    ROUND292_LARGE_SECTOR,
    ROUND292_PRICE_VALIDATION_FIELDS,
    ROUND292_REQUIRED_TARGET_ALIASES,
    ROUND292_SHADOW_WEIGHT_ROWS,
    ROUND292_STAGE4B_WATCH_TRIGGERS,
    render_round292_green_gate_review_markdown,
    render_round292_stage4b_4c_review_markdown,
    round292_audit_payload,
    round292_case_records,
    round292_case_rows,
    round292_deep_sub_archetype_rows,
    round292_shadow_weight_rows,
    round292_summary,
    write_round292_r10_loop14_reports,
)


class Round292R10Loop14ConstructionRealEstateBuildingMaterialsTests(unittest.TestCase):
    def test_round292_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND292_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND292_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND292_REQUIRED_TARGET_ALIASES["PF_LIQUIDITY_HARD_4C_WATCH"],
            E2RArchetype.PF_LIQUIDITY_HARD_4C_WATCH.value,
        )
        self.assertEqual(
            ROUND292_REQUIRED_TARGET_ALIASES["CONSTRUCTION_SAFETY_HARD_4C"],
            E2RArchetype.CONSTRUCTION_SAFETY_HARD_4C.value,
        )
        self.assertEqual(
            ROUND292_REQUIRED_TARGET_ALIASES["US_LOCALIZATION_CAPEX_FALSE_POSITIVE"],
            E2RArchetype.US_LOCALIZATION_CAPEX_FALSE_POSITIVE.value,
        )

    def test_round292_archetype_definitions_capture_loop14_gates(self) -> None:
        pf = archetype_definition(E2RArchetype.PF_LIQUIDITY_HARD_4C_WATCH)
        policy = archetype_definition(E2RArchetype.REAL_ESTATE_POLICY_STAGE2_NOT_GREEN)
        safety = archetype_definition(E2RArchetype.CONSTRUCTION_SAFETY_HARD_4C)
        epc = archetype_definition(E2RArchetype.OVERSEAS_EPC_ORDER_4B_WATCH)
        nuclear = archetype_definition(E2RArchetype.NUCLEAR_CONSTRUCTION_EXPORT_STAGE2)
        weak = archetype_definition(E2RArchetype.BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING)
        tariff = archetype_definition(E2RArchetype.BUILDING_MATERIAL_TARIFF_RELIEF_EVENT_PREMIUM)
        capex = archetype_definition(E2RArchetype.US_LOCALIZATION_CAPEX_FALSE_POSITIVE)

        self.assertIn("PF delinquency spike", pf.stage4c_thesis_break_signals)
        self.assertIn("building permits", policy.stage3_high_conviction_signals)
        self.assertIn("fatal construction safety event", safety.stage4c_thesis_break_signals)
        self.assertIn("advance payment", epc.stage3_high_conviction_signals)
        self.assertIn("final contract signing", nuclear.stage3_high_conviction_signals)
        self.assertIn("net-profit estimate cut", weak.stage4c_thesis_break_signals)
        self.assertIn("tariff relief without ASP/margin", tariff.false_positive_patterns)
        self.assertIn("funding clarity", capex.stage3_high_conviction_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round292_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND292_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round292_cases_as_candidate_generation_input", record.green_guardrails)

        summary = round292_summary()
        self.assertEqual(summary["round_id"], "round_220")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 2)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["event_premium_count"], 4)
        self.assertEqual(summary["hard_4c_case_count"], 2)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 4)
        self.assertEqual(summary["stage4c_watch_count"], 5)
        self.assertEqual(summary["price_moved_without_evidence_count"], 4)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 1)
        self.assertEqual(summary["false_positive_score_count"], 3)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["hard_4c_confirmed"])

    def test_construction_policy_safety_epc_and_material_cases_are_separated(self) -> None:
        by_id = {case.case_id: case for case in ROUND292_CASE_CANDIDATES}
        pf = by_id["r10_loop14_taeyoung_pf_liquidity_hard_watch"]
        policy = by_id["r10_loop14_seoul_property_policy_stage2_not_green"]
        safety = by_id["r10_loop14_hdc_gwangju_construction_safety_hard_4c"]
        epc = by_id["r10_loop14_samsung_ena_fadhili_epc_order_4b"]
        nuclear = by_id["r10_loop14_czech_nuclear_construction_export_stage2"]
        weak = by_id["r10_loop14_hyundai_steel_rebar_weak_construction_demand"]
        tariff = by_id["r10_loop14_hyundai_posco_steel_plate_antidumping_event"]
        capex = by_id["r10_loop14_hyundai_steel_us_plant_capex_false_positive"]

        self.assertEqual(pf.extra_price_metrics["government_support_package_krw_trn"], 40.6)
        self.assertEqual(pf.extra_price_metrics["pf_delinquency_end_2023_pct"], 2.70)
        self.assertTrue(pf.hard_4c_confirmed)

        self.assertIn("Gangnam", policy.extra_price_metrics["permit_zone_districts"])
        self.assertEqual(policy.extra_price_metrics["ltv_after_pct"], 40)
        self.assertIn("property_supply_policy_only", policy.red_flag_fields)

        self.assertEqual(safety.extra_price_metrics["fatalities"], 6)
        self.assertTrue(safety.extra_price_metrics["chairman_resignation"])
        self.assertEqual(safety.rerating_result, "thesis_break")

        self.assertEqual(epc.extra_price_metrics["contract_value_usd_bn"], 6.0)
        self.assertEqual(epc.extra_price_metrics["event_price_krw"], 26750)
        self.assertEqual(epc.event_mfe_pct, 8.5)

        self.assertEqual(nuclear.extra_price_metrics["doosan_enerbility_3m_gain_pct"], 48)
        self.assertFalse(nuclear.extra_price_metrics["final_contract_signed"])
        self.assertEqual(nuclear.extra_price_metrics["court_blocked_contract_value_usd_bn_min"], 18)

        self.assertEqual(weak.extra_price_metrics["net_profit_estimate_cut_pct"], -73)
        self.assertEqual(weak.event_mae_pct, -1.2)
        self.assertEqual(weak.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(tariff.extra_price_metrics["hyundai_steel_event_mfe_pct"], 5.8)
        self.assertEqual(tariff.extra_price_metrics["chinese_share_of_korean_steel_imports_pct"], 49)
        self.assertEqual(tariff.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(capex.extra_price_metrics["us_plant_investment_usd_bn"], 6)
        self.assertEqual(capex.event_mae_pct, -21.0)
        self.assertEqual(capex.score_price_alignment, "false_positive_score")

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND292_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND292_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND292_PRICE_VALIDATION_FIELDS)
        shadow_rows = {row["archetype"]: row for row in round292_shadow_weight_rows()}
        deep_rows = round292_deep_sub_archetype_rows()
        green_markdown = render_round292_green_gate_review_markdown()
        stage_markdown = render_round292_stage4b_4c_review_markdown()

        self.assertIn("PF_repayment_visibility_confirmed", required)
        self.assertIn("capex_IRR_funding_clarity_confirmed", required)
        self.assertIn("order_value_headline_only", forbidden)
        self.assertIn("capex_localization_without_IRR", forbidden)
        self.assertIn("nuclear_preferred_bidder_plus_30_to_50pct", ROUND292_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("fatal_construction_safety_event", ROUND292_HARD_4C_GATES)
        self.assertIn("capex_funding_anchor", fields)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("HDC Hyundai Development", stage_markdown)
        self.assertIn("hard 4C", stage_markdown)
        self.assertEqual(len(ROUND292_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["OVERSEAS_EPC_ORDER_4B_WATCH"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["CONSTRUCTION_SAFETY_HARD_4C"]["hard_4c_sensitivity"], "+5")
        self.assertTrue(any("Taeyoung E&C" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Hyundai Steel" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round292_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_292.md")
        self.assertEqual(audit["round_id"], "round_220")
        self.assertEqual(audit["large_sector"], ROUND292_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertIn("do_not_use_round292_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round292_r10_loop14_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round292_case_rows()
            self.assertEqual(len(records), len(ROUND292_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND292_CASE_CANDIDATES))
            self.assertIn("Samsung E&A", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("PF_repayment_visibility_confirmed", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("PF_LIQUIDITY_HARD_4C_WATCH", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("capex_funding_anchor", paths["price_validation_plan"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[3]["extra_price_metrics"])["event_price_krw"], 26750)


if __name__ == "__main__":
    unittest.main()
